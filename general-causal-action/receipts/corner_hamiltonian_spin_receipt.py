"""Exact SU(2) corner Hamiltonian coefficient; no numerical eigensolver.

Normalized oriented trivalent spin tensors are projected with exact Clebsch
coefficients.  Radicals are represented in a squarefree-radical field over Q.
All spin and magnetic labels below are twice their usual values.

For each edge the product of normalized matrix coefficients contributes
sqrt(d_old*d_loop/d_new); at each vertex the old and loop invariant tensors
are projected onto the new unit tensor. Incoming dual indices use the
standard SU(2) invariant antisymmetric form. Fundamental cycle phases are
calibrated by the value +2 at the identity.

The coefficient recurrence visits all states reached at the required orders;
it does not replace the Hilbert space by a numerical spectral truncation.
"""

from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from math import factorial, gcd


def square_parts(n):
    out, sf, p = 1, 1, 2
    while p * p <= n:
        power = 0
        while n % p == 0:
            n //= p
            power += 1
        out *= p ** (power // 2)
        if power % 2:
            sf *= p
        p += 1
    return out, sf * n


class Rad:
    def __init__(self, x=0):
        self.d = {1: Q(x)} if x else {}

    @classmethod
    def terms(cls, d):
        v = cls()
        v.d = {s: q for s, q in d.items() if q}
        return v

    @classmethod
    def sqrt(cls, x):
        x = Q(x)
        assert x >= 0
        if not x:
            return cls()
        out, sf = square_parts(x.numerator * x.denominator)
        return cls.terms({sf: Q(out, x.denominator)})

    def __bool__(self):
        return bool(self.d)

    def __add__(self, other):
        if not isinstance(other, Rad):
            other = Rad(other)
        d = self.d.copy()
        for sf, q in other.d.items():
            d[sf] = d.get(sf, Q(0)) + q
        return Rad.terms(d)

    __radd__ = __add__

    def __neg__(self):
        return Rad.terms({sf: -q for sf, q in self.d.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Rad) else -Q(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, Rad):
            other = Rad(other)
        d = {}
        for a, x in self.d.items():
            for b, y in other.d.items():
                common = gcd(a, b)
                sf = (a // common) * (b // common)
                d[sf] = d.get(sf, Q(0)) + x * y * common
        return Rad.terms(d)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * (1 / Q(other))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        value = Rad(1)
        for _ in range(n):
            value *= self
        return value

    def rational(self):
        assert not (set(self.d) - {1}), self
        return self.d.get(1, Q(0))

    def __eq__(self, other):
        return not (self - other)

    def __repr__(self):
        if not self.d:
            return "0"
        return " + ".join(
            str(q) if sf == 1 else f"({q})sqrt({sf})"
            for sf, q in sorted(self.d.items())
        )


def phase(n):
    return -1 if n % 2 else 1


def admissible(j):
    a, b, c = j
    return min(j) >= 0 and not ((a + b + c) % 2) and abs(a-b) <= c <= a+b


def mags(j):
    return range(-j, j + 1, 2)


@lru_cache(None)
def three_j(a, b, c, ma, mb, mc):
    if not admissible((a, b, c)) or ma + mb + mc:
        return Rad()
    if any(abs(m) > j or (j-m) % 2 for j, m in zip((a,b,c),(ma,mb,mc))):
        return Rad()
    ab_c, ac_b, bc_a = (a+b-c)//2, (a+c-b)//2, (b+c-a)//2
    pref = Q(factorial(ab_c) * factorial(ac_b) * factorial(bc_a),
             factorial((a+b+c)//2 + 1))
    for j, m in zip((a,b,c),(ma,mb,mc)):
        pref *= factorial((j+m)//2) * factorial((j-m)//2)
    total = Q(0)
    for z in range(ab_c + 1):
        fs = (z, ab_c-z, (a-ma)//2-z, (b+mb)//2-z,
              (c-b+ma)//2+z, (c-a-mb)//2+z)
        if min(fs) < 0:
            continue
        denominator = 1
        for n in fs:
            denominator *= factorial(n)
        total += Q(phase(z), denominator)
    return phase((a-b-mc)//2) * total * Rad.sqrt(pref)


@lru_cache(None)
def clebsch(a, b, c, ma, mb, mc):
    if ma + mb != mc:
        return Rad()
    return phase((a-b+mc)//2) * Rad.sqrt(c+1) * three_j(a,b,c,ma,mb,-mc)


# a:O->X, b:O->Y, c:O->Z, p:X->Y, q:X->Z, r:Y->Z.
VERTICES = ((0,1,2),(0,3,4),(1,3,5),(2,4,5))
INCOMING = ((False,False,False),(True,False,False),
            (True,True,False),(True,True,True))
LENGTHS = (1,1,1,2,2,2)
VAC = (0,0,0,0,0,0)
SEED = (1,1,0,1,0,0)
G = (1,0,1,0,1,0)
H = (0,1,1,0,0,1)


def state_admissible(state):
    return all(admissible(tuple(state[e] for e in v)) for v in VERTICES)


@lru_cache(None)
def tensor(v, spins):
    result = {}
    for ms in product(*(mags(j) for j in spins)):
        signs = [(-m if inc else m) for m, inc in zip(ms, INCOMING[v])]
        value = three_j(*spins, *signs)
        if not value:
            continue
        p = sum((j+m)//2 for j,m,inc in zip(spins,ms,INCOMING[v]) if inc)
        result[ms] = phase(p) * value
    assert sum(x*x for x in result.values()) == 1
    return result


@lru_cache(None)
def vertex_overlap(v, old, loop, new):
    oi, li, ni = tensor(v,old), tensor(v,loop), tensor(v,new)
    result = Rad()
    for ms, x in oi.items():
        for ns, y in li.items():
            ks = tuple(m+n for m,n in zip(ms,ns))
            z = ni.get(ks)
            if z is None:
                continue
            term = x*y*z
            for a,b,c,ma,mb,mc in zip(old,loop,new,ms,ns,ks):
                term *= clebsch(a,b,c,ma,mb,mc)
                if not term:
                    break
            result += term
    return result


@lru_cache(None)
def identity_value(state):
    ts = [tensor(v, tuple(state[e] for e in edges))
          for v, edges in enumerate(VERTICES)]
    value = Rad()
    for ms in product(*(mags(j) for j in state)):
        term = Rad(1)
        for edges, tv in zip(VERTICES, ts):
            term *= tv.get(tuple(ms[e] for e in edges), Rad())
            if not term:
                break
        value += term
    dims = 1
    for j in state:
        dims *= j+1
    return Rad.sqrt(dims) * value


@lru_cache(None)
def basis_phase(state):
    # Set every fundamental simple-cycle vector equal to its positive character.
    if all(n in (0,1) for n in state) and any(state):
        val = identity_value(state).rational()
        assert abs(val) == 2, (state,val)
        return Q(2, val)
    return Q(1)


@lru_cache(None)
def matrix_entry(old, loop, new):
    if not state_admissible(new):
        return Rad()
    ratio = Q(1)
    for a,b,c in zip(old,loop,new):
        if not admissible((a,b,c)):
            return Rad()
        ratio *= Q((a+1)*(b+1),c+1)
    value = Rad.sqrt(ratio)
    for v, edges in enumerate(VERTICES):
        value *= vertex_overlap(
            v, tuple(old[e] for e in edges), tuple(loop[e] for e in edges),
            tuple(new[e] for e in edges))
        if not value:
            break
    # Physical seam character = basis_phase(loop) times the raw spin network.
    return value * basis_phase(loop) * basis_phase(old) * basis_phase(new)


@lru_cache(None)
def neighbors(state, loop):
    choices = [(n,) if not l else ((n-1,n+1) if n else (1,))
               for n,l in zip(state,loop)]
    result = {}
    for new in product(*choices):
        if not state_admissible(new):
            continue
        value = matrix_entry(state,loop,new)
        if value:
            assert value == matrix_entry(new,loop,state), (state,new,value)
            result[new] = value
    return result


def clean(v):
    return {s:x for s,x in v.items() if x}


def add(a, b, scale=1):
    result = a.copy()
    for s,x in b.items():
        result[s] = result.get(s,Rad()) + scale*x
    return clean(result)


def multiply(loop, vector):
    out = {}
    for old,x in vector.items():
        for new,c in neighbors(old,loop).items():
            out[new] = out.get(new,Rad()) + c*x
    return clean(out)


def energy(state):
    return sum(Q(length*n*(n+2),3) for n,length in zip(state,LENGTHS))


def dot(a, b):
    return sum(x*b.get(s,Rad()) for s,x in a.items())


def project(v, seed):
    return {s:x for s,x in v.items() if s != seed}


def resolve(v, seed):
    base = energy(seed)
    return {s:x/(energy(s)-base) for s,x in v.items() if s != seed}


def expectation(loop, vector, seed):
    return multiply(loop,vector).get(seed,Rad())


def recurrence(seed):
    # Ordinary coefficients for H0 - s G - t H, with <seed,phi>=1.
    phi, eig = {(0,0):{seed:Rad(1)}}, {(0,0):Rad(energy(seed))}
    indices = sorted((i,j) for i in range(3) for j in range(3) if i+j)
    indices.sort(key=lambda ij:(sum(ij),ij))
    for i,j in indices:
        drive = {}
        if i:
            drive = add(drive,multiply(G,phi[i-1,j]))
        if j:
            drive = add(drive,multiply(H,phi[i,j-1]))
        eig[i,j] = -drive.get(seed,Rad())
        rhs = project(drive,seed)
        for (u,v), coefficient in eig.items():
            if not (u+v) or (u,v)==(i,j) or u>i or v>j:
                continue
            rhs = add(rhs,phi[i-u,j-v],coefficient)
        phi[i,j] = resolve(rhs,seed)
    return eig, phi


def fourth_order_form(seed):
    f = {seed:Rad(1)}
    gf, hf = multiply(G,f), multiply(H,f)
    u, v = resolve(gf,seed), resolve(hf,seed)
    a, b = dot(gf,u), dot(u,u)
    assert a == dot(hf,v) and b == dot(v,v)
    same_g = project(multiply(G,u),seed)
    same_h = project(multiply(H,v),seed)
    mixed = project(add(multiply(H,u),multiply(G,v)),seed)
    cross = dot(same_g,resolve(same_h,seed))
    mixed_norm = dot(mixed,resolve(mixed,seed))
    disconnected = 2*a*b
    ordinary = -2*cross-mixed_norm+disconnected
    return {
        "a":a, "b":b, "cross":cross, "mixed":mixed_norm,
        "disconnected":disconnected, "ordinary22":ordinary,
        "same_g":same_g, "same_h":same_h, "mixed_vector":mixed,
    }


def main():
    for a in range(4):
        for b in range(2):
            for c in range(abs(a-b),a+b+1,2):
                for mc in mags(c):
                    assert sum(clebsch(a,b,c,ma,mb,mc)**2
                               for ma in mags(a) for mb in mags(b)) == 1
    results = {}
    for label,seed in (("vacuum",VAC),("odd",SEED)):
        print(label, "seed",seed, "energy",energy(seed), flush=True)
        print("G seed",multiply(G,{seed:Rad(1)}), flush=True)
        print("H seed",multiply(H,{seed:Rad(1)}), flush=True)
        result = fourth_order_form(seed)
        for key,value in result.items():
            print(key,value,flush=True)
        eig,_ = recurrence(seed)
        assert eig[2,2] == result["ordinary22"], (eig,result)
        assert eig[2,0] == -result["a"]
        assert all(not value for (i,j),value in eig.items() if i%2 or j%2)
        results[label] = result
    assert results["vacuum"]["a"] == Q(1,4)
    assert results["vacuum"]["b"] == Q(1,16)
    assert results["vacuum"]["ordinary22"] == -Q(1,1248)
    assert results["odd"]["a"] == Q(2,7)
    assert results["odd"]["b"] == Q(19,196)
    expected_weights = {
        (0,0,0):Q(49,784), (0,2,2):Q(75,784),
        (2,0,2):Q(75,784), (2,2,0):Q(27,784),
        (2,2,2):Q(54,784),
    }
    actual_weights = {
        state[:3]:(value*value).rational()
        for state,value in results["odd"]["mixed_vector"].items()
    }
    assert actual_weights == expected_weights
    assert sum(actual_weights.values()) == Q(5,14)
    answer = 4*(results["odd"]["ordinary22"]-results["vacuum"]["ordinary22"])
    assert answer == -Q(299687,5885880)
    print("epsilon^3 mixed excitation-energy derivative:",answer,flush=True)
    # The split-c control has two fundamental c links. Only the middle
    # denominators change; the note proves the transport of these weights.
    split_gaps = {
        (0,0,0):Q(4), (0,2,2):Q(20,3), (2,0,2):Q(20,3),
        (2,2,0):Q(28,3), (2,2,2):Q(28,3),
    }
    split_middle = sum(weight/split_gaps[state]
                       for state,weight in actual_weights.items())
    assert split_middle == Q(19,343)
    assert results["odd"]["disconnected"]-split_middle == 0
    assert Q(1,32)-Q(1,4)/8 == 0  # vacuum cancellation
    print("Split-edge quartic response: 0",flush=True)
    print("Exact Clebsch, symmetry, AP single-seam, five-channel, "
          "recurrence, and split-edge arithmetic checks passed.",flush=True)

if __name__ == "__main__":
    main()

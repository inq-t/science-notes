"""Exact FJ row-form expectations, using Gaussian Wick contractions.

No random samples, floating-point integration, or spectral truncation.
Coordinates are original comb-face Lie algebra vectors.  The scalar state
is PP's normalized soft two-quantum excitation.  Rotation invariance lets
one evaluate the T_1 row and multiply its expectation by three.
"""

from fractions import Fraction as Q
from functools import lru_cache


class F:
    """Q(sqrt(2),sqrt(3)), in basis 1,sqrt(2),sqrt(3),sqrt(6)."""
    def __init__(self, x=0):
        self.a = x.a if isinstance(x, F) else (Q(x), Q(0), Q(0), Q(0))

    @classmethod
    def coeffs(cls, a):
        v = cls()
        v.a = tuple(a)
        return v

    def __bool__(self):
        return any(self.a)

    def __add__(self, other):
        other = F(other)
        return F.coeffs(a+b for a,b in zip(self.a, other.a))

    __radd__ = __add__

    def __neg__(self):
        return F.coeffs(-a for a in self.a)

    def __sub__(self, other):
        return self + (-F(other))

    def __rsub__(self, other):
        return F(other) + (-self)

    def __mul__(self, other):
        other = F(other)
        out = [Q(0)] * 4
        for i,a in enumerate(self.a):
            if not a:
                continue
            for j,b in enumerate(other.a):
                if b:
                    common = i & j
                    factor = (2 if common & 1 else 1)*(3 if common & 2 else 1)
                    out[i ^ j] += a*b*factor
        return F.coeffs(out)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * (1/Q(other))

    def __eq__(self, other):
        return self.a == F(other).a

    def __repr__(self):
        names = ("", "*sqrt(2)", "*sqrt(3)", "*sqrt(6)")
        return " + ".join(str(x)+names[i] for i,x in enumerate(self.a) if x) or "0"


SQ2 = F.coeffs((Q(0),Q(1),Q(0),Q(0)))
SQ3 = F.coeffs((Q(0),Q(0),Q(1),Q(0)))
SQ6 = SQ2*SQ3


def clean(p):
    return {e:c for e,c in p.items() if c}


def add(p, q, factor=1):
    out = p.copy()
    factor = F(factor)
    for e,c in q.items():
        out[e] = out.get(e,F()) + factor*c
    return clean(out)


def scale(p, c):
    return clean({e:F(c)*v for e,v in p.items()})


def mul(p, q):
    out = {}
    for e,a in p.items():
        for f,b in q.items():
            ef = tuple(x+y for x,y in zip(e,f))
            out[ef] = out.get(ef,F()) + a*b
    return clean(out)


def deriv(p, i):
    out = {}
    for e,c in p.items():
        if e[i]:
            ne = list(e)
            ne[i] -= 1
            out[tuple(ne)] = c*e[i]
    return out


def p_sum(ps):
    out = {}
    for p in ps:
        out = add(out,p)
    return out


class Experiment:
    def __init__(self, L):
        assert L in (1,2)
        self.L, self.N, self.dim = L,L*L,3*L*L
        self.zero = (0,)*self.dim
        self.one = {self.zero:F(1)}
        self.x = []
        for i in range(self.dim):
            e = [0]*self.dim
            e[i] = 1
            self.x.append({tuple(e):F(1)})
        if L == 1:
            self.C, self.S = [[F(2)]], [[F(Q(1,4))]]
            self.v = [Q(1)]
            self.soft_frequency = F(2)
        else:
            had = ((1,1,1,1),(1,-1,1,-1),
                   (1,1,-1,-1),(1,-1,-1,1))
            rates = (SQ2,F(2),F(2),SQ6)
            precisions = (SQ2/4,F(Q(1,4)),F(Q(1,4)),SQ6/12)
            self.C = [[sum(rates[k]*Q(had[k][i]*had[k][j],4)
                           for k in range(4)) for j in range(4)] for i in range(4)]
            self.S = [[sum(precisions[k]*Q(had[k][i]*had[k][j],4)
                           for k in range(4)) for j in range(4)] for i in range(4)]
            self.v = [Q(1,2)]*4
            self.soft_frequency = SQ2
        self.grad_log = [
            p_sum(scale(self.x[3*q+c], self.S[p][q]) for q in range(self.N))
            for p in range(self.N) for c in range(3)
        ]
        self.rows = self.make_rows()
        for p in range(self.N):
            for q in range(self.N):
                assert sum(self.C[p][r]*self.S[r][q] for r in range(self.N)) == Q(p==q,2)
                incidence = sum(row["s"].get(p,0)*row["s"].get(q,0) for row in self.rows)
                distance = abs(p%L-q%L)+abs(p//L-q//L)
                assert incidence == (4 if p==q else -1 if distance==1 else 0)

    def face(self, i, j):
        return (j-1)*self.L+i-1

    def vector(self, p):
        return self.x[3*p:3*p+3]

    def vector_sum(self, ps):
        return [p_sum(self.x[3*p+c] for p in ps) for c in range(3)]

    def ad(self, x):
        # x cross e_1
        return [{},x[2],scale(x[1],-1)]

    def adprod(self, x, y):
        # x cross (y cross e_1) = y*x_1 - e_1*(x dot y)
        return [
            scale(add(mul(x[1],y[1]),mul(x[2],y[2])),-1),
            mul(x[0],y[1]), mul(x[0],y[2]),
        ]

    def make_rows(self):
        rows=[]
        def fresh(name):
            return {"name":name,"D0":[],"D1":[],"D2":[],"s":{}}
        def append(row, order, p, vec, factor=1):
            for c,pol in enumerate(vec):
                if pol:
                    row[order].append((3*p+c,scale(pol,factor)))
        def piece(row,p,side,sign=1,prefix=()):
            x=self.vector(p)
            row["s"][p]=row["s"].get(p,0)+sign
            row["D0"].append((3*p,scale(self.one,sign)))
            if side=="R":
                append(row,"D1",p,self.ad(x),Q(sign,2))
                append(row,"D2",p,self.adprod(x,x),Q(sign,12))
            else:
                append(row,"D1",p,self.ad(x),Q(-sign,2))
                append(row,"D2",p,self.adprod(x,x),Q(sign,12))
                if prefix:
                    # Only one factor can occur for the L=2 control.
                    assert len(prefix)==1
                    s=self.vector(prefix[0])
                    append(row,"D1",p,self.ad(s),-sign)
                    append(row,"D2",p,self.adprod(s,s),Q(sign,2))
                    append(row,"D2",p,self.adprod(x,s),Q(sign,2))
        def conjugate(row,p):
            append(row,"D1",p,self.ad(self.vector(p)),-1)
        for i in range(1,self.L+1):
            for j in range(1,self.L+1):
                row=fresh(("horizontal",i,j))
                piece(row,self.face(i,j),"R",-1)
                if j<self.L:
                    piece(row,self.face(i,j+1),"L")
                rows.append(row)
            row=fresh(("bottom",i))
            piece(row,self.face(i,1),"L")
            for a in range(i+1,self.L+1):
                for k in range(1,self.L+1):
                    conjugate(row,self.face(a,k))
            rows.append(row)
        for c in range(self.L+1):
            for j in range(1,self.L+1):
                row=fresh(("vertical",c,j))
                if c>=1:
                    piece(row,self.face(c,j),"L",
                          prefix=tuple(self.face(c,k) for k in range(1,j)))
                if c<self.L:
                    piece(row,self.face(c+1,j),"R",-1)
                    for k in range(j+1,self.L+1):
                        conjugate(row,self.face(c+1,k))
                rows.append(row)
        assert len(rows)==2*self.L*(self.L+1)
        return rows

    @lru_cache(None)
    def moment_color(self,e):
        if sum(e)%2:
            return F()
        if not any(e):
            return F(1)
        i=next(i for i,n in enumerate(e) if n)
        rem=list(e)
        rem[i]-=1
        out=F()
        for j,n in enumerate(rem):
            if n:
                rem[j]-=1
                out+=n*self.C[i][j]*self.moment_color(tuple(rem))
                rem[j]+=1
        return out

    @lru_cache(None)
    def moment(self,e):
        out=F(1)
        for c in range(3):
            ec=tuple(e[3*p+c] for p in range(self.N))
            if sum(ec)%2:
                return F()
            out*=self.moment_color(ec)
        return out

    def inner(self,p,q):
        def grouped(poly):
            groups={}
            for e,c in poly.items():
                parity=tuple(sum(e[3*f+a] for f in range(self.N))%2 for a in range(3))
                groups.setdefault(parity,[]).append((e,c))
            return groups
        gp,gq=grouped(p),grouped(q)
        out=F()
        for parity,terms in gp.items():
            for e,a in terms:
                for f,b in gq.get(parity,()):
                    value=self.moment(tuple(x+y for x,y in zip(e,f)))
                    if value:
                        out+=a*b*value
        return out

    def source(self):
        ys=[p_sum(scale(self.x[3*p+c],self.v[p]) for p in range(self.N))
            for c in range(3)]
        quadratic=p_sum(mul(y,y) for y in ys)
        invsqrtfreq=F(Q(1,2)) if self.L==1 else SQ2/2
        return add(scale(quadratic,invsqrtfreq*SQ6/6),self.one,-SQ6/2)

    def evaluate(self,f):
        assert self.inner(f,f)==1
        gradients=[add(deriv(f,i),mul(self.grad_log[i],f),-1) for i in range(self.dim)]
        def apply(row,order):
            return p_sum(mul(pol,gradients[i]) for i,pol in row[order])
        d1norm,cross,haar=F(),F(),F()
        perrow=[]
        for row in self.rows:
            d0,d1,d2=(apply(row,o) for o in ("D0","D1","D2"))
            measure=p_sum(scale(self.x[3*p],Q(s,12)) for p,s in row["s"].items())
            norm=3*self.inner(d1,d1)
            crossrow=6*self.inner(d0,d2)
            haarrow=6*self.inner(d0,mul(measure,f))
            d1norm+=norm
            cross+=crossrow
            haar+=haarrow
            perrow.append((row["name"],norm,crossrow,haarrow))
        r4=p_sum(mul(p_sum(mul(v,v) for v in self.vector(p)),
                     p_sum(mul(v,v) for v in self.vector(p))) for p in range(self.N))
        magnetic=-self.inner(f,mul(r4,f))/192
        return {"D1_norm":d1norm,"D0_D2_cross":cross,
                "electric_metric":d1norm+cross,"Haar":haar,
                "magnetic":magnetic,"total":d1norm+cross+haar+magnetic,
                "rows":perrow}


def main():
    for L in (1,2):
        ex=Experiment(L)
        results={}
        for label,f in (("vacuum",ex.one),("soft_scalar",ex.source())):
            out=ex.evaluate(f)
            results[label]=out
            print("L",L,label,flush=True)
            for k,v in out.items():
                if k!="rows":
                    print(" ",k,"=",v,flush=True)
            assert out["Haar"]==-L*L
        diff={k:results["soft_scalar"][k]-results["vacuum"][k]
              for k in ("D1_norm","D0_D2_cross","electric_metric","Haar","magnetic","total")}
        print("direct excitation-minus-vacuum:",diff,flush=True)
        if L==1:
            assert results["vacuum"]["total"]==-Q(21,16)
            assert results["soft_scalar"]["total"]==-Q(41,16)
            assert diff["total"]==-Q(5,4)
        else:
            c=(SQ2+4+SQ6)/4
            assert results["vacuum"]["magnetic"]==-Q(5,16)*c*c
            assert diff["magnetic"]==-Q(5,32)-Q(5,24)*SQ2-Q(5,48)*SQ3
            assert results["vacuum"]["electric_metric"] == (
                -Q(19,8)+Q(19,16)*SQ2+SQ3/8+Q(7,16)*SQ6)
            assert results["soft_scalar"]["electric_metric"] == (
                -Q(19,8)+Q(133,48)*SQ2+Q(7,24)*SQ3+Q(7,16)*SQ6)
            assert results["vacuum"]["total"] == (
                -Q(219,32)+Q(33,32)*SQ2+Q(3,64)*SQ3+Q(9,32)*SQ6)
            assert results["soft_scalar"]["total"] == (
                -7+Q(77,32)*SQ2+Q(7,64)*SQ3+Q(9,32)*SQ6)
            assert diff["total"] == -Q(5,32)+Q(11,8)*SQ2+SQ3/16
    print("PASS: exact row, covariance, Haar, magnetic and direct-energy checks; L1 calibration.",flush=True)


if __name__=="__main__":
    main()

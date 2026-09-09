"""Exact finite Hermite calculation for FJ/NV; no sampled or truncated dynamics."""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, sqrt


class Q:
    """Q(sqrt(2),sqrt(3)), basis indexed by square-root bit masks."""
    __slots__ = ("v",)
    def __init__(self, a=0, b=0, c=0, d=0):
        self.v = tuple(map(F, (a, b, c, d)))
    def __add__(self, other):
        other = asq(other)
        return Q(*(a+b for a,b in zip(self.v,other.v)))
    __radd__ = __add__
    def __neg__(self):
        return Q(*(-a for a in self.v))
    def __sub__(self, other):
        return self + -asq(other)
    def __rsub__(self, other):
        return asq(other) + -self
    def __mul__(self, other):
        other = asq(other)
        out = [F(0)]*4
        for i,a in enumerate(self.v):
            if not a: continue
            for j,b in enumerate(other.v):
                if b:
                    common=i&j
                    out[i^j] += a*b*(2 if common&1 else 1)*(3 if common&2 else 1)
        return Q(*out)
    __rmul__ = __mul__
    def __truediv__(self, other):
        return self * inverse(asq(other).v)
    def __rtruediv__(self, other):
        return asq(other) * inverse(self.v)
    def __pow__(self,n):
        if n<0: return inverse(self.v)**(-n)
        out=Q(1)
        for _ in range(n): out=out*self
        return out
    def __bool__(self): return any(self.v)
    def __eq__(self, other): return self.v == asq(other).v
    def __repr__(self):
        return " + ".join(str(x)+s for x,s in zip(self.v,("", "*sqrt(2)", "*sqrt(3)", "*sqrt(6)")) if x) or "0"
    def approx(self):
        return sum(float(a)*b for a,b in zip(self.v,(1,sqrt(2),sqrt(3),sqrt(6))))


def asq(x): return x if isinstance(x,Q) else Q(x)


@lru_cache(None)
def inverse(v):
    q=Q(*v)
    if not q: raise ZeroDivisionError
    numerator=Q(1)
    for s,t in ((-1,1),(1,-1),(-1,-1)):
        numerator *= Q(v[0],s*v[1],t*v[2],s*t*v[3])
    norm=q*numerator
    assert norm.v[1:]==(0,0,0)
    return Q(*(a/norm.v[0] for a in numerator.v))


def add(p,q,scale=1):
    out=p.copy(); scale=asq(scale)
    for k,v in q.items():
        out[k]=out.get(k,Q())+scale*v
        if not out[k]: del out[k]
    return out


def scaled(p,s):
    s=asq(s)
    return {k:v*s for k,v in p.items() if v*s}


def omultiply(p,q):
    out={}
    for k,a in p.items():
        for l,b in q.items():
            key=tuple(sorted(k+l))
            out[key]=out.get(key,Q())+a*b
    return {k:v for k,v in out.items() if v}


def cross(a,b):
    return [add(omultiply(a[(i+1)%3],b[(i+2)%3]),
                omultiply(a[(i+2)%3],b[(i+1)%3]),-1) for i in range(3)]


def vadd(a,b,s=1): return [add(x,y,s) for x,y in zip(a,b)]
def vscale(a,s): return [scaled(x,s) for x in a]
def basis(t): return [{():Q(int(a==t))} if a==t else {} for a in range(3)]


class Model:
    def __init__(self,L):
        assert L in (1,2)
        self.L=L
        self.faces=[(i,j) for j in range(1,L+1) for i in range(1,L+1)]
        self.index={p:i for i,p in enumerate(self.faces)}
        self.n=L*L; self.dim=3*self.n; self.zero=(0,)*self.dim
        if L==1:
            self.V=[[F(1)]]; self.w=[Q(2)]
        else:
            self.V=[[F(x,2) for x in row] for row in
                    ((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1))]
            self.w=[Q(0,1),Q(2),Q(2),Q(0,0,0,1)]
        self.x=[ [{(3*m+a,):Q(self.V[p][m]) for m in range(self.n)}
                 for a in range(3)] for p in range(self.n)]
        self.rows=[]
        for t in range(3):
            et=basis(t)
            for i,j in self.faces:
                row=self.empty()
                self.insert(row,(i,j),"R",et,-1)
                if j<L: self.insert(row,(i,j+1),"L",et)
                self.rows.append(row)
            for i in range(1,L+1):
                row=self.empty()
                self.insert(row,(i,1),"L",et)
                for a,k in self.faces:
                    if a>i: self.insert(row,(a,k),"C",et)
                self.rows.append(row)
            for c in range(L+1):
                for j in range(1,L+1):
                    row=self.empty()
                    if c>=1:
                        # Ad_(X_(j-1)^-1 ... X_1^-1) on the generator.
                        transport=[et,[{},{},{}],[{},{},{}]]
                        for k in range(1,j):
                            x=self.x[self.index[c,k]]
                            old=transport
                            transport=[old[0],vadd(old[1],cross(x,old[0]),-1),
                                vadd(vadd(old[2],cross(x,old[1]),-1),
                                     cross(x,cross(x,old[0])),F(1,2))]
                        self.insert(row,(c,j),"L",et,transport=transport)
                    if c<L:
                        self.insert(row,(c+1,j),"R",et,-1)
                        for k in range(j+1,L+1):
                            self.insert(row,(c+1,k),"C",et)
                    self.rows.append(row)
        assert len(self.rows)==3*2*L*(L+1)

    def empty(self): return [[{} for _ in range(self.dim)] for _ in range(3)]

    def insert(self,row,face,side,t,sign=1,transport=None):
        p=self.index[face]; x=self.x[p]
        if transport is None: transport=[t,[{},{},{}],[{},{},{}]]
        t0,t1,t2=transport
        if side=="C":
            jets=[[{},{},{}],vscale(cross(x,t0),-1),vscale(cross(x,t1),-1)]
        else:
            z=F(-1,2) if side=="L" else F(1,2)
            jets=[t0,vadd(t1,cross(x,t0),z),
                  vadd(vadd(t2,cross(x,t1),z),cross(x,cross(x,t0)),F(1,12))]
        for r in range(3):
            for a in range(3):
                for m in range(self.n):
                    k=3*m+a
                    row[r][k]=add(row[r][k],jets[r][a],sign*self.V[p][m])

    def y(self,p,k):
        out={}; w=self.w[k//3]
        for n,a in p.items():
            up=list(n); up[k]+=1; up=tuple(up)
            out[up]=out.get(up,Q())+a
            if n[k]:
                dn=list(n); dn[k]-=1; dn=tuple(dn)
                out[dn]=out.get(dn,Q())+a*n[k]*w
        return {n:a for n,a in out.items() if a}

    def derivative(self,p,k):
        out={}
        for n,a in p.items():
            if n[k]:
                dn=list(n); dn[k]-=1
                out[tuple(dn)]=a*n[k]
        return out

    def times(self,ordinary,p):
        out={}
        for mon,c in ordinary.items():
            q=p
            for k in mon: q=self.y(q,k)
            out=add(out,q,c)
        return out

    def row(self,coeff,p):
        out={}
        for k,c in enumerate(coeff):
            if c:
                dp=add(self.derivative(p,k),self.y(p,k),-1/(2*self.w[k//3]))
                out=add(out,self.times(c,dp))
        return out

    def density(self,row):
        out={}
        for k,c in enumerate(row[0]):
            out=add(out,omultiply(c,{(k,):Q(F(1,12))}))
        return out

    def energy(self,n):
        return sum((self.w[k//3]*v for k,v in enumerate(n)),Q())

    def inv(self,p,shift=0):
        out={}
        for n,c in p.items():
            den=self.energy(n)-shift
            if not den:
                assert not c, (n,c,shift)
            else: out[n]=c/den
        return out

    def K(self,p): return {n:a*self.energy(n) for n,a in p.items() if self.energy(n)}

    @lru_cache(None)
    def normweight(self,n):
        z=Q(1)
        for k,r in enumerate(n):
            if r: z*=factorial(r)*self.w[k//3]**r
        return z

    def inner(self,p,q):
        return sum((a*q.get(n,Q())*self.normweight(n) for n,a in p.items()),Q())

    def f(self,p):
        out=scaled(p,-3)
        for a in range(3):
            out=add(out,self.y(self.y(p,a),a),1/self.w[0])
        return scaled(out,1/Q(0,0,0,1))

    def H1(self,p):
        out={}
        for row in self.rows:
            out=add(out,self.row(row[0],self.row(row[1],p)),-1)
            out=add(out,self.row(row[1],self.row(row[0],p)),-1)
        return out

    def direct(self,p):
        electric=Q(); density=Q()
        for row in self.rows:
            d0=self.row(row[0],p); d1=self.row(row[1],p); d2=self.row(row[2],p)
            electric+=self.inner(d1,d1)+2*self.inner(d0,d2)
            density+=2*self.inner(d0,self.times(self.density(row),p))
        magnetic=Q()
        for x in self.x:
            r2={}
            for a in x: r2=add(r2,omultiply(a,a))
            rp=self.times(r2,p)
            magnetic-=self.inner(rp,rp)/192
        return electric,density,magnetic


def report(label,value):
    print(label, "=", value, "; decimal =", format(value.approx(),".12g"))


def run(L):
    m=Model(L); vac={m.zero:Q(1)}; phi=m.f(vac); c=2*m.w[0]
    assert m.inner(phi,phi)==1 and m.inner(vac,phi)==0
    a=m.H1(vac); b=m.H1(phi)
    u=scaled(m.inv(a),-1); eta=scaled(m.inv(b,c),-1)
    fu=m.f(u); ell=add(fu,eta,-1)
    v0=m.inner(a,m.inv(a)); v1=m.inner(b,m.inv(b,c))
    d0=m.direct(vac); d1=m.direct(phi)
    e0=sum(d0,Q())-v0; e1=sum(d1,Q())-v1; gap=e1-e0
    weight=m.inner(ell,ell)
    leakage=m.inner(ell,m.inv(ell))-weight/c
    source=-gap/c**2+leakage
    q=add(fu,b,-1/c)
    alternative=m.inner(q,m.inv(q))-m.inner(fu,fu)/c-(sum(d1,Q())-e0)/c**2
    assert source==alternative, ("NV11 versus NV13",source,alternative)
    direct_moment=m.inner(fu,add(m.K(fu),fu,-c))+2*m.inner(fu,b)+sum(d1,Q())-e0
    spectral_moment=gap+m.inner(ell,add(m.K(ell),ell,-c))
    assert direct_moment==spectral_moment
    assert all(sum(n)==3 for n in a)
    assert all(sum(n) in (3,5) for n in b)
    assert all(sum(n)==3 for n in ell)
    assert d0[1]==-L*L and d1[1]==-L*L
    if L==1:
        assert not a and not b and not ell
        assert e0==Q(F(-21,16)) and e1==Q(F(-41,16))
        assert gap==Q(F(-5,4)) and source==Q(F(5,64))
    print("PATCH",L, "Hermite supports",len(a),len(b),len(ell))
    for label,z in (("direct vacuum electric",d0[0]),("direct vacuum density",d0[1]),
       ("direct vacuum magnetic",d0[2]),("direct excited electric",d1[0]),
       ("direct excited density",d1[1]),("direct excited magnetic",d1[2]),
       ("virtual vacuum",v0),("virtual excited",v1),("vacuum h2",e0),
       ("excited h2",e1),("gap h2",gap),("leakage weight",weight),
       ("susceptibility leakage",leakage),("normalized susceptibility h2",source),
       ("normalized source energy h2",spectral_moment)):
        report(label,z)
    if L==2:
        assert gap==Q(F(-5,32),F(3,56),F(-5,48))
        assert weight==Q(0,F(2,49),F(1,2))
        assert source==Q(F(-33517,87808),F(109,21952),F(53,384))
        def triple(i,j,k):
            out={}
            for a,b,c,s in ((0,1,2,1),(1,2,0,1),(2,0,1,1),
                             (0,2,1,-1),(1,0,2,-1),(2,1,0,-1)):
                n=[0]*m.dim
                n[3*i+a]=n[3*j+b]=n[3*k+c]=1
                out[tuple(n)]=Q(s)
            return out
        t012=triple(0,1,2); t013=triple(0,1,3)
        expected=add(scaled(t012,Q(0,0,F(1,42))),t013,Q(0,0,F(1,12)))
        assert ell==expected
        # The g-independent compact cubic coefficients -2/7 and -1
        # induce the scaled linear jet -(1/7)T012-(1/2)T013.
        bsharp1=add(scaled(t012,F(-1,7)),t013,F(-1,2))
        fusharp=add(fu,bsharp1,1/Q(0,0,2))
        assert fusharp==eta
        qsharp=add(fusharp,b,-1/c)
        ssharp=m.inner(qsharp,m.inv(qsharp))-m.inner(fusharp,fusharp)/c-(sum(d1,Q())-e0)/c**2
        assert ssharp==-gap/c**2
        report("corrected probe susceptibility h2",ssharp)
        channels={}
        for n,a in ell.items():
            key=tuple(sum(n[3*j:3*j+3]) for j in range(4))
            channels[key]=channels.get(key,Q())+a*a*m.normweight(n)
        for key,w in sorted(channels.items()):
            report("leakage channel "+str(key),w)
        short_terms=[]
        for key,w in sorted(channels.items()):
            nu=sum((m.w[j]*n for j,n in enumerate(key)),Q())
            short_terms.append(w*nu*(nu-c)/c)
        assert short_terms==[Q(3,0,0,1),Q(F(2,7))]
        short_coefficient=2*(gap+sum(short_terms,Q()))
        assert short_coefficient==Q(F(701,112),F(3,28),F(-5,24),2)
        report("innovation h2 short-duration slope",short_coefficient)
    return gap,weight,source


if __name__=="__main__":
    run(1)
    run(2)
    print("PASS: exact field, physical source, density, parity and two response assemblies")

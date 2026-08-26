#!/usr/bin/env python3
"""Receipts for nilpotency-and-the-wall. Stdlib only; exit nonzero on failure.
Verifies (1) the SL(2,R) trace trichotomy on samples, (2) the s6 manuscript's
lattice data as printed (T1^3=I, T2^4=I, T0=(T1T2)^{-1} unipotent, N^2=0,
stated action of N), (3) the A2 discriminant's two fold branches and b -> -b
symmetry. Passing verifies OUR TRANSCRIPTION AND ALGEBRA, not the manuscript's
Main Theorem, which remains conditional per algebra/s6-manuscript-branch."""
import math, sys
from fractions import Fraction as F

fails = []
def ok(name, cond):
    if not cond: fails.append(name)

# (1) trace trichotomy samples: rotation, unipotent, dilation
import cmath
def eig_abs(m):
    a,b,c,d = m
    tr, det = a+d, a*d-b*c
    disc = cmath.sqrt(tr*tr - 4*det)
    return abs((tr+disc)/2), abs((tr-disc)/2)
rot   = (math.cos(1), -math.sin(1), math.sin(1), math.cos(1))   # |tr|<2
unip  = (1, 1, 0, 1)                                            # |tr|=2
dil   = (2, 0, 0, 0.5)                                          # |tr|>2
ok("elliptic |tr|<2", abs(rot[0]+rot[3]) < 2 and abs(eig_abs(rot)[0]-1) < 1e-12)
ok("parabolic |tr|=2 nondiag", abs(unip[0]+unip[3]) == 2)
N2x2 = (0,1,0,0)
ok("nilpotent squares to zero", (N2x2[0]*N2x2[0]+N2x2[1]*N2x2[2]) == 0)
ok("hyperbolic |tr|>2", abs(dil[0]+dil[3]) > 2)

# (2) manuscript lattice data, basis (gamma,u,w,delta), columns = images
I4 = [[1 if i==j else 0 for j in range(4)] for i in range(4)]
T1 = [[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]]
T2 = [[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def mpow(A,n):
    R = I4
    for _ in range(n): R = mm(R,A)
    return R
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(4) for j in range(4))
ok("T1^3 = I", eq(mpow(T1,3), I4))
ok("T2^4 = I", eq(mpow(T2,4), I4))
def inv(A):
    n=4; M=[[F(A[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c,n) if M[r][c]!=0); M[c],M[p] = M[p],M[c]
        piv = M[c][c]; M[c] = [x/piv for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]!=0:
                f=M[r][c]; M[r]=[a-f*b for a,b in zip(M[r],M[c])]
    return [[int(M[i][j+n]) for j in range(n)] for i in range(n)]
T0 = inv(mm(T1,T2))
N  = [[T0[i][j]-I4[i][j] for j in range(4)] for i in range(4)]
ok("N^2 = 0", all(v==0 for row in mm(N,N) for v in row))
col = lambda A,j: [A[i][j] for i in range(4)]
ok("N gamma = 0",  col(N,0) == [0,0,0,0])
ok("N u = 0",      col(N,1) == [0,0,0,0])
ok("N w = -u",     col(N,2) == [0,-1,0,0])
ok("N delta = gamma", col(N,3) == [1,0,0,0])
# rank of N is 2 (the rank-two transverse datum)
ok("rank N = 2", sum(1 for j in range(4) if col(N,j) != [0,0,0,0]) == 2)

# (3) A2 discriminant 4a^3+27b^2: two fold branches for a<0, b->-b symmetric
disc = lambda a,b: 4*a**3 + 27*b**2
for a in (-1.0, -0.3, -2.5):
    b = 2*(-a/3)**1.5
    ok(f"fold branch a={a}", abs(disc(a,b)) < 1e-9 and abs(disc(a,-b)) < 1e-9)
ok("cusp at origin", disc(0,0) == 0)
ok("interior: three real roots side", disc(-1, 0.1) < 0)
ok("exterior: one real root side",  disc(-1, 1.0) > 0)

if fails:
    print("FAILED:", fails, file=sys.stderr); sys.exit(1)
print("ALL RECEIPTS PASS")

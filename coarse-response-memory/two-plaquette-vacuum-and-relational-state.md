# The Interacting Two-Plaquette Vacuum Requires a Relational Channel

Adding a second plaquette introduces a physical relative orientation that cannot be replaced by the two separate plaquette traces. For the supplied two-plaquette Yang--Mills Hamiltonian, the exact vacuum depends on that relational variable at every positive magnetic coupling. An explicit invariant differential operator and complete harmonic basis make this a computable interacting test: the relational term first enters the vacuum at second order, while a single plaquette's hidden dynamical response already appears at first order. This distinguishes genuine growth of the physical carrier from redundant graph subdivision.

**Status: exact finite-system operator and all-positive-coupling nonclosure theorem; fixed-system perturbation and numerical vacuum diagnostics.** The physical Hamiltonian is supplied, not derived from a new action principle. No four-dimensional limit or new physical mass-gap bound is claimed.

## Use the entire physical carrier

Take two adjacent square plaquettes with seven distinct links and
common electric coefficient \(\kappa>0\). The shared path has
weight \(\kappa\), and each outer path has weight \(3\kappa\).
With \(Q=-2\operatorname{Tr}\) on \(SU(2)\),
[[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|the full tree reduction]]
gives
\[
\begin{aligned}
\mathcal H&=L^2(SU(2)^2,dx\,dy)^{\operatorname{Ad}SU(2)},\\
H_\lambda&=H_0+\lambda(2-a-b),\qquad\lambda\ge0,\\
H_0&=4\kappa(D_x+D_y)-2\kappa\sum_AR_{x,A}R_{y,A},\\
a&=\tfrac12\operatorname{Tr}x,\qquad
b=\tfrac12\operatorname{Tr}y.
\end{aligned}
\tag{TP1}
\]
Its positive kinetic form is the sum of the two outer-path forms
and \(\kappa\sum_A|R_{x,A}+R_{y,A}|^2\). Its operator and form
domains are the inherited invariant \(H^2\) and \(H^1\) on the
smooth covering product, not independent boundary conditions in
orbit coordinates. Bounded smooth magnetic multiplication does
not change the operator domain.

Write \(x=aI-i\mathbf x\cdot\boldsymbol\sigma\),
\(y=bI-i\mathbf y\cdot\boldsymbol\sigma\), and put
\[
z=\mathbf x\cdot\mathbf y,\qquad
|z|\le\sqrt{(1-a^2)(1-b^2)}.
\tag{TP2}
\]
The triple \((a,b,z)\) separates simultaneous-conjugation orbits:
it specifies the Gram matrix of the two real vectors, and two
vector pairs with the same Gram matrix are related by an
\(SO(3)\) rotation. This remains true when their span is smaller
than two. Thus these variables describe the complete physical
measurable algebra. Functions of \((a,b)\) alone omit an actual
invariant, not a gauge redundancy.

## An exact differential operator on those invariants

For a smooth function of \((a,b,z)\), write
\[
H_0f=\kappa\left[
3a\,\partial_af+3b\,\partial_bf+
\left(5z-\tfrac32ab\right)\partial_zf
-\sum_{i,j\in\{a,b,z\}}g_{ij}\partial_i\partial_jf
\right],
\tag{TP3}
\]
where \(g\) is dimensionless, symmetric, and
\[
\begin{gathered}
g_{aa}=1-a^2,\qquad g_{bb}=1-b^2,\qquad g_{ab}=z/4,\\
g_{az}=-az-\tfrac14b(1-a^2),\qquad
g_{bz}=-bz-\tfrac14a(1-b^2),\\
g_{zz}=\tfrac32-\tfrac12(a^2+b^2)-\tfrac12a^2b^2
       -\tfrac32z^2+\tfrac12abz.
\end{gathered}
\tag{TP4}
\]
The actual cometric is \(\kappa g\). The double sum in (TP3)
includes both orders of each mixed derivative.

These coefficients follow by differentiation before taking the
gauge quotient. For example,
\[
R_xa=-\mathbf x/2,\quad R_yb=-\mathbf y/2,\quad
R_xz=(a\mathbf y-\mathbf x\times\mathbf y)/2,\quad
R_yz=(b\mathbf x+\mathbf x\times\mathbf y)/2.
\tag{TP5}
\]
The kinetic form in (TP1) then gives (TP4) and its positivity on
the physical orbit domain. Direct differentiation gives the
first-order coefficients in (TP3). Useful exact checks are
\[
H_0(ab)=\kappa(6ab-z/2),\qquad
H_0z=\kappa(5z-3ab/2),\qquad
H_0(ab+z)=\tfrac92\kappa(ab+z).
\tag{TP6}
\]
These agree with
[[gauge-boundary-frame-gluing/holonomy-refinement-and-clock-compatibility#Individually autonomous loop readouts can have a nonautonomous join|the exact free two-channel return]].
Discarding the shared derivative would remove precisely the
\(z\)-term in \(H_0(ab)\).

## The exact vacuum cannot depend only on separate traces

Compact ellipticity and positivity improvement give a unique
normalized smooth strictly positive ground vector
\(\psi_\lambda\). The Hamiltonian commutes with interchange of
\(x,y\), so uniqueness and positivity give an exchange-symmetric
vacuum. Suppose, for contradiction, that
\(\psi_\lambda=F(a,b)\), with no dependence on \(z\).

The only \(z\)-dependent term of its eigenvalue equation is
\(-\kappa z F_{ab}/2\). For every interior \((a,b)\), the allowed
\(z\)-interval has positive length, so \(F_{ab}=0\).
Hence \(F=A(a)+B(b)\), and exchange symmetry permits the form
\(F=A(a)+A(b)\) after adjusting constants.

The remaining kinetic and eigenvalue terms are sums of separate
functions of \(a\) and \(b\). Applying \(\partial_a\partial_b\)
to the magnetic term therefore forces
\[
-\lambda[A'(a)+A'(b)]=0.
\tag{TP7}
\]
When \(\lambda>0\), taking \(a=b\) makes \(A\) constant.
A positive constant cannot solve the eigenvalue equation with
the nonconstant potential \(\lambda(2-a-b)\). Consequently
\[
\boxed{\lambda>0\quad\Longrightarrow\quad
\psi_\lambda\notin L^2(\sigma(a,b),dx\,dy).}
\tag{TP8}
\]
Almost-everywhere trace-only dependence also yields the same
contradiction: smoothness promotes it to independence along
interior \(z\)-fibers. This proves genuine relational dependence,
not a positive pointwise lower bound on \(|\partial_z\psi|\).
Since \(\psi>0\), its density \(w=\psi^2\) has the same
nonclosure property. The theorem is stronger than failure of a
product ansatz \(F(a,b)=F_1(a)F_2(b)\).

## Static and dynamical relational terms start at different orders

Put \(r=\lambda/\kappa\). Analytic perturbation of the simple
Haar vacuum, with elliptic regularity, gives
\[
\begin{aligned}
E_0/\kappa&=2r-r^2/6+O(r^3),\\
\psi_\lambda
&=1+\frac r3(a+b)\\
&\quad+r^2\left[
\frac{a^2+b^2-\tfrac12}{24}
+\frac{40ab+4z}{351}-\frac1{36}
\right]+O(r^3).
\end{aligned}
\tag{TP9}
\]
The vector is normalized in product Haar \(L^2\). To check the
second coefficient, use (TP6) and
\(H_0(a^2-1/4)=8\kappa(a^2-1/4)\). The constant \(-1/36\)
is minus one half the squared norm of \((a+b)/3\).
The remainder is controlled in every fixed smooth or Sobolev
norm on the underlying compact \(SU(2)^2\). No uniform bound on
singular-coordinate derivatives at the orbit boundary, or on
larger graph volumes, is asserted.

Let \(\mathcal L_\lambda=-\psi_\lambda^{-1}
(H_\lambda-E_0)\psi_\lambda\) be the physical ground-state
generator on \(L^2(w\,dx\,dy)\). Set
\[
\mathcal L_\lambda(2a)
=-6\kappa a+4\kappa\sum_jg_{aj}\partial_j\log\psi_\lambda.
\tag{TP10}
\]
Using the first-order vacuum alone gives
\[
\mathcal L_\lambda(2a)
=-6\kappa a+\frac{4\lambda}{3}(1-a^2)
 +\frac{\lambda}{3}z+O(\lambda^2/\kappa).
\tag{TP11}
\]
Thus the shared response already sends this single-plaquette
observable into the relational channel at first order. The
vacuum itself first contains an explicit \(z\)-term at second
order. These are different mechanisms and different objects.

## Measure memory against the complete one-plaquette readout

Let \(P_a=\mathbb E_w[\cdot\mid a]\), retaining every function
of \(a\), and put
\[
\mathcal D_\lambda
=\|(I-P_a)\mathcal L_\lambda(2a)\|_w^2
=\mathbb E_w\operatorname{Var}_w
       (\mathcal L_\lambda(2a)\mid a).
\tag{TP12}
\]
This is the exact short-time coefficient in the compressed
semigroup defect, by
[[interacting-gauge-vacuum-and-local-memory|the physical local-memory identity]].
It is not compression onto the span of one character.
Since \(\mathbb E_H[z\mid a]=0\) and
\(\mathbb E_Hz^2=3/16\), (TP11) gives
\[
\mathcal D_\lambda=\lambda^2/48+O(\lambda^4/\kappa^2).
\tag{TP13}
\]
For finite positive coupling, the conditional law must be that
of the actual interacting vacuum, not Haar. The all-coupling
state theorem (TP8) by itself does not prove a strictly positive
value of (TP12) at every coupling. The improved even-order
remainder in (TP13) uses the central-flip symmetry established
below; it is specific to this two-plaquette family.

To compute the complete conditional integral, write
\(z=\sqrt{(1-a^2)(1-b^2)}u\). Product Haar reduces to
\[
d\mu_H(a)\,d\mu_H(b)\,\frac{du}{2},\qquad
d\mu_H(a)=\frac2\pi\sqrt{1-a^2}\,da,
\quad -1\le a,b,u\le1.
\tag{TP14}
\]
Equivalently, its density on the orbit body (TP2) is the
constant \(2/\pi^2\) relative to \(da\,db\,dz\). The Jacobian
\(dz=\sqrt{(1-a^2)(1-b^2)}\,du\) cancels the two radial Haar
weights. Consequently \(-\kappa\operatorname{div}(g\nabla)\)
independently reproduces (TP3), including every drift coefficient.
Flat coordinate density does not make the response metric flat,
or authorize new boundary conditions on this stratified body.

For each \(a\), integrate both \(b\) and \(u\), weighted by
\(\psi^2\), to obtain its marginal and conditional mean in
(TP12). Omitting \(u\) from the vacuum basis would presuppose
exactly the false closure excluded by (TP8).

## A complete basis makes the interacting test reproducible

Let \(n,m\) be nonnegative integers and
\(0\le k\le\min(n,m)\). A real orthogonal physical basis is
\[
B_{nmk}(a,b,u)=
(1-a^2)^{k/2}(1-b^2)^{k/2}
C_{n-k}^{k+1}(a)C_{m-k}^{k+1}(b)P_k(u).
\tag{TP15}
\]
Here \(C_p^\alpha\) and \(P_k\) are Gegenbauer and Legendre
polynomials with their usual normalizations. In terms of
\((a,b,z)\) these are polynomials: the multiplied Legendre
factor satisfies
\[
S_0=1,\quad S_1=z,\quad
(k+1)S_{k+1}=(2k+1)zS_k
-k(1-a^2)(1-b^2)S_{k-1}.
\tag{TP16}
\]
Separation into spherical harmonics on each \(S^3\), followed by
pairing equal \(SO(3)\) angular momentum to a singlet, gives
precisely this basis. There are no omitted angular singlets for
two vectors. Its norm is
\[
\|B_{nmk}\|^2=\frac{h_{n-k,k}h_{m-k,k}}{2k+1},\qquad
h_{p,k}=\frac{(p+2k+1)!}
 {4^k p!(p+k+1)(k!)^2}.
\tag{TP17}
\]
Orthogonality follows directly from (TP14) and the corresponding
weighted polynomial orthogonalities. Their union spans the full
invariant carrier and gives a smooth operator core.

In the normalized basis, \(H_0\) preserves each \((n,m)\) block.
This also follows from commutation with \(D_x,D_y\). Magnetic
multiplication by \(a\) or \(b\) changes its respective harmonic
degree by one. For \(K=H_0/\kappa\), the nonzero block entries are
\[
\begin{aligned}
K_{kk}&=n(n+2)+m(m+2)-\tfrac12k(k+1),\\
K_{k,k+1}&=-\frac{k+1}{2}
\sqrt{\frac{[(n+1)^2-(k+1)^2][(m+1)^2-(k+1)^2]}
 {(2k+1)(2k+3)}}.
\end{aligned}
\tag{TP18}
\]
They are symmetric; all other entries vanish. Multiplication by
\(a\) has raising entry
\[
\langle n+1,m,k|a|n,m,k\rangle
=\frac12\sqrt{\frac{(n-k+1)(n+k+2)}{(n+1)(n+2)}}.
\tag{TP19}
\]
The lowering entry is its transpose; interchange \(n,m\) for
\(b\). Equation (TP19) is the normalized Gegenbauer recurrence.
For (TP18), apply (TP3) to the polynomial form (TP16): the
highest \(z\)-degree can increase by at most one. Self-adjointness
therefore makes the block tridiagonal. The top coefficient,
Gegenbauer differentiation, and (TP17) give the off-diagonal
entry; the coefficient at the same degree gives its diagonal.
The \(n=m=1\) block has diagonal \((6,5)\) and off-diagonal
\(-\sqrt3/2\), agreeing with (TP6).

Cutoffs \(n,m\le N\) therefore give a convergent
Rayleigh--Ritz construction with every allowed \(k\) retained.
The omitted-neighbor coefficients of the potential provide a
full-space residual check; the residual of the finite eigensolver
alone would not do so.

[[receipts/two_plaquette_vacuum_receipt.py|The interacting two-plaquette receipt]]
uses this complete basis, independent polynomial-operator checks,
cutoff refinement and positive conditional quadrature. Its
floating-point diagnostics do not replace the exact proofs above
or constitute interval-certified spectral bounds.

With \(\kappa=1\), the computed values are:

| Magnetic coupling \(\lambda\) | Vacuum energy \(E_0\) | Conditional memory \(\mathcal D_\lambda\) |
| --- | --- | --- |
| 0.5 | 0.958505191537 | 0.00506469497865 |
| 1.0 | 1.83601100236 | 0.0186933033059 |

The cutoffs \(N=2,4,6,8\) contain \(14,55,140,285\) invariant
modes. The final full-space residuals are below \(10^{-12}\) in
floating point. Independent radial/angular quadratures agree on
the complete conditional mean and variance. At \(\lambda=0.02\),
\(\mathcal D_\lambda/\lambda^2\simeq0.020832391034\), approaching
\(1/48\); at \(\lambda=1\) it is about \(0.0186933\), so using
the leading coefficient as an exact finite-coupling value would
be wrong. These are computed local-memory values, not masses.

## The leading finite-time return retains two hidden rates

The same finite system permits an analytic test beyond an
instantaneous coefficient. For \(\chi=2a\), define
\[
d_\lambda(t)=\|(I-P_a)e^{t\mathcal L_\lambda}\chi\|_w^2
=\langle\chi,(R_{2t}-R_t^2)\chi\rangle_w,
\quad R_t=P_ae^{t\mathcal L_\lambda}|_{L^2(\sigma(a),w)}.
\tag{TP20}
\]
Centering \(\chi\) by its actual mean leaves the defect unchanged.
Put \(\tau=\kappa t\), \(r=\lambda/\kappa\). For fixed \(\tau\),
\[
\boxed{
d_\lambda(t)=r^2\left[
\frac{(e^{-3\tau}-e^{-9\tau/2})^2}{144}
+\frac{(e^{-3\tau}-e^{-13\tau/2})^2}{2352}
\right]+O(r^4).
}
\tag{TP21}
\]
The remainder can be controlled uniformly on compact
\(\tau\)-intervals. This is not a long-time-uniform expansion
or a bound on the interacting spectral threshold.

One must carry the changing vacuum and conditional projection
when deriving (TP21). In fixed Haar space, transport by
\(f\mapsto\psi_\lambda f\), and write \(\widetilde P_r\) for
the projection onto \(\psi_\lambda L^2(\sigma(a),w)\).
At \(r=0\), \(\widetilde P_0\) is Haar conditioning on \(a\),
and direct differentiation of that conditional formula gives
\(\widetilde P'_0\chi=2ab/3\).
Since
\((H_\lambda-E_0)/\kappa=H_0/\kappa-r(a+b)+O(r^2)\),
Duhamel differentiation on this fixed carrier gives
\[
(I-\widetilde P_r)e^{-t(H_\lambda-E_0)}
 (\psi_\lambda\chi)
=\frac r3\int_0^\tau
 e^{-(\tau-s)K_H}z\,e^{-3s}\,ds+O(r^2),
\tag{TP22}
\]
where \(K_H\) is \(H_0/\kappa\) restricted to the Haar-hidden
subspace. The projection derivative cancels an otherwise
spurious \(ab\) contribution. This argument uses bounded
potential perturbation of the fixed compact operator, not an
assumed bounded retained/hidden off-diagonal operator.

The forcing stays in the two-dimensional hidden space spanned by
\(B=ab+z\) and \(C=3ab-z\). They are Haar-orthogonal, with
eigenvalues \(9/2,13/2\), squared norms \(1/4,3/4\), and
\(z=(3B-C)/4\). Evaluating the two convolutions in (TP22) and
taking the squared norm gives (TP21). Its small-\(\tau\)
coefficient is \(r^2\tau^2/48=\lambda^2t^2/48\), consistent
with (TP13). The finite-time experiment therefore retains the
hidden rates, not just one averaged local rate.

The even-order remainder follows from an exact symmetry, not
a numerical fit. Extend the finite family to signed \(r\) near
zero and let \(UF(x,y)=F(-x,-y)\). Centrality preserves \(H_0\),
while
\[
UH_rU^{-1}=H_{-r}+4\kappa rI,\qquad U\chi=-\chi.
\tag{TP23}
\]
Here \(H_r\) means (TP1) with \(\lambda=\kappa r\).
The energy shift cancels in the ground-state-transformed clock.
The flip preserves the one-plaquette readout algebra, so both
\(d_r\) and \(\mathcal D_{\kappa r}\) are even analytic
functions of \(r\). This removes odd terms in their expansions;
it does not make the vacuum vector itself even.

The receipt also evolves the inserted raw vector
\(\psi_\lambda\chi\) with the full Galerkin Hamiltonian and
then conditions on the entire \(a\)-algebra. It does not
exponentiate a rebuilt one-variable clock. At \(\kappa=1\),
\(\lambda=0.01\), \(t=0.4\), the computed
\(d_\lambda(t)/\lambda^2\) is \(0.000150137076\), compared
with the leading value \(0.000150140070\). Cutoffs 6 and 8,
independent positive quadratures, and the zero-coupling control
agree. This verifies a finite-time calculation, not a
long-time-uniform approximation.

## The actual marginal retains a tensorial condition

[[radial-marginal-and-conditional-stress|The radial marginal and conditional metric stress]]
owns the exact marginal equation and its small-coupling
curvature result. The shared-edge terms force cancellation
between the horizontal and hidden kinetic contributions.
The effective force nevertheless depends on orbit stress,
not just the shape-projected scalar response. This is a
constraint on how the joint state can return a local clock;
it does not make the marginal a closed physical dynamics.

## What this changes in the whole-to-local programme

[[positive-amplitude-kernel-and-preparation|The positive amplitude-kernel realization]]
extracts another constraint from the same shared geometry.
The actual Haar heat amplitude is a Gram average, with a
completely positive kernel evolution. Its normalized square
returns the local probability law; its transported rows
return conditional response. Even this stronger positivity
class admits states whose initially flat local marginals
lose latitude concavity. The preparation, not only its
positive cone, must constrain the relevant correlations.

[[gauge-boundary-frame-gluing/source-action-transport-through-ordered-cuts#Coherent spatial extension retains its reference experiment|Coherent transport through redundant vertices]]
preserves an already chosen comparison law but cannot remove its
initial reference experiment. Genuine cycle addition is different:
it enlarges the physical carrier, and the supplied interacting
equation already forces the state outside the separate-trace
subalgebra. A proposed assembly law that keeps only regional
scalar densities cannot reproduce even this finite target.

The required relational channel is not a new field or a fitted
potential term: it is an existing invariant on the full gauge
carrier, whose participation is forced by the shared derivative
and the eigenvalue equation. This is a constraint on what a
replacement mathematical framework must preserve. It does not
select the physical Hamiltonian used to prove the constraint,
identify nonassociativity with temporal ordering, or supply a
uniform lower bound on all nonvacuum excitations.

The separate-trace functions already form an associative
subalgebra. Conditional expectation onto them therefore has zero
[[algebra/octonionic-associator-and-branch-forgetting#A retained product can become nonassociative|projected-product associator]]:
the failure here is dynamical closure, not associativity of their
multiplication. A nonassociative parent remains a possible
organizing structure. A bridge must specify its multiplication
or comparison operation and show how its defect constrains the
omitted orientation channel; the forced channel is not itself
that defect.

The [[local-score-bounds-and-the-order-of-hidden-response#Joining scalar readouts changes the differential order|full joined-readout test]]
makes this loss quantitative beyond the first character. Omitting
\(z\) creates a hidden second derivative whose norm cannot be
bounded by the retained first-derivative energy, at any fixed
finite coupling. The sharp Haar replacement is an operator-domain
bound, not a form-domain bound. Thus the mixed response changes
the required operator type, not merely the value of a coefficient.

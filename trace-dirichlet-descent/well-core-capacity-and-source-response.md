# Well-Core Capacity and the Metric of a Retained Distinction

A sharp finite label is not a finite-energy observable of a connected smooth diffusion. Harmonic interpolation between separated well cores supplies a legitimate retained form, whose conductance and inherited inner product must both be kept. Changing to a diagonal label metric changes the apparent rate, but the binary quotient of source response by that rate remains exactly the required source transfer squared divided by capacity. This exposes a slow channel without assigning it a new clock.

## A hard label has the wrong form domain

Let \(Y\) be a closed connected positive-dimensional Riemannian manifold with smooth positive probability density \(\mu\), and use
\[
\mathcal E(f)=\int|\nabla f|^2d\mu,\qquad D(\mathcal E)=H^1(Y).
\tag{WC1}
\]
An \(H^1\) function taking finitely many real values is constant almost everywhere. To prove this, choose a smooth Lipschitz scalar function \(\psi\) fixing those values and having derivative zero near each of them. Then \(\psi(f)=f\), while the Sobolev chain rule gives \(\nabla f=\psi'(f)\nabla f=0\). Connectedness makes \(f\) constant.

Consequently a nontrivial hard finite partition does not pull back a densely defined diffusion form on its full finite label algebra: only its constant functions belong to the inherited form domain. A discontinuous label is still a valid bounded measurable observable, but inserting it into \(\mathcal E\) is not automatically meaningful. Its statistical Fisher information and its gradient energy have different domain requirements.

## Interpolate through the separator

Choose \(k\ge2\) disjoint closed smooth cores \(A_1,\ldots,A_k\) with positive volume and positive separation. Let \(T=Y\setminus\bigcup_i A_i\) be the transition region. For \(u\in\mathbb R^k\), minimize
\[
\mathcal E(H_u)=
\inf\{\mathcal E(f):f=u_i\ {\rm a.e.\ on}\ A_i\}.
\tag{WC2}
\]
Smooth separated cutoff functions make the affine constraint nonempty. The anchored Poincare inequality, using any positive-volume core to fix constants, makes the direct method coercive on its homogeneous constraint space. Weak compactness and lower semicontinuity give a minimizer. The difference of two minimizers has zero energy and vanishes on the cores, hence is zero.

This defines a linear harmonic lift \(H\). Its functions are \(H^1\), harmonic for the weighted diffusion on \(T\), and constant on the cores. Normal derivatives need not match across core boundaries, so global smoothness is not asserted.

Put \(h_i=H_{e_i}\). Truncation and uniqueness give
\[
0\le h_i\le1,\qquad \sum_i h_i=1.
\]
The retained conductance form is
\[
C_{ij}=\mathcal E(h_i,h_j),\qquad
\mathcal E(H_u)=u^\mathsf TC u.
\tag{WC3}
\]
It has \(C\mathbf1=0\), \(C_{ij}\le0\) for \(i\ne j\), and kernel exactly the constants. Indeed a normal contraction \(\psi\) sends a feasible \(H_u\) to a feasible competitor for the core values \(\psi(u)\), proving the finite Dirichlet contraction property. Its equivalent matrix statement gives the off-diagonal signs.

This is a domain-compatible instance of [[inq|harmonic trace descent]]. Prescribing core values, unlike an arbitrary conditional average, commutes with normal contractions. That distinction is why the conductance matrix is Markovian here.

## The energy matrix is not the whole operator

The inherited whole \(L^2(\mu)\) metric is
\[
M_{ij}=\mu(h_i h_j),\qquad
\pi_i=\mu(h_i),\qquad D_\pi=\operatorname{diag}(\pi_i).
\tag{WC4}
\]
Positive core masses make \(M\) positive definite. Since the \(h_i\) form a partition of unity,
\[
\boxed{
\operatorname{diag}(\mu(A_i))\le M\le D_\pi,\qquad
D_\pi-M=\mu[\operatorname{diag}(h)-hh^\mathsf T]\ge0.}
\tag{WC5}
\]
The difference is the covariance of the interpolation weights. It vanishes on the cores and measures their remaining ambiguity in the transition region.

Two distinct operator constructions now exist:
\[
A_M=M^{-1}C,\qquad A_\pi=D_\pi^{-1}C.
\tag{WC6}
\]
The first is the operator of the harmonic-image restricted form in its exact inherited metric. It is positive and self-adjoint for that metric, but \(-A_M\) need not generate a positivity-preserving semigroup on the coordinatewise positive cone. The second has stationary weights \(\pi\) and generates a reversible Markov evolution with generator \(-A_\pi\). It replaces the inherited metric by a diagonal one; it is not an isometric return to the original \(L^2\) carrier.

Nor does a restricted-form operator equal the actual whole evolution compressed to that image unless the image is reducing. Harmonic minimization fixes an energy extension, not an invariant time evolution. A gap proved only on this trial subspace is an upper test for the complete gap, not a lower bound on every whole mode.

### A four-vertex witness to the metric distinction

Take an undirected graph with conductances \(c_{14}=2\), \(c_{24}=c_{34}=1\), \(c_{12}=6\), all others zero, and \(\mu_i=1/4\). Use
\(\mathcal E(f)=\sum_{i<j}c_{ij}(f_i-f_j)^2\). Retain vertices \(1,2,3\) as the cores. The hidden harmonic row is \((1/2,1/4,1/4)\), giving
\[
M=\frac1{64}
\begin{pmatrix}20&2&2\\2&17&1\\2&1&17\end{pmatrix},
\qquad
C=\frac14
\begin{pmatrix}28&-26&-2\\-26&27&-1\\-2&-1&3\end{pmatrix}.
\tag{WC7}
\]
Although \(C\) has the required conductance signs,
\((M^{-1}C)_{32}=2/11>0\). Starting the coordinate evolution at \(e_2\) produces a negative derivative in component three. Thus an exact inherited metric can prevent a harmonic-image operator from being a jump generator even though its energy form has the familiar finite conductance matrix.

This example concerns a graph, where hard vertex labels do have finite energy. It illustrates the metric issue separately from the smooth-domain obstruction above.

## Source transfer divided by capacity

At a fixed reference law, take a real mean-zero score \(s\in L^2(\mu)\), and keep the harmonic test functions fixed when pairing with it. Define
\[
r_i=\mu(s h_i),\qquad \sum_i r_i=0.
\]
For every \(v\in L^2(TY,\mu)\) satisfying
\(-\operatorname{div}(\mu v)=\mu s\) weakly,
\[
|r^\mathsf Tu|
=|\mu(\nabla H_u\cdot v)|
\le\sqrt{u^\mathsf TC u}\,\|v\|_{L^2(\mu)}.
\]
The identity extends to \(H^1\) tests by density. Optimizing over \(u\) gives
\[
\boxed{\int|v|^2d\mu\ge r^\mathsf TC^+r.}
\tag{WC8}
\]
Here \(C^+\) is the Euclidean matrix pseudoinverse; the expression is unambiguous because \(r\) annihilates the constant kernel. This is a lower bound on all transport energies, not an assertion that testing only the harmonic core image captures the full optimum.

If the harmonic functions are recomputed as the state varies, differentiating them produces extra terms. The fixed-reference score pairing in (WC8) must not be confused with that moving-test derivative.

For two cores, let \(h=h_+\), \(p=\mu h\), \(v_h=\operatorname{Var}_\mu h\), \(d=\mu(sh)\), and
\[
c=\mathcal E(h)=\operatorname{cap}_\mu(A_+,A_-).
\]
The two apparent nonzero rates and squared source norms are
\[
\lambda_M=c/v_h,\qquad I_M=d^2/v_h,\qquad
\lambda_\pi=\frac{c}{p(1-p)},\qquad
I_\pi=\frac{d^2}{p(1-p)}.
\tag{WC9}
\]
The last source norm is the Fisher information of the soft readout with probabilities \((\mu h,1-\mu h)\), when its kernel \(h\) is held fixed. The first is the dual norm of the same source functional in the inherited harmonic-image metric. They satisfy the exact common quotient
\[
\boxed{
\frac{I_M}{\lambda_M}
=\frac{I_\pi}{\lambda_\pi}
=\frac{d^2}{c}
\le\inf_v\int|v|^2d\mu.}
\tag{WC10}
\]
Changing the metric alters both the rate and the source norm. Keeping only the altered rate would mistype the comparison.

Moreover,
\[
p(1-p)-v_h=\mu[h(1-h)].
\tag{WC11}
\]
For cores exchanged by a symmetry preserving both the measure and the Dirichlet form, such as a measure-preserving isometry, uniqueness gives \(h\circ R=1-h\). Thus \(p=1/2\) and
\[
4c\le\lambda_M\le\frac{4c}{1-\mu(T)}.
\tag{WC12}
\]
The upper bound uses \(h(1-h)\le\mathbf1_T/4\). More generally, if \(0\le\varepsilon<1\) and \(\mu(A_i)\ge(1-\varepsilon)\pi_i\) for every core, the first nonzero restricted-form eigenvalues obey
\(\lambda_\pi\le\lambda_M\le\lambda_\pi/(1-\varepsilon)\), by (WC5) on the common \(\pi\)-mean-zero subspace.

## Application to the Wilson well label

For [[rg-covariance-residue/su3-context-flux-obstruction|the symmetric \(SU(3)\) conditional]], choose small fixed cores about \(zI,z^2I\), exchanged by inversion. They contain the only minima. Their complement therefore has exponentially small \(q_\kappa\)-probability, with \(\kappa=2\beta/3\). The equilibrium potential is one on the positive core, zero on the negative core, and stays between zero and one.

The same concentration that gives (SF13) now yields
\[
p=\tfrac12,\qquad v_h\to\tfrac14,\qquad
d/\beta\to-2\sqrt3.
\tag{WC13}
\]
A smooth barrier cutoff equal to the prescribed values on the cores is an admissible competitor in the capacity minimization. [[rg-covariance-residue/frustrated-su3-conditional-wells|The barrier estimate]] consequently gives, for each fixed \(0<\eta<1/2\),
\[
c\le C_\eta\kappa^4e^{-\eta\kappa},
\qquad
\inf_v\int|v|^2dq_\kappa
\ge c_\eta\beta^2\kappa^{-4}e^{\eta\kappa}
\quad(\beta\ {\rm sufficiently\ large}).
\tag{WC14}
\]
The cores can be chosen inside the plateau regions of these cutoffs. The exact norm and diagonal metric become asymptotically equivalent, but the capacity and both rates still tend to zero. Retaining the label exposes the slow channel; assigning it a unit-rate refresh would change the dynamics.

Capacity is an \(L^2\) variational energy through a transition region. It is not the \(L^1\) weighted perimeter in [[conditional-fisher-coercivity/bounded-transport-and-cut-flux|the maximum-speed cut criterion]]. Their source bounds answer different optimization questions.

[[rg-covariance-residue/coherent-staple-localization|Allowing surrounding links to move]] instead changes which degrees of freedom participate in the joint estimate, while keeping the actual law and inherited form. That construction controls a local bad-context sector but still leaves a block-response problem. Neither label interpolation nor joint localization is yet the physical transfer operator of a four-dimensional continuum theory.

The [[receipts/well_core_response_receipt.py|finite receipt]] checks harmonic minimization, conductance signs, the inherited Gram correction, the non-Markov witness, and the binary quotient identities. The Sobolev-domain and continuum capacity statements have the direct proofs above.

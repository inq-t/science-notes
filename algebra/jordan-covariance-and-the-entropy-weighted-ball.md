# Jordan Covariance and the Entropy-Weighted Ball

The sphere-to-ball projection determines a local diffusion co-metric that is exactly the symmetrized covariance of qubit observables. Its inverse is the symmetric-logarithmic-derivative metric, not the determinant Hessian or the relative-entropy Hessian. The forgotten fibers contribute a volume weight; together with this metric, that weight fixes the drift, weighted curvature and sharp response gap. Thus one declared whole-to-local geometry constrains several retained structures at once. This is a state-space construction, not yet an emergent spacetime or a Yang–Mills mass.

## The same retained geometry has a quantum covariance

Use the [[sphere-to-ball-descent-and-the-jacobi-response|sphere-to-ball construction]] with \(n=9\), \(k=3\). Primitive elements of the selected rank-two octonionic corner form \(S^8\). Retaining a complex three-plane sends them to
\[
\rho_x=\frac{I+x\cdot\sigma}{2},\qquad |x|\le1.
\]
The round law and spherical Laplacian induce
\[
a(x)=I-xx^T,\qquad
\mathcal Lf=a^{ij}\partial_i\partial_jf-8x\cdot\nabla f,
\qquad
d\nu=\frac{105}{32\pi}(1-|x|^2)^2\,dx.
\tag{JC1}
\]
Here \(x\) labels a qubit state, not a position in physical space.

For a Hermitian matrix \(A=a_0I+\mathbf a\cdot\sigma\), its affine expectation symbol is
\[
f_A(x)=\operatorname{Tr}(\rho_xA)=a_0+\mathbf a\cdot x.
\]
Use the bilinear carré du champ
\[
\Gamma(f,g)=\frac12\{\mathcal L(fg)-f\mathcal Lg-g\mathcal Lf\}
=\nabla f^Ta\nabla g.
\tag{JC2}
\]
The Pauli multiplication rule proves
\[
\boxed{
\Gamma(f_A,f_B)
=\mathbf a\cdot\mathbf b-(\mathbf a\cdot x)(\mathbf b\cdot x)
=\operatorname{Tr}\bigl(\rho_x(A\circ B)\bigr)-f_Af_B,
\quad A\circ B=\frac{AB+BA}{2}.}
\tag{JC3}
\]
Scalar parts cancel. The induced co-metric therefore measures the symmetrized covariance of the retained affine observables. It is not merely a positive matrix independently attached to the ball.

The marked complex corner also supplies an oriented bracket
\[
\Pi_x(f_A,f_B)
=x\cdot(\mathbf a\times\mathbf b)
=\operatorname{Tr}\left(\rho_x\frac{[A,B]}{2i}\right).
\]
Extending both pairings complex-bilinearly, on **complex affine symbols** the even and odd pieces give
\[
\boxed{f_A\star f_B=f_Af_B+\Gamma(f_A,f_B)+i\Pi_x(f_A,f_B)=f_{AB}.}
\tag{JC4}
\]
The quadratic terms cancel, so the answer remains affine. Since \(A\mapsto f_A\) is injective, this product is associative, with \(f_A^*=f_{A^*}\); the matrix operator norm supplies its \(C^*\)-norm. Reversing the chosen orientation gives the opposite product.

This distinguishes two algebra structures on related carriers. Affine expectation symbols are not a subalgebra under ordinary pointwise multiplication, but with (JC4) they reproduce \(M_2(\mathbb C)\). The full commutative function algebra on the ball is different. For example, \(x_1+ix_2\) has ordinary supremum norm one but matrix norm two. The transported norm satisfies \(\|f\|_\star^2=\sup_{|x|\le1}(\bar f\star f)(x)\).

Applying the same differential formula beyond the affine carrier actually fails associativity. With \(z=x_1\),
\[
(z\star z)\star z^2-z\star(z\star z^2)=-2(1-z^2)^2.
\]
This is a failure of that extension, not an identification of its associator with octonionic multiplication. The covariance alone does not select the odd bracket or physical chirality.

## Which metric has actually appeared?

Inside the ball the inverse co-metric is
\[
g_x=a(x)^{-1}=I+\frac{xx^T}{1-|x|^2}.
\tag{JC5}
\]
Its quantum meaning can be checked directly. For a tangent \(v\), put \(d\rho=(v\cdot\sigma)/2\), and solve the symmetric logarithmic derivative equation
\[
d\rho=\frac{\rho_x\ell_v+\ell_v\rho_x}{2}.
\]
Writing \(\ell_v=\alpha I+\mathbf b\cdot\sigma\) gives
\[
\alpha=-\frac{x\cdot v}{1-|x|^2},\qquad
\mathbf b=v+\frac{x\cdot v}{1-|x|^2}x,
\]
\[
\boxed{\operatorname{Tr}(\rho_x\ell_v^2)
=|v|^2+\frac{(x\cdot v)^2}{1-|x|^2}=g_x(v,v).}
\tag{JC6}
\]
Thus (JC5) is the SLD Fisher metric in this normalization.

For comparison, set \(r=|x|\) and use the affine Bloch tangent \(v\) in all three rows:

| Metric on the trace-one slice | Tangential coefficient | Radial coefficient |
|---|---:|---:|
| SLD Fisher, (JC6) | \(1\) | \((1-r^2)^{-1}\) |
| BKM relative-entropy Hessian | \(\operatorname{artanh}(r)/r\) | \((1-r^2)^{-1}\) |
| Affine Hessian of \(\mathcal F=-\tfrac12\log\det(I+x\cdot\sigma)\) | \((1-r^2)^{-1}\) | \((1+r^2)(1-r^2)^{-2}\) |

The BKM row follows by evaluating
\(\operatorname{Tr}(d\rho\,D\log\rho_x[d\rho])\) in the eigenbasis of \(\rho_x\): the off-diagonal divided difference is \(2\operatorname{artanh}(r)/r\), with the factors of \(1/2\) in \(d\rho\) included. Its Hessian role is explained in [[basic-concepts/hessians/gibbs-free-energy-relative-entropy|relative entropy and response]]. The determinant row is the restriction of the [[positive-cone-processes-and-the-complex-corner|cone potential]] to this affine slice.

All three agree at \(x=0\), interpreting \(\operatorname{artanh}(r)/r\) by its limit. They differ away from the center. Sharing positivity and a common value at the balanced state does not identify their operators.

[[purification-descent-and-the-matrix-response|Matrix purification descent, PM11a]]
extends the covariance/SLD duality to every faithful finite matrix state.
Its covariance maps observable classes modulo the scalar identity to
traceless state tangents; the inverse solves the SLD Sylvester equation.
This specifies the dual carriers without identifying either response
with a BKM Hessian.

## Fiber volume fixes the remaining drift

Return to general \(n>k\ge1\), with \(m=n-k\ge2\). Put
\[
y=\sqrt{1-|x|^2},\qquad b=m-1>0,\qquad N=k+b=n-1.
\]
The graph \(x\mapsto(x,y)\) is the open upper hemisphere of the unit \(S^k\). Its round metric is exactly (JC5), now in \(k\) coordinates:
\[
g=I+\frac{xx^T}{y^2},\qquad d\operatorname{vol}_g=y^{-1}\,dx.
\]
The whole sphere metric decomposes as
\[
g_{\mathrm{whole}}=g+y^2g_{S^b}.
\tag{JC7}
\]
Consequently the volume of the hidden sphere contributes the weight \(y^b\), and the pushed-forward probability measure is
\[
d\nu=Z^{-1}e^{-V}\,d\operatorname{vol}_g,\qquad
V=-b\log y,\qquad Z=\int y^b\,d\operatorname{vol}_g.
\tag{JC8}
\]
For the octonionic specialization, \(\mathcal F=-\log y\), so
\[
\boxed{V=5\mathcal F,\qquad -\log(d\nu/dx)=4\mathcal F+\text{constant}.}
\tag{JC9}
\]
These coefficients differ because their reference volume forms differ. The missing factor is the hemisphere Jacobian, not an inconsistency or an adjustable entropy parameter. \(V\) is a negative logarithmic fiber-volume weight; it is not, by itself, the entropy of a selected state.

The weighted Laplacian is
\[
\boxed{\mathcal L=\Delta_g-\langle\nabla_gV,\nabla_g\,\cdot\,\rangle.}
\tag{JC10}
\]
In coordinates, \(\Delta_g=a^{ij}\partial_i\partial_j-kx\cdot\nabla\) and \(\nabla_gV=bx\). Hence the total drift is \(-(k+b)x=-Nx\), exactly the spherical return. For \(k=3,b=5\), the three-dimensional hemisphere term and the five-dimensional hidden-fiber term together give \(-8x\). These dimensions count state and fiber geometry, not spacetime dimensions.

## A reverse characterization fixes the differential law

One can now recover the local expression without first prescribing the spherical Laplacian. Suppose a conservative second-order differential generator \(\mathcal A\) on the open ball has smooth coefficients, coordinate covariance
\(\Gamma_{\mathcal A}(x_i,x_j)=\delta_{ij}-x_ix_j\), and is symmetric in \(L^2(\nu)\) on compactly supported smooth tests. Its second-order part is then fixed. Symmetry forces
\[
\boxed{\mathcal A
=\frac1w\partial_i\!\left(w a^{ij}\partial_j\right)
=\mathcal L,\qquad w=d\nu/dx.}
\tag{JC10a}
\]
Indeed subtract the displayed symmetric divergence operator. The remainder is a real vector-field derivative \(v\cdot\nabla\); its formal adjoint is \(-v\cdot\nabla-w^{-1}\operatorname{div}(wv)\). Equality with its adjoint forces its first-order coefficient \(v\) to vanish.

This proves uniqueness of the differential expression, not every boundary extension. The inherited sphere realization still fixes that domain. It also identifies exactly what is insufficient: interior stationarity allows \(\mathcal A=\mathcal L+v\cdot\nabla\) with \(\operatorname{div}(wv)=0\), subject to separate boundary and nonexplosion conditions for a global process. For \(k\ge2\), \(v(x)=\Omega x\) with nonzero \(\Omega^T=-\Omega\) preserves this radial law, is tangent to the boundary and commutes with \(\mathcal L\); heat followed by rotation supplies an actual stationary process with local circulation. Covariance and stationary measure do not by themselves force detailed balance.

Matching the generator covariance to the static Jordan covariance chooses a dimensionless process normalization, not physical seconds. In the spherical member, the hidden-drift quotient proves the required local symmetry; the reverse theorem shows that the resulting local drift is then fixed rather than an independent fit.

## Weighted curvature explains the sharp response edge

The unit hemisphere satisfies
\[
\operatorname{Ric}_g=(k-1)g,\qquad
\operatorname{Hess}_g y=-yg.
\]
Differentiating \(V=-b\log y\) gives
\[
\operatorname{Ric}_g+\operatorname{Hess}_gV
=(N-1)g+b\,\frac{dy\otimes dy}{y^2}.
\]
The finite-effective-dimension weighted Ricci tensor is therefore
\[
\boxed{
\operatorname{Ric}_{V,N}
:=
\operatorname{Ric}_g+\operatorname{Hess}_gV
-\frac{dV\otimes dV}{N-k}
=(N-1)g.}
\tag{JC11}
\]
Here \(N-k=b\). The fiber contribution and the correction term cancel exactly. The parameter \(N\) is a weighted comparison dimension, not a proposed extra physical dimension.

For real smooth \(f\), define
\[
\Gamma_2(f)=\frac12\mathcal L\Gamma(f,f)-\Gamma(f,\mathcal Lf).
\]
Bochner's identity and
\[
\frac{(\Delta_gf)^2}{k}
+\frac{\langle\nabla_gV,\nabla_gf\rangle^2}{b}
\ge\frac{(\mathcal Lf)^2}{N}
\]
give the pointwise inequality
\[
\boxed{\Gamma_2(f)\ge(N-1)\Gamma(f,f)+\frac{(\mathcal Lf)^2}{N}.}
\tag{JC12}
\]
This includes both the horizontal Hessian norm and the hidden-fiber term. Keeping only ordinary Ricci curvature would discard part of the same descent geometry.

Use the inherited self-adjoint realization and polynomial core proved in the sphere-to-ball note. Weighted boundary fluxes vanish on this core; in particular \(\Gamma(f,f)\) is again a polynomial. Invariance and integration by parts give
\[
\int\Gamma_2(f)\,d\nu=\int(\mathcal Lf)^2\,d\nu.
\]
Since \(N>1\), integrating (JC12) yields
\[
\int(\mathcal Lf)^2\,d\nu\ge N\int\Gamma(f,f)\,d\nu.
\]
Apply this to the polynomial eigenbasis of the inherited realization. Every nonzero eigenvalue of \(H=-\mathcal L\) is at least \(N\), and the coordinate functions satisfy \(Hx_i=Nx_i\). Thus
\[
\boxed{H\ge N(I-P_1),\qquad \operatorname{gap}H=N=n-1.}
\tag{JC13}
\]
For the qubit ball, \(\operatorname{Ric}_{V,N}=7g\) and the sharp response gap is \(8\). This recovers the spectral result by a geometric mechanism: retained covariance and hidden-fiber weight constrain the same operator.

## Entropy evolution and the matrix readout

For a sufficiently regular positive probability density \(h_t\), bounded away from zero and evolving by \(\partial_t h_t=\mathcal Lh_t\), integration by parts gives
\[
\frac{d}{dt}\operatorname{Ent}_\nu(h_t)
=-\int\frac{\Gamma(h_t,h_t)}{h_t}\,d\nu.
\tag{JC14}
\]
This is decay of relative entropy against the declared equilibrium law. It does not mean that an ontological information inventory has been destroyed. Nor is this entropy the von Neumann entropy of one qubit: \(h_t\) describes an ensemble of Bloch parameters, whereas each \(\rho_x\) is one retained matrix state. The individual qubit bound \(\log2\) does not bound relative entropy on this continuous ensemble carrier.

The [[finite-entropy-cost-and-rank-changing-readout|finite conditional entropy deficit]] separately measures what the initial sphere-to-ball readout forgets. Its Hessian vanishes on already-retained distinctions. In contrast, (JC2) measures variation *among* retained states. These are different forms from the same specified projection and reference geometry, not interchangeable definitions of a residue.

On affine symbols only, the heat evolution has the exact matrix return
\[
e^{t\mathcal L}f_A=f_{\Phi_t(A)},\qquad
\Phi_t(A)=a_0I+e^{-8t}\mathbf a\cdot\sigma.
\tag{JC15}
\]
This is the unital completely positive qubit depolarizing channel. At \(t=\log3/8\), its coefficient is \(1/3\), agreeing with the one-step channel in [[exceptional-state-comparison/peirce-context-averaging-and-the-emergent-qubit-process|Peirce context averaging]]. That equality does not identify their clocks: the earlier unit-rate Poisson and logarithmic interpolations have different generators. The present sphere law also determines higher polynomial modes absent from the finite matrix carrier.

The construction begins with a chosen round geometry and selected complex context. [[primitive-state-diffusion/inq|Primitive overlap refinement]] now constructs the normalized spherical generator from a declared tensor-comparison and iteration law, instead of supplying its differential expression independently. The retained law, covariance and decay structure follow, but their physical selection does not. The limiting whole spherical generator already has gap eight; the projection retains visible modes attaining that gap rather than creating it from a gapless whole. Rescaling the whole generator rescales the response edge. Neither an obtained outcome, a spacetime translation, the interacting Yang–Mills observable algebra nor a physical mass calibration has been constructed.

[[octonionic-hopf-descent-and-the-complex-purification|The Hopf parent]]
relates those sphere data to a larger normalized amplitude carrier: the
quadratic readout excludes its lower linear modes. The
[[partial-trace-clock-consistency-and-the-fluctuation-limit|partial-trace limit]]
then tests whether a normalized response and nonvanishing distinctions
survive together, distinguishing the state ensemble from the quantum
observable carrier.

[[directed-analytic-realization/sphere_ball_descent_receipt.py|The sphere-ball receipt]] checks exact finite covariance, SLD, drift and weighted-curvature identities alongside the projection spectrum and entropy calibrations. [[directed-analytic-realization/sphere-ball-descent-receipt-output.txt|Its output]] records the checked cases; the core and differential arguments above carry the general claims.

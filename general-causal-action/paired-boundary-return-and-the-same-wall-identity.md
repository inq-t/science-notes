# Paired Boundary Return and the Same-Wall Identity

A state-preserving retraction returns its own boundary inclusion exactly, but the return through a different boundary generally contracts. On the actual stationary chronological pair, these cross-boundary maps are \(P\) and \(P^*\), so their return is \(P^*P\) and their loss is the oriented innovation \(I-P^*P\). This remains true when the entire pair algebra is commutative. A separate qubit calculation distinguishes the KMS return of an inclusion from its relative-entropy Hessian: the two use different operator means.

**Status: exact identities for a declared stationary pair and faithful finite matrices.** The chronological carrier and gap criterion are already constructed in [[two-slice-innovation-geometry/oriented-innovation-and-finite-temporal-repair|OI1–5]]. [[channel-loss-and-recovery/preserving-expectation-loss|Preserving-expectation loss]] owns the distinction between a same-wall retraction and forgotten incoming tangents. The result here identifies the two boundary inclusions that make these statements compatible.

## Two inclusions in one stationary pair

Let \(P\) be a Markov kernel on a standard Borel probability space \((X,\pi)\), with invariant probability \(\pi\). Its stationary pair law and commutative algebras are
\[
d\mu(x,y)=\pi(dx)P(x,dy),\qquad
\mathcal N=L^\infty(X,\pi),\qquad
\mathcal M=L^\infty(X\times X,\mu).
\tag{PB1}
\]
Both endpoint marginals are \(\pi\). Define the distinct inclusions
\[
\iota_-f(x,y)=f(x),\qquad
\iota_0f(x,y)=f(y).
\tag{PB2}
\]
Conditional integration defines normal unital positive maps \(E_-,E_0:\mathcal M\to\mathcal N\):
\[
(E_-F)(x)=\mathbb E_\mu[F(X,Y)\mid X=x],\qquad
(E_0F)(y)=\mathbb E_\mu[F(X,Y)\mid Y=y].
\tag{PB3}
\]
Their lifted maps \(\iota_-E_-\) and \(\iota_0E_0\) are ordinary state-preserving conditional expectations onto the respective endpoint subalgebras. They satisfy
\[
\boxed{
E_-\iota_-=E_0\iota_0=I,\qquad
E_-\iota_0=P,\qquad E_0\iota_-=P^*.}
\tag{PB4}
\]
Here \(P^*\) is the adjoint on \(L^2(\pi)\), equivalently the reversed stationary kernel. The last equality follows by integrating \(\overline{f(y)}g(x)\) against \(\mu\). No reversibility assumption is needed.

Thus the same-inclusion returns are identities, while the future-to-past-to-future return is
\[
\boxed{
D_{0\to-\to0}
=E_0\iota_-E_-\iota_0=P^*P.}
\tag{PB5}
\]
This is a state-preserving Markov map and a positive self-adjoint contraction on \(L^2(\pi)\). A single inclusion and its own retraction do not encode the relative position of these two endpoint subalgebras.

## The cross return is the existing physical innovation

Let \(J_-,J_0:L^2(\pi)\to L^2(\mu)\) be the endpoint isometries induced by (PB2), and write \(\Pi_-=J_-J_-^*\). Then
\[
\delta=(I-\Pi_-)J_0,\qquad
(\delta f)(x,y)=f(y)-(Pf)(x),
\]
\[
\boxed{
\delta^*\delta=I-P^*P=I-D_{0\to-\to0}.}
\tag{PB6}
\]
Indeed, \(J_-^*J_0=P\), and \(J_0^*J_-=P^*\). Equivalently,
\[
\|\delta f\|_{L^2(\mu)}^2
=\int\operatorname{Var}_{P(x,\cdot)}(f)\,\pi(dx)
=\|f\|_{L^2(\pi)}^2-\|Pf\|_{L^2(\pi)}^2.
\tag{PB7}
\]
The left side is a loss of a specified future distinction when only its past boundary is retained. It can be nonzero even though both same-inclusion returns in (PB4) are identities.

For the actual reversible supported chronology, take the \(P\) in (PB1) to be the physical slab transfer \(A=P_{\rm RS}^k=e^{-\ell H}\) of OI, with \(\ell=ka_t>0\). Equations (PB5)–(PB6) become
\[
D_{0\to-\to0}=e^{-2\ell H},\qquad
\delta^*\delta=I-e^{-2\ell H}=R_+.
\tag{PB8}
\]
On a nonzero reducing centered physical sector with energy infimum \(\Delta\),
\[
\|D_{0\to-\to0}\|_{\mathscr H_0}=e^{-2\ell\Delta},\qquad
\inf_{\substack{f\in\mathscr H_0\\\|f\|=1}}\|\delta f\|^2
=1-e^{-2\ell\Delta}.
\tag{PB9}
\]
These are consequences of the already selected chronological clock, not a way to determine that clock from an arbitrary probability law. The factor two counts the two chronological returns in (PB5). It does not establish a universal factor-two mass law for a different nested regional channel.

The [[channel-loss-and-recovery/binary-channel-witness|binary channel]] gives the smallest exact control. Let \(\pi(\pm1)=1/2\) and
\[
P_\lambda(x,y)=\frac{1+\lambda xy}{2},\qquad 0<\lambda<1.
\]
For the centered unit source \(f(x)=x\), the same-inclusion returns are \(I\) for every \(\lambda\), whereas
\[
D_{0\to-\to0}f=\lambda^2f,\qquad
\|\delta f\|^2=1-\lambda^2,\qquad
\Delta_\lambda=-\ell^{-1}\log\lambda.
\tag{PB10}
\]
The same commutative endpoint algebras therefore support a positive fixed gap or a gap-closing family, depending on their actual joint law. Trivial modular flow of a commutative algebra does not erase this chronological distinction.

## The relative-entropy Hessian also sees the cross loss

For bounded real centered \(f\), define a nearby joint state by
\[
d\mu_t(x,y)=(1+tf(y))\,d\mu(x,y),\qquad
|t|\,\|f\|_\infty<1.
\]
Its past marginal has density \(1+tPf\) relative to \(\pi\). Expanding \(u\log u\) at \(u=1\) gives
\[
\boxed{
\left.\frac{d^2}{dt^2}\right|_{t=0}
\left[
D(\mu_t\Vert\mu)
-D((\mu_t)_-\Vert\pi)
\right]
=\|f\|^2-\|Pf\|^2
=\|\delta f\|^2.}
\tag{PB11}
\]
Bounded centered functions are dense in the centered \(L^2\) carrier, and the resulting quadratic form is bounded. Thus the same formula extends to that carrier by closure. It is exactly the commutative Fisher/BKM loss of [[channel-loss-and-recovery/bkm-loss-operators|the restriction channel]], evaluated on the prescribed future-source lift.

There is no conflict with the zero minimum-lift result for a preserving expectation. For a prescribed past density \(1+tg(x)\), the recovered joint lift \((1+tg(x))\mu\) has zero loss. In (PB11), the physical source has already selected a different lift, \((1+tf(y))\mu\). Minimizing over all joint lifts would discard this boundary specification.

## The KMS and BKM returns use different means

The finite distinction can be checked without any infinite-dimensional modular calculation. For a faithful density \(\rho\), put
\[
\mathsf S_\rho(B)=\rho^{1/2}B\rho^{1/2},\qquad
\Omega_\rho(B)=\int_0^1\rho^sB\rho^{1-s}\,ds.
\tag{PB12}
\]
The first defines the KMS observable inner product
\(\langle A,B\rangle_{\rm KMS,\rho}=\operatorname{Tr}(A^*\mathsf S_\rho B)\).
The second defines the BKM observable inner product; its inverse defines the BKM density-tangent metric. [[library/conditional-expectations-and-a-theorem-of-takesaki/inq|Accardi–Cecchini]] is the source for the generalized expectation, while [[channel-loss-and-recovery/bkm-loss-operators|the entropy-loss operator]] fixes the BKM adjoint convention.

For a finite inclusion \(\iota:\mathcal N\hookrightarrow\mathcal M\), use compatible matrix traces, the trace adjoint \(\Phi=\iota^\dagger\), and \(\sigma=\Phi\rho>0\). The KMS adjoint of the inclusion and the BKM observable adjoint are respectively
\[
E_{\rm KMS}
=\mathsf S_\sigma^{-1}\Phi\mathsf S_\rho,\qquad
E_{\rm BKM}
=\Omega_\sigma^{-1}\Phi\Omega_\rho.
\tag{PB13}
\]
The KMS map is the finite Heisenberg Accardi–Cecchini/Petz-dual map. The BKM formula specifies a Hilbert-space adjoint; it is not asserted to be a completely positive channel in general. Distinct means cannot be substituted merely because both constructions depend on the same state and inclusion.

Take \(\mathcal M=M_2(\mathbb C)\), \(\mathcal N\) its diagonal algebra, and
\[
\rho=\frac{I+r\sigma_x}{2},\qquad
\sigma=\frac I2,\qquad Z=\sigma_z,\qquad 0<r<1.
\]
Because \(Z\) interchanges the two eigenspaces of \(\rho\),
\[
\mathsf S_\rho(Z)=\frac{\sqrt{1-r^2}}2Z,\qquad
\Omega_\rho(Z)=\frac{r}{2\operatorname{artanh}r}Z.
\]
The first coefficient is the geometric mean of \((1+r)/2\) and \((1-r)/2\); the second is their logarithmic mean. Since both output inverse means multiply by two,
\[
\boxed{
(E_{\rm KMS}\iota)Z=\sqrt{1-r^2}\,Z,\qquad
(E_{\rm BKM}\iota)Z=
\frac{r}{\operatorname{artanh}r}\,Z.}
\tag{PB14}
\]
These are unequal for every \(0<r<1\).

For the actual trace-zero density tangent \(X=Z/2\), direct differentiation of relative entropy gives
\[
g_\rho^{\rm BKM}(X,X)=\frac{\operatorname{artanh}r}{r},
\qquad
g_\sigma^{\rm BKM}(\Phi X,\Phi X)=1.
\]
Consequently the normalized restriction-Hessian loss is
\[
\boxed{
\frac{\ell_\Phi^\rho[X]}{g_\rho^{\rm BKM}(X,X)}
=1-\frac{r}{\operatorname{artanh}r}
=\frac{r^2}{3}+O(r^4),}
\]
\[
1-\lambda_{\rm KMS}
=1-\sqrt{1-r^2}
=\frac{r^2}{2}+O(r^4).
\tag{PB15}
\]
This refutes an unqualified identification of the KMS same-wall defect with the relative-entropy susceptibility. It does not refute either map or their possible comparison under additional hypotheses. The relative-entropy/BKM relationship is the one treated by [[library/monotone-riemannian-metrics-and-relative-entropy/inq|Lesniewski–Ruskai]].

## What the wall comparison changes

The same-wall identity is true for the classical pair algebra. The inference that all its gap-sensitive responses must therefore vanish is false: it changes the two-inclusion composite (PB5) into one of the same-inclusion composites in (PB4). Equation (PB11) identifies the corresponding nonzero susceptibility without introducing a different physical metric.

This does not construct the proper regional quantum algebras or their cyclic and separating vacuum. [[prepared-sources-and-the-modular-wall|The prepared-source modular-wall theorem]] still distinguishes those objects from equal-time multiplication algebras and their unrestricted dynamical completion. A noncommutative nested-wall channel is a separate possible observable, whose carrier, centering and comparison with the complete physical spectrum must be proved.

The useful common structure is a state together with multiple boundary inclusions and their transported comparisons. Non-Abelian group multiplication can enter the joint density while the algebra of functions on its histories remains commutative. In the current programme that structure already contains the selected chronology. Its unresolved task remains the uniform spatial and continuum estimate for the actual cross-boundary return; commutativity of the history algebra neither proves nor excludes that estimate.

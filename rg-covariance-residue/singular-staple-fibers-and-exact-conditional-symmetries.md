# Singular Staple Fibers and Exact Conditional Symmetries

Preserving a Wilson conditional law means preserving its entire matrix source, not just choosing a vector in the source derivative's kernel at one point. At the extremal six-staple source, that kernel has dimension 32 while the exact fiber has only 20 isolated points. Smooth source-preserving motion on the six outer links must therefore stop there. This is an exact obstruction to one proposed commuting escape operator, not an obstruction to motion on the larger path-factor carrier or a physical mass-gap theorem.

## An exposed trace minimum makes the source fiber finite

Use the metric \(g(X,Y)=-\operatorname{ReTr}(XY)/3\), and let
\[
\Sigma:SU(3)^6\longrightarrow M_3(\mathbb C),\qquad
\Sigma(W_1,\ldots,W_6)=\sum_{j=1}^6W_j,\qquad z=e^{2\pi i/3}.
\tag{SR1}
\]
The [[frustrated-su3-conditional-wells|trace-minimum theorem]] says
\(\operatorname{ReTr}W\ge-3/2\), with equality only at \(zI,z^2I\).
Consequently
\[
\boxed{\Sigma^{-1}(-3I)
=\{\text{ordered assignments of three }zI\text{ and three }z^2I\},
\qquad |\Sigma^{-1}(-3I)|=\binom63=20.}
\tag{SR2}
\]
Indeed the sum has real trace \(-9\), so all six summands attain their individual trace minimum. Its imaginary part then forces equal multiplicities. Every continuous path in this fiber is constant.

For a fixed \(V\in SU(3)\), left multiplication by \(V^*\) gives the same statement at source \(-3V\): the staples are three \(zV\)'s and three \(z^2V\)'s. Under endpoint gauge changes \(W_j\mapsto gW_jh^*\), the reference \(V\) transforms the same way. No physical gauge choice is required by this classification.

This is a consequence of an exposed support face, as in [[special-unitary-source-support|special-unitary source support]]. It does not assume that generic source fibers are discrete.

## The derivative kernel is not an integrable freedom

At a point of (SR2), write \(\dot W_j=z^{\epsilon_j}X_j\), with \(X_j\in\mathfrak{su}(3)\), three \(\epsilon_j=1\) and three \(\epsilon_j=2\). Then
\[
D\Sigma(X)=zA+z^2B,\qquad
A=\sum_{\epsilon_j=1}X_j,\quad B=\sum_{\epsilon_j=2}X_j.
\tag{SR3}
\]
Since
\[
zA+z^2B=-\tfrac12(A+B)+\tfrac{i\sqrt3}{2}(A-B),
\]
its anti-Hermitian and Hermitian parts vanish separately exactly when \(A=B=0\). Both sums can be prescribed arbitrarily. Thus, over the real numbers,
\[
\boxed{\operatorname{rank}D\Sigma=16,\qquad
\dim\ker D\Sigma=48-16=32.}
\tag{SR4}
\]
These are first-order stationary source variations, not the tangent space of a positive-dimensional smooth fiber. The constant-rank theorem cannot be invoked from the rank at this singular point alone.

The obstruction already appears at second order. Put
\[
F(W)=\operatorname{ReTr}\Sigma(W)+9\ge0.
\]
For every twice differentiable path through (SR2), with initial velocity \(X\),
\[
F'(0)=0,\qquad F''(0)=\tfrac32\sum_j\|X_j\|_g^2.
\tag{SR5}
\]
The acceleration term drops out because every summand is a critical trace minimum. A nonzero vector in \(\ker D\Sigma\) therefore cannot be continued as a constant-source path by choosing a compensating acceleration.

There is also a quantitative form. For \(Z=\{zI,z^2I\}\), compactness and the nondegenerate minima give a constant \(C<\infty\) such that
\[
\sum_j\operatorname{dist}_g(W_j,Z)^2
\le C\bigl(\operatorname{ReTr}\Sigma(W)+9\bigr).
\tag{SR6}
\]
Near either minimum this follows from its positive Hessian; outside fixed neighborhoods the positive trace deficit has a positive minimum and the distance is bounded. This controls approach to the separate central labels. It is not a bound on the conditional Poincare constant, which instead becomes small in the linked well example.

## Exact commutation fixes the whole source

For fixed \(\beta>0\), define
\[
q_M(U)=Z(M)^{-1}\exp\!\left[\tfrac{\beta}{3}
\operatorname{ReTr}(U^*M)\right].
\]
Let \(X\) be a smooth vector field in retained variables, with coefficients independent of \(U\). Normalized differentiation gives
\[
X\log q_M(U)=\tfrac{\beta}{3}
\left(\operatorname{ReTr}(U^*XM)
-q_M[\operatorname{ReTr}(U^*XM)]\right).
\tag{SR7}
\]
Hence \(Xq_M=0\) if and only if \(XM=0\). To prove the nontrivial direction, the real trace pairing in (SR7) must be constant for all \(U\). Haar averaging makes the constant zero. Evaluating also at \(zU\) makes the complex pairing zero. Matrix-coefficient orthogonality for the defining representation,
\(\int U_{ab}\overline{U_{ij}}\,dU=\delta_{ai}\delta_{bj}/3\),
then gives \(XM=0\).

The [[conditional-fisher-coercivity/lyapunov-localization-certificate#Commuting escape preserves the original innovation|conditional commutator formula]] shows that this is also equivalent to \([X,P_e]=0\) on all smooth tests. At \(\beta=0\) the conditional is Haar and that equivalence with source preservation no longer holds.

Suppose this commutation identity holds on a neighborhood, not only at one point, and \(X\) operates on the six staple variables alone. Its local flow preserves \(\Sigma\). Starting at (SR2), the flow is constant, so
\[
\boxed{X(W)=0\quad\text{for every }W\in\Sigma^{-1}(-3I).}
\tag{SR8}
\]
For a Wilson star with the transverse path factors held fixed, each outer parallel link maps diffeomorphically to its own staple. Thus the same conclusion holds for smooth commuting fields acting only on those six outer links.

If a finite family of such fields defines an actual-law symmetric form
\(\mathcal E_X(f)=\sum_A\|X_Af\|^2\), its generator is
\(L=-\sum_AX_A^*X_A\). At an extremal context all fields vanish, and \(LW=0\) for every smooth positive \(W\). It cannot supply a strictly positive pointwise Lyapunov potential \(-LW/W\) there. Singular mobilities are outside this smooth-field statement.

## What the obstruction leaves available

A path product can remain fixed while its individual factors move. The finite fiber in (SR2) concerns the six path products, not the full retained lattice configuration. It does not rule out compensating transverse-link motions, fields acting outside the active star, controlled noncommuting derivatives, or enlarged-block estimates.

[[second-ring-commuting-escape|Second-ring commuting escape]] supplies an explicit alternative in one actual context: a farther link changes the surrounding action while leaving every active staple unchanged. This identifies the carrier on which the simple operator genuinely acts.

The [[receipts/commuting_context_rigidity_receipt.py|finite receipt]] enumerates the 20 central assignments, checks the derivative rank and second-order obstruction, and tests the alternative's full-lattice geometry. The exact statements follow from the proofs here, not from sampled configurations.

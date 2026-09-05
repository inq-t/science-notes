# SU(2) Staple Elimination and Response

An actual Wilson link can be integrated exactly at any finite coupling. Its external context is an unnormalized quaternion staple sum, not a globally defined preferred group direction. The same integral returns a uniformly coercive conditional law and a geometry-dependent boundary response: coherent staples can moderate sensitivity, while cancelled staples produce a growing negative contribution to the induced Hessian. Conditional stiffness and context sensitivity are different estimates.

**Status: [EXACT FINITE-WILSON IDENTITIES AND CONDITIONAL BOUND]; [OPEN] for iterated weak-coupling coarse control and a physical continuum gap.**

## Use the unnormalized context

Take an ordinary finite Wilson lattice, with no plaquette traversing the active link twice. Orient each complementary three-edge path \(W_p\) from the active link's source to its target so that its plaquette trace is \(\operatorname{ReTr}(U^*W_p)\). For real couplings \(\beta_p\), identify \(SU(2)\) with unit quaternions and set
\[
a(R)=\sum_{p\ni e}\beta_p w_p(R)\in\mathbb R^4,\qquad
\kappa=|a|.
\tag{ST1}
\]
The action convention is \(S=\sum_p\beta_p[1-\operatorname{ReTr}U_p/2]\). Conditional on all other links \(R\),
\[
dq_a(u)=Z(a)^{-1}e^{u\cdot a}\,d\sigma(u),\qquad
Z(a)=\frac{2I_1(\kappa)}{\kappa},\quad Z(0)=1.
\tag{ST2}
\]
The normalized \(S^3\) latitude density and [NIST's integral representation](https://dlmf.nist.gov/10.32.E2) give (ST2). The normalization and character multipliers are already owned by [[bridge-score-fusion-geometry/wilson-bridge-envelopes-under-temporal-blocking|the Wilson convolution calculation]]. [[library/computational-strategies-in-lattice-qcd/inq|Luscher's exact conditional construction]] fixes the complementary-path meaning of the staple.

Quaternion closure is special here: a real weighted sum \(A\) of \(SU(2)\) matrices satisfies \(A^*A=|a|^2I\). When \(a\ne0\), \(a/|a|\) defines a group direction, but this direction is undefined at cancellation. The law, its normalizer and its mean remain smooth there. No singular boundary condition is needed at \(a=0\).

The new [[conditional-fisher-coercivity/linear-tilted-sphere-coercivity|linear-tilted sphere theorem]] gives
\[
\operatorname{Var}_{q_a}F\le\int|\nabla_{S^3}F|^2\,dq_a
\tag{ST3}
\]
for every finite \(a\), with unit round metric. It does not assume weak field or discard unfavorable exterior configurations.

## The complete mean and covariance response

Let \(b(\kappa)=I_2(\kappa)/I_1(\kappa)\), \(n=a/\kappa\). Differentiating the normalized integral gives
\[
m(a):=\mathbb E_{q_a}u=b(\kappa)n,
\]
\[
\boxed{
\mathcal F(a):=\nabla_a^2\log Z(a)
=\operatorname{Cov}_{q_a}(u)
=b'(\kappa)nn^\top+
\frac{b(\kappa)}{\kappa}(I-nn^\top),}
\tag{ST4}
\]
where
\[
b'=1-b^2-\frac{3b}{\kappa}.
\tag{ST5}
\]
At \(a=0\), \(m=0\) and \(\mathcal F=I/4\). The small-field expansions are \(m(a)=a/4+O(|a|^3)\) and \(\log Z=|a|^2/8+O(|a|^4)\).

For a retained tangent \(\xi\), the normalized score is
\[
s_R[\xi]=(u-m)\cdot da[\xi],\qquad
I_R(\xi,\xi)=da[\xi]^\top\mathcal F(a)\,da[\xi].
\tag{ST6}
\]
This is a joint score of the actual conditional law; summing worst-case sensitivities for separate staples may lose its geometry. At large \(\kappa\), its radial and transverse covariance eigenvalues behave respectively as \(3/(2\kappa^2)\) and \(1/\kappa\). At cancellation the covariance is instead \(I/4\).

## Differentiate the induced law, including its curved context map

Integrating the link gives
\[
V_{\mathrm{eff}}(R)=S_{\mathrm{rest}}(R)-\log Z(a(R))
\tag{ST7}
\]
up to a constant. On the product manifold of retained links, the exact covariant Hessian is
\[
\boxed{
\operatorname{Hess}V_{\mathrm{eff}}[\xi,\zeta]
=\operatorname{Hess}S_{\mathrm{rest}}[\xi,\zeta]
-da[\xi]^\top\mathcal F(a)\,da[\zeta]
-m(a)\cdot\operatorname{Hess}a[\xi,\zeta].}
\tag{ST8}
\]
The last term retains nonlinear ordered staple products and inverse edges. It cannot be dropped because the intermediate source \(a\) lives in a vector space. This is the explicit one-link specialization of [[joint-fisher-response-of-normalized-gauge-blocking|conditional covariance subtraction]].

For two staples with equal weight \(\beta\ge0\) and a unit round generator \(T=i\sigma_j\), compare the contribution \(-\log Z\) along two paths:
\[
\begin{array}{lll}
W_1=I,\ W_2=e^{\theta T}:&
\displaystyle\frac{d^2}{d\theta^2}[-\log Z]_{\theta=0}
=\frac{\beta b(2\beta)}2,\\[2mm]
W_1=I,\ W_2=-e^{\theta T}:&
\displaystyle\frac{d^2}{d\theta^2}[-\log Z]_{\theta=0}
=-\frac{\beta^2}{4}.
\end{array}
\tag{ST9}
\]
These vary the trace of the relative holonomy \(W_1^*W_2\), so the distinction is not a common endpoint gauge rotation. They isolate the induced term; other retained plaquettes contribute their own \(S_{\mathrm{rest}}\).

Conversely, a common endpoint rotation of every staple preserves \(|a|\). Along that path the covariance and second-derivative contributions cancel exactly. Counting only the covariance would assign stiffness to a gauge motion that leaves the integrated potential unchanged.

The conditional bound (ST3) therefore does not make the retained potential uniformly convex. At cancellation a boundary variation with \(da=\beta\,dv\) has Fisher cost \(\beta^2|dv|^2/4\), although the conditional law itself is Haar. This is the precise obstruction to inferring a weak-coupling response bound from strong single-link coercivity.

## One independent layer, not a closed Wilson recursion

Let \(H\) be a link set with at most one selected link per plaquette. Assume additional boundary factors depend only on retained variables or contribute linear sources already included in \(a_e\). Conditional independence alone would not suffice for a nonlinear one-link boundary potential. Then exactly
\[
\mu_R(dR)\propto
e^{-S_{\mathrm{rest}}(R)}
\prod_{e\in H}Z(a_e(R))\,dR,\qquad
\mu(dU_H\mid R)=\bigotimes_{e\in H}q_{a_e(R)}.
\tag{ST10}
\]
The hidden gradient bound (ST3) tensorizes with the same constant. Its joint boundary Fisher form is
\[
I_R(\xi,\xi)=
\sum_{e\in H}da_e[\xi]^\top\mathcal F(a_e)\,da_e[\xi].
\tag{ST11}
\]
Together with a proved gap for the **actual** marginal in (ST10), this can enter [[contemporary-puzzles/yang-mills-mass-gap/two-scale-rg-descent-and-the-crossover-lemma|the two-scale conditional-Fisher estimate]]. Neither the marginal gap nor a uniformly small response is supplied by (ST3).

One permitted set selects a fixed orientation \(i\) and bases with \(\sum_{j\ne i}x_j\) even, on an open lattice or compatible even periodic sizes. Selecting every parallel link fails: a plaquette contains two of them. The induced terms are finite-range for this one layer, but couple retained edges absent from a common original plaquette. The opposite original checkerboard is generally no longer independent under the new action.

For a spatial orientation, the full spacetime checkerboard includes time parity and generally is not invariant under the usual link reflection \(t\mapsto1-t\). Reflection positivity transfers only for a reflection-equivariant readout preserving the positive-half observable algebra and an appropriate preparation. [[temporal-column-response/spatial-elimination-and-self-return#The actual whole-column marginal|Whole-column elimination]] is the temporally coherent alternative; its partition functions are not products of one-link Bessel factors.

The retained law preserves all retained observables exactly, not every original observable. Nonzero conditional fluctuations of plaquettes crossing hidden links remain in the discarded sector. [[coarse-response-memory/inq|Hidden dynamical return]] is an additional obligation before a conditional gradient estimate can be read as physical energy.

[[receipts/staple_elimination_receipt.py|The finite receipt]] checks normalization, score covariance, induced Hessian signs, gauge-rotation cancellation, allowed checkerboards and conditional spherical test spaces.

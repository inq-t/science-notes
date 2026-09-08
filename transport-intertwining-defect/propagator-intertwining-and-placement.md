# Propagator Intertwining and Placement

The derivative of an inserted comparison map is the obstruction to intertwining the evolution on its two sides. A product rule gives the resulting terminal-state sensitivity on declared invariant domains. The obstruction transforms covariantly under changes of presentation, and its vanishing makes insertion address irrelevant without making the comparison invertible.

## Carriers and differentiability

Let \(I\) be an interval with parameter \(N\), and take two Banach carriers, with Hilbert spaces as a special case:
\[
X_-\quad\text{before comparison},\qquad X_+\quad\text{after comparison}.
\tag{WD1}
\]
Supply strongly continuous evolution families of bounded operators \(U_\pm(s,t)\), for \(s\geq t\) in \(I\), with the identity and composition laws. Require local uniform boundedness on compact parameter sets. For unbounded generators, fix dense invariant domains
\[
D_-\subset X_-,\qquad D_+\subset X_+,
\tag{WD1a}
\]
such that \(A_\pm(N):D_\pm\to X_\pm\), each propagator preserves its domain, and its fixed-domain orbits obey the strong derivative equations below. Declare the comparison map
\[
J_\sigma:X_-\longrightarrow X_+
\tag{WD2}
\]
with
\[
J\in C^1\!\left(I,\mathcal B(X_-,X_+)\right)
\quad\text{in operator norm},\qquad J_\sigma(D_-)\subseteq D_+.
\tag{WD2a}
\]
The bounded-generator case takes \(D_\pm=X_\pm\). These hypotheses are a supplied evolution package, not an existence theorem for arbitrary unbounded \(A_\pm\).

Fix \(N_i<N_f\) and \(x_i\in D_-\). Inserting the map at \(N_i<\sigma<N_f\) gives
\[
x_f(\sigma)=U_+(N_f,\sigma)J_\sigma U_-(\sigma,N_i)x_i.
\tag{WD3}
\]
The endpoint parameter and incoming state are fixed while \(\sigma\) varies.

## The exact wall-defect identity

Assume, on the respective invariant domains,
\[
\partial_sU_\pm(s,t)=A_\pm(s)U_\pm(s,t),\qquad
\partial_tU_\pm(s,t)=-U_\pm(s,t)A_\pm(t).
\tag{WD4}
\]
Define the transport-intertwining defect, also called the wall-crossing defect when \(J\) is a proposed wall:
\[
\boxed{\mathfrak D_\sigma:=J_\sigma'+J_\sigma A_-(\sigma)-A_+(\sigma)J_\sigma.}
\tag{WD5}
\]
It is initially an operator \(D_-\to X_+\). Differentiating the composite gives
\[
\boxed{\frac{\mathrm d x_f}{\mathrm d\sigma}
=U_+(N_f,\sigma)\mathfrak D_\sigma U_-(\sigma,N_i)x_i.}
\tag{WD6}
\]
Indeed, \(y(\sigma)=J_\sigma U_-(\sigma,N_i)x_i\) is strongly differentiable in \(X_+\), with values in \(D_+\). In the difference quotient for \(U_+(N_f,\sigma)y(\sigma)\), differentiate the propagator on the fixed vector \(y(\sigma)\), and use strong continuity and the local operator bound on the changing-vector term. This avoids treating an unbounded generator as an everywhere bounded matrix.

The three terms are
\[
\begin{array}{rcl}
J_\sigma'&:&\text{change of the comparison map},\\
J_\sigma A_-&:&\text{evolve first, then compare},\\
A_+J_\sigma&:&\text{compare first, then evolve}.
\end{array}
\tag{WD7}
\]
The defect acts on the incoming vector at the insertion point. Its operator type alone supplies neither a positive form nor an energy interpretation.

An integral version requires additional regularity. If the composite is absolutely continuous and the right-hand side of (WD6) is its Bochner-integrable derivative, then for \(a<b\),
\[
x_f(b)-x_f(a)=\int_a^b
U_+(N_f,s)\mathfrak D_sU_-(s,N_i)x_i\,\mathrm ds.
\]
For example, strong continuity of this derivative on \([a,b]\) suffices. The pointwise domain calculation alone does not establish that integration hypothesis.

## The defect is covariant under presentation changes

Let \(S_\pm(N):X_\pm\to\widetilde X_\pm\) be operator-norm \(C^1\) bounded isomorphisms with bounded inverses, carrying \(D_\pm\) onto fixed declared domains \(\widetilde D_\pm\). Present vectors as \(\widetilde x_\pm=S_\pm x_\pm\). Then
\[
\widetilde A_\pm=S_\pm'S_\pm^{-1}+S_\pm A_\pm S_\pm^{-1},\qquad
\widetilde J_\sigma=S_+(\sigma)J_\sigma S_-(\sigma)^{-1}.
\tag{WD7a}
\]
Differentiating the inverse and cancelling the frame-derivative terms gives
\[
\boxed{\widetilde{\mathfrak D}_\sigma
=S_+(\sigma)\mathfrak D_\sigma S_-(\sigma)^{-1}.}
\tag{WD7b}
\]
Thus vanishing is presentation invariant. A norm or singular value requires compatible transport of the source and target metrics as well. Define
\[
[X_-,X_+,J,A_-,A_+]_{\mathrm{pres}}
:=\text{orbit under these }(S_-,S_+).
\tag{WD7c}
\]
This covariance holds for any map satisfying the hypotheses; it does not prove that the map was selected by a physical law. [[transport-intertwining-defect/connection-and-generator-conventions|The induced connection on maps]] gives the equivalent connection notation and its sign convention.

## A zero defect erases placement

If
\[
\mathfrak D_\sigma=0\quad\text{on }D_-
\quad\text{for every relevant }\sigma,
\tag{WD8}
\]
then (WD6) makes \(x_f(\sigma)\) constant on each connected interval of admissible insertion addresses. Any observation factoring only through this terminal vector, with no explicit insertion-address dependence or additional environment record, is equally insensitive. Boundedness of the composite operators and density of \(D_-\) extend the resulting equality of composites to \(X_-\).

This is an insertion-placement result, not an invertibility theorem. With trivial evolution, the constant projection \(J:\mathbb R^2\to\mathbb R\), \(J(x_1,x_2)=x_1\), has zero defect and forgets a whole direction. Conversely, a nonzero defect may be killed by the occupied input, the outgoing propagator or the final readout. [[transport-intertwining-defect/observation-of-a-transport-defect|The observation criterion]] keeps these separate losses of sensitivity explicit.

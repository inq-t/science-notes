# Metric Response of an Intertwining Defect

An intertwining defect is a map between carriers, and generally has no positivity order. A chosen target metric turns its action into a nonnegative source quadratic form. Closability, the resulting kernel and a positive lower bound require a Hilbert-space operator realization; none follows from the formal defect expression alone.

## A target metric gives a pullback

Fix an insertion address in [[transport-intertwining-defect/propagator-intertwining-and-placement|the propagator construction]]. Assume now that \(X_-\) and \(X_+\) are Hilbert spaces with specified norms and \(D_-\) is dense in \(X_-\). Supply a bounded self-adjoint positive operator \(G_+\) on \(X_+\). The initial response is
\[
\mathfrak q_{\mathfrak D}[x]
:=\langle\mathfrak D_\sigma x,G_+\mathfrak D_\sigma x\rangle_{X_+},
\qquad x\in D_-.
\tag{WD11a}
\]
Equivalently, \(\mathfrak q_{\mathfrak D}[x]=\|T_0x\|^2\), where
\[
T_0:=G_+^{1/2}\mathfrak D_\sigma:D_-\longrightarrow X_+.
\]
Its initial kernel is \(\{x\in D_-:\mathfrak D_\sigma x\in\ker G_+\}\). Even a nonzero defect can lie entirely in that metric kernel. Rescaling \(G_+\) rescales the response, so positivity alone chooses no normalization.

The form is closable exactly when \(T_0\) is closable. If this is proved, let \(T=\overline{T_0}\). The closed form is
\[
\overline{\mathfrak q}_{\mathfrak D}[x]=\|Tx\|^2,
\qquad x\in\operatorname{Dom}T,
\]
with associated positive self-adjoint operator \(T^*T\). The domain and kernel in any spectral claim must refer to this realization. Merely knowing a formal expression on a dense core does not establish closability or identify the closed form's domain.

## Closed range is the quantitative condition on the quotient

For any densely defined closed operator \(T:X_-\supseteq\operatorname{Dom}T\to X_+\), bounded operators included, the following are equivalent:
\[
\operatorname{Ran}T\text{ is closed};
\qquad
\exists c>0:\quad
\|Tx\|\geq c\,\operatorname{dist}_{X_-}(x,\ker T)
\quad(x\in\operatorname{Dom}T).
\]
If the range is closed, the inverse of the restricted bijection
\(T:\operatorname{Dom}T\cap(\ker T)^\perp\to\operatorname{Ran}T\)
has a closed graph and is bounded into \(X_-\). Conversely, the estimate makes minimum-kernel representatives of any convergent image sequence Cauchy in \(X_-\); closedness of \(T\) then puts the limit back in its range.

Thus the squared response has a positive floor on the kernel quotient precisely under this closed-range condition. The quotient norm is the specified Hilbert norm, not an arbitrary graph norm in which a lower bound might be automatic. A declared physical null space equals the response kernel only after a separate coverage theorem.

For a family \(T_\sigma\), individual closed ranges need not give a uniform positive \(c\). Even on \(\mathbb R\), \(T_\sigma x=\sigma x\) is invertible for every \(\sigma>0\) but has no positive lower bound uniform as \(\sigma\downarrow0\).

## Covariance does not select the metric or physical carrier

The defect's vanishing is invariant under admissible presentations. Its numerical response is invariant only when the metrics are transported with the maps. A chosen positive \(G_+\) and a closed-range estimate still give a response in the declared source norm. [[measured-response-carriers/closed-form-carrier-transport|Closed-form carrier transport]] supplies conditions for moving that form to another Hilbert carrier; [[measured-response-carriers/response-to-energy-comparison|response-to-energy comparison]] additionally requires physical coverage and an independently normalized energy comparison. The positive pullback itself supplies neither.

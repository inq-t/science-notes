# Response-to-Energy Comparison

A positive response edge becomes a Hamiltonian gap only through a lower frame on a complex physical energy-form core and an independently normalized energy comparison. This theorem isolates that reusable implication; it neither constructs the response carrier nor identifies an auxiliary parameter with physical time.

Let \(q\) be a densely defined closed nonnegative Hermitian form on a complex Hilbert space \(\mathcal K\), with associated operator \(L\ge0\).

Let \(\mathfrak h_{\mathrm{phys}}\) be a densely defined closed nonnegative
form on a physical Hilbert space, with associated self-adjoint Hamiltonian
\(H_{\mathrm{phys}}\) and normalized vacuum \(\Omega\), with \(H_{\mathrm{phys}}\Omega=0\). Let
\(\mathcal K_{\mathrm{phys}}\subset
\operatorname{Dom}(\mathfrak h_{\mathrm{phys}})\cap\Omega^\perp\) be a
complex linear subspace, and let
\(J:\mathcal K_{\mathrm{phys}}\to\operatorname{Dom}(q)\) be complex linear.
Suppose

\[
\|J\psi\|_{\mathcal K}^2
\geq
b_J\|\psi\|_{\mathrm{phys}}^2,
\qquad
b_J>0.
\tag{MC21f}
\]

Assume the response form has an edge on the represented image,

\[
q[J\psi]\geq\kappa\|J\psi\|_{\mathcal K}^2,
\qquad
\kappa>0,
\tag{MC21g}
\]

and that an independently normalized energy comparison gives

\[
\mathfrak h_{\mathrm{phys}}[\psi]
\geq
\eta_{\mathrm{sol}}E_*\,q[J\psi],
\qquad
\eta_{\mathrm{sol}}>0,
\quad E_*>0.
\tag{MC21h}
\]

Then

\[
\boxed{
\mathfrak h_{\mathrm{phys}}[\psi]
\geq
\eta_{\mathrm{sol}}E_*\kappa b_J
\|\psi\|_{\mathrm{phys}}^2.}
\tag{MC21i}
\]

If \(\mathcal K_{\mathrm{phys}}\) is a form core for the restriction of
\(\mathfrak h_{\mathrm{phys}}\) to \(\Omega^\perp\) and
\(\ker H_{\mathrm{phys}}=\mathbb C\Omega\), then

\[
\Delta_E
:=
\inf\sigma\!\left(H_{\mathrm{phys}}\big|_{\Omega^\perp}\right)
\geq
\eta_{\mathrm{sol}}E_*\kappa b_J.
\tag{MC21j}
\]

**Proof.** Chain (MC21h), (MC21g), and (MC21f) on the declared core. Approximate an arbitrary vector of the physical energy-form domain in \(\Omega^\perp\) in its form norm, and pass the resulting energy/norm inequality (MC21i) to the limit. The spectral theorem gives (MC21j). This requires neither surjectivity of \(J\) nor a bounded extension of \(J\) to the whole physical Hilbert space.

The inequality argument also works when a positive Hermitian response form is given only on the represented image. Closedness of \(q\) is needed for its associated response operator \(L\), not for chaining the three inequalities and closing the **physical energy form**. A construction using only such an image form must not claim a self-adjoint response generator without a separate closure theorem.

The image-specific hypothesis (MC21g) matters. A gap for \(L\) only on \((\ker L)^\perp\) does not suffice if \(J\psi\) can lie in its kernel. Either require \(J\mathcal K_{\mathrm{phys}}\subset(\ker L)^\perp\), or replace (MC21f) by the relative frame
\(\operatorname{dist}(J\psi,\ker L)^2\ge b_J\|\psi\|_{\mathrm{phys}}^2\)
and use the corresponding modulo-kernel response inequality.

This implication is exact; its premises contain the physical work. A real BKM Hessian first needs a positive Hermitian extension, and the comparison must hold on a **complex form core of the full physical vacuum complement**, not merely a selected channel. \(E_*\) must be selected without fitting the desired gap. [[hessian-response-geometry/relative-response-spectrum|The response metric pair]] fixes the quotient being bounded; [[inq#Parameter Hessians are pullbacks, not new carriers|a parameter Hessian]] cannot manufacture the missing lower frame.

The operator registers are therefore:

\[
\begin{array}{c|c}
\text{object}&\text{extra datum needed before energy}\\
\hline
\text{BKM or Fisher response}&
\text{complex physical analysis map and Hermitian extension}\\
\text{spatial probability precision}&
\text{configuration-to-energy or OS/kinetic solder}\\
\text{Dirichlet or Markov defect}&
\text{energy comparison or calibrated Euclidean-time realization}\\
\text{positive transfer step}&
\text{injectivity and calibrated duration}\\
\text{Hamiltonian edge}&
\text{Poincare reconstruction before invariant mass}
\end{array}
\tag{MC21k}
\]

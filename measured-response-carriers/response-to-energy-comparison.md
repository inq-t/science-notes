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

This implication is exact; its premises contain the physical work. A real BKM Hessian first needs a positive Hermitian extension, and the comparison must hold on a **complex form core of the full physical vacuum complement**, not merely a selected channel. \(E_*\) must be selected without fitting the desired gap. [[hessian-response-geometry/relative-response-spectrum|The response metric pair]] fixes the quotient being bounded; [[measured-response-carriers/response-pullbacks-and-radicals#Parameter Hessians are pullbacks, not new carriers|a parameter Hessian]] cannot manufacture the missing lower frame.

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

## A reflected comparison needs only a form sandwich

For a fixed-duration route, the physical comparison is bounded. It therefore admits a weaker interface than an exact operator intertwiner between two full carriers.

Let \(\mathscr P_+\) be a complex linear space of positive-time source expressions, including every finite linear combination under consideration. Assume one complete returned law supplies vacuum-centered reflected pairings
\[
K^c(F,G;t)
=\langle Q_\Omega[F],e^{-tH}Q_\Omega[G]\rangle,
\qquad H\ge0,\qquad H\Omega=0.
\tag{RD1}
\]
Their vectors must have dense span in the intended physical vacuum complement. The parameter \(t\) uses the returned length convention and \(H\) has inverse-length units. Write
\[
N(F)=K^c(F,F;0),\qquad
D_\ell(F)=N(F)-K^c(F,F;2\ell),\qquad \ell>0.
\tag{RD2}
\]
Then \(0\le D_\ell(F)\le N(F)\).

The missing response interface can be specified as a positive Hermitian form \(R\) on \(\mathscr P_+\) satisfying
\[
\boxed{
bN(F)\le R(F,F)
\le L^2D_\ell(F)+\eta N(F),
\qquad b>\eta\ge0,\quad L>0.}
\tag{RD3}
\]
This is a **sufficient type contract**, not a construction of \(R\) and not a requirement on every possible proof of a mass gap. The left inequality says that the response detects every physical distinction quantitatively. The right says that the returned chronology detects that response, allowing a controlled quadratic discrepancy. Both statements concern all finite complex linear combinations, including mixed sources.

For any
\[
0<\kappa<\min\left\{1,\frac{b-\eta}{L^2}\right\},
\]
subtracting the error in (RD3) gives \(D_\ell\ge\kappa N\). Density and spectral calculus then give
\[
H\ge-\frac{\log(1-\kappa)}{2\ell}Q_\Omega.
\tag{RD4}
\]
[[positive-semigroup-decay/source-pairing-limit-and-the-mass-gap|The source-pairing theorem]] supplies the same conclusion when the pairings first arise as limits.

The sandwich also settles two interface conditions automatically. Since \(R(F,F)\le(L^2+\eta)N(F)\), Cauchy–Schwarz for the positive form shows that every \(N\)-null source annihilates both arguments of \(R\). Thus \(R\) descends continuously to the completed centered physical quotient. This is a quotient by a null vector subspace, not necessarily an algebra ideal; centering itself makes constants null. No claim that multiplication descends through this quotient is needed.

An optional source-map implementation explains the lower constant. Suppose a positive Hermitian source form \(q_s\) obeys \(q_s(u)\ge c\|Q_su\|^2\), \(c>0\), and a linear comparison map \(J\) takes the dense physical source span into its form domain. Require, for \(a>0\),
\[
\|Q_sJx\|\ge a\|x\|,\qquad
q_s(Jx)\le L^2\|\delta_{\mathrm{phys},\ell}x\|^2
+\eta\|x\|^2,
\tag{RD5}
\]
where \(\delta_{\mathrm{phys},\ell}^*\delta_{\mathrm{phys},\ell}
=I-e^{-2\ell H}\). If \(ca^2>\eta\), then \(R(x,x)=q_s(Jx)\) realizes (RD3) with \(b=ca^2\). A lower bound on the uncentered \(\|Jx\|\) would be insufficient: its norm could reside in the source vacuum. Surjectivity, equality of full carriers and a unitary equivalence across the realization are unnecessary.

The image form \(q_s\) may be unbounded elsewhere; (RD3) bounds its physical pullback. Separate closedness assumptions are needed only if an additional closed source operator or operator extension is claimed. When \(q_s(u)=\|\delta_su\|^2\), an exact factorization \(\delta_sJ=\Lambda\delta_{\mathrm{phys},\ell}\), \(\|\Lambda\|\le L\), is one stronger way to satisfy the upper bound. An amplitude error bounded by \(\varepsilon\|x\|\) instead gives the margin \((\sqrt c\,a-\varepsilon)^2/L^2\), provided \(\varepsilon<\sqrt c\,a\); it must not be confused with the quadratic error \(\eta\) in (RD3).

Along a regulator construction, \(b,\eta,L\) may vary provided one common positive \(\kappa\) survives and the same reflected pairings converge at \(\ell_r\to\ell>0\). The forms \(R_r\), comparison maps and repairs need not converge. Full reconstruction, nontriviality and the Yang–Mills identification remain independent return obligations. [[scale-bearing-descent/yang-mills-return-signature|The Yang–Mills signature]] separates those obligations from this quantitative interface.

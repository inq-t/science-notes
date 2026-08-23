# Referee Disposition and Revision Record

## Causal-Wall Spectral Theory v2.0 → v3.0

**Date:** 22 August 2026  
**Documents reviewed:**

- *Causal-Wall Spectral Theory: A Non-Stochastic Completion of the Scalar Cosmological Sector*, v2.0;
- *Referee Report — Causal-Wall Spectral Theory v2.0*;
- *Causal-Wall Spectral Theory — Completion Memo v2.1*.

**Outcome:** The referee found several genuine weaknesses and supplied useful repairs, but the completion memo sometimes converts plausible programme hypotheses into stronger “theorems” than the present construction supports. Version 3.0 integrates the valid repairs, rejects the overextensions, and adds several corrections that neither referee document noticed.

---

## 1. Executive verdict

The central spectral dictionary in v2.0 is sound once its conventions are fixed:

\[
\Delta_\zeta^2(k)
=\frac{k^3}{16\pi^2\operatorname{Im}B(-k^2-i0)}
=\frac{4}{\pi^4c^{(0)}(k)},
\]

\[
\mathcal K_\zeta(k)
=\frac{k^3}{2\pi^2\Delta_\zeta^2(k)}
=8\operatorname{Im}B(-k^2-i0)
=\frac{\pi^2}{8}c^{(0)}(k)k^3.
\]

The numerical conversions in v2.0 also reproduce.

The central unresolved issue is narrower and more important than the v2.0 prose suggested:

> **Construct the actual causal-wall scale-to-state map and prove that its information-geometric Hessian becomes the continued stress-trace spectral precision with the required normalization.**

That equality is not established merely by observing that a Weyl source inserts the stress trace. It requires a regular quantum source family, a continuation prescription, and a precise factor-of-two convention between a state-space metric and the probability precision derived from a wavefunctional.

Version 3.0 therefore changes the title from **“completion”** to **“formulation.”** The theory has completed a rigorous *retyping* of the scalar target, but not yet a microscopic calculation of the target from the causal-wall algebra.

---

## 2. Finding-by-finding disposition

| Referee finding | Disposition in v3.0 | Reason |
|---|---|---|
| **F1 — BKM/stress-trace weld** | **Accepted in substance; materially corrected** | The exponential-family Hessian lemma is valid, but the actual wall map has not been shown to be such a family. The referee’s abelianization shortcut is not used: the stress-tensor source sector is not automatically a commutative statistical model, and Chentsov uniqueness does not erase the distinction among Euclidean, BKM, Wightman, and spectral kernels in a generic QFT. The contact-term quotient and branch registration are retained. |
| **F2 — fixed-point 0×∞ problem** | **Accepted; resolution rewritten** | At the exact fixed point, the precision operator has a null direction and cannot be inverted before quotienting. The formal divergence of a coordinate covariance is not a prediction of infinite physical lumpiness. The completion memo’s stronger claim that all coupling-weighted observables “go to zero” is not generally established; in the Einstein member, combinations such as \(\epsilon\Delta_\zeta^2\) may remain finite. |
| **F3 — two-invariant economy** | **Accepted** | Until the wall algebra computes \(c^{(0)}(k)\), the framework still contains an unknown function. \(c^{(0)}(k_*)\) and a constant exponent describe one minimal power-law member, not the parameter count of the unfinished theory. |
| **F4 — Planck–ACT tilt difference** | **Partly accepted; proposed inference rejected** | The difference is worth registering, but comparing best-fit \(n_s\) values from different likelihood combinations is not a direct estimator of running. Assigning an ad hoc \(\Delta\ln k\) and inferring \(\alpha_s\sim3\!-
6\times10^{-3}\) is not statistically valid. Version 3.0 instead quotes the ACT DR6 extended-model result \(\alpha_s=0.0062\pm0.0052\), which is consistent with zero. |
| **F5 — tensor slot** | **Accepted with qualification** | The distinction between \(c^{(2)}/c^{(0)}>222.2\) and the per-polarization precision ratio \(2/r>55.6\) is correct and retained. The \(c^{(2)}\) normalization is registered. The Einstein identities are stated as leading semiclassical single-clock relations, not exact identities of the general wall class. No universal general-class result \(n_t=O(\delta^2)\) is claimed. |
| **F6 — higher cumulants** | **Major correction** | Large-capacity factorization is a possible microscopic mechanism, but it does not follow from the numerical size of \(c^{(0)}\). The spin-zero trace response is beta-weighted and is not automatically the central charge controlling all normalized correlators. The proposed universal floor \(1/\sqrt{c^{(0)}}\) and kill \(|f_{\rm NL}|\gtrsim1\) are therefore omitted. |
| **F7 — conservation joint** | **Accepted** | Rank-one descent gives vanishing non-adiabatic pressure; stress conservation then gives superhorizon conservation of \(\zeta\), which supplies the bridge to deterministic transfer at re-entry. |
| **F8 — support from holographic fits** | **Accepted** | Published perturbative-QFT fits support the spectral *typing*, not the constant-exponent power-law member. The logarithmic-running perturbative-QFT form is named as a distinct member. |
| **F9 — convention registration** | **Accepted** | Branch positivity, the tensor normalization, data-combination names, pivot, and vocabulary are frozen explicitly. “Response,” “capacity,” “discernibility,” and “precision” are no longer conflated. |
| **F10 — no intrinsic scale vs running** | **Accepted** | Exact dilation covariance fixes the critical kernel. Running is controlled breaking of that critical member, not a contradiction of the critical theorem. |
| **F11 — block diagonality** | **Corrected** | Quotienting out constants does not by itself imply orthogonality in an arbitrary metric. At a homogeneous and isotropic reference, harmonic/Fourier symmetry makes the \(k=0\) and \(k\neq0\) blocks orthogonal at quadratic order. That is the actual argument. |
| **F12 — age paragraph** | **Accepted** | Retained as an explicitly tagged register remark, not as an empirical claim about cosmic age. |
| **F13 — presentation corrections** | **Accepted and expanded** | The scalar spectrum is typeset unambiguously; “precision” replaces “covariance” at the Weyl-response joint; and an additional normalization correction is made. |
| **F14 — checks passed** | **Accepted** | The reported scalar and tensor numerical conversions reproduce. |
| **F15 — strengths** | **Accepted** | The spectral retyping is the right generalization and connects the programme to an existing 2-point/3-point computational literature. |
| **F16 — one open-problem list** | **Accepted** | The duplicate member-side and wall-side debts are merged into CW–T1 through CW–T4. |

---

## 3. Corrections not identified by the referee

### 3.1 The hidden factor of two

Version 2.0 defined

\[
\mathscr S[\zeta]=D(\omega_\zeta\|\omega_0)
\]

and called its Hessian the cosmological precision. For a regular quantum exponential family, however,

\[
\operatorname{Hess}_0D(\omega_\zeta\|\omega_0)=G^{\rm BKM},
\]

while the trace–trace correlator is \(4B\). The cosmological probability precision is \(8\operatorname{Im}B\), because passing from a wavefunctional to \(|\Psi|^2\) doubles the suppression exponent.

Version 3.0 repairs this by defining the symmetrized divergence

\[
\mathscr J[\zeta]
=D(\omega_\zeta\|\omega_0)+D(\omega_0\|\omega_\zeta),
\]

so that

\[
\operatorname{Hess}_0\mathscr J=2G^{\rm BKM}.
\]

After spectral continuation, the standard BKM trace kernel contributes \(4\rho_B\), and the symmetric Hessian contributes precisely

\[
8\rho_B=\mathcal K_\zeta.
\]

Equivalently, one may retain one-sided relative entropy and define cosmological precision as twice its Hessian. The v3.0 convention makes the factor explicit instead of hiding it.

### 3.2 Higher derivatives of relative entropy are not cosmological cumulants

The v2.0 chain

\[
K_3\leftrightarrow\text{bispectrum},
\qquad
K_4\leftrightarrow\text{trispectrum}
\]

was too quick. Beyond quadratic order one must distinguish:

1. source derivatives of \(\log Z\), which generate connected stress correlators;
2. derivatives of relative entropy, which are Bregman combinations and have different numerical coefficients;
3. vertices of the probability effective action, whose inverse-kernel contractions generate connected \(\zeta\) correlators.

At tree level,

\[
\langle\zeta_1\zeta_2\zeta_3\rangle_c
=-C_1C_2C_3\,\Gamma_3(1,2,3)+\cdots,
\]

not simply “the third Hessian coefficient.” Holographically, \(\Gamma_3\) is built from the continued \(\langle TTT\rangle\) response plus semilocal terms. Version 3.0 makes this distinction explicit.

### 3.3 \(P_3\) is the critical shape, not a nonzero trace operator at the fixed point

The earlier presentation placed two statements too close together:

- exact conformal symmetry gives the \(|k|^3\) critical shape;
- at an exact CFT, the stress trace vanishes.

The resolution is

\[
\mathcal K_\zeta\simeq C(k)P_3,
\qquad
C(k)=\frac{\pi^2}{8}c^{(0)}(k),
\]

with \(C(k)\to0\) at the fixed point. \(P_3\) fixes the normalized *shape* of a near-critical response; it does not imply a nonzero spin-zero trace response at the fixed point.

### 3.4 The curved \(P_3\) completion needs filling data

Flat-space homogeneity, isotropy, weight zero, positivity, and dilation covariance force \(|k|^3\). On a curved conformal manifold, the fractional GJMS operator is the canonical scattering-theoretic completion once an appropriate Poincaré–Einstein/conformal filling is supplied. Flat symmetry alone does not prove a unique curved nonlocal operator on every conformal manifold without that global datum.

### 3.5 \(c^{(0)}\) is not automatically a central charge

In the McFadden spectral representation, \(c^{(0)}\) is the spin-zero spectral density of the trace response. Near a fixed point it is beta-function weighted and tends to zero. It must not be identified without further proof with a fixed-point central charge or used to infer a microscopic rank \(N\sim\sqrt{c^{(0)}}\). The spin-two density \(c^{(2)}\), or a properly normalized \(c_T\), is the more natural capacity-like datum.

---

## 4. Main architectural changes in v3.0

1. **Title demotion:** “completion” → “formulation.”
2. **Claim registers:** established, conditional, programme hypothesis, open slot.
3. **Exact Fourier normalization:** precision is fixed first from \(P_\zeta\) and \(\Delta_\zeta^2\).
4. **Symmetrized relative entropy:** repairs the factor of two and aligns BKM geometry with probability precision.
5. **Conditional source-family theorem:** the causal-wall map must still be constructed.
6. **Spectral discontinuity:** contact terms are quotiented by \(\operatorname{Disc}\), with branch positivity registered.
7. **Fixed-point quotient:** no inversion of a null operator.
8. **Power-law member separated from general typing:** \(\alpha_s=0\) belongs to the member; no unsupported \(\delta^2\) bound.
9. **Tensor claims scoped:** exact spectral ratios, leading Einstein relations, open general tensor slot.
10. **Higher-point sector rebuilt:** wavefunctional vertices and semilocal terms replace the naive \(K_3\leftrightarrow B_\zeta\) shorthand.
11. **Rank-one conservation bridge added.**
12. **Scope-indexed falsification table:** failures are assigned to the critical member, power-law member, rank-one member, microscopic QFT, Einstein member, or causal-wall weld.
13. **One open list:** CW–T1 through CW–T4.

---

## 5. Final assessment

The referee report was valuable because it found the right pressure points: the BKM/stress-trace joint, the exact-CFT limit, the economy claim, the conservation bridge, and the distinction between spectral typing and a particular holographic member.

Its completion memo should not be adopted verbatim. Four of its strongest claims outrun the evidence:

- that abelianization makes all relevant correlators coincide;
- that \(c^{(0)}\) itself establishes a large-\(N\) capacity and a \(1/\sqrt{c^{(0)}}\) non-Gaussianity floor;
- that the Planck–ACT best-fit difference can be converted directly into a running estimate;
- that a general near-critical wall class universally predicts \(n_t=O(\delta^2)\) or is killed by \(|f_{\rm NL}|\gtrsim1\).

The revised result is more modest but stronger:

> **The scalar cosmological target is exactly a positive spectral precision problem. The holographic dictionary and critical \(P_3\) shape are established. The causal-wall theory becomes a physical model only when it constructs the source family and computes the spectral functions rather than importing them from the sky.**

That is a mathematically economical stopping point, and it identifies a finite theorem programme rather than a fictitious perturbing substance.

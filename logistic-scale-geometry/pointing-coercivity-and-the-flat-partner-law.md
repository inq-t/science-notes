# Pointing Coercivity and the Flat-Partner Law

The normalized core dual action equips a logistic scale state with a gradient form of sharp Poincare edge \(\nu^2\). A homogeneous Darboux partner and one normalizable ordered zero mode select that profile, but leave its width free until an additional capacity or readout law is declared. This note isolates the core-state realization, the heavy-tail obstruction and the local entropy comparison; the physical mass implication requires the separate [[logistic-scale-geometry/scale-wall-to-casimir-comparison|scale-wall-to-Casimir comparison]].

**Status: [EXACT — SCALE-SHADOW THEOREM AFTER THE DECLARED DERIVATION]; [ASSUMPTION — HOMOGENEOUS-PARTNER LAW]; [CONSTRUCTION AXIOM — OPTIONAL CAPACITY/READOUT AND INCOMING-DENSITY SOLDERS]; [CONDITIONAL THEOREM — WALL--CASIMIR]; [OPEN CONSTRUCTION — YANG--MILLS REALIZATION].** The operator below acts on functions of logarithmic spectral scale. It is not a Hamiltonian, modular generator, spacetime Laplacian, gluon mass operator, or Poincare Casimir.

## The carrier is the commutative scale shadow

Let \(X\) be the logarithmic affiliated coordinate in [[wall-construction-interface/core-spectral-wall|the core spectral wall]], normalized by

$$
\tau(f(X))
=
\int_{\mathbb R}e^x f(x)\,\mathrm dx,
\qquad
\frac{\mathrm d}{\mathrm dN}\log\tau(e_N)=1.
$$

For the core density

$$
d_{\nu,N_c}
=
e^{-X}q_{\nu,N_c}(X),
\qquad
q_{\nu,N_c}(x)
=
\frac{\nu}{2}\operatorname{sech}^2\!\bigl(\nu(x-N_c)\bigr),
$$

restriction of the normal state \(\Omega_d\) to the abelian algebra \(\mathcal D_X:=W^*(X)\) gives

$$
\Omega_d(f(X))
=
\int_{\mathbb R}f(x)q_{\nu,N_c}(x)\,\mathrm dx.
$$

Thus its GNS carrier is

$$
\mathcal H_{\mathrm{sc}}
:=
L^2(\mathbb R,\mu_{\nu,N_c}),
\qquad
\mathrm d\mu_{\nu,N_c}=q_{\nu,N_c}\,\mathrm dN.
$$

This is a commutative spectral image of one state on the core. It is neither the type-III local algebra nor the physical Yang--Mills vacuum representation.

## Exact scale-shadow gap

The measure alone does not canonically select a Dirichlet form. Here the normalized core dual action supplies the derivation

$$
\delta_{\mathrm{sc}}f(X)
:=
\left.\frac{\mathrm d}{\mathrm ds}\beta_s(f(X))\right|_{s=0}
=-f'(X).
$$

Its sign disappears after squaring, while its normalization is fixed by \(\mathrm d\log\tau(e_N)/\mathrm dN=1\). Close the resulting gradient form

$$
\mathcal E_{\nu,N_c}[f]
:=
\int_{\mathbb R}|f'(N)|^2\,\mathrm d\mu_{\nu,N_c}(N)
$$

from smooth compactly supported functions together with constants. Its nonnegative generator is

$$
L_{\nu,N_c}f
=
-q_{\nu,N_c}^{-1}
\frac{\mathrm d}{\mathrm dN}
\left(q_{\nu,N_c}\frac{\mathrm df}{\mathrm dN}\right)
=
-f''+2\nu\tanh\!\bigl(\nu(N-N_c)\bigr)f'.
$$

The [[binary-information-geometry/witten-darboux#Scale, address, and the sharp weighted gap|scaled Witten--Darboux theorem]] identifies multiplication by \(\sqrt q\) as a unitary ground-state transform and gives

$$
\boxed{\sigma(L_{\nu,N_c})=\{0\}\cup[\nu^2,\infty),
\qquad
\mathcal E_{\nu,N_c}[f]\geq\nu^2\operatorname{Var}_{\mu_{\nu,N_c}}(f).}
\tag{PC1}
$$

The zero mode is constant on the probability carrier, and the positive spectrum begins continuously. The state address \(N_c\) does not change the edge. The inverse width \(\nu\) is a dimensionless rate per normalized logarithmic scale, not a physical clock rate or mass.

## Why the logistic is no longer merely a convenient profile

The [[binary-information-geometry/witten-darboux#Flat-partner uniqueness|flat-partner uniqueness theorem]] assumes a real smooth first-order factor \(A_W=\partial_N+W\) on the whole line, a homogeneous partner on the stated self-adjoint closures,

$$
A_WA_W^\dagger=-\partial_N^2+\lambda,
\qquad \lambda\in\mathbb R,
\tag{PC2}
$$

and a nonzero normalizable zero mode of \(A_W\). It proves \(\lambda=\nu^2>0\) and uniquely gives

$$
W(N)=\nu\tanh\!\bigl(\nu(N-N_c)\bigr),
\qquad |\psi_0|^2=q_{\nu,N_c}.
\tag{PC3}
$$

The homogeneous-partner law selects the logistic shape rather than merely accepting it as a convenient state. The positive magnitude \(\nu\) and translation address remain free, and the law itself remains a proposed construction axiom. [[logistic-scale-geometry/indexed-scale-wall-and-the-causal-grain|The indexed wall]] makes the ordered orientation precise: with domain \(H^1(\mathbb R)\), the displayed factor has index \(+1\); reversing its kink interchanges the ordered partners and gives \(-1\). This integer does not fix the width or supply physical clock evolution.

## Pointing is not sufficient; exponential tail confinement is the hinge

The core theorem that every normal state breaks exact scale covariance does not by itself imply (PC1). For \(p>1/2\), the heavy-tailed probability density

$$
q_p(N)
\propto
(1+N^2)^{-p}
$$

also defines a normalizable pointing. Its half-density score \(W_p=-\partial_N\log\sqrt{q_p}\) is

$$
W_p(N)=\frac{pN}{1+N^2},
$$

and its ground-state transform has potential

$$
W_p^2-W_p'
=
\frac{p(p+1)N^2-p}{(1+N^2)^2}
\longrightarrow0.
$$

Consequently its essential spectrum reaches zero and the ordinary gradient form has no positive Poincare gap. This agrees with the generalized-Cauchy analysis in [[library/a-note-on-spectral-gap-and-weighted-poincare-inequalities-for-some-one-dimensional-diffusions/inq|Bonnefont, Joulin, and Ma]]: weighting can restore coercivity, but normalizability alone cannot.

The exact distinction is therefore

$$
\boxed{
\text{normalizable pointing}
\not\Longrightarrow
\text{coercivity};
\qquad
\text{homogeneous partner plus a normalizable }A_W\text{-zero mode}
\Longrightarrow
\text{sharp scale coercivity}.}
\tag{PC4}
$$

The causal content proposed for \(\nu>0\) is **two-sided exponential tail confinement in logarithmic scale**: moving indefinitely away from the state address retains a nonzero asymptotic half-density-score cost. That is a property of distinctions across scale, not a pixelation of scale. “Exponential tightness” is deliberately avoided here because it is a different technical property of families of probability measures.

## The local entropy Hessian sees the same constant

Let \(f\) be bounded, real, and locally absolutely continuous, with \(\int f\,\mathrm d\mu=0\) and \(f'\in L^2(\mu)\). For \(|\varepsilon|<\|f\|_\infty^{-1}\), let

$$
\mathrm d\mu_\varepsilon
=
(1+\varepsilon f)\,\mathrm d\mu.
$$

Use the relative Fisher convention

$$
I(\mu_\varepsilon\Vert\mu)
:=
\int_{\mathbb R}
\left|
\partial_N\log(1+\varepsilon f)
\right|^2
(1+\varepsilon f)\,\mathrm d\mu.
$$

Define the two local quadratic forms by

$$
g_D(f,f)
:=
\left.
\frac{\mathrm d^2}{\mathrm d\varepsilon^2}
D(\mu_\varepsilon\Vert\mu)
\right|_{\varepsilon=0}
=
\int f^2\,\mathrm d\mu,
$$

and

$$
g_I(f,f)
:=
\left.
\frac12\frac{\mathrm d^2}{\mathrm d\varepsilon^2}
I(\mu_\varepsilon\Vert\mu)
\right|_{\varepsilon=0}
=
\int|f'|^2\,\mathrm d\mu.
$$

Equation (PC1), for every \(f\) in the closed weighted gradient-form domain, is therefore the Hessian inequality

$$
\boxed{
g_I
\geq
\nu^2g_D}
\tag{PC5}
$$

with this explicit half-Fisher-Hessian convention. Entropy supplies the norm of an infinitesimal distinction; the gradient form supplies its scale variation; the lower bound says that no centered scale distinction is arbitrarily cheap. It does not identify entropy with energy.

## What switches on at \(\nu=0\)

For every \(\nu>0\), the family has both a normalized state and the lower edge \(\nu^2\). As \(\nu\downarrow0\),

$$
q_{\nu,N_c}(N)\,\mathrm dN
$$

loses tightness on \(\mathbb R\): probability escapes every bounded scale interval. At \(\nu=0\), the flat partner is the free Laplacian, the zero-mode candidate is constant and nonnormalizable, and the lower edge reaches zero. Thus, within the flat-partner family,

$$
\boxed{
\text{unpointed weight-like limit}
\xleftarrow{\ \nu\downarrow0\ }
\text{normal pointed state with a scale gap}.}
\tag{PC6}
$$

This is an exact model of “pointing and gap engage together.” It is not a discrete transition: \(\nu\) varies continuously. Conditional on the homogeneous-partner law, normalizable pointing already excludes \(\nu=0\); a causal grain would still have to fix or quantize the positive magnitude, or make the passage between \(\nu=0\) and \(\nu>0\) a noninvertible carrier change. The Witten factorization does none of those things by itself.

## The binary normalization fork and a boundary selection

[[wall-construction-interface/scale-character-solder#Extending the solder: the binary normalization fork|The scale-character solder]] owns the full comparison. Its essential warning is that the binary family has two natural parameters once the generator is typed:

$$
\alpha
:=
\log\frac{Z}{1-Z}
=2\nu(N-N_c)
\quad\text{for }P_+\in\{0,1\},
\qquad
\theta
:=
\frac12\alpha
=\nu(N-N_c)
\quad\text{for }Q=2P_+-\mathbf1\in\{-1,+1\}.
\tag{PC7}
$$

The core capacity difference is \(\zeta_{\mathrm{cap}}=N-N_c\). Requiring the proposed capacity-to-readout comparison to intertwine the identity action gives \(\nu=1/2\) if it maps the core projection to the projection-coded generator \(P_+\), but \(\nu=1\) if it maps to the normalized involution \(Q\). Both consequences are exact after their respective construction axioms. Thus strict equivariance is not enough by itself; the operator on which the additive parameter acts must be specified. The projection branch is algebraically type-matched to the core projection \(e_N\), but the physical comparison map remains unconstructed.

Within the logistic family, the separate incoming-density axiom

$$
\boxed{
0<\lim_{N\to-\infty}
e^{-N}q_{\nu,N_c}(N)<\infty
\quad\Longleftrightarrow\quad
\nu=\frac12,
\quad
\lambda=\frac14}
\tag{PC7a}
$$

selects the projection-branch value: the normal-state density is then neither erased nor amplified relative to canonical core trace capacity at the incoming ideal boundary. It does not by itself select \(P_+\) as the physical readout generator. This condition is a proposed construction axiom, not a consequence of core normality. The mismatch exponent \(\varepsilon_{\mathrm{in}}=2\nu-1\) divides the logistic family into divergent, finite-nonzero, and vanishing incoming core-density classes; \(\nu=1/2\) is their exact rate-matching wall, although crossing it need not be a discrete event. At the selected value, \(q_{1/2,N_c}=Z'=Z(1-Z)=G^{\mathrm{bin}}_{NN}\) as coordinate coefficients in normalized \(N\). It is not an identity of geometric types: \(q\,\mathrm dN\) is a probability measure, whereas \(G^{\mathrm{bin}}_{NN}\,\mathrm dN^2\) is a metric. Nor are the boundary condition and coefficient equality independent evidence; within this family both merely restate \(\nu=1/2\).

## Physical comparison

[[logistic-scale-geometry/scale-wall-to-casimir-comparison|The scale-wall-to-Casimir comparison]] separates the exact conditional-expectation construction of the OS interface carrier from the open geometric analysis map into the mean-zero scale form domain. If that map has a uniform lower frame bound \(b>0\) and the physical Casimir dominates its scale form with independently normalized coefficient \(\eta E_*^2>0\), then the physical Hamiltonian obeys \(H\geq E_*\nu\sqrt{\eta b}(1-P_0)\). The statement requires the reconstructed positive-energy Poincare carrier, the declared form domains and a uniform positive limiting product.

The [[logistic-scale-geometry/resolvent-logistic-scale-transform|resolvent transform]] supplies exact coverage once an interface operator is given. Its log-Haar codomain retains a different center for every spectral channel, whereas the comparison uses a fixed-center weighted probability carrier. Identifying those carriers without losing the centers, selecting the operator geometrically and proving the physical form comparison remain separate requirements. The comparison note also states the local-QFT recovery and continuum obligations.

## Construction boundary

The exact return is the scale-shadow form after its derivation is declared, together with the profile selection implied by a homogeneous partner and a normalizable ordered zero mode. A fundamental interpretation still owes the partner law and a physically selected capacity-to-readout comparison. The separate [[logistic-scale-geometry/scale-wall-to-casimir-comparison|physical comparison theorem]] then requires a geometric interface operator, an information-preserving carrier map, a Casimir comparison, an independent energy yardstick and a nontrivial continuum limit. A causal-grain interpretation must explain those maps and the nonzero tail cost; it does not identify the wall with a smallest spacetime interval.

[[logistic-scale-geometry/receipts/scale_pointing_gap_receipt.py|The scale-pointing receipt]] checks normalization, the Riccati and Darboux identities, the weighted-to-flat ground-state transform, the projection/involution parameter fork, the incoming-density identities, approach to the continuum threshold, the local entropy/Fisher Hessian expansion, and the heavy-tail contrast. It does not test either construction axiom, the operator-domain proof, the carrier map, or Yang--Mills.

## Sources

[[library/supersymmetry-and-quantum-mechanics/inq|Cooper, Khare, and Sukhatme]] give the standard supersymmetric factorization, shape-invariant \(\tanh\) superpotential, and reflectionless partner construction. [[library/a-note-on-spectral-gap-and-weighted-poincare-inequalities-for-some-one-dimensional-diffusions/inq|Bonnefont, Joulin, and Ma]] state the spectral-gap/weighted-Poincare equivalence for one-dimensional diffusions and exhibit the no-gap ordinary gradient form for generalized Cauchy measures. The scaled logistic identities and flat-partner uniqueness used here are proved directly in [[binary-information-geometry/witten-darboux]].

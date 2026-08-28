---
inq.module: "entropic-gravity"
inq.include:
  - "**/*.md"
---
# Entropic Gravity

Entropic gravity is not one theory but a family of attempts to make gravitational dynamics derivative of thermodynamic or information-theoretic structure. Jacobson conditionally obtains Einstein dynamics from universal local equilibrium; Verlinde reconstructs known force laws from holographic screen assignments and later proposes a de Sitter entropy-displacement response. The former is a strong theorem-shaped universality argument with unproved microscopic premises; the latter is conceptually fertile but remains an incomplete and empirically mixed constitutive programme.

The first step is to refuse the name’s false unity. [[lineages-and-scope]] distinguishes a particle entropic force,

$$
F=T\nabla S,
$$

from a local-horizon Clausius law,

$$
\delta Q=T\,\delta S,
$$

from fixed-volume total-entropy stationarity,

$$
\delta S_{\mathrm{tot}}|_V=0,
$$

and from a de Sitter elastic bound,

$$
\int_{\mathcal B}\varepsilon^2\,dV\leq V_M(\mathcal B).
$$

Those equations concern different objects. Most confusions in this literature begin by sliding between them.

## Einstein dynamics as thermodynamic universality

[[jacobson-local-horizon-thermodynamics]] begins at an arbitrary point and imposes one equilibrium principle for every local Rindler horizon and null direction. With Unruh temperature, universal entropy per area, matter boost energy as heat, and stress conservation, Raychaudhuri focusing forces

$$
G_{ab}+\Lambda g_{ab}
=8\pi G T_{ab}.
$$

The result does not say that a particle is pulled by entropy. It says that Einstein’s equation is the unique local equation of state compatible with the stipulated horizon thermodynamics. The area coefficient fixes \(G\), while \(\Lambda\) remains an integration constant.

The argument becomes more revealing when it fails naïvely. [[jacobson-non-equilibrium-thermodynamics]] shows that curvature-dependent entropy density cannot generally remain in the same equilibrium category. An internal production term is required, and a specific entropy-balance law yields metric \(f(R)\) dynamics. The episode is a model of good theoretical discipline: changing the entropy functional changes the type of thermodynamics.

[[jacobson-vacuum-entanglement]] develops the vacuum-entanglement interpretation already suggested in 1995 and asks whether gravity itself regulates the ultraviolet divergence. Vacuum entanglement across the causal boundary is a plausible carrier, but the regulator and universal finite density are not calculated. [[jacobson-entanglement-equilibrium]] develops a different and more controlled small-ball statement: for conformal matter, first-order total-entropy stationarity at fixed volume is equivalent, under the stated area assumption, to the semiclassical Einstein equation. After the area coefficient is identified with \(1/(4\hbar G)\), that total entropy has the Bekenstein generalized-entropy form. Its generic nonconformal and finite-variation extensions remain conditional.

The Jacobson lineage is therefore not a completed quantum gravity, but it is more than analogy. It identifies a sparse universality class of state–horizon relations whose local geometric consequence is Einstein dynamics.

## Gravity as an entropic force

[[verlinde-entropic-force]] starts from a different picture: emergent space, information-bearing screens, and a normal entropy gradient for matter. The assignments

$$
\Delta S
=2\pi k_B\frac{mc}{\hbar}\Delta x,
\qquad
k_BT=\frac{\hbar a}{2\pi c},
\qquad
F\Delta x=T\Delta S
$$

give \(F=ma\). Area-proportional screen degrees of freedom and equipartition then give the inverse-square force, while the general-screen and static relativistic versions reproduce Poisson and Komar–Einstein forms.

The algebra is exact, but its direction of explanation is limited. The bit-density normalization already contains \(G\); the factor \(2\pi\) is matched to Unruh temperature; and the Newtonian potential defines the screen foliation used to reconstruct its own force law. The paper offers a coherent thermodynamic representation and a proposed ontology, not an independently specified microphysics.

## De Sitter entropy displacement

[[verlinde-emergent-gravity]] is not merely the same screen argument with dark energy added. It proposes that de Sitter entropy is long-range entanglement distributed through bulk volume, that localized matter removes part of it, and that the residual medium responds elastically.

Its controlled general statement is an inequality. Saturating the principal-strain bound—equivalently, taking the transverse principal strains to be equal—and neglecting the exterior strain-energy tail produces an approximate bulk equality. Translating that equality into gravitational variables further requires a gradient displacement and an aligned equipotential boundary. Only after adding four dimensions, isolation, equilibrium, and approximate spherical symmetry does one obtain

$$
\int_0^r
\frac{GM_D^2(r')}{r'^2}\,dr'
=\frac{a_0}{6}M_B(r)r.
$$

For a point mass this gives \(g_D^2=(a_0/6)g_B\), the baryonic Tully–Fisher scaling. The paper presents it as an estimate, not a MOND field equation. It supplies no general covariant dynamics, native lensing equation, cosmological perturbations, or structure-formation history.

[[vendor/entropic-gravity/empirical-status]] therefore evaluates what has actually been tested: the restricted effective mass relation and later phenomenological implementations, often embedded in GR and \(\Lambda\)CDM interfaces which the theory itself does not provide. Galaxy scaling is genuinely suggestive, and some implementation-specific dwarf and lensing comparisons are favorable; finite-disc residuals, the direct Solar-System test, galaxy-type dependence, and cluster profiles leave a mixed record. [[covariant-completions]] separates Verlinde’s original proposal from later vector-field theories, whose added couplings and stability problems are not consequences of one unique completion.

## What is worth taking from the vendor

The commentary is deliberately downstream from the exposition. [[vendor/entropic-gravity/commentary/standard-physics-audit|The standard-physics audit]] records reconstruction loops, coefficient matching, conservative-force integrability, the inequality-to-equality step, and the incomplete empirical interface. [[vendor/entropic-gravity/commentary/translation-into-causal-charge|The causal-charge translation]] identifies real rhymes with our work while refusing false identities. [[vendor/entropic-gravity/commentary/methodological-lessons|The methodological lessons]] extract a reusable audit for later vendored theories.

The deepest rhyme is not “gravity is entropy.” It is this:

> a universal relation among state response, causal boundary, and flux can constrain the form of geometry.

Jacobson demonstrates that principle locally after the entropy-area density is granted. Verlinde makes vivid the stronger possibility that localization has a geometric price paid by the arena itself. Neither supplies the proposed conserved causal charge, the BKM–area soldering, or the structure of factive descent.

The most fruitful import is therefore a theorem target. Construct a state-side causal capacity independently of \(G\); show that it defines one universal, cut-local areal density; solder the same tangent to gravitational response; and only then ask whether a common charge or balance law survives the descent into facthood. [[vendor/entropic-gravity/sources/entry|The local source archive]] makes every upstream step available for that comparison.

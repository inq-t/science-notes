# The Scale Torsor and the Global--Local Gap Invariant

A scale-free whole should not be modeled as possessing no scales at all. The precise replacement is a family of locally calibrated presentations over a positive scale torsor, with no preferred section. The invariant carried between those presentations is not a numerical mass but a dimensionless transfer or quadratic-form class. A local scale section turns that invariant into a length, clock rate, energy, and finally Poincare mass. This makes the Copernican reversal exact enough to test while preserving the Clay theorem as the required downstream return value.

**Status: [EXACT] for the torsor covariance and spectral consequences under the stated hypotheses; [CONDITIONAL] for the global--local reconstruction schema; [OPEN] for the upstream Yang--Mills carrier, scale selector, uniform coercivity, and continuum reconstruction.**

## “No scale” has two inequivalent meanings

Let \(\mathcal S\) be a principal \(\mathbb R_{>0}\)-torsor. Its points are possible calibrations, and

$$
(\lambda,s)\longmapsto \lambda s
\tag{S1}
$$

is free and transitive. There is no canonical origin or unit in \(\mathcal S\), but ratios of two points are defined. This is the appropriate type for **no preferred scale**.

It must be distinguished from **no intrinsic physical scale**. A conformal theory may have the latter property. A massive theory can lack a preferred numerical unit while still possessing invariant dimensionless ratios and a nonzero element of an inverse-length quantity line. Changing metres to centimetres changes its numerical representative, not the theory.

[[conformal-scale-geometry/causal-order-and-metric-scale|Causal order and metric scale]] gives the corresponding spacetime statement: causal order determines a conformal class under its hypotheses, while a positive scale section selects a metric representative. It does not select that section.

## What “invariant yardstick” must mean

Three distinct questions sit behind the word invariant:

- Does the number survive a change of measurement units?
- Does it survive a coordinate change on its mathematical carrier?
- Is it unchanged under the physical frame transformations of the theory?

The quotient \(v/c\) passes the first test but generally not the third: different inertial observers assign different velocities to the same massive trajectory. A Poincare mass ratio passes the third when both masses are scalars of the reconstructed representation. A bare dimensionless Hessian eigenvalue can fail the second; [[hessian-response-geometry/relative-response-spectrum|the relative-response spectrum]] shows why both the response and its reference metric must be transported.

The role of \(c\) is particularly instructive. It relates length and duration, but the simultaneous calibration change \(\ell\mapsto a\ell,\ t\mapsto at\) leaves \(\ell/t\) unchanged. It therefore cannot select either scale by itself. The current SI metre likewise uses both \(c\) and a separately specified atomic clock ([BIPM, metre definition](https://www.bipm.org/en/si-base-units/metre)). This metrological fact is not a proof that every conceivable length comparison requires light signals. Geometrically, the stronger relevant statement remains that causal cones do not choose a conformal scale section.

For a Yang--Mills prediction the target is correspondingly a relation

$$
\frac{m_{\mathrm{gap}}c^2}{E_*}=C_{\mathrm{gap}},
\tag{S1a}
$$

where the upstream geometry must determine the normalized coefficient and independently construct or select the reference energy \(E_*\). A lower-bound theorem returns \(\geq\underline C>0\), not equality with the lightest glueball mass. Identifying a particular glueball also requires the appropriate gauge-invariant channel and spectral support; an all-channel gap theorem is a different result.

An integer such as \(3\) or \(8\) can constrain \(C_{\mathrm{gap}}\) through representation geometry or a proved response spectrum. It cannot be inserted as that coefficient merely because it occurs in the carrier's dimension. Likewise, \(G\), a horizon temperature, and a cosmological rate are admissible **candidate calibration data**, but their relevance must be established by a comparison law rather than by their ability to repair units.

## A scale-equivariant family

Suppose every \(s\in\mathcal S\) gives a pointed Hilbert presentation

$$
(\mathcal H_s,\Omega_s,K_s,\mathfrak A_s),
\tag{S2}
$$

where \(K_s\geq0\) is a self-adjoint inverse-length Euclidean generator, \(\|\Omega_s\|=1\), and \(\ker K_s=\mathbb C\Omega_s\). Write \(P_{0,s}=|\Omega_s\rangle\langle\Omega_s|\). The uniqueness assumption makes the single-vacuum complement and full zero-spectral complement agree. Suppose scale transport is implemented by unitaries \(U_{\lambda,s}:\mathcal H_s\to\mathcal H_{\lambda s}\) satisfying the cocycle law and

$$
U_{\lambda,s}\Omega_s=\Omega_{\lambda s},
\qquad
K_{\lambda s}U_{\lambda,s}
=\lambda^{-1}U_{\lambda,s}K_s.
\tag{S3}
$$

For matched lengths \(\ell_{\lambda s}=\lambda\ell_s\), the dimensionless transfer is natural:

$$
U_{\lambda,s}e^{-\ell_sK_s}U_{\lambda,s}^*
=e^{-\ell_{\lambda s}K_{\lambda s}}.
\tag{S4}
$$

Consequently the dimensionless form

$$
\widehat{\mathfrak h}_s[\psi]
:=\ell_s\|K_s^{1/2}\psi\|^2,
\qquad \psi\in D(K_s^{1/2}),
\tag{S5}
$$

and its vacuum-complement floor

$$
\boxed{
\widehat\Delta
:=
\inf_{\substack{\psi\in D(K_s^{1/2}),\ \psi\perp\Omega_s\\\|\psi\|=1}}
\ell_s\|K_s^{1/2}\psi\|^2}
\tag{S6}
$$

are independent of the chosen presentation. Equation (S6), or equivalently the matched-slab attenuation

$$
-\log\|e^{-\ell_sK_s}(I-P_{0,s})\|,
\tag{S7}
$$

is a candidate invariant between the “globaled” and “localed” registers. The global object can carry its natural equivalence class without carrying one preferred numerical ruler.

After a physical clock and Osterwalder--Schrader or direct Hamiltonian reconstruction have been proved,

$$
H_s=\hbar cK_s,
\qquad
\Delta_{E,s}=\frac{\hbar c}{\ell_s}\widehat\Delta.
\tag{S8}
$$

Only after a positive-energy Poincare representation is reconstructed may the same lower edge be called a mass gap. The factors \(c\) and \(\hbar\) convert registers; they do not create (S6).

A section may itself be selected by a [[the-grain-of-causal-scale/relational-grain-construction|matched-ledger construction]], but there is no reason for two different carriers to select the same member. The cosmological common-count length is therefore a model of the method, not a default Yang--Mills input. A Yang--Mills yardstick must be reconstructed from ledgers natural to its own whole-law carrier, or derived with both theories from one proved common upstream object.

## Why the family matters

If one nonzero positive operator on one fixed Hilbert space obeys exact unitary dilation covariance under all positive rescalings, its spectrum is scale invariant and cannot have a positive isolated lower edge. The apparent escape in (S2)--(S4) is not a trick: scaling compares different calibrated members rather than acting as a symmetry of one already pointed physical member. [[mass-as-casimir-and-realization]] proves the same-carrier no-gap lemma and distinguishes this family covariance from a fixed-member symmetry.

Therefore a nonzero physical scale must enter through at least one additional structure:

- a scale anomaly or renormalization-group invariant such as \(\Lambda_{\mathrm{YM}}\);
- a state, boundary, or wall that selects a member of the family;
- a change of carrier or operator domain whose admissible sector is not dilation invariant; or
- an independent global--local comparison producing a preferred quantity line.

The statement “the whole has no scale, but the part does” is incomplete until one of these arrows is constructed.

## The conditional Copernican theorem

Let \(\mathfrak d_s\) be a nonnegative dimensionless response form on a linear domain \(\mathcal D_s\) in an upstream carrier \(\mathcal W_s\). Suppose this family has declared scale transport compatible with the physical transport. Let \(H_s\geq0\) be the reconstructed energy generator with closed energy form \(\mathfrak h_s[\psi]=\|H_s^{1/2}\psi\|^2\). Construct an injective linear map

$$
J_s:\mathcal D_s\longrightarrow
D(H_s^{1/2})\cap\Omega_s^\perp
$$

whose image is a **form core** for the energy form on the complete physical nonvacuum carrier. Upstream gauge-null directions have already been quotiented. Normalize the response against the pulled-back physical norm,

$$
g_s[\xi]:=\|J_s\xi\|^2.
$$

If, uniformly through volume and regulator removal,

$$
\mathfrak d_s[\xi]\geq
\kappa g_s[\xi]
\quad(\xi\in\mathcal D_s),
\qquad
\mathfrak h_s[J_s\xi]\geq
\eta E_s\mathfrak d_s[\xi],
\tag{S9}
$$

with \(\kappa,\eta>0\), fixed normalization, and an independently selected energy unit \(E_s>0\) satisfying \(E_{\lambda s}=\lambda^{-1}E_s\) in the presentation family (with \(\hbar,c\) held fixed), then

$$
\frac{\Delta_{E,s}}{E_s}\geq\eta\kappa>0.
\tag{S10}
$$

Indeed, (S9) implies \(\mathfrak h_s[J_s\xi]\geq\eta E_s\kappa\|J_s\xi\|^2\). The form-core assumption extends this inequality to the full energy-form domain, and the spectral variational principle gives (S10). Mere Hilbert-space density is not a substitute for the form-core hypothesis.

The normalization is essential. On a one-dimensional nonvacuum carrier take \(H=\varepsilon I\), \(\mathfrak d[\xi]=|\xi|^2\), and \(J=\varepsilon^{-1/2}I\), with \(\eta=E=1\) and \(0<\varepsilon<1\). Then \(J\) is onto and \(\mathfrak h[J\xi]=\mathfrak d[\xi]\), but the physical gap is \(\varepsilon\), not the unit floor of \(\mathfrak d\) in the upstream norm. The correct reference is \(g[\xi]=\varepsilon^{-1}|\xi|^2\), giving the relative edge \(\kappa=\varepsilon\). More generally a bound against the upstream norm incurs a factor \(\|J\|^{-2}\) when \(J\) is bounded; without norm control it gives no stated physical constant.

The ratio in (S10) is the invariant; \(E_s\) is the local presentation of the yardstick. This is the conditional content available in the thought that mass is a rate of factification. The response and comparison map must be constructed independently of the target spectral edge, and the energy comparison must not define \(\mathfrak d_s[\xi]:=\mathfrak h_s[J_s\xi]/E_s\) after the fact. The reference metric specifies the denominator of the problem; it does not prove the lower response bound.

## A causal patch is not an ordinary resonant box

If the only confinement scale is a causal-diamond radius \(R\), an ordinary box mode gives

$$
K_R\sim\frac{1}{R},
\tag{S11}
$$

which vanishes as \(R\to\infty\). That cannot prove the Clay gap on \(\mathbb R^4\). A causal-patch construction remains viable only if its boundary or descent law yields a coercive invariant uniform under enlargement of the patch, and if an atlas of such patches reconstructs locality, Poincare covariance, and the same infinite-volume vacuum representation. [[causal-patch-boundary-and-two-times]] states those recovery conditions.

Thus “confinement” in the proposed wave picture cannot merely mean a finite spatial cavity. It must mean an admissibility, gluing, or closed-range condition on the global carrier that continues to exclude arbitrarily soft physical distinctions after the apparent box has been removed.

## The fresh problem

The new question is not “which constant should multiply a guessed mass operator?” It is:

$$
\boxed{
\begin{gathered}
\text{Construct one scale-equivariant whole whose local presentations}\\
\text{recover pure Yang--Mills and whose natural dimensionless response}\\
\text{has a uniform positive floor on the complete vacuum complement.}
\end{gathered}}
\tag{S12}
$$

This abandons pre-given metric scale as an explanatory primitive. It does not abandon the continuum, locality, unitarity, or Poincare symmetry that must reappear as properties of the local physical presentation. “The whole is not unitary” is best typed as: *unitarity is not yet a predicate of the upstream object*. It becomes meaningful only after a Hilbert carrier and a reversible clock action have been reconstructed.

[[global-local-response-reconstruction/inq|Global--Local Response Reconstruction]] packages this torsor statement with the concrete two-boundary response operator and the QFT recovery contract.

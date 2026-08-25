# Localized Areal Response Geometry

Localized areal response geometry asks whether a transported positive state-response form can be represented by a countably additive bilinear measure on a causal cut and compared with an independently normalized area measure. Its primary object is the measure-valued form; the local modulus, cut average, and proposed universal scalar are different contractions. Existence, covariance, continuum finiteness, absolute continuity, and compatibility with central evaluation are open constructions.

## Inputs and ordering policy

This note begins with a causal cut \(\Sigma\), a transported physical tangent \(H^{\mathrm p}_\Sigma\), and a positive response supplied by [[program-core/common-response-form|the common response form]]. The algebra, state, transport, physical quotient, and tangent normalization must already be declared; a rescaling \(v\mapsto av\) rescales every quadratic response by \(a^2\).

For a nontrivial center, [[program-core/center-valued-response|the center-valued owner]] supplies

$$
\mathfrak G^Z
=
(Z,\mathbf G^Z,\omega^Z).
$$

A declared scalar policy \(\mathsf p\) gives a numerical form \(G^{\mathsf p}\). The normal whole-state policy gives, on the homogeneous scale tangent,

$$
G^\perp_{NN}
:=\omega^Z(\mathbf G^{Z,\perp}_{NN})\geq0,
$$

whereas a normalized sector metric or character evaluation is a different input.

There are then two possible construction orders:

$$
\mathbf G^Z
\xrightarrow{\ \mathsf p\ }
G^{\mathsf p}
\xrightarrow{\ \mathrm{Loc}^{\mathsf p}\ }
\mu^{\mathrm{desc},\mathsf p},
$$

or a stronger center-linear localization

$$
\mathbf G^Z
\xrightarrow{\ \mathrm{Loc}^Z\ }
\boldsymbol\mu^{\mathrm{desc},Z}
\xrightarrow{\ \mathsf p\ }
\mu^{\mathrm{desc},\mathsf p}.
$$

The two orders agree only if the localization is center-linear and compatible with the chosen evaluation. This note does not assume that commutation by notation.

## Localization is an additional theorem target

Fix a scalar policy \(\mathsf p\) and suppress it on the measure symbol. For physical horizontal tangents \(v,w\), the **[OPEN CONSTRUCTION]** is a symmetric bilinear map into finite signed measures on measurable patches \(U\subseteq\Sigma\),

$$
\mu^{\mathrm{desc}}_{v,w}(U),
$$

whose diagonal \(\mu^{\mathrm{desc}}_{v,v}\) is positive and countably additive. Localization must recover the supplied global response:

$$
\boxed{
\mu^{\mathrm{desc}}_{v,w}(\Sigma)
=G^{\mathsf p}(v,w).}
$$

Cross measures may equivalently be obtained by polarization,

$$
\mu^{\mathrm{desc}}_{v,w}
=\frac14\left(
\mu^{\mathrm{desc}}_{v+w,v+w}
-\mu^{\mathrm{desc}}_{v-w,v-w}
\right),
$$

provided a measure-level Cauchy--Schwarz bound makes them finite. The form should be local or controlledly quasilocal, covariant under presentation arrows, finite after a declared renormalization, and compatible with restriction to subregions.

Let \(\mu_A\) be an independently normalized causal-area measure and set

$$
A_\Sigma:=\mu_A(\Sigma).
$$

Require every diagonal measure to satisfy

$$
\mu^{\mathrm{desc}}_{v,v}\ll\mu_A.
$$

With the polarization and Cauchy--Schwarz hypotheses, the cross measures are then absolutely continuous as well. Equivalently, one may posit an absolutely continuous matrix-valued measure from the outset. The Radon--Nikodym derivative defines the **areal descent modulus**

$$
\boxed{
\boldsymbol\chi_{\Sigma,\omega}(v,w;p)
:=
\frac{\mathrm d\mu^{\mathrm{desc}}_{v,w}}
{\mathrm d\mu_A}(p),\qquad p\in\Sigma.}
$$

For \(v=w\), it is nonnegative almost everywhere. In a smooth finite-rank realization with dimensionless normalized tangent coordinates, its components form an \(L^{-2}\)-valued symmetric bilinear form on the physical horizontal tangent bundle. In a singular groupoid or stack it may instead belong to a tangent complex or stratified family; the scalar notation does not prejudge regularity.

## Local density, cut average, and universal scalar

Three objects must not share one symbol:

1. the local contraction

   $$
   \chi_N(p):=\boldsymbol\chi(v_N,v_N;p);
   $$

2. the cut average

   $$
   \overline\chi_{\Sigma,N}
   :=\frac{\mu^{\mathrm{desc}}_{v_N,v_N}(\Sigma)}
   {A_\Sigma};
   $$

3. a universal Einstein-class scalar \(\chi_*\), if the local density is shown to be constant throughout a declared class.

The first can vary over a cut, the second can hide that variation, and the third is a strong universality statement. Extensive scaling on one cosmological horizon proves neither locality nor universality.

The historical scalar notation is retained only as an alias for the cut average:

$$
\boxed{
\chi_\downarrow[\Sigma,N]
:=\frac{G^\perp_{NN}(N)}{A_\Sigma}
=\overline\chi_{\Sigma,N}.}
$$

It must not be substituted for the local field \(\chi_N(p)\) without a homogeneity theorem.

The inverse on a nondegenerate sector is **causal compliance**:

$$
\mathfrak a_N(p):=\chi_N(p)^{-1},
\qquad
[\mathfrak a_N]=L^2.
$$

It is area per unit natural-log distinguishability curvature. It is not automatically an area atom, minimal pixel, or spectrum eigenvalue.

## Why the primary object is tensorial

Contracting the tangent bilinear form to one number or one preferred direction at the outset would erase its directional structure. The local bilinear form allows:

- different homogeneous and observational response blocks;
- anisotropic eigenvalues;
- null or constrained directions;
- state-, species-, curvature-, or scale-dependent response; and
- mixing terms between sectors.

Einstein universality would be the special case in which the relevant state-to-geometry identification makes this form proportional to one gravitational form with one constant coefficient. A modified return value is therefore informative rather than a definitional failure.

## Relation to the common response form

If [[program-core/common-response-form|the common response form]] contains homogeneous, observational, mixed, and hidden blocks, a successful localization may return the corresponding matrix of measures or Radon--Nikodym densities. Every scalar block must use one declared evaluation policy, or else the localized blocks are not contractions of one form. The construction must also prove that evaluation and localization commute or retain the center-valued measure until evaluation.

Localization does not perform a Fourier covariance-to-precision map. A three-dimensional spectral precision changes carrier and measure and belongs to CWST's W2 consumer; it is not the localized observational block merely because both are quadratic. A spatial kernel normalized per volume can have units \(L^{-3}\), whereas \(\boldsymbol\chi\) has units \(L^{-2}\). An integration, boundary map, or soldering theorem must account for the mismatch.

A normalized one-channel response shape likewise cannot fix the areal measure, its extensive normalization, or the number of channels per area. [[causal-scale-theory/response-family-interface|The CST response-family interface]] owns member shapes, [[causal-scale-theory/open-questions/extensive-channel-normalization|the extensive-factor problem]] owns the missing multiplicity, and [[deriving-value-of-g/obstructions-to-an-unconditional-proof|the capacity no-go results]] explain why replication defeats a derivation from normalized algebra alone.

## Response does not form facts

The BKM form compares neighboring states; it does not select an outcome or prove that a lost distinction has become geometry. [[program-core/response-registers|The response register]] owns the distinction among state response, areal modulus, spatial precision, and gravitational response. [[program-core/operation-registers|The operation register]] separately types quotient, readout, factual selection, and record extension, while [[program-core/ontological-registers|the ontological register]] keeps state, fact, and record distinct. Localization and continuum completion remain open here; fact formation remains open in the factive branch.

## Failure conditions

- If the input blocks do not live on one transported physical tangent, there is no common form to localize.
- If no positive countably additive diagonal measure recovers the global response, localization fails.
- If the response measure is not absolutely continuous with respect to the independently normalized area measure, the displayed areal modulus does not exist; a singular decomposition may be required instead.
- If area normalization imports the gravitational coefficient being explained, the modulus comparison is circular.
- If central evaluation and localization are silently interchanged without center-linearity, the scalar density is ambiguous.
- If a localized response is called spatial precision, gravitational response, or a fact without the corresponding consumer map, the failure is one of typing rather than calculation.

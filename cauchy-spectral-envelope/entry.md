# Heat Mixtures and Cauchy Spectral Envelopes

A normalized mixture of Gaussian heat suppressions over an exponential distribution of heat scales is exactly a Cauchy-shaped spectral multiplier, hence a positive resolvent of a self-adjoint generator. *Lorentzian* here names only the Cauchy line shape, not spacetime signature; the canonical module name therefore uses *Cauchy*. This identity is a useful analytic component for spectral transfer, but it neither produces Lorentzian spacetime nor implements factual descent: its multiplier has no kernel, and its inverse is ordinarily unbounded rather than nonexistent. A Gamma family extends the construction and can yield a conditional three-dimensional \(|k|^{-3}\) covariance asymptotic only after the spatial carrier, generator, covariance interpretation, physical quotient, and normalization have been constructed independently.

## The meaning

Suppose a mode of spectral size \(E\) is attenuated at a fixed resolution scale \(s\) by

$$
e^{-s^2E^2}.
$$

If the scale itself is unresolved, an observer may see an average of these Gaussian attenuations rather than one Gaussian. One particular law for the unresolved scale converts the exponential tail in \(E^2\) into a rational tail. The mathematical content is stronger and cleaner when stated without premature ontology:

$$
\boxed{
\text{exponential mixing in heat time}
\Longleftrightarrow
\text{a resolvent spectral multiplier}.}
$$

This gives a rigorous sense in which unresolved scale can make reconstruction ill-conditioned. High spectral modes remain present but are strongly attenuated, so arbitrarily small observational error can become arbitrarily large when one attempts to invert the envelope. That is an operational resolution limit. It is not yet a proof that the attenuated distinctions cease to exist, because the map is injective and has dense range.

The starting source is [Sigtermans' non-peer-reviewed TEQ preprint](https://doi.org/10.20944/preprints202506.0446.v2). Its Gaussian-mixture calculation is correct after normalization. The present note extracts that calculation, places it in functional calculus, and audits the larger claims made around it.

## The exact scalar identity

Fix \(m>0\), corresponding to the source's \(E_0\), and put the normalized Rayleigh density

$$
p_m(s)=2m^2s e^{-m^2s^2},
\qquad s\geq0.
$$

Normalization follows from

$$
\int_0^\infty 2m^2s e^{-m^2s^2}\,\mathrm ds=1.
$$

Then, for real \(E\),

$$
\begin{aligned}
K_m(E)
&=\int_0^\infty e^{-s^2E^2}p_m(s)\,\mathrm ds\\
&=\int_0^\infty
e^{-uE^2}m^2e^{-m^2u}\,\mathrm du
\qquad (u=s^2)\\
&=\frac{m^2}{E^2+m^2}.
\end{aligned}
$$

Thus the Rayleigh law in the scale \(s\) is simply an exponential law in the heat parameter \(u=s^2\). The body of the source preprint first writes \(s e^{-m^2s^2}\) and calls it normalized. That statement is false; the appendix correctly restores the factor \(2m^2\).

The normalized multiplier

$$
\frac{m^2}{E^2+m^2}
=\frac{1}{1+(E/m)^2}
$$

is commonly called a Lorentzian line shape and is, after rescaling, the density shape of a Cauchy distribution. The phrase **Cauchy spectral envelope** is preferable here because it prevents a consequential homonym.

## The operator theorem

Let \(\mathcal H\) be a complex Hilbert space and let

$$
A:\mathcal D(A)\subseteq\mathcal H\longrightarrow\mathcal H
$$

be densely defined and self-adjoint. Then \(A^2\) is nonnegative and self-adjoint, and \(e^{-uA^2}\) is a strongly continuous contraction semigroup. Define the strong operator integral, equivalently the vector-valued Bochner integral after applying it to each \(x\in\mathcal H\),

$$
T_m
:=\int_0^\infty
e^{-uA^2}m^2e^{-m^2u}\,\mathrm du.
$$

Because the scalar weight is nonnegative and integrates to one, this is a bounded operator. The spectral theorem gives the **[EXACT HEAT--RESOLVENT IDENTITY]**

$$
\boxed{
T_m
=m^2(A^2+m^2I)^{-1}.}
$$

Equivalently,

$$
T_m
=\int_0^\infty
e^{-s^2A^2}2m^2s e^{-m^2s^2}\,\mathrm ds.
$$

For the spectral measure \(P_A\) of \(A\), the proof is pointwise:

$$
T_m
=\int_{\mathbb R}
\left[
\int_0^\infty
e^{-u\lambda^2}m^2e^{-m^2u}\,\mathrm du
\right]\mathrm dP_A(\lambda)
=\int_{\mathbb R}
\frac{m^2}{\lambda^2+m^2}\,\mathrm dP_A(\lambda).
$$

Consequently:

- \(T_m\) is positive, self-adjoint, and \(0\leq T_m\leq I\) in quadratic-form order;
- \(\ker T_m=\{0\}\), because its scalar multiplier is strictly positive at every finite spectral value;
- \(\operatorname{Ran}T_m=\mathcal D(A^2)\), regarded as a dense subspace of \(\mathcal H\); and
- on that range,

$$
T_m^{-1}=I+m^{-2}A^2,
\qquad
\mathcal D(T_m^{-1})=\mathcal D(A^2).
$$

If \(A\) is unbounded, \(T_m^{-1}\) is unbounded, \(T_m\) is not onto \(\mathcal H\), and its range is not closed. If \(A\) is bounded, however, \(T_m\) has a bounded inverse. The correct conclusion is therefore not categorical "noninvertibility," but an inverse problem whose severity depends on the spectrum and the chosen operator category.

## Terminology firewall: two unrelated Lorentzians

The multiplier

$$
L_m(E)=\frac{m^2}{E^2+m^2}
$$

is called Lorentzian because of its line shape. A Lorentzian spacetime instead carries an indefinite metric of signature \((-+++)\) or \((+---)\), causal cones, and hyperbolic propagation. No implication runs from one meaning to the other.

The heat operator \(e^{-uA^2}\) is parabolic or Euclidean spectral data. Its parameter \(u\) is heat time, not automatically physical time, modular time, cosmological scale, or record order. Likewise, a positive resolvent does not choose retarded, advanced, Feynman, or in-in boundary conditions. Any Lorentzian realization still requires a state, causal prescription, hyperbolic operator, and the spacetime realization demanded by [[algebra/real-forms-and-factive-spacetime|real forms and factive spacetime]].

## What is universal, and what was selected

For any probability measure \(\nu\) on \([0,\infty)\), a Gaussian heat mixture has the form

$$
F(E^2)
=\int_0^\infty e^{-uE^2}\,\mathrm d\nu(u).
$$

It is completely monotone as a function of \(x=E^2\):

$$
(-1)^nF^{(n)}(x)
=\int_0^\infty u^ne^{-ux}\,\mathrm d\nu(u)
\geq0.
$$

Bernstein's representation theorem gives the converse under its regularity hypotheses: completely monotone functions are precisely Laplace transforms of positive measures. The universal conclusion is therefore a **class** of completely monotone spectral envelopes. The Cauchy member is selected by the exponential heat-time density

$$
\mathrm d\nu(u)=m^2e^{-m^2u}\,\mathrm du.
$$

Variation of entropy curvature or unresolved resolution scales does not by itself select that law. A derivation of the Lorentzian specifically must derive the exponential law, not merely posit fluctuating widths. Alternative mixing measures yield other completely monotone envelopes.

The maximum-entropy justification in the source also requires repair. Relative to Lebesgue measure \(\mathrm ds\) on \([0,\infty)\), maximizing differential entropy with fixed \(\mathbb E[s^2]\) gives a half-normal density proportional to \(e^{-\lambda s^2}\), not a Rayleigh density proportional to \(s e^{-\lambda s^2}\). The Rayleigh law follows as the radius of an isotropic two-dimensional Gaussian, or as a maximum-entropy law relative to the radial base measure \(s\,\mathrm ds\). The base measure or the two-dimensional isotropic fluctuation model is additional structure and must be stated.

There is a further sign obligation upstream. With the conventional oscillatory weight \(e^{iS_{\mathrm{eff}}/\hbar}\), the source's displayed

$$
S_{\mathrm{eff}}
=\int(L-i\hbar\beta g)\,\mathrm dt
$$

produces \(e^{+\beta\int g\,\mathrm dt}\), while the next displayed formula uses suppression \(e^{-\beta\int g\,\mathrm dt}\). The sign of the imaginary term or the path-weight convention must be changed before the TEQ path-integral narrative entails the Gaussian starting point. This does not affect the independent heat-mixture identity.

## Gamma mixtures and fractional resolvents

The exponential law is the first member of a normalized Gamma family. For \(\alpha>0\), define

$$
p_{\alpha,m}(s)
=\frac{2m^{2\alpha}}{\Gamma(\alpha)}
s^{2\alpha-1}e^{-m^2s^2},
\qquad s\geq0.
$$

Under \(u=s^2\), this becomes the Gamma density

$$
\frac{m^{2\alpha}}{\Gamma(\alpha)}
u^{\alpha-1}e^{-m^2u}\,\mathrm du.
$$

Functional calculus then gives the **[EXACT GAMMA-MIXTURE IDENTITY]**

$$
\boxed{
T_{\alpha,m}
:=\int_0^\infty
e^{-s^2A^2}p_{\alpha,m}(s)\,\mathrm ds
=\left(\frac{m^2}{A^2+m^2I}\right)^\alpha.}
$$

This is again a positive, self-adjoint, injective contraction. For integer \(\alpha\) it is a power of a resolvent; for noninteger \(\alpha\) it is defined unambiguously by the spectral theorem.

If \(2\alpha=d\), the scale density contains the radial factor \(s^{d-1}\). This is the radial law induced by an isotropic Gaussian in \(d\) auxiliary resolution dimensions. It is a mathematically natural family, but the dimension of that auxiliary mixing space must not be silently identified with the dimension of observable space.

## The conditional three-dimensional critical asymptotic

Assume, rather than derive, all of the following:

1. a translation-invariant three-dimensional spatial carrier has already been constructed;
2. \(A=\sqrt{-\Delta}\) is the positive self-adjoint generator on a declared physical subspace;
3. a dimensionally normalized multiple of \(T_{\alpha,m}\) is interpreted as a covariance multiplier rather than merely a filter;
4. covariance and probability-1PI precision are inverse operators on that subspace; and
5. regulators, zero modes, dimensions, and normalization have been fixed.

For \(d=3\), hence \(\alpha=3/2\), the normalized Fourier envelope is

$$
T_{3/2,m}(k)
=\frac{m^3}{(k^2+m^2)^{3/2}}.
$$

This multiplier is dimensionless. A covariance for a dimensionless field in the repository's Fourier convention must instead have units \(L^3\). Up to an independently fixed dimensionless amplitude \(a>0\), the dimensionally typed covariance candidate is therefore

$$
P_m(k)
:=a\,m^{-3}T_{3/2,m}(k)
=\frac{a}{(k^2+m^2)^{3/2}}.
$$

At \(|k|\gg m\),

$$
P_m(k)
\sim a|k|^{-3},
\qquad
P_m(k)^{-1}
\sim a^{-1}|k|^3.
$$

This conditionally reproduces the covariance and precision **shapes** classified by [[critical-scale-kernels/flat-weight-zero-precision|the flat weight-zero theorem]]. It does not derive their amplitude, their field, or the three-dimensional carrier. The finite scale \(m\) also breaks exact dilation covariance; the match is asymptotic.

An exact scale-free identity is available only as an unnormalized Mellin integral. On a subspace where \(|A|^{-3}\) is defined,

$$
\boxed{
|A|^{-3}
=\frac{4}{\sqrt\pi}
\int_0^\infty s^2e^{-s^2A^2}\,\mathrm ds.}
$$

For the positive operator \(A=\sqrt{-\Delta}\), one has \(|A|^{-3}=A^{-3}\), with symbol \(|k|^{-3}\). But the measure \(s^2\,\mathrm ds\) is not a probability distribution, and the resulting multiplier is singular at \(k=0\). Infrared quotienting and distributional or regulated interpretation are essential. Exact critical scaling is therefore not obtained for free from normalized uncertainty averaging.

## Typed connections to the larger programme

### W2: an analytic factor after the carrier change

[[causal-wall-spectral-theory/conjectures/bkm-to-spatial-precision|W2]] seeks a map from a mean-zero observational BKM block to a three-dimensional probability-1PI precision. The heat-mixture theorem can provide a positive spectral-multiplier factor only **after** W2 has supplied a spatial Hilbert space and a self-adjoint generator \(A\). It does not itself provide:

- localization or areal-to-volume measure conversion;
- the state-dependent BKM-to-source transform;
- the choice of \(A\) or proof of spatial dimension three;
- the covariance interpretation of \(T_{\alpha,m}\);
- the Legendre-1PI construction; or
- the normalization that relates the result to the common response form.

Thus the valid prospective factorization is not \(G^{\mathrm{BKM}}=T_{\alpha,m}^{-1}\), but a longer construction in which the heat multiplier acts on an already constructed spatial carrier. The exact theorem constrains a candidate W2 member; it does not close W2.

### The hidden resolvent: same function, different operation

[[spectral-wall-descent/hidden-resolvent-and-seesaw|The hidden-resolvent note]] obtains

$$
G_{xx}^{\mathrm{eff}}
=G_{xx}-BL^{-1}B^*
$$

by eliminating a hidden quadratic block. If \(L=A^2+m^2I\), the same resolvent function appears. But the types and signs differ:

- heat mixing directly gives the positive attenuation \(m^2L^{-1}\);
- Schur elimination gives the negative precision correction \(-BL^{-1}B^*\); and
- a covariance is the inverse of a precision only after the hypotheses in [[basic-concepts/hessians/fourier-covariance-and-precision|Fourier covariance and precision]] hold.

The shared resolvent is a reusable analytic grammar, not evidence that averaging, integrating out a field, and inverting a covariance are one physical operation.

### Descent and factivity: smoothing is not forgetting

The proposed wall in [[spectral-wall-descent/conditional-expectation-balance|conditional-expectation balance]] is idempotent and genuinely many-to-one. By contrast,

$$
T_m^2\neq T_m,
\qquad
\ker T_m=\{0\}.
$$

An abstract heat semigroup on a Hilbert space is not automatically a unital completely positive map on an observable algebra either; Markov or CP properties require additional algebraic hypotheses. Scale mixing therefore does not implement algebraic descent, select an observable context, produce a character, or extend a persistent record. It may describe degraded access within one carrier, while [[conservation-of-causal-charge/factive-descent-and-records|factive descent and records]] asks for a different, noninvertible arrow.

The philosophical distinction is exact. Unbounded inverse means that recovering fine distinctions is unstable under finite error. A nontrivial kernel or quotient means that distinctions have been identified by the map. Only the second is literal algebraic forgetting. Conflating them would replace the programme's desired ontology of fact-production with an ill-conditioned reconstruction problem.

## A theorem-shaped project target

The strongest honest use of this material would be a realization theorem of the following form:

> Given a completed wall interface returning a three-dimensional physical carrier \(\mathcal H_{\mathrm{sp}}\), a natural positive self-adjoint generator \(A\), and a transported BKM response, prove that a specified Gamma heat mixture is the covariance of the wall field; prove that its inverse is the renormalized 1PI precision; and show compatibility with restriction, symmetry, the physical quotient, and Lorentzian realization.

The heat-mixture and fractional-resolvent steps of that theorem are already exact. Every noun before and after them remains a construction obligation. The useful discovery is therefore not that a Cauchy line shape is the universal boundary of being. It is that positive heat averaging supplies a disciplined functional-calculus route from Gaussian suppression to resolvent and fractional-resolvent kernels, with a sharp ledger of what is retained, attenuated, and not actually forgotten.

## Primary sources

- David Sigtermans, “The Lorentzian Kernel as an Emergent Epistemic Envelope: Averaging, Resolution, and the Geometry of Distinguishability,” Preprints.org (2025), version 2, [doi:10.20944/preprints202506.0446.v2](https://doi.org/10.20944/preprints202506.0446.v2). A local source copy and abstract are archived in the library under the same title.
- Serge Bernstein, “Sur les fonctions absolument monotones,” *Acta Mathematica* **52** (1929), 1–66, [doi:10.1007/BF02592679](https://doi.org/10.1007/BF02592679). This is the original source behind the positive-measure representation of completely monotone functions.
- Salomon Bochner, “Diffusion Equation and Stochastic Processes,” *Proceedings of the National Academy of Sciences* **35** (1949), 368–370, [doi:10.1073/pnas.35.7.368](https://doi.org/10.1073/pnas.35.7.368). This is an original source for probabilistic subordination of diffusion.
- Einar Hille and Ralph S. Phillips, *Functional Analysis and Semi-Groups*, American Mathematical Society Colloquium Publications 31, revised edition (1957), [AMS record](https://bookstore.ams.org/COLL/31). This is a primary monograph for Laplace integrals, generators, resolvents, and operational calculus.
- Edwin T. Jaynes, “Information Theory and Statistical Mechanics,” *Physical Review* **106** (1957), 620–630, [doi:10.1103/PhysRev.106.620](https://doi.org/10.1103/PhysRev.106.620). This is the primary source for the maximum-entropy inference principle whose answer depends on the stated constraints and base measure.

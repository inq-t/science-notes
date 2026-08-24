# Conjecture: The Wall Response Admits a Covariant Realization

The homogeneous CST pulse becomes a physical cosmological component only if it is the FLRW restriction of a covariant, constrained, and stable response system. “Realization” here means a map between equally real mathematical regimes, not promotion of a formal model into reality. No such stress tensor, constitutive system, effective action, or natural transformation from wall response to covariant response has yet been derived, so growth, lensing, sound propagation, and primary-CMB predictions remain open.

The target may be an effective tensor \(T^X_{ab}\) satisfying

$$
T^X{}^a{}_b
\big|_{\mathrm{FLRW}}
=\operatorname{diag}(-\rho_X,p_X,p_X,p_X),
\qquad
p_X=w_X\rho_X,
$$

where the homogeneous functions are the conditional outputs of [[program-core/ruble-equations|the Ruble equations]]. If \(X\) is separately conserved, then

$$
\nabla_aT_X^{ab}=0.
$$

If the completion instead converts response among sectors, it must use tracked exchange currents,

$$
\nabla_aT_I^{ab}=J_I^b,
\qquad
\sum_IJ_I^b=0,
$$

rather than combine separate conservation with unaccounted transfer.

At the categorical level, let

$$
\mathsf{WallResp}:\mathsf{Bg}^{\mathrm{op}}\to\mathsf{WallData},
\qquad
\mathsf{CovResp}:\mathsf{Bg}^{\mathrm{op}}\to\mathsf{CovData}
$$

assign the constructed wall response and the corresponding gauge-reduced covariant stress or constitutive data under admissible background restrictions. Because their codomains differ, the bridge first requires a carrier-change functor

$$
F:\mathsf{WallData}\longrightarrow\mathsf{CovData}
$$

and then a natural transformation

$$
\eta:
\;F\circ\mathsf{WallResp}
\Longrightarrow
\mathsf{CovResp}
$$

whose pullback to the FLRW subcategory returns \((\rho_X,p_X)\). Derived or constrained geometry may organize the target complex, but it does not supply \(\eta\), its action, physical inner product, or hyperbolic evolution.

The upstream state family, transport, and physical tangent belong to [[wall-construction-interface/entry|the wall-construction interface]]. A covariant realization must additionally determine its gauge-invariant scalar, vector, and tensor variables; constraint algebra and physical modes; kinetic and gradient operators; characteristic cones; anisotropic stress; coupling to imported matter and radiation; initial or boundary data; and transfer functions. It must be regular through the response crossing and preserve the tested local sector required by [[compatible-with-existing-physics/local-physics-interface|the local-physics interface]]. [[algebra/real-forms-and-factive-spacetime|The real-form route]] can supply a candidate three-dimensional carrier under exact hypotheses, but it supplies none of this Lorentzian response data.

An optional stronger route asks whether [[binary-information-geometry/witten-darboux|the exact binary Witten--Darboux operator]] is a symmetry-reduced normal block of the covariant constraint complex. The internal factorization supplies no spacetime kinetic term or stability theorem; the parent complex, physical inner product, constraints, and reduction would all have to be derived.

## Upgrade criterion

Supply a covariant action, constitutive law, or Ward-identity system; prove its constraints, well-posedness, and absence of ghost and gradient instabilities in its declared regime; derive the homogeneous Ruble response as a solution rather than an input; and calculate perturbation observables in a reproducible Einstein--Boltzmann implementation.

## Failure criterion

The conjecture fails for a proposed completion if it has an inconsistent constraint algebra, an unavoidable ghost or gradient instability, acausal characteristics, a singular crossing, or unacceptable growth and lensing while preserving its background. [[causal-scale-theory/no-gos/positive-kinetic-field-crossing|The positive-kinetic scalar no-go]] excludes only the simplest canonical-field and positive-definite sigma-model realizations, not every collective, constrained, nonlocal, multicomponent, or geometric completion.

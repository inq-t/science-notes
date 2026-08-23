# Covariant Completions of Verlinde-Inspired Gravity

The available covariant “emergent gravity” models are independent effective-field-theory completions inspired by Verlinde’s elastic analogy, not unique consequences of his 2016 premises. They introduce a dynamical timelike displacement vector and matter couplings which materially enlarge the ontology; results about their stability or Hamiltonians therefore constrain those completions rather than the entire idea of emergent gravity.

## Why a completion is needed

[[verlinde-emergent-gravity]] supplies a restricted static elastic relation, not a covariant action or a complete rule for particles, light, cosmological perturbations, or gravitational waves. A relativistic theory requires at least

- dynamical fields and an action or closed field equations;
- a stress tensor and conservation law;
- a declaration of the metric followed by matter and light;
- initial-value and stability analysis; and
- a limit reproducing the intended static relation.

No theorem in Verlinde’s paper selects a unique completion satisfying these requirements.

## Hossenfelder’s vector-field model

[[vendor/entropic-gravity/sources/papers/1703.01415-hossenfelder-covariant-verlinde-emergent-gravity.pdf|Hossenfelder 2017]] promotes the elastic displacement to a timelike vector \(u^\mu\). In the paper’s convention,

$$
\varepsilon_{\mu\nu}
=\nabla_\mu u_\nu+\nabla_\nu u_\mu,
\qquad
u=\sqrt{-u^\mu u_\mu}.
$$

The kinetic scalar is

$$
\chi
=\alpha_\chi(\nabla_\mu u^\mu)^2
+\beta_\chi
(\nabla_\nu u_\kappa)(\nabla^\nu u^\kappa)
+\gamma_\chi
(\nabla_\nu u_\kappa)(\nabla^\kappa u^\nu).
$$

For

$$
\alpha_\chi=\frac43,
\qquad
\beta_\chi=\gamma_\chi=-\frac12,
$$

this can be written

$$
\chi
=-\frac14\varepsilon_{\mu\nu}\varepsilon^{\mu\nu}
+\frac13\varepsilon^2,
\qquad
\varepsilon:=\varepsilon^\mu{}_\mu.
$$

The proposed action contains Einstein gravity, ordinary matter, a direct vector–matter coupling, and a fractional-power vector kinetic term:

$$
\mathcal L_{\mathrm{tot}}
=m_p^2R
+\mathcal L_M
-\frac{u^\mu u^\nu}{Lu}T_{\mu\nu}
+\frac{m_p^2}{L^2}\chi^{3/2}
-\frac{\lambda^2m_p^2}{L^4}u_\mu u^\mu.
$$

The static spherical weak-field solution has a logarithmic extra potential and therefore a \(1/r\) acceleration. This is a concrete relativistic model, but it achieves that result by postulating a new vector field and its couplings.

## Full variation and particle motion

[[vendor/entropic-gravity/sources/papers/1806.03807-lim-wang-field-equations-covariant-emergent-gravity.pdf|Lim and Wang 2018]] formulate a fuller action treatment,

$$
I=\int d^4x\sqrt{-g}
\left[
\frac{R}{16\pi G}
+\mathcal L_m
+\frac{\alpha}{16\pi G}\chi^{3/2}
-V(u)
+\frac{\beta}{2}
\frac{u^\mu u^\nu}{u}T_{\mu\nu}
\right],
$$

and retain metric-variation terms arising through \(\delta\Gamma^\lambda{}_{\mu\nu}\). They identify a factor needed in the matter interaction and derive exact and perturbative static spherical solutions.

In their formulation, ordinary massive matter follows geodesics of an effective metric

$$
\widetilde g_{\mu\nu}
=g_{\mu\nu}
-\beta\frac{u_\mu u_\nu}{u},
$$

rather than \(g_{\mu\nu}\) itself. Light is treated through the backreaction of \(u^\mu\) on the spacetime metric. Thus massive-particle motion and lensing depend on coupling choices which are not fixed by Verlinde’s entropy-displacement argument.

## Stability and consistency results

[[vendor/entropic-gravity/sources/papers/1706.07854-dai-stojkovic-note-covariant-emergent-gravity.pdf|Dai and Stojkovic 2017]] correct the de Sitter solution of the Hossenfelder model and find growing perturbations around that vacuum in the sector they analyze. Matter or radiation can alter that conclusion, so the result is a stability problem for the proposed vacuum rather than a universal no-go theorem.

[[vendor/entropic-gravity/sources/papers/2003.10410-zatrimaylov-critique-covariant-emergent-gravity.pdf|Zatrimaylov 2020]] exhibits field configurations for which the Hossenfelder-type Hamiltonian is unbounded below. A Maxwell-like kinetic combination avoids that particular vector-energy problem, but its gauge identity conflicts with the desired sourced MOND-like behavior. This is a serious obstruction for that class of vector actions.

[[vendor/entropic-gravity/sources/papers/1710.00946-dai-stojkovic-inconsistencies-verlinde-emergent-gravity.pdf|Dai and Stojkovic 2017]] separately argue that Verlinde’s elasticity dictionary is internally inconsistent and can return Newtonian rather than MOND scaling when applied differently. [[vendor/entropic-gravity/sources/papers/2003.03198-yoon-comment-inconsistencies-emergent-gravity.pdf|Yoon 2020]] disputes their dictionary and proposes a repaired relation. This remains a contested critique; the uncontested internal limitation is already recorded in [[verlinde-emergent-gravity]]: the original elastic derivation gives an inequality and requires extra assumptions to use equality.

## Classification

| Claim | Status |
|---|---|
| A covariant action can be written whose static limit is MOND-like | Demonstrated for particular added vector fields and couplings |
| That action is derived uniquely from Verlinde’s microscopic hypotheses | Not demonstrated |
| The Hossenfelder model has a stable, bounded vacuum theory | Challenged by the cited perturbative and Hamiltonian analyses |
| A failure of one vector completion refutes all entropic or emergent gravity | Does not follow |
| Verlinde’s original spherical relation itself supplies cosmology and lensing | Does not follow |

These papers are best read as probes of what a completion would have to add and survive, not as later chapters of one already closed theory.

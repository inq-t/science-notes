# The Causal-Scale Interface

The proposed wall is best treated as an interface that relates local quantum states across changes of physical scale, not as a new two-level membrane or an already constructed three-dimensional QFT. A rigorous interface must specify the observable algebras, states, comparison maps, and physical scale action before relative entropy, Connes cocycles, or spectral responses can be attributed to it.

## Logical role

The useful distinction among theories is by logical role, not by length scale:

$$
\begin{aligned}
\text{local QFT} &: \text{ observables, states, correlations, and local dynamics},\\
\text{GR} &: \text{ metric--stress compatibility and gravitational propagation},\\
\text{causal-scale theory} &: \text{ selection and comparison of the cosmic state across scale}.
\end{aligned}
$$

The resulting picture is a bundle rather than a replacement hierarchy. At each scale $N$, ordinary QFT may provide a fiber $(\mathcal A_N,\omega_N)$. Vertical modular flow acts inside one fiber,

$$
\sigma_s^{\omega_N}:\mathcal A_N\longrightarrow\mathcal A_N,
$$

whereas the proposed new structure is horizontal comparison across fibers,

$$
\Phi_{N_2:N_1}:(\mathcal A_{N_1},\omega_{N_1})\longrightarrow
(\mathcal A_{N_2},\omega_{N_2}).
$$

This extends [[causal-scale-master/modular-flow|the distinction between modular flow and state deformation]]. It permits the Standard Model to remain the local quantum theory while placing a nontrivial burden on the scale interface.

## Three different objects called a wall

The sources presently use “wall” for three objects that are not canonically identical.

| Object | Natural dimension and structure | Role | Missing bridge |
|---|---|---|---|
| Observer-region algebra | A local net $O\mapsto\mathcal A_N(O)$ on a four-dimensional Lorentzian causal region $D_N$ | Contains the measurements available to an observer and supports ordinary AQFT states | Construct the region family, net, state, and inclusions on the relevant cosmology |
| Horizon or cut sector | A three-dimensional null worldvolume or a codimension-two spacelike cut $\Sigma_N$ with normal data | Carries horizon, corner, boost, area, or reduced normal degrees of freedom | Derive it from the region algebra and justify any binary infrared quotient |
| Euclidean spectral QFT | A three-dimensional Euclidean generating functional with stress response $A$ and $B$ | Realizes a domain-wall/cosmology dictionary for scalar and tensor correlators | Derive a duality or a complete analytic-continuation map from the Lorentzian observer/cut structure |

A codimension-two cut is not itself a three-dimensional Euclidean QFT. Evolving the cut along a null horizon does not by itself supply Euclidean reflection positivity, a stress tensor, a vacuum prescription, or the domain-wall/cosmology continuation. The word “wall” cannot serve as the missing functor.

## Minimal mathematical package

A scale-indexed interface should contain at least

$$
\mathfrak W=
\bigl(
\{D_N,\mathcal H_N,\Sigma_N\},
\{\mathcal A_N(O)\},
\{\omega_N\},
\{\iota_{N_2:N_1}\},
\Phi,
\{u_{N_2:N_1}(s)\},
T
\bigr),
$$

where:

- $D_N$ is an observer-accessible causal region, with horizon or boundary $\mathcal H_N$ and selected cut $\Sigma_N$;
- $\mathcal A_N(O)$ is a local algebra satisfying isotony, locality, covariance, and an appropriate time-slice property;
- $\omega_N$ is a faithful normal state with the needed ultraviolet regularity;
- $\iota_{N_2:N_1}$ identifies, embeds, or transports observables when the region or algebra changes;
- $\Phi$ gives the scale-to-state law independently of the spectrum it is meant to explain;
- $u_{N_2:N_1}(s)$ is relative modular data after both states have been placed on a common algebra;
- $T$ is the renormalized operator proposed to generate a local Weyl-source direction.

The common-algebra clause is essential. Araki relative entropy and a Connes cocycle compare states on one von Neumann algebra. If $\mathcal A_{N_1}$ and $\mathcal A_{N_2}$ differ, an inclusion, isomorphism, common standard form, or other transport must precede the notation

$$
[D\omega_{N_2}:D\omega_{N_1}]_s.
$$

Locally covariant relative Cauchy evolution is a plausible way to define metric response on controlled backgrounds; [[causal-wall-spectral-theory/sources/papers/0112041-brunetti-fredenhagen-verch-generally-covariant-locality.pdf|Brunetti, Fredenhagen, and Verch]] give the standard functorial framework. A renormalized stress response additionally inherits the locality, covariance, scaling, and metric-variation ambiguities treated by [[causal-wall-spectral-theory/sources/papers/9903028-brunetti-fredenhagen-microlocal-renormalization-physical-backgrounds.pdf|Brunetti and Fredenhagen]] and [[causal-wall-spectral-theory/sources/papers/0103074-hollands-wald-local-wick-polynomials-time-ordered-products.pdf|Hollands and Wald]]. None of these constructions automatically implements a global homogeneous Weyl change or identifies changing cosmological regions, so they are candidate components rather than a finished solution.

State selection is a substantive additional law. [[causal-wall-spectral-theory/sources/papers/1106.4785-fewster-verch-dynamical-locality-covariance.pdf|Fewster and Verch]] show that a covariant preferred state is unavailable under broad dynamical-locality hypotheses. A CWST state family must therefore give a physical selection rule and state which hypotheses or background structures allow it, rather than treating a preferred $\omega_N$ as functorially automatic.

## Controlled precedents, not a construction

Several results show that pieces of the proposed interface are mathematically constructible in restricted settings. [[causal-wall-spectral-theory/sources/papers/0712.1770-dappiaggi-moretti-pinamonti-cosmological-horizons-qft.pdf|Dappiaggi, Moretti, and Pinamonti]] map the algebra of a linear Klein--Gordon field into a cosmological-horizon algebra and induce a preferred bulk state on a selected class of expanding spacetimes. [[causal-wall-spectral-theory/sources/papers/1703.10656-casini-teste-torroba-null-plane-modular-hamiltonians.pdf|Casini, Teste, and Torroba]] obtain local stress-tensor modular Hamiltonians and a Markov property for vacuum regions on a null plane, or a null cone in a CFT. [[causal-wall-spectral-theory/sources/papers/2306.01837-jensen-sorce-speranza-generalized-entropy-subregions.pdf|Jensen, Sorce, and Speranza]] construct observer-dependent type-II subregion algebras in the $G_N\to0$ limit, using states whose instantaneously geometric modular flow is conjectural. [[causal-wall-spectral-theory/sources/papers/2406.01669-kudler-flam-leutheusser-satishchandran-algebraic-observational-cosmology.pdf|Kudler-Flam, Leutheusser, and Satishchandran]] construct gravitationally dressed observables for a comoving observer in past-asymptotically-de Sitter FLRW. [[causal-wall-spectral-theory/sources/papers/2601.07915-chandrasekaran-flanagan-subregion-algebras-gravity.pdf|Chandrasekaran and Flanagan]] construct horizon-cut algebras with edge modes and half-sided modular structure in perturbative gravity about black-hole backgrounds. None supplies the scale-indexed state law, the binary reduction, or the cosmological spectral weld required here.

## Three rank-one claims

The archive also uses “rank one” for three distinct reductions:

1. one noncentral horizontal generator $Q$ in a reduced normal sector;
2. one common cosmological clock residue shared by all material species;
3. one spin-zero form factor $B$ in the stress-tensor two-point decomposition.

None currently implies the other two. A microscopic construction must show separately why a large type-III local algebra reduces to one binary horizontal mode, why that mode is the gauge-invariant adiabatic curvature mode, and why its state metric is represented by the continued $B$ channel.

## Two legitimate completion levels

The programme can stop at either of two levels, provided it names the level accurately.

### Interface completion

Take established local QFT as input and construct a universal horizontal geometry over its admissible states. The primitive cosmological datum may be a positive precision functional $\mathcal K_\zeta$, with a three-dimensional QFT serving as one representation rather than the ontology of the wall. This level still has to derive or postulate $\mathcal K_\zeta$ independently and show how it couples consistently to GR.

### Microscopic holographic completion

Construct a particular wall algebra or dual QFT that calculates

$$
c^{(0)}(k),\qquad c^{(2)}(k),\qquad
\langle TTT\rangle,\ldots
$$

and proves the continuation to cosmological observables. This is stronger, but it is not required merely to formulate an autonomous interface theory.

The v3 master sometimes treats the holographic branch as load-bearing while later chats make $\mathcal K_\zeta$ primary. The clean resolution is to keep both branches explicit: the spectral QFT is a controlled representation only in members for which its duality and continuation are supplied.

## Independence and recovery tests

The interface is explanatory only if $\Phi$ and its response can be obtained without solving backward from $H(z)$, $\Delta_\zeta^2(k)$, or a fitted $w(z)$. Otherwise the construction is an effective fluid or covariance rewritten in new notation.

Leaving QFT “alone” also requires more than announcing it as an input. A successful local recovery statement must show that, in the relevant limit,

$$
\Gamma_{\mathrm{eff}}[g,\Psi;\mu]
=\Gamma_{\mathrm{GR+SM}}^{\mathrm{ren}}[g,\Psi;\mu]
+\Delta\Gamma_{\mathrm{wall}},
\qquad
\Delta\Gamma_{\mathrm{wall}}\longrightarrow0,
$$

where $\Gamma_{\mathrm{GR+SM}}^{\mathrm{ren}}$ is the ordinary renormalized low-energy effective action, including the cosmological, curvature, and matter counterterms allowed by its regime. Accessible Standard Model correlators, Ward identities, causal propagation, stress conservation, and anomaly cancellation must approach their established forms. No such action-level or algebraic decoupling theorem is presently given.

## Claim status

- **Standard framework:** local nets, faithful-state modular theory, relative entropy on a common algebra, and stress response to supported metric variations.
- **Coherent programme architecture:** QFT fibers with a horizontal causal-scale connection; the spectral QFT as a possible representation.
- **Unconstructed:** the relevant region family, state-selection law, common-algebra transport, binary quotient, global Weyl action, and Lorentzian-to-Euclidean wall map.
- **Not implied:** that a constructible observer algebra will yield $Q^2=1$, a $\operatorname{sech}^2$ BKM profile, a $P_3$ kernel, or the observed spectrum.

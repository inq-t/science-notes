# Vertical Modular Flow and Horizontal State Change

Modular evolution at one fixed state and cosmological displacement through a family of states are different kinds of motion. CST uses the second. The distinction is exact at the level of typing and prevents a fixed-state Tomita flow from being mistaken for a scale-evolution law.

For a von Neumann algebra $\mathcal A$ in standard form with faithful normal state $\omega$, Tomita--Takesaki theory supplies a modular operator $\Delta_\omega$ and the automorphism group

$$
\sigma_s^\omega(A)
=\Delta_\omega^{is}A\Delta_\omega^{-is},
\qquad A\in\mathcal A.
$$

This is **vertical** motion: $\mathcal A$ and $\omega$ are fixed while observables move under an automorphism indexed by modular parameter $s$.

CST instead proposes a horizontal assignment

$$
N\longmapsto (\mathcal A_N,\omega_N).
$$

Even when every fiber possesses its own modular group, $s$ is not thereby $N$, cosmic time, proper time, or a Weyl factor. A horizontal derivative requires a rule that identifies the fibers.

## Why transport comes first

If $\mathcal A_{N_1}\ne\mathcal A_{N_2}$, the formal expression

$$
\partial_N\omega_N
$$

subtracts states on different domains. Relative entropy and the Connes cocycle also compare states on a common algebra. One must first supply an embedding, identification, or transport

$$
\iota_{N_2:N_1}:\mathcal A_{N_1}\longrightarrow\mathcal A_{N_2}
$$

with an appropriate composition law. The minimal package and its anti-circularity conditions are specified in [[wall-construction-interface/entry|the wall-construction interface]].

After transport to a common state space, a smooth family may have a horizontal tangent $\dot\omega_N$ and a BKM norm. That construction is not automatic in a type-III local algebra: faithfulness, domains, finiteness or renormalization, and physical state selection all remain part of the problem.

## A useful schematic, not a theorem

It is sometimes helpful to depict a horizontal derivative as

$$
\nabla_N^{\mathrm{hor}}
=\partial_N+\Gamma_N,
$$

where $\Gamma_N$ represents the chosen comparison of fibers. This is only a schematic until the bundle, connection, and gauge equivalences are defined. It must not be used to smuggle in a preferred state path.

## Distinct clocks and coordinates

The following labels are not interchangeable:

$$
\text{proper time }t,
\quad
\text{conformal time }\eta,
\quad
\text{scale age }N,
\quad
\text{modular parameter }s,
\quad
\text{horizontal coordinate }\theta,
\quad
\text{horizon rapidity }\widehat\eta_A.
$$

Relations among them require maps with explicit hypotheses. [[causal-scale-theory/scale-soldering]] concerns $N\mapsto\theta$; [[causal-scale-theory/horizon-clock]] defines $N\mapsto\widehat\eta_A$ from FLRW kinematics. Neither relation identifies the two targets.

## A diagnostic exclusion

Changing the inverse temperature of one fixed modular Hamiltonian is not the binary $Q$-direction used by CST. [[no-gos/modular-rescaling-is-not-the-binary-tangent|The explicit variance calculation]] shows that their tangent norms disagree already at the self-dual point. It rules out that direct identification, not every possible relation between scale and modular data.

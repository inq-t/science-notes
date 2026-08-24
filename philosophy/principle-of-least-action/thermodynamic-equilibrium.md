# Thermodynamic Variational Principles

Thermodynamics contains powerful extremum principles, but there is no single unrestricted "least thermodynamic action." At equilibrium, entropy is maximized or an appropriate thermodynamic potential is minimized under clearly stated environmental constraints. The extremum is over macrostates rather than over histories, which is what separates this flavor from Hamilton's principle; the history-valued relatives belong to [[kinetic-and-stochastic]].

## Equilibrium: entropy maximum

For an isolated system with fixed internal energy $U$, volume $V$, and particle numbers $N_a$, stable equilibrium maximizes thermodynamic entropy:

$$
\delta S_{\mathrm{th}}=0,
\qquad
\delta^2S_{\mathrm{th}}<0
$$

for permitted nontrivial variations near a strict stable equilibrium. The first condition identifies a candidate equilibrium; the concavity or second-variation condition supplies stability.

For example, let two subsystems exchange energy while their total energy is fixed. With $U_2=U-U_1$,

$$
S_{\mathrm{tot}}(U_1)
=S_1(U_1)+S_2(U-U_1).
$$

Stationarity gives

$$
\frac{\partial S_1}{\partial U_1}
=\frac{\partial S_2}{\partial U_2},
$$

and because $1/T=\partial S/\partial U$, the equilibrium condition is $T_1=T_2$. Entropy maximization is therefore a compact way to derive the equality of intensive variables subject to conservation constraints.

## The environment selects the potential

Legendre transforms replace constrained entropy maximization by minimization of the potential natural to the quantities controlled by the environment.

| Controlled variables | Stable-equilibrium principle | Potential |
|---|---|---|
| $U,V,N_a$ | Maximize entropy | $S_{\mathrm{th}}$ |
| $S_{\mathrm{th}},V,N_a$ | Minimize internal energy | $U$ |
| $T,V,N_a$ | Minimize Helmholtz free energy | $F=U-TS_{\mathrm{th}}$ |
| $T,P,N_a$ | Minimize Gibbs free energy | $G=U-TS_{\mathrm{th}}+PV$ |
| $T,V,\mu_a$ | Minimize grand potential | $\Omega=U-TS_{\mathrm{th}}-\sum_a\mu_aN_a$ |

These statements apply to the appropriate stable equilibrium and admissible variations. Phase coexistence, metastability, long-range forces, nonconcave entropy, and finite-size effects can complicate the global-extremum picture.

## Statistical-mechanical origin

In equilibrium statistical mechanics, entropy is a functional of a probability distribution. For discrete microstates,

$$
S[p]=-k_B\sum_i p_i\ln p_i.
$$

Maximizing $S[p]$ subject to normalization and a fixed mean energy gives the canonical distribution,

$$
p_i=\frac{1}{Z}e^{-\beta E_i},
\qquad
Z=\sum_i e^{-\beta E_i}.
$$

The Lagrange multipliers encode the imposed constraints. Without the mean-energy constraint, maximum entropy would instead produce the uniform distribution over the allowed states. “Maximum entropy” is therefore an inference or equilibrium rule only after the state space, measure, and constraints are supplied.

Equivalently, for fixed temperature the canonical distribution minimizes the nonequilibrium free-energy functional

$$
\mathcal F[p]
=\sum_i p_iE_i
+k_BT\sum_i p_i\ln p_i.
$$

The difference from the equilibrium value is

$$
\mathcal F[p]-F_{\mathrm{eq}}
=k_BT\,D(p\|p_{\mathrm{eq}})\ge0,
$$

where $D$ is relative entropy. This is a precise minimum principle, not merely an analogy.

## The second law is not a least-action law

For an isolated macroscopic system, the second law states

$$
\Delta S_{\mathrm{th}}\ge0
$$

for an allowed process, or $\dot S_{\mathrm{tot}}\ge0$ in a suitable local description. It supplies an arrow and an inequality. It does **not** generally say that the realized irreversible history maximizes total entropy production, minimizes entropy production, or extremizes the time integral of entropy.

Those stronger claims require a separately derived regime and functional. Far-from-equilibrium systems may form patterns, sustain currents, and depend on kinetic details not fixed by state-function thermodynamics alone.

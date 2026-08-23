# Capacity, Compactness, and Gravitational Strength

Several standard gravitational quantities become ratios of energetic information budgets to areal horizon capacity. These identities give precise content to the interpretation of weak gravity as large geometric information stiffness, but they all reuse \(G\) through the Planck area or gravitational radius and therefore do not derive it.

Throughout,

$$
\eta_{\mathrm E}
:=\frac{c^3}{4\hbar G}
=\frac{1}{4\ell_P^2}
$$

is the [[areal-information-modulus|Einstein entropy--area density]].

## Compactness as a ratio of bounds

For a complete, weakly gravitating system in the regime of the original Bekenstein bound, let \(E\) be its energy and \(R\) a circumscribing radius. Define the Bekenstein information budget

$$
\mathcal I_B(E,R)
:=\frac{2\pi ER}{\hbar c}.
$$

This is the right-hand side of the Bekenstein entropy bound in natural-log units, not the actual entropy of every system. In quantum field theory, [[deriving-value-of-g/sources/papers/0804.2182-casini-relative-entropy-bekenstein-bound.pdf|Casini's relative-entropy formulation]] supplies a controlled interpretation for suitable regions and states.

The Bekenstein--Hawking capacity assigned to a spherical horizon of the same areal radius is

$$
\mathcal C_A(R)
:=\frac{A}{4\ell_P^2}
=\frac{\pi R^2}{\ell_P^2}.
$$

Their ratio is

$$
\begin{aligned}
\frac{\mathcal I_B(E,R)}{\mathcal C_A(R)}
&=\frac{2\pi ER}{\hbar c}
\frac{\ell_P^2}{\pi R^2}\\
&=\frac{2GE}{c^4R}\\
&=\frac{r_s(E)}{R},
\end{aligned}
$$

where

$$
r_s(E):=\frac{2GE}{c^4}.
$$

Thus

$$
\boxed{
\frac{\text{Bekenstein entropy budget}}
{\text{horizon capacity at the same radius}}
=\text{gravitational compactness}.}
$$

At the formal compactness threshold \(R=r_s\), the Bekenstein budget and black-hole capacity formulas have the same numerical value. The weak-gravity derivation of the original bound should not be extrapolated across that threshold without further argument. The identity does not prove that every collapsing system saturates the bound, that its microscopic information is uniformly stored on a boundary, or that horizon formation has been derived from information theory. The exact statement is the algebraic equality of the three dimensionless expressions under their stated definitions.

## Quantum localization and \(\alpha_G\)

For a particle of mass \(m\), define its reduced Compton length

$$
\lambda_C:=\frac{\hbar}{mc}
$$

and dimensionless gravitational coupling

$$
\alpha_G(m):=\frac{Gm^2}{\hbar c}.
$$

Then

$$
\alpha_G(m)
=\frac{\ell_P^2}{\lambda_C^2}
=\frac{1}{4\eta_{\mathrm E}\lambda_C^2},
$$

and

$$
2\alpha_G(m)=\frac{r_s(mc^2)}{\lambda_C}.
$$

The dimensionful \(G\) has become a dimensionless comparison between the trapping scale associated with the excitation and its quantum localization scale. At \(\lambda_C\gg\ell_P\),

$$
\alpha_G\ll1.
$$

At \(\lambda_C\sim\ell_P\), the quantum localization and gravitational compactness scales become comparable. This identifies the Planck regime; it does not provide a microscopic theory of that regime.

For \(E=mc^2\) and \(R=\lambda_C\), the Bekenstein budget is

$$
\mathcal I_B=2\pi,
$$

while

$$
\mathcal C_A(\lambda_C)
=\frac{\pi}{\alpha_G}.
$$

Consequently

$$
\frac{\mathcal I_B}{\mathcal C_A}=2\alpha_G.
$$

In this limited sense, ordinary particle gravity is weak because an order-unity localization budget is tiny compared with the Einstein horizon capacity at the same length.

## The causal-scale analogy and its limit

The exact compactness ratio has the same broad grammar as the causal-scale Ruble ratio:

$$
\frac{\text{state or energy information}}
{\text{causal capacity}}
\longrightarrow
\text{dimensionless gravitational importance}.
$$

Here

$$
\mathfrak R_\Sigma
:=\frac{\chi_{\downarrow}}{\eta_{\mathrm E}}
$$

compares the proposed horizontal BKM modulus with the Einstein entropy--area density on the same cut.

The objects are nevertheless different:

| Ratio | Numerator | Mathematical order | Status |
|---|---|---|---|
| \(\mathcal I_B/\mathcal C_A\) | energy--radius entropy bound | first-order modular-energy or entropy budget | exact algebra after definitions |
| \(\mathfrak R_\Sigma\) | horizontal BKM squared speed | second-order relative-entropy Hessian | causal-scale physical principle at the self-dual cut |

First-order modular energy and second-order BKM geometry should not be identified merely because both are information-theoretic. Controlled holographic results such as [[deriving-value-of-g/sources/papers/1508.00897-lashkari-van-raamsdonk-canonical-energy-quantum-fisher-information.pdf|canonical energy as quantum Fisher information]] show that a second-order equality can exist in a specified regime; they do not establish it for a dynamical FLRW wall.

## Why none of these equations fixes \(G\)

Each equality contains \(G\) twice in translated form:

$$
\ell_P^2=\frac{\hbar G}{c^3},
\qquad
r_s=\frac{2GE}{c^4},
\qquad
\eta_{\mathrm E}=\frac{c^3}{4\hbar G}.
$$

Dividing the resulting quantities reveals structure but cancels no unknown independent input. A derivation requires an independently constructed area modulus or a dimensionless gravitational ratio relative to an independently derived mass or length. That missing object is specified in [[causal-scale-derivation-target]].

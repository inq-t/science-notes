---
title: "Causal Scale Dynamics"
subtitle: "Modular Information Geometry, Horizon Capacity, and the Ruble Equations"
author: "Thomas Ruble"
date: "21 August 2026"
lang: en-US
papersize: letter
fontsize: 11pt
geometry: margin=0.76in
toc: true
toc-depth: 3
numbersections: true
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes:
  - |
    \usepackage{amsmath,amssymb,mathtools,booktabs,longtable,array,graphicx,microtype,float,xcolor,tcolorbox}
    \definecolor{ink}{HTML}{172033}
    \definecolor{accent}{HTML}{345B83}
    \definecolor{soft}{HTML}{EEF4F8}
    \definecolor{warn}{HTML}{FAF3E8}
    \definecolor{open}{HTML}{F3EFF8}
    \newcommand{\BKM}{\mathrm{BKM}}
    \newcommand{\E}{\mathcal E}
    \newcommand{\dd}{\mathrm d}
    \newcommand{\sech}{\operatorname{sech}}
    \newcommand{\avg}[1]{\left\langle #1\right\rangle}
    \newcommand{\vperp}{\varrho_\perp}
    \newcommand{\Ruble}{\mathfrak R_c}
    \newcommand{\Xscale}{\mathcal X_\sigma}
    \newcommand{\Sbar}{\mathcal S}
    \newcommand{\rc}{r_c}
    \newtcolorbox{thesisbox}{colback=soft,colframe=accent,boxrule=0.8pt,arc=1.2mm,left=3mm,right=3mm,top=2mm,bottom=2mm}
    \newtcolorbox{warningbox}{colback=warn,colframe=orange!55!black,boxrule=0.7pt,arc=1.2mm,left=3mm,right=3mm,top=2mm,bottom=2mm}
    \newtcolorbox{openbox}{colback=open,colframe=purple!45!black,boxrule=0.7pt,arc=1.2mm,left=3mm,right=3mm,top=2mm,bottom=2mm}
---

> **Working master research note v7.0. Not peer reviewed.** This note distinguishes **[STANDARD]**, **[THEOREM]**, **[DEDUCTION]**, **[PRINCIPLE]**, **[CONDITIONAL]**, **[NEGATIVE]**, and **[OPEN]** statements. The homogeneous theory is closed by one explicitly stated physical equivalence principle, not advertised as a theorem of mathematics alone. The covariant perturbation theory and the global vacuum sector remain separate research problems. The declared cosmological baseline is four-dimensional spatially flat FLRW with radiation, pressureless matter, one collective scale-capacity response, and an exactly zero residual late-time floor. Current observational comparisons are background-level or response-level analyses, not an official joint Boltzmann likelihood.

# Abstract {.unnumbered}

This note develops a self-contained formulation of gravity and cosmic history in which causal order, metric scale, modular state geometry, horizon entropy, and late-time acceleration are treated as different registers of one structure rather than as unrelated inputs.

Under the standard causality and regularity hypotheses, causal order determines a Lorentzian spacetime only up to conformal scale. The metric is represented by a conformal class $[g]$ and a positive scale section

$$
\sigma\in\Gamma(\E[1]),
\qquad
g_\sigma=\sigma^{-2}\boldsymbol g.
$$

Its two-jet is the scale tractor

$$
I_A=\frac14D_A\sigma.
$$

In four dimensions the trace-free Einstein equation is equivalent to the scale-transport equation

$$
\boxed{
\left(\nabla_a\nabla_b\sigma+P_{ab}\sigma\right)_0
=\frac{4\pi G}{c^4}\,\sigma T_{ab}^{\circ},
}
$$

while the trace and one scalar lift determine

$$
\boxed{
I^2=\frac{2\pi G}{3c^4}T-\frac{\Lambda_g}{3}.
}
$$

Trace-free stress is therefore the obstruction to parallel transport of scale; the cosmological constant belongs to a distinct global calibration channel.

A causal region and faithful state carry another geometry: modular flow, relative entropy, and its Bogoliubov--Kubo--Mori Hessian. The corrected theory separates vertical modular automorphism flow from horizontal deformation of the state family. At a homogeneous codimension-two cut, the normal plane supplies a canonical chirality operator

$$
Q=P_+-P_-,
\qquad
Q^2=1,
\qquad
JQJ=-Q.
$$

The associated binary exponential family is

$$
\omega_\theta=\frac{e^{\theta Q}}{2\cosh\theta},
$$

with dual information coordinates

$$
\eta=\avg Q=\tanh\theta,
\qquad
G^{\BKM}_{\theta\theta}=\frac{\dd\eta}{\dd\theta}=\sech^2\theta.
$$

The state coordinate is soldered to logarithmic Weyl scale

$$
N=\ln\frac{a}{a_c}=-\ln\frac{\sigma}{\sigma_c}
$$

through a measurable Connes-cocycle character. Under the rank-one ratio and measurability hypotheses, cocycle composition forces

$$
\theta=\vperp(N-N_c).
$$

The value of $\vperp$ is not fixed by Cauchy's equation. The present theory selects the fundamental normal representation, $\vperp=1$, as a physical structural law rather than as a continuously fitted dark-energy parameter.

The central closure is the **Scale--Capacity Equivalence Principle**. Let $S_c$ be the Bekenstein--Hawking entropy of the self-dual causal wall, $T_c=\hbar c/(2\pi k_BR_c)$ its canonically normalized horizontal modular temperature, $V_c$ its areal volume, and $G^{\perp}_{NN}$ the BKM norm of the fundamental horizontal scale tangent. The principle states

$$
\boxed{
\frac{k_B}{S_c}\,G^{\perp}_{NN}(N)
=\sech^2(N-N_c).
}
$$

Equivalently, the entropy-normalized BKM speed at self-duality is unity:

$$
\boxed{
\Ruble
:=\frac{k_B}{S_c}G^{\perp}_{NN}(N_c)=1.
}
$$

The physical source is the quadratic modular free-energy curvature per causal-wall volume,

$$
\boxed{
\rho_X(N)=\frac{k_BT_c}{2V_c}G^{\perp}_{NN}(N).
}
$$

In $3+1$ dimensional flat FLRW, horizon thermodynamics gives

$$
k_BT_c\frac{S_c}{k_B}
=E_{\rm MS,c}
=\rho_{\rm crit,c}V_c.
$$

Consequently,

$$
\boxed{
\rho_X(N)
=\frac12\rho_{\rm crit,c}\sech^2(N-N_c).
}
$$

At the self-dual crossing,

$$
\boxed{
\Omega_{X,c}=\frac12,
\qquad
\rho_X(N_c)=\rho_{\rm ordinary}(N_c).
}
$$

The former free normalization $r_c=1$ is therefore replaced by the scale-capacity principle. Relative to dust alone there is a calculable radiation correction of order $4\times10^{-4}$ for the benchmark cosmology.

Separate conservation yields

$$
\boxed{
w_X(N)=-1+\frac23\tanh(N-N_c),
}
$$

and the parameter-free differential invariant

$$
\boxed{
9(1+w_X)^2+6\frac{\dd w_X}{\dd N}=4.
}
$$

The sign change of cosmic acceleration is not inserted as an independent event. It follows from the competition between ordinary dilution and a single self-dual susceptibility pulse. The model predicts one observed acceleration entry, one future exit, and asymptotic coasting when the global residual floor is exactly zero.

For $\Omega_{m0}=0.310598$ and $\Omega_{r0}=9.15\times10^{-5}$, the capacity-normalized branch predicts

$$
N_c=-0.294007,
\qquad
z_c=0.341793,
$$

$$
q_0=-0.336902,
\qquad
j_0=-0.111246,
$$

$$
z_{\rm acc}=0.785694,
\qquad
\frac{a_{\rm exit}}{a_0}=11.7865.
$$

The previously reported background comparison gives $\chi^2\simeq1398.3$ for the rigid history and $1401.6$ for flat $\Lambda$CDM with the same number of background shape parameters. This is viability, not discovery. The strongest empirical test is the redshift-by-redshift invariant above, followed by the prediction that self-duality, $w_X=-1$, and ordinary--dark equality coincide.

The theory is closed at the homogeneous level by one equivalence law and one global sector choice. It does not yet provide a complete covariant perturbation action. The binary information geometry canonically generates a reflectionless Witten/Darboux pair, but the embedding of that pair into scalar, vector, and tensor spacetime perturbations remains open. That is the next research layer rather than an unfixed background parameter.


# The Ruble Equations

The theory is most compactly stated as a sequence of definitions and one physical equivalence principle. The equations are organized by mathematical type rather than by discovery history.

## Kinematic and geometric register

**R1 — causal scale.**

$$
\boxed{
g_{\rm phys}=\sigma^{-2}\boldsymbol g,
\qquad
N=-\ln\frac{\sigma}{\sigma_c}=\ln\frac{a}{a_c}.
}
$$

The conformal metric $\boldsymbol g$ fixes causal cones; the scale section $\sigma\in\Gamma(\E[1])$ fixes physical calibration. $N$ is logarithmic Weyl scale, not Newtonian absolute time.

**R2 — scale tractor.**

$$
\boxed{
I_A=\frac14D_A\sigma.
}
$$

The scale tractor packages $\sigma$, its first derivative, and the trace combination of its second derivative.

**R3 — tractor transport and norm.**

$$
\boxed{
\left(\nabla_a\nabla_b\sigma+P_{ab}\sigma\right)_0
=\frac{4\pi G}{c^4}\sigma T_{ab}^{\circ},
}
$$

$$
\boxed{
I^2=\frac{2\pi G}{3c^4}T-\frac{\Lambda_g}{3}.
}
$$

The first equation is local and trace-free. The second fixes the scalar calibration channel up to a global constant.

## Horizontal state register

**R4 — normal chirality.**

$$
\boxed{
Q=P_+-P_-,
\qquad
Q^2=1,
\qquad
JQJ=-Q.
}
$$

$P_\pm$ project onto the two null lines of the Lorentzian normal plane of a codimension-two cut. The homogeneous horizontal response is assumed to factor through this fundamental chirality quotient.

**R5 — binary exponential family.**

$$
\boxed{
\omega_\theta=\frac{e^{\theta Q}}{2\cosh\theta},
\qquad
\Psi(\theta)=\ln(2\cosh\theta).
}
$$

Its dual coordinates and metric are

$$
\boxed{
\eta=\Psi'(\theta)=\tanh\theta,
\qquad
G^{\BKM}_{\theta\theta}=\Psi''(\theta)=\sech^2\theta.
}
$$

The identity

$$
\boxed{
\eta^2+G^{\BKM}_{\theta\theta}=1
}
$$

is the normalized binary moment relation $\avg{Q^2}=1$.

**R6 — horizontal soldering.**

Under the rank-one ratio and measurability hypotheses, the Connes cocycle chain rule gives

$$
\theta=\vperp(N-N_c).
$$

The theory selects the fundamental character

$$
\boxed{\vperp=1.}
$$

This is a physical representation choice: the fundamental null-normal character is identified with the fundamental scale/inverse-scale character. It is not a theorem of Cauchy's equation, and it is not obtained from an integer restriction on conformal weights.

## Scale-capacity closure

**R7 — Ruble scale-capacity number.**

Let $G^{\perp}_{NN}$ be the physical BKM norm of the selected horizontal scale tangent and $S_c$ the horizon entropy of the self-dual wall. Define

$$
\boxed{
\Ruble:=\frac{k_B}{S_c}G^{\perp}_{NN}(N_c).
}
$$

The Scale--Capacity Equivalence Principle is

$$
\boxed{\Ruble=1.}
$$

In canonical binary coordinates this is equivalently

$$
\boxed{
\frac{k_B}{S_c}G^{\perp}_{NN}(N)=\sech^2(N-N_c).
}
$$

It states that the fundamental Weyl translation is isometric, at self-duality, to the fundamental horizontal state translation when the BKM metric is normalized by horizon entropy.

**R8 — modular free-energy source.**

$$
\boxed{
\rho_X(N)=\frac{k_BT_c}{2V_c}G^{\perp}_{NN}(N).
}
$$

This is the constitutive law. It converts dimensionless relative-entropy curvature into energy density by the physical modular temperature and causal-wall volume. The factor $1/2$ is the Taylor coefficient of relative entropy at coincidence.

**R9 — Hawking--Friedmann conversion.**

For a flat four-dimensional FLRW apparent horizon,

$$
\boxed{
R_c=\frac{c}{H_c},
\qquad
\frac{S_c}{k_B}=\frac{\pi R_c^2c^3}{G\hbar},
\qquad
k_BT_c=\frac{\hbar c}{2\pi R_c},
}
$$

and

$$
\boxed{
k_BT_c\frac{S_c}{k_B}
=E_{\rm MS,c}
=\rho_{\rm crit,c}V_c.
}
$$

**R10 — closed source.**

Combining R7--R9 gives

$$
\boxed{
\rho_X(N)=\frac12\rho_{\rm crit,c}\sech^2(N-N_c).
}
$$

At the crossing,

$$
\boxed{
\Omega_{X,c}=\frac12,
\qquad
\rho_X(N_c)=\rho_{\rm ordinary}(N_c).
}
$$

The exact equality is with the complete non-dark sector. Relative to dust alone,

$$
\frac{\rho_X(N_c)}{\rho_m(N_c)}
=1+\frac{\rho_r(N_c)}{\rho_m(N_c)}+\cdots.
$$

## Dynamical consequences

**R11 — equation of state.**

Separate conservation,

$$
\rho_X'=-3(1+w_X)\rho_X,
$$

gives

$$
\boxed{
w_X(N)=-1+\frac23\tanh(N-N_c).
}
$$

**R12 — shape invariant.**

$$
\boxed{
9(1+w_X)^2+6w_X'=4.
}
$$

Equivalent forms are

$$
\boxed{
\frac{\rho_X}{\rho_*}
+\frac14\left(\frac{\dd\ln\rho_X}{\dd N}\right)^2=1,
}
$$

and

$$
X'=\frac23-\frac32X^2,
\qquad X:=1+w_X.
$$

**R13 — self-dual comparison.**

The symmetrized relative entropy of the state and its modular reflection is

$$
\boxed{
\mathfrak S_J(\theta)=4\theta\tanh\theta.
}
$$

It has a unique global minimum at $\theta=0$. Along the rigid history,

$$
\boxed{
\mathfrak S_J=6(N-N_c)(1+w_X).
}
$$

Thus relative-entropy positivity fixes the orientation of the $w_X=-1$ crossing relative to increasing Weyl scale.

**R14 — central blindness.**

$$
\boxed{
\operatorname{Var}(K+\alpha\mathbf1)=\operatorname{Var}(K).
}
$$

The local response is blind to the absolute energy zero. A global scalar lift remains in $\Lambda_g$.

![Dependency structure of the theory. The scale-capacity principle is the single new equivalence law closing the homogeneous amplitude.](figures/dependency_v7.pdf){width=94%}

## What is law, what is solution data, and what is measured

| Quantity | Type | Role |
|---|---|---|
| $[g]$ | causal/conformal geometry | fixes null cones and causal order |
| $\sigma$ | scale section | metric calibration |
| $N$ | Weyl coordinate | logarithmic scale displacement |
| $Q$ | normalized normal chirality | fundamental horizontal binary score |
| $\theta$ | horizontal state coordinate | relative modular polarization |
| $\Ruble$ | dimensionless equivalence number | entropy-normalized peak BKM speed; postulated value $1$ |
| $N_c$ | solution origin | location of the intrinsic self-dual event relative to today |
| $\Omega_{m0},\Omega_{r0}$ | measured state data | determine the location of the crossing in the closed background |
| $\Lambda_g$ | global lift/sector | not part of local trace-free transport; zero in the open-future branch |

The theory therefore contains no continuously fitted dark-history function and no independent dark amplitude. It does contain one explicit physical equivalence principle and one global sector choice.


# Retyping the primitive notions

## Causal order is not Newtonian clock time

Several quantities called “time” are categorically different:

| Symbol/concept | Mathematical type | Reversal property |
|---|---|---|
| causal order $x\prec y$ | partial order on events | orientation is part of the relation |
| Newtonian/coordinate $t$ | parameter in equations | often reversed by $t\mapsto-t$ |
| proper time $\tau$ | metric length along a timelike curve | depends on calibrated metric |
| Weyl scale time $N=\ln a$ | additive coordinate on positive scale ratios | reverses between expansion and contraction |
| modular parameter $s$ | vertical automorphism parameter of a fixed state | a reversible one-parameter group |
| horizon rapidity $\eta_A$ | geometric boost coordinate when modular flow is geometric | vertical clock at a cut |
| horizontal polarization $\theta$ | coordinate comparing different states/fibers | state deformation, not elapsed modular time |

The v5.0 notation conflated $\eta_A$ and $\theta$. The corrected theory distinguishes

$$
\boxed{
\frac{\dd\eta_A}{\dd N}=\mu_A(N),
\qquad
\frac{\dd\theta}{\dd N}=\vperp.
}
$$

The first is a running horizon-clock rate; the second is the proposed horizontal scale-to-state conversion.

## Metric geometry is conformal structure plus scale

A conformal manifold is $(M,[g])$, with

$$
g_{ab}\sim\Omega^2g_{ab}.
$$

A positive scale section

$$
\sigma\in\Gamma(\mathcal E[1])
$$

selects the physical metric

$$
g_\sigma=\sigma^{-2}\boldsymbol g.
$$

The pair $([g],\sigma)$ contains the same information as a metric. The physical proposal is not that one has discovered an algebraic decomposition. It is that causal geometry and metric calibration may obey different dynamical laws and should not be fused before asking what sources each register.

## Matter and dark response are not new signed charges

The primitive local source is not a scalar “gravitational charge.” In the conformal description it is the trace-free stress obstructing parallel scale transport. In the proposed state description it is a positive information-geometric response. Signed modular orientation lives in $\avg{Q}=\tanh\theta$; the susceptibility is even:

$$
\operatorname{Var}(Q)=\sech^2\theta=\sech^2(-\theta).
$$

This permits conjugate state orientations without introducing positive and negative gravitational charges.



# Conformal gravity as transport and calibration

## Scale tractor

For four-dimensional conformal geometry define

$$
P_{ab}=\frac12\left(R_{ab}-\frac16Rg_{ab}\right),
\qquad
J=P^a{}_a=\frac{R}{6}.
$$

In a chosen representative metric, a standard tractor is written

$$
V^A\simeq(\alpha,\mu_a,\beta),
$$

with tractor norm

$$
h(V,V)=2\alpha\beta+g^{ab}\mu_a\mu_b.
$$

The scale tractor is

$$
\boxed{
I_A=\frac14D_A\sigma
\simeq
\left(
\sigma,
\nabla_a\sigma,
-\frac14(\Delta\sigma+J\sigma)
\right).
}
$$

The almost-Einstein operator is

$$
\boxed{
\E_{ab}(\sigma)
:=\left(\nabla_a\nabla_b\sigma+P_{ab}\sigma\right)_0.
}
$$

**[STANDARD]** On the open set where $\sigma\neq0$,

$$
\nabla_a^TI_B=0
\Longleftrightarrow
\E_{ab}(\sigma)=0
\Longleftrightarrow
g_\sigma\text{ is Einstein}.
$$

In the physical scale,

$$
\boxed{I^2=-\frac{R[g_\sigma]}{12}.}
$$

## Transport and norm equations

Taking the trace-free part of Einstein’s equation gives

$$
G^{\circ}_{ab}=\frac{8\pi G}{c^4}T^{\circ}_{ab}.
$$

The conformal transformation law yields

$$
G^{\circ}_{ab}[g_\sigma]
=2\sigma^{-1}\E_{ab}(\sigma),
$$

hence

$$
\boxed{
\E_{ab}(\sigma)
=\frac{4\pi G}{c^4}\sigma T^{\circ}_{ab}.
}
$$

Taking the trace gives

$$
\boxed{
I^2=\frac{2\pi G}{3c^4}T-\frac{\Lambda_{\rm g}}3.
}
$$

The accurate slogan is therefore:

$$
\boxed{
\begin{aligned}
\text{vacuum Einstein geometry}
&=\text{parallel scale transport},\\
\text{noncentral matter stress}
&=\text{transport defect},\\
\text{stress trace}
&=\text{norm variation},\\
\Lambda_{\rm g}
&=\text{global scalar lift}.
\end{aligned}}
$$

A measured $w_X\neq-1$ is not simply evidence for a new force. In this language it is evidence that the dark sector contributes to the failure of scale-tractor parallelism.

## Why the local equation is blind to the vacuum zero

Under

$$
T_{ab}\mapsto T_{ab}+\lambda g_{ab},
$$

one has

$$
T^{\circ}_{ab}\mapsto T^{\circ}_{ab}.
$$

Likewise a normalized Gibbs state is invariant under

$$
H\mapsto H+C\mathbf 1.
$$

Thus an additive vacuum offset is central in both languages:

$$
\boxed{
\begin{aligned}
H&\sim H+C\mathbf1,\\
T_{ab}&\sim T_{ab}+\lambda g_{ab},\\
\text{local causal response}&\sim\text{equivalence class modulo the central direction}.
\end{aligned}}
$$

This explains local vacuum blindness. It does not by itself make the remaining scalar lift radiatively stable. Section 11 returns to the global completion.



# Modular state geometry, self-duality, and the horizontal scale line

## Vertical modular flow and horizontal state deformation

For a local von Neumann algebra $\mathcal A$ and faithful state $\omega$, Tomita--Takesaki theory supplies ([6]) a modular operator $\Delta_\omega$, conjugation $J_\omega$, and automorphism group

$$
\sigma_s^\omega(A)=\Delta_\omega^{is}A\Delta_\omega^{-is}.
$$

This is **vertical** motion: an automorphism at fixed state. A family

$$
N\longmapsto\omega_N
$$

is **horizontal** motion through state space. A Connes cocycle or modular Berry connection is required to compare the modular frames of different fibers.

Schematically,

$$
\boxed{
\partial_NK_N
=[\mathcal A_N,K_N]
+(\mathcal D_NK_N)_\perp
+c_N'\mathbf1.
}
$$

| term | mathematical role |
|---|---|
| $[\mathcal A_N,K_N]$ | change of modular frame / vertical gauge |
| $(\mathcal D_NK_N)_\perp$ | physical horizontal noncentral deformation |
| $c_N'\mathbf1$ | central normalization shift |

The gravitational boost-charge principle acts on the vertical generator. Scale capacity acts on the horizontal tangent. The vacuum energy zero is central.

This distinction is essential. The vertical horizon rapidity satisfies

$$
\frac{\dd\eta_A}{\dd N}=\mu_A=\frac{1-q}{2},
$$

whereas the horizontal state coordinate obeys

$$
\frac{\dd\theta}{\dd N}=\vperp.
$$

They are not the same parameter.

## The normal pair and the fundamental score

A spacelike codimension-two cut has a Lorentzian normal plane

$$
N(\Sigma)=L_+\oplus L_-.
$$

Let $P_\pm$ be the two null-line projectors. The normal chirality operator

$$
Q=P_+-P_-
$$

satisfies

$$
Q^2=P_++P_-=1.
$$

Normal reflection exchanges the rays and gives

$$
JQJ=-Q.
$$

The full modular generator of a type-III algebra need not have two eigenvalues. The structural identification is narrower:

> **Fundamental normal reduction.** The homogeneous $J$-odd horizontal response is the infrared projection of the full state deformation onto the normal chirality quotient.

This is the one physical representation choice underlying the binary model. It is not a claim that the entire quantum field theory has a two-level Hilbert space.

## Cocycle composition and affine soldering

Assume the reduced relative cocycle depends on two scale sections only through their ratio $r=\sigma_2/\sigma_1$ and has one noncentral generator $Q$. Connes' chain rule then reduces to

$$
\theta(r_1r_2)=\theta(r_1)+\theta(r_2).
$$

Measurability is sufficient to solve the Cauchy equation:

$$
\boxed{
\theta(r)=-\vperp\ln r
=\vperp(N-N_c).
}
$$

This derives the logarithmic form but not the coefficient. The Claude closure's proposed integrality argument is not valid in ordinary conformal geometry: density bundles $\E[w]$ exist for every real $w$, so a real character $r^{\vperp}$ is mathematically admissible. The present theory selects the unit fundamental character as a physical law,

$$
\boxed{\vperp=1,}
$$

rather than pretending that Cauchy's equation or conformal representation theory alone excludes all other real values.

## Binary information geometry

The maximum-entropy family generated by $Q$ is

$$
\omega_\theta=\frac{e^{\theta Q}}{Z(\theta)},
\qquad
Z(\theta)=2\cosh\theta.
$$

The log-partition potential

$$
\Psi(\theta)=\ln Z(\theta)
$$

generates the mixture coordinate and BKM metric:

$$
\eta=\Psi'(\theta)=\avg Q=\tanh\theta,
$$

$$
\boxed{
G^{\BKM}_{\theta\theta}=\Psi''(\theta)=\operatorname{Var}_\theta(Q)=\sech^2\theta.
}
$$

The identity

$$
\eta^2+G^{\BKM}_{\theta\theta}=1
$$

is simply $\avg{Q^2}=1$.

The full Fisher distance of the crossover is

$$
\boxed{
L_F=\int_{-\infty}^{\infty}\sech\theta\,\dd\theta=\pi.
}
$$

The state traverses the complete binary simplex from one extremal ray to the other. The width in Weyl scale is fixed by the soldering coefficient.

![The complete binary traversal. The total Fisher distance is fixed; the Weyl soldering determines how that distance is distributed over cosmic scale.](figures/fisher_complete_traversal.pdf){width=90%}

## Modular self-duality

Because $JQJ=-Q$,

$$
J\omega_\theta J=\omega_{-\theta}.
$$

The symmetrized relative entropy is ([19])

$$
\boxed{
\mathfrak S_J(\theta)
=S(\omega_\theta\|\omega_{-\theta})
+S(\omega_{-\theta}\|\omega_\theta)
=4\theta\tanh\theta.
}
$$

It is nonnegative, vanishes only at $\theta=0$, and has

$$
\mathfrak S_J'(0)=0,
\qquad
\mathfrak S_J''(0)=8.
$$

The crossing is therefore intrinsically defined as the unique self-dual state. Its numerical date relative to today remains solution data determined by the matter/radiation state and flatness.

The relation

$$
\mathfrak S_J=6(N-N_c)(1+w_X)
$$

later implies that the phantom-to-quintessence orientation is fixed relative to increasing Weyl scale. It does not derive why the universe chooses the expanding rather than time-reversed branch.

## What information geometry fixes

Čencov's theorem fixes the classical Fisher metric up to a global scale under the relevant statistical morphisms. Petz classifies quantum monotone metrics; monotonicity alone does not uniquely select BKM. The relative-entropy Hessian selects the BKM metric, and the binary normalization $Q^2=1$ fixes the dimensionless shape.

None of those theorems converts dimensionless BKM curvature into energy density. That conversion is supplied by the scale-capacity equivalence principle and horizon thermodynamics, not by a hidden normalization theorem.


# The Scale--Capacity Equivalence Principle

The previous versions contained two numbers:

$$
\vperp=\frac{\dd\theta}{\dd N}
$$

for the horizontal conversion rate and

$$
\chi_\perp
$$

for the conversion from BKM susceptibility to energy density. Background data partly degenerate them. The present closure replaces the arbitrary stiffness by an invariant relation among the state metric, horizon entropy, modular temperature, and causal volume.

## Capacity and the physical BKM norm

The normalized binary metric

$$
\sech^2\theta
$$

fixes shape but is not the extensive capacity of the whole causal wall. Write

$$
G^{\perp}_{NN}(N)
=C_{\perp,c}\vperp^2\sech^2[\vperp(N-N_c)],
$$

where

$$
C_{\perp,c}=G^{\perp}_{\theta\theta}(0)
$$

is the physical BKM capacity carried by the selected horizontal mode.

The entanglement capacity of a state is

$$
C_E=\operatorname{Var}(K).
$$

It is not equal to entropy for arbitrary states. In controlled holographic CFTs with an ordinary Einstein-gravity dual and the preferred gravitational regularization, spherical regions satisfy ([26])

$$
C_E=S_{EE}/k_B.
$$

Higher-derivative gravity and generic quantum states can change the ratio. The equality therefore characterizes an Einstein-capacity universality class rather than a tautology.

## The invariant Ruble number

Define

$$
\boxed{
\Ruble
:=\frac{k_B}{S_c}G^{\perp}_{NN}(N_c)
=\frac{k_BC_{\perp,c}}{S_c}\vperp^2.
}
$$

This combination is invariant under rescaling the coordinate $\theta$: the BKM metric and coordinate slope transform oppositely. It is the entropy-normalized squared speed of the horizontal state under one Weyl e-fold.

The fundamental law is

$$
\boxed{\Ruble=1.}
$$

Equivalently,

$$
\boxed{
\left.
\Phi^*\left(\frac{k_B}{S_c}G^{\perp}_{\BKM}\right)
\right|_{N_c}
=\dd N^2.
}
$$

This is the stopping principle of the homogeneous theory. It is analogous in logical status to an equivalence principle or a universal conversion law: it is not derived from a more primitive metric convention, and it is directly falsifiable.

Under the fundamental normal representation, $\vperp=1$, the same law implies

$$
C_{\perp,c}=S_c/k_B.
$$

Conversely, if the selected wall mode saturates the Einstein capacity, the unit Ruble number fixes $\vperp=1$.

## Relative entropy as modular free-energy curvature

Let $\omega_c$ be the self-dual KMS reference state and $\mathcal H_c=k_BT_cK_c$ its physical modular Hamiltonian. Nonequilibrium free energy obeys the exact identity

$$
F_c(\rho)-F_c(\omega_c)
=k_BT_cS(\rho\|\omega_c).
$$

For a neighboring scale state,

$$
S(\omega_{c+\delta N}\|\omega_c)
=\frac12G^{\perp}_{NN}(N_c)\delta N^2+O(\delta N^3).
$$

Therefore the quadratic free-energy curvature is

$$
\lim_{\delta N\to0}
\frac{F_c(\omega_{c+\delta N})-F_c(\omega_c)}{\delta N^2}
=\frac{k_BT_c}{2}G^{\perp}_{NN}(N_c).
$$

The homogeneous source law is defined by distributing that collective modular free energy over the causal-wall volume:

$$
\boxed{
\rho_X(N)=\frac{k_BT_c}{2V_c}G^{\perp}_{NN}(N).
}
$$

This is not a canonical local scalar kinetic term. $\theta$ is a collective state coordinate, and the energy is the free-energy curvature of the state family. The single-field ghost no-go therefore does not invalidate the homogeneous construction.

## Hawking--Friedmann conversion

For a flat FLRW apparent horizon in four spacetime dimensions,

$$
R_c=\frac{c}{H_c},
\qquad
A_c=4\pi R_c^2,
\qquad
V_c=\frac{4\pi}{3}R_c^3.
$$

Use the Bekenstein--Hawking entropy

$$
\frac{S_c}{k_B}=\frac{A_cc^3}{4G\hbar}
=\frac{\pi R_c^2c^3}{G\hbar}
$$

and the canonically normalized horizontal causal-diamond temperature

$$
k_BT_c=\frac{\hbar c}{2\pi R_c}.
$$

Then

$$
\boxed{
k_BT_c\frac{S_c}{k_B}=\frac{c^4R_c}{2G}=E_{\rm MS,c}.}
$$

The flat Friedmann relation gives

$$
E_{\rm MS,c}=\rho_{\rm crit,c}V_c.
$$

Thus

$$
\boxed{
\frac{k_BT_c}{V_c}\frac{S_c}{k_B}=\rho_{\rm crit,c}.
}
$$

This is the dimensional bridge. The BKM metric supplies dimensionless response; horizon temperature supplies energy per information unit; the causal volume supplies density; Friedmann marginality identifies the result with the critical density.

![The homogeneous amplitude closes by composing binary BKM geometry, modular free energy, and horizon thermodynamics.](figures/scale_capacity_closure.pdf){width=96%}

## Closed amplitude

Using

$$
G^{\perp}_{NN}(N)
=\Ruble\frac{S_c}{k_B}\sech^2(N-N_c),
$$

the source becomes

$$
\boxed{
\rho_X(N)=\frac{\Ruble}{2}\rho_{\rm crit,c}\sech^2(N-N_c).
}
$$

For the fundamental value $\Ruble=1$,

$$
\boxed{
\rho_X(N)=\frac12\rho_{\rm crit,c}\sech^2(N-N_c).
}
$$

At the crossing,

$$
\Omega_{X,c}=\frac12.
$$

Spatial flatness implies

$$
\rho_{\rm ordinary,c}=\rho_{\rm crit,c}-\rho_{X,c}=\frac12\rho_{\rm crit,c},
$$

and hence

$$
\boxed{
\rho_X(N_c)=\rho_{\rm ordinary}(N_c).
}
$$

The former postulate $r_c=1$ is thereby derived from the scale-capacity law. The exact equality includes radiation and any other non-dark contribution.

## General spatial dimension

Let $d$ be the number of spatial dimensions. The apparent-horizon area and volume scale as

$$
A=\Omega_{d-1}R^{d-1},
\qquad
V=\frac{\Omega_{d-1}}{d}R^d.
$$

Einstein-Friedmann geometry gives

$$
\frac{k_BT_c(S_c/k_B)}{V_c}
=\frac{2}{d-1}\rho_{\rm crit,c}.
$$

Therefore

$$
\boxed{
\Omega_{X,c}=\frac{\Ruble}{d-1},
}
$$

and

$$
\boxed{
\frac{\rho_{X,c}}{\rho_{\rm ordinary,c}}
=\frac{\Ruble}{d-1-\Ruble}.
}
$$

For $\Ruble=1$,

$$
\frac{\rho_{X,c}}{\rho_{\rm ordinary,c}}=\frac1{d-2}.
$$

Equal ordinary and response densities occur in three spatial dimensions:

$$
\boxed{
\Ruble=1,
\quad
\rho_X=\rho_{\rm ordinary}
\quad\Longleftrightarrow\quad
d=3.
}
$$

This does not independently prove that space must have three dimensions. It shows that the unit scale-capacity law and equal self-dual partition are mutually compatible precisely in the observed dimension.

![The dimension dependence of the self-dual crossing.](figures/dimension_crossing_ratio.pdf){width=78%}

## Status of the closure

The closure contains one physical law:

$$
\boxed{
\left.
\frac{k_B}{S_c}G^{\perp}_{NN}
\right|_{N_c}=1.
}
$$

The supporting evidence is:

- capacity equals entropy in controlled spherical Einstein-holographic settings ([26]);
- modular-Hamiltonian variance equal to horizon entropy has been proposed for flat, de Sitter, and suitable holographic causal diamonds ([27,28]);
- the BKM Hessian equals gravitational canonical energy in controlled holographic perturbation theory ([12]);
- apparent-horizon thermodynamics gives the exact Hawking--Friedmann dimensional conversion ([24,25]).

The law has not been proved for a dynamical FLRW causal wall. It is the theory's equivalence principle and its most direct target for independent derivation or falsification.


# Exact homogeneous dynamics and the sign of acceleration

## Flat FLRW scale dictionary

For a spatially flat FLRW metric

$$
\dd s^2=a^2(\eta)(-\dd\eta^2+\dd\mathbf x^2),
$$

choose the flat conformal representative. Then

$$
\sigma=\frac1a,
\qquad
N=\ln a=-\ln\sigma.
$$

The following identities are exact:

$$
\boxed{\sigma'=-H,}
$$

$$
\boxed{\mathcal R=-\frac{\sigma}{\sigma'},}
$$

$$
\boxed{\mathcal R'=q,}
$$

and

$$
\boxed{
q=-1+\frac{\sigma\sigma''}{\sigma'^2}
=\frac{(\ln\sigma)''}{[(\ln\sigma)']^2}.
}
$$

Here a prime denotes conformal-time differentiation and $\mathcal R=1/(aH)$ is the comoving Hubble radius.

The homogeneous null-energy condition is

$$
\rho+p\ge0
\quad\Longleftrightarrow\quad
\sigma''\ge0,
$$

so it is convexity of the scale section. Accelerated expansion is

$$
q<0
\quad\Longleftrightarrow\quad
(\ln\sigma)''<0,
$$

so it is log-concavity of scale.

The tractor norm becomes

$$
\boxed{
I^2=\frac12\sigma\sigma''-\sigma'^2
=-\frac12(1-q)H^2.
}
$$

## Closed background equation

With ordinary radiation and matter plus the scale-capacity source,

$$
\boxed{
H^2(N)=\frac{8\pi G}{3c^2}
\left[
\rho_{m0}e^{-3N}
+\rho_{r0}e^{-4N}
+\frac12\rho_{\rm crit,c}\sech^2(N-N_c)
\right].
}
$$

At the self-dual point,

$$
\frac12\rho_{\rm crit,c}
=\rho_m(N_c)+\rho_r(N_c)+\cdots.
$$

Present flatness determines $N_c$ from

$$
\boxed{
1=\Omega_{m0}+\Omega_{r0}
+\left[
\Omega_{m0}e^{-3N_c}
+\Omega_{r0}e^{-4N_c}
\right]\sech^2N_c.
}
$$

Thus $N_c$ is not an independently fitted dark parameter. Its intrinsic meaning is fixed by self-duality; its position relative to today is fixed by the measured ordinary state and flatness.

## Equation of state and structural invariant

The density law gives

$$
\frac{\dd\ln\rho_X}{\dd N}
=-2\tanh(N-N_c).
$$

Separate conservation gives

$$
\boxed{
w_X(N)=-1+\frac23\tanh(N-N_c).
}
$$

Let

$$
X:=1+w_X.
$$

Then

$$
\boxed{
X'=\frac23-\frac32X^2.
}
$$

The two fixed points are

$$
w_-=-\frac53,
\qquad
w_+=-\frac13.
$$

The observed history is the unique heteroclinic orbit from the early to the late fixed point. The one density maximum and one $w_X=-1$ crossing are not separately adjusted features.

The binary normalization becomes the differential invariant

$$
\boxed{
9(1+w_X)^2+6w_X'=4.
}
$$

This relation is independent of the amplitude and crossing date. It is the primary structural test of the theory.

## Why acceleration begins and ends

The total deceleration parameter is

$$
q=-1+\frac32
\frac{
\rho_m+\frac43\rho_r+(1+w_X)\rho_X
}{
\rho_m+\rho_r+\rho_X
}.
$$

Acceleration occurs when

$$
\boxed{
(2-3[1+w_X])\rho_X>\rho_m+2\rho_r.
}
$$

The response is negligible in the remote past, rises through the ordinary budget, and later decays as $a^{-2}$. Consequently the inequality is satisfied only on a finite interval.

The model therefore predicts two zeroes of $q$:

1. an observed past transition from deceleration to acceleration;
2. a future transition back to nonacceleration.

The phrase “the sign flip of cosmic acceleration” ordinarily refers to the first. The second is an independent future prediction.

## Benchmark

For

$$
\Omega_{m0}=0.310598,
\qquad
\Omega_{r0}=9.15\times10^{-5},
$$

the closed solution is

$$
\boxed{
N_c=-0.2940066,
\qquad
z_c=0.3417927.
}
$$

The crossing density in present critical units is

$$
\frac{\rho_*}{\rho_{\rm crit,0}}=0.7506311.
$$

The exact ordinary-sector equality is

$$
\frac{\rho_*}{\rho_m(N_c)+\rho_r(N_c)}=1.
$$

Relative to dust alone,

$$
\frac{\rho_*}{\rho_m(N_c)}=1.0003953.
$$

The present and transition observables are

| quantity | prediction |
|---|---:|
| $w_0$ | $-0.809454$ |
| tangent $w_a$ | $-0.612205$ |
| $q_0$ | $-0.336902$ |
| $j_0$ | $-0.111246$ |
| $q(N_c)$ | $-0.249901$ |
| horizon index $\mu_A(N_c)$ | $0.624951$ |
| acceleration entry | $z=0.785694$ |
| acceleration exit | $a/a_0=11.7865$ |

![The capacity-normalized background. The self-dual crossing, the observed acceleration entry, and the predicted exit are distinct events.](figures/rigid_history_v7.pdf){width=94%}

## Future causal character

At late times,

$$
\rho_X\propto a^{-2},
\qquad
w_X\to-\frac13.
$$

If the residual scalar floor is exactly zero,

$$
H\propto a^{-1},
\qquad
\dot a\to\text{constant},
\qquad
a(t)\sim t.
$$

The future conformal-time integral diverges,

$$
\int^\infty\frac{\dd t}{a(t)}\sim\int^\infty\frac{\dd t}{t}=\infty,
$$

so there is no permanent future event horizon.

A positive residual $\Lambda_g$, however small today, eventually dominates and changes the asymptotic state to de Sitter. Exact zero and observationally negligible are therefore distinct global sectors.


# Local gravitational sourcing and the vacuum catastrophe

## One causal boost charge [CONJECTURAL UNITY PRINCIPLE]

For an equilibrium causal cut, propose that the modular boost charge of the restricted state and the gravitational Noether boost charge of the cut are two representations of one causal charge.

The state side gives the entanglement first law ([7,9,10])

$$
\delta S_{\rm out}=\delta\avg{K}.
$$

The geometric side gives

$$
S_{\rm grav}=\frac{k_BA}{4\ell_P^2}
$$

in the Einstein regime. Raychaudhuri focusing relates area variation to $R_{ab}k^ak^b$. Equating the two boost-charge responses for every local null direction yields

$$
R_{ab}k^ak^b=\frac{8\pi G}{c^4}T_{ab}k^ak^b.
$$

A Lorentzian tensor lemma then gives

$$
R_{ab}^{\circ}=\frac{8\pi G}{c^4}T_{ab}^{\circ},
$$

and therefore the tractor transport equation in Section 4.

This is a conditional derivation combining established ingredients with one unity principle. It is not derived from the binary late-time model.

## Vacuum offset as a vertical/central direction

A constant Hamiltonian shift leaves the normalized state unchanged:

$$
\frac{e^{-\beta(H+C\mathbf1)}}{\operatorname{tr}e^{-\beta(H+C\mathbf1)}}
=\frac{e^{-\beta H}}{\operatorname{tr}e^{-\beta H}}.
$$

It therefore has zero BKM length. The corresponding stress shift is annihilated by the trace-free source equation.

The proposed retyping is:

$$
\boxed{
\begin{aligned}
\text{central vacuum offset}
&=\text{vertical normalization direction},\\
\text{physical state response}
&=\text{horizontal BKM displacement},\\
\text{cosmological scalar curvature}
&=\text{global lift data}.
\end{aligned}}
$$

This shows why the local causal dynamics need not respond to the QFT zero of energy. It does not determine or stabilize the global lift.

## One explicit global completion

Manifestly local vacuum-energy sequestering introduces four-form sectors ([26,27]) whose equations force the cosmological variables to be spacetime constants while global flux constraints subtract the spacetime-averaged vacuum contribution. Schematically,

$$
M^2G^a{}_b
=T^a{}_b-\frac14\delta^a_b\avg{T}-\Delta\Lambda\,\delta^a_b.
$$

Writing

$$
T^a{}_b=-V_{\rm vac}\delta^a_b+\tau^a{}_b
$$

gives

$$
M^2G^a{}_b
=\tau^a{}_b-\frac14\delta^a_b\avg{\tau}-\Delta\Lambda\,\delta^a_b.
$$

The spacetime-filling matter-loop vacuum cancels from the source. A Gauss–Bonnet extension has been proposed to protect the residual against the cutoff-dominated graviton-loop sector within effective field theory.

This is one published completion, not a consequence of modular–Weyl geometry. The master programme’s claim is that the local quotient and global top-form lift have compatible mathematical types.

## What remains of the cosmological constant

The surviving residual

$$
\Lambda_{\rm res}
$$

is a global flux or superselection datum. The rigid branch takes

$$
\Lambda_{\rm res}=0
$$

exactly. A small positive value is not equivalent: it eventually dominates and restores a future event horizon.

The programme does not yet derive which flux sector nature selects.



## Relation to the scale-capacity source

The scale-capacity source is automatically blind to a central modular shift because its primitive is a covariance:

$$
G^{\BKM}_{NN}\sim\operatorname{Var}(K_N),
$$

and

$$
\operatorname{Var}(K+\alpha\mathbf1)=\operatorname{Var}(K).
$$

This does not mean that every quantum contribution proportional to the metric has been removed from a fully renormalized gravitational effective action. It means that the **local horizontal response law** depends only on noncentral state distinguishability. The cosmological constant and radiative stability of the scalar lift are logically separate.

The theory therefore assigns the two problems to different mathematical slots:

$$
\boxed{
\begin{aligned}
\text{transient late response}
&\longleftrightarrow
\text{horizontal BKM free-energy curvature},\\
\text{constant vacuum offset}
&\longleftrightarrow
\text{central/global norm sector}.
\end{aligned}}
$$

This separation is one of the principal motivations for the framework. It does not replace the need to specify the global sector.


# Horizons, black holes, entropy, and the meanings of time

## Four distinct notions of time

The framework uses several ordered parameters that must not be conflated.

| Symbol or notion | Meaning |
|---|---|
| causal order | a partial order on events; no metric duration is implied |
| proper or clock time $\tau$ | metric length along a timelike worldline |
| Weyl scale time $N$ | logarithmic change of the scale section, $N=\ln(a/a_c)$ |
| vertical modular parameter $s$ | automorphism parameter within one algebra/state fiber |
| horizontal state coordinate $\theta$ | relative modular polarization across a family of states |

The v5.0 inconsistency arose from treating the last two as the same parameter. They are different directions even when they use the same normal boost generator.

## Running horizon index

For a spherical horizon of areal radius $R_H$, define

$$
\boxed{
\mu_H:=\frac{|\kappa_H|R_H}{c^2}.
}
$$

It compares a normal-boost rate with an inverse geometric scale. It is a state-dependent index, not the Ruble number and not a measure of a total “amount of gravity.”

For a flat FLRW apparent horizon,

$$
R_A=\frac{c}{H},
$$

and the Kodama--Hayward surface gravity gives

$$
\boxed{
\mu_A=\frac{1-q}{2}=-\frac{I^2}{H^2}.
}
$$

The first equality is horizon kinematics; the second is scale-tractor geometry. In four-dimensional spherical Einstein gravity,

$$
S_A=k_B\frac{\pi R_A^2c^3}{G\hbar},
\qquad
E_A=\frac{c^4R_A}{2G},
$$

so, with the positive Kodama--Hayward temperature,

$$
\mu_A=\frac{T_AS_A}{E_A}.
$$

Representative values are

| regime | $w$ | $q$ | $\mu_A$ |
|---|---:|---:|---:|
| radiation | $1/3$ | $1$ | $0$ |
| matter | $0$ | $1/2$ | $1/4$ |
| coasting / acceleration threshold | $-1/3$ | $0$ | $1/2$ |
| de Sitter | $-1$ | $-1$ | $1$ |

Therefore

$$
\boxed{
\ddot a>0\iff\mu_A>\frac12.
}
$$

The value $1/2$ also equals $|\kappa|R/c^2$ for a four-dimensional Schwarzschild horizon. This identifies a shared dimensionless surface-gravity balance; it does not identify an FLRW spacetime with a Schwarzschild spacetime.

## Clock allocation

The dimensionless apparent-horizon entropy is

$$
\mathcal S_A=\frac{S_A}{k_B}=\frac{\pi c^5}{G\hbar H^2}.
$$

Hence

$$
\frac{\dd\ln\mathcal S_A}{\dd N}=4(1-\mu_A).
$$

Define a geometrically normalized vertical horizon rapidity potential $\eta_A$ by

$$
\frac{\dd\eta_A}{\dd t}=\frac{|\kappa_A|}{c}.
$$

Since $\dd N/\dd t=H$,

$$
\frac{\dd\eta_A}{\dd N}=\mu_A.
$$

Thus

$$
\boxed{
\dd N=\dd\eta_A+\frac14\dd\ln\mathcal S_A.
}
$$

One Weyl e-fold decomposes exactly into vertical horizon-rapidity advance and horizon-information growth. The horizontal fundamental law is instead

$$
\frac{\dd\theta}{\dd N}=1.
$$

Consequently,

$$
\boxed{
\theta'-\eta_A'
=1-\mu_A
=\frac14(\ln\mathcal S_A)'.
}
$$

This is the corrected relation among horizontal state motion, vertical horizon motion, and information capacity.

## Smarr and Hawking relations as scale homogeneity

For a one-scale asymptotically flat black hole in $D$ spacetime dimensions,

$$
E\propto R_H^{D-3},
\qquad
S\propto R_H^{D-2}.
$$

Euler homogeneity and $\dd E=T\dd S$ give

$$
\boxed{
(D-3)E=(D-2)TS.
}
$$

The Smarr relation is therefore the compatibility of thermodynamic variation with scale homogeneity. In four dimensions, $E=2TS$.

The cosmological relation used in the amplitude closure is not the stationary Schwarzschild Smarr relation. It uses the canonically normalized horizontal causal-diamond temperature,

$$
k_BT_c=\frac{\hbar c}{2\pi R_c},
$$

together with the apparent-horizon area law and Misner--Sharp marginality to obtain

$$
T_cS_c=E_{\rm MS,c}.
$$

This distinction between vertical dynamical surface gravity and horizontal modular normalization is essential.

## Holography as a controlled laboratory

In a holographic code subspace, the JLMS relation takes the schematic form

$$
K_A^{\rm CFT}
=\frac{\widehat A(\chi_A)}{4G_N\hbar}
+K_a^{\rm bulk}
+\text{central term}
+O(G_N).
$$

Boundary modular charge decomposes into a geometric area charge and a bulk modular charge. In related controlled settings:

- the Hessian of relative entropy equals gravitational canonical energy;
- modular Berry curvature maps to gravitational symplectic structure;
- crossed-product gravitational algebras make generalized entropy a genuine von Neumann entropy for suitable subregions.

These results do not prove the FLRW scale-capacity law. They establish that modular charge, area, information Hessian, symplectic form, and gravity can form one coherent subregion structure.


# Horizontal perturbation geometry and the open spacetime lift

The homogeneous source is closed by the scale-capacity law. A complete physical theory must also determine inhomogeneous perturbations. This section records what is fixed by the binary state geometry and what remains open.

## Canonical Witten--Darboux pair

The binary information potential is

$$
\Psi(\theta)=\ln(2\cosh\theta),
$$

with

$$
\eta(\theta)=\Psi'(\theta)=\tanh\theta,
\qquad
\eta'(\theta)=\sech^2\theta.
$$

Define first-order operators

$$
\mathcal A=\partial_\theta+\eta,
\qquad
\mathcal A^\dagger=-\partial_\theta+\eta.
$$

Their partner Hamiltonians are

$$
\mathcal H_-:=\mathcal A^\dagger\mathcal A
=-\partial_\theta^2+\eta^2-\eta',
$$

$$
\mathcal H_+:=\mathcal A\mathcal A^\dagger
=-\partial_\theta^2+\eta^2+\eta'.
$$

Using $\eta^2+\eta'=1$ gives the exact factorization

$$
\boxed{
\mathcal H_-=-\partial_\theta^2+1-2\sech^2\theta,
}
$$

$$
\boxed{
\mathcal H_+=-\partial_\theta^2+1.
}
$$

Equivalently, define the two-component Dirac/Witten operator

$$
\boxed{
\mathcal D_\Psi=
\begin{pmatrix}
0&\mathcal A^\dagger\\
\mathcal A&0
\end{pmatrix},
\qquad
\mathcal D_\Psi^2=
\begin{pmatrix}
\mathcal H_-&0\\
0&\mathcal H_+
\end{pmatrix}.
}
$$

This pair is not an independently guessed Pöschl--Teller ansatz. It is generated canonically by the binary log-partition potential; reflectionless $\sech^2$ operators are a standard exactly solvable class ([33]).

## Bound mode, BKM density, and transparency

The zero-mode equation

$$
\mathcal A\psi_0=0
$$

has normalized solution

$$
\boxed{
\psi_0(\theta)=\frac1{\sqrt2}\sech\theta.
}
$$

Therefore

$$
\boxed{
2|\psi_0|^2=\sech^2\theta=G^{\BKM}_{\theta\theta}.
}
$$

The same function is simultaneously:

- the BKM/Fisher metric density;
- the normalized dark-history shape;
- the density of the unique bound mode of the Witten pair.

For continuum energy $1+k^2$, applying $\mathcal A^\dagger$ to a free wave gives

$$
\psi_k(\theta)=(-ik+\tanh\theta)e^{ik\theta}.
$$

At both asymptotic ends there is no $e^{-ik\theta}$ component, so

$$
\boxed{R(k)=0.}
$$

The continuum is transmitted with a phase shift; it is not absent. The correct statement is one normalizable bound mode plus a reflectionless continuum.

The Witten index is one, matching the unit topological charge of the Fisher kink. The total Fisher length is $\pi$, and the one-bound-state Levinson phase is also $\pi$; these are consequences of the same factorization rather than independent evidence.

## What this pair does and does not prove

The Witten pair closes the **internal horizontal operator geometry**. It explains why the fundamental pair is $\ell=1$, why there is one localized mode, and why the continuum is reflectionless.

It does not yet identify these operators with the physical scalar, vector, or tensor perturbation operators of an FLRW spacetime. A spacetime perturbation theory must specify:

- how inhomogeneous deformations of causal cuts induce horizontal state tangents;
- how the two-component Witten complex is embedded in spacetime constraints;
- how spatial gradients and causal propagation enter;
- which observable combination couples to matter and metric perturbations;
- whether the resulting system is ghost-free, hyperbolic, and regular at the crossing.

Thus the pair completion is canonical, but the spacetime lift remains open.

## Negative result: ordinary matter growth is not the pair operator

The standard smooth-dark-response matter-growth equation can be reduced to a Schrödinger-like zero-energy equation, but its effective potential contains ordinary matter and Hubble-friction terms. It is not proportional to $\rho_X$ and is not the Pöschl--Teller operator above.

Therefore transparency must not be imposed on the ordinary matter-growth equation. The Witten pair belongs to the internal horizontal response sector, not to a rebranding of standard growth.

## Negative result: canonical single-field completion

For a canonical single scalar, the kinetic normalization is proportional to $1+w_X$. In the rigid history,

$$
1+w_X=\frac23\tanh\theta,
$$

which is negative throughout the entire pre-crossing branch. At the crossing, the corresponding single-field mode function behaves as

$$
z\sim|\theta|^{1/2},
$$

so

$$
\frac{z''}{z}\sim-\frac1{4\theta^2},
$$

at the critical inverse-square coupling. The horizontal state coordinate therefore cannot be interpreted as an ordinary canonical local scalar field.

This is not a defect of the homogeneous free-energy construction. It says that the physical completion must be collective, constrained, multi-component, algebraic, or otherwise noncanonical.

## Perturbative stopping condition

A perturbative completion is adequate when it derives, without arbitrary functions,

1. a conserved $\delta T^X_{ab}$;
2. a regular crossing;
3. a finite number of propagating or constrained modes fixed by the Witten pair;
4. a definite gradient structure and sound/cone speed;
5. CMB, lensing, and growth responses that can be calculated in a Boltzmann code.

Until then, the background equations are closed but the theory is not a complete cosmological perturbation theory.


# Quantitative predictions, observational status, and kill conditions

## Parameter-free rigid branch

The rigid branch uses

$$
\Ruble=1,
\qquad
\vperp=1,
\qquad
\Lambda_{\rm res}=0,
\qquad
k=0.
$$

The present ordinary matter and radiation abundances are observational inputs, not dark-sector fit parameters. The crossing date is then fixed by present flatness.

## P1 — differential shape invariant

The primary test is

$$
\boxed{
9(1+w_X(z))^2+6\frac{\dd w_X}{\dd N}=4.
}
$$

This constrains the whole reconstructed history. It is independent of the amplitude and crossing date.

**Kill condition K1.** A statistically significant redshift dependence of the left-hand side, after accounting for reconstruction covariance, rejects the binary affine theory.

## P2 — local tangent locus

At the present epoch, the exact history has CPL tangent

$$
\boxed{
w_a=\frac32(1+w_0)^2-\frac23.
}
$$

For the benchmark,

$$
(w_0,w_a)=(-0.80945,-0.61221).
$$

This is a compressed diagnostic only; the exact pulse should be fitted directly.

**Kill condition K2.** A clean posterior excluding this locus rejects the rigid branch.

## P3 — self-dual crossing and equality

The model predicts

$$
\boxed{
z_c=0.34179,}
$$

and the exact coincidence

$$
\boxed{
\rho_X(N_c)=\rho_{\rm ordinary}(N_c),
\qquad
w_X(N_c)=-1.
}
$$

Relative to dust alone, the ratio is $1.000395$ because radiation is small but nonzero.

**Kill condition K3.** Independent reconstructions of the $w=-1$ crossing and ordinary--dark equality that disagree beyond errors reject the scale-capacity normalization.

## P4 — observed acceleration entry and future exit

The benchmark predicts

$$
\boxed{z_{\rm acc}=0.78569}
$$

for the past entry into acceleration, and

$$
\boxed{a_{\rm exit}/a_0=11.7865}
$$

for the future exit. The crossing/equality event is not the acceleration onset.

The future tends to

$$
w_X\to-\frac13,
\qquad
a(t)\sim t,
$$

with no permanent event horizon if and only if the residual floor is exactly zero.

## P5 — present cosmography

The rigid benchmark predicts

$$
\boxed{q_0=-0.33690,}
$$

$$
\boxed{j_0=-0.11125.}
$$

The jerk is separated by order unity from the flat-$\Lambda$CDM value $j=1$.

**Kill condition K4.** A robust model-independent reconstruction near $j_0=1$ and inconsistent with the value above strongly rejects the rigid history.

## P6 — dimension and crossing fraction

In $d$ spatial dimensions, the scale-capacity law predicts

$$
\boxed{
\Omega_{X,c}=\frac{1}{d-1},
\qquad
\frac{\rho_{X,c}}{\rho_{\rm ordinary,c}}=\frac1{d-2}.
}
$$

The equal partition occurs only for $d=3$. This is not an empirical prediction within our already observed dimension; it is a structural consistency condition relevant to dimensional-selection attempts.

## P7 — horizontal operator structure

The internal response geometry predicts the Witten pair

$$
\mathcal H_-=-\partial_\theta^2+1-2\sech^2\theta,
\qquad
\mathcal H_+=-\partial_\theta^2+1,
$$

with one bound mode and reflectionless continuum.

**Kill condition K5.** A derived spacetime completion whose horizontal response has a different bound-state count or cannot realize the pair invalidates the claimed canonical perturbation structure.

## Current background comparison

The previously completed background-only analysis of public DESI distance data and Pantheon+ supernovae gives approximately ([34,36,37])

| model | background shape parameters | joint $\chi^2$ |
|---|---:|---:|
| flat $\Lambda$CDM | 1 | 1401.63 |
| rigid capacity-normalized history | 1 | 1398.29 |
| flexible pulse | 3 | 1397.26 |

The rigid history is viable and modestly improves this restricted statistic at equal background shape-parameter count. These values are not a discovery significance. The comparison excludes primary CMB, full lensing, growth, and a derived dark perturbation likelihood.

## Neutrino residual

Current cosmological analyses infer an unusually tight neutrino-mass bound in flat $\Lambda$CDM and, under a formal continuation, can prefer an effective negative response ([35]). Allowing evolving late-time geometry substantially weakens that result.

The rigid history has the correct qualitative structure to address the residual:

- it modifies low- and intermediate-redshift expansion with opposite signs relative to a matched $\Lambda$CDM history;
- its smooth-growth response increases CMB lensing in the direction opposite positive neutrino mass;
- a geometry-level pushforward places weight near a normal-ordering sum of order $0.07$--$0.08$ eV.

However, null ensembles show that the lensing anti-alignment is common among smooth positive transient histories. The neutrino calculation is therefore a necessary class-membership test, not a distinctive confirmation.

A direct CLASS/CAMB implementation with a derived perturbation closure is required before the neutrino anomaly can be claimed as a prediction or resolution.

## Epistemic status of the observational evidence

The current evidence supports:

1. compatibility of the rigid background with present distance data;
2. current dynamical-dark-energy summaries lying near the invariant's natural value;
3. a redshift structure capable of reducing the neutrino residual.

It does not establish:

1. the scale-capacity principle for FLRW causal walls;
2. a complete perturbation theory;
3. the global zero-floor sector;
4. a statistically preferred particle-mass posterior under the full model.


# Economy, epicycles, and the novelty test

## Four distinct economies

Parameter count alone is not explanatory economy. Distinguish:

$$
\begin{aligned}
\mathcal E_{\rm fit}&=\text{number of continuously fitted parameters},\\
\mathcal E_{\rm law}&=\text{number of independently postulated laws or functions},\\
\mathcal E_{\rm ontology}&=\text{number of new fields, fluids, or forces},\\
\mathcal E_{\rm consequence}&=\text{number of predictions locked together}.
\end{aligned}
$$

Epicycles fail principally because corrections are independently adjustable. A fixed but unexplained function can have zero fitted parameters and still be ad hoc.

The rigid causal-scale theory has no continuously fitted dark-history shape parameter once its equivalence principle and global sector are fixed. More importantly, one structure ties together:

- one density maximum;
- one $w=-1$ crossing;
- the full differential invariant;
- one acceleration interval;
- a future separatrix;
- the self-dual amplitude;
- a canonical horizontal Witten pair;
- local blindness to central vacuum shifts.

This is a stronger kind of economy than low parameter count alone.

## Economical competitors

Several existing cosmologies are also economical at the background level ([38-40]):

- flat $\Lambda$CDM has one constant vacuum term;
- phenomenological emergent dark-energy models can have no extra fitted parameter;
- vacuum metamorphosis derives a late transition from a curvature-triggered quantum effect;
- running-vacuum models use a small number of QFT-inspired coefficients;
- hyperbolic-tangent crossing models can closely resemble the rigid background with two fitted shape parameters.

The present framework is not unique because it uses a $\sech^2$ profile or because it fits without a free $w_0,w_a$ pair. Its claim to novelty is the proposed identity

$$
\boxed{
\text{Weyl-scale translation}
\longrightarrow
\text{horizontal modular-state displacement}
\longrightarrow
\text{BKM capacity}
\longrightarrow
\text{gravitational free-energy density}.
}
$$

If that chain is independently constructed, the profile is a consequence. If the chain is only inferred from the fitted expansion history, the model is an effective fluid in new notation.

## Musical-chairs test

The decisive criterion is:

$$
\boxed{
\begin{array}{ll}
\theta\text{ is defined only by rearranging }H(z)
&\Rightarrow\text{relabelled fluid},\\[1mm]
\theta\text{ is defined by an independent causal-state construction}
&\Rightarrow\text{new physical structure}.
\end{array}}
$$

The present theory addresses this by defining $\theta$ as the noncentral Connes-cocycle coordinate of a scale-indexed wall-state family and by identifying the active quotient with normal chirality. The full construction for a dynamical FLRW wall remains to be carried out.

## Assumption ledger after closure

The homogeneous theory now contains:

| item | status |
|---|---|
| causal conformal geometry plus scale | standard mathematical factorization |
| local modular/gravitational boost-charge identity | physical equivalence principle used for the local source equation |
| fundamental normal chirality quotient | structural identification of the active homogeneous mode |
| affine cocycle soldering | theorem given rank-one ratio dependence and measurability |
| fundamental representation $\vperp=1$ | physical representation choice / unit character |
| scale--capacity number $\Ruble=1$ | physical equivalence principle closing the amplitude |
| separate homogeneous conservation | effective-sector assumption pending covariant completion |
| $\Lambda_{\rm res}=0$ | global sector choice |
| spatial flatness | empirical/background sector choice |

It is therefore not correct to say that mathematics alone derives every premise. It is correct to say that one compact equivalence law replaces the former free amplitude and that the resulting background history contains no adjustable dark function.

## Stopping condition

A foundational theory is not required to derive every axiom from something deeper. It is adequate when:

1. primitive quantities are operationally and mathematically typed;
2. independent representations are connected by explicit equivalence laws;
3. no hidden functions are introduced to fit individual anomalies;
4. the laws produce many linked predictions;
5. the theory states clear failure conditions;
6. further elaboration concerns new regimes, not repair of the background law.

By this standard, the homogeneous theory has reached a defensible stopping point:

$$
\boxed{
\left.\frac{k_B}{S_c}G^{\perp}_{NN}\right|_{N_c}=1
}
$$

is taken as a fundamental scale-capacity equivalence principle. The background equations and amplitude follow. The perturbation lift and global vacuum sector are separate layers, not unresolved coefficients in the homogeneous model.


# Audit of the proposed final closure

The attached AI closure contains a valuable synthesis but also two invalid deductions. This section records the audit so that the final theory does not inherit attractive category errors.

## Useful conclusions retained

The closure correctly emphasizes:

1. vertical and horizontal modular sectors must remain distinct;
2. the BKM Hessian of a modular rescaling family is a capacity/variance;
3. a self-dual crossing is the natural place to evaluate the response;
4. the homogeneous theory should end with one structural law rather than an indefinitely expanding assumption ledger;
5. the perturbation sector remains open even after background closure.

These points are incorporated into the present formulation.

## Rejected claim: conformal-weight integrality

The proposed argument stated that

$$
\mathcal E[1]\oplus\mathcal E[-1]
$$

forces

$$
\vperp\in\mathbb Z,
$$

and that an observational existence ceiling then selects $\vperp=1$.

That does not follow. Conformal density bundles $\mathcal E[w]$ exist for real weights $w$; the representation theory of the positive scale group admits continuous real characters. There is no general integrality theorem.

The valid statement is narrower:

> The fundamental null-normal pair and the fundamental scale/inverse-scale pair both carry characters $e^{\pm x}$. Identifying those fundamental representations gives $\vperp=1$ as a physical representation choice.

The existence ceiling is a prediction and consistency bound. It cannot be used to derive a universal constant from measured $\Omega_m$ without making the derivation data dependent and circular.

## Rejected claim: the normal plane is a two-dimensional CFT

The closure argued that the normal plane is two-dimensional, so Cardy thermodynamics gives $C=S$ and hence the capacity ratio equals one.

A two-dimensional Lorentzian normal vector space is not, by that fact alone, a $1+1$ dimensional conformal quantum field theory. Cardy's formula requires a CFT, a Hamiltonian, central charge, boundary conditions, and a thermodynamic regime. The dimension of the normal plane does not supply these structures.

The valid replacement is:

> Capacity equals entropy in specific Einstein-holographic spherical settings and is conjectured or supported for certain causal horizons. This motivates a universality principle for the self-dual Einstein wall; it is not a consequence of dimensionality alone.

## Why the revised closure is stronger

The final law does not require an integrality theorem or an assumed 2D CFT:

$$
\boxed{
\Ruble
=\frac{k_B}{S_c}G^{\perp}_{NN}(N_c)=1.
}
$$

It is coordinate invariant and combines the slope and capacity normalization into one measurable quantity. Existing capacity--entropy results supply precedent, while Hawking--Friedmann thermodynamics supplies the dimensional conversion.

The consequences are then algebraic:

$$
\Omega_{X,c}=\frac12,
$$

$$
\rho_X(N_c)=\rho_{\rm ordinary}(N_c),
$$

and in general spatial dimension

$$
\Omega_{X,c}=\frac1{d-1}.
$$

This is an explicitly stated equivalence principle with falsifiable consequences, not a theorem obtained by smuggling in observed cosmological parameters.


# Status, stopping principle, and research programme

## What is closed

Conditional on the stated equivalence principles, the homogeneous theory now fixes:

- the mathematical type of scale;
- the local trace-free gravitational source equation;
- the horizontal binary state geometry;
- affine state--scale soldering;
- the unit shape coefficient;
- the amplitude at the self-dual crossing;
- the entire background density and equation-of-state history;
- the sign change of acceleration;
- the future coasting branch;
- the differential invariant and other observational tests.

There is no arbitrary function $w(z)$, no free dark-energy particle potential, and no fitted late-time amplitude.

## What is not closed

The following remain separate research layers:

1. **FLRW causal-wall construction.** Build the scale-indexed local algebras and states for a dynamical FLRW apparent horizon and derive the horizontal cocycle directly.
2. **Perturbation lift.** Embed the canonical Witten pair into a covariant scalar/vector/tensor perturbation system.
3. **Global vacuum sector.** Derive or select the residual top-form/tractor-norm sector, including whether $\Lambda_{\rm res}=0$.
4. **Initial state and arrow.** Explain the low-Weyl, low-variance boundary condition and the selection of the expanding orientation.
5. **Full likelihood.** Implement the perturbation completion in a Boltzmann solver and test CMB, lensing, growth, BAO, and supernovae jointly.

These do not reopen the homogeneous dark-history amplitude. They decide whether the framework extends beyond its closed background sector.

## Research priorities

1. Construct the self-dual FLRW causal diamond and calculate $G^{\perp}_{NN}/(S/k_B)$ from modular data rather than postulating it.
2. Derive the spacetime perturbation operator from deformations of the causal-cut family and compare it with the Witten pair.
3. Test the invariant nonparametrically from reconstructed $w(z)$.
4. Test the predicted coincidence of equality and $w=-1$ crossing.
5. Perform the direct Boltzmann likelihood, with the neutrino residual treated as a secondary structured test.
6. Study the dimension formula as a possible consistency principle rather than a claim that spatial dimensionality has already been derived.

## Falsifiability

The homogeneous framework is false if any of the following is established:

- the redshift-dependent invariant is not constant or not four;
- the self-dual crossing fraction is not one half;
- equality and $w=-1$ crossing are significantly separated;
- the required crossing date conflicts with flatness and the ordinary budget;
- the dark history has multiple maxima or repeated crossing episodes;
- a derived perturbation completion necessarily introduces unstable or arbitrarily tunable modes;
- the FLRW wall capacity ratio is calculated and is inconsistent with unity.

The scale-tractor reformulation and local vacuum-blind quotient can survive failure of the late-time capacity model; the theory is deliberately modular in its logical dependencies.


# Conclusion

Causal Scale Dynamics begins from a standard theorem-level distinction: causal order determines conformal geometry but not physical scale. The scale is a section $\sigma\in\Gamma(\mathcal E[1])$, and its two-jet is packaged by the scale tractor. In this language, trace-free stress is the obstruction to parallel scale transport, while the scalar curvature and cosmological lift occupy a separate norm channel.

The quantum register supplies a second geometry. A causal region and state carry modular structure; relative entropy supplies a BKM Hessian. The corrected theory distinguishes vertical modular automorphism flow from horizontal change of the state family. Homogeneous normal chirality gives a binary exponential family with

$$
\eta=\tanh\theta,
\qquad
G^{\BKM}_{\theta\theta}=\sech^2\theta.
$$

Cocycle composition makes the horizontal coordinate affine in Weyl scale. The fundamental representation sets

$$
\theta=N-N_c.
$$

The remaining amplitude is closed by the Scale--Capacity Equivalence Principle,

$$
\boxed{
\left.\frac{k_B}{S_c}G^{\perp}_{NN}\right|_{N_c}=1.
}
$$

Relative entropy converts this dimensionless response into modular free-energy curvature, and horizon thermodynamics supplies the units:

$$
\rho_X=\frac{k_BT_c}{2V_c}G^{\perp}_{NN},
$$

$$
T_cS_c=E_{\rm MS,c}=\rho_{\rm crit,c}V_c.
$$

Therefore, in $3+1$ dimensions,

$$
\boxed{
\rho_X(N)=\frac12\rho_{\rm crit,c}\sech^2(N-N_c).
}
$$

At self-duality,

$$
\boxed{
\rho_X=\rho_{\rm ordinary},
\qquad
w_X=-1,
\qquad
\Omega_X=\frac12.
}
$$

Separate conservation gives

$$
\boxed{
w_X=-1+\frac23\tanh(N-N_c),
}
$$

and the structural test

$$
\boxed{
9(1+w_X)^2+6w_X'=4.
}
$$

The observed acceleration transition follows from the changing balance between the ordinary sector and this one self-dual response. It is not generated by an independently postulated repulsive force. The same law predicts a future exit and asymptotic coasting when the global residual floor is exactly zero.

The theory has therefore reached a legitimate homogeneous stopping point: one clearly stated equivalence principle replaces the former amplitude postulate and produces a closed, economical background history. The next problems are not further adjustment of that history. They are the construction of the dynamical FLRW wall, the covariant perturbation lift, and the global vacuum sector.

The central retyping is:

$$
\boxed{
\text{late cosmic response is the modular free-energy curvature of causal-state change under scale.}
}
$$

This statement is precise enough to inspire independent mathematical construction and sufficiently constrained to be rejected by observation.


\appendix

# Symbol dictionary

| symbol | definition | mathematical type / status |
|---|---|---|
| $(M,[g])$ | conformal spacetime | standard Lorentzian conformal geometry |
| $\boldsymbol g$ | conformal metric | section of the weighted metric bundle |
| $\sigma\in\Gamma(\mathcal E[1])$ | positive scale | density-bundle section |
| $g_{\rm phys}=\sigma^{-2}\boldsymbol g$ | physical metric | conformally invariant combination |
| $I_A=\tfrac14D_A\sigma$ | scale tractor | packages the scale two-jet |
| $P_{ab}$ | Schouten tensor | standard conformal curvature tensor |
| $N=-\ln(\sigma/\sigma_c)$ | Weyl e-fold coordinate | additive scale displacement |
| $s$ | vertical modular automorphism parameter | state-preserving modular flow |
| $\eta_A$ | vertical horizon rapidity potential | geometric definition; modular interpretation conditional |
| $\theta$ | horizontal state coordinate | noncentral relative modular polarization |
| $Q=P_+-P_-$ | normal chirality | binary quotient, $Q^2=1$, $JQJ=-Q$ |
| $\Psi(\theta)=\ln(2\cosh\theta)$ | log-partition potential | binary exponential family |
| $\eta=\langle Q\rangle$ | mixture coordinate | $\eta=\tanh\theta$ |
| $G^{\rm BKM}$ | BKM metric | Hessian of Umegaki relative entropy |
| $G^{\perp}_{NN}$ | pullback BKM norm | extensive horizontal capacity per squared e-fold |
| $S_c$ | self-dual wall entropy | Bekenstein--Hawking entropy in the closure law |
| $T_c$ | horizontal modular temperature | canonical $2\pi$ normal-boost normalization |
| $V_c$ | causal-wall volume | areal volume of the crossing apparent horizon |
| $\Ruble$ | scale-capacity number | $(k_B/S_c)G^{\perp}_{NN}(N_c)$; fundamental value $1$ |
| $\vperp$ | horizontal soldering slope | $d\theta/dN$; fundamental representation value $1$ |
| $\rho_X,p_X,w_X$ | effective homogeneous response variables | derived from the scale-capacity source and conservation |
| $N_c,z_c$ | self-dual crossing location | intrinsic event, cosmic date fixed by the solution |
| $\mu_A$ | horizon modular--Weyl index | $(1-q)/2=-I^2/H^2$; running state variable |
| $\Lambda_g,\Lambda_{\rm res}$ | scalar lift/global residual | global sector, not local trace-free source |
| $\mathcal A,\mathcal A^\dagger$ | Witten/Darboux first-order operators | generate the horizontal pair |
| $\mathcal H_\pm$ | horizontal partner operators | one reflectionless Pöschl--Teller partner and one free partner |

# Core derivations

## Binary information geometry

For

$$
\omega_\theta=\frac{e^{\theta Q}}{2\cosh\theta},
\qquad Q^2=1,
$$

the partition potential is

$$
\Psi=\ln\operatorname{tr}e^{\theta Q}=\ln(2\cosh\theta).
$$

Therefore

$$
\Psi'=\tanh\theta,
\qquad
\Psi''=\sech^2\theta,
$$

and

$$
\langle Q\rangle^2+\operatorname{Var}(Q)=1.
$$

## Cocycle soldering

Assume the reduced noncentral Connes cocycle depends on two scales only through $r=\sigma_2/\sigma_1$ and is measurable. Cocycle composition gives

$$
\theta(r_1r_2)=\theta(r_1)+\theta(r_2).
$$

The measurable solutions are

$$
\theta(r)=-\vperp\ln r.
$$

Since $N=-\ln(\sigma/\sigma_c)$,

$$
\theta=\vperp(N-N_c).
$$

The equation fixes the form but not the value of $\vperp$.

## Free-energy Hessian

For a KMS reference state with physical modular Hamiltonian $\mathcal H_c=k_BT_cK_c$,

$$
F_c(\rho)-F_c(\omega_c)=k_BT_cS(\rho\|\omega_c).
$$

At coincidence,

$$
S(\omega_{c+\delta N}\|\omega_c)
=\frac12G^{\perp}_{NN}(N_c)\delta N^2+O(\delta N^3).
$$

Therefore the quadratic free-energy curvature per causal-wall volume is

$$
\rho_{X,c}=\frac{k_BT_c}{2V_c}G^{\perp}_{NN}(N_c).
$$

## Hawking--Friedmann conversion

In $3+1$ dimensional flat FLRW,

$$
R_c=\frac{c}{H_c},
\quad
\frac{S_c}{k_B}=\frac{\pi R_c^2c^3}{G\hbar},
\quad
k_BT_c=\frac{\hbar c}{2\pi R_c}.
$$

Thus

$$
k_BT_c\frac{S_c}{k_B}=\frac{c^4R_c}{2G}=E_{\rm MS,c}.
$$

Since

$$
V_c=\frac{4\pi R_c^3}{3},
$$

$$
\frac{E_{\rm MS,c}}{V_c}=\frac{3c^4}{8\pi GR_c^2}=\frac{3c^2H_c^2}{8\pi G}=\rho_{\rm crit,c}.
$$

## Scale-capacity amplitude

The equivalence law is

$$
G^{\perp}_{NN}(N_c)=\Ruble\frac{S_c}{k_B}.
$$

Therefore

$$
\rho_{X,c}=\frac{\Ruble}{2}\rho_{\rm crit,c}.
$$

For $\Ruble=1$, flatness gives

$$
\rho_{X,c}=\rho_{\rm ordinary,c}=\frac12\rho_{\rm crit,c}.
$$

## General dimension

For $d$ spatial dimensions,

$$
A=\Omega_{d-1}R^{d-1},
\qquad
V=\frac{\Omega_{d-1}}{d}R^d,
$$

and Einstein--Friedmann marginality gives

$$
\frac{k_BT(S/k_B)}{V}=\frac{2}{d-1}\rho_{\rm crit}.
$$

Thus

$$
\Omega_{X,c}=\frac{\Ruble}{d-1},
$$

and

$$
\frac{\rho_{X,c}}{\rho_{\rm ordinary,c}}=
\frac{\Ruble}{d-1-\Ruble}.
$$

## Shape invariant

With

$$
\rho_X=\rho_*\sech^2(N-N_c),
$$

$$
\Delta_X:=-\frac{\dd\ln\rho_X}{\dd N}=2\tanh(N-N_c).
$$

Then

$$
\Delta_X'=2\sech^2(N-N_c)=2-\frac12\Delta_X^2,
$$

so

$$
\Delta_X^2+2\Delta_X'=4.
$$

Using $\Delta_X=3(1+w_X)$ gives

$$
9(1+w_X)^2+6w_X'=4.
$$

## Witten pair

Let $\eta=\tanh\theta$. Then

$$
\eta^2+\eta'=1.
$$

With

$$
\mathcal A=\partial_\theta+\eta,
\qquad
\mathcal A^\dagger=-\partial_\theta+\eta,
$$

$$
\mathcal A^\dagger\mathcal A=-\partial_\theta^2+1-2\sech^2\theta,
$$

$$
\mathcal A\mathcal A^\dagger=-\partial_\theta^2+1.
$$

The normalized zero mode is $\psi_0=2^{-1/2}\sech\theta$.


# Receipt, data, and audit ledger

The accompanying script `receipts/receipts_v7.py` verifies the exact identities and benchmark values used in this note. The machine-readable output is `receipts/receipts_v7.json`; the expected field is

```json
"all_exact_residuals_zero": true
```

The receipts verify:

- binary moments and the BKM metric;
- affine-shape identities;
- Fisher length $\pi$;
- the Witten/Darboux factorization and zero mode;
- Hawking--Friedmann conversion;
- the dimension-dependent crossing fraction;
- the closed benchmark and radiation correction;
- present cosmography and the two acceleration transitions.

The package includes the earlier background-fit, direct-response, and economy-audit results used for the observational status section. These analyses use different baselines and are not combined as independent measurements.

The attached AI referee notes were used as adversarial inputs. Their useful results and rejected claims are recorded in the body. In particular:

- the cocycle argument for affine soldering was retained;
- the vertical/horizontal distinction was retained;
- the warnings about the sigma-model completion and response normalization were retained;
- conformal-weight integrality and the identification of a two-dimensional normal plane with a two-dimensional CFT were rejected.

# Epistemic status ledger

| statement | status |
|---|---|
| causal order fixes conformal geometry under standard hypotheses | standard theorem |
| scale as $\Gamma(\mathcal E[1])$ and scale tractor | standard conformal geometry |
| Einstein metric iff parallel scale tractor | standard theorem |
| trace-free tractor source equation | exact reformulation of GR |
| modular/gravitational boost-charge identity | physical unity principle, supported in controlled settings |
| fundamental normal chirality quotient | structural identification |
| affine cocycle law | conditional theorem from ratio dependence and measurability |
| $\vperp=1$ | fundamental representation choice |
| binary BKM metric $\sech^2\theta$ | exact after chirality reduction |
| scale--capacity number $\Ruble=1$ | fundamental equivalence principle |
| free-energy source law | constitutive definition motivated by relative entropy |
| Hawking--Friedmann conversion | exact horizon/Friedmann identity in the stated regime |
| closed homogeneous pulse | deduction from the preceding laws |
| Witten pair | exact internal horizontal construction |
| covariant perturbation theory | open |
| zero residual floor | global sector choice |
| sequestering completion | published candidate, not derived from the scale-capacity law |

# References

1. S. W. Hawking, A. R. King, and P. J. McCarthy, “A new topology for curved space-time which incorporates the causal, differential, and conformal structures,” *J. Math. Phys.* **17** (1976) 174.
2. D. B. Malament, “The class of continuous timelike curves determines the topology of spacetime,” *J. Math. Phys.* **18** (1977) 1399.
3. T. N. Bailey, M. G. Eastwood, and A. R. Gover, “Thomas’s structure bundle for conformal, projective and related structures,” *Rocky Mountain J. Math.* **24** (1994) 1191.
4. S. Curry and A. R. Gover, “An introduction to conformal geometry and tractor calculus, with a view to applications in general relativity,” [arXiv:1412.7559](https://arxiv.org/abs/1412.7559).
5. A. R. Gover, “Almost Einstein and Poincaré–Einstein manifolds in Riemannian signature,” *J. Geom. Phys.* **60** (2010) 182.
6. J. J. Bisognano and E. H. Wichmann, “On the duality condition for quantum fields,” *J. Math. Phys.* **17** (1976) 303.
7. H. Casini, M. Huerta, and R. C. Myers, “Towards a derivation of holographic entanglement entropy,” [arXiv:1102.0440](https://arxiv.org/abs/1102.0440).
8. R. M. Wald, “Black hole entropy is the Noether charge,” [arXiv:gr-qc/9307038](https://arxiv.org/abs/gr-qc/9307038).
9. T. Jacobson, “Thermodynamics of spacetime: The Einstein equation of state,” [arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004).
10. T. Jacobson, “Entanglement equilibrium and the Einstein equation,” [arXiv:1505.04753](https://arxiv.org/abs/1505.04753).
11. D. L. Jafferis, A. Lewkowycz, J. Maldacena, and S. J. Suh, “Relative entropy equals bulk relative entropy,” [arXiv:1512.06431](https://arxiv.org/abs/1512.06431).
12. N. Lashkari and M. Van Raamsdonk, “Canonical energy is quantum Fisher information,” [arXiv:1508.00897](https://arxiv.org/abs/1508.00897).
13. B. Czech, L. Lamprou, S. McCandlish, and J. Sully, “Modular Berry Connection,” [arXiv:1712.07123](https://arxiv.org/abs/1712.07123).
14. B. Czech et al., “Changing states in holography: From modular Berry curvature to the bulk symplectic form,” [arXiv:2305.16384](https://arxiv.org/abs/2305.16384).
15. D. Petz, “Monotone metrics on matrix spaces,” *Linear Algebra Appl.* **244** (1996) 81.
16. N. N. Čencov, *Statistical Decision Rules and Optimal Inference*, AMS (1982).
17. S.-I. Amari and H. Nagaoka, *Methods of Information Geometry*, AMS/Oxford (2000).
18. M. R. Grasselli and R. F. Streater, “On the uniqueness of the Chentsov metric in quantum information geometry,” [arXiv:math-ph/0006030](https://arxiv.org/abs/math-ph/0006030).
19. R. Chatterjee, “Modular Self-Duality, Symmetrized Relative Entropy, and Bogoliubov–Kubo–Mori Susceptibility in Quantum Field Theory,” [arXiv:2605.19106](https://arxiv.org/abs/2605.19106).
20. K. Jensen, J. Sorce, and A. Speranza, “Generalized entropy for general subregions in quantum gravity,” [arXiv:2306.01837](https://arxiv.org/abs/2306.01837).
21. T. Faulkner and A. J. Speranza, “Gravitational algebras and the generalized second law,” [arXiv:2405.00847](https://arxiv.org/abs/2405.00847).
22. V. Chandrasekaran and É. É. Flanagan, “Subregion algebras in classical and quantum gravity,” [arXiv:2601.07915](https://arxiv.org/abs/2601.07915).
23. S. A. Hayward, “Unified first law of black-hole dynamics and relativistic thermodynamics,” [arXiv:gr-qc/9710089](https://arxiv.org/abs/gr-qc/9710089).
24. R.-G. Cai and S. P. Kim, “First law of thermodynamics and Friedmann equations of the Friedmann–Robertson–Walker universe,” [arXiv:hep-th/0501055](https://arxiv.org/abs/hep-th/0501055).
25. M. Akbar and R.-G. Cai, “Thermodynamic behavior of Friedmann equation at apparent horizon of FRW universe,” [arXiv:hep-th/0609128](https://arxiv.org/abs/hep-th/0609128).
26. J. de Boer, J. Järvelä, and E. Keski-Vakkuri, “Aspects of capacity of entanglement,” [arXiv:1807.07357](https://arxiv.org/abs/1807.07357).
27. T. Banks and K. M. Zurek, “Conformal description of near-horizon vacuum states,” *Phys. Rev. D* **104**, 126026 (2021), [arXiv:2108.04806](https://arxiv.org/abs/2108.04806).
28. T. Banks and P. Draper, “Generalized entanglement capacity of de Sitter space,” [arXiv:2404.13684](https://arxiv.org/abs/2404.13684).
29. D. Kastor, S. Ray, and J. Traschen, “Enthalpy and the mechanics of AdS black holes,” [arXiv:0904.2765](https://arxiv.org/abs/0904.2765).
30. N. Kaloper, A. Padilla, D. Stefanyszyn, and G. Zahariade, “A manifestly local theory of vacuum energy sequestering,” [arXiv:1505.01492](https://arxiv.org/abs/1505.01492).
31. N. Kaloper and A. Padilla, “Vacuum energy sequestering and graviton loops,” [arXiv:1606.04958](https://arxiv.org/abs/1606.04958).
32. A. Vikman, “Can dark energy evolve to the phantom?” [arXiv:astro-ph/0407107](https://arxiv.org/abs/astro-ph/0407107).
33. J. Lekner, “Reflectionless eigenstates of the $\sech^2$ potential,” *Am. J. Phys.* **75** (2007) 1151.
34. DESI Collaboration, “DESI DR2 results: measurements of baryon acoustic oscillations and cosmological constraints,” [arXiv:2503.14738](https://arxiv.org/abs/2503.14738).
35. DESI Collaboration, “DESI DR2 results: neutrino mass constraints,” [arXiv:2503.14744](https://arxiv.org/abs/2503.14744).
36. DESI Collaboration, “DESI DR2 Results IV: Ly$\alpha$-forest full-shape measurements and cosmological constraints,” [arXiv:2607.27410](https://arxiv.org/abs/2607.27410).
37. D. Brout et al., “The Pantheon+ analysis: cosmological constraints,” [arXiv:2202.04077](https://arxiv.org/abs/2202.04077).
38. X. Li and A. Shafieloo, “A simple phenomenological emergent dark energy model,” [arXiv:1906.08275](https://arxiv.org/abs/1906.08275).
39. L. Parker and A. Raval, “Vacuum-driven metamorphosis,” [arXiv:gr-qc/0312108](https://arxiv.org/abs/gr-qc/0312108).
40. J. Solà Peracaula et al., “Running vacuum in the Universe,” [arXiv:2203.13757](https://arxiv.org/abs/2203.13757).

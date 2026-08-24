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

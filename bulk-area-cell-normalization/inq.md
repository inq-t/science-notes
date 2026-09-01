---
inq.module: "bulk-area-cell-normalization"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
---
# Bulk--Area Cell Normalization

If the crossing ledger is literally the response weight of uniform correlation cells in a spherical Hubble bulk, ordinary Euclidean geometry fixes the formerly free coefficient: \(\zeta=\gamma s_*/3\), and hence \(\zeta=s_*/3\) for one species at unit packing. This exact normalization makes the coefficient and the per-cell weight one unknown in the minimal model, sharpens the carrier target to roughly \(57\)--\(62\,\mathrm{MeV}\), and exposes the still-open theorem: an average areal count, a local BKM wall modulus, a bulk correlation cell, and a boundary area cell are different objects until explicit maps identify them.

## The meaning of the factor \(1/3\)

The symbol \(\zeta\) in this module is the fossil bulk coefficient, more explicitly \(\zeta_{\mathrm{bulk}}\). It is never the signed horizon rapidity \(\widehat\zeta_A\) used by [[conformal-scale-geometry/horizon-allocation|horizon allocation]].

The factor is not an exceptional-group coefficient and not a fit. It is the ratio of the volume of a three-ball to its boundary area:

$$
V(R)=\frac{4\pi}{3}R^3,
\qquad
A(R)=4\pi R^2,
\qquad
\frac{V(R)}{A(R)}=\frac R3.
$$

Consequently, a uniform response density of one weighted cell per volume \(\lambda_*^3\) induces an areal response density with the coefficient \(1/3\). The result is exact **if** the literal spherical bulk-cell reading is the correct physical projection. Geometry fixes the coefficient only after that reading has been adopted.

The source audit in `inbox/the-carrier-and-zeta/the-carrier-and-zeta.md` first pushed this normalization through both cosmological branches and the fitted response interval. Its extended receipt also tests candidate masses, occupancies, Bianchi propagation, and kernel positivity. This module owns only the cell-normalization result.

## The normalization proposition

Let the selected crossing cut have apparent-horizon radius \(R_c\), area \(A_c=4\pi R_c^2\), and enclosed Euclidean volume \(V_c=4\pi R_c^3/3\). Let \(\lambda_*\) be a physical correlation length and let

$$
N_{\mathrm{bulk}}
:=\gamma\frac{V_c}{\lambda_*^3}
=\gamma\frac{4\pi}{3}
\left(\frac{R_c}{\lambda_*}\right)^3.
$$

Here \(\gamma>0\) is the total degeneracy, packing, and projection factor. Until a microscopic model constructs actual discrete cells, \(N_{\mathrm{bulk}}\) is an effective dimensionless count, not necessarily an integer.

Suppose each bulk cell contributes a dimensionless response weight \(s_*\), and suppose the crossing ledger is exactly the total bulk response:

$$
\iota_{A,c}=s_*N_{\mathrm{bulk}}.
$$

The integrated ledger determines the average areal density

$$
\bar\chi_c
:=\frac{\iota_{A,c}}{A_c}
=\frac{\gamma s_*}{3}
\frac{R_c}{\lambda_*^3}.
$$

Comparing this with the fossil parametrization

$$
\bar\chi_c=\zeta\frac{R_c}{\lambda_*^3}
$$

gives

$$
\boxed{
\zeta=\frac{\gamma s_*}{3}.
}
$$

For one species at unit packing and unit projection, \(\gamma=1\), so

$$
\boxed{
\zeta=\frac{s_*}{3},
\qquad
\iota_{A,c}
=s_*\frac{4\pi}{3}
\left(\frac{R_c}{\lambda_*}\right)^3.
}
$$

Thus \(\zeta\) and \(s_*\) are one unknown only in the minimal \(\gamma=1\) reading. A proposed \(\gamma\ne1\) must be derived; it cannot be reintroduced merely to rescue a preferred carrier mass.

The bar is load-bearing. The quotient \(\iota_{A,c}/A_c\) is an integrated or average density. Identifying it with a local Radon--Nikodym or BKM modulus \(\chi_c(x)\) requires a homogeneous wall state and an explicit bulk-to-boundary projection that makes \(\chi_c(x)=\bar\chi_c\) almost everywhere. The cell geometry alone does not prove that local identification.

## What \(s_*\) means

In the counting ansatz, \(s_*\) is the dimensionless response weight assigned to one effective bulk cell. Calling it an **entropy per cell** is legitimate only after a theorem identifies the extensive wall response with a logarithmic entropy or record capacity. A BKM Hessian is a positive quadratic response, not itself an entropy.

[[deriving-g-v2/index-not-entropy|Index is not entropy]] gives a conditional type-I inequality relating an edge entropy to finite index. It does not select \(s_*=1\), choose the relevant expectation, identify a bulk carrier, or prove that a BKM channel occupies one Compton volume. The fitted value \(s_*=0.9861\) is a pushforward of the chosen cosmological response model, not an algebraic calculation.

[[causal-scale-theory/open-questions/extensive-channel-normalization|Extensive channel normalization]] owns the regulator, tangent, discarded-mode, and cut-size dependence hidden in a proposed channel count. [[deriving-value-of-g/obstructions-to-an-unconditional-proof|The unconditional-proof obstructions]] explain why a replicated binary response cannot determine a number of channels per square metre without an independent physical scale.

## Three cells that must not be merged

| Name | Carrier | Dimensionless quantity | Present status |
|---|---|---|---|
| wall channel | a state-space or finite-index response sector | candidate weight \(s_*\) | algebraic model; physical multiplicity open |
| bulk correlation cell | a volume \(\lambda_*^3\) inside \(V_c\) | \(N_{\mathrm{bulk}}=\gamma V_c/\lambda_*^3\) | literal closure hypothesis |
| boundary ruler cell | an area \(\lambda_*^2\) on \(A_c\) | \(k_{\lambda_*}=\eta_E\lambda_*^2\) | exact after the Einstein area law is imported |

For the boundary ruler, [[deriving-g-v2/rulers-are-matter|rulers are matter]] gives the exact factorization

$$
\boxed{
\iota_A
=\frac{A}{\lambda_*^2}
\frac{\lambda_*^2}{4\ell_P^2}
=N_Ak_{\lambda_*},
}
$$

where

$$
N_A:=\frac{A}{\lambda_*^2},
\qquad
k_{\lambda_*}:=\frac{\lambda_*^2}{4\ell_P^2}
=\left(\frac{m_P}{2m_*}\right)^2.
$$

This identity holds for any chosen ruler \(\lambda_*\). It does not imply the bulk matching \(\iota_{A,c}=s_*N_{\mathrm{bulk}}\), and \(k_{\lambda_*}\) is generally enormous rather than one. The missing construction is a chain

$$
\text{wall channel}
\longrightarrow
\text{bulk correlation cell}
\longrightarrow
\text{boundary area response}.
$$

A proper K-oriented correspondence, a specified relative extension, or a longitudinal groupoid index may provide a stable bulk-to-boundary skeleton. Each option still requires explicit source and target algebras, orientation data, and a proof that the induced map carries the proposed wall class. [[flux-record-and-top-form-realizations/inq|Baum--Connes assembly]] can organize such an index only after the groupoid and coefficient algebra are built; neither K-theory nor assembly supplies the metric factor \(V/A\), the local weight \(s_*\), or the normalization \(\gamma\).

## Conditional carrier equation

Assume the [[crossing-evaluated-flat-modulus/inq|crossing-evaluated fossil closure]], the reduced Compton ruler

$$
\lambda_*:=\frac{\hbar}{m_*c},
$$

and the noncircular homogeneous matching \(\bar\chi_c=\eta_E=c^3/(4\hbar G)\). Substituting \(\zeta=\gamma s_*/3\) gives

$$
\boxed{
Gm_*^3
=\frac{3\hbar^2H_c}{4\gamma s_*c}.
}
$$

Equivalently,

$$
m_*
=\left(
\frac{3\hbar^2H_c}{4\gamma s_*cG}
\right)^{1/3},
\qquad
H_c
=\frac{4\gamma s_*cGm_*^3}{3\hbar^2}.
$$

The second form is the falsifiable direction only conditional on an independently measured or independently derived \(G\): a separately selected \((m_*,\gamma,s_*)\), together with that coupling, predicts the crossing rate. Inverting measured \(G\) and \(H_c\) merely diagnoses which carrier the hypothesis would require.

Using the two currently recorded conditional crossing rates (the CMB-conditional value follows the fixed-physical-density protocol of [[the-grain-of-causal-scale/inq|the grain module]], which replaced the earlier mixed-composition \(82.64\)),

$$
H_c=88.2608
\quad\text{or}\quad
83.1058
\ \mathrm{km\,s^{-1}\,Mpc^{-1}},
$$

the minimal \(\gamma=s_*=1\) model gives

$$
m_*=59.48
\quad\text{or}\quad
58.30\ \mathrm{MeV}/c^2.
$$

At the fitted \(s_*=0.9861\), the values are \(59.76\) and \(58.58\,\mathrm{MeV}/c^2\). Across both branches and the recorded interval \(s_*\in[0.9175,1.0621]\), the target is approximately

$$
\boxed{57.14\le m_*c^2/\mathrm{MeV}\le61.22.}
$$

The focused standard-library check is [[bulk-area-cell-normalization/normalization_receipt.py|the normalization receipt]].

## The sharpened falsifier

At \(\gamma=1\), neither \(m_\pi/2\) nor \(f_\pi\) lies in the fitted interval. They would require approximately

$$
s_*(m_\pi/2)=0.62,
\qquad
s_*(f_\pi)=0.27,
$$

and would predict crossing rates near \(142.5\) and \(327.6\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\) at unit baseline normalization. The earlier broad “chiral window” therefore fails under the literal one-species spherical reading.

Three possibilities remain open:

1. the wall algebra derives a nontrivial \(\gamma\);
2. \(m_*\) is a correlation or capacity grain rather than a particle pole mass; or
3. the literal uniform bulk-cell projection is false.

The extremely low baryon and photon occupancy of the effective cells in the source receipt supports the second interpretation over a literal occupant count. It does not identify the grain.

## Claim ledger

| Status | Claim |
|---|---|
| exact geometry | \(V/A=R/3\) for a Euclidean three-ball |
| exact conditional deduction | the bulk-count hypotheses imply \(\zeta=\gamma s_*/3\) |
| reproduced diagnostic | the two crossing branches and fitted \(s_*\) interval give the stated \(57.14\)--\(61.22\,\mathrm{MeV}\) window when measured \(G\) is inverted |
| open construction | the carrier, \(\gamma\), wall-channel count, bulk-to-boundary map, and state--geometry weld |
| failure condition | an independently derived carrier and multiplicity, together with an independently fixed \(G\), predict an incompatible \(H_c\), or no regulator-independent cell projection exists |

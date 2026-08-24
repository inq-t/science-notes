# Causal Scale Dynamics — Master Research Note v7.0

**Subtitle:** Modular Information Geometry, Horizon Capacity, and the Ruble Equations  
**Author:** Thomas Ruble  
**Date:** 21 August 2026  
**Status:** Working research note; not peer reviewed.

## Main deliverables

- `Causal_Scale_Dynamics_Master_v7_0.pdf` — 52-page self-contained master document.
- `Causal_Scale_Dynamics_Master_v7_0.md` — editable source.
- `Causal_Scale_Dynamics_Master_v7_0.tex` — generated LaTeX source.
- `sections/` — component Markdown sources.
- `Ruble_Equations_Reference.pdf` — compact equation reference.
- `receipts/receipts_v7.py` — exact symbolic and numerical verification.
- `receipts/receipts_v7.json` — machine-readable receipt output.
- `make_figures_v7.py` — figure-generation script.
- `figures/` — publication figures.
- `sources/ai_referee_notes/` — AI-authored hand-off notes audited in the document.
- `data/` — prior background, neutrino-response, and economy-audit outputs used only for the observational status section.

## Central closure

The theory defines the entropy-normalized horizontal BKM speed at the self-dual causal wall,

\[
\mathfrak R_c
:=
\frac{k_B}{S_c}
G^{\perp}_{NN}(N_c).
\]

The **Scale–Capacity Equivalence Principle** is

\[
\mathfrak R_c=1.
\]

Relative entropy converts the BKM Hessian into modular free-energy curvature,

\[
\rho_X(N)=\frac{k_BT_c}{2V_c}G^{\perp}_{NN}(N),
\]

and flat-FLRW horizon thermodynamics gives

\[
k_BT_c\frac{S_c}{k_B}
=E_{\rm MS,c}
=\rho_{\rm crit,c}V_c.
\]

Therefore, in 3+1 dimensions,

\[
\rho_X(N)
=\frac12\rho_{\rm crit,c}\operatorname{sech}^2(N-N_c).
\]

At the crossing,

\[
\Omega_{X,c}=\frac12,
\qquad
\rho_X(N_c)=\rho_{\rm ordinary}(N_c).
\]

The old amplitude postulate is thus replaced by one explicit equivalence law. The law is not claimed as a theorem of mathematics; it is the stopping principle of the homogeneous theory and a direct target for independent derivation or falsification.

## Exact observable structure

Separate conservation gives

\[
w_X(N)=-1+\frac23\tanh(N-N_c),
\]

and

\[
9(1+w_X)^2+6\frac{dw_X}{dN}=4.
\]

The benchmark for

\[
\Omega_{m0}=0.310598,
\qquad
\Omega_{r0}=9.15\times10^{-5}
\]

is

| quantity | value |
|---|---:|
| `N_c` | -0.2940066 |
| `z_c` | 0.3417927 |
| `q_0` | -0.3369025 |
| `j_0` | -0.1112465 |
| acceleration entry | z = 0.7856935 |
| acceleration exit | a/a0 = 11.7865245 |
| rho*/ordinary at crossing | 1 exactly |
| rho*/matter at crossing | 1.0003953 |

## What was accepted and rejected from the AI closure

Retained:

- the vertical/horizontal modular distinction;
- capacity as a BKM/relative-entropy Hessian;
- self-duality as the intrinsic crossing event;
- the need for one clear stopping law;
- the open status of perturbations.

Rejected:

- conformal-weight integrality as a derivation of `varrho_perp=1`;
- the inference that a two-dimensional normal plane is automatically a two-dimensional CFT;
- use of Cardy thermodynamics as an unconditional derivation of the capacity ratio.

The final document uses the more invariant scale-capacity equivalence law instead.

## Reproduce exact receipts

```bash
python receipts/receipts_v7.py
```

Expected field:

```json
"all_exact_residuals_zero": true
```

The script checks algebraic consequences only. It does not prove the physical scale-capacity principle, geometric modular flow for a dynamical FLRW wall, or the covariant perturbation completion.

## Regenerate figures

```bash
python make_figures_v7.py
```

## Rebuild the PDF

Pandoc and XeLaTeX are required.

```bash
pandoc Causal_Scale_Dynamics_Master_v7_0.md \
  --pdf-engine=xelatex \
  --resource-path=. \
  -o Causal_Scale_Dynamics_Master_v7_0.pdf
```

## Logical stopping point

The homogeneous theory is closed by:

1. the fundamental normal chirality quotient;
2. affine Connes-cocycle soldering with the fundamental character;
3. the scale-capacity equivalence principle;
4. a chosen global residual sector.

The remaining research is a new layer, not a hidden background parameter:

- construct the dynamical FLRW causal-wall state family;
- derive the scalar/vector/tensor perturbation lift;
- test the invariant and the equality-crossing coincidence;
- determine the global vacuum sector;
- perform the direct CMB/lensing/growth likelihood.

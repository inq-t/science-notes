# Expansion History and Future Classes

After a present-flatness root is selected, the generalized response fixes a conditional homogeneous expansion history. The zero-residual future is classified by the scale-state rate \(\nu\), while the integrated crossing ratio \(\mathfrak R_c\), root branch, ordinary contents, and residual sector still control the finite history and whether acceleration occurs at all.

Let \(x_c\) be a selected root from [[causal-scale-theory/flatness-branches|the crossing-branch analysis]], set \(x=N+x_c\), and define

$$
D:=1-\Omega_{m0}-\Omega_{r0}.
$$

For the flat matter-plus-radiation background with separate response conservation and zero residual, the **[CONDITIONAL OUTPUT]** is

$$
\boxed{
\begin{aligned}
E^2(x):=\frac{H^2(x)}{H_0^2}
=\;&\Omega_{m0}e^{3(x_c-x)}
+\Omega_{r0}e^{4(x_c-x)}\\
&+D\frac{\operatorname{sech}^2(\nu x)}
{\operatorname{sech}^2(\nu x_c)}.
\end{aligned}}
$$

This is the background interface consumed by distances, ages, and cosmography. It is not a covariant response sector and does not determine structure growth.

## Zero-residual future

[[causal-scale-theory/theorems/future-response-classes|The future-class theorem]] owns the proof of the following classification:

| Rate \(\nu\) | Leading ever-expanding future |
|---|---|
| \(0<\nu<1\) | response-dominated power-law acceleration with a future event horizon |
| \(\nu=1\) | response-dominated coasting with divergent future conformal time |
| \(1<\nu<3/2\) | response-dominated deceleration |
| \(\nu=3/2\) | response and matter have the same leading dilution |
| \(\nu>3/2\) | matter eventually dominates |

In the response-dominated range \(0<\nu<3/2\), the theorem gives

$$
\rho_X\sim a^{-2\nu},
\qquad
w_X\longrightarrow-1+\frac{2\nu}{3},
\qquad
a(t)\sim t^{1/\nu}.
$$

A positive constant residual eventually replaces every row by de Sitter behavior. A negative residual can instead force a turnaround if the total density reaches zero. These are sector changes, not corrections to the rigid-response theorem.

## Finite acceleration

The rate alone does not determine an accelerating interval. Under the same flat, noninteracting, zero-residual assumptions, [[causal-scale-theory/theorems/acceleration-condition|the acceleration theorem]] gives the necessary and sufficient condition

$$
\boxed{
\bigl(2-3[1+w_X]\bigr)\rho_X
>\rho_m+2\rho_r.}
$$

Within this zero-residual theorem, the amplitude, selected closure root, and abundances all enter through the densities. A different residual sector adds its own active-mass contribution and requires the correspondingly modified condition. In particular, the unit response can dominate the late energy density while its negative active mass becomes too small to sustain acceleration; [[causal-scale-theory/unit-branch|the unit-branch application]] records the resulting finite exit.

## Horizon reconstruction

With the same flat FLRW geometry and an area-law apparent horizon, every selected \(H(N)\) also determines the deceleration \(q\), the radius \(R_A=c/H\), and the signed horizon rapidity \(\widehat\zeta_A\) up to an additive constant. [[conformal-scale-geometry/horizon-allocation|The exact conformal-scale identity]] defines

$$
\mathrm d\widehat\zeta_A
:=\frac{1-q}{2}\,\mathrm dN,
\qquad
\mathrm dN
=\mathrm d\widehat\zeta_A
+\frac14\,\mathrm d\ln S_A.
$$

Here \(\widehat\zeta_A\) is a signed horizon-rapidity potential reconstructed from the same FLRW history. It is neither conformal time nor the binary polarization, and the identity is not by itself a thermodynamic exchange law or conserved charge.

# Conjecture: BKM Capacity Has an Areal Measure

A possible geometric carrier for residual state-space capacity is a positive measure on causal-wall patches whose density is proportional to area. If realized, this would turn “capacity becomes space” into a precise Radon--Nikodym statement and relate the capacity density to Newton's constant.

For suitable wall patches $U$, seek a renormalized measure

$$
\mu^\perp_{\mathrm{BKM}}(U)
:=G^\perp_{NN,\mathrm{ren}}[U]
$$

that is additive on the appropriate class of disjoint patches and absolutely continuous with respect to area measure $\mu_A$:

$$
\frac{\mathrm d\mu^\perp_{\mathrm{BKM}}}{\mathrm d\mu_A}
=\chi_*.
$$

If horizon entropy satisfies

$$
\delta\left(\frac{S_{\mathrm{hor}}}{k_B}\right)
=\chi_*\,\delta A,
$$

comparison with the Bekenstein--Hawking density gives

$$
\chi_*=\frac{c^3}{4G\hbar},
\qquad
G=\frac{c^3}{4\hbar\chi_*}.
$$

The last equation would determine $G$ only if $\chi_*$ were calculated from independent microscopic data. Rewriting the known entropy law to define $\chi_*$ would be dimensional bookkeeping, not a derivation.

## Upgrade criterion

A theorem needs a specified wall algebra, a renormalized finite BKM quadratic form, locality or additivity, a state-independent measure class, and an independent calculation of $\chi_*$. The homogeneous equality in [[unit-amplitude-principle]] should then follow as an integral over the crossing wall.

## Failure criterion

The route fails if the BKM quantity is intrinsically nonlocal, scheme dependent in its area term, not positive on physical tangents, or scales with a geometric measure other than area. The precise derivation target is explored further in [[deriving-value-of-g/causal-scale-derivation-target|the $G$-derivation module]].

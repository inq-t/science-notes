# Wilson Vacuum Coercivity Through Temporal Refinement

The actual anisotropic Wilson vacuum has an explicit gradient Poincare bound uniform in temporal spacing and spatial volume when the magnetic interaction is sufficiently small relative to the kinetic time scale. Entire temporal columns, not individual time sites, are the variables of the dependence estimate. This removes the single-link certificate's failure as its temporal coupling grows. It does not remove the spatial regulator or prove a complete two-ended bridge bound.

**Status: [EXACT APPLICATION] of temporal-column response to the declared \(SU(2)\) Wilson family; [EXACT SUFFICIENT REGIME] below.** The [[wilson-slab-conditional-fisher-certificate|adjacent-slice certificate]] and this theorem have different outputs. Here the output is actual-vacuum gradient coercivity through time refinement; its Hamiltonian interpretation requires the separate limit argument.

## Keep the Wilson history and change its grouping

Use the conventions of the slab certificate: \(\phi(g)=\operatorname{ReTr}(g)/2\), the unit-\(S^3\) gradient metric, Haar Poincare constant \(3\), and
\[
T_{x,\beta}=M_{e^{-\beta W/2}}K_xM_{e^{-\beta W/2}},
\qquad
W(U)=\sum_p[1-\phi(U_p)].
\tag{WC1}
\]
Assume \(\beta\ge0\) and \(d_s\ge2\). The spatial lattice is finite hypercubic with ordinary four-distinct-link plaquettes and incidence at most \(2(d_s-1)\) per link. Temporal preparations have free integrated endpoints with their half spatial potentials, so their midpoint laws are \(\nu_N\propto(T^N1)^2\,dU\).

Conditioning on every column but \(e\) gives a one-dimensional chain with kernel \(k_x\) and arbitrary time-dependent one-site potentials obeying
\[
b=4(d_s-1)\beta,\qquad \operatorname{osc}v_t\le b.
\tag{WC2}
\]
No magnetic insertion has been dropped. End half-potentials satisfy the same bound.

For \(x\ge1\), set \(n=\lceil4x\rceil\). The [[bridge-score-fusion-geometry/wilson-bridge-envelopes-under-temporal-blocking|all-representation Wilson kernel estimate]] gives
\[
m_n=26/35,\quad M_n=44/35,\quad R_n=22/13.
\tag{WC3}
\]
Thus the conditional-chain constants are
\[
\tau=\tanh\!\left[\frac{\log(22/13)+nb}{2}\right],\qquad
\mathcal S=\frac{2n}{1-\tau}-1.
\tag{WC4}
\]

For the column influence calculation, use the different auxiliary base metric \(d_0(u,v)=\|u-v\|_{\mathbb R^4}/2\). It is a compact compatible chordal metric of diameter one. It has not replaced the unit-\(S^3\) gradient metric.

Let \(m_{ef}\) count the spatial plaquettes shared by links \(e,f\). Quaternion multiplication and inversion preserve the Euclidean norm, and the normalized plaquette trace is linear in each quaternion when the others are fixed. Changing \(u_f\) to \(v_f\) therefore changes \(e\)'s potential by \(h\) with
\[
\operatorname{osc}_{u_e}h
\le2\beta m_{ef}\|u_f-v_f\|
=4\beta m_{ef}d_0(u_f,v_f).
\tag{WC5}
\]
The bound remains valid under linear interpolation of the old and new scalar potentials; the interpolation need not correspond to an intermediate quaternion.

## An explicit horizon- and refinement-safe bound

Since \(\sum_{f\ne e}m_{ef}\le6(d_s-1)\), [[temporal-column-response/inq|the whole-column theorem]] gives
\[
q_{\mathrm{col}}=6(d_s-1)\beta\mathcal S.
\tag{WC6}
\]
If \(q_{\mathrm{col}}<1\), the actual vacuum law \(\nu_{x,\beta}=\psi_{x,\beta}^2dU\) obeys
\[
\boxed{\lambda_{\nu_{x,\beta}}\ge
3e^{-D_{\mathrm{mid}}}(1-q_{\mathrm{col}}),\qquad
D_{\mathrm{mid}}=b+2nb+2\log(22/13).}
\tag{WC7}
\]
The finite history is estimated first; finite-volume Perron convergence is taken afterward. Constants do not count spatial links or preparation layers.

A convenient conservative window is
\[
\boxed{x\ge1,\qquad
\zeta:=(d_s-1)\beta x\le\frac1{200}.}
\tag{WC8}
\]
Indeed \(n\le5x\), \(nb\le20\zeta\le1/10\), and
\(\log(22/13)+1/10<\log2\), so \(\tau\le1/3\). The last logarithmic inequality follows, for example, from
\(\log(13/11)\ge2/13>1/10\).
Hence \(\mathcal S\le3n\le15x\), \(q_{\mathrm{col}}\le9/20\), and
\[
D_{\mathrm{mid}}\le2\log(22/13)+11/50.
\]
Therefore
\[
\boxed{\lambda_{\nu_{x,\beta}}\ge
\lambda_*:=
\frac{33}{20}\left(\frac{13}{22}\right)^2e^{-11/50}>0.}
\tag{WC9}
\]
These rational constants certify a sufficient regime; they are not optimized thresholds or proposed constants of nature.

Along \(x=1/\varepsilon,\ \beta=g\varepsilon\), (WC8) becomes \((d_s-1)g\le1/200\), independent of \(\varepsilon\le1\). In contrast the old temporal term \(2\tanh x\) tends to two. The improvement comes from allowing temporal dependence inside the column and charging only its finite integrated susceptibility against spatial interactions.

## What survives, and what still must be built

[[wilson-to-hamiltonian-vacuum-limit|The fixed-volume vacuum limit]] passes (WC9) to
\[
H_g=\tfrac12\sum_eL_{S^3,e}+gW.
\]
Its exact ground-state transform then gives a physical Hamiltonian gap at least \(\lambda_*/2\) in these dimensionless energy units, uniformly in spatial volume. Multiplying the entire declared Hamiltonian by an independent energy unit multiplies that bound by the same unit.

This is not a proof that the finite-\(\varepsilon\) Wilson logarithm dominates the group Laplacian. Its high-representation asymptotics prohibit that shortcut. It also does not turn a vacuum Poincare inequality or a Hamiltonian gap into a complete two-endpoint bridge floor.

In conventional lattice gauge scaling, \(g\) here is proportional to the magnetic/electric ratio, hence to \(g_0^{-4}\). The four-dimensional asymptotically free trajectory makes this ratio large, not small. The estimate closes a temporal-refinement obstruction at strong bare coupling; the spatial crossover and nontrivial continuum reconstruction remain open.

[[temporal-column-response/receipts/temporal_column_response_receipt.py|The finite receipt]] checks inhomogeneous block bounds, full-path sensitivity, actual coupled-column variance factorization, midpoint density comparison and a finite-state Hamiltonian limit. It is not a discretization proof for \(SU(2)\); the compact-group coefficient comes from the analytic kernel bound.

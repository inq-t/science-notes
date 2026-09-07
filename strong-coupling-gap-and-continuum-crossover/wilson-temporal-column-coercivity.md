# Wilson Vacuum and Bridge Coercivity Through Temporal Refinement

The actual anisotropic Wilson law has explicit vacuum Poincare and complete two-ended bridge bounds uniform in temporal refinement and finite spatial volume when the magnetic interaction is sufficiently small relative to the kinetic time scale. Entire temporal columns control dependence; a gradual change of the initial configuration spreads its endpoint score across a finite physical depth while retaining every magnetic insertion. This closes the adjacent-slice certificate's temporal-refinement failure, not the spatial continuum problem.

**Status: [EXACT APPLICATION] of temporal-column response and conditional Fisher coercivity to the declared \(SU(2)\) Wilson family; [EXACT SUFFICIENT REGIME] below.** The proofs are internal derivations, not a claim of independent publication review or a new solution of the Clay problem. Unlike the [[wilson-slab-conditional-fisher-certificate|adjacent-slice certificate]], the bridge here uses a fixed positive blocked depth through refinement. Its Hamiltonian return uses the separately established vacuum and joint-law limits.

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

For \(x\ge1\), set \(m=\lceil4x\rceil\). The [[bridge-score-fusion-geometry/wilson-bridge-envelopes-under-temporal-blocking|all-representation Wilson kernel estimate]] gives
\[
\underline k_m=26/35,\quad \overline k_m=44/35,\quad R=22/13.
\tag{WC3}
\]
Thus the conditional-chain constants are
\[
\tau=\tanh\!\left[\frac{\log(22/13)+mb}{2}\right],\qquad
\mathcal S=\frac{2m}{1-\tau}-1.
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
D_{\mathrm{mid}}=b+2mb+2\log(22/13).}
\tag{WC7}
\]
The finite history is estimated first; finite-volume Perron convergence is taken afterward. Constants do not count spatial links or preparation layers.

A convenient conservative window is
\[
\boxed{x\ge1,\qquad
\zeta:=(d_s-1)\beta x\le\frac1{200}.}
\tag{WC8}
\]
Indeed \(m\le5x\), \(mb\le20\zeta\le1/10\), and
\(\log(22/13)+1/10<\log2\), so \(\tau\le1/3\). The last logarithmic inequality follows, for example, from
\(\log(13/11)\ge2/13>1/10\).
Hence \(\mathcal S\le3m\le15x\), \(q_{\mathrm{col}}\le9/20\), and
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

## Spread the endpoint score across an actual interacting block

Set \(n=2m\). Start with the finite one-sided history in the slab certificate, with fixed initial configuration \(U_0=U\), a free terminal preparation at \(N\ge n\), and all intermediate Wilson potentials. Let \(\eta_{N,U}^{(n)}\) be its law of \(U_n\). The ramp argument below bounds endpoint Fisher information for these histories, including their fixed initial values. Its kinetic and interaction constants can both be calculated in the declared unit-\(S^3\) gradient metric.

For a tangent vector \(v=(v_e)\) written as left-multiplication directions, put
\[
h_t=(1-t/m)_+,
\qquad
U_{t,e}\longmapsto e^{s h_t v_e}U_{t,e}.
\tag{WC10}
\]
The initial configuration changes by \(e^{s v_e}\), while \(U_n\) and all later variables remain unchanged. Haar measure is preserved. For \(Z_{t,e}=U_{t,e}U_{t+1,e}^{-1}\), cyclicity of the trace gives exactly
\[
\phi(e^{s h_t v_e}Z_{t,e}e^{-s h_{t+1}v_e})
=\phi(e^{s(h_t-h_{t+1})v_e}Z_{t,e}).
\]
There is no missing adjoint or commutativity assumption on different increments. Differentiating the transformed finite-history weight gives, up to a deterministic initial half-potential that cancels upon normalization,
\[
F_v=\sum_e B_e+D_v,
\qquad
B_e=\frac{x}{m}\sum_{t=0}^{m-1}d\phi(Z_{t,e})[v_e],
\qquad
D_v=-\beta\sum_{t=1}^{m-1}h_t\,dW(U_t)[v].
\tag{WC11}
\]
Thus the normalized endpoint score is
\(\mathbb E[F_v\mid U_n]-\mathbb E F_v\), and its variance is at most \(\operatorname{Var}F_v\). This statement concerns the endpoint marginal of the same interacting history, not a separately chosen process.

Under one reference Wilson increment, Haar integration by parts and \(d_v^2\phi=-\|v\|^2\phi\) give
\[
\mathbb E_{k_x}d_v\phi=0,
\qquad
x\,\mathbb E_{k_x}(d_v\phi)^2
=\|v\|^2\mathbb E_{k_x}\phi\le\|v\|^2.
\tag{WC12}
\]
The one-increment Fisher constant is therefore at most \(x\), not \(x^2\). Independence of the first \(m\) reference increments yields \(\mathbb E B_e^2\le(x/m)\|v_e\|^2\). After conditioning on their product with the remaining \(m\) increments, the latter contribute at most \(\overline k_m/\underline k_{2m}\le R\); the lower bound follows also from \(k_x^{*(2m)}=k_x^{*m}*k_x^{*m}\ge\underline k_m\).

Now condition on the complete exterior columns and further on \(U_{n,e}\). The early column segment is its actual inhomogeneous bridge, with potential oscillation at most \(2mb\). Comparing only this conditional segment with its kinetic bridge gives
\[
\mathbb E[B_e^2\mid\hbox{exterior columns}]
\le A\|v_e\|^2,
\qquad
A:=R e^{2mb}\frac{x}{m}.
\tag{WC13}
\]
The comparison first holds uniformly in \(U_{n,e}\); the rest of the history merely mixes that endpoint. No bound on the oscillation of a global Perron message, and no comparison of the entire spatial law with product Haar, is used.

The spatial score also responds when an exterior tangent acts on a plaquette meeting the resampled column. Let \(J_{ef}\) count plaquettes containing both \(e\) and \(f\), including \(e=f\). Every directional plaquette derivative has absolute value at most \(\|v_f\|\). Since \(2\sum_{t=1}^{m-1}h_t=m-1\),
\[
\delta_eD_v\le\beta(m-1)\sum_fJ_{ef}\|v_f\|,
\qquad
\left\|\tfrac12\delta D_v\right\|_2
\le4(d_s-1)\beta(m-1)\|v\|_2
\le mb\|v\|_2.
\tag{WC14}
\]
Here \(\delta_e\) is whole-column oscillation. The symmetric matrix \(J\) has row and column sums at most \(8(d_s-1)\), because each incident plaquette contributes four entries. This accounts for all tangent components jointly, including the mixed neighboring-plaquette scores.

These are the inputs of [[temporal-column-response/smoothed-endpoint-response|the smoothed-endpoint theorem]]: \(j\le x\), \(D_m\le2mb\), \(R_m\le R\), and \(L_m\le mb\). Its column variance factorization, square-root variance triangle inequality and half-oscillation bound give
\[
\boxed{
I_{\eta_{N,U}^{(n)}}(v,v)\le C_F\|v\|_2^2,
\qquad
C_F:=\frac{(\sqrt A+mb)^2}{1-q_{\mathrm{col}}}.}
\tag{WC15}
\]
The constants are independent of \(U\), \(N\), the number of spatial links and the endpoint values used in the conditional bridge. At each fixed finite carrier, Perron convergence followed by one smooth-kernel application gives convergence of the normalized endpoint densities and their first derivatives. Hence (WC15) passes to the actual Doob transition \(\eta_U^{(n)}=P_T^n(U,\cdot)\). This is a fixed-volume limiting argument after the uniform finite-history estimate; it assumes neither a volume-uniform Perron convergence rate nor a bound on derivatives of an unconstructed infinite-volume vacuum.

## The complete two-ended floor survives temporal refinement

The actual reversible stationary Doob law has conditionally independent endpoints \(n\) steps to either side of its midpoint. Its joint forward Fisher tensor is bounded by \(2C_F\) times the product gradient metric. In [[conditional-fisher-coercivity/inq#A background-metric certificate that permits singular Fisher information|the background-metric certificate (CF9)]], take the midpoint vacuum as the context and the endpoint pair as the hidden carrier. Combining (WC7) with (WC15), then using equality of the centered norms of the forward conditional-mean map and its adjoint, gives
\[
\boxed{
I-S_{\mathrm{bridge}}^{(n)}\ge\kappa Q_0,
\qquad
\kappa=\frac{\underline\lambda_\nu}{\underline\lambda_\nu+2C_F},
\qquad
\underline\lambda_\nu=3e^{-D_{\mathrm{mid}}}(1-q_{\mathrm{col}}).}
\tag{WC16}
\]
Here \(\underline\lambda_\nu\) is the proved lower certificate, not a claim to the optimal Poincare constant. \(S_{\mathrm{bridge}}^{(n)}\) is the prediction return on the complete midpoint \(L^2(\nu)\) carrier, and \(Q_0\) removes constants. Smooth positive densities on each finite compact carrier supply the differentiation and dense-core hypotheses. The result does not discard higher representations, non-score observables, or arbitrary soft directions. Restriction to gauge-invariant midpoint functions retains it; [[bridge-score-fusion-geometry/gauge-quotients-of-midpoint-bridges|independently quotienting the endpoints]] can only remove predictors and increase the residual floor.

Within (WC8), \(x/m\le1/4\), \(mb\le1/10\), and \(1-q_{\mathrm{col}}\ge11/20\). Thus one fully explicit certificate is
\[
C_*:=\frac{\left[\tfrac12\sqrt{22/13}\,e^{1/10}+1/10\right]^2}{11/20},
\qquad
\boxed{I-S_{\mathrm{bridge}}^{(2\lceil4x\rceil)}
\ge\kappa_*Q_0,
\qquad
\kappa_*:=\frac{\lambda_*}{\lambda_*+2C_*}>0.}
\tag{WC17}
\]
Numerically \(\lambda_*\simeq0.4623602620\), \(C_*\simeq1.2191229068\), and \(\kappa_*\simeq0.1594012596\). The inequalities use their exact expressions, not rounded values. These are conservative bounds for the declared interacting law, not universal mass predictions.

## The same bridge has a Hamiltonian return

[[wilson-to-hamiltonian-vacuum-limit|The fixed-volume vacuum limit]] passes (WC9) to
\[
H_g=\tfrac12\sum_eL_{S^3,e}+gW.
\]
Its exact ground-state transform then gives a physical Hamiltonian gap at least \(\lambda_*/2\) in these dimensionless energy units, uniformly in spatial volume. Multiplying the entire declared Hamiltonian by an independent energy unit multiplies that bound by the same unit.

The bridge return is a separate consequence of (WC17), not an inference from that Hamiltonian gap. Along \(x=1/\varepsilon\), \(\beta=g\varepsilon\), its half-slab depth obeys \(2\lceil4/\varepsilon\rceil\varepsilon\to8\). The fixed-volume operator-norm semigroup limit and \(L^2\) vacuum convergence identify the joint law at times \((-8,0,8)\): moments of bounded continuous product tests are vacuum matrix elements of two normalized transfer blocks and a midpoint multiplication operator. They converge to the corresponding matrix elements of \(e^{-8(H_g-E_g)}\). Products are dense in the continuous functions on the compact triple carrier.

The [[bridge-data-augmentation-solder/bridge-floor-under-joint-limits|joint-limit theorem]] then passes the inequality in its predictor form,
\[
\mathbb E|f(U_0)-G(U_{-n},U_n)|^2
\ge\kappa_*\operatorname{Var}_\nu f,
\tag{WC18}
\]
first for bounded continuous tests, then by \(L^2\) density for the complete limiting carrier. No convergence of Fisher tensors or conditional-expectation operators is asserted. This establishes the same positive bridge floor at half-slab time \(8\) for the actual finite-volume Hamiltonian vacuum, with the same constant at every allowed spatial volume.

The [[bridge-score-fusion-geometry/gauge-quotients-of-midpoint-bridges|one-boundary order]] also gives the physical-transfer estimate
\[
\|\bar P_T^{\,n}Q_0\|\le\sqrt{1-\kappa_*},
\qquad
\Delta_{\varepsilon}\ge
-\frac{\log(1-\kappa_*)}{2n\varepsilon},
\tag{WC19}
\]
where \(\Delta_\varepsilon\) is the centered gap of \(-\varepsilon^{-1}\log\bar P_T\) in the declared time units. Its Hamiltonian bound at depth \(8\) is approximately \(0.0108525534\), weaker than the independent gradient bound \(\lambda_*/2\). Its significance here is the full bridge comparison. The construction still does not say that the finite-\(\varepsilon\) Wilson logarithm dominates the group Laplacian; its high-representation asymptotics prohibit that shortcut.

In conventional lattice gauge scaling, \(g\) here is proportional to the magnetic/electric ratio, hence to \(g_0^{-4}\). The four-dimensional asymptotically free trajectory makes this ratio large, not small. Uniform constants for a family of finite-volume laws do not themselves construct an infinite-volume representation or a nontrivial continuum limit. The spatial crossover, compatible joint limiting observables and full physical reconstruction remain open; the graph, action and clock calibration are still supplied inputs.

[[temporal-column-response/receipts/temporal_column_response_receipt.py|The column receipt]] checks inhomogeneous block bounds, full-path sensitivity, actual coupled-column variance factorization, midpoint density comparison and a finite-state Hamiltonian limit. [[receipts/wilson_slab_fisher_receipt.py|The Wilson receipt]] additionally checks simultaneous noncommuting quaternion ramp derivatives, mixed neighboring-plaquette scores, Haar Fisher quadrature and the constants in (WC17). These are finite checks, not a discretization proof of the full \(SU(2)\) carrier or its limits; the complete bounds use the analytic arguments above.

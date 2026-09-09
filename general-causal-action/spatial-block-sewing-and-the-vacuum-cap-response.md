# Spatial Block Sewing and the Vacuum Cap Response

Integrating an adjacent spatial block changes the actual Wilson chronological law through both its local crossing plaquettes and its interacting vacuum at the two outer boundaries. The latter contribution is an amplitude copula, not a product vacuum assumption. Its complete source message gives a finite interface bound on chronological conditional variance. Applying that bound to the oriented innovation also requires the part of the evolved source that spreads outside the retained block; its lag cost cannot be discarded.

**Status: exact finite-graph sewing and source identities; proved finite conditional-influence bound; open uniform spatial surplus.** The transfer and actual vacuum are those returned in [[cycle-moments-and-the-pure-gauge-vacuum-return|CM7 and CM17–21]]. [[rg-covariance-residue/exact-wilson-interface-statistics|Exact Wilson interface statistics]] owns the corresponding bare-action reduction. Here the Perron boundary amplitudes are retained, and the final comparison uses the actual chronological word of [[oriented-innovation-and-finite-temporal-repair|OI19–28]].

## The two actual vacuum caps survive a spatial cut

Fix a finite spatial graph, \(b>0\), a physical temporal step \(a_t>0\), and \(k\ge1\). Let \(T=T_{W,b}\), \(T\psi=\lambda\psi\), \(\psi>0\), and \(\int\psi^2\,dU=1\). Restore all raw spatial and temporal links on the \(3k\)-step strip. Its vacuum probability amplitude is
\[
d\Gamma_{\rm raw}
=\lambda^{-3k}\psi(U_-)\psi(U_+)
 e^{-S_{\rm strip}(U)}\,dU.
\tag{SB1}
\]
All Haar measures are normalized. The strip action has half the spatial weight at its two outer slices, full spatial weights internally, and full temporal plaquettes. Integrating the intermediate links returns OI's four-boundary law. Retain framed variables until the joint gauge integration; no independent regional gauge quotient is introduced.

Partition the raw variables into left history \(A\), right history \(B\), and a separator history \(S\). Write
\[
S_{\rm strip}=S_L(A;S)+S_R(B;S)+S_0(S)+S_\times(A,B;S).
\]
A complete separator makes \(S_\times=0\). Keeping it explicit also covers a thinner cut. At either outer separator configuration \(s\), define
\[
z_s=\int\psi(a,s,b)^2\,da\,db,\qquad
\pi_s(a,b)=\frac{\psi(a,s,b)^2}{z_s},
\]
\[
c_s(a,b)=
\sqrt{\frac{\pi_s(a,b)}{\pi_A^s(a)\pi_B^s(b)}},
\qquad
\psi(a,s,b)=\sqrt{z_s}\sqrt{\pi_A^s(a)}
                         \sqrt{\pi_B^s(b)}c_s(a,b).
\tag{SB2}
\]
These are the actual conditional vacuum density and its marginals. All factors are positive and continuous. The amplitude copula \(c_s\) equals one precisely when that conditional vacuum density factors.

At fixed \(S\), normalize the two uncoupled history weights
\[
\ell(A;S)=e^{-S_L(A;S)}
 \sqrt{\pi_A^{s_-}(A_-)\pi_A^{s_+}(A_+)},
\quad p_L=\ell/z_L,
\]
and similarly \(p_R\). Put
\[
C_S(A,B)=e^{-S_\times(A,B;S)}
 c_{s_-}(A_-,B_-)c_{s_+}(A_+,B_+),\qquad
Z_C(S)=\mathbb E_{p_Lp_R}C_S .
\]
Then the exact conditional history and unnormalized separator weight are
\[
\boxed{d\Gamma(A,B\mid S)=
 \frac{C_S(A,B)}{Z_C(S)}\,dp_L(A\mid S)\,dp_R(B\mid S),}
\]
\[
\lambda^{-3k}e^{-S_0(S)}
 \sqrt{z_{s_-}z_{s_+}}\;z_Lz_RZ_C(S)\,dS .
\tag{SB3}
\]
Even when no local plaquette crosses the retained separator, both vacuum copulas remain. Integrating block interiors does not make them functions of a narrow collar without another estimate.

## The sewn message retains the mixed source

For bounded real sources \(F_L(A),F_R(B)\), define
\[
Z_S(j_L,j_R)=
 \mathbb E_{p_Lp_R}
 [C_S e^{j_LF_L+j_RF_R}],\qquad
M_R(A;j_R)=\mathbb E_{p_R}[C_S(A,B)e^{j_RF_R(B)}].
\tag{SB4}
\]
The full sourced separator weight is the prefactor in (SB3) with \(Z_C\) replaced by \(Z_S\). A joint source is inserted inside the same integral. At zero source the sewn left law is \(dp_L^{\rm sew}=M_R(A;0)dp_L/Z_C\), so
\[
\mathbb E_{\rm sew}F_L-\mathbb E_{p_L}F_L
=\frac{\operatorname{Cov}_{p_L}(F_L,M_R)}{\mathbb E_{p_L}M_R},
\]
\[
\boxed{\left.\partial_{j_L}\partial_{j_R}\log Z_S\right|_0
=\operatorname{Cov}_{p_L^{\rm sew}}
  \bigl(F_L,\mathbb E[F_R\mid A,S]\bigr).}
\tag{SB5}
\]
This is the mixed boundary response, including the two vacuum normalizers.

For a smooth left variation \(v\), set \(q_v=d_A\log C_S[v]\). Differentiating the normalized right conditional law gives
\[
d_A\mathbb E[F_R\mid A,S][v]
=\operatorname{Cov}_{B\mid A,S}(F_R,q_v),\qquad
\mathcal I_A(v,w)=\operatorname{Cov}_{B\mid A,S}(q_v,q_w).
\tag{SB6}
\]
Here \(q_v=-d_AS_\times[v]+d_A\log c_{s_-}[v]+d_A\log c_{s_+}[v]\). The covariance is taken after adding these scores: the two cap cross terms cannot be replaced by a sum of independent Fisher matrices. [[vacuum-aligned-innovation-completion/local-perron-oscillation-and-conditional-coercivity|The Perron score identities]] and [[seam-coupling-response-and-the-vacuum-cap|the seam-coupling response]] determine the actual cap variation.

## A finite influence bound from a rectangular cap ratio

Let a probability law on compact spaces have positive continuous density proportional to \(p_A(a)p_B(b)C(a,b)\), relative to reference probability measures of full support. Define its rectangular log oscillation
\[
\Delta(C)=\sup_{a,a',b,b'}
\log\frac{C(a,b)C(a',b')}{C(a,b')C(a',b)},\qquad
\eta=\tanh\!\frac{\Delta(C)}4<1.
\tag{SB7}
\]
One-variable factors cancel. For the cut above,
\[
\Delta(C_S)\le\Delta(e^{-S_\times})
 +\Delta(c_{s_-})+\Delta(c_{s_+}),\qquad
\Delta(c_s)=\Delta\bigl(\psi(\,\cdot,s,\cdot\,)\bigr).
\tag{SB8}
\]
For \(N_\times\) crossing Wilson plaquettes counted with their strip half-weights, the elementary bound is \(\Delta(e^{-S_\times})\le4bnN_\times\), where \(n=\dim\rho\). This follows from \(0\le b[n-\operatorname{Re}\chi_\rho]\le2bn\). It counts the seam, not the whole graph. The cap terms have no such interface-only estimate yet.

**Finite maximal-correlation theorem.** Let \(Kf(a)=\mathbb E[f(B)\mid A=a]\), with adjoint given by reverse conditioning in the actual marginals. Then
\[
\boxed{\|K\|_{L^2_0(B)\to L^2_0(A)}\le\eta.}
\tag{SB9}
\]
To prove it, the log likelihood ratio of any two rows of \(K\) has oscillation at most \(\Delta(C)\). The elementary likelihood-ratio bound proved in [[vacuum-aligned-innovation-completion/boundary-action-fixed-points-and-physical-linearization|BF9]] gives row total-variation distance at most \(\eta\). Thus \(K\) contracts real oscillation by \(\eta\); the reverse kernel has the same bound. The positive compact operator \(K^*K\) contracts oscillation by \(\eta^2\). Its nonzero eigenfunctions are continuous, since its continuous kernel maps \(L^2\) into continuous functions. Applying the oscillation bound to each nonconstant eigenfunction bounds its eigenvalue by \(\eta^2\). Strict positivity leaves only constants at eigenvalue one, and compact self-adjoint spectral theory gives (SB9), also for complex functions.

The same bound holds after fixing part of \(A\) or \(B\), with a uniform bound on (SB7). Integrating coordinates separately on each side also preserves \(\Delta\): multiply the pointwise cross-ratio inequality by the four product weights and integrate. Consequently, for every centered joint \(f\),
\[
\mathbb E\operatorname{Var}(f\mid A)
+\mathbb E\operatorname{Var}(f\mid B)
\ge(1-\eta)\operatorname{Var}f.
\tag{SB10}
\]
Indeed the two conditional projections have centered subspace angle at most \(\eta\), so their sum has norm at most \(1+\eta\). This is a conditional-variance estimate on the given law, not the selection of a resampling clock. [[collared-quasi-factorization-and-surface-response/fisher-collar-bound-for-wilson-laws|The Wilson Fisher collar]] supplies related source bounds under its own stated strong-coupling hypotheses.

## Apply the cut to the chronological word

For this step no separator history is frozen. Assign its variables to one block and use the same factorization with all crossing plaquettes in \(C\). Assume (SB7) is bounded by \(\Delta\) for this complete raw three-slab history. Its marginal at times \(0,k,2k,3k\), denoted \((x',x,y,y')\), is the actual OI law
\[
d\Gamma=\pi(dx')A(x',dx)A(x,dy)A(y,dy'),
\qquad A=P_W^k,\qquad \pi=\psi^2dU.
\tag{SB11}
\]
The outer-pair marginal is \(\mu_3=\pi A^3\); the middle-pair marginal is \(\mu_1=\pi A\). Write \(Q\zeta=\mathbb E_\Gamma[\zeta(x',y')\mid x,y]\). Let \(O_L\) and \(M_L\) retain the left spatial coordinates of the outer and middle pairs, respectively, and let \(Q_L\) be their actual marginal conditional map. It is not the transfer of an independently prepared block.

For an outer source \(\zeta\), define
\[
\zeta_L=\mathbb E_{\mu_3}[\zeta\mid O_L],\quad
d=\zeta-\zeta_L,\quad
e=\mathbb E_\Gamma[d\mid M_L],\quad
r=Q\zeta-\mathbb E_\Gamma[Q\zeta\mid M_L].
\tag{SB12}
\]
The tower property gives \(\mathbb E[Q\zeta\mid M_L]=Q_L\zeta_L+e\). Orthogonality therefore gives the exact before/after-sewing ledger
\[
\boxed{
V_Q(\zeta)=V_{Q_L}(\zeta_L)+\|d\|_{\mu_3}^2-\|e\|^2
-2\operatorname{Re}\langle Q_L\zeta_L,e\rangle-\|r\|_{\mu_1}^2,}
\tag{SB13}
\]
where \(V_Q(\zeta)=\|\zeta\|_{\mu_3}^2-\|Q\zeta\|_{\mu_1}^2\); the analogous regional norms use the true marginal laws. Both norms and both source-exchange terms have changed. Dropping \(e\) assumes a conditional source-transport property that sewing alone does not supply.

For a left outer source \(\zeta_L\), condition on \(M_L\). The remaining left history and right history still satisfy (SB9); marginalizing to the right middle pair preserves that bound. Hence
\[
\|Q\zeta_L-Q_L\zeta_L\|^2
\le\eta^2 V_{Q_L}(\zeta_L),\qquad
V_Q(\zeta_L)\ge(1-\eta^2)V_{Q_L}(\zeta_L).
\]
For a general source the conditional-projection triangle inequality now gives
\[
\boxed{
\sqrt{V_Q(\zeta)}
\ge\left[
\sqrt{1-\eta^2}\sqrt{V_{Q_L}(\zeta_L)}
-\|d\|_{\mu_3}
\right]_+.}
\tag{SB14}
\]
This is a bound on the actual chronological \(Q\), not on a block-update generator.

In particular, retain the same physical source throughout OI:
\[
h_f(x,y)=f(y)-(Af)(x),\qquad
\zeta=\iota h_f,\qquad
C_{\rm lag}(h_f)=\|\zeta\|_{\mu_3}^2-\|h_f\|_{\mu_1}^2.
\]
Even when \(f\) is regional, \(Af\) generally is not; \(d\) in (SB12) measures the resulting discarded outer information. Equation (SB14) gives the explicit sufficient block test
\[
\left[
\sqrt{1-\eta^2}\sqrt{V_{Q_L}(\zeta_L)}-\|d\|_{\mu_3}
\right]_+^2
\ \ge\ C_{\rm lag}(h_f)+c\|h_f\|_{\mu_1}^2.
\tag{SB15}
\]
If independently established on the required source carrier, this implies the OI surplus with that \(c\). Neither (SB9) nor finite local coercivity establishes (SB15). In particular, a positive regional variance must pay both the source leakage and the changed-lag cost.

## A discriminator and the next seam experiment

Interface strength alone cannot bound the cap in arbitrary positive chronologies. On two spins, take
\[
H_\epsilon=R I-\epsilon(X_A+X_B)-JZ_AZ_B,\qquad
R=\sqrt{J^2+4\epsilon^2},\quad J,\epsilon>0.
\]
Its strictly positive normalized ground amplitude in the \(Z\) basis has matrix
\[
\psi_\epsilon=\begin{pmatrix}a&b\\b&a\end{pmatrix},\qquad
\frac ab=\frac{R+J}{2\epsilon},\qquad
\Delta(\psi_\epsilon)=2\log\frac ab .
\tag{SB16}
\]
Diagonalizing the symmetric two-dimensional sector gives these formulas; the other energies before the common shift are \(-J,J\), so the physical gap is \(R-J\). At fixed single interface coupling \(J\), the cap oscillation diverges and the gap closes as \(\epsilon\downarrow0\). The regional kinetic scales also close. This is a finite stoquastic-transfer discriminator, not a Wilson or non-Abelian counterexample: an interface estimate needs regional chronological control, not merely an interface count.

[[adjacent-wilson-plaquette-and-the-chronological-surplus|AP1–20]] now performs the seam experiment on the actual two-square Wilson transfer. The left raw-link marginal remains Haar, and its vacuum cap conditioned on the common edge is one, while the actual three-slab source leakage has a strictly positive quadratic coefficient. The fixed left source's surplus can improve even as the complete physical gap decreases. The common edge cannot be frozen when using the unfrozen chronological bound (SB14).

The [[three-face-corner-and-joint-seam-response|joint-seam programme]] retains a shared edge between the two added interactions and compares the full-sector edge with the fixed source. Its complete amplitude must retain (SB4), the source-exchange correction (SB13), the \(\mu_1\)-to-\(\mu_3\) cost and the actual vacuum normalization. Whether their combined non-Abelian response supplies a positive surplus through the required physical limits remains open.

[[compact-regional-covariance-and-susceptibility-return|The compact regional return]] preserves the inherited harmonic covariance and susceptibility of each fixed finite profile family. [[vacuum-hellinger-return-and-regional-conditional-projections|The actual one-face conditional kernels]] fail the semigroup law, with a defect equal to the information propagated outside the retained region. [[regional-innovation-and-exterior-information-balance|The regional innovation balance]] fixes how that omitted information changes the predictor variance and the squared full response. This channel must be transported alongside the cap, source-exchange and changed-lag terms above; it is not automatically identical to any one of those history-dependent costs. [[uniform-collar-capture-and-the-local-gap-limitation|Uniform collar capture]] now controls it on every one-face radial harmonic source, with a compact return for the prescribed quadratic away from zero scaled time. [[finite-pairing-range-and-the-harmonic-innovation-floor|The pairing-range theorem]] now gives the quadratic floor's order \(\min\{1,t/(R+1)\}\), and [[compact-quadratic-carrier-and-the-pairing-range-return|the compact quadratic return]] preserves it on the quantified window for every signed matrix. Thus even the growing quadratic inventory still loses a range-independent floor. [[four-face-diagonal-sources-and-the-relational-schur-defect|The four-face Schur test]] exposes the old/new mixed deficit explicitly. [[four-face-oriented-source-extension-and-the-schur-surplus|Its oriented extension]] removes the positive leakage left by even the optimal quadratic readout and follows the negative gap correction. SB15 therefore needs a law for the complete sourced composition, with all three-slab history terms retained; automatic positive reinforcement under source extension is not available at this order.

A proposed normal-form reduction of those marked histories must transport products and regional embeddings. [[two-face-source-access-and-the-normal-form-obstruction|The access obstruction]] rules out matching the entire prepared pair inventory by one odd normal form. [[four-face-covariant-route-response|The nonnested conditional calculation]] and [[conditional-boundary-translation-and-source-products|its retained boundary message]] restore original source products with the actual vacuum. [[covariant-source-memory-and-the-first-chronological-response|The first chronological comparison]] carries these jets into a nonzero mixed physical-scalar exterior response. [[radius-orientation-chronological-gram-and-the-source-pencil|The complete covariance]] and [[radius-orientation-source-extension-and-the-innovation-floor|its generalized source comparison]] now retain both innovation forms and prove strict lowering relative to the actual radius-only quotient at short fixed duration. These use the original transfer, with no conditional-update clock. The single-time exterior form still has to be compared with the complete history terms in (SB15).

[[logarithmic-vacuum-curvature-and-conditional-cumulants|The next conditional correction]] forces a fourth cumulant, and [[equal-character-hessians-and-the-nonlinear-source-discriminator|the equal-Hessian preparation family]] distinguishes nonlinear source and spectral data invisible to the first-order law. These are further channels for spatial sewing to retain. Neither they nor the evaluated mixed source pencil replace SB15's vacuum caps, source exchange, changed lag and required uniform estimates.

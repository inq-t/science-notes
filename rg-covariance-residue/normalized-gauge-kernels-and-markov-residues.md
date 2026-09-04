# Normalized Gauge Kernels and Markov Residues

A probability-valued gauge block can cover every fine configuration while preserving symmetry among equally weighted paths. Its normalization preserves the original fine law exactly, including configurations where a deterministic polar mean is singular. On the enlarged joint carrier, nested suffix algebras recover the same covariance-residue theorem as deterministic blocking. This is an auxiliary integration construction, not a claim that nature is fundamentally stochastic; its discarded correlations still require an independent ultraviolet estimate.

## A full-domain readout with a different codomain

Let \(G\subset U(r)\) be a compact matrix group with normalized Haar measure. For each coarse link \(b\), choose finitely many fine path transports \(W_{b,i}(U)\in G\) sharing its endpoints, and fixed nonnegative weights summing to one. Put

$$
Z_b(U)=\sum_iw_{b,i}W_{b,i}(U),\qquad
\phi(V,Z)=\frac1r\operatorname{ReTr}(V^*Z).
\tag{NK1}
$$

The matrix \(Z_b\) need not belong to \(G\) or be invertible. For a finite dimensionless parameter \(\kappa\ge0\), define

$$
\begin{aligned}
N_\kappa(Z)&=\int_G e^{\kappa\phi(W,Z)}\,\mathrm dW,\\
q_\kappa(V\mid U)
&=\prod_b
\frac{e^{\kappa\phi(V_b,Z_b(U))}}{N_\kappa(Z_b(U))}.
\end{aligned}
\tag{NK2}
$$

This returns an element of \(\operatorname{Prob}(G^{\mathcal B})\), not a selected group element. It therefore does not contradict [[regular-gauge-averages-and-the-selection-obstruction|the deterministic selection obstruction]].

Since \(\|Z_b\|_{\rm op}\le1\), each normalized factor lies between \(e^{-2\kappa}\) and \(e^{2\kappa}\). It is smooth and strictly positive, including at singular averages. Those per-link bounds do not constitute volume-uniform bounds on the whole product.

Under endpoint transformations, \(V_b\) and \(Z_b\) both transform as \(g_s(\cdot)g_t^{-1}\). The pairing and Haar integral are invariant, so the kernel is gauge equivariant. Equal weights give permutation symmetry among the paths; unequal weights allow simultaneous permutation of weight-path pairs, not arbitrary permutation at fixed unequal weights. Path overlaps cause no coordinate singularity because (NK2) is not an attempted change of variables.

Normalized gauge-blocking kernels have a direct precedent in [[library/the-classically-perfect-fixed-point-action-for-su3-gauge-theory/inq|DeGrand, Hasenfratz, Hasenfratz, and Niedermayer (1995)]], equations (4)--(7). Their normalization keeps the partition function unchanged. Their exponent uses a product of blocking and action coefficients; \(\kappa\) here denotes the entire coefficient in (NK2).

## The normalization is part of the hidden action

Start with a finite smooth law
\(\mu(\mathrm dU)=Z_{\rm fine}^{-1}e^{-S(U)}\mathrm dU\). Define

$$
\mathbb P(\mathrm dU,\mathrm dV)
=\mu(\mathrm dU)\,q_\kappa(V\mid U)\,\mathrm dV.
\tag{NK3}
$$

Integrating out \(V\) gives exactly \(\mu\). All original expectations of fine observables are unchanged. Conditioning on \(V\) instead gives a fixed-Haar hidden carrier,

$$
\begin{aligned}
\nu_V(\mathrm dU)&=\mathcal Z(V)^{-1}e^{-A(V,U)}\mathrm dU,\\
A(V,U)&=S(U)-\kappa\sum_b\phi(V_b,Z_b(U))
+\sum_b\log N_\kappa(Z_b(U)).
\end{aligned}
\tag{NK4}
$$

There is no excluded region or coarea singularity. Omitting the **plus** normalization term changes the fine marginal to one proportional to
\(e^{-S(U)}\prod_bN_\kappa(Z_b(U))\).
Unless that product is \(U\)-independent, this is a different normalized fine theory, not another coordinate presentation. At \(\kappa=0\), or with one group-valued path per block, the normalizer is constant and only the overall normalization changes.

For a right coarse variation \(V_b\mapsto V_be^{tX}\), \(X\in\mathfrak g\), the real retained score is

$$
s_{b,X}=R_{b,X}A
=\frac{\kappa}{r}\operatorname{ReTr}\!\left(XV_b^*Z_b(U)\right).
\tag{NK5}
$$

The [[conditioned-source-transport|conditioned-source derivative]] is consequently

$$
R_{b,X}KF=-\operatorname{Cov}_{\nu_V}(s_{b,X},F),
\qquad KF(V)=\nu_V(F),
\tag{NK6}
$$

for a fine source \(F(U)\); an explicitly \(V\)-dependent source adds its direct derivative. The real score occupies the first slot of the sesquilinear covariance.

The normalizer has no \(V\)-derivative, but it remains in \(\nu_V\) and its response operator. For
$$
\mathcal M_\kappa(Z)=
\frac{\int_G W e^{\kappa\phi(W,Z)}\,\mathrm dW}{N_\kappa(Z)},
$$
direct differentiation gives

$$
d_UA=d_US-\frac{\kappa}{r}\sum_b
\operatorname{ReTr}\!\left[
(V_b-\mathcal M_\kappa(Z_b))^*d_UZ_b\right].
\tag{NK7}
$$

The matrix moment \(\mathcal M_\kappa\) is not generally a group element. Formula (NK7) displays the normalizer's contribution to the hidden mean force.

If \(p_{b,e}=\sum_iw_{b,i}n_{b,i,e}\) is the weighted number of occurrences of fine edge \(e\) in the paths, unitary product differentiation yields

$$
|s_{b,X}|\le\kappa\|X\|_{\rm op},\qquad
|D_{e,Y}s_{b,X}|
\le\kappa\|X\|_{\rm op}\|Y\|_{\rm op}p_{b,e}.
\tag{NK8}
$$

These are local score bounds. They do not control the inverse conditional Witten operator acting on the score.

[[compact-gauge-kernel-tangent-response|The compact tangent-response calculation]] now evaluates the normalizer's second derivative exactly. At coincident inputs, a mode Hessian penalizes path scatter, while the forward Fisher metric detects only the averaged velocity. Its normalized diffusive limit matches [[soft-gaussian-gauge-blocking|the soft Gaussian carrier]] in four dimensions with the declared physical noise scale. This is a fixed-regulator local limit, not uniform nonlinear response control.

## The correct filtration for probabilistic blocking

Let standard Borel carriers and normalized Markov kernels define

$$
\mathbb P(\mathrm dx_0\cdots\mathrm dx_J)
=\mu_0(\mathrm dx_0)
\prod_{j<J}\mathsf Q_j(\mathrm dx_{j+1}\mid x_j).
\tag{NK9}
$$

Take \(F,G\in L^2(\mu_0)\), viewed as functions of \(X_0\), and let all conditional-expectation projections act on \(L^2(\mathbb P)\). The individual sigma algebras \(\sigma(X_j)\) need not be nested. Use instead

$$
\mathcal B_j=\sigma(X_j,\ldots,X_J),\qquad
E_j=\mathbb E_{\mathbb P}[\,\cdot\mid\mathcal B_j].
\tag{NK10}
$$

These are nested on one extended law, with \(E_0=I\). For an initial source \(F(X_0)\), conditional independence of past and future given the present gives

$$
E_jF
=\mathbb E[F(X_0)\mid X_j]
=f_j(X_j).
\tag{NK11}
$$

This representation is not asserted for arbitrary functions of the entire chain. A history-dependent blocking rule needs an enlarged Markov state.

Let \(\mu_j\) be the actual \(X_j\) marginal. Define the reverse conditional kernel by

$$
\mu_j(\mathrm dx)\mathsf Q_j(\mathrm dy\mid x)
=\mu_{j+1}(\mathrm dy)\nu_{j,y}(\mathrm dx).
\tag{NK12}
$$

Then \(f_{j+1}(y)=\nu_{j,y}(f_j)\). Orthogonality of
\(D_j=E_j-E_{j+1}\) proves

$$
\boxed{
\operatorname{Cov}_{\mu_0}(F,G)
=\operatorname{Cov}_{\mu_J}(f_J,g_J)
+\sum_{j<J}\int
\operatorname{Cov}_{\nu_{j,y}}(f_j,g_j)\,
\mu_{j+1}(\mathrm dy).}
\tag{NK13}
$$

Thus [[inq|the covariance-residue summation theorem]] applies unchanged to initial physical sources when its uniform shell and terminal bounds are proved on this extended carrier. The reverse kernel \(\nu\), not the forward readout kernel \(\mathsf Q\), controls the forgotten conditional correlations.

## An exact negative control

At the first step, \(\kappa=0\) makes \(X_1\) independent product Haar, unrelated to \(X_0\). For centered initial \(F\),

$$
f_j=0\ (j\ge1),\qquad D_0F=F,\qquad D_jF=0\ (j\ge1).
\tag{NK14}
$$

Every original correlation then lies in the first residue, even though the terminal covariance vanishes. If the original law has a massless power-law tail, the residue has that tail too.

Likewise, \(L^2\) contraction of conditional expectation does not bound spatially weighted source derivatives. A convenient, rapidly mixing forward readout can coexist with uncontrolled reverse conditional correlations.

The parameter \(\kappa\), path family, and weights are supplied blocking choices. This construction is removable auxiliary bookkeeping, not an assertion about ontological dice, a mechanism selecting an observed outcome, or a mass scale. Gauge covariance also does not by itself prove reflection positivity or locality of the induced coarse law. A Clay proof still needs the actual non-Abelian response estimates, a Yang--Mills continuum limit, and the full reconstruction hypotheses.

[[receipts/normalized_kernel_receipt.py|The finite verification receipt]] checks exact normalization on a finite compact subgroup, the score derivative with complex sources, and nested Markov suffix projections. Its independent-readout and nonnested-state-algebra controls test why neither a trivial coarse law nor separate single-state projections establish a gap.

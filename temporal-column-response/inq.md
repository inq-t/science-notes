---
inq.module: "temporal-column-response"
inq.include:
  - "**/*.md"
  - "**/*.py"
---
# Temporal Column Response

Strong dependence along time need not be counted as a weak interaction. Treat a complete finite temporal history as one variable, control its internal conditional propagation in blocks, and measure the response between histories in a bounded path metric. A local perturbation then pays a temporal susceptibility, not the total preparation depth. When inter-column influence is small, this gives a volume- and horizon-uniform variance factorization; smoothed midpoint conditionals turn it into an inequality for the actual vacuum.

**Status: [EXACT CONDITIONAL THEOREM] for finite compact chains with the kernel, potential and inter-column bounds stated below.** The [[strong-coupling-gap-and-continuum-crossover/wilson-temporal-column-coercivity|Wilson application]] supplies those bounds in an anisotropic strong-coupling regime. This is a response construction, not a primitive stochastic ontology or a four-dimensional continuum theorem.

## A block retains every internal potential

Let \(M\) be a compact metric space with a probability reference measure \(m\), and let \(k(u,v)>0\) be a continuous symmetric Markov density. Fix an integer \(n\ge1\) and constants
\[
0<m_n\le k^{(n)}(u,v)\le M_n<\infty,\qquad R_n=M_n/m_n.
\tag{TC1}
\]
Consider finite open chains with density proportional to the product of their \(k\) bonds, one-site factors \(e^{-v_t}\), and separate nonnegative left and right end weights for which the partition function is finite and strictly positive. Assume \(\operatorname{osc}v_t\le b\). Fixed endpoints are also allowed. Bounds below are independent of the end weights and chain length. Periodic time or a correlated joint endpoint weight requires a different argument.

An \(n\)-bond conditional kernel \(A_{s,s+n}\) includes all intermediate potentials. Additive constants in the \(v_t\)'s do not change normalized laws. Center the included potentials so their absolute values are at most \(b/2\). With at most \(n\) such factors,
\[
e^{-nb/2}k^{(n)}(u,v)
\le A_{s,s+n}(u,v)
\le e^{nb/2}k^{(n)}(u,v).
\tag{TC2}
\]
Endpoint multipliers can instead be left outside the kernel; they cancel from its cross ratios. Thus
\[
\mathfrak D(A_{s,s+n})\le2\log R_n+2nb,\qquad
\tau:=\tanh\!\left(\frac{\log R_n+nb}{2}\right)<1.
\tag{TC3}
\]
The [[vacuum-aligned-innovation-completion/boundary-action-fixed-points-and-physical-linearization|likelihood-ratio lemma]] implies that any two normalized rows have total-variation distance at most \(\tau\), even after multiplication by the same future message. This controls a genuine inhomogeneous interacting conditional chain, not a power of its kinetic kernel with the potentials removed.

## One coupling controls the entire path

Condition at time \(r\) on two different values. Past and future are independent given that value. In either direction, couple successive \(n\)-step endpoint transitions maximally. Once the two block starts agree, draw the whole next block identically. Otherwise couple the block endpoints and fill each block with its exact conditional bridge.

After \(j\) completed blocks, disagreement has probability at most \(\tau^j\). Every internal point of the next block has disagreement probability at most that of its starting point. A terminal partial block only shortens the bound. This is one compatible coupling of whole paths, giving
\[
\Pr(Y_t\ne Y'_t)\le a_{|t-r|},\qquad
a_d:=\tau^{\lfloor d/n\rfloor},\qquad
\mathcal S:=\sum_{d\in\mathbb Z}a_{|d|}
=\frac{2n}{1-\tau}-1.
\tag{TC4}
\]
Here \(a_0=1\), including the \(\tau=0\) case. Common external endpoints and end messages do not change the estimate.

For a bounded function \(F\) of the entire path, let \(\delta_tF\) be its single-time oscillation. The coupling gives
\[
\operatorname{osc}_{y_r}\mathbb E[F\mid Y_r=y_r]
\le\sum_t\delta_tF\,a_{|t-r|}.
\tag{TC5}
\]
An insertion \(h(Y_r)\) therefore satisfies
\[
|\operatorname{Cov}(F,h(Y_r))|
\le\frac{\operatorname{osc}h}{4}
\sum_t\delta_tF\,a_{|t-r|}.
\tag{TC6}
\]
This is an ordinary covariance bound, derived by conditioning on \(Y_r\) and bounding covariance by one quarter of the product of oscillations.

## A local insertion has a finite whole-column cost

Use a compact compatible base metric \(d_0\le1\) on \(M\), and on a finite column set
\[
d_{\mathrm{col}}(u,v)=\sum_t d_0(u_t,v_t).
\tag{TC7}
\]
The expected cost under (TC4) is at most \(\mathcal S\). Suppose two chain laws differ only by a factor \(e^{-h(Y_r)}\), and interpolate their one-site potentials linearly, remaining in the class \(\operatorname{osc}v_t\le b\). Their derivatives are \(-\operatorname{Cov}(F,h)\). For every \(1\)-Lipschitz \(F\) in (TC7), \(\delta_tF\le1\). Integration and Kantorovich duality give
\[
W_{1,d_{\mathrm{col}}}(\mu,\mu')
\le\frac{\operatorname{osc}h}{4}\mathcal S.
\tag{TC8}
\]
The Hamming mismatch in the coupling proves an upper bound on this compact Polish metric. It is not an assertion that the uncountable discrete Hamming topology is Polish.

This bound is Lipschitz in the whole input path's distance. It is not a horizon-uniform total-variation estimate between laws with arbitrarily different complete exterior paths.

Now let columns be indexed by spatial sites \(e\). Suppose changing one value \(u_{f,r}\) to \(v_{f,r}\) in exterior column \(f\) changes column \(e\)'s conditional potential only at time \(r\), by \(h\) satisfying
\[
\operatorname{osc}h\le4J_{ef}d_0(u_{f,r},v_{f,r}).
\tag{TC9}
\]
Telescoping over changed times and applying (TC8) bounds the column interdependence coefficients by \(C_{ef}=\mathcal S J_{ef}\). If a nonnegative majorant satisfies
\[
q:=\sup_e\sum_{f\ne e}C_{ef}<1,
\tag{TC10}
\]
then [[library/poincare-and-transportation-inequalities-for-gibbs-measures-under-the-dobrushin-uniqueness-condition/inq|Wu's Theorem 2.1]] applies on the finite compact column space:
\[
\boxed{(1-q)\operatorname{Var}_\mu F
\le\sum_e\mathbb E_\mu
\operatorname{Var}(F\mid\hbox{all columns except }e).}
\tag{TC11}
\]
Finite-horizon metric diameters grow with horizon, but all are finite; the spectral constant in (TC11) depends on the influence matrix, not those diameters. Neither a space of infinite paths with this metric nor a passage of that metric to continuous time is required.

[[temporal-column-response/spatial-elimination-and-self-return|Spatial coordinate elimination]] preserves this certified subcritical bound after integrating any set of hidden columns, provided their mediated self-returns are normalized correctly. The exact matrix criterion cannot be improved just by recycling the same majorant. A finite Ising example nevertheless shows that a fresh computation of the actual marginal can improve its influence radius, so failure of that majorant is not failure of the coarse-graining method.

## Extract the actual midpoint, not an arbitrary reference state

Suppose also that \(M\) is a compact Riemannian manifold whose reference law has gradient Poincare constant \(\lambda_m>0\). A midpoint at least \(n\) bonds from each temporal end has, conditional on the other entire columns, density
\[
p_e(u)\propto e^{-v_0(u)}L_e(u)R_e(u).
\]
An \(n\)-bond smoothing of either incoming message has log-oscillation at most \(\log R_n+nb\), by (TC2). Consequently
\[
\operatorname{osc}\log p_e\le D_{\mathrm{mid}}
:=b+2nb+2\log R_n.
\tag{TC12}
\]
Reference-law comparison gives conditional midpoint Poincare constant at least \(\lambda_m e^{-D_{\mathrm{mid}}}\). Apply (TC11) only to functions of the complete midpoint, then apply this single-coordinate inequality inside each conditional variance:
\[
\boxed{\operatorname{Var}_{\nu_N} f
\le\frac{e^{D_{\mathrm{mid}}}}{\lambda_m(1-q)}
\int\sum_e|\nabla_ef|^2\,d\nu_N.}
\tag{TC13}
\]
If the finite-volume midpoint preparations converge to an actual vacuum law \(\nu\), smooth bounded tests pass the same inequality to \(\nu\). This needs convergence of those marginal laws, not a horizon-uniform Perron convergence rate.

There is no global density comparison with product \(m\); only a one-coordinate midpoint comparison after conditioning on the rest of the histories. Nor does (TC13) yet give a finite-step physical transfer or complete midpoint-to-two-endpoint gap. The [[strong-coupling-gap-and-continuum-crossover/wilson-to-hamiltonian-vacuum-limit|Hamiltonian limit]] supplies one additional physical return with an exact ground-state Dirichlet identity.

[[library/uniqueness-problem-for-quantum-lattice-systems-with-compact-spins/inq|Albeverio, Kondratiev, Minlos and Shchepan'uk]] provide a separate path-space precedent: their compact-spin pair-interaction proof keeps both heat-kernel and integrated interaction activities after temporal blocking. Their uniqueness theorem is not the column inequality above and is not a Yang--Mills bridge theorem.

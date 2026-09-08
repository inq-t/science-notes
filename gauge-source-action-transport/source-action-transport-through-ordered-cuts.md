# Source Action Transport through Ordered Cuts

An ordered cut preserves a retained heat source's state, likelihood and Fisher response when the actual source actions travel through the cut. The resulting actions depend on the preceding path pieces. Endpoint-only transport discards score information, while independently resetting regional actions changes the interacting response even when the state agrees. Exact covariance preserves a chosen experiment without selecting it.

**Status: exact source-transport identities, finite chain realization and first-order interacting obstruction for the specified heat sources.** The source action, heat parameters and interaction remain inputs. No four-dimensional reconstruction or physical gap follows.

## Endpoint transport changes the experiment

The normalized heat bridge in
[[gauge-graph-source-response/loop-correlations-and-the-source-response|the loop-tilt construction]]
is unchanged by a potential depending only on its terminal product.
However,
[[conditional-fisher-coercivity/measure-preserving-horizontal-lifts#A law-preserving lift has the marginal likelihood|conditional-law-preserving lifts]]
have exactly the marginal likelihood, not the retained-path likelihood.

For \(G=SU(2)\), \(Q=-2\operatorname{Tr}\), and endpoint law
\(p_t(W)dW\), the experiment
\(W\mapsto e^{\epsilon\xi}We^{-\epsilon\eta}\) has Fisher pairing
\[
g_{\rm end}(\xi,\eta)=j_t|\xi-\eta|_Q^2,\qquad
j_t=\frac13\int|\nabla\log p_t|_Q^2p_t\,dW,\qquad
0<j_t<\frac1{2t}.
\tag{ST1}
\]
Centrality makes its score depend only on \(\xi-\eta\);
adjoint invariance makes its Gram scalar. Positivity follows
because the finite-time heat density is not constant.
For strictness, take the retained-source ramp with endpoint
controls \(\xi=\alpha\delta,\eta=-\beta\delta\),
\(\alpha+\beta=1\). Its nonzero score is an unbounded Gaussian
with variance \(|\delta|^2/(2t)\). Its conditional endpoint score
is smooth and bounded. Their conditional variance cannot vanish,
so (MH17) gives the strict inequality.

On class functions the Fisher dual of this endpoint experiment is
\(j_t^{-1}|\nabla f|^2\), strictly greater than the retained-source
response \(2t|\nabla f|^2\) wherever the gradient is nonzero.
Thus the endpoint-only lift already changes the zero-tilt response.
It is not a repair of that retained-source construction.

## Cut the complete retained paths instead

Use the based paths \(U,V\) of
[[gauge-path-fisher-response/heat-factor-response-and-the-compression-defect|the heat-factor construction]],
of speeds \(\alpha,\beta>0\), over \([0,s+t]\).
Their readout is \(X=UV^{-1}\). Write their left future increments as
\[
U^{(2)}_u=U_s^{-1}U_{s+u},\qquad
V^{(2)}_u=V_s^{-1}V_{s+u}.
\]
Define the source cut
\[
\Phi_s(U,V)=
\left(U_{\le s},V_{\le s},
\widetilde U_u=\operatorname{Ad}_{V_s}U^{(2)}_u,
\widetilde V_u=\operatorname{Ad}_{V_s}V^{(2)}_u\right).
\tag{ST2}
\]
Its inverse is explicit:
\[
U_{s+u}=U_sV_s^{-1}\widetilde U_uV_s,\qquad
V_{s+u}=\widetilde V_uV_s.
\tag{ST3}
\]
Conditioned on the prefix, simultaneous conjugation preserves the
independent future heat laws. Thus \(\Phi_s\) is a probability-space
isomorphism onto the product of the two regional paired-path laws.
With \(Y_s=U_sV_s^{-1}\) and
\(Z_u=\widetilde U_u\widetilde V_u^{-1}\), it gives
\[
X_{s+u}=Y_sZ_u.
\tag{ST4}
\]
The complete readout therefore agrees with the charged ordered cut,
including observables that pair nontrivial boundary charges.

Now act on the whole source by \(U\mapsto kU,V\mapsto lV\).
Put \(\kappa_u=k_s^{-1}k_{s+u}\) and
\(\ell_u=l_s^{-1}l_{s+u}\). Recutting the transformed paths gives
\[
\boxed{
\begin{aligned}
\widetilde U'_u
 &=l_sY_s^{-1}\kappa_uY_s\,\widetilde U_ul_s^{-1},\\
\widetilde V'_u
 &=l_s\ell_u\,\widetilde V_ul_s^{-1}.
\end{aligned}}
\tag{ST5}
\]
The prefix retains its original \(kU,lV\) actions.
Equation (ST5) follows by substituting (ST3), not by choosing a
mobility to cancel a response defect. The future action is
prefix-dependent. Independently resetting deterministic future
factor translations is a different source experiment.

## What full source covariance proves

For any bimeasurable source isomorphism
\(\Phi:S_{\rm whole}\to S_{\rm cut}\), set
\(\nu_{\rm cut}=\Phi_*\nu_{\rm whole}\) and
\(T_{\rm cut}=\Phi T_{\rm whole}\Phi^{-1}\).
Whenever the source pushforward is absolutely continuous,
\[
\frac{d(T_{\rm cut})_*\nu_{\rm cut}}{d\nu_{\rm cut}}
=
\left(\frac{d(T_{\rm whole})_*\nu_{\rm whole}}
            {d\nu_{\rm whole}}\right)\circ\Phi^{-1}.
\tag{ST6}
\]
Changing variables proves equality of relative entropies.
For every finite-dimensional control family through the identity, assume
that its likelihoods are differentiable in quadratic mean at zero:
\(\sqrt{R_\theta}=1+\tfrac12\sum_a\theta_aS_a+o(|\theta|)\)
in \(L^2(\nu_{\rm whole})\), with \(S_a\in L^2(\nu_{\rm whole})\).
Composition with \(\Phi^{-1}\) is an \(L^2\) isometry, so it transports
this expansion, the scores and their Fisher Gram matrix. Assume also
that the selected observable core has derivatives along these actions.
Differentiating the conjugated-action identity transports those
derivatives; an abstract measurable \(\Phi\) need not itself have a
differential.
Quotient score radicals and complete the entire control space
isometrically. For derivatives continuous in that norm, their full
pointwise dual responses agree, hence so do their integrated forms.
Neither a selected submatrix nor a newly selected family of
controls is covered by this statement.

An interaction \(e^{-\lambda\mathcal V(X)}\), with a specified
real smooth common-conjugation-invariant finite-evaluation
\(\mathcal V\), travels through the
same map. Equations (ST2)--(ST6) therefore preserve its complete
source likelihood and response, not only the unweighted law.
For such bounded cylinder weights, the [[gauge-graph-source-response/loop-correlations-and-the-source-response#Coercivity survives every finite smooth tilt|Gaussian-tail comparison (LT15)--(LT17)]] applies with
\(\sup\Gamma_0(\mathcal V)<\infty\). It makes the tilted response
norm equivalent to the unweighted one at each fixed finite
coupling and horizon.

Multiplication and inversion carry the smooth finite-holonomy
cores bijectively through (ST2)--(ST4), inserting the cut endpoint
when necessary. Closing these isometric core identities therefore
transports the complete cylinder-closure form domains and rebuilt
generators. This does not identify them with any independently
specified larger domain. It also does not make the original source
semigroup preserve the output subspace. The unweighted source
non-descent theorem survives this change of presentation; no
non-descent theorem for every tilted source generator is asserted.

For several cuts, the \(j\)-th raw increment pair is conjugated
by the cumulative original \(V\)-prefix. The equality
\(\operatorname{Ad}_{V_1V_2}
=\operatorname{Ad}_{V_1}\operatorname{Ad}_{V_2}\) and the explicit
inverse path reconstruction make both parenthesizations identical.
This is covariance under ordered cuts, not an intrinsic
irreversibility theorem.

## Independent edge actions fail after a tilt

[[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock#The ordered response is a reduced chain geometry|The paired-edge chain]]
realizes the entire unweighted ordered form on a finite graph.
Consider two of its bigons and
\[
W=U_1U_2V_2^{-1}V_1^{-1},\quad
q(W)=\tfrac12\operatorname{Tr}W,\quad
\mathcal V=1-q(W).
\]
Take each raw edge to be one retained heat path with independent
deterministic left shifts. Its four heat lengths, in order
\((U_1,U_2,V_1,V_2)\), are
\[
d=(\alpha t_1,\alpha t_2,\beta t_1,\beta t_2),
\qquad t=t_1+t_2=\sum_ed_e,\quad
m=e^{-3t/4}.
\tag{ST7}
\]
Haar vertex frames can impose the complete Gauss carrier; invariant
readouts and their source derivatives do not depend on these
frames. These single-path edge sources have the same unweighted
response as [[gauge-graph-source-response/haar-vertex-source-and-joint-gauge-response#The same source fixes the mixed endpoint response|the paired-factor endpoint construction (HV6)]].
They are not being identified as tilted statistical experiments.

Write \(p_e=D_eq(W)\) for the actual left raw-edge covector,
\(s=(1,1,-1,-1)\), \(r_e=s_ep_e\), and
\(w=\nabla_Lq(W)\). Every \(r_e\) is an adjoint rotation of \(w\).
The unweighted endpoint-control dual is
\(D_0=\operatorname{diag}(2d_e)\otimes I_3\).
Independence and the scalar fundamental heat means give
\[
\mathbb E_0q(k_1U_1k_2U_2V_2^{-1}k_4^{-1}V_1^{-1}k_3^{-1})
=m q(k_1k_2k_4^{-1}k_3^{-1}).
\]
Its potential Hessian is consequently
\[
\mathsf H_0=\frac m4(ss^T)\otimes I_3.
\tag{ST8}
\]
The [[gauge-graph-source-response/loop-correlations-and-the-source-response#Conjugation reduces the whole entropy correction to endpoints|common-conjugation argument (LT8)]] applies to these
independent retained paths too: their full Fisher correction is
the averaged endpoint Hessian, with zero-endpoint bridges
orthogonal to endpoint ramps. Differentiating the *full* inverse
stiffness therefore gives
\[
\dot\Gamma_{{\rm raw},0}(q)
=-p^TD_0\mathsf H_0D_0p
=-m\left|\sum_ed_er_e\right|^2.
\]
The original whole paired-path experiment instead gives
\(\dot\Gamma_{{\rm whole},0}(q)=-mt^2|w|^2\).
Since all \(|r_e|=|w|\), their difference is exactly
\[
\boxed{
\dot\Gamma_{{\rm raw},0}(q)-\dot\Gamma_{{\rm whole},0}(q)
=m\sum_{e<f}d_ed_f|r_e-r_f|^2.
}
\tag{ST9}
\]
This identity is on the retained source; do not declare its
individual terms basic before conditional averaging.

Its expectation is strictly positive. For example, at
\(V_1=V_2=e\), \(U_1=e^{aT_1}\), \(U_2=e^{bT_2}\), three
\(r_e\) equal \(w\), while
\(r_{U_2}=\operatorname{Ad}_{U_1}^{-1}w\ne w\) for generic
nonzero \(a,b\). Continuity and strictly positive heat densities
give an open positive-measure witness. The two complete increment
states coincide at every coupling. Their common density derivative
cancels in the energy comparison because both unweighted
responses equal \(2t|w|^2\). Hence
\[
\left.\partial_\lambda\right|_0
\bigl[\mathcal E_{{\rm raw},\lambda}(q)
      -\mathcal E_{{\rm whole},\lambda}(q)\bigr]>0.
\tag{ST10}
\]
Smooth finite-matrix dependence proves a mismatch for sufficiently
small positive coupling, not for every coupling.

## The selecting obligation is now sharper

Order need not be an arbitrary error: the chain supplies a concrete
incidence geometry whose reduction returns it. But that geometric
realization does not settle which transformations count as
admissible comparisons after interaction. Full source transport
succeeds because it carries those transformations; independently
resetting them fails even on the same underlying increment space.

The next primitive law must therefore constrain an interaction
*and* a compatible family of comparison actions through graph
assembly. Merely conjugating a previously chosen action proves
covariance, not selection. In particular, arbitrary positive loop
weights remain admissible in (ST6), so this exact transport theorem
does not select a Yang--Mills vacuum or force a gap.

[[gauge-source-action-transport/joint-path-law-and-the-shared-boundary-action|The theta-path test]]
obtains one compatibility condition without first prescribing
the transported family. Its joint quadratic variation forces the
right controls of neighboring loop paths to agree. The surviving
family is closed under the two tree charts. Independent right
controls give mutually singular joint laws, not additional finite
Fisher directions. This is a restriction supplied by the joint
path state; bounded positive interaction tilts retain exactly the
same restriction, so it does not select their potential.

The separate
[[algebra/octonionic-associator-and-branch-forgetting|octonionic branch construction]]
already supplies a nonzero multiplication associator and its
positive vector response. Such a parent could constrain a future
comparison law, but its trilinear multiplication defect is not the
ordering of loop placements or the coherent parenthesization of
(ST2). Nor is the squared response discrepancy in (ST9)
automatically that associator. A bridge would have to retain the
nonassociative multiplication and make it restrict the admissible
source actions or their interaction, on a specified common carrier.

[[gauge-path-fisher-response/receipts/two_sided_fisher_receipt.py|The extended receipt]] tests
the actual source-cut inverse and action, three-cut coherence,
full raw-edge derivatives for three invariant chain probes, and
the averaged \(12\times12\) Hessian and inverse derivative in
(ST8)--(ST9). The analytic arguments above, not these finite
checks, supply the likelihood and strict integrated obstruction.

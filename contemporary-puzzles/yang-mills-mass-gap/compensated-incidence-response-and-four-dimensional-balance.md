# Compensated Incidence Response and the Four-Dimensional Balance

A paired scale filtration need not acquire a floor only by deleting all joint incidences beyond a hard diagonal wall. It can retain arbitrarily deep joint shells if an independently constructed positive response form grows quickly enough to compensate their inverse-scale attenuation. The exact object is the closed pullback form \(q[f]=\|\overline{R^{1/2}M_p}f\|^2\) on the joint-active carrier: \(M_p\) says how a reciprocal distinction is presented at scale, while \(R\) says how strongly its presented image responds. For a bilateral logarithmic scale operator \(A\), the model law \(M_p=e^{-pA}\), \(R_q=e^{qA}\) has a uniform floor only at the scale-neutral balance \(q=2p\). If—and these are open geometric hypotheses—the response is a codimension-two boundary frame with exponent \(q=D-2\), the address is soldered to log length, and presentation has first inverse-length order \(p=1\), then \(D=4\) is the unique power-law-neutral spacetime dimension within this homogeneous ansatz. This is an exact conditional exponent theorem, not yet a Yang--Mills construction or a derivation of its mass scale.

**Status: [EXACT DIAGONAL COMPENSATION THEOREM]; [EXACT NONCOMMUTING PULLBACK CRITERION]; [EXACT CONDITIONAL CRITICAL-EXPONENT THEOREM]; [CANDIDATE LOG-LENGTH SOLDER, FIRST-ORDER PRESENTATION, AND CODIMENSION-TWO RESPONSE]; [OPEN YANG--MILLS RESPONSE, CASIMIR SOLDER, AND CONTINUUM LIMIT].**

## Hard and soft walls

Let the joint-active carrier of [[paired-scale-filtrations-and-the-invariant-incidence-wall]] be

$$
\mathcal H_{\leftrightarrow}
=
P_{\leftrightarrow}\mathcal H
=
\bigoplus_{\alpha\in\Sigma}Q_\alpha\mathcal H,
\qquad
\sum_{\alpha\in\Sigma}Q_\alpha=P_{\leftrightarrow},
\tag{CR1}
$$

where \(\alpha=(j,k)\), \(Q_\alpha=Q_{jk}\), and

$$
a_\alpha
:=
\overline N_{jk}
=
\frac{N_j^++N_k^-}{2}.
\tag{CR2}
$$

The self-adjoint invariant address and its order-\(p\) inverse-scale presentation are

$$
A
=
\sum_{\alpha\in\Sigma}a_\alpha Q_\alpha,
\qquad
M_p
:=
e^{-pA},
\qquad p>0,
\tag{CR3}
$$

with their maximal spectral domains. The earlier incidence theorem is the neutral-response case \(R=I\): a positive floor for \(M_p\) is exactly an upper bound on the occupied addresses. This is a **hard wall** because sufficiently deep joint shells are absent.

A different mechanism is possible. Let \(R\geq0\) be a densely defined positive self-adjoint dimensionless response operator on the presented carrier, after any physical energy coefficient has been factored out. Instead of asking whether \(M_p\) alone is bounded below, ask whether the composition

$$
C_{R,p}
:=
\overline{R^{1/2}M_p}
\tag{CR4}
$$

is bounded below, whenever the raw product is densely defined and closable. Deep incidences may remain present, but their images must be charged increasingly strongly. This is a **compensated wall** or **soft wall**. Its cost is not a metaphor: it is the closed quadratic form

$$
q_{R,p}[f]
:=
\|C_{R,p}f\|^2.
\tag{CR5}
$$

The bar in (CR4) is essential. For unbounded operators the composition, its domain, and its closure must be proved rather than inferred from formal multiplication.

## Exact diagonal compensation theorem

Assume first that \(R\) strongly commutes with every joint-shell projection. Then

$$
R
=
\bigoplus_{\alpha\in\Sigma}R_\alpha,
\qquad
R_\alpha
:=
R\restriction_{Q_\alpha\mathcal H},
\tag{CR6}
$$

and joint functional calculus gives the canonical closed operator

$$
C_{R,p}
=
\bigoplus_{\alpha\in\Sigma}
e^{-pa_\alpha}R_\alpha^{1/2}.
\tag{CR7}
$$

Finite-shell vectors whose \(\alpha\)-component lies in \(D(R_\alpha^{1/2})\) form a graph core for this direct-sum operator. Hence (CR7) is precisely the closure in (CR4), not a merely formal block product.

Its form is

$$
q_{R,p}[f]
=
\sum_{\alpha\in\Sigma}
e^{-2pa_\alpha}
\|R_\alpha^{1/2}Q_\alpha f\|^2,
\tag{CR8}
$$

on the explicit form domain

$$
D(q_{R,p})
=
\left\{
f:
Q_\alpha f\in D(R_\alpha^{1/2})\ \text{for every }\alpha,
\quad
\sum_\alpha e^{-2pa_\alpha}
\|R_\alpha^{1/2}Q_\alpha f\|^2<\infty
\right\}.
\tag{CR8a}
$$

Put

$$
\rho_\alpha
:=
\inf\sigma(R_\alpha).
\tag{CR9}
$$

For \(\kappa>0\), approximate bottom-spectrum vectors in each nonzero block prove

$$
\boxed{
q_{R,p}[f]\geq\kappa^2\|f\|^2
\text{ for every }f\in D(q_{R,p})
\quad\Longleftrightarrow\quad
\inf_{\alpha:Q_\alpha\neq0}
\rho_\alpha e^{-2pa_\alpha}
\geq\kappa^2.}
\tag{CR10}
$$

Thus the optimal squared floor is

$$
\kappa_{\mathrm{opt}}^2
=
\inf_{\alpha:Q_\alpha\neq0}
\rho_\alpha e^{-2pa_\alpha}.
\tag{CR11}
$$

When \(R\) is scalar on each shell, \(R_\alpha=r_\alpha I_\alpha\), the condition is simply

$$
r_\alpha
\geq
\kappa^2e^{2pa_\alpha}
\qquad
\text{on every occupied joint shell.}
\tag{CR12}
$$

Consequently a bounded response cannot compensate addresses unbounded above. If \(R\leq BI\), then spectral vectors with \(a_\alpha\to+\infty\) make the coefficient in (CR8) tend to zero. The response must grow along every escaping occupied sequence, not merely on average.

If \(R\) is injective and dimensionless, define the compensated address by joint functional calculus,

$$
A_{\mathrm{comp}}
:=
pA-\frac12\log R.
\tag{CR13}
$$

This is the joint spectral function \((a,r)\mapsto pa-\tfrac12\log r\), not an unqualified difference of unbounded operators. Then

$$
C_{R,p}=e^{-A_{\mathrm{comp}}},
\qquad
q_{R,p}\geq\kappa^2I
\quad\Longleftrightarrow\quad
A_{\mathrm{comp}}\leq-\log\kappa\,I.
\tag{CR14}
$$

Here and below, inequalities involving \(q_{R,p}\) are closed quadratic-form inequalities.

For a general strongly commuting pair with joint spectral measure \(E(da,dr)\), the exact support statement is

$$
E\!\left(
\{(a,r):re^{-2pa}<\kappa^2\}
\right)=0.
\tag{CR15}
$$

The hard incidence wall is the special case \(R=I\). Equation (CR15) then reduces to the absence of spectral support above \(a=-p^{-1}\log\kappa\). A compensated wall does not erase that support; it bends the allowed joint support in the enlarged \((a,r)\)-plane.

## The safe noncommuting statement

Strong shell commutation is convenient, not automatic. Without it, neither \(M_pRM_p\) nor \(pA-\tfrac12\log R\) should be written as though all products were defined and self-adjoint.

Let

$$
\mathfrak r[g]
:=
\|R^{1/2}g\|^2
\tag{CR16}
$$

be the closed response form and define

$$
C_0
:=
R^{1/2}M_p,
\qquad
D(C_0)
=
\{f\in D(M_p):M_pf\in D(R^{1/2})\}.
\tag{CR17}
$$

Require this domain to be dense and \(C_0\) to be closable, including the special case in which it is already closed, and put \(C=\overline{C_0}\). The exact criterion is then

$$
\boxed{
\|Cf\|\geq\kappa\|f\|
\quad(f\in D(C))
\quad\Longleftrightarrow\quad
C^*C\geq\kappa^2I.}
\tag{CR18}
$$

On the presented variable \(g=M_pf\), the same statement is

$$
\boxed{
\mathfrak r[g]
\geq
\kappa^2\|M_p^{-1}g\|^2,
\qquad
g\in\operatorname{Ran}M_p\cap D(R^{1/2}).}
\tag{CR19}
$$

Analytically, the floor says that \(C\) is injective with closed range and that its inverse on that range is bounded by \(\kappa^{-1}\). This is the noncommutative content of “the response compensates inverse-scale attenuation.” It is a closed-range theorem, not a statement that the two factors have separate gaps.

No response can repair an exact missing-input kernel. If \(M_p\) is extended by zero outside \(P_{\leftrightarrow}\mathcal H\), then \(C f=0\) on every terminal or one-sided sector. A full vacuum-complement floor still requires

$$
P_{\leftrightarrow}=1-P_0.
\tag{CR20}
$$

### The floor is quantitative distinction

Extend \(C\) by zero on the vacuum line and suppose \(\ker C=P_0\mathcal H\). Then the floor can be written

$$
\boxed{
\|Cf\|
\geq
\kappa\,\operatorname{dist}(f,P_0\mathcal H)
=
\kappa\|(1-P_0)f\|
\qquad(f\in D(C)).}
\tag{CR20a}
$$

Equivalently, the induced map

$$
\widetilde C:
D(C)/P_0\mathcal H
\longrightarrow
\operatorname{Ran}C
\tag{CR20b}
$$

has closed image and an inverse bounded from \(\operatorname{Ran}C\) into the Hilbert quotient \(\mathcal H/P_0\mathcal H\). If \(C\) is bounded, it extends to a topological embedding of the full Hilbert quotient. There is then no sequence of normalized nonvacuum distinctions in the form domain whose response converges to the null response. This is an exact sense in which a gap is **quantitative distinction**: “not vacuum” remains uniformly separated from “vacuum” after the declared presentation and response.

The resemblance to measurement is real but limited. A measurement channel may quotient distinct incoming states into one readout class, and a discrete context may label alternatives. Neither fact proves (CR20a), and (CR20a) does not choose one alternative or write a record. The mass problem asks for uniform separation on the full physical vacuum quotient; the outcome problem asks which contextual possibility becomes factual. They can share a carrier and a wall architecture without being the same operator or theorem.

## What the operator operates on

The composition has a strict type order:

$$
\boxed{
f
\xmapsto{\ M_p\ }
g=M_pf
\xmapsto{\ R^{1/2}\ }
\text{response amplitudes},
\qquad
q_{R,p}[f]=\mathfrak r[M_pf].}
\tag{CR21}
$$

- \(f\) is a centered, gauge-reduced state-vector or tangent direction on the declared common carrier.
- \(M_p\) operates on its reciprocal joint-shell components and assigns their invariant scale attenuation. It is not the Hamiltonian and does not act on bare spacetime points.
- \(R^{1/2}\) operates on the presented image \(g\). Depending on the realization, it may analyze boundary flux, regional state change, a Dirichlet gradient, or another response channel.
- \(C^*C\), when defined through the closed form, is the pullback cost on the original distinction. It is the first object in this chain that can possess the compensated floor.

The conceptual nouns therefore retain different mathematical types:

| Concept | Role in this construction | Not identified with |
|---|---|---|
| space | the scale order and joint incidence relation among distinguishable components | a container through which vectors move, or a lattice pixel |
| causality | the directed pairing and compatibility law between reciprocal filtrations | the reversible clock parameter |
| entropy | a functional of a declared state/channel whose Hessian may contribute to \(R\) | energy, actuality, or a gap |
| energy | the dimensionful positive form associated with reconstructed clock translations | the dimensionless address or response by itself |
| mass | the lower edge of the joint Poincare Casimir after the same-carrier solder | either causal generator, boundary area, or a number obtained by unit conversion |

A useful frame realization makes the distinction between boundary size and boundary stiffness exact. On a joint shell, let \(J_\alpha\) be a closed densely defined analysis map with

$$
J_\alpha:
Q_\alpha\mathcal H
\longrightarrow
\bigoplus_{\ell\in I_\alpha}\mathcal Y_{\alpha\ell},
\qquad
R_\alpha=J_\alpha^*J_\alpha.
\tag{CR22}
$$

Then \(\rho_\alpha\) is the lower frame bound of the boundary or flux readout on that shell. Merely having \(|I_\alpha|\) channels, or an entropy proportional to their count, does not imply \(\rho_\alpha>0\): all channels may share a blind direction. The required statement is

$$
\|J_\alpha v\|^2
\geq
\rho_\alpha\|v\|^2
\qquad
(v\in D(J_\alpha)),
\tag{CR23}
$$

uniformly over the regulator and all occupied shells.

## Exact critical-exponent theorem

The simplest homogeneous response family is

$$
R_{q,r_0}
:=
r_0e^{qA},
\qquad
r_0>0,
\quad q\in\mathbb R.
\tag{CR24}
$$

Joint functional calculus gives

$$
C_{p,q}
:=
\overline{R_{q,r_0}^{1/2}M_p}
=
\sqrt{r_0}\,e^{(q/2-p)A},
\qquad
C_{p,q}^*C_{p,q}
=
r_0e^{(q-2p)A}.
\tag{CR25}
$$

Assume that the spectral support of \(A\) is unbounded both above and below. If \(q-2p>0\), vectors at \(A\to-\infty\) make the form coefficient tend to zero. If \(q-2p<0\), vectors at \(A\to+\infty\) do so. Therefore

$$
\boxed{
\inf\sigma(C_{p,q}^*C_{p,q})>0
\quad\Longleftrightarrow\quad
q=2p,}
\tag{CR26}
$$

and at the balanced exponent

$$
C_{p,2p}^*C_{p,2p}=r_0I.
\tag{CR27}
$$

Equivalently, under a scale translation \(A\mapsto A+sI\), the squared response transforms by the character \(e^{(q-2p)s}\). It is scale-neutral precisely when \(q=2p\). This is a **common translation of invariant mean scale** and should be interpreted as address or theory-family covariance, not an exact unitary dilation symmetry inside one fixed gapped theory; [[mass-as-casimir-and-realization#A gap obstructs exact same-carrier dilation covariance|the same-carrier dilation no-go]] forbids the latter. It is also distinct from the reciprocal frame or boost shift of the two directional addresses, under which their mean \(A\) is already fixed.

The bilateral hypothesis is load-bearing and is not supplied by an ordinary semi-infinite RG tower. If \(A\) is bounded below and unbounded above, the exact homogeneous model has a floor whenever \(q\geq2p\); if \(A\) is bounded above and unbounded below, it has a floor whenever \(q\leq2p\). Equality is uniquely forced by a bilateral carrier, or by the stronger requirement that the response be scale-neutral rather than merely bounded below. A physical application must construct the relevant support and covariance rather than silently extending a one-sided filtration. Likewise, choosing \(R=e^{2pA}\) after seeing (CR26) is a tautology. Explanatory content begins only if geometry derives \(R\), its exponent, and its normalization independently of the desired floor.

### An exact categorical source of the square

The law \(R=e^{2A}\) need not be introduced only as the answer required by (CR26). [[finite-index-duality-and-the-square-response]] supplies an independent algebraic instance, but with an important normalization split. For a chosen normal faithful finite-index expectation between properly infinite von Neumann algebras, the conjugate/Q-system construction contains an intertwiner \(\widetilde v_E\) with

$$
\widetilde v_E^*\widetilde v_E
=
\operatorname{Ind}(E)
\tag{CR27a}
$$

Writing the chosen-expectation address

$$
A_E:=\frac12\log\operatorname{Ind}(E)
$$

gives

$$
\widetilde v_E^*\widetilde v_E=e^{2A_E},
\qquad
\widetilde v_Ee^{-A_E}=V_E,
\qquad
V_E^*V_E=1.
\tag{CR27b}
$$

In a factor with chosen index greater than one, \(V_E\) is a proper isometry. The number \(A_E\) generally depends on the expectation and is not automatically fusion additive. Only for the minimal expectation \(E^0\) and standard conjugate solution does

$$
\operatorname{Ind}(E^0)=d(\iota)^2,
\qquad
A_{\mathrm{cat}}:=\log d(\iota),
\tag{CR27c}
$$

where the intrinsic statistical dimension multiplies under Connes fusion and \(A_{\mathrm{cat}}\) adds. Thus standard duality supplies the response-square/additive-address grammar exactly; an arbitrary expectation supplies only an expectation-dependent normalization square.

This does not establish the hypotheses of the present theorem. For one fixed factor inclusion, both \(A_E\) and, when defined, \(A_{\mathrm{cat}}\) are scalar and bounded; the normalized identity preserves all vector norms and supplies no vacuum-selective response. A physical application must prove that a scale-indexed family of standard correspondences yields the bilateral address \(A\), that its conjugate intertwiner controls the same boundary or flux form \(R\), and that the resulting residual lower edge is regulator uniform. Without those maps, (CR27b)--(CR27c) are normalization identities rather than Yang--Mills stiffness.

## The codimension-two balance

Now declare, rather than smuggle in, the geometric hypotheses:

1. an independently proved scale-character solder identifies the abstract invariant address with \(A=\log(L/L_0)\) on a bilateral scale carrier;
2. the presentation map has independently fixed first inverse-length order, \(M_1=e^{-A}=L_0/L\);
3. a transverse spatial cut of a codimension-one causal boundary in \(D\) spacetime dimensions has dimension \(D-2\); and
4. in the scale-diagonal branch, an independently normalized boundary-frame theorem factors its response into the engineering boundary character and a dimensionless residual,

   $$
   R_{\partial,D}
   =
   r_0e^{(D-2)A}Z_D(A),
   \qquad
   Z_D(a)>0\quad E_A\text{-almost everywhere}.
   \tag{CR28}
   $$

The exactly homogeneous or two-sided-comparable ansatz additionally requires scale- and regulator-independent constants \(0<c_-\leq c_+<\infty\) such that \(c_-I\leq Z_D(A)\leq c_+I\), with common form domains. That extra bound is not part of the bare factorization. Accordingly, if this comparison is abbreviated as \(R_{\partial,D}\asymp r_0e^{(D-2)A}\), the symbol \(\asymp\) must mean a global, regulator-uniform, two-sided quadratic-form comparison on that common domain across both spectral tails. Ordinary large-\(L\) asymptotics or a one-sided lower bound is insufficient for the necessity direction in (CR30).

The first two clauses are not changes of notation. An address may instead log an operator parameter of differential order \(d\), which rescales \(p\) and changes the apparent dimensional balance. [[resolvent-logistic-scale-transform]] and [[wall-construction-interface/scale-character-solder]] isolate this normalization problem. The value \(p=1\) is therefore as load-bearing as the codimension exponent.

There is also a codimension firewall. The reflection-fixed separator in [[vacuum-boundary-gluing-and-wall-response]] is a codimension-one Euclidean interface. It does not automatically furnish the codimension-two transverse cut used in (CR28). A Lorentzian causal-boundary reconstruction, a further cut, and a carrier map between their response forms are additional obligations.

Under the scale-diagonal factorization the pulled-back squared response is

$$
C_{\partial,D,1}^*C_{\partial,D,1}
=
r_0e^{(D-4)A}Z_D(A).
\tag{CR29}
$$

At the level of the explicit power character, the critical balance is exactly

$$
\boxed{
D-4=0
\quad\Longleftrightarrow\quad
D=4.}
\tag{CR30}
$$

In words: a codimension-two response contributes the area character, while a first-order inverse-scale amplitude contributes its square. Only in four spacetime dimensions do these **power characters** cancel without another power-law factor. If \(A\) has bilateral support and \(Z_D(A)\) obeys the uniform two-sided bounds above, the actual response floor exists exactly at \(D=4\). Without those residual bounds, (CR30) asserts engineering neutrality only.

Power cancellation is only engineering marginality. In \(D=4\), (CR29) becomes

$$
C_{\partial,4,1}^*C_{\partial,4,1}
=
r_0Z_4(A),
\qquad
\boxed{
\inf\sigma(C_{\partial,4,1}^*C_{\partial,4,1})>0
\Longleftrightarrow
\operatorname*{ess\,inf}_{E_A}Z_4>0.}
\tag{CR30a}
$$

Here \(Z_4\) may contain quantum running or anomalous response after the power character has been removed. Thus four-dimensionality cancels the power drift but does not supply the uniform size of the residual response. Dimensional transmutation can furnish an independent energy yardstick; the uniform multiscale dynamical theorem must still prove that \(Z_4\) does not decay to zero on any physical scale channel.

If the running response does not reduce the address spectral measure, the function \(Z_D(A)\) is unavailable and the correct target remains the noncommuting pullback inequality (CR19).

This is closely related to the ordinary statement that Yang--Mills coupling is dimensionless in four spacetime dimensions. It may be a geometric re-expression of that power counting rather than an independent explanation of it. In \(D\neq4\), a dimensionful coupling can contribute the missing scale character. Therefore (CR30) does **not** prove that nature must be four-dimensional, that codimension-two boundaries exist pre-geometrically, or that four-dimensional Yang--Mills is gapped. It isolates two sharper construction targets:

$$
\boxed{
\text{derive a gauge-invariant boundary/flux lower frame}
\quad
R_{\partial,4}\gtrsim e^{2A}
\quad
\text{for four-dimensional sufficiency},}
\tag{CR31}
$$

and, for a claim that the geometry selects four dimensions **among independently constructed \(D\)-dimensional candidates**, derive the exponent factorization (CR28), bilateral scale support, and bounds showing that \(Z_D\) does not hide a compensating power character. Neither target may import the Yang--Mills action's known power counting.

In (CR31), \(\gtrsim\) denotes a regulator-uniform lower quadratic-form bound on a declared common domain. That one-sided estimate is a sufficiency target after fixing \(D=4\); it cannot by itself select \(D=4\) among dimensions.

The integer \(D-2\) must arise from the incidence or boundary geometry itself. The exponent \(p\) must arise from the order of the presentation map. Their equality is then a theorem about compatible scale characters rather than an equation of units mistaken for an equation of concepts. The positive lower bound for \(Z_4\) is a further dynamical theorem, not another dimensional identity.

## Where entropy, flux, and RG can enter

Entropy is relevant at the response arrow, but an entropy value is not the response operator. An area law can motivate an extensive boundary capacity or multiplicity. Distinguishability is instead state-pair- and tangent-dependent; the needed object is its second variation or analysis-frame operator on the same tangent directions:

$$
R_{\mathrm{ent}}
=
J^*G_{\mathrm{BKM}}J,
\tag{CR32}
$$

with a lower bound of the form (CR23). [[regional-relative-entropy-frames]] gives this pullback type and shows why local channels can share blind directions. [[horizon-saturation-and-entropic-distinction]] explains why relative-entropy positivity, maximal entropy, or a first-law identity does not provide the required Hessian floor. Leading area contributions can also cancel from relative entropy, as [[spectral-wall-descent/finite-index-area-weld#Relation to gravity and to lost response|the area-term no-go]] makes explicit, so their \(D-2\) scaling need not survive in \(R_{\mathrm{ent}}\). A black-hole area coefficient also imports \(G\), so it cannot set the scale of the gravity-free Clay problem.

The finite-regulator electric-flux Dirichlet form in [[gauge-descent-flux-fisher-coercivity]] is a more direct physical cost. The exact target is not separate shell estimates unless the form reduces the shell projections, but the joint inequality

$$
\mathfrak R_r[M_{p,r}f]
\geq
\kappa^2\|f\|^2.
\tag{CR33}
$$

When reduction is proved, this becomes the regulator-uniform coefficient condition

$$
\inf_{r,\alpha}
\rho_{r,\alpha}e^{-2pa_{r,\alpha}}>0.
\tag{CR34}
$$

The most plausible source of the scale dependence in \(\rho_{r,\alpha}\) is the two-scale machinery of [[two-scale-rg-descent-and-the-crossover-lemma]]: conditional fiber coercivity, coarse coercivity, and a controlled mixed Hessian must survive every blocking step. Established results prove that such compensation is mathematically possible without making randomness fundamental. [[library/a-note-on-spectral-gap-and-weighted-poincare-inequalities-for-some-one-dimensional-diffusions/inq|Weighted Poincare inequalities]] include diffusions whose ordinary form is gapless while a position-dependent response weight restores a spectral gap. [[library/a-two-scale-approach-to-logarithmic-sobolev-inequalities/inq|The two-scale logarithmic-Sobolev theorem]] and [[library/poincare-and-transportation-inequalities-for-gibbs-measures-under-the-dobrushin-uniqueness-condition/inq|the Dobrushin Poincare theorem]] give exact local-to-global assembly mechanisms under their stated hypotheses. [[library/spectral-gap-critical-exponent-for-glauber-dynamics-of-hierarchical-spin-models/inq|The Bauerschmidt--Bodineau recursion]] transports inverse-gap forms across hierarchical covariance slices while its critical examples show that multiscale decomposition itself need not create a floor. [[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Strong-coupling lattice Yang--Mills]] supplies a genuine gauge-theory endpoint precedent.

None of those results proves (CR34) along the asymptotically free four-dimensional continuum trajectory. Their stochastic generators organize functional inequalities on declared Euclidean carriers; they are not ontological dice and are not automatically the Lorentzian clock Hamiltonian.

## From a dimensionless floor to mass

The compensated form is still dimensionless. After a positive-energy Poincare representation has been reconstructed, let

$$
\mathcal C
=
H^2-c^2|\mathbf P|^2
\tag{CR35}
$$

be the energy-squared presentation of the physical Poincare mass Casimir; the spectrum condition makes it nonnegative. [[joint-causal-generators-and-the-mass-casimir#Casimir solder to a distinction frame|The canonical Casimir-solder note]] owns this downstream comparison. A direct same-carrier solder would have to prove

$$
\|\mathcal C^{1/2}f\|^2
\geq
\eta E_*^2q_{R,p}[f]
\qquad
(f\in D(\mathcal C^{1/2})),
\tag{CR36}
$$

where \(E_*\) is independently normalized and \(D(\mathcal C^{1/2})\subseteq D(q_{R,p})\). Equations (CR10) and (CR36) would give

$$
\mathcal C
\geq
\eta E_*^2\kappa^2(1-P_0),
\qquad
\Delta_E
\geq
E_*\sqrt\eta\,\kappa.
\tag{CR37}
$$

The separate coefficients are normalization-dependent. Rescaling \(R\mapsto aR\) sends \(q_{R,p}\mapsto aq_{R,p}\) and \(\kappa^2\mapsto a\kappa^2\), while the same physical solder is registered by \(\eta\mapsto\eta/a\). Only \(\eta\kappa^2\), and hence \(E_*\sqrt\eta\,\kappa\), is invariant. The normalization of \(R\) must therefore be frozen upstream if its factors are to have explanatory meaning.

Alternatively, after positive-energy Poincare reconstruction, prove the analogue of (CR36) for one fixed physical null pair on the entire vacuum complement. The fixed-direction theorem in the paired-filtration note then gives the Hamiltonian gap and the full Casimir floor. A countable dense all-direction family remains an exact direct-tomography alternative. One oriented pair is insufficient only when it is abstract, sector-restricted, differently carried, or not identified with the physical null translations.

Neither \(c\) nor \(\hbar\) supplies \(E_*\): they convert space to time and inverse time to energy. In pure Yang--Mills the honest current yardstick is a declared scheme-dependent dimensional-transmutation scale, with the dimensionless coefficient transforming oppositely under a scheme change. Importing \(G\), a Hawking temperature, a glueball mass, or the numerical causal-grain coincidence would forfeit the claimed derivation unless a separate decoupling and transport theorem is proved.

## Stopping and kill conditions

This route has crossed from analogy to a physical theorem only when:

1. the paired filtrations, common carrier, shell addresses, and terminal vacuum are constructed from frozen gauge/RG data without using the target spectrum;
2. the response form is independently derived from gauge flux, boundary gluing, an entropy Hessian, or another declared geometry, with its normalization and domains fixed upstream;
3. the composition \(R^{1/2}M_p\) is proved closable and its closure satisfies a regulator-, volume-, shell-, and direction-uniform lower bound;
4. any codimension-two exponent is proved as a lower-frame scaling law, not inferred from area, multiplicity, or the already-known engineering dimension of the Yang--Mills coupling; a claim of unique dimensional selection additionally proves the matching upper scaling and bilateral support;
5. the response survives infinite-volume and continuum removal on identified carriers with convergent vacuum projections;
6. Poincare covariance, the spectrum condition, locality, gauge-invariant observables, and nontrivial Yang--Mills short-distance behavior are reconstructed; and
7. a same-carrier fixed-null-pair, all-direction, or direct-Casimir solder supplies the physical energy scale.

The route is killed if \(R=e^{2pA}\) or its shell coefficients are chosen solely to force (CR10); if boundary channel count is substituted for the lower frame bound (CR23); if entropy positivity or an entropy maximum is called stiffness; if form cross-terms are discarded without a reduction theorem; if the response leaves a nonvacuum terminal kernel; if the \(D=4\) exponent is imported from the Yang--Mills action and reported as independently derived; or if the dimensionless floor is converted into MeV before (CR36) and an independent \(E_*\) exist.

## Claim ledger

| Status | Claim |
|---|---|
| Exact | for a shell-reducing positive response, the compensated form has a floor exactly when \(\inf_\alpha\rho_\alpha e^{-2pa_\alpha}>0\) |
| Exact | without commutation, the well-typed statement is the closed-range inequality for \(\overline{R^{1/2}M_p}\), equivalently the pullback response bound (CR19) |
| Exact | a response cannot repair an exact terminal or one-sided kernel of the presentation map |
| Exact conditional theorem | on a bilateral scale carrier, the homogeneous response \(e^{qA}\) compensates \(e^{-pA}\) uniformly iff \(q=2p\) |
| Conditional geometric consequence | if a codimension-two boundary supplies the homogeneous response character \(D-2\) and presentation has inverse-length order one, power neutrality selects \(D=4\); an actual floor still requires a positive residual lower edge |
| Established precedent | weighted Poincare, two-scale LSI, Dobrushin, and strong-coupling lattice results show concrete response-weight and local-to-global gap mechanisms on their declared carriers |
| Open | derive the boundary/flux response, its lower frame and normalization, the bilateral fixed-pair/all-direction/direct-Casimir realization, the continuum estimate, and the Poincare-Casimir solder from four-dimensional Yang--Mills geometry |

[[contemporary-puzzles/yang-mills-mass-gap/receipts/compensated_incidence_response_receipt.py|The finite receipt]] illustrates exact diagonal compensation on one finite two-sided window, decreasing sampled floors for the fixed bounded response \(R=7I\), the arithmetic obtained after assuming \(q=D-2,p=1\) for \(D=3,4,5\), and persistence of one selected terminal kernel; [[contemporary-puzzles/yang-mills-mass-gap/receipts/compensated-incidence-response-receipt-output.txt|its stored output]] records the passing run. It does not establish unbounded spectral support, the exponent hypotheses, uniqueness of \(D=4\), any infinite-dimensional theorem, or any open physical arrow.

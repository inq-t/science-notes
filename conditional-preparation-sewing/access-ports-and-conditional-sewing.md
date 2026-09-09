# Access Ports and Conditional Sewing

A new access can enlarge a Gaussian preparation while preserving every old prior readout. Several such extensions compose coherently when they are conditionals of one joint covariance; this law commutes with pure subdivisions that preserve the same accessible vertices and multiplication words. A stronger demand has an exact obstruction: adding a positive comparison generally changes the old marked posterior. The distinction gives a concrete sewing rule and identifies which response an attachment may legitimately change.

**Status: exact finite Gaussian identities and presentation statements.** Covariance selection, the physical comparison and its time limit are additional data. [[conditional-preparation-sewing/conditional-preparation-extension-at-new-access|The conditional access construction]] supplies the actual pair of multiplication words; [[general-causal-action/preparation-transport-through-spatial-subdivision|Preparation transport]] supplies the preceding physical-loop obstruction.

## One extension preserves the complete old prior

Let \(E,F\) be finite complex Hilbert spaces, with normalized Lebesgue reference measures \(d_E x=\prod_a d^2x_a/\pi\), and choose
\[
x\sim\operatorname{CN}(0,\Gamma),\qquad
\varepsilon\sim\operatorname{CN}(0,\Delta),\qquad
y=Mx+\varepsilon,
\qquad \Gamma>0,\quad\Delta>0.
\tag{AP1}
\]
The two preparations on the right are independent. The joint covariance and its determinant are
\[
\mathsf G=
\begin{pmatrix}
\Gamma&\Gamma M^\dagger\\
M\Gamma&M\Gamma M^\dagger+\Delta
\end{pmatrix}>0,
\qquad
\det\mathsf G=\det\Gamma\det\Delta.
\tag{AP2}
\]
The triangular map \((x,\varepsilon)\mapsto(x,y)\) has complex determinant one. Thus (AP2) is an equality of the complete normalized densities, including their reference measures. Conversely, every faithful centered joint Gaussian whose old marginal is \(\Gamma\) has the unique form (AP1), with
\[
M=\mathsf G_{yx}\Gamma^{-1},\qquad
\Delta=\mathsf G_{yy}-\mathsf G_{yx}\Gamma^{-1}\mathsf G_{xy}>0.
\tag{AP3}
\]
Completing the square gives (AP3); the residual \(y-Mx\) is Gaussian and uncorrelated with \(x\), hence independent.

For every old linear source \(j\) and Hermitian quadratic source \(T\) with \(\Gamma^{-1}+T>0\), integration over the new conditional variable gives
\[
\boxed{
\mathbb E_{\mathsf G}e^{2\Re(j^\dagger x)-x^\dagger Tx}
=\frac{\exp[j^\dagger(\Gamma^{-1}+T)^{-1}j]}
{\det\Gamma\det(\Gamma^{-1}+T)}.}
\tag{AP4}
\]
This preserves the entire old prior experiment, not only its covariance or norm. A source-free weight depending only on \(x\) can be inserted on both sides. A weight involving the new variable is a different assertion, tested below. The fixed-reference unnormalized versions and hidden-source factors are owned by [[general-causal-action/marked-gaussian-constraints-and-sewing-measures|marked Gaussian sewing measures]].

## The joint law, rather than an order of additions, carries the correlations

For two new accesses write
\[
y_i=M_i x+\varepsilon_i,
\qquad
\begin{pmatrix}\varepsilon_1\\\varepsilon_2\end{pmatrix}
\sim\operatorname{CN}\!\left(0,
\mathsf C=\begin{pmatrix}C_1&R\\R^\dagger&C_2\end{pmatrix}\right),
\qquad\mathsf C>0,
\tag{AP5}
\]
independently of \(x\). Adding access 1 first and then access 2 means
\[
\begin{aligned}
\varepsilon_1&\sim\operatorname{CN}(0,C_1),\\
\varepsilon_2&=R^\dagger C_1^{-1}\varepsilon_1+\zeta_2,
&\zeta_2&\sim\operatorname{CN}(0,C_2-R^\dagger C_1^{-1}R).
\end{aligned}
\tag{AP6}
\]
The displayed innovations are independent. Reversing the order uses
\[
\varepsilon_2\sim\operatorname{CN}(0,C_2),\qquad
\varepsilon_1=RC_2^{-1}\varepsilon_2+\zeta_1,
\qquad
\zeta_1\sim\operatorname{CN}(0,C_1-RC_2^{-1}R^\dagger).
\tag{AP7}
\]
Both Schur complements are positive. The conditional means in (AP6)–(AP7) are essential: a fresh independent residual at the second step would set \(R=0\).

**Conditional sewing theorem.** The two orders give the same joint preparation, every mixed linear and quadratic source amplitude, and every integrable subsequent comparison of its declared readouts. In particular their normalization factors agree:
\[
\boxed{
\det\mathsf C
=\det C_1\det(C_2-R^\dagger C_1^{-1}R)
=\det C_2\det(C_1-RC_2^{-1}R^\dagger).}
\tag{AP8}
\]
To prove the claim, complete the square in the joint positive Gaussian density in either block order. The triangular changes have determinant one; (AP8) accounts for all scalar factors. Arbitrary sources or readout weights are the same function of \((x,y_1,y_2)\) before this change of integration coordinates. Absolute integrability permits either order of integration. Repeating this argument proves the statement for any finite number of accesses and parenthesizations, provided the conditionals come from one common faithful covariance.

This is a coherence condition on supplied joint data, not a rule selecting those data. For example, take scalar complex variables, \(\Gamma=1\), \(M_1=M_2=1\), \(C_1=C_2=1\), and real \(-1<R<1\). Every value gives the same two old/new marginals, while
\[
\mathbb E[y_1\overline{y_2}]=1+R,
\qquad
\operatorname{Cov}(|y_1|^2,|y_2|^2)=|1+R|^2.
\tag{AP9}
\]
The last identity follows by complex Gaussian pairings, or by taking two derivatives of the marked determinant. The choices \(R=0\) and \(R=1/2\) therefore preserve each old/new experiment but disagree on a joint source. Pairwise old readout preservation cannot determine multi-access sewing.

## Gauge covariance constrains where a fixed correlation may live

Suppose preparations at two different ports carry unitary actions \(D_p,D_q\), with independently variable vertex gauges. A configuration-independent cross covariance \(C=\mathbb E[x y^\dagger]\) of an invariant joint preparation must obey
\[
D_p(h_p)C D_q(h_q)^\dagger=C
\quad\text{for all }h_p,h_q.
\qquad
\boxed{C=P_p^{\rm inv}C P_q^{\rm inv}.}
\tag{AP9a}
\]
Here \(P_p^{\rm inv},P_q^{\rm inv}\) are Haar averages of the two representations, hence orthogonal projections onto their invariant vectors. Integrating the independent gauge actions proves the boxed identity; conversely that identity makes the covariance invariant. In particular \(C=0\) if either port representation has no invariant vector. Rectangular preparations carrying a nontrivial irreducible \(\rho\) on the left satisfy this hypothesis, however many columns they have.

At the same terminal port only the diagonal action is imposed. A scalar covariance between two copies then obeys the required intertwining automatically. Thus the common terminal port in (AP12) is part of what permits the nonzero fixed correlation in the conditional access construction. Across independently gauged ports a correlation can instead use an actual transported map \(M(q)\), with
\[
M(h\cdot q)=D_q(h_q)M(q)D_p(h_p)^\dagger.
\tag{AP9b}
\]
Its joint Gaussian then depends on the retained configuration, and all comparisons, sources and normalization factors must use that dependence. Such a connection-dependent preparation is allowed by (AP1); it is extra multiplication data rather than an invariant fixed cross block on two unrelated ports.

## A pure subdivision must preserve the same access ports

Call a vertex an access port when its incident multiplication words, possible attachments or retained stage readouts are part of the current experiment. A pure presentation change may insert or remove only an unaccessed bivalent stage; it preserves the words between the access ports and transports every retained source. This definition is about the marked experiment. It does not by itself declare a gauge at the port fixed.

Here is a precise sufficient square. Fix one access-resolved graph, its joint preparation \(z=(x,\varepsilon_1,\ldots,\varepsilon_b)\) with covariance \(G_z\), and its actual readout maps \(B(q)\), linear in \(z\). On any pure subdivision with product map \(\pi\), use
\[
B_f(\mathbf U)z=B(\pi\mathbf U)z,
\qquad
j_{\rm eff}=B_f(\mathbf U)^\dagger j,
\qquad
T_{\rm eff}=B_f(\mathbf U)^\dagger TB_f(\mathbf U).
\tag{AP10}
\]
Successive stage readouts may be stacked as in the preparation-transport theorem. Deterministic stage constraints use its normalized complex deltas, with no fresh Gaussian covariance or extra clock norm. The source amplitude is
\[
\mathcal Z(j,T;q)
=\frac{\exp[j_{\rm eff}^\dagger
(G_z^{-1}+T_{\rm eff})^{-1}j_{\rm eff}]}
{\det G_z\det(G_z^{-1}+T_{\rm eff})},
\tag{AP11}
\]
when the precision is positive. Actual temporal comparisons add their precision before applying (AP11).

Extending the preparation using (AP5) and then subdividing, or subdividing and then performing those same conditional extensions, gives identical maps on the same random variables. Equations (AP8), (AP10) and the identity fiber integrals prove equality of all marked amplitudes, including raw scalars. Normalized Haar integration over the new redundant vertex fibers then proves the physical operator equivalence in the preparation-transport owner. Arbitrary new marks must follow (AP10); keeping their old coordinate labels without transport is not the same test. Covariance and its gauge transformation law must likewise be carried with the readouts.

For the concrete access graph, put
\[
A=U_1U_2,
\qquad L=U_1W^{-1},
\qquad B=LA=U_1W^{-1}U_1U_2.
\tag{AP12}
\]
Both \(A\) and \(B\) are paths from \(v_0\) to \(v_2\), and their rectangular preparations can occupy that same terminal port. Subdividing any of the three edges \(U_1,U_2,W\) into factors preserves these products exactly. Equations (AP10)–(AP11) therefore apply to the conditional access construction's actual rows \(\rho(A)x\) and \(\rho(B)y\).

But erasing the vertex between \(U_1\) and \(U_2\) before declaring the attachment \(W\) changes the access data. The product \(A\) alone does not determine \(L\) or \(B\), even when \(W\) is retained. The loop-character proof in (PT14)–(PT18) exhibits a fully gauge-invariant function that the old product transfer annihilates. Thus the two purported orders are not a presentation square on the same resolved experiment. This is why conditional covariance coherence cannot alone repair that operator.

## A positive added comparison changes the old marked posterior

Fix a pair of configurations. Let the old preparation precision after its own comparison be \(Q_0=\Gamma^{-1}+B_0>0\), where \(B_0\ge0\). Keep the independent innovation \(\varepsilon\) from (AP1), and add the nonnegative comparison
\[
\|D x+E\varepsilon\|^2.
\tag{AP13}
\]
The operators \(D,E\) include the comparison strength and the actual representation differences at this pair. Integrating the innovation first gives
\[
\begin{aligned}
\mathbb E_{\varepsilon}
 e^{-\|Dx+E\varepsilon\|^2}
&=c_E e^{-x^\dagger Sx},\\
c_E&=\det(I+E\Delta E^\dagger)^{-1}>0,\\
S&=D^\dagger(I+E\Delta E^\dagger)^{-1}D\ge0.
\end{aligned}
\tag{AP14}
\]
Completing the square in \(\varepsilon\), followed by the identity
\(I-E(\Delta^{-1}+E^\dagger E)^{-1}E^\dagger=(I+E\Delta E^\dagger)^{-1}\), proves (AP14). Hence, for marks retaining positive precision, the full old marked amplitude becomes
\[
\mathcal K(j,T)
=\frac{c_E\exp[j^\dagger(Q_0+S+T)^{-1}j]}
{\det\Gamma\det(Q_0+S+T)}.
\tag{AP15}
\]

**Marked-posterior obstruction.** At this fixed configuration pair, (AP15) equals the original marked amplitude times a scalar independent of all old \(j,T\) if and only if \(D=0\). Indeed equality for all linear sources at \(T=0\) forces \((Q_0+S)^{-1}=Q_0^{-1}\), hence \(S=0\). The middle matrix in (AP14) is strictly positive, so \(S=0\) exactly when \(D=0\). The converse follows directly, with scalar \(c_E\).

For a new comparison \(\|N y\|^2\), (AP1) gives \(D=NM\), \(E=N\). A genuine correlated old contribution therefore generally changes the old posterior even though (AP4) preserves the prior exactly. A comparison of the residual \(y-Mx\) has \(D=0\) and passes the fixed-pair test, but its ability to distinguish the new physical word is a separate requirement. The scalar \(c_E\) can still depend on configurations, so even this test alone does not preserve an old configuration marginal or its clock.

The obstruction is deliberately pointwise and concerns adding one positive quadratic row with its original Gaussian measure. It does not exclude a conditionally normalized new transition, a transported configuration integration, or a new dynamical law with a stated coarse memory. Those alternatives change the relevant experiment and must carry their scalar factors explicitly.

## Old prior preservation does not promise an autonomous old clock

There is an independent exact test of the dynamical requirement. For a faithful real Gaussian \(N(0,\Sigma)\), constant symmetric positive mobility \(K\), and nonnegative reversible generator
\[
\mathcal L=-K:\nabla^2+(K\Sigma^{-1}z)\cdot\nabla,
\tag{AP16}
\]
let \(P\) be a surjective linear readout, with covariance \(\Sigma_c=P\Sigma P^T\). An old generator of this form with mobility \(K_c\) intertwines the full semigroup under \(Jf=f\circ P\) exactly when
\[
\boxed{
PKP^T=K_c,
\qquad
PK\Sigma^{-1}=K_c\Sigma_c^{-1}P.}
\tag{AP17}
\]
Necessity follows by applying the generator to all linear and quadratic old tests. For sufficiency, the first condition fixes the projected noise covariance, and the second closes its drift on \(Pz\). The explicit linear stochastic evolution then projects to the stated old Gaussian evolution for every initial point, hence intertwines the complete semigroups. [[rg-covariance-residue/gaussian-readout-naturality|Gaussian readout naturality]] owns the stronger selection theorem requiring this for every linear readout.

A conditional preparation extension fixes \(\Sigma_c\), but need satisfy neither equation for the mobility returned by a new physical comparison. Thus preserving the old preparation is a meaningful exact condition that allows a genuine new attachment to alter dynamics. Pure subdivision preserves the old whole experiment; new access preserves specified readouts while introducing a new joint response. Determining that response from multiplication, and controlling it on growing gauge diagrams, remains the construction problem.

## Sequential conditional normalization needs a declared retained access

The order theorem (AP8) applies to one joint law with the same subsequent weight. It does not make two different conditional-normalization prescriptions equal. A concrete counterexample uses \(G=SU(2)\), its defining representation, and \(x,y\in\mathbb C^{2\times k}\), with \(m=2k\ge4\). Give the pair the exchangeable centered Gaussian covariance
\(\sigma^2\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)\otimes I_m\),
where \(\sigma>0\) and \(0<\rho<1\). Both preparations occupy the same terminal port. Let \(S=\|x\|^2\), \(T=\|y\|^2\), and define
\[
\begin{aligned}
q_{\alpha,S}(A,A')&=e^{-\alpha S[2-\operatorname{Tr}(A^{-1}A')]},\\
z_\alpha(s)&=\int_Gq_{\alpha,s}(e,g)\,dg,
&\overline z_\alpha&=\mathbb E z_\alpha(S),\\
b_\alpha(s)&=\mathbb E[z_\alpha(T)\mid S=s],\\
F_{1\to2}^{M}
&=\mathbb E\!\left[
\frac{M(x,y)q_{\alpha,S}(A,A')q_{\alpha,T}(B,B')}
{\overline z_\alpha b_\alpha(S)}\right],\\
F_{2\to1}^{M}
&=\mathbb E\!\left[
\frac{M(x,y)q_{\alpha,S}(A,A')q_{\alpha,T}(B,B')}
{\overline z_\alpha b_\alpha(T)}\right].
\end{aligned}
\tag{AP18}
\]
Here \(\alpha>0\) is fixed, and the marks are required to be integrable. The first prescription retains access 1 and extends access 2 by [[conditional-preparation-sewing/conditional-normalization-and-marked-access|conditional normalization]]. The reverse prescription retains access 2. Exchangeability makes their scalar \(\overline z_\alpha\) and conditional function \(b_\alpha\) identical; it does not identify their pointwise denominators.

Both unmarked operators are positive self-adjoint Markov contractions. Positivity follows from their positive mixtures of Gaussian distance kernels. Integrating both outgoing group coordinates in the first formula gives
\(\mathbb E[z_\alpha(S)z_\alpha(T)/b_\alpha(S)]/\overline z_\alpha=1\),
and similarly for the second. Integrating only \(B'\) in the first preserves the complete one-link marked transfer of \(x\); integrating only \(A'\) in the second preserves that of \(y\). This is precisely the respective retained-access identity.

But these two complete experiments differ. The conditional representation is \(y=\rho x+\varepsilon\), with innovation variance \(\sigma^2(1-\rho^2)>0\). Formula (NA8) proves that \(b_\alpha(s)\) is strictly decreasing. At coincident boundary configurations \(A=A'\), \(B=B'\), use the gauge-invariant quadratic mark \(M=S-T\). Then
\[
\boxed{
F_{1\to2}^{S-T}-F_{2\to1}^{S-T}
=\frac1{\overline z_\alpha}
\mathbb E\!\left[(S-T)
\left(\frac1{b_\alpha(S)}-\frac1{b_\alpha(T)}\right)\right]>0.}
\tag{AP19}
\]
The integrand is positive whenever \(S\ne T\), an event of probability one for this faithful joint Gaussian. Its expectation is finite: the row lower bound used in (NA11) gives \(b_\alpha(s)^{-1}\le C_\alpha(1+s)^{3/2}\), and all Gaussian norm moments are finite. Thus one derivative of an ordinary quadratic source already detects the distinction. The unmarked values at these coincident endpoints agree by exchangeability; their equality does not erase the marked difference.

The comparison fixes the final labeled pair but changes which access is first retained. It does not refute order coherence for extensions over one fixed retained root. It proves that the normalized rule needs that extra datum, or a further rule identifying its different root choices. In particular, Schur associativity of the original Gaussian cannot be cited as associativity of a subsequently chosen conditional normalization. An order theorem for growing access diagrams must carry the actual denominators along with the joint covariance and multiplication words.

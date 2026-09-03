# The Gauge-Index No-Go and the Four-Dimensional Center Square

The full continuous compact-group fixed-point route cannot be the finite-index carrier behind the square response: for a faithful minimal compact-group action on a factor with separable predual, the fixed-point inclusion has finite index exactly when the effective acting group is finite, so the faithful global \(SU(N)\) fixed-point inclusion has infinite index. This theorem does not classify local Gauss-law gauge reduction. A canonical finite square nevertheless survives in pure four-dimensional gauge theory at a different type: a ring and its causal complement are both rings, and the jointly available electric and magnetic nonlocal classes form \(Z(G)^*\times Z(G)\), giving index \(|Z(G)|^2\) and certainty budget \(2\log|Z(G)|\) under the finite-center hypotheses. This is a topological information plateau, not a mass gap. Its exact value can label a branch of descent, but only the scale-dependent vacuum response around that branch, pulled back to a normalized physical carrier and compared with the Poincare Casimir, could become energetic stiffness.

**Status: [EXACT -- FAITHFUL MINIMAL COMPACT-GROUP ACTIONS WITH SEPARABLE PREDUAL] for the finite-versus-infinite fixed-point-index theorem; [STANDARD/CONDITIONAL ON THE NET HYPOTHESES] for the four-dimensional ring center square and certainty relation; [EXACT ON A DECLARED SMOOTH ARAKI/BKM TANGENT DOMAIN] for the preserving-expectation Hessian split; [NO-GO] for deriving a normalized BKM or energetic floor from index alone; [OPEN] for the scale-dependent Yang--Mills response, continuum coercivity, and Casimir solder.**

## Four different inclusions must not be conflated

The word *gauge* can hide four mathematically different relations:

| Relation | What is compared | Candidate index behavior |
|---|---|---|
| local gauge reduction | redundant field presentations versus gauge-invariant observables | not automatically a subfactor fixed-point problem |
| compact global fixed points | \(\mathcal M^G\subset\mathcal M\) for a faithful minimal action | infinite for an infinite compact effective \(G\) |
| charged-field extension | one observable factor and a same-region finite-statistics extension or Q-system | finite when only finitely many finite-statistics sectors enter |
| ring additivity--duality inclusion | additive regional algebra inside the maximal algebra carrying nonlocal flux classes | finite when the surviving class group is finite |

The Doplicher--Roberts compact group reconstructs global internal symmetry from superselection data. It does not turn the local gauge redundancy of a Yang--Mills connection into a finite-index quotient. Likewise, a finite-index Q-system can encode a finite collection of charged sectors without being the inclusion between all fields and all \(SU(N)\)-invariant observables.

Nor may this reconstruction be used circularly to generate the gap. If the physical justification of the DHR localization and sector hypotheses has already excluded infrared or long-range sectors by massive-particle assumptions, the reconstructed compact group organizes that supplied sector structure; it does not prove the vacuum mass floor on which the application relied.

## Exact no-go for the full continuous fixed-point route

Let a compact group \(G\) act faithfully and minimally on a factor \(\mathcal M\) with separable predual, and put

$$
\mathcal N=\mathcal M^G.
\tag{GI1}
$$

The spectral/Galois analysis in [[library/a-galois-correspondence-for-compact-groups-of-automorphisms/inq|Izumi--Longo--Popa]] associates to every irreducible representation \(\pi\in\widehat G\) a sector \(\rho_\pi\) of statistical dimension \(d(\rho_\pi)=d_\pi\). The dual canonical endomorphism contains those sectors with the Peter--Weyl multiplicities:

$$
\theta
\simeq
\bigoplus_{\pi\in\widehat G}d_\pi\rho_\pi.
\tag{GI2}
$$

Consequently its statistical dimension is

$$
[\mathcal M:\mathcal M^G]
=d(\theta)
=\sum_{\pi\in\widehat G}d_\pi^2.
\tag{GI3}
$$

For finite \(G\), the representation-theoretic identity \(\sum_\pi d_\pi^2=|G|\) gives the familiar finite group index. An infinite compact group has infinitely many irreducible representations, so (GI3) diverges. The equivalent finite-sum criterion for the dual canonical endomorphism appears in [[library/compact-hypergroups-from-discrete-subfactors/inq|the discrete-subfactor reconstruction]]. Therefore

$$
\boxed{
[\mathcal M:\mathcal M^G]<\infty
\quad\Longleftrightarrow\quad
G\text{ is finite}}
\tag{GI4}
$$

under the stated faithful minimal-action hypotheses. Without effectiveness, an infinite abstract group could act through a finite quotient; (GI4) concerns the effective acting group. In particular, replacing \(G\) by a convenient finite subgroup of \(SU(N)\) would manufacture a finite index chosen by hand. It would not explain the continuum \(SU(N)\) theory.

## The canonical finite remnant is the center, not the gauge group

Pure Yang--Mills does contain finite nonlocal loop-class data encoding generalized symmetries. Wilson classes are labeled by characters of the center \(Z(G)^*\), and 't Hooft classes by \(Z(G)\). These are not local gauge transformations; [[library/generalized-global-symmetries/inq|generalized global symmetry]] supplies the distinction. Their simultaneous presence in the maximal comparison algebra does not mean that every class is a genuine mutually local line operator in one chosen Haag--Dirac net: a global-form or local-net choice selects a mutually local dyonic subgroup.

For a ring-shaped region \(R\), write \(\mathcal A_{\mathrm{add}}(R)\) for the algebra generated additively by local operators and

$$
\mathcal A_{\max}(R)
:=
\mathcal A_{\mathrm{add}}(R')'
\tag{GI5}
$$

for the maximal algebra allowed by causal commutation. Under the transportability and purity assumptions in [[library/entropic-order-parameters-for-the-phases-of-qft/inq|Casini--Huerta--Magan--Pontello]], four spacetime dimensions are special because the causal complement \(R'\) is again ring-like. Both nonlocal classes can then live in the same maximal algebra:

$$
\mathcal A_{\max}(R)
=
\mathcal A_{\mathrm{add}}(R)
\vee\{W_\chi:\chi\in Z(G)^*\}
\vee\{T_z:z\in Z(G)\}.
\tag{GI6}
$$

The conditional expectation \(E_{WT}\) that kills every nontrivial Wilson--'t Hooft class has

$$
\boxed{
\operatorname{Ind}(E_{WT})
=|Z(G)^*\times Z(G)|
=|Z(G)|^2,}
\tag{GI7}
$$

and the complementary-region relative entropies obey a certainty relation. Let

$$
E_{WT}^{R'}:
\mathcal A_{\max}(R')
\longrightarrow
\mathcal A_{\mathrm{add}}(R')
$$

be the analogous expectation in the causal complement. If \(\omega_R\) and \(\omega_{R'}\) denote the restrictions of the same pure global vacuum to the two maximal regional comparison algebras, then

$$
\boxed{
S_{\mathcal A_{\max}(R)}
(\omega_R\Vert\omega_R\circ E_{WT})
+
S_{\mathcal A_{\max}(R')}
(\omega_{R'}\Vert\omega_{R'}\circ E_{WT}^{R'})
=2\log|Z(G)|.}
\tag{GI8}
$$

For \(SU(N)\), this gives \(N^2\) and \(2\log N\). A comparison retaining only Wilson or only 't Hooft classes instead has index \(N\) and certainty constant \(\log N\). The combined square is not dimensional numerology: it is the cardinality of the electric--magnetic class product in the maximal comparison.

The topology matters. In dimensions other than four, the nontrivial topology of a ring and its causal complement generally supports different-dimensional order and disorder operators. In \(3+1\) dimensions both are loops. This provides an exact four-dimensional *duality square*—but not yet a theorem that knotting selects three-space, and not a spectral floor.

## What the index actually measures

For finite-dimensional von Neumann algebra inclusions and \(II_1\) subfactors, [[library/relative-entropy-and-subalgebra-index/inq|Gao--Junge--LaRacuente]] identify the logarithm of the inverse Pimsner--Popa constant of the trace-preserving inclusion with a supremum of statewise relative entropy. For Umegaki entropy,

$$
-\log\lambda(\mathcal M:\mathcal N)
=
\sup_{\rho\in S(\mathcal M)}
D(\rho\Vert E_\tau(\rho))
=
\sup_{\rho\in S(\mathcal M)}
\inf_{\sigma\in S(\mathcal N)}D(\rho\Vert\sigma).
\tag{GI9}
$$

This is an information **capacity** in those stated finite/tracial settings: the largest relative-entropy distance from the subalgebra. For a general finite von Neumann inclusion the paper proves bounds rather than this full equality, and \(\lambda(\mathcal M:\mathcal N)^{-1}\) is not automatically the Kosaki index of an arbitrary chosen expectation. A mass gap is an infimum over normalized nonvacuum physical excitations. Replacing the latter by the former reverses both the quantifier and the carrier.

The preserving-state Hessian makes the mismatch exact. Let \(E:\mathcal M\to\mathcal N\) preserve a faithful normal state \(\sigma\), let \(\operatorname{res}\) restrict normal states, and let \(j_E\eta=\eta\circ E\) recover them. On a common smooth Araki/BKM tangent domain,

$$
P_E:=j_E\operatorname{res},
\qquad
q_{\sigma,E}[\xi]
=
\|(1-P_E)\xi\|_{\mathrm{BKM},\sigma}^2.
\tag{GI10}
$$

Thus the restriction-loss form is exactly coercive, with constant one, on the **forgotten vertical quotient**. Yet every retained output tangent \(y\) has the recovered lift \(j_Ey\), so

$$
\boxed{
\inf_{\operatorname{res}\xi=y}q_{\sigma,E}[\xi]=0.}
\tag{GI11}
$$

Finite index is irrelevant to both statements. If the reference state is not \(E\)-invariant, even a fixed index does not control the smallest positive Hessian ratio: the index-\(4\) inclusion

$$
M_2\otimes1
\subset
M_2\otimes M_2,
\qquad
E=\operatorname{id}\otimes\tau_2,
\tag{GI12}
$$

where \(I_2\) is the identity and \(X,Z\) are the Pauli matrices, the faithful states

$$
\sigma_t
=
\frac{I_2\otimes I_2+tX\otimes X}{4},
\qquad 0<t<1,
$$

and the tangent \(\xi=(Z\otimes I_2)/4\) give the transverse BKM ratio

$$
1-\frac{t}{\operatorname{artanh}t}
=\frac{t^2}{3}+O(t^4)
\longrightarrow0.
\tag{GI13}
$$

Tensoring (GI12) with a Type III factor preserves the index and the counterexample. Hence no positive lower-edge theorem can depend on index alone.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/finite_index_bkm_counterexample_receipt.py|The fixed-index BKM receipt]] evaluates the two metrics directly and diagonalizes the full \(15\)-dimensional traceless Hermitian tangent space; [[contemporary-puzzles/yang-mills-mass-gap/receipts/finite-index-bkm-counterexample-receipt-output.txt|the frozen output]] records the multiplicities and limiting edge.

## The corrected square-response chain

The finite center square can still do a precise job. It can identify a topologically protected branch or plateau of the observable inclusion. It cannot set the response rate on that branch. The chain must be

$$
\boxed{
\begin{aligned}
&\text{continuous gauge reduction}
\longrightarrow
\text{gauge-invariant net},\\
&\text{four-dimensional ring topology}
\longrightarrow
Z(G)^*\times Z(G)
\longrightarrow
|Z(G)|^2,\\
&\text{scale-dependent vacuum state and response}
\longrightarrow
\text{normalized transverse physical frame},\\
&\text{uniform continuum coercivity}
\longrightarrow
\text{Poincare-Casimir floor}.
\end{aligned}}
\tag{GI14}
$$

If \(J_{a,r}\) pulls the \(a\)-th regional loss form back to a common finite-regulator physical tangent carrier and \(P_{a,r}\) is its BKM recovered projection, the live estimate has the form

$$
\boxed{
\sum_a
\|(1-P_{a,r})J_{a,r}\Psi\|_{\mathrm{BKM},\sigma_r}^2
\geq
\kappa_r\|(1-P_{0,r})\Psi\|^2,
\qquad
\inf_r\kappa_r>0.}
\tag{GI15}
$$

The relative positions of the descents—their angle or transversality—are now load bearing. Their individual indices do not determine (GI15). Neither does topology normalize the maps: replacing every \(J_{a,r}\) by \(\varepsilon J_{a,r}\) leaves every index unchanged and multiplies the left side by \(\varepsilon^2\).

## Universality no-go and the role of the causal grain

The Clay problem concerns every compact simple gauge group. Some compact simple groups, including \(G_2\), \(F_4\), and \(E_8\), have trivial center. For them (GI7) is \(1\), while the expected Yang--Mills mass gap is not zero. Therefore the center square cannot be the universal cause of the gap.

It can instead be a **finite fossil of one branch of realization**. In the causal-grain language, a stable class such as (GI7) may record which electric--magnetic distinctions became admissible when a rest-bearing sector engaged. The engagement itself would have to be a change in the scale-dependent form in (GI15)—for example, failure versus success of uniform closed range—not a claim that the integer index turned into MeV. [[causal-grain-as-a-mass-engagement-fossil]] keeps the later CMB/BAO transport map separate.

This also states the strongest defensible relation to knots. Four-dimensional causal complementation puts two loop-class algebras on equal topological footing. Knotting may refine the family of loop observables and improve transversality, but the finite center index sees only generalized-symmetry classes; it does not see enough geometry to force a gap.

## Stopping conditions

This route contributes to the pure Yang--Mills mass-gap proof only if it supplies the first six items below without reading the answer backward from a glueball or cosmological scale. The stronger causal-grain identification additionally requires the seventh:

1. a regulator-level gauge-invariant family of regional and flux channels whose continuum limit is controlled;
2. faithful reference states and declared BKM tangent domains;
3. physically normalized pullbacks \(J_{a,r}\), fixed by gauge/boundary geometry rather than arbitrary rescaling;
4. a uniform transversality estimate of the form (GI15), including centerless compact simple groups;
5. an independent identification of the resulting closed form with, or lower comparison to, the full Poincare Casimir;
6. a dimensional scale supplied by the Yang--Mills continuum trajectory or a separately derived geometric yardstick; and
7. a fossil map showing how any proposed mass-engagement transition alters prospectively frozen external-validation observables after standard cosmological transfer.

The route is falsified as a universal explanation if its only nontrivial datum is \(|Z(G)|^2\), if a fixed index is advertised as a lower Hessian eigenvalue, or if a categorical logarithm is converted directly into energy. Its exact contribution is narrower and valuable: **four-dimensional causal topology supplies a canonical electric--magnetic square, while the mass gap remains the problem of making a normalized family of such distinctions jointly unavoidable.**

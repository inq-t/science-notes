# The Indexed Scale Wall and the Causal Grain

The logistic scale wall carries two related first-order operators whose distinction reveals a genuine critical index structure. The probability half-density factor \(A_\nu\) has Fredholm index \(+1\) for every \(\nu>0\) and its square has the sharp positive edge \(\nu^2\). The factor \(B_\nu\) built from the state density **relative to core capacity** has index \(0\) below \(2\nu=1\), loses Fredholmness exactly at the rate-matching wall, and has index \(+1\) above it. Thus the exact reduced mechanism is not a spacetime pixel: a directed probability state remains coercive at the critical value while its capacity-relative presentation crosses a topological boundary. A still-unconstructed physical carrier map must transport this structure to the Yang--Mills Casimir.

**Status: [EXACT] for both Sobolev-domain Fredholm classifications and the logistic spectrum; [STANDARD] for Fredholm-index stability; [CONSTRUCTION AXIOM] for adopting nondegenerate incoming density as a selection law; [OPEN CONSTRUCTION] for a Yang--Mills or cosmological realization.**

## The ordered factor has an integer index

Fix \(\nu>0\), \(N_c\in\mathbb R\), and write \(x=N-N_c\). Regard

$$
A_{\nu,N_c}
:=
\frac{\mathrm d}{\mathrm dN}
+\nu\tanh(\nu x)
,
\qquad
\operatorname{Dom}(A_{\nu,N_c})=H^1(\mathbb R)
\subset L^2(\mathbb R)
\tag{I1}
$$

as a closed densely defined operator on \(L^2(\mathbb R)\). Equivalently, equip its domain with the graph norm—equivalent here to the usual \(H^1\) norm—and regard it as a bounded Fredholm map \(H^1\to L^2\). Its \(L^2\)-adjoint is

$$
A_{\nu,N_c}^*
=
-\frac{\mathrm d}{\mathrm dN}
+\nu\tanh(\nu x),
\qquad
\operatorname{Dom}(A_{\nu,N_c}^*)=H^1(\mathbb R).
$$

The factorizations in [[binary-information-geometry/witten-darboux#Scale, address, and the sharp weighted gap|the Darboux calculation]] give

$$
A_{\nu,N_c}A_{\nu,N_c}^*
=
-\frac{\mathrm d^2}{\mathrm dN^2}+\nu^2
\geq
\nu^2 I
\tag{I2}
$$

on \(H^2(\mathbb R)\). Hence \(A_{\nu,N_c}\) is onto. Indeed, for \(f\in L^2(\mathbb R)\),

$$
u
:=
A_{\nu,N_c}^*
\bigl(A_{\nu,N_c}A_{\nu,N_c}^*\bigr)^{-1}f
\in H^1(\mathbb R)
$$

satisfies \(A_{\nu,N_c}u=f\). The two first-order kernel equations have the solutions

$$
A_{\nu,N_c}u=0
\quad\Longrightarrow\quad
u=C\,\operatorname{sech}(\nu x),
$$

$$
A_{\nu,N_c}^*v=0
\quad\Longrightarrow\quad
v=C\,\cosh(\nu x).
$$

Only the first is square-integrable. Therefore

$$
\boxed{
\dim\ker A_{\nu,N_c}=1,
\qquad
\dim\ker A_{\nu,N_c}^*=0,
\qquad
\operatorname{ind}A_{\nu,N_c}=1.}
\tag{I3}
$$

This statement avoids the continuum ambiguity of an undeclared heat-kernel “Witten index”: it is the ordinary index of the closed Fredholm \(L^2\) operator, equivalently of its bounded graph-norm map \(H^1(\mathbb R)\to L^2(\mathbb R)\). [[library/supersymmetry-and-quantum-mechanics/inq|Cooper, Khare, and Sukhatme]] supply the supersymmetric-factorization background and warn that other index prescriptions can be subtle in the presence of continuum spectrum.

Reversing the wall,

$$
W(N)=-\nu\tanh\!\bigl(\nu(N-N_c)\bigr),
$$

places the normalizable mode in \(\ker A^*\) and gives index \(-1\). A constant asymptotic orientation \(W=\pm\nu\) gives an invertible operator and index \(0\). The integer therefore records the **ordered passage between inequivalent ends**, not the translation address \(N_c\).

## The sign-at-infinity theorem

The discrete datum is not special to the exact hyperbolic profile. Let \(W\) be real, bounded, locally absolutely continuous, and suppose

$$
W_\pm:=\lim_{N\to\pm\infty}W(N)
$$

exist and are nonzero. Then

$$
A_W=\partial_N+W,
\qquad
\operatorname{Dom}(A_W)=H^1(\mathbb R),
$$

is Fredholm and

$$
\boxed{
\operatorname{ind}A_W
=
\frac{\operatorname{sgn}W_+
-\operatorname{sgn}W_-}{2}.}
\tag{I4}
$$

One proof replaces \(W\) by a step function with the same two limits. Multiplication by their difference is compact from \(H^1(\mathbb R)\) to \(L^2(\mathbb R)\): Rellich compactness controls every bounded interval and decay of the multiplier controls the tails. The index is therefore that of the step operator. Its kernel equations show directly that \(A_W\) has one normalizable mode exactly when \(W_-<0<W_+\), while \(A_W^*\) has one exactly when \(W_->0>W_+\).

This is the scalar one-dimensional member of the open-space Dirac-index pattern developed by [[library/axial-anomalies-and-index-theorems-on-open-spaces/inq|Callias]]. The proof here is elementary because the endpoint symbols are real scalars.

Consequently, the index cannot change along a norm-continuous family that remains Fredholm. To pass between index \(0\) and index \(+1\), at least one asymptotic value must cross zero, an end must cease to exist, or compact control must fail. At that point the operator leaves the Fredholm set. An explicit one-parameter witness is

$$
W_s(N)=a+s\tanh(N-N_c),
\qquad a>0,\quad s\geq0.
$$

For \(s<a\), both ends are positive and the index is zero; at \(s=a\), the incoming end vanishes and the operator is not Fredholm; for \(s>a\), the ends have opposite signs and the index is one. This realizes

$$
\text{index-zero orientation}
\;\longrightarrow\;
\text{non-Fredholm wall}
\;\longrightarrow\;
\text{index-one orientation}.
\tag{I5}
$$

The logistic probability family \(W_\nu=\nu\tanh(\nu x)\) is different: it has index \(+1\) for every \(\nu\neq0\), because \(W_{-\nu}=W_\nu\). At \(\nu=0\) it terminates at

$$
A_0=\partial_N:H^1(\mathbb R)\to L^2(\mathbb R),
$$

whose range is not closed and whose continuum reaches zero. Its Fredholm index is **undefined**, not zero. The family therefore reaches a non-Fredholm endpoint but does not itself supply the index-zero side of (I5).

This is a precise integer for the **orientation** of a causal pointing. It is a loss of asymptotic invertibility required to change directed wall class. It is not yet the index transition at the core-capacity sweet spot, because \(\operatorname{ind}A_{\nu,N_c}=1\) for every \(\nu>0\).

## Relative core capacity makes the sweet spot a Fredholm wall

The state density relative to canonical core trace contains information absent from the probability density alone. Write the core-capacity character more generally as

$$
\tau(e_N)\propto e^{\chi_{\mathrm{core}}N},
\qquad
\chi_{\mathrm{core}}>0,
$$

and define

$$
d_{\nu,N_c}^{(\chi)}(N)
:=
e^{-\chi_{\mathrm{core}}N}q_{\nu,N_c}(N).
\tag{I5a}
$$

This is the Radon--Nikodym coefficient of the state relative to core trace. Now regard its positive square root as a half-density on the additive scale group's translation-Haar carrier \(L^2(\mathbb R,\mathrm dN)\), and define

$$
\begin{aligned}
B_{\nu,N_c}^{(\chi)}
&:=
\partial_N
-\partial_N\log\sqrt{d_{\nu,N_c}^{(\chi)}}\\
&=
\partial_N
+\frac{\chi_{\mathrm{core}}}{2}
+\nu\tanh\!\bigl(\nu(N-N_c)\bigr)
:
H^1(\mathbb R)\to L^2(\mathbb R).
\end{aligned}
\tag{I5b}
$$

This operator does not act on the probability carrier of \(A_\nu\). It acts on **capacity-relative half-densities**, after the trace-growth factor has been removed and the additive scale coordinate is equipped with Haar measure.

That carrier declaration is essential. Let

$$
\mathcal H_\chi
:=
L^2\!\left(\mathbb R,e^{\chi_{\mathrm{core}}N}\mathrm dN\right),
\qquad
U_\chi:\mathcal H_\chi\to L^2(\mathrm dN),
\qquad
(U_\chi f)(N)=e^{\chi_{\mathrm{core}}N/2}f(N).
$$

Define the weighted-carrier factor by the same differential expression as (I5b), but with domain

$$
\operatorname{Dom}(\widehat B_{\nu,N_c}^{(\chi)})
=U_\chi^{-1}H^1(\mathbb R).
$$

Then \(U_\chi\) is unitary between the two displayed Hilbert spaces, sends \(\sqrt d\) to \(\sqrt q\), and gives the typed conjugation

$$
U_\chi\widehat B_{\nu,N_c}^{(\chi)}U_\chi^{-1}
=A_{\nu,N_c}.
$$

Its index is therefore \(+1\) for every \(\nu>0\). The phase transition below is exact only after declaring that the **relative coefficient itself** is to be treated as a half-density on translation-Haar scale. The continuous dual action makes this a natural candidate, but core normality alone does not force the choice.

Its asymptotic coefficients are

$$
W_-^{\mathrm{rel}}
=
\frac{\chi_{\mathrm{core}}}{2}-\nu,
\qquad
W_+^{\mathrm{rel}}
=
\frac{\chi_{\mathrm{core}}}{2}+\nu.
\tag{I5c}
$$

The sign-at-infinity theorem therefore gives the exact phase diagram

$$
\boxed{
\operatorname{ind}B_{\nu,N_c}^{(\chi)}
=
\begin{cases}
0,&2\nu<\chi_{\mathrm{core}},\\
\text{undefined: \(B\) is not Fredholm},&2\nu=\chi_{\mathrm{core}},\\
1,&2\nu>\chi_{\mathrm{core}}.
\end{cases}}
\tag{I5d}
$$

Indeed,

$$
B_{\nu,N_c}^{(\chi)}
\sqrt{d_{\nu,N_c}^{(\chi)}}=0,
$$

and this candidate belongs to \(L^2(\mathbb R,\mathrm dN)\) exactly when \(2\nu>\chi_{\mathrm{core}}\). At equality it approaches a nonzero constant at the incoming end: it is a threshold solution rather than a normalizable kernel vector. The essential spectrum of \(B^*B\) begins at

$$
\min\!\left\{
\left(\frac{\chi_{\mathrm{core}}}{2}-\nu\right)^2,
\left(\frac{\chi_{\mathrm{core}}}{2}+\nu\right)^2
\right\}
=
\left(\nu-\frac{\chi_{\mathrm{core}}}{2}\right)^2,
\tag{I5e}
$$

so zero reaches the essential spectrum precisely at the middle line of (I5d).

For \(2\nu>\chi_{\mathrm{core}}\), its exact unnormalized kernel norm is

$$
\left\|\sqrt{d_{\nu,N_c}^{(\chi)}}\right\|_{L^2(\mathrm dN)}^2
=
e^{-\chi_{\mathrm{core}}N_c}
B\!\left(
1-\frac{\chi_{\mathrm{core}}}{2\nu},
1+\frac{\chi_{\mathrm{core}}}{2\nu}
\right),
\tag{I5e'}
$$

where \(B(\cdot,\cdot)\) is Euler's beta function. It diverges as \(2\nu\downarrow\chi_{\mathrm{core}}\). After normalization, the kernel vector tends weakly to zero and its rank-one projection tends strongly, but not in operator norm, to zero: the mode escapes toward the incoming ideal boundary rather than disappearing at any finite \(N\). The escape statement is exact; interpreting it as “forgetting at infinity” is a proposed realization. Strong rank loss alone is not a protected finite event; the Fredholm endpoint data are what carry the integer distinction.

For the canonically normalized core, \(\chi_{\mathrm{core}}=1\). Hence the previously derived mismatch

$$
\varepsilon_{\mathrm{in}}=2\nu-1
$$

is not merely a comparison of exponents: it is the sign controlling the Fredholm class of \(B_\nu\). The passage

$$
\operatorname{ind}B_\nu:
\quad
0
\;\longrightarrow\;
\text{undefined at }\nu=\frac12
\;\longrightarrow\;
1
\tag{I5f}
$$

is the strongest exact candidate for the discrete causal grain. The index does not jump *at* a Fredholm operator; the critical member is the non-Fredholm wall separating two indexed phases.

For a fixed supercritical \(\nu>\chi_{\mathrm{core}}/2\), the scalar coefficient of \(B\) crosses zero once, at

$$
N_*
=
N_c
-\frac1\nu
\operatorname{artanh}\!\left(
\frac{\chi_{\mathrm{core}}}{2\nu}
\right).
\tag{I5g}
$$

The crossing is upward and carries the unit index. As \(\nu\downarrow\chi_{\mathrm{core}}/2\), \(N_*\to-\infty\): the crossing exits through the incoming ideal boundary. This is spectral flow in the scale coordinate for each fixed supercritical member. The parameter path through the critical member is not ordinary Fredholm spectral flow, because that member is non-Fredholm.

## Boundary extension and the integer

The two asymptotic symbols can be packaged without treating infinity as an ordinary point of the scale line. The compactification extension

$$
0
\longrightarrow
C_0(\mathbb R)
\longrightarrow
C([-\infty,+\infty])
\longrightarrow
C(\{-\infty,+\infty\})
\longrightarrow
0
\tag{I5h}
$$

has a \(K\)-theory connecting map. When both endpoint coefficients are nonzero, their positive-sign projections define boundary \(K_0\) data; the connecting class measures their difference, and pairing it with the translation Dirac class gives the scalar index in (I4). At the critical wall the incoming coefficient is zero, its sign projection is undefined, and the Fredholm lift fails.

This is the appropriate sense in which a boundary remembers an integer that no finite-\(N\) support calculation sees. For every \(\nu>0\), \(q_{\nu,N_c}(N)>0\) at every finite \(N\), so the support projection of the probability state is always the identity. There is no state-support jump. Above the relative wall, the kernel projection of \(B_\nu\) is rank one; as the wall is approached it escapes strongly to zero while retaining operator norm one. That is a kernel-projection event on the auxiliary relative carrier, not a support jump of \(q_\nu\).

If the construction is lifted directly to the semifinite noncommutative core, a Breuer index need not be integer-valued. Integrality must come from an ordinary Fredholm realization, an integral \(K\)-homology pairing, or an additional theorem. Merely invoking a Type-III core, torsor, groupoid, or conditional expectation supplies none of these boundary maps.

## The exact part of a frozen fossil is homotopy memory

There is now a rigorous meaning for “frozen” that does not turn the grain into a microscopic ruler. Let \(t\mapsto W_t\) be a path of real bounded coefficients such that

$$
B_t:=\partial_N+W_t:H^1(\mathbb R)\longrightarrow L^2(\mathbb R)
$$

is continuous in operator norm as a family of bounded maps from the fixed Sobolev space \(H^1\) to \(L^2\), and Fredholm for every \(t\) in a connected interval. Then

$$
\boxed{\operatorname{ind}B_t\ \text{is constant along the interval}.}
\tag{I5i}
$$

For scalar walls, uniform nonzero asymptotic end values give the relevant Fredholm region. The index can change only when the family leaves that region—for the canonical relative-density wall, precisely when the incoming end value reaches zero at \(2\nu=1\). Thus a path that has passed into \(2\nu>1\) can deform its detailed profile, width, and centre without losing its unit index, provided the deformation remains norm-continuous and the end gap does not close. If the carriers vary, the same statement first requires continuous Hilbert-bundle trivializations or an equivalent continuous Fredholm-family construction.

This is the first exact candidate for a fossil: a downstream member can retain the homotopy class of a past crossing even though no literal \(4.2\,\mathrm{fm}\) cell remains active. But the theorem preserves only the index. It does not preserve a local overlap, an acoustic wavelength, a transfer amplitude, or an energy unit. Indeed, a translated kernel can leave every fixed compact detector region while the index stays one, and the normalized critical kernel already escapes weakly toward the incoming ideal boundary. An observable fossil therefore requires an additional characteristic map or pairing that transports the index class to retained physical data. BAO cannot be identified with the integer merely because both are robust records.

The causal interpretation is consequently two-stage:

$$
\boxed{
\text{non-Fredholm crossing}
\longrightarrow
\text{homotopy-stable Fredholm class}
\xrightarrow{\text{open physical characteristic}}
\text{observable residue}.}
\tag{I5j}
$$

Only the first arrow and the stability of the middle object are established in this reduced scale model.

## The integer protects pointing; the asymptotic modulus supplies stiffness

Introduce the graded self-adjoint operator

$$
\mathscr D_{\nu,N_c}
:=
\begin{pmatrix}
0&A_{\nu,N_c}^*\\
A_{\nu,N_c}&0
\end{pmatrix}
$$

as a self-adjoint operator on \(L^2(\mathbb R)\oplus L^2(\mathbb R)\) with domain \(H^1(\mathbb R)\oplus H^1(\mathbb R)\). Its square is

$$
\mathscr D_{\nu,N_c}^2
=
\begin{pmatrix}
A_{\nu,N_c}^*A_{\nu,N_c}&0\\
0&A_{\nu,N_c}A_{\nu,N_c}^*
\end{pmatrix},
$$

and hence

$$
\boxed{
\sigma(\mathscr D_{\nu,N_c})
=
\{0\}
\cup(-\infty,-\nu]
\cup[\nu,\infty).}
\tag{I6}
$$

The index fixes the chirality and robustness of the single zero mode. The asymptotic modulus \(\nu=|W_\pm|\) fixes the continuum threshold, while the squared zero-mode sector has

$$
\sigma(A^*A)=\{0\}\cup[\nu^2,\infty).
$$

[[library/dirac-operators-and-domain-walls/inq|Lu, Watson, and Weinstein]] analyze the corresponding Dirac domain-wall pattern and its localized zero mode. Their physical-space mass kink is a precedent for the operator theory, not an identification with the logarithmic-scale carrier used here.

These are different accomplishments:

| Datum | Type | What it controls |
|---|---|---|
| \(\operatorname{ind}A\) | integer | orientation and net zero-mode count |
| \(|W_\pm|=\nu\) | dimensionless rate | asymptotic invertibility and the exact flat-partner edge |
| \(\operatorname{ind}B\) | phase-dependent integer | capacity-relative localization below or above the rate wall |
| \(N_c\) | scale-torsor address | where the pointing is centred |
| \(E_*\) | dimensional comparison | conversion of a dimensionless physical-form bound into energy |

Index alone does not prove a positive excitation gap. Index-preserving perturbations may introduce paired low-lying states, and a regulator family can have a positive gap at every member while its infimum tends to zero. The sharp edge \(\nu^2\) follows here because the complementary partner is exactly homogeneous. Conversely, the flat-partner theorem assumes a normalizable ordered zero mode, so the index calculation does not independently derive that mode; it proves that the resulting direction is a stable integer class rather than a profile-specific accident.

## Two carriers meet at one critical value

For canonical core character, the boundary law in [[wall-construction-interface/scale-character-solder#A boundary law that selects the projection-branch value|the scale-character solder]] selects \(\nu=1/2\) by requiring the state density to be neither erased nor amplified relative to incoming trace capacity. At exactly that value,

$$
\boxed{
\operatorname{ind}A_{\frac12,N_c}=1,
\qquad
\sigma(A_{\frac12,N_c}^*A_{\frac12,N_c})
=
\{0\}\cup\left[\frac14,\infty\right),
\qquad
B_{\frac12,N_c}\ \text{is not Fredholm}.}
\tag{I7}
$$

There is no contradiction. The operators have different inputs:

- \(A_\nu\) acts on the square root of the normalized probability profile \(q_\nu\). Its zero mode remains normalizable and its squared excitation edge is \(1/4\).
- \(B_\nu\) acts on the square root of the density \(d_\nu=e^{-N}q_\nu\) relative to exponentially growing core capacity, viewed on translation-Haar scale. At the critical rate its incoming tail is constant, so its would-be zero mode lies exactly at the continuum threshold.

The strongest reduced causal-grain statement is therefore not “the index equals one at the sweet spot.” It is

$$
\boxed{
\begin{array}{c}
\text{probability pointing remains index-one and coercive},\\[2pt]
\text{capacity-relative pointing crosses }0
\to\text{non-Fredholm}\to1
\text{ at the same rate.}
\end{array}}
\tag{I8}
$$

This separates **probability pointing** from **capacity-relative localization** without separating their critical coordinate. The discrete “either/or” is the change of Fredholm phase across the wall; the dimensionless \(1/4\) is the probability-carrier stiffness at the wall. Neither is yet an obtained fact or a mass in MeV, and the critical member itself has no \(B\)-index.

## A conditional carrier can be born gapped

The two-carrier structure supports a precise reversal of the usual question. This construction must not be stacked onto the earlier finite-nonzero boundary-density law as a second condition on one static member. That law selects the **critical** value \(2\nu=\chi_{\mathrm{core}}\), where \(B_\nu\) is non-Fredholm and its relative zero mode is not normalizable. The rule below instead treats critical equality as a transition locus and declares the strictly supercritical region to be the post-crossing admissible phase. Relating those two roles requires a scale evolution \(r\mapsto\nu(r)\) and a carrier-formation map that have not been constructed.

With that distinction, define the capacity-admissible widths by the existence of a normalizable relative zero mode,

$$
\mathsf{Adm}_\chi
:=
\left\{
\nu>0:
\ker B_{\nu,N_c}^{(\chi)}\neq\{0\}
\right\}.
\tag{I9}
$$

The phase calculation gives

$$
\mathsf{Adm}_\chi
=
\left(\frac{\chi_{\mathrm{core}}}{2},\infty\right).
\tag{I10}
$$

For every admitted width, multiplication by the capacity half-character gives an exact one-dimensional line isomorphism

$$
T_{\nu,\chi}:
\ker B_{\nu,N_c}^{(\chi)}
\longrightarrow
\ker A_{\nu,N_c},
\qquad
T_{\nu,\chi}f
:=
e^{\chi_{\mathrm{core}}N/2}f,
\tag{I10a}
$$

because it sends \(\sqrt d\) to \(\sqrt q\). This is not a bounded isomorphism of the two full translation-Haar carriers; it is only a canonical relation between their kernel lines after both are normalizable.

Meanwhile the probability-carrier excitation stiffness is

$$
g_{\mathrm{prob}}(\nu)
:=
\inf\sigma\!\left(
A_{\nu,N_c}^*A_{\nu,N_c}
\big|_{\ker A_{\nu,N_c}^{\perp}}
\right)
=
\nu^2.
$$

Therefore

$$
\boxed{
\inf_{\nu\in\mathsf{Adm}_\chi}
g_{\mathrm{prob}}(\nu)
=
\frac{\chi_{\mathrm{core}}^2}{4}>0.}
\tag{I11}
$$

For canonical core character, every capacity-admissible member has \(g_{\mathrm{prob}}(\nu)>1/4\), and \(1/4\) is the unattained onset infimum. Equivalently, the first-order Dirac threshold has infimum \(1/2\). The critical member \(\nu=1/2\) is the boundary of the **declared admissible** phase, not a member with a normalizable relative zero mode.

Thus, **conditional on the admissibility rule (I9)**, no allowed carrier has a probability gap that can be made arbitrarily small. The scale-shadow carrier is not obtained by continuously lifting one excitation out of a fixed gapless space; it first becomes jointly admissible only on the side where it is already coercive. This is an exact implication of a declared carrier-selection rule and is the cleanest current model of “mass engagement.”

The load-bearing word is *declared*. Nothing yet proves that physical existence requires the relative-Haar zero mode, promotes the line map (I10a) to an identification of physical vacuum data, or transports either carrier to Yang--Mills. On the natural core-trace carrier, \(\widehat B_\nu^{(\chi)}\) is unitarily equivalent to \(A_\nu\), the admissible set is all \(\nu>0\), and the infimum collapses to zero. For a varying-regulator family with noncanonical \(\chi_r\), uniform positivity would additionally require \(\inf_r\chi_r>0\); the canonical core instead fixes \(\chi_r=1\). A physical descent theorem must select the relative carrier and construct the full correspondence; otherwise (I11) is a mathematically exact conditional selection effect, not an explanation of nature.

## Why this is not a Yang--Mills index theorem

[[library/solitons-with-fermion-number-one-half/inq|Jackiw and Rebbi]] provide a physical precedent in which a Dirac zero mode is localized by nontrivial soliton data. The resemblance is structural, not an identification. The operator in (I1) acts on half-densities over logarithmic core scale. It is not a spacetime Dirac operator, a Faddeev--Popov operator, a Yang--Mills instanton complex, or the physical Hamiltonian.

In particular, an instanton number or fermionic Dirac index does not imply a bosonic Yang--Mills mass gap. Such indices usually protect zero modes; the Clay target asks for a uniform positive lower edge on the entire nonvacuum physical carrier. Importing a familiar topological charge without an intertwiner would merely rename the missing construction.

A physical realization must supply all of the following:

1. gauge- and OS-null-quotient-compatible analogues of both the probability factor \(A_r\) and capacity-relative factor \(B_r^{\mathrm{cap}}\), distinct from the OS interface unitary \(B_r^{\mathrm{OS}}\);
2. a reason their zero mode, Fredholm phases, and critical loss of Fredholmness represent vacuum pointing and the factive wall rather than an unrelated topological sector;
3. a complete frame or analysis map that does not erase any nonvacuum physical direction;
4. a same-carrier quadratic-form comparison between \(\mathbb A_r^*\mathbb A_r\), or its wall descendant, and the reconstructed Poincare Casimir;
5. an independently fixed dimensional scale and regulator-uniform lower bound; and
6. an index class, vacuum projection, and coercive form that survive continuum reconstruction.

The construction fails if the proposed index lives only on an auxiliary gauge-fixed carrier, if different physical excitations lie in the kernel of the analysis map, if the index changes only because a regulator is removed singularly without a controlled limiting carrier, or if the dimensional scale is chosen from the observed glueball mass.

The result is nevertheless a genuine advance in the pre-QFT layer. The reduced wall now contains a principled discrete phase boundary and a simultaneously nonzero probability-carrier edge. The outstanding problem is no longer “where could discreteness come from?” It is whether Yang--Mills boundary descent realizes these two carriers completely enough for the critical index structure and dimensionless stiffness to become one physical joint-Casimir statement.

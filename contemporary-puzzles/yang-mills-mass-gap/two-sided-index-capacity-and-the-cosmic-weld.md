# Two-Sided Index Capacity and the Cosmic Weld

A finite-index expectation between infinite-dimensional factors carries an exact, Type-III-compatible quantity of distinction: its log index is both the largest relative-entropy loss attainable under the expectation and a statewise budget shared with the dual expectation on the commutant. For a standard finite-index sector realized over infinite-dimensional factors this becomes \(2\log d(X)\), additive under Connes fusion. A proposed identification with logarithmic horizon-capacity growth therefore has a precise mathematical type and reduces an entire discrete cosmological ladder to one generator-level weld. It still supplies neither local Yang--Mills coercivity nor energy; those require a separate common-carrier response theorem and dimensional solder.

**Status: [ESTABLISHED] for the finite-index relative-entropy identities under the stated factor and standard-form hypotheses; [STANDARD CONDITIONAL COROLLARY] for the correspondence and fusion formulas when a standard minimal sector realization over infinite-dimensional factors is supplied; [EXACT CONDITIONAL] for the cosmological ladder after the monoidal weld and Einstein apparent-horizon capacity law are assumed; [CONJECTURE] for the weld itself, the selection of a physical sector and rung, and any identification with mass engagement; [OPEN] for the Yang--Mills carrier map, uniform coercivity, energy solder, fossil transport, and gravity-decoupled continuum limit.**

## The exact quantity carried by an inclusion

Let

\[
\mathcal B\subset\mathcal A
\]

be an inclusion of \(\sigma\)-finite infinite-dimensional factors, with \(\mathcal A\) acting in standard form, and let

\[
\varepsilon:\mathcal A\longrightarrow\mathcal B
\]

be a normal faithful conditional expectation of finite Kosaki index. Its dual operator-valued weight is a scalar multiple of a conditional expectation on the commutants,

\[
\varepsilon^{-1}
=
[\mathcal A:\mathcal B]_{\varepsilon}\,\varepsilon',
\qquad
\varepsilon':\mathcal B'\longrightarrow\mathcal A'.
\tag{IC1}
\]

For a faithful normal state \(\varphi\) represented by a vector in the natural cone, write \(\varphi'\) for the induced state on \(\mathcal B'\), and define

\[
L_{\varepsilon}(\varphi)
:=
S_{\mathcal A}
(\varphi\Vert\varphi\circ\varepsilon),
\qquad
L_{\varepsilon'}(\varphi')
:=
S_{\mathcal B'}
(\varphi'\Vert\varphi'\circ\varepsilon').
\tag{IC2}
\]

The dual relative-entropy identity gives

\[
\boxed{
L_{\varepsilon}(\varphi)
+L_{\varepsilon'}(\varphi')
=
\log[\mathcal A:\mathcal B]_{\varepsilon}.}
\tag{IC3}
\]

The summands vary with the state; their sum does not. The inclusion therefore carries a two-sided **distinction budget**. One side measures distinguishability erased by the declared expectation, while the commutant side measures the complementary deficit. This is not conservation of a material substance and not a Noether law. It is an exact duality between an inclusion and its commutant inclusion.

For infinite-dimensional factors the same log index is the optimal one-sided loss:

\[
\boxed{
\mathfrak C(\varepsilon)
:=
\sup_{\varphi\in\mathfrak S_n(\mathcal A)}
S_{\mathcal A}
(\varphi\Vert\varphi\circ\varepsilon)
=
\log[\mathcal A:\mathcal B]_{\varepsilon}.}
\tag{IC4}
\]

Thus the index is not merely a discrete label. It is the exact maximum amount of relative-entropy distinction that this algebraic forgetting can hide. Equations (IC3) and (IC4) remain meaningful for Type-III factors because they use Araki relative entropy rather than density-matrix entropy.

The functional in (IC4) is Longo--Witten's direct-state supremum. It is not definitionally the Connes--Størmer--Hiai inclusion entropy, whose optimization ranges over expectation-invariant barycentres and decompositions into positive functionals. For an infinite subfactor, [[library/minimum-index-for-subfactors-and-entropy-ii/inq|Hiai's ensemble functional]] reaches \(\log\operatorname{Index}E\) exactly on the minimal-expectation branch; Longo--Witten's direct-state supremum reaches it for every finite-index expectation between infinite-dimensional factors. The two can therefore have the same endpoint under overlapping hypotheses without being the same functional.

This result realizes one part of the proposed Copernican reversal:

\[
\boxed{
\text{inclusion and duality}
\longrightarrow
\text{finite distinction capacity},}
\]

instead of postulating an entropy and then searching for an algebra that represents it.

## The finite-dimensional half-index firewall

The factor-of-two convention cannot be inferred from a small matrix example without checking which index and which ancillary carrier are being used. For

\[
\mathbb C\mathbf1\subset M_d(\mathbb C),
\qquad
\varepsilon(x)=\operatorname{tr}_d(x)\mathbf1,
\]

a pure state obeys

\[
D(\rho\Vert\tau_d)=\log d.
\tag{IC5}
\]

Here the best positivity constant gives Pimsner--Popa index \(d\), whereas the completely bounded, Jones--Watatani, or categorical index is \(d^2\). The one-sided unamplified loss is therefore

\[
\log d
=
\frac12\log d^2.
\]

More generally, for

\[
M_n\otimes\mathbf1_d
\subset
M_n\otimes M_d
\]

with the tracial expectation, the ordinary, unamplified maximum is

\[
\mathfrak C_{n,d}
=
\log\!\bigl(d\min\{n,d\}\bigr).
\tag{IC6}
\]

It ranges from \(\log d\) when \(n=1\) to \(2\log d\) when \(n\geq d\). The stabilized capacity obtained after arbitrary matrix amplification is the full log Watatani index. In particular, for \(n=d\), take a maximally entangled pure state \(\Phi_d\). The tracial coarse-graining sends it to \(\tau_d\otimes\tau_d\), so

\[
D(\Phi_d\Vert\tau_d\otimes\tau_d)
=
2\log d
=
\log d^2.
\tag{IC7}
\]

The full index capacity is therefore relational: the retained side information matters. This is exactly why the half-log product-edge identity in [[spectral-wall-descent/finite-index-area-weld]] and the two-sided capacity (IC3)--(IC4) must not be identified.

## From a standard sector to an additive capacity character

Let \(X\) be a dualizable factor endocorrespondence which is realized by a finite-index endomorphism or standard subfactor sector over infinite-dimensional factors, and let \(\varepsilon_X\) be its standard minimal expectation. Under the standard solution of the conjugate equations,

\[
[\mathcal A:\mathcal B]_{\varepsilon_X}
=
d(X)^2.
\tag{IC8}
\]

Define the capacity character

\[
\mathfrak C(X)
:=
\mathfrak C(\varepsilon_X)
=
2\log d(X).
\tag{IC9}
\]

For composable standard factor sectors, statistical dimension is multiplicative under Connes fusion. Hence

\[
\boxed{
\mathfrak C(X\boxtimes Y)
=
\mathfrak C(X)+\mathfrak C(Y),
\qquad
\mathfrak C(X^{\boxtimes n})
=
2n\log d(X).}
\tag{IC10}
\]

The logarithm is not an aesthetic choice: it is the additive character of the multiplicative categorical dimension. With nontrivial centers, the scalar must be replaced by the full dimension matrix or correspondence together with matched spherical or Markov data. An arbitrary expectation need not be minimal, and a bare correspondence does not itself select an expectation, edge state, or physical carrier.

## The one-generator cosmic weld

Let

\[
\iota_A(t)
:=
\frac{S_A(t)}{k_B}
\]

denote a dimensionless whole-capacity ledger. For the flat Einstein apparent horizon audited in [[contemporary-puzzles/yang-mills-mass-gap/cosmic-geon-hypothesis-and-horizon-rate-ledger|the cosmic-geon rate ledger]],

\[
\iota_A(t)
=
\frac{\pi c^5}{G\hbar H(t)^2}.
\tag{IC11}
\]

Choose a birth cut \(b\) and a sequence of candidate wall cuts \(t_n\) on an expanding branch with \(H_b,H_n>0\), and assume \(d(X)>1\). There are two inequivalent welds.

The conservative **additive-entropy weld** would be

\[
\boxed{
\iota_A(t_n)-\iota_A(t_b)
\stackrel{?}{=}
\mathfrak C(X^{\boxtimes n})
=
2n\log d(X).}
\tag{IC12}
\]

It compares two quantities additive under independent composition. By (IC11), it would imply

\[
\frac{H_n}{H_b}
=
\left(
1+\frac{2n\log d}{\iota_b}
\right)^{-1/2}.
\tag{IC13}
\]

This is not a geometric \(d^{-n}\) ladder.

The stronger **multiplicative effective-cell-count weld** treats \(\iota_A\), under the additional area-cell interpretation, as the positive effective count on which the categorical index acts multiplicatively:

\[
\boxed{
\mathscr D_{\mathrm{cos}}(n)
:=
\log\frac{\iota_A(t_n)}{\iota_A(t_b)}
\stackrel{?}{=}
\mathfrak C(X^{\boxtimes n})
=
2n\log d(X).}
\tag{IC14}
\]

Equation (IC14) is not a consequence of the relative-entropy theorem. It is an independent exponential-growth law,

\[
\frac{\iota_n}{\iota_b}
\stackrel{?}{=}
\operatorname{Ind}_{\mathrm{cat}}(X^{\boxtimes n})
=
d(X)^{2n},
\tag{IC15}
\]

and its physical content is precisely the claim that categorical multiplicity counts relative effective horizon cells rather than additive entropy increments. The Bekenstein--Hawking formula makes \(\iota_A\) a dimensionless entropy and normalized area. Calling that normalized area a cell count is an additional interpretation; the formula does not establish literal discrete cells or decide which categorical object corresponds to which reading.

Suppose the admissible cuts on the multiplicative branch compose homogeneously,

\[
\mathscr D_{\mathrm{cos}}(m+n)
=
\mathscr D_{\mathrm{cos}}(m)
+
\mathscr D_{\mathrm{cos}}(n),
\qquad
\mathscr D_{\mathrm{cos}}(0)=0.
\tag{IC16}
\]

Then the entire weld follows from the one-cell condition

\[
\mathscr D_{\mathrm{cos}}(1)=\mathfrak C(X).
\tag{IC17}
\]

This elementary generator theorem is structurally important. It reduces an infinite family of numerical matches to one naturality square: construct one primitive correspondence, one primitive whole-capacity increment, and a composition-preserving comparison between them. Fitting each rung separately is forbidden.

Under (IC11), the conditional ladder is

\[
\boxed{
\frac{\iota_n}{\iota_b}=d^{2n},
\qquad
\frac{H_n}{H_b}=d^{-n}.}
\tag{IC18}
\]

Let \(N=\log a\) be e-fold or Misner time and

\[
\epsilon:=-\frac{\dot H}{H^2}.
\]

Equivalently, for the deceleration parameter \(q:=-\ddot a/(aH^2)\),

\[
\epsilon=1+q.
\tag{IC18a}
\]

Since \(\mathrm d\log H/\mathrm dN=-\epsilon\), the same weld is

\[
\boxed{
\int_{N_b}^{N_n}\epsilon(N)\,\mathrm dN
=
n\log d.}
\tag{IC19}
\]

The local history may be smooth. Only the globally admissible endpoints are discrete. This is a precise version of “continuous local patches, discrete whole geometry.” It does not mean spacetime has pixels.

## What cosmic expansion contributes

Differentiating the horizon ledger gives an exact capacity-flow rate,

\[
\boxed{
\frac{\mathrm d}{\mathrm dt}\log\iota_A
=
-2\frac{\dot H}{H}
=
2\epsilon H.}
\tag{IC20}
\]

This is the signed fractional change rate of the horizon ledger. The signed additive entropy rate is instead

\[
\dot\iota_A=2\epsilon H\,\iota_A.
\tag{IC21}
\]

Thus the fractional rate is \(2H(1+q)\): cosmic acceleration enters through the dimensionless shape factor \(1+q\), while \(H\) supplies the clock rate.

This distinguishes four notions that loose “cosmic leakage” language can collapse:

- \(H\) is the logarithmic expansion rate of the scale factor;
- \(\epsilon H=-\mathrm d\log H/\mathrm dt\) is the signed logarithmic decay rate of \(H\);
- \(2\epsilon H\) is the signed fractional change rate of the apparent-horizon ledger; and
- \(2\epsilon H\iota_A\) is its additive growth in nats per unit proper time.

For \(\epsilon>0\) the ledger grows; for a phantom branch with \(\epsilon<0\) it shrinks. In exact de Sitter expansion, \(H>0\) but \(\epsilon=0\), so the horizon capacity does not change. Therefore expansion alone cannot be the proposed distinction-production or leakage rate. The fractional change of the whole ledger is \(2\epsilon H\); its additive change is \(2\epsilon H\iota_A\).

The exchange-rate reading of \(G\) does not remove this distinction. Since \(c^3/G\) has units of mass per proper time, the two cosmic rates define two inequivalent quotients,

\[
\boxed{
m_{\mathrm{frac}}
:=
\frac{c^3/G}{\mathrm d\log\iota_A/\mathrm dt}
=
\frac{c^3}{2G\epsilon H},
\qquad
m_{\mathrm{nat}}
:=
\frac{c^3/G}{\mathrm d\iota_A/\mathrm dt}
=
\frac{c^3}{2G\epsilon H\iota_A}.}
\tag{IC21a}
\]

The first is a whole mass per fractional capacity e-fold; the second is a mass per added nat. Neither is yet a microscopic particle mass, and both become undefined when the ledger is stationary even though the apparent-horizon mass remains finite. Thus “mass is a rate” is not a complete type declaration: one must name the dimensionless numerator, decide whether the ledger is logarithmic or additive, and construct the process whose proper-time derivative is being taken.

If the weld is valid, define the continuous address

\[
\nu(t)
:=
\frac{\log(\iota_A(t)/\iota_b)}{2\log d}.
\tag{IC22}
\]

Then

\[
\dot\nu(t)
=
\frac{\epsilon(t)H(t)}{\log d},
\qquad
\nu(t_n)=n.
\tag{IC23}
\]

Equation (IC23) is a smooth cosmic address on the multiplicative branch whose integer crossings label candidate categorical walls. The integer is not continuously varying ontology; it is attained only at the selected cuts. [[contemporary-puzzles/yang-mills-mass-gap/causal-grain-as-a-mass-engagement-fossil|A mass-engagement claim]] would additionally have to prove that one crossing changes the physical carrier or its neutral response and that the resulting scale is transported as a fossil.

## From capacity to a candidate dimensional yardstick

The log index is dimensionless. It can select a member of a scale family but cannot become an energy by itself. Once a cut has been selected, the common-count construction in [[cosmological-selection-of-the-yang-mills-yardstick]] gives

\[
Q_{\mathrm{cc}}^3
=
\frac{3}{4\pi\gamma s_*}\,\iota_A,
\qquad
E_*
=
\hbar H Q_{\mathrm{cc}},
\tag{IC24}
\]

or equivalently

\[
E_*^3
=
\frac{3}{4\gamma s_*}
\frac{\hbar^2c^5H}{G}.
\tag{IC25}
\]

There is also an \(\hbar\)-free presentation if \(\iota_A\) is first supplied as an independent algebraic count. The apparent-horizon mass and the common-count member are

\[
M_A
=
\frac{c^3}{2GH},
\qquad
m_*
=
\left(\frac{6\pi^2}{\gamma s_*}\right)^{1/3}
M_A\,\iota_A^{-2/3}.
\tag{IC25a}
\]

Here \(c^3/G\) has units of mass per time: it is a mass exchange rate, not a mass. The cosmic duration \(H^{-1}\) returns the whole mass \(M_A\), and the dimensionless capacity quotient selects a candidate local member. If \(\iota_A\) is then identified with Bekenstein--Hawking entropy, (IC11) reintroduces \(\hbar\); the \(\hbar\)-free display has not derived the action unit.

For comparison, the rate quotients in (IC21a) are \(m_{\mathrm{frac}}=M_A/\epsilon\) and \(m_{\mathrm{nat}}=M_A/(\epsilon\iota_A)\), whereas (IC25a) scales as \(M_A\iota_A^{-2/3}\). The exponent \(-2/3\) is therefore additional whole-to-part geometry, not dimensional analysis and not a consequence of entropy production alone.

Thus \(k_B\) converts entropy to the dimensionless ledger \(\iota_A=S_A/k_B\); \(c,G,H\) can provide a whole mass once a cosmic clock is admitted; \(\hbar\) enters the Einstein entropy/action identification and the clock-energy solder; and \(\gamma s_*\) records the declared effective-cell convention. Write

\[
\mathfrak C_n
:=
\mathfrak C(X^{\boxtimes n})
=
2n\log d(X).
\tag{IC25b}
\]

Combining (IC14), (IC18), and (IC24) at two cuts with the same effective-cell law gives

\[
\boxed{
\frac{Q_{\mathrm{cc},n}}{Q_{\mathrm{cc},b}}
=
e^{\mathfrak C_n/3}
=
d^{2n/3},
\qquad
\frac{E_{*,n}}{E_{*,b}}
=
e^{-\mathfrak C_n/6}
=
d^{-n/3}.}
\tag{IC26}
\]

Thus one dimensionless distinction capacity controls three different ratios:

\[
\Delta\log\iota_A=\mathfrak C_n,
\qquad
\Delta\log H=-\frac12\mathfrak C_n,
\qquad
\Delta\log E_*=-\frac16\mathfrak C_n.
\tag{IC27}
\]

These are exact consequences of the declared weld and common-count geometry, not evidence that the weld is physically true.

Neither a dimensionless age \(Ht\) nor normalized acceleration breaks the remaining dilation orbit. If a proper age \(t_c\) is independently constructed and a dimensionless shape law selects \(\Theta_c=H_ct_c\), then \(H_c=\Theta_c/t_c\); the proper duration is the dimensional input. Alternatively, an intrinsically fixed birth capacity \(\iota_b\) makes (IC11) an absolute normalization. Without one such section, (IC14) fixes ratios only.

## Why this is not yet the mass gap

The exact capacity (IC4) is a supremum over states. A Yang--Mills mass gap requires a positive infimum over every nonvacuum physical direction. Those are opposite quantifiers:

\[
\sup_{\varphi}
S(\varphi\Vert\varphi\varepsilon)
=
\log\operatorname{Ind}(\varepsilon)
\quad\not\Longrightarrow\quad
\inf_{\psi\perp\Omega}
\frac{\langle\psi,H_{\mathrm{YM}}\psi\rangle}{\|\psi\|^2}
>0.
\tag{IC28}
\]

A preserving expectation is projection-like on its \(L^2\) carrier and has a forgotten kernel. Its descent-loss Hessian is stiff vertically but vanishes on retained directions. [[subfactor-angle-coercivity-and-the-index-firewall]] makes the quantitative obstruction exact for two descents: after their common range is removed, the edge is \(1-c_F\), but a spin-model family keeps all three Jones indices fixed at \(2,2,4\) while \(c_F\to1\). Even the common inclusion and its standard reducible Q-system can be held fixed while the angle collapses. Index therefore does not determine the mixed relative position that coercivity needs.

[[quantum-g2-categorical-rigidity-and-the-carrier-firewall]] supplies the complementary positive result and an even sharper internal control. The fundamental quantum-\(G_2\) category has a universal categorical edge for \(q\neq1\), while at \(q=1\) its sector capacity remains \(2\log7>0\) and its categorical rigidity vanishes. Thus maximum forgetting capacity and minimum distinction cost are independent invariants even within one continuous categorical family. The log index normalizes how much can be forgotten; only an additional relative-position law or Kazhdan-type invariant can prove that every declared nontrivial direction is seen.

The missing theorem must construct, independently of the target spectrum:

\[
\boxed{
\begin{aligned}
\text{whole sector and dual expectation}
&\longrightarrow
\text{normalized capacity character},\\
\text{cosmic history and selected wall}
&\longrightarrow
\text{dimensional member }E_*,\\
\text{Yang--Mills observable carrier}
&\longrightarrow
\text{uniform positive distinction form},\\
\text{same-carrier comparison}
&\longrightarrow
\text{Hamiltonian edge and Poincare mass}.
\end{aligned}}
\tag{IC29}
\]

The first arrow is now mathematically exact under finite-index factor hypotheses. The second is conditionally explicit. The third and fourth remain the mass-gap problem.

## Stopping condition

The cosmic/index programme becomes explanatory only when all of the following are supplied:

1. a canonically selected finite-index sector or Q-system and its standard minimal expectation;
2. a physical decision between the additive weld (IC12) and multiplicative weld (IC14), plus a natural composition-preserving map proving the chosen generator equality rather than fitting it;
3. a unique wall rung or stopping rule determined without glueball, BAO, or CMB scale fitting;
4. an absolute normalization section such as an independently derived birth capacity or proper duration;
5. a constructed map from the whole inclusion data to a complex vacuum-reduced Yang--Mills tangent carrier;
6. a regulator-uniform lower-frame or coercivity estimate on every neutral nonvacuum direction;
7. an energy comparison and Poincare reconstruction that turn that response into a mass floor; and
8. a controlled limit in which gravity and cosmology decouple while the positive pure-Yang--Mills coefficient and observable net survive.

Failure at item 2 leaves numerology. Failure at item 4 leaves only ratios. Failure at items 5--7 leaves an entropy/index construction rather than a mass-gap theorem.

Primary sources: [[library/a-note-on-continuous-entropy/inq|Longo and Witten on the optimal log-index entropy bound and dual identity]], [[library/minimum-index-for-subfactors-and-entropy-ii/inq|Hiai on minimum index and inclusion entropy]], [[library/quantum-complementarity-through-entropic-certainty-principles/inq|Magan and Pontello on entropic certainty]], [[library/on-relative-entropy-and-global-index/inq|Xu on relative-entropy duality and global index]], and [[library/relative-entropy-and-subalgebra-index/inq|Gao, Junge, and LaRacuente on subalgebra relative-entropy capacity]].

[[contemporary-puzzles/yang-mills-mass-gap/receipts/two-sided-index-capacity-receipt.py|The finite receipt]] and its [[contemporary-puzzles/yang-mills-mass-gap/receipts/two-sided-index-capacity-receipt-output.txt|stored output]] check the half-index/full-index distinction, exhibit ancillary-carrier dependence, and illustrate the declared scalar ladder and rate-quotient arithmetic. They do not prove either finite supremum, test Connes fusion or the Type-III theorem, construct the physical weld or wall selection, supply a common carrier, or establish any Yang--Mills estimate.

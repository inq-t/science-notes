# Octonionic Clifford Completion of the Color Normal

The factor \(8\) in the exceptional color metric is not a free normalization and not merely a recurrence of a favored numeral. Selecting a complex direction \(u\in S^6=G_2/SU(3)\) first derives color as its stabilizer and the minimal carrier \(T_uS^6\cong(\mathbb C^3)_{\mathbb R}\); its Hilbert--Schmidt holonomy response is already exactly Wilson's fundamental plaquette response up to a fixed factor. For the same derived color \(SU(3)\), the 149-dimensional flag normal and the 24-dimensional Jordan-frame tangent then obey the exact stable representation identity
\[
N_{\mathrm{def}}\oplus\mathbb R^{43}
\cong
8\,T_{\mathrm{fr}}
\cong
24\,\mathbb O .
\]
The selected complex slice \(\mathbb C_u\subset\mathbb O\) has a six-dimensional orthogonal complement \(W\cong(\mathbb C^3)_{\mathbb R}\), and left octonion multiplication makes \(\mathbb O\) the irreducible ordinary real module of \(\mathrm{Cl}_{0,6}\). Thus the stabilized normal is exactly twenty-four copies of a module for the Clifford algebra representing Brauer--Wall degree six, while differentiation of the stable character gives \(b_N=8(-B_{\mathfrak{su}(3)})\). This puts the slice torsor, Wilson character, trace-metric eight, octonionic triality, and a degree-six Clifford residue on one carrier. It does **not** derive a connection from a slice choice, identify multiplication by eight in a representation ring with Bott's invertible degree-eight shift, supply a complete graded real spectral cycle, construct Connes' finite spectral triple, or prove a Yang--Mills mass gap.

**Status: [EXACT CITED] for \(S^6=G_2/SU(3)\), its principal-bundle structure, \(\mathbb O=\mathbb C\oplus\mathbb C^3\), the color action, and the \(\operatorname{Spin}(8)\) triality tangent; [EXACT] for the minimal Wilson response, stable color-representation identity, ordinary Clifford action, trace-form consequence, and Morita no-go; [PROPOSED READING] for the class-six complement as the algebraic residue of complex descent; [OPEN] for a derived connection, nontrivial four-dimensional bundle sectors, a compatible graded real cycle, an \(H\)-equivariant bundle lift, a finite spectral triple, a physical response carrier, interacting-vacuum coercivity, and continuum reconstruction.**

## One color subgroup acts on both carriers

Choose a unit imaginary octonion \(u\) and write

\[
\mathbb C_u:=\operatorname{span}_{\mathbb R}\{1,u\},
\qquad
W:=\mathbb C_u^\perp .
\tag{OC1}
\]

The color group selected by the exceptional complex flag is

\[
SU(3)_{\mathrm c}
=
\operatorname{Aut}(\mathbb O;u).
\tag{OC2}
\]

The construction used in [[library/standard-model-from-exceptional-jordan-algebra/inq|the exceptional-Jordan source]] gives the orthogonal real \(SU(3)_{\mathrm c}\)-module decomposition

\[
\mathbb O
\cong
\mathbb C_u\oplus\mathbb C^3
\cong
\mathbb R^2\oplus W,
\qquad
W\cong(\mathbb C^3)_{\mathbb R}.
\tag{OC3}
\]

The group is trivial on \(\mathbb C_u\) and fundamental on \(\mathbb C^3\). If \(g\in SU(3)_{\mathrm c}\), then

\[
\chi_W(g)
=
\operatorname{tr}_{\mathbb R}g|_W
=
2\operatorname{Re}\operatorname{tr}_{\mathbf3}g.
\tag{OC4}
\]

Let

\[
T_{\mathrm{fr}}
:=
T(F_4/\operatorname{Spin}(8))
\tag{OC5}
\]

at the standard ordered Jordan frame. Triality identifies its three off-diagonal Peirce slots with

\[
T_{\mathrm{fr}}
\cong
\mathbb O_v\oplus\mathbb O_s\oplus\mathbb O_c .
\tag{OC6}
\]

The same color subgroup acts by octonion automorphisms on all three matrix entries while fixing the diagonal frame. Therefore

\[
\left.T_{\mathrm{fr}}\right|_{SU(3)_{\mathrm c}}
\cong
\mathbb R^6\oplus3W,
\qquad
\chi_{T_{\mathrm{fr}}}=6+3\chi_W .
\tag{OC7}
\]

This is the precise common-carrier statement. The color \(SU(3)\) appearing here is not a second isomorphic group chosen after the fact.

## The slice torsor already carries the minimal Wilson representation

The same selection has an exact homogeneous-space form. Fixing a reference unit
imaginary octonion \(u_0\),

\[
\pi:G_2\longrightarrow S^6,
\qquad
\pi(g)=g(u_0),
\qquad
S^6\cong G_2/SU(3)_{\mathrm c}
\tag{OC7a}
\]

is a principal \(SU(3)_{\mathrm c}\)-bundle. Its isotropy representation is precisely
the real color module \(W\), so

\[
T S^6
\cong
G_2\times_{SU(3)_{\mathrm c}}W,
\qquad
W=T_{u_0}S^6\cong(\mathbb C^3)_{\mathbb R}.
\tag{OC7b}
\]

[[inbox/causal-grain-cmb-spectroscopy/s6-positivity-integrability-duality|The (S^6) slice note]] keeps this homogeneous choice space distinct from a complex atlas on the manifold. [Gyenge's explicit transition-function calculation](https://sigma-journal.com/2019/078/) further identifies this fibration with a generator of \(\pi_5(SU(3))\).

This is a particularly economical Copernican order of explanation:

\[
\boxed{
\text{choice of local complex direction }u
\longrightarrow
\text{stabilizer }SU(3)_{\mathrm c}
\longrightarrow
\text{color carrier }T_uS^6 .}
\tag{OC7c}
\]

No symmetry is broken in this statement. The whole \(G_2\)-family contains all
complex directions; the symmetry observed in one presentation is the automorphism
group of the selected direction.

If \(s:X\to S^6\) is a field of slice choices on some base \(X\), its local
presentations form the pullback torsor

\[
P_s:=s^*G_2\longrightarrow X .
\tag{OC7d}
\]

Local lifts of \(s\) differ by \(SU(3)_{\mathrm c}\)-valued transition functions.
Thus the selection derives the allowed gauge-coordinate changes and the associated
bundle

\[
E_W=P_s\times_{SU(3)_{\mathrm c}}W
\cong s^*TS^6 .
\tag{OC7e}
\]

It does **not** derive a connection. A connection on \(P_s\), or an equivalent
rule for comparing neighboring presentations, is additional data. Once such a
comparison gives plaquette holonomies \(U_p\in SU(3)_{\mathrm c}\), however, the
Hilbert--Schmidt response of the tangent carrier is already exactly Wilson's
fundamental response. With

\[
Q_W^{\mathrm{Wilson}}(U)
:=
\sum_p\left(1-\frac13
\operatorname{Re}\operatorname{tr}_{\mathbf3}U_p\right),
\tag{OC7f}
\]

equation (OC4) gives

\[
\begin{aligned}
Q_{S^6}(U)
&:=
\sum_p\left\|\rho_W(U_p)-I_W\right\|_{\mathrm{HS}}^2\\
&=
\sum_p2\bigl(6-\chi_W(U_p)\bigr)\\
&=
12Q_W^{\mathrm{Wilson}}(U).
\end{aligned}
\tag{OC7g}
\]

Consequently \((\beta_{S^6}/2)Q_{S^6}\) is the Wilson plaquette action with
\(\beta_W=6\beta_{S^6}\). The three nested carriers then obey the exact finite-holonomy identities

\[
\boxed{
Q_{T_{\mathrm{fr}}}
=3Q_{S^6}
=36Q_W^{\mathrm{Wilson}},
\qquad
Q_N
=24Q_{S^6}
=8Q_{T_{\mathrm{fr}}}
=288Q_W^{\mathrm{Wilson}}.}
\tag{OC7h}
\]

Their infinitesimal metrics express the same ladder. In the normalization of
(OC21)--(OC24),

\[
b_{S^6}
=\frac13(-B_{\mathfrak{su}(3)}),
\qquad
b_{T_{\mathrm{fr}}}
=-B_{\mathfrak{su}(3)},
\qquad
b_N
=8(-B_{\mathfrak{su}(3)}).
\tag{OC7i}
\]

Thus the trace-metric eight is not a primitive property of color: it is the
normal quotient's multiplicity relative to the triality carrier, while the
triality carrier is three copies of the minimal slice tangent. This also shows
why the corresponding Casimir number is not an absolute energy scale. Changing
the declared response carrier changes the trace metric and is compensated by the
coefficient of the physical kinetic form.

Two firewalls prevent overreading this result. First, the principal bundle
\(G_2\to S^6\) is not the universal \(SU(3)\)-bundle. It represents a generator
of \(\pi_5(SU(3))\); for a four-dimensional CW base every map to the
five-connected sphere \(S^6\) is null-homotopic, so a pullback of this one bundle
is topologically trivial. In particular, a slice field alone does not recover
the nonzero instanton sectors seen after compactifying \(\mathbb R^4\) to
\(S^4\). Second, none of (OC7a)--(OC7i) uses an integrable complex structure on
the manifold \(S^6\). It uses the standard homogeneous sphere of octonionic
complex **choices** and its isotropy representation. The canonical octonionic
almost-complex structure is nonintegrable, while the established integrable
complex structures on the same smooth sphere are different geometries; the two
must not be silently identified.

## The flag normal is eight stable triality tangents

[[exceptional-normal-holonomy-and-the-residual-gauge-form]] derives

\[
\left.(N_{\mathrm{def}})_{\mathbb C}\right|_{SU(3)_{\mathrm c}}
\cong
5\mathbf1\oplus24\mathbf3\oplus24\bar{\mathbf3}.
\tag{OC8}
\]

The quotient that produces the number \(24\) can be read before any trace is taken. Color fixes
\(B=\mathfrak h_3(\mathbb C)\) pointwise, while

\[
B^\perp\cong M_3(\mathbb C)\cong3W
\tag{OC8a}
\]

as real color modules. The full defining-data tangent and the flag-orbit tangent therefore restrict as

\[
\begin{aligned}
V_f
&=J\oplus\operatorname{Hom}(B,B^\perp)
\cong
\mathbb R^9\oplus30W,\\
T_f(F_4/H)
&\cong
\mathbb R^4\oplus6W.
\end{aligned}
\tag{OC8b}
\]

The first coefficient is
\(30=3(1+\dim_{\mathbb R}B)=3\cdot10\): one copy of \(B^\perp\) lies in \(J\), and nine more lie in \(\operatorname{Hom}(B,B^\perp)\). The orbit consumes \(6W=2B^\perp\). Compactness makes the real quotient split, so

\[
N_{\mathrm{def}}
\cong
\mathbb R^5\oplus(30-6)W
=
\mathbb R^5\oplus24W.
\tag{OC8c}
\]

Since the color-active part of \(T_{\mathrm{fr}}\) is \(3W=B^\perp\), the augmentation classes already obey

\[
\begin{aligned}
[V_f]_0&=10[T_{\mathrm{fr}}]_0,\\
[T_f(F_4/H)]_0&=2[T_{\mathrm{fr}}]_0,\\
[N_{\mathrm{def}}]_0&=(10-2)[T_{\mathrm{fr}}]_0.
\end{aligned}
\tag{OC8d}
\]

Thus the eight is literally a normal-quotient residue: ten color-active triality blocks in the defining-data ambient carrier minus two presentation-orbit blocks. Since \(\dim_{\mathbb R}B=9\),

\[
10-2
=
\dim_{\mathbb R}B-1
=
\dim_{\mathbb R}B_0
=
8,
\qquad
B_0:=\{b\in B:\operatorname{tr}b=0\}.
\tag{OC8e}
\]

At the color-isotypic level,
\[
(N_{\mathrm{def}})_{\mathrm{active}}
\cong
8B^\perp .
\tag{OC8f}
\]
This makes a precise proposed reading available: the metric coefficient counts the traceless distinction directions of the selected local qutrit algebra after presentation-orbit directions are quotiented out. It does **not** yet give a canonical full-\(H\) identification
\(N_{\mathrm{active}}\cong B_0\otimes B^\perp\); the equality presently proved is the color-restricted representation and index statement.

Equivalently, because \(\mathbf3\) is not self-conjugate, the paired complex summands in (OC8) are the complexification of \(W\). As a real color representation,

\[
\left.N_{\mathrm{def}}\right|_{SU(3)_{\mathrm c}}
\cong
\mathbb R^5\oplus24W,
\qquad
\chi_N=5+24\chi_W .
\tag{OC9}
\]

Now compare (OC7) and (OC9):

\[
\chi_N+43
=
48+24\chi_W
=
8(6+3\chi_W)
=
8\chi_{T_{\mathrm{fr}}}.
\tag{OC10}
\]

Real representations of a compact group are determined by their characters. Therefore

\[
\boxed{
N_{\mathrm{def}}\oplus\mathbb R^{43}
\cong
8\,T_{\mathrm{fr}}
\cong
24\,\mathbb O
}
\qquad
\text{as real }SU(3)_{\mathrm c}\text{-modules}.
\tag{OC11}
\]

Equivalently, in the augmentation ideal of
\(RO(SU(3))=KO^0_{SU(3)}(\mathrm{pt})\),

\[
\boxed{
[N_{\mathrm{def}}]-149[\mathbf1]
=
8\bigl([T_{\mathrm{fr}}]-24[\mathbf1]\bigr)
=
24\bigl([W]-6[\mathbf1]\bigr).
}
\tag{OC12}
\]

The number \(43\) carries no proposed physics. It is the exact trivial-representation deficit: twenty-four copies of \(\mathbb O=\mathbb R^2\oplus W\) require forty-eight color singlets, whereas \(N_{\mathrm{def}}\) contains five. The equality is stable and color-restricted; it is not an isomorphism of full \(H=S(U(2)\times U(3))\)-modules.

## The selected complement is a class-six Clifford carrier

The orthogonal complement \(W\) consists of imaginary octonions. For \(w\in W\), define an operator on \(\mathbb O\) by left multiplication,

\[
c(w):=L_w,
\qquad
L_wx:=wx.
\tag{OC13}
\]

Alternativity gives

\[
L_w^2x=w(wx)=(w^2)x=-\lVert w\rVert^2x.
\tag{OC14}
\]

Polarizing (OC14) yields

\[
c(w)c(z)+c(z)c(w)
=
-2\langle w,z\rangle I .
\tag{OC15}
\]

The universal property of the Clifford algebra therefore produces

\[
c:\mathrm{Cl}_{0,6}\longrightarrow
\operatorname{End}_{\mathbb R}(\mathbb O).
\tag{OC16}
\]

Since \(\mathrm{Cl}_{0,6}\cong M_8(\mathbb R)\), both sides have real dimension \(64\), and the unital map is an isomorphism. Moreover, for \(g\in SU(3)_{\mathrm c}\),

\[
gL_wg^{-1}=L_{gw},
\tag{OC17}
\]

so this is an equivariant Clifford action. The octonion is not merely an eight-dimensional vector space in this comparison: it is the irreducible real spinor module of the six-dimensional color-bearing complement.

Combining (OC11) and (OC16) gives an exact **Clifford completion**:

\[
\boxed{
N_{\mathrm{def}}\oplus\mathbb R^{43}
\cong
\mathbb O^{\oplus24}
}
\tag{OC18}
\]

with an \(SU(3)_{\mathrm c}\)-equivariant ordinary \(\mathrm{Cl}_{0,6}\)-module structure on the stabilized carrier. No such unital action exists on \(N_{\mathrm{def}}\) itself: every \(M_8(\mathbb R)\)-module has real dimension divisible by eight, while \(149\) is not.

The word **ordinary** is load-bearing. The eight-dimensional irreducible module above has not been supplied with a real \(\mathbb Z/2\)-grading on which every \(w\in W\) acts oddly. A graded Clifford module, and still more a real spectral triple with operators \((J,D,\gamma)\), requires additional carrier data. The construction proves which graded algebra class is present and gives an ungraded spinor representation of it; it does not silently manufacture the KO-cycle.

Complexification does supply a canonical partial sign-table witness. On

\[
\mathcal H_{\mathbb O}:=\mathbb O\otimes_{\mathbb R}\mathbb C
\tag{OC18a}
\]

put

\[
\gamma_u:=iL_u,
\qquad
J_0(x\otimes z):=x\otimes\bar z.
\tag{OC18b}
\]

Because \(L_u^*=-L_u\) and \(L_u^2=-I\),
\(\gamma_u^*=\gamma_u\) and \(\gamma_u^2=I\). The Clifford generators \(L_w\), \(w\in W\), anticommute with \(\gamma_u\), while the color action commutes with it. Moreover,

\[
J_0^2=I,
\qquad
J_0\gamma_u=-\gamma_uJ_0.
\tag{OC18c}
\]

These are exactly the \((\varepsilon,\varepsilon'')=(+,-)\) signs of KO-degree \(6\). Up to interchanging the signs of \(\gamma_u\), its chiral color spaces are

\[
\mathcal H_{\mathbb O}^+
\cong\mathbf1\oplus\mathbf3,
\qquad
\mathcal H_{\mathbb O}^-
\cong\mathbf1\oplus\bar{\mathbf3},
\tag{OC18d}
\]

and \(J_0\) exchanges them. This is stronger than a dimension count: the selected complex orientation produces the grading operator and the class-six real-structure signs on the same color carrier. It remains only a **partial** KO witness. No physical finite algebra, Dirac operator, order-one condition, Pfaffian, or fermion multiplicity has been constructed, so the missing sign \(JD=\varepsilon'DJ\) and the spectral content cannot be declared.

There is also an exact Brauer--Wall statement. Orthogonal sums become graded tensor products,

\[
\mathrm{Cl}_{0,8}
\cong
\mathrm{Cl}_{0,2}\,\widehat\otimes\,\mathrm{Cl}_{0,6},
\tag{OC19}
\]

so in \(\mathrm{BW}(\mathbb R)\cong\mathbb Z/8\),

\[
0=2+6\pmod 8.
\tag{OC20}
\]

In the Euclidean convention of [[ko-dimension-as-morita-class/inq|KO-dimension as a graded Morita class]], choosing the real two-plane \(\mathbb C_u\) inside the period-eight octonionic whole leaves a real six-plane whose Clifford algebra has the complementary class \(6\). This makes “six as the residue of selecting the complex face of eight” exact at the Clifford level. It does not yet identify that residue with the KO-dimension of the finite noncommutative Standard-Model geometry: no algebra representation, \(D\), \(J\), grading, Pfaffian condition, or fermion carrier has been derived here.

## Differentiating the stable identity explains the Killing factor

For anti-Hermitian generators \(X_a=it_a\) normalized by

\[
\operatorname{tr}_{\mathbf3}(t_at_b)=\frac12\delta_{ab},
\tag{OC21}
\]

the realification \(W=(\mathbb C^3)_{\mathbb R}\) contributes

\[
\operatorname{Tr}_W
\bigl(\mathrm d\rho(X_a)^*\mathrm d\rho(X_b)\bigr)
=
\delta_{ab}.
\tag{OC22}
\]

The six trivial directions in (OC7) contribute nothing, so

\[
b_{T_{\mathrm{fr}}}(X_a,X_b)
=
3\delta_{ab}
=
-B_{\mathfrak{su}(3)}(X_a,X_b).
\tag{OC23}
\]

Likewise (OC9) gives \(b_N(X_a,X_b)=24\delta_{ab}\). Thus (OC11) differentiates to

\[
\boxed{
b_N
=
8b_{T_{\mathrm{fr}}}
=
8\bigl(-B_{\mathfrak{su}(3)}\bigr).
}
\tag{OC24}
\]

The trace-metric eight is therefore the ratio of the color-active stable representation classes:

\[
8
=
\frac{24\,W}{3\,W}
=
\frac{I_{SU(3)}(N_{\mathrm{def}})}
       {I_{SU(3)}(T_{\mathrm{fr}})}.
\tag{OC25}
\]

This is stronger than observing \(24=3\cdot8\). The numerator and denominator are traces of the same Lie-algebra action on two carriers derived from the same exceptional Jordan whole.

It still does not supply an energy. Rescaling a configuration-space metric rescales its Laplacian inversely, while the electric kinetic coefficient rescales reciprocally. The physical invariant is their dimensionful product after the state, clock, and continuum normalization have been fixed.

## The two eights remain different operations

The stable identity uses multiplication by the integer

\[
8\cdot:
RO(SU(3))\longrightarrow RO(SU(3)),
\qquad
[V]\longmapsto[V^{\oplus8}],
\tag{OC26}
\]

without changing degree. Bott periodicity instead uses an invertible class of degree eight to give

\[
KO^q_G(X)\xrightarrow{\ \cong\ }KO^{q+8}_G(X).
\tag{OC27}
\]

These cannot be identified. Multiplication by \(8\) is not invertible even on
\(KO^0(\mathrm{pt})\cong\mathbb Z\), whereas the Bott shift is an isomorphism. At the Clifford-algebra level the distinction is visible in

\[
\mathrm{Cl}_{0,n+8}
\cong
\mathrm{Cl}_{0,n}\otimes M_{16}(\mathbb R):
\tag{OC28}
\]

the Morita class repeats while the matrix size changes.

Nor is a Brauer--Wall degree the same type as a numerical KO charge. At a point,

\[
KO^{-6}(\mathrm{pt})=0,
\qquad
KO^{-8}(\mathrm{pt})\cong\mathbb Z.
\tag{OC28a}
\]

Thus the class-six Clifford algebra in (OC16) cannot emit an integer \(8\) through a degree-six point index. An integer appears only after a full degree-eight Thom or symbol construction has supplied the corresponding KO class.

The Atiyah--Bott--Shapiro construction also identifies exactly what the ordinary color character forgets. Let \(V,S^+,S^-\) be the three eight-dimensional \(\operatorname{Spin}(8)\) triality modules. The Bott symbol retains the graded Clifford-multiplication map

\[
c(v):S^+\longrightarrow S^-,
\qquad
v\in V.
\tag{OC28b}
\]

On restriction to the same color subgroup,

\[
V|_{SU(3)}
\cong
S^+|_{SU(3)}
\cong
S^-|_{SU(3)}
\cong
\mathbb O|_{SU(3)}.
\tag{OC28c}
\]

The ungraded color character therefore cannot distinguish \(S^+\) from \(S^-\): it forgets the oriented difference carried by the Bott symbol. The positive trace metric instead adds squared actions and is insensitive to that grading. This is the Clifford version of the programme's phase/modulus firewall. Triality supplies a common upstream object for Bott periodicity and the Killing metric, but the two descendants retain different information.

This yields a useful no-go theorem:

> **Morita trace-scale no-go.** No graded Morita class by itself determines a representation-trace normalization. Stabilizing a representative or taking \(m\) copies preserves its Morita class but multiplies the trace form by \(m\).

So \(\mathrm{BW}(\mathbb R)\cong\mathbb Z/8\) cannot, by itself, force the coefficient in (OC24). The coefficient is fixed here only because the exceptional construction supplies more than a Morita class: it supplies the particular color representation \(N_{\mathrm{def}}\), the triality tangent \(T_{\mathrm{fr}}\), and the stable intertwining relation (OC11). A true Bott-to-normal bridge must lift that abstract color isomorphism to an \(SU(3)\)-equivariant graded Clifford symbol or \(KKO\)-class and then state the separate pairing that returns the trace form.

## The next bridge is sharply typed

The exact triangle is

\[
\boxed{
\begin{array}{c}
\mathbb O=\mathbb C_u\oplus W,\quad
\mathrm{Cl}(W)\cong\operatorname{End}_{\mathbb R}(\mathbb O)
\\[3pt]
\Downarrow
\\[3pt]
T_{\mathrm{fr}}|_{SU(3)}
=3\mathbb O,
\qquad
N_{\mathrm{def}}\oplus\mathbb R^{43}
=24\mathbb O
\\[3pt]
\Downarrow
\\[3pt]
b_N=8(-B_{\mathfrak{su}(3)}).
\end{array}}
\tag{OC29}
\]

To turn this into a physical theorem one must still:

1. lift the color-restricted stable isomorphism to a natural bundle or correspondence over the oriented-flag field, rather than choose an abstract character isomorphism;
2. determine whether the Clifford action extends compatibly to the full residual group \(H\), or prove that a dynamical color projection is forced;
3. construct the first-order operator, real structure, grading, state, and restriction system needed for an actual KO-dimension-six spectral cycle;
4. compare the resulting field-valued Clifford response with the Wilson electric form on the complete interacting-vacuum complement; and
5. transport a regulator-uniform positive product through OS and Poincare reconstruction.

The stopping condition has consequently improved. A future claim that Bott periodicity “explains the \(8\)” must recover (OC11) or a stronger natural intertwiner, not merely repeat the numeral. A future claim that the class-six residue explains matter must build the spectral cycle, not merely count the six discarded real directions. A future mass-gap claim must still prove the interacting and continuum coercivity that neither stable representation theory nor Clifford periodicity contains.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/exceptional_normal_holonomy_receipt.py|The exceptional-normal receipt]] checks the real multiplicity and stable-character arithmetic in (OC7)--(OC12), together with (OC24). [[contemporary-puzzles/yang-mills-mass-gap/receipts/exceptional-normal-holonomy-receipt-output.txt|Its stored output]] records the passing run. The Clifford relations (OC14)--(OC17) are the direct alternativity proof above; the receipt does not promote the resulting stable module to a physical field carrier.

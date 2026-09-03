# The Octonionic Slice Groupoid and the Orientation Torsor

The ordinary orbit set of octonionic complex directions is a point, but the corresponding differentiable quotient stack is not: for \(S^6=G_2/SU(3)\), the transitive action groupoid presents \([S^6/G_2]\simeq\mathbf B SU(3)\). This is the precise category in which a selected complex direction is an origin for relational symmetry rather than a location in a prior space. The stack retains the stabilizer, all twisted \(SU(3)\)-torsors, and the universal associated color carrier \(W=(\mathbb C^3)_{\mathbb R}\); its free-path transgression gives the standard unconstrained link-configuration groupoid \(SU(3)^E\mathbin{/\mkern-6mu/}SU(3)^V\) on a fixed graph. The homogeneous presentation also carries one canonical \(G_2\)-invariant characteristic connection with full \(SU(3)\) holonomy, but it does not generate the arbitrary four-dimensional connections or quantum measure of Yang--Mills theory. Passing from oriented directions \(S^6\) to unoriented complex subalgebras \(\mathbb RP^6\) extends the stabilizer by a reversal \(\mathbb Z_2\); an \(SU(3)\)-reduction is then exactly a choice of handed origin in the resulting double-cover torsor. The internal Clifford grading changes sign under this reversal, whereas the Wilson and Killing responses descend because they are even. This derives a rigorous common grammar for origin, torsor, orientation, connection, and color, but it does not yet derive weak chirality, a physical scale, or a Yang--Mills mass gap.

**Status: [EXACT] for the transitive-groupoid equivalence, torsor classification, free-path lattice transgression, associated tangent and Clifford carriers, invariant-connection uniqueness and holonomy, orientation-reduction obstruction, and Wilson character; [EXACT CITED] for the \(G_2\to S^6\) transition function and the canonical nearly Kähler connection; [PROPOSED INTERPRETATION] for a selected orientation as the structural origin of an observed symmetry; [OPEN] for a dynamically selected reduction, arbitrary four-dimensional continuum gauge configurations, the Yang--Mills state, the Standard Model chiral bimodule, anomaly cancellation, interacting-vacuum coercivity, continuum reconstruction, and dimensional calibration.**

## The coarse quotient commits the category error

Fix a unit imaginary octonion \(u_0\), and put

\[
H_{\mathrm c}:=\operatorname{Aut}(\mathbb O;u_0)\cong SU(3).
\tag{SG1}
\]

The \(G_2=\operatorname{Aut}(\mathbb O)\) action on unit imaginary octonions is
transitive, so

\[
S^6\cong G_2/H_{\mathrm c}.
\tag{SG2}
\]

If one takes only the coarse orbit set, then

\[
S^6/G_2=\{*\}.
\tag{SG3}
\]

That point has forgotten the very symmetry the construction is meant to explain.
The action groupoid retains it:

\[
G_2\ltimes S^6
=
\bigl(G_2\times S^6\rightrightarrows S^6\bigr).
\tag{SG4}
\]

The full subgroupoid on the one object \(u_0\) has arrow group exactly
\(H_{\mathrm c}\).
Its inclusion into (SG4) is fully faithful, and it is essentially surjective
because every \(u\in S^6\) is \(g(u_0)\) for some \(g\in G_2\). Therefore the
two Lie groupoids are Morita equivalent, and their differentiable quotient
stacks obey

\[
\boxed{
[S^6/G_2]
\simeq
\mathbf B H_{\mathrm c}
=
\mathbf B SU(3).}
\tag{SG5}
\]

The displayed equivalence uses the reference object \(u_0\); another reference
changes it by conjugacy and a natural 2-isomorphism, not by new physical data.
This is the standard Morita-invariant notion of a differentiable stack used by
[[library/differentiable-stacks-and-gerbes/inq|Behrend and Xu]].

This is not the numerical observation that \(SU(3)\) happens to stabilize one
octonion. It is an equivalence of moduli problems. The left side presents a
covariant whole of complex directions and comparison arrows; the right side
presents color torsors.

In the language of [[basic-concepts/groupoids/inq|groupoids]] and
[[basic-concepts/stacks/inq|stacks]], the Copernican correction is

\[
\boxed{
\text{coarse quotient }S^6/G_2=*
\quad\rightsquigarrow\quad
\text{structural quotient }[S^6/G_2]\simeq\mathbf B SU(3).}
\tag{SG6}
\]

The coarse quotient remembers only that every presentation is equivalent. The
stack remembers the arrows, their composition, and the automorphisms of each
presentation. Symmetry is precisely that retained isotropy.

## A point of the stack is a color torsor

For a test manifold or suitable base \(X\), (SG5) gives an equivalence of
groupoids

\[
\boxed{
\operatorname{Map}\bigl(X,[S^6/G_2]\bigr)
\simeq
\operatorname{Bun}_{SU(3)}(X).}
\tag{SG7}
\]

A map to the quotient stack may be described as a principal \(G_2\)-bundle
together with a \(G_2\)-equivariant map to \(S^6\), equivalently a reduction of
that bundle to \(H_{\mathrm c}\). Under (SG5), this is simply an arbitrary principal
\(SU(3)\)-bundle. Local complex directions and their comparison arrows are not
extra decoration on the torsor; they are another presentation of the same
descent datum.

This resolves an important false no-go. A literal global field

\[
s:X\longrightarrow S^6
\tag{SG8}
\]

inside one fixed trivial \(G_2\)-background produces only the special pullback
\(s^*G_2\to X\). If \(X\) is a four-dimensional CW complex, \(s\) is
null-homotopic because \(S^6\) is five-connected, so this pullback is trivial.
That narrow model cannot recover nonzero instanton bundles on \(S^4\).

The stack-valued field in (SG7) is larger. It permits local slice presentations
whose transition arrows form nontrivial descent data, and it is equivalent to
the groupoid of **all** \(SU(3)\)-torsors, including nonzero second-Chern-class
sectors. The global map and the stack map are different types:

\[
\boxed{
X\to S^6
\quad\text{is a chosen global presentation, whereas}\quad
X\to[S^6/G_2]
\quad\text{is a possibly twisted color object}.}
\tag{SG9}
\]

[[library/transition-function-of-g2-over-s6/inq|Gyenge's transition-function calculation]]
shows that the particular bundle \(G_2\to S^6\) has clutching function generating
\(\pi_5(SU(3))\). Equation (SG7) does not claim that this one bundle is universal;
it says the *quotient stack of its transitive presentation* is the classifying
stack because twisting and descent have been retained.

## Free-path transgression gives the lattice gauge groupoid

Let \(\Gamma\) be a finite oriented graph, with one orientation chosen for each
unoriented edge, and let \(\mathcal P_\Gamma\) be the free path groupoid on those
generators. Write \(\mathbf B_{\mathrm{grp}}H_{\mathrm c}\) for the one-object
Lie groupoid presenting the differentiable stack
\(\mathbf B H_{\mathrm c}\). An ordinary functor

\[
\mathcal P_\Gamma\longrightarrow\mathbf B_{\mathrm{grp}}H_{\mathrm c}
\tag{SG9a}
\]

assigns an element \(U_e\in H_{\mathrm c}\) to every chosen edge and
\(U_{\bar e}=U_e^{-1}\) to its reverse. A natural isomorphism is a vertex
assignment \(k=(k_v)_{v\in V}\in H_{\mathrm c}^{V}\). With the transporter
convention used here, its action is

\[
(U\mathbin{\cdot}k)_e
=
k_{t(e)}^{-1}U_ek_{s(e)}.
\tag{SG9b}
\]

This is a right action. In the conventional natural-transformation notation
\(\eta:F\Rightarrow F'\), take \(\eta_v=k_v^{-1}\); naturality then reads
\(U'_e=\eta_{t(e)}U_e\eta_{s(e)}^{-1}\).

Consequently there is an isomorphism of groupoids

\[
\operatorname{Fun}(\mathcal P_\Gamma,\mathbf B_{\mathrm{grp}}H_{\mathrm c})
\cong
H_{\mathrm c}^{E}\mathbin{/\mkern-6mu/}H_{\mathrm c}^{V},
\tag{SG9c}
\]

where the right side is the action groupoid, not its coarse orbit space. The
isotropy inclusion \(\mathbf B_{\mathrm{grp}}H_{\mathrm c}\to
G_2\ltimes S^6\) is fully faithful and essentially surjective. Postcomposition
therefore induces an equivalence of these finite representation groupoids:

\[
\boxed{
\operatorname{Fun}
\bigl(\mathcal P_\Gamma,G_2\ltimes S^6\bigr)
\simeq
SU(3)^E\mathbin{/\mkern-6mu/}SU(3)^V.}
\tag{SG9d}
\]

Coordinate-free, the equivalent torsor presentation assigns an
\(H_{\mathrm c}\)-torsor \(P_v\) to every vertex and an equivariant transport
\(P_{s(e)}\to P_{t(e)}\) to every edge. Choosing one frame in each \(P_v\)
produces the coordinates \(U_e\in H_{\mathrm c}\); changing those frames gives
(SG9b). For connected \(\Gamma\), the diagonal center
\(Z(SU(3))\cong\mu_3\) acts trivially and remains as isotropy in the action
groupoid—it has not been silently divided out.

The left side assigns local octonionic slice presentations to vertices and
comparison arrows to edges. Choosing vertex lifts turns those comparisons into
the familiar link coordinates \(U_e\); changing the lifts gives exactly
(SG9b). Thus the lattice gauge law is the coordinate law of the transgressed
slice groupoid.

The word **free** is essential. If \(\Gamma\) is the one-skeleton of a
two-complex \(\Lambda\), write an oriented plaquette boundary in traversal order
as \(e_1^{\varepsilon_1}\cdots e_n^{\varepsilon_n}\), based at \(v\). The
functor evaluates it to

\[
U_p
=
U_{e_n}^{\varepsilon_n}\cdots U_{e_1}^{\varepsilon_1},
\qquad
U_p\longmapsto k_v^{-1}U_pk_v.
\tag{SG9e}
\]

Changing the chosen base vertex conjugates \(U_p\), while reversing the face
orientation sends it to \(U_p^{-1}\); the real Wilson character is insensitive
to both choices. For connected \(\Gamma\), spanning-tree gauge gives the
equivalent presentation
\(H_{mathrm c}^{E}\mathbin{/\mkern-6mu/}H_{mathrm c}^{V}simeq
\operatorname{Hom}(\pi_1\Gamma,H_{mathrm c})\mathbin{/\mkern-6mu/}H_{mathrm c}\).

No two-cell relation has been imposed, so \(U_p\) is not forced to be the
identity. Replacing \(\mathcal P_\Gamma\) by the fundamental groupoid of the
filled complex would instead impose flatness and erase the lattice curvature
that the Wilson response must measure.

As a local system on a one-complex this data is flat, but there is no
**face-flatness** constraint and noncontractible graph cycles may have arbitrary
holonomy. It is all unconstrained connection data on the fixed graph, not the
bundle classification of the filled complex: its higher cells and second-Chern
topology are absent. A continuum pair \((P,A)\) restricts to graph transport but
cannot be reconstructed from one such restriction. In the continuum, a nonflat
connection is encoded by transport on the **thin** path groupoid; the ordinary
fundamental groupoid retains only homotopy-invariant transport and would again
be too coarse. [[library/parallel-transport-and-functors/inq|Schreiber and
Waldorf]] give the corresponding smooth functor/descent characterization.

This is an exact finite-regulator kinematic statement. It does not turn the
homogeneous connection on \(S^6\) into independent link variables, choose a
probability law on \(SU(3)^E\), or construct a continuum connection.

## The symmetry group has an origin but the torsor does not

For \(x\in X\), the fibre \(P_x\) of a principal \(H_{\mathrm c}\)-bundle is an
[[basic-concepts/torsors/inq|\(H_{\mathrm c}\)-torsor]]. It has a canonical
difference map

\[
\delta:P_x\times P_x\longrightarrow H_{\mathrm c},
\qquad
p\,\delta(p,q)=q,
\tag{SG10}
\]

but no preferred point that could play the role of the identity. Choosing
\(p\in P_x\) identifies the fibre with \(H_{\mathrm c}\) by \(h\mapsto ph\);
changing \(p\)
changes that coordinate identification while leaving every relational
difference intact.

There is a second, structural meaning of origin. Before \(u_0\) is selected,
there is a family of conjugate stabilizers

\[
H_u:=\operatorname{Aut}(\mathbb O;u),
\qquad
u\in S^6,
\tag{SG11}
\]

and arrows \(g:u\to v\) identify them only by conjugation. Selecting an object
\(u\) chooses the presentation about which its automorphisms are measured:

\[
H_u=\operatorname{Aut}_{G_2\ltimes S^6}(u).
\tag{SG12}
\]

Thus the selected direction is an **origin of this stabilizer presentation**,
not an absolute point of prior physical space. Interpreting this as the origin
of observed color symmetry is the proposed physical step. Mathematically, the
symmetry group is the loop group at that object. Forgetting the object but
retaining the groupoid preserves that statement up to equivalence; collapsing
the groupoid to its orbit set does not.

## The universal tangent carrier is the fundamental color carrier

The isotropy representation of \(H_{\mathrm c}\) on the tangent at \(u_0\) is

\[
W:=T_{u_0}S^6
\cong
(\mathbb C^3)_{\mathbb R},
\qquad
\chi_W(U)=2\operatorname{Re}\operatorname{tr}_{\mathbf3}U.
\tag{SG13}
\]

Equivariantly,

\[
TS^6\cong G_2\times_{H_{\mathrm c}} W.
\tag{SG14}
\]

Under (SG5), this tangent bundle corresponds to the universal associated real
color bundle. For a color torsor \(P\to X\), the carrier is therefore

\[
E_W:=P\times_{H_{\mathrm c}} W.
\tag{SG15}
\]

This statement survives every topological sector. It does not require \(E_W\)
to be the pullback of \(TS^6\) along one global map \(X\to S^6\).

The Clifford operator globalizes on the homogeneous presentation as well. Use
\(\mathrm{Cl}^{-}(V)\) for the Clifford algebra with
\(v^2=-\lVert v\rVert^2\). For \(u\in S^6\) and
\(w\in T_uS^6\subset\operatorname{Im}\mathbb O\), define

\[
c_u(w):=L_w\in\operatorname{End}_{\mathbb R}(\mathbb O).
\tag{SG16}
\]

Alternativity gives

\[
c_u(w)c_u(z)+c_u(z)c_u(w)
=-2\langle w,z\rangle I,
\tag{SG17}
\]

and hence the smooth \(G_2\)-equivariant fibrewise isomorphism of ungraded
algebra bundles

\[
\boxed{
\mathrm{Cl}^{-}(TS^6)
\cong
S^6\times\operatorname{End}_{\mathbb R}(\mathbb O).}
\tag{SG18}
\]

The associated octonion bundle is trivial because the
\(H_{\mathrm c}\)-representation on \(\mathbb O\) extends to \(G_2\):

\[
G_2\times_{H_{\mathrm c}}\mathbb O
\xrightarrow{\ \cong\ }
S^6\times\mathbb O,
\qquad
[g,x]\longmapsto(g u_0,gx).
\tag{SG19}
\]

For \(U\in H_{\mathrm c}\), the Clifford and holonomy actions obey the exact
covariance
identity

\[
\rho_{\mathbb O}(U)c(w)\rho_{\mathbb O}(U)^{-1}
=
c\bigl(\rho_W(U)w\bigr),
\qquad
\rho_{\mathbb O}=\mathbf1_{\mathbb R^2}\oplus\rho_W.
\tag{SG20}
\]

Thus Clifford multiplication and color holonomy are compatible operations on
one carrier. Neither is being inferred from a matching dimension.

## The homogeneous geometry supplies one canonical connection

The bare classifying stack \(\mathbf B H_{\mathrm c}\) classifies torsors, not
connections. The
particular reductive homogeneous presentation nevertheless carries a canonical
one. With the \(H_{\mathrm c}\)-invariant orthogonal decomposition

\[
\mathfrak g_2=\mathfrak h\oplus\mathfrak m,
\qquad
\mathfrak h=\mathfrak{su}(3),
\qquad
\mathfrak m\cong W,
\tag{SG21}
\]

the \(\mathfrak h\)-component of the Maurer--Cartan form on \(G_2\) is a
principal connection on \(G_2\to S^6\):

\[
A_{\mathrm{can}}
:=
\operatorname{pr}_{\mathfrak h}(g^{-1}\mathrm dg).
\tag{SG22}
\]

By [[library/invariant-connections-over-a-principal-fibre-bundle/inq|Wang's
classification of invariant connections]],
invariant connections differ from this one by an element of
\(\operatorname{Hom}_{H_{\mathrm c}}(\mathfrak m,\mathfrak h)\). After
complexification,

\[
\mathfrak m_{\mathbb C}\cong\mathbf3\oplus\bar{\mathbf3},
\qquad
\mathfrak h_{\mathbb C}\cong\mathbf8,
\tag{SG23}
\]

so this Hom-space vanishes. The canonical connection is therefore the unique
\(G_2\)-invariant \(SU(3)\) connection on the homogeneous bundle.

For \(X,Y\in\mathfrak m\), its curvature at the reference point is

\[
F_{\mathrm{can}}(X,Y)
=
-[X,Y]_{\mathfrak h}.
\tag{SG24}
\]

The \(H_{\mathrm c}\)-equivariant bracket from
\(\mathbf3\otimes\bar{\mathbf3}\) has nonzero adjoint component and therefore
spans the irreducible \(\mathbf8\); zero image would make \(\mathfrak m\) a
proper ideal of the simple algebra \(\mathfrak g_2\). Ambrose--Singer then gives
restricted holonomy \(SU(3)\), and simple connectedness of \(S^6\) makes this
the full holonomy. In the standard nearly Kähler language this is the
torsionful characteristic \(SU(3)\)-instanton connection, not the
Levi--Civita connection and not an integrable-complex claim. It is written
explicitly by [[library/instantons-on-the-six-sphere-and-twistors/inq|Lechtenfeld
and Popov]].

This is a real derivation of **one** connection from the homogeneous whole. A
global slice field \(s:X\to S^6\) pulls it back to the composite connection
\(s^*A_{\mathrm{can}}\). Such fields remain topologically trivial on a
four-dimensional CW base and their pulled-back connections occupy a highly
constrained subset of all Yang--Mills connections. For an arbitrary torsor in
(SG7), a connection is still additional differential data, represented by a
lift from \(\mathbf B H_{\mathrm c}\) to a differential classifying object such
as \(\mathbf B_\nabla H_{\mathrm c}\).
The canonical homogeneous connection does not define the Yang--Mills path
measure or action coefficient on every color bundle.

## Its minimal holonomy response is exactly Wilson

Once either the canonical connection or an independently supplied color
connection gives plaquette holonomies \(U_p\), the invariant metric on \(W\)
defines

\[
\begin{aligned}
Q_W^{\mathrm{car}}(U)
&:=
\sum_p\|\rho_W(U_p)-I\|_{\mathrm{HS}}^2\\
&=
\sum_p2\bigl(6-\chi_W(U_p)\bigr)\\
&=
12\sum_p\left(1-\frac13
\operatorname{Re}\operatorname{tr}_{\mathbf3}U_p\right).
\end{aligned}
\tag{SG25}
\]

Therefore

\[
\boxed{
Q_W^{\mathrm{car}}=12Q_{\mathrm{fund}}^{\mathrm{Wilson}}.}
\tag{SG26}
\]

Here \(Q_{\mathrm{fund}}^{\mathrm{Wilson}}\) denotes the final sum in (SG25);
the subscript distinguishes the fundamental Wilson class function from the
carrier \(W\).

The same formula holds on the octonion carrier because its two extra real
directions are color singlets. [[octonionic-clifford-completion-of-the-color-normal]]
places this minimal response in the exact ladder

\[
Q_{T_{\mathrm{fr}}}
=3Q_W^{\mathrm{car}},
\qquad
Q_N
=24Q_W^{\mathrm{car}}
=8Q_{T_{\mathrm{fr}}}.
\tag{SG27}
\]

The groupoid construction therefore recovers the ordinary fundamental Wilson
class function on every color torsor once a connection and coupling are
supplied. The canonical homogeneous connection gives one distinguished
evaluation of this response. Neither result derives the arbitrary
continuum-connection configuration space, the bare coupling, or the interacting
vacuum measure.

Four operator types must remain distinct:

1. \(c_u(w)=L_w\) acts on the octonionic spinor fibre;
2. \(\rho_R(U_p)-I\) acts on a finite response fibre
   \(R=W,\mathbb O,T_{\mathrm{fr}},N\), and its Hilbert--Schmidt norm gives a
   plaquette class function;
3. multiplication by the resulting sum \(Q_R(U)\) acts on configuration
   wavefunctions; and
4. the electric Laplacian acts on those wavefunctions, with the trace metric
   from \(R\) fixing only its normalization.

After normalized Haar measure has been supplied, the gauge-invariant carrier is

\[
\mathcal H_\Gamma
:=
L^2(H_{\mathrm c}^{E},\mu_{\mathrm H}^{E})^{H_{\mathrm c}^{V}}.
\tag{SG27a}
\]

Because the graph is finite and \(H_{\mathrm c}\) is compact,
\(M_{Q_R}\) is bounded, positive, and self-adjoint. Let \(X_{e,a}\) denote the
left-invariant vector field on the \(e\)-th group factor generated by a basis
element of \(\mathfrak h\). The response trace metric \(b_R\) is
\(\operatorname{Ad}\)-invariant, so the summed Casimir preserves the
gauge-invariant subspace. On its smooth core, the electric operator is the
unbounded positive differential operator

\[
\begin{aligned}
(M_{Q_R}\psi)(U)
&=
Q_R(U)\psi(U),\\
\Delta_{\Gamma,b_R}
&=
-\sum_{e,a,b}(b_R^{-1})^{ab}X_{e,a}X_{e,b}.
\end{aligned}
\tag{SG27b}
\]

The finite Kogut--Susskind Hamiltonian has the typed form

\[
H_\Gamma
=
\kappa_a\Delta_{\Gamma,b_R}
+\lambda_aM_{Q_R},
\qquad
\kappa_a,\lambda_a>0,
\tag{SG27c}
\]

with dimensionful regulator coefficients. The electric Laplacian is essentially
self-adjoint on the smooth core. The Hamiltonian gap is a spectral property on
\(\mathcal H_\Gamma\); if a specified ground state is strictly positive, its
ground-state transform restates that gap as a weighted-vacuum coercivity
problem. It is not an eigenvalue of \(c_u(w)\), of \(\rho_R(U_p)-I\), or of the
finite normal Hessian.

## Handedness is a reduction of the unoriented torsor

The complex subalgebra depends only on the unoriented line:

\[
\mathbb C_u=\mathbb C_{-u}.
\tag{SG28}
\]

Let

\[
K_{\pm u}
:=
\operatorname{Stab}_{G_2}(\{u_0,-u_0\})
=
N_{G_2}(H_{\mathrm c}).
\tag{SG29}
\]

The last equality follows because the
\(H_{\mathrm c}\)-fixed subspace of \(\operatorname{Im}\mathbb O\) is the line
\(\mathbb R u_0\). Thus \(H_{\mathrm c}\) fixes the chosen orientation, while
the other component reverses it, and

\[
1\longrightarrow H_{\mathrm c}\longrightarrow K_{\pm u}
\longrightarrow\mathbb Z_2\longrightarrow1.
\tag{SG30}
\]

The oriented and unoriented homogeneous spaces form the double cover

\[
S^6=G_2/H_{\mathrm c}
\longrightarrow
G_2/K_{\pm u}\cong\mathbb RP^6.
\tag{SG31}
\]

At the structural quotient level this becomes

\[
\boxed{
[S^6/G_2]\simeq\mathbf B H_{\mathrm c}
\longrightarrow
[\mathbb RP^6/G_2]\simeq\mathbf B K_{\pm u}.}
\tag{SG32}
\]

The map is extension of structure group along
\(H_{\mathrm c}\hookrightarrow K_{\pm u}\). It forgets which
orientation-preserving reduction was chosen. For a \(K_{\pm u}\)-torsor
\(Q\to X\),

\[
Q/H_{\mathrm c}\longrightarrow X
\tag{SG33}
\]

is the associated \(\mathbb Z_2\)-torsor of handed origins. An
\(H_{\mathrm c}\)-reduction is equivalent to a section of (SG33). Its Čech
class

\[
w_1(\lambda_Q)\in H^1(X;\mathbb Z_2)
\tag{SG33a}
\]

is the obstruction to a global choice, where \(\lambda_Q\) is the associated
real sign line.

This makes “handedness as preferred origin” exact. The preference is not a
marked spatial location. It is a reduction from transformations that may reverse
the complex axis to transformations that preserve one chosen axis. If the
\(\mathbb Z_2\)-torsor is nontrivial, local handed choices cannot be glued. If it
is trivial, a sheet may be chosen, but neither the torsor nor the vanishing of
the obstruction says which sheet becomes factual.

## The internal grading is orientation-odd

Let

\[
\varepsilon:K_{\pm u}\longrightarrow\{\pm1\},
\qquad
ku_0=\varepsilon(k)u_0,
\tag{SG34a}
\]

be the orientation character. For the \(K_{\pm u}\)-torsor \(Q\to X\), form

\[
\mathcal H_Q
:=
Q\times_{K_{\pm u}}
\bigl(\mathbb O\otimes_{\mathbb R}\mathbb C_{\mathrm{ext}}\bigr),
\qquad
\lambda_Q
:=
Q\times_{K_{\pm u}}\mathbb R_{\varepsilon}.
\tag{SG34b}
\]

On an oriented local lift, define

\[
\mathcal H_{\mathbb O}
:=
\mathbb O\otimes_{\mathbb R}\mathbb C_{\mathrm{ext}},
\qquad
\gamma_u:=i_{\mathrm{ext}}L_u,
\qquad
J_0:=\operatorname{id}_{\mathbb O}\otimes\text{complex conjugation},
\qquad
P_\pm(u):=\frac{1\pm\gamma_u}{2}.
\tag{SG34}
\]

Then

\[
\gamma_{-u}=-\gamma_u,
\qquad
P_\pm(-u)=P_\mp(u),
\qquad
J_0\gamma_u=-\gamma_uJ_0,
\tag{SG35}
\]

and, up to which sign is named positive,

\[
P_+(u)\mathcal H_{\mathbb O}\cong\mathbf1\oplus\mathbf3,
\qquad
P_-(u)\mathcal H_{\mathbb O}\cong\mathbf1\oplus\bar{\mathbf3}.
\tag{SG36}
\]

The covariance law is

\[
\rho_{\mathbb O}(k)\gamma_{u_0}\rho_{\mathbb O}(k)^{-1}
=
\varepsilon(k)\gamma_{u_0}.
\tag{SG36a}
\]

Consequently the signed octonionic grading is not an ordinary endomorphism
field on the unoriented quotient. It descends as

\[
\Gamma\in
\Gamma\!\left(
\operatorname{End}_{\mathbb C}(\mathcal H_Q)
\otimes_{\mathbb R}\lambda_Q
\right),
\qquad
\Gamma^2=I,
\tag{SG37}
\]

where the square uses the canonical trivialization
\(\lambda_Q^{\otimes2}\cong\mathbb R\). Choosing an
\(H_{\mathrm c}\)-reduction trivializes \(\lambda_Q\) and turns the relative
distinction into the labels \(+/-\). The projectors \(P_\pm\) are not separately
global before that choice; reversal exchanges them.

The no-go is exact. A deck-invariant ordinary grading on the unoriented quotient
would pull back with
\(\gamma_{-u}=\gamma_u\), while (SG35) gives
\(\gamma_{-u}=-\gamma_u\). Since \(\gamma_u^2=1\), no such grading exists.

The even descendants

\[
\gamma_u^2,
\qquad
\|\rho_W(U)-I\|_{\mathrm{HS}}^2,
\qquad
b_W(X,Y)
=
\operatorname{Tr}_W\bigl(
\mathrm d\rho(X)^*\mathrm d\rho(Y)
\bigr)
\tag{SG38}
\]

survive the quotient because they are invariant under reversal. This is the
exact sense in which an observable can be a quotient **with retained
structure**: the stack remembers isotropy, the associated bundle remembers what
the symmetry acts on, and the invariant metric supplies a dimensionless scale
of relational difference. Passing all the way to the coarse orbit set destroys
those data.

The physical yardstick remains separate. Multiplying the invariant metric by a
positive constant changes the Casimir normalization and is compensated by the
kinetic coefficient. A dimensionless quotient metric does not yet define clock
energy or invariant mass.

## What this changes in the mass-gap programme

Within this construction, the Copernican reversal removes four conflations:

1. the \(SU(3)\) identified with color in this exceptional construction is the
   automorphism group of a selected complex presentation, not a primordial
   symmetry waiting to be broken;
2. the quotient stack, unlike the orbit set or a single global slice field,
   retains every color torsor and its topological sectors;
3. the homogeneous geometry derives one canonical full-holonomy connection
   without pretending to derive every Yang--Mills connection; and
4. the signed internal grading is a reduction/section problem for an orientation
   torsor, while the Wilson response is its orientation-even metric shadow.

It does not identify these outputs with a mass gap. The partial carrier in
(SG36) is balanced, and its \(\mathbf3/\bar{\mathbf3}\) split is color conjugacy,
not the observed weak left/right matter asymmetry. A physical chiral construction
still needs a finite algebra and bimodule, a complete real spectral cycle, a
justified representation-theoretic asymmetry on the independent fermions,
anomaly cancellation, and gauge-invariant experimental channels. A nonzero
total Fredholm index is one possible witness, not a necessary condition for a
real-doubled chiral theory. Because \(J_0\) exchanges
\(\mathbf1\oplus\mathbf3\) with \(\mathbf1\oplus\bar{\mathbf3}\), the present
pair may instead encode real or particle--antiparticle doubling. Its two halves
must not be counted directly as independent Weyl sectors in an anomaly trace,
and conjugate pairing here does not establish vectorlike anomaly cancellation.

The obstruction \(w_1(\lambda_Q)\) is degree-one orientation data.
Four-dimensional perturbative gauge anomalies are degree-six characteristic
data, while global anomalies require five-dimensional bordism or eta data.
The \(\mathbb Z_2\) cover in (SG30) therefore neither is nor cancels the Witten
\(SU(2)\) anomaly. Pure Yang--Mills has no fermionic matter.

Likewise, (SG26) recovers the Wilson regulator rather than solving it. The mass
gap still requires the interacting vacuum state, a regulator-uniform Poincare or
equivalent coercivity estimate on its complete gauge-invariant complement,
Osterwalder--Schrader continuum reconstruction, the Poincare Casimir, and an
independently normalized dimensional scale. The groupoid supplies the right
carrier category. It does not supply the missing positive lower edge.

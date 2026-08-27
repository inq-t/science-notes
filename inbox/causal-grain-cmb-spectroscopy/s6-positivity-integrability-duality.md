# The \(S^6\) Positivity--Integrability Duality

The six-sphere can organize a precise global/local duality, provided three nearby structures are not collapsed into one. The octonionic sphere \(S^6\cong G_2/SU(3)\) parametrizes choices of an imaginary unit and hence of a local associative complex slice \(\mathbb C_u\subset\mathbb O\). The exceptional Jordan cone supplies a positive order carrier, and a compatible one-sided semigroup turns that order into causal direction; a selected complex slice supplies the scalar and operator calculus of local noncommutative observables, while integrability is the further condition that such local complex data glue coherently. Connes' modular flow then contributes a distinguished algebraic time direction: not another coordinate inside the local object, but an automorphism flow of the state--algebra pair. The proposed causal grain is the primitive positive passage that selects and realizes one such local fiber from the symmetric whole.

## The meaning of the duality

The strongest charitable reading is not

$$
\text{positivity on }S^6
=
\text{complex integrability on }S^6.
$$

The two sides live on different carriers:

$$
\boxed{
\begin{aligned}
\text{global directedness}
&:\quad
\mathfrak h_3(\mathbb O)_+
\ \text{and its positive process cone},\\
\text{local complex presentation}
&:\quad
\mathbb C_u\subset\mathbb O,
\quad
\mathcal A_u\ \text{an associative complex operator algebra},\\
\text{integrable gluing}
&:\quad
\text{compatible holomorphic transition data among local fibers},\\
\text{choice space}
&:\quad
u\in S^6
\cong G_2/SU(3).
\end{aligned}}
$$

Thus \(S^6\) is the moduli space of admissible local complex directions. The nonassociative whole contains all of them without choosing one. A local observable context chooses one \(u\), thereby reducing the octonionic automorphism symmetry from \(G_2\) to the stabilizer \(SU(3)\). A single \(\mathbb C_u\) is already associative; “integrability” becomes nontrivial when these local choices are asked to assemble into a complex geometry or holomorphic field of observable algebras.

This is a duality of roles:

| Global / positive side | Local / integrable side |
|---|---|
| exceptional nonassociative carrier | associative complex fiber |
| invariant positive cone | complex-linear observable calculus |
| no preferred imaginary unit | selected \(u\) and \(\mathbb C_u\) |
| \(G_2\), \(F_4\), or cone symmetry | stabilizer symmetry of one context |
| causal possibility and directedness | measurable phase and spectral resolution |
| covariance among all local choices | one here-and-now algebra of observables |

Neither side is an approximation to the other. Their relation is the proposed descent.

## Two different appearances of \(S^6\)

Two uses of the six-sphere must be kept separate.

### The sphere of octonionic complex choices

The unit imaginary octonions form

$$
S^6
=
\{u\in\operatorname{Im}\mathbb O:u^2=-1\}.
$$

Each \(u\) generates an associative copy

$$
\mathbb C_u
:=
\operatorname{span}_{\mathbb R}\{1,u\}
\subset\mathbb O.
$$

The compact exceptional group \(G_2=\operatorname{Aut}(\mathbb O)\) acts transitively on these choices, and the stabilizer of one \(u\) is \(SU(3)\):

$$
S^6\cong G_2/SU(3),
\qquad
SU(3)\longrightarrow G_2\longrightarrow S^6.
$$

This is theorem-level homogeneous and bundle geometry. It says that a local complex presentation is a point of a highly symmetric family, not an absolute complex axis written into the whole.

### A complex structure on the manifold \(S^6\)

The standard octonionic almost-complex structure is

$$
J_u(v)=u\times v,
\qquad
u\in S^6,
\quad
v\in T_uS^6.
$$

It is \(G_2\)-invariant and nonintegrable. In the repository's declared left-multiplication convention, its Nijenhuis tensor is exactly the octonion associator up to a normalization:

$$
\boxed{
N_{J,u}(v,w)
=
2[u,v,w].
}
$$

The numerical coefficient and sign depend on the Nijenhuis and left/right multiplication conventions; the invariant content is

$$
[u,v,w]\neq0
\quad\Longleftrightarrow\quad
N_J\neq0
$$

for the standard structure. Nonassociativity is therefore not merely analogous to its failure of integrability: the associator is the local obstruction tensor. Its intrinsic torsion is part of the standard nearly Kähler geometry. A hypothetical integrable complex structure on the smooth six-sphere would be another structure, not an integrable version of this same homogeneous octonionic \(J\).

The conditional manuscript in [[algebra/s6-manuscript-branch|the \(S^6\) manuscript branch]] claims such an integrable structure through a globally assembled torus family. Its status remains conditional. Even if it survives scrutiny, the resulting compact complex threefold cannot be Kähler because

$$
H^2(S^6;\mathbb R)=0.
$$

The exact philosophical fork is therefore already visible:

$$
\boxed{
\begin{array}{c}
\text{retain the canonical octonionic }G_2\text{ symmetry}\\
\Downarrow\\
\text{nonintegrable nearly Kähler complex direction}
\end{array}
\qquad\middle|\qquad
\begin{array}{c}
\text{select a globally integrable complex presentation}\\
\Downarrow\\
\text{lose the claim to canonical }G_2\text{-homogeneity}
\end{array}}
$$

This is not yet a formal duality theorem, but it is a genuine incompatibility of demands for the known canonical structures. Full octonionic symmetry and global complex integrability cannot simply be assigned to the same \(J\).

The qualification is essential. Positivity and integrability are not absolutely incompatible: any complex manifold admits Hermitian metrics. What \(S^6\) forbids is a Kähler or symplectic polarization, because \(H^2(S^6;\mathbb R)=0\). The sharp fork is therefore

$$
\boxed{
\text{canonical round-compatible \(G_2\) nearly Kähler structure}
\quad\text{versus}\quad
\text{hypothetical integrable, necessarily non-Kähler structure}.
}
$$

No diffeomorphism or ordinary \(G_2\) symmetry can exchange the two, because the Nijenhuis tensor is natural under pullback. If the programme's “duality” maps them, it must be a carrier-changing correspondence that transports associator torsion into declared holonomy, curvature, or cocycle data.

## Positivity supplies directedness

The phrase **nonassociative positivity** is made precise by moving from the sphere of slice choices to the exceptional Euclidean Jordan algebra

$$
J_3^{\mathbb O}
:=
\mathfrak h_3(\mathbb O).
$$

Its cone of squares

$$
(J_3^{\mathbb O})_+
=
\{x^2:x\in J_3^{\mathbb O}\}
$$

is homogeneous and self-dual. The compact group \(F_4\) preserves the Jordan product and the distinguished unit; the appropriate noncompact structure group acts transitively on the cone interior. Primitive idempotents provide normalized extreme directions, while positive sums move into higher-rank interiors.

The cone supplies an algebraic distinction between allowed positive direction and its negative before a Lorentzian clock exists. A compatible compression semigroup then turns this direction into causal order:

$$
S_W
=
\{g:gW\preceq W\}.
$$

The causal orientation does not come from the reversible \(G_2\), \(F_4\), or \(S_3\) actions themselves. It comes from the pointed cone and the one-sided subsemigroup they preserve relative to a local context.

This makes the user's claim exact in type:

> Nonassociative exceptional positivity supplies the invariant cone from which causal directedness can be constructed; \(S^6\) organizes the symmetry-related complex slices in which that order becomes locally observable.

Connes' reconstruction of von Neumann algebras from suitably self-dual, facially homogeneous complex cones supplies a theorem-level neighboring bridge between positivity, complex structure, and operator algebra. Its “complex cone” is an operator-algebraic object, not an integrable almost-complex structure on the manifold \(S^6\). The programme still has to construct the functor from the exceptional Jordan cone and its slice family to such local standard-form cones.

## Integrability supplies local observability

Once \(u\) is selected, the local scalar field is ordinary and associative:

$$
\mathbb C_u\cong\mathbb C.
$$

A local algebra of observables may therefore be a complex associative, generally noncommutative algebra

$$
\mathcal A_u
\subseteq
\mathcal B(\mathcal H_u).
$$

The relevant adjectives do different work:

- **complex-associative** means phases, spectral calculus, and local analytic continuation can be represented without octonionic bracketing ambiguity;
- **integrable**, when applied to the fibered geometry, means the local complex presentations satisfy the compatibility needed for a genuine holomorphic atlas or operator field;
- **noncommutative** means the observable product retains order sensitivity and quantum incompatibility;
- **associative** means products and operator domains can be composed without an octonionic bracketing ambiguity.

The local theory is therefore not made commutative by integrability. It is made complex-associative. Its noncommutativity is the ordinary noncommutativity of operators, not the nonassociativity of the global carrier.

The descent has the type

$$
\boxed{
\text{nonassociative positive whole}
\longrightarrow
\text{associative complex, noncommutative local algebra}.
}
$$

The exact finite local-context flag

$$
\mathfrak h_2(\mathbb C_u)
\subset
\mathfrak h_3(\mathbb C_u)
\subset
\mathfrak h_3(\mathbb O)
$$

strengthens this from a dimension-counting metaphor. The Hermitian matrix spaces are commutative Jordan observable algebras; their ordinary noncommutative associative envelopes are \(M_2(\mathbb C_u)\) and \(M_3(\mathbb C_u)\). A physical descent must still prove positivity of the projection or conditional expectation and dynamical closure of the selected context.

## The groupoid and fiber formulation

Let \(\mathsf U\) be the groupoid of local complex choices:

$$
\operatorname{Ob}(\mathsf U)=S^6,
\qquad
\operatorname{Mor}_{\mathsf U}(u,v)
=
\{g\in G_2:g\cdot u=v\}.
$$

Over it place a field of local operator algebras,

$$
u
\longmapsto
\mathcal A_u,
$$

and then independently supply a faithful weight section

$$
\varphi_u
\in
\mathcal W_{\mathrm{faithful}}(\mathcal A_u).
$$

The complex slice selects the algebraic context; it does not by itself select the state or weight.

The desired object is not one privileged algebra but a covariant fibered family

$$
\mathscr A
\longrightarrow
[S^6/G_2].
$$

Transport along \(g:u\to v\) should give a \(*\)-isomorphism, correspondence, or explicitly declared functor

$$
\alpha_g:
\mathcal A_u
\longrightarrow
\mathcal A_v.
$$

Within a fixed fiber, changing the faithful weight from \(\varphi\) to \(\psi\) is governed by the Connes cocycle

$$
\sigma_t^\varphi(A)
=
(D\varphi:D\psi)_t\,
\sigma_t^\psi(A)\,
(D\varphi:D\psi)_t^*.
$$

There are consequently two reversible comparison groupoids:

1. the \(G_2\) groupoid compares **which complex slice** is used;
2. the Connes cocycle groupoid compares **which faithful weight or modular presentation** is used inside a slice.

The global-to-local fact-producing arrow is not an arrow of either groupoid. It is a one-sided realization

$$
q_{\mathrm{wall}}:
\bigl(J_3^{\mathbb O},\omega,\mathscr A\bigr)
\dashrightarrow
\bigl(u,\mathcal A_u,\omega_{x,u},x,\text{record}\bigr).
$$

This is the precise location of the causal grain: it is the primitive positive unit of selection and record realization, while the groupoids express the high symmetry among the unrealized alternatives.

## Connes' time is the unlike dimension

For a faithful normal state or weight \(\varphi\) on \(\mathcal A_u\), Tomita--Takesaki theory returns a modular automorphism group

$$
\sigma^\varphi:
\mathbb R
\longrightarrow
\operatorname{Aut}(\mathcal A_u).
$$

This parameter does not begin as a fourth coordinate placed beside three spatial coordinates. It acts **on the algebra of local determinations**. In the Connes--Rovelli thermal-time hypothesis, the physical time flow is selected by the state through this modular group. Changing the state changes its representative, while the Connes cocycle supplies their comparison and the outer modular class supplies state-independent structure. [[inbox/causal-grain-cmb-spectroscopy/connes-time-as-algebraic-dimension|Connes time as an algebraic dimension]] separates this flow from the core dual action, the flow of weights, one-sided causal order, record history, scale-age, conformal time, and proper time.

The temporal dimension is therefore unlike the others in three linked senses:

1. spatial directions belong to an object or local real form;
2. modular time is an automorphism direction of the state--algebra pair;
3. historical time is the orientation of composable fact-and-record arrows.

The proposed realization ladder is

$$
\boxed{
\text{state--algebra modular possibility}
\longrightarrow
\text{positive half-sided inclusion}
\longrightarrow
\text{modular data plus oriented positive translation/inclusion order}
\longrightarrow
\text{record-oriented Lorentzian history}
\longrightarrow
\text{proper-time readings}.
}
$$

The arrows are construction obligations, not a claim that positivity mathematically generates Tomita--Takesaki theory. Modular flow is reversible and state-relative; the positive inclusion selects an oriented half-line; record extension is one-sided; proper time is metric and worldline-relative. Connes' algebraic time can explain why time is not merely another spatial coordinate without being equated to every later clock.

## The symmetry is higher than energy conservation

Energy conservation presupposes one selected time-translation action and its generator. The present ambient symmetry acts one level higher: it compares the choices of complex context, weight, and therefore possible modular clock.

The relevant exceptional nesting can be displayed schematically as

$$
E_{7(-25)}
\supset
E_{6(-26)}
\supset
F_4
\supset
G_2
\supset
SU(3),
$$

tracking, respectively, the exceptional conformal/Freudenthal structure, determinant-cone structure, Jordan automorphisms, octonion automorphisms, and the stabilizer of one chosen imaginary unit. These groups act on different but related carriers; the chain is not one undifferentiated physical gauge group.

Let \(\mathsf G_{\mathrm{ctx}}\) denote the desired total groupoid whose objects are pairs \((u,\varphi_u)\). Given a declared slice transport \(\alpha_g:\mathcal A_u\to\mathcal A_v\), a morphism to \((v,\psi_v)\) consists of \(g:u\to v\) together with the Connes cocycle

$$
U_t
=
\left(
D\psi_v:
D\bigl(\varphi_u\circ\alpha_g^{-1}\bigr)
\right)_t
\in
\mathcal A_v.
$$

The construction must verify composition and functoriality under this combined transport. A fixed-context Noether symmetry is then an isotropy subgroup:

$$
G_{\mathrm{Noether},(u,\varphi_u)}
\subseteq
\operatorname{Aut}_{\mathsf G_{\mathrm{ctx}}}(u,\varphi_u),
\qquad
\pi:
\mathsf G_{\mathrm{ctx}}
\longrightarrow
G_2\ltimes S^6.
$$

The first object acts inside one selected clock presentation; the full groupoid compares different possible contexts and clocks. The invariant sought is not merely one Hamiltonian value. It is the naturality of the whole descent under changes of local slice and modular presentation. A successful theory must make the square

$$
\begin{array}{ccc}
(\mathcal A_u,\varphi_u)
&\xrightarrow{\ q_u\ }&
\text{records in }u
\\[2mm]
\downarrow\scriptstyle{(g,U_t)}
&&
\downarrow\scriptstyle{\text{record comparison}}
\\[2mm]
(\mathcal A_v,\psi_v)
&\xrightarrow{\ q_v\ }&
\text{records in }v
\end{array}
$$

commute up to a declared cocycle or anomaly. Conservation of energy is then one local shadow of this wider covariance after a clock has been selected.

## The CMB reading

The CMB provides many local readout channels of one globally constrained state. In the present duality:

- exceptional positivity fixes a common causal orientation and admissible whole-state covariance;
- a selected complex-associative fiber supplies the phase variable whose real and imaginary quadratures become temperature displacement and velocity-sourced polarization, while integrable gluing would make that phase compatible across contexts;
- the groupoid requires different sky patches and observer presentations to descend compatibly;
- Connes' state-dependent time supplies a candidate algebraic precursor to the local thermal clock of the photon bath; and
- the causal grain counts one primitive whole-to-local realization, not one oscillation of the plasma.

The ideal phase dictionary is

$$
\Psi_k=A_ke^{i\theta_k},
\qquad
T_k^{\mathrm{osc}}\propto\operatorname{Re}\Psi_k,
\qquad
E_k^{\mathrm{source}}\propto\operatorname{Im}\Psi_k.
$$

This makes the TT/EE interleaving and TE sign changes a natural test of one descended photon--baryon complex phase. The standard Einstein--Boltzmann equations still calculate the local transfer. The new explanation would be why one globally positive, context-covariant primordial state supplies a common causal orientation and a natural growing-mode phase to every local fiber.

Three sharper empirical candidates follow.

1. **Naturality of state and acoustic phase:** one primordial state/covariance and one photon--baryon growing-mode phase underwrite TT, TE, and EE, with their phase and shape shifts fixed by distinct declared transfer kernels. Lensing and matter are separately calculated descendants of the same primordial state and background, not additional acoustic quadratures.
2. **Holonomy residual:** failure to glue the local complex slices trivially produces a representation-fixed off-diagonal, parity, or higher-point closure pattern rather than arbitrary sky anisotropy.
3. **Ternary selection:** in the explicitly linear, coherent branch-averaged log-power template, equal \(A_2\) weights cancel the first branch moment, while a third harmonic may survive after a separately derived nonlinear map into a cubic statistic. Equal random branch weights do not generically erase a two-point variance.

These targets are not automatic consequences of \(S^6\). They become predictions only when the algebra field, connection, state, positive semigroup, and curvature-to-CMB map are constructed.

## Exact content and open weld

| Statement | Grade |
|---|---|
| \(S^6\cong G_2/SU(3)\) parametrizes octonionic imaginary-unit choices | established mathematics |
| each \(u\) defines an associative complex subalgebra \(\mathbb C_u\) | established algebra |
| the standard octonionic almost-complex structure on \(S^6\) is nonintegrable | established mathematics |
| \(N_J=2[\ ,\ ,\ ]\) in the declared convention | established associator/Nijenhuis identity; coefficient is convention-sensitive |
| an integrable complex structure on the smooth \(S^6\) exists | conditional local manuscript claim; classical problem otherwise unresolved |
| any such integrable \(S^6\) is Kähler or \(G_2\)-homogeneous | excluded for the standard meanings used here |
| the exceptional Jordan algebra has a homogeneous self-dual positive cone | established mathematics |
| that cone is the programme's premetric causal cone | proposed physical identification |
| local observable algebras form a \(G_2\)-covariant field over \(S^6\) | construction target |
| Connes modular and outer flows are algebraic time structures unlike spatial coordinates | theorem-grade structure; thermal-time interpretation and metric solder are additional |
| one primitive positive descent unifies cone direction, complex selection, fact, and scale | principal welded-grain conjecture |
| this duality explains the CMB phase architecture with fewer inputs | empirical programme target |

The decisive theorem target is a positive, groupoid-natural realization functor

$$
\mathfrak D:
\bigl(J_3^{\mathbb O},\mathscr A,\omega\bigr)
\longrightarrow
\bigl(\mathsf{LorHist}_3,\{\mathcal A_u\},\{\text{records}\}\bigr)
$$

whose noninvertible elementary arrows have index \(+1\), whose reversible changes of \(u\) and weight are covariant, and whose local output recovers complex noncommutative observables, Lorentzian causal physics, one photon--baryon growing-mode phase family for TT/TE/EE, and separately transferred lensing and matter descendants.

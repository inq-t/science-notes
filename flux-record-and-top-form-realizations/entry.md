# Flux, Records, Top Forms, and Assembly

A crossing calibration can persist through several mathematically distinct mechanisms: covariant boundary-flux balance, inclusion of a durable record, a spacetime-constant top-form sector, or transport of an operator K-theory class. These mechanisms may eventually be faces of one wall, but none may be substituted for another. Baum--Connes assembly is important precisely because it gives a rigorous local-geometric-to-global-analytic map for reversible presentation groupoids; the irreversible passage from a probability law to a fact requires a separate wall correspondence, and a physical scalar still requires an independently normalized pairing.

## The meaning of flow at the wall

[[sufficient-reason/entry|Sufficing reason]] terminates in a probability measure on the spectrum of a readout context. Necessitating reason terminates in a character that fixes the contextual fact. Those are explanatory termini, not names for two ordinary substances.

The wall between them must contain at least two kinds of arrow:

1. reversible arrows identifying equivalent presentations; and
2. a factive or record-forming process that is not invertible in the physical register.

The first kind can form a groupoid. The second generally does not belong to its maximal subgroupoid. [[algebra/local-global-individuation|Local--global individuation]] therefore asks for an ambient process category with a reversible core, while [[conservation-of-causal-charge/factive-descent-and-records|factive descent]] asks for the instrument, obtained value, and persistent record.

This distinction prevents the phrase “the flow through the wall” from hiding several inequivalent constructions.

| Flow or flux | Mathematical carrier | Reversible? | What it can mean |
|---|---|---:|---|
| modular automorphism flow | \(\sigma_s^\omega\in\operatorname{Aut}(A)\) | yes, an \(\mathbb R\)-group | vertical motion at fixed algebra and state |
| dual flow / flow of weights | dual action on a canonical core | yes, an \(\mathbb R\)-group | trace or weight scaling |
| horizontal scale transport | inclusions or correspondences \(X_{N_2:N_1}\) | not fixed in advance | comparison of different cut fibers |
| accessibility or record arrow | an additive \([0,\infty)\)-semigroup or proper record inclusion | generally no | one-sided becoming or persistence |
| Noether boundary flux | \(\mathcal F_\xi[W]\) | signed balance | physical charge crossing a boundary |
| top-form flux | a period or cohomology class of \(F_4\) | sector datum | integration constant or superselection label |
| K-theory boundary map | a connecting morphism \(\partial\) | functorial, not a time evolution | K-theoretic boundary or index class crossing an extension |
| lost BKM response | a positive quadratic defect | no such implication | distinguishability not retained by a channel |

[[wall-construction-interface/vertical-and-horizontal-motion|Vertical and horizontal motion]] owns the first firewall. [[program-core/symmetry-conservation-and-action|Symmetry, conservation, and action]] owns the distinction among K-classes, indices, Casimirs, response capacities, and Noether charges.

## Physical flux and the characteristic gravitational rate

For Hamiltonian sectors carrying one common symmetry with generator \(\xi\), the controlled subsystem template is

$$
\boxed{
Q_\xi[\Sigma_2]-Q_\xi[\Sigma_1]
+\mathcal F_\xi[W]=0.
}
$$

Every term must live in the same moment-map target. [[conservation-of-causal-charge/diagonal-charge-balance|Diagonal charge balance]] proves the finite-dimensional product theorem; [[conservation-of-causal-charge/causal-individuation-balance|causal-individuation balance]] states the still-open gravitational specialization. Positive BKM capacity is not the signed linear charge.

One proposed areal modulus has a useful process presentation. If

$$
\eta_*:=\frac{c^3}{4\hbar G},
$$

then

$$
\boxed{
P_G
:=\frac{c^5}{G}
=4\hbar c^2\eta_*.
}
$$

This is a characteristic gravitational power scale. It is not the actual flux through every horizon and is not, without additional hypotheses, a universal maximum-luminosity theorem.

The same scale has three useful presentations:

$$
P_G
=\frac{\hbar c^2}{\ell_P^2}
=\frac{2c^3M}{r_s}
\stackrel{\mathrm{fossil}}{=}
\frac{4\zeta\hbar c^3}{H_c\lambda_*^3}.
$$

The Planck expression and the Schwarzschild expression follow by substituting \(\ell_P^2=G\hbar/c^3\) and \(r_s=2GM/c^2\). The last equality additionally assumes the fossil closure. With [[bulk-area-cell-normalization/entry|the literal spherical normalization]], \(\zeta=\gamma s_*/3\).

For a flat FLRW apparent horizon, let \(\varepsilon\) and \(p\) denote physical energy density and pressure. A standard signed Kodama/apparent-horizon energy-supply convention gives

$$
\boxed{
P_A(N)
=(\varepsilon+p)A_Ac
=(1+q(N))P_G
=\left(-\frac{\dot H}{H^2}\right)\frac{c^5}{G},
}
$$

with the overall sign reversed if the boundary orientation is reversed; \(|P_A|\) is the magnitude. Here the factor \(c\) enters through \(HR_A=c\) in the horizon energy-supply law, not because ordinary matter is assumed to cross the horizon at speed \(c\). A stationary Schwarzschild solution has no corresponding nonzero outward flux merely because \(P_G\) is finite. The stationary horizon supplies a Noether-charge and saturation test; the evolving FLRW horizon supplies a process-rate shadow. [[conservation-of-causal-charge/black-hole-saturation-boundary|The black-hole boundary]] and [[deriving-g-v2/the-leak-register|the leak register]] keep those claims separate.

## Baum--Connes: what assembly actually assembles

Let \(\mathcal G\) be a second-countable locally compact Hausdorff groupoid with a Haar system. Let \(A\) be a separable \(\mathcal G\)-\(C^*\)-algebra: a \(C_0(\mathcal G^{(0)})\)-algebra equipped with a continuous \(\mathcal G\)-action. In the standard proper-space model,

$$
K_*^{\mathrm{top}}(\mathcal G;A)
:=\varinjlim_X
KK_*^{\mathcal G}(C_0(X),A),
$$

where \(X\) ranges over proper \(\mathcal G\)-compact subspaces of a universal proper \(\mathcal G\)-space. The Baum--Connes assembly map with coefficients has the form

$$
\boxed{
\mu_{\mathcal G,A}:
K_*^{\mathrm{top}}(\mathcal G;A)
\longrightarrow
K_*(A\rtimes_r\mathcal G).
}
$$

For a group and a proper \(\mathcal G\)-compact space \(X\), its analytic construction is schematically

$$
KK_*^{\mathcal G}(C_0(X),A)
\xrightarrow{\ j_r^{\mathcal G}\ }
KK_*(C_0(X)\rtimes_r\mathcal G,
A\rtimes_r\mathcal G)
\xrightarrow{\ [p_X]\otimes-\ }
K_*(A\rtimes_r\mathcal G),
$$

where \([p_X]\) is the K-class of the projection constructed from a cutoff function. The groupoid version requires the corresponding Haar-system and cutoff hypotheses rather than an automatic reuse of the group formula. Assembly sends equivariant geometric or topological cycles to analytic operator-algebraic index classes. The conjecture asserts that this map is an isomorphism in the stated version and class of objects.

That is exactly the kind of assembly grammar the programme needs: local geometric representatives can determine one stable analytic invariant without choosing a preferred presentation. It is not:

- an evolution equation;
- a probability-to-character map;
- a measurement instrument;
- a Noether conservation theorem;
- a BKM-to-entropy identity;
- a numerical area density; or
- a derivation of \(G\), \(H(z)\), or a carrier length.

The coefficient form cannot simply be assumed: Higson, Lafforgue, and Skandalis construct counterexamples to Baum--Connes **with coefficients**, including failure of surjectivity in the relevant constructions; this is not the same as a blanket refutation of the original coefficient-free conjecture. Conversely, Tu proves the coefficient conjecture for broad amenable groupoid settings under explicit hypotheses. A proposed wall groupoid must therefore earn amenability or another applicable theorem rather than inherit assembly-isomorphism language by analogy.

## Assembly around, not through, the factive wall

The clean naturality theorem begins with one reversible presentation groupoid \(\mathcal G\) and two coefficient algebras \(A_{\mathrm{pre}}\) and \(A_{\mathrm{rec}}\). The irreversible wall is additional data. If its equivariant structural shadow is represented by

$$
w\in KK_d^{\mathcal G}(A_{\mathrm{pre}},A_{\mathrm{rec}}),
$$

then descent gives the analytic wall class

$$
[W]:=j_r^{\mathcal G}(w)
\in KK_d\!\left(
A_{\mathrm{pre}}\rtimes_r\mathcal G,
A_{\mathrm{rec}}\rtimes_r\mathcal G
\right).
$$

A conditional expectation or completely positive instrument does not automatically define \(w\). Once it does exist, compatibility of descent with the Kasparov product gives the naturality square

$$
\begin{array}{ccc}
K_i^{\mathrm{top}}(\mathcal G;A_{\mathrm{pre}})
&\xrightarrow{\ -\otimes_{A_{\mathrm{pre}}}w\ }&
K_{i+d}^{\mathrm{top}}(\mathcal G;A_{\mathrm{rec}})
\\[4pt]
\big\downarrow\scriptstyle{\mu_{\mathcal G,A_{\mathrm{pre}}}}
&&
\big\downarrow\scriptstyle{\mu_{\mathcal G,A_{\mathrm{rec}}}}
\\[4pt]
K_i(A_{\mathrm{pre}}\rtimes_r\mathcal G)
&\xrightarrow{\ -\otimes[W]\ }&
K_{i+d}(A_{\mathrm{rec}}\rtimes_r\mathcal G).
\end{array}
$$

Baum--Connes governs the two vertical assembly maps. The wall is \(w\) and its descent \([W]\), not \(\mu\). With these arrows obtained from the same equivariant correspondence, commutativity is a theorem rather than an anomaly test. If the two sides genuinely require different groupoids, one must additionally supply a proper generalized morphism or groupoid correspondence, coefficient transport, and the applicable functoriality theorem, together with a K-orientation when a geometric wrong-way map is intended. Two independently posited horizontal arrows do not define a commutator: their failure to agree is underdetermined, not yet an anomaly. Only after a canonical comparison is constructed can a resulting defect become an obstruction candidate, and only a further physical realization and pairing could call it curvature or flux. [[spectral-wall-descent/index-and-curvature-transgression|Index and curvature transgression]] owns the existing theorem programme for a fixed structural class with changing local representatives, and [[semiorthogonal-decompositions/categorical-wall-interface|the categorical wall interface]] names the missing categorical-to-analytic bridge.

## Why Connes--Thom and a boundary map are nearer the flow

For a strongly continuous, equivalently point-norm-continuous, \(\mathbb R\)-action \(\alpha\) on a \(C^*\)-algebra \(A\), the Connes--Thom theorem gives a natural degree-one isomorphism

$$
\boxed{
K_i(A)
\cong
K_{i+1}(A\rtimes_\alpha\mathbb R).
}
$$

Because \(\mathbb R\) is amenable, its full and reduced crossed products agree. Thus the vertical modular \(\mathbb R\)-action does not require an appeal to the open general Baum--Connes conjecture. A technical gate remains: [[wall-construction-interface/core-spectral-wall|the present canonical core]] is formulated as a von Neumann crossed product. Applying \(C^*\)-crossed-product K-theory requires an invariant \(C^*\)-subalgebra on which the modular action is point-norm continuous, plus a justified comparison with the von Neumann completion.

The one-sided wall is different. Replacing the additive semigroup \([0,\infty)\) by its group completion \(\mathbb R\) may erase the very arrow the programme wants to explain; the multiplicative space \((0,\infty)\) would already be a group. A continuous additive semigroup points first toward Wiener--Hopf or Toeplitz extensions, continuous product systems, or \(E_0\)-semigroups. Deaconu--Renault groupoids and Cuntz--Pimsner machinery become candidates after a discrete \(\mathbb N\)-action, endomorphism, or correspondence has actually been selected.

For an extension

$$
0\longrightarrow I_W
\longrightarrow\mathcal T_W
\longrightarrow A_{\mathrm{future}}
\longrightarrow0,
$$

operator K-theory supplies a connecting morphism

$$
\boxed{
\partial:
K_i(A_{\mathrm{future}})
\longrightarrow
K_{i-1}(I_W).
}
$$

The connecting class \(\partial x\) is exactly a K-theoretic boundary class; in a suitable Toeplitz, Wiener--Hopf, or Fredholm realization it may acquire an index interpretation. Calling it an **index flux** is project terminology motivated by its boundary role. Pairing it with a cyclic cocycle requires a dense smooth subalgebra, usually holomorphically closed, a continuous cyclic cocycle on that subalgebra, and matching parity; such a cocycle is often obtained from a summable Fredholm module or spectral triple. The result is generally a complex scalar. Integrality is guaranteed when the pairing factors through an integral K-homology/Fredholm index class, or when a separate integrality theorem is proved. Interpreting the result as spectral flow additionally requires a self-adjoint Fredholm path or an appropriate unbounded-KK theorem. It is still not an energy flux, causal charge, or entropy current until a physical pairing theorem identifies the carriers.

## One class, three pairings

The strongest useful synthesis is not that Planck scale, Schwarzschild radius, and supernova redshift are the same observable. It is that one stable wall class might admit three separately constructed realizations:

$$
x_{\mathrm{wall}}
\in K_*(A\rtimes_r\mathcal G),
$$

$$
\left\langle\phi_{\mathrm{UV}},x_{\mathrm{wall}}\right\rangle,
\qquad
\left\langle\phi_{\mathrm{hor}},x_{\mathrm{wall}}\right\rangle,
\qquad
\left\langle\phi_{\mathrm{cos}},x_{\mathrm{wall}}\right\rangle.
$$

Each \(\phi\) must be a K-homology class, or a cyclic cocycle on a suitable smooth subalgebra, with the analytic hypotheses needed for its pairing. The three candidates would encode:

| Pairing | Intended shadow | Independent obligation |
|---|---|---|
| ultraviolet | Planck translation of an inverse-area modulus | construct a finite normalization without importing \(G\) |
| horizon | Schwarzschild/Iyer--Wald boundary charge | prove the same class and normalization in the local Einstein restriction |
| cosmological | crossing evaluation and FLRW horizon process | construct horizontal transport and compare with calibrated \(H_0E(z_c)\) |

Equality of the three numbers would require a naturality or transgression theorem and compatible normalization. K-theory is deliberately insensitive to much metric information; it cannot by itself fix a length, an area density, or a continuously valued coupling. A type-III algebra has no canonical tracial pairing, but K-theory/K-homology pairings do not in general require a trace. A nontracial modular cocycle, a K-homology class, or passage to a core must be constructed separately; a core trace also carries the movable-origin problem diagnosed by [[wall-construction-interface/core-spectral-wall|the core wall]].

Coarse Baum--Connes is not a shortcut to the supernova curve. In the intended discrete Roe-algebra model, one first needs a proper bounded-geometry metric carrier. Coarse invariants are insensitive to multiplication of the metric by a fixed positive constant, and more generally to coarse-equivalent changes, whereas a calibrated redshift--distance relation contains differential metric information beyond coarse equivalence, and an absolute scale only after calibration.

## Record realization

A record supplies persistence without a conserved hidden substance. Let a crossing instrument write a dimensionless calibration observable

$$
\widehat q_c:=\lambda_*^2\widehat\chi_c
\in Z(\mathcal R_c)
$$

into a record algebra \(\mathcal R_c\). Suppose later record algebras contain it through monomorphisms

$$
j_{Nc}:\mathcal R_c\hookrightarrow\mathcal R_N
$$

and the realized characters are compatible:

$$
\chi_N\circ j_{Nc}=\chi_c.
$$

Then

$$
\boxed{
\chi_N\!\left(j_{Nc}(\widehat q_c)\right)
=\chi_c(\widehat q_c).
}
$$

If \(\lambda_*\) is independently fixed, the realized value

$$
\eta_N
:=\frac{
\chi_N(j_{Nc}(\widehat q_c))
}{\lambda_*^2}
$$

is constant along the record system. This is an exact conditional persistence result. It does not choose the outcome, construct the write instrument, determine \(q_c\), or prove Noether conservation. [[program-core/record-scale-soldering|Record--scale soldering]] owns the additional theorem required before record extension can be identified with cosmic scale growth.

## Top-form realization

A covariant constancy mechanism can instead place the calibration in a global form sector. In four spacetime dimensions, let \(A_3\) be a three-form and \(\eta\) a scalar modulus. The schematic topological term

$$
S_{\mathrm{top}}
=\int_M A_3\wedge\mathrm d\eta
$$

gives

$$
\boxed{
\mathrm d\eta=0
}
$$

upon variation with respect to \(A_3\). The integration-by-parts identity is

$$
\mathrm d(\eta A_3)
=-A_3\wedge\mathrm d\eta+\eta F_4,
\qquad
A_3\wedge\mathrm d\eta
=\eta F_4-\mathrm d(\eta A_3),
$$

where \(F_4=\mathrm dA_3\). Thus the bulk term is **plus** \(\int_M\eta F_4\) modulo the displayed boundary term.

The standalone action is not yet a nonzero-flux model. If \(\eta\) is also varied freely, its equation is \(F_4=0\). A nonzero flux sector therefore requires a larger coupled action with additional \(\eta\)-dependent terms or sources, a global constraint, or a treatment in which \(\eta\) is not independently varied. Moreover, if \(A_3\) is one globally defined form, then \(F_4\) is exact and has trivial de Rham periods on closed cycles. Nontrivial quantized flux requires local gauge potentials organized as a higher connection, or equivalent differential-cohomological data. Only in such a completed construction can a top-form period label a global sector while \(\eta\) has no ordinary propagating scalar mode.

A codimension-one transition hypersurface \(W_c\) could be represented schematically by

$$
\mathrm d\eta
=q_c\,\delta_{W_c},
$$

so that the modulus is piecewise constant and the wall deposits a jump. This equation is distributional and schematic: \(\delta_{W_c}\) must be the closed Poincare-dual current of a gauge-consistent wall source, since \(\mathrm d^2\eta=0\) requires the source current to be closed. A codimension-two causal cut cannot support this equation without an enclosing world tube, relative-cohomology formulation, or another degree-correct source construction.

This mechanism stabilizes a supplied value; it does not select the flux sector or derive

$$
\eta_c
=\frac{\gamma s_*}{3}
\frac{R_c}{\lambda_*^3}.
$$

[[causal-scale-theory/conjectures/local-global-vacuum-completion|Local--global vacuum completion]] correctly lists top-form fluxes, unimodular integration data, sequestering-like constraints, and boundary data as competing realizations. [[library/cosmological-constant-and-general-covariance/entry|Henneaux and Teitelboim]] provide the unimodular precedent. Kaloper, Padilla, Stefanyszyn, and Zahariade, archived in [[deriving-value-of-g/sources/entry|the G source ledger]], give a primary four-form construction in which gravitational parameters become spacetime constants while the selected values remain global data.

Top-form flux, record persistence, and Bianchi protection can coexist. Their conjunction still does not calculate the crossing calibration unless the wall action and its global constraint determine the same value noncircularly.

## Primary assembly sources

- [Baum, Connes, and Higson, *Classifying Space for Proper Actions and K-Theory of Group C\*-Algebras*](https://doi.org/10.1090/conm/167/1292018) formulate the proper-action assembly map and its coefficient version.
- [Connes, *An Analogue of the Thom Isomorphism for Crossed Products by an Action of \(\mathbb R\)*](https://doi.org/10.1016/0001-8708(81)90056-6) proves the degree-one K-theory isomorphism for \(\mathbb R\)-crossed products.
- [Connes and Skandalis, *The Longitudinal Index Theorem for Foliations*](https://doi.org/10.2977/prims/1195180375) develops the groupoid/foliation index precedent in bivariant K-theory.
- [Le Gall, *Théorie de Kasparov équivariante et groupoïdes. I*](https://doi.org/10.1023/A:1007707525423) supplies the equivariant KK framework for locally compact groupoids used by the groupoid formulation.
- [Higson and Kasparov, *E-Theory and KK-Theory for Groups Which Act Properly and Isometrically on Hilbert Space*](https://doi.org/10.1007/s002220000118) prove Baum--Connes with coefficients for second-countable locally compact a-T-menable groups.
- [Tu, *The Baum--Connes Conjecture for Amenable Foliations*](https://doi.org/10.1023/A:1007744304422) proves the coefficient isomorphism for the stated amenable groupoid setting.
- [Higson, Lafforgue, and Skandalis, *Counterexamples to the Baum--Connes Conjecture*](https://doi.org/10.1007/s00039-002-8249-5) supply the essential guard against assuming the conjecture with arbitrary coefficients.
- [Muhly and Renault, *C\*-Algebras of Multivariable Wiener--Hopf Operators*](https://doi.org/10.1090/S0002-9947-1982-0670916-3) represent the stated Wiener--Hopf algebras as images of groupoid \(C^*\)-algebras.
- [Deaconu, *Groupoids Associated with Endomorphisms*](https://doi.org/10.1090/S0002-9947-1995-1233967-5) supplies a primary groupoid model for discrete one-sided endomorphism data.
- [Kellendonk and Schulz-Baldes, *Boundary Maps for C\*-Crossed Products with \(\mathbb R\)*](https://doi.org/10.1007/s00220-004-1122-7) identifies the Wiener--Hopf K-theory boundary map with the Connes--Thom isomorphism and relates it to cyclic pairings.

These sources establish mathematical tools. None proposes the physical identification made by this programme.

## Construction gates

The synthesis becomes a theory only after it supplies:

1. explicit reversible presentation groupoids with the required Haar systems, and separable coefficient \(\mathcal G\)-\(C^*\)-algebras with continuous actions;
2. proof that the relevant assembly theorem applies, rather than an unqualified appeal to Baum--Connes;
3. a genuine one-sided wall correspondence or extension that does not erase the process arrow;
4. a naturality or transgression theorem linking its structural class across the wall;
5. normalized ultraviolet, horizon, and cosmological pairings on compatible carriers;
6. a map from any index flux to the common physical moment-map flux, if that identification is claimed;
7. a factive instrument and persistent record; and
8. a global equation that selects, rather than merely freezes, the crossing modulus.

The ambitious statement is then precise: the local representatives may flow, accessible energy may cross a horizon, and new facts may extend the record while one assembled structural class and one calibrated areal law endure. At present that is a theorem programme, not a completed conservation law.

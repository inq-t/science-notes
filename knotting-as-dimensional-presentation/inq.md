---
inq.module: "knotting-as-dimensional-presentation"
inq.include:
  - "**/*.md"
---
# Knotting as Three-Dimensional Presentation

Ordinary knotting makes three-dimensional space mathematically exceptional, but only after the primitive carrier has been fixed to be a single bare closed line. A connection canonically supplies one-dimensional probes because it assigns transport to paths; it does not by itself select one-dimensional physical carriers. The resulting dimension filter is rigorous but conditional, while the ontological reversal remains conjectural. If an observable spatial presentation must preserve nontrivial ambient-isotopy classes of primitive loop carriers, then three is the unique Euclidean spatial dimension. Knot topology supplies **distinction** between components of a configuration space; it supplies neither direction, energy, mass, nor an arrow of time. The strongest bridge now visible is a typed chain from loop holonomy, through codimension-two complement data and a closed energy form, to a coercive physical Hamiltonian. Chern--Simons transgression and instanton Floer theory give an exact Euclidean three-configuration/four-dimensional correspondence for part of this chain, while the Yang--Mills mass gap still requires a continuum Yang--Mills construction plus a uniform coercivity theorem on the whole gauge-invariant vacuum complement.

## The correction that makes the intuition exact

Let \(\mathfrak K_d\) denote the set of ambient-isotopy classes of unparametrized, tame, unframed, single smooth circles embedded in Euclidean \(d\)-space:

$$
\mathfrak K_d
:=
\left\{
S^1\hookrightarrow\mathbb R^d
\right\}/\text{ambient isotopy}.
$$

Then

$$
\boxed{
|\mathfrak K_2|=1,
\qquad
|\mathfrak K_3|>1,
\qquad
|\mathfrak K_d|=1\quad(d\ge 4).
}
$$

The planar statement follows from Jordan--Schoenflies. Three-space contains the ordinary nontrivial knots. Skopenkov's [survey of embedding and knotting](https://arxiv.org/abs/math/0604045) states the ambient-unknotting theorem in the relevant stable range: every embedded \(n\)-manifold unknots in \(\mathbb R^m\) for \(m\ge2n+2\), which gives every tame embedded circle the unknot type for \(d\ge4\). It treats the trefoil as the exceptional low-dimensional example.

This is not the assertion that all knots exist only in three dimensions. Codimension-two knots \(S^p\hookrightarrow S^{p+2}\) occur in higher dimensions, as in Zeeman's [spinning construction](https://www.lms.ac.uk/sites/default/files/1961%20Knotting%20manifolds.pdf), and smooth higher-codimension Haefliger knots also exist; in particular, embeddings \(S^3\hookrightarrow S^6\) have nontrivial smooth isotopy classes in Haefliger's [classification](https://annals.math.princeton.edu/1966/83-3/p02). Framed knots, links, wild embeddings, internal labels, and nontrivial ambient topology change the classification again.

The exact exceptional statement is therefore:

> **[EXACT TOPOLOGY]** Three is the unique Euclidean ambient dimension in which one bare closed one-dimensional carrier has nontrivial ordinary knot type.

The dimension is not selected by “knotting” without a type declaration. It is selected by the pair

$$
(\text{carrier dimension},\text{ambient dimension})=(1,3).
$$

## What the obstruction operates on

A knot type is a connected-component label of an unparametrized embedding space:

$$
\operatorname{Emb}(S^1,\mathbb R^3)/\operatorname{Diff}(S^1)
=
\coprod_{[K]\in\mathfrak K_3}\mathcal E_{[K]},
\qquad
[K]\in\pi_0\!\left(
\operatorname{Emb}(S^1,\mathbb R^3)/\operatorname{Diff}(S^1)
\right).
$$

The obstruction therefore operates on **deformations of embeddings**. A path inside one component is an isotopy. Changing knot type requires leaving the embedding space through a singular crossing, cutting, reconnection, or some enlargement of the allowed carrier.

This already separates four concepts that are easily conflated:

| Structure | Mathematical content | What it does not yet supply |
|---|---|---|
| knot type | component of an embedding space | direction of traversal |
| oriented knot | choice of orientation on the carrier | temporal irreversibility |
| chiral knot | inequivalence to a mirror image | an arrow of time |
| dynamically protected knot | topology plus an energy law that suppresses escape | a gap on every physical excitation |

Every ambient isotopy can be run backward. Knotting is therefore an obstruction to **unrestricted deformation**, not an intrinsically directed process. It can become a conserved charge only when the admissible dynamics stays inside the embedding space. It becomes a persistent fact only when an obtained component is recorded by the noninvertible process described in [[algebra/local-global-individuation|local--global individuation]].

The precise philosophical correction is:

$$
\boxed{
\text{knot topology supplies distinction; dynamics supplies cost; record extension supplies direction.}
}
$$

## Why three appears: carrier and detector are both loops

Let a smooth or locally flat \(p\)-dimensional carrier \(K\) be embedded in an \(n\)-dimensional spatial manifold. If its codimension is \(q=n-p\), a small transverse disk has boundary

$$
\mu_K\simeq S^{q-1}=S^{n-p-1}.
$$

This boundary is the canonical local meridian encircling the carrier. If the primitive detector is specifically that meridian and has dimension \(k=q-1\), then

$$
\boxed{n=p+k+1.}
$$

If the persistent carrier is a loop and its primitive detector is also a loop, then \(p=k=1\) and

$$
\boxed{n=1+1+1=3.}
$$

This is stronger and cleaner than the slogan that knots “prefer” three dimensions. Codimension two is exactly where the canonical local meridian is itself a loop, so ordinary path holonomy can detect meridional linking.

Alexander duality gives, for a spherical carrier \(S^p\hookrightarrow S^n\),

$$
\widetilde H_i(S^n\setminus S^p;\mathbb Z)
\cong
\widetilde H^{n-i-1}(S^p;\mathbb Z),
$$

so the complement is homologically an \(S^{n-p-1}\). In codimension two it is a homology circle. The abelian meridian charge \(H_1\cong\mathbb Z\) is not enough to distinguish a trefoil from an unknot; the global information lies in nonabelian complement data such as

$$
\Gamma_K:=\pi_1(Y\setminus \nu K),
$$

its peripheral subgroup, and its representation varieties. Kervaire's [higher-dimensional knot analysis](https://www.numdam.org/articles/10.24033/bsmf.1624/) proves that the meridian normally generates a codimension-two knot group and that its abelianization is \(\mathbb Z\).

## Why one-dimensional probes are canonical for connections

A connection \(A\) is read by parallel transport along paths. It therefore supplies a canonical one-dimensional probe, though it neither selects a one-dimensional physical carrier nor excludes higher-dimensional observables. Closing a path removes endpoint frame choices up to conjugacy, and a representation \(R\) gives the Wilson observable

$$
W_R(K)[A]
=
\operatorname{Tr}_R\,
\mathcal P\exp\!\left(\oint_K A\right).
$$

For a fixed knot complement, flat connection data with any required meridional constraint is organized by

$$
\mathcal X_G(K)
=
\operatorname{Hom}(\Gamma_K,G)/G.
$$

Culler and Shalen's [character-variety construction](https://annals.math.princeton.edu/1983/117-1/p05) is a primary source for this algebraic use of three-manifold groups.

There are two related but distinct operative chains. An ordinary Wilson loop uses the carrier itself:

$$
A
\longmapsto
\operatorname{Hol}_A(K)
\longmapsto
W_R(K).
$$

Defect or complement data instead uses

$$
K
\longmapsto
X_K:=Y\setminus\nu K
\longmapsto
\pi_1(X_K)
\longmapsto
\operatorname{Hom}(\pi_1(X_K),G)/G,
$$

with prescribed meridional conjugacy data when the defect model requires it. A flat connection on the complement does not directly define holonomy along the removed knot, so these chains may not be silently identified.

The roles must remain typed. Parallel transport operates on paths and returns fiber isomorphisms. A based loop returns a group element only after a frame is chosen; without that choice it supplies a conjugacy class. The Wilson-loop observable is a function of a connection. Only after a regulator or continuum definition, representation, renormalization, and operator domain are supplied may it define an operator on a gauge-invariant state carrier. The Hamiltonian operates on states. The knot is a label or support for an observable; it is not itself a mass operator.

## Gauge closure already has an exact kinematic cost

There is now a precise result one logical level below embedding and knotting. Let a compact connected simple group $G$ label the links of a finite connected graph $\Gamma$, equip $G$ with the negative-Killing metric, and impose the full gauge group at every vertex. Peter--Weyl theory and the spin-network basis give

$$
\boxed{
\lambda_\Gamma^{\mathrm{GI}}
=
g(\Gamma)\lambda_G,}
$$

where $\lambda_\Gamma^{\mathrm{GI}}$ is the sharp product-Haar electric-flux Poincare constant on nonconstant gauge-invariant functions, $g(\Gamma)$ is graph girth, and $\lambda_G$ is the smallest nonzero Casimir allowed by the global form of $G$. The reason is elementary but structural: nontrivial gauge-invariant spin-network support cannot terminate at a degree-one vertex, so it must contain a cycle; a Wilson character on a shortest cycle saturates the bound. [[contemporary-puzzles/yang-mills-mass-gap/gauge-descent-flux-fisher-coercivity#Gauge invariance sharpens the constant to girth times Casimir|The girth--Casimir theorem]] gives the proof and boundary qualifications.

For $SU(3)$ the convention gives $\lambda_G=4/9$, and a simple square-plaquette graph gives the exact dimensionless number $16/9$. This is the first rigorous instance in this programme where **closure multiplies group geometry to produce a nonzero dimensionless distinction cost**.

But the theorem is deliberately weaker than the knot hypothesis. Graph girth is combinatorial and dimension independent; no embedding, crossing, linking, or ambient isotopy enters. Its measure is product Haar, not the interacting vacuum measure. It therefore proves neither selection of three spatial dimensions nor the physical Yang--Mills mass gap. What it does prove is that “closure” is not merely poetic: once the carrier and flux operator are typed, closed gauge support can sharpen a local group constant into an exact full-carrier kinematic frame bound.

Witten's [Chern--Simons construction of the Jones polynomial](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-121/issue-3/Quantum-field-theory-and-the-Jones-polynomial/cmp/1104178138.full) makes this relation explicit at the formal path-integral level: Wilson-line expectation values in three-dimensional Chern--Simons theory produce framed-link invariants; an unframed Jones invariant requires a framing choice followed by the appropriate correction or normalization. Reshetikhin and Turaev's [quantum-group construction](https://doi.org/10.1007/BF01239527) gives the associated topological invariants a rigorous realization. Pure classical Chern--Simons theory is metric-independent, while the quantum theory retains framing dependence. It supplies topological distinction without a local propagating energy or mass scale.

## A conditional dimension-selection theorem

Assume:

1. **[PHYSICAL AXIOM]** the primitive persistent spatial carrier is a single tame, unframed closed line;
2. **[PHYSICAL AXIOM]** inequivalent facts must remain inequivalent under ambient isotopy of that carrier;
3. **[GEOMETRIC AXIOM]** the ambient presentation is globally \(\mathbb R^d\) or \(S^d\), with \(d\ge2\), rather than a manifold whose prior handles or obstacles manufacture loop sectors; and
4. **[MINIMALITY AXIOM]** the selected spatial dimension is one in which the carrier has nontrivial, rather than merely unique, ambient-isotopy classes.

Then the spatial dimension is \(3\).

The proof is the preceding trichotomy: a circle cannot knot in \(2\)-space, can knot in \(3\)-space, and unknots again in every \(d\ge4\).

This theorem does **not** yet reverse geometry into algebra. “Embedding,” “ambient isotopy,” and “Euclidean dimension” already presuppose spatial topology. A genuinely Copernican reversal must begin with a pregeometric doctrine that independently produces a cyclic probe object \(\ell\), a notion of deformation, and a distinction invariant, and must then prove that its minimal faithful geometric realization sends

$$
\ell\longmapsto S^1,
\qquad
\text{deformation}\longmapsto\text{ambient isotopy},
$$

with a nontrivial realization first occurring in three dimensions. That missing realization theorem is the actual ontological target. The existing doctrine in [[algebra/inq|the algebraic pre-core]] provides places for probes, presentation, obstruction, and factual record, but it does not yet derive the cyclic primitive.

## Kinematic clue: null momenta can sum to timelike momentum

A null four-vector is nonzero even though its Lorentzian norm vanishes. A photon can connect distinct emission and absorption events while carrying no proper-time clock and admitting no rest frame. “Zero proper time” does not mean “no motion” or “no causal relation.”

More importantly, null constituents need not have null total momentum. In flat spacetime, for an isolated finite-energy system with total energy \(E\) and momentum \(\mathbf p\), invariant mass is

$$
M^2c^4=E^2-c^2|\mathbf p|^2.
$$

For two photons with energies \(E_1,E_2\) and opening angle \(\theta\),

$$
M^2c^4=2E_1E_2(1-\cos\theta).
$$

Unless the momenta are exactly parallel, their sum lies inside the future light cone and the composite has a center-of-momentum frame. This is standard relativistic kinematics; see the Particle Data Group's [kinematics review](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-kinematics.pdf). A generic curved cosmology need not admit one global four-momentum or global center-of-momentum frame.

This suggests a sharply scoped interpretation:

> **[CONDITIONAL INTERPRETATION]** For a composite of future-directed massless constituents, invariant mass is the timelike norm of total four-momentum, nonzero when the constituent momenta are not all collinear. This is not drag. It is not a definition of every massive excitation as a composite of null flux.

A knot could matter by topologically trapping circulating or non-collinear flux, but that is only a hypothesis. One would have to prove

$$
\text{topological trapping}
\Longrightarrow
\text{stable localized finite energy}
\Longrightarrow
-P^\mu P_\mu=M^2c^2>0
\Longrightarrow
\text{collective rest frame},
$$

using signature \((-+++)\). An operational clock would require the further implication

$$
\text{rest frame}
+
\text{scale-bearing recurrent observable}
\Longrightarrow
\text{possible operational clock}.
$$

No standard theorem supplies these chains. Radiation itself gravitates because Einstein's equation couples curvature to stress--energy, not only to rest mass. An isotropic kinetic or coarse-grained photon gas has a timelike fluid rest frame, characterized by the timelike eigenvector of \(T^\mu{}_{\nu}\); a single coherent null beam, and arbitrary anisotropic radiation configurations, need not. Carroll's [general-relativity notes](https://arxiv.org/abs/gr-qc/9712019) give the perfect-fluid and radiation equations. What light rays determine without an independent calibration is the conformal causal structure \([g]\), not one metric scale representative; this is exactly the distinction proved in [[conformal-scale-geometry/causal-order-and-metric-scale|causal order and metric scale]]. The surviving insight is therefore about the realization of **scale-bearing timelike organization**, not the existence of spacetime in the absence of elementary rest mass.

The Higgs mechanism should likewise not be described literally as friction. It changes the representation and dispersion law so that an excitation occupies a timelike mass shell; it does not dissipate its energy or make unitary dynamics irreversible.

## A toy theorem for dimensionless geometry times a yardstick

The proposed grammar “dimensionless number from geometry times a dimensional unit gives an energy” is exactly realizable for an elastic flux loop. Let \(\gamma\) be a closed curve with tension \(T\) and bending stiffness \(B\):

$$
E[\gamma]
=
T L(\gamma)
+
B\int_\gamma\kappa^2\,ds.
$$

Under a spatial dilation \(\gamma\mapsto\lambda\gamma\), the two terms scale as \(\lambda\) and \(\lambda^{-1}\). The arithmetic--geometric mean and Cauchy--Schwarz inequalities give

$$
\begin{aligned}
E[\gamma]
&\ge
2\sqrt{TB\,L\int_\gamma\kappa^2ds}\\
&\ge
2\sqrt{TB}\int_\gamma|\kappa|\,ds.
\end{aligned}
$$

Fenchel's theorem says that a closed curve has total curvature at least \(2\pi\), while the Fary--Milnor theorem says that a nontrivial knot has total curvature strictly greater than \(4\pi\). Consequently,

$$
E_{\mathrm{closed}}\ge4\pi\sqrt{TB},
\qquad
E_{\mathrm{knot}}>8\pi\sqrt{TB}.
$$

Milnor's [total-curvature proof](https://people.reed.edu/~ormsbyk/milnor-total-curvature.pdf) therefore gives the desired factorization in a literal model:

$$
\boxed{
\underbrace{4\pi}_{\text{universal nontrivial-knot curvature threshold}}
\times
\underbrace{2\sqrt{TB}}_{\text{dynamical energy yardstick}}
<E_{\mathrm{knot}}.
}
$$

These are classical infimum bounds on the restricted space of smooth embedded closed curves with fixed positive \(T\) and \(B\), not a quantum spectral gap. If disappearance or reconnection is allowed, knot type need not define a superselection sector. The model also exposes the missing principle: if \(B=0\), tension alone gives \(E=T L\mapsto\lambda E\), so the knot retains its topological class while its energy tends to zero as it shrinks. Geometry does not manufacture its own unit. The coefficients \(T\) and \(B\) must be derived from the physical carrier and its dynamics; inserting them phenomenologically does not solve a fundamental mass problem.

## An exact model in which knot topology costs energy

The Faddeev--Skyrme model gives a controlled example. A finite-energy field

$$
n:\mathbb R^3\cup\{\infty\}\simeq S^3\longrightarrow S^2
$$

has a Hopf charge

$$
Q_H\in\pi_3(S^2)\cong\mathbb Z.
$$

Preimages of two regular values are linked loops, and the linking number is \(Q_H\). With a quadratic and a quartic derivative term,

$$
E[n]=E_2[n]+E_4[n],
$$

the rescaling \(n_\lambda(x)=n(x/\lambda)\) gives

$$
E_2[n_\lambda]=\lambda E_2[n],
\qquad
E_4[n_\lambda]=\lambda^{-1}E_4[n].
$$

The competing scalings remove the simple Derrick dilation instability and impose a virial balance on stationary solutions. The Vakulenko--Kapitanskii inequality has the form

$$
E[n]\ge C|Q_H|^{3/4}.
$$

Vakulenko and Kapitanskii's [original bound](https://www.mathnet.ru/eng/dan42751) proves a positive lower bound in sectors with \(Q_H\ne0\). Existence and dynamical stability require separate analysis; Faddeev and Niemi's [numerical knot solitons](https://arxiv.org/abs/hep-th/9610193) give evidence for stable finite-energy configurations. The controlled conclusion is

$$
\text{topological sector}
+
\text{scale-balancing energy}
\Longrightarrow
\text{positive lower bound in nonzero Hopf sectors}.
$$

Topology alone does not set the size or energy. Derrick's [scaling theorem](https://doi.org/10.1063/1.1704233) explains why broad classes of scalar models have no stable finite-energy static solitons without such balancing terms.

This example is not a Yang--Mills mass-gap proof. It bounds nonzero Hopf sectors, whereas a mass gap is a bound on the entire vacuum-orthogonal Hilbert space. The model without a potential also has massless small fluctuations about a constant vacuum. Positive classical soliton rest energy can therefore coexist with zero global spectral gap.

## The exact three-configuration/four-dimensional Euclidean bridge

Let \(Y\) be an oriented three-manifold. Define the Chern--Simons three-form density

$$
\operatorname{cs}_3(A)
=
\frac{1}{8\pi^2}
\operatorname{tr}\!\left(
A\wedge dA+\frac{2}{3}A\wedge A\wedge A
\right),
$$

and its functional on connection space by

$$
\operatorname{CS}_Y(A)
=\int_Y\operatorname{cs}_3(A).
$$

Under large gauge transformations, this functional is generally defined only modulo a convention-dependent period lattice.

The density obeys the transgression identity

$$
d\operatorname{cs}_3(A)
=
\frac{1}{8\pi^2}\operatorname{tr}(F_A\wedge F_A).
$$

The first variation of the functional is

$$
D\operatorname{CS}_Y(A)[a]
=
\frac{1}{4\pi^2}\int_Y\operatorname{tr}(a\wedge F_A).
$$

On the Riemannian product \((\mathbb R\times Y,dt^2+g_Y)\), in temporal gauge and up to normalization, time rescaling, and orientation convention, negative \(L^2\)-gradient flow,

$$
\partial_tA=-*_YF_A,
$$

is equivalent to the anti-self-dual Yang--Mills equation \(F_{\mathcal A}^{+}=0\) in four dimensions. Critical points are flat connections on \(Y\); the relevant Floer trajectories are finite-energy ASD connections modulo gauge. This is the geometric core of instanton Floer theory. Kronheimer and Mrowka's [instanton knot homology](https://arxiv.org/abs/0806.1053) adds knots in three-manifolds through prescribed codimension-two singular and meridional data.

The result is an exact Euclidean and Morse-theoretic correspondence:

$$
\boxed{
\text{three-dimensional connection configurations}
\quad\xrightarrow{\text{finite-energy ASD trajectories}}\quad
\text{four-dimensional Euclidean gauge geometry}.
}
$$

It is tempting to read the extra dimension as time, and a knot history as a worldsheet or cobordism in \(Y\times I\). Floer trajectories are not Lorentzian Yang--Mills evolution. The mathematics by itself licenses only a Morse/Floer or Euclidean history parameter. It does not yet produce Lorentzian causal time, irreversible actuality, or a physical Hamiltonian spectrum. Those require the typed realization described in [[algebra/real-forms-and-factive-spacetime|real forms and factive spacetime]] and a separate positivity and reconstruction theorem or direct Lorentzian construction.

## Why the Yang--Mills coincidence is worth pursuing

There are two independent dimension statements:

1. a one-dimensional holonomy probe has nontrivial ordinary knot types only in spatial dimension \(d=3\), if it is also realized as the primitive physical carrier; and
2. the Yang--Mills coupling has engineering dimension

$$
[g]=\frac{4-D}{2},
$$

so the classical Yang--Mills action is scale invariant precisely in spacetime dimension \(D=4\).

If a history construction supplies \(D=d+1\), the two meet at \(3+1\):

$$
\boxed{
\begin{aligned}
&\text{loop holonomy plus persistent knot distinction}
&&\Longrightarrow d=3,\\
&\text{one history dimension}
&&\Longrightarrow D=4,\\
&\text{dimensionless Yang--Mills coupling in }D=4
&&\Longrightarrow \text{no classical intrinsic mass scale}.
\end{aligned}}
$$

This conjunction is mathematically nontrivial and free of numerical coincidence. It still does not derive the quantum scale \(\Lambda_{\mathrm{YM}}\), prove that it is nonzero, or prove a gap. If a nonzero renormalization-group invariant scale exists, it is introduced through renormalization and dimensional transmutation, schematically as

$$
\Lambda_{\mathrm{YM}}
=
\mu\exp\!\left[-\frac{1}{2\beta_0g^2(\mu)}+\cdots\right],
$$

but a generated scale is not yet a lower spectral bound. [[contemporary-puzzles/yang-mills-mass-gap/inq|The Yang--Mills mass-gap module]] keeps those obligations separate.

## The carrier-first construction

The proposed reversal can now be written without letting an equation change the meaning of its terms:

$$
\begin{aligned}
&\text{pregeometric algebraic doctrine}\\
&\longrightarrow \text{distinguished cyclic probe and deformation law}\\
&\longrightarrow \text{three-dimensional knot presentation }(Y,K)\\
&\longrightarrow \Gamma_K=\pi_1(Y\setminus\nu K)\\
&\longrightarrow \mathcal X_G(K)=\operatorname{Hom}(\Gamma_K,G)/G\\
&\dashrightarrow \underbrace{\mathcal H_{\mathrm{phys}}}_{\text{missing quantization and realization map}}\\
&\longrightarrow \text{closed energy form }\mathcal E\\
&\longrightarrow H\\
&\longrightarrow \text{spectral statement}.
\end{aligned}
$$

Each arrow has a different job:

- topology classifies possible distinctions;
- holonomy turns a loop into a gauge observable;
- a state or measure, constraints, positive representation, and completion must construct the Hilbert carrier;
- the closed form measures energetic cost;
- if the form is densely defined, closed, and lower-semibounded, its self-adjoint generator \(H\) governs evolution;
- the spectrum of \(H\), not the knot label, defines mass gaps.

The Wilson--'t Hooft loop algebra is a particularly sharp candidate for the algebra of distinction. For suitable electric and magnetic charge labels \(e,m\) in an \(SU(N)\) theory, equal-time loop operators satisfy schematically

$$
W_e(C)T_m(C')
=
\exp\!\left(\frac{2\pi i\langle e,m\rangle}{N}\operatorname{Link}(C,C')\right)
T_m(C')W_e(C).
$$

The linking number of two supports becomes a central phase in an order--disorder operator algebra. 't Hooft's [original analysis](https://dspace.library.uu.nl/handle/1874/4701) and the modern [generalized-symmetry formulation](https://arxiv.org/abs/1412.5148) make this more than a visual analogy. Global gauge-group form, regulator, renormalization, and superselection sector determine whether both defects act as endomorphisms of one physical Hilbert representation. The relation is still a commutation or charge statement, not an energetic inequality.

The most important reversal is not “calculate mass from curvature instead of curvature from mass.” It is:

> Construct the carrier and its admissible distinctions first; then ask which closed form makes those distinctions costly; only afterward recover the operator and the geometry it generates.

This is the same reversal developed in [[contemporary-puzzles/yang-mills-mass-gap/carrier-first-reversal|carrier-first reversal]].

## The stopping condition for an actual mass-gap contribution

Let \(\Omega\) be the physical vacuum and let \(\mathcal E\) be the closed quadratic form of \(H-E_0\) on the gauge-invariant carrier. The required bound is

$$
\boxed{
\inf_{\substack{\psi\perp\Omega\\\|\psi\|=1}}
\mathcal E[\psi]
\ge\Delta>0.
}
$$

The dimensionless-geometry-times-yardstick proposal can be promoted to an operator target. Let

$$
\mathcal D_0
:=
\{A\Omega:\ A\in\mathcal A_{\mathrm{loop}},\ \omega(A)=0\}
$$

be an \(\mathcal E\)-form core in \(\Omega^\perp\). Suppose one constructs dimensionless closable linear maps

$$
\delta_j:\mathcal D_0\longrightarrow\mathcal K_j,
$$

with \(\delta_j\Omega=0\) on the enlarged domain and with the sum below finite or convergent. Flux insertion, meridional twisting, and loop surgery are only motivations until such maps are actually defined; a unitary twist would normally enter through \(U_j-1\) or a commutator. If one proves, with constants uniform in regulator and volume,

$$
\sum_j\|\delta_j\psi\|_{\mathcal K_j}^2
\ge
\kappa_{\mathrm{top}}\|\psi\|^2,
\qquad \psi\in\mathcal D_0,
$$

with a dimensionless \(\kappa_{\mathrm{top}}>0\), and independently proves

$$
\mathcal E[\psi]
\ge
\varepsilon_*
\sum_j\|\delta_j\psi\|_{\mathcal K_j}^2,
\qquad \psi\in\mathcal D_0,
$$

with a dynamical energy scale \(\varepsilon_*>0\), then the composite inequality holds on the form core and extends to \(\operatorname{Dom}\mathcal E\cap\Omega^\perp\) by form-core approximation and closedness:

$$
\boxed{\operatorname{gap}(H)\ge\varepsilon_*\kappa_{\mathrm{top}}.}
$$

This is the rigorous form of the desired multiplication. Geometry or algebra must prove that every nonvacuum vector has a distinction; dynamics must price that distinction. On an enlarged common domain the required kernel condition is

$$
\bigcap_j\ker\delta_j=\operatorname{Ran}P_0.
$$

If the intersection is a larger subspace, the result is merely a transverse or sector gap. The displayed argument proves an energy gap for an already constructed \(H\). It becomes a relativistic Yang--Mills mass-gap result only after the theory, translation representation, spectrum condition, and vacuum sector have also been constructed.

Knot topology contributes to this theorem only if all of the following are constructed:

1. **Carrier:** the knot or flux sectors occur in the physical gauge-invariant Hilbert space, not merely in classical field space or a gauge-fixed auxiliary space.
2. **Stability:** the relevant sector label survives all allowed quantum processes, or the energy required for reconnection is itself controlled.
3. **Coercivity:** one common positive lower bound holds over the union of all nonvacuum sectors; separate sector bounds may tend to zero.
4. **Exhaustivity:** the sector decomposition controls the whole vacuum complement, including topologically trivial local excitations.
5. **Uniformity:** the bound survives infinite volume and regulator removal in fixed physical units.
6. **Realization:** reflection positivity, locality, covariance, regularity, and reconstruction produce the required Lorentzian positive-energy theory. Floer gradient flow is not an Osterwalder--Schrader measure and supplies none of these automatically.

A lower bound only for knotted solitons proves none of items 4--6. A topological theory with knot invariants proves none of items 3--6. A dynamically generated scale proves neither 3 nor 4. [[contemporary-puzzles/yang-mills-mass-gap/physical-distinction-coercivity|Physical distinction and coercivity]] gives the operator-signature verdict: the problem stops only when the centered physical carrier has one joint, uniform coercive bound.

## Research programme

The conjectural contribution can be separated into four theorem-sized targets.

**Cyclic-primitivity theorem.** Derive, from the pre-observable algebraic doctrine rather than from a chosen manifold, why the primitive gauge-invariant probe is cyclic and one-dimensional.

**Minimal-realization theorem.** Construct a realization functor from those cyclic probes to embeddings and prove that faithful preservation of their obstruction sectors first occurs in spatial dimension three.

**Topological-timelike theorem.** Give a Lorentz-covariant field model in which nontrivial knot charge forces stable localized non-collinear flux and hence strictly timelike total four-momentum.

**Uniform-coercivity theorem.** Show that the same structure controls every vector orthogonal to the Yang--Mills vacuum with a positive regulator- and volume-uniform bound.

The first two would make a real contribution to dimensional selection. The third would ground the intuition that persistent closure can realize composite invariant mass and a collective timelike rest frame. Turning such a frame into a clock would still require a scale-bearing recurrent observable. Only the fourth, together with continuum existence, reaches the Clay mass-gap problem.

## Verdict

The Copernican reversal survives as a proposed realization principle:

$$
\boxed{
\text{three-space is the minimal presentation with nontrivial ordinary loop-knot distinction}
}
$$

provided loop primitivity and faithful obstruction are first derived rather than assumed. Knotting need not be interpreted as irreversibility; it is the algebraic-geometric possibility of a distinction that cannot be erased by admissible local deformation. Energy is the form that prices departure from or persistence within that distinction. For an isolated system, invariant mass is the Lorentz-invariant norm of total four-momentum; in quantum theory, masses occur in the spectrum of the Poincare Casimir \(P^\mu P_\mu\). A timelike sector does not by itself constitute a clock. **[ONTOLOGICAL PROPOSAL]** Directed record extension may ground an arrow of time, but relativistic time and proper time are not defined by irreversibility. Gravity responds to stress--energy, including radiation; neither elementary rest mass nor knot topology is required.

The important new clue is therefore not “knots prove \(3+1\).” It is that **loop carrier, loop detector, three-dimensional knot distinction, four-dimensional gauge history, and four-dimensional scale generation fit into one typed architecture**. The architecture is exact at several separate joints. The missing realization and coercivity arrows are now explicit enough to attack.

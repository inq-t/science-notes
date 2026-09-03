# The Yang--Mills Gap as Gauge-Descended Flux Coercivity

At a finite lattice regulator, the Yang--Mills Hamiltonian gap is exactly a Poincare constant of the ground-state-weighted electric-flux form. On a connected pure-gauge graph containing a cycle, compact-group geometry and gauge closure give the sharp dimensionless Haar constant: graph girth times the smallest allowed Casimir. It does not deteriorate with graph volume and is volume independent on fixed-girth families such as ordinary square-plaquette lattices. Comparison with the interacting vacuum yields an explicit but generally volume-degrading bound. Wu's theorem instead gives an exact sufficient local-to-global estimate, assuming uniform conditional Poincare bounds and an influence matrix with spectral radius below one. On the real multiplication sector, the denominator also has an exact classical Fisher-score realization. The unsolved problem is to prove the local vacuum estimates from Yang--Mills dynamics and carry the resulting positive bound through the continuum limit in physical renormalization-group units.

**Status: [EXACT REGULATED, HAAR-FRAME, AND GIRTH--CASIMIR THEOREMS; CONDITIONAL LOCAL-TO-GLOBAL THEOREM; OPEN VACUUM-MIXING AND CONTINUUM PROGRAMME].** The ground-state transform, product-Haar frame, gauge-invariant girth refinement, coordinate-expectation decomposition, and bounded-density comparison below are finite-dimensional functional analysis on products of compact groups. They neither prove existence of four-dimensional continuum Yang--Mills nor supply the regulator-uniform interacting-vacuum hypotheses that would prove its mass gap.

## The category correction

The misleading question is

> What object gives a mass to a massless gluon?

The operator question is

> After gauge descent and vacuum selection, can a normalized physical distinction be made with arbitrarily small energy?

Let \(H_{\mathrm{phys}}\) be the physical time-translation generator and let \(\Omega\) be its vacuum. A gap is

$$
H_{\mathrm{phys}}\geq\Delta_H(1-P_\Omega),
\qquad
\Delta_H>0.
$$

It forbids a sequence of gauge-invariant unit vectors orthogonal to the vacuum whose energy tends to zero. It does not require a gauge-dependent \(A_\mu A^\mu\) term, a massive gluon pole, or a smallest spatial pixel.

The geometric inversion is consequently precise:

$$
\boxed{
\text{gap}
=
\text{least horizontal flux cost of a distinguishable vacuum fluctuation}.
}
$$

Here *horizontal* means physical after the Gauss-law redundancy has been removed. The curvature involved below is curvature of weighted configuration space, not curvature of physical spacetime.

[[contemporary-puzzles/yang-mills-mass-gap/carrier-first-reversal|The carrier-first reversal]] makes the methodological consequence explicit: the closed flux form can be primary, the self-adjoint operator can be reconstructed from it, and its intrinsic geometry can be read from the carré du champ afterward.

## A finite \(SU(3)\) carrier

Let \(\Gamma\) be a finite connected oriented spatial cell complex or lattice, with vertex, edge, and plaquette sets \(V(\Gamma)\), \(E(\Gamma)\), and \(P(\Gamma)\). Its connected graph \(1\)-skeleton carries the link variables. Put

$$
\mathcal C_\Gamma
:=
SU(3)^{E(\Gamma)},
\qquad
\mathcal G_\Gamma
:=
SU(3)^{V(\Gamma)}.
$$

The gauge group acts on link configurations by

$$
(g\cdot U)_e
=
g_{s(e)}U_eg_{t(e)}^{-1}.
$$

With normalized product Haar measure \(\mu_\Gamma\), gauge averaging is the conditional expectation

$$
E_{\mathcal G}F(U)
:=
\int_{\mathcal G_\Gamma}F(g\cdot U)\,\mathrm dg,
$$

and the physical carrier is

$$
\mathcal H_\Gamma^{\mathrm{phys}}
=
L^2(\mathcal C_\Gamma,\mu_\Gamma)^{\mathcal G_\Gamma}.
$$

We assume this carrier has nonconstant vectors, as it does when the cell complex contains a nontrivial loop sector. On a tree with the full vertex gauge group, the invariant carrier can collapse to the constants, in which case there is no first physical excitation to estimate.

Fix the Lie-algebra metric to be \(-B_{\mathfrak{su}(3)}\), as in the Haar-frame theorem below. For a basis orthonormal in that convention and indexed by \(A\), let \(X_e^A\) be the corresponding invariant vector field on the copy of \(SU(3)\) assigned to edge \(e\). The electric-flux Laplacian is

$$
K_\Gamma
:=
-\sum_{e,A}(X_e^A)^2.
$$

The finite Kogut--Susskind Hamiltonian has the typed form

$$
H_\Gamma
=
\kappa_aK_\Gamma+V_\Gamma,
\qquad
\kappa_a>0,
$$

where \(\kappa_a\) carries the dimensional lattice prefactor and \(V_\Gamma\) is the bounded gauge-invariant potential built from plaquettes in \(P(\Gamma)\). [[library/hamiltonian-formulation-of-wilsons-lattice-gauge-theories/inq|Kogut and Susskind]] supply this canonical electric-flux structure.

Because \(\mathcal C_\Gamma\) is compact and connected and the kinetic operator is elliptic, \(H_\Gamma\) has compact resolvent and a unique strictly positive ground state \(\psi_{0,\Gamma}\), up to normalization. Gauge invariance of the Hamiltonian and uniqueness make this ground state gauge invariant. Write

$$
H_\Gamma\psi_{0,\Gamma}
=
E_{0,\Gamma}\psi_{0,\Gamma},
\qquad
\int\psi_{0,\Gamma}^2\,\mathrm d\mu_\Gamma=1,
$$

and define the vacuum probability measure

$$
\boxed{
\mathrm d\nu_\Gamma
:=
\psi_{0,\Gamma}^2\,\mathrm d\mu_\Gamma.
}
$$

This finite construction avoids pretending that the orbit quotient is globally a smooth manifold. Quotient geometry can be recovered on regular strata, but the invariant-function formulation remains meaningful across stabilizer strata.

## Exact ground-state-transform theorem

For every sufficiently regular gauge-invariant \(f\), multiplication by the vacuum gives a physical vector

$$
U_0f:=\psi_{0,\Gamma}f.
$$

Integration by parts and the ground-state equation give

$$
\boxed{
\left\langle
U_0f,
(H_\Gamma-E_{0,\Gamma})U_0f
\right\rangle
=
\kappa_a
\sum_{e,A}
\int_{\mathcal C_\Gamma}
|X_e^Af|^2\,\mathrm d\nu_\Gamma.
}
$$

Equivalently,

$$
U_0^{-1}(H_\Gamma-E_{0,\Gamma})U_0
=
\kappa_a\mathscr L_\Gamma,
$$

where the positive weighted Laplacian is characterized by the Dirichlet form

$$
\mathcal E_\Gamma(f,f)
:=
\sum_{e,A}\int|X_e^Af|^2\,\mathrm d\nu_\Gamma.
$$

If locally

$$
\psi_{0,\Gamma}
=
Z^{-1/2}e^{-S_\Gamma/\hbar},
$$

let \(q\) denote the orbit map. In a smooth quotient chart, write the pushed-forward Haar measure as

$$
q_*\mu_\Gamma
=
J_{\mathrm{orb}}\,\mathrm{dvol}_{G_\Gamma}.
$$

The pushed-forward vacuum measure is then

$$
q_*\nu_\Gamma
=
e^{-W_\Gamma}\mathrm{dvol}_{G_\Gamma},
\qquad
W_\Gamma
=
\frac{2S_\Gamma}{\hbar}
-\log J_{\mathrm{orb}}
+\text{constant},
$$

and the local weighted generator is

$$
\mathscr L_\Gamma
=
-\Delta_{G_\Gamma}
+
\left\langle
\nabla W_\Gamma,
\nabla\,\cdot
\right\rangle_{G_\Gamma}.
$$

This is the Witten or Bakry--Emery weighted Laplacian. The orbit-volume or Weyl/Faddeev--Popov factor cannot be dropped: it is part of the same geometry exposed in [[contemporary-puzzles/yang-mills-mass-gap/a2-weyl-radial-operator|the compact radial audit]]. If \(\mathrm{dvol}_{G_\Gamma}\) is instead defined to be the pushed-forward Haar measure, this Jacobian is absorbed by convention. The negative logarithm of the vacuum is not an optional entropy ansatz: the remaining weight is fixed by the ground state of the same Hamiltonian.

## The gap is a Poincare constant

The vacuum corresponds to the constant function \(1\) after the transform. Orthogonality to it is

$$
\int f\,\mathrm d\nu_\Gamma=0.
$$

The min--max principle therefore gives the exact identity

$$
\boxed{
\Delta_\Gamma
=
\kappa_a
\inf_{\substack{
f\neq0\\
\int f\,\mathrm d\nu_\Gamma=0
}}
\frac{
\displaystyle
\sum_{e,A}\int|X_e^Af|^2\,\mathrm d\nu_\Gamma
}{
\displaystyle
\int|f|^2\,\mathrm d\nu_\Gamma
}.
}
$$

Thus \(\Delta_\Gamma>0\) is equivalent to the Poincare inequality

$$
\operatorname{Var}_{\nu_\Gamma}(f)
\leq
\frac{\kappa_a}{\Delta_\Gamma}
\mathcal E_\Gamma(f,f).
$$

This is stronger conceptually than a dimensional match. It identifies the right carrier, the right norm, the right derivatives, and the right operator.

## A volume-uniform kinematic frame

The interacting vacuum is difficult, but the compact-group carrier already proves a nontrivial frame theorem. Let $G$ be a compact connected simple Lie group. Fix the bi-invariant metric

$$
\langle X,Y\rangle_K=-B_{\mathfrak g}(X,Y)
$$

and let $\{T_A\}$ be orthonormal in this convention. If $\pi$ is an irreducible unitary representation, define its Casimir number by

$$
-\sum_A\mathrm d\pi(T_A)^2=c_K(\pi)I,
\qquad
\lambda_G
:=
\min_{\substack{\pi\in\widehat G\\\pi\neq\mathbf1}}
c_K(\pi)>0.
$$

Only representations that descend to the chosen global form of $G$ enter the minimum. Thus $\lambda_G$ can distinguish two groups with the same Lie algebra. With the metric $-B_{\mathfrak g}$, $c_K(\mathrm{Ad})=1$; another declared metric convention rescales every $c_K(\pi)$.

For a finite edge set $E$, put $\mu_E=\mu_G^{\otimes E}$ and define the dimensionless Haar analysis map

$$
\mathscr D_E^{\mathrm H}f
:=
\bigl(X_e^Af\bigr)_{e,A},
\qquad
\|\mathscr D_E^{\mathrm H}f\|^2
=
\sum_{e,A}\int_{G^E}|X_e^Af|^2\,\mathrm d\mu_E.
$$

**Product-Haar flux-frame theorem.** For every $f\in H^1(G^E)$,

$$
\boxed{
\|\mathscr D_E^{\mathrm H}f\|^2
\geq
\lambda_G\operatorname{Var}_{\mu_E}(f).}
\tag{Haar-frame}
$$

The constant is optimal on the full product and independent of $|E|$.

**Proof.** By Peter--Weyl, the positive single-copy Laplacian is diagonal on matrix coefficients with eigenvalues $c_K(\pi)$; [[library/spectra-of-the-laplace-beltrami-operator-on-compact-semisimple-lie-groups/inq|Beers and Millman]] give a primary spectral-geometric treatment. The product Laplacian is the sum of the commuting single-copy Laplacians, so its eigenvalues are finite sums $\sum_ec_K(\pi_e)$. The least nonzero sum is $\lambda_G$. The Rayleigh principle gives the inequality. $\square$

The metric scale is not itself an observable number. Rescaling the invariant metric rescales $\lambda_G$ and the coordinate expression of the kinetic prefactor $\kappa_a$ reciprocally. The product $\kappa_a\lambda_G$, followed by its independently specified renormalization-group comparison, is the typed energy quantity.

## Gauge invariance sharpens the constant to girth times Casimir

Let $\Gamma=(V,E)$ be a finite connected graph, with the full vertex gauge group acting by

$$
(g\mathbin{\cdot}U)_e
=
g_{s(e)}U_eg_{t(e)}^{-1}.
$$

On the nonconstant gauge-invariant carrier, define

$$
\lambda_\Gamma^{\mathrm{GI}}
:=
\inf_{
\substack{f\in H^1(G^E)^{G^V}\\f\not\equiv\mathrm{const}}
}
\frac{\|\mathscr D_E^{\mathrm H}f\|^2}
{\operatorname{Var}_{\mu_E}(f)}.
$$

The spin-network decomposition gives the exact representation-theoretic formula

$$
\lambda_\Gamma^{\mathrm{GI}}
=
\min_{\substack{
(\pi_e)\neq(\mathbf1)\\
\operatorname{Inv}_v(\{\pi_e\})\neq0\ \text{for every }v
}}
\sum_{e\in E}c_K(\pi_e).
\tag{spin-network-gap}
$$

Here $\operatorname{Inv}_v$ is the invariant tensor space obtained from the outgoing representation spaces and the duals of the incoming ones. [[library/spin-network-states-in-gauge-theory/inq|Baez's spin-network basis]] supplies this decomposition on a fixed graph; the following girth identity is a short deduction from it, not a theorem quoted from that paper.

Let $g(\Gamma)$ be the girth of the underlying multigraph, counting a self-loop as a cycle of length one and a pair of parallel edges as a cycle of length two.

**Finite-graph girth--Casimir theorem.** If $\Gamma$ contains a cycle, then

$$
\boxed{
\lambda_\Gamma^{\mathrm{GI}}
=
g(\Gamma)\lambda_G.}
\tag{girth-Casimir}
$$

**Proof.** In a nontrivial spin-network block, the subgraph of nontrivially labelled edges cannot have a degree-one vertex: a single nontrivial irreducible representation has no invariant vector. Every finite nonempty graph of minimum degree at least two contains a cycle. Its support therefore has at least $g(\Gamma)$ nontrivial edges, each contributing at least $\lambda_G$ to (spin-network-gap). This proves the lower bound.

For saturation, choose a shortest cycle $C$ and a representation $\pi_*$ attaining $\lambda_G$. The Wilson character

$$
f_C(U)
=
\chi_{\pi_*}\!\left(
\prod_{e\in C}U_e^{\varepsilon_e}
\right)
$$

is gauge invariant, has Haar mean zero, and is an eigenfunction with eigenvalue $g(\Gamma)c_K(\pi_*)$. This proves the reverse bound. $\square$

Thus a simple pure-gauge hypercubic graph with square plaquettes and no shorter periodic identification has the sharp kinematic constant $4\lambda_G$, independent of its total volume. A tree with every vertex gauged has only constant invariant functions. The saturation argument assumes that every edge on a shortest cycle remains an independent $G$-valued coordinate with product Haar measure. Ungauged boundary vertices, charged endpoints, matter fields, fixed boundary links or holonomy, flatness constraints, and other restrictions of $G^E$ can alter the admissible spin networks and invalidate the girth formula.

For $G=SU(3)$ in the $-B_{\mathfrak{su}(3)}$ convention, the fundamental representation is allowed and

$$
\lambda_{SU(3)}
=
\frac{C_2(\mathbf3)}{C_2(\mathrm{Ad})}
=
\frac{4/3}{3}
=
\frac49.
$$

An ordinary plaquette lattice therefore has the exact dimensionless Haar-frame constant

$$
\boxed{
g(\Gamma)\lambda_{SU(3)}
=
\frac{16}{9}.}
$$

For the global form $PSU(3)=SU(3)/\mathbb Z_3$, the fundamental representation does not descend; the smallest allowed representation is instead the adjoint in this comparison, giving $\lambda_{PSU(3)}=1$. The number is therefore sensitive to global gauge structure, as it should be. Neither $16/9$ nor $4$ is a mass gap: it is a normalized kinematic frame constant that still requires interacting-vacuum transfer and an energy solder.

This is a genuine closure result, but not yet a knot theorem. The obstruction is the impossibility of a gauge-invariant nontrivial open end, and the relevant topology is the shortest cycle of an abstract graph. It exists in every graph dimension; embedding, linking, and knotting in three-space do no work in this proof. Any specifically three-dimensional knot mechanism must enter through an additional carrier or dynamics.

The individual derivatives $X_e^A$ need not return gauge-invariant functions. Their direct sum is a gauge-covariant response vector whose squared norm is gauge invariant. The analysis operator therefore acts on physical invariant vectors while its response carrier remembers the electric-flux direction.

The weaker product estimate also has an exact coordinate conditional-expectation presentation. For each edge, let

$$
(\mathsf E_e^{\mathrm H}f)(U_{\neq e})
:=
\int_G f(U_{\neq e},u_e)\,\mathrm d\mu_G(u_e).
$$

On $L^2(\mu_E)$, Haar bi-invariance makes $\mathsf E_e^{\mathrm H}$ an orthogonal state-preserving expectation that sends gauge-invariant functions to gauge-invariant functions. The single-copy Poincare inequality gives

$$
\|(I-\mathsf E_e^{\mathrm H})f\|_2^2
\leq
\frac1{\lambda_G}
\sum_A\|X_e^Af\|_2^2.
\tag{local-Haar}
$$

Choose an ordering $e_1,\ldots,e_m$, set $F_0=I$, and put

$$
F_j
:=
\mathsf E_{e_j}^{\mathrm H}\cdots
\mathsf E_{e_1}^{\mathrm H},
\qquad
D_j:=F_{j-1}-F_j.
$$

The expectations commute, their ranges form a decreasing filtration, and $F_m$ is expectation to the constants. Hence the $D_j$ are mutually orthogonal and

$$
\sum_{j=1}^m\|D_jf\|_2^2
=
\operatorname{Var}_{\mu_E}(f).
$$

Because $F_{j-1}$ is a contraction commuting with the $e_j$ expectation, (local-Haar) implies

$$
\sum_A\|X_{e_j}^Af\|_2^2
\geq
\lambda_G\|D_jf\|_2^2.
$$

Summation recovers (Haar-frame). This is an exact finite model of Haar coordinate omission and flux response. It is not a causal wall, a measurement outcome, or an interacting Yang--Mills vacuum.

## What the interacting vacuum changes

Write the finite-volume vacuum density as

$$
\rho_\Gamma:=\psi_{0,\Gamma}^2,
\qquad
\mathrm d\nu_\Gamma=\rho_\Gamma\,\mathrm d\mu_\Gamma.
$$

Elliptic positivity and compactness give finite constants

$$
0<m_\Gamma:=\min\rho_\Gamma
\leq
\rho_\Gamma
\leq
M_\Gamma:=\max\rho_\Gamma<\infty.
$$

For every regular $f$,

$$
\mathcal E_\Gamma(f,f)
\geq
m_\Gamma\mathcal E_\Gamma^{\mathrm H}(f,f),
\qquad
\operatorname{Var}_{\nu_\Gamma}(f)
\leq
M_\Gamma\operatorname{Var}_{\mu_\Gamma}(f).
$$

Combining these estimates with (Haar-frame) proves

$$
\mathcal E_\Gamma(f,f)
\geq
\lambda_G\frac{m_\Gamma}{M_\Gamma}
\operatorname{Var}_{\nu_\Gamma}(f).
$$

For gauge-invariant $f$, (girth-Casimir) sharpens the finite-regulator bound to

$$
\boxed{
\mathcal E_\Gamma(f,f)
\geq
g(\Gamma)\lambda_G\frac{m_\Gamma}{M_\Gamma}
\operatorname{Var}_{\nu_\Gamma}(f).}
\tag{vacuum-comparison}
$$

If $W_\Gamma=-\log\rho_\Gamma$, then

$$
\frac{m_\Gamma}{M_\Gamma}
=
e^{-\operatorname{osc}W_\Gamma},
$$

and the ground-state transform yields

$$
\boxed{
\Delta_\Gamma
\geq
\kappa_a g(\Gamma)\lambda_G
e^{-\operatorname{osc}W_\Gamma}.}
\tag{regulated-gap-bound}
$$

The factors have different types:

- $g(\Gamma)\lambda_G$ is regulator incidence or combinatorics plus compact-group geometry;
- $W_\Gamma=-2\log\psi_{0,\Gamma}$ and its mixing properties are interacting-vacuum dynamics;
- $\kappa_a$ and the tuned comparison across regulators provide dimensional calibration; and
- a factive outcome map, if one is wanted, is a further operational structure.

The bound is positive at each fixed regulator and does not insert an excited eigenvalue. It is nevertheless ground-state-dependent and a posteriori: $\psi_{0,\Gamma}$ comes from the same interacting Hamiltonian. It becomes explanatory only if $W_\Gamma$ or its local conditionals can be controlled from independently stated bare or renormalized data.

A global density ratio is generally the wrong control. If $W_\Gamma$ is extensive, then $\operatorname{osc}W_\Gamma=O(|P(\Gamma)|)$ and (regulated-gap-bound) can decay exponentially with volume. Even a product probability density can have an exponentially bad global ratio while retaining a volume-independent Poincare constant by tensorization. The decay therefore indicts the global comparison proof, not the true interacting gap.

This comparison is the elementary Poincare analogue of the [[library/logarithmic-sobolev-inequalities-and-stochastic-ising-models/inq|Holley--Stroock bounded-perturbation principle]]. It is useful as a finite receipt and a warning about global oscillation, not as the intended continuum proof.

The replacement must be local or multiscale. For the actual vacuum measure, one may ask for:

1. a compatible local or block specification for $\nu_\Gamma$ derived from the Hamiltonian rather than fitted correlators;
2. uniform conditional Poincare or logarithmic-Sobolev bounds on each block with arbitrary admissible boundary data;
3. a quantitative interdependence or spatial-mixing condition preventing a collective low-cost mode; and
4. constants natural under volume growth and the tuned regulator comparison maps.

These requirements have an exact raw-link assembly theorem. At fixed $\Gamma$, use the product carrier $G^{E(\Gamma)}$ before quotienting. Give every link the geodesic metric $d_K$ and gradient determined by the same $-B_{\mathfrak g}$ normalization as $K_\Gamma$, and let $\nu_e(\cdot\mid x)$ be the conditional law of link $e$. Define the Wasserstein--Dobrushin matrix

$$
c_{ej}
:=
\sup_{\substack{x=y\ \mathrm{off}\ j\\x_j\neq y_j}}
\frac{
W_{1,d_K}\!\left(
\nu_e(\cdot\mid x),
\nu_e(\cdot\mid y)
\right)
}{d_K(x_j,y_j)},
\qquad
C_\Gamma=(c_{ej}).
$$

Suppose

$$
\lambda_{\mathrm{loc},\Gamma}
\operatorname{Var}_{\nu_e(\cdot\mid x)}h
\leq
\sum_A\int_G|X^Ah|^2\,\mathrm d\nu_e(\cdot\mid x),
\qquad
r_{\mathrm{sp}}(C_\Gamma)<1
\tag{local-mixing-data}
$$

for every link, conditional configuration, and admissible boundary datum. Compactness supplies the finite-moment hypothesis. Then [[library/poincare-and-transportation-inequalities-for-gibbs-measures-under-the-dobrushin-uniqueness-condition/inq|Wu's sharp Dobrushin estimate]] first gives approximate variance tensorization,

$$
(1-r_{\mathrm{sp}}(C_\Gamma))
\operatorname{Var}_{\nu_\Gamma}(f)
\leq
\sum_e
\int
\operatorname{Var}_{\nu_e(\cdot\mid x)}(f)
\,\mathrm d\nu_\Gamma(x),
$$

and therefore, for every regular $f$,

$$
\boxed{
\mathcal E_\Gamma(f,f)
\geq
\lambda_{\mathrm{loc},\Gamma}
[1-r_{\mathrm{sp}}(C_\Gamma)]
\operatorname{Var}_{\nu_\Gamma}(f).}
\tag{local-to-global}
$$

The inequality holds on the raw product and hence on its gauge-invariant subspace, where the ground-state transform identifies it with a Hamiltonian bound. This is a **conditional theorem**, not a Yang--Mills result smuggled in through vocabulary. The hard work is proving (local-mixing-data) for $\nu_{a,L}=\psi_{0,a,L}^2\mu_{a,L}$ from bare or renormalized local dynamics without importing an already known gap or clustering length.

A raw-link condition may be too rigid along the continuum trajectory, so gauge-invariant blocks with explicit boundary variables may be the natural scale. Wu's displayed theorem does not automatically apply to overlapping, constrained, or heterogeneous blocks. A block version must provide either a disjoint energy-isometric product factorization or a separately proved comparison

$$
\mathcal E_{a,L}
\geq
b_{a,L}\mathcal E_{a,L}^{\mathrm{coord}},
\qquad
b_{a,L}>0.
$$

The resulting lower constant is $b_{a,L}\lambda_{\mathrm{loc}}(a,L)[1-r_{\mathrm{sp}}(C_{a,L})]$. A singular orbit space cannot simply be assumed to have product coordinates or an energy-isometric block gradient.

To state the regulator gate without hiding the volume quantifiers, define

$$
\underline\lambda_{\mathrm{loc}}(a)
:=
\inf_{L,\,\mathrm{boundary}}
\lambda_{\mathrm{loc}}(a,L),
\qquad
\overline q(a)
:=
\sup_{L,\,\mathrm{boundary}}
r_{\mathrm{sp}}(C_{a,L}),
\qquad
\underline b(a)
:=
\inf_L b_{a,L}.
$$

For the raw-link theorem $\underline b(a)=1$. Let $\widehat\Lambda_{\mathrm{YM},a}^{(\mathsf s)}>0$ be an independently specified energy-valued regulator comparison satisfying

$$
\widehat\Lambda_{\mathrm{YM},a}^{(\mathsf s)}
\longrightarrow
\Lambda_{\mathrm{YM}}^{(\mathsf s)}
$$

along the tuned trajectory. The regulator-uniform coercivity gate for this route is

$$
\boxed{
\liminf_{a\to0}
\frac{
\kappa_a\underline b(a)
\underline\lambda_{\mathrm{loc}}(a)[1-\overline q(a)]
}{
\widehat\Lambda_{\mathrm{YM},a}^{(\mathsf s)}
}
>0.}
\tag{Dobrushin-stop}
$$

One also needs $\overline q(a)<1$ and positive local and comparison constants at every regulator where the theorem is invoked. Their separate dimensionless values may tend to zero as $a\to0$; that is not fatal if $\kappa_a$ compensates and the displayed physical ratio retains a positive lower limit. Conversely, (Dobrushin-stop) is not by itself a continuum mass-gap theorem. The form and vacuum-projection convergence, nontrivial continuum carrier, and OS or positive-energy recovery conditions stated below are still required.

[[library/dobrushin-uniqueness-theorem-and-logarithmic-sobolev-inequalities/inq|Zegarlinski's theorem]] proves, for Riemannian single-site spaces under its declared Dobrushin hypotheses, that local specification control can yield a unique Gibbs measure satisfying a logarithmic Sobolev inequality; linearization then gives a Poincare bound. It cannot simply be cited for lattice Yang--Mills. One must first prove that the ground-state density $\psi_{0,\Gamma}^2$ defines the required compatible quasilocal specification after gauge reduction and that the influence bound remains below its threshold uniformly. Neither follows from locality of the original Hamiltonian, because taking the logarithm of an interacting ground-state wavefunction can generate nonlocal dependence.

### The renormalization-group crossover is the bridge

At bare weak coupling a one-link Dobrushin condition should not be expected to solve the continuum problem. The known Yang--Mills functional-inequality precedent lies at explicit strong coupling, whereas an asymptotically free continuum trajectory sends the bare coupling toward zero. Extrapolating the raw-link constant between those regimes is exactly the unjustified step that a proof must replace.

A viable RG version would form gauge-invariant blocks at an independently fixed physical scale (R), integrate the ultraviolet variables inside them, prove conditional mixing between the resulting block carriers, and identify their block defects with the causal-frame maps. As (a\to0), each fixed-(R) block contains order ((R/a)^d) microscopic cells, so uniformity of the block comparison and influence estimates is a genuine multiscale theorem. If (R) were instead chosen from the observed correlation length or desired gap, the construction would be circular; it must be fixed by an independent renormalization condition or upstream causal rule.

This is a precise use of “crossing a wall”: not discreteness by itself, but a local conditional distinction whose influence on remote blocks contracts after a controlled ultraviolet-to-infrared transformation. It also identifies the price of the carrier-first reversal. Finding variables in which infrared coercivity is transparent is useful only if the change of carrier is constructed along the RG trajectory and shown to recover the same observable theory. The block route does not evade renormalization; it turns the RG crossover into the exact missing comparison estimate.

There is a rigorous nearby precedent. [[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen, Zhu, and Zhu]] prove volume-uniform Bakry--Emery, Poincare, and logarithmic-Sobolev estimates for the Euclidean Wilson lattice measure at explicit strong coupling; for $SU(N)$ their convention includes $|\beta|<1/[16(d-1)]$. Their carrier is the Euclidean Wilson Gibbs measure, their generator is Langevin or stochastic-quantization dynamics, and their “mass gap” conclusion is exponential covariance decay. It is not the equal-time Hamiltonian vacuum measure $\psi_0^2\mu_{\mathrm H}$, not the ground-state-transformed Kogut--Susskind generator, and not a continuum-limit theorem. The precedent proves that compact-group curvature plus local interaction control can yield the desired kind of volume-uniform functional inequality; it does not identify the two problems.

There is also a carrier firewall. $\mathsf E_e^{\mathrm H}$ is orthogonal and state preserving in $L^2(\mu_E)$ only. The corresponding interacting map is the conditional expectation $\mathsf E_e^\nu$ in $L^2(\nu_\Gamma)$, and (local-Haar) does not automatically transfer to it. Moreover, either expectation forgets continuous configuration data; neither selects an outcome character or creates a record. A factive wall would additionally require a readout context and instrument. What the calculation supplies is a Haar-carrier prototype. The interacting same-carrier wall map and its uniform flux inequality remain open.

## Classical Fisher information realizes the real denominator

A commuting tangent to the vacuum measure has the form

$$
\dot\nu=f\nu_\Gamma,
\qquad
\int f\,\mathrm d\nu_\Gamma=0.
$$

For a real score \(f\), the classical Fisher metric, equivalently the commuting restriction of the BKM metric, is

$$
g^{\mathrm{BKM,comm}}_{\nu_\Gamma}
(\dot\nu,\dot\nu)
=
\int f^2\,\mathrm d\nu_\Gamma.
$$

Define the score-to-vector identification and its flux form by

$$
\dot\nu=f\nu_\Gamma
\longmapsto
U_0f=\psi_{0,\Gamma}f,
\qquad
\mathcal E_{\mathrm{flux}}(\dot\nu)
:=
\mathcal E_\Gamma(f,f).
$$

This identification is the differential of the classical Hellinger embedding \(\nu\mapsto2\sqrt{\mathrm d\nu/\mathrm d\mu_\Gamma}\): for \(\dot\nu=f\nu_\Gamma\), its differential is precisely \(f\psi_{0,\Gamma}=U_0f\). Thus the Fisher norm equals the real Hilbert norm in this convention.

Because the real Schrödinger operator and its quadratic form split into real and imaginary parts, the Rayleigh infimum may be taken over real \(f\). Consequently,

$$
\boxed{
\frac{\Delta_\Gamma}{\kappa_a}
=
\inf_{\dot\nu\perp1}
\frac{
\mathcal E_{\mathrm{flux}}(\dot\nu)
}{
g^{\mathrm{BKM,comm}}_{\nu_\Gamma}(\dot\nu,\dot\nu)
}.
}
$$

This is a classical configuration-space realization, not the full quantum BKM geometry of all physical vacuum perturbations. The physical Born map uses \(\sqrt p\), not the Hellinger convention \(2\sqrt p\). For an amplitude path \(\psi_\varepsilon=\psi_0(1+\varepsilon h)\), the induced probability score is \(2\operatorname{Re}h\); pure phase directions are invisible to \(\nu_\Gamma\) even though they can carry Hamiltonian energy. Homogeneity cancels the factor two in the real Rayleigh quotient, but no claim about all quantum tangent directions follows.

The types now remain separate:

| Structure | Role |
|---|---|
| gauge expectation \(E_{\mathcal G}\) | selects the physical invariant carrier |
| electric derivatives \(X_e^A\) | measure flux variation along configuration directions |
| vacuum density \(\psi_0^2\) | weights which configurations occur in the ground state |
| classical Fisher/BKM norm | measures a real probability-score tangent |
| Dirichlet form | measures the energetic cost of that tangent |
| Rayleigh infimum | supplies the dimensionless coercivity relative to the kinetic normalization |
| \(\kappa_a\) and its RG limit | attach physical energy units |

This is the exact content available for the claim that mass is a property of facts rather than of little objects: a gap is a lower bound on the energetic cost of a physical distinction from the vacuum. It does not identify every fact with a particle or every Fisher tangent with an on-shell state.

## Entropy enters through a decay rate

Let \(\mathcal A_0\) be the full physical sigma algebra and let \(\mathcal A_{n+1}=\mathbb C1\). For a finite nested family

$$
P_t:=e^{-t\mathscr L_\Gamma}
$$

be the reversible Markov semigroup of the ground-state-transformed operator. Then

$$
\frac{\mathrm d}{\mathrm dt}
\operatorname{Var}_{\nu_\Gamma}(P_tf)
=
-2\mathcal E_\Gamma(P_tf,P_tf).
$$

The Poincare inequality is therefore equivalent to exponential \(L^2\) relaxation,

$$
\operatorname{Var}_{\nu_\Gamma}(P_tf)
\leq
e^{-2(\Delta_\Gamma/\kappa_a)t}
\operatorname{Var}_{\nu_\Gamma}(f).
$$

For an evolving probability density \(u_t\) relative to \(\nu_\Gamma\), the relative entropy obeys the de Bruijn identity

$$
-\frac{\mathrm d}{\mathrm dt}
\operatorname{Ent}_{\nu_\Gamma}(u_t)
=
\int
|\nabla\log u_t|^2u_t\,\mathrm d\nu_\Gamma.
$$

A logarithmic Sobolev inequality would turn this into exponential entropy decay, but it is stronger than the Poincare inequality needed for a spectral gap. Entropy is therefore not the dimensional yardstick. The selected *rate at which variance or entropy can relax under the named generator* is the relevant inverse time.

Before the ground-state transform is tied to the Hamiltonian, \(t\) is Markov depth. After the unitary equivalence above, or after an Osterwalder--Schrader transfer construction, \(\hbar/\Delta_\Gamma\) is a physical correlation time. This is where time and energy enter; the logarithm alone supplies neither.

## Orbit-space curvature is a sufficient route

For the pushed-forward measure

$$
\mathrm d(q_*\nu_\Gamma)
=
e^{-W_\Gamma}\mathrm{dvol}_{G_\Gamma},
$$

the weighted curvature is

$$
\operatorname{Ric}_{\nu_\Gamma}
=
\operatorname{Ric}_{G_\Gamma}
+
\operatorname{Hess}_{G_\Gamma}W_\Gamma.
$$

Under the usual smooth completeness hypotheses, a lower bound

$$
\operatorname{Ric}_{\nu_\Gamma}
\geq
\rho_\Gamma G_\Gamma,
\qquad
\rho_\Gamma>0,
$$

implies a Poincare bound and hence a gap. This is the geometric programme proposed in [[library/orbit-space-curvature-as-a-source-of-mass-in-quantum-gauge-theory/inq|Moncrief--Marini--Maitra]] and developed conditionally in [[library/a-geometric-approach-to-the-yang-mills-mass-gap/inq|Mondal]].

The important refinement is that pointwise positive weighted Ricci curvature is sufficient, not necessary. Yang--Mills orbit space is stratified, has flat directions in some curvature components, and becomes infinite dimensional in the continuum. A direct Poincare, Cheeger, transport, or multiscale estimate may survive even when a global pointwise curvature lower bound does not.

There is also a circularity firewall. The weight \(W_\Gamma\) contains the unknown exact ground state of the same Hamiltonian. Computing its curvature from already known spectral decay would merely repackage the gap. A useful proof must control \(\operatorname{Ric}_{\nu_\Gamma}\), or another functional-inequality constant, from the bare kinetic metric, plaquette interaction, orbit Jacobian, gauge constraints, and regulator data without assuming the desired gap or long-distance clustering.

## A finite strong-coupling bound

When the orthogonal complement of the constants in the gauge-invariant carrier is nontrivial, let \(\lambda_1(K_\Gamma|_{\mathrm{phys}})\) be its first kinetic eigenvalue and define

$$
\operatorname{osc}(V_\Gamma)
:=
\sup V_\Gamma-\inf V_\Gamma.
$$

The min--max principle gives

$$
\boxed{
\Delta_\Gamma
\geq
\kappa_a\lambda_1(K_\Gamma|_{\mathrm{phys}})
-
\operatorname{osc}(V_\Gamma).
}
$$

This is positive whenever

$$
\kappa_a\lambda_1(K_\Gamma|_{\mathrm{phys}})
>
\operatorname{osc}(V_\Gamma),
$$

which gives a controlled finite-lattice strong-coupling criterion. It is not the Clay estimate: its lower bound can deteriorate with volume, and the continuum trajectory is weakly coupled in lattice units.

## Gauge descent is not energy evolution

Gauge averaging satisfies \(E_{\mathcal G}^2=E_{\mathcal G}\), so \(1-E_{\mathcal G}\) has an exact projection gap on the unphysical complement. Its kernel, however, is the entire gauge-invariant carrier, not the vacuum line. A gauge Casimir likewise vanishes on gauge-invariant observables.

Therefore

$$
\text{removal of redundancy}
\neq
\text{Hamiltonian relaxation within the physical sector}.
$$

This is a second category error worth quarantining. Descent constructs the carrier on which the gap question can be asked. It does not answer the question by itself.

The wall expectations already in the workspace can still define a comparison form, but only after transporting them to one common carrier. Suppose each \(E_i\) is an orthogonal conditional expectation for the same \(L^2(\nu_\Gamma)\) inner product, or a self-adjoint projection for one declared common GNS/BKM inner product. Put

$$
\mathscr L_{\mathrm{wall}}
:=
\sum_i c_i(1-E_i),
\qquad
c_i>0.
$$

Its kernel is

$$
\ker\mathscr L_{\mathrm{wall}}
=
\bigcap_i\operatorname{Ran}E_i.
$$

An ergodicity theorem reducing this intersection to \(\mathbb C1\), followed by a vacuum-preserving intertwiner and comparison with \(\mathcal E_\Gamma\), would turn descent into a genuine coercive bound without identifying expectation with time evolution. Mere state preservation does not ensure positivity, self-adjointness, or the kernel identity above. Finite-index or Q-system data alone proves none of these steps.

## Multiscale descent can localize the missing inequality

Let

$$
\mathcal A_0
\supset
\mathcal A_1
\supset\cdots\supset
\mathcal A_{n+1}
=
\mathbb C1,
$$

let \(E_j\) be the \(L^2(\nu_\Gamma)\)-orthogonal conditional expectation onto \(L^2(\mathcal A_j,\nu_\Gamma)\). Thus \(E_0=I\) and \(E_{n+1}f=\int f\,\mathrm d\nu_\Gamma\). The martingale differences

$$
D_j:=E_j-E_{j+1}
$$

are mutually orthogonal, so for mean-zero \(f\),

$$
\lVert f\rVert_2^2
=
\sum_j\lVert D_jf\rVert_2^2.
$$

Consequently, a scale-local flux estimate

$$
\mathcal E_\Gamma(f,f)
\geq
\sum_j c_j\lVert D_jf\rVert_2^2
$$

implies a global Poincare bound with constant \(\inf_j c_j\). This is a concrete role for descent: isolate what each scale contributes to distinguishability, then prove that electric flux charges every nonconstant shell. The difficult statements are the existence of vacuum-preserving expectations compatible with gauge locality and a lower bound on \(c_j\) that survives arbitrarily many shells. A formal tower without these estimates is only a decomposition, not a gap theorem.

[[physical-distinction-coercivity]] separates this energetic shell statement from the superficially similar discreteness of a measurement projection. It also states a possible noncommutative continuum gate: if nested subalgebras are invariant under one faithful vacuum modular flow, Takesaki's theorem supplies vacuum-preserving expectations whose GNS implementations are orthogonal. Constructing such a useful filtration is a strong sufficient architecture, not a necessary consequence of having a gap.

## The continuum theorem to pursue

Let \(a\) be lattice spacing and \(L\) physical volume. Define the energy form after ground-state transform by

$$
\mathfrak h_{a,L}(f,f)
:=
\left\langle
U_{0,a,L}f,
(H_{a,L}-E_{0,a,L})U_{0,a,L}f
\right\rangle.
$$

The decisive estimate has the form

$$
\boxed{
\mathfrak h_{a,L}(f,f)
\geq
\gamma_{\mathsf s}\Lambda_{\mathrm{YM}}^{(\mathsf s)}
\lVert f\rVert_{L^2(\nu_{a,L})}^2,
\qquad
\int f\,\mathrm d\nu_{a,L}=0,
}
$$

with one \(\gamma_{\mathsf s}>0\) uniform in \(L\) and along a tuned continuum sequence \(a\to0\) representing fixed \(\Lambda_{\mathrm{YM}}^{(\mathsf s)}\). A raw gap in lattice units should tend to zero on that trajectory; what must remain positive is the ratio in physical RG units. Both \(\gamma_{\mathsf s}\) and \(\Lambda_{\mathrm{YM}}^{(\mathsf s)}\) are scheme-labelled, while their product is physical.

This inequality would still have to be accompanied by:

1. a nontrivial continuum limit of the local gauge-invariant observables and vacuum state;
2. reflection positivity or a direct positive-energy Hamiltonian reconstruction;
3. a unique vacuum and control of every physical sector, not only a chosen scalar channel;
4. locality and Poincare covariance in the limit; and
5. identification of the limiting \(\Lambda_{\mathrm{YM}}^{(\mathsf s)}\) in one declared scheme or replacement by a scheme-independent observable ratio.

The operator problem has therefore become concrete. The Clay track is to prove uniform vacuum-measure coercivity. The deeper ontology track may ask why the RG yardstick has its realized value, but it must not be used to hide the missing coercivity theorem.

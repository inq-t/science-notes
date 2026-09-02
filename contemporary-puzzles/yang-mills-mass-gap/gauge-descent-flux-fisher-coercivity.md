# The Yang--Mills Gap as Gauge-Descended Flux Coercivity

At a finite lattice regulator, the Yang--Mills Hamiltonian gap is exactly a Poincare constant of the ground-state-weighted electric-flux form. On the real multiplication sector, its \(L^2\) denominator has an exact classical Fisher-score realization. This turns the philosophical inversion into a theorem: mass is not a substance added to a gauge field, but coercivity of the physical vacuum geometry. The theorem is exact at finite regulator. The unsolved problem is to construct the continuum theory and retain a positive bound in physical renormalization-group units, uniformly in volume and regulator removal.

**Status: [EXACT REGULATED THEOREM; OPEN CONTINUUM PROGRAMME].** The ground-state transform below is standard elliptic analysis on a finite product of compact groups. It neither proves existence of four-dimensional continuum Yang--Mills nor supplies the uniform estimate that would prove its mass gap.

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

For an orthonormal Lie-algebra basis indexed by \(A\), let \(X_e^A\) be the corresponding invariant vector field on the copy of \(SU(3)\) assigned to edge \(e\). The electric-flux Laplacian is

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

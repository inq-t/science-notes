# Symmetry Without a Random Trigger

An invariant state evolving by equivariant dynamics remains invariant. An unstable potential does not supply a symmetry-selecting datum, and quantum variance is not itself a sequence of random kicks. This gives a rigorous target for an asymmetry-first theory: derive the observed algebra, effective symmetric dynamics, and conditioned state from a deeper formation law. It does not establish that uncertainty requires mass, that spontaneous symmetry breaking means absence of cause, or that state selection implies a Yang--Mills gap.

## The invariant-state obstruction

Let \(\mathcal A\) be an observable algebra, \(\alpha_g\) a symmetry action, \(\tau_t\) its time evolution, and \(\omega\) a state. Suppose

$$
\alpha_g\tau_t=\tau_t\alpha_g,\qquad
\omega\alpha_g=\omega.
\tag{ST1}
$$

Then \(\omega_t=\omega\tau_t\) obeys

$$
\boxed{\omega_t\alpha_g
=\omega\tau_t\alpha_g
=\omega\alpha_g\tau_t
=\omega\tau_t=\omega_t.}
\tag{ST2}
$$

In a Hilbert-space presentation, the sufficient conditions are
\(U_g\rho_0U_g^*=\rho_0\) and commutation of \(U_g\) with the time-evolution unitaries. They imply \(U_g\rho_tU_g^*=\rho_t\). For unbounded \(H\), “commutes with \(H\)” means the corresponding strong spectral commutation, not merely a formal commutator on an unspecified domain.

A symmetric wavepacket can spread away from an unstable hilltop while its state remains symmetric. This theorem does not deny asymmetric branches, environmental conditioning, or nonunique equilibrium phases. It says the complete invariant state does not become a uniquely selected asymmetric state through the stated equivariant evolution alone.

Classically, an exactly critical configuration with zero velocity remains there when the evolution has that equilibrium and a unique solution. Instability means that nearby initial data depart; it does not specify which nearby data were prepared. Calling an unstable critical point “perfectly stable” confuses stationarity with stability.

## What spontaneous symmetry breaking does and does not claim

For a genuine global symmetry, equilibrium symmetry breaking concerns states: symmetry can permute distinct extremal ground or equilibrium states even when the governing law is invariant. A standard selection procedure uses a symmetry-selecting source or boundary condition, takes a thermodynamic limit, and only then removes the source. The order of limits matters. This is a mathematical phase structure, not the definition of an event without a reason.

It leaves a different question open: which state describes a particular physical preparation, and why? The label “spontaneous” does not make that question meaningless, and the potential alone does not answer it.

[[rg-covariance-residue/regular-gauge-averages-and-the-selection-obstruction|The group-mean selection obstruction]] gives a related finite example: a symmetric collection of open transports can have no definite group-valued output compatible with all its input symmetries. A regular averaging map needs an explicit domain and selection data. This is a theorem about that map's codomain, not a proof that a gauge representative is a physical outcome or that quantum statistics require mass.

Local gauge transformations require a further distinction. [[library/impossibility-of-spontaneously-breaking-local-symmetries/inq|Elitzur's theorem]] obstructs ordinary spontaneous breaking of local gauge symmetry under its lattice hypotheses without gauge fixing. A gauge-variant field direction is not by itself a physical orientation chosen by nature. [[higgs-reduction-as-local-shadow/inq|The reduction picture]] separates gauge-covariant direction, invariant radial data, and physical spectra.

There is also a concrete correction to the cosmic story. At the physical Higgs mass, [[library/standard-model-cross-over-on-the-lattice/inq|D'Onofrio and Rummukainen's Standard Model calculation]] finds a smooth thermal electroweak crossover, not a genuine symmetry-breaking phase transition. Their “broken” and “symmetric” labels refer conventionally to low- and high-temperature regimes. The calculation uses an effective theory matched to the Standard Model; it is not direct observation of primordial history or proof of an ontological random trigger.

Heating and cooling are two directions through an equilibrium family; that family alone does not derive the universe's initial condition or ontological arrow. Conversely, identifying symmetry more clearly at high temperature or high probe energy is not a theorem that arbitrary additional energy always produces more symmetry. Temperature, collision energy, resolution, and a change of state have different types.

## Uncertainty is not a microscopic shaking trajectory

[[library/the-uncertainty-principle/inq|Robertson's inequality]] concerns variances in a state. For a normalized vector \(\psi\) in the requisite domains, set

$$
u=(A-\langle A\rangle)\psi,\qquad
v=(B-\langle B\rangle)\psi.
$$

Cauchy--Schwarz gives the domain-safe form

$$
\Delta_\psi A\,\Delta_\psi B\ge
|\operatorname{Im}\langle u,v\rangle|.
\tag{ST3}
$$

If the products needed for the commutator are defined, this becomes
\(\Delta_\psi A\,\Delta_\psi B\ge\tfrac12|\langle[A,B]\rangle_\psi|\).
No mass parameter, gravitational collapse condition, or detector model occurs in this deduction.

For an electromagnetic mode relative to a specified observer and mode decomposition,

$$
X=\frac{a+a^\dagger}{2},\quad
Y=\frac{a-a^\dagger}{2i},\quad
[a,a^\dagger]=1
\quad\Longrightarrow\quad
[X,Y]=\frac{i}{2},\quad
\Delta X\,\Delta Y\ge\frac14.
\tag{ST4}
$$

The vacuum has \(\Delta X^2=\Delta Y^2=1/4\). It is nevertheless stationary under the free mode Hamiltonian. A stationary probability distribution with nonzero variance is not a classical trajectory jittering through definite values. Nor does the mode require a photon rest frame: its frequency is defined relative to the observer's time, not the photon's nonexistent proper-time clock.

Preparation variance is also not the same quantity as measurement error or disturbance. [[library/uncertainty-noise-and-disturbance/inq|Ozawa's analysis]] separates them and shows why the simple error-times-disturbance version is not universally valid. Replacing state uncertainty by a detector-disturbance story would conflate these registers again.

[[library/observation-of-squeezed-states-in-an-optical-cavity/inq|Optical squeezing experiments]] observe phase-dependent electromagnetic noise below the calibrated vacuum level in one quadrature. Their cavities, atoms, and detectors are material. That is an important limit on what was observed: not an apparatus-free radiation-only universe. But it does not imply that apparatus mass generates the field commutator. An alternative theory must reproduce the preparation, propagation, and measurement correlations, not merely note the detector's presence.

The admissible upstream hypothesis is therefore stronger and cleaner than “photons have no uncertainty”: explain why this noncommutative mode algebra and its state statistics appear in a formed observational context. Its mathematical recovery need not identify quantum probabilities with fundamental indeterminism.

## A gravitational localization wall is an additional construction

An order-of-magnitude localization argument may combine

$$
E\sim\frac{\hbar c}{L},
\qquad
r_s\sim\frac{GE}{c^4},
\qquad
r_s\lesssim L
\quad\Longrightarrow\quad
L^2\gtrsim\frac{\hbar G}{c^3}.
\tag{ST5}
$$

Numerical coefficients and operational conditions are deliberately not fixed here. This is a heuristic combining quantum localization energy with a gravitational collapse scale, not a theorem for arbitrary measurements. It adds \(G\), gravitational geometry, and a localization model to the quantum assumptions. It cannot serve as the definition or proof of (ST3), which needs none of those additions.

The proposed causal wall may explain both structures in a deeper model. The burden is to construct two return maps and recover their different regimes, not declare them identical because both limit an observation.

## An asymmetry-first construction with a definite test

Let a candidate upstream carrier have an ontic law \(T\), an observational formation map \(q_c\), and a rule \(\mathsf W_c\) producing local states or statistical weights. The required output is

$$
(\mathfrak W,T,c)
\xrightarrow{\ \mathsf{Form}\ }
(\mathcal A_c,\omega_c,\tau_c,G_c).
\tag{ST6}
$$

The state rule is indispensable. Noninjectivity, a torsor, or an inaccessible fiber alone does not assign probabilities to alternatives. Deterministic dynamics plus a specified state/weight rule can induce observational statistics; the statistics alone do not prove or disprove that ontology.

Three different questions now have explicit places:

1. **Why this observable symmetry?** Derive the action of \(G_c\) on the formed algebra. The [[higgs-reduction-as-local-shadow/inq|kernel-stabilizer quotient]] gives one exact algebraic mechanism for lifted symmetry; it does not yet select the Standard Model.
2. **Why this state or outcome?** Specify which upstream or conditioning datum is not invariant, or which limit selects an extremal state. If all supplied data and maps remain equivariant and the starting state is invariant, (ST2) forbids a unique asymmetric return by that evolution alone.
3. **Why a nonzero neutral spectral floor?** Prove a uniform response estimate on a source-complete physical family and reconstruct its energy--momentum representation. Neither an asymmetric state nor a discrete outcome supplies this estimate.

[[rg-covariance-residue/inq|The covariance-residue theorem]] makes the third question more concrete: every correlation is a retained part plus a sum of correlations in forgotten distinctions. The required bound must control both. This is a useful sense in which “the reason is in what was forgotten,” without mistaking loss of access for a proof of mass.

Pure Yang--Mills contains no Higgs field. Explaining or replacing the Higgs story therefore cannot, by itself, discharge the Clay problem. A deeper theory must recover that pure-gauge limit and its strictly positive gap independently of the electroweak construction.

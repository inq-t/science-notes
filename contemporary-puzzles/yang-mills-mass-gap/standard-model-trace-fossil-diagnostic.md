# The Standard-Model Trace Fossil Diagnostic

The thermal Standard Model supplies a direct diagnostic for the claim that the \(46.27\,\mathrm{MeV}\) causal-grain presentation marks when mass or nonconformality “switched on.” At zero chemical potential, equilibrium thermodynamics gives \((\rho-3p)/\rho=4(1-g_{*s}/g_{*\rho})\). At the Saikawa--Shirai central values, the \(46.284\,\mathrm{MeV}\) row gives about \(0.0845\), while selected rows across \(150\)--\(200\,\mathrm{MeV}\) give about \(0.25\)--\(0.31\). Thus \(46\,\mathrm{MeV}\) is not a maximum among these selected central rows, and the table supplies no distinguished onset criterion there. Without covariance-aware uncertainty propagation, this is a central-value diagnostic rather than a statistical exclusion. It does not falsify the primitive causal-grain proposal, but it blocks an effortless identification and forces any surviving claim to name a different operator, threshold, or transported profile.

**Status: [EXACT] for the equilibrium identity; [EXACT WITHIN A FREE EQUILIBRIUM GAS MODEL] for the boson and fermion trace formulas; [EXACT UNDER HOMOGENEOUS SAME-SECTOR CONSERVATION] for the FLRW scale-rate form; [NUMERICAL DIAGNOSTIC] for the sampled central table values and bracketed ideal-gas stationary points; [HEURISTIC] for an instantaneous relaxation-to-Hubble comparison; [OPEN] for uncertainty propagation, an interacting kinetic threshold, a wall-to-thermal map, and any CMB/BAO consequence.**

## The local trace rate from two degree counts

Work in \(k_B=\hbar=c=1\) at negligible chemical potential. The equilibrium identities

$$
s=\frac{\rho+p}{T},
\qquad
\rho=\frac{\pi^2}{30}g_{*\rho}T^4,
\qquad
s=\frac{2\pi^2}{45}g_{*s}T^3
$$

give

$$
p=Ts-\rho,
\qquad
\boxed{
\frac{\Theta}{\rho}
:=
\frac{\rho-3p}{\rho}
=
4\left(1-\frac{g_{*s}}{g_{*\rho}}\right).}
\tag{ST1}
$$

If \(N=\log a\), \(T=T(N)\) follows a homogeneous FLRW trajectory, and this same stress sector is conserved so that \(\mathrm d\rho/\mathrm dN=-3(\rho+p)\), then [[trace-residue-as-a-scale-cocycle]] makes this the local logarithmic-scale rate

$$
\frac{\Theta}{\rho}
=
\frac{\mathrm d}{\mathrm dN}\log(a^4\rho).
\tag{ST2}
$$

With inter-sector energy transfer \(Q\) defined by \(\dot\rho+3H(\rho+p)=Q\), the right side of (ST2) becomes \(\Theta/\rho+Q/(H\rho)\). The sampled quantity is a dimensionless scalar constructed from thermal expectation values of the stress tensor. The map \(T\mapsto\Theta(T)/\rho(T)\) is an equation-of-state diagnostic, not itself a mass operator or Hamiltonian.

## The \(46\,\mathrm{MeV}\) row lies below the crossover and the selected central maximum

Selected central rows from [[library/primordial-gravitational-waves-precisely/inq|the Saikawa--Shirai Standard-Model table]] give:

| \(T\) | \(g_{*\rho}\) | \(g_{*s}\) | \(4(1-g_{*s}/g_{*\rho})\) |
|---:|---:|---:|---:|
| \(20.054\,\mathrm{MeV}\) | \(11.3260\) | \(11.2390\) | \(0.0307\) |
| \(46.284\,\mathrm{MeV}\) | \(14.3149\) | \(14.0125\) | \(0.0845\) |
| \(100.324\,\mathrm{MeV}\) | \(17.7666\) | \(17.3524\) | \(0.0932\) |
| \(150.039\,\mathrm{MeV}\) | \(27.1715\) | \(25.4504\) | \(0.2534\) |
| \(175.512\,\mathrm{MeV}\) | \(35.6643\) | \(32.8791\) | \(0.3124\) |
| \(200.014\,\mathrm{MeV}\) | \(41.0951\) | \(38.1086\) | \(0.2907\) |
| \(299.129\,\mathrm{MeV}\) | \(52.3468\) | \(49.8756\) | \(0.1888\) |

These are central-value diagnostics. The table supplies separate theoretical-error columns but no covariance matrix; because \(g_{*\rho}\) and \(g_{*s}\) arise from the same equation-of-state construction, treating them as independent is unjustified. No significance is therefore assigned to the central-value ordering. The \(46\,\mathrm{MeV}\) row lies well below the chiral-crossover band and in the low-temperature hadronic regime, whereas larger selected central values occur across the crossover. [[library/equation-of-state-in-2-plus-1-flavor-qcd/inq|HotQCD]] locates the chiral crossover around \(145\)--\(163\,\mathrm{MeV}\), not at \(46\,\mathrm{MeV}\).

Consequently, the following statements are inequivalent:

1. QCD becomes nonperturbative and crosses into its hadronic regime;
2. stable hadronic rest-bearing sectors become available;
3. a species such as the pion becomes sufficiently nonrelativistic to alter dwell or abundance strongly;
4. a primitive pre-clock carrier changes admissibility or coercivity; and
5. the later acoustic observables retain an image of one of those changes.

The equation of state directly constrains the first claim as an equilibrium thermodynamic crossover and can reflect changes in thermally populated species. It does not establish the second as a spectral or stability theorem; its low-temperature hadronic description already assumes the relevant states. A \(46\,\mathrm{MeV}\) pion or hadron threshold would require a separate kinetic and abundance calculation. The fourth is the proposed causal-grain ontology, and the fifth is a transfer problem. Numerically similar energy presentations do not identify these concepts.

## An illustrative single-species pion trace shoulder

There is nevertheless a physically typed reason to inspect the quotient \(m_\pi/T\). For one free spin-zero Bose species at zero chemical potential, put \(x=m/T\). Its interaction measure is

$$
\frac{\rho-3p}{T^4}
=
\frac{g}{2\pi^2}
x^3
\sum_{n=1}^{\infty}\frac{K_1(nx)}{n}.
\tag{ST3}
$$

This is the trace carried by that thermally populated species, not its mass spectrum. Differentiation gives

$$
\frac{\mathrm d}{\mathrm dx}
\left[
x^3
\sum_{n=1}^{\infty}\frac{K_1(nx)}{n}
\right]
=
x^2
\left[
2\sum_{n=1}^{\infty}\frac{K_1(nx)}{n}
-
x\sum_{n=1}^{\infty}K_0(nx)
\right].
\tag{ST4}
$$

Numerically, the stationary maximum bracketed on \(1<x<5\) occurs at

$$
x_{\max}\simeq2.302863,
\qquad
T_{\max}^{\pi^\pm}
=
\frac{m_{\pi^\pm}}{x_{\max}}
\simeq60.607\,\mathrm{MeV}.
\tag{ST5}
$$

The Maxwell--Boltzmann \(n=1\) approximation instead gives \(x_{\max}\simeq2.386736\) and \(T_{\max}^{\pi^\pm}\simeq58.478\,\mathrm{MeV}\). At the conditionally retyped grain value \(T_g=46.2747\,\mathrm{MeV}\),

$$
x_g=\frac{m_{\pi^\pm}}{T_g}\simeq3.01613,
\qquad
\frac{\mathcal I_\pi(x_g)}{\mathcal I_\pi(x_{\max})}
\simeq0.91865,
\tag{ST6}
$$

where \(\mathcal I_\pi(x)\) denotes the dimensionless Bose shape in (ST3). This says only that the isolated charged-pion ideal-gas contribution lies on the low-temperature side of a broad thermal maximum. Degeneracy cancels from the position and normalized ratio, but a physical pion gas contains three slightly nondegenerate charge states and interacts with the rest of the plasma. More decisively, the shape is generic to every massive ideal species: repeating the calculation with the alternating Fermi series for the muon gives a stationary point \(x\simeq2.453869\), \(T\simeq43.058\,\mathrm{MeV}\), and a normalized shape about \(0.99381\) at the same retyped grain temperature. The pion comparison is therefore a compatibility observation, not an independent particle selector, event criterion, or large-fraction claim for the total Standard-Model trace.

A genuine kinetic threshold must start from the coupled distributional carrier \(\delta f=(\delta f_a)_a\) of every participating species. A pion-only carrier requires a derived bath or open-system reduction. Let \(\mathcal C_T\geq0\) be a proper-time linearized collision operator on a declared weighted kinetic Hilbert space, with collisional invariants quotiented out and sign convention

$$
\partial_t\delta f
=
-\mathcal C_T\delta f
+\mathcal L_{H,T}\delta f
+\delta S.
$$

Here \(\mathcal L_{H,T}\) is the expansion/redshift Liouville term, not merely the scalar \(H\). If \(\gamma_\pi(T)\) denotes the relevant nonzero edge of the reduced collision operator, then

$$
\boxed{
\frac{\gamma_\pi(T_*)}{H_{\mathrm{FLRW}}(T_*)}=1}
\tag{ST7}
$$

is only an order-one instantaneous timescale diagnostic. Tracking an evolving equilibrium profile can instead compare \(\gamma_\pi\) with \(|\mathrm d\log f_{\mathrm{eq}}/\mathrm dt|\), and survival of a perturbation depends on the mode-resolved optical depth

$$
\tau_\gamma(N_1,N_2)
=
\int_{t_1}^{t_2}\gamma_\pi(t)\,\mathrm dt
=
\int_{N_1}^{N_2}\frac{\gamma_\pi(N)}{H(N)}\,\mathrm dN.
\tag{ST7a}
$$

The operator acts on distributional distinctions; the full collision-plus-Liouville evolution diagnoses which relax and which survive as a record. Existing early-universe kinetics already makes the generic pion reading implausible at \(46\,\mathrm{MeV}\). [[library/unstable-hadrons-in-hot-hadron-gas/inq|Kuznetsova and Rafelski]] treat decay together with inverse formation, while [[library/cosmological-strangeness-abundance/inq|Yang and Rafelski]] find several reaction-specific loss-of-balance temperatures below \(34\,\mathrm{MeV}\), not one universal hadronic freeze-out. As a crude scale check, standard radiation domination gives \(H(46.27\,\mathrm{MeV})\simeq1.67\times10^3\,\mathrm{s}^{-1}\), whereas the charged-pion vacuum lifetime gives \(\tau_{\pi^\pm}^{-1}/H\simeq2.30\times10^4\). Vacuum decay is not itself the interacting relaxation edge, but it decisively shows that a \(46\,\mathrm{MeV}\) match would have to concern a specifically derived, much slower projected collective mode—not generic pion relaxation.

## The selected integrated residues do not yield a canonical unit nat

For an adiabatic thermal history, selected endpoint pairs give

$$
\Xi_\Theta(T_1\to T_2)
=
\log\frac{g_{*\rho}(T_2)}{g_{*\rho}(T_1)}
-
\frac43\log\frac{g_{*s}(T_2)}{g_{*s}(T_1)}.
\tag{ST8}
$$

Using the same central rows while the universe cools,

$$
\begin{aligned}
\Xi_\Theta(299.129\to46.284\,\mathrm{MeV})&\simeq0.39619,\\
\Xi_\Theta(150.039\to46.284\,\mathrm{MeV})&\simeq0.15485,\\
\Xi_\Theta(100.324\to46.284\,\mathrm{MeV})&\simeq0.06903,\\
\Xi_\Theta(299.129\to20.054\,\mathrm{MeV})&\simeq0.45607.
\end{aligned}
\tag{ST9}
$$

These residues accumulate the entire interval; choosing \(46\,\mathrm{MeV}\) as an endpoint does not localize their source at \(46\,\mathrm{MeV}\). Moreover, \(\Xi_\Theta\) generally varies continuously with the endpoints, so even a tuned interval on which it happened to equal one would not thereby be canonical. None of the displayed intervals yields one, an integer, or a \(6^2\) datum, and no independent rule selects these endpoints. The informative failure is narrower: neither choosing \(46\,\mathrm{MeV}\) as an endpoint nor integrating the standard thermal trace over these legible thermal ranges automatically recovers the primitive scale valuation. A nontrivial wall-to-material theorem would have to select the profile and interval before these numbers are examined.

## What survives of the shell-casing hypothesis

The strongest surviving possibility is not

$$
46\,\mathrm{MeV}
=
\text{the Standard-Model trace turn-on}.
$$

It is the typed chain

$$
\text{pre-clock transition class}
\longrightarrow
\text{restricted thermal/constitutive profile}
\longrightarrow
\text{predeclared weighted fossil signatures}
\longrightarrow
\text{CMB/BAO data}.
\tag{ST10}
$$

For a nonzero one-profile amplitude model, nonzero overlap with at least one predeclared acoustic response kernel is exactly the local noiseless injectivity condition. A multi-parameter profile requires full restricted rank, a nonlinear family requires a separate global-identifiability argument, and stable inference requires a positive post-nuisance singular value. [[trace-residue-as-a-scale-cocycle#The fossil readout is a quotient operator|The finite-rank fossil theorem]] states these distinctions. If a literal resonance is intended, the theory must instead construct a propagating or response operator with a mode, pole, or spectral enhancement near an independently selected scale and recover the correlated phase pattern. The standard BAO ruler is produced by photon--baryon acoustic evolution and later drag freeze-out; an earlier mass-engagement event can be its causal antecedent only through a derived background, constitutive, active-source, or initial-condition channel.

The diagnostic rejects identifying \(46\,\mathrm{MeV}\) with the standard chiral-crossover scale, the maximum among the selected central \(\Theta/\rho\) rows, a particle-specific ideal-gas shoulder, or generic pion freeze-out. **Any surviving \(46\,\mathrm{MeV}\) hypothesis must independently define a slower projected kinetic mode, a different hadronic or algebraic threshold, or a nonthermal presentation of the grain, and then derive its transfer to observables; numerical proximity alone is not evidence.**

[[receipts/standard_model_trace_fossil_receipt.py|The arithmetic receipt]] reproduces the selected-row values, the endpoint residues, and the ideal-pion trace-shape calculation.

# Calibrated Presentation Holonomy and Spectral Return

Returning the same complete spectral experiment is stronger than returning the same spectrum. For the finite prepared physical carrier, a unitary that fixes every prepared source and one actual heat step must be a scalar phase. A positive gap also forbids an exact nontrivial rescaling around a closed presentation loop, but that implication assumes the gap. These statements give a precise calibration condition without forbidding physical gauge holonomy, identifying modular spectra with particle energies, or deriving a scale.

## The object transported is an experiment

Use a nontrivial finite incidence or access construction on its entire physical carrier. In the ground-state presentation of [[prepared-sources-and-the-modular-wall|the source-to-wall theorem]], write
\[
\mathcal H=L^2(Q,\nu),\qquad \Omega=1,\qquad
H\ge0,\qquad \ker H=\mathbb C\Omega,\qquad T_t=e^{-tH}.
\tag{CH1}
\]
Here \(H\) is the centered returned physical Hamiltonian after the ground-state unitary transport. Its source multiplication algebra is
\[
\mathcal A_0=\{M_F:F\text{ is a prepared physical source}\}''
=L^\infty(Q,\nu).
\tag{CH2}
\]
[[prepared-readout-algebra-and-physical-source-completeness|Prepared readout completeness]] proves this equality using faithful matrix entries, their pointwise algebra and joint gauge averaging. It is not an assumption that Gaussian expectation preserves products.

A presentation path \(\gamma:x\to y\) must specify its Hilbert-space unitary, vacuum transport, source-label transport and clock normalization. Gauge changes of description are compared after that declared source pullback. A change of physical background or preparation is a different experiment, even when it uses the same coordinate labels.

Centering the Hamiltonian in (CH1) does not discard the original ground-energy scalar. [[closed-normalization-and-cosmic-response|Closed normalization]] retains it and its source dependence in the full amplitudes. The following operator statements do not authorize a source-dependent renormalization of those amplitudes.

## Complete calibration leaves only a scalar phase

Let a closed presentation path return a unitary \(U_\gamma\) on \(\mathcal H\). Assume that its returned experiment has exactly the same source actions and one heat step:
\[
U_\gamma M_FU_\gamma^*=M_F
\quad\text{for every prepared }F,\qquad
U_\gamma T_{t_0}U_\gamma^*=T_{t_0},
\qquad t_0>0.
\tag{CH3}
\]
The source labels in this formula have already been transported back. Equality of a selected spectrum or of a few expectation values is weaker than (CH3).

**Complete-calibration theorem.** Under (CH1)--(CH3),
\[
\boxed{U_\gamma=e^{i\vartheta_\gamma}I.}
\qquad
U_\gamma\Omega=\Omega\ \Longrightarrow\ U_\gamma=I.
\tag{CH4}
\]
Indeed the finite heat-kernel theorem proves
\[
W^*(\mathcal A_0,T_{t_0})=B(\mathcal H).
\tag{CH5}
\]
Equation (CH3) puts \(U_\gamma\) in this algebra's commutant, which is \(\mathbb C I\); unitarity fixes its modulus. This reuses the exact strict-heat-positivity proof in the source-to-wall owner. It is not a claim that arbitrary quantum field nets satisfy (CH5) by definition.

Thus complete calibration fixes presentation holonomy up to a phase invisible to these observables and the vacuum ray. If presentation maps compose, their scalar loop phases compose multiplicatively. This does not select the phases, derive the complex scalar field, or prove compactness of the physical gauge group: the theorem starts on a complex Hilbert carrier. It also does not say that every gauge connection is flat.

Preserving \(H\)'s spectrum alone cannot establish (CH4). Even commuting with \(H\) leaves nontrivial spectral unitaries, such as \(e^{isH}\); those generally move the prepared multiplication observables. The source algebra is the additional information that makes the conclusion possible.

## A positive gap excludes scale holonomy only conditionally

Suppose a family of centered physical clocks and presentation maps satisfies
\[
H_y=a_\gamma U_\gamma H_xU_\gamma^*,\qquad
a_\gamma>0,\qquad U_\gamma D(H_x)=D(H_y).
\tag{CH6}
\]
The positive scalar compares the declared clock units or family normalizations. Which interpretation is intended must be specified, as in [[mass-scale-calibration/scale-torsor-and-the-global-local-gap-invariant|the scale-torsor comparison]]. For a closed presentation path at \(x\), assume the same operator is returned and
\[
0<\Delta_x:=\inf\sigma(H_x|_{\Omega_x^\perp})<\infty.
\]
Functional calculus transports the kernel and nonvacuum spectrum, giving
\[
\boxed{\Delta_x=a_\gamma\Delta_x
\quad\Longrightarrow\quad a_\gamma=1.}
\tag{CH7}
\]
The more general [[mass-scale-calibration/internal-yardstick-as-a-generalized-rate-edge#Why an invariant edge cannot fix an unpointed scale|unitary-rescaling obstruction]] already proves that even one exact nontrivial rescaling of a nonzero positive operator produces spectral values approaching zero by iteration. Equation (CH7) is its closed-presentation corollary.

This is not a converse. Trivial scale holonomy does not imply a gap; a gapless clock can have identity presentation transport. Nor does (CH7) select \(\Delta_x\), the transmutation scale, or a dimensionless positive lower bound. [[physical-response-coercivity/conditional-vacuum-rigidity-and-the-physical-gap|Complete physical susceptibility]] remains the separate source-response criterion for proving that bound.

## Physical phase holonomy can change a spectrum

Consider the circle carrier \(L^2(S^1,d\theta/2\pi)\), periodic domain \(H^2(S^1)\), and the dimensionless family
\[
H_\alpha=(-i\partial_\theta-\alpha)^2,\qquad
H_\alpha e^{in\theta}=(n-\alpha)^2e^{in\theta},
\qquad n\in\mathbb Z.
\tag{CH8}
\]
The flat \(U(1)\) connection has holonomy \(e^{2\pi i\alpha}\). For an integer \(k\), multiplication by \(e^{ik\theta}\) is a single-valued unitary and
\[
U_kH_\alpha U_k^*=H_{\alpha+k}.
\tag{CH9}
\]
This is a gauge change with the same spectrum, relabeled by \(n\mapsto n-k\). Changing \(\alpha\) modulo integers changes the physical holonomy and can change the spectrum. For example, \(H_0\) has ground energy zero, while \(H_{1/3}\) has ground energy \(1/9\); their centered first gaps are respectively \(1\) and \(1/3\).

The distinction is exact: unitary changes of gauge presentation preserve a fixed experiment, while changing its gauge-invariant flux changes the experiment. A phase acquired around a physical loop need not be the scalar presentation operator in (CH4). Flat curvature on a noncontractible circle also need not mean trivial holonomy. The blanket rule that phase holonomy cannot affect spectral lines is therefore too strong.

## Keep the physical clock separate from regional modular data

[[regional-preparation-algebras-and-vacuum-support|Regional support]] gives a concrete reason not to identify every local modular generator with the physical frequency standard. Pure subdivision transports the whole physical vacuum and clock, while changing the regional cut can change the Schmidt support and the represented regional algebra. The asymmetric two-plaquette cut cannot have a separating vacuum for its full regional factor; a balanced cut admits faithful preparations. These are statements about regional algebras, not changes of the underlying transported physical spectrum.

[[modular-recurrence-and-the-regional-limit|Modular recurrence]] further shows that the faithful type-I factor preparations considered there cannot realize a proper exact common-vector half-sided modular inclusion. The required regional limit and its identification with physical translations remain constructions to prove. A universal modular normalization does not itself fix a particle mass or the conversion to a physical proper-time clock.

The useful next compatibility test is consequently a square of actual maps: does changing physical presentation before scale or access transport give the same sourced, normalized return as doing it afterward? [[scale-score-connection/inq|The scale connection]] and [[transport-intertwining-defect/connection-and-generator-conventions|the induced derivative on maps]] supply its existing differential language once carriers and transports are constructed. An ordinary connection over one scale interval has no curvature two-form; a mixed defect needs at least the additional presentation direction. Neither naming that defect an anomaly nor imposing (CH3) supplies the missing transport law.

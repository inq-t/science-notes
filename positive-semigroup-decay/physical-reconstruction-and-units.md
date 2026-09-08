# Physical Reconstruction and Units

A common Euclidean correlation exponent becomes an energy bound only after the limiting law supplies the intended Hilbert space, translation semigroup and total family of physical states. The separation coordinate must be a fixed physical Euclidean length. A further Lorentz-covariant joint-spectrum theorem turns that energy bound into an invariant-mass bound; neither step identifies an auxiliary sampling clock with physical time.

## Reconstruct before applying the spectral theorem

Require a limiting Euclidean theory satisfying a full applicable OS reconstruction theorem, including its regularity or growth, covariance and positivity hypotheses. The original [[library/axioms-for-euclidean-greens-functions/inq|Osterwalder–Schrader paper]] and [[library/axioms-for-euclidean-greens-functions-ii/inq|its continuation and correction]] provide the primary reconstruction framework. Reflection positivity by itself constructs a nonnegative pairing; it is not the entire reconstruction theorem.

Suppose that reconstruction supplies \((\mathcal H,\Omega)\), a vacuum-normalized Hamiltonian \(H-E_0\), and

$$
T(s)=e^{-sA},
\qquad
A=\frac{H-E_0}{\hbar c}\geq0
\tag{ARL16a}
$$

with \(s\) Euclidean length along the reconstructed time axis, \(\|\Omega\|=1\), and \(A\Omega=0\). Put \(P_0=\mathbf1_{\{0\}}(A)\) and \(Q=I-P_0\). Centering an observable against \(\Omega\) removes only that vacuum line. It puts its reconstructed vector in \(Q\mathcal H\) only when all ground components have been removed, or vacuum uniqueness has been established.

Require reflected diagonal correlations to equal \(\langle\psi,e^{-sA}\psi\rangle\) for a family whose complex span is dense in \(Q\mathcal H\). If one physical \(\sigma_*>0\) bounds those correlations as in [[positive-semigroup-decay/total-family-spectral-gap|the total-family theorem]], then

$$
\boxed{
H-E_0\geq\hbar c\,\sigma_*Q.}
\tag{ARL18}
$$

This is a bound on the reconstructed energy operator. It does not imply an isolated one-particle pole, discrete excited spectrum, or coverage of charged sectors outside the reconstructed representation.

## Transport the exponent in the correct coordinate

Equal-time spatial clustering needs Euclidean covariance or another proved comparison before it becomes decay along the OS translation direction. The shape and placement of the reflected supports also matter. If their separation satisfies \(r\ge s-d_F\) with a fixed source-dependent physical offset, then
\[
C_F e^{-\sigma_*r}\le C_Fe^{\sigma_*d_F}e^{-\sigma_*s}.
\]
That offset changes a prefactor, not the exponent. A cutoff-dependent offset or uncontrolled source normalization cannot be hidden in a constant claimed uniform through the limit.

Uniform finite-regulator estimates must pass to correlations of one limiting source family and one reconstructed theory. The exponent alone is insufficient when prefactors or onsets diverge with the cutoff. Source-dependent constants are allowed by the spectral theorem after a finite limiting bound has been obtained for each fixed source.

## Invariant mass uses the joint spectrum

For a strongly continuous positive-energy Poincare representation, require Lorentz covariance and the closed-forward-cone spectrum condition. The [[mass-scale-calibration/mass-as-casimir-and-realization#Quantum reversal: mass labels Poincare representation components|joint-spectrum energy–mass equivalence]] then turns (ARL18) into \(M_{\mathrm{gap}}\ge\hbar\sigma_*/c\) on the corresponding nonvacuum representation. Its proof uses Lorentz orbits of spectral points; it does not require normalizable states in a zero-spatial-momentum eigenspace.

The physical law, field identification and nontrivial continuum reconstruction remain part of an application. The semigroup theorem supplies their spectral conclusion conditional on these objects and the common decay estimate; it does not construct them.

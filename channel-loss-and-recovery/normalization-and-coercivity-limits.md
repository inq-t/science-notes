# Normalization and Coercivity Limits

A channel's kernel and positivity do not determine a physical rate, and pointwise nondegeneracy does not determine a global spectral edge. A preserving expectation admits every externally chosen relaxation rate on its forgotten subspace. Any physical lower bound must therefore supply both a quantitative estimate on the full carrier and an independently selected scale.

## The normalization no-go

The descent structure cannot choose its own physical rate. Let \(\sigma\) be a faithful normal state, suppose a \(\sigma\)-preserving ordinary conditional expectation \(E:\mathcal M\to\mathcal N\) exists with \(E\ne I\), and let \(E_2\) be its orthogonal \(L^2(\mathcal M,\sigma)\) implementation. Faithfulness ensures that its forgotten \(L^2\) subspace is nonzero. For every freely chosen \(\gamma>0\),

$$
T_t^{(\gamma)}
:=
E+e^{-\gamma t}(I-E)
=
(1-e^{-\gamma t})E+e^{-\gamma t}I
\tag{D5i}
$$

is a normal unital completely positive \(\sigma\)-preserving semigroup. Its positive \(L^2\) generator is

$$
\boxed{
L_2^{(\gamma)}
=
\gamma(I-E_2),}
\tag{D5j}
$$

whose lower edge on \(L^2(\mathcal N)^\perp\) is exactly \(\gamma\). The same inclusion, expectation, state, kernel, and distinction split therefore admit every positive relaxation gap merely by changing an external number.

This gives the decisive **[EXACT NORMALIZATION NO-GO]**:

$$
\boxed{
\text{descent plus positivity determines a kernel decomposition, not a physical mass scale}.}
\tag{D5k}
$$

For an independently selected KMS-symmetric quantum Markov semigroup on an arbitrary von Neumann algebra, [[library/derivations-and-kms-symmetric-quantum-markov-semigroups/inq|Vernooij and Wirth]] prove, on its canonical KMS \(L^2\) implementation, the first-order factorization

$$
L_2=\delta^*\delta,
\qquad
\mathcal E(\xi)=\|\delta\xi\|^2.
\tag{D5l}
$$

This supplies the operator shape without a trace. It starts with the semigroup and does not select it, its rate, or a gap. A physical realization must derive a Yang--Mills-specific \(\delta\), construct a physically normalized pullback from retained Yang--Mills directions into one or several [[channel-loss-and-recovery/bkm-loss-operators|loss forms such as (D5f)]], prove a regulator-uniform lower frame there, and compare that same-carrier form with reconstructed energy or the Poincare Casimir. Establishing (D5h) on [[channel-loss-and-recovery/preserving-expectation-loss|one preserving expectation's incoming quotient]] is already automatic. [[measured-response-carriers/lazification-and-clock-calibration|Lazification and clock calibration]] isolates the related distinction between a positive discrete step and a physical duration.

The causal grain can therefore do only a sharply typed job here. A Fredholm or Q-system transition may select which descent carrier exists; a logarithmic scale character may normalize its dimensionless response; cosmological data may later calibrate or test a dimensional realization. None of those steps permits setting \(\gamma=46.27\,\mathrm{MeV}\) by unit conversion. The grain must determine the normalization through an independent scale/geometry theorem if it is to contribute more than the topology of forgetting.

## Local invertibility still does not give global coercivity

The Jacobian counterexamples supply the complementary warning. A polynomial map can have an invertible differential at every point and still be globally many-to-one and nonproper. Pulling back a positive target metric then produces a pointwise positive source metric, but this does not give a global inverse, a uniform least singular value, compact resolvent, or a Poincare constant.

That distinction is exactly the one the mass-gap programme needs:

$$
\boxed{
\text{pointwise nondegenerate Hessian or Jacobian}
\not\Longrightarrow
\text{global spectral coercivity}.}
\tag{D18}
$$

[[sufficient-reason/noninvertible-presentation-and-apparent-chance|Noninvertible presentation and apparent chance]] gives the deterministic reading and the groupoid/torsor firewall. Here its analytic lesson is that the stopping condition must control the full carrier and its behavior at infinity, not merely every local chart.

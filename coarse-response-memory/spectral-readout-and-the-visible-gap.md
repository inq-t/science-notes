# Spectral Readout and the Visible Gap

A readout of a positive generator carries a positive operator-valued spectral measure even when its compressed evolution is not an autonomous semigroup. Its first moment is the pulled-back response form, but that moment does not determine the visible threshold. This gives a composable whole-to-local object without requiring every context to be dynamically closed: retain the spectral response, including its hidden-return memory, and state separately when the readouts cover the whole excitation carrier.

## Read the spectral measure, not just the instantaneous rate

Let \(K\ge0\) be self-adjoint on \(\mathcal H\), with spectral measure \(E_K\). Let \(V:\mathcal R\to\mathcal H\) be an isometry and \(P=VV^*\). Define
\[
\boxed{\mathsf M(B)=V^*E_K(B)V,\qquad B\subseteq[0,\infty)\ \text{Borel}.}
\tag{SR1}
\]
This is a normalized positive operator-valued measure on \(\mathcal R\): \(\mathsf M(B)\ge0\), \(\mathsf M([0,\infty))=I\), and disjoint countable unions add weakly. These facts follow by compressing the corresponding projection-valued identities. No invariance of \(V\mathcal R\) under \(K\) is needed.

For bounded Borel \(f\), its integration map is
\[
\int f(\lambda)\,d\mathsf M(\lambda)=V^*f(K)V.
\tag{SR2}
\]
It is unital and completely positive. Positivity at matrix levels follows by applying the spectral calculus to each positive matrix-valued function and then compressing by \(I_n\otimes V\). This is a map from a commutative algebra of spectral functions, not yet a construction of a noncommutative local field algebra.

The exact heat, unitary and resolvent readouts are
\[
\begin{aligned}
R_s&=V^*e^{-sK}V=\int e^{-s\lambda}\,d\mathsf M(\lambda),&&s\ge0,\\
C_t&=V^*e^{-itK}V=\int e^{-it\lambda}\,d\mathsf M(\lambda),&&t\in\mathbb R,\\
G(z)&=V^*(z+K)^{-1}V=\int(z+\lambda)^{-1}\,d\mathsf M(\lambda),&&z>0.
\end{aligned}
\tag{SR3}
\]
The \(R_s\) need not form a semigroup and the \(C_t\) need not be unitary. They are nevertheless coherent readouts of one whole dynamics. [[inq|Coarse response memory]] owns the exact hidden-return equation and Schur resolvent in its stated block-domain setting. Replacing \(R_s\) by a new autonomous local semigroup generally discards that information.

For a vector \(\eta\), the scalar law \(\langle\eta,\mathsf M(\cdot)\eta\rangle\) is a probability measure when \(\|\eta\|=1\). This spectral probability is a mathematical measurement law on a specified carrier; it does not select an outcome or establish an ontological collapse mechanism.

## Projection-valuedness is precisely the reducing case

For every Borel set \(B\),
\[
\boxed{\mathsf M(B)-\mathsf M(B)^2
=V^*E_K(B)(I-P)E_K(B)V\ge0.}
\tag{SR4}
\]
It vanishes exactly when \(E_K(B)V\mathcal R\subseteq V\mathcal R\). Because \(E_K(B)\) is self-adjoint, this is also reduction by that spectral projection. Consequently \(\mathsf M\) is projection-valued if and only if \(V\mathcal R\) reduces every spectral projection of \(K\).

In that case \(K\) restricts to a self-adjoint operator \(K_{\mathcal R}\), with the transported spectral domain, and (SR3) becomes its own semigroup, unitary group and resolvent. Without reduction, these conclusions do not follow from positivity of \(\mathsf M\).

For bounded \(K\), put
\[
A=V^*KV,\qquad B=(I-P)KV.
\]
Then the first two moments satisfy
\[
\boxed{\int\lambda^2\,d\mathsf M(\lambda)-A^2
=V^*K^2V-(V^*KV)^2=B^*B.}
\tag{SR5}
\]
The second-moment defect measures precisely the response sent outside the retained carrier. It is zero if and only if the carrier reduces \(K\). The semigroup's first derivative only sees \(A\); at second order it sees \(B^*B\).

For unbounded \(K\), the first moment is the form
\[
\mathcal E_{\mathcal R}[\eta]
=\int\lambda\,d\langle\eta,\mathsf M(\lambda)\eta\rangle
=\|K^{1/2}V\eta\|^2,
\]
with domain \(\{\eta:V\eta\in\operatorname{Dom}K^{1/2}\}\). That domain must be dense before it defines a self-adjoint form generator on all of \(\mathcal R\). The moment identities must not be treated as bounded operator products without their domain conditions.

[[gauge-star-state-and-hidden-clock|The compact gauge-star construction]]
realizes this moment distinction on a smooth \(SU(2)\) source with a
unique vacuum. Its whole returned Haar state and response form can
remain fixed while the complete centered visible edge approaches zero
with nonvanishing spectral weight. That example needs no hidden zero
mode at any positive parameter; resetting the compressed family to its
first-moment semigroup loses the slow return.

[[charged-link-probes-and-vacuum-spectral-width|The actual Wilson link probe]]
gives an all-spin instance of (SR5). Its finite-dimensional entry
space lies in the smooth operator domain. Independent endpoint
symmetry makes its compressed spectral law scalar: the mean is
\(\kappa j(j+1)\), while the second-moment defect is
\(4\kappa^2j(j+1)I_e/3\), where \(I_e\) is the actual link score
energy. The first moment stays fixed as the vacuum changes; the
width does not. These charged readouts do not cover the neutral
physical excitation carrier or determine a lower threshold.

## Correlation can hide a zero mode from the local form

[[algebra/expected-inclusions-and-mirror-clock-consistency|The mirror-inclusion calculation]]
supplies an actual matrix-state example, not an arbitrary two-by-two block.
It uses the faithful state
\(\rho_{AB}=\operatorname{diag}(9,1,1,9)/20\), its first-factor readout,
and a whole response built from the included first-factor frame.

For a normalized local coherence, the pulled-back rate is one but the spectral measure is
\[
\mathsf m_{\mathrm{coh}}
=\tfrac1{10}\delta_5+\tfrac9{10}\delta_{5/9}.
\tag{SR6}
\]
Its first moment is one, its second-moment excess over one is \(16/9\), and its actual heat readout is a sum of two exponentials, not \(e^{-s}\).

More sharply, for the normalized centered first-factor \(Z\) distinction,
\[
\boxed{\mathsf m_Z=\tfrac{16}{25}\delta_0+\tfrac9{25}\delta_{50/9}.}
\tag{SR7}
\]
Its first moment is two, agreeing exactly with the local form. Yet the actual readout tends to \(16/25\), not zero. The whole row has an untreated second-factor kernel; correlations make that kernel visible from the first factor.

This is not a claim that correlations imply physical gaplessness. This particular whole row was not irreducible on the full carrier. It proves that a local form gap cannot replace an audit of the whole kernel and the actual spectral readout.

## A visible threshold is an all-time statement

Now remove the actual whole vacuum and use a readout into its orthogonal complement. Write \(K_0\) for that nonnegative restriction, and use \(\mathsf M\) for its compressed measure. For \(\delta>0\),
\[
\boxed{
\mathsf M([0,\delta))=0
\quad\Longleftrightarrow\quad
V^*e^{-sK_0}V\le e^{-\delta s}I
\ \text{for every }s\ge0.}
\tag{SR8}
\]
The forward implication integrates the scalar bound on the supported spectrum. Conversely, if a vector measure had positive mass \(m\) in \([0,b]\) with \(b<\delta\), its heat readout would be at least \(m e^{-bs}\), contradicting the asserted estimate for sufficiently large \(s\). The intervals \([0,b]\), \(b<\delta\), exhaust \([0,\delta)\).

Even an estimate \(C e^{-\delta s}\) with one finite \(C\) for all \(s\) gives the same spectral exclusion. A good fit on a bounded interval of \(s\), or a finite list of moments, does not.

For example, \(0<\varepsilon<1\) gives the scalar measures
\[
\mu_\varepsilon=(1-\varepsilon)\delta_1+\varepsilon\delta_\varepsilon.
\tag{SR9}
\]
Their first moments are \(1-\varepsilon+\varepsilon^2\to1\). More strongly, their heat readouts obey
\[
0\le\int e^{-s\lambda}\,d\mu_\varepsilon(\lambda)-e^{-s}
=\varepsilon(e^{-\varepsilon s}-e^{-s})\le\varepsilon
\quad(s\ge0).
\]
Convergence is uniform in absolute error over all nonnegative times. Nevertheless each readout sees a mode at \(\varepsilon\), so there is no common positive threshold for the family. Uniform absolute approximation is weaker than a common relative exponential-decay bound.

The weak limit itself is gapped. The example therefore does not say that every gapped limiting theory must have a uniform gap in every stronger regulator carrier. It says that weak spectral or fixed-time convergence alone does not decide whether disappearing soft modes survive the intended physical observable normalization and completion.

## Covering the actual excitation carrier is a separate requirement

For a family of readouts \(V_i:\mathcal R_i\to\mathcal H_0\), suppose
\[
\overline{\operatorname{span}\bigcup_i V_i\mathcal R_i}=\mathcal H_0.
\tag{SR10}
\]
If every \(\mathsf M_i([0,\delta))=0\) with the same \(\delta>0\), then
\[
E_{K_0}([0,\delta))V_i=0
\]
for every \(i\), since the squared norm is the compressed projection form. Density forces \(E_{K_0}([0,\delta))=0\), hence \(K_0\ge\delta I\). A common visible floor becomes a whole floor only after this coverage is established.

A single readout may instead suffice when its minimal spectral carrier
\[
\mathcal H_{\mathrm{vis}}
=\overline{\operatorname{span}\{E_{K_0}(B)V\eta\}}
\tag{SR11}
\]
is all of \(\mathcal H_0\). It is reducing, and its spectrum is exactly what the compressed measure can detect. Unseen reducing sectors cannot be excluded by its measurements.

Individual positive thresholds are not enough: on \(\ell^2(\mathbb N)\), take \(K_0 e_n=n^{-1}e_n\) and read out each coordinate separately. Each one-dimensional readout has a positive threshold, their ranges span the whole space, and the whole infimum is still zero.

[[algebra/oriented-gram-descent-and-invariant-coverage|The three-loop
orientation test]] supplies the complementary failure: the whole
pairwise-trace carrier is reducing, so all its time-dependent data are
exactly autonomous, but it omits a nonzero gauge-invariant odd sector.
Minimal spectral dilation cannot recover a sector absent from every
input observable. In that finite electric example the missing sector
lies above the lowest even excitation; the point is incomplete
observable coverage, not an incorrectly estimated free gap.

## Inclusion compatibility need not be autonomous-clock compatibility

If \(W:\mathcal R_1\to\mathcal R_2\) is an isometry and \(V_1=V_2W\), then
\[
\boxed{\mathsf M_1(B)=W^*\mathsf M_2(B)W.}
\tag{SR12}
\]
The same relation holds for all bounded spectral functions and hence all readouts in (SR3). It is automatic for compatible whole embeddings even when neither smaller carrier reduces \(K\).

This is weaker than demanding a separate local generator whose exponential is the compression. It is also a meaningful assembly condition: [[global-local-response-reconstruction/compatible-spectral-readouts-and-positive-clock|compatible spectral readouts]] can be assembled and dilated into one positive clock without first supplying the whole Hilbert carrier.

The physical target remains stronger. These spectral maps do not themselves supply gauge-invariant local algebras, spacelike commutation, Poincaré covariance or the Yang--Mills dynamics. Nor does (SR8) derive the positive threshold: it identifies the exact response statement that a geometric or algebraic lower bound must establish on a sufficiently complete family of physical readouts.

[[directed-analytic-realization/preparation-overlaps-and-the-transition-algebra|Preparation transitions]]
give these readouts a concrete whole operator algebra. Their centered
vacuum-created vectors are total on the minimal excitation carrier, so
the coverage criterion above applies to an actual family of returned
operators. This does not establish that those operators are physical
local observables or that their responses share a positive floor.

[[directed-analytic-realization/mirror_inclusion_receipt.py|The finite mirror-inclusion receipt]] and [[directed-analytic-realization/mirror-inclusion-receipt-output.txt|its output]] test the correlated spectral atoms and the bounded moment defect. They do not prove the all-time or limiting assertions, whose proofs and hypotheses are given above.

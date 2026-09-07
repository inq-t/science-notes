# Purification Fluctuation and the Oscillator Return

The full purification fluctuation limit returns an oscillator algebra and a compatible positive clock, not only a Gaussian distribution of state parameters. Coordinate multiplication and its response to the inherited generator supply conjugate operators; their noncentral finite response approaches the canonical commutation relation. The limiting Weyl algebra is preserved by the same clock, and its stationary state action follows. This changes the observable carrier relative to the earlier finite matrix-symbol construction and does not supply spacetime locality, interactions or a Yang–Mills mass scale.

## The carrier and clock are already linked by the parent law

Use [[algebra/purification-response-normalization-and-the-full-clock-limit|the full-clock theorem]]
at fixed \(d\ge2\), \(r=d^2-1\), and \(D=dK\to\infty\).
Whiten the fluctuation coordinates by \(y=G^{-1/2}\xi\). The limiting
Hilbert space, vacuum and closed generator are
\[
\mathcal H=L^2(\mathbb R^r,\gamma),\quad
d\gamma=(2\pi)^{-r/2}e^{-|y|^2/2}dy,\quad
\Omega=1,\quad
\mathcal N=-\Delta+y\cdot\nabla.
\tag{FO1}
\]
The positive semigroup \(e^{-s\mathcal N}\) and unitary clock
\(U_t=e^{-it\mathcal N}\) are returns of the same polynomial-compatible
limit. The actual finite generators satisfy
\(U_D^*H_DU_D=\mathcal N+\mathcal N(\mathcal N-1)/D\).
Here \(U_D\) compares Hilbert spaces, while \(U_t\) is the limiting
clock; their meanings must not be interchanged.

## Conjugacy comes from the response of coordinates

On the complex polynomial core, let \(Q_j\) be multiplication by
\(y_j\). Gaussian integration by parts gives
\[
a_j=\partial_j,\qquad a_j^*=y_j-\partial_j,
\qquad \mathcal N=\sum_j a_j^*a_j.
\tag{FO2}
\]
The star here first denotes the adjoint pairing on the core; closed
operators are specified below. Define the conjugate response by
\[
\boxed{P_j=i[\mathcal N,Q_j]
=i(y_j-2\partial_j)=i(a_j^*-a_j).}
\tag{FO3}
\]
This is extracted from the inherited clock and the coordinate readout,
not an independently chosen matrix multiplication. Direct differentiation
proves
\[
[Q_i,Q_j]=[P_i,P_j]=0,\qquad
[Q_i,P_j]=2i\delta_{ij}I,
\tag{FO4}
\]
and
\[
\boxed{\mathcal N=\frac14\sum_j(Q_j^2+P_j^2)-\frac r2I.}
\tag{FO5}
\]
The constant is fixed by \(\mathcal N\Omega=0\). No new vacuum-energy
subtraction has been fitted to obtain a gap. These are dimensionless
response operators; \(i\) belongs to the complex Hilbert realization.
Dividing both \(Q,P\) by \(\sqrt2\) gives commutator \(iI\), not a
derivation of a dimensional value of \(\hbar\).

There is a finite precursor rather than an unexplained jump to (FO4).
After whitening, the finite generator on polynomials is
\(\mathcal A_D=a^{(D)}_{ij}(y)\partial_i\partial_j-y\cdot\nabla\),
where the co-metric comes from
[[algebra/partial-trace-clock-consistency-and-the-fluctuation-limit|the exact Jordan response]].
For finite coordinate multiplication \(Q_j^{(D)}\), set
\(R_j^{(D)}=i[H_D,Q_j^{(D)}]\) on that core. Then
\[
R_j^{(D)}=i\left(y_j-2\sum_i a^{(D)}_{ij}\partial_i\right),\qquad
[Q_i^{(D)},R_j^{(D)}]=2i\,a^{(D)}_{ij}(y).
\tag{FO6}
\]
The co-metric converges polynomially to \(\delta_{ij}\), so these
identities converge to (FO3)--(FO4) on each fixed polynomial degree under
the theorem's comparisons. For qubits,
\[
a^{(D)}_{ij}(y)=\frac{D+1}{D}\delta_{ij}-\frac{y_iy_j}{D}.
\tag{FO7}
\]
The finite commutator is noncentral. A limiting constant commutator is a
consequence of the flattened response geometry in this regime. No claim
about self-adjoint closures of the finite \(R_j^{(D)}\) is needed here.

## The limiting closures give an actual clock-preserved algebra

The unitary map \(W:\mathcal H\to L^2(\mathbb R^r,dy)\),
\(Wf=\gamma(y)^{1/2}f\), where \(\gamma(y)\) is the displayed
density, gives on polynomial times Gaussian vectors
\[
WQ_jW^*=y_j,\qquad WP_jW^*=-2i\partial_j,\qquad
W\mathcal NW^*=-\Delta+\frac{|y|^2}{4}-\frac r2.
\tag{FO8}
\]
Finite Hermite spans are cores for these essentially self-adjoint
coordinate, derivative and oscillator operators. Thus their closures
define bounded Weyl unitaries
\[
\mathcal W(s,t)=e^{i(s\cdot Q+t\cdot P)},\qquad s,t\in\mathbb R^r,
\]
obeying
\[
\mathcal W(s,t)\mathcal W(s',t')
=e^{-i(s\cdot t'-t\cdot s')}
\mathcal W(s+s',t+t').
\tag{FO9}
\]
The exponent denotes the self-adjoint linear combination in this
Schrodinger realization, not a formal sum of unspecified closures.
The vacuum evaluation is
\(\langle\Omega,\mathcal W(s,t)\Omega\rangle
=e^{-(|s|^2+|t|^2)/2}\).

With the Heisenberg convention \(U_\theta^*(\cdot)U_\theta\),
\[
Q(\theta)=Q\cos\theta+P\sin\theta,\qquad
P(\theta)=P\cos\theta-Q\sin\theta.
\tag{FO10}
\]
Therefore the same clock preserves the Weyl-generated operator algebra.
Its von Neumann closure is \(B(\mathcal H)\): in (FO8), commuting with
all coordinate phase multipliers and translations forces a bounded
commutant operator to be scalar. The vector vacuum is cyclic but not
separating for this whole algebra. This is consistent with the
[[algebra/faithful-stationary-states-and-the-positive-clock|faithful-state restriction]],
not a counterexample to it.

The algebra is not the previously supplied \(M_d(\mathbb C)\) acting
by left multiplication on affine symbols. That
[[algebra/matrix-symbol-realization-and-the-clock-algebra|matrix-symbol clock]]
does not preserve its algebra. The present construction uses all
polynomial fluctuations, coordinate readout and conjugate response to
return a different, infinite-dimensional oscillator algebra. A claimed
identification of these two algebras would undo the type distinction.

## Stationary action is a returned description

The [[algebra/quotient-clock-and-stationary-action|state-action theorem]]
applied to \(\mathcal N\) gives
\[
\mathcal S[\psi]=\int
\left[\frac i2\big(\langle\psi,\dot\psi\rangle
-\langle\dot\psi,\psi\rangle\big)
-\langle\psi,\mathcal N\psi\rangle\right]dt,
\tag{FO11}
\]
on its stated graph-continuous path domain, with endpoint-vanishing
variations. Its stationarity is exactly
\(i\dot\psi=\mathcal N\psi\). This is not a saddle approximation to
an undefined path integral, nor a variational principle selecting the
whole purification process.

The gap is one in the forced-order normalized response duration; with
remaining clock calibration \(\omega\), it is \(\omega\). The source
geometry and original \(\Delta_S/4\) process are still primitive choices.
The \(r\) coordinate modes are internal state distinctions, not spatial
dimensions. Their oscillator return has no constructed spacelike net,
Poincare action or gauge-field interaction. The finite nonlinear degree
correction vanishes in this limit, so this result also identifies the
Gaussian limit's inability to deliver the interacting Clay target by itself.

[[algebra/occupation-conditioned-clocks-and-the-vacuum-boundary|The occupied-background test]]
examines a different limit of that same spectral law. A macroscopic
background occupation shifts the visible oscillator rate after a
sector-dependent subtraction. It does not restore a nonlinear visible
interaction, and forgetting a distribution of background rates prevents
an autonomous clock on the full visible algebra. This is not a vacuum
mass-generation mechanism concealed in the fixed-degree limit.

[[fluctuation_clock_receipt.py|The exact finite receipt]] and
[[fluctuation-clock-receipt-output.txt|its output]] test the polynomial
moments, response, resolvents and commutators. Infinite-dimensional
convergence and closures rely on the proofs, not on those finite tests.

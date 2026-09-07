# Occupation-Conditioned Clocks and the Vacuum Boundary

A visible excitation rate can be a discrete derivative of the whole spectral law, rather than an independently chosen local parameter. For the exact purification clock, conditioning on a macroscopically occupied background retains a background-dependent oscillator rate but removes the visible nonlinear interaction in the limit. Forgetting a nontrivial distribution of background rates gives memory, not one autonomous clock. This is an exact test of a chosen mode readout; its excited reference sector and observable algebra must not be mistaken for the original vacuum or a physical spacetime decomposition.

## The whole clock and the additional mode readout

The [[purification-response-normalization-and-the-full-clock-limit|full-clock theorem]]
transports the purification generator to a Gaussian Hermite carrier:
\[
B_D=h_D(\mathcal N),\qquad
h_D(m)=m+\frac{m(m-1)}D.
\tag{OC1}
\]
Choose a splitting of its whitened modes into nonempty sets \(A,B\).
The Gaussian tensor decomposition gives
\[
\mathcal H=\mathcal H_A\otimes\mathcal H_B,\qquad
\mathcal N=\mathcal N_A\otimes I+I\otimes\mathcal N_B.
\]
The two number operators strongly commute, so their joint spectral
calculus defines all expressions below. Finite Hermite spans are cores.
The split is additional readout data. In particular, the \(B\)-modes
are not the \(K\)-dimensional environment of the original purification,
nor are these mode factors derived spacelike regions. The Hilbert
comparison was not a product-preserving map of the finite density algebra.

Expansion of the same whole clock gives
\[
\boxed{B_D=h_D(\mathcal N_A)+h_D(\mathcal N_B)
+\frac{2}{D}\mathcal N_A\mathcal N_B.}
\tag{OC2}
\]
There is a finite coupling: superpositions of different occupations can
acquire conditional phases and become entangled. It is not legitimate
to call the whole finite clock noninteracting. Its coupling is uniform
between the chosen modes and carries no distance or propagation law.

## The visible rate is a derivative of the whole law

On a background eigenspace \(\mathcal N_B=n\), subtract its reference
value \(h_D(n)\). The visible relative clock is exactly
\[
\boxed{
B_D^{(n)}=h_D(n+\mathcal N_A)-h_D(n)
=\left(1+\frac{2n}{D}\right)\mathcal N_A
+\frac{\mathcal N_A(\mathcal N_A-1)}D.}
\tag{OC3}
\]
Its first visible excitation costs \(1+2n/D\). More generally
\[
h_D(n+k+1)-h_D(n+k)=1+\frac{2(n+k)}D.
\tag{OC4}
\]
The rate is a first discrete derivative; the mixed interaction cost for
increments \(a,b\) is a second one:
\[
h_D(n+a+b)-h_D(n+a)-h_D(n+b)+h_D(n)=\frac{2ab}{D}.
\tag{OC5}
\]
These follow from the parent clock, not a separate fit of its local
rate. The occupation labels count Hermite excitations, not pixels of space.

For \(n_D/D\to\rho\ge0\), let \(c_D=1+2n_D/D\),
\(c=1+2\rho\). Then
\[
B_D^{(n_D)}\longrightarrow c\mathcal N_A.
\tag{OC6}
\]
This is norm-resolvent convergence on the fixed visible carrier. For
\(z>0\), evaluating on degree \(k\) gives
\[
\left\|(B_D^{(n_D)}+z)^{-1}-(c\mathcal N_A+z)^{-1}\right\|
\le\frac{1}{Dc_D^2}+\frac{|c_D-c|}{c_Dc}.
\tag{OC7}
\]
The first term bounds the quadratic correction by comparison with
\(c_D\mathcal N_A\); the second compares two linear rates. At finite
\(D\) the domain is \(\operatorname{Dom}\mathcal N_A^2\), while
the limit has domain \(\operatorname{Dom}\mathcal N_A\).
The unitary groups converge strongly, locally uniformly in time, by
finite-degree approximation. The limiting visible oscillator gap is
\(c\), with remaining common clock calibration still unfixed.

Thus macroscopic occupation retains a rate shift, not the nonlinear
coupling among finitely many visible excitations. The finite mixed
curvature (OC5) still vanishes. This is a moving-sector spectral limit;
the earlier fixed-polynomial convergence of density observations does
not establish their behavior on these high-degree states.

## Changing the reference sector changes the vacuum question

If \(\rho>0\), then
\[
\frac{h_D(n_D)}D\longrightarrow\rho+\rho^2.
\tag{OC8}
\]
The background energy diverges relative to the original constant
vacuum. Subtracting \(h_D(n_D)\) on the whole original carrier would
make that vacuum negative. Positivity of (OC3) is a statement on the
selected sector, not a new positive vacuum Hamiltonian on the old whole.
If the entire background eigenspace \(E_{n_D}\) is retained, the
relative zero space is \(\Omega_A\otimes E_{n_D}\); its dimension
need not be one.

One can instead define the nonnegative relative operator
\(B_D-h_D(\mathcal N_B)\) on the whole tensor carrier. Its kernel
contains \(\Omega_A\otimes\mathcal H_B\). Because the subtraction
commutes with the amplified visible algebra \(B(\mathcal H_A)\otimes I\),
it leaves that algebra's Heisenberg evolution unchanged. It does change
the evolution of operators that move between background occupations.
A sector-dependent subtraction is therefore not an innocuous scalar
shift of the whole dynamics.

## Forgetting the rate produces a memory-bearing readout

For a probability measure \(\mu\) of bounded support in \([0,\infty)\),
retain the background label on
\[
\mathcal K=L^2(\mu;\mathcal H_A),\qquad
(H\Psi)(\rho)=(1+2\rho)\mathcal N_A\Psi(\rho).
\tag{OC9}
\]
The domain requires \(\int(1+2\rho)^2\|\mathcal N_A\Psi(\rho)\|^2
d\mu<\infty\). This is a positive direct-integral clock. The measure
specifies a state/readout pairing; it asserts no ontology of randomness.

Discarding the label gives a unital completely positive Heisenberg map
on the visible algebra:
\[
\Phi_t(X)=\int e^{it(1+2\rho)\mathcal N_A}
X e^{-it(1+2\rho)\mathcal N_A}\,d\mu(\rho).
\tag{OC10}
\]
The integral is understood weakly. For normalized number eigenvectors
\(u_k,u_l\) and \(E_{kl}=|u_k\rangle\langle u_l|\), its factor is
\(\int e^{it(k-l)c}\,d\mu\), where \(c=1+2\rho\).
For \(k\ne l\), the second derivative at zero differs from the
square of the first by
\[
-(k-l)^2\operatorname{Var}_\mu(c).
\tag{OC11}
\]
Hence on the full visible algebra a continuous semigroup composition
law requires \(\operatorname{Var}_\mu(c)=0\). Conversely a single
rate gives a unitary automorphism group. The bounded-support assumption
justifies both derivatives. If only observables commuting with
\(\mathcal N_A\) are retained, every rate gives the identity and
this test cannot distinguish them.

For \(\mu=\tfrac12\delta_0+\tfrac12\delta_1\), the rates are
\(1,3\) and
\[
\Phi_t(E_{10})=e^{2it}\cos(t)E_{10},\qquad
\Phi_{\pi/2}^{\,2}(E_{10})=0\ne-E_{10}=\Phi_\pi(E_{10}).
\tag{OC12}
\]
The same coherence formula holds exactly at finite \(D\) with background
occupations \(0,D\) and visible occupations \(0,1\). A sharp rate at
each conditioned label does not give one autonomous rate after the
label is forgotten.

The revival also rules out interpreting this example as irreversible
record formation or a theorem of monotonically growing entropy.
It supplies a loss of autonomous closure, not the full directed causal
law sought by the programme.

This is distinct from averaging Hilbert amplitudes. With
\(J\psi(\rho)=\psi\), the compressed positive transfer is
\[
R_s=J^*e^{-sH}J=\int e^{-s(1+2\rho)\mathcal N_A}\,d\mu,
\tag{OC13}
\]
not the channel (OC10). It too fails the semigroup law for a nontrivial
bounded rate distribution. [[coarse-response-memory/inq|Coarse response memory]]
owns the general compression mechanism; replacing \(c\) by its mean
would keep only the first spectral moment.

## A minimal spectral carrier need not retain the visible algebra

The zero space of (OC9) is \(L^2(\mu)\otimes\Omega_A\), not
merely the chosen vector \(J\Omega_A\). A useful exact two-rate
test distinguishes removing that degeneracy from preserving observables.
Write \(\mathcal K=\mathbb C^2\otimes\mathcal H_A\),
\(H=\operatorname{diag}(\mathcal N_A,3\mathcal N_A)\), and
\(J\psi=(\psi,\psi)/\sqrt2\). Let
\(\Omega_\pm=(\Omega_A,\pm\Omega_A)/\sqrt2\).
The minimal spectral-cyclic carrier generated by \(E_H(B)J\psi\) is
\[
\mathcal K_{\min}=\mathbb C\Omega_+
\oplus\big(\mathbb C^2\otimes\Omega_A^\perp\big).
\tag{OC14}
\]
For any degree \(m>0\), the distinct energies \(m,3m\) separate
the two components of \(J u_m\). At degree zero only \(\Omega_+\)
appears. This proves (OC14), with a unique vacuum and gap one.

But for a unit degree-one vector \(u\), the retained vector
\(x_-=(u,-u)/\sqrt2\) satisfies
\[
\big(I\otimes|\Omega_A\rangle\langle u|\big)x_-=\Omega_-
\notin\mathcal K_{\min}.
\tag{OC15}
\]
Thus the minimal carrier does not reduce the original amplified visible
algebra. Compressing that algebra again loses its multiplication law.
The [[global-local-response-reconstruction/compatible-spectral-readouts-and-positive-clock|minimal positive spectral realization]]
is valid; it is not, by that fact, a realization of the same observable
algebra with a unique vacuum. This is a concrete instance of the
state/algebra/clock compatibility obligation.

## The remaining construction problem

The whole law constrains the visible rate through (OC3), so it supplies
more than unrelated global and local parameters. Yet a macroscopic
background choice has not generated a vacuum mass, a spatial metric,
a causal cone or a Yang–Mills interaction. The bounded-energy theorem
rules out rescuing this particular spectral correction in the original
vacuum limit. The occupied-sector alternative yields a linear rate,
and forgetting its label introduces memory and an algebraic vacuum
boundary. A physical continuation must supply the background selection,
observable inclusion and clock together, rather than choosing a rate
or deleting zero modes after the fact.

[[directed-analytic-realization/occupation_clock_receipt.py|The exact finite receipt]]
and [[directed-analytic-realization/occupation-clock-receipt-output.txt|its output]]
check the spectral derivatives, sector subtraction, resolvent estimates,
composition defect and minimal-carrier obstruction. The limit and
operator-domain arguments are proved above, not inferred from samples.

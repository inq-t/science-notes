# Characters, Factorization and the Modular Carrier

A multiplicative state has a one-dimensional GNS carrier, so it cannot itself support a nontrivial modular flow or excitation spectrum. Factorization of traced observables can yield such a character on a commutative coordinate algebra without making the noncommutative master-field state multiplicative. The missing information can survive in suitably rescaled connected responses, but their carrier and dynamics require a separate construction. This distinguishes a definite macroscopic presentation from the algebra acting on its possible excitations.

## A character collapses its own cyclic representation

Let \(\chi\) be a normalized positive multiplicative functional on a
unital C*-algebra \(A\), and let
\((\pi_\chi,\mathcal H_\chi,\Omega_\chi)\) be its GNS representation.
For every \(a\in A\),
\[
\begin{aligned}
\|\pi_\chi(a-\chi(a)1)\Omega_\chi\|^2
&=\chi\big((a-\chi(a)1)^*(a-\chi(a)1)\big)\\
&=\chi(a^*a)-|\chi(a)|^2=0.
\end{aligned}
\tag{CF1}
\]
Cyclicity therefore gives
\[
\boxed{\mathcal H_\chi=\mathbb C\Omega_\chi,\qquad
\pi_\chi(a)=\chi(a)I.}
\tag{CF2}
\]
The represented von Neumann algebra is \(\mathbb C I\). Its Tomita
operator is complex conjugation, so \(\Delta_\chi=I\) and its modular
logarithm vanishes. Every unitary group fixing \(\Omega_\chi\) is
the identity. An excitation-gap inequality here is vacuous: the vacuum
complement is zero. It does not construct a nontrivial gapped theory.

This concerns the GNS representation of the character on the declared
whole algebra. A character on a smaller readout context does not collapse
an independently retained larger representation. Nor is a pure state on
a noncommutative algebra generally a character. The
[[faithful-stationary-states-and-the-positive-clock|faithful-state clock theorem]]
and [[directed-analytic-realization/pure-vacuum-loss-and-the-returned-clock|pure-vacuum return]]
depend precisely on such state/algebra distinctions.

## Two different products occur in a master-field description

For matrix words \(p,q\), distinguish a normalized trace \(\tau_N\)
from the evaluation \(\omega_N\) of products of scalar traced probes.
Large-\(N\) factorization, when established, concerns
\[
\omega_N\big(\tau_N(p)\tau_N(q)\big)
-\omega_N\big(\tau_N(p)\big)\omega_N\big(\tau_N(q)\big)
\longrightarrow0.
\tag{CF3}
\]
It does not assert
\[
\tau(pq)=\tau(p)\tau(q)
\tag{CF4}
\]
for the limiting noncommutative word functional. At finite size the
distinction is already exact: for \(x=\operatorname{diag}(1,-1)\) and
\(\tau=\tfrac12\operatorname{Tr}\),
\(\tau(x)=0\) but \(\tau(x^2)=1\).

A commutative coordinate algebra can have distinct generators \(w_p\)
and \(w_{pq}\). Evaluation at one moment law obeys
\(\chi(w_pw_q)=\chi(w_p)\chi(w_q)\), while
\(\chi(w_{pq})\) remains a different quantity. There is no relation
\(w_{pq}=w_pw_q\) merely because their labels contain the same words.
[[library/mastering-the-master-field/inq|Gopakumar--Gross]] use
noncommutative probability and operator master fields; replacing their
word product by multiplication of scalar moments changes the carrier.

Consequently a factorized macroscopic loop law and a nontrivial
master-field representation may coexist. They are not the same state on
the same algebra. Even a noncommutative tracial state has trivial modular
automorphisms in its faithful tracial representation; a proposed
nontrivial modular response requires additional regional state and
inclusion data, not just the word “master field.”

## A definite limiting point can hide a nonzero scaled response

There is a simple exact model. On \(C([-1,1])\), let
\[
\omega_N(f)=\tfrac12f(1/N)+\tfrac12f(-1/N).
\tag{CF5}
\]
For every fixed continuous \(f\),
\(\omega_N(f)\to f(0)=\chi_0(f)\), a character. Yet for the
\(N\)-dependent probe \(F_N(x)=Nx\),
\[
\omega_N(F_N)=0,\qquad \omega_N(F_N^2)=1.
\tag{CF6}
\]
The nonzero response is lost by taking the point limit before rescaling
the probes. This supplies neither a quantum interpretation nor a clock;
it proves that first-order concentration does not exhaust the possible
response data. [[matrix-symbol-realization-and-the-clock-algebra|The matrix-symbol construction]]
owns a separate worked operator realization of fluctuations.

[[purification-response-normalization-and-the-full-clock-limit|The full purification limit]]
goes further for a particular concentrating law: nondegenerate covariance
and a non-frozen continuous clock force its two rescaling orders, and
the whole inherited generator converges under polynomial-compatible
Hilbert comparisons. Its
[[directed-analytic-realization/purification-fluctuation-and-the-oscillator-return|oscillator return]]
constructs a clock-preserved operator algebra. This supplies a worked
response carrier alongside a character limit on density parameters;
it does not establish the corresponding limit for Yang--Mills loops.

For a trace-loop family with connected covariance of order \(N^{-2}\),
one can instead investigate the limit of its \(N^2\)-rescaled connected
pairing and the process acting on its null quotient. Existence,
nondegeneracy, compatibility with composition and physical localization
must be proved. Factorization alone proves none of these, and the
rescaling must not be chosen merely to insert a desired spectral edge.

The constructive question is thus what law supplies both a definite
presentation and its retained response geometry. “Construct a character,
then extract its positive modular rate” discards the nonvacuum carrier
at its first step. A comparison between the character and an independently
constructed response carrier is the missing arrow.

## Factorization amplitude does not determine a spectral edge

Two exact spectral test models make the last obligation visible. For
\(t\ge0\), \(m>0\), consider
\[
C_N(t)=N^{-2}e^{-mt},\qquad
\widetilde C_N(t)=\frac{N^{-2}}{1+t}.
\tag{CF7}
\]
Their positive Laplace measures are respectively
\(N^{-2}\delta_m\) and \(N^{-2}e^{-\lambda}d\lambda\) on
\([0,\infty)\). Thus both define positive reflected kernels
\(C_N(s+t)\), and both vanish at every fixed \(t\) as \(N\to\infty\).
Their \(N^2\)-rescaled responses differ decisively: the first has
spectral edge \(m\), while the second has support arbitrarily close to
zero. The Laplace identity for the latter is the elementary integral
\(\int_0^\infty e^{-(1+t)\lambda}d\lambda=(1+t)^{-1}\).

These are explicit positive-response controls, not large-N Yang--Mills
constructions. They show that a vanishing connected amplitude cannot
determine its normalized decay rate. The
[[coarse-response-memory/spectral-readout-and-the-visible-gap|visible-gap theorem]]
separately requires that the readouts cover the physical spectral carrier.
Rescaling connected probes can recover a candidate response law; it does
not by itself prove that all physical nonvacuum directions are covered.

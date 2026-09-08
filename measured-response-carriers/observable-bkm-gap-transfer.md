# Observable BKM Gap Transfer

A quantum Markov semigroup's exponential GNS contraction rate also holds in each state-induced observable norm associated with a normalized operator-monotone function, including BKM. Wirth's theorem applies to arbitrary von Neumann algebras with a faithful normal invariant state and allows a nontrivial fixed algebra. It supplies an observable norm comparison; passage to the inverse density-tangent metric and to physical energy requires separate maps.

## An operator-monotone gap transfer on arbitrary von Neumann algebras

The transfer theorem concerns observables and their state-induced Hilbert norms. Let
\((\Phi_t)_{t\geq0}\) be a quantum Markov semigroup on an arbitrary von
Neumann algebra with faithful normal invariant state \(\omega\). Suppose it
has GNS gap \(\lambda>0\): in the scalar-fixed case,

\[
\|\Phi_t(x)\|_{\mathrm{GNS}}
\leq
e^{-\lambda t}\|x\|_{\mathrm{GNS}},
\qquad \omega(x)=0.
\tag{MC19e}
\]

[[library/the-kms-and-gns-spectral-gap-of-quantum-markov-semigroups/inq|Wirth's operator-monotone interpolation theorem]],
Corollary 3.7, implies

\[
\boxed{
\|\Phi_t(x)\|_f
\leq
e^{-\lambda t}\|x\|_f}
\tag{MC19f}
\]

for every normalized operator-monotone
\(f:(0,\infty)\to(0,\infty)\), including
\(f_{\mathrm{BKM}}(t)=(t-1)/\log t\), with \(f_{\mathrm{BKM}}(1)=1\). If the fixed-point algebra is \(N\) rather than
\(\mathbb C\mathbf1\), the same result holds on \(\ker E\), where
\(E:\mathcal A\to N\) is the \(\omega\)-preserving conditional expectation
(Remark 3.9). Here \(N\) means the joint fixed algebra of the semigroup.
No GNS-symmetry or detailed-balance hypothesis is needed; the premise is
the exponential norm bound (MC19e), with prefactor one, not merely an
unqualified spectral exclusion for a possibly nonnormal generator.

The norm in this theorem is defined on bounded observables by

\[
\langle x,y\rangle_f
:=\left\langle f(\Delta_\omega)^{1/2}\pi_\omega(x)\Omega_\omega,
 f(\Delta_\omega)^{1/2}\pi_\omega(y)\Omega_\omega\right\rangle,
\qquad f(1)=1.
\]

Its completion is the observable Hilbert space \(H_f\). The source's
Lemma 2.5 gives \(f(\Delta_\omega)\leq I+\Delta_\omega\), so \(x\Omega_\omega\) lies in the required square-root domain for every
\(x\in\mathcal A\).
Proposition 3.5 supplies a strongly continuous contraction semigroup on
\(H_f\). These observable-domain facts already hold in Type III.

The comparison follows by applying the source's Theorem 3.1 to
\(e^{\lambda t}\Phi_t\) on the centered observable subspace, or on
\(\ker E\). The projection onto that subspace is \(*\)-preserving and
GNS orthogonal. For each \(t\), the rescaled map is \(*\)-preserving and
GNS contractive there; operator-monotone interpolation gives (MC19f),
which extends to the Hilbert completion. Squared norms decay with
\(e^{-2\lambda t}\).

## Observable covariance and density-tangent metric

A GNS Markov edge therefore persists in the **observable BKM norm**, even
in Type III. In the finite faithful case, its kernel is the logarithmic
mean \(\mathcal K_\rho\), whereas the relative-entropy Hessian on density
tangents uses \(\mathcal K_\rho^{-1}\).
[[measured-response-carriers/state-tangent-bkm-bridge#The canonical finite-dimensional bridge|The finite score construction]]
defines both metrics and their duality map explicitly.

The interpolation theorem does not prove the state-tangent intertwiner or
the comparison (MC19b)--(MC19c) in the
[[measured-response-carriers/state-tangent-bkm-bridge#A conditional BKM--GNS bridge|conditional BKM--GNS bridge]].
A score or predual identification, its common domain and its physical
range must still be supplied before transporting a bound to the chosen
relative-entropy tangent carrier. In Type III, unbounded modular functions
and their inverses make the
[[measured-response-carriers/state-tangent-bkm-bridge#The Type-III domain and range obligations|domain, closability and range obligations]]
substantive.

Nor does (MC19f) identify the Markov parameter with clock time or its
generator with energy. The
[[measured-response-carriers/lazification-and-clock-calibration|clock-calibration problem]]
remains separate from interpolation. In the
[[categorical-gauge-response/kazhdan-markov-process-carrier#The BKM gain, and its exact limit|Kazhdan--Markov construction]],
the additional input is a state-preserving group action and a chosen
symmetric probability with a Kazhdan lower bound. Interpolation supplies
neither that action nor the physical meaning of one Markov step.

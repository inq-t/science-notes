# Lazification and Clock Calibration

Lazification turns a self-adjoint contraction into a positive contraction and rescales its defect by one half. An injective result admits a self-adjoint logarithmic generator, but physical energy requires an independently constructed transfer interpretation and duration. The spectral calculation supplies neither the clock nor the dimensional normalization.

Use the GNS contraction and vacuum-centered defect of [[measured-response-carriers/measured-operations-and-gns-defects|measured operations and GNS defects]].

## Lazification does not supply a clock

A self-adjoint \(V_\Phi\) need not be positive. The canonical lazification

\[
B_\Phi:=\frac{I+V_\Phi}{2}
\tag{MC13}
\]

obeys

\[
0\leq B_\Phi\leq I,
\qquad
I-B_\Phi=\frac12D_\Phi.
\tag{MC14}
\]

If \(D_\Phi\geq\kappa(I-P_{\Omega_\omega})\), then

\[
B_\Phi(I-P_{\Omega_\omega})
\leq
\left(1-\frac\kappa2\right)(I-P_{\Omega_\omega}).
\tag{MC15}
\]

This remains a dimensionless discrete-step statement. Only after an
independent construction identifies an **injective** \(B_\Phi\) with one
physical Euclidean transfer step of duration \(\tau\) may spectral calculus
define the positive, possibly unbounded operator

\[
H_\tau
=
-\frac{\hbar}{\tau}\log B_\Phi,
\qquad
\operatorname{Dom}(H_\tau)=\operatorname{Dom}(\log B_\Phi).
\tag{MC16}
\]

Injectivity removes a zero spectral projection but does not keep zero out of
the continuous spectrum, so \(H_\tau\) need not be bounded. Iteration
supplies the integer \(n\) in \(B_\Phi^n\). It does not supply
\(\tau\), the equation \(t=n\tau\), or the physical energy interpretation.

# Interacting Comparison Refinement

Repeated positive comparisons can construct a nonlinear clock without requiring every finite comparison width to be an exact duration of that clock. A free Gaussian proximity kernel, weighted by a response derived from a supplied state and configuration metric, has a symmetric product limit equal to the state's full reversible diffusion. A uniformly convex quartic example has a complete positive gap and changes matrix elements as well as spectral rates. The construction is finite-dimensional configuration quantum mechanics; it supplies neither the state from pure algebra nor a physical Yang–Mills clock.

## State, metric and endpoint weighting are the inputs

Work on a declared Euclidean configuration space \(\mathbb R^d\), with Lebesgue measure and mobility \(C=I\). Let
\[
U_\lambda(z)=\frac{|z|^2}{2}+\lambda V(z),\qquad
d\mu_\lambda=Z_\lambda^{-1}e^{-U_\lambda(z)}dz,
\qquad \psi_\lambda=Z_\lambda^{-1/2}e^{-U_\lambda/2}.
\tag{IC1}
\]
Assume \(U_\lambda\) is smooth, \(0<Z_\lambda<\infty\), and the derived function
\[
S_\lambda
=\frac14|\nabla U_\lambda|^2-\frac12\Delta U_\lambda
\tag{IC2}
\]
is bounded below. These assumptions hold for the quartic family below. The endpoint rule (IC2) is a constitutive choice: it is the square-and-divergence response from [[algebra/response-factorization-and-the-vacuum|response factorization]], in the present normalization. It is not inferred from an unknown physical vacuum after the desired Hamiltonian has already been chosen.

On compactly supported smooth functions set
\[
D_\lambda=\nabla+\tfrac12\nabla U_\lambda,\qquad
\mathfrak h_\lambda[u]=\|D_\lambda u\|_2^2.
\tag{IC3}
\]
Smooth coefficients make \(D_\lambda\) closable. Integration by parts gives
\[
H_\lambda=D_\lambda^*D_\lambda
=-\Delta+S_\lambda
\tag{IC4}
\]
as equality of the closed nonnegative form realization and the Schrödinger form sum. To check this equality, add a constant \(b\ge0\) with \(S_\lambda+b\ge0\): on the initial core the squared-response form plus \(b\|u\|^2\) is exactly the sum of the gradient form and \(\int(S_\lambda+b)|u|^2\). Smooth cutoffs and local approximation give the common form closure.

The vacuum belongs to that closure. For cutoffs \(\chi_R\to1\) with \(\|\nabla\chi_R\|_\infty\to0\),
\(D_\lambda(\chi_R\psi_\lambda)=\psi_\lambda\nabla\chi_R\).
Thus \(H_\lambda\psi_\lambda=0\). Conversely a zero-form vector satisfies \(\nabla(u/\psi_\lambda)=0\) weakly, so connectedness gives
\[
\ker H_\lambda=\mathbb C\psi_\lambda.
\tag{IC5}
\]

## The primitive comparison is an explicit free kernel

For \(h>0\), use
\[
k_h(z,z')=(4\pi h)^{-d/2}
\exp\left[-\frac{|z-z'|^2}{4h}\right],
\]
\[
\boxed{F_h
=e^{-hS_\lambda/2}\,e^{h\Delta}\,e^{-hS_\lambda/2}.}
\tag{IC6}
\]
Thus its integral kernel is \(e^{-hS_\lambda(z)/2}k_h(z,z')e^{-hS_\lambda(z')/2}\). The only heat kernel inserted here is the displayed free Gaussian; the desired interacting heat kernel is not primitive data. The same endpoint rule and the same metric apply at every width.

Each \(F_h\) is bounded, positivity preserving and self-adjoint. It is also positive as a Hilbert-space operator:
\[
\langle u,F_hu\rangle
=\|e^{h\Delta/2}e^{-hS_\lambda/2}u\|_2^2\ge0,
\qquad \|F_h\|\le e^{bh}.
\tag{IC7}
\]
It need not fix \(\psi_\lambda\) at finite \(h\), and its ground-transported version need not be a Markov transition at that width. These are positive transfer comparisons; their state preservation is a property of the limit established below.

For every \(t\ge0\), the symmetric product theorem gives
\[
\boxed{F_{t/n}^{\,n}u\longrightarrow e^{-tH_\lambda}u
\quad\text{for every }u\in L^2(dz).}
\tag{IC8}
\]
At \(t=0\) set \(F_0=I\). Apply the standard symmetric Trotter form theorem to \(-\Delta\) and multiplication by \(S_\lambda+b\); their form-domain intersection contains \(C_c^\infty\) and is dense. Removing the scalar \(e^{-bt}\) proves (IC8). The theorem also gives strong convergence uniformly on bounded nonnegative time intervals. Only strong convergence is used here, with no asserted operator-norm error rate. [[library/trotter-kato-product-formula-for-unitary-groups/inq|Exner and Neidhardt]] record the positive-parameter form theorem and its symmetric product in introductory equations (1.3)–(1.4); this invocation is distinct from their subsequent imaginary-time result.

At finite subdivision, composition integrates over all intermediate configuration variables, with half the endpoint weight and full weights on interior vertices. Associativity is exact for those products. What is relinquished is the stronger identity \(F_hF_s=F_{h+s}\) for the original one-step family. The limiting operators have that identity. The [[gaussian-overlap-balancing-and-clock-sewing|Gaussian exact-width classification]] therefore does not exclude (IC8): it classifies a stricter requirement on a different finite comparison family.

## The full returned diffusion is conservative

Multiplication \(\mathcal U_\lambda f=\psi_\lambda f\) is unitary from \(L^2(\mu_\lambda)\) to \(L^2(dz)\). On the transported form domain,
\[
\mathfrak h_\lambda[\mathcal U_\lambda f]
=\int|\nabla f|^2d\mu_\lambda,
\qquad
\boxed{L_\lambda=\mathcal U_\lambda^{-1}H_\lambda\mathcal U_\lambda
=-\Delta+\nabla U_\lambda\cdot\nabla.}
\tag{IC9}
\]
The weighted form is closed, densely defined and Markovian. Its constant function has zero form energy, by the same cutoff argument. Hence its self-adjoint semigroup is positivity preserving, contractive and conservative, with unique constant vacuum. Equivalently, positivity of the limiting transfer and \(e^{-tH_\lambda}\psi_\lambda=\psi_\lambda\) give the actual stationary reversible transition on the supplied state. Equation (IC8) transports to this whole carrier, not just its first coordinates.

When \(\nabla^2U_\lambda\ge mI\), \(m>0\), the complete weighted gap satisfies
\[
\int|\nabla f|^2d\mu_\lambda
\ge m\operatorname{Var}_{\mu_\lambda}(f).
\tag{IC10}
\]
The integrated Bochner identity underlying the bound is
\[
\|L_\lambda f\|_2^2
=\int\left[\|\nabla^2f\|_{\mathrm{HS}}^2
+\nabla^2U_\lambda(\nabla\overline f,\nabla f)\right]d\mu_\lambda
\ge m\langle f,L_\lambda f\rangle.
\tag{IC11}
\]
Cutoffs extend it from the smooth core; spectral calculus excludes spectrum in \((0,m)\), and (IC5) identifies the zero space. For the polynomial quartic members, the transported compactly supported smooth functions are operator cores and the Schrödinger potential tends to infinity, so this argument applies directly to the complete discrete spectrum. The gap is that of the specified configuration response. Its identification with a mass would require a separate physical clock and observable realization.

## A quartic member has a controlled nonlinear response

Choose \(V(z)=|z|^4/4\), \(\lambda\ge0\). Then
\[
\nabla^2U_\lambda
=(1+\lambda|z|^2)I+2\lambda zz^T\ge I,
\]
\[
S_\lambda
=\frac{|z|^2}{4}-\frac d2
+\frac\lambda2\big[|z|^4-(d+2)|z|^2\big]
+\frac{\lambda^2}{4}|z|^6.
\tag{IC12}
\]
This potential is bounded below and tends to infinity for every \(\lambda\ge0\). Local compactness and its tail bound give compact resolvent. Thus (IC8) constructs a full infinite-dimensional \(L^2\) response with a unique vacuum and gap at least one, even though its configuration space is finite-dimensional. The quartic state, its coefficient, the Euclidean metric and the square-and-divergence prescription remain supplied data.

In one dimension, use the normalized flat Hermite basis \(\phi_n\) for
\(N=-\partial_x^2+x^2/4-1/2\), with \(N\phi_n=n\phi_n\). Then
\[
H_\lambda=N+\lambda B+\lambda^2x^6/4,
\qquad B=(x^4-3x^2)/2.
\tag{IC13}
\]
The exact Hermite multiplication rule \(x\phi_n=\sqrt{n+1}\phi_{n+1}+\sqrt n\phi_{n-1}\) gives
\[
B_{nn}=3n^2,\qquad
B_{n+2,n}=\frac{4n+3}{2}\sqrt{(n+1)(n+2)},
\]
\[
B_{n+4,n}=\frac12\sqrt{(n+1)(n+2)(n+3)(n+4)}.
\tag{IC14}
\]
The other nonzero entries follow by symmetry. In particular the interaction changes eigenvectors and the vacuum, not only their energies.

For each fixed \(n\), the ordered eigenvalue has the one-sided expansion
\[
E_n(\lambda)=n+3n^2\lambda+O_n(\lambda^2),\qquad\lambda\downarrow0.
\tag{IC15}
\]
No convergent perturbation series is assumed. For small \(\lambda\), the form bound \(H_\lambda\ge(1-6\lambda)N-3\lambda\) and trial spaces spanned by finitely many Hermite functions give \(E_n(\lambda)\to n\). The vector
\[
\phi_n+\lambda\sum_{j\ne n}\frac{B_{jn}}{n-j}\phi_j
\tag{IC16}
\]
is a finite sum and has residual \(O_n(\lambda^2)\) at energy \(n+3n^2\lambda\). Spectral separation near the integer \(n\) then proves (IC15). This checks the complete one-dimensional levels individually, rather than inferring the gap from a curvature at one point.

The first heat-response derivative on every fixed finite Hermite span is also explicit:
\[
\langle\phi_j,e^{-tH_\lambda}\phi_n\rangle
=\delta_{jn}e^{-nt}-\lambda B_{jn}I_{jn}(t)+O_T(\lambda^2),
\]
\[
I_{jn}(t)=
\begin{cases}
t e^{-nt},&j=n,\\
\displaystyle\frac{e^{-nt}-e^{-jt}}{j-n},&j\ne n.
\end{cases}
\tag{IC17}
\]
Here the remainder is uniform for \(0\le t\le T\), with fixed tested degrees. To justify it, solve the first inhomogeneous evolution using \(N\) and the finite-band matrix \(B\). Substitution into the full equation leaves an \(O_T(\lambda^2)\) residual consisting of finitely many polynomial Gaussian vectors; contraction of \(e^{-tH_\lambda}\) bounds the accumulated error. This is a strong finite-preparation statement, not differentiation in operator norm. Pairings of fixed multiplication observables in \(L^2(\mu_\lambda)\) must additionally transport their endpoint vectors by the actual \(\psi_\lambda\).

## A nonlinear spectral function is a different deformation

The [[algebra/purification-response-normalization-and-the-full-clock-limit|purification full-clock theorem]] transports its finite parent to
\(h_D(N)=N+N(N-1)/D\). That operator changes degree rates while preserving every Hermite eigenspace under its stated Hilbert comparison. In contrast, (IC14) has nonzero matrix elements between different degrees on the canonical Gaussian-to-flat carrier, and (IC1) changes the state used by multiplication observations.

Even first-order eigenvalues can conceal the difference. Taking \(D^{-1}=3\lambda\) formally, and multiplying the purification clock by \(1+3\lambda\), gives
\[
(1+3\lambda)\big[N+3\lambda N(N-1)\big]
=N+3\lambda N^2+O(\lambda^2)
\tag{IC18}
\]
on every fixed Hermite span, matching the diagonal shifts in (IC15). It still has none of the off-diagonal response in (IC17). This comparison concerns the algebraic spectral family; actual purification dimensions retain their integer restrictions. Agreement of a gap, or of first-order level shifts after recalibration, is insufficient to identify the processes or their observable multiplication.

## A partial readout retains a calculable interaction memory

For the two-dimensional radial member write \(z=(x,y)\), and let \(P_\lambda\) be the conditional expectation onto functions of \(x\) in the actual \(\mu_\lambda\) carrier. Put \(Q_\lambda=I-P_\lambda\) and \(m_{2,\lambda}(x)=\mathbb E_{\mu_\lambda}[y^2\mid x]\). The first coordinate belongs to the full generator domain and obeys
\[
L_\lambda x=x+\lambda x(x^2+y^2),\qquad
\boxed{Q_\lambda L_\lambda x
=\lambda x\big[y^2-m_{2,\lambda}(x)\big].}
\tag{IC19}
\]

Let \(J_\lambda f=f(x)\) and \(R_t=J_\lambda^*e^{-tL_\lambda}J_\lambda\). The [[coarse-response-memory/interacting-gauge-vacuum-and-local-memory|conditional-score memory identity]] applies without bounded off-diagonal block assumptions and gives
\[
\lim_{t\downarrow0}t^{-2}
\langle x,(R_{2t}-R_t^2)x\rangle
=\lambda^2\mathbb E_{\mu_\lambda}
\big[x^2\operatorname{Var}_{\mu_\lambda}(y^2\mid x)\big]>0
\quad(\lambda>0).
\tag{IC20}
\]

Strict positivity follows from the positive conditional density on the full real line and nonconstant \(y^2\). The exact coefficient is finite because quartic confinement gives all polynomial moments. As \(\lambda\downarrow0\), the conditional law tends to a standard Gaussian, so the coefficient is \(2\lambda^2+O(\lambda^3)\). One-sided differentiation is controlled here directly: the conditional potential is \(y^2/2+\lambda(x^2y^2/2+y^4/4)\), whose second and higher even moments are bounded by their Gaussian values, while their first derivatives are bounded by polynomials in \(x\). The marginal has uniformly bounded polynomial moments for small nonnegative \(\lambda\). These bounds justify the expansion of the conditional variance and its integral.

This is a positive return defect of an actual interacting process. Its leading hidden response is \(\lambda x(y^2-1)\); the omitted quadratic channel carries information beyond the exact marginal drift. It is not an independently postulated memory force and does not vanish under a scalar clock change.

The revision is therefore specific: replace exact closure of one finite-width formula by a controlled product limit, while keeping the complete boundary integrations and a declared endpoint rule. The [[rg-covariance-residue/gaussian-readout-naturality|all-linear-readout characterization]] proves why constant-mobility autonomy under every linear observation would force a Gaussian state in dimension at least two. Equations (IC19)–(IC20) retain the appropriate defect instead. The algebraic selection of the state and metric, spatial locality, and the field-theory limit remain separate work.

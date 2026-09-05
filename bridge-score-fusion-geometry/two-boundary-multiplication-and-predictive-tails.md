# Two-Boundary Multiplication and Predictive Tails

A boundary pair predicts midpoint distinctions through products of separately propagated observables. Its complete prediction norm therefore depends on both transfer and multiplication, measured in the actual joint endpoint law. Exact sufficient observable algebras survive this product operation; a linear spectral cutoff generally does not. This distinction supplies concrete weighted-kernel and fusion-coefficient tests for discarded prediction.

**Status: [EXACT] conditional-expectation identities and finite certificates; [CONDITIONAL] smoothing bound under stated density hypotheses; [OPEN] for estimates uniform along the interacting Yang--Mills continuum trajectory.** The results are direct operator calculations, not a novelty claim. [[inq|Bridge-score fusion]] owns the physical midpoint carrier and its transfer comparison; [[bridge-data-augmentation-solder/predictive-sufficient-interfaces|predictive sufficient interfaces]] owns the lifting theorem.

## The adjoint multiplies two propagated observables

Let \(P_\ell\) be a stationary reversible Markov kernel on a standard Borel space with probability measure \(\nu\). Let \(Y\) be the midpoint and \(X,Z\) the endpoints, with joint law
\[
\mu(dx,dy,dz)=\nu(dy)p_\ell(y,dx)p_\ell(y,dz).
\tag{TM1}
\]
The conditional independence is a property of this declared law, not an assumption about an ontically random mechanism. The endpoint law is
\[
J(dx,dz)=\nu(dx)p_{2\ell}(x,dz),\qquad p_{2\ell}=p_\ell p_\ell.
\]
The subscript denotes two steps; a continuous semigroup is an additional hypothesis where needed.

Define
\[
K:L^2(\nu)\longrightarrow L^2(J),\qquad
Kf=\mathbb E[f(Y)\mid X,Z].
\]
Its adjoint acts on bounded rectangles by
\[
\boxed{K^*(u\otimes v)=(P_\ell u)(P_\ell v).}
\tag{TM2}
\]
This follows by conditioning first on \(Y\). Finite linear combinations of bounded rectangles are dense in \(L^2(J)\); their norm is the joint-law norm, not a product-prior norm.

For any orthogonal discarded projection \(Q\) annihilating constants,
\[
\delta=\|KQ\|^2=\|QK^*\|^2.
\tag{TM3}
\]
Thus the relevant estimate controls complete combinations of the products in (TM2), including their correlations. Separate bounds on \(P_\ell Q\) do not generally give the same bound on \(KQ\).

## A sufficient algebra and a low-mode span are different objects

Suppose \(Q=I-\mathbb E_\nu[\cdot\mid\mathcal A]\) for an actual observable sigma algebra. If \(P_\ell Q=0\), reversibility gives \(QP_\ell=0\). Every bounded \(P_\ell u\) is then \(\mathcal A\)-measurable, so its products are too. Equation (TM2) and density prove
\[
P_\ell Q=0\quad\Longrightarrow\quad KQ=0.
\tag{TM4}
\]
There is a stronger measurable statement: the minimal statistic defined by the one-end conditional law \(y\mapsto p_\ell(y,\cdot)\) is also the minimal statistic for the pair law \(y\mapsto p_\ell(y,\cdot)\otimes p_\ell(y,\cdot)\). Tensoring constructs the second from the first, and marginalization recovers the first. Joint observation adds predictive strength and products, not a larger minimal predictive sigma algebra.

A retained linear span need not be multiplication-closed. On \(\mathbb Z_2^2\), take the symmetric convolution transition matrix
\[
P(x,y)=\tfrac14\bigl[1+a\chi_1(x)\chi_1(y)
+b\chi_2(x)\chi_2(y)+c\chi_{12}(x)\chi_{12}(y)\bigr].
\tag{TM5}
\]
For \(a,b>0\), \(c=0\), \(a+b<1\), all entries are positive and the Hilbert-space operator is positive. Nevertheless,
\[
P\chi_{12}=0,\qquad
\|K\chi_{12}\|^2=
\frac{2a^2b^2}{1-(a^2+b^2)^2}>0.
\tag{TM6}
\]
Indeed the bridge predictor is \(ab[\chi_1(x)\chi_2(z)+\chi_2(x)\chi_1(z)]/[1+a^2\chi_1(xz)+b^2\chi_2(xz)]\). The span of \(1,\chi_1,\chi_2\) is not a retained observable algebra. This example therefore does not contradict (TM4).

At \(c>0\), \(a+b+c<1\), the exact parity prediction is
\[
\frac{(c+ab)^2}{1+a^2+b^2+c^2}
+\frac{(c-ab)^2}{1-a^2-b^2+c^2}.
\]
It stays positive as \(c\downarrow0\), whereas \(\|P\chi_{12}\|^2=c^2\). Strict Hilbert positivity and a Hamiltonian logarithm do not repair this same-thickness comparison. These particular kernels need not be Markov-semigroup time slices: \(c=0\) forbids a finite-state finite-time exponential, and positive convolution eigenvalues require \(c\ge ab\), \(b\ge ac\), \(a\ge bc\) for a convolution Markov generator.

[[gaussian-bridge-gap-calibration/two-boundary-half-smoothing|The Gaussian and bit-flip calibration]] gives a genuine continuous-semigroup counterexample to a uniform same-thickness comparison, together with a useful half-smoothing repair. [[three-block-bridge-factorization/inq|The high-girth construction]] owns the stronger general failure of inferring a bridge floor from one-ended mixing.

## The insertion is a weighted kernel, not operator division

Assume densities relative to \(\nu\), and write
\[
F_f(x,z)=\int p_\ell(x,y)f(y)p_\ell(y,z)\,\nu(dy).
\]
For bounded \(f\), this is the kernel of \(P_\ell M_fP_\ell\). Then
\[
\boxed{Kf(x,z)=\frac{F_f(x,z)}{p_{2\ell}(x,z)},\qquad
\|Kf\|_J^2=\int\frac{|F_f(x,z)|^2}{p_{2\ell}(x,z)}\,\nu(dx)\nu(dz).}
\tag{TM7}
\]
The ratio is pointwise and defined \(J\)-almost everywhere; set the displayed norm integrand to zero where \(p_{2\ell}=0\). It is never the operator quotient \((P_\ell M_fP_\ell)/P_{2\ell}\). Conditional expectation extends the construction to \(L^2\); an unbounded multiplication operator requires its own domain.

If \(p_{2\ell}\ge m>0\), (TM7) is bounded by \(m^{-1}\|P_\ell M_fP_\ell\|_{\mathrm{HS}}^2\). The denominator cannot simply be discarded. A minimum that tends to zero with area or regulator supplies no uniform theorem.

The Perron-dressed Wilson version is equally important. Let \(\mathcal T_\ell\) have nonnegative symmetric kernel \(k_\ell\) relative to a reference measure \(dU\), normalized so \(\mathcal T_\ell\psi=\psi\), \(\psi>0\), \(\int\psi^2dU=1\). The stationary law is \(\nu=\psi^2dU\), and its density kernel is \(p_\ell(U,Y)=k_\ell(U,Y)/[\psi(U)\psi(Y)]\). With
\[
I_f(U,Z)=\int k_\ell(U,Y)f(Y)k_\ell(Y,Z)\,dY
\]
one gets
\[
\boxed{\|Kf\|^2=
\int\psi(U)\psi(Z)\frac{|I_f(U,Z)|^2}{k_{2\ell}(U,Z)}\,dU\,dZ,\qquad
\|f\|^2=\int\psi^2|f|^2\,dU.}
\tag{TM8}
\]
Again set the integrand to zero on a zero-denominator set. Perron factors cancel inside each normalized bridge fiber but remain in the complete norm. Replacing (TM8) by an unrelated Haar heat bridge changes the law under study.

## A finite multiplication certificate

For a finite reversible chain, choose a real orthonormal eigenbasis \(\phi_a\) in \(L^2(\nu)\), with \(P_\ell\phi_a=\lambda_a\phi_a\). Define the multiplication coefficients and actual endpoint Gram matrix by
\[
C_{ab}^{\,k}=\langle\phi_a\phi_b,\phi_k\rangle_\nu,\qquad
G_{ab,cd}=\sum_k\lambda_k^2 C_{ac}^{\,k}C_{bd}^{\,k}.
\tag{TM9}
\]
The second identity follows from
\(G_{ab,cd}=\mathbb E_J[\phi_a(X)\phi_b(Z)\phi_c(X)\phi_d(Z)]\).
Let \(F\) have columns
\[
F_{ab}=\lambda_a\lambda_b Q(\phi_a\phi_b).
\]
Then
\[
\boxed{\delta=\|F G^{\dagger/2}\|^2,\qquad
\delta\le d\ \Longleftrightarrow\ F^*F\le dG.}
\tag{TM10}
\]
Here \(G^{\dagger/2}\) is the positive square root of the Moore--Penrose inverse on its support. Null endpoint combinations have zero conditional expectation, so \(\ker G\subseteq\ker F\).

This finite certificate uses transfer eigenvalues and multiplication coefficients; it does not assume the bridge answer. It may still be expensive. Replacing \(G\) by the identity, testing only individual columns, or truncating endpoint products without a bound on the omitted actual-\(J\) orthogonal complement is invalid. Character fusion is one structured way to estimate these coefficients; [[compact-heat-bridge-fusion-tail|the compact heat-bridge calculation]] gives a complete high-spin tail.

## A quantitative sufficient-algebra estimate

For \(Q=I-\mathbb E_\nu[\cdot\mid\mathcal A]\), assume
\[
p_{2\ell}\ge m>0,\qquad
R:=\mathop{\mathrm{ess\,sup}}_y\int p_\ell(y,x)^2\,\nu(dx)<\infty,\qquad
\varepsilon:=\|QP_\ell\|_{\mathrm{HS}}^2<\infty.
\tag{TM11}
\]
Then
\[
\boxed{\delta\le\min\{1,4R\varepsilon/m\}.}
\tag{TM12}
\]
To prove it, put \(p_x(y)=p_\ell(y,x)\), \(a_x=\mathbb E[p_x\mid\mathcal A]\), \(d_x=p_x-a_x\). Multiplicative closure gives
\[
Q(p_xp_z)=Q(p_xd_z+a_zd_x).
\]
Each term has \(L^2(\nu(dy)\nu(dx)\nu(dz))\) norm at most \(\sqrt{R\varepsilon}\); for the second use conditional Jensen to bound \(\|a_\cdot(y)\|_{L^2(\nu)}^2\le R\). The square of their sum is at most \(4R\varepsilon\). Applying the weighted insertion formula and the Hilbert--Schmidt bound proves (TM12).

The hypotheses expose the price of this sufficient route: Hilbert--Schmidt discarded smoothing, a row-square envelope, and endpoint nondegeneracy. Each can carry a volume penalty. A one-ended operator norm alone does not supply them.

## What this changes in the gap search

The [[bridge-data-augmentation-solder/predictive-sufficient-interfaces|additive lifting theorem]] works for any orthogonal retained/discarded split on the centered carrier: if retained response has floor \(a\) and discarded prediction has norm squared \(\delta\), then the complete floor is at least \(a-\delta\). An actual coarse-statistic interpretation requires the additional observable-algebra structure.

The immediate target is therefore a law-derived interface with controlled multiplication and the correct endpoint weight, together with a positive retained-response margin. Neither a list of representation dimensions nor positive transfer eigenvalues establishes it. The resulting dimensionless response could constrain physical mass only after the fixed-thickness comparison, continuum existence and OS/Poincare reconstruction in [[inq|the owning bridge theorem]]. Cosmological and vacuum applications may share this signature without sharing a numerical grain, a state, or a boundary law.

[[receipts/two_boundary_prediction_receipt.py|The finite receipt]] tests the product adjoint, actual Gram certificate, sufficient-algebra estimate, parity obstruction and Perron-weighted insertion. It is an algebraic and numerical calibration, not a continuum construction.

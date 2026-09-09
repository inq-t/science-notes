# Anchored Word Cost and the Interacting Return

A weak identity comparison, using the same preparation as the spatial word transfer, returns the complete interacting two-plaquette Hamiltonian. Its magnetic coefficient is a positive moment of the preparation selected by localization, while its electric coefficient is an inverse moment of that same preparation. Their reciprocal scale dependence is exact in the isotropic family. The graph, elementary metric, Gaussian law, comparison strength and duration are declared inputs; this is a finite spatial benchmark return, not a four-dimensional continuum construction.

## Compare each cell word with its identity

Use the two-cell words \(q=(x,y)\), the distance \(d(q,q')\), and the shared preparation \(\Xi\in E=M_2(\mathbb C)\oplus M_2(\mathbb C)\) of [[spatial-word-comparison-and-mixed-motion|spatial word comparison]]. The pairing is the sum of \(\operatorname{Tr}(A^\dagger B)/2\), \(\Xi\) is circular complex Gaussian with covariance \(\Gamma>0\), and \(S=\|\Xi\|^2\). The main example is \(\Gamma=I_E\), so \(S\sim\operatorname{Gamma}(8,1)\). Define
\[
V(q)=2-a-b,\qquad a=\tfrac12\operatorname{Tr}x,\quad b=\tfrac12\operatorname{Tr}y,
\qquad
\|(x-I)\Xi\|^2+\|(y-I)\Xi\|^2=2SV(q).
\tag{AW1}
\]
Thus \(V\ge0\) is the sum of the two declared cell identity comparisons. Fix \(\beta\ge0\) and use the duration \(\epsilon=1/\alpha\). At each transfer edge set
\[
f_{\alpha,q}(\Xi)=e^{-\beta SV(q)/(2\alpha)},\qquad
K_{\alpha,\beta}(q,q')=
\mathbb E_\Gamma\!\left[f_{\alpha,q}e^{-\alpha Sd(q,q')^2}f_{\alpha,q'}\right].
\tag{AW2}
\]
The same preparation carries the spatial and identity rows. Its identity cost per step is proportional to the step duration. This extensive-action prescription is an input, rather than a consequence of Gaussian positivity.

Keep the exact unmarked spatial row normalization
\[
z_\alpha=\int\mathbb E_\Gamma e^{-\alpha Sd(q,q')^2}dq',
\qquad (F_{\alpha,\beta}\psi)(q)=z_\alpha^{-1}\int K_{\alpha,\beta}(q,q')\psi(q')dq'.
\tag{AW3}
\]
The scalar \(z_\alpha\) is independent of \(q\) and \(\beta\). It is not the row degree of the new damped kernel.

## Positivity and the full Gaussian source law

For each fixed \(\Xi\), the kernel in (AW2) is the positive Gaussian distance kernel multiplied at its two endpoints by \(f_{\alpha,q}>0\). The injective embedding argument of the spatial owner therefore proves positivity and injectivity on the full Haar \(L^2(SU(2)^2)\). Since \(0<K_{\alpha,\beta}\le K_{\alpha,0}\), symmetry and the row bound give \(\|F_{\alpha,\beta}\|\le1\) by the Schur test. Thus it is an exact positive self-adjoint contraction, and is sub-Markov rather than necessarily conservative. It preserves the simultaneous-conjugation invariant carrier.

For arbitrary \(j\in E\), \(T=T^\dagger\), with \(\Gamma^{-1}+T>0\), define
\[
\begin{aligned}
A_{q,q'}^{\alpha,T}
&=\Gamma^{-1}+\left[\alpha d(q,q')^2+
\frac\beta{2\alpha}(V(q)+V(q'))\right]I_E+T,\\
K_{\alpha,\beta}^{j,T}(q,q')
&=\frac{\exp\!\left[j^\dagger(A_{q,q'}^{\alpha,T})^{-1}j\right]}
{\det\Gamma\,\det A_{q,q'}^{\alpha,T}}.
\end{aligned}
\tag{AW4}
\]
This inserts \(e^{2\Re(j^\dagger\Xi)-\Xi^\dagger T\Xi}\) in the actual Gaussian integral. All linear and quadratic sources on the spatial words and identity rows pull back to (AW4), including cross-context blocks. These source derivatives hold the original unmarked \(z_\alpha\) fixed; changing the covariance prescription itself must also transport its normalization. The conditional covariance is \((A_{q,q'}^{\alpha,T})^{-1}\); no word receives an independently reset preparation. For \(\Gamma=I_E\), the unmarked kernel is exactly
\[
K_{\alpha,\beta}(q,q')=
\left[1+\alpha d(q,q')^2+\frac\beta{2\alpha}(V(q)+V(q'))\right]^{-8}.
\tag{AW5}
\]

## One preparation returns both coefficients

Define its localization moments
\[
\rho_\Gamma=\frac{\mathbb E S^{-4}}{\mathbb E S^{-3}},
\qquad \eta_\Gamma=\frac{\mathbb E S^{-2}}{\mathbb E S^{-3}},
\qquad \kappa=\frac{\rho_\Gamma}{15},\quad \lambda=\beta\eta_\Gamma.
\tag{AW6}
\]
With the right-multiplication derivatives and \(Q=-2\operatorname{Tr}\) convention fixed by the spatial owner,
\[
\boxed{F_{\alpha,\beta}\psi
=\psi-\alpha^{-1}H_\lambda\psi+O_\psi(\alpha^{-2}),\qquad
H_\lambda=4\kappa(D_{Q,x}+D_{Q,y})-2\kappa\sum_AR_{x,A}R_{y,A}
+\lambda(2-a-b).}
\tag{AW7}
\]
Here \(\beta,\Gamma\) are fixed, and the estimate holds on smooth functions in the uniform norm. To prove the new term, expand the endpoint factors as
\(f_{\alpha,q}f_{\alpha,q'}=1-\beta S(V(q)+V(q'))/(2\alpha)+O(\alpha^{-2}S^2)\), uniformly in the frames. Localization in six configuration dimensions gives the weight \(S^{-3}\). Consequently the normalized integral with one extra \(S\) is \(\eta_\Gamma\psi+O_\psi(\alpha^{-1})\); with two extra powers its row norm is bounded by a constant proportional to \(\mathbb E S^{-1}/\mathbb E S^{-3}\). The linear term therefore contributes \(-\beta\eta_\Gamma V\psi/\alpha\), with controlled \(O(\alpha^{-2})\) remainder. The pure spatial remainder is already proved using moments through \(\mathbb E S^{-5}\). All these moments are finite in complex dimension eight. Using the exact same \(z_\alpha\) cancels the unmarked scalar geometric correction.

The operator (AW7) is uniformly elliptic with smooth bounded real potential on the compact product, with form domain \(H^1\), operator domain \(H^2\), and smooth core. Positivity of the potential makes it nonnegative. Contractivity and telescoping the smooth-core expansion give
\[
\boxed{F_{n/t,\beta}^{\,n}\psi\longrightarrow e^{-tH_\lambda}\psi}
\tag{AW8}
\]
strongly on the full Haar carrier and on its complete simultaneous-invariant subspace, uniformly for bounded nonnegative times, with the identity at zero. Smooth semigroup orbits have bounded required norms on those intervals; density and contractivity extend their error estimate to all \(L^2\) vectors.

For \(\Gamma=I_E\), \(\rho_\Gamma=1/4\) and \(\eta_\Gamma=5\). Hence
\[
\boxed{\kappa=\frac1{60},\qquad \lambda=5\beta,
\qquad \frac\lambda\kappa=300\beta.}
\tag{AW9}
\]
This is the complete operator of [[coarse-response-memory/two-plaquette-vacuum-and-relational-state|the two-plaquette benchmark]], not just a match of one observable. Its simple positive vacuum, angular dependence and perturbative expansion therefore follow from that owner. For every \(\beta>0\), the vacuum depends on the signed relational variable \(z=\mathbf x\cdot\mathbf y\); it cannot be a function of \(a,b\) alone.

The two anchored strengths can be varied independently. Replacing \(\beta V\) throughout by \(\beta_x(1-a)+\beta_y(1-b)\), with \(\beta_x,\beta_y\ge0\), gives
\[
H_{\beta_x,\beta_y}=H_0+\eta_\Gamma[\beta_x(1-a)+\beta_y(1-b)].
\tag{AW9a}
\]
Taking \(\eta_\Gamma\beta_x=\beta_{\rm internal}\), \(\eta_\Gamma\beta_y=t\gamma\), and recording the additive scalar \(t\gamma\), gives \(H_0+\beta_{\rm internal}(1-a)-t\gamma b\) of [[coarse-response-memory/correlated-interface-tangent|the exact interface tangent]]. Its analytic bounded-potential family fixes the tangent at \(t=0\), already determined from the positive-cost side. Both radial channels therefore return with the same operator. Vacuum-centering subtracts the returned ground energy; it does not erase the scalar factors from the original amplitude.

The same preparation also ties the electric and magnetic coefficients. For \(\Gamma=\sigma^2I_E\),
\[
\rho_\Gamma=\frac1{4\sigma^2},\qquad \eta_\Gamma=5\sigma^2,
\qquad \kappa=\frac1{60\sigma^2},\qquad \lambda=5\beta\sigma^2,
\qquad \boxed{\kappa\lambda=\frac\beta{12}.}
\tag{AW10}
\]
These are the declared comparison-clock units. More generally, with \(d\nu=S^{-3}d\gamma_\Gamma/\mathbb E S^{-3}\), one has \(\rho_\Gamma\eta_\Gamma=(\mathbb E_\nu S^{-1})(\mathbb E_\nu S)>1\) by Cauchy–Schwarz and the nonconstant Gaussian norm. The value \(5/4\) is specific to the isotropic gamma family, not arbitrary covariance. This couples the two returned coefficients without deriving a physical running coupling or fixing the action strength \(\beta\).

## The normalization choice determines the state return

An exact degree normalization would give a different law. Applied to (AW2), its first-order row correction cancels \(\lambda V\) and leaves the free electric diffusion. For \(\Gamma=I_E\) and fixed, unscaled flatness feature \(f_q=e^{-\beta SV(q)/2}\), the degree protocol instead has leading stationary density proportional to \((1+\beta V)^{-5}\), and Haar ground vector proportional to \((1+\beta V)^{-5/2}\). That trace-only vector is excluded as an interacting benchmark vacuum by the two-plaquette theorem. A commutator-only degree state is additionally even under each separate central sign and cannot supply the Wilson vacuum. These are distinctions between prescribed returns, not failures of excitation coverage; [[shared-preparation-state-and-mobility|the shared-preparation owner]] supplies the general degree calculation.

Successive transfer edges use independent copies of the whole Gaussian preparation, with shared words inside each edge. Intermediate full loop pairs and all source blocks are integrated by [[commutator-preparation-transfer-and-marked-gluing|marked gluing]]. A closed \(N\)-step amplitude retains \(z_\alpha^{-N}\) multiplying the integral of the \(N\) actual kernels. Source insertions keep these original unmarked normalizations fixed. Reusing a single preparation across several steps or renormalizing after each insertion changes that experiment. The finite benchmark now returns from the stated multiplication comparisons and pace; selection of these inputs, compatible graph refinement and the physical continuum gap remain open.

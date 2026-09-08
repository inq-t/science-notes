# Witten Covariance and Local Response

On a finite closed connected configuration manifold, the inverse weighted one-form Laplacian on its exact sector represents the covariance induced by a local score. Uniform weighted response control then gives covariance decay between distant supports. The scalar gap, the one-form domain, spatial locality, and physical reconstruction are separate inputs.

## The configuration and physical carriers

The construction uses several operators, and none may inherit the interpretation of another merely because their spectra have the same units after a convention is chosen.

| Symbol | Carrier | Operation | It is not |
|---|---|---|---|
| \(P_t=e^{-tL_0}\) | \(L^2(\mu)\) functions of a Euclidean configuration | auxiliary reversible averaging | Lorentzian or OS clock evolution |
| \(d\) | configuration functions to configuration-space one-forms | takes the score of a perturbation | a spacetime exterior derivative |
| \(L_1\) | configuration-space one-forms | transports susceptibility response | the physical Hamiltonian |
| \(L_1^{-1}dG\) | exact score one-forms | global response induced by the local score \(dG\) | a particle wavefunction |
| \(H_{\mathrm{OS}}\) | reconstructed physical Hilbert space | generates Euclidean clock translation and then Lorentzian energy | a sampler generator |

The candidate gap-bearing object before clock reconstruction is a decay rate per declared cut distance. The deeper invariant is the dimensionless product of that rate with a cut separation. Energy and mass arise only after a physical scale section, \(c\), and an action unit have been supplied by the recovery map.

## The covariance identity

Let

$$
X=\mathsf G^E,
\qquad
d\mu=Z^{-1}e^{-S}\,d\operatorname{vol},
\tag{ARL9}
$$

where \(\mathsf G\) is a compact connected Lie group, \(E\) is a finite set of lattice edges or blocked cells, and \(X\) has a smooth product Riemannian metric. Let \(S\) be smooth, so that \(\mu\) is a smooth strictly positive probability law on the closed connected manifold \(X\). There is no configuration-space boundary in this realization. Let \(d_\mu^*\) be the weighted adjoint of the configuration differential and define

$$
L_0=d_\mu^*d,
\qquad
L_1=dd_\mu^*+d_\mu^*d.
\tag{ARL10}
$$

Here \(L_1\) acts on one-forms over **configuration space**. Their components are indexed by edge or cell variables; they are not one-forms on reconstructed spacetime. For compatible self-adjoint realizations, the intertwining relation on a common smooth core and then by closure is

$$
dL_0=L_1d.
\tag{ARL11}
$$

Use the compatible self-adjoint weighted de Rham realizations and the closure of their common smooth domain. At each fixed closed connected carrier, the scalar Poincare inequality gives closed range for \(d\) and \(\ker L_0=\mathbb C1\); a lower bound uniform over a family of carriers is a separate hypothesis. The intertwining identifies centered scalar functions with the closed exact sector through \(dL_0^{-1/2}\). For centered real-valued smooth observables \(F,G\), \(L_1^{-1}\) below means the bounded reduced inverse on \(\overline{\operatorname{Ran}d}\), never an inverse on every one-form. Other boundary realizations require compatible domain and boundary conditions before the same argument can be used. Then

$$
\boxed{
\operatorname{Cov}_\mu(F,G)
=
\left\langle dF,L_1^{-1}dG\right\rangle_{L^2(\mu;T^*X)}.}
\tag{ARL12}
$$

Indeed, if \(u=L_0^{-1}G\), then \(du=L_1^{-1}dG\), and integration by parts gives

$$
\langle F,G\rangle
=
\langle F,L_0u\rangle
=
\langle dF,du\rangle.
\tag{ARL13}
$$

With complex observables, take the inner product conjugate-linear in its first slot and define covariance with conjugation of the first observable; the same identity follows by sesquilinearity.

## From weighted response to covariance decay

Suppose \(G\) is supported in a cell set \(B\), and define a weight on configuration one-forms by

$$
(W_{\sigma,B}\omega)_e
=
e^{\sigma d(e,B)}\omega_e.
\tag{ARL14}
$$

If one \(\sigma>0\) and, for each fixed local observable class, one \(C_G<\infty\) work uniformly in cutoff, volume, allowed boundary condition, retained sector, and translation of \(G\), so that

$$
\|W_{\sigma,B}L_1^{-1}dG\|_2
\leq C_G
\tag{ARL15}
$$

holds, then every \(F\) supported in \(A\) obeys

$$
\boxed{
|\operatorname{Cov}_\mu(F,G)|
\leq
\|dF\|_2C_G
e^{-\sigma d(A,B)}.}
\tag{ARL16}
$$

This follows by inserting \(W_{\sigma,B}^{-1}W_{\sigma,B}\) in (ARL12). It identifies what the inverse operator operates on: a local score is sent to the whole-law susceptibility it induces, and the desired theorem says that this response is exponentially unable to remain equally strong at arbitrary distance.

For a cutoff-uniform covariance estimate, the full prefactor \(\|dF\|_2C_G\) must also remain bounded for the declared local observable family.

## Gauge invariance and the exact sector

For gauge-invariant \(F,G\), one may work on the smooth product \(\mathsf G^E\) rather than prematurely quotienting by the stratified gauge orbit space. With an invariant metric and action, \(L_0\) and \(L_1\) commute with the gauge action, while \(dF\) and \(dG\) are invariant exact forms annihilating vertical gauge directions. A scalar Poincare gap controls this exact sector, not every coexact or harmonic one-form. If a different chosen generator has a fixed algebra larger than the constants, the [[auxiliary-clock-elimination|centered contraction estimate]] and any corresponding reduced inverse must instead use the orthogonal fixed-space projection, and every conclusion is confined to its complement. Neither these configuration-space one-forms nor their exact sector are carriers for a generalized one-form global symmetry; the later local OS argument reaches only the cyclic neutral vacuum representation unless an extended-operator totality theorem is added. Neither (ARL11) nor the parabolic Witten heat semigroup supplies finite propagation by itself; weighted off-diagonal control is a separate theorem.

[[exact-source-locality-without-a-full-form-gap|Exact-source locality]] gives a separate sufficient route to covariance decay without assuming (ARL15) or a full one-form gap. Spatial weights need not preserve exact forms: bounded weighted growth is proved on the full nonnegative operator, while long-time decay is used only on the original exact source. Splitting those estimates gives the direct off-support bound (ES6) and hence covariance bound (ES12). It does not automatically give the global weighted norm (ARL15) at the same endpoint exponent; summability and spatial-growth control, generally with a smaller weight exponent, would be needed for that stronger conclusion. [[rg-covariance-residue/nonlinear-conditional-gauge-response|The normalized compact gauge law]] supplies explicit Hessian and locality constants in a conditional strong-coupling regime.

## Primary precedents and their scope

[[library/witten-laplacian-methods-for-the-decay-of-correlations/inq|Lo, v9 §7, Proposition 22 and Corollary 23]] gives a weighted covariance precedent for unbounded spin systems with \(\Phi(x)=|x|^2/2+\Psi(x)\), the stated bounds on derivatives of \(\nabla\Psi\) and the observables, and a positive quadratic-form lower bound for \(M^{-1}\operatorname{Hess}\Phi\,M\) over the admitted weight ratios. Both the prefactor and the decay exponent may depend on support sizes. Those statements do not by themselves supply a common positive exponent across a total local family.

[[library/witten-laplacian-on-a-lattice-spin-system/inq|Shigekawa, Theorems 5.1–5.2]] obtains volume- and boundary-uniform positive-degree form floors under quantitative potential and interaction hypotheses: a bounded perturbation of a uniformly convex self-potential with the specified interaction bound, or a quartic double-well potential satisfying its separate small-interaction inequality. These full-form estimates require more than a scalar Poincare inequality. Neither source establishes the Yang--Mills continuum hypotheses.

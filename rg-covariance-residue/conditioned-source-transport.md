# Conditioned Source Transport

Differentiating a conditioned observable gives its direct derivative minus its covariance with the score that moves the hidden conditional law. This identifies the operator responsible for the spatial tails of a retained source. A weighted influence estimate controls those tails through successive blockings, but a bounded cost per step is not a uniform continuum bound: amplification accumulates toward the terminal scale, whereas the covariance-residue theorem permits growth only toward the discarded ultraviolet scales.

**Status: [EXACT SOURCE DERIVATIVES AND CONDITIONAL INFLUENCE ESTIMATES]; [OPEN] the uniform renormalized-source envelope and conditional localization for four-dimensional Yang--Mills.**

## The derivative operates on observables

Let \(Y\times Z\) be a fixed smooth product with closed compact fiber \(Z\), and write

$$
\nu_y(\mathrm dz)=\mathcal Z(y)^{-1}e^{-U(y,z)}\,\mathrm dz,
\qquad
(KF)(y)=\int_ZF(y,z)\,\nu_y(\mathrm dz).
\tag{CS1}
$$

The fiber volume is fixed. Assume smoothness and differentiation under the integral; compactness supplies domination for smooth data locally in \(y\). Sources \(F\) may be complex. Use the sesquilinear covariance
\(\operatorname{Cov}_y(A,F)=E_y(\overline A F)-\overline{E_yA}E_yF\).
For a real retained tangent \(u\), put \(\ell_u=d_yU[u]\). Differentiating numerator and denominator gives

$$
\boxed{d_y(KF)[u]
=E_y[d_yF[u]]-\operatorname{Cov}_y(\ell_u,F).}
\tag{CS2}
$$

The real score goes in the **first** covariance slot: the result is complex-linear in \(F\). In particular, the derivative may be nonzero when \(F\) has no explicit \(y\)-dependence. Conditioning changes which hidden configurations contribute to its mean.

For a moving reference density \(J(y,z)\,\mathrm dz\), use \(U=S-\log J\). Omitting \(d_y\log J\) omits part of the conditional score. This differentiates retained data, not the external scale parameter in [[scale-score-connection/inq|Scale Score Connection]]; the changing fiber density may encode geometry as well as coordinate choices.

There is a coordinate-independent local version for a smooth Euclidean submersion \(\xi:X\to Y\). With \(G=\nabla\xi\nabla\xi^{\mathsf T}\) nonsingular, choose

$$
v_\alpha=\sum_\beta(G^{-1})_{\alpha\beta}\nabla\xi_\beta,
\qquad
\ell_\alpha=v_\alpha S-\operatorname{div}v_\alpha.
\tag{CS3}
$$

For the coarea conditional measure and no unaccounted boundary flux,

$$
\partial_\alpha E[F\mid\xi=y]
=E[v_\alpha F\mid\xi=y]
-\operatorname{Cov}(\ell_\alpha,F\mid\xi=y).
\tag{CS4}
$$

This follows by applying [[library/a-general-two-scale-criteria-for-logarithmic-sobolev-inequalities/inq|Lelièvre's Lemma 2.3]] to numerator and denominator; his local mean force includes the divergence term. A singular gauge quotient does not satisfy the submersion hypothesis automatically. [[wilson-path-product-fibers|Wilson path-product fibers]] instead supplies global product coordinates upstairs, with no changing Haar-volume term.

## The response acts on the hidden score, not on mass

On a connected compact fiber with smooth positive density, let \(C_y\) be the conditional Witten operator on the closed exact-one-form subspace. At each fixed finite regulator it has a positive inverse there. Uniformity in regulator and volume is a separate estimate. Under the covariance-representation domains, define

$$
\mathcal R_{y,u}=C_y^{-1}d_Z\ell_u.
\tag{CS5}
$$

Then

$$
\boxed{d_y(KF)[u]
=E_y[d_yF[u]]
-\langle\mathcal R_{y,u},d_ZF\rangle_{L^2(T^*Z,\nu_y)}.}
\tag{CS6}
$$

The inverse operates on a **conditional configuration-space score one-form**. It returns the hidden response to a retained perturbation. It is not a spacetime propagator, a physical Hamiltonian inverse, or a mass operator. The [[contemporary-puzzles/yang-mills-mass-gap/vacuum-boundary-gluing-and-wall-response#The nonlinear residue has a fixed sign|existing nonlinear Witten/Schur formula]] owns the corresponding effective-Hessian identity.

For a product fiber, let \(\Pi_x\) select the one-form component at hidden site \(x\). A direct source-tail estimate needs only

$$
\sup_{y,\|u_i\|=1}\|\Pi_x\mathcal R_{y,u_i}\|_2,
\tag{CS7}
$$

for the actual retained scores, not necessarily the full inverse norm on every hidden one-form. This can be weaker than a full operator-localization theorem. It does not replace the separate shell-covariance estimate needed for two arbitrary physical sources.

If one uses blocks \(\Pi_xC_y^{-1}\Pi_z\), first extend the inverse by zero on the orthogonal complement of the exact-one-form subspace. Coordinate projections need not preserve exactness. Such a projected inverse is well defined under these hypotheses; its locality is not automatic.

## A sufficient spatial influence matrix

Use product coordinates with retained sites \(R\), hidden sites \(H\), and seminorms \(a_x(F)=\|\nabla_xF\|_\infty\). Suppose the actual conditional law obeys, uniformly in \(y\),

$$
|\operatorname{Cov}_y(F,G)|
\le\sum_{x,z\in H}C_j(x,z)a_x(F)a_z(G),
\qquad C_j(x,z)\ge0.
\tag{CS8}
$$

Define the mixed-score bound

$$
B_j(z,i)=\sup_{y,z'}\|\nabla_{z}d_{y_i}U_j(y,z')\|_{\mathrm{op}}.
\tag{CS9}
$$

Here the first \(z\) labels a site and \(z'\) is a complete hidden configuration. Equation (CS2) yields

$$
a_i(K_jF)\le\sum_xT_j(i,x)a_x(F),\qquad
T_j(i,x)=
\begin{cases}
\delta_{ix},&x\in R,\\
\sum_{z\in H}C_j(x,z)B_j(z,i),&x\in H.
\end{cases}
\tag{CS10}
$$

In nonlinear coordinates, the direct \(\delta\) is replaced by the corresponding derivative matrix, with its norm and spatial range declared. The score-response bound (CS7) gives another way to supply the hidden entries of \(T_j\), without assuming all of (CS8).

Thus the source derivative depends on two different ingredients: the local mixed score that launches a response, and the conditional susceptibility that transports it. Locality of the first does not prove locality of the second.

[[local-completion-of-soft-gauge-conditioning|The one-step Gaussian gauge completion]] constructs both ingredients on a complete linear gauge carrier: its normalized curvature law has a local positive completion, and the mixed coarse score is \(Q^*h/(\eta b^2)\). [[uniform-gaussian-conditional-locality|Uniform Gaussian conditional locality]] extends the terminal inverse and score estimates through the actual accumulated Gaussian precision. [[nonlinear-conditional-gauge-response|The normalized compact conditional law]] supplies a separate full nonlinear strong-coupling estimate, with the log-normalizer retained. Neither statement alone controls the source norms through the nonlinear RG iteration below.

## Iteration and the direction of cutoff growth

Let \(b_{j+1}=Lb_j\), \(L>1\), and embed the scale-dependent sites at physical locations \(p_x\). For a fixed physical source support \(A\), set

$$
S_{j,\nu}(F;A)
=\sum_xe^{\nu\,\operatorname{dist}(p_x,A)/b_j}a_x(F),
\qquad \nu>0.
\tag{CS11}
$$

With \(d_j(i,x)=|p_i-p_x|/b_j\), define the weighted column bound

$$
M_{j,\nu}
=\sup_x\sum_iT_j(i,x)e^{(\nu/L)d_j(i,x)}.
\tag{CS12}
$$

Then

$$
\boxed{S_{j+1,\nu}(K_jF;A)\le M_{j,\nu}S_{j,\nu}(F;A).}
\tag{CS13}
$$

Indeed, the triangle inequality bounds the output weight by
\(e^{(\nu/L)d_j(i,x)}e^{(\nu/L)\operatorname{dist}(p_x,A)/b_j}\);
the second factor is at most the input weight in (CS11). Sum (CS10).
The factor \(\nu/L\), rather than \(\nu\), records the change to coarse distance units. Bounded block-location offsets add their explicit exponential factors.

For example, assume \(C_j(x,z)\le K_je^{-\mu d_j(x,z)}\), uniformly polynomial spatial growth, and

$$
\mathcal B_j(q)=\sup_z\sum_i e^{q d_j(i,z)}B_j(z,i)<\infty.
$$

For \(q=\nu/L<\mu\), the triangle inequality supplies the sufficient estimate

$$
M_{j,\nu}\le
1+K_j\mathcal B_j(q)
\sup_x\sum_z e^{-(\mu-q)d_j(x,z)}.
\tag{CS14}
$$

Use the analogous direct-term bound instead of \(1\) when retained coordinate locations or derivatives change. No spatial kernel is inferred merely from finite \(K_j\).

For \(f_j=E_jF_a\), iteration gives

$$
S_{j,\nu}(f_j;A)
\le S_{0,\nu}(F_a;A)\prod_{\ell<j}M_{\ell,\nu}.
\tag{CS15}
$$

A uniform bound \(M_{\ell,\nu}\le M>1\) gives growth
\((b_j/a)^{\log M/\log L}\). This is polynomial in the scale ratio \(b_j/a\), exponential in the number of blocking steps, and **diverges at the terminal fixed physical scale** as \(a\to0\).

The [[inq|covariance-residue theorem]] instead allows a factor
\((b_*/b_j)^p\): growth toward the ultraviolet, with a finite terminal value.
These ratios run in opposite directions. A sufficient source envelope is

$$
\boxed{S_{0,\nu}(F_a;A)\prod_{\ell<j}M_{\ell,\nu}
\le C_F(b_*/b_j)^{p_F}
\quad\text{for every }a,j.}
\tag{CS16}
$$

Combined with the conditional covariance prefactor and sufficient exponent margin, this can feed the shell theorem. It is a new estimate to prove, not a consequence of bounded one-step influence.

Renormalization may involve normalization, operator mixing, and subtractions. It must be specified for the actual source family whose physical correlations converge nontrivially. Freely shrinking that family until (CS16) holds can erase the physical states and fail OS totality. Likewise, multiplying an intermediate representative by a scale-dependent number does not change the original correlation: its inverse conversion reappears when reconstruction is performed.

## Two exact failure tests

An invertible coordinate change can amplify gradients without forgetting anything. On the circle,

$$
y=h_\epsilon(x)=x-(1-\epsilon)\sin x,\qquad F(x)=\sin x,
\qquad 0<\epsilon<1.
$$

The map is a diffeomorphism, but
\(\partial_y E[F\mid y]_{y=0}=1/\epsilon\).
Choosing \(\epsilon=e^{-1/a}\) produces superpolynomial amplification.
The transported metric accounts for it; a fixed output coordinate norm does not.

A local quadratic action can produce nonlocal retained sources. For

$$
S(y,z)=\tfrac12z^{\mathsf T}Az+z^{\mathsf T}By
+\tfrac12y^{\mathsf T}Dy,\qquad A>0,
$$

with a positive full quadratic form, conditioning sends \(F=z_x\) to
\(-(A^{-1}By)_x\). Sparse \(A,B\) do not imply a sparse or uniformly exponentially localized \(A^{-1}B\). A local positive example uses two lattice scalar fields with gradient energies and a local spring coupling \(\epsilon^2(z-y)^2/2\), plus a positive infrared regulator. As the spring and regulator vanish, the hidden conditional operator approaches a massless Laplacian and its localization length diverges.

The next Yang--Mills target is therefore not an unspecified “operator that forgets.” It is the response (CS5), on the actual conditional gauge carrier, with uniform weighted bounds and a nontrivial renormalized-source envelope. Terminal mixing and continuum construction remain additional obligations.

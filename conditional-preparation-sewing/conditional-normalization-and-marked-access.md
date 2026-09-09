# Conditional Normalization and Marked Access

A correlated preparation can acquire a new physical comparison while preserving every old marked transfer under boundary readout. The necessary normalization is conditional on the retained preparation. A single scalar generally fails this test, although it preserves the old Gaussian prior. The conditional rule is positive and returns finite dynamics for the newly accessible loop; it changes the complete comparison prescription and is not an innocuous removal of a determinant. This supplies an explicit alternative to the single-Gaussian extension, with a different returned clock.

## The integrated boundary is part of the experiment

Use the actual paths of [[conditional-preparation-sewing/conditional-preparation-extension-at-new-access|the new-access construction]]:
\[
A=U_1U_2=U,\qquad B=U_1W^{-1}U_1U_2=LU,
\qquad L=U_1W^{-1}=BA^{-1}.
\tag{NA1}
\]
Both paths run from the same initial vertex to the same final vertex. Their pair identifies the complete quotient by the intermediate vertex gauge. Product Haar on the three links pushes forward to product Haar on \((A,B)\). Boundary gauges act simultaneously by \((A,B)\mapsto(h_0Ah_2^{-1},h_0Bh_2^{-1})\). These are multiplication words, not two independently postulated loop variables.

Let \(\xi\) be the old preparation, and give a new preparation the conditional law \(P(d\eta\mid\xi)\), with joint prior \(P(d\xi,d\eta)\). For a faithful unitary representation define
\[
p_{\alpha,\xi}(A,A')=e^{-\alpha\|[\rho(A)-\rho(A')]\xi\|^2},\qquad
q_{\alpha,\eta}(B,B')=e^{-\alpha\|[\rho(B)-\rho(B')]\eta\|^2},
\]
\[
z_\alpha=\int_G\mathbb E p_{\alpha,\xi}(e,a)\,da,\qquad
b_\alpha(\xi)=\mathbb E\!\left[\int_Gq_{\alpha,\eta}(e,b)\,db\mid\xi\right]>0.
\tag{NA2}
\]
Each fixed-preparation kernel is invariant under simultaneous left translation. Its row integral is consequently independent of the retained group point, even when it is not central. Norms, measures and covariances are declared inputs.

For an old source insertion \(M(\xi)\), the single-Gaussian raw extension has the integrated kernel
\[
\int_G\mathbb E[M(\xi)p_{\alpha,\xi}(A,A')q_{\alpha,\eta}(B,B')]\,dB'
=\mathbb E[M(\xi)p_{\alpha,\xi}(A,A')b_\alpha(\xi)].
\tag{NA3}
\]
This retains an extra preparation-dependent weight. A scalar \(c_\alpha\) makes the right side equal to \(c_\alpha\mathbb E[Mp_{\alpha,\xi}]\) for **all** bounded old marks if and only if \(b_\alpha=c_\alpha\) almost surely. Necessity follows by testing bounded functions of \(\xi\); the strictly positive factor \(p\) may be absorbed into the measure. The same conclusion follows from the complete Fourier source family by uniqueness of the finite measure. Sufficiency is immediate. Equality of the Gaussian prior marginals alone says nothing about this extra comparison weight.

For a nondegenerate correlated Gaussian, \(b_\alpha\) is already nonconstant in the elementary \(SU(2)\) example below. Thus preservation of the old preparation and preservation of its processed experiment are distinct conditions. [[conditional-preparation-sewing/access-ports-and-conditional-sewing|Conditional sewing]] gives the complementary Schur-complement test at a fixed pair of boundary configurations; (NA3) instead includes the declared Haar readout of a new boundary.

## A positive extension with exact old marked readout

Define a different comparison rule:
\[
\boxed{\widetilde F_\alpha^{M}(A,B;A',B')
=z_\alpha^{-1}\mathbb E\!\left[
M(\xi)p_{\alpha,\xi}(A,A')
\frac{q_{\alpha,\eta}(B,B')}{b_\alpha(\xi)}\right].}
\tag{NA4}
\]
The denominator is the **source-free conditional row integral** and is held fixed when differentiating marks. It depends on the old preparation and on \(\alpha\), but not on either boundary configuration. Inserting arbitrary joint sources gives their expectation against this same weighted integral whenever it is integrable; generally there is no single quadratic Gaussian determinant for the resulting amplitude.

Integration over the new outgoing boundary proves
\[
\boxed{\int_G\widetilde F_\alpha^{M}(A,B;A',B')\,dB'
=z_\alpha^{-1}\mathbb E[M(\xi)p_{\alpha,\xi}(A,A')].}
\tag{NA5}
\]
For \(Jf(A,B)=f(A)\), this is the exact old marked kernel identity \(\widetilde F_\alpha^M J=J F_{\alpha,\mathrm{old}}^M\). It holds before localization and hence through any temporal product with transported old marks on the separate preparations. It extends to an old endpoint feature depending on \(A,\xi\), because that feature can stay inside the old expectation in (NA5). A genuinely new weak interaction involving \(B\) generally changes this identity.

For the unmarked rule, positivity follows by conditioning on \((\xi,\eta)\): the product of two Gaussian distance kernels is positive, and \(1/b_\alpha(\xi)>0\). Assume both preparations have full row rank almost surely, as in the Gaussian law below. Faithfulness then gives strict positivity on nonzero Haar-density measures by the Gaussian embedding argument of [[general-causal-action/general-group-preparation-and-the-casimir-return|the general-group theorem]]. Thus the operator is injective. Its kernel is symmetric and its row integral is exactly one by (NA5), so it is a self-adjoint Markov contraction. In the correlated isotropic law below it also commutes with both boundary gauge actions. These conclusions concern the complete framed carrier and its complete gauge-invariant subspace.

This is a substantive constitutive choice. The factor \(b_\alpha(\xi)^{-1}\) reweights the auxiliary preparation in the full comparison. It preserves an explicitly specified old readout while altering the joint raw amplitudes and the new response. It cannot be dropped from a closed trace or from homogeneous source derivatives.

## An exact correlated example and its two finite clocks

Use \(G=SU(2)\), \(\rho\) fundamental, \(\xi,\eta\in\mathbb C^{2\times k}\), \(k\ge2\), with unnormalized Hilbert–Schmidt pairing. Write \(m=2k\), and take
\[
\xi\sim\operatorname{CN}(0,\sigma^2I_m),\qquad
\eta=a\xi+\epsilon,\qquad
\epsilon\sim\operatorname{CN}(0,\tau^2I_m),\quad \epsilon\perp\xi,
\quad \sigma,\tau>0.
\tag{NA6}
\]
Here \(a\in\mathbb C\); the new innovation is nondegenerate. This uses \(Q(X,Y)=-\operatorname{Re}\operatorname{Tr}(XY)\), not the normalized-trace rotor metric. Set \(S=\|\xi\|^2\), \(T=\|\eta\|^2\). The fundamental identity gives \(p=e^{-\alpha S d(A,A')^2}\), \(q=e^{-\alpha T d(B,B')^2}\), where \(d^2=2-\operatorname{Tr}(A^{-1}A')\). Also \(g_\xi=(S/2)Q\), so a fixed scalar norm contributes the generator coefficient \(1/(2S)\) multiplying \(D_Q=-\Delta_Q\).

For \(0<p<m\), completing the conditional Gaussian square and using the Laplace formula for a negative power gives
\[
h_p(s):=\mathbb E[T^{-p}\mid S=s]
=\frac1{\Gamma(p)}\int_0^\infty t^{p-1}(1+\tau^2t)^{-m}
\exp\!\left[-\frac{|a|^2st}{1+\tau^2t}\right]dt.
\tag{NA7}
\]
This formula is finite, positive and bounded above by \(h_p(0)\). For \(a\ne0\) it is strictly decreasing in \(s\). Directly,
\[
b_\alpha(s)=\int_G(1+\alpha\tau^2d(e,b)^2)^{-m}
\exp\!\left[-\frac{\alpha|a|^2s\,d(e,b)^2}{1+\alpha\tau^2d(e,b)^2}\right]db
\tag{NA8}
\]
is strictly decreasing for every \(\alpha>0\), proving the nonconstant-weight obstruction in (NA3). The single-Gaussian prescription consequently increases the old limiting clock as proved in the new-access owner; the conditional prescription has a different return.

The limiting preparation measure for (NA4) is
\[
d\widetilde\nu(\xi,\eta)
=\frac{S^{-3/2}}{\mathbb E S^{-3/2}}
\frac{T^{-3/2}}{h_{3/2}(S)}\,dP(\xi,\eta).
\tag{NA9}
\]
In particular its old marginal is exactly the original one-link localization law \(\nu_0\), under which \(S\sim\operatorname{Gamma}(m-3/2,\sigma^2)\). The returned operator is
\[
\boxed{\widetilde H=\kappa_0D_{Q,A}+\kappa_1D_{Q,B},\qquad
\kappa_0=\frac1{2\sigma^2(m-5/2)},\qquad
\kappa_1=\frac12\mathbb E_{\nu_0}
\frac{h_{5/2}(S)}{h_{3/2}(S)}\in(0,\infty).}
\tag{NA10}
\]
Thus \(\widetilde F_{N/t}^{\,N}\to e^{-t\widetilde H}\) strongly on the full framed carrier and its gauge-invariant subspace, uniformly on bounded nonnegative time intervals. The original coarse clock remains fixed despite the correlation.

Here are domination details for that return. The scalar row integral \(z(t)=\int e^{-t d(e,b)^2}db\) is bounded above and below by positive constants times \((1+t)^{-3/2}\); this follows from compactness and the nondegenerate quadratic minimum in three-dimensional normal coordinates. Jensen's inequality therefore gives, for \(\alpha\ge1\),
\[
\alpha^{3/2}b_\alpha(s)\ge c(1+|a|^2s+m\tau^2)^{-3/2},\qquad
h_{3/2}(s)\ge(|a|^2s+m\tau^2)^{-3/2}.
\tag{NA11}
\]
The radial second and fourth moment integrals are bounded by \(C\alpha^{-5/2}h_{5/2}(s)\) and \(C\alpha^{-7/2}h_{7/2}(s)\). Dividing by (NA11) gives polynomial-in-\(s\) domination of the scaled conditional moments. All needed \(h_p(0)\) are finite since \(m\ge4\). The old marginal localization is dominated by \(S^{-3/2}dP\), its scaled second moment by \(S^{-5/2}dP\), and its scaled fourth moment by \(S^{-7/2}dP\), including those polynomial factors. These are integrable since \(m\ge4\). Inversion symmetry in each group variable cancels odd and mixed second derivatives; the second moments give (NA10). Fourth moments and Cauchy–Schwarz control the mixed Taylor remainder. Dominated convergence yields the smooth-core first-order limit; the exact contractions extend its product limit to the whole carrier. No claim uniform in \(\tau\downarrow0\), graph growth or physical lattice spacing is made.

## The new loop and the mixed response survive

For a nontrivial irreducible character \(\chi\), with \(D_Q\chi=C_Q(\chi)\chi\),
\[
\widetilde H\chi(BA^{-1})=(\kappa_0+\kappa_1)C_Q(\chi)\chi(BA^{-1}).
\tag{NA12}
\]
This is a nonzero, finite physical rate. It repairs the annihilated loop in [[general-causal-action/preparation-transport-through-spatial-subdivision|PT14–18]]. There is also actual mixed motion in the inherited \((U,L)\) coordinates. Define \(\mathcal L_Xf(U)=\partial_t f(e^{tX}U)|_0\) and \(\mathcal R_Xf(L)=\partial_t f(Le^{tX})|_0\). Varying \(A\) at fixed \(B\) gives \(\mathcal L_{U,X}-\mathcal R_{L,X}\); varying \(B\) gives \(\mathcal L_{L,X}\). Hence
\[
\widetilde H=\kappa_0D_{Q,U}+(\kappa_0+\kappa_1)D_{Q,L}
+2\kappa_0\sum_i\mathcal L_{U,e_i}\mathcal R_{L,e_i}.
\tag{NA13}
\]
The mixed term comes from the actual path word. It does not prove equality with the local raw-link metric of an independently specified lattice Hamiltonian.

Shared source response also survives. Under the original Gaussian prior, \(\operatorname{Cov}(S,T)=m|a|^2\sigma^4\). Under the actual limiting law (NA9),
\[
\operatorname{Cov}_{\widetilde\nu}(S,T)
=\operatorname{Cov}_{\nu_0}\!\left(S,\frac{h_{1/2}(S)}{h_{3/2}(S)}\right)>0
\quad(a\ne0).
\tag{NA14}
\]
For strict positivity, expand the conditional Laplace transform in (NA7) as the Poisson mixture
\(T\mid S=s,N\sim\operatorname{Gamma}(m+N,\tau^2)\),
\(N\mid S=s\sim\operatorname{Poisson}(|a|^2s/\tau^2)\).
Weighting by \(T^{-3/2}\) multiplies the Poisson probabilities by \(\tau^{-3}\Gamma(m+N-3/2)/\Gamma(m+N)\). The resulting mean of \(T\) is \(\tau^2(m-3/2+\mathbb E_sN)\). The derivative of \(\mathbb E_sN\) with respect to the log Poisson parameter is its strictly positive variance. Thus this mean is strictly increasing in \(s\), and its covariance with the nondegenerate \(S\) is positive. Integrability follows also from \(\mathbb E[T\mid S=s]\) as an upper bound after the decreasing norm tilt.

The full finite-width source response is given by (NA4), with the actual joint insertion and the fixed denominator. Neither of the two displayed covariances may be substituted for that finite conditional response. Preserving the old complete readout does not force zero joint response, nor does nonzero joint response force a change in the old clock.

## A genuine interaction uses the retained preparation

The rule also returns an interacting vacuum. Use the actual transported row \((L-I)A\xi\), whose norm squared is \(2V(L)S\), where \(V(L)=1-\operatorname{Tr}(L)/2\). Insert the two endpoint factors
\[
f_{\alpha,A,B}(\xi)=e^{-\beta V(BA^{-1})S/(2\alpha)},\qquad \beta\ge0,
\tag{NA15}
\]
in (NA4), retaining its source-free \(z_\alpha\) and \(b_\alpha(\xi)\). Conditional Gaussian positivity and domination by the unmarked Markov kernel again give positive injective contractions. The same localization proof, with polynomial norm moments, returns
\[
\boxed{\widetilde H_\beta=\widetilde H+\lambda V(BA^{-1}),\qquad
\lambda=\beta\mathbb E_{\widetilde\nu}S
=\beta\sigma^2(m-3/2).}
\tag{NA16}
\]
On this fixed compact carrier the operator is uniformly elliptic with smooth bounded potential, and has a simple positive ground vector. All vertex gauges commute with it. On the fully gauge-invariant one-loop carrier it is exactly \((\kappa_0+\kappa_1)D_{Q,L}+\lambda V(L)\) restricted to class functions; it therefore supplies that operator's actual interacting vacuum. The new potential generally changes the old readout identity (NA5), as a genuine interaction is permitted to do.

The normalized extension fixes the old magnetic moment as well as its free electric coefficient. Its dependence on the new innovation enters the loop kinetic coefficient \(\kappa_1\). The single-Gaussian prescription instead weights both old moments by the joint localization factor. Thus these are two complete finite interacting constructions, whose different response laws can be compared. Neither has yet been shown to recover the required local many-cell Yang–Mills dynamics through spatial refinement.

## The remaining constitutive choice is visible

The single-Gaussian extension retains the simplest quadratic amplitude and changes the old processed marginal through localization. The conditional extension retains that old processed marginal and introduces a preparation-dependent normalization. Both use the same multiplication words and prior covariance, and both retain the new physical loop. Their difference must be decided by an explicit law for genuine access extensions; pure presentation covariance does not choose between them.

[[conditional-preparation-sewing/conditional-access-families-and-the-returned-clock|Conditional access families]] extend the normalized rule to general groups and a growing number of accesses over one retained root. The full-source counterexample in (AP18)–(AP19) shows why this fixed-root coherence is not yet invariance under changing the retained root.

A common-source cosmological calculation must differentiate the selected full prescription, including \(b_\alpha(\xi)^{-1}\) when present. The raw normalization and contact terms in [[general-causal-action/closed-normalization-and-cosmic-response|the closed-source calculation]] cannot be imported unchanged from the single-Gaussian rule. The exact finite construction identifies a meaningful selection question; it supplies no four-dimensional continuum or Yang–Mills gap theorem.

# Feature-Number Grading and Compact Reconstruction

The reflected transfer has an explicit symmetric-tensor feature map, but its degree-zero vector is not the physical vacuum. An actual centered neutral plaquette source has a nonzero degree-zero feature component. Moreover, any reconstruction that sends every distinction through the global weighted feature analysis and finitely many number or ladder operations is compact, so its residual from the identity has norm at least one on the infinite-dimensional frame-source sector. This rejects one concrete repair strategy. It does not reject a repair retaining the direct middle-slice innovation, and it is not a soft-energy counterexample.

## The feature number does not diagonalize temporal sewing

Use the supported boundary carrier and kernel of [[reflection-sewing-and-the-auxiliary-boundary-carrier|RS6–14]]. Write \(S(\Xi)=\|\Xi\|^2\), \(\kappa=rw>0\), and let \(\mathcal F^{\mathcal G}\) be the gauge-invariant subspace of the complexified symmetric-tensor feature space. Its number operator \(N\) multiplies degree \(j\) by \(j\). Define
\[
v_\kappa(\Xi)=P_{\mathcal G}^{\rm feat}
\bigoplus_{j\ge0}\sqrt{\frac{(2\kappa)^j}{j!}}\,\Xi^{\otimes j},
\qquad
A h=\int v_\kappa(\Xi)h(\Xi)m(\Xi)\,d\Xi .
\tag{FN1}
\]
Here \(A:L^2(m\,d\Xi)^{\mathcal G}\to\mathcal F^{\mathcal G}\), and the exact transfer is
\[
\widetilde{\mathsf T}=A^*A.
\tag{FN2}
\]
The real Euclidean tensor pairing is complexified; \(A\) is linear in \(h\). The Haar projection commutes with \(N\).

Let \(\Pi_j\) project to feature degree \(j\). The dual transfer has moment blocks
\[
\Pi_jAA^*\Pi_l
=\int v_{\kappa,j}(\Xi)\otimes
v_{\kappa,l}(\Xi)^*\,m(\Xi)\,d\Xi .
\tag{FN3}
\]
Its \(0\)-to-\(2\) block is nonzero. Indeed, contraction against the invariant quadratic tensor giving \(\|\Xi\|^2\) is a positive constant times \(\int S\,m\,d\Xi>0\). Therefore
\[
[N,AA^*]\ne0.
\tag{FN4}
\]
This is a finite-degree matrix-element assertion; it does not require an unqualified commutator identity on the domain of the unbounded \(N\). Even the Gaussian weight mixes homogeneous tensor degrees.

Let \(\varphi>0\) be the normalized actual temporal vacuum, with \(\widetilde{\mathsf T}\varphi=\lambda_0\varphi\). Physical centering of a boundary wave \(h\) gives
\[
\langle\varphi,h\rangle=0
\quad\Longrightarrow\quad
\left\langle\frac{A\varphi}{\sqrt{\lambda_0}},Ah\right\rangle=0.
\tag{FN5}
\]
It does not give \(\Pi_0Ah=0\). Thus the elementary number inequality \(N\ge I-\Pi_0\) is not already an inequality above the actual temporal vacuum. The following source calculation makes the mismatch explicit on frame observables.

## A centered neutral plaquette retains feature degree zero

Take \(G=SU(2)\) in its fundamental representation, one auxiliary copy, and a spatial graph consisting of one square with four vertices. Such a spatial square fits the declared hypercubic slicing for \(D\ge3\). Put \(S_x=\|\xi_x\|^2\). With
\[
m_0(\Xi)=e^{-\sum_xS_x},
\]
the \(S_x\) are independent \(\operatorname{Gamma}(2,1)\) variables under \(m_0\,d\Xi\). Every nonzero spinor can be written \(\xi_x=\sqrt{S_x}\,g_xe_1\), with \(g_x\in SU(2)\).

For an oriented edge define \(t_{xy}=2\kappa\sqrt{S_xS_y}\). Its conditional link density is proportional to \(e^{t_{xy}\operatorname{ReTr}(g_x^*U_{xy}g_y)/2}\). The normalized character integral, with \(I_j\) the modified Bessel function, gives
\[
z(t)=\int_{SU(2)}e^{t\operatorname{ReTr}(U)/2}\,dU
=\frac{2I_1(t)}t,
\qquad
\mathbb E[D^j(U_{xy})\mid\Xi]
=\frac{I_{2j+1}(t_{xy})}{I_1(t_{xy})}
D^j(g_xg_y^*).
\tag{FN6}
\]
The value \(z(0)=1\) is by continuity. The character calculation is the one in [[relative-multiplication-transfer-and-the-rotor-limit|RT4–6]]; \(D^j\) has dimension \(2j+1\).

For the normalized spin-\(j\) square source \(F_j=\chi_j(U_\square)/(2j+1)\), conditional links are independent and the endpoint rotations telescope. Hence its exact returned source is
\[
\boxed{\displaystyle
\Phi_\kappa F_j(\Xi)
=\prod_{\{x,y\}\in E_\square}
\frac{I_{2j+1}(2\kappa\sqrt{S_xS_y})}
{I_1(2\kappa\sqrt{S_xS_y})}.}
\tag{FN7}
\]
This is a bounded neutral frame source, not a freely added radial observable. The formula includes inverse orientations by adjoint transport.

Write \(F=F_{1/2}\), \(P_S=\prod_xS_x\), and let \(\varphi_\kappa\) be normalized in \(L^2(m_\kappa\,d\Xi)\). As \(\kappa\downarrow0\),
\[
\begin{aligned}
m_\kappa
&=m_0\left[1+\frac{\kappa^2}{2}
\sum_{\{x,y\}\in E_\square}S_xS_y+O(\kappa^4)\right],\\
\varphi_\kappa
&=1+\kappa^2\left(\sum_xS_x-12\right)+O(\kappa^4),\\
\Phi_\kappa F
&=\frac{\kappa^4}{16}P_S+O(\kappa^6).
\end{aligned}
\tag{FN8}
\]
The first and third lines follow from \(z(t)=1+t^2/8+O(t^4)\) and \(I_2(t)/I_1(t)=t/4+O(t^3)\). For the middle line, the temporal kernel is \(1+\frac{\kappa^2}{2}\sum_xS_xS'_x+O(\kappa^4)\). The mean of the spatial weight correction is \(8\); the temporal eigenvalue is \(1+16\kappa^2+O(\kappa^4)\). Solving its order-\(\kappa^2\) eigenvector equation and imposing \(\int m_\kappa\varphi_\kappa^2=1\) gives the constant \(12\).

These expansions are used in Gaussian-weighted norms and moment integrals, not as uniform polynomial remainders at arbitrarily large \(S\). Their control follows directly from the original full-slice kernel \(b_\kappa K_\kappa b_\kappa\): in a fixed small complex neighborhood of \(\kappa=0\), its derivatives are bounded by a polynomial in \(S+S'\) times an integrable Gaussian, with a fixed positive mass margin. It is therefore an analytic Hilbert–Schmidt operator family on the fixed full-slice \(L^2\) carrier. At zero it is the rank-one operator \(|b_0\rangle\langle b_0|\), with isolated eigenvalue one. A resolvent contour around that eigenvalue gives its real-analytic normalized vacuum for real \(\kappa\). The same Gaussian estimates permit polynomial moments of the displayed expansions. All integrated quantities below can also be written with that full-slice vector, bounded \(F\), and \(b_\kappa\), avoiding division by a small slice weight.

Put \(d\pi_\kappa=\varphi_\kappa^2m_\kappa\,d\Xi\), and center the actual returned source:
\[
h_\kappa
=\varphi_\kappa\left[\Phi_\kappa F
-\int\Phi_\kappa F\,d\pi_\kappa\right].
\]
It is orthogonal to the physical vacuum and belongs to the vacuum image of the cyclic neutral frame-source sector. Yet its degree-zero feature coefficient is
\[
\boxed{\displaystyle
\Pi_0Ah_\kappa
=\int h_\kappa m_\kappa\,d\Xi
=-\frac{\kappa^6}{16}
\operatorname{Cov}_{m_0d\Xi}
\left(P_S,\sum_xS_x\right)+O(\kappa^8)
=-4\kappa^6+O(\kappa^8).}
\tag{FN9}
\]
Here \(\mathbb E P_S=16\), \(\mathbb E(P_S\sum_xS_x)=192\), and \(\mathbb E\sum_xS_x=8\), so the covariance is \(64\). Terms from the next source coefficient and the perturbed slice measure cancel upon physical centering. Equation (FN9) is nonzero for all sufficiently small positive \(\kappa\); a degree-zero deletion would remove part of an actual centered neutral source.

For the remainder in (FN9), if \(\Psi_\kappa=b_\kappa\varphi_\kappa\) is the full-slice normalized vacuum, its left side is exactly
\(\langle b_\kappa,M_F\Psi_\kappa\rangle-\langle\Psi_\kappa,M_F\Psi_\kappa\rangle\langle b_\kappa,\Psi_\kappa\rangle\).
The analytic kernel argument therefore controls the displayed scalar remainder using bounded multiplication by the original frame source.

## Finite number and ladder operations still leave compact analysis

Write \(\Phi_\kappa^{\rm feat}\) for the unprojected feature vector in (FN1), distinguishing it from the conditional source map \(\Phi_\kappa\). For each integer \(s\ge0\),
\[
\|N^s\Phi_\kappa^{\rm feat}(\Xi)\|^2
=\sum_{j\ge0}j^{2s}\frac{(2\kappa S)^j}{j!}
=e^{2\kappa S}\,\mathcal T_{2s}(2\kappa S),
\tag{FN10}
\]
where \(\mathcal T_{2s}\) is a fixed polynomial with nonnegative coefficients; at \(s=0\) it equals one. This is the elementary Poisson moment polynomial. Since the Haar projection commutes with \(N\), RS3 gives
\[
\|N^sA\|_{\rm HS}^2
=\int\|N^sv_\kappa(\Xi)\|^2m(\Xi)\,d\Xi
\le\int e^{-(1-r)S}\mathcal T_{2s}(2\kappa S)\,d\Xi<\infty.
\tag{FN11}
\]
Thus every fixed power of feature number composed with the actual analysis remains Hilbert–Schmidt. A fixed finite word of creation and annihilation operators has a norm bound by a fixed power of \(N+1\), so it has the same property after composition with \(A\). Haar projections between these operations do not change that estimate. The constants are finite at each fixed preparation; no uniformity near a closing mass margin or growing inventory is asserted.

The frame-source sector is already infinite dimensional in the square example. On the diagonal \(S_x=s>0\), (FN7) has leading behavior
\[
\Phi_\kappa F_j
\sim\frac{(\kappa s)^{8j}}{[(2j+1)!]^4}
\quad(s\downarrow0).
\tag{FN12}
\]
Distinct spins therefore give linearly independent returned functions. A finite linear relation in the Hilbert space would hold everywhere on the positive radial domain by continuity and full support, and restriction to this diagonal contradicts the distinct leading powers. Removing the constant source leaves an infinite-dimensional centered sector.

## One explicit reconstruction attempt is excluded

Let \(\delta_\ell\) be the actual middle-versus-two-endpoint discrepancy of [[determinant-response-sewing-and-relational-rigidity|DS10e–g]], and let \(U_\varphi f=\varphi f\) be the vacuum unitary from \(L^2(\pi)\) to \(L^2(m\,d\Xi)\). Consider the direct feature reconstruction
\[
\mathcal B_\ell=D\,N^sA\,U_\varphi\,\delta_\ell^*,
\tag{FN13}
\]
where \(D\) is any bounded synthesis map into the centered frame sector. Every map is typed on the actual measures; no invariance of that sector under \(\delta_\ell^*\delta_\ell\) is assumed.

By (FN11), \(\mathcal B_\ell\delta_\ell\) is compact. For an orthonormal sequence \(f_j\) in the centered frame sector, compactness gives \(\mathcal B_\ell\delta_\ell f_j\to0\). Consequently
\[
\boxed{\displaystyle
\|I-\mathcal B_\ell\delta_\ell\|\ge1.}
\tag{FN14}
\]
It cannot satisfy DS10g with residual norm strictly below one, even at a fixed member of the square family. The argument also covers finite sums of such bounded reconstruction branches and fixed finite ladder words in place of \(N^s\).

This excludes repairs whose every branch passes through the global compact feature analysis. It does not exclude a branch retaining the direct innovation, or a local operation with uncompressed spectator variables. An inverse of \(A\) on its range would evade the boundedness assumption only by being unbounded: the nonzero singular values of \(A\) tend to zero.

That last fact is not itself a mass-gap obstruction. Small singular values of \(A\) are small eigenvalues of the transfer and hence high energies of its logarithm. A positive energy gap instead concerns separation of the next transfer eigenvalue from the top one. The failed reconstruction tries to undo smoothing on every normalized distinction; feature positivity and a bare number gap do not justify that inverse.

The next viable feature-based repair must therefore retain a noncompact innovation channel and prove an additional relation controlling its residual in the actual vacuum geometry. The number grading alone neither aligns the two vacua nor provides that relation.

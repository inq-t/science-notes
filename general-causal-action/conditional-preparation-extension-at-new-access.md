# Conditional Preparation Extension at New Access

An old Gaussian preparation and a correlated innovation can compare two actual paths that retain a newly accessible loop. The complete old preparation marginal survives, the new transfer is positive and injective, and a finite Casimir evolution replaces the annihilation found under inherited product comparison. The same preparation supplies a weak loop potential. With a single joint Gaussian integral and one scalar normalization, new localization changes the old clock; preservation of the old marked transfer is a stronger requirement than preservation of its preparation marginal.

## Extend the preparation at a common endpoint

Use the graph of [[preparation-transport-through-spatial-subdivision|preparation transport, PT14–18]]: an old edge is presented by \(U=U_1U_2\), and a new path \(W\) reaches its intermediate vertex. The internal-vertex quotient retains
\[
A=U_1U_2=U,\qquad L=U_1W^{-1},\qquad
B=LA=U_1W^{-1}U_1U_2.
\tag{CE1}
\]
Both \(A\) and \(B\) are actual paths from \(v_0\) to \(v_2\). Their use as comparison rows is a declared choice; algebra does not yet select this path inventory. The repeated \(U_1\) in \(B\) is its actual occurrence in the word, not a fresh link variable. The map to \((A,L)\), or equivalently \((A,B)\), pushes product Haar to product Haar. At fixed \((A,L)\), choose \(U_1\) freely and set \(U_2=U_1^{-1}A\), \(W=L^{-1}U_1\); these fibers are precisely the internal-vertex gauge orbits. Thus \(L^2(G^2)\) is the complete internally invariant carrier, before imposing the old endpoint gauges.

Let \(G\) be compact and connected with simple Lie algebra of dimension \(d\), and choose a faithful unitary representation \(\rho:G\to U(n)\). Use the unnormalized Hilbert–Schmidt convention and \(Q=-\operatorname{Re}\operatorname{Tr}(d\rho\,d\rho)\) of [[general-group-preparation-and-the-casimir-return|the general-group preparation theorem]]. On \(E=\mathbb C^{n\times k}\), of complex dimension \(m=nk\), take
\[
\Xi\sim\operatorname{CN}(0,\sigma^2I_E),\qquad
\varepsilon\sim\operatorname{CN}(0,\tau^2I_E),\qquad
\Eta=a\Xi+\varepsilon,
\qquad \sigma,\tau>0,
\tag{CE2}
\]
with independent \(\Xi,\varepsilon\) and any \(a\in\mathbb C\). The joint covariance is
\[
\Gamma=
\begin{pmatrix}
\sigma^2&\overline a\sigma^2\\
a\sigma^2&|a|^2\sigma^2+\tau^2
\end{pmatrix}\otimes I_E>0,
\qquad \det\Gamma=(\sigma^2\tau^2)^m.
\tag{CE3}
\]
Projection \((\Xi,\Eta)\mapsto\Xi\) recovers the original Gaussian measure and every old linear or quadratic source amplitude exactly. This is the explicit conditional extension of [[access-ports-and-conditional-sewing|access ports and conditional sewing]]. For example, with \(S=\|\Xi\|^2\) and \(T=\|\Eta\|^2\), the original prior has
\[
\operatorname{Cov}(S,T)=m|a|^2\sigma^4.
\tag{CE4}
\]
Conditioning on \(\Xi\) gives \(\mathbb E(T\mid\Xi)=|a|^2S+m\tau^2\), which proves (CE4). Thus nonzero \(a\) has a measured mixed preparation response. This covariance belongs to the prior; localization and inserted marks change the relevant law.

Both preparations transform by \(\rho(h_2)\) at \(v_2\). The paths transform as \(A,B\mapsto h_0(A,B)h_2^{-1}\), so the two output rows transform by \(\rho(h_0)\). The joint covariance is invariant. Correlating preparations at this common endpoint therefore requires no unmentioned identification of distinct vertex carriers.

## Compare the actual paths with the full Gaussian law

For fixed comparison paces \(r,s>0\), put
\[
\Phi_{A,B}(\Xi,\Eta)
=\big(r^{-1/2}\rho(A)\Xi,\ s^{-1/2}\rho(B)\Eta\big),
\qquad
K_\alpha(q,q')=\mathbb E_\Gamma
e^{-\alpha\|(\Phi_q-\Phi_{q'})(\Xi,\Eta)\|^2}.
\tag{CE5}
\]
For \(B_\rho(g)=2I_n-\rho(g)-\rho(g)^\dagger\), define the positive matrix on \(E\oplus E\)
\[
D(q,q')=
\operatorname{diag}\!\left(
r^{-1}I_k\otimes B_\rho(A^{-1}A'),\
s^{-1}I_k\otimes B_\rho(B^{-1}B')\right).
\tag{CE6}
\]
The complete marked kernel, for arbitrary joint \(j\) and Hermitian \(\mathcal T\), is
\[
\boxed{
K_\alpha^{j,\mathcal T}(q,q')
=\frac{\exp(j^\dagger\mathcal Q^{-1}j)}
{\det\Gamma\,\det\mathcal Q},\qquad
\mathcal Q=\Gamma^{-1}+\alpha D(q,q')+\mathcal T>0.}
\tag{CE7}
\]
All path, stage and cross-row sources pull back to this formula by their actual linear readout maps. This includes off-diagonal blocks between \(\Xi\) and \(\Eta\). The normalized Gaussian reference measure is the same as in [[marked-gaussian-constraints-and-sewing-measures|marked Gaussian sewing]]; no stage carries a new independent Gaussian measure.

The unmarked kernel depends only on \((A^{-1}A',B^{-1}B')\). Its row integral
\[
z_\alpha=\int_{G^2}K_\alpha(q,q')dq',\qquad
R_\alpha=z_\alpha^{-1}K_\alpha
\tag{CE8}
\]
is constant, with normalized product Haar understood in the operator notation. The kernel is invariant under simultaneous right translations and under each relative inversion, because \(B_\rho(g^{-1})=B_\rho(g)\). In particular it commutes with the two endpoint gauge actions. It need not factor into two separate determinant kernels when \(a\ne0\).

For \(k\ge n\), both preparations have full row rank almost surely. Faithfulness then makes \(q\mapsto\Phi_q(\Xi,\Eta)\) an injective compact embedding. Conditional Gaussian distance positivity, its strictly positive Euclidean Fourier density and Fourier uniqueness prove that \(R_\alpha\) is a positive injective operator on all of \(L^2(G^2)\). Symmetry and its unit row integral make it a self-adjoint Markov contraction. No new loop sector is removed by a quotient or by zero operator action.

## Joint localization returns two finite clocks

Let \(g_\Xi\) and \(g_\Eta\) be their real tangent metrics on \(\mathfrak g\), as in (GG4), and set
\[
w_\Xi=(\det_Qg_\Xi)^{-1/2},\qquad
w_\Eta=(\det_Qg_\Eta)^{-1/2},\qquad
d\nu=\frac{w_\Xi w_\Eta\,dP_\Gamma}
{\mathbb E_\Gamma(w_\Xi w_\Eta)}.
\tag{CE9}
\]
An explicit sufficient inventory is
\[
k>n+\frac d2.
\tag{CE10}
\]
Indeed, if \(\Lambda=\lambda_{\max}(\Gamma)\), the joint Gaussian density is bounded by a constant times the density of two independent isotropic Gaussians of variance \(\Lambda\). Every needed product of \(w\), \(w\|g^{-1}\|\), and fixed polynomial norm factors is therefore integrable by the one-preparation inverse-moment proof (GG7–9), applied separately to the two variables. This argument uses \(\tau>0\); it is not uniform as the innovation covariance becomes singular.

For fixed preparations, the tangent comparison metric is block diagonal, \(g_\Xi/r\oplus g_\Eta/s\). The two localization integrals and their second-moment bounds give
\[
z_\alpha\sim
\frac{\pi^d(rs)^{d/2}}{\operatorname{Vol}_Q(G)^2}
\alpha^{-d}\,\mathbb E_\Gamma(w_\Xi w_\Eta),
\]
\[
\boxed{
H=\kappa_A(-\Delta_{Q,A})+\kappa_B(-\Delta_{Q,B}),\qquad
\kappa_A=\frac r{4d}\mathbb E_\nu\operatorname{tr}_Qg_\Xi^{-1},\qquad
\kappa_B=\frac s{4d}\mathbb E_\nu\operatorname{tr}_Qg_\Eta^{-1}.}
\tag{CE11}
\]
Simultaneous \(\rho(G)\) invariance of the joint law and the determinant weights makes each averaged inverse metric scalar by simplicity of \(\mathfrak g\). There is no mixed second derivative in the \((A,B)\) coordinates: at fixed preparations the leading tangent Gaussian has zero cross covariance. Correlation of preparation norms changes their localized averages, not this block-diagonal fact.

The dominated second-order argument of (GG9–12) now yields
\[
\alpha(R_\alpha-I)f\longrightarrow-Hf,
\qquad
R_{N/t}^{\,N}\longrightarrow e^{-tH}
\quad\text{strongly on }L^2(G^2).
\tag{CE12}
\]
The first limit is uniform for smooth \(f\); the second includes the identity at zero and is uniform on bounded nonnegative time intervals. Finite Peter–Weyl sums give a dense invariant core, and contractivity extends the product limit to every vector. No operator-norm or uniform graph-growth estimate is asserted.

## The composite path supplies mixed motion in old and new observables

Write \(\ell_{U,i}f=\left.\partial_t f(e^{te_i}U,L)\right|_0\), and let \(R_{L,i}\) generate \(L\mapsto Le^{te_i}\). Changing \(A\) on the left while keeping \(B\) fixed changes \((U,L)\) to \((e^{te_i}U,Le^{-te_i})\). Changing \(B\) on the left at fixed \(A\) changes \(L\) on the left. Hence the same operator is
\[
\boxed{H=-\kappa_A\sum_i(\ell_{U,i}-R_{L,i})^2
-\kappa_B\sum_i\ell_{L,i}^2,}
\]
\[
\mathcal E(F)=\int\left[
\kappa_A\sum_i|\ell_{U,i}F-R_{L,i}F|^2
+\kappa_B\sum_i|\ell_{L,i}F|^2\right]dU\,dL.
\tag{CE13}
\]
The two fields in each first square act on different factors and commute. Thus the cross term is an exact consequence of the actual word \(B=LU\). Correlating two preparation norms without this word would not supply it. Conversely, the word supplies this mixed term even at \(a=0\); the mixed kinetic response and (CE4) are distinct measurements.

An old function of \(U\) alone evolves with coefficient \(\kappa_A\). A loop character \(\chi_\lambda(L)\) obeys
\[
H\chi_\lambda(L)=(\kappa_A+\kappa_B)C_Q(\lambda)\chi_\lambda(L),\qquad
e^{-tH}\chi_\lambda
=e^{-t(\kappa_A+\kappa_B)C_Q(\lambda)}\chi_\lambda.
\tag{CE14}
\]
Here \(-\Delta_Q\chi_\lambda=C_Q(\lambda)\chi_\lambda\). A nontrivial character has \(C_Q(\lambda)>0\). It is invariant under every vertex gauge of this graph and has finite, nonzero evolution. This directly repairs the failure of (PT18) on the complete new physical loop carrier. It is a finite compact-system result, not a field mass-gap estimate.

## A single Gaussian normalization changes the old clock

For a sharper explicit case take the defining representation of \(SU(2)\), \(n=2\), any \(k\ge2\), and \(m=2k\). The special matrix identity gives
\[
g_\Xi=\frac S2 I_3,\qquad g_\Eta=\frac T2 I_3,\qquad
d\nu\propto S^{-3/2}T^{-3/2}dP_\Gamma,
\]
\[
\kappa_A=\frac r2\mathbb E_\nu S^{-1},\qquad
\kappa_B=\frac s2\mathbb E_\nu T^{-1}.
\tag{CE15}
\]
These lower inventories are justified directly by the scalar norm formula. Gaussian density domination reduces the needed inverse moments to independent \(\operatorname{Gamma}(m,\Lambda)\) variables, and \(m>5/2\) suffices. They do not follow from the sufficient general-group bound (CE10). The metric here is \(Q=-\operatorname{Re}\operatorname{Tr}\), not the \(-2\operatorname{Tr}\) metric of the normalized-matrix incidence example.

The old isolated path has localized law \(\nu_0\) with \(S\sim\operatorname{Gamma}(m-3/2,\sigma^2)\), and coefficient
\[
\kappa_{\rm old}=\frac r{2\sigma^2(m-5/2)}.
\tag{CE16}
\]
For \(0<p<m\), conditional Gaussian integration and the Laplace representation of a negative power give
\[
h_p(S):=\mathbb E(T^{-p}\mid\Xi)
=\frac1{\Gamma(p)}\int_0^\infty
\frac{u^{p-1}}{(1+\tau^2u)^m}
\exp\!\left[-\frac{|a|^2uS}{1+\tau^2u}\right]du.
\tag{CE17}
\]
For \(p=3/2\), \(h_p\) is finite and strictly decreasing in \(S\) whenever \(a\ne0\). The new \(S\)-marginal is \(h_{3/2}(S)d\nu_0/\mathbb E_{\nu_0}h_{3/2}\). Since \(S^{-1}\) is also strictly decreasing and \(\nu_0\) is nondegenerate,
\[
\mathbb E_\nu S^{-1}-\mathbb E_{\nu_0}S^{-1}
=\frac{\operatorname{Cov}_{\nu_0}(S^{-1},h_{3/2}(S))}
{\mathbb E_{\nu_0}h_{3/2}(S)}>0,
\qquad \boxed{\kappa_A>\kappa_{\rm old}\quad(a\ne0).}
\tag{CE18}
\]
Strict positivity follows by taking two independent \(S,S'\): the covariance is half the expectation of \((S^{-1}-{S'}^{-1})(h_{3/2}(S)-h_{3/2}(S'))\), positive off the diagonal. All moments are finite by the preceding bounds. Thus even the old limiting clock changes when the new comparison shares its Gaussian preparation. Its unchanged prior/source marginal does not imply an unchanged weighted experiment. At \(a=0\), the joint kernel factors, \(\kappa_A=\kappa_{\rm old}\), and the prior norm covariance vanishes.

The condition \(\tau>0\) has a further concrete role. At \(\tau=0\), \(a\ne0\), and \(m=4\), the two norms obey \(T=|a|^2S\). The six-dimensional comparison then has localization weight \(S^{-3}\), while its ordinary diffusion coefficient needs \(\mathbb E S^{-4}\), which diverges. This is precisely the critical shared-preparation case of [[preparation-rank-and-locality|preparation rank and locality]]. The positive innovation in (CE2) opens independent preparation directions and gives finite ordinary clocks for every fixed \(\tau>0\); these clocks are not asserted uniformly bounded toward the singular endpoint.

## A weak loop cost uses the retained old preparation

At \(q=(U,L)\), add the actual closed-loop identity row
\[
C_q\Xi=[\rho(L)-I_n]\rho(U)\Xi,\qquad
\mathcal C(q,\Xi)=\frac\beta2\|C_q\Xi\|^2,
\qquad f_{\alpha,q}=e^{-\mathcal C(q,\Xi)/(2\alpha)},
\quad\beta\ge0.
\tag{CE19}
\]
The output is based at \(v_0\), with both multiplication paths retained. Insert \(f_{\alpha,q}f_{\alpha,q'}\) inside the same joint Gaussian integral (CE5), and keep the free scalar \(z_\alpha\) of (CE8). In (CE7), this adds \(\beta(C_q^\dagger C_q+C_{q'}^\dagger C_{q'})/(4\alpha)\) to the \(\Xi\) block of its precision, with column multiplicity understood. The exact transfer remains positive, injective, contractive and endpoint-gauge invariant.

The joint polynomial moment bounds above justify the weak-cost expansion. For
\[
\overline A_\Xi=\mathbb E_\nu(\Xi\Xi^\dagger),
\qquad
V_\beta(L)=\beta\operatorname{Tr}
[\overline A_\Xi(I_n-\operatorname{Re}\rho(L))],
\tag{CE20}
\]
the product limit is \(e^{-t(H+V_\beta)}\). Simultaneous \(\rho(G)\) invariance gives \([\overline A_\Xi,\rho(G)]=0\), removing the \(\rho(U)\) transports only from this leading expected potential. The finite marked kernel still contains them. The operator is uniformly elliptic on the compact product, with bounded smooth potential, \(H^1\) form domain, \(H^2\) operator domain and a simple positive gauge-invariant ground vector. For irreducible \(\rho\), \(\overline A_\Xi=(\mathbb E_\nu S/n)I_n\); the expectation uses the joint law (CE9), not the isolated preparation coefficient.

This construction resolves the new-access annihilation with actual multiplication rows, a complete shared preparation law and a returned interacting operator for every declared compact simple group. It leaves the representation, paces, covariance extension and word inventory as constitutive inputs. It also exposes a choice of normalization: a single joint Gaussian integral preserves old preparation marginals but usually changes old dynamics. [[conditional-normalization-and-marked-access|Conditional normalization and marked access]] gives a distinct law that preserves the old marked transfer exactly; it must retain its conditional factors rather than claim the single determinant (CE7). Selecting a coherent family over growing access diagrams, and obtaining the four-dimensional Yang–Mills and cosmological returns, remain open.

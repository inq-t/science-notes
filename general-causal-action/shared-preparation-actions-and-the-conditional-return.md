# Shared Preparation Actions and the Conditional Return

The same sampled Gaussian matrix can drive several actual frame actions without sacrificing positivity or finite clock control. Normalize each increment at fixed preparation, compose the operators symmetrically before averaging, and use the directed diagram's exact preparation law. For the three-cell chain this gives a positive interacting transfer with shared bridge and path preparations, the complete inherited electric operator, and explicit terminal-to-root transport. The preparation is reused; the group increments remain conditionally independent. These choices define a finite construction, not an automatic spatial marginal or continuum theorem.

## A fixed matrix supplies positive Fourier matrices

Use the faithful representation, Hilbert–Schmidt norm and metric \(Q=Q_\rho\) of [[general-group-preparation-and-the-casimir-return|GG1–11]]. Thus \(G\) is compact and connected with simple Lie algebra, \(d=\dim G\), \(\rho:G\to U(n)\) is faithful, and \(\xi\in\mathbb C^{n\times k}\). For \(r,\alpha>0\), set
\[
q_{\xi,\alpha,r}(h)=e^{-\alpha\|[\rho(h)-I]\xi\|^2/r},\qquad
\zeta_{\xi,\alpha,r}=\int_Gq_{\xi,\alpha,r}(h)\,dh,\qquad
p_{\xi,\alpha,r}=q_{\xi,\alpha,r}/\zeta_{\xi,\alpha,r}.
\tag{SA1}
\]
The fixed-matrix density is generally noncentral. It is nevertheless inversion symmetric, since
\[
\|[\rho(h)-I]\xi\|^2
=\operatorname{Tr}\{\xi\xi^\dagger[2I-\rho(h)-\rho(h)^\dagger]\}.
\]
Moreover, \(q_\xi(g^{-1}h)\) is the Gaussian distance kernel on \(g\mapsto\rho(g)\xi\). If \(\xi\) has full row rank, this is an injective compact embedding. The Euclidean Gaussian Fourier argument in GG therefore makes its energy strictly positive on every nonzero finite measure. In particular, every irreducible Fourier matrix is positive definite:
\[
B_{\xi,\alpha,r;\tau}
=\int_Gp_{\xi,\alpha,r}(h)\tau(h)\,dh>0.
\tag{SA2}
\]
Inversion symmetry identifies this convention with the adjoint Fourier convention. Positivity of the whole convolution excludes a negative eigenvalue of any block; injectivity excludes a zero eigenvalue. These are finite positive matrices, not generally scalar multipliers.

Let \(\Phi\) be any smooth Haar-measure-preserving left action on a compact carrier \(M\). Define
\[
(T_{\Phi,\xi,\alpha,r}f)(q)
=\int_Gp_{\xi,\alpha,r}(h)f(\Phi_hq)\,dh .
\tag{SA3}
\]
The action representation uses inverse pullback; inversion symmetry gives the same operator. Its compact-group decomposition has blocks \(B_{\xi,\alpha,r;\tau}\otimes I\), so (SA3) is positive, injective, self-adjoint and Markov. Neither a free action nor a density on all of \(M\times M\) is required. This extends [[prepared-frame-actions-and-the-bridge-return|FA3–5]] from scalar central multipliers to fixed-preparation matrix multipliers.

## Retain the diagram law before reusing its matrices

Take a finite Gaussian preparation DAG from [[conditional-preparation-sewing/conditional-preparation-diagrams-and-ancestral-readout|PD1–3]], with scalar parent maps and positive innovation variances. Each node has a declared reference pace \(r_i>0\). Write
\[
b_{i,\alpha}
=\mathbb E[\zeta_{\xi_i,\alpha,r_i}\mid\xi_{\operatorname{pa}(i)}],
\qquad
d\nu_{D,\alpha}(\xi)
=\prod_i\frac{\zeta_{\xi_i,\alpha,r_i}}{b_{i,\alpha}}\,dP_D(\xi).
\tag{SA4}
\]
This is precisely PD's normalized finite-width preparation law. Its nodewise conditional factors integrate to one, and its ancestral marginals retain their original normalizers.

At fixed full \(\xi\), choose finitely many action operators of the form (SA3), allowing repeated use of any \(\xi_i\). Their action paces may differ from the reference paces in (SA4). If \(C_{\xi,\alpha}\) is another positive injective Markov operator and \(K_{\xi,\alpha}\) a finite product of the action operators, then
\[
\mathcal S_{\xi,\alpha}
=K_{\xi,\alpha}^*C_{\xi,\alpha}K_{\xi,\alpha},
\qquad
\mathcal S_\alpha
=\int\mathcal S_{\xi,\alpha}\,d\nu_{D,\alpha}(\xi)
\tag{SA5}
\]
are positive injective self-adjoint Markov contractions. Every factor is a probability transition, and
\(\langle f,\mathcal S_{\xi,\alpha}f\rangle
=\langle K_{\xi,\alpha}f,C_{\xi,\alpha}K_{\xi,\alpha}f\rangle>0\)
for \(f\ne0\). Averaging preserves that strict inequality. Each occurrence uses a separate group increment conditional on the one full preparation. It does not sample a second copy of a reused matrix.

For marks depending only on the preparations, the exact unit row is particularly informative:
\[
\mathcal S_\alpha^M1=\mathbb E_{\nu_{D,\alpha}}M.
\tag{SA6}
\]
There is only one factor \(\zeta_i/b_i\) per preparation node, regardless of its number of uses. Changing an action pace leaves (SA4) fixed. Changing a reference pace \(r_i\) changes the finite preparation law and is a different marked experiment.

## Transport the shared matrix through the actual reference path

Use four actual paths \(P_0,P_1,P_2,P_3\) between one retained root and one common terminal, with the charged carrier \(L^2(G^4)\). The matrices \(\xi_i\) occupy the common terminal port. The root loop coordinates and the isometric quotient pullback are
\[
x=P_0P_1^{-1},\qquad y=P_2P_1^{-1},\qquad z=P_3P_2^{-1},
\qquad
(JF)(P)=F(x,y,z).
\tag{SA7}
\]
Product Haar disintegrates into these three coordinates and the reference path \(P_1\). Gauge reduction at the terminal is performed after constructing the full averaged operator.

Define two terminal-parameter actions on the charged carrier:
\[
\begin{aligned}
\widetilde A_k(P)
&=(P_0,P_1,P_1kP_1^{-1}P_2,P_1kP_1^{-1}P_3),\\
\widetilde B_k(P)
&=(P_0,P_1,P_2k^{-1},P_3k^{-1}).
\end{aligned}
\tag{SA8}
\]
They are smooth Haar-preserving left actions and commute. Each preserves \(P_1\) along its own orbit. At that boundary, their root increment and root preparation are
\[
h=P_1kP_1^{-1},\qquad \eta_i(P)=\rho(P_1)\xi_i,\qquad
\|[\rho(h)-I]\eta_i(P)\|^2
=\|[\rho(k)-I]\xi_i\|^2.
\tag{SA9}
\]
On \((x,y,z)\), the actions become exactly \(A_h(x,y,z)=(x,hy,hzh^{-1})\) and \(B_h(x,y,z)=(x,yh^{-1},z)\). Thus they carry the two actual bridge rows of [[three-cell-incidence-and-shared-path-motion|TC15]].

This transport is necessary. The same terminal matrix generally gives different root matrices at two boundaries if the reference path changes between them. Replacing both by one fixed root matrix would define a different preparation law.

Let
\[
(\mathcal R_{\xi,\alpha}f)(P)
=\int_{G^4}\prod_{i=0}^3p_{\xi_i,\alpha,r_i}(k_i)\,
f(P_0k_0,P_1k_1,P_2k_2,P_3k_3)\prod_i dk_i .
\tag{SA10}
\]
It is the positive injective product of the four fixed-preparation comparisons. Reuse \(\xi_2\) in both bridges, putting
\[
T_{a,\xi,\alpha}=T_{\widetilde A,\xi_2,\alpha,s_a},
\quad T_{b,\xi,\alpha}=T_{\widetilde B,\xi_2,\alpha,s_b},
\]
\[
\boxed{\mathcal S_{\xi,\alpha}
=T_{a,\xi,\alpha}T_{b,\xi,\alpha}\mathcal R_{\xi,\alpha}
T_{b,\xi,\alpha}T_{a,\xi,\alpha},\qquad
S_\alpha=J^*\mathbb E_{\nu_{D,\alpha}}
[\mathcal S_{\xi,\alpha}]J.}
\tag{SA11}
\]
The same \(\xi_2\) appears in its central path comparison and all four bridge occurrences. The central step may change \(P_1\); each subsequent occurrence of (SA8) uses its current value. Compression of the fixed-preparation middle step before constructing the palindrome would lose this boundary transport and is not the definition.

Under a common terminal gauge \(t\), transform
\[
P_i\mapsto P_it^{-1},\qquad \xi_i\mapsto\rho(t)\xi_i,\qquad
k\mapsto tkt^{-1}.
\tag{SA12}
\]
Every displayed action and comparison is covariant, and (SA4) is invariant. Therefore the averaged operator preserves the terminal-invariant subspace; \(J^*(\cdot)J\) is its exact restriction. Common left root transformations also commute with the averaged operator and induce simultaneous conjugation of \(x,y,z\). The final physical restriction is to \(L^2(G^3)^{\operatorname{Ad}G}\). Positivity, injectivity and the Markov property hold on all these stated carriers.

If the four bridge factors are removed, (SA4) and (SA10) cancel their one-row \(\zeta_i\) factors exactly. The resulting charged kernel is PD4, and its quotient is the old conditional-family transfer. This is also an equality of marked amplitudes when the same actual terminal and transported root sources are retained. With bridges present, the new law is an extension of that experiment; equality of all its old processed readouts is not inferred from positivity.

## A uniform pace comparison keeps the same inverse-moment threshold

Different uses of a matrix need not have equal paces. Here is a bound independent of the matrix and the width. Regard the orbit \(\{\rho(g)\xi:g\in G\}\) as a subset of \(\mathbb R^N\), \(N=2nk\), with its chord pseudometric. Let \(v_\xi(R)\) be the Haar measure of a ball of radius \(R\). Left multiplication is isometric and transitive, so every orbit-centered ball of that radius has the same measure. Euclidean packing gives, for \(R\ge u>0\),
\[
v_\xi(R)\le (1+2R/u)^N v_\xi(u).
\tag{SA13}
\]
A maximal \(u\)-separated set in the radius-\(R\) ball covers it by radius-\(u\) balls. Its disjoint Euclidean radius-\(u/2\) balls lie in a radius-\(R+u/2\) ball, proving the bound. This argument also permits a stabilizer or deficient matrix rank.

Write \(Z_\xi(t)=\int e^{-t\|[\rho(g)-I]\xi\|^2}dg\). The radius \(t^{-1/2}\) ball gives \(Z_\xi(t)\ge e^{-1}v_\xi(t^{-1/2})\). Splitting into annuli of that width and applying (SA13) yields, for any fixed \(c>0\),
\[
\boxed{\frac{Z_\xi(t/c)}{Z_\xi(t)}
\le e\sum_{j=0}^\infty(2j+3)^Ne^{-j^2/c}
=C_{N,c}<\infty.}
\tag{SA14}
\]
Consequently \(\zeta_{\xi,\alpha,r}/\zeta_{\xi,\alpha,s}\) is uniformly bounded for any fixed positive pair \(r,s\).

Assume the same sufficient inventory as PD:
\[
k>n+\frac d2.
\tag{SA15}
\]
Let \(\ell_i=\lambda_{\min}(\xi_i\xi_i^\dagger)\). The density bound PD11 dominates \(\nu_{D,\alpha}\) by a polynomial in the parent norms times \(\prod_i\ell_i^{-d/2}P_D\). For one increment using node \(i\) at pace \(s\), its scaled second moment contributes
\[
\alpha\,
\frac{\zeta_{\xi_i,\alpha,r_i}}{\zeta_{\xi_i,\alpha,s}}
\int_G\operatorname{dist}_Q(e,k)^2
q_{\xi_i,\alpha,s}(k)\,dk.
\tag{SA16}
\]
Bound the ratio by (SA14) before applying GG9. Combining with the conditional denominator lower bounds leaves only the \(i\)-th inverse power raised to \(\ell_i^{-d/2-1}\). All other conditional increments integrate to one, even when they use that same matrix. PD's domination by a larger-variance product Gaussian and its polynomial inverse-moment bounds prove integrability under (SA15).

At fixed full preparation, the independent increment laws are inversion symmetric. Taylor expansion of the entire smooth finite composition therefore has no linear term or mixed increment covariance. Its surviving second derivatives are the sum of the individual action generators. The scaled second-moment tail tends to zero for fixed preparation. Cross-tails factor conditionally into one scaled second moment and another tail probability, and (SA16) dominates their average. Repeated matrices do not require repeated negative powers of their smallest eigenvalues.

## The shared law returns the complete three-cell operator

The preparation measures converge with polynomially weighted domination to PD8,
\[
d\nu_D=\prod_i\frac{w_i}{\mathbb E[w_i\mid\xi_{\operatorname{pa}(i)}]}\,dP_D,
\qquad
w_i=(\det_Qg_{\xi_i})^{-1/2}.
\]
Define the finite strictly positive coefficients
\[
c_i=\frac1{4d}\mathbb E_{\nu_D}\operatorname{tr}_Qg_{\xi_i}^{-1}.
\tag{SA17}
\]
The joint law is invariant under common \(\rho(G)\), so each averaged inverse tangent metric is \(4c_i I\). The preceding estimates give the uniform smooth-core limit on the charged carrier
\[
\alpha(\mathbb E_{\nu_{D,\alpha}}\mathcal S_{\xi,\alpha}-I)
\longrightarrow-\mathcal H,\qquad
\mathcal H=\sum_i r_ic_iD_{P_i}
+2s_ac_2D_{\widetilde A}+2s_bc_2D_{\widetilde B}.
\tag{SA18}
\]
The factors of two count the mirrored bridge occurrences, not independent preparation draws. Because neither bridge differentiates \(P_1\), its transported orthonormal basis produces no additional derivative of that frame.

Choose the declared paces by
\[
(r_0c_0,r_1c_1,r_2c_2,r_3c_3)
=(3,1,1,3)\kappa,\qquad
s_a=s_b=r_2/2,\qquad \kappa>0.
\tag{SA19}
\]
The limiting law \(\nu_D\), hence the \(c_i\), is independent of these fixed reference paces; every coefficient is positive and finite, so this calibration exists. The inherited operator on \(G^3\) is then exactly
\[
\boxed{H_{\rm ch}=H_\parallel+\kappa D_a+\kappa D_b,}
\tag{SA20}
\]
with the full form TC6, including the transported angular row \(L_y+C_z\). The underlying covariance may have genuine multiple parents, for example roots \(0,1\), node \(2\) with parents \(0,1\), and node \(3\) with parents \(1,2\). No independence of the reused preparation from the other paths is required.

The product comparison in (SA18) is uniformly elliptic on \(G^4\); its quotient has the compact elliptic domains established in TC. Smooth core convergence and contraction give
\[
S_{N/t}^{\,N}\longrightarrow e^{-tH_{\rm ch}}
\quad\text{strongly, uniformly on bounded nonnegative times}.
\tag{SA21}
\]
The identity is used at \(t=0\). A fresh full preparation is averaged at each macroscopic transfer step; it is reused within that step. Freezing a single preparation through all temporal steps is a different experiment and is not this semigroup limit. No uniform bound over a growing action list, diagram, or vanishing innovation variance is asserted. For \(Q'=sQ\), replace \(c_i\) by \(s c_i\); in particular \(Q_{\rm TP}=2Q\) requires the same factor two as FA.

## The same preparation also supplies an endpoint interaction

Let \(U_c(P)\) be actual root-based closed words, such as \(x,y,z\), and take \(\beta_c\ge0\). Use the reused preparation itself:
\[
\mathcal C(P,\xi)
=\frac12\sum_c\beta_c
\|[\rho(U_c(P))-I]\rho(P_1)\xi_2\|^2,
\qquad
m_{\alpha,\xi}(P)=e^{-\mathcal C(P,\xi)/(2\alpha)}.
\tag{SA22}
\]
Replace the fixed-preparation palindrome in (SA11) by
\(m_{\alpha,\xi}\mathcal S_{\xi,\alpha}m_{\alpha,\xi}\),
keeping all source-free normalizers and (SA4) fixed. This is positive injective and self-adjoint, with row sums at most one. Equation (SA9) supplies its actual port typing at each endpoint.

Polynomial versions of (SA16) control the endpoint expansion and its remainder. The return is \(H_{\rm ch}+V\), where
\[
V(x,y,z)=\sum_c\beta_c\operatorname{Tr}
[\overline A_2(I-\operatorname{Re}\rho(U_c))],
\qquad
\overline A_2=\mathbb E_{\nu_D}\xi_2\xi_2^\dagger.
\tag{SA23}
\]
The matrix \(\overline A_2\) commutes with \(\rho(G)\), removing the reference transport only after taking this leading expectation. For the fundamental \(SU(2)\) representation, \(V=\sum_c\beta_c\,\mathbb E_{\nu_D}\|\xi_2\|^2[1-\operatorname{Tr}(U_c)/2]\). These are finite positive coefficients from the same localized preparation; the choices of \(\beta_c\) are still inputs.

The strong product limit, compact elliptic domains and simple positive gauge-invariant ground vector follow as in FA18. This supplies an interaction from the shared prepared norm, rather than appending an unrelated physical potential. It does not select the magnetic strengths or establish a uniform physical gap.

The full marked experiment is the path integral of (SA11) or (SA22): retain the single joint \(\xi\), every conditionally independent group increment, each actual intermediate \(P\), and every factor in (SA1) and (SA4). Insert marks without differentiating or resetting those source-free normalizers. Bounded marks always suffice. Joint Gaussian linear and quadratic marks are admissible when the resulting total Gaussian precision is positive; at each fixed width the reciprocal row integrals grow at most polynomially in the matrix norms. General increment or boundary marks require their stated integrability.

Terminal sources transform with (SA12); root sources couple to the actual transported readout \(\rho(P_1)\xi_i\) at their own boundary. Perform this source transport before a gauge quotient. An arbitrary charged mark need not descend to a physical scalar, and a mark need not preserve positivity. The source-free properties proved above do not assert otherwise.

The shared law differs from FA's product of separately averaged preparations: averaging a fixed-preparation palindrome retains correlations between its occurrences. [[bridge-forgetting-and-the-inherited-marked-transfer|The spatial marginal theorem]] computes its retained experiment with these same matrices, transported sources and normalizers. Positive transfer, a recovered electric operator, and a shared Gaussian origin do not identify that composite marginal with a newly calibrated old preparation experiment.

# General-Group Preparation and the Casimir Return

A relative Gaussian comparison in any declared faithful unitary representation of a compact connected simple Lie group returns a Casimir diffusion on the complete group carrier. A sufficient finite preparation inventory controls small singular values by an elementary row-distance argument. A weak identity comparison returns a character potential from the same localized preparation. Irreducible representations give an exact magnetic coefficient and a reciprocal electric–magnetic inequality, whose excess measures preparation shape. Faithful reducible representations remain necessary for some global forms. These are compact-group transfer limits with declared inputs, not a Yang–Mills continuum construction.

## A faithful matrix comparison retains the whole group

Let \(G\) be compact and connected with simple Lie algebra \(\mathfrak g\), \(d=\dim G\), and fix a faithful unitary representation \(\rho:G\to U(n)\). Write \(T_X=d\rho(X)\), and use the positive bi-invariant metric
\[
Q(X,Y)=-\operatorname{Re}\operatorname{Tr}(T_XT_Y).
\tag{GG1}
\]
Choose a \(Q\)-orthonormal basis \(e_i\), with left-invariant fields \(\mathsf X_i f(U)=\left.\partial_t f(Ue^{te_i})\right|_0\). Then \(\Delta_Q=\sum_i\mathsf X_i^2\) is nonpositive. Haar measure is normalized; its density in these exponential coordinates at zero is \(1/\operatorname{Vol}_Q(G)\).

Let \(\Xi\in\mathbb C^{n\times k}\) have independent centered circular complex Gaussian entries with variance \(\sigma^2>0\). The norm is Hilbert–Schmidt, with no normalized matrix trace. Put
\[
A=\Xi\Xi^\dagger,\qquad B(g)=2I-\rho(g)-\rho(g)^\dagger\ge0,
\]
\[
\boxed{
k_\alpha(U,V)=\mathbb E e^{-\alpha\|(\rho(U)-\rho(V))\Xi\|_{\rm HS}^2}
=\det[I_n+\alpha\sigma^2B(U^{-1}V)]^{-k}.}
\tag{GG2}
\]
This is a central, inversion-symmetric relative kernel. Centrality uses the isotropic preparation law; it is not automatic for an arbitrary replacement covariance. Define the retained scalar normalization and Markov convolution
\[
z_\alpha=\int_G k_\alpha(g)dg,\qquad
R_\alpha f(U)=z_\alpha^{-1}\int_G k_\alpha(g)f(Ug)dg.
\tag{GG3}
\]

For \(k\ge n\), almost every \(\Xi\) has full row rank. Faithfulness then makes \(U\mapsto\rho(U)\Xi\) an injective compact embedding. The Gaussian distance kernel has strictly positive energy on every nonzero finite complex measure: its Euclidean Fourier representation is the integral of the squared Fourier transform against a strictly positive Gaussian density. Fourier uniqueness excludes zero energy. Pushing a nonzero Haar-density measure through the embedding and averaging proves that \(R_\alpha\) is a positive injective contraction on all of \(L^2(G)\).

Consequently every Peter–Weyl block has a scalar multiplier \(b_{\alpha,\tau}>0\). The constant block has multiplier one, and every other block has multiplier strictly below one: the strictly positive Markov kernel permits only constant fixed functions. No representation sectors have been discarded. If \(\rho\) were not faithful, the kernel would instead factor through \(G/\ker\rho\), annihilating the complementary sectors. The full-carrier assertion requires the declared global faithfulness.

## Localization selects an inverse-determinant preparation law

For each preparation define its real tangent metric, expressed in the basis of (GG1), by
\[
g_\Xi(X,Y)=\operatorname{Re}\operatorname{Tr}[(T_X\Xi)^\dagger T_Y\Xi],
\qquad w(\Xi)=(\det_Q g_\Xi)^{-1/2},
\qquad d\nu=\frac{w\,dP}{\mathbb Ew}.
\tag{GG4}
\]
The determinant is on the real \(d\)-dimensional Lie algebra. If \(\ell=\lambda_{\min}(A)>0\), then \(g_\Xi\ge\ell Q\), so
\[
w\le\ell^{-d/2},\qquad
w\|g_\Xi^{-1}\|_Q\le\ell^{-d/2-1}.
\tag{GG5}
\]
The sufficient condition used below is
\[
\boxed{k>n+\frac d2.}
\tag{GG6}
\]
It is deliberately sufficient, not necessary; special representations can require fewer columns, as in the scalar identity of [[relative-multiplication-transfer-and-the-rotor-limit|the SU(2) relative return]].

Here is an elementary inverse-moment proof. For a standard \(n\times k\) complex Gaussian matrix \(Z\), let \(r_i\) denote row \(i\). The Schur-complement identity gives
\[
[(ZZ^\dagger)^{-1}]_{ii}
=\operatorname{dist}(r_i,\operatorname{span}\{r_j:j\ne i\})^{-2}.
\tag{GG7}
\]
Conditionally on the other rows, the squared distance is \(\operatorname{Gamma}(k-n+1,1)\): orthogonal projection retains \(k-n+1\) independent complex Gaussian coordinates. Since \(\lambda_{\min}(ZZ^\dagger)^{-1}\le\operatorname{Tr}(ZZ^\dagger)^{-1}\), the elementary power bound for a finite sum yields
\[
\mathbb E\ell^{-p}<\infty\qquad(0<p<k-n+1).
\tag{GG8}
\]
Scaling by \(\sigma\) changes only the finite constant. Independence of the row distances is unnecessary. Hölder's inequality, with an exponent chosen within the strict bound, also permits any fixed polynomial factor in \(\|\Xi\|\). Thus (GG6) proves all integrability needed for (GG4), its inverse metric and the weak anchored cost below.

## The whole normalized transfer returns a Casimir

For fixed full-rank \(\Xi\),
\(h_\Xi(g)=\operatorname{Tr}[AB(g)]\) satisfies
\(h_\Xi(g^{-1})=h_\Xi(g)\) and
\(h_\Xi(e^X)=g_\Xi(X,X)+O_\Xi(|X|^4)\).
Faithfulness and compactness give a global bound
\(h_\rho(g):=\|\rho(g)-I\|_{\rm HS}^2\ge c\,\operatorname{dist}_Q(g,e)^2\), and \(h_\Xi\ge\ell h_\rho\). Gaussian radial bounds on a compact manifold therefore imply
\[
\alpha^{d/2}\int_G e^{-\alpha h_\Xi}dg\le C\ell^{-d/2},\qquad
\alpha^{d/2+1}\int_G\operatorname{dist}_Q(g,e)^2e^{-\alpha h_\Xi}dg
\le C\ell^{-d/2-1}.
\tag{GG9}
\]
These hold for all \(\alpha>0\). Fixed-preparation Laplace expansion, followed by dominated convergence using (GG8), gives
\[
\boxed{z_\alpha\sim
\frac{\pi^{d/2}}{\operatorname{Vol}_Q(G)}\alpha^{-d/2}\mathbb Ew,}
\]
\[
\alpha(R_\alpha-I)f\longrightarrow
\frac14\sum_{i,j}\mathbb E_\nu[(g_\Xi^{-1})_{ij}]\mathsf X_i\mathsf X_jf
\quad\text{uniformly for smooth }f.
\tag{GG10}
\]
For the numerator, replace \(f(Ug)-f(U)\) by its inversion-symmetric difference. It is bounded by a constant times \(\operatorname{dist}_Q(g,e)^2\). Its quadratic Taylor coefficient is \(1/2\), and the centered Gaussian tangent covariance is \(g_\Xi^{-1}/2\); these supply the factor \(1/4\). Equation (GG9) controls both the small-preparation tail and the spatial complement. No fourth inverse moment or \(O(\alpha^{-2})\) remainder is asserted under (GG6).

The law of \(\rho(a)\Xi\) equals that of \(\Xi\), and it conjugates \(g_\Xi\) by \(\operatorname{Ad}_{a^{-1}}\). The determinant weight preserves this invariance. Simplicity of \(\mathfrak g\) consequently forces the averaged inverse metric to be scalar:
\[
\mathbb E_\nu g_\Xi^{-1}=c_{\rho,k,\sigma}I,
\qquad c_{\rho,k,\sigma}=\frac1d\mathbb E_\nu\operatorname{tr}_Q g_\Xi^{-1}>0,
\qquad H_0=-\frac{c_{\rho,k,\sigma}}4\Delta_Q.
\tag{GG11}
\]
For fixed \(t\ge0\), with the identity at zero,
\[
\boxed{R_{n'/t}^{\,n'}\longrightarrow e^{-tH_0}\quad\text{strongly on }L^2(G).}
\tag{GG12}
\]
Here the integer \(n'\) counts steps, independently of the representation dimension \(n\). Finite Peter–Weyl sums and (GG10) prove the limit on a dense carrier; contractivity extends it to all vectors, uniformly on bounded time intervals. The positive multipliers also define a densely defined nonnegative operator \(H_\alpha=-\alpha\log R_\alpha\), with domain
\(\sum_\tau|\alpha\log b_{\alpha,\tau}|^2\|f_\tau\|^2<\infty\).
Finite Peter–Weyl sums are a core, and blockwise convergence proves strong-resolvent convergence to \(H_0\). No ordering over representations or uniform spectral-tail bound has been supplied, so the operator-norm limits proved for the special SU(2) family are not asserted here.

## The same preparation supplies the weak identity cost

Fix \(\beta\ge0\), and set
\[
q_U(\Xi)=\|(\rho(U)-I)\Xi\|_{\rm HS}^2=\operatorname{Tr}[AB(U)],
\qquad f_{\alpha,U}=e^{-\beta q_U/(4\alpha)}.
\tag{GG13}
\]
Multiply the relative Gaussian kernel at its two endpoints by these factors before averaging. Divide by the original scalar \(z_\alpha\) of (GG3), denoting the resulting operator by \(F_{\alpha,\beta}\). Positivity and injectivity follow from the same embedding argument. Pointwise domination by the unmarked kernel and the Schur test make it an exact positive contraction. It is generally no longer convolution, but it preserves the complete conjugation-invariant subspace.

The first-order endpoint expansion returns
\[
\boxed{\alpha(F_{\alpha,\beta}-I)f\longrightarrow-H_\beta f,\qquad
H_\beta=H_0+V_\beta,\qquad
V_\beta(U)=\frac\beta2\mathbb E_\nu q_U
=\beta\operatorname{Tr}[\overline A(I-\operatorname{Re}\rho(U))],}
\tag{GG14}
\]
where \(\overline A=\mathbb E_\nu A\) and \(\operatorname{Re}\rho=(\rho+\rho^\dagger)/2\). This is a real nonnegative smooth potential. The exponential remainder is bounded by \(C\alpha^{-2}\|\Xi\|^4\). Equations (GG8)–(GG9), including their polynomially weighted versions, control its normalized integral. The linear term localizes to the displayed \(\nu\)-expectation. The convergence is uniform on smooth functions and on bounded sets of the needed smooth norms.

The resulting uniformly elliptic operator has form domain \(H^1(G)\), operator domain \(H^2(G)\), and smooth core. Contractivity and telescoping along smooth semigroup orbits give
\(F_{n'/t,\beta}^{\,n'}\to e^{-tH_\beta}\) strongly on the full Haar carrier, uniformly on bounded nonnegative time intervals. The same is true on its complete conjugation-invariant subspace. This extends the weak-cost mechanism of [[anchored-word-cost-and-the-interacting-return|the anchored SU(2) benchmark]]; it does not yet supply a spatial gauge diagram. Dividing by the marked row degree instead cancels this first-order potential and defines a different return.

For full linear and quadratic marks, stack the columns of \(\Xi\) into \(\xi\in\mathbb C^{nk}\), take \(j\in\mathbb C^{nk}\), \(T=T^\dagger\), and assume \(\sigma^{-2}I+T>0\). Then
\[
\begin{aligned}
\mathcal Q_{U,V}
&=\sigma^{-2}I_{nk}
+I_k\otimes\left[\alpha B(U^{-1}V)+\frac\beta{4\alpha}(B(U)+B(V))\right]+T,\\
K_{\alpha,\beta}^{j,T}(U,V)
&=\frac{\exp(j^\dagger\mathcal Q_{U,V}^{-1}j)}
{\det(\sigma^2\mathcal Q_{U,V})}.
\end{aligned}
\tag{GG15}
\]
This inserts \(e^{2\operatorname{Re}j^\dagger\xi-\xi^\dagger T\xi}\) in the same preparation integral, including arbitrary cross-column blocks. General marks need not preserve centrality. Source differentiation keeps the unmarked \(z_\alpha\) fixed. Successive transfer edges have independent whole preparations; cross-edge marks use the block precision of [[marked-gaussian-constraints-and-sewing-measures|marked Gaussian sewing]]. The raw scalar factors remain part of every closed amplitude.

## Radial reciprocity and preparation shape are distinct

Write \(A=S\Omega\), where \(S=\operatorname{Tr}A=\|\Xi\|_{\rm HS}^2\) and \(\operatorname{Tr}\Omega=1\). The original isotropic law separates \(S\sim\operatorname{Gamma}(nk,\sigma^2)\) from its shape \(\Omega\), using shape and scale as the Gamma parameters. Since \(g_\Xi=Sg_\Omega\), the localized law factorizes exactly as
\[
S\sim\operatorname{Gamma}(q,\sigma^2),\qquad q=nk-\frac d2>1,
\qquad
d\nu_{\rm shape}\propto(\det_Q g_\Omega)^{-1/2}dP_{\rm shape}.
\tag{GG16}
\]
The same inverse-moment proof ensures that this shape normalization and its required inverse-metric expectation are finite. In particular \(\mathbb E_\nu S=\sigma^2q\) and \(\mathbb E_\nu S^{-1}=1/[\sigma^2(q-1)]\).

If \(\rho\) is irreducible, invariance and Schur's lemma give \(\mathbb E_{\nu_{\rm shape}}\Omega=I/n\). Thus
\[
\boxed{\overline A=aI,\qquad a=\frac{\sigma^2q}{n},\qquad
V_\beta(U)=\beta a\,[n-\operatorname{Re}\chi_\rho(U)].}
\tag{GG17}
\]
This is the exact Wilson character coefficient for the declared endpoint convention (GG13). Both coefficients come from the same preparation: \(a\propto\sigma^2\), whereas \(c_{\rho,k,\sigma}\propto\sigma^{-2}\).

The excess over radial reciprocity has the exact expression
\[
\boxed{
ac_{\rho,k,\sigma}=\frac q{q-1}\,\mathfrak s_{\rho,k},\qquad
\mathfrak s_{\rho,k}=\frac1{nd}\mathbb E_{\nu_{\rm shape}}
\operatorname{tr}_Q g_\Omega^{-1}\ge1.}
\tag{GG18}
\]
For a direct proof, \(\sum_iT_{e_i}^\dagger T_{e_i}=(d/n)I\): this operator commutes with the irreducible representation, and its trace is \(d\). Hence \(\operatorname{tr}_Q g_\Omega=d/n\) for every shape. The arithmetic–harmonic mean inequality gives \(\operatorname{tr}_Q g_\Omega^{-1}\ge nd\), with equality precisely when \(g_\Omega=I/n\). Equivalently, averaging first gives \(\mathbb E g_\Omega=I/n\), and matrix inversion is convex.

Equality in (GG18) holds exactly when \(g_\Omega=I/n\) almost surely. For \(k\ge n\), the shape law has full support on positive trace-one Hermitian matrices, and the positive determinant tilt keeps that support. Since each metric entry is linear in \(\Omega\), this equality is equivalent to the matrix identity
\[
\boxed{T_XT_Y+T_YT_X=-\frac2nQ(X,Y)I
\qquad(X,Y\in\mathfrak g).}
\tag{GG19}
\]
Indeed, \(g_\Omega(X,Y)=-\tfrac12\operatorname{Tr}[\Omega(T_XT_Y+T_YT_X)]\). Equality on the open set of positive trace-one matrices forces the displayed scalar matrix. The fundamental representation of SU(2) satisfies this Clifford relation. Thus \(q/(q-1)\) is the radial factor, while \(\mathfrak s_{\rho,k}\) measures a separate inverse-metric shape cost.

Lie-bracket closure itself excludes this equality when \(d>3\). If (GG19) held, \(\Gamma_i=i\sqrt n\,T_{e_i}\) would be Hermitian matrices with \(\{\Gamma_i,\Gamma_j\}=2\delta_{ij}I\). For \(i\ne j\), the trace pairing of \([T_{e_i},T_{e_j}]\) with \(T_{e_\ell}\) vanishes when \(\ell=i,j\) by cyclicity. For distinct \(i,j,\ell\), choose a fourth index \(m\). Conjugating the triple product by \(\Gamma_m\) reverses its sign, so its trace also vanishes. Thus the bracket is \(Q\)-orthogonal to the entire represented Lie algebra. Closure and nondegeneracy force it to be zero, contradicting \([T_{e_i},T_{e_j}]=2T_{e_i}T_{e_j}\ne0\), since each generator squares to \(-I/n\). Therefore
\[
\boxed{d>3\quad\Longrightarrow\quad
\mathfrak s_{\rho,k}>1,\qquad
ac_{\rho,k,\sigma}>\frac q{q-1}.}
\tag{GG19a}
\]
This strictness is for the fixed irreducible representation and preparation inventory above; it supplies no uniform excess over varying inventories and is not an excitation-gap statement. No classification of the remaining equality cases is required.

## Global faithfulness need not be irreducible

For a faithful reducible representation write
\(\rho=\bigoplus_r\rho_r\otimes I_{m_r}\), with inequivalent irreducible \(\rho_r\) of dimensions \(d_r\). Invariance under \(\rho(G)\) and under all unitary operators commuting with it gives
\[
\overline A=\bigoplus_r a_rI_{d_r}\otimes I_{m_r},\quad a_r>0,
\qquad
\boxed{V_\beta(U)=\beta\sum_r m_ra_r[d_r-\operatorname{Re}\chi_{\rho_r}(U)],}
\]
\[
\sum_r m_rd_ra_r=\sigma^2\left(nk-\frac d2\right).
\tag{GG20}
\]
The kinetic return is still the single Casimir of (GG11), because the Lie algebra is simple. The potential is generally a weighted sum of character costs; (GG17) cannot be imported by pretending the reducible representation is irreducible. Trivial summands contribute no identity cost. All \(a_r\) scale as \(\sigma^2\), but their individual values require the shared shape law.

[[weighted-character-scale-and-bounded-lie-sources|The weighted Hessian]] gives the precise confinement index \(I_{\overline A}\) for this returned cost and keeps it distinct from the unweighted projection index \(I_\rho\). [[fixed-group-compact-vacuum-and-oriented-source-return|The fixed-group compact source theorem]] uses that actual cost, including its reducible weights, on the four-face patch.

This distinction matters for the global target. By Schur's lemma the center acts by scalars in an irreducible representation. A noncyclic finite center cannot inject into \(U(1)\), whose finite subgroups are cyclic, so such a group has no faithful irreducible representation. The theorem uses a declared faithful finite-dimensional representation without imposing irreducibility, and therefore does not exclude these global forms.

A faithful finite-dimensional choice exists for every group in the stated class. The complexified adjoint representation is unitary and has kernel \(Z(G)\). This center is finite: its Lie algebra is zero, and it is compact. For each of its finitely many nonidentity elements \(z\), Peter–Weyl separation supplies an irreducible representation with \(\rho_z(z)\ne I\). The direct sum of the adjoint representation and these finitely many representations is faithful. This proves existence of the declared representation input without selecting a canonical choice.

The group, global form, representation, covariance scale, preparation inventory, identity-cost strength, normalization and step duration remain inputs. Condition (GG6) proves a fixed-group return; it does not select an inventory stable under growing diagrams. [[preparation-rank-and-locality|The rank/locality obstruction]] remains relevant when the configuration carrier grows. Strong full-carrier convergence here supplies neither a uniform spatial estimate nor the four-dimensional gauge-field, Poincaré, infinite-volume or physical-gap return.

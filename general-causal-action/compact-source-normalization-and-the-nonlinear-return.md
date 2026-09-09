# Compact Source Normalization Beyond the Harmonic Limit

The planar scalar probe has a genuine fixed-patch asymptotic expansion in the actual compact-group vacuum. Polynomial oscillator correctors compute its coefficients, but the scaled probe has a growing operator norm, so a low-order vacuum approximation alone does not justify normalized source response. Arbitrarily accurate local quasimodes control that loss. This establishes the finite-patch meaning of the nonlinear covariance and susceptibility coefficients while leaving their uniform spatial remainder as a separate estimate.

**Status: proved at each fixed finite planar patch.** [[planar-patch-confinement-and-the-spatial-soft-mode|PP1–13]] supplies the compact Hamiltonian, isolated well, complete Gauss carrier and scalar probe. [[nonlinear-scalar-source-and-the-vacuum-response-coefficient|The vacuum-response coefficient]] owns the finite oscillator formulas. The physical parameters and comparison paths are fixed before taking the limit.

## Fix both the Hamiltonian and the physical probe

Keep \(\kappa>0\) and the patch size \(L\) fixed. Specify the rooted connectors used in the based plaquette holonomies \(P_p\), and put
\[
h=(\kappa/g)^{1/4},\qquad
E_h=\sqrt{\kappa g}=\kappa h^{-2},\qquad
\widehat H_h=E_h^{-1}H_{L,g},\qquad
\widehat K_h=\widehat H_h-\widehat E_0(h).
\tag{CS1}
\]
Let \(\psi_h>0\) be its normalized actual vacuum. If
\(P_p=q_{0,p}I-i\mathbf q_p\cdot\sigma\), use the same bounded physical multiplication source at every strength:
\[
\mathcal B_L=\left|\sum_p v_{11}(p)\mathbf q_p\right|^2,\qquad
\widetilde B_h=\frac4{h^2}\mathcal B_L.
\tag{CS2}
\]
Multiplying a source by \(4/h^2\) cancels from its normalized susceptibility. It is a calculational normalization of this fixed probe, not a change in the Hamiltonian or the physical clock.

For its actual centered vector, variance and reduced susceptibility, set
\[
\begin{split}
m_h&=\langle\psi_h,\widetilde B_h\psi_h\rangle,&
F_h&=(\widetilde B_h-m_h)\psi_h,\\
N_h&=\|F_h\|^2,&
T_h&=\langle F_h,\widehat K_h^{-1}F_h\rangle,\qquad
\mathcal S_L(h)=T_h/N_h .
\end{split}
\tag{CS3}
\]
The inverse acts on the actual vacuum complement. Thus \(\mathcal S_L(h)\) is \(E_h\) times the physical susceptibility divided by physical variance.

Changing coordinates while pulling back this same function leaves (CS3) unchanged. Choosing different comparison paths for the based plaquettes can instead change \(\mathcal B_L\) beyond its common quadratic jet. Such a change is a new physical probe. [[comb-face-transport-and-the-first-nonlinear-jet|The comb presentation]] fixes a concrete family for evaluating the coefficients.

## The local operator and source have polynomial jets

In the equivariant local face chart \(x_p\), write the actual Haar density as \(\rho_L(x)\,dx\). Dilation \(x=hX\) and multiplication by its square root give the local differential expansion
\[
\widehat H_h\ \sim\
\mathcal O_L+hV_{1,L}+h^2V_{2,L}+\cdots .
\tag{CS4}
\]
This is an expansion after transforming the density as well as the derivatives. Each \(V_{r,L}\) is a polynomial differential operator on \(\mathbb R^{3L^2}\). Its coefficients are fixed by the raw-edge form, the magnetic potential and the chosen chart. The second-order jet includes the density correction; retaining only the quartic magnetic potential is insufficient.

Let \(\Pi f(X)=f(-X)\). Taylor homogeneity gives
\[
\Pi V_{r,L}\Pi=(-1)^rV_{r,L}.
\tag{CS5}
\]
The leading oscillator and its vacuum are even. The first physical excited state is the simple even scalar state of PP9. This parity statement concerns the local expansion; it does not assert that inversion of every compact link is a symmetry of the interacting theory.

For \(Y=\sum_pv_{11}(p)X_p\), the actual source has
\[
\widetilde B_h
\sim B_0+h^2B_2+O(h^4),\qquad
B_0=|Y|^2,\qquad
B_2=-\frac1{12}Y\cdot\sum_pv_{11}(p)|X_p|^2X_p .
\tag{CS6}
\]
This follows from
\(\mathbf q_p(hX)=hX_p/2-h^3|X_p|^2X_p/48+O(h^5|X_p|^5)\).
Both displayed source jets are even.

## Accurate quasimodes control the actual vacuum

The following construction is at fixed \(L\), with no estimate uniform in the number of faces. Choose a smooth invariant cutoff \(\chi(x)\), equal to one near the well and supported strictly inside the face chart. For a polynomial times the normalized oscillator Gaussian \(\Omega_L\), define the compact local vector
\[
(\mathcal J_h u)(x)
=h^{-3L^2/2}\rho_L(x)^{-1/2}\chi(x)\,u(x/h),
\tag{CS7}
\]
extended by zero outside the chart. On each fixed finite collection of such vectors, their inner products are preserved up to an error smaller than every power of \(h\). The cutoff and density transform commute with the simultaneous Gauss action.

Taylor expansion of the exact operator on these vectors gives, for every fixed integer \(M\),
\[
\left\|\widehat H_h\mathcal J_h u
-\mathcal J_h\sum_{r=0}^{M}h^rV_{r,L}u\right\|
\le C_{L,M,u}h^{M+1},\qquad V_{0,L}=\mathcal O_L.
\tag{CS8}
\]
Polynomial factors multiplying a Gaussian make the Taylor remainder integrable. Derivatives of the cutoff act where \(|X|\) is of order \(h^{-1}\), so those terms decay faster than any prescribed power. Smooth coefficients and finitely many derivatives suffice for each specified order.

The oscillator maps polynomial-Gaussian vectors into that same algebraic class. On a finite polynomial degree, its reduced inverses are finite Hermite calculations. Recursively solve the eigen-equation and normalization order by order for the vacuum and the first physical scalar state. Their leading physical eigenvalues are simple and separated by PP7–8. Every solvability condition fixes the next energy coefficient; the reduced inverse fixes the orthogonal vector correction. The resulting compact quasimodes have arbitrarily high residual order.

For small enough \(h\), depending on \(L\), PP7 separates the relevant actual eigenvalues from all other physical eigenvalues by positive constants in the scaled units. The spectral theorem then converts a quasimode residual into a norm bound on its component outside the corresponding eigenline. This proves the asymptotic eigenvector and eigenvalue expansions to every fixed finite order. No analyticity or convergence of their infinite formal series is needed.

In particular, writing \(c_L=2\sqrt{\lambda_{\min}(A_L)}\),
\[
\frac{\Delta_L(g)}{E_h}
=c_L+h^2d_L+O_L(h^4).
\tag{CS9}
\]
Odd energy coefficients vanish by (CS5) and simplicity of the selected leading eigenstates. The coefficient \(d_L\) is the difference of the two actual second-order energy coefficients, including the virtual \(V_{1,L}\) transitions.

## Multiplication by the scaled source needs higher accuracy

Although \(\mathcal B_L\) is bounded on the compact space, \(\|\widetilde B_h\|=O_L(h^{-2})\). A vacuum norm error of order \(h^3\) would therefore yield only an order-\(h\) bound after multiplication. It cannot establish a second-order source expansion.

Use the arbitrary-order vacuum construction above before multiplying. For example, a vacuum approximation with norm error \(O_L(h^8)\) produces a multiplied error \(O_L(h^6)\). Taylor expansion of the source on its polynomial-Gaussian quasimode, then truncation to the needed order, gives the actual centered-source expansion. All expectations in (CS3) are formed with that same actual vacuum. Parity cancels the odd scalar coefficients.

The reduced inverse in (CS3) causes no additional fixed-\(L\) obstruction. Equation (CS9) bounds its norm by \(2/c_L\) for sufficiently small \(h\). Alternatively solve the centered Poisson equation \(\widehat K_hY_h=F_h\) order by order using oscillator polynomial correctors, impose orthogonality to the actual vacuum, and apply this bound to the residual. Both constructions yield
\[
\begin{aligned}
m_h&=m_0+h^2m_2+O_L(h^4),\\
N_h&=N_0+h^2N_2+O_L(h^4),\\
T_h&=T_0+h^2T_2+O_L(h^4),\\
\mathcal S_L(h)&=\frac1{c_L}+h^2S_{2,L}+O_L(h^4),
\qquad m_0=3\sqrt{\lambda_{\min}},\quad N_0=6\lambda_{\min}.
\end{aligned}
\tag{CS10}
\]
Since \(N_0>0\) at each fixed \(L\), division by the actual variance is justified. The exact finite formulas for \(m_2,N_2,T_2,S_{2,L}\) are those in [[nonlinear-scalar-source-and-the-vacuum-response-coefficient|the vacuum-response coefficient]]. They include the source jet, moving centering, density and actual vacuum energy.

The same centered-source control realizes NV14–15 at fixed scaled durations. After removing the actual first-excitation component, the leading leaked vector has order \(h\) and finite Hermite degree. Project it onto the finite set of oscillator energy clusters it reaches, retaining any degeneracy within each cluster. PP's separated cluster limits and the quasimode construction return their spectral projections. Bounded functional calculus then gives their covariance weights through order \(h^2\), with remainder \(o_L(h^2)\); all other source weight is \(o_L(h^2)\). The innovation quotient follows for each fixed positive duration, since its leading denominator is nonzero. This concerns the specified two-point source response, not a theorem uniform over arbitrary growing families of marks.

This proves more than a formal oscillator analogy: the coefficients belong to the original compact source and Hamiltonian. Their spatial growth can also be bounded, although that does not yet control the remainder.

## A conservative spatial envelope for the first coefficient

For the specified comb connectors, the finite row formulas give an explicit polynomial bound. Write \(P_{\le m,L}\) for total oscillator Hermite degree at most \(m\), before taking invariants. The sine spectrum gives
\(\lambda_{\min}\asymp(1+L)^{-2}\) and \(\lambda_{\max}\le8\). Consequently each face coordinate and derivative obey
\[
\|X_{p,a}P_{\le m,L}\|\le C_m,\qquad
\|\partial_{X_{p,a}}P_{\le m,L}\|\le C_m(1+L)^{1/2}.
\tag{CS11}
\]
To see the dimension-independent constants, express that coordinate as a linear combination of normalized oscillator creation and annihilation operators. The squared coefficient sum is bounded by a diagonal entry of \(A_L^{1/2}\), and that of a derivative by a diagonal entry of \(A_L^{-1/2}\). Their operator-norm bounds give (CS11); total Hermite degree controls the remaining creation and annihilation factors.

A based face word has \(O(L)\) raw edges, with at most three occurrences of any specified raw edge. After comb substitution, an adjoint prefix has \(O(L^2)\) face factors. Its order-\(r\) row jet therefore has at most \(C_rL^{2+2r}\) monomial-derivative terms, including the sum over faces. Applying (CS11) successively on finite degree gives the deliberately loose estimate
\(\|D_rP_{\le m,L}\|\le C_{m,r}(1+L)^{5/2+2r}\).
There are \(O(L^2)\) raw rows. The density shifts and magnetic quartic terms obey the same upper envelope, so the exact jets in FJ12 satisfy
\[
\boxed{\|V_{1,L}P_{\le m,L}\|\le C_m(1+L)^9,\qquad
\|V_{2,L}P_{\le m,L}\|\le C_m(1+L)^{11}.}
\tag{CS12}
\]
The exponents are bounds from word counting, not claimed asymptotic growth rates.

Let \(u\), \(\eta_1\), \(\ell_L\) and \(d_L\) be the vacuum correction, first-excitation correction, source leakage and gap coefficient in NV4 and NV12–13. The vectors \(V_1\Omega_L\) and \(V_1\phi_L\) are odd physical scalars. A scalar with odd Hermite degree has at least three quanta: the one-quantum adjoint representation has no invariant vector. Thus on this odd physical subspace the harmonic inverse denominators obey
\[
\|K^{-1}\|\le\frac1{3\sqrt{\lambda_{\min}}},\qquad
\|(K-c_L)^{-1}\|\le\frac1{\sqrt{\lambda_{\min}}}.
\tag{CS13}
\]
If the odd subspace is absent, the relevant vectors are zero. Multiplication by the normalized soft polynomial
\(f_L=(|Y|^2/\sqrt{\lambda_{\min}}-3)/\sqrt6\)
has a degree-restricted norm bounded independently of \(L\), since \(Y/\lambda_{\min}^{1/4}\) is a normalized three-component oscillator coordinate.

Equations (CS12)–(CS13) and the finite coefficient formulas therefore give constants independent of \(L\ge1\) such that
\[
\boxed{
\|u\|+\|\eta_1\|+\|\ell_L\|\le C(1+L)^{10},\qquad
|d_L|\le C(1+L)^{19},\qquad
|S_{2,L}|\le C(1+L)^{21}.}
\tag{CS14}
\]
Indeed the two virtual energy terms cost at most \(O(L)\) times the squares of the order-\(L^9\) jet norms. The normalized susceptibility adds two inverse-gap factors to \(d_L\), or one to the squared leakage. The direct source-shape coefficient cancels from this normalized response as proved in NV11.

In particular the displayed first susceptibility correction, relative to \(1/c_L\), is bounded by \(Ch^2(1+L)^{20}\). The condition \(h(1+L)^{10}\to0\) makes that term subleading. It is **not** yet a sufficient window for the full compact asymptotic expansion: no bound uniform in \(L\) has been proved for the remainders in (CS8)–(CS10) or their onset thresholds. [[uniform-marked-well-return-and-the-growing-patch-test|Uniform marked well return]] states a concrete conjectural upgrade and derives its conditional joint-limit consequences. These coefficient bounds supply neither a positive nonlinear mass correction nor a fixed-coupling infinite-volume gap.

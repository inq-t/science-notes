# Comb Chart Ellipticity and Uniform Local Comparison

On a ball of total scaled face radius \(R\), the exact comb electric row matrix differs from its flat incidence matrix by at most \(6h\sqrt L\,R\) in operator norm. The long prefixes do not cause an exponential loss. Comparing this error with the smallest lattice singular value gives a uniform relative metric bound of order \(h(L+1)^{3/2}R\). Product Haar, the magnetic potential and finite-order local Taylor remainders admit compatible bounds. These are local comparisons of the inherited Hamiltonian; they do not assert that its actual low states are localized in the ball.

**Status: proved uniform local estimates for the specified comb chart.** [[comb-face-transport-and-the-first-nonlinear-jet|FJ]] owns the exact raw rows and product-Haar coordinates. [[uniform-marked-well-return-and-the-growing-patch-test|GW]] states the growing-patch test. [[compact-source-normalization-and-the-nonlinear-return|CS]] supplies the finite-degree oscillator bounds used below. All constants not explicitly indexed are independent of \(L,h,R\).

## The matrix being compared is the raw electric matrix

Put \(n=L+1\), \(N=L^2\), and write the based face variables as
\[
X_p=\exp(-ihx_p\cdot\sigma/2),\qquad
|x|^2=\sum_p|x_p|^2,\qquad B_R=\{x:|x|<R\}.
\tag{UC1}
\]
Assume \(hR\le1\). This is a single-valued equivariant product chart. Let \(\mathsf B_h(x)\) map a face covector \(v=(v_p)\in(\mathbb R^3)^N\) to the collection of its contractions with the coefficients of all scaled raw rows \(hZ_{e,t}\). Thus
\[
\sum_{e,t}|hZ_{e,t}u|^2=|\mathsf B_h(x)\nabla u|^2,\qquad
\mathsf B_0^{\mathsf T}\mathsf B_0=A_L\otimes I_3,\quad
A_L=4I-\operatorname{Adj}_L .
\tag{UC2}
\]
There are \(2L(L+1)\) raw edges. No facewise gauge quotient or reset electric operator is used. The estimates hold before the simultaneous Gauss restriction and hence also on physical invariant functions.

The exact logarithmic left and right Jacobians are
\[
J_\pm(y)=P_\parallel+
\frac{|y|}{2}\cot\frac{|y|}{2}\,P_\perp
\ \pm\frac12\operatorname{ad}_y ,
\qquad \operatorname{ad}_yt=y\times t .
\tag{UC3}
\]
Use the smooth value \(J_\pm(0)=I\); the sign assignment is that of FJ6. For \(|y|\le1\),
\(\|J_\pm(y)-I\|\le|y|\).
Indeed, for \(t=|y|/2\le1/2\),
\[
0\le1-t\cot t
=\frac{\sin t-t\cos t}{\sin t}
\le\frac{8}{23}t^2,
\]
using \(\sin t\ge23t/24\) and
\(\sin t-t\cos t=\int_0^t s\sin s\,ds\le t^3/3\).
The sum of this bound and \(t\) is at most \(|y|\).

## Four parts of the connector distortion

The exact row decomposition in FJ3–4 gives
\[
\boxed{\|\mathsf B_h(x)-\mathsf B_0\|
\le(\sqrt8+3)h\sqrt L\,|x|
\le6h\sqrt L\,|x|.}
\tag{UC4}
\]
To prove this, separate four contributions.

1. **Local logarithmic Jacobians.** Each row has at most two incident face blocks and each face occurs in four such blocks. Their block norms are at most \(h|x_p|\le h|x|\). The block row/column bound gives \(\sqrt8\,h|x|\). Orthogonal prefix rotations on these errors do not change their norms.
2. **Prefix rotations.** In the vertical left term, split
   \(J_-(hx_p)\operatorname{Ad}_{P}-I
   =(J_-(hx_p)-I)\operatorname{Ad}_{P}
   +(\operatorname{Ad}_{P}-I)\).
   The prefix contains at most \(L-1\) faces in one column, so telescoping its orthogonal factors gives
   \(\|\operatorname{Ad}_{P}-I\|\le h\sum_{k<j}|x_{c,k}|
   \le h\sqrt L\,|x|\).
   This part acts on exactly one face derivative in each affected row; every face appears in just one such row. Its operator norm is therefore the maximum block norm, not the sum over all prefixes.
3. **Bottom conjugation tails.** The exact identity
   \(h(\mathcal L-\mathcal R)=-h\operatorname{ad}_x\cdot\partial\)
   makes each tail linear. For its action on \(v\), Cauchy–Schwarz bounds each of at most \(L\) output rows by \(h|x|\,|v|\). The whole family has norm at most \(h\sqrt L\,|x|\).
4. **Vertical conjugation tails.** Treat each face column separately. The sum of squared tail outputs in that column is at most
   \(h^2L(\sum_{\rm column}|x_p|^2)
   (\sum_{\rm column}|v_p|^2)\).
   Summing columns bounds this family by \(h\sqrt L\,|x|\).

Thus the two nonlocal tail families and the prefix family each cost only \(\sqrt L\). The estimate does not replace the transported row by its principal part.

Write
\[
\lambda_L=\lambda_{\min}(A_L)
=8\sin^2\frac{\pi}{2n},\qquad
\eta=\frac{6h\sqrt L\,R}{\sqrt{\lambda_L}}
\le3h n^{3/2}R .
\tag{UC5}
\]
If \(\eta<1\), the triangle inequality applied to
\(|\mathsf B_0v|\ge\sqrt{\lambda_L}|v|\) gives the quadratic-form comparison
\[
\boxed{
(1-\eta)^2 A_L\otimes I_3
\ \le\ \mathsf B_h(x)^{\mathsf T}\mathsf B_h(x)
\ \le\ (1+\eta)^2 A_L\otimes I_3,\qquad x\in B_R .}
\tag{UC6}
\]
This is uniform ellipticity relative to the actual soft lattice metric, whose smallest eigenvalue decreases with \(L\).

## Haar and magnetic terms use the same total radius

Apart from a common constant, the exact scaled Haar density and potential are
\[
\rho_h(x)=\prod_p\left(
\frac{\sin(h|x_p|/2)}{h|x_p|/2}\right)^2,\qquad
W_h(x)=\frac2{h^2}\sum_p\left(1-\cos\frac{h|x_p|}{2}\right).
\tag{UC7}
\]
On \(B_R\),
\[
\boxed{
e^{-h^2R^2/8}\le\rho_h(x)\le1,\qquad
|\nabla\log\rho_h(x)|\le\frac{h^2|x|}{4},}
\tag{UC8}
\]
\[
\boxed{
\left(1-\frac{h^2R^2}{48}\right)\frac{|x|^2}{4}
\le W_h(x)\le\frac{|x|^2}{4}.}
\tag{UC9}
\]
For (UC8), \(\sin t/t\ge1-t^2/6\) and
\(-\log(1-z)\le z/(1-z)\), \(0\le t\le1/2\), give
\(-2\log(\sin t/t)\le8t^2/23\le(2t)^2/8\).
Also \(1/t-\cot t\le8t/23\), which gives the gradient bound after scaling. For (UC9), use
\(z^2/2-z^4/24\le1-\cos z\le z^2/2\) and
\(\sum_p|x_p|^4\le R^2|x|^2\).

For a nonzero smooth function supported in \(B_R\), define
\[
\mathcal R_h(u)=
\frac{\int (|\mathsf B_h\nabla u|^2+W_h|u|^2)\rho_h\,dx}
{\int |u|^2\rho_h\,dx},\qquad
\mathcal R_0(u)=
\frac{\int(\nabla u^{*}(A_L\otimes I_3)\nabla u
+|x|^2|u|^2/4)\,dx}{\int|u|^2dx}.
\]
With \(\zeta=h^2R^2/8\) and \(\vartheta=h^2R^2/48\), (UC6)–(UC9) imply
\[
\boxed{
e^{-\zeta}\min\{(1-\eta)^2,1-\vartheta\}\mathcal R_0(u)
\le\mathcal R_h(u)
\le e^\zeta(1+\eta)^2\mathcal R_0(u).}
\tag{UC10}
\]
The density is retained in both the form and norm. This estimate does not need to introduce a separate flat-density potential. Its error multiplies absolute oscillator energies, including the order-\(L^2\) vacuum energy; it is not automatically a comparably small error in their difference.

## Higher local Taylor remainders have polynomial size bounds

For every fixed integer \(M\ge0\), let \(\mathsf B_r(x)\) be the actual Taylor coefficients at \(h=0\). There is a constant \(C_M\), independent of the patch, such that
\[
\left\|\mathsf B_h(x)-\sum_{r=0}^M h^r\mathsf B_r(x)\right\|
\le C_M\bigl(h\sqrt L\,|x|\bigr)^{M+1},
\qquad h|x|\le1 .
\tag{UC11}
\]
The logarithmic Jacobian has uniformly bounded derivatives on \(|hx_p|\le1\), with its \(r\)-th \(h\)-derivative bounded by \(C_r|x_p|^r\). For a real-parameter prefix
\(\prod_k e^{-h\operatorname{ad}_{x_k}}\), differentiation and the multinomial formula bound its \(r\)-th derivative by
\((\sum_k|x_k|)^r\): all undifferentiated factors remain orthogonal. The one-face-per-prefix argument used in (UC4) then gives \(L^{r/2}|x|^r\). Conjugation tails have no derivatives beyond first order. Integral Taylor remainder proves (UC11), without complex-parameter exponential bounds.

Here is a form version that includes the measure. Assume \(h\sqrt L\,R\le1\). Set
\(a_h=\rho_h\mathsf B_h^{\mathsf T}\mathsf B_h\) and \(b_h=\rho_h W_h\).
Their Taylor polynomials, and that of \(\rho_h\), obey on \(B_R\)
\[
\begin{aligned}
\left|\,\rho_h-\sum_{r\le M}h^r\rho_r\,\right|
&\le C_Mh^{M+1}|x|^{M+1},\\
\left\|a_h-\sum_{r\le M}h^ra_r\right\|
&\le C_Mh^{M+1}L^{(M+1)/2}|x|^{M+1},\\
\left|\,b_h-\sum_{r\le M}h^rb_r\,\right|
&\le C_Mh^{M+1}L^{(M+1)/2}|x|^{M+3}.
\end{aligned}
\tag{UC12}
\]
For the density, derivatives of its logarithm of order \(r\ge2\) are bounded by \(C_r|x|^r\); its first derivative is bounded by \(Ch|x|^2\le C|x|\). Since \(\rho_h\le1\) along the real Taylor segment, the product rule proves its bound without a factor exponential in \(N\). The Jacobian bounds and \(\|\mathsf B_h\|\le\sqrt8+6\) prove the remaining claims. Write \(W_h=\sum_p|x_p|^2F(h|x_p|)\) with \(F\) smooth on \([-1,1]\) to handle its apparent \(h^{-2}\) factor.

For \(u\) of total oscillator Hermite degree at most fixed \(m\), (UC12) implies
\[
\left|q_{h,R}(u)-\sum_{r=0}^M h^r q_{r,R}(u)\right|
\le C_{m,M}h^{M+1}n^{(3M+9)/2}\|u\|^2 .
\tag{UC13}
\]
Here \(q_{h,R}=\int_{B_R}(\nabla u^*a_h\nabla u+b_h|u|^2)dx\), and \(q_{r,R}\) uses the displayed coefficient polynomials on that same ball. These are restricted integrals of the uncut oscillator vector. Multiplying \(u\) by a cutoff adds derivative terms that (UC13) does not discard.

To verify the exponent, the creation/annihilation estimates in CS11 give
\(\||x|^k u\|\le C_{m,k}n^k\|u\|\) and
\(\sum_{p,a}\|\partial_{p,a}u\|^2\le C_mn^3\|u\|^2\).
Every derivative vector has total degree at most \(m+1\). Consequently
\(\int |x|^{M+1}|\nabla u|^2dx\le C_{m,M}n^{M+4}\|u\|^2\).
Multiplying by \(L^{(M+1)/2}\) gives (UC13); the potential term has the smaller bound \(C_{m,M}n^{(3M+7)/2}\).
The density-norm Taylor error separately is at most
\(C_{m,M}h^{M+1}n^{M+1}\|u\|^2\).

## What this removes from the growing-patch test

For example, on \(R=n^2\), the exact metric distortion is \(O(hn^{7/2})\), while the logarithmic density error is \(O(h^2n^4)\). Both are small throughout the proposed \(hn^{10}\) window. More generally, with \(\epsilon=hn^{10}\) and a fixed \(A>0\), the radius
\[
R=A n^2\epsilon^{-1/3}
\quad\text{gives}\quad
\eta\le3A\epsilon^{2/3}n^{-13/2},\qquad
\zeta=\frac{A^2}{8}\epsilon^{4/3}n^{-16}.
\tag{UC14}
\]
Thus local chart degeneration is not an unquantified obstruction in that window. [[uniform-planar-localization-and-the-first-physical-levels|UP]] supplies the compact localization argument, its cutoff cost and control of competing states outside the well, giving an actual coarse spectral return. Equation (UC13) remains a local finite-degree form remainder, not the operator residual or actual centered Poisson estimate required for the marked remainder in GW4.

## The first two flat-density jets have sharper degree bounds

The exact coefficient estimates can be taken globally on polynomial-Gaussian vectors, without a cutoff: differentiate the pointwise bounds at \(h=0\), where every fixed \(x\) is admissible. Write \(P_{\le m,L}\) for total Hermite degree at most \(m\). For the flat-density operator jets \(V_1,V_2\) in FJ12, the result is
\[
\boxed{
\|V_1P_{\le m,L}\|\le C_m n^{9/2},\qquad
\|V_2P_{\le m,L}\|\le C_m n^6 .}
\tag{UC15}
\]
These are operator bounds between the actual finite-degree subspaces of the full oscillator cover, hence also on their physical invariant parts.

For the first coefficient, \(\rho_1=0\), the magnetic linear coefficient vanishes, and
\(a_1=\mathsf B_0^{\mathsf T}\mathsf B_1+\mathsf B_1^{\mathsf T}\mathsf B_0\).
Thus \(\|a_1(x)\|\le C\sqrt L\,|x|\). For vectors \(u,v\) of fixed bounded degree,
\[
|\langle u,V_1v\rangle|
\le C\sqrt L\,\||x|\nabla u\|\,\|\nabla v\|
\le C_m n^{9/2}\|u\|\,\|v\|.
\]
The polynomial differential operator \(V_1\) maps degree at most \(m\) into degree at most \(m+3\). Testing against that entire target space proves the first operator-norm estimate, without an infinite-dimensional polarization assumption.

The weighted quadratic coefficient \(q_2\) of (UC12) obeys
\(|q_2(u,v)|\le C_mn^6\|u\|\|v\|\): its derivative coefficient is bounded by \(CL|x|^2\), and its potential coefficient by \(C|x|^4\). The flat-density conversion must still be made. Since
\[
\rho_h^{-1/2}=1+h^2G+O(h^4),\qquad G=|x|^2/24,
\]
it gives the exact coefficient identity
\[
\boxed{
\langle u,V_2u\rangle=q_2(u,u)
+2\operatorname{Re}q_0(Gu,u).}
\tag{UC16}
\]
On fixed degree, \(\|Gu\|\le C_mn^2\|u\|\) and
\(\|\mathcal O_Lu\|\le C_mn^2\|u\|\). Hence
\(|q_0(Gu,u)|=|\langle Gu,\mathcal O_Lu\rangle|\le C_mn^4\|u\|^2\), below the \(n^6\) envelope. Polarization on degree at most \(m+4\), which contains \(V_2P_{\le m,L}\), proves the second bound in (UC15). This includes the Haar half-density term; it does not identify the weighted coefficient with the flat coefficient.

Let \(u_L,\eta_{1,L},\ell_L,d_L,S_{2,L}\) be respectively NV's first vacuum correction, first-excitation correction, source leakage, gap coefficient and normalized susceptibility coefficient. The harmonic reduced inverses on their physical sectors cost at most \(Cn\), and the normalized soft polynomial is bounded on each finite-degree space independently of \(L\). Equations (UC15) and NV's complete coefficient formulas therefore improve the earlier conservative CS14 envelopes to
\[
\boxed{
\|u_L\|+\|\eta_{1,L}\|+\|\ell_L\|\le Cn^{11/2},\qquad
|d_L|\le Cn^{10},\qquad
|S_{2,L}|\le Cn^{12}.}
\tag{UC17}
\]
Indeed the virtual energy terms cost \(n(n^{9/2})^2=n^{10}\), dominating the direct \(n^6\) term. Two inverse-gap factors give \(n^{12}\) for the gap contribution to susceptibility; the leakage contribution costs \(n(n^{11/2})^2=n^{12}\). All changing-vacuum and source terms remain included. The relative first correction is consequently bounded by \(Ch^2n^{11}\). This sharper coefficient envelope does not establish a full expansion in the enlarged window \(hn^{11/2}\ll1\); the uniform higher residual and marked Poisson bounds are separate statements.

## Every fixed jet and formal corrector has a polynomial envelope

The exact flat-density row, valued in the direct sum of raw-edge color spaces, is
\[
\mathsf E_h=\mathsf B_h\nabla-\tfrac12\mathsf B_h\nabla\log\rho_h
\sim\sum_{r\ge0}h^r\mathsf E_r,\qquad
\boxed{\|\mathsf E_rP_{\le m,L}\|
\le C_{m,r}n^{3r/2+3/2}.}
\tag{UC18}
\]
For \(r\ge1\), its derivative-matrix coefficient is homogeneous of degree \(r\), with norm at most \(C_rL^{r/2}|x|^r\), by (UC11). Its zero-order vector coefficient has degree \(r-1\), norm at most \(C_rL^{r/2}|x|^{r-1}\), and vanishes for \(r=1\). Indeed, the coefficient of \(h^{2k}\) in \(\nabla\log\rho_h\) has vector norm at most \(C_k|x|^{2k-1}\); multiplying by the row coefficients proves the assertion. At \(r=0\), only the constant derivative matrix remains. The finite-degree moment estimates used in (UC13) now give (UC18), including the norm over all raw rows.

The inherited flat electric form is \(\|\mathsf E_hu\|^2\). Pairing \(\mathsf E_su\) with \(\mathsf E_tv\), \(s+t=r\), bounds its coefficient by \(C_{m,r}n^{3r/2+3}\|u\|\|v\|\). The magnetic coefficient vanishes for odd \(r\); otherwise it is a constant times \(\sum_p|x_p|^{r+2}\), with finite-degree norm at most \(C_{m,r}n^{r+2}\). Each complete flat jet \(V_r\) raises total Hermite degree by at most \(r+2\). Polarization against this entire finite target space therefore gives
\[
\boxed{\|V_rP_{\le m,L}\|\le C_{m,r}n^{3r/2+3},
\qquad r\ge1.}
\tag{UC19}
\]
All constants are indexed by the fixed degree and order; no uniformity in \(m\) or \(r\) is asserted. The density terms in this argument are the exact Taylor coefficients of the row transform, not an omitted lower-order correction.

For either the harmonic vacuum or first physical scalar excitation, let \(\psi_0\) be the normalized leading vector, with absolute oscillator energy \(e_0\). Fix formal series
\[
\psi(h)\sim\sum_{r\ge0}h^r\psi_r,\qquad
e(h)\sim e_0+\sum_{r\ge1}h^re_r,\qquad
\|\psi(h)\|^2\sim1,
\]
with \(\langle\psi_0,\psi(h)\rangle\) real and positive to leading order. Let \(R_0=(\mathcal O_L-e_0)^{-1}\) on the complete physical complement of \(\psi_0\), and zero on its line. The harmonic isolation in [[planar-physical-cluster-separation-and-the-uniform-window|PS]] gives \(\|R_0\|\le Cn\) for both choices. At order \(r\), solve
\[
\begin{aligned}
e_r&=\langle\psi_0,V_r\psi_0\rangle
+\sum_{s=1}^{r-1}\langle\psi_0,(V_s-e_s)\psi_{r-s}\rangle,\\
\psi_r^\perp&=-R_0\sum_{s=1}^{r}(V_s-e_s)\psi_{r-s},\\
\langle\psi_0,\psi_r\rangle
&=-\tfrac12\sum_{j=1}^{r-1}\langle\psi_j,\psi_{r-j}\rangle .
\end{aligned}
\]
The last sum is real by pairing its conjugate terms; it fixes the remaining normalization component. If the leading degree is \(d_0=0\) or \(2\), then \(\psi_r\) has degree at most \(d_0+3r\). Resolvents preserve total Hermite degree and the physical subspace. Induction using (UC19) yields
\[
\boxed{
\|\psi_r\|\le C_r n^{11r/2},\qquad
|e_r|\le C_r n^{11r/2-1},
\qquad r\ge1.}
\tag{UC20}
\]
For the induction, \(V_s\psi_{r-s}\) costs at most
\(n^{3s/2+3+11(r-s)/2}\le n^{11r/2-1}\).
The terms \(e_s\psi_{r-s}\) have the same envelope; the reduced inverse adds one power of \(n\). Products fixing the normalization cost \(n^{11r/2}\). At each fixed order, all degrees and constants are finite and independent of patch size.

These are bounds on exact local coefficient operators and their formal eigenpairs; they do not assert convergence of the infinite formal series. [[compact-operator-taylor-remainder-on-planar-wells|The actual operator remainder]] and [[compact-cutoffs-and-uniform-polynomial-quasimodes|the compact cutoff construction]] supply the additional finite-order norm estimates. Together with actual spectral isolation and the centered-source construction, they yield [[uniform-nonlinear-planar-gap-and-marked-response|uniform nonlinear return]] on the stated growing-patch window.

# The Conditional Character Response Returns in the Original Chronology

The preparation-sensitive conditional fourth cumulant has a controlled time-resolved response in the actual compact vacuum. Its original mixed covariance returns the harmonic kernel uniformly over all scaled times and in absolute time integral along the growing-patch confinement window. A uniform temporal tail follows from centered evolution and the two actual source-vector estimates. This controls the full time profile of this one response, rather than only its signed susceptibility.

**Status: proved uniform actual temporal comparison and bulk profile limit for the fixed three-block \(SU(2)\) preparation family.** [[conditional-cumulant-influence-and-the-original-chronology|CI]] identifies the influence and harmonic profile. [[conditional-influence-vectors-and-the-original-source-carrier|IV]] and [[magnetic-character-insertion-and-centered-source-control|MI]] return the two actual vectors; [[centered-compact-chronology-and-integrable-source-return|CC]] proves their integrable chronological comparison. The full exterior and original source maps are retained, together with each preparation's own physical Hamiltonian.

## One mixed kernel with its actual vacuum and centering

Fix the preparation interval \(I\Subset(-1/14,1/16)\) of [[uniform-weighted-character-return-and-the-soft-gap|UW]]. On the open \(L\times L\) patch, retain every vertex Gauss constraint and the complete based face words. Write
\[
n=L+1,\qquad h=(\kappa/(15g))^{1/4},\qquad
\delta=hn^{10},\qquad\theta=hn^{11/2},\qquad
0<\delta\le\eta_I.
\tag{TP1}
\]
The fixed upper bound may be reduced to accommodate the finite approximation orders in the source theorems. All constants below are independent of \(L,h\), the source face \(r\), and \(\varepsilon\in I\).

Let \(\widehat H_\varepsilon\) be the specified scaled Hamiltonian, \(v_\varepsilon\) its normalized positive vacuum, \(\lambda_\varepsilon\) its vacuum energy, and \(K_\varepsilon=\widehat H_\varepsilon-\lambda_\varepsilon\). Set \(B_\varepsilon=\partial_\varepsilon\widehat H_\varepsilon\), holding \(L,h\), the electric operator and source maps fixed. Let \(F_\mu\) be CI2's full influence of the conditional fourth cumulant of the original GM mark \(2q_\rho(P_r)/h\), conditioned on all other complete faces. Put
\[
f_h=(F_\mu-\mathbb E_\mu F_\mu)v_\varepsilon,\qquad
g_h=h^{-2}(B_\varepsilon-\mathbb E_\mu B_\varepsilon)v_\varepsilon.
\]
The actual normalized mixed profile is
\[
\boxed{
k_{\varepsilon,L,r,h}(s)
=\langle f_h,e^{-sK_\varepsilon}g_h\rangle
=h^{-2}\operatorname{Cov}_\mu
\bigl(F_\mu(U_0),B_\varepsilon(U_s)\bigr).}
\tag{TP2}
\]
Here \(U_s\) follows the stationary ground transform of the original Hamiltonian. The influence includes the changing conditional mean, covariance and retained marginal. Neither source is substituted by a conditional-update generator.

## The actual vectors satisfy the centered chronological criterion

In the harmonic law let
\[
C_L=\sqrt{4I-\operatorname{Adj}_L},\qquad
\sigma_{L,r}=\bigl((C_L^{-1})_{rr}\bigr)^{-1},\qquad
\eta_r=\sigma_{L,r}(C_L^{-1}X)_r.
\]
With harmonic vacuum \(\Omega_L\), define the centered physical vectors
\[
f_0=\bigl(|\eta_r|^4-10\sigma_{L,r}|\eta_r|^2
+15\sigma_{L,r}^2\bigr)\Omega_L,
\]
\[
b_0=(B_2-\mathbb E_0B_2)\Omega_L,\qquad
B_2=-\frac7{120}\sum_p|X_p|^4.
\]
Both have total Hermite degree at most four, even though their face support need not be local. If \(Q\) and \(Q_0\) remove the actual and harmonic vacua and \(\mathcal J\) is the exact cutoff density map, put \(\mathcal I=Q\mathcal JQ_0\). IV13 and MI11 prove
\[
\boxed{
\|f_0\|\le C_I,\quad \|b_0\|\le C_In,\quad
\|f_h-\mathcal If_0\|\le C_I\theta,\quad
\|g_h-\mathcal Ib_0\|\le C_In\theta.}
\tag{TP3}
\]
The \(O(n)\) magnetic norm uses the centered correlated Gaussian fourth-power sum, not the \(O(n^2)\) size of its mean. Subtracting the common harmonic scalar before amplitude comparison leaves the actual centered insertion unchanged.

These are exactly CC10's hypotheses. Its generator defect is \(C_Ihn^{9/2}\), the two physical gaps are bounded below by \(c_I/n\), and centering \(\mathcal I\) makes the Duhamel defect orthogonal to the actual vacuum. CC9–11 therefore give
\[
\boxed{\begin{aligned}
|k_{\varepsilon,L,r,h}(s)-k_{0,L,r}(s)|
&\le C_Ihn^{13/2}(1+s/n)e^{-c_Is/n},
\\
\int_0^\infty|k_{\varepsilon,L,r,h}(s)-k_{0,L,r}(s)|\,ds
&\le C_Ihn^{15/2}
=C_I\delta n^{-5/2},
\end{aligned}}
\tag{TP4}
\]
where \(k_{0,L,r}(s)=\langle f_0,e^{-sK_0}b_0\rangle\). In particular,
\[
\sup_{s\ge0}|k_{\varepsilon,L,r,h}(s)-k_{0,L,r}(s)|
\le C_I\delta n^{-7/2}.
\tag{TP5}
\]
The absolute value is inside the time integral. These estimates do not follow by comparing signed integrals, and their proof does not assume that either mixed profile has a fixed sign.

## A uniform actual temporal tail

CI7–9 evaluates
\[
\boxed{
k_{0,L,r}(s)
=-7\sigma_{L,r}^4
\sum_{p\in\Lambda_L}(e^{-sC_L})_{pr}^4,\qquad
|k_{0,L,r}(s)|\le C(1+s)^{-6}.}
\tag{TP6}
\]
The underlying estimate comes from killed-walk subordination and [[lattice-poisson-tails-and-collar-localization|LP7]], with \(\sigma_{L,r}\le2\).

Integrating TP4 only after \(T\) bounds the error tail by
\(C_I\delta n^{-5/2}(1+T/n)e^{-c_IT/n}\), after adjusting constants. For \(T\ge1\), set \(z=T/n\); the function \(z^{5/2}(1+z)e^{-c_Iz}\) is bounded. For \(T\le1\), the full integral bound suffices. Thus CC12, now with its actual source hypotheses discharged, proves
\[
\boxed{
\sup_{\substack{L\ge1,\ r\in\Lambda_L,\ \varepsilon\in I\\0<hn^{10}\le\eta_I}}
\int_T^\infty|k_{\varepsilon,L,r,h}(s)|\,ds
\le C_I(1+T)^{-5}
+C_I\eta_I(1+T)^{-5/2},\qquad T\ge0.}
\tag{TP7}
\]
The second power is a uniform upper bound obtained by optimizing over patch sizes. It is not an asserted asymptotic decay exponent of an individual system. This estimate proves uniform integrability of the actual family despite its closing scaled physical gap.

## The bulk candidate is the inherited lattice profile

Let the source face recede from every boundary and translate it to the origin. On the full square lattice define
\[
C_\infty=\sqrt{4I-\operatorname{Adj}_{\mathbb Z^2}},\qquad
a_s(x)=(e^{-sC_\infty})_{x0},
\]
\[
\sigma_\infty=
\left\{\int_{[-\pi,\pi]^2}
\frac{d^2q}{(2\pi)^2\sqrt{4-2\cos q_1-2\cos q_2}}\right\}^{-1}>0.
\]
[[character-memory-in-the-local-conditional-fourth-cumulant|LCM10–11]] proves \(\sigma_{L,r}\to\sigma_\infty\) and integrability of \(\sum_xa_s(x)^4\). The candidate profile is
\[
\boxed{
k_\infty(s)=-7\sigma_\infty^4
\sum_{x\in\mathbb Z^2}a_s(x)^4.}
\tag{TP8}
\]
It is strictly negative at every finite \(s\), has absolute tail bounded by \(C(1+T)^{-5}\), and has integral \(-7\sigma_\infty^4J_\infty\).

Here is the full harmonic convergence argument. For every fixed \(s,x\), killed-walk comparison and a containing ball of increasing radius give
\[
0\le(e^{-sC_L})_{r+x,r}\le a_s(x),\qquad
(e^{-sC_L})_{r+x,r}\longrightarrow a_s(x).
\]
Extend the killed kernel by zero outside its patch. Domination by the summable sequence \(a_s(x)^4\) gives convergence of the fourth-power sum for each \(s\). No nesting of the patches is needed. TP6 then gives dominated convergence in time.

To obtain uniform rather than only pointwise convergence, write \(a_s^L=e^{-sC_L}e_r\), extended by zero. Since \(\|C_L\|\le\sqrt8\) and \(\|a_s^L\|_2\le1\),
\[
\left|\frac{d}{ds}\sum_p(a_s^L(p))^4\right|
\le4\|a_s^L\|_6^3\|C_La_s^L\|_2
\le4\sqrt8.
\]
The same estimate holds on the full lattice. With \(\sigma_{L,r}\le2\), the harmonic profiles are uniformly Lipschitz. Their pointwise convergence therefore is uniform on each bounded interval; the common \(C(1+s)^{-6}\) bound controls the remaining pointwise tail. Consequently
\[
\boxed{
\|k_{0,L,r}-k_\infty\|_{L^1(0,\infty)}
+\sup_{s\ge0}|k_{0,L,r}(s)-k_\infty(s)|
\longrightarrow0.}
\tag{TP9}
\]

Combine TP4–5 with TP9. For any sequence with the source's distance to the boundary tending to infinity, \(\varepsilon_L\in I\), and \(0<h_L(L+1)^{10}\le\eta_I\),
\[
\boxed{
\|k_{\varepsilon_L,L,r_L,h_L}-k_\infty\|_{L^1(0,\infty)}
+\sup_{s\ge0}
|k_{\varepsilon_L,L,r_L,h_L}(s)-k_\infty(s)|
\longrightarrow0.}
\tag{TP10}
\]
The confinement parameter need not tend to zero. This is convergence of one actual mixed response profile; it does not construct a fixed-coupling infinite-volume compact vacuum.

## The clock and the source scope remain explicit

CI5 gives
\[
h^{-2}\partial_\varepsilon\mathbf K_{\varepsilon,L,r}(h)
=-2\int_0^\infty k_{\varepsilon,L,r,h}(s)\,ds.
\]
Combining this exact identity with TP4 and TP6 improves the direct conditional estimate by one power of the patch width:
\[
\boxed{\begin{aligned}
\left|\partial_\varepsilon\mathbf K_{\varepsilon,L,r}(h)
-14h^2\sigma_{L,r}^4J_{L,r}\right|
&\le C_Ih^3n^{15/2},\\
\left|\mathbf K_{\varepsilon_2,L,r}(h)
-\mathbf K_{\varepsilon_1,L,r}(h)
-14(\varepsilon_2-\varepsilon_1)h^2\sigma_{L,r}^4J_{L,r}\right|
&\le C_I|\varepsilon_2-\varepsilon_1|h^3n^{15/2}.
\end{aligned}}
\tag{TP11}
\]
The second line integrates the actual parameter derivative on \(I\), so it retains arbitrarily small contrast sizes. TP10 recovers the bulk derivative \(14\sigma_\infty^4J_\infty\), now with absolute temporal control rather than a cancellation-prone signed limit. The additive error in TP4 does not prove that every actual finite-regulator profile is negative for all times.

Time \(s\) is the scaled time of the original \(K_\varepsilon\). Physical duration is \(s/E\), with the supplied common \(E=\kappa h^{-2}\). Since \(\partial_\varepsilon H_{\rm physical}=E B_\varepsilon\), the corresponding normalized physical-insertion profile at duration \(t\) is \(E\,k_{\varepsilon,L,r,h}(Et)\). This identity preserves the integrated susceptibility without fitting a new clock. The uniform profile limit in TP10 is stated in scaled time; a limit at fixed physical duration is not inferred from it.

The influence retains the complete exterior and the global insertion retains every face. Their joint temporal return must not be read as an autonomous one-face Markov law. A spatial composition still has to preserve [[regional-innovation-and-exterior-information-balance|RI's exterior response]] and [[spatial-block-sewing-and-the-vacuum-cap-response|SB's caps and source exchange]]. One controlled matrix element supplies no positive floor for the complete physical source algebra, no fixed-coupling thermodynamic limit, and no four-dimensional Yang–Mills construction.

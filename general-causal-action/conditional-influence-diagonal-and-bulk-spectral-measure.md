# The Conditional Influence Has a Soft Bulk Spectral Measure

The actual conditional influence returns diagonally through the original chronology, uniformly over scaled time and in absolute time integral. Its normalized bulk spectral measure is the fourth convolution of an explicitly weighted lattice frequency law. That measure has density proportional to the cube of the energy near zero, so the diagonal correlation decays as the inverse fourth power of time. Its susceptibility is finite even though its spectral support reaches zero.

**Status: proved actual diagonal return, uniform temporal tail, bulk spectral-measure return and exact low-energy asymptotics.** [[conditional-influence-vectors-and-the-original-source-carrier|IV]] supplies the full actual influence vector; [[centered-compact-chronology-and-integrable-source-return|CC]] returns its centered evolution. The harmonic law below retains the complete exterior of the marked face. Weak spectral-measure convergence is not used to infer an infimum over actual normalized chronological filters.

## Return the original influence against itself

Use the fixed three-block \(SU(2)\) preparation family and compact parameter interval \(I\) of [[uniform-weighted-character-return-and-the-soft-gap|UW]]. On the open \(L\times L\) patch retain all Gauss constraints and put
\[
n=L+1,\qquad h=(\kappa/(15g))^{1/4},\qquad
\delta=hn^{10},\qquad\theta=hn^{11/2},
\qquad 0<\delta\le\eta_I.
\]
Let \(K_h=\widehat H_{\varepsilon,L,h}-\lambda_{\varepsilon,L,h}\), and let \(f_h\) be IV1's centered actual influence vector of the conditional fourth cumulant of the same GM mark \(2q_\rho(P_r)/h\). Conditioning retains every other complete face. Define
\[
d_{\varepsilon,L,r,h}(s)=\langle f_h,e^{-sK_h}f_h\rangle,
\qquad s\ge0.
\tag{DI1}
\]
This is the actual diagonal covariance of the influence, with its own vacuum and mean. It is nonnegative by spectral calculus; this diagonal positivity says nothing about the sign of a mixed covariance.

In the harmonic law write
\[
C_L=\sqrt{4I-\operatorname{Adj}_L},\qquad
\sigma_{L,r}=\bigl((C_L^{-1})_{rr}\bigr)^{-1},\qquad
\eta_r=\sigma_{L,r}(C_L^{-1}X)_r,
\]
\[
f_{0,L,r}=\mathcal H_{4,\sigma_{L,r}}(\eta_r)\Omega_L,\qquad
\mathcal H_{4,\sigma}(\eta)=|\eta|^4-10\sigma|\eta|^2+15\sigma^2 .
\]
IV proves \(\|f_0\|\le C\) and
\(\|f_h-\mathcal I f_0\|\le C_I\theta\), where
\(\mathcal I=Q_h\mathcal JQ_0\) centers the cutoff comparison in both vacua. Applying CC9 with both harmonic input norms \(O(1)\), and both source errors \(O(\theta)\), gives
\[
\boxed{\begin{aligned}
|d_{\varepsilon,L,r,h}(s)-d_{0,L,r}(s)|
&\le C_Ihn^{11/2}(1+s/n)e^{-c_Is/n},\\
\int_0^\infty|d_{\varepsilon,L,r,h}(s)-d_{0,L,r}(s)|\,ds
&\le C_Ihn^{13/2}=C_I\delta n^{-7/2}.
\end{aligned}}
\tag{DI2}
\]
Here \(d_{0,L,r}(s)=\langle f_0,e^{-sK_0}f_0\rangle\). In particular the uniform-in-time error is \(O_I(\theta)=O_I(\delta n^{-9/2})\). CC's finite-degree input condition is satisfied because \(f_0\) has total Hermite degree four; no finite-dimensional invariant source space for \(K_h\) is assumed.

## The conditional residual changes the lattice weight

Define the positive diagonal kernel
\[
b_{L,r}(s)=(C_L^{-1}e^{-sC_L})_{rr}
=\int_s^\infty(e^{-tC_L})_{rr}\,dt .
\tag{DI3}
\]
In the stationary harmonic chronology,
\[
\operatorname{Cov}_0(\eta_{r,a}(0),\eta_{r,b}(s))
=\sigma_{L,r}^2 b_{L,r}(s)\delta_{ab}.
\]
Indeed the field covariance at separation \(s\) is \(C_Le^{-sC_L}\); multiplying by the two residual coefficients \(\sigma C_L^{-1}\) produces this expression. The radial fourth-Hermite contraction is \(120q^4\) when the component cross covariance is \(q\). Therefore
\[
\boxed{
d_{0,L,r}(s)=120\sigma_{L,r}^8 b_{L,r}(s)^4,\qquad
d_{0,L,r}(0)=120\sigma_{L,r}^4.}
\tag{DI4}
\]
The inverse \(C_L^{-1}\) is essential. The influence contains the complete exterior conditional residual, not the original coordinate \(X_r\).

For the unrestricted lattice set
\[
\omega(k)=\sqrt{4-2\cos k_1-2\cos k_2},\qquad
b_\infty(s)=\int_{[-\pi,\pi]^2}
\frac{e^{-s\omega(k)}}{\omega(k)}\,\frac{d^2k}{(2\pi)^2},
\qquad \sigma_\infty=b_\infty(0)^{-1}.
\tag{DI5}
\]
The integral at zero is finite and positive: the only zero of \(\omega\) is at the origin, and \(\omega(k)\ge2|k|/\pi\) on the Fourier square. Thus the apparent \(1/|k|\) singularity is integrable in two dimensions.

[[lattice-poisson-tails-and-collar-localization|LP2–7]] bounds the killed Poisson diagonal by its unrestricted counterpart. Integrating that comparison and its \(C(1+t)^{-2}\) bound gives, for every box and source face,
\[
\boxed{
0<b_{L,r}(s)\le b_\infty(s)\le\frac{C}{1+s},\qquad
0<\sigma_\infty\le\sigma_{L,r}\le2.}
\tag{DI6}
\]
The lower bound on \(\sigma_{L,r}\) follows from \(b_{L,r}(0)\le b_\infty(0)\). Its upper bound is the harmonic conditional-variance inequality
\(\sigma_{L,r}\le(C_L)_{rr}\le2\). No assumption that the source face is far from the boundary is needed for these uniform inequalities.

Consequently the harmonic diagonal has a uniform integrable tail,
\[
0\le d_{0,L,r}(s)\le C(1+s)^{-4},\qquad
\int_T^\infty d_{0,L,r}(s)\,ds\le C(1+T)^{-3}.
\]
Integrating DI2 from \(T\), and maximizing
\(n^{-7/2}(1+T/n)e^{-c_IT/n}\) over \(n\ge2\), proves the actual bound
\[
\boxed{
\sup_{\substack{L\ge1,\ r\in\Lambda_L,\ \varepsilon\in I\\0<hn^{10}\le\eta_I}}
\int_T^\infty d_{\varepsilon,L,r,h}(s)\,ds
\le C_I(1+T)^{-3}+C_I\eta_I(1+T)^{-7/2}.}
\tag{DI7}
\]
For \(T\ge1\), substitute \(z=T/n\) and bound
\(z^{7/2}(1+z)e^{-c_Iz}\); for \(T\le1\), the full integral estimate suffices. The second exponent is an optimized uniform upper bound, not the decay exponent asserted for an individual compact system.

## Normalize before identifying the spectral measure

DI4 and DI6 give \(d_{0,L,r}(0)\ge120\sigma_\infty^4>0\). Equation DI2 at zero therefore gives, after reducing the fixed window if necessary,
\[
\boxed{
0<c_I\le\|f_h\|^2\le C_I,\qquad
0<c_I\le\|f_0\|^2\le C_I.}
\tag{DI8}
\]
Define the probability-normalized diagonal functions
\[
r_{\varepsilon,L,r,h}(s)
=\frac{d_{\varepsilon,L,r,h}(s)}{d_{\varepsilon,L,r,h}(0)},
\qquad
r_{0,L,r}(s)=\frac{d_{0,L,r}(s)}{d_{0,L,r}(0)}
=[\sigma_{L,r}b_{L,r}(s)]^4 .
\tag{DI9}
\]
Subtract these fractions with their actual normalizers retained. The denominator errors are \(O_I(\theta)\); the harmonic numerator is at most its initial value times \(e^{-\gamma_0s}\), with \(\gamma_0\ge c/n\). Thus DI2 and DI7 also hold for these normalized functions after changing constants. This uses a proved lower bound on the entire source norm, not an inverse actual conditional variance.

Let \(\{u_\alpha,\omega_\alpha\}\) be an orthonormal eigenbasis for \(C_L\). The probability measure
\[
m_{L,r}=\sigma_{L,r}\sum_\alpha
\frac{|u_\alpha(r)|^2}{\omega_\alpha}\,\delta_{\omega_\alpha}
\tag{DI10}
\]
has Laplace transform \(\sigma_{L,r}b_{L,r}(s)\). Consequently the normalized harmonic source spectral measure is exactly
\[
\nu_{0,L,r}=m_{L,r}^{*4}.
\]
This identity follows from DI9 and uniqueness of Laplace transforms of finite measures. It describes the spectral law of the single invariant fourth-Hermite source; it does not introduce four independent physical systems or remove Gauss constraints.

## The actual bulk diagonal and spectral law return

Let the source's distance to every boundary tend to infinity and translate it to the origin. Killed-walk comparison, subordination and the common integrable \(t^{-2}\) bound show
\[
b_{L,r}(s)\longrightarrow b_\infty(s),\qquad
\sigma_{L,r}\longrightarrow\sigma_\infty
\]
at every fixed \(s\). This is the same containing-patch limit as [[character-memory-in-the-local-conditional-fourth-cumulant|LCM10]], without a requirement that the boxes be nested.

The functions \(b_{L,r}\) have derivative
\(- (e^{-sC_L})_{rr}\), of absolute value at most one. They are uniformly Lipschitz, as is \(b_\infty\). Pointwise convergence is therefore uniform on bounded intervals. DI6 controls the remainder of the time axis. Taking fourth powers and using the integrable diagonal tail gives
\[
\boxed{
d_{0,L,r}\longrightarrow d_\infty
\quad\text{uniformly on }[0,\infty)\text{ and in }L^1(ds),
\qquad
d_\infty(s)=120\sigma_\infty^8 b_\infty(s)^4.}
\tag{DI11}
\]
DI2 gives the same convergence for the actual diagonals throughout the original confinement window, including sequences with \(\delta\) fixed. DI8 gives the corresponding convergence of their normalized versions to
\[
r_\infty(s)=[\sigma_\infty b_\infty(s)]^4.
\]
The preparation parameter may vary in \(I\) along the sequence.

The normalized limiting measure is
\[
\boxed{
m_\infty
=\sigma_\infty\,\omega_*
\left(\frac{d^2k}{(2\pi)^2\omega(k)}\right),\qquad
\nu_\infty=m_\infty^{*4}.}
\tag{DI12}
\]
The notation \(\omega_*\) denotes pushforward by \(k\mapsto\omega(k)\). The first measure has total mass one and support in \([0,\sqrt8]\); its fourth convolution has support in \([0,4\sqrt8]\).

For completeness, the actual normalized spectral probability measures also converge weakly to \(\nu_\infty\). Their Laplace transforms are the normalized actual diagonals. Pointwise convergence to \(r_\infty\), continuous at zero with value one, gives tightness directly:
\[
\nu_h([M,\infty))
\le \frac{1-r_h(t)}{1-e^{-tM}}\qquad(t>0).
\]
First choose \(t\) small, using \(r_\infty(t)\to1\), then choose \(M\) large. Any weak subsequential limit has the same Laplace transform. Uniqueness follows, for example, by mapping \(\lambda\mapsto e^{-\lambda}\) and using uniqueness of a finite measure on \([0,1]\) from all its polynomial moments. This proves weak return without asserting convergence of support endpoints.

## The low-energy density and long-time constant

The low-energy density can be calculated without a lattice density-of-states formula. In polar coordinates \(k=r\vartheta\), uniformly in \(\vartheta\in S^1\),
\[
\omega(r\vartheta)=r+O(r^3),\qquad
\partial_r\omega(r\vartheta)=1+O(r^2).
\]
For a sufficiently small energy \(\lambda>0\), the level set lies in this chart and has a unique radial solution
\(r=r(\lambda,\vartheta)=\lambda+O(\lambda^3)\), with
\(\partial_\lambda r=1+O(\lambda^2)\). Changing variables on each ray gives
\[
\boxed{
\frac{dm_\infty}{d\lambda}
=\frac{\sigma_\infty}{(2\pi)^2}
\int_{S^1}\frac{r(\lambda,\vartheta)}{\lambda}
\partial_\lambda r(\lambda,\vartheta)\,d\vartheta
=\frac{\sigma_\infty}{2\pi}+O(\lambda^2).}
\tag{DI13}
\]
The origin is the only zero of the dispersion, so there are no additional contributions for sufficiently small \(\lambda\).

On the simplex where four positive energies sum to \(\lambda\), each factor in the convolution is \(c+O(\lambda^2)\), with \(c=\sigma_\infty/(2\pi)\). The simplex volume is \(\lambda^3/3!\). Hence
\[
\boxed{
\frac{d\nu_\infty}{d\lambda}
=\frac{\sigma_\infty^4}{96\pi^4}\lambda^3
+O(\lambda^5),\qquad \lambda\downarrow0.}
\tag{DI14}
\]
In particular zero belongs to its support but is not an atom. Every sufficiently small positive energy interval has nonzero mass.

The same local calculation gives the long-time expansion
\[
b_\infty(s)=\frac1{2\pi s}+O(s^{-3}).
\]
Indeed the density of the unnormalized measure in DI5 is \(1/(2\pi)+O(\lambda^2)\) near zero, while the complement of a fixed small energy neighborhood contributes exponentially little. Thus
\[
\boxed{
r_\infty(s)=\frac{\sigma_\infty^4}{16\pi^4}s^{-4}
+O(s^{-6}),\qquad
d_\infty(s)=\frac{15\sigma_\infty^8}{2\pi^4}s^{-4}
+O(s^{-6}).}
\tag{DI15}
\]
These are exact leading bulk constants in the original scaled chronology. They are not the long-time asymptotics of each finite compact system.

The inverse-energy moments make the distinction explicit:
\[
\boxed{
\int\lambda^{-p}\,\nu_\infty(d\lambda)<\infty
\quad\Longleftrightarrow\quad 0\le p<4
\qquad(p\ge0).}
\tag{DI16}
\]
For \(p\ge4\) the divergence follows from DI14, logarithmically at \(p=4\). For \(p<4\), the density controls the origin and the integrand is bounded away from it. In particular the diagonal susceptibility is finite, while the limiting cyclic spectral support has no positive lower endpoint.

## Fixed low-energy intervals and moving normalized filters

The complete chronological family generated by an influence is a source-selected reducing sector, not automatically the full physical algebra. In this specific return the limiting measure has strictly positive mass in every sufficiently small fixed interval \((0,\epsilon)\). The lower bound for open sets under weak convergence therefore forces
\(\liminf\nu_h((0,\epsilon))\ge\nu_\infty((0,\epsilon))>0\).
Since the actual sources are centered, this is nonvacuum spectral weight. Thus the actual visible lower spectral edge tends to zero along the bulk sequence. The [[chronological-cyclic-sources-and-the-innovation-floor|cyclic spectral calculation]] translates this qualitative fact to the infimum of the fixed-scaled-duration OI quotient.

What weak return does not supply is a quantitative estimate on a shrinking energy interval, such as one of width \(1/n\), or norm control for filters whose durations grow with the patch. [[conditional-influence-soft-band-and-chronological-filters|The actual soft-band construction]] supplies both for a central face: at least \(c_In^{-4}\) weight below \(20/n\), and an explicit filter time \(T_n=\tfrac34n\log n\) whose normalized OI quotient is of order \(1/n\). Conversely, for a limiting measure with a positive spectral edge, weak return could conceal an arbitrarily small amount of actual soft weight. A single original-source quotient must not replace the entire closed chronological family.

All durations above are scaled durations for \(K_h\). Physical duration is \(s/E\), with the unchanged \(E=\kappa h^{-2}\). Low scaled energy in the limiting measure does not by itself imply low physical energy along the strong-confinement trajectory. The result neither constructs a fixed-coupling thermodynamic theory nor decides the full four-dimensional physical gap.

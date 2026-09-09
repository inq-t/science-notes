# Compact Collar Memory Returns Uniformly over Retained Regions

The actual compact planar source retains its harmonic exterior-memory response uniformly over every set of retained faces containing the source, even when that set grows with the patch. The proof uses a fiberwise conditional-projection estimate whose constant is independent of the retained and eliminated dimensions. The normalized memory-to-innovation ratio returns uniformly away from zero scaled time. Its short-time denominator and its fixed-physical-time behavior remain distinct parts of the statement.

**Status: proved one-source collar-memory return on the confinement window.** [[fixed-regional-sources-and-the-compact-vacuum-return|FR]] supplies the actual normalized source and vacuum, [[compact-chronology-on-finite-hermite-sources|HC]] its evolved vector, and [[vacuum-hellinger-return-and-regional-conditional-projections|VH]] the conditional-projection estimate. [[regional-innovation-and-exterior-information-balance|RI]] fixes the exterior-memory and full-innovation comparison. All regions use the same inherited vacuum, comb connectors and clock.

## The retained set can grow without changing the source

Work on the open \(L\times L\) patch with full Gauss law, including every boundary vertex. Put
\[
n=L+1,\qquad h=(\kappa/g)^{1/4},\qquad
0<\epsilon=hn^{10}\le\eta,\qquad
\theta=hn^{11/2}.
\tag{CL1}
\]
Fix any face \(p\) of the patch. For its prescribed compact observable
\(B_h=4|\mathbf q_p|^2/h^2\), use the actual mean and variance to define the normalized source function \(f_h\). In FR's global principal chart let
\[
\Phi_h=\mathcal U_h\psi_h,\qquad
z_h=\Phi_hf_h,\qquad
\mathsf T_h(t)=\mathcal U_he^{-t\widehat K_h}\mathcal U_h^*,
\]
where \(\widehat K_h\) is the actual vacuum-subtracted scaled Hamiltonian. These are vectors and operators on the common Euclidean space, with the compact chart image zero extended as specified in FR16.

Write \(C_L=\sqrt{A_L}\), \(A_L=4I-\operatorname{Adj}_L\), and
\[
c_{p,L}=(C_L)_{pp},\qquad
f_0=\frac{|X_p|^2-3c_{p,L}}{\sqrt6\,c_{p,L}},\qquad
z_0=\Omega_Lf_0,\qquad u_0(t)=e^{-tK_0}z_0.
\tag{CL2}
\]
Both source vectors have norm one and are centered in their respective actual vacua.

For any face subset \(S\) containing \(p\), let \(\mathsf E_{h,S}\) project onto vectors \(\Phi_h a(X_S)\), and define \(\mathsf E_{0,S}\) similarly with \(\Omega_L\). The projections are those of the inherited probability densities. They commute with common color rotations, so their restrictions to invariant vectors return the physical regional observable algebras. No independent gauge quotient or product physical vacuum across the cut is imposed.

Define the exterior vectors and their memory responses by
\[
w_{h,S}(t)=(I-\mathsf E_{h,S})\mathsf T_h(t)z_h,\qquad
w_{0,S}(t)=(I-\mathsf E_{0,S})u_0(t),
\]
\[
M_{h,S}(t)=\|w_{h,S}(t)\|^2,\qquad
M_{0,S}(t)=\|w_{0,S}(t)\|^2.
\tag{CL3}
\]
By RI2 these are source values of the actual conditional-compression defect. The family of sets \(S\) is unrestricted: it may include disconnected sets, collars of varying width, or the entire patch.

## The conditional-projection constant does not count faces

VH's fiber argument applies to every split \(X=(X_S,X_{S^c})\). For normalized nonnegative amplitudes \(\Phi,\Omega\) and \(g\in L^4(\Omega^2dX)\),
\[
\|(\mathsf E_{\Phi,S}-\mathsf E_{\Omega,S})(\Omega g)\|
\le2\|g\|_{L^4(\Omega^2dX)}
       \|\Phi-\Omega\|^{1/2}.
\tag{CL4}
\]
Each fiber contains two amplitude lines; their projection-angle estimate has no dimension factor. Clipping \(g\) and integrating over the retained coordinates also introduces none. Zero fibers are included by the definition in VH1. Thus the same constant works for all \(S\), not merely for a fixed-size region.

FR16 and HC7 give
\[
\|\Phi_h-\Omega_L\|\le C\theta,\qquad
\sup_{t\ge0}\|\mathsf T_h(t)z_h-u_0(t)\|\le C\theta .
\tag{CL5}
\]
Write \(u_0(t)=\Omega_Lg_t\). The harmonic ground transform is Markov, hence
\(\|g_t\|_4\le\|f_0\|_4\). The latter is a universal constant: \(f_0\) is the centered, normalized square norm of three standard Gaussian components. Applying (CL4) to this full evolved function and then using (CL5) proves
\[
\boxed{
\sup_{S\ni p,\ t\ge0}
\|w_{h,S}(t)-w_{0,S}(t)\|
\le C\sqrt\theta,\qquad
\sup_{S\ni p,\ t\ge0}
|M_{h,S}(t)-M_{0,S}(t)|
\le C\sqrt\theta .}
\tag{CL6}
\]
The second bound uses \(\|w_{h,S}\|,\|w_{0,S}\|\le1\). Constants are independent of \(p,L,h,t,S\) on the sufficiently small fixed window.

This is a uniform comparison over retained sets for one prescribed normalized quadratic source. It is not convergence in operator norm on the full one-face \(L^2\) space: the \(L^4\) bound used in (CL4) is not uniform over its unit sphere.

## The full point-source innovation has a uniform denominator

Let
\[
G_h(t)=1-\langle z_h,\mathsf T_h(2t)z_h\rangle,\qquad
G_0(t)=1-r_L(2t),\qquad
r_L(s)=\left[\frac{k_L(s)}{c_{p,L}}\right]^2,
\]
\[
k_L(s)=(C_Le^{-sC_L})_{pp}.
\tag{CL7}
\]
Thus \(G_h(t)\) is the full-predictor innovation variance for duration \(t\), as in RI5. It is independent of the chosen retained set \(S\). It is not the variance obtained after replacing the full predictor by a regional one. [[compact-regional-covariance-and-susceptibility-return|RC5]] gives
\[
\sup_{t\ge0}|G_h(t)-G_0(t)|\le C\theta.
\tag{CL8}
\]

The one-face energy and Cauchy–Schwarz bounds give
\(\sqrt2\le c_{p,L}\le2\). Let \(\mu_{p,L}\) be the probability measure on harmonic frequencies for which
\[
\frac{k_L(s)}{c_{p,L}}=\int e^{-s\omega}\,d\mu_{p,L}(\omega).
\]
It is supported in \((0,\sqrt8)\), and
\[
\int\omega\,d\mu_{p,L}(\omega)
=\frac{(A_L)_{pp}}{c_{p,L}}=\frac4{c_{p,L}}\ge2.
\tag{CL9}
\]
Concavity gives
\(1-e^{-2t\omega}\ge
\omega(1-e^{-2t\sqrt8})/\sqrt8\).
Since \(1-a^2\ge1-a\) for \(0\le a\le1\), it follows that
\[
\boxed{
a_*\min\{t,1\}\le G_0(t)
\le8\sqrt2\min\{t,1\},\qquad
a_*=\frac2{\sqrt8}(1-e^{-2\sqrt8})>0.}
\tag{CL10}
\]
For the upper bound use \(1-a^2\le2(1-a)\),
\(1-e^{-2t\omega}\le2t\omega\), and \(c_{p,L}\ge\sqrt2\); also \(G_0\le1\). These estimates are independent of patch size and of the face's distance from the boundary.

## Normalize only where the error controls the denominator

There is an exact comparison, valid separately in the harmonic and actual compact laws:
\[
\boxed{0\le M_{h,S}(t)\le G_h(t),\qquad
0\le M_{0,S}(t)\le G_0(t).}
\tag{CL11}
\]
For proof in probability coordinates, \(f_h\) is regional whenever \(p\in S\). Therefore
\[
(I-E_S)P_tf_h=(I-E_S)(P_t-I)f_h.
\]
The squared norm is at most
\(\|(I-P_t)f_h\|^2\le
\langle f_h,(I-P_{2t})f_h\rangle\).
The last inequality follows from \((1-x)^2\le1-x^2\) on the spectrum \(0\le x\le1\). No collar approximation is used.

For \(t>0\), define the normalized memory fraction
\(\mathfrak m_{h,S}(t)=M_{h,S}(t)/G_h(t)\), and likewise \(\mathfrak m_{0,S}\). Whenever the covariance error satisfies
\(C\theta\le(a_*/2)\min\{t,1\}\), (CL8)–(CL11) give
\[
\boxed{
\sup_{S\ni p}
|\mathfrak m_{h,S}(t)-\mathfrak m_{0,S}(t)|
\le C\frac{\sqrt\theta}{\min\{t,1\}}.}
\tag{CL12}
\]
Indeed subtraction of the fractions costs
\[
\frac{|M_{h,S}-M_{0,S}|}{G_h}
+\frac{M_{0,S}}{G_0}\frac{|G_h-G_0|}{G_h},
\]
and the second numerator ratio is at most one. In particular, for every fixed \(t_0>0\), sufficiently small \(\theta\) gives
\[
\sup_{S\ni p,\ t\ge t_0}
|\mathfrak m_{h,S}(t)-\mathfrak m_{0,S}(t)|
\le C_{t_0}\sqrt\theta.
\tag{CL13}
\]
Neither the onset condition nor \(C_{t_0}\) depends on the collar size.

The same estimates (CL12)–(CL13) hold for the exterior fraction in the full OI surplus,
\[
\frac{M_{h,S}(2t)}{G_h(t)}
\quad\text{compared with}\quad
\frac{M_{0,S}(2t)}{G_0(t)}.
\]
Its numerator uses twice the duration. RI7 gives the required exact bound
\(M_{h,S}(2t)\le\langle f_h,(I-P_{2t})^2f_h\rangle\le G_h(t)\),
and likewise harmonically; (CL6) is already uniform in its time argument.

At \(t=0\) both memory and innovation vanish. The constant absolute error in (CL6) cannot be divided by that zero. For a varying \(t_L\downarrow0\), the sufficient condition supplied here for relative convergence is
\(\sqrt{\theta_L}/t_L\to0\). The proof gives no uniform relative return at all arbitrarily short scaled times.

At each fixed finite regulator the source is smooth and lies in the generator domain. Then
\[
M_{h,S}(t)
=t^2\|(I-E_S)H_hf_h\|^2+o(t^2),\qquad
G_h(t)=2t\langle f_h,H_hf_h\rangle+o(t),
\tag{CL14}
\]
where \(H_h\) is the actual ground-transformed scaled generator. This explains the vanishing relative memory at that fixed regulator. Bounds on these differentiated quantities uniform in \(L,h\) would be an additional result; they are not inferred from the absolute return.

## Fixed physical time uses a different part of the same law

Let \(\widehat\Delta_{L,h}\) be the complete actual scaled gap. Centering and spectral calculus give, at every finite regulator,
\[
M_{h,S}(t)\le e^{-2t\widehat\Delta_{L,h}},\qquad
G_h(t)\ge1-e^{-2t\widehat\Delta_{L,h}},
\]
\[
\boxed{
\mathfrak m_{h,S}(t)
\le\min\left\{1,\frac1{e^{2t\widehat\Delta_{L,h}}-1}\right\},
\qquad t>0.}
\tag{CL15}
\]
This is a separate exact use of the full compact gap, uniform over \(S\).

For fixed positive physical duration \(\ell\), the scaled time is
\(t=\ell\sqrt{\kappa g}\), and
\(t\widehat\Delta_{L,h}=\ell\Delta_L(g)\).
[[uniform-nonlinear-planar-gap-and-marked-response|UN]] proves
\(\Delta_L(g)\sim2\sqrt2\pi\kappa n^{19}/\epsilon_L^2\to\infty\)
on every growing-patch sequence \(0<\epsilon_L\le\eta\). Hence (CL15) forces the memory fraction to zero at fixed physical duration, uniformly over all retained sets containing the source. This rapidly confining trajectory differs from the fixed scaled-duration regional-memory comparison.

The collar return preserves RI's positive exterior-information term and nested-region identities. It does not identify that term with SB's changed-history lag cost, establish a bound for every regional observable, or provide a fixed-coupling or four-dimensional Yang–Mills limit.

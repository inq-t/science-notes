# Centered Compact Chronology Gives an Integrable Source Return

Centering the cutoff embedding in the actual vacuum makes both sides of Duhamel's formula decay. The resulting chronological error is integrable over all scaled times, uniformly on the weighted planar confinement window. For a bounded-norm local influence vector paired with an extensive character insertion of norm \(O(L+1)\), the source and evolution errors have time integral \(O(h(L+1)^{15/2})\). An independently controlled harmonic tail then gives a uniform actual tail, without replacing the original Hamiltonian by conditional-update dynamics.

**Status: proved centered finite-degree semigroup comparison and source-return criterion.** [[compact-chronology-on-finite-hermite-sources|HC]] supplies the uncentered cutoff comparison. [[uniform-weighted-character-return-and-the-soft-gap|UW]] verifies its operator inputs for the fixed three-block character family. The additional source-vector hypotheses below are stated explicitly; a scalar integrated coefficient alone does not supply them.

## Keep the weighted Hamiltonian and actual vacuum

Fix a compact preparation interval \(I\subset(-1/14,1/16)\), the full Gauss carrier on an open \(L\times L\) patch, and
\[
n=L+1,\qquad h=(\kappa/(15g))^{1/4},\qquad
\delta=hn^{10},\qquad\theta=hn^{11/2},\qquad
\tau=hn^{3/2},\qquad 0<\delta\le\eta_I.
\]
The exact physical scale is \(E=\kappa h^{-2}\), independent of the preparation parameter \(\varepsilon\in I\). Write
\[
H=\widehat H_{\varepsilon,L,h},\qquad
K=H-\lambda_{\varepsilon,L,h},\qquad
K_0=\mathcal O_L-e_0(L),
\]
\[
Q=1-|v_{\varepsilon,L,h}\rangle\langle v_{\varepsilon,L,h}|,\qquad
Q_0=1-|\Omega_L\rangle\langle\Omega_L|.
\tag{CC1}
\]
Here \(v\) is the actual normalized vacuum, while \(\Omega_L\) is the oscillator vacuum. The extensive vacuum energies \(\lambda\) and \(e_0\) are retained before subtraction. UW and [[planar-physical-cluster-separation-and-the-uniform-window|PS]] give
\[
\boxed{
|\lambda-e_0|\le C_Ih^2n^{10},\qquad
K|_{\operatorname{ran}Q}\ge\gamma_h,\qquad
K_0|_{\operatorname{ran}Q_0}\ge\gamma_0,\qquad
\gamma_h,\gamma_0\ge c_I/n.}
\tag{CC2}
\]
For example one may use the exact harmonic gap
\(\gamma_0=4\sqrt2\sin(\pi/(2n))\ge8/n\).
The vacuum-shift estimate follows from UW's finite branch expansion and parity, as in HC2; it does not bound the extensive \(e_0\) by a small number.

Let \(P_{m,L}\) be the physical oscillator projector onto total Hermite degree at most a fixed \(m\). Let \(\mathcal J\) be [[compact-cutoffs-and-uniform-polynomial-quasimodes|CQ's]] exact Haar-density transform and magnetic cutoff. It is a contraction, independent of \(\varepsilon\). Define the centered embedding
\[
\boxed{\mathcal I=Q\mathcal JQ_0.}
\tag{CC3}
\]
Its image is exactly orthogonal to the actual vacuum. This changes the comparison map, not the Hamiltonian or the prepared observable.

## The weighted generator defect has the same spatial bound

UW proves that the weighted potential has the same quadratic term, no first magnetic jet and uniform higher local Taylor bounds. The electric rows, Haar density and CQ cutoff are unchanged. Thus HC's actual norm argument, using the first-order operator truncation, gives
\[
\begin{aligned}
\|(K\mathcal J-\mathcal JK_0)P_{m,L}\|
&\le C_{I,m}\bigl(
hn^{9/2}+h^2n^{10}+h^2n^7+h^3n^5
\bigr)\\
&\le \alpha,\qquad
\alpha=C_{I,m}hn^{9/2}.
\end{aligned}
\tag{CC4}
\]
The four terms are the first electric jet, actual vacuum shift, interior operator remainder and cutoff commutator. The last uses CQ's tail order one. Each is controlled on the stated window. This extension uses UW's verified weighted operator bounds, not merely equality of the quadratic Hessian.

Since \(KQ=QK=K\) and \(K_0Q_0=K_0\),
\[
\boxed{
(K\mathcal I-\mathcal IK_0)P_{m,L}Q_0
=Q(K\mathcal J-\mathcal JK_0)P_{m,L}Q_0,\qquad
\|(K\mathcal I-\mathcal IK_0)P_{m,L}Q_0\|\le\alpha.}
\tag{CC5}
\]
The defect itself has image in \(\operatorname{ran}Q\). This is the additional fact that permits decay on the left of the Duhamel integral.

## Both sides of the Duhamel integral decay

For \(u\in\operatorname{ran}(P_{m,L}Q_0)\),
\[
e^{-tK}\mathcal Iu-\mathcal Ie^{-tK_0}u
=-\int_0^t e^{-(t-s)K}
(K\mathcal I-\mathcal IK_0)e^{-sK_0}u\,ds .
\]
The oscillator evolution preserves its finite degree. The cutoff vectors and the subtracted actual vacuum lie in the compact operator domain, so this identity follows by differentiation in its graph norm at each fixed regulator. Equations CC2 and CC5 yield
\[
\boxed{
\|e^{-tK}\mathcal Iu-\mathcal Ie^{-tK_0}u\|
\le\alpha\,d(t)\|u\|,\qquad
d(t)=\int_0^t e^{-\gamma_h(t-s)}e^{-\gamma_0s}\,ds
\le t e^{-c_It/n}.}
\tag{CC6}
\]
In particular,
\[
\boxed{
\sup_{t\ge0}\alpha d(t)\le C_{I,m}hn^{11/2},\qquad
\int_0^\infty\alpha d(t)\,dt
=\frac{\alpha}{\gamma_h\gamma_0}
\le C_{I,m}hn^{13/2}.}
\tag{CC7}
\]
The exact integral follows by Fubini. An actual vacuum component in \(\mathcal Ju\) would prevent this argument; CC3 removes it explicitly.

## Retain the centered embedding's Gram error

The weighted vacuum return gives \(\|v-\mathcal J\Omega_L\|\le C_I\theta\). This follows directly from any fixed-order UW quasimode, whose first vector correction is \(O(\theta)\). CQ's finite-degree tail estimate gives
\[
|\langle\mathcal Ju,\mathcal Jw\rangle-\langle u,w\rangle|
\le C_m\tau^4\|u\|\|w\|.
\]
For centered \(u\), it also gives
\[
|\langle v,\mathcal Ju\rangle|
\le\|v-\mathcal J\Omega_L\|\|u\|
+|\langle\mathcal J\Omega_L,\mathcal Ju\rangle|
\le C_{I,m}\theta\|u\|.
\]
The second inner product is purely a cutoff error, since
\(\langle\Omega_L,u\rangle=0\).
Subtracting the product of these actual vacuum overlaps therefore proves
\[
\boxed{
|\langle\mathcal Iu,\mathcal Iw\rangle-\langle u,w\rangle|
\le\beta\|u\|\|w\|,\qquad
\beta=C_{I,m}(\tau^4+\theta^2),}
\tag{CC8}
\]
for centered vectors of degree at most \(m\). No isometry of the complete compact and oscillator carriers is asserted.

## A mixed source criterion with an integrable error

Let centered harmonic physical vectors \(u,w\) have degree at most \(m\), and let centered actual vectors \(f,g\) satisfy
\[
\|u\|\le A,\qquad \|w\|\le B,\qquad
\|f-\mathcal Iu\|\le e_f,\qquad
\|g-\mathcal Iw\|\le e_g.
\]
Put \(E_{\rm src}=e_f(B+e_g)+Ae_g\).
Subtract the two source errors first, use CC6 for evolution, and then use CC8 with \(e^{-tK_0}w\). Every source difference is in the actual vacuum complement. Hence
\[
\boxed{\begin{aligned}
&|\langle f,e^{-tK}g\rangle-\langle u,e^{-tK_0}w\rangle|\\
&\quad\le E_{\rm src}e^{-\gamma_ht}
+AB\{\alpha d(t)+\beta e^{-\gamma_0t}\},\\
&\int_0^\infty
|\langle f,e^{-tK}g\rangle-\langle u,e^{-tK_0}w\rangle|\,dt\\
&\quad\le \frac{E_{\rm src}}{\gamma_h}
+AB\left\{\frac{\alpha}{\gamma_h\gamma_0}
+\frac{\beta}{\gamma_0}\right\}.
\end{aligned}}
\tag{CC9}
\]
This estimate permits signed mixed kernels and sources spread over the whole patch. Neither their positivity nor invariance of a finite source span under \(K\) is assumed.

For the local-influence/global-character application, the sufficient source hypotheses are
\[
\boxed{
A\le C_I,\qquad B\le C_In,\qquad
e_f\le C_I\theta,\qquad e_g\le C_In\theta.}
\tag{CC10}
\]
They concern actual source vectors, including their changing vacuum and centering; they must be proved independently. With CC10, CC9 becomes
\[
\boxed{\begin{aligned}
|G_h(t)-G_0(t)|
&\le C_Ihn^{13/2}(1+t/n)e^{-c_It/n},\\
\int_0^\infty|G_h(t)-G_0(t)|\,dt
&\le C_Ihn^{15/2}
=C_I\delta n^{-5/2},
\end{aligned}}
\tag{CC11}
\]
where \(G_h(t)=\langle f,e^{-tK}g\rangle\) and
\(G_0(t)=\langle u,e^{-tK_0}w\rangle\).
Indeed \(E_{\rm src}=O(n\theta)\), while the Gram contribution
\(n\beta\) is smaller by another factor \(O(\theta)\).

[[magnetic-character-insertion-and-centered-source-control|MI4]] proves the \(O(n)\) norm of the centered harmonic character insertion, while [[conditional-influence-vectors-and-the-original-source-carrier|IV3]] gives the harmonic influence norm \(\sqrt{120}\,\sigma_{L,r}^2=O(1)\). Those harmonic checks do not replace the actual-vector comparisons in CC10.

## A uniform actual tail follows from the source criterion

Integrating the first line of CC11 from \(T\) onward gives
\[
\int_T^\infty|G_h(t)-G_0(t)|\,dt
\le C_I\delta n^{-5/2}(1+T/n)e^{-c_IT/n}.
\]
For \(T\ge1\), set \(z=T/n\). The function
\(z^{5/2}(1+z)e^{-c_Iz}\) is bounded, so the supremum over patch sizes is at most \(C_I\eta_I T^{-5/2}\). If the harmonic pair has CI's uniform tail, this proves
\[
\boxed{
\int_T^\infty|G_h(t)|\,dt
\le C_I(1+T)^{-5}+C_I\eta_I(1+T)^{-5/2},\qquad T\ge0,}
\tag{CC12}
\]
uniformly for source families satisfying CC10. The actual error in CC11 tends to zero in \(L^1(dt)\) as the patch grows throughout the confinement window. Thus the integrated comparison does not require a guessed cutoff time or integration of a nondecaying error.

All times here are the scaled times of the original \(K\); physical duration is \(t/E\). The construction introduces no replacement generator, regional reset or new clock. Its finite-degree and source-vector hypotheses do not supply a complete-source OI bound, a fixed-coupling thermodynamic limit or a four-dimensional physical return.

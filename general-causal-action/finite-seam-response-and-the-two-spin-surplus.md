# Finite Seam Response and the Two-Spin Surplus

A nonnegative spatial seam can increase or decrease the normalized chronological innovation surplus, even when the kinetic transfer is fixed and the moving vacuum is retained exactly. In a two-spin instance of the existing seam sandwich, two source directions have opposite first derivatives. A fixed regional source has zero first derivative and a second derivative that changes sign with the declared kinetic parameter. These are controls against automatic monotonicity of positive sewing, not counterexamples to the non-Abelian Wilson surplus conjecture.

**Status: exact finite positive chronology and source calculation.** The deformation is precisely [[seam-coupling-response-and-the-vacuum-cap|SV1]], starting from its allowed product control. [[spatial-block-sewing-and-the-vacuum-cap-response|SB16]] already uses the two-spin kinetic carrier to distinguish bounded seam action from uniform vacuum control. No gauge factorization of a Wilson region is assumed here.

## Fix the kinetic transfer and add one nonnegative seam

Let \(x=(x_L,x_R)\in\{-1,1\}^2\), with uniform reference measure \(\mu_0\), and fix \(0<p<1\). The one-spin and product transfers are
\[
K_p(x,y)=\frac{1+p\,xy}{2},\qquad
T_0=K_p\otimes K_p.
\tag{SF1}
\]
They act by summing the displayed transition probabilities. Equivalently, at a declared duration \(a_t>0\),
\[
K_p=e^{-a_t\epsilon(I-X)},\qquad p=e^{-2a_t\epsilon},
\]
where \(X\) flips the spin. This is the uncoupled kinetic member of the two-spin control; \(\epsilon\) and \(a_t\) remain fixed during the seam deformation.

Choose the bounded nonnegative interaction
\[
V(x)=1-x_Lx_R\in\{0,2\},\qquad
T_s=e^{-sV/2}T_0e^{-sV/2},\qquad s\ge0.
\tag{SF2}
\]
The formulas also extend to real \(s\) near zero. Every finite \(s\) gives a strictly positive matrix and a positive-definite operator. Let
\[
T_s\psi_s=\lambda_s\psi_s,\qquad
\int\psi_s^2d\mu_0=1,\qquad
d\pi_s=\psi_s^2d\mu_0,\qquad
P_sf=\frac{T_s(\psi_sf)}{\lambda_s\psi_s}.
\tag{SF3}
\]
Thus the state and clock are the actual Perron return of the same seam sandwich. All source comparisons below use \(\pi_s\) and \(P_s\).

Put
\[
c=\frac{1+p^2}{2},\qquad d=\frac{1-p^2}{2},\qquad
B(s)=\sqrt{d^2+c^2\sinh^2s},
\]
\[
\Lambda(s)=c\cosh s+B(s),\qquad
t(s)=\frac{c\sinh s}{B(s)}.
\tag{SF4}
\]
On the two-dimensional subspace even under simultaneous spin flip, \(e^sT_s\) has matrix
\[
\begin{pmatrix}ce^s&d\\d&ce^{-s}\end{pmatrix}
\]
in the normalized aligned and antialigned indicators. Its eigenvalues are \(\Lambda(s)\) and \(p^2/\Lambda(s)\). The two odd eigenvalues of \(e^sT_s\) are \(pe^s\) and \(pe^{-s}\). In particular,
\[
\boxed{
\lambda_s=e^{-s}\Lambda(s),\qquad
\psi_s(x)^2=1+t(s)x_Lx_R,\qquad
\pi_s(x_Lx_R)=t(s).}
\tag{SF5}
\]
Here \(|t(s)|<1\), so the vacuum is faithful. The identity
\[
\partial_s\log\Lambda(s)=t(s)
\]
also gives \(\partial_s\log\lambda_s=-1+t(s)=-\pi_sV\), as required by SV3.

## Compare the actual normalized innovations

For a fixed real source \(F\), let \(f_s=F-\pi_sF\), \(A_s=P_s^k\), and \(R_s=I-A_s^2\), with a fixed integer \(k\ge1\). The normalized OI surplus is
\[
\mathscr S_F(s;k)
=\frac{\langle f_s,R_s^2f_s\rangle_{\pi_s}}
       {\langle f_s,R_sf_s\rangle_{\pi_s}}
=\frac{\|h_s\|^2-\|\mathcal K_{\parallel,s}h_s\|^2}
       {\|h_s\|^2},
\qquad h_s=\delta_s f_s.
\tag{SF6}
\]
The last equality is [[oriented-innovation-and-finite-temporal-repair|OI25]], using its actual changed pair law. It includes \(A_sf_s\), the vacuum centering and the normalization of the innovation. Rescaling \(f_s\) or \(h_s\) does not change this ratio.

The fixed functions \(F_+=x_L+x_R\) and \(F_-=x_L-x_R\) are centered for every \(s\). Multiplication by \(\psi_s\) leaves each in its one-dimensional odd eigenspace, so
\[
P_sF_\pm=\theta_\pm(s)F_\pm,\qquad
\theta_\pm(s)=\frac{pe^{\pm s}}{\Lambda(s)}.
\]
Consequently
\[
\boxed{
\mathscr S_{F_\pm}(s;k)=1-\theta_\pm(s)^{2k},\qquad
\partial_s\mathscr S_{F_\pm}
=-2k\,\theta_\pm^{2k}(\pm1-t(s)).}
\tag{SF7}
\]
The plus-source derivative is strictly negative and the minus-source derivative strictly positive at every finite \(s\). At zero they equal \(-2kp^{2k}\) and \(+2kp^{2k}\), respectively. The two signs occur for the same transfer and the same positive direction of seam coupling.

The underlying closed-normalization susceptibility nevertheless stays positive:
\[
\partial_s^2\log\lambda_s=t'(s)
=\frac{cd^2\cosh s}{B(s)^3}>0.
\tag{SF8}
\]
By SV15, this is the squared norm of the seam's own transition score. Its positivity does not force a sign for the change of another source's normalized surplus.

## A fixed regional source has a sign-changing first nonzero response

Take the genuinely regional function \(F(x)=x_L\). Simultaneous spin-flip symmetry gives
\[
\pi_sF=0,\qquad \|F\|_{L^2(\pi_s)}=1
\]
for every \(s\). No moving mean or source norm has been suppressed. Define its exact chronological correlation
\[
M_n(s)=\langle F,P_s^nF\rangle_{\pi_s}.
\]
Its weights in the two odd eigenspaces are \((1+t(s))/2\) and \((1-t(s))/2\). Therefore
\[
\boxed{
M_n(s)=\frac{p^n}{\Lambda(s)^n}
\left[\cosh(ns)+t(s)\sinh(ns)\right].}
\tag{SF9}
\]
Both the transported source and its moving vacuum weights appear here.

Let
\[
\gamma=\frac{1+p^2}{1-p^2}.
\]
Then \(\Lambda(0)=1\), \(t(0)=0\), \(t'(0)=\gamma\), and
\[
(\log\Lambda)''(0)=\gamma,\qquad
M_n'(0)=0,\qquad
M_n''(0)=p^n n(n+\gamma).
\tag{SF10}
\]
Indeed, \(t\) is odd and \(\Lambda\) even. The coefficient of \(s^2\) in the bracket of (SF9) is \(n^2/2+n\gamma\), while the exponential factor contributes \(-n\gamma/2\).

Put \(a=2k\) and \(r_k=p^{2k}\). The full normalized ratio is
\[
\mathscr S_F(s;k)
=\frac{1-2M_a(s)+M_{2a}(s)}{1-M_a(s)}.
\]
Its first derivative vanishes at zero. Applying (SF10) to both numerator and denominator yields
\[
\boxed{
\mathscr S_F''(0;k)
=a r_k\left[
\frac{a(3r_k-1)}{1-r_k}-\gamma
\right].}
\tag{SF11}
\]
For example, the unsimplified numerator after quotient differentiation is
\[
-(1+r_k)r_k a(a+\gamma)
+r_k^2(2a)(2a+\gamma),
\]
divided by \(1-r_k\). This checks the contribution of the changing innovation normalization.

For one slab, \(k=1\) and \(r=p^2\), the formula reduces to
\[
\boxed{
\mathscr S_F'(0;1)=0,\qquad
\mathscr S_F''(0;1)=\frac{2r(5r-3)}{1-r}.}
\tag{SF12}
\]
It is negative for \(0<r<3/5\) and positive for \(3/5<r<1\). For instance, the exact values at \(r=1/4\) and \(r=3/4\) are \(-7/6\) and \(9/2\). The function is even and analytic near zero, so these signs determine its first nonzero change for small positive seam coupling. The kinetic parameter is fixed within each deformation; the two values compare two allowed kinetic inputs.

The three centered transition eigenvalues are \(\theta_+\), \(\theta_-\) and \(\theta_+\theta_-\). For \(s\ge0\), the largest is \(\theta_+\), so the infimum of (SF6) over all nonzero centered sources is \(1-\theta_+^{2k}\). It decreases even when the fixed regional source initially improves. A positive response in one source therefore does not estimate the change of the full-source floor.

## The scope of the discriminator

Positive temporal sewing, a nonnegative bounded seam and a strictly positive moving vacuum do not imply monotone improvement of the normalized innovation surplus. This fails both on two source directions of one fixed family and on the first nonzero regional-source response across allowed product controls. The failure is a statement about monotonicity: every finite member here still has a positive chronological gap.

These spins are the declared physical variables of the finite control. No neutral Yang–Mills source identification or factorization of an interacting gauge cut is asserted. [[adjacent-wilson-plaquette-and-the-chronological-surplus|The actual adjacent Wilson plaquette]] now gives a separate physical gauge calculation: a fixed source can improve while the full finite gap decreases. A non-Abelian global estimate must therefore absorb negative seam terms rather than infer their positivity from the group alone. The complete moving-vacuum, transported-source and normalization terms remain essential.

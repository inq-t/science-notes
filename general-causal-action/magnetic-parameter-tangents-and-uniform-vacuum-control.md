# Magnetic Parameter Tangents Have Uniform Vacuum Control

Varying the prepared character changes only the magnetic multiplication terms. This improves the spatial bound on every fixed formal vacuum tangent by eight powers of the patch width. An exact differentiated-residual identity then compares the actual normalized vacuum derivative with the differentiated compact quasimode, including the moving eigenprojection. At order eighteen the error remains small after the fourth-product cost of the original bounded face mark.

**Status: proved uniform vacuum and parameter-tangent estimates for UW's fixed family.** Use the representation, positive weight interval and actual compact Hamiltonian of [[uniform-weighted-character-return-and-the-soft-gap|UW]]. The argument concerns its isolated planar confinement window; it neither changes the preparation nor supplies a conditional-product theorem without a separate stability estimate.

## Differentiate the finite normalized recursion

Fix a compact interval \(I\subset(-1/14,1/16)\), put \(n=L+1\), and retain
\[
h=(\kappa/(15g))^{1/4},\qquad
\delta=hn^{10},\qquad \theta=hn^{11/2}.
\]
The parameter \(\varepsilon\in I\) changes the weight \(A_\varepsilon\), while \(h\), the electric operator, the Haar transform and the cutoff stay fixed. A prime denotes this parameter derivative. For each fixed order \(M\ge2\), work on \(0<\delta\le\eta_{I,M}\); the window may be reduced by a constant depending on the chosen order, independently of \(L\).

Let \(\psi_r,e_r\) be the real formally normalized coefficients of [[comb-chart-ellipticity-and-uniform-local-comparison|UC20]], for the harmonic vacuum seed \(\psi_0=\Omega_L\). UW proves
\[
\begin{gathered}
\|\psi_r\|\le C_{I,r}n^{11r/2},\qquad
|e_r|\le C_{I,r}n^{11r/2-1},\\
V'_0=V'_1=0,\qquad
\|V'_rP_{\le m,L}\|\le C_{I,m,r}n^2\quad(r\ge2),\\
|e'_r|\le C_{I,r}n^{11r/2-9}\quad(r\ge2).
\end{gathered}
\tag{MVT1}
\]
The last line follows from coefficientwise normalized Feynman–Hellmann. The harmonic inverse is independent of \(\varepsilon\) and has norm at most \(Cn\) on the physical vacuum complement.

Differentiating the actual finite recursion gives
\[
\boxed{\psi'_0=\psi'_1=0,\qquad
\|\psi'_r\|\le C_{I,r}n^{11r/2-8}\quad(r\ge2).}
\tag{MVT2}
\]
Here is the induction. An insertion \(V'_j\psi_{r-j}\), \(j\ge2\), followed by the inverse costs
\(n^{3+11(r-j)/2}\le n^{11r/2-8}\).
An unchanged insertion \(V_j\psi'_{r-j}\) costs, after that inverse,
\(n^{11r/2-4j-4}\le n^{11r/2-8}\).
The terms \(e'_j\psi_{r-j}\) and \(e_j\psi'_{r-j}\) have the same final envelope by MVT1. Differentiating the norm-fixing coefficient gives products with exponent \(11r/2-8\). These are finite coefficient identities; no derivative of an unspecified remainder is used. Every differentiated vector retains degree at most \(3r\).

Let \(\mathcal J_{L,h}\) be [[compact-cutoffs-and-uniform-polynomial-quasimodes|CQ's]] parameter-independent cutoff and inverse density transform. Define
\[
U_M=\sum_{r=0}^M h^r\psi_r,\qquad
q_M=\frac{\mathcal J_{L,h}U_M}{\|\mathcal J_{L,h}U_M\|},
\qquad z_M=e_0+\sum_{r=1}^M h^re_r.
\]
Its normalization denominator is bounded below. Since
\(\sum_{r=2}^M h^rn^{11r/2-8}\le C_Mh^2n^3\), direct differentiation of this quotient and MVT1 give
\[
\boxed{\|q'_M\|\le C_{I,M}h^2n^3,\qquad
|z'_M|\le C_{I,M}h^2n^2.}
\tag{MVT3}
\]

## Compare with the actual moving eigenline

Write \(H=\widehat H_{\varepsilon,L,h}\) and
\[
r_M=(H-z_M)q_M,\qquad
\rho_M=C_{I,M}h^{M+1}n^{11(M+1)/2-1}.
\]
UW's differentiated compact construction gives
\[
\boxed{\|r_M\|+\|r'_M\|\le C_{I,M}\rho_M.}
\tag{MVT4}
\]
This is the conservative derivative envelope, sufficient below. Its justification is explicit: differentiate the finite operator products and coefficient recursion; differentiate the magnetic Taylor remainder; and keep the same parameter-independent cutoff and density transform. CQ's tail bounds apply to each resulting finite-degree vector. The differentiated normalization denominator is controlled by MVT3. Thus MVT4 does not follow merely by differentiating the inequality for \(\|r_M\|\).

Let \(v_\varepsilon\) be the positive real normalized actual vacuum, with energy \(\lambda_\varepsilon\), and let
\[
P=|v_\varepsilon\rangle\langle v_\varepsilon|,\qquad
R=(H-\lambda_\varepsilon)^{-1}(1-P).
\]
UW's physical isolation and the quasimode identification yield
\[
\boxed{\|R\|\le C_In,\qquad
\|v_\varepsilon-q_M\|\le C_{I,M}n\rho_M,\qquad
|\lambda_\varepsilon-z_M|\le C_{I,M}\rho_M.}
\tag{MVT5}
\]
The sign of \(q_M\) is chosen by positive overlap. The multiplication perturbation \(H'\) is bounded on the compact carrier, with
\(\|H'\|\le C_Ih^{-2}n^2\). The common operator domain and isolated simple eigenvalue therefore give differentiable eigenvectors; equivalently this follows by differentiating the resolvent identity on a contour enclosing that eigenvalue.

Suppress the subscript \(M\) in the following exact identity. Real normalization gives
\(\langle v,v'\rangle=\langle q,q'\rangle=0\), and differentiating the eigen-equation gives \(v'=-RH'v\). Applying \(R\) to the differentiated residual gives
\[
\boxed{
v'-q'
=-RH'(v-q)-Rr'-z'Rq-(z-\lambda)Rq'-Pq'.}
\tag{MVT6}
\]
Indeed \(R(H-z)=(1-P)+(\lambda-z)R\). This retains the moving spectral line; it does not replace the actual reduced inverse by the harmonic inverse.

In particular
\[
\|Rq\|\le Cn\|q-v\|,\qquad
\|Pq'\|\le\|v-q\|\,\|q'\|,
\]
where the second bound uses the exact normalization of \(q\). Combining MVT3–6 proves
\[
\boxed{\|v'_\varepsilon-q'_M\|
\le C_{I,M}h^{-2}n^4\rho_M.}
\tag{MVT7}
\]
The largest term is \(RH'(v-q)\), bounded by
\(Cn(h^{-2}n^2)(n\rho_M)\).
The other terms cost at most \(Cn\rho_M\), \(Ch^2n^4\rho_M\) and \(Ch^2n^5\rho_M\), all below this envelope on the stated window.

## Density tangents and the fourth-product budget

Use the same compact Haar reference measure for both amplitudes and put
\(p_\varepsilon=v_\varepsilon^2\), \(p_{M,\varepsilon}=q_M^2\).
The quasimode amplitude need not be pointwise positive; its square is a normalized density. Cauchy–Schwarz gives
\[
\boxed{
\|p_\varepsilon-p_{M,\varepsilon}\|_1\le C_{I,M}n\rho_M,\qquad
\|p'_\varepsilon-p'_{M,\varepsilon}\|_1
\le C_{I,M}h^{-2}n^4\rho_M.}
\tag{MVT8}
\]
For the second estimate, use
\[
p'-p'_M=2v(v'-q'_M)+2(v-q_M)q'_M
\]
and MVT3, MVT5 and MVT7. Consequently
\[
\boxed{\|(p_{\varepsilon_2}-p_{\varepsilon_1})
-(p_{M,\varepsilon_2}-p_{M,\varepsilon_1})\|_1
\le C_{I,M}|\varepsilon_2-\varepsilon_1|
h^{-2}n^4\rho_M.}
\tag{MVT9}
\]
This is a signed density-increment estimate, not by itself a derivative theorem for nonlinear conditional integration.

For the original scaled mark \(2q_\rho(P_r)/h\), boundedness of \(q_\rho\) gives a fourth-product cost \(Ch^{-4}\). At the fixed choice \(M=18\),
\[
\rho_{18}=C_Ih^{19}n^{207/2},\qquad
\boxed{h^{-4}\,h^{-2}n^4\rho_{18}
=C_Ih^{13}n^{215/2}.}
\tag{MVT10}
\]
Compared with an \(h^3n^{17/2}\) conditional-expansion error, this budget has ratio
\[
\boxed{\frac{h^{13}n^{215/2}}{h^3n^{17/2}}
=h^{10}n^{99}=\frac{\delta^{10}}n.}
\tag{MVT11}
\]
[[conditional-replica-cumulants-and-amplitude-stability|The conditional replica estimate]] proves the needed \(C^{1,1}\) amplitude stability for the integrated conditional fourth cumulant: its derivative norm on the unit ball and its global derivative Lipschitz constant are at most \(Ch^{-4}\). For the normalized amplitudes here, the chain rule bounds the difference of its parameter derivatives by
\(Ch^{-4}\{\|v'-q'_M\|+\|v-q_M\|\|q'_M\|\}\).
MVT7 therefore gives the actual-to-quasimode derivative budget in MVT10, with both changing conditional marginals retained. Evaluating the quasimode statistic and its local Taylor remainder is a separate step. No inverse conditional-density estimate or Gaussian reset is inserted.

All constants refer to a fixed finite order, the stated preparation interval and the isolated planar carrier. There is no convergence claim for the infinite formal series, nor a fixed-coupling thermodynamic or four-dimensional physical return.

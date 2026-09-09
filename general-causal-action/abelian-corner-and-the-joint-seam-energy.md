# An Abelian Corner Has a Nonzero Joint Seam Energy

On the same nine-edge corner as the three-face test, an explicitly calibrated \(U(1)\) transfer has a strictly negative connected fourth-order excitation-energy response for every heat-kernel parameter. The two seams commute as multiplication operators, but their shared raw edge couples the charge costs. Duplicating that edge removes the connected energy response exactly. A nonzero corner coefficient therefore detects shared incidence already in an Abelian theory; its value or sign alone does not establish a non-Abelian mechanism.

**Status: exact finite-graph coefficient for a declared Abelian heat transfer; controlled small-\(t\) fixed-source expansion.** [[three-face-corner-and-joint-seam-response|CJ]] fixes the original graph and its complete Gauss reduction. The fundamental multiplier and temporal duration below match its \(SU(2)\) comparison. Higher-charge heat multipliers are additional declared data, distinct from the \(SU(2)\) Wilson multipliers. No physical-limit gap follows from this calibration.

## The retained central flux selects a complete sector

Keep the based words \(U=apb^{-1}\), \(V=aqc^{-1}\), \(W=brc^{-1}\), with the three axis links of length one and each exterior path of length two. The Abelian physical carrier is \(L^2(U(1)^3)\). Its orthonormal charge basis is
\[
e_{n,\ell,m}=U^nV^\ell W^m,\qquad n,\ell,m\in\mathbb Z.
\tag{AC1}
\]
The signed raw-link charges are \(n+\ell,-n+m,-\ell-m\) on \(a,b,c\), and \(n,\ell,m\) on the two links of \(p,q,r\), respectively. Thus all raw-vertex Gauss constraints are retained.

Fix \(0<t<1\) and \(a_t>0\). On each original raw link choose the normalized \(U(1)\) heat kernel with multiplier \(\tau_r=t^{r^2}\). Set \(t\) equal to the \(SU(2)\) fundamental Wilson multiplier when making the comparison. The resulting free transfer \(D\) is diagonal:
\[
\boxed{
D e_{n,\ell,m}=\theta_{n,\ell,m}e_{n,\ell,m},\qquad
\theta_{n,\ell,m}
=t^{4n^2+4\ell^2+4m^2+2n\ell-2nm+2\ell m}.}
\tag{AC2}
\]
The \(2\ell m\) term comes from the one shared seam edge \(c\). All path lengths in (AC2) remain those of the original nine raw links.

Use real characters of unit Haar variance:
\[
G_1=\frac{V+V^{-1}}{\sqrt2},\qquad
G_2=\frac{W+W^{-1}}{\sqrt2},\qquad
F=\frac{U+U^{-1}}{\sqrt2}.
\]
Put \(H_{\mathbf s}=s_1G_1+s_2G_2\), and remove only the common scalar from the nonnegative potentials \(V_i=\sqrt2-G_i\):
\[
B_{\mathbf s}=e^{H_{\mathbf s}/2}D e^{H_{\mathbf s}/2},
\qquad
T_{\mathbf s}=e^{-\sqrt2(s_1+s_2)}B_{\mathbf s}.
\tag{AC3}
\]
The energy ratio and ground-state transition are the same for these two transfers. The clock \(a_t\) is fixed throughout.

The untouched exclusive path \(p\) makes its integer flux \(n\) an exact conserved label under both seam multiplications. Retain the entire \(n=+1\) sector, not just \(U\). Its largest free eigenvalue is \(\alpha=t^4\), simple at \((\ell,m)=(0,0)\). Indeed
\[
\log_t(\theta_{1,\ell,m}/t^4)
=\frac{5(\ell+m)^2+3(\ell-m)^2+4(\ell-m)}2
\]
is zero only at the origin and is at least two elsewhere. The three states attaining two are \((-1,0),(0,1),(-1,1)\). Compactness isolates the top eigenvalue. The \(n=-1\) sector is its complex conjugate and has the same continued eigenvalue; the real source \(F\) uses both sectors with equal weights.

Let \(\Lambda_1(\mathbf s)\) be the isolated top branch on \(n=+1\), and \(\Lambda_0(\mathbf s)\) the actual vacuum eigenvalue. Near zero define
\[
E_1(\mathbf s)=-a_t^{-1}
 \log\frac{\Lambda_1(\mathbf s)}{\Lambda_0(\mathbf s)}.
\tag{AC4}
\]
The positive vacuum lies in \(n=0\), hence is independent of \(U\). Its actual normalized density \(\pi_{\mathbf s}=\psi_{\mathbf s}^2\,dU\,dV\,dW\) satisfies \(\pi_{\mathbf s}F=0\) and \(\pi_{\mathbf s}F^2=1\) at every finite seam pair. Separate shifts \(V\mapsto-V\), \(W\mapsto-W\) make both branches of \(B\), and their ratio, even in each seam strength.

## Nine closed charge states give the exact coefficient

Only the origin, its four nearest neighbors, and the four diagonal neighbors can occur in a closed walk with two insertions of each seam. The shift coefficient in either direction is \(1/\sqrt2\). For a branch with base eigenvalue \(a\), write
\[
x_i=\frac1{1-\theta_{i,0}/a},\quad
y_j=\frac1{1-\theta_{0,j}/a},\quad
z_{ij}=\frac{\theta_{i,j}}a,\qquad i,j\in\{-1,+1\},
\]
where the fixed \(n\) label is suppressed, and put \(X=\sum_i x_i\), \(Y=\sum_jy_j\). The exact closed-walk result is
\[
\boxed{
\left.\partial_1^2\partial_2^2\log\Lambda\right|_0
=\sum_{i,j}\frac{(x_i+y_j-1)^2}{1-z_{ij}}
-Y\sum_i x_i^2-X\sum_j y_j^2+XY.}
\tag{AC5}
\]
[[quartic-seam-eigenvalues-and-the-generalized-pencil|The generalized-pencil recurrence]] gives a direct independent check. For example, the generalized eigenvalue equation
\(D\phi=\Lambda e^{-H_{\mathbf s}}\phi\), with the origin component of \(\phi\) fixed to one, gives
\[
\frac{\Lambda_{20}}a=\frac{X-1}{2},\qquad
\frac{\Lambda_{02}}a=\frac{Y-1}{2},
\]
when subscripts denote ordinary power-series coefficients. At order \((1,1)\) the diagonal component is
\((x_i+y_j-1)/(2(1-z_{ij}))\). The order-\((2,1)\) component at the \(j\)-neighbor is
\[
\frac{y_j}{2\sqrt2}
\left[\sum_i\frac{x_i+y_j-1}{1-z_{ij}}-Xy_j\right],
\]
with the transposed expression at order \((1,2)\). Substitution at the origin at order \((2,2)\), followed by
\(\partial_{22}\log\Lambda=4(\Lambda_{22}/a-\Lambda_{20}\Lambda_{02}/a^2)\), gives (AC5). States farther away cannot return with the remaining insertions. This is an exact derivative of the complete sector, not a spectral truncation.

Set
\[
q=t^2,\quad C_r(q)=1+q+\cdots+q^{r-1},\quad
A=\frac1{1-q^3},\quad B=\frac1{1-q},\quad
v=\frac1{1-q^2}.
\]
For the vacuum, all \(x_i,y_j\) equal \(v\); the diagonal ratios are \(q^5,q^3,q^3,q^5\). For \(n=1\), the two lists are \((A,B)\) and \((B,A)\); three diagonal ratios equal \(q^5\), and the remaining one, joining the two \(B\) neighbors, equals \(q\). Therefore (AC5) becomes
\[
L_0=2(2v-1)^2\left(\frac1{1-q^5}+\frac1{1-q^3}\right)
-8v^3+4v^2,
\]
\[
L_1=
\frac{2(A+B-1)^2+(2A-1)^2}{1-q^5}
+\frac{(2B-1)^2}{1-q}
-2(A+B)(A^2+B^2)+(A+B)^2.
\tag{AC6}
\]
Both are derivatives of logarithms, so the disconnected products have already been subtracted. The physical energy requires their difference. Exact polynomial expansion gives
\[
\boxed{
\left.\partial_1^2\partial_2^2E_1\right|_0
=-\frac{q\,P(q)}
 {a_t(1-q)^3 C_2(q)^3 C_3(q)^3 C_5(q)}<0,}
\tag{AC7}
\]
where
\[
\begin{aligned}
P(q)={}&1+8q+30q^2+79q^3+151q^4+234q^5+294q^6
+318q^7\\
&+294q^8+234q^9+151q^{10}+79q^{11}
+30q^{12}+8q^{13}+q^{14}.
\end{aligned}
\tag{AC8}
\]
Every coefficient is positive. In particular, for the connected energy residual obtained by subtracting both single-seam responses,
\[
E_{1,\mathrm{joint}}(\mathbf s)
=-\frac{s_1^2s_2^2}{4}
\frac{qP(q)}{a_t(1-q)^3C_2^3C_3^3C_5}
+O\!\left(s_1^2s_2^2(s_1^2+s_2^2)\right).
\tag{AC9}
\]
At fixed \(a_t\), its fourth derivative has the strong-attenuation expansion
\(\partial_{22}E_1=-t^2/a_t+O(t^4/a_t)\) as \(t\downarrow0\). The derivative is taken at zero seam strength before this kinetic limit.

## The actual fixed-source chronology also has a joint response

The vacuum normalization and both source caps remain present in
\[
C_N(\mathbf s)
=\Lambda_0(\mathbf s)^{-N}
\langle \psi_{\mathbf s},
 (B_{\mathbf s}|_{n=1})^N\psi_{\mathbf s}\rangle.
\tag{AC10}
\]
Here multiplication by \(U\) identifies the vacuum and \(n=1\) charge bases. The complex source \(U\) and the real unit-variance source \(F\) have the same \(C_N\), by the conjugacy of the two flux sectors.

There is a direct controlled expansion of (AC10). Write \(v_j=e^{H_{\mathbf s}/2}e_j\), \(v=v_0\), and \(Z=\langle v,v\rangle\). The actual vacuum transfer is \(|v\rangle\langle v|+O(q^2)\), while
\[
\frac{B_{\mathbf s}|_{n=1}}{t^4}
=|v\rangle\langle v|
+q\!\!\sum_{j=(-1,0),(0,1),(-1,1)}
 |v_j\rangle\langle v_j|+O(q^2).
\tag{AC11}
\]
The remainders hold in operator norm locally uniformly in seam strength; the same finite derivatives are controlled. The isolated vacuum is \(v/\sqrt Z+O(q^2)\). Its Fourier means are
\[
b_i=\frac{I_1(\sqrt2s_i)}{I_0(\sqrt2s_i)}.
\]
Expanding the \(N\) transfer factors in (AC10), including the actual \(\Lambda_0^{-N}\), gives for every fixed \(N\ge1\)
\[
C_N(\mathbf s)
=t^{4N}\left[
1+Nq(b_1^2+b_2^2+b_1^2b_2^2)+O(q^2)\right].
\tag{AC12}
\]
Thus
\[
\boxed{
\partial_{22}C_N(0)=N t^{4N+2}+O(t^{4N+4}),\qquad
\partial_{22}\mathfrak c_k(F;0)
=-2k\,t^{8k+2}+O(t^{8k+4}),}
\tag{AC13}
\]
where \(\mathfrak c_k=(1-2C_{2k}+C_{4k})/(1-C_{2k})\). The second formula includes the quotient's mixed normalization contacts; those products enter only beyond its displayed leading order. It is a fixed-source expansion for small \(t\), whereas (AC7) is an exact all-\(t\) result for the complete retained sector.

## Removing the shared incidence removes the connected energy

As a separate graph diagnostic, duplicate the shared seam edge \(c\) into two independent length-one links and split its exterior endpoint. The original source face and both seam faces keep their four raw links. This is a different ten-edge graph, not a presentation change of the corner.

Its exponent in (AC2) loses only the cross term \(2\ell m\):
\[
\theta'_{n,\ell,m}
=t^{4n^2}\,t^{4\ell^2+2n\ell}\,t^{4m^2-2nm}.
\tag{AC14}
\]
Consequently each fixed-\(n\) transfer factors into the two one-seam transfers. Both \(\log\Lambda_n\) and the normalized sector energy are sums of functions of the separate seam strengths. Their connected \((2,2)\) coefficient is exactly zero. A nonlinear quotient of source moments need not factor this way.

The distinction between (AC7) and (AC14) is therefore an exact test of spatial incidence. All character multiplications commute in both cases. Comparing the non-Abelian corner must retain its full spin recouplings and its declared higher-representation kinetic law; neither an unequal numerical coefficient nor Abelian nonfactorization by itself establishes the proposed uniform physical attenuation mechanism.

## The matched continuous-time coefficient is finite and negative

There is also a temporal Hamiltonian benchmark on this same finite graph. Fix \(\epsilon>0\), put \(t=e^{-\epsilon a_t}\), and use physical seam strengths \(g_i\) through \(s_i=a_tg_i\). The limiting Hamiltonian is
\[
\mathsf H_{\mathbf g}
=\epsilon\mathsf N+g_1V_1+g_2V_2,
\]
where \(\mathsf N\) has the integer eigenvalues in the exponent of (AC2). The source-sector energy gap at zero seam strength is \(4\epsilon\). Since \(P(1)=1912\), \(C_2(1)^3C_3(1)^3C_5(1)=1080\), and \(1-q\sim2\epsilon a_t\), (AC7) gives
\[
\boxed{
\left.\partial_{g_1}^2\partial_{g_2}^2
 E_1^{\rm Ham}(\mathbf g)\right|_0
=\lim_{a_t\downarrow0}
 a_t^4\left.\partial_{s_1}^2\partial_{s_2}^2E_1\right|_0
=-\frac{239}{1080\,\epsilon^3}.}
\tag{AC15}
\]
This limit is also checked by the finite fourth-order charge walks of \(\mathsf H_{\mathbf g}\). The ordinary \(g_1^2g_2^2\) Taylor coefficients of its vacuum and \(n=1\) eigenenergies are respectively \(-1/(480\epsilon^3)\) and \(-31/(540\epsilon^3)\). Their difference, multiplied by \(2!2!=4\), gives (AC15). They retain both the disconnected products and the actual vacuum energy. Equivalently, the same separate values follow by taking the limits of \(L_0,L_1\) in (AC6).

The factor \(a_t^4\) is required because these are derivatives with respect to physical strengths \(g_i\), not fixed dimensionless lattice strengths \(s_i\). This benchmark takes continuous time on the supplied finite spatial graph. It does not take a spatial continuum or infinite-volume limit.

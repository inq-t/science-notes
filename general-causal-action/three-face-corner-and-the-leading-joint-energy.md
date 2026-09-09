# The Corner's Leading Joint Energy Is Negative

The first joint seam coefficient of the actual \(SU(2)\) corner transfer is negative at small temporal coupling. Three exact length-six channels control the leading correction to its complete source-face odd sector; the outer triangular channel contributes the mixed response. After both vacuum and disconnected normalizations are retained, the mixed energy derivative is \(-t^2/(4a_t)+O(t^4/a_t)\), where \(t\) is the actual fundamental temporal multiplier. The same calculation gives a negative joint change of the fixed source's normalized surplus. This decides the first analytic regime of the corner test; the coefficient away from that regime remains open.

**Status: exact channel identities and controlled operator asymptotics; proved joint sign at small temporal coupling; open physical-limit estimate.** [[three-face-corner-and-joint-seam-response|CJ1–14]] fixes the nine raw links, Gauss carrier, parity sector and complete quartic normalization. [[adjacent-wilson-plaquette-and-the-chronological-surplus|AP]] owns the single-seam control. The proof below evaluates the corner coefficient using a uniform bound on all omitted spins, rather than replacing the actual transfer by an independently normalized loop clock.

## The four lowest channels of the complete odd sector

Keep CJ's oriented paths \(a,b,c,p,q,r\), with lengths \(1,1,1,2,2,2\), and face words
\[
U=apb^{-1},\qquad V=aqc^{-1},\qquad W=brc^{-1}.
\]
After tree gauge fixing, \(U,V,W\) have product Haar measure before the remaining joint conjugation quotient. Put
\[
F=\chi_{1/2}(U),\qquad G=\chi_{1/2}(V),\qquad H=\chi_{1/2}(W),
\]
\[
x=2b_t,\qquad
\tau_j(x)=\frac{I_{2j+1}(x)}{I_1(x)},\qquad
t=\tau_{1/2}(x),\qquad \alpha=t^4 .
\tag{JL1}
\]
Each character has unit Haar norm. Retain the complete physical sector odd under a center flip of one \(p\)-path raw link. Its normalized free transfer is denoted \(P_{0,-}\).

For a spin network, write \(n_e=2j_e\) on the three axes and \(n_p=2\ell_p,n_q=2\ell_q,n_r=2\ell_r\) on the outer paths. Its weighted spin cost is
\[
N=n_a+n_b+n_c+2(n_p+n_q+n_r).
\tag{JL2}
\]
The actual multiplier is CJ4's product of the corresponding \(\tau_j\), with the same path-length powers. The sum of the parity conditions at vertices \(X,Y,Z\) makes \(N\) even.

There are exactly four odd states of cost at most six:

| State | \((n_a,n_b,n_c;n_p,n_q,n_r)\) | Actual multiplier |
|---|---|---|
| \(F=\chi(U)\) | \((1,1,0;1,0,0)\) | \(t^4\) |
| \(L_G=\chi(UV^{-1})\) | \((0,1,1;1,1,0)\) | \(t^6\) |
| \(L_H=\chi(UW)\) | \((1,0,1;1,0,1)\) | \(t^6\) |
| \(L_\triangle=\chi(UWV^{-1})\) | \((0,0,0;1,1,1)\) | \(t^6\) |

These are normalized, mutually orthogonal physical characters. The last word is conjugate to \(prq^{-1}\), the outer triangle in the reduced graph, with six original links.

For completeness, \(n_p\) is odd. If \(n_p\ge3\), the two triangle bounds \(n_a+n_q\ge n_p\), \(n_b+n_r\ge n_p\) imply \(N\ge4n_p\ge12\). If \(n_p=1\), cost at most six leaves \(n_q+n_r\le2\). Sum zero gives \(F\). Sum one gives exactly \(L_G\) or \(L_H\); choosing the higher allowed axis spin already gives cost eight. Sum two permits only \(n_q=n_r=1\), with all three axis spins zero, giving \(L_\triangle\). The cases \(n_q=2\) or \(n_r=2\) cost at least ten. Thus every omitted odd state has \(N\ge8\). Trivalent \(SU(2)\) intertwiners have multiplicity one, so no additional channel is hidden at these costs.

## The remainder controls every higher spin

The positive Bessel series and \(I_1(x)\ge x/2\) give, for integer \(m\ge0\),
\[
\tau_{m/2}(x)
\le e^{x^2/4}\frac{(x/2)^m}{(m+1)!}.
\tag{JL3}
\]
There are nine original link factors. For sufficiently small \(x>0\), any omitted multiplier therefore obeys
\[
0\le\theta_{\mathbf j}
\le e^{9x^2/4}(x/2)^N
\le Cx^8=O(t^8).
\]
The inequality is uniform over all spin labels; \(t=x/4+O(x^3)\). Since the free spin basis is orthonormal and diagonal, this is an operator-norm bound. With
\[
\Pi_6=|L_G\rangle\langle L_G|
     +|L_H\rangle\langle L_H|
     +|L_\triangle\rangle\langle L_\triangle|,
\]
the exact low-cost decomposition has the controlled form
\[
\boxed{\frac{P_{0,-}}{\alpha}
=|F\rangle\langle F|+t^2\Pi_6+O_{\rm op}(t^4).}
\tag{JL4}
\]
On the full physical carrier, every nonconstant spin network has cost at least four, so similarly
\[
P_0=|1\rangle\langle1|+O_{\rm op}(t^4).
\tag{JL5}
\]
One way to see the minimum is to follow the support of any nontrivial edge: the triangle conditions prevent an endpoint of that support. A cycle in the original bipartite corner graph has at least four links, each nontrivial label costs at least one. Equations (JL4)–(JL5) retain the whole physical carrier, including the sectors beyond CJ's finite quartic closure.

## The actual vacuum normalizer cancels only after it is included

For seams \(s_1(2-G)\) and \(s_2(2-H)\), set
\[
M_{\mathbf s}=e^{(s_1G+s_2H)/2},\qquad
B_{\mathbf s}=M_{\mathbf s}P_0M_{\mathbf s}.
\]
Write \(\Lambda_-(\mathbf s)\) and \(\Lambda_\Omega(\mathbf s)\) for its top odd-sector and vacuum eigenvalues. The original transfer also has the common raw factor \(z_t^9e^{-2(s_1+s_2)}\); retain it in the closed amplitude. It cancels from the excitation ratio
\[
\theta_-(\mathbf s)=\frac{\Lambda_-(\mathbf s)}{\Lambda_\Omega(\mathbf s)},
\qquad
E_-(\mathbf s)=-a_t^{-1}\log\theta_-(\mathbf s).
\tag{JL6}
\]
No duration is changed.

Define
\[
Z(s)=\int_{SU(2)}e^{s\chi_{1/2}(U)}\,dU,\qquad
m(s)=\frac{Z'(s)}{Z(s)},\qquad
Z_{\mathbf s}=Z(s_1)Z(s_2).
\]
Then \(Z(0)=1\), \(m(0)=0\), \(m'(0)=1\). The product Haar coordinates give
\[
\|M_{\mathbf s}F\|^2=\|M_{\mathbf s}1\|^2=Z_{\mathbf s}.
\tag{JL7}
\]
The equality uses \(\int F^2dU=1\), not an assumption that the interacting vacuum factors.

Rank-one perturbation of (JL4), with normalized vector
\(v_{\mathbf s}=M_{\mathbf s}F/\sqrt{Z_{\mathbf s}}\), gives
\[
\frac{\Lambda_-(\mathbf s)}{\alpha}
=Z_{\mathbf s}\left[1+t^2\mathcal A(\mathbf s)+O(t^4)\right],
\]
\[
\mathcal A(\mathbf s)=
\frac1{Z_{\mathbf s}^2}
\sum_{L\in\{L_G,L_H,L_\triangle\}}
\left|\left\langle L,F e^{s_1G+s_2H}\right\rangle\right|^2.
\tag{JL8}
\]
Equation (JL5) separately gives
\[
\Lambda_\Omega(\mathbf s)=Z_{\mathbf s}[1+O(t^4)],
\qquad
\psi_{\Omega,\mathbf s}
=\frac{M_{\mathbf s}1}{\sqrt{Z_{\mathbf s}}}+O_{L^2}(t^4).
\tag{JL9}
\]
This is a controlled approximation to the actual vacuum branch. Its corrections are not reset to zero.

All remainders in (JL8)–(JL9) and below are uniform with the seam derivatives needed through order \((2,2)\) on a fixed small seam neighborhood. To justify that statement, extend \(M_{\mathbf s}\) holomorphically to a fixed complex bidisc. It remains bounded there, and \(Z_{\mathbf s}\) stays away from zero. The isolated rank-one eigenvalue has a common separating contour for sufficiently small \(t\). The operator bounds (JL4)–(JL5), the contour resolvent expansion and Cauchy estimates therefore bound the derivatives of each remainder by \(O(t^4)\). The complex continuation uses the analytic bilinear normalization, with squared real overlaps continued as algebraic squares; on real seams it is the positive normalized vacuum. This prevents an unjustified exchange of the small-\(t\) estimate with four seam derivatives.

## Two Schur contractions fix the outer-loop coefficient

Haar orthogonality gives
\[
\int\chi(AU)\chi(U^{-1}B)\,dU=\frac12\chi(AB),\qquad
\int D^{1/2}(U)e^{s\chi(U)}\,dU=\frac{Z'(s)}2I .
\tag{JL10}
\]
Use the actual loop words in the table. Integrating the independent \(U,V,W\) coordinates yields
\[
\left\langle L_G,F e^{s_1G+s_2H}\right\rangle
=\frac12Z'(s_1)Z(s_2),
\]
\[
\left\langle L_H,F e^{s_1G+s_2H}\right\rangle
=\frac12Z(s_1)Z'(s_2),
\]
\[
\boxed{
\left\langle L_\triangle,F e^{s_1G+s_2H}\right\rangle
=\frac14Z'(s_1)Z'(s_2).}
\tag{JL11}
\]
In the last line the \(U\) integration leaves \(\chi(WV^{-1})/2\); the remaining two central matrix integrals give the second factor \(1/2\). Thus the phase and normalization are fixed by the physical characters themselves. In particular \(\langle L_\triangle,FGH\rangle=1/4\).

Substitution into (JL8) gives the explicit leading function
\[
\boxed{
\mathcal A(s_1,s_2)
=\frac14m(s_1)^2+\frac14m(s_2)^2
 +\frac1{16}m(s_1)^2m(s_2)^2.}
\tag{JL12}
\]
The first two terms are single-seam returns. The third is the joint outer-loop contribution. The inverse-dimension factors are the standard normalized boundary contractions already owned by [[gauge-boundary-frame-gluing/finite-gauss-gluing|BG9–9a]] and [[interacting-vacuum-support-at-the-balanced-cut|IS6]]; the new calculation is their complete chronological energy response on this corner.

## Evaluate the joint energy, including disconnected products

Taking the ratio of (JL8) and (JL9) gives
\[
\log\theta_-(\mathbf s)
=\log\alpha+t^2\mathcal A(\mathbf s)+O(t^4).
\]
Since \(\partial_1^2\partial_2^2\mathcal A(0,0)=1/4\),
\[
\boxed{
\partial_1^2\partial_2^2E_-(0,0)
=-\frac{t^2}{4a_t}+O(t^4/a_t)<0
\quad\text{for sufficiently small }t>0.}
\tag{JL13}
\]
The leading coefficient is nonzero. Subtracting both isolated seam energies as in CJ11 gives
\[
E_{\rm joint}(s_1,s_2)
=-\frac{t^2}{16a_t}s_1^2s_2^2
 +O(t^4s_1^2s_2^2/a_t)
 +O\!\left(s_1^2s_2^2(s_1^2+s_2^2)/a_t\right)
\]
locally in the seams, with the small-\(t\) interpretation supplied by the derivative statement (JL13).

The derivative ledger makes the quartic cancellations explicit:
\[
\frac{\Lambda_{-,20}}{\alpha}
=\frac{\Lambda_{-,02}}{\alpha}
=1+\frac{t^2}{2}+O(t^4),\qquad
\frac{\Lambda_{-,22}}{\alpha}
=1+\frac{5t^2}{4}+O(t^4),
\]
\[
\frac{\Lambda_{-,20}\Lambda_{-,02}}{\alpha^2}
=1+t^2+O(t^4),\qquad
\Lambda_{\Omega,20}
=\Lambda_{\Omega,02}
=\Lambda_{\Omega,22}=1+O(t^4).
\tag{JL14}
\]
Thus CJ14's disconnected odd product removes \(1+t^2\), while its vacuum log combination starts at \(O(t^4)\). Keeping only \(\Lambda_{-,22}\) would even retain a false order-one joint effect. As a separate normalization check, (JL12) gives the single-seam \((\log\theta_-)_{20}=t^2/2+O(t^4)\), exactly the small-\(t\) limit of AP19.

The result concerns the complete source-face odd-sector edge. A connected fourth derivative of the full physical gap is not inferred from the sector upper bound; other physical branches may compete.

## The fixed source also has a negative leading joint surplus

Keep the actual source \(F\). CJ7 gives its zero mean and unit variance for every seam pair. In the Haar carrier, its vacuum-weighted vector obeys
\[
F\psi_{\Omega,\mathbf s}=v_{\mathbf s}+O_{L^2}(t^4),
\]
while (JL4) and the actual vacuum normalization give
\[
\frac{B_{\mathbf s}|_{\mathcal H_-}}
       {\alpha\Lambda_\Omega(\mathbf s)}
=|v_{\mathbf s}\rangle\langle v_{\mathbf s}|
 +t^2\frac{M_{\mathbf s}\Pi_6M_{\mathbf s}}{Z_{\mathbf s}}
 +O_{\rm op}(t^4).
\tag{JL15}
\]
For each fixed \(n\ge1\), expanding the finite power gives
\[
\boxed{
C_n(\mathbf s)
=\langle F,P_{\mathbf s}^nF\rangle_{\pi_{\mathbf s}}
=\alpha^n[1+n t^2\mathcal A(\mathbf s)+O(t^4)],
\qquad
C_{n,22}(0,0)=\frac n4t^{4n+2}+O(t^{4n+4}).}
\tag{JL16}
\]
Each of the \(n\) single insertions has the same matrix element
\(\langle v,M\Pi_6Mv\rangle/Z_{\mathbf s}=\mathcal A\).
The remainder retains the uniform seam-derivative control established above.

With \(k\ge1\) fixed, use the actual OI quantities
\[
D_k=1-C_{2k},\quad
S_k=1-2C_{2k}+C_{4k},\quad
r_k=S_k/D_k .
\]
Expanding these complete functions, including their denominator, yields
\[
\boxed{
S_{k,22}(0,0)=-k\,t^{8k+2}+O(t^{8k+4}),\qquad
r_{k,22}(0,0)=-\frac k2t^{8k+2}+O(t^{8k+4}).}
\tag{JL17}
\]
Both are negative for sufficiently small \(t\). The calculation uses the same normalized chronology before and after the two seams. In particular its \(S_k\) is the actual \(V_Q-C_{\rm lag}\), with the outer-law change and all vacuum source factors already included. It is not a conditional-update surrogate.

## The surviving comparison is attenuation, not positive joint energy

[[abelian-corner-and-the-joint-seam-energy|The Abelian corner control]] declares heat multipliers \(\tau_m=t^{m^2}\), the same fundamental multiplier \(t\), the same \(a_t\), and unit-norm real seam sources. Its exact energy coefficient has leading term \(-t^2/a_t\). The \(SU(2)\) coefficient (JL13) is one quarter of that leading magnitude. Both signs are negative, so nonzero joint response itself is not a discriminator of non-Abelian rigidity. The higher-representation kinetic laws also differ and remain declared.

The useful candidate is more specific: normalized non-Abelian fusion might limit the accumulation of energy-lowering outer-loop responses. Here that reduction is exactly the squared \(1/4\) overlap in (JL11), compared with the Abelian control's normalization. It is not an area-law theorem, a positive joint-energy law, or a proof of the full innovation floor.

The next test is whether such a comparison survives complete recoupling when \(t\to1\), with the same physical kinetic calibration. Fix \(\varepsilon>0\), choose \(t=e^{-\varepsilon a_t}\), and put \(s_i=a_tg_i\). The fixed-spin Wilson expansion then gives
\[
\tau_j=1-\frac{4\varepsilon}{3}j(j+1)a_t+O(a_t^2).
\]
The corresponding finite-graph Hamiltonian test is therefore
\[
H_{\rm SU(2)}(\mathbf g)
=\frac{4\varepsilon}{3}\sum_{\text{nine raw links}}C_e
 +g_1(2-G)+g_2(2-H),\qquad C_e=j_e(j_e+1),
\]
\[
\boxed{\mathcal J_{\rm SU(2)}
=\varepsilon^3
\left.\partial_{g_1}^2\partial_{g_2}^2
E_{-,{\rm Ham}}(\mathbf g)\right|_{\mathbf0}.}
\tag{JL18}
\]
Its free source-sector edge is \(4\varepsilon\), matching the Abelian fundamental clock. [[abelian-corner-and-the-joint-seam-energy|AC15]] evaluates the complete fixed-charge Abelian benchmark as \(\mathcal J_{U(1)}=-239/1080\). The \(SU(2)\) value is not yet evaluated.

The high-spin remainder in (JL4) is no longer small in this weak-step regime. For the quartic response (JL18), all channels allowed by CJ's exact finite closure must be reinstated, including its vacuum and disconnected terms; arbitrarily many spins are not required for that coefficient. The full discrete-\(t\) function is also open. This is a finite spatial graph with a temporal Hamiltonian limit, not spatial continuum or volume-uniform control. [[strong-coupling-gap-and-continuum-crossover/inq|The strong-coupling/continuum distinction]] remains binding; more faces at small \(t\) would not settle this test.

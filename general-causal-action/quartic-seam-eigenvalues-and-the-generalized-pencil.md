# Quartic Seam Eigenvalues from a Generalized Pencil

A symmetric seam transfer has an exact coefficient recurrence that keeps the vacuum and disconnected logarithmic terms explicit. Passing to its generalized eigenvalue pencil avoids differentiating both endpoint exponentials separately. Through two insertions of each seam, only a finite set of actual multiplication paths is needed. The recurrence reproduces the single-seam spin weights, the Abelian corner coefficient and its Hamiltonian limit; exact Haar contractions independently fix the leading non-Abelian corner coefficient.

**Status: exact analytic recurrence and executed rational checks.** [[three-face-corner-and-joint-seam-response|CJ]] specifies the physical graph and finite spin closure. [[three-face-corner-and-the-leading-joint-energy|JL]] proves the complete-spin remainder for its evaluated small-coupling result. [[abelian-corner-and-the-joint-seam-energy|AC]] evaluates the complete Abelian corner coefficient. The calculation here changes neither their transfer nor their clock.

## Fix a branch before expanding

Let \(P\) be a bounded positive self-adjoint transfer on its declared physical sector. Let \(e\) be a unit vector with simple isolated eigenvalue \(a>0\). The bounded self-adjoint multiplication operators \(G,H\) commute. Set
\[
B(s,t)=e^{(sG+tH)/2}P e^{(sG+tH)/2},\qquad
B\psi=\lambda\psi.
\tag{QP1}
\]
The analytic substitution \(\phi=e^{(sG+tH)/2}\psi\), followed by scalar intermediate normalization \(\langle e,\phi\rangle=1\), gives
\[
\boxed{P\phi=\lambda e^{-sG-tH}\phi.}
\tag{QP2}
\]
Write all coefficients in this note as **ordinary powers**:
\[
\lambda=\sum_{m,n\ge0}\lambda_{mn}s^mt^n,\qquad
\phi=\sum_{m,n\ge0}\phi_{mn}s^mt^n,
\quad \lambda_{00}=a,\quad \phi_{00}=e.
\]
For \((m,n)\ne(0,0)\), \(\langle e,\phi_{mn}\rangle=0\). A derivative of order \((2,2)\) is four times the corresponding ordinary coefficient. This differs from CJ's derivative-subscript convention.

Let \(R_a\) be \((a-P)^{-1}\) on \(e^\perp\), extended by zero on \(e\). Isolation makes it bounded. Put
\[
E_{ij}=\frac{(-1)^{i+j}}{i!j!}G^iH^j.
\tag{QP3}
\]
For a nonzero multi-index \(r=(m,n)\), use coordinatewise inequalities and define
\[
K_r=\sum_{0<d\le r}E_d\phi_{r-d},\qquad
z_r=\phi_r+K_r,\qquad z_{00}=e,
\]
\[
F_r=aK_r+
\sum_{\substack{0<q\le r\\q\ne r}}\lambda_q z_{r-q}.
\tag{QP4}
\]
Every term in \(F_r\) has already been determined at a lower total degree. Equating coefficients in (QP2) gives
\[
(P-a)\phi_r=F_r+\lambda_r e,
\qquad
\boxed{\lambda_r=-\langle e,F_r\rangle,\qquad
\phi_r=-R_aF_r.}
\tag{QP5}
\]
Thus (QP3)–(QP5), ordered by total degree, are a finite executable recurrence through any declared bidegree. They retain the reduced-resolvent denominators of the actual free transfer.

## The connected fourth derivative

Suppose separate parity symmetries make this eigenbranch even in each seam parameter. Through bidegree \((2,2)\), its nonconstant eigenvalue coefficients can then only be \(\lambda_{20},\lambda_{02},\lambda_{22}\). Consequently
\[
\boxed{\partial_s^2\partial_t^2\log\lambda\big|_0
=4\left(\frac{\lambda_{22}}a
-\frac{\lambda_{20}\lambda_{02}}{a^2}\right).}
\tag{QP6}
\]
For an excitation energy \(E=-a_t^{-1}\log(\lambda_-/\lambda_\Omega)\), evaluate (QP6) separately on the complete selected sector and the actual vacuum, subtract them, and multiply by \(-a_t^{-1}\). The two disconnected products and the vacuum response are required.

For explicit implementation, the last exponential coefficient is
\[
\begin{aligned}
K_{22}={}&-G\phi_{12}-H\phi_{21}
+\tfrac12G^2\phi_{02}+GH\phi_{11}+\tfrac12H^2\phi_{20}\\
&-\tfrac12G^2H\phi_{01}-\tfrac12GH^2\phi_{10}
+\tfrac14G^2H^2e.
\end{aligned}
\tag{QP7}
\]
The two lower eigenvalue insertions in \(F_{22}\) give
\[
\lambda_{22}=-a\langle e,K_{22}\rangle
+\frac{2\lambda_{20}\lambda_{02}}a,
\]
\[
\partial_s^2\partial_t^2\log\lambda\big|_0
=4\left[-\langle e,K_{22}\rangle
+\frac{\lambda_{20}\lambda_{02}}{a^2}\right].
\tag{QP8}
\]
For example, the vector immediately below it is
\[
K_{21}=-G\phi_{11}-H\phi_{20}
+\tfrac12G^2\phi_{01}+GH\phi_{10}-\tfrac12G^2He,
\]
\[
\phi_{21}=-R_a\left[aK_{21}
+\lambda_{20}(\phi_{01}-He)\right],
\tag{QP9}
\]
with the transposed formula for \(\phi_{12}\). These expressions fix the insertion factorials as well as the resolvent signs.

At second order the same recurrence gives
\[
\phi_{10}=aR_aGe,\qquad
\lambda_{20}=a^2\langle Ge,R_aGe\rangle
-\frac a2\|Ge\|^2
=\frac a2\sum_j|\langle e_j,Ge\rangle|^2
\frac{a+\beta_j}{a-\beta_j}.
\tag{QP10}
\]
The sum ranges over the complement, with \(Pe_j=\beta_je_j\); the corresponding spectral integral applies without a discrete complement. Separate evenness ensures \(\langle e,Ge\rangle=0\). The weights \(1/4,3/4\) in [[adjacent-wilson-plaquette-and-the-chronological-surplus|AP18]] therefore give its exact second derivative after multiplying (QP10) by two.

## A finite calculation can represent a complete-sector derivative

The finite input must contain every actual multiplication path that can contribute to the requested closed coefficient. It is not enough to retain a few large kinetic eigenvalues. Multiplication may leave a low-energy subspace and return within four insertions; deleting such a path changes (QP8). Resolvents and free powers preserve the free spectral labels and introduce no additional transitions.

For the Abelian corner, two insertions of each nearest-neighbor seam can visit only the origin, four neighbors and four diagonal neighbors on a closed walk. Excursions to a coordinate of magnitude two cannot return while still inserting the other seam twice. Its nine-state calculation is therefore exact for the complete-sector derivative. CJ's non-Abelian finite closure follows the same criterion, while retaining all allowed spin recouplings and intertwiner phases.

The [[general-causal-action/receipts/quartic_seam_eigenvalue_receipt.py|executable coefficient receipt]] uses rational arithmetic in a diagonal spectral basis. An orthogonal unnormalized basis is permitted when its coordinate functional and multiplication matrices are transformed together. This removes the square root from AP's two channel weights. For the Abelian check the move amplitude is first \(1/2\), then both seam parameters are rescaled to restore \(1/\sqrt2\); a \((2,2)\) coefficient gains a factor four.

The executed checks give:

| Check | Exact result |
|---|---|
| Disjoint two-factor branches | \(\partial_{22}\log\lambda=0\) |
| AP single-seam channel weights | (QP10) with \(1/4,3/4\), including the factor two to obtain a derivative |
| Heat \(U(1)\) corner, \(t_{\rm heat}=1/2\), vacuum | \(\partial_{22}\log\Lambda_0=559232/24168375\) |
| Same corner, retained charge one | \(\partial_{22}\log\Lambda_1=62312660/85266027\) |
| Their difference | \(7542461188/10658253375\) |
| Complete Abelian rational expression | \((1-q)^3C_2^3C_3^3C_5(L_1-L_0)=qP(q)\), coefficient by coefficient |
| Matched Abelian Hamiltonian, \(\epsilon=1\) | \(\partial_{22}E=-239/1080\) |
| Fundamental \(SU(2)\) outer-loop overlap | \(\langle L_\triangle,FGH\rangle=1/4\) |

The first control follows from exact tensor factorization. The two Abelian transfer values agree independently with AC5's closed-walk expression. A separate exact polynomial calculation multiplies AC6's \(L_1-L_0\) by \((1-q)^3C_2^3C_3^3C_5\); every coefficient equals that of \(qP(q)\) in AC8, and all fifteen coefficients of \(P\) are positive. This verifies the all-parameter sign algebra without sampling parameter values. The Hamiltonian check directly expands \(H_0-sG-tH\) on the same closed paths, retaining its energy-dependent normalization terms. Its ordinary vacuum and charge-one quartic coefficients are \(-1/480\) and \(-31/540\); their difference times four agrees with the temporal limit in AC15. For general \(\epsilon\), the three free resolvents give the factor \(\epsilon^{-3}\).

In the non-Abelian check, the two fundamental Haar contractions give the exact overlaps \(1/2,1/2,1/4\). Squaring the joint overlap and taking two derivatives in each unit-variance seam gives \(4(1/4)^2=1/4\). The conclusion
\[
\partial_{22}\log(\Lambda_-/\Lambda_\Omega)
=\frac{t_f^2}{4}+O(t_f^4)
\tag{QP11}
\]
also uses JL's complete low-cost inventory, rank-one normalization and uniform analytic remainder. The arithmetic receipt checks its coefficient; it does not replace that analytic proof or evaluate the full function of \(t_f\).

Finally, intermediate normalization in (QP2) is only an eigenvalue convenience. For source histories one must return to \(\psi=e^{-(sG+tH)/2}\phi\), normalize the actual vacuum, and include both source caps and the transfer normalizer. [[seam-coupling-response-and-the-vacuum-cap|SV]] and the actual corner source calculations retain those terms. A sector eigenvalue recurrence alone does not calculate a normalized-source surplus or establish a uniform physical gap.

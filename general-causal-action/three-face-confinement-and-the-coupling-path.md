# Three-Face Confinement Depends on the Coupling Path

When all three corner faces are confined at comparable strengths, the full physical gap grows like a nine-dimensional gauge-invariant oscillator gap. With central strength \(\lambda=rg\), \(r>0\) fixed, its leading value is \(2\sqrt{\kappa g\,\eta_-(r)}\), where \(\eta_-(r)=(4r+3-\sqrt{16r^2-16r+9})/2\). At equal strengths this is \(2\sqrt{2\kappa g}\). It differs from extrapolating the residual-rotor theorem beyond its fixed-central-strength hypothesis; both limits remain consistent.

**Status: proved full finite-graph gap asymptotic for each fixed \(r>0\).** [[strong-seam-resolvent-and-the-physical-rotor|The residual-rotor return]] treats \(g\to\infty\) with central strength fixed. This note treats the diagonal family of the same Hamiltonian. The proof applies [[corner-fast-vacuum-and-harmonic-separation|FH's equivariant localization argument]] to all three holonomies, with no surviving matrix fiber or independently chosen vacuum.

## The same nine-link Hamiltonian has a new well

Retain the based corner words \(U,V,W\), their product Haar measure and simultaneous Gauss action from [[three-face-corner-and-joint-seam-response|CJ1–5]]. Fix \(\kappa=4\epsilon/3>0\) and define
\[
\mathsf H_{g,r}=\mathsf H_0+g\mathcal V_r,\qquad
\mathcal V_r=r(2-\chi_{1/2}(U))
+(2-\chi_{1/2}(V))+(2-\chi_{1/2}(W)),
\tag{CP1}
\]
where
\[
\begin{aligned}
\mathsf H_0=\kappa\bigl[&
2(C_U+C_V+C_W)
+\mathcal C(\mathcal L_U+\mathcal L_V)\\
&+\mathcal C(-\mathcal R_U+\mathcal L_W)
+\mathcal C(\mathcal R_V+\mathcal R_W)\bigr],
\qquad \mathcal C(X)=-\sum_aX_a^2 .
\end{aligned}
\tag{CP2}
\]
These are the actual nine raw-link Casimirs in [[corner-hamiltonian-invariant-polynomials|IP3]]. The physical carrier is
\[
\mathcal H_{\rm phys}=L^2(SU(2)^3,dU\,dV\,dW)^{\mathrm{Ad}SU(2)}.
\]
For \(r>0\), \(\mathcal V_r\) has exactly one zero, \((I,I,I)\). The real kinetic form is uniformly elliptic on the compact smooth cover. The ground state is positive, unique and gauge invariant. Denote the two lowest physical eigenvalues by \(E_0(g,r),E_1(g,r)\), and their difference by \(\Delta(g,r)\). The central magnetic term prevents use of the previous conserved \(U\)-spin blocks.

Use exponential coordinates
\[
U=e^{-ix\cdot\sigma/2},\qquad
V=e^{-iy\cdot\sigma/2},\qquad
W=e^{-iz\cdot\sigma/2}.
\]
At the well the principal kinetic matrix and quadratic potential are
\[
A_3=\begin{pmatrix}4&1&-1\\1&4&1\\-1&1&4\end{pmatrix},
\qquad D_r=\operatorname{diag}(r,1,1),
\]
\[
\mathsf H_0^{\rm principal}=\kappa p^{\mathsf T}(A_3\otimes I_3)p,
\qquad
\mathcal V_r=\frac{r|x|^2+|y|^2+|z|^2}{4}
+O_r(|(x,y,z)|^4).
\tag{CP3}
\]
The signs of the two \(U\)-seam cross terms retain the raw orientations. The eigenvalues of \(A_3\) are \(2,5,5\), so the well is nondegenerate in all nine covering coordinates.

## Diagonalize the oscillator before imposing its scalar sector

Put \(h=(\kappa/g)^{1/4}\) and rescale \((x,y,z)=h(X,Y,Z)\). Dividing by \(\sqrt{\kappa g}=\kappa/h^2\) gives the limiting oscillator
\[
\mathcal O_r
=p^{\mathsf T}(A_3\otimes I_3)p
+\frac14(X,Y,Z)^{\mathsf T}(D_r\otimes I_3)(X,Y,Z).
\tag{CP4}
\]
The canonical coordinate change by \(D_r^{1/2}\) makes the quadratic potential Euclidean. Its squared excitation frequencies are therefore the eigenvalues of
\[
D_r^{1/2}A_3D_r^{1/2}
=\begin{pmatrix}
4r&\sqrt r&-\sqrt r\\
\sqrt r&4&1\\
-\sqrt r&1&4
\end{pmatrix}.
\]
The vector \((0,1,1)\) has eigenvalue \(5\). In its orthogonal complement, the matrix is
\(\begin{pmatrix}4r&\sqrt{2r}\\\sqrt{2r}&3\end{pmatrix}\).
Thus
\[
\boxed{\eta_0=5,\qquad
\eta_\pm(r)=\frac{4r+3\pm\sqrt{16r^2-16r+9}}2.}
\tag{CP5}
\]
Their product relation is \(\eta_+\eta_-=10r\). The two-by-two characteristic polynomial at \(3\) is \(-2r<0\), so \(0<\eta_-<3<\eta_+\). Therefore \(\sqrt{\eta_-}\) is always the smallest excitation frequency. Each frequency occurs in three Lie-algebra components, and the oscillator ground energy is
\[
\omega_0(r)=\frac32\left(\sqrt5+\sqrt{\eta_+(r)}+\sqrt{\eta_-(r)}\right).
\tag{CP6}
\]

All normal-coordinate changes act on the three face labels and commute with the common adjoint rotation of their vector components. Joint Gauss invariance is therefore precisely the scalar \(SO(3)\) sector of this oscillator. Its ground Gaussian is a scalar. Every one-quantum state transforms as spin one and is excluded. Two quanta in the slowest normal mode contain the nonzero scalar creation state
\(\sum_{a=1}^3(a_{-,a}^\dagger)^2\Omega\).
No state with two or more quanta has smaller energy. Consequently the first invariant excitation is
\[
\boxed{\omega_1^{\rm phys}(r)-\omega_0(r)=2\sqrt{\eta_-(r)}.}
\tag{CP7}
\]
There is no retained representation fiber here that could pair with a single spin-one quantum. Replacing the physical scalar sector by the unrestricted oscillator would miss the factor two.

## The equivariant harmonic comparison applies to the full carrier

For clarity, the transfer of FH's proof does not assume oscillator convergence. Fix \(r>0\) and \(0<\alpha<1\). Use simultaneous-conjugation-invariant IMS cutoffs around the well with radius \(\delta_h=h^\alpha\). The scaled localization error is \(O(h^2/\delta_h^2)=o(1)\). Outside the inner ball, the scaled potential is bounded below by \(c_r(\delta_h/h)^2\to\infty\).

Inside the ball, the principal coefficients differ from \(A_3\otimes I_3\) by \(O(\delta_h)\). The potential differs from its positive quadratic part by relative \(O_r(\delta_h^2)\), and Haar density is its value at the origin times \(1+O(\delta_h^2)\). Dilation and multiplication by the square root of that density give an isometry to a ball of radius \(2\delta_h/h\) in \(\mathbb R^9\). This map intertwines simultaneous conjugation exactly. The scaled inner form differs from (CP4) by a vanishing relative form error and a vanishing additive error.

The min–max lower bound follows from the localized direct sum: its outside block escapes to infinity, and extending the inside Dirichlet functions by zero compares them with the invariant oscillator on all of \(\mathbb R^9\). For the upper bound, pull back finitely many invariant oscillator eigenfunctions and cut off their Gaussian tails. Their finite Rayleigh matrices converge to the oscillator matrices. Hence every fixed ordered physical eigenvalue satisfies
\[
\frac{E_m(g,r)}{\sqrt{\kappa g}}\longrightarrow
\omega_m^{\rm phys}(r)
\qquad(g/\kappa\to\infty).
\tag{CP8}
\]
The cutoffs and chart are equivariant on the smooth group cover; no singular orbit coordinate or boundary condition is introduced. The constants may depend on the fixed \(r\).

Subtracting the two actual lowest energies gives the full physical gap theorem
\[
\boxed{\Delta(g,r)
=2\sqrt{\kappa g\,\eta_-(r)}+o_r(\sqrt{\kappa g}),
\qquad r>0\ \text{fixed}.}
\tag{CP9}
\]
Both the ground energy and its subtraction come from the original interacting operator.

## Two coupling paths give different asymptotic coefficients

At equal strengths, \(\eta_-(1)=2\), and therefore
\[
\boxed{\Delta(g,1)=2\sqrt{2\kappa g}+o(\sqrt{\kappa g}).}
\tag{CP10}
\]
By contrast, [[strong-seam-resolvent-and-the-physical-rotor|PR16–18]] first sends the two seam strengths \(g\) to infinity at a fixed central strength \(\lambda\). Its returned Hamiltonian on class functions is
\[
\mathsf T_\lambda=\frac{10\kappa}{3}C_U
+\lambda(2-\chi_{1/2}(U)).
\]
Applying the same local argument in three covering dimensions to this rotor, then imposing its scalar sector, gives
\[
\operatorname{gap}(\mathsf T_\lambda)
=2\sqrt{\frac{10\kappa}{3}\lambda}
+o(\sqrt{\kappa\lambda})
\qquad(\lambda/\kappa\to\infty).
\tag{CP11}
\]
Setting \(\lambda=g\) in this iterated-limit expression would give a coefficient different from (CP10): the actual equal-strength coefficient divided by that extrapolated coefficient is \(\sqrt{3/5}\). That substitution is outside PR's fixed-\(\lambda\) hypothesis. For fixed positive \(\lambda/g\), all three normal modes occupy comparable confining scales, so the central variable is no longer the retained slow rotor of that limit.

The coefficients have the expected overlap at small positive ratio:
\[
\boxed{\eta_-(r)=\frac{10}{3}r-\frac{20}{27}r^2+O(r^3)
\qquad(r\downarrow0).}
\tag{CP12}
\]
Its leading term agrees with the residual coefficient. This algebraic expansion does not establish a spectral estimate uniform as \(r\to0\); the nondegenerate-well constants then deteriorate.

The two results describe different coupling paths through one fixed finite graph. They neither contradict each other nor justify replacing the inherited physical gap by a single coupling-independent rotor formula. No bound uniform in spatial size, no spatial continuum limit and no infinite-volume Yang–Mills conclusion is asserted.

# The Abelian Corner Returns a Strong-Seam Rotor

At fixed electric scale, making both magnetic seams strong sends the complete \(U(1)\) central-flux energy to \((10/3)\epsilon n^2\). Completing the actual nine-edge kinetic form leaves a flat torus twist. Diamagnetism gives a lower bound, and a localized trial state gives an error at most \(C\epsilon\sqrt{\epsilon/g}\), uniformly in the integer flux. The fractional phase cannot be removed globally except when \(n\) is divisible by three; the proof retains that distinction.

**Status: exact finite-graph identity and proved strong-seam energy limit.** [[abelian-corner-and-the-joint-seam-energy|AC1–2 and AC15]] fix the actual charge law and Hamiltonian calibration. Both seams below have the same physical strength \(g\). This establishes the Abelian endpoint for comparison with the non-Abelian quantum return; it takes neither spatial continuum nor infinite volume.

## Complete the kinetic square on the actual torus

Write \(V=e^{i\theta}\), \(W=e^{i\varphi}\) and retain the complete central-flux sector \(n\in\mathbb Z\). With \(D=-i(\partial_\theta,\partial_\varphi)\), its Hamiltonian is
\[
\mathsf H_n
=\epsilon\left[
4n^2+4D_\theta^2+4D_\varphi^2
+2nD_\theta-2nD_\varphi+2D_\theta D_\varphi\right]
+g\mathcal V(\theta,\varphi),
\]
\[
\mathcal V=\sqrt2(2-\cos\theta-\cos\varphi).
\tag{AR1}
\]
The physical seam characters are \(\sqrt2\cos\theta,\sqrt2\cos\varphi\), as in AC. The quadratic form domain is the usual periodic \(H^1(\mathbb T^2)\).

Set
\[
A=\begin{pmatrix}4&1\\1&4\end{pmatrix},\qquad
\eta_n=\frac n3(1,-1),\qquad
K_{\eta,g}=\epsilon(D+\eta)^TA(D+\eta)+g\mathcal V.
\]
Since \(A\eta_n=n(1,-1)\) and \(\eta_n^TA\eta_n=2n^2/3\),
\[
\boxed{\mathsf H_n=\frac{10}{3}\epsilon n^2+K_{\eta_n,g}.}
\tag{AR2}
\]
Let \(\mu_\eta(g)\) be the lowest eigenvalue of \(K_{\eta,g}\). The actual full vacuum lies in \(n=0\); its positive normalized wavefunction \(\psi_g(\theta,\varphi)\) is independent of \(U\). Thus the complete retained-flux excitation energy is
\[
E_n(g)=\frac{10}{3}\epsilon n^2+
\mu_{\eta_n}(g)-\mu_0(g).
\tag{AR3}
\]
No truncation of the two remaining integer charges is made.

The phase \(e^{-in(\theta-\varphi)/3}\) is a periodic unitary only when \(n\in3\mathbb Z\). For other \(n\), treating it as a global periodic gauge transformation would change the domain and incorrectly discard the twist.

## The twist correction is nonnegative and uniformly bounded

For a complex test function \(f=r e^{i\alpha}\), the local kinetic identity is
\[
|(D+\eta)f|_A^2
=|\nabla r|_A^2+r^2|\nabla\alpha+\eta|_A^2
\ge|\nabla|f||_A^2.
\tag{AR4}
\]
The inequality extends to the form domain across zeros by approximation. The variational principle gives \(\mu_\eta(g)\ge\mu_0(g)\).

Adding an integer vector to \(\eta\) is a periodic unitary change. Complex conjugation changes \(\eta\) to \(-\eta\). Consequently \(\mu_{\eta_n}\) depends only on \(n\bmod3\), with the two nonzero classes equal. Denote their common excess by \(\delta(g)\). Testing their representative \(\eta=(1,-1)/3\) against the real positive untwisted vacuum gives
\[
\frac{\langle\psi_g,K_{\eta,g}\psi_g\rangle}{\|\psi_g\|^2}
=\mu_0(g)+\epsilon\eta^TA\eta
=\mu_0(g)+\frac23\epsilon.
\]
The term linear in \(D\) vanishes by periodicity and reality. Therefore
\[
\boxed{
E_n(g)=\frac{10}{3}\epsilon n^2+
\begin{cases}
0,&n\in3\mathbb Z,\\
\delta(g),&n\notin3\mathbb Z,
\end{cases}
\qquad 0\le\delta(g)\le\frac23\epsilon.}
\tag{AR5}
\]
This holds for every \(g\ge0\). At \(g=0\), the minimum free twist cost is \(2\epsilon/3\), so \(E_1(0)=4\epsilon\), consistently with the preceding corner calculations.

## A cutoff controls the strong-seam error

The potential has one zero on the torus, at \((0,0)\). Choose fixed nested balls about that point contained in one coordinate chart. A normalized Gaussian trial function, cut off inside the chart, with width proportional to \((\epsilon/g)^{1/4}\), gives
\[
\mu_0(g)\le C_1\sqrt{\epsilon g},\qquad g\ge\epsilon.
\tag{AR6}
\]
Indeed its kinetic expectation is bounded by \(C\epsilon/h^2\), and \(\mathcal V\le C|(\theta,\varphi)|^2\) bounds its potential expectation by \(Cgh^2\). The cutoff and its width constant can be chosen once.

Away from a fixed neighborhood of the well, \(\mathcal V\ge c_0>0\). Positivity of both terms of \(K_{0,g}\) and (AR6) imply
\[
\int_{\text{outside that neighborhood}}|\psi_g|^2
\le \frac{\mu_0(g)}{c_0g}
\le C_2\sqrt{\epsilon/g}.
\tag{AR7}
\]
Choose a smooth real cutoff \(0\le\chi\le1\), equal to one near the well and supported inside the chart. Its transition annulus lies where (AR7) applies. The exact ground-state product identity is
\[
\langle\chi\psi_g,K_{0,g}\chi\psi_g\rangle
-\mu_0(g)\|\chi\psi_g\|^2
=\epsilon\int(\nabla\chi)^TA(\nabla\chi)\,\psi_g^2.
\tag{AR8}
\]
It follows by integration by parts using the actual eigenvalue equation, so the vacuum normalization has not been replaced by a trial Gaussian.

Now use the twisted trial state
\[
f_{n,g}=e^{-in(\theta-\varphi)/3}\chi\psi_g.
\tag{AR9}
\]
It extends periodically by zero outside the chart and belongs to the required form domain for every integer \(n\). The flat connection cancels its phase exactly on the support. Equations (AR7)–(AR8) therefore give
\[
0\le\mu_{\eta_n}(g)-\mu_0(g)
\le
\frac{\epsilon\int(\nabla\chi)^TA(\nabla\chi)\psi_g^2}
     {\|\chi\psi_g\|^2}
\le C_3\epsilon\sqrt{\epsilon/g}
\tag{AR10}
\]
when \(g\ge C_4\epsilon\), since \(\|\chi\psi_g\|^2\ge1-C_2\sqrt{\epsilon/g}\). All constants are independent of \(n\), \(g\) and \(\epsilon\). The phase has unit modulus and leaves no \(n\)-dependent cutoff term.

Combining this estimate with the bound \(2\epsilon/3\) in (AR5), and increasing the constant on the bounded interval \(\epsilon\le g\le C_4\epsilon\), yields
\[
\boxed{
0\le E_n(g)-\frac{10}{3}\epsilon n^2
\le C\epsilon\sqrt{\epsilon/g},
\qquad g\ge\epsilon,\quad n\in\mathbb Z.}
\tag{AR11}
\]
In particular \(E_1(g)\to10\epsilon/3\), and the correction is identically zero at every strength for \(n\in3\mathbb Z\). The proof gives a polynomial error bound; exponential decay and monotonicity in \(g\) are not claimed.

This theorem concerns the bottom of each complete retained-flux sector, relative to the actual vacuum. It does not by itself estimate all excited states within \(n=0\), identify the full physical gap at every seam strength, or prove the corresponding non-Abelian limit. In that comparison, the quantum vacuum and its derivative couplings must be controlled before a classical Schur complement is identified with the effective rotor.

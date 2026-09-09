# Oriented Triad Resonance and the Physical Source Block

A cubic Lie-bracket jet can be removed by an odd polynomial normal form precisely when its resonant component vanishes. The denominator is the triangle polynomial of the three oscillator frequencies. At a frequency-sum resonance, its compatibility condition is also an explicit matrix element between two neutral physical source states. Even when that coupling vanishes, matching the kinetic jet and vacuum leaves a nonzero freedom in the source-product contact. The open five-by-five patch supplies an exact candidate resonance; its actual edge contractions remain a separate calculation.

**Status: exact oscillator-core algebra and physical source normalization.** [[four-face-source-products-and-the-oriented-contact|PC3]] gives the coefficient system, and [[all-group-oriented-kinetic-jet-and-source-lift|AJ]] derives its Cartan-tensor form from actual group words. [[comb-face-transport-and-the-first-nonlinear-jet|The comb rows]] supply the coefficients when a graph is selected. [[lie-bracket-source-contact-and-the-positive-comparison-test|LC]] fixes the invariant metric and structure-constant norm. No nonzero coupling on the candidate patch is assumed here.

## The triad equation and its denominator

Fix a compact simple Lie algebra with invariant positive metric \(Q\), dimension \(d\), and Cartan form
\[
T_G(X,Y,Z)=Q(X,[Y,Z]).
\]
Choose three distinct spatial modes \(i,j,k\) in this order. Their positive oscillator frequencies are \(\omega_i,\omega_j,\omega_k\), and \(q_a=\omega_a^2\). On the polynomial-Gaussian core use
\[
K_0=\sum_a\left(-\omega_a^2\Delta_a+
\frac{|Y_a|_Q^2}{4}-\frac{d\omega_a}{2}\right),
\qquad
\nabla_a\Omega=-\frac{Y_a}{2\omega_a}\Omega .
\tag{RT1}
\]
Other modes, if present, are spectators.

Keep the slot orientation explicit:
\[
\begin{aligned}
D_i&=T_G(Y_i,\nabla_j,\nabla_k),&
U_i&=T_G(\nabla_i,Y_j,Y_k),\\
D_j&=T_G(\nabla_i,Y_j,\nabla_k),&
U_j&=T_G(Y_i,\nabla_j,Y_k),\\
D_k&=T_G(\nabla_i,\nabla_j,Y_k),&
U_k&=T_G(Y_i,Y_j,\nabla_k),\\
P&=T_G(\nabla_i,\nabla_j,\nabla_k).
\end{aligned}
\]
For a real jet \(V^{ijk}=v_iD_i+v_jD_j+v_kD_k\), seek
\(S^{ijk}=u_iU_i+u_jU_j+u_kU_k+pP\) with
\([K_0,S^{ijk}]=-V^{ijk}\). The identities
\([K_0,Y_a]=-2q_a\nabla_a\) and
\([K_0,\nabla_a]=-Y_a/2\) give
\[
\boxed{
u_i+u_j+u_k=0,\qquad
2q_ku_j+2q_ju_k+\frac p2=v_i,
\quad\text{and cyclic permutations}.}
\tag{RT2}
\]
Each term of \(S^{ijk}\) is formally skew on this core. No closed operator or exponential is required.

Define
\[
w_i=q_i(q_j+q_k-q_i),\qquad
\Delta=2(q_iq_j+q_jq_k+q_kq_i)-q_i^2-q_j^2-q_k^2.
\]
Then \(\sum_a w_a=\Delta\). Multiplying the three equations in (RT2) by the respective \(w_a\) gives
\[
\sum_a w_av_a
=4q_iq_jq_k(u_i+u_j+u_k)+\frac p2\Delta.
\]
Consequently, whenever \(\Delta\ne0\),
\[
\boxed{p=\frac{2\sum_a w_av_a}{\Delta}.}
\tag{RT3}
\]
This is not merely a necessary formula: the complete system has a unique solution. For example, putting \(a=q_k-q_i-q_j\), elimination yields
\[
\begin{aligned}
u_i&=-\frac{2q_i(v_i-v_k)+a(v_j-v_k)}{2\Delta},\\
u_j&=-\frac{a(v_i-v_k)+2q_j(v_j-v_k)}{2\Delta},\qquad
u_k=-u_i-u_j.
\end{aligned}
\]
The determinant of these two difference equations is \(4\Delta\).
For the four-face triple with \(q=(2,4,4)\), (RT3) recovers
\(p=(6v_i+4v_j+4v_k)/7\).

## Resonance is an exact compatibility condition

The denominator factors as
\[
\boxed{
\Delta=(\omega_i+\omega_j+\omega_k)
(-\omega_i+\omega_j+\omega_k)
(\omega_i-\omega_j+\omega_k)
(\omega_i+\omega_j-\omega_k).}
\tag{RT4}
\]
Since all frequencies are positive, \(\Delta=0\) precisely when one is the sum of the other two. Relabel so that
\(\omega_k=\omega_i+\omega_j\). Writing
\(a=\omega_i\), \(b=\omega_j\), \(c=\omega_k=a+b\), one has
\[
(w_i,w_j,w_k)=2abc(a,b,-c).
\]
The exact solvability condition is therefore
\[
\boxed{r:=av_i+bv_j-cv_k=0.}
\tag{RT5}
\]
The coefficient system has rank three: its null space is
\[
(u_i,u_j,u_k;p)=s(a,b,-c;-4abc),\qquad s\in\mathbb R.
\tag{RT6}
\]
For instance, subtracting the \(k\) equation from the other two in the homogeneous system forces \(u_j=(b/a)u_i\), after which the sum and \(k\) equations determine \(u_k,p\). Thus (RT5) is sufficient as well as necessary.

A nonzero \(r\) prevents removal of this component by a normal form. When \(r=0\), a solution exists but its third-derivative coefficient has the freedom (RT6). The uniqueness argument used for the four-face odd normal form cannot be carried through this resonance. Because the third derivative contributes to the multiplier product contact, this freedom also matters when transporting the source algebra.

## The obstruction survives full Gauss reduction

The resonance is not automatically lost when charged one-quantum states are excluded. In a \(Q\)-orthonormal basis let
\[
f_{\alpha\beta\gamma}=Q(e_\alpha,[e_\beta,e_\gamma]),
\qquad
\mathfrak F_Q=\sum_{\alpha,\beta,\gamma}
f_{\alpha\beta\gamma}^2>0.
\]
Use the normalized ladder operators
\[
a_{m,\alpha}
=\frac{Y_{m,\alpha}}{2\sqrt{\omega_m}}
+\sqrt{\omega_m}\,\partial_{m,\alpha},
\qquad
a^\dagger_{m,\alpha}
=\frac{Y_{m,\alpha}}{2\sqrt{\omega_m}}
-\sqrt{\omega_m}\,\partial_{m,\alpha}.
\]
They obey \([a_{m,\alpha},a^\dagger_{n,\beta}]
=\delta_{mn}\delta_{\alpha\beta}\) and \(a_{m,\alpha}\Omega=0\).

Consider the two unit vectors
\[
\chi_k
=\frac{\sum_\alpha(a^\dagger_{k,\alpha})^2\Omega}{\sqrt{2d}}
=\frac{|Y_k|_Q^2/\omega_k-d}{\sqrt{2d}}\Omega,
\]
\[
\tau_{ijk}
=\frac{\sum_{\alpha,\beta,\gamma}f_{\alpha\beta\gamma}
a^\dagger_{i,\alpha}a^\dagger_{j,\beta}a^\dagger_{k,\gamma}
\Omega}{\sqrt{\mathfrak F_Q}}
=\frac{T_G(Y_i,Y_j,Y_k)\Omega}
{\sqrt{\omega_i\omega_j\omega_k\mathfrak F_Q}}.
\tag{RT7}
\]
Their normalizations follow from independent oscillator modes: the squared norm of the radial pair is \(2d\), and that of the Cartan creation tensor is \(\mathfrak F_Q\). Both states are invariant under simultaneous \(\operatorname{Ad}G\). Their energies are \(2c\) and \(a+b+c=2c\), while their total polynomial parities differ.

Let
\[
W=\sum_{\alpha,\beta,\gamma}f_{\alpha\beta\gamma}
a^\dagger_{i,\alpha}a^\dagger_{j,\beta}a_{k,\gamma}.
\]
Since \(Y_m=\sqrt{\omega_m}(a_m+a_m^\dagger)\) and
\(\partial_m=(a_m-a_m^\dagger)/(2\sqrt{\omega_m})\),
the coefficients of \(W\) in \(D_i,D_j,D_k\) are respectively
\[
-\frac{a}{4\sqrt{abc}},\qquad
-\frac{b}{4\sqrt{abc}},\qquad
\frac{c}{4\sqrt{abc}}.
\]
The adjoint terms have the same coefficients. The resonant part of this triad is therefore
\[
\boxed{V^{ijk}_{\rm res}
=-\frac{r}{4\sqrt{abc}}(W+W^\dagger).}
\tag{RT8}
\]
Here \([K_0,W]=0\). Also
\[
W\chi_k=\sqrt{\frac{2\mathfrak F_Q}{d}}\,\tau_{ijk}.
\]
All other ladder monomials have different mode occupations, so
\[
\boxed{
\langle\tau_{ijk},V^{ijk}\chi_k\rangle
=-\frac{r}{4\sqrt{abc}}
\sqrt{\frac{2\mathfrak F_Q}{d}}.}
\tag{RT9}
\]
Repeated-mode angular terms cannot supply this transition because it changes occupations in three distinct modes.

For equal-energy core vectors, every commutator
\(\langle\tau,[K_0,S]\chi\rangle\) is zero. Hence a nonzero (RT9) obstructs removing the jet even on the physical invariant core, not only within the chosen differential ansatz. Conversely, the null generator in (RT6) equals
\(-2s\sqrt{abc}(W-W^\dagger)\), displaying the physical resonant freedom directly.

The first vacuum correction is a different question. An odd jet has zero vacuum mean, and the inverse of \(K_0\) off the vacuum remains available on each fixed finite polynomial input. This resonance can obstruct a universal source normal form without obstructing the first vacuum quasimode or implying a vanishing physical gap.

## Compatible resonance still leaves a source-identification choice

Suppose \(r=0\) and let \(S\) be one solution. The generator
\[
\boxed{
N=aU_i+bU_j-cU_k-4abcP
=-2\sqrt{abc}(W-W^\dagger)}
\tag{RT10}
\]
is real, odd, invariant and formally skew on the full polynomial core. It satisfies
\([K_0,N]=0\) and \(N\Omega=0\). Hence every
\(S+\theta N\), \(\theta\in\mathbb R\), has the same kinetic commutator and first vacuum correction.

For its multiplier lift and product contact write
\[
\mathcal D_N(F)=\Omega^{-1}[N,M_F]\Omega,\qquad
\mathcal C_N(F,G)=\mathcal D_N(FG)-F\mathcal D_N(G)-G\mathcal D_N(F).
\]
With \(R_m=|Y_m|_Q^2\), the ladder expressions give
\[
\boxed{
\mathcal D_N(R_i)=\mathcal D_N(R_j)=0,\qquad
\mathcal D_N(R_k)=-4c\,T_G(Y_i,Y_j,Y_k),}
\]
\[
\boxed{
\mathcal C_N(R_i,R_j)=8ab\,T_G(Y_i,Y_j,Y_k).}
\tag{RT11}
\]
Indeed \(R_m\Omega=d\omega_m\Omega+
\omega_m\sum_\alpha(a^\dagger_{m,\alpha})^2\Omega\).
Both \(W,W^\dagger\) annihilate the \(i\)- and \(j\)-radius states, while \(W\) acting on the \(k\)-radius creates twice the Cartan tensor. On \(R_iR_j\Omega\), only \(W^\dagger\) survives, with coefficient \(4ab\). Substitution in (RT10) proves both formulas. Equivalently, the third-derivative coefficient \(p=-4abc\) gives
\(\mathcal C_N(R_i,R_j)=-2p\,T_G/c\), agreeing with the double-commutator rule.

Thus even the separate multiplier lifts of \(R_i\) and \(R_j\), together with the kinetic jet and vacuum, need not determine the multiplier lift of their product.

At the full operator level, however, this is a presentation freedom. For any finite chronological word on the polynomial-Gaussian core,
\[
\mathcal W=M_{F_1}e^{-t_1K_0}M_{F_2}\cdots
e^{-t_{m-1}K_0}M_{F_m},\qquad t_\ell\ge0,
\]
changing each operator lift by \(\theta h[N,M_{F_\ell}]\) changes the word's first coefficient by \(\theta[N,\mathcal W]\). The insertion sum telescopes because \(N\) commutes with every heat step. Formal skew symmetry and \(N\Omega=0\) give
\[
\langle\Omega,[N,\mathcal W]\Omega\rangle=0.
\]
Every operator used here preserves the polynomial-Gaussian core, so this coefficient identity needs no global exponential. All finite chronological vacuum words are unchanged to first order under the consistent operator comparison.

Consequently contact nonuniqueness alone is not an observable physical ambiguity. It matters when differential operator lifts are replaced by vacuum-equivalent scalar multipliers, or when a source-access algebra is held fixed: equality on the vacuum does not imply equality at intermediate positions in a word. Such a specified source identification can fix the comparison freedom; the kinetic equation alone cannot. No change in the actual Hamiltonian, vacuum or physical gap has been established, and no actual compact operator-comparison theorem for the larger patch is asserted.

## An exact candidate on the five-by-five patch

[[planar-patch-confinement-and-the-spatial-soft-mode|The planar incidence spectrum]] gives
\[
\omega_{rs}
=\sqrt{4-2\cos\frac{r\pi}{L+1}-2\cos\frac{s\pi}{L+1}}.
\]
At \(L=5\),
\[
\omega_{11}=\sqrt3-1,\qquad
\omega_{55}=\sqrt3+1,\qquad
\omega_{rs}=2\quad\text{for }(r,s)\in\mathcal M,
\]
\[
\mathcal M=\{(1,5),(2,4),(3,3),(4,2),(5,1)\}.
\tag{RT12}
\]
These are all the frequency-two modes. The sine basis is
\(v_{rs}(x,y)=\frac13\sin(r\pi x/6)\sin(s\pi y/6)\).
Thus every triple \((11,m,55)\), \(m\in\mathcal M\), satisfies the exact frequency-sum resonance.

For each such ordered triple, compute its three coefficients from the sixty actual comb edge rows:
\[
v_{\ell;jk}
=2\sum_e
(\bar s_{ek}\bar z_{ej\ell}-\bar s_{ej}\bar z_{ek\ell}),
\]
with the cyclic orientation of (RT2). Define
\[
r_m=(\sqrt3-1)v_{11}^{(m)}
+2v_m^{(m)}-(\sqrt3+1)v_{55}^{(m)}.
\]
All sine entries and these raw contractions lie in
\(\mathbb Q(\sqrt3)\), so the test requires only finite exact arithmetic. Here \(abc=4\); the physical matrix element is
\[
-\frac{r_m}{8}\sqrt{\frac{2\mathfrak F_Q}{d}}.
\]
The sum \(\sum_{m\in\mathcal M}r_m^2\) is invariant under orthogonal changes of basis in the degenerate frequency-two space. A positive value proves a nonzero physical resonant block. A zero value clears this selected block only; it does not establish absence of other resonances or a spatially uniform normal form.

If this block is compatible, its null generator has \(p=-16\) and changes the radius-product contact by
\[
16(\sqrt3-1)\,T_G(Y_{11},Y_m,Y_{55})
\]
per unit of the parameter \(\theta\). Compatibility therefore does not restore the four-face uniqueness argument.

The spectrum alone supplies no value for any \(r_m\). Those coefficients must retain the actual edge inventory and connector terms. [[five-by-five-resonance-and-the-source-selection-test|The separate five-by-five evaluation]] owns that exact contraction and its outcome. If a nonzero block is found, the next normal-form equation must retain that block rather than divide by its zero denominator. This is a discriminator of the universal oriented source transport on the selected geometry, not a counterexample to the full Yang–Mills target.

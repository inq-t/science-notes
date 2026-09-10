# A Source-Pairing Inequality That Survives Reconstruction

A uniform reconstruction bound can reach a continuum mass gap without convergence of the reconstruction operators themselves. Its scalar consequence is an inequality between centered, reflected source pairings at two separations. If those pairings converge in one complete source law satisfying the full reconstruction hypotheses, the inequality passes to the physical transfer operator. The essential requirements are the same source norm, the same inherited clock and control of every finite linear combination of local sources.

**Status: exact conditional theorem.** This is a route through converging source evaluations. [[positive-semigroup-decay/total-family-spectral-gap|The total-family theorem]] gives a different route through large-time decay in an already constructed carrier. Neither theorem constructs the required Yang–Mills source law.

## The norm and the translation must belong to one evaluation

Let \(r\) index a proposed continuum and infinite-volume construction. Use a common abstract algebra \(\mathscr S_+\) of renormalized, gauge-invariant polynomial sources, with smearing supported inside the open positive-time half-space. Its realization at regulator \(r\) is included in the notation. Every finite complex linear combination belongs to the algebra. No restriction of continuum fields to a sharp time-zero slice is assumed.

For a normalized source functional \(S_r\), an antilinear reflected adjoint \(\Theta\), and the positive-time translation \(\tau_t\), put
\[
\begin{aligned}
K_r(F,G;t)&=S_r(\Theta F\,\tau_tG),&
m_r(F)&=S_r(F),\\
K_r^c(F,G;t)&=K_r(F,G;t)
 -\overline{m_r(F)}m_r(G).
\end{aligned}
\tag{SL1}
\]
Assume the reflected quotient has a normalized distinguished vacuum \(\Omega_r=[1]_r\) and the actual positive transfer
\[
K_r(F,G;t)=\langle[F]_r,T_r(t)[G]_r\rangle,\qquad
T_r(t)=e^{-tH_r},\qquad H_r\ge0,\qquad H_r\Omega_r=0.
\tag{SL2}
\]
At a lattice regulator, the times used here may be permitted multiples of the transfer step. The parameters \(t,\ell_r\) use one inherited length convention, with \(H_r\) in inverse-length units. Write \(Q_r=I-P_{\Omega_r}\), where the projection subtracts this single vacuum line.

The pairing in (SL1) is the physical reflected pairing, not an independently chosen classical \(L^2\) norm. An actual two-history realization can establish the needed comparison identity. If
\[
J_{0,r},J_{1,r}:\mathcal H_r\longrightarrow\mathcal E_r
\quad\hbox{are isometries},\qquad
J_{0,r}^*J_{1,r}=T_r(\ell_r),
\]
then the innovation
\[
\delta_r=(I-J_{0,r}J_{0,r}^*)J_{1,r}
\quad\hbox{satisfies}\quad
\delta_r^*\delta_r=I-T_r(2\ell_r).
\tag{SL3}
\]
Indeed, multiplying out gives \(I-T_r(\ell_r)^*T_r(\ell_r)\). Positivity and the semigroup law give the displayed result. An arbitrary dilation of an already supplied transfer also gives such isometries; the construction programme must obtain the histories and their physical identification from its source sewing.

[[two-slice-innovation-geometry/oriented-innovation-and-finite-temporal-repair|Oriented innovation]] and [[algebra/os-descent-naturality-and-clock-no-go|OS descent naturality]] state the related realization requirements. A conditional predictor qualifies only after its state carrier and transfer have been identified with (SL2).

## A bounded repair gives a reflected contraction

Suppose the source construction supplies
\[
B_r\delta_r=Q_r-E_r,\qquad
\|B_r\|\le C,\qquad 0<C<\infty,\qquad
\|E_r\|\le\rho<1
\tag{SL4}
\]
on the centered source span, with constants independent of \(r\). For \(x=Q_r[F]_r\),
\[
(1-\rho)\|x\|
\le\|B_r\delta_rx\|
\le C\|\delta_rx\|.
\]
Choose any
\[
0<\kappa<\min\left\{1,\frac{(1-\rho)^2}{C^2}\right\}.
\]
Equations (SL1)–(SL3) now yield
\[
\boxed{
0\le K_r^c(F,F;2\ell_r)
\le(1-\kappa)K_r^c(F,F;0)
\quad\text{for every }F\in\mathscr S_+.}
\tag{SL5}
\]
The lower inequality uses the positive transfer. The upper inequality is the part that excludes soft modes.

The constant may instead come from any independently proved complete-source response bound. [[scale-bearing-descent/phase-and-distinguishability-from-one-kernel|Cyclic comparison]] and [[scale-bearing-descent/constructive-descent-division|constructive repair]] are proposed sources of such a bound. They have to apply to the comparison in (SL3).

## Conditional limit theorem

Assume the following three properties along the same cofinal family of regulator removal and increasing volume.

1. **Convergence of the marked pairings.** For every \(F\in\mathscr S_+\), with \(\ell_r\to\ell>0\),
   \[
   m_r(F)\to m(F),\qquad
   K_r(F,F;0)\to K(F,F;0),\qquad
   K_r(F,F;2\ell_r)\to K(F,F;2\ell).
   \tag{SL6}
   \]
   The renormalized sources, their products, reflection and translated test functions must be controlled in these limits.
2. **Full reconstruction.** A limiting source law supplies these pairings and satisfies an applicable Osterwalder–Schrader reconstruction theorem, including its regularity, covariance and locality requirements. Its reconstructed transfer is \(T(t)=e^{-tH}\), \(H\ge0\), with normalized vacuum \(\Omega\) and \(H\Omega=0\).
3. **Complete source coverage.** The vectors \([F]\), \(F\in\mathscr S_+\), have dense complex linear span in the intended physical vacuum representation.

Then
\[
\boxed{
T(2\ell)\le P_\Omega+(1-\kappa)Q_\Omega,\qquad
H\ge\frac{-\log(1-\kappa)}{2\ell}\,Q_\Omega.}
\tag{SL7}
\]

**Proof.** Pass to the limit in (SL5). Vacuum subtraction in (SL1) becomes
\[
\langle Q_\Omega[F],T(2\ell)Q_\Omega[F]\rangle
\le(1-\kappa)\|Q_\Omega[F]\|^2.
\]
Density extends this quadratic inequality to the whole vacuum complement because \(T(2\ell)\) is bounded. The vacuum is fixed by the transfer. Spectral calculus gives (SL7). \(\square\)

The theorem requires neither convergence of \(B_r\) nor a common realization of their target spaces. It also does not require a separate form-convergence theorem for this argument. Those may be useful construction methods, but their scalar consequence (SL5) is enough for the gap passage.

Subtracting only \(P_\Omega\) has a further consequence: (SL7) excludes any additional zero-energy vector orthogonal to \(\Omega\). Vacuum uniqueness within this representation therefore follows from the estimate. Subtracting the entire ground-space projection would prove a different statement and would leave its dimension unrestricted.

## Why the quantifiers matter

A bound at one fixed time on each member of a Hilbert-total list is insufficient. For example, on a putative \(\mathbb C^2\) vacuum complement, let \(T=\operatorname{diag}(1,\varepsilon)\), \(0<\varepsilon<1\), and adjoin a separate distinguished vacuum line. Each of \(e_1+e_2\) and \(e_1-e_2\) has Rayleigh quotient \((1+\varepsilon)/2<1\), yet their sum has quotient \(1\). This is an actual finite-time positive semigroup with an undetected extra zero-energy direction. Thus (SL5) must hold for the finite linear combinations too. This differs from [[positive-semigroup-decay/total-family-spectral-gap|the large-time theorem]], where positivity of spectral measures and a common asymptotic exponent can control each member separately.

The clock also matters. If \(\ell_r\to0\), \(\kappa\) stays strictly positive, and translated pairings converge continuously to their zero-time values, (SL5) forces every centered limiting norm to vanish. The putative vacuum theory becomes trivial. A viable fixed-step comparison therefore uses \(\ell>0\) in the returned chronology; a shrinking lattice spacing is a different quantity. Variable margins are possible, but require control of the full ratio \(-\log(1-\kappa_r)/(2\ell_r)\) and transport to fixed positive times.

Finally, convergence can erase every nonvacuum source. Nontriviality needs at least one source with \(K^c(F,F;0)>0\), and Yang–Mills identification needs much more: the stipulated gauge-invariant fields and short-distance structure. A nonzero reconstructed vacuum complement together with a strongly continuous transfer has nonempty finite-energy spectral support, so the positive spectral edge is finite.

## The Yang–Mills return is a separate identification theorem

For the [[library/quantum-yang-mills-theory/inq|Clay target]], the limiting local fields must correspond, with the usual renormalization qualifications, to gauge-invariant curvature polynomials and covariant derivatives. Their short-distance behavior, stress tensor and operator products must have the required Yang–Mills correspondence. A positive pairing or a leading \(F^2\) term does not establish that identity.

An applicable reconstruction must return the stipulated local theory on four-dimensional Minkowski space. Positive-energy Poincaré covariance then gives the energy exclusion its invariant-mass meaning. The construction must work for every compact simple group; the constants may depend on the group.

This isolates a precise economy in [[scale-bearing-descent/pointed-comparison-and-the-yang-mills-return|the backwards programme]]: build the whole theory from a stably reconstructible source law, and pass one complete reflected inequality through its return. The difficult existence and identification claims remain, but they no longer require reconstructing a limiting repair operator before the gap can be concluded.

# Source Memory Has a Forced First Chronological Response

The oriented vacuum correction changes an actual mixed exterior-information response, not only a static conditional mean. On the four-face patch, a retained radius and a retained three-face orientation are physical scalar sources. Their mixed exterior response has a strictly positive first coefficient at short scaled durations, although each diagonal response has no linear correction. The coefficient retains the changing vacuum and actual chronology. Its sign does not supply an OI floor: the complete chronological source Gram forms and their normalization remain necessary.

**Status: proved fixed-patch, fixed-group, finite-source chronological first jet and exact short-duration coefficient.** [[all-group-oriented-kinetic-jet-and-source-lift|AJ]] fixes the raw odd operator and its polynomial normal form. [[fixed-group-compact-vacuum-and-oriented-source-return|GV]] and [[regional-conditional-projection-and-the-vacuum-score|VP]] give the actual compact vacuum, source and regional projection estimates. The argument extends [[four-face-optimal-quadratic-response-and-parity|OQ4's finite polynomial evolution proof]] to the specified source family. [[regional-innovation-and-exterior-information-balance|RI]] fixes which exterior response belongs to the original clock.

## Differentiate the actual ground-transformed chronology

Keep GM's faithful weighted cost and fixed compact connected group with simple Lie algebra. The scale is
\[
h=(\kappa/g_{\rm eff})^{1/4},\qquad
E=\sqrt{\kappa g_{\rm eff}},\qquad
K_h=(H-E_{\rm vac})/E.
\]
Let \(P_{t,h}\) be the actual vacuum ground transform of \(e^{-tK_h}\). Time \(t\) is scaled by \(E\). Work in VP's exact common face chart. Write
\[
\Phi_h=\Omega(1+h\alpha)+O_{\rm weighted}(h^2),\qquad
K_h=K_0+hV_1+O(h^2),\qquad
[K_0,S]=-V_1,\quad S\Omega=\alpha\Omega.
\]
On the Gaussian function core define
\[
D=\Omega^{-1}S\Omega-M_\alpha,\qquad D1=0,\qquad
P_t^0=\Omega^{-1}e^{-tK_0}\Omega .
\tag{TM1}
\]
Here conjugation by \(\Omega\) denotes the map from polynomial functions to polynomial-Gaussian vectors. It is not division of an approximate compact vacuum. Formal skewness gives
\[
D^*=-D-2M_\alpha\quad\hbox{in }L^2(\mu_0),\qquad
d\mu_0=\Omega^2dX .
\]
The chronological first jet is
\[
\boxed{\dot P_t=[D,P_t^0].}
\tag{TM2}
\]
Indeed the flat heat jet is \([S,e^{-tK_0}]\). Its ground transform subtracts \(M_\alpha P_t^0\) and adds \(P_t^0M_\alpha\), leaving (TM2).

This is an actual source-vector asymptotic. If a fixed finite family of compact marks has function jets \(f_h=f+hf_1+O(h^2)\), then, for every fixed \(T<\infty\),
\[
\boxed{
\Phi_hP_{t,h}f_h
=\Omega\left[
P_t^0f+h\{\alpha P_t^0f+[D,P_t^0]f+P_t^0f_1\}
\right]+O_T(h^2),\quad 0\le t\le T.}
\tag{TM3}
\]
The error is in the common flat \(L^2\) carrier. The actual source mean and variance are included in \(f_1\) when the source is centered or normalized.

To prove (TM3), solve the first two polynomial-Gaussian evolution equations
\[
\dot v_0=-K_0v_0,\qquad
\dot v_1=-K_0v_1-V_1v_0,\qquad
v_0(0)=\Omega f,\quad
v_1(0)=\Omega(\alpha f+f_1).
\]
Their explicit solution is the displayed pair of coefficients in (TM3). Both curves lie in a fixed finite Hermite-degree space on \([0,T]\). Apply GV's arbitrary-order local operator expansion and cutoff to these curves. Their actual equation residual is \(O_T(h^2)\), including the actual vacuum-energy subtraction, whose first correction vanishes. Duhamel with the exact nonnegative compact \(K_h\) bounds the evolved error by its initial error plus the integral of that residual. VP's weighted vacuum estimate justifies multiplication by every coefficient polynomial before removing the cutoff. This proves (TM3) for each fixed group on the declared four-face patch; it does not exponentiate \(S\) or a truncated differential Hamiltonian.

## The regional exterior jet retains the moving measure

Let \(\mathcal A\) be a fixed set of complete prepared faces, and put
\[
E_{\mathcal A}=\mathbb E_0[\,\cdot\,|X_{\mathcal A}],
\qquad \alpha_{\mathcal A}=E_{\mathcal A}\alpha .
\]
Use \(\mathcal E_{\mathcal A,h}\) for the actual conditional-function map. Its first jet, in the moving vacuum norm, is
\[
\dot{\mathcal E}_{\mathcal A}
=2(E_{\mathcal A}M_\alpha-M_{\alpha_{\mathcal A}}E_{\mathcal A}).
\tag{TM4}
\]
For a regional source define its exterior predictor
\[
\ell_{h,t}(f_h)=(I-\mathcal E_{\mathcal A,h})P_{t,h}f_h,
\qquad
\ell_t(f)=(I-E_{\mathcal A})P_t^0f .
\]
Combining VP's projection derivative with (TM3) gives
\[
\begin{aligned}
\dot\ell_t(f;f_1)
={}&(I-E_{\mathcal A})[D,P_t^0]f
-\dot{\mathcal E}_{\mathcal A}P_t^0f
+(I-E_{\mathcal A})P_t^0f_1,\\
\Phi_h\ell_{h,t}(f_h)
={}&\Omega\{\ell_t(f)+h[\alpha\ell_t(f)+\dot\ell_t(f;f_1)]\}
+O_T(h^2).
\end{aligned}
\tag{TM5}
\]
The amplitude projection derivative and the conditional-function derivative are distinct representations; (TM5) includes both required marginal-score subtractions. It holds on each specified finite polynomial source family, not in global operator norm.

Consequently the complete mixed exterior response
\(\mathcal M_h(t;f,g)=\langle\ell_{h,t}(f_h),\ell_{h,t}(g_h)\rangle_{\mu_h}\)
has derivative
\[
\boxed{\begin{aligned}
\dot{\mathcal M}(t;f,g)
={}&\langle\dot\ell_t(f;f_1),\ell_t(g)\rangle_0
+\langle\ell_t(f),\dot\ell_t(g;g_1)\rangle_0\\
&+2\mathbb E_0[\alpha\,\ell_t(f)\ell_t(g)].
\end{aligned}}
\tag{TM6}
\]
The last term is the changing probability measure. Omitting it changes the coefficient below. For vector-valued boundary marks this formula contracts their common index with \(Q\), but a covariant time correlator would require that boundary transport to be specified. The witness used next consists instead of invariant scalars before evolution and lies directly on RI's physical carrier.

## A physical scalar mixed coefficient is nonzero

Use FC's face ordering \(a,b,c,d\) and let \(C=\sqrt{A_2}\). Retain
\(\mathcal A=\{a,b,c\}\), and choose the scalar compact marks with harmonic labels
\[
f=Q(X_a,X_a)-dC_{aa},\qquad
g=T_G(X_a,X_b,X_c).
\tag{TM7}
\]
The actual marks use \(\widehat X_{p,h}=2q_\rho(P_p)/h\) and actual centering. Their coordinate jets have no order-\(h\) correction. The orientation's first mean can be nonzero, but its centering correction is a constant; exterior predictors and full responses annihilate that constant. The individual variance corrections vanish at first order by parity.

The harmonic measure, heat flow and conditional map preserve simultaneous \(X\mapsto-X\). The score and \(D\) are odd. Thus
\[
\mathcal M_0(t;f,g)=0,\qquad
\dot{\mathcal M}(t;f,f)=\dot{\mathcal M}(t;g,g)=0.
\tag{TM8}
\]
A mixed coefficient between these opposite parities is not excluded.

Here is a short-duration calculation using every original kinetic row. Let
\[
\mathcal L_0=-\partial^{\mathsf T}(C^2\otimes I)\partial
+(CX)\cdot\partial,\qquad P_t^0=e^{-t\mathcal L_0}.
\]
Write \(X_d=m_d+\eta_d\) conditional on \(X_a,X_b,X_c\), with
\[
m_d=-\sum_{p=a,b,c}\frac{(C^{-1})_{dp}}{(C^{-1})_{dd}}X_p,\qquad
\sigma_d=((C^{-1})_{dd})^{-1}.
\]
The exact exterior generator vectors are
\[
\begin{aligned}
A_f&=(I-E_{\mathcal A})\mathcal L_0f
=2C_{ad}Q(X_a,\eta_d),\\
A_g&=(I-E_{\mathcal A})\mathcal L_0g
=Q(W,\eta_d),\\
W&=C_{ad}[X_b,X_c]+C_{bd}[X_c,X_a]+C_{cd}[X_a,X_b].
\end{aligned}
\tag{TM9}
\]
The diffusion contractions in \(\mathcal L_0g\) vanish against the alternating Cartan tensor. The retained mean substitutions give no omitted conditional-covariance term.

The actual first positive ground generator is
\[
\boxed{
\mathcal L_1F
=\Omega^{-1}\{V_1(F\Omega)-F V_1\Omega\}
-2\sum_i\omega_i^2 Q(\nabla_i\alpha,\nabla_iF).}
\tag{TM10}
\]
The last term is the changed vacuum drift. Equivalently \(\mathcal L_1=[D,\mathcal L_0]\). Since
\(\ell_t(f)=-tA_f+O(t^2)\), (TM6) gives
\[
\begin{aligned}
\dot{\mathcal M}(t;f,g)
&=t^2\mathfrak B+O(t^3),\\
\mathfrak B
&=\langle\mathcal L_1f,A_g\rangle_0
+\langle A_f,\mathcal L_1g\rangle_0
+2\langle\alpha A_f,A_g\rangle_0 .
\end{aligned}
\tag{TM11}
\]
The derivative \(\dot{\mathcal E}_{\mathcal A}\) in the function representation maps into the retained range, so its pairing with \(A_f\) or \(A_g\) is zero here. This cancellation does not allow removing the density term; the amplitude projection derivative has a different range decomposition.

The three contributions, divided by \(\mathfrak F_Q=\sum f_{abc}^2\), are

| Contribution | Exact value divided by \(\mathfrak F_Q\) |
| --- | --- |
| \(\langle\mathcal L_1f,A_g\rangle_0\) | \((102-85\sqrt2+32\sqrt3-15\sqrt6)/7\) |
| \(\langle A_f,\mathcal L_1g\rangle_0\) | \((-117+129\sqrt2-93\sqrt3+39\sqrt6)/7\) |
| \(2\langle\alpha A_f,A_g\rangle_0\) | \((291-162\sqrt2+117\sqrt3-108\sqrt6)/7\) |

The exact polynomial calculation is reproducible in [the chronological exterior receipt](receipts/first_chronological_exterior_receipt.py). It imports the audited full raw comb rows, verifies \(\alpha\Omega=-K_0^{-1}V_1\Omega\), and checks each table entry with rational radical arithmetic.

The general-color factor follows before using three-dimensional identities. In the first entry, \(\mathcal L_1f\) and \(A_g\) are Cartan cubics. The second derivative of the radius contracts an alternating tensor with a symmetric color delta and vanishes. In the other two entries every surviving Wick diagram contains exactly two alternating structure tensors. A contraction within one tensor is zero; joining all remaining indices gives \(\pm\mathfrak F_Q\). A disconnected radial trace would contract the two legs of \(A_f\) together, which vanishes because one is retained and the other is the independent centered residual. The subtraction \(V_1(F\Omega)-F V_1\Omega\) removes the disconnected vacuum term. No cross-product completeness relation or higher representation invariant enters this reduction.

Adding the entries proves
\[
\boxed{
\mathcal M_h(t;f,g)
=h\,\dot{\mathcal M}(t;f,g)+O_T(h^2),\qquad
\dot{\mathcal M}(t;f,g)
=\mathfrak F_Q\beta\,t^2+O(t^3),}
\]
\[
\boxed{\beta=\frac{276}{7}-\frac{118\sqrt2}{7}
+8\sqrt3-12\sqrt6>0.}
\tag{TM12}
\]
For example \(\sqrt2<283/200\), \(\sqrt3>433/250\), and \(\sqrt6<49/20\), each certified by squaring, give \(\beta>111/3500\). The sharper value is about \(0.0515009\). The duration expansion is taken in the proved first \(h\)-coefficient; no uniform joint small-\(h\), small-\(t\) quotient is claimed.

Dividing by the actual source standard deviations gives the same statement with leading divisor
\[
\sigma_f\sigma_g
=\sqrt{2d}\,C_{aa}\sqrt{\mathfrak F_Q\det C_{\mathcal A\mathcal A}}.
\]
Actual centering does not remove (TM12).

## The full RI numerator still has to be retained

For these retained sources set
\[
r_{h,t}f_h=f_h-\mathcal E_{\mathcal A,h}P_{2t,h}f_h .
\]
RI gives the exact mixed forms
\[
\begin{aligned}
\mathcal G_h(t;f,g)&=\langle f_h,r_{h,t}g_h\rangle_{\mu_h},\\
\mathcal N_h(t;f,g)&=\langle r_{h,t}f_h,r_{h,t}g_h\rangle_{\mu_h}
+\mathcal M_h(2t;f,g).
\end{aligned}
\tag{TM13}
\]
Their first jets retain both the changed regional response and the changed measure. For fixed function labels,
\[
\dot r_t f=-\dot{\mathcal E}_{\mathcal A}P_{2t}^0f
-E_{\mathcal A}[D,P_{2t}^0]f.
\]
Differentiate each inner product in (TM13) by the same rule as (TM6). Moving source jets contribute their ordinary linear terms. The positive mixed coefficient (TM12) is only one entry of this complete ledger; a symmetric first-order block with zero diagonal and nonzero off-diagonal is itself indefinite.

There is also a direct finite-exponential route to the full chronological calculation. For the harmonic-centered labels in (TM7), define the actual centered covariance
\(\mathcal C_h(s;f,g)=\langle f_h,P_{s,h}g_h\rangle_{\mu_h}\).
Formal skewness and (TM3) give
\[
\boxed{
\dot{\mathcal C}(s;f,g)
=-\langle Df,P_s^0g\rangle_0
-\langle P_s^0f,Dg\rangle_0 .}
\tag{TM14}
\]
The constant centering jets contribute zero. Both pairings have finite Hermite expansions. Hence
\[
\dot{\mathcal G}(t)=\dot{\mathcal C}(0)-\dot{\mathcal C}(2t),\qquad
\dot{\mathcal N}(t)=\dot{\mathcal C}(0)-2\dot{\mathcal C}(2t)
+\dot{\mathcal C}(4t).
\tag{TM15}
\]
[[radius-orientation-chronological-gram-and-the-source-pencil|The complete Gram calculation]] evaluates these finite sums as nine explicit exponentials and proves that the mixed coefficient changes sign with duration. [[radius-orientation-source-extension-and-the-innovation-floor|The source-extension comparison]] then retains \(\mathcal G_h\), both diagonal harmonic forms and actual centering. For short fixed duration the optimized two-source quotient is strictly lower than the actual radius-only quotient by \(h^2\Gamma(t)+o_t(h^2)\), with \(\Gamma(t)>0\). Comparing against that actual baseline cancels its unknown absolute second-order shift; the eigenvalues of the exterior matrix alone would not supply this result.

The [[covariant-boundary-source-and-the-oriented-return|static boundary return]] and the [[regional-vacuum-score-and-the-three-face-orientation|three-face score]] now have a nonzero response under the actual chronology. This proves no strict OI floor. All constants here are for a fixed patch, group and bounded interval of scaled duration. At fixed physical duration the scaled time grows with \(E\), outside the stated uniformity. Spatial assembly must also retain [[spatial-block-sewing-and-the-vacuum-cap-response|SB's vacuum caps, source exchange and changed-history lag]]. A static Gaussian translation or a positive conditional variance is not a replacement clock or a complete finite-strength joint law.

# A Gauge-Star State Does Not Determine Its Hidden Clock

A shared Haar reference realizes the exact finite star amplitude for arbitrary positive face profiles. Pulling back a specified product diffusion gives a closed response on the boundary, but the original diffusion descends to that full boundary carrier only when all profiles are constant. A Wilson-profile example on \(SU(2)\) has the same entire boundary state and reconstructed clock for every profile strength; varying the hidden source-rate split can drive its actual visible spectral edge to zero while keeping that returned clock fixed. The missing datum is the hidden dynamical return, not another normalization of the instantaneous response.

**Status: exact compact-group construction and spectral counterexample.** The general compression and memory mechanism belongs to [[inq|coarse response memory]] and [[spectral-readout-and-the-visible-gap|spectral readout]]. The source diffusion below is a declared input, not the physical Yang--Mills transfer operator or the original Wilson link dynamics.

## The actual star and a specified source

Let \(G\) be compact, connected, with normalized Haar measure and a fixed bi-invariant metric \(Q\). Let \(p_i>0\), \(1\le i\le m\), be smooth normalized densities. On
\[
\mathcal S=G^{m+1},\qquad
d\rho(v,h)=\prod_{i=1}^m p_i(v_i)\,dv_i\,dh,
\]
define the readout and its state by
\[
\pi(v,h)_i=v_i h^{-1}=g_i,\qquad
A(g)=\int_G\prod_i p_i(g_i h)\,dh,\qquad
d\mu(g)=A(g)\prod_i dg_i.
\tag{GS1}
\]
Changing variables \(v_i=g_i h\) proves the pushforward identity and the actual conditional law
\[
d\nu_g(h)=A(g)^{-1}\prod_i p_i(g_i h)\,dh.
\tag{GS2}
\]
Replacing \(h\) by \(u^{-1}\) identifies (GS1) with the normalized [[holonomy-state-refinement/overlap-kernels-and-face-refinement#The exact response of a coincident boundary star|shared-edge star integral]]. For unnormalized weights \(w_i\), its normalizer is \(\prod_i\int w_i\). This is a static identity. A based heat reference at finite time has an extra heat density in (GS1) and is a different framed state.

The carrier here is the **full framed boundary** \(L^2(G^m,\mu)\). If all profiles are central, simultaneous conjugation is a symmetry and its invariant subspace is also available. Separate invariance in every factor would discard boundary charge pairings. General noncentral profiles require transforming their backgrounds before asserting gauge covariance.

For a \(Q\)-orthonormal basis \(T_a\), fix derivative conventions
\[
D^L_a f(g)=\left.\frac{d}{ds}f(e^{sT_a}g)\right|_0,\qquad
D^R_a f(g)=\left.\frac{d}{ds}f(ge^{sT_a})\right|_0,\qquad
\Delta=\sum_a(D^L_a)^2=\sum_a(D^R_a)^2.
\]
The superscripts label the side of multiplication. Set \(b_i=D^L\log p_i\). Choose positive rates \(a_0,\ldots,a_m\), and the nonpositive reversible source generator
\[
\mathcal L_{\mathrm{src}}
=\sum_i a_i\bigl(\Delta_{v_i}+b_i(v_i)\cdot D^L_{v_i}\bigr)
+a_0\Delta_h,\qquad K=-\mathcal L_{\mathrm{src}}\ge0.
\tag{GS3}
\]
Its closed form is the sum of these weighted gradient energies on \(H^1(\mathcal S,\rho)\). Compactness, smooth strict positivity and positive rates give the usual elliptic realization with smooth core. No stochastic ontology is assumed by using this reversible diffusion as a mathematical source.

An isolated Wilson-profile star is included by choosing its actual profiles. An entire Wilson lattice has additional ordered staple maps and exterior correlations: [[rg-covariance-residue/su2-staple-elimination-and-response|actual link elimination]] retains them. Equality of a marginal density does not identify (GS3) with that lattice's dynamics.

## The returned form and the clock that is rebuilt from it

Let \(Jf=f\circ\pi\), \(P=JJ^*\), and \(\mathcal R=L^2(G^m,\mu)\). The source derivatives give exactly
\[
\mathcal E_{\mathrm{ret}}(f)
=\mathcal E_{\mathrm{src}}(Jf)
=\int A(g)\left[
\sum_i a_i|D_i^Lf|^2+
a_0\left|\sum_iD_i^Rf\right|^2
\right]dg.
\tag{GS4}
\]
There is no factor two with convention (GS3). The shared reference supplies mixed derivatives, as in [[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|the theta-loop clock]], rather than an independent clock for every branch.

Since the leaf part is uniformly elliptic and \(A\) is smooth and strictly positive, (GS4) has closed domain \(H^1(G^m,\mu)\). On smooth functions its reconstructed nonpositive generator is
\[
\mathcal L_{\mathrm{ret}}
=\sum_i a_i\left[\Delta_i+
(D_i^L\log A)\cdot D_i^L\right]
+a_0\sum_a\left(\sum_iD^R_{i,a}\right)^2.
\tag{GS5}
\]
Indeed \(A(g_1k,\ldots,g_mk)=A(g)\), so the common-right row has no density drift. Differentiating (GS1) gives
\[
D_i^L\log A(g)=\mathbb E_{\nu_g}b_i(g_i h).
\tag{GS6}
\]
Equations (GS4)--(GS6) construct a boundary semigroup from the pulled-back form. They do **not** prove that it equals the actual compression
\[
C_t=J^*e^{-tK}J.
\tag{GS7}
\]

## When the source clock really descends

On the full framed carrier, with all \(a_i>0\),
\[
\boxed{\operatorname{Ran}J\text{ reduces }K
\quad\Longleftrightarrow\quad p_i=1\text{ for every }i.}
\tag{GS8}
\]
For a smooth \(f\), the source action is the basic second-order expression in (GS5), but with \(D_i^L\log A\) replaced by the hidden score \(b_i(g_i h)\). If the subspace reduces, apply this identity to \(f\) depending on \(g_i\) alone. Its first derivative at any chosen \(g_i\) is arbitrary. Basicness forces every component of \(b_i(g_i h)\) to be independent of \(h\). Strictly positive conditional density and smoothness promote the almost-everywhere identity to an everywhere identity. Hence \(b_i\) is a constant vector on \(G\).

For each component, Haar integration gives
\(\int D^L_a\log p_i\,dv_i=0\), so that constant is zero. Connectedness and normalization imply \(p_i=1\). Conversely, with every profile constant the product Laplacians preserve basic functions, giving the intertwined heat semigroup.

This is not an impossibility theorem for gauge reduction, nor an automatic characterization on a smaller relative or gauge-neutral subcarrier. It concerns the specified source, response and full readout together.

The obstruction is quantitative. For smooth real \(f\), define
\[
B_f(g,h)=\sum_i a_i b_i(g_i h)\cdot D_i^Lf(g),\qquad
\mathfrak m_g(df,df)=\operatorname{Var}_{\nu_g}B_f(g,\cdot).
\tag{GS9}
\]
Then
\[
\boxed{
\lim_{t\downarrow0}
\frac{\langle f,(C_{2t}-C_t^2)f\rangle_\mu}{t^2}
=\|(I-P)KJf\|_\rho^2
=\int\mathfrak m_g(df,df)\,d\mu(g).}
\tag{GS10}
\]
The [[trace-dirichlet-descent/standard-form-pullback-and-reducing-wall#The operations that must not be conflated|exact bounded compression identity]] writes the numerator as
\(\|(I-P)e^{-tK}Jf\|^2\). Since \(Jf\in D(K)\), divide its vector by \(t\) and use strong differentiation. Subtracting the conditional mean in (GS6) leaves precisely (GS9). No boundedness of the whole generator or unverified block-domain decomposition is needed. Complex readouts use the corresponding Hermitian covariance.

For nonconstant profiles, the operator \(C_{2t}-C_t^2\) is nonzero for every \(t>0\). Otherwise \(\operatorname{Ran}J\) would reduce \(e^{-tK}\); the injective spectral function \(\lambda\mapsto e^{-t\lambda}\) then implies reduction of \(K\), contradicting (GS8). This does not claim one fixed test vector detects every duration.

## One Wilson profile: identical boundary clock, different spectral edge

Take \(m=1\). Whatever the positive normalized profile \(p\),
\[
A(x)=1,\qquad
\mathcal E_{\mathrm{ret}}=(a_0+a_1)\mathcal E_{\mathrm{Haar}},
\qquad
K_{\mathrm{ret}}=-(a_0+a_1)\Delta.
\tag{GS11}
\]
Thus the **entire** returned state and form, not just one moment or marginal, are independent of \(p\). Conditional on \(x\), the variable \(v=xh\) still has law \(p(v)\,dv\). Haar integration of \(D^Lp\) makes its mean score zero, and (GS10) becomes
\[
\int\mathfrak m_x(df,df)\,dx
=a_1^2\int (D^Lf)^\top\mathsf F_p(D^Lf)\,dx,\qquad
\mathsf F_p=\int b(v)b(v)^\top p(v)\,dv.
\tag{GS12}
\]

Use \(G=SU(2)\), \(Q=-2\operatorname{Tr}\), \(T_a=-i\sigma_a/2\), and
\[
v=v_0I+i\mathbf v\cdot\sigma,\qquad
p_\beta(v)=Z_\beta^{-1}e^{\beta v_0},\qquad
Z_\beta=\frac{2I_1(\beta)}{\beta},\qquad \beta>0.
\]
This is the single Wilson profile in [[rg-covariance-residue/su2-staple-elimination-and-response|the staple normalization]], but the present metric is four times the unit round metric. Put
\[
b(\beta)=\mathbb E_{p_\beta}v_0=\frac{I_2(\beta)}{I_1(\beta)},
\qquad c=\frac34,\qquad f(x)=\chi_{1/2}(x)=\operatorname{Tr}x.
\]
Here \(\|f\|_{\mathrm{Haar}}=1\), its mean is zero, and \(-\Delta f=cf\).
It is a conjugation-invariant framed probe, not an invariant under two
independently acting boundary endpoints. For \(m=1\), that further
left-right quotient has only constants; nontrivial framed probes must
instead be retained or paired with exterior boundary data.
The score has components \(\beta v_a/2\). Rotational symmetry and the latitude integration identity give
\[
\mathsf F_{p_\beta}
=\frac{\beta b(\beta)}4 I_3,\qquad
\int\mathfrak m_x(df,df)\,dx
=\frac{3a_1^2\beta b(\beta)}{16}>0.
\tag{GS13}
\]

There is also an exact all-time spectral conclusion, without diagonalizing the tilted diffusion. Write \(K_v\) for its nonnegative unit-rate generator. The actual lifted character is
\[
Jf(v,h)=2\sum_{\mu=0}^3v_\mu h_\mu.
\tag{GS14}
\]
Every \(h_\mu\) belongs to the Haar eigenspace with eigenvalue \(c\). The projection of (GS14) onto functions constant in \(v\) is
\[
b(\beta)\chi_{1/2}(h^{-1}),
\]
of squared norm \(b(\beta)^2\). It is an eigenvector of the whole generator at \(a_0c\). On the remainder, the positive first eigenvalue \(\lambda_\beta\) of \(K_v\) gives
\[
\begin{split}
r_\beta(t)&:=\langle f,C_tf\rangle
=e^{-a_0ct}\bigl[b(\beta)^2+s_\beta(t)\bigr],\\
0&\le s_\beta(t)\le
(1-b(\beta)^2)e^{-a_1\lambda_\beta t}.
\end{split}
\tag{GS15}
\]
Positivity of \(s_\beta\) follows from the nonnegative spectral measure, not a pointwise assertion about matrix entries. Hence the visible character measure has an atom of weight \(b(\beta)^2\) at \(a_0c\), and its threshold is exactly \(a_0c\).

This is also the edge visible from the **whole centered output carrier**. For every mean-zero \(f\), \(\int_h f(vh^{-1})\,dh=0\) at each \(v\). Thus \(Jf\) lies in the nonconstant \(h\) sector, on which \(K\ge a_0c\); (GS14) attains that visible edge when \(\beta>0\).

In contrast, at \(\beta=0\) both factors are Haar and (GS8) gives the autonomous output clock with edge \((a_0+a_1)c\). For every \(\beta\ge0\) the first character moment nevertheless equals
\[
\langle Jf,KJf\rangle=(a_0+a_1)c.
\tag{GS16}
\]
Fix any \(\beta>0\), set \(a_0=\varepsilon\), \(a_1=1-\varepsilon\), \(0<\varepsilon<1\). The output state, full returned form and rebuilt clock stay fixed; the actual visible edge is \(\varepsilon c\to0\), with fixed nonzero weight \(b(\beta)^2\). There is no uniform actual gap inferable from the fixed returned form.

This is the compact-group, actual-profile counterpart of [[inq#A fast instantaneous rate with a slow observable tail|the three-state slow-tail example]]. It identifies a necessary datum for a whole-to-local construction; it does not attribute these auxiliary rates to physical energy.

## The slow return survives endpoint-neutral pairing

For two central profiles, the endpoint action on the star is
\((g_1,g_2)\mapsto(kg_1\ell^{-1},kg_2\ell^{-1})\). Its full invariant
algebra consists of class functions of
\[
x=g_1g_2^{-1}=v_1v_2^{-1}.
\]
This is a relative loop, not a separately neutralized factor. Its state
and returned form are
\[
q(x)=\int p_1(xv)p_2(v)\,dv,\qquad
\mathcal E_{\mathrm{rel}}(f)
=(a_1+a_2)\int_G|\nabla f|_Q^2q\,dx
\quad(f\text{ a class function}).
\tag{GS16a}
\]
The reference \(h\) cancels identically. The two leaf gradients are
related by bi-invariant isometries, so their pointwise squared norms
agree. Equation (GS16a) therefore specifies the entire returned form,
with domain \(H^1(G,q)^{\operatorname{Ad}G}\), independently of the rate
split. The endpoint action lifts to
\(v_i\mapsto kv_i k^{-1}\), \(h\mapsto\ell hk^{-1}\); central profiles
make this a symmetry of the source state and evolution. The invariant
source carrier is larger than the relative readout: it also contains
class functions of an individual hidden leaf. Its preservation does
not imply preservation of the smaller relative-readout subspace.

Take fixed \(SU(2)\) Wilson profiles with \(\beta_1,\beta_2>0\), and
write \(b_i=b(\beta_i)\), \(b_1'=db/d\beta|_{\beta_1}>0\).
For the centered relative character
\[
f(x)=\chi_{1/2}(x)-2b_1b_2,
\]
project \(Jf\) onto functions constant in \(v_2\). The resulting vector
on the first leaf is
\[
g(v_1)=b_2(\chi_{1/2}(v_1)-2b_1),\qquad
W:=\|g\|_{p_1}^2=4b_2^2 b_1'>0.
\tag{GS16b}
\]
This is a genuine orthogonal projection under the product source
state, not a new boundary preparation. With \(K_1\) the unit-rate
weighted first-leaf generator, its energy is
\[
M:=\langle g,K_1g\rangle_{p_1}
=\frac{3b_2^2b_1}{\beta_1},\qquad
R:=\frac{2M}{W}
=\frac{3b_1}{2\beta_1b_1'}.
\tag{GS16c}
\]
Indeed \(|\nabla\chi_{1/2}|_Q^2=1-v_{1,0}^2\),
\(\mathbb E_{p_1}(1-v_{1,0}^2)=3b_1/\beta_1\), and
\(\operatorname{Var}_{p_1}(v_{1,0})=b_1'\).

The spectral measure of \(g\) for \(K_1\) has no zero atom and total
weight \(W\). Its first moment \(M\) implies that at least \(W/2\)
lies in \((0,R]\). Set \(a_1=\varepsilon\),
\(a_2=1-\varepsilon\), \(0<\varepsilon<1\). The sector constant in
\(v_2\) and \(h\) reduces the source generator and carries
\(\varepsilon K_1\). Orthogonality of its spectral contribution gives
\[
\boxed{
\langle Jf,E_K((0,\varepsilon R])Jf\rangle\ge W/2,\qquad
\langle f,C_tf\rangle_q\ge(W/2)e^{-\varepsilon Rt}
\quad(t\ge0).}
\tag{GS16d}
\]
Here \(C_t\) is the compression for this relative readout. Normalizing
\(f\) divides both lower weights by its fixed nonzero \(q\)-norm
squared.

Thus the visible edge is at most \(\varepsilon R\), with a fixed
positive amount of weight in a shrinking low-energy interval, while
the whole endpoint-neutral state and rebuilt response remain fixed.
No eigenvalue of the tilted diffusion has been guessed or fitted.
At each positive \(\varepsilon\), compact ellipticity still gives the
source a unique constant vacuum and a positive gap. The failure is
uniformity in this family, not an accidental extra zero mode.

This strengthens (GS16): the missing dynamical data remain missing
after genuine boundary charge pairing. It is still a declared finite
source family, not the original Wilson lattice transfer law.


## The same conditional tensor has two different roles at coincidence

Return to \(m\ge2\), equal profiles \(p_i\propto w\), and equal leaf rates \(a_i=a\). At \(g=(e,\ldots,e)\), put
\[
d\nu\propto w(h)^m\,dh,\qquad
C(u,v)=\mathbb E_\nu[(D_u^L\log w)(D_v^L\log w)].
\]
The score mean is zero by Haar integration by parts. If \(v_i\) are tangent vectors and \(v^\flat\) their covectors under the supplied product metric \(Q\), then
\[
\mathfrak m_e(v^\flat,v^\flat)
=a^2 C\!\left(\sum_i v_i,\sum_i v_i\right).
\tag{GS17}
\]
Combining this with the already proved coincident-star Hessian yields
\[
\boxed{
\operatorname{Hess}_e(-\log A)(v,v)
+a^{-2}\mathfrak m_e(v^\flat,v^\flat)
=m\sum_i C(v_i,v_i).}
\tag{GS18}
\]
Static relative-boundary curvature and hidden common-direction return are complementary contractions of one actual conditional tensor. This is a precise joint relation, but it uses the declared source dynamics and the metric identification of covectors with vectors; a Hessian and a memory cometric are not the same type of object.

Equation (GS18) is pointwise at coincidence. It is neither a global convexity estimate nor the integrated coefficient (GS10). For semisimple \(G\), a smooth simultaneously-conjugation-invariant scalar has zero first derivative at this coincident tuple. Nonzero jets in (GS17) are therefore framed or charged data, not a nonzero neutral scalar response there. The full boundary carrier matters.

## What a spatial construction must retain next

This calculation replaces a heat-profile analogy by the specified finite star state and an exact hidden-response test. It also exposes its remaining supplied choices: face profiles, group metric and source mobilities. It does not select a physical clock.

The next compositional test is two overlapping stars with their actual exterior joint law. After the first integration, transport the induced cross-response and spectral return into the second reduction. Resetting to independent profile diffusions would require a new justification; matching the new static integral is insufficient. Alternatively, retain [[spectral-readout-and-the-visible-gap|the compatible spectral readout]] without demanding that every partial boundary have its own autonomous clock.

[[receipts/gauge_star_memory_receipt.py|The quaternion receipt]] checks the actual source readout, generator moments, hidden score covariance and fixed-response slow-tail families, including the fully endpoint-neutral relative character. Its finite integrations support the formulas; (GS8), (GS10), (GS15) and the spectral-weight bound (GS16d) have the analytic proofs above. No four-dimensional reconstruction or physical mass gap is asserted.

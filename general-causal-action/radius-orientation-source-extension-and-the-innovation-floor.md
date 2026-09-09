# Radius–Orientation Extension Lowers the Actual Source Quotient

The orientation source has a strictly larger harmonic innovation quotient than the radius source at every positive duration. Nevertheless their forced first nonlinear mixing lowers the optimal two-source quotient relative to the actual radius-only value. The subtraction retains the changing innovation denominator and does not require the unknown second-order radius correction: that correction cancels in this relative comparison. The lowering is strictly nonzero at sufficiently short fixed scaled durations.

**Status: proved fixed-group, fixed-four-face source-extension coefficient.** [[covariant-source-memory-and-the-first-chronological-response|TM]] supplies actual centered source and chronological first jets. [[radius-orientation-chronological-gram-and-the-source-pencil|The complete mixed Gram calculation]] evaluates their finite exponential coefficients from the actual kinetic rows. [[four-face-oriented-source-extension-and-the-schur-surplus|OE]] gives the generalized-pencil interpretation. No Hamiltonian, clock or regional preparation is changed.

## The two harmonic diagonal forms are explicit

Keep the positive invariant metric \(Q\), \(d=\dim\mathfrak g\), and
\(\mathfrak F=\sum f_{\alpha\beta\gamma}^2>0\) for the fixed compact simple Lie algebra. On the inherited four-face vacuum set
\[
f=Q(X_a,X_a)-dC_{aa},\qquad
g=T_G(X_a,X_b,X_c),\qquad C=\sqrt{A_2}.
\tag{RO1}
\]
The actual compact marks use GM's \(\widehat X_{p,h}=2q_\rho(P_p)/h\) and actual vacuum centering. Their scalar physical indices are already closed in the common prepared frame.

Write \(a=\sqrt2\), \(b=\sqrt6\) for the two distinct endpoint frequencies; here these italic letters are numbers, not face labels. The normal frequencies are \((a,2,2,b)\), and \(X_a=(Y_0+Y_1+Y_2+Y_3)/2\). Gaussian contraction gives
\[
\boxed{
\begin{aligned}
C_f(s)&=\langle f,P_s^0f\rangle_0
=\frac d8\bigl(ae^{-as}+4e^{-2s}+be^{-bs}\bigr)^2,\\
C_g(s)&=\langle g,P_s^0g\rangle_0
=\mathfrak F\bigl[
ae^{-(a+4)s}+2\sqrt3\,e^{-(a+b+2)s}
+be^{-(b+4)s}\bigr].
\end{aligned}}
\tag{RO2}
\]
Indeed
\[
g=\tfrac12(T_{012}+T_{013}-T_{023}-T_{123}),
\qquad
\|T_{ijk}\|_0^2=\mathfrak F\omega_i\omega_j\omega_k.
\]
These four Cartan chaoses are orthogonal. The radius covariance is the Wick square of its one-color linear covariance. Opposite parity makes the harmonic mixed covariance zero.

For \(r_\lambda(t)=1-e^{-2t\lambda}\), define the complete chronological forms
\[
D_f=C_f(0)-C_f(2t),\qquad
N_f=C_f(0)-2C_f(2t)+C_f(4t),
\tag{RO3}
\]
and the analogous \(D_g,N_g\). Equivalently each denominator is
\(\sum_\lambda w_\lambda r_\lambda\), and each numerator is
\(\sum_\lambda w_\lambda r_\lambda^2\), with the following positive weights:

| Radius energy \(\lambda\) | \(w_\lambda/d\) |
| --- | --- |
| \(2a\) | \(1/4\) |
| \(a+2\) | \(a\) |
| \(a+b\) | \(\sqrt3/2\) |
| \(4\) | \(2\) |
| \(b+2\) | \(b\) |
| \(2b\) | \(3/4\) |

| Orientation energy \(\lambda\) | \(w_\lambda/\mathfrak F\) |
| --- | --- |
| \(a+4\) | \(a\) |
| \(a+b+2\) | \(2\sqrt3\) |
| \(b+4\) | \(b\) |

Each quotient is an innovation-weighted average of \(r_\lambda\). Since
\(2\sqrt6<4+\sqrt2\), the entire radius support lies below the entire orientation support. Consequently
\[
\boxed{
q_f(t):=\frac{N_f}{D_f}
\le r_{2b}(t)<r_{a+4}(t)
\le\frac{N_g}{D_g}=:q_g(t),\qquad t>0.}
\tag{RO4}
\]
There are no harmonic quotient crossings. The two-source harmonic minimum is the radius line, with a positive complementary pencil block at every fixed positive duration.

## Retain the actual denominator when adjoining the orientation

For the actual centered compact sources \(f_h,g_h\), put
\[
\mathcal C_{uv,h}(s)=\langle f_{u,h},P_{s,h}f_{v,h}\rangle_{\mu_h},
\quad
D_h=\mathcal C_h(0)-\mathcal C_h(2t),\quad
N_h=\mathcal C_h(0)-2\mathcal C_h(2t)+\mathcal C_h(4t).
\tag{RO5}
\]
Here \(u,v\in\{f,g\}\). These are the full physical innovation forms, not the regional compression alone. Simultaneous source rescaling changes both matrices and leaves the generalized roots unchanged.

TM's actual first jets and parity imply, for each fixed \(t>0\),
\[
D_{ff,h}=D_f+O_t(h^2),\quad
N_{ff,h}=N_f+O_t(h^2),
\]
\[
D_{gg,h}=D_g+O_t(h^2),\quad
N_{gg,h}=N_g+O_t(h^2),\qquad
D_{fg,h}=h\,d_1(t)+O_t(h^2),\quad
N_{fg,h}=h\,n_1(t)+O_t(h^2).
\tag{RO6}
\]
Let \(M_1(s)=\partial_h\mathcal C_{fg,h}(s)|_0\), evaluated in the linked mixed Gram calculation. The two different temporal combinations are
\[
d_1=M_1(0)-M_1(2t),\qquad
n_1=M_1(0)-2M_1(2t)+M_1(4t),
\]
\[
\boxed{c(t)=n_1(t)-q_f(t)d_1(t).}
\tag{RO7}
\]
Replacing \(c\) by \(n_1\) would discard the changing denominator.

Write
\[
q_f(h;t)=\frac{N_{ff,h}}{D_{ff,h}},\qquad
q_{\rm pair}(h;t)=
\min_{(u,v)\ne0}
\frac{(u,v)N_h(u,v)^{\mathsf T}}
     {(u,v)D_h(u,v)^{\mathsf T}} .
\]
The actual denominator stays positive definite by its harmonic limit. Eliminating the orientation block at the actual radius-only root gives
\[
\boxed{
q_{\rm pair}(h;t)-q_f(h;t)
=-h^2\Gamma(t)+o_t(h^2),\qquad
\Gamma(t)=
\frac{c(t)^2}{D_f(t)D_g(t)[q_g(t)-q_f(t)]}\ge0.}
\tag{RO8}
\]
To verify the normalization, the radius entry of \(N_h-\lambda D_h\) is exactly
\(D_{ff,h}[q_f(h;t)-\lambda]\). At that root the mixed entry is
\(hc(t)+O_t(h^2)\), and the orientation entry tends to
\(D_g(q_g-q_f)>0\). Its Schur subtraction is therefore
\(h^2c^2/[D_g(q_g-q_f)]+o_t(h^2)\); dividing by the radius threshold derivative \(D_f\) proves RO8.

No second-order diagonal coefficient is needed for this difference. An absolute comparison with the harmonic value \(q_f(t)\) would still need the actual second-order radius response. Fixing the radius coefficient to one, the optimizing combination is
\[
f_h-h\,\frac{c(t)}{D_g(t)[q_g(t)-q_f(t)]}\,g_h+o_t(h).
\tag{RO9}
\]
This is a source change inside the same compact theory. The factor \(h\) reflects the different scaling of the quadratic and cubic physical marks.

## The subtraction is strictly nonzero at short durations

Let \(A_j\) be the \(j\)-th spectral moment of \(C_f/d\), and \(B_j\) that of \(C_g/\mathfrak F\). RO2 gives
\[
\begin{aligned}
A_1&=16+4\sqrt2+4\sqrt6,&
A_2&=90+6\sqrt2+4\sqrt3+10\sqrt6,\\
B_1&=8+10\sqrt2+4\sqrt3+6\sqrt6,&
B_2&=88+42\sqrt2+24\sqrt3+30\sqrt6 .
\end{aligned}
\tag{RO10}
\]
The exact mixed calculation supplies
\[
m_1=-\frac{M_1'(0)}{\mathfrak F}
=\frac{78}{7}+\frac{12\sqrt2}{7}-7\sqrt3,
\]
\[
m_2=\frac{M_1''(0)}{\mathfrak F}
=\frac{400}{7}-\frac{319\sqrt2}{14}
-\frac{38\sqrt3}{7}-\frac{51\sqrt6}{14}.
\]
Put
\[
\eta=m_2-\frac{A_2}{A_1}m_1,\qquad
\Delta=\frac{B_2}{B_1}-\frac{A_2}{A_1}>0 .
\]
The positivity of \(\Delta\) follows already from the separated energy supports. Exact radical simplification yields
\[
\boxed{
A_1\eta=
\frac27(-1032-743\sqrt2+885\sqrt3+253\sqrt6)>0.}
\tag{RO11}
\]
For example, \(\sqrt2<283/200\), \(\sqrt3>433/250\), and
\(\sqrt6>2449/1000\), each certified by squaring, make the parenthesis greater than \(69\).

Expanding the finite exponentials now gives
\[
c(t)=4\mathfrak F\eta\,t^2+O(t^3),\qquad
D_f=2dA_1t+O(t^2),\quad
D_g=2\mathfrak F B_1t+O(t^2),\quad
q_g-q_f=2\Delta t+O(t^2).
\]
Hence
\[
\boxed{
\Gamma(t)=
\frac{2\mathfrak F}{d}\,
\frac{\eta^2}{A_1B_1\Delta}\,t+O(t^2)>0
\quad\hbox{for sufficiently small }t>0.}
\tag{RO12}
\]
The strict source-extension lowering therefore survives actual centering and normalization. More generally RO8 is explicit at every fixed positive duration through the finite exponential \(M_1\). The function \(c(t)\) is real analytic and is not identically zero, so any zeros inside \((0,\infty)\) are isolated; no assertion that there are no such zeros is required here.

These are sequential asymptotics: first extract the actual \(h^2\) relative coefficient at fixed \(t>0\), then examine that coefficient as \(t\downarrow0\). They supply no uniform joint \(h,t\) remainder, fixed-physical-time limit, full-source floor or physical-gap shift. The positive exterior entry from TM becomes only one component of this complete source pencil. Its extension lowers the radius-only quotient even though the added source is harmonically faster. Spatial sewing still has to retain [[regional-innovation-and-exterior-information-balance|RI's exterior term]] and [[spatial-block-sewing-and-the-vacuum-cap-response|SB's vacuum caps, source exchange and changed-history lag]].

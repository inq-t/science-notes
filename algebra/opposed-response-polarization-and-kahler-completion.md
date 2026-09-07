# Opposed Response Polarization and Kähler Completion

Two nonlinear positive response graphs admit a joint symplectic carrier, but their separately supplied Hessian metrics are generally incompatible with that pairing. Polar normalization repairs the mismatch through the matrix geometric mean of the two Hessians. A different, constant exchange prescription instead gives an integrable Kähler structure with their arithmetic mean. For convex quartic responses, that exchange geometry has an explicit circle action whose moment function supplies a compatible complete nonlinear clock. The positive pairing and clock normalization remain declared choices, not consequences of complexification alone.

## A nonlinear pair chart

Let \(W\in C^4(\mathbb R^n;\mathbb R)\) have everywhere positive-definite Hessian, and use the supplied Euclidean metric to define \(N=\nabla W\). At a pair \((x,y)\), write

\[
P=\operatorname{Hess}W(x),\qquad
M=\operatorname{Hess}W(y),\qquad C=P+M.
\tag{OP1}
\]

The sum of points on the opposed exact Lagrangian graphs defines

\[
F(x,y)=(q,p)=(x+y,N(x)-N(y)),\qquad
DF=\begin{pmatrix}I&I\\P&-M\end{pmatrix}.
\tag{OP2}
\]

Since \(C>0\), this is a local diffeomorphism. It is globally injective: for fixed \(q\), the map \(x\mapsto N(x)-N(q-x)\) has positive-definite derivative and is strictly monotone. Thus \(F\) is a diffeomorphism onto its open image. It need not cover every \((q,p)\); in one dimension \(W(v)=\sqrt{1+v^2}\) bounds the image of \(p\). If \(\operatorname{Hess}W\geq mI\) for some \(m>0\), minimizing
\(W(x)+W(q-x)-p\cdot x\) proves surjectivity and hence a global pair chart.

All differential and complex-geometry formulas below also apply locally when the positive Hessian is known only on a convex neighborhood. For example, the [[directed-analytic-realization/quantum-response-regularity-at-the-gauge-origin|actual homogeneous quantum response]] has a positive Hessian at its origin and therefore on a sufficiently small ball. That result supplies a local input for this construction, not global convexity, surjectivity or a complete clock. It does not identify that quantum response with the quartic family considered below.

For the [[algebra/cauchy-response-and-local-action|canonical Green pairing]]

\[
\sigma((\delta q,\delta p),(\delta q',\delta p'))
=\delta q\cdot\delta p'-\delta p\cdot\delta q',
\]

its pullback is

\[
\Omega=F^*\sigma
=-\sum_{i,j}C_{ij}\,dx^i\wedge dy^j,
\qquad
[\Omega]=\begin{pmatrix}0&-C\\ C&0\end{pmatrix}.
\tag{OP3}
\]

The diagonal blocks vanish because each response is a Hessian. The form is closed and nondegenerate. The affine configuration carrier and the sum map in (OP2) are inputs; nonlinear graph addition has not become an intrinsic vector-space decomposition independent of those choices.

## The separate Hessian metrics do not already match

Declare the positive candidate metric

\[
g=\begin{pmatrix}P&0\\0&M\end{pmatrix}.
\tag{OP4}
\]

This adds the two response Hessian costs and agrees with the quadratic norm in the linear opposed-boundary construction. It is a candidate prescription, not the unique possible metric on the pair carrier.

Fix the sign convention by defining \(L\) through
\(2g(Lu,v)=\Omega(u,v)\). Then

\[
L=\frac12
\begin{pmatrix}0&P^{-1}C\\-M^{-1}C&0\end{pmatrix},
\]
\[
L^2=-\frac14
\begin{pmatrix}
2I+P^{-1}M+M^{-1}P&0\\
0&2I+M^{-1}P+P^{-1}M
\end{pmatrix}.
\tag{OP5}
\]

The same diagonal expression can appear in both blocks without being symmetric in the Euclidean metric; each block has its appropriate \(g\)-adjointness. Using \(T=P^{-1}M\), which is similar to a positive-definite symmetric matrix, the condition \(L^2=-I\) is equivalent to \(T+T^{-1}=2I\). Its positive eigenvalues must all be one, and diagonalizability gives

\[
\boxed{L^2=-I\quad\Longleftrightarrow\quad P=M.}
\tag{OP6}
\]

Raw compatibility therefore holds on the diagonal \(x=y\), but on every independently variable pair only when the Hessian is constant, so \(W\) is quadratic up to affine terms. Strict positivity alone does not supply the linear construction's exact compatibility.

## Polar normalization produces a geometric mean

Because \(L\) is invertible and \(g\)-skew-adjoint, set

\[
Q=(-L^2)^{1/2},\qquad
J_{\rm pol}=LQ^{-1},\qquad
\widehat g(u,v)=g(Qu,v).
\tag{OP7}
\]

The positive square root is taken in the \(g\)-inner product. These tensors satisfy

\[
J_{\rm pol}^2=-I,\qquad
2\widehat g(J_{\rm pol}u,v)=\Omega(u,v).
\tag{OP8}
\]

Polar normalization preserves \(g\)-orthogonality of the resulting \(J_{\rm pol}\), but compatibility with the original symplectic form requires the corrected metric \(\widehat g\), not generally \(g\) itself.

The result has a simple form in the \((q,p)\) chart. Define the parallel sum and matrix geometric mean

\[
R=(P^{-1}+M^{-1})^{-1}=P(P+M)^{-1}M,
\]
\[
A=P\#M
=P^{1/2}\big(P^{-1/2}MP^{-1/2}\big)^{1/2}P^{1/2}.
\tag{OP9}
\]

The inverse differential of (OP2) gives

\[
g_{(q,p)}=
\begin{pmatrix}R&0\\0&C^{-1}\end{pmatrix}.
\tag{OP10}
\]

The geometric mean obeys \(AP^{-1}A=M\) and \(AM^{-1}A=P\). Consequently \(AC^{-1}A=R\), which identifies the polar tensors as

\[
\boxed{
J_{\rm pol}(\delta q,\delta p)=(-A^{-1}\delta p,A\delta q),
\qquad
\widehat g_{(q,p)}=\frac12
\begin{pmatrix}A&0\\0&A^{-1}\end{pmatrix}.}
\tag{OP11}
\]

Thus the nonlinear polar completion replaces a single linear response rate by the geometric mean of the responses at the two paired configurations. This gives an almost-Kähler structure because \(\sigma\) is closed. Integrability of this polar almost-complex structure in higher dimensions is a separate condition, not a consequence asserted here.

## One-dimensional integrability need not mean flat response geometry

For \(n=1\), write \(b(v)=W''(v)>0\). In the original pair coordinates,

\[
J_{\rm pol}(\delta x,\delta y)
=\left(\sqrt{\frac{b(y)}{b(x)}}\,\delta y,
-\sqrt{\frac{b(x)}{b(y)}}\,\delta x\right).
\tag{OP12}
\]

The local coordinates

\[
X=\int^x\sqrt{b(s)}\,ds,\qquad
Y=\int^y\sqrt{b(s)}\,ds
\]

give \(J_{\rm pol}\partial_X=-\partial_Y\), so \(z=X-iY\) is a complex coordinate. Here

\[
g=dX^2+dY^2,\qquad
\widehat g=\nu(dX^2+dY^2),\qquad
\nu=\frac{b(x)+b(y)}{2\sqrt{b(x)b(y)}}.
\tag{OP13}
\]

The original candidate metric is flat in these coordinates, while the metric compatible with the canonical pairing generally is not. Since
\(\nu=\cosh[(\log b(x)-\log b(y))/2]\), its Gaussian curvature along the diagonal is

\[
\boxed{
K_{\widehat g}\big|_{x=y=a}
=-\frac{b'(a)^2}{4b(a)^3}.}
\tag{OP14}
\]

Indeed \(K=-(2\nu)^{-1}(\partial_X^2+\partial_Y^2)\log\nu\); on the diagonal \(\nu=1\) and its first derivatives vanish. A local affine slope \(b(v)=1+\lambda v>0\) gives \(K(0,0)=-\lambda^2/4\). Pointwise raw compatibility at \(x=y\) therefore does not imply flat geometry near that locus.

## A different exchange prescription is Kähler in every dimension

The affine identification between the two copies of configuration space permits a different choice:

\[
J_0(\delta x,\delta y)=(\delta y,-\delta x).
\tag{OP15}
\]

Demanding \(2g_0(J_0u,v)=\Omega(u,v)\) now fixes

\[
\boxed{
g_0=\frac12
\begin{pmatrix}P+M&0\\0&P+M\end{pmatrix}.}
\tag{OP16}
\]

The constant exchange \(J_0\) is integrable in \(z=x-iy\), and \(\Omega\) is closed. Therefore \((J_0,g_0,\Omega/2)\) is Kähler for every positive response \(W\) under consideration. With the conventions
\(\omega=i\partial\bar\partial\mathcal K\) and
\(ds^2=2\mathcal K_{i\bar j}dz^i d\bar z^j\), its potential is

\[
\mathcal K(z,\bar z)=W(x)+W(y),
\qquad
\mathcal K_{i\bar j}=\frac14(P+M)_{ij},
\qquad \omega=\frac12\Omega.
\tag{OP17}
\]

This prescription takes the arithmetic mean of the two Hessians on each tangent factor. The polar prescription instead respects the original separate Hessian metric while normalizing its skew operator. They agree when \(P=M\), but they are genuinely different away from that locus.

The [[hessian-response-geometry/tangent-bundle-complexification|Hessian tangent-bundle construction]] supplies another integrable complexification, using a flat affine connection to split a tangent bundle into horizontal and vertical copies of a single base tangent space. Here the carrier is a pair of configurations, both responses may vary independently, and the symplectic form comes from their opposed graph sum. Neither construction derives its real base dimension. The constant exchange in (OP15) is a declared identification, not a proof that this complexification is uniquely necessary.

## A complex realization still does not choose its clock

Consider the [[algebra/nonlinear-response-and-clock-realization|classical response clock]] in one dimension:

\[
H_C(q,p)=\frac12p^2+\frac12N(q)^2,\qquad
B_C=(p,-f(q)),\qquad f=N'N.
\tag{OP18}
\]

It preserves \(\sigma\), but need not preserve the polar complex structure. Write
\(\alpha(q,p)=\sqrt{b(x)b(y)}\), where \((x,y)=F^{-1}(q,p)\). From (OP11),

\[
\mathcal L_{B_C}\widehat g
=\frac12
\begin{pmatrix}
B_C\alpha&\alpha-f'/\alpha\\
\alpha-f'/\alpha&-(B_C\alpha)/\alpha^2
\end{pmatrix}.
\tag{OP19}
\]

Since the clock is symplectic, preservation of \(J_{\rm pol}\) is equivalent to preservation of \(\widehat g\). Equation (OP19) supplies an exact negative control. Take

\[
W(v)=\frac12v^2+\frac14v^4,\qquad N(v)=v+v^3,
\]

and \(x=y=1\), so \((q,p)=(2,0)\). Then \(\alpha=4\), whereas
\(f'(2)=N'(2)^2+N(2)N''(2)=289\). The off-diagonal component of (OP19) is

\[
\frac12\left(4-\frac{289}{4}\right)=-\frac{273}{8}\neq0.
\tag{OP20}
\]

Thus even an integrable polar complex structure and a response-generated classical Hamiltonian need not form a holomorphic isometric clock. Complex geometry constrains a proposed realization; it does not make every normal-to-clock rule compatible.

## A quartic exchange geometry supplies a compatible circle clock

There is also a positive return. On \(\mathbb R^n\), take

\[
W(v)=\frac12v^TAv+W_4(v),\qquad A>0,
\qquad B_4(v)=\operatorname{Hess}W_4(v),
\tag{OP21}
\]

where \(W_4\) is a convex homogeneous quartic polynomial. Then \(B_4(v)\geq0\), the response is uniformly strictly convex, and (OP2) is a global diffeomorphism. Work with the exchange prescription (OP15)–(OP17), not with the polar metric.

Since \(B_4\) is quadratic, simultaneous rotations of the pair preserve its summed Hessian:

\[
\begin{aligned}
x_t&=\cos t\,x-\sin t\,y,&
y_t&=\sin t\,x+\cos t\,y,\\
B_4(x_t)+B_4(y_t)&=B_4(x)+B_4(y).
\end{aligned}
\tag{OP22}
\]

The mixed terms cancel by polarization of the quadratic matrix function. Consequently this complete circle action preserves \(g_0\), \(J_0\) and \(\Omega\). In the complex coordinates \(z=x-iy\), it is \(z_t=e^{-it}z\). Its infinitesimal generator is \(X_{\rm rot}=(-y,x)\).

The moment function for the full Green form is explicit:

\[
\boxed{
\begin{aligned}
H_{\rm rot}(x,y)
={}&x^TAx+y^TAy
+3W_4(x)+3W_4(y)
+\frac12x^TB_4(y)x,\\
\iota_{X_{\rm rot}}\Omega={}&dH_{\rm rot}.
\end{aligned}}
\tag{OP23}
\]

To verify it, let \(C=2A+B_4(x)+B_4(y)\). The contraction of (OP3) is
\((Cx)\cdot dx+(Cy)\cdot dy\). Homogeneity gives
\(B_4(x)x=3\nabla W_4(x)\). Symmetry of the quartic coefficient tensor gives

\[
\nabla_y\!\left[\frac12x^TB_4(y)x\right]=B_4(x)y,
\]

and the \(x\)-gradient of this mixed term is \(B_4(y)x\). These identities prove (OP23). Convexity and homogeneity make all quartic terms nonnegative, so \(H_{\rm rot}\geq x^TAx+y^TAy\) is proper, nonnegative and vanishes only at the origin. For the Kähler form \(\omega=\Omega/2\), the moment function is \(H_{\rm rot}/2\).

In one dimension, \(W(v)=av^2/2+\lambda v^4/4\), with \(a>0\) and \(\lambda\geq0\), gives the particularly simple return

\[
\boxed{
\begin{gathered}
r^2=x^2+y^2,\qquad
g_0=\left(a+\frac{3\lambda}{2}r^2\right)(dx^2+dy^2),\\
\Omega=-2\left(a+\frac{3\lambda}{2}r^2\right)dx\wedge dy,
\qquad
H_{\rm rot}=ar^2+\frac{3\lambda}{4}r^4.
\end{gathered}}
\tag{OP24}
\]

The clock parameter here is rotation angle, with period \(2\pi\), and the sign in (OP22) fixes its orientation. Replacing \(X_{\rm rot}\) by \(\kappa X_{\rm rot}\) replaces \(H_{\rm rot}\) by \(\kappa H_{\rm rot}\); geometry's circle action does not by itself calibrate a physical duration or select this multiplicative rate.

Transporting through the global pair chart gives a complete Hamiltonian flow on \((q,p)\) with
\(\widetilde H_{\rm rot}=H_{\rm rot}\circ F^{-1}\). Its canonical stationary action is

\[
S_{\rm rot}[q,p]
=\int\left[p\cdot\dot q-\widetilde H_{\rm rot}(q,p)\right]dt.
\tag{OP25}
\]

Here the Hamiltonian and its action are returned from a chosen geometric circle action and the same opposed response pairing. They have not been selected independently on an unrelated carrier.

This clock is not generally (OP18). In the scalar quartic family, along \(x=y=s\), one has \(H_{\rm rot}=2as^2+3\lambda s^4\), whereas \(H_C\circ F=\tfrac12(2as+8\lambda s^3)^2\). For \(\lambda>0\), no constant rate change identifies them. In the linear limit \(\lambda=0\), choosing \(\kappa=a\) recovers the usual response-clock rate.

The scalar member must not be mistaken for a new interaction. With \(a>0\), \(\lambda\geq0\), define global coordinates
\[
Q=\sqrt{2a+\tfrac32\lambda r^2}\,x,\qquad
P=-\sqrt{2a+\tfrac32\lambda r^2}\,y.
\tag{OP26}
\]
Then \(dQ\wedge dP=\Omega\) and \(H_{\rm rot}=(Q^2+P^2)/2\). The radial map is smooth and strictly increasing onto the full plane. It conjugates this clock to the ordinary unit-frequency harmonic oscillator. The response geometry can remain curved, but the scalar symplectic dynamics is canonically free; a nonlinear expression for its Hamiltonian in the earlier chart is not evidence of a new physical interaction.

A linear Hilbert-state carrier and quantum evolution still require an additional construction beyond this curved Kähler phase manifold. The exact return is nevertheless constructive: a declared opposed-response complexification can possess a complete holomorphic isometric clock, with its Hamiltonian fixed by contraction against the inherited Green form. The choice between the polar and exchange prescriptions, and the selection and calibration of the relevant group action, remain explicit parts of the realization.

The [[directed-analytic-realization/opposed_response_geometry_receipt.py|finite geometry receipt]] independently checks the noncommuting matrix mean, both compatible pairings, scalar curvature, the failed prescribed clock, the moment function for a nonradial convex quartic response, and the scalar harmonic-conjugacy control. [[directed-analytic-realization/opposed-response-geometry-receipt-output.txt|Its stored output]] records those checks. The complete finite-dimensional clock above is not a construction of the required local Yang–Mills dynamics or its quantum gap.

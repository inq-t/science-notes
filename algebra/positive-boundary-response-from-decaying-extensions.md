# A Positive Boundary Response from Decaying Extensions

Near a nondegenerate vacuum of an analytic finite-dimensional potential, the decaying Euclidean extension constructs a unique local gradient response with positive Hessian and exactly the original squared-response potential. A contraction proves existence, decay and compatibility; the higher response coefficients are then fixed recursively. This repairs the pointwise absolute-Hessian shortcut by solving for a whole compatible response, but it presupposes the configuration metric and a nonzero quadratic stiffness.

## The input and the local return

Fix a Euclidean configuration space \(Q=\mathbb R^d\). Let \(V\) be real analytic near zero, with

\[
V(0)=0,\quad \nabla V(0)=0,\quad
\operatorname{Hess}V(0)=A^2,\qquad A=A^T>0.
\tag{PD1}
\]

The subtraction \(V(0)=0\) fixes a constant, not dynamics. Write
\(a=\lambda_{\min}(A)>0\) and \(R(q)=\nabla V(q)-A^2q=O(|q|^2)\).
We will construct a real analytic germ \(W\) satisfying

\[
W(0)=0,\quad \nabla W(0)=0,\quad
\operatorname{Hess}W(0)=A,\qquad
\boxed{\frac12|\nabla W|^2=V.}
\tag{PD2}
\]

Its Hessian is positive definite on a sufficiently small ball. The response \(N=\nabla W\) is selected by an actual decaying boundary-value problem, not by taking the absolute value of a matrix separately at each configuration.

## A half-line Green operator constructs the branch

Seek a trajectory with prescribed boundary value \(q\):

\[
\gamma''=A^2\gamma+R(\gamma),\qquad
\gamma(0)=q,\qquad (\gamma,\gamma')\longrightarrow(0,0).
\tag{PD3}
\]

Choose \(0<\alpha<a\). On continuous paths into the complexification of \(Q\), use the Banach norm

\[
\|u\|_\alpha=\sup_{t\geq0}e^{\alpha t}|u(t)|.
\tag{PD4}
\]

Complex paths serve only to prove analyticity; real initial data will give real trajectories. The Dirichlet Green kernel for \(\partial_t^2-A^2\), with decay at infinity, is

\[
G(t,s)=-\frac1{2A}
\left(e^{-A|t-s|}-e^{-A(t+s)}\right).
\tag{PD5}
\]

In particular, \(G(0,s)=0\). Diagonalizing \(A\) gives

\[
\|G(t,s)\|\leq\frac1{2a}e^{-a|t-s|},\qquad
\|Gf\|_\alpha\leq C_\alpha\|f\|_\alpha,
\quad C_\alpha=\frac1{a^2-\alpha^2}.
\tag{PD6}
\]

The second estimate follows by splitting the integral at \(s=t\): its two contributions are bounded by \(1/(a-\alpha)\) and \(1/(a+\alpha)\), before multiplication by \(1/(2a)\).

Choose a closed complex ball of radius \(\rho\) inside a holomorphic extension domain of \(R\), and set

\[
L_\rho=\sup_{|z|\leq\rho}\|DR(z)\|,
\qquad \theta=C_\alpha L_\rho<1.
\tag{PD7}
\]

Such a choice exists because \(DR(0)=0\); for example require \(\theta\leq1/2\). If \(|q|<(1-\theta)\rho\), the map

\[
\mathcal T_q u(t)=e^{-At}q+
\int_0^\infty G(t,s)R(u(s))\,ds
\tag{PD8}
\]

maps the closed \(\rho\)-ball of (PD4) into itself and is a contraction with constant at most \(\theta\). Indeed \(|R(z)|\leq L_\rho|z|\) on this ball. Its unique fixed point satisfies

\[
\|\gamma_q\|_\alpha\leq\frac{|q|}{1-\theta}.
\tag{PD9}
\]

Differentiation of the Green integral gives a \(C^2\) solution of (PD3). For the derivative, the explicit bound

\[
\|\partial_tGf\|_\alpha\leq D_\alpha\|f\|_\alpha,
\qquad
D_\alpha=\frac{a}{a^2-\alpha^2}+\frac1{2(a+\alpha)}
\tag{PD10}
\]

follows from \(\|\partial_tG(t,s)\|\leq
(e^{-a|t-s|}+e^{-a(t+s)})/2\), away from the diagonal jump. Thus \(\gamma_q'\) decays at the same weighted rate. Uniform holomorphic contraction iterates, or the analytic implicit-function theorem with inverse \((I-D_u\mathcal T_q)^{-1}\), prove analytic dependence on \(q\). Explicitly, as operator norms from boundary variations into the weighted path space,

\[
\|D_q\gamma_q\|_\alpha\leq\frac1{1-\theta},\qquad
\|D_q\gamma_q'\|_\alpha
\leq\|A\|+\frac{D_\alpha L_\rho}{1-\theta}.
\tag{PD10a}
\]

The branch is consistent under taking tails. Put \(r_0=(1-\theta)\rho\). For \(|q|<(1-\theta)r_0\), (PD9) keeps every \(\gamma_q(t)\) inside the initial-data ball of radius \(r_0\). The shifted path stays in the same weighted \(\rho\)-ball. It solves the same decaying boundary problem with initial value \(\gamma_q(t)\), hence uniqueness gives

\[
\gamma_{\gamma_q(t)}(s)=\gamma_q(t+s).
\tag{PD11}
\]

Here any decaying solution in the weighted ball satisfies (PD8): subtract the Green representation; the remaining solution of \(u''=A^2u\) has zero initial value and decays, so vanishes. This justifies applying fixed-point uniqueness to the shifted trajectory.

## Decay forces an integrable positive response

Define the outward boundary response

\[
N(q)=-\gamma_q'(0)
=Aq+\int_0^\infty e^{-As}R(\gamma_q(s))\,ds.
\tag{PD12}
\]

It is analytic and \(DN(0)=A\). To prove closedness, take two parameter variations \(\xi,\eta\) along the same real trajectory. They satisfy
\(\xi''=\operatorname{Hess}V(\gamma_q)\xi\), and likewise for \(\eta\). Symmetry of this Hessian makes their Wronskian constant:

\[
\frac d{dt}\left(\langle\xi,\eta'\rangle-
\langle\xi',\eta\rangle\right)=0.
\tag{PD13}
\]

Exponential decay of both variations and their derivatives makes this constant zero. At the boundary, \(\xi(0)=v\), \(\eta(0)=w\), \(\xi'(0)=-DN(q)v\), and \(\eta'(0)=-DN(q)w\). Therefore \(DN(q)\) is symmetric. On the initial-data ball, set

\[
W(q)=\int_0^1\langle N(sq),q\rangle\,ds.
\tag{PD14}
\]

Closedness gives \(\nabla W=N\). Conservation of
\(\frac12|\gamma_q'|^2-V(\gamma_q)\), whose limiting value is zero, now proves (PD2). Continuity of \(DN\) and \(A>0\) give, after shrinking the ball,
\(\operatorname{Hess}W\geq aI/2\).

This constructs the stable Lagrangian graph \(p=-\nabla W(q)\); it was not an extra hypothesis. Tail consistency gives \(\gamma_q'=-N(\gamma_q)\), so integration of \(dW(\gamma_q)/dt=-|N(\gamma_q)|^2\) also identifies its boundary cost:

\[
W(q)=\int_0^\infty
\left[\frac12|\gamma_q'|^2+V(\gamma_q)\right]dt.
\tag{PD15}
\]

The [[algebra/nonlinear-response-and-clock-realization|nonlinear response theorem]] then supplies the opposed normal graph and the conditionally returned classical clock action. It owns those action and endpoint identities; this construction supplies their previously conditional regular decaying branch near the vacuum.

The positive germ is unique. Any other \(C^2\) solution of (PD2) has a sufficiently small forward gradient-decay flow with rate greater than \(\alpha\), because its Hessian is close to \(A\). These paths solve (PD3), remain in the contraction ball and hence coincide with \(\gamma_q\). Their gradients agree, and the normalization at zero fixes the constant. A positive Hessian at zero cannot choose a different quadratic matrix: it must be the unique positive square root of \(A^2\).

## The higher coefficients are determined together

Expand the analytic germs into homogeneous polynomials:

\[
V=\frac12q^TA^2q+\sum_{n\geq3}V_n,
\qquad W=\frac12q^TAq+\sum_{n\geq3}W_n.
\tag{PD16}
\]

On degree \(n\), the equation is

\[
L_AW_n=F_n,
\quad L_AF=(Aq)\cdot\nabla F,
\quad
F_n=V_n-\frac12\sum_{j=3}^{n-1}
\nabla W_j\cdot\nabla W_{n+2-j}.
\tag{PD17}
\]

The empty sum for \(n=3\) is zero. Its inverse is explicit:

\[
\boxed{L_A^{-1}F(q)=\int_0^\infty F(e^{-tA}q)\,dt.}
\tag{PD18}
\]

Differentiating under the integral proves the inverse identity. In an eigenbasis of \(A\), a monomial \(q^\beta\) has eigenvalue \(\beta\cdot\operatorname{spec}(A)\geq na\). In the supremum norm of degree-\(n\) polynomials on the unit sphere, \(\|L_A^{-1}\|\leq1/(na)\). In particular,

\[
W_3=L_A^{-1}V_3,\qquad
W_4=L_A^{-1}\left(V_4-\frac12|\nabla W_3|^2\right).
\tag{PD19}
\]

Recursion alone is a formal statement: differentiation in its nonlinear terms still requires convergence control. Here convergence follows from the independently constructed analytic germ, whose Taylor coefficients must satisfy the unique recursion.

For a signed response with
\(S(x,y)=(x^2-y^2)/2+g x^2y\), \(g\neq0\), its squared-response potential is

\[
V=\frac12|\nabla S|^2
=\frac{x^2+y^2}{2}+g x^2y
+\frac{g^2}{2}x^4+2g^2x^2y^2.
\tag{PD20}
\]

Now \(A=I\), so (PD19) gives

\[
W=\frac{x^2+y^2}{2}+\frac g3x^2y
+\frac{g^2}{9}(x^4+4x^2y^2)+O(|(x,y)|^5).
\tag{PD21}
\]

This is not the pointwise absolute Hessian of \(S\). Already to first order,

\[
\operatorname{Hess}W
=I+\frac{2g}{3}\begin{pmatrix}y&x\\x&0\end{pmatrix}+O(|(x,y)|^2),
\qquad
|\operatorname{Hess}S|
=I+2g\begin{pmatrix}y&0\\0&0\end{pmatrix}+O(|(x,y)|^2).
\tag{PD22}
\]

The [[algebra/absolute-hessian-and-response-integrability|absolute-Hessian obstruction]] is avoided by solving the compatibility and squared-response equations jointly. More generally, if \(\nabla S(0)=0\) and \(H_0=\operatorname{Hess}S(0)\) is invertible, this construction begins with \(A=|H_0|\), but does not prescribe \(\operatorname{Hess}W(q)=|\operatorname{Hess}S(q)|\) away from zero.

## What the nondegeneracy assumption does not explain

If \(A\) has zero modes, monomials supported entirely in its kernel have zero \(L_A\)-eigenvalue. Formula (PD18) then generally diverges, and the recursive equations become solvability conditions rather than an invertible prescription. Nonlinear terms can still select a response, but not by this theorem. For example, \(V(q)=q^4/2\) has the stable boundary cost \(|q|^3/3\), which is not analytic at zero; the two analytic signed branches do not both describe stable decay on both sides.

Even when each finite-dimensional \(A\) is positive, the Green bounds deteriorate as its smallest eigenvalue approaches zero. No regulator-uniform radius or response estimate follows without additional control. The homogeneous determinant gauge vacuum has zero quadratic stiffness, so the present theorem does not settle that case.

What is removed is the separate local assumption that a compatible positive response exists: the supplied analytic potential and metric construct it near a nondegenerate vacuum. What remains supplied is the finite configuration carrier, its metric, the potential, the nonzero quadratic scale and the normal-to-clock prescription. Global continuation, local gauge gluing, a normalizable quantum state and a continuum-uniform physical gap do not follow. In particular, [[algebra/response-factorization-and-the-vacuum|quantum factorization]] retains its divergence correction; (PD2) is a classical response identity, not a quantum vacuum equation.

For spatial gauge data, [[directed-analytic-realization/cubic-gauge-boundary-response-and-gauss-completion|the cubic boundary response]] applies the sum-rate inverse at coefficient level and supplies the required Gauss completion. It does not inherit this existence theorem across harmonic zero modes. The [[directed-analytic-realization/gauge_boundary_response_receipt.py|finite receipt]] checks (PD19)–(PD21) and the scalar weighted Green integral; analytic existence rests on the contraction above, not on those samples.

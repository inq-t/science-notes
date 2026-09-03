# The Binary Witten--Darboux Pair

The square root of the balanced binary susceptibility is the unique normalizable zero mode of a factored one-dimensional Schrödinger operator whose continuum is reflectionless. After scale and address are restored, the same factorization is unitarily equivalent to the sharp Poincare inequality for the logistic measure. More strongly, a homogeneous partner with an initially unspecified real constant and one normalizable ordered zero mode force the constant to be positive and uniquely force the logistic profile. These statements are exact for the declared one-dimensional carriers and have no automatic spacetime interpretation.

On the common core \(C_c^\infty(\mathbb R)\subset L^2(\mathbb R,\mathrm d\theta)\), define

$$
A
:=\frac{\mathrm d}{\mathrm d\theta}+\tanh\theta,
\qquad
A^\dagger
:=-\frac{\mathrm d}{\mathrm d\theta}+\tanh\theta.
$$

Direct multiplication gives

$$
\boxed{
H_-:=A^\dagger A
=-\frac{\mathrm d^2}{\mathrm d\theta^2}
+1-2\operatorname{sech}^2\theta,}
$$

and

$$
\boxed{
H_+:=AA^\dagger
=-\frac{\mathrm d^2}{\mathrm d\theta^2}+1.}
$$

The bounded real potentials define self-adjoint Schrödinger operators on the standard domain \(H^2(\mathbb R)\). Equivalently,

$$
\mathcal D
:=
\begin{pmatrix}
0&A^\dagger\\
A&0
\end{pmatrix},
\qquad
\mathcal D^2
=
\begin{pmatrix}
H_-&0\\
0&H_+
\end{pmatrix}.
$$

These identities are **[EXACT — AFTER BALANCED BINARY REDUCTION]**.

## Zero mode

The first-order equation

$$
A\psi_0=0
$$

has the square-integrable solution

$$
\boxed{
\psi_0(\theta)
=\frac1{\sqrt2}\operatorname{sech}\theta.}
$$

It is normalized because

$$
\int_{-\infty}^{+\infty}
\operatorname{sech}^2\theta\,\mathrm d\theta
=2.
$$

Using [[balanced-exponential-family|the binary metric]],

$$
\boxed{
|\psi_0(\theta)|^2
=\frac12g^{\mathrm{bin}}_{\theta\theta}.}
$$

The kernel is one dimensional because every solution of \(A\psi=0\) is proportional to \(\operatorname{sech}\theta\).

## Spectrum

The free partner has

$$
\sigma(H_+)=[1,\infty).
$$

Factorization gives \(H_-\geq0\). If \(H_-\psi=\lambda\psi\) for any \(\lambda>0\), then \(A\psi\neq0\) would be an \(L^2\) eigenvector of \(H_+\) with the same eigenvalue. The free operator \(H_+\) has no point spectrum, so \(H_-\) has no positive \(L^2\) eigenvalue. The decaying potential leaves the essential spectrum at \([1,\infty)\). Consequently,

$$
\boxed{
\sigma(H_-)=\{0\}\cup[1,\infty),}
$$

with the isolated zero eigenvalue supplied by \(\psi_0\). The function \(\tanh\theta\) is a bounded but non-normalizable threshold solution of

$$
H_-\tanh\theta=\tanh\theta.
$$

Threshold counting therefore requires an explicitly declared convention.

## Scale, address, and the sharp weighted gap

Let \(\nu>0\), let \(N_c\in\mathbb R\), and put \(x:=N-N_c\). Define

$$
q_{\nu,N_c}(N)
:=
\frac{\nu}{2}\operatorname{sech}^2(\nu x),
\qquad
\mathrm d\mu_{\nu,N_c}(N)
:=
q_{\nu,N_c}(N)\,\mathrm dN.
$$

This is the probability density used in [[wall-construction-interface/core-spectral-wall|the core spectral wall]]. Its positive half-density and factored operators are

$$
\psi_{0,\nu,N_c}(N)
=
\sqrt{q_{\nu,N_c}(N)},
$$

$$
A_\nu
:=
\frac{\mathrm d}{\mathrm dN}
+\nu\tanh(\nu x),
\qquad
A_\nu^\dagger
:=
-\frac{\mathrm d}{\mathrm dN}
+\nu\tanh(\nu x).
$$

Then

$$
A_\nu\psi_{0,\nu,N_c}=0,
$$

$$
H_{-,\nu}
:=
A_\nu^\dagger A_\nu
=
-\frac{\mathrm d^2}{\mathrm dN^2}
+\nu^2
-2\nu^2\operatorname{sech}^2(\nu x),
$$

and

$$
H_{+,\nu}
:=
A_\nu A_\nu^\dagger
=
-\frac{\mathrm d^2}{\mathrm dN^2}
+\nu^2.
$$

Translation and unitary dilation reduce these operators to the unit-width pair above, so

$$
\boxed{
\sigma(H_{-,\nu})
=
\{0\}\cup[\nu^2,\infty).}
$$

The multiplication map

$$
U_{\nu,N_c}:
L^2(\mathbb R,\mu_{\nu,N_c})
\longrightarrow
L^2(\mathbb R,\mathrm dN),
\qquad
U_{\nu,N_c}f
:=
\psi_{0,\nu,N_c}f,
$$

is unitary. Since

$$
A_\nu(\psi_{0,\nu,N_c}f)
=
\psi_{0,\nu,N_c}f',
$$

it identifies the closed weighted form

$$
\mathcal E_{\nu,N_c}[f]
:=
\int_{\mathbb R}|f'(N)|^2\,\mathrm d\mu_{\nu,N_c}(N)
$$

with the quadratic form of \(H_{-,\nu}\). Constants correspond to the zero mode. Hence the exact spectral statement is equivalently the sharp Poincare inequality

$$
\boxed{
\nu^2\operatorname{Var}_{\mu_{\nu,N_c}}(f)
\leq
\int_{\mathbb R}|f'(N)|^2\,\mathrm d\mu_{\nu,N_c}(N).}
$$

The constant is sharp but is not attained by a nonconstant \(L^2(\mu_{\nu,N_c})\) eigenfunction: the positive spectrum begins continuously at \(\nu^2\). The address \(N_c\) translates the state and leaves the lower edge unchanged; the inverse width \(\nu\) fixes the dimensionless rate.

## Flat-partner uniqueness

Let

$$
A_W:=\frac{\mathrm d}{\mathrm dN}+W(N)
$$

for a real \(C^1\) function on the whole line. Suppose only that its ordered partner is homogeneous: for some real constant \(\lambda\),

$$
\boxed{
A_WA_W^\dagger
=
-\frac{\mathrm d^2}{\mathrm dN^2}+\lambda}
$$

on \(C_c^\infty(\mathbb R)\), with the equality extending to the standard nonnegative self-adjoint closures, and suppose \(A_W\) has a nonzero \(L^2(\mathbb R,\mathrm dN)\) zero mode. Since \(A_WA_W^\dagger\geq0\) and the spectrum of the constant partner is \([\lambda,\infty)\), one first obtains \(\lambda\geq0\). If \(\lambda=0\), the globally smooth Riccati solutions are \(W=0\) and pole branches; the zero mode for \(W=0\) is constant and not square-integrable. Hence \(\lambda>0\). Write \(\lambda=\nu^2\) with \(\nu>0\).

Equality of the zeroth-order terms now gives

$$
W'(N)+W(N)^2=\nu^2.
$$

Its globally smooth solutions are the translated kinks

$$
W(N)=\nu\tanh\!\bigl(\nu(N-N_c)\bigr)
$$

and the two constants \(W=\pm\nu\); the remaining real solution branches have a pole. The constant branches give \(e^{\mp\nu N}\), which is not square-integrable on the whole line. Therefore the normalizable-zero-mode hypothesis leaves exactly

$$
\boxed{
W(N)=\nu\tanh\!\bigl(\nu(N-N_c)\bigr),
\qquad
|\psi_0(N)|^2
=
\frac{\nu}{2}\operatorname{sech}^2\!\bigl(\nu(N-N_c)\bigr).}
$$

Thus a homogeneous constant partner plus one normalizable pointing forces positivity of the partner constant, the logistic wall, its translation modulus, and its dimensionless lower edge. It does not fix the positive magnitude \(\nu\), nor explain why the homogeneous-partner law is fundamental. When \(\nu\downarrow0\), the probability measures lose tightness, the normalized state has no probability-measure limit on the line, and the lower edge closes as \(\nu^2\).

## Reflectionless continuum

For \(k>0\), applying \(A^\dagger\) to a free wave produces a generalized eigenfunction at energy \(1+k^2\):

$$
\psi_k(\theta)
=(-ik+\tanh\theta)e^{ik\theta}.
$$

It has no \(e^{-ik\theta}\) component at either end. After unit incoming normalization,

$$
\boxed{
R(k)=0,
\qquad
T(k)=\frac{k+i}{k-i},
\qquad
|T(k)|=1.}
$$

With \(u:=\ln k\), one continuous phase convention is

$$
\arg T
=2\arctan(e^{-u})
=\frac{\pi}{2}-\operatorname{gd}(u).
$$

The same Gudermannian that flattens [[fisher-line|the Fisher line]] therefore describes the scattering phase sweep. These are two representations of the same hyperbolic profile, not independent evidence for a physical model.

## Boundary of the theorem

Positivity of \(H_-=A^\dagger A\) is positivity of this internal operator on its declared domain. It does not prove stability, ghost freedom, causal propagation, or transparency for a spacetime perturbation. Such conclusions require a covariant action, constraint reduction, physical inner product, spacetime variable, and a theorem identifying its second-variation operator with \(H_-\).

An unqualified heat-regularized Witten index or Levinson count is not asserted here. On a noncompact line, continuum and threshold contributions make those prescriptions depend on domains and counting conventions. There is, however, one unambiguous domain-specific integer: with \(A_\nu\) regarded as a map \(H^1(\mathbb R)\to L^2(\mathbb R)\), the flat-partner identity makes it surjective, its kernel is spanned by \(\operatorname{sech}(\nu x)\), and its adjoint kernel is trivial. Hence its ordinary Fredholm index is \(+1\). [[contemporary-puzzles/yang-mills-mass-gap/indexed-scale-wall-and-the-causal-grain|The indexed-scale-wall theorem]] proves this statement and separates the integer wall charge from the continuous edge \(\nu^2\).

# The Binary Witten--Darboux Pair

The square root of the balanced binary susceptibility is the unique normalizable zero mode of a factored one-dimensional Schrödinger operator whose continuum is reflectionless. The statement is exact for the declared operators on \(L^2(\mathbb R,\mathrm d\theta)\) and has no automatic spacetime interpretation.

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

No Witten-index or Levinson-theorem value is asserted here. On a noncompact line, continuum and threshold contributions make those statements dependent on the chosen operator domains and counting conventions.

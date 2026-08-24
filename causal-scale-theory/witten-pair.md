# The Binary Witten--Darboux Pair

The square root of the binary susceptibility is the normalizable zero mode of an exact supersymmetric one-dimensional operator pair. This factorization is an internal consequence of the reduced state-space profile. It is not a cosmological perturbation equation, a spacetime chirality theorem, or evidence of ghost freedom.

On the binary coordinate $\theta$, define

$$
A:=\frac{\mathrm d}{\mathrm d\theta}+\tanh\theta,
\qquad
A^\dagger:=-\frac{\mathrm d}{\mathrm d\theta}+\tanh\theta.
$$

Then

$$
H_-:=A^\dagger A
=-\frac{\mathrm d^2}{\mathrm d\theta^2}
+1-2\operatorname{sech}^2\theta,
$$

and

$$
H_+:=AA^\dagger
=-\frac{\mathrm d^2}{\mathrm d\theta^2}+1.
$$

Equivalently, the two-component Witten operator is

$$
\mathcal D_\psi
:=
\begin{pmatrix}
0&A^\dagger\\
A&0
\end{pmatrix},
\qquad
\mathcal D_\psi^2
=
\begin{pmatrix}
H_-&0\\
0&H_+
\end{pmatrix}.
$$

These are **[EXACT — AFTER BINARY REDUCTION]**.

## Zero mode and susceptibility

The equation $A\psi_0=0$ has solution

$$
\psi_0(\theta)
=\frac1{\sqrt2}\operatorname{sech}\theta,
$$

normalized because

$$
\int_{-\infty}^{+\infty}\operatorname{sech}^2\theta\,\mathrm d\theta=2.
$$

Thus

$$
|\psi_0|^2
=\frac12G^{\mathrm{BKM}}_{\theta\theta}.
$$

The state-space susceptibility is literally the zero-mode density up to normalization.

## Spectrum

$H_+$ has continuum spectrum $[1,\infty)$. Darboux intertwining gives $H_-$ the same continuum together with the normalizable zero mode. The potential

$$
1-2\operatorname{sech}^2\theta
$$

is reflectionless for continuum scattering. The function $\tanh\theta$ is a non-normalizable threshold solution at eigenvalue one, so threshold counting requires care.

For continuum eigenvalue $1+k^2$, applying $A^\dagger$ to a free wave gives

$$
\psi_k(\theta)
=(-ik+\tanh\theta)e^{ik\theta}.
$$

There is no $e^{-ik\theta}$ component at either end, so

$$
R(k)=0.
$$

After unit incoming normalization, the transmission amplitude may be written

$$
T(k)=\frac{k+i}{k-i},
\qquad
|T(k)|=1,
$$

up to an overall phase convention. Its phase changes by $\pi$ between threshold and high momentum. With $u:=\ln k$ and the same convention,

$$
\delta(u)
=2\arctan(e^{-u})
=\frac\pi2-\operatorname{gd}(u).
$$

Thus the momentum-space phase sweep and [[causal-scale-theory/binary-geometry|the position-space Fisher half-turn]] use the same Gudermannian geometry. This is one factorization seen in two representations, not two independent pieces of evidence. No Witten-index or Levinson-theorem claim is needed here; continuum and threshold contributions make those statements convention- and domain-sensitive on the noncompact line.

The absence of a negative eigenvalue is exact for this internal operator. It says only that $A^\dagger A\ge0$ on its declared domain.

## Why no spacetime conclusion follows

A physical scalar perturbation operator is obtained from the second variation of a covariant action, after constraints and gauge redundancies are handled. No such derivation currently identifies its canonical variable, measure, time coordinate, or potential with $(\theta,H_-)$.

Therefore the following inferences are invalid without a new bridge:

$$
\text{internal factorization}
\not\Longrightarrow
\text{stable FLRW perturbations},
$$

$$
\text{reflectionless in }\theta
\not\Longrightarrow
\text{transparent spacetime propagation}.
$$

[[no-gos/positive-kinetic-field-crossing|The canonical-field no-go]] in fact shows that the most direct one-field lift fails across the response crossing. A successful covariant descendant remains a separate conjecture in [[conjectures/covariant-response-sector]].

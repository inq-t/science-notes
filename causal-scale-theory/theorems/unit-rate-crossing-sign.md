# CST-B2 Unit-Rate Candidate-Crossing Sign

On the flat zero-residual CST-B2 unit-rate background, the present-flatness function is strictly increasing, so its distinguished-reference root is unique and its past, present, or future sign is fixed exactly by comparing \(\mathfrak R_c\) with \(2D\). This is a member theorem about the \(\operatorname{sech}^2\) closure function; the root becomes a physical crossing date only after the member's event interpretation is constructed.

Assume the hypotheses of [[causal-scale-theory/theorems/present-flatness-closure|present-flatness closure]], set \(\nu=1\), and suppose

$$
\Omega_{m0},\Omega_{r0}\geq0,
\qquad
\Omega_{m0}+\Omega_{r0}>0.
$$

Define

$$
F_1(x)
=\left(\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}\right)
\operatorname{sech}^2x.
$$

Where \(F_1>0\),

$$
\frac{F_1'}{F_1}
=
\frac{3\Omega_{m0}e^{3x}+4\Omega_{r0}e^{4x}}
{\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}}
-2\tanh x.
$$

The first term lies between \(3\) and \(4\), while \(-2<2\tanh x<2\). Hence

$$
\frac{F_1'}{F_1}>1,
$$

so \(F_1\) is strictly increasing on \(\mathbb R\). Its limiting values are

$$
\lim_{x\to-\infty}F_1(x)=0,
\qquad
\lim_{x\to+\infty}F_1(x)=+\infty.
$$

Therefore every positive threshold admits exactly one real closure root.

At \(x=0\),

$$
F_1(0)=\Omega_{m0}+\Omega_{r0}=1-D.
$$

The threshold is \(T_{\mathfrak R}=D(2-\mathfrak R_c)/\mathfrak R_c\). Since \(F_1\) is strictly increasing,

$$
x_c>0
\quad\Longleftrightarrow\quad
T_{\mathfrak R}>F_1(0)
\quad\Longleftrightarrow\quad
\mathfrak R_c<2D.
$$

Thus

$$
\boxed{
\begin{aligned}
\mathfrak R_c<2D&\Longleftrightarrow x_c>0
&&\text{past candidate-crossing reference},\\
\mathfrak R_c=2D&\Longleftrightarrow x_c=0
&&\text{present candidate-crossing reference},\\
\mathfrak R_c>2D&\Longleftrightarrow x_c<0
&&\text{future candidate-crossing reference}.
\end{aligned}}
$$

This global uniqueness and sign theorem is special to \(\nu=1\). For other rates the root function can fold and the sign must be stated root by root.

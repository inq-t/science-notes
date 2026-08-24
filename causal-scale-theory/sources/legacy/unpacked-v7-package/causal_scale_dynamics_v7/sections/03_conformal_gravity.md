# Conformal gravity as transport and calibration

## Scale tractor

For four-dimensional conformal geometry define

$$
P_{ab}=\frac12\left(R_{ab}-\frac16Rg_{ab}\right),
\qquad
J=P^a{}_a=\frac{R}{6}.
$$

In a chosen representative metric, a standard tractor is written

$$
V^A\simeq(\alpha,\mu_a,\beta),
$$

with tractor norm

$$
h(V,V)=2\alpha\beta+g^{ab}\mu_a\mu_b.
$$

The scale tractor is

$$
\boxed{
I_A=\frac14D_A\sigma
\simeq
\left(
\sigma,
\nabla_a\sigma,
-\frac14(\Delta\sigma+J\sigma)
\right).
}
$$

The almost-Einstein operator is

$$
\boxed{
\E_{ab}(\sigma)
:=\left(\nabla_a\nabla_b\sigma+P_{ab}\sigma\right)_0.
}
$$

**[STANDARD]** On the open set where $\sigma\neq0$,

$$
\nabla_a^TI_B=0
\Longleftrightarrow
\E_{ab}(\sigma)=0
\Longleftrightarrow
g_\sigma\text{ is Einstein}.
$$

In the physical scale,

$$
\boxed{I^2=-\frac{R[g_\sigma]}{12}.}
$$

## Transport and norm equations

Taking the trace-free part of Einstein’s equation gives

$$
G^{\circ}_{ab}=\frac{8\pi G}{c^4}T^{\circ}_{ab}.
$$

The conformal transformation law yields

$$
G^{\circ}_{ab}[g_\sigma]
=2\sigma^{-1}\E_{ab}(\sigma),
$$

hence

$$
\boxed{
\E_{ab}(\sigma)
=\frac{4\pi G}{c^4}\sigma T^{\circ}_{ab}.
}
$$

Taking the trace gives

$$
\boxed{
I^2=\frac{2\pi G}{3c^4}T-\frac{\Lambda_{\rm g}}3.
}
$$

The accurate slogan is therefore:

$$
\boxed{
\begin{aligned}
\text{vacuum Einstein geometry}
&=\text{parallel scale transport},\\
\text{noncentral matter stress}
&=\text{transport defect},\\
\text{stress trace}
&=\text{norm variation},\\
\Lambda_{\rm g}
&=\text{global scalar lift}.
\end{aligned}}
$$

A measured $w_X\neq-1$ is not simply evidence for a new force. In this language it is evidence that the dark sector contributes to the failure of scale-tractor parallelism.

## Why the local equation is blind to the vacuum zero

Under

$$
T_{ab}\mapsto T_{ab}+\lambda g_{ab},
$$

one has

$$
T^{\circ}_{ab}\mapsto T^{\circ}_{ab}.
$$

Likewise a normalized Gibbs state is invariant under

$$
H\mapsto H+C\mathbf 1.
$$

Thus an additive vacuum offset is central in both languages:

$$
\boxed{
\begin{aligned}
H&\sim H+C\mathbf1,\\
T_{ab}&\sim T_{ab}+\lambda g_{ab},\\
\text{local causal response}&\sim\text{equivalence class modulo the central direction}.
\end{aligned}}
$$

This explains local vacuum blindness. It does not by itself make the remaining scalar lift radiatively stable. Section 11 returns to the global completion.


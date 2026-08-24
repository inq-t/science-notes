# Exact homogeneous dynamics and the sign of acceleration

## Flat FLRW scale dictionary

For a spatially flat FLRW metric

$$
\dd s^2=a^2(\eta)(-\dd\eta^2+\dd\mathbf x^2),
$$

choose the flat conformal representative. Then

$$
\sigma=\frac1a,
\qquad
N=\ln a=-\ln\sigma.
$$

The following identities are exact:

$$
\boxed{\sigma'=-H,}
$$

$$
\boxed{\mathcal R=-\frac{\sigma}{\sigma'},}
$$

$$
\boxed{\mathcal R'=q,}
$$

and

$$
\boxed{
q=-1+\frac{\sigma\sigma''}{\sigma'^2}
=\frac{(\ln\sigma)''}{[(\ln\sigma)']^2}.
}
$$

Here a prime denotes conformal-time differentiation and $\mathcal R=1/(aH)$ is the comoving Hubble radius.

The homogeneous null-energy condition is

$$
\rho+p\ge0
\quad\Longleftrightarrow\quad
\sigma''\ge0,
$$

so it is convexity of the scale section. Accelerated expansion is

$$
q<0
\quad\Longleftrightarrow\quad
(\ln\sigma)''<0,
$$

so it is log-concavity of scale.

The tractor norm becomes

$$
\boxed{
I^2=\frac12\sigma\sigma''-\sigma'^2
=-\frac12(1-q)H^2.
}
$$

## Closed background equation

With ordinary radiation and matter plus the scale-capacity source,

$$
\boxed{
H^2(N)=\frac{8\pi G}{3c^2}
\left[
\rho_{m0}e^{-3N}
+\rho_{r0}e^{-4N}
+\frac12\rho_{\rm crit,c}\sech^2(N-N_c)
\right].
}
$$

At the self-dual point,

$$
\frac12\rho_{\rm crit,c}
=\rho_m(N_c)+\rho_r(N_c)+\cdots.
$$

Present flatness determines $N_c$ from

$$
\boxed{
1=\Omega_{m0}+\Omega_{r0}
+\left[
\Omega_{m0}e^{-3N_c}
+\Omega_{r0}e^{-4N_c}
\right]\sech^2N_c.
}
$$

Thus $N_c$ is not an independently fitted dark parameter. Its intrinsic meaning is fixed by self-duality; its position relative to today is fixed by the measured ordinary state and flatness.

## Equation of state and structural invariant

The density law gives

$$
\frac{\dd\ln\rho_X}{\dd N}
=-2\tanh(N-N_c).
$$

Separate conservation gives

$$
\boxed{
w_X(N)=-1+\frac23\tanh(N-N_c).
}
$$

Let

$$
X:=1+w_X.
$$

Then

$$
\boxed{
X'=\frac23-\frac32X^2.
}
$$

The two fixed points are

$$
w_-=-\frac53,
\qquad
w_+=-\frac13.
$$

The observed history is the unique heteroclinic orbit from the early to the late fixed point. The one density maximum and one $w_X=-1$ crossing are not separately adjusted features.

The binary normalization becomes the differential invariant

$$
\boxed{
9(1+w_X)^2+6w_X'=4.
}
$$

This relation is independent of the amplitude and crossing date. It is the primary structural test of the theory.

## Why acceleration begins and ends

The total deceleration parameter is

$$
q=-1+\frac32
\frac{
\rho_m+\frac43\rho_r+(1+w_X)\rho_X
}{
\rho_m+\rho_r+\rho_X
}.
$$

Acceleration occurs when

$$
\boxed{
(2-3[1+w_X])\rho_X>\rho_m+2\rho_r.
}
$$

The response is negligible in the remote past, rises through the ordinary budget, and later decays as $a^{-2}$. Consequently the inequality is satisfied only on a finite interval.

The model therefore predicts two zeroes of $q$:

1. an observed past transition from deceleration to acceleration;
2. a future transition back to nonacceleration.

The phrase “the sign flip of cosmic acceleration” ordinarily refers to the first. The second is an independent future prediction.

## Benchmark

For

$$
\Omega_{m0}=0.310598,
\qquad
\Omega_{r0}=9.15\times10^{-5},
$$

the closed solution is

$$
\boxed{
N_c=-0.2940066,
\qquad
z_c=0.3417927.
}
$$

The crossing density in present critical units is

$$
\frac{\rho_*}{\rho_{\rm crit,0}}=0.7506311.
$$

The exact ordinary-sector equality is

$$
\frac{\rho_*}{\rho_m(N_c)+\rho_r(N_c)}=1.
$$

Relative to dust alone,

$$
\frac{\rho_*}{\rho_m(N_c)}=1.0003953.
$$

The present and transition observables are

| quantity | prediction |
|---|---:|
| $w_0$ | $-0.809454$ |
| tangent $w_a$ | $-0.612205$ |
| $q_0$ | $-0.336902$ |
| $j_0$ | $-0.111246$ |
| $q(N_c)$ | $-0.249901$ |
| horizon index $\mu_A(N_c)$ | $0.624951$ |
| acceleration entry | $z=0.785694$ |
| acceleration exit | $a/a_0=11.7865$ |

![The capacity-normalized background. The self-dual crossing, the observed acceleration entry, and the predicted exit are distinct events.](figures/rigid_history_v7.pdf){width=94%}

## Future causal character

At late times,

$$
\rho_X\propto a^{-2},
\qquad
w_X\to-\frac13.
$$

If the residual scalar floor is exactly zero,

$$
H\propto a^{-1},
\qquad
\dot a\to\text{constant},
\qquad
a(t)\sim t.
$$

The future conformal-time integral diverges,

$$
\int^\infty\frac{\dd t}{a(t)}\sim\int^\infty\frac{\dd t}{t}=\infty,
$$

so there is no permanent future event horizon.

A positive residual $\Lambda_g$, however small today, eventually dominates and changes the asymptotic state to de Sitter. Exact zero and observationally negligible are therefore distinct global sectors.

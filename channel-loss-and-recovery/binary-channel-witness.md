# Binary Channel Witness

A noisy binary symmetric channel has an invertible tangent map but a positive minimum-lift output form. This separates metric contraction from forgetting a nontrivial fiber and gives an exact test of the incoming loss cocycle, including the zero-loss identity channel.

## Binary channel witness

Let

$$
p_t=\left(\frac12+t,\frac12-t\right)
$$

be a faithful binary state for $|t|<1/2$, and let a binary symmetric channel have contraction parameter

$$
0<\lambda\leq1,
\qquad
t\longmapsto\lambda t.
$$

At the balanced state $t=0$, identify a tangent perturbation with its scalar coordinate $t$. The Fisher/BKM tangent metric is

$$
g(t,t)=4t^2.
$$

The [[channel-loss-and-recovery/bkm-loss-operators|incoming loss (D4)]] and [[channel-loss-and-recovery/minimum-lift-output-forms|minimum-lift output form (D9)]] become

$$
\ell_\lambda(t)
=
4(1-\lambda^2)t^2,
\tag{D15}
$$

$$
g_\lambda^\uparrow(s,s)
=
\frac{4s^2}{\lambda^2},
\qquad
\boxed{
\tau_\lambda(s)
=
4s^2(\lambda^{-2}-1).}
\tag{D16}
$$

For $0<\lambda<1$, the coefficient $\lambda^{-2}-1$ is strictly positive, so $\tau_\lambda(s)>0$ for every nonzero output tangent $s$. At $\lambda=1$, both incoming loss and output transgression vanish. Every allowed tangent map is invertible; the noisy maps show that positive output transgression does not require a nontrivial forgotten fiber.

For two channels,

$$
\ell_{\lambda_2\lambda_1}(t)
=
\ell_{\lambda_1}(t)
+
\ell_{\lambda_2}(\lambda_1t).
\tag{D17}
$$

[[channel-loss-and-recovery/receipts/descent_loss_cocycle_receipt.py|The descent-loss receipt]] checks the carrier split, weighted quotient metric, general two-arrow infimal composition, and binary identities (D15)--(D17) numerically. The positive coefficient on the noisy branch is a dimensionless contraction cost. No energy or time parameter occurs.

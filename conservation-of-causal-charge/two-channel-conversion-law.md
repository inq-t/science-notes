# The Two-Channel Conversion Law

A fixed positive total split into two channels acquires the hyperbolic \(\tanh/\operatorname{sech}^2\) form when the logarithm of their ratio is used as coordinate. The \(\operatorname{sech}^2\) pulse is then exactly the conversion current between the channels, and its integrated weight is an oriented endpoint index. This theorem is non-stochastic and purely algebraic; identifying the two channels physically remains open.

## Allocation theorem

Let \(C_+(N)>0\) and \(C_-(N)>0\) satisfy

$$
C_+(N)+C_-(N)=C_{\mathrm{tot}}>0.
$$

Define their logarithmic ratio and normalized imbalance by

$$
2\theta
:=\ln\frac{C_+}{C_-},
\qquad
m:=\frac{C_+-C_-}{C_{\mathrm{tot}}}.
$$

Solving the sum and ratio equations gives

$$
C_+
=C_{\mathrm{tot}}
\frac{e^\theta}{2\cosh\theta},
\qquad
C_-
=C_{\mathrm{tot}}
\frac{e^{-\theta}}{2\cosh\theta},
$$

and therefore

$$
\boxed{m=\tanh\theta.}
$$

Differentiating gives

$$
\boxed{
\frac{\mathrm dm}{\mathrm d\theta}
=1-m^2
=\operatorname{sech}^2\theta.
}
$$

Conversely, every \(m\in(-1,1)\) determines a unique positive allocation

$$
C_\pm=\frac{C_{\mathrm{tot}}}{2}(1\pm m)
$$

and a unique ratio coordinate \(\theta=\operatorname{artanh}m\).

## Affine scale transport

Suppose the independent hypotheses of [[basic-concepts/soldering/affine-scale-state|affine scale--state soldering]] hold, so the ratio coordinate is affine in logarithmic scale,

$$
\theta(N)=\nu(N-N_c),
\qquad
\nu>0.
$$

Then the channel-transfer current is

$$
J_C(N)
:=\frac{\mathrm dC_+}{\mathrm dN}
=-\frac{\mathrm dC_-}{\mathrm dN}
=\frac{\nu C_{\mathrm{tot}}}{2}
\operatorname{sech}^2\!\bigl(\nu(N-N_c)\bigr).
$$

The ordinary conservation equation is exact:

$$
\boxed{
\frac{\mathrm d}{\mathrm dN}(C_++C_-)=0.
}
$$

The normalized balance obeys

$$
\boxed{
m^2+\frac1\nu\frac{\mathrm dm}{\mathrm dN}=1.
}
$$

On the unit branch this becomes

$$
1=m^2+\frac{\mathrm dm}{\mathrm dN}.
$$

The pulse is therefore not inserted as a force profile. It is the conversion rate forced by four ingredients: positivity, a fixed two-channel total, a logarithmic ratio, and affine transport in that ratio.

## Endpoint index

If the history reaches the two saturated asymptotic allocations,

$$
m(-\infty)=-1,
\qquad
m(+\infty)=+1,
$$

then

$$
\mathcal I_C
:=\frac12\int_{-\infty}^{+\infty}
\frac{\mathrm dm}{\mathrm dN}\,\mathrm dN
=\frac12[m]_{-\infty}^{+\infty}
=1.
$$

Equivalently,

$$
\boxed{
\frac{\nu}{2}
\int_{-\infty}^{+\infty}
\operatorname{sech}^2\!\bigl(\nu(N-N_c)\bigr)
\,\mathrm dN
=1.
}
$$

This is a pathwise or topological normalization: it depends only on the endpoint sectors and is insensitive to translating \(N_c\). It is not a Noether charge derived from a spacetime action.

## The physical retyping is not part of the theorem

The theorem permits a precise non-stochastic reading of the binary family: \(C_\pm/C_{\mathrm{tot}}\) can be allocation weights rather than primitive random chances. Operational probabilities may still be represented by the same numbers; the algebra alone does not decide their ontology.

In the current causal-scale model, the two channels originate as a reduced normal chirality. They must not yet be renamed “observable information” and “gravity.” Such a reading requires one common physical type, an independently defined conserved total, and the equivariant weld proposed in [[state-geometry-charge-weld]]. [[binary-casimir-balance]] records the same structure as a Casimir partition rather than as channel transfer.

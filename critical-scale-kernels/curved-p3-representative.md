# The Curved \(P_3\) Representative

On a conformal three-manifold that carries suitable Poincare--Einstein filling or scattering data, the critical fractional conformal operator \(P_3\) is a natural curved representative of the flat \(|k|^3\) precision. Its conformal covariance and round-sphere spectrum are standard; existence, filling dependence, domain, kernel, and positivity must be checked for the selected geometry.

## Conditional construction

Let \((\Sigma^3,[g])\) occur as the conformal boundary of admissible filling or scattering data. Fractional conformal geometry associates a pseudodifferential operator of order three,

$$
P_3^g:C^\infty(\Sigma)\longrightarrow C^\infty(\Sigma),
$$

with principal symbol \(|\xi|_g^3\). At the critical weight, if

$$
\widehat g=e^{2\omega}g,
$$

its covariance takes the weight-zero form

$$
\boxed{
P_3^{\widehat g}(f)
=e^{-3\omega}P_3^g(f).}
$$

This is **[STANDARD — CONDITIONAL ON THE FRACTIONAL-CONFORMAL CONSTRUCTION]**. The scattering origin and conformal covariance are developed by [[causal-wall-spectral-theory/sources/papers/0109089-graham-zworski-scattering-matrix-conformal-geometry.pdf|Graham--Zworski]] and [[causal-wall-spectral-theory/sources/papers/1003.0398-chang-gonzalez-fractional-laplacian-conformal-geometry.pdf|Chang--Gonzalez]]. Positivity and extension results require additional hypotheses of the kind studied by [[causal-wall-spectral-theory/sources/papers/1012.0579-gonzalez-qing-fractional-conformal-laplacians-yamabe.pdf|Gonzalez--Qing]] and [[causal-wall-spectral-theory/sources/papers/1406.1846-case-chang-fractional-gjms-operators.pdf|Case--Chang]].

## Flat and round representatives

For the standard flat filling,

$$
\boxed{P_3=(-\Delta)^{3/2},}
$$

whose Fourier symbol is \(|k|^3\), agreeing with [[flat-weight-zero-precision|the flat classification theorem]].

On the round three-sphere of radius \(R\), scalar harmonics satisfy

$$
\boxed{
P_3Y_{\ell mn}
=R^{-3}\ell(\ell+1)(\ell+2)Y_{\ell mn},
\qquad \ell\geq0.}
$$

The \(\ell=0\) eigenvalue vanishes. For the standard round construction the operator is positive on the nonconstant harmonics.

## What the curved construction does not make automatic

The notation \(P_3^g\) suppresses data that can matter globally:

- the filling or scattering structure used to define the operator;
- the self-adjoint domain and boundary conditions;
- possible kernel beyond constants;
- positivity or lower boundedness on the proposed physical subspace; and
- regularity assumptions required by the critical endpoint.

Different admissible fillings need not determine identical global operators. Conformal covariance alone therefore does not select one universal positive precision on every curved conformal three-manifold.

## Running on a curved cut

The flat expression

$$
\mathcal K_\zeta(k)=C(k)|k|^3
$$

uses global momentum. A generic curved cut has no such coordinate. A covariant deformation must instead specify an operator through spectral calculus, a pseudodifferential symbol, or another geometrically defined functional of \(P_3\). Writing \(C(k)P_3\) without defining \(k\) is not a curved completion.

## Physical status

Using \(P_3\) as a cosmological or wall precision is **[IDENTIFICATION — OPEN]**. The standard geometry supplies a candidate operator after its hypotheses are met. It does not identify the field, construct its state, prove the required physical quotient, or provide Lorentzian evolution.

# Auxiliary Clock Elimination

An invariant Markov semigroup with both centered contraction and a spatial influence bound gives exponential covariance decay. Balancing the two estimates removes the auxiliary time parameter; rescaling that proof clock changes both rates together and leaves the static inverse-distance exponent unchanged. A scalar gap alone supplies no spatial locality.

## Forgetting and influence hypotheses

Let \((X,\mu)\) be a probability space carrying a unital, \(\mu\)-invariant Markov semigroup

$$
P_t=e^{-tL_0},
\qquad
\mu(P_th)=\mu(h).
\tag{ARL1}
$$

Let \(f\) and \(g\) be real-valued local square-integrable observables whose supports are separated by distance \(r\). Write \(h^\circ=h-\mu(h)\). Assume two estimates, uniform over the volumes, boundary conditions, and sectors under consideration.

First, centered functions forget at auxiliary rate \(\kappa>0\):

$$
\|P_th^\circ\|_2
\leq
e^{-\kappa t}\|h^\circ\|_2.
\tag{ARL2}
$$

Second, the failure of the semigroup to factor a separated product has a finite-influence estimate

$$
\left|
\mu\!\left(P_t(fg)-P_tf\,P_tg\right)
\right|
\leq
C_{f,g}e^{-\alpha(r-vt)},
\qquad 0\leq t\leq r/v,
\tag{ARL3}
$$

where \(\alpha>0\) is a spatial off-diagonal exponent and \(v>0\) is the **two-observable** influence speed appearing in this multiplicativity-defect bound, measured in distance per auxiliary time. The prefactor may depend on fixed support sizes and seminorms but not on the translation distance \(r\). This is a quasi-locality hypothesis on the proof dynamics, not a claim that stochastic time is physically real. If a source theorem instead gives two separately expanding cones and hence \(r-2vt\), replace \(v\) in (ARL3) by \(2v\); the optimized exponent changes accordingly.

## A static covariance bound

Stationarity gives the exact split

$$
\boxed{
\operatorname{Cov}_\mu(f,g)
=
\mu\!\left(P_t(fg)-P_tf\,P_tg\right)
+
\operatorname{Cov}_\mu(P_tf,P_tg).}
\tag{ARL4}
$$

By (ARL2)--(ARL3) and Cauchy--Schwarz,

$$
|\operatorname{Cov}_\mu(f,g)|
\leq
C_{f,g}e^{-\alpha(r-vt)}
+
\|f^\circ\|_2\|g^\circ\|_2e^{-2\kappa t}.
\tag{ARL5}
$$

Choose \(t=\theta r/v\) and balance the two coefficients of \(r\) in the exponents. This maximizes the certified common exponential rate; when the two prefactors in (ARL5) differ, it need not be the pointwise minimizer of the full right-hand side. The balancing value and common exponent are

$$
\theta_*
=
\frac{\alpha v}{\alpha v+2\kappa},
\qquad
\boxed{
\sigma_{\mathrm{aux}}
=
\frac{2\alpha\kappa}{\alpha v+2\kappa}.}
\tag{ARL6}
$$

Thus

$$
|\operatorname{Cov}_\mu(f,g)|
\leq
\left(C_{f,g}+\|f^\circ\|_2\|g^\circ\|_2\right)
e^{-\sigma_{\mathrm{aux}}r}.
\tag{ARL7}
$$

## Independence from clock normalization

This is an **[EXACT CONDITIONAL THEOREM]**. Invariance and unitality give (ARL4); reversibility is not used once (ARL2) is assumed. The auxiliary parameter has been eliminated. If the same generator is rescaled by \(L_0\mapsto qL_0\) with \(q>0\), equivalently \(P_t^{(q)}=P_{qt}\), then

$$
\kappa\mapsto q\kappa,
\qquad
v\mapsto qv,
\qquad
\alpha\mapsto\alpha,
\tag{ARL8}
$$

and (ARL6) is unchanged. Neither \(\kappa\) nor \(v\) is independently physical; their static response-cone combination is normalization invariant. Different admissible samplers for the same law can still give different nonoptimal certificates. A canonical number would require an independently selected sampler class and optimal constants, or a supremum over that declared class.

[[receipts/auxiliary_response_localization_receipt.py|The finite receipt]] and its [[receipts/auxiliary-response-localization-receipt-output.txt|recorded output]] check (ARL4), the balanced exponent, generator-rescaling invariance, and the linear-Gaussian instance of [[witten-covariance-and-local-response|the Witten covariance identity]]. They test none of the locality, Yang--Mills, RG, or continuum premises.

A scalar Poincare gap alone is therefore insufficient. It supplies (ARL2) after its normalization is declared but contains no physical distance. The locality or commutator estimate (ARL3) is the second indispensable input.

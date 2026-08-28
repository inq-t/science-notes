# Fisher Response

Fisher response is the local statistical sensitivity of a family of states to a declared parameter: it measures how rapidly neighboring probability laws become distinguishable. In a commuting exponential family it is simultaneously the Fisher information, the Hessian of relative entropy at coincidence, the variance of the generating observable, and the BKM metric coefficient. The word *response* here does not by itself mean time evolution, retarded susceptibility, or a spacetime response function.

## Scores and local distinguishability

Let

$$
p_\theta=(p_1(\theta),\ldots,p_n(\theta))
$$

be a differentiable family of strictly positive probability distributions. Its score is

$$
s_i(\theta):=\partial_\theta\log p_i(\theta).
$$

Normalization implies

$$
\sum_i p_i(\theta)s_i(\theta)=0.
$$

The Fisher information in the coordinate $\theta$ is

$$
\boxed{
I_\theta
:=\sum_i p_i(\theta)s_i(\theta)^2.}
$$

Its immediate meaning is local discriminability. For a small displacement $\delta\theta$,

$$
D_{\mathrm{KL}}(p_{\theta+\delta\theta}\Vert p_\theta)
=\frac12I_\theta\,\delta\theta^2
+O(\delta\theta^3).
$$

Thus $I_\theta\,\delta\theta^2$ is the leading squared information length between nearby states. Fisher information is a metric coefficient, so its numerical value changes under a reparametrization; the line element

$$
\mathrm ds^2=I_\theta\,\mathrm d\theta^2
$$

is the coordinate-invariant object.

## Why an exponential family responds by its variance

For fixed real labels $q_i$, let

$$
p_i(\theta)
=\frac{w_i e^{\theta q_i}}
{\sum_jw_je^{\theta q_j}},
\qquad w_i>0.
$$

Writing

$$
\Psi(\theta)
:=\log\sum_jw_je^{\theta q_j},
\qquad
m(\theta):=\sum_i p_i(\theta)q_i,
$$

one obtains

$$
s_i(\theta)=q_i-m(\theta).
$$

It follows that

$$
\boxed{
I_\theta
=\operatorname{Var}_{p_\theta}(q)
=\Psi''(\theta)
=\frac{\mathrm dm}{\mathrm d\theta}.}
$$

This last equality licenses the term *response*: the metric is the static susceptibility of the mean $m$ to its conjugate affine parameter. It remains a state-family statement. A law identifying $\theta$ with scale, temperature, a source, or time must be supplied independently.

For the three labels $(+1,-1,0)$ with equal reference weights, this calculation returns

$$
I_\theta
=\frac{2(\cosh\theta+2)}{(1+2\cosh\theta)^2},
$$

which is the response in [[a2-ternary-response/inq|the $A_2$ ternary test]].

## Why Fisher equals BKM here

For a faithful density operator $\rho$ and centered self-adjoint observables $\widetilde A$ and $\widetilde B$, the observable-coordinate Kubo--Mori form is

$$
g^{\mathrm{BKM}}_\rho(A,B)
:=
\int_0^1
\operatorname{Tr}
\!\left(
\rho^s\widetilde A\rho^{1-s}\widetilde B
\right)
\mathrm ds.
$$

When $A$, $B$, and $\rho$ commute, the operator ordering disappears and this reduces to ordinary covariance. Diagonal density matrices also turn quantum relative entropy into classical Kullback--Leibler divergence. Therefore the BKM coincidence Hessian on the commuting family is exactly its Fisher metric:

$$
g^{\mathrm{BKM}}_{\theta\theta}
=I_\theta
=\operatorname{Var}_{\rho_\theta}(Q).
$$

The equality is not a declaration that every quantum Fisher metric is BKM. Noncommuting quantum state space admits a family of monotone metrics; additional hypotheses select BKM. [[basic-concepts/hessians/inq|The Hessian account]] owns that wider distinction.

## Nearby response registers

For the exponential family above, Fisher response equals static susceptibility and, because the family commutes, BKM response. It is neither a Kubo real-time response, which needs dynamics and a causal prescription, nor a spatial precision, whose construction is the open CWST W2 map. [[program-core/response-registers|The response register]] owns the wider comparison so that it need not be repeated in each finite model.

Fisher information is also not a quantity of hidden facts stored in a state. It is a bilinear response of a specified family under specified variations. Changing the family or tangent changes the question being measured.

## Primary literature

Fisher introduced the statistical information associated with estimation in [[library/mathematical-foundations-of-theoretical-statistics/inq|*On the Mathematical Foundations of Theoretical Statistics*]]. Kullback and Leibler introduced the divergence used in the coincidence expansion in [[library/information-and-sufficiency/inq|*On Information and Sufficiency*]]. Kubo's [[library/statistical-mechanical-theory-of-irreversible-processes-i/inq|statistical-mechanical response paper]] is part of the quantum-response lineage, but its causal dynamical response must not be inferred from the static Fisher calculation. Petz's [[library/monotone-metrics-on-matrix-spaces/inq|classification of monotone matrix metrics]] and [[library/uniqueness-of-chentsov-metric-quantum-information-geometry/inq|Grasselli--Streater's finite-dimensional uniqueness theorem]] delimit the stronger hypotheses under which BKM is selected in noncommutative information geometry.

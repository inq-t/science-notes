# The Anchored Free-Energy Source Law

CST proposes that the renormalized horizontal BKM norm, evaluated along the full scale path and normalized by crossing horizon data, is a homogeneous response energy density. This is a constitutive law. The local relative-entropy Hessian explains the choice of susceptibility but does not derive the all-history profile or its factor of one half.

The proposed law is

$$
\boxed{
\rho_X(N)
:=\frac{k_BT_c}{2V_c}G^\perp_{NN}(N),}
$$

where $T_c$, $V_c$, and the extensive normalization of $G^\perp_{NN}$ are anchored at the self-dual crossing $N_c$.

Its intended meaning is that the energetic response associated with a scale displacement is proportional to the local distinguishability curvature of the horizontal state path. The factor $1/2$ is the declared quadratic-response normalization. It is not obtained by evaluating a fixed-reference free energy at finite separation.

## Exact motivation and constitutive extension

[[relative-entropy-hessian]] establishes, under its analytic hypotheses,

$$
\delta^2F_c=k_BT_cG^{\mathrm{BKM}}_{NN}(N_c)(\delta N)^2.
$$

The source law makes three additional moves:

1. it selects the reflection-odd horizontal block $G^\perp_{NN}$;
2. it promotes a local susceptibility to a density at every $N$;
3. it holds the crossing conversion data $(T_c,V_c)$ fixed along the history.

Those moves are **[CONSTITUTIVE]**, not consequences of the Hessian identity.

In particular, [[no-gos/fixed-reference-free-energy-does-not-give-the-pulse|the fixed-reference no-go]] shows explicitly that the corresponding binary relative entropy has a nonzero first derivative away from the crossing. A derivation that silently substitutes a neighboring-state expansion for that fixed-reference quantity is invalid.

## General profile before horizon conversion

With affine soldering, a balanced binary channel, and the fixed extensive normalization stated in [[causal-scale-theory/scale-capacity]],

$$
G^\perp_{NN}(N)
=\frac{S_c}{k_B}\mathfrak R_c
\operatorname{sech}^2(\nu x).
$$

Therefore

$$
\rho_X(N)
=\frac{T_cS_c}{2V_c}\mathfrak R_c
\operatorname{sech}^2(\nu x).
$$

[[causal-scale-theory/hawking-friedmann]] supplies the separate horizon identity that turns $T_cS_c/V_c$ into $\rho_{\mathrm{crit},c}$.

## Falsification and alternatives

The law fails if an independently constructed response source depends on another information-geometric functional, includes a linear term, uses instantaneous rather than anchored horizon data, or carries a nontrivial scale-dependent channel factor. Such a result would not alter the local BKM Hessian.

A viable alternative must still specify a covariant stress tensor or effective action. The present law closes only the homogeneous density; separate conservation is an additional background assumption used in [[causal-scale-theory/generalized-background]].

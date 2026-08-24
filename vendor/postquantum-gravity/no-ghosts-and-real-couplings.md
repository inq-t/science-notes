# No Ghosts, Because the Couplings Are Real

The best idea in this vendor. Higher-derivative gravitational actions are usually fatal: Ostrogradsky's theorem makes the Hamiltonian unbounded below, and quantisation returns negative-energy states or negative-norm ghosts. But that theorem assumes the action generates *deterministic* evolution. The same functional form, with a real rather than imaginary coefficient, is not a Lagrangian at all — it is an Onsager--Machlup weight, the log-probability of a diffusion, and it carries no instability. Quadratic gravity's ghost and the postquantum theory's diffusion are the same expression read under two different exponentials.

## One expression, two readings

Consider a free particle diffusing with no drift. The probability of reaching $q_f$ is

$$
P(q_f\mid q_0,\dot q_0,\ddot q_0)
=\frac{1}{\mathcal N}\int\mathcal Dq\;
e^{-\frac{1}{2D_2}\int_0^{t_f}(\ddot q)^2dt},
$$

which suppresses paths violating $\ddot q=0$ by an amount set by $D_2$. Now change one coefficient:

$$
-\frac{1}{2D_2}\;=\;\frac{i}{\hbar}.
$$

The integrand becomes an amplitude, $(\ddot q)^2$ becomes a Lagrangian with Euler--Lagrange equation $\mathrm d^4q/\mathrm dt^4=0$, and Ostrogradsky applies: the Hamiltonian $H=P_1X_2+\tfrac14P_2^2$ is linear in $P_1$ and unbounded below, which quantum mechanically returns negative energies or negative norms.

| | Amplitude reading | Probability reading |
|---|---|---|
| weight | $e^{iS/\hbar}$ | $e^{-\frac{1}{2D_2}\int(\ddot q)^2}$ |
| coefficient of $\int(\ddot q)^2$ | imaginary | real and negative |
| what $\ddot q^2$ is | a higher-derivative Lagrangian | a log-probability density on paths |
| obtained by integrating out | a **negative-energy** ghost field | a **positive-energy** noise source |
| Hamiltonian | Ostrogradsky, unbounded below | the ordinary $p^2/2m$, with diffusion |
| stationary points are | equations of motion | most probable paths, given initial *and* final data |
| the extra data are | negative-norm states | $\ddot q_0$ and $\dddot q_0$: the acceleration fluctuates |

The provenance row is the argument's spine and is worth stating on its own. An $i\ddot q^2$ term arises in quantum field theory by integrating out a field that must have negative energy. An $-\ddot q^2/2D_2$ term arises in stochastic dynamics by integrating out a noise source that has positive energy. Identical algebra, opposite ontology.

## Why the saddle points are not equations of motion

Because an Onsager--Machlup action is an equation of motion squared, varying it returns the original equation of motion as the *global* extremum — with action zero — together with further extremal solutions of the fourth-order equation. Those further solutions are not dynamical histories. They are **most probable paths**: the likeliest trajectory connecting given initial and final data for a particle whose acceleration is itself fluctuating. Specifying $q$ and $\dot q$ at $t=0$ no longer determines the trajectory, and the additional parameters $\ddot q_0,\dddot q_0$ record that fact rather than adding physical degrees of freedom with wrong-sign kinetic terms.

The same reading transfers to gravity. The postquantum action does not modify the ADM Hamiltonian of general relativity; it uses the equations of motion that Hamiltonian generates to build an Onsager--Machlup weight over metrics. A solution of the Einstein--Hilbert action remains a global extremum. What the $R^2$ and $C^{\mu\nu\rho\sigma}C_{\mu\nu\rho\sigma}$ terms of [[renormalisation]] measure is the *cost of deviating* from Einstein's equations, not new propagating content.

## What this does and does not establish

It establishes that the standard objection to higher-derivative gravity does not apply, because that objection presupposes a reading the theory rejects. It does not establish that the theory is well defined. The obligations transfer rather than vanish: where quadratic gravity must show that negative-norm states decouple, the postquantum theory must show that the weight is a genuine probability — that the two-point functions are positive semidefinite, that the path integral is normalisable, and that the non-positive-semidefinite deWitt kernel of [[cq-construction]] does no harm. Those are the subjects of [[renormalisation]] and [[stochastic-modes]], and they are not yet closed.

The trade is exact, and the published paper names it: the problem of negative-norm states and ghosts is **mapped to the problem of convergence of the path integral**. An indefiniteness in the norm has become a positivity question about a probability measure. Whether that is progress depends entirely on whether the positivity can be proved, and the sources are candid that it has been proved only sector by sector.

## Why this matters beyond the vendor

Read structurally rather than physically, the move is: a term that looks pathological under a *necessitating* reading of the action becomes innocuous under a *sufficing* one. The imaginary coefficient makes the action determine a history; the real coefficient makes it determine only a law of probability over histories. That is precisely the distinction this project draws between the two species of ground in [[sufficient-reason/two-species-of-reason|Two Species of Reason]], and the correspondence is developed in [[vendor/postquantum-gravity/commentary/descent-instead-of-diffusion|descent instead of diffusion]].

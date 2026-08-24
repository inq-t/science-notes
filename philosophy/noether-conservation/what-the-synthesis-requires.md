# What the Synthesis Requires

The theorem is a single identity in which the two axioms enter at two different places. The variational axiom supplies the decomposition of a variation into an equation-of-motion term plus a boundary term; the invariance axiom makes the symmetry variation of the Lagrangian density a pure divergence; setting the equation-of-motion term to zero along solutions leaves a conserved current. Neither axiom alone produces either half, the invariance required is invariance of the action rather than of the laws, and it must be invariance locally rather than of the integral over one fixed region.

## The setting

Let fields $\phi^a$ on a spacetime $\mathcal M$ have a local action

$$
S[\phi]=\int_{\mathcal M}\mathcal L(\phi^a,\partial_\mu\phi^a,x)\,\mathrm d^dx ,
$$

with Euler--Lagrange expressions

$$
E_a=\frac{\partial\mathcal L}{\partial\phi^a}-\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi^a)} .
$$

Let a Lie group with finitely many parameters act on $(x,\phi)$, with generators indexed by $k=1,\dots,r$ acting infinitesimally by

$$
x^\mu\mapsto x^\mu+\epsilon\,\xi^\mu_k,
\qquad
\phi^a\mapsto\phi^a+\epsilon\,\delta_k\phi^a .
$$

Because the transformation moves the coordinates as well as the fields, the object the calculus wants is the **characteristic**

$$
Q^a_k:=\delta_k\phi^a-\xi^\nu_k\,\partial_\nu\phi^a ,
$$

which measures the change of the field at a fixed point.

## The identity

For any vertical variation the variational axiom gives the pointwise decomposition

$$
\delta\mathcal L=E_a\,\delta\phi^a+\partial_\mu\Theta^\mu[\delta\phi],
\qquad
\Theta^\mu[\delta\phi]=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi^a)}\delta\phi^a ,
$$

an identity holding off shell. The invariance axiom supplies, again pointwise, invariance of the Lagrangian *top form* rather than of the scalar $\mathcal L$:

$$
\delta_k\bigl(\mathcal L\,\mathrm d^dx\bigr)=\partial_\mu K^\mu_k\,\mathrm d^dx,
\qquad\text{that is}\qquad
\operatorname{pr}v_k(\mathcal L)+\mathcal L\,\partial_\mu\xi^\mu_k=\partial_\mu K^\mu_k .
$$

The Jacobian term $\mathcal L\,\partial_\mu\xi^\mu_k$ is invisible for translations, rotations, and boosts, all of which have $\partial_\mu\xi^\mu_k=0$, and indispensable otherwise: for massless $\phi^4$ under dilatation $\xi^\mu=x^\mu$, $\delta\phi=-\phi$, the scalar alone gives $\operatorname{pr}v(\mathcal L)=-4\mathcal L$, which is no total divergence, while the top form gives $-4\mathcal L+4\mathcal L=0$. Locality here is likewise not decoration: equality of two integrals over one fixed region would not give equality of integrands, so the hypothesis must be invariance on every subregion, which is how [[philosophy/symmetry-principle/invariance-of-what|invariance of what]] states it. Combining the two and restoring the transport term that the coordinate motion contributes,

$$
j^\mu_k:=\Theta^\mu[Q_k]+\mathcal L\,\xi^\mu_k-K^\mu_k
\qquad\Longrightarrow\qquad
\partial_\mu j^\mu_k=-E_a\,Q^a_k ,
$$

hence

$$
\boxed{
\partial_\mu j^\mu_k=0
\quad\text{on shell},
\qquad k=1,\dots,r .
}
$$

For a purely internal symmetry $\xi^\mu_k=0$, the characteristic reduces to $\delta_k\phi^a$ and the current to $\Theta^\mu-K^\mu$. Dropping the $\mathcal L\xi^\mu_k$ term in general is not a simplification: without it, time translation does not return the energy.

The content of the synthesis is visible in the two substitutions. The variational axiom is what makes $\Theta^\mu$ exist; the invariance axiom is what makes $K^\mu_k$ exist; passing to solutions is what kills $E_aQ^a_k$. Remove any one and the identity produces nothing.

$K^\mu_k$ is the Noether boundary term, unrelated to the extrinsic-curvature trace $K$ of [[philosophy/principle-of-least-action/einstein-hilbert-action|the Einstein--Hilbert action]] or the modular Hamiltonian $K_\theta$ of [[program-core/symmetry-conservation-and-action|Symmetry, conservation, and action]].

## Why the invariance must be of the action

A symmetry of the *equations* guarantees only that solutions map to solutions, which says nothing about $\delta_k\mathcal L$ and supplies no $K^\mu_k$. A symmetry of the action, or of the action up to a divergence, supplies it by definition. The re-typing this demands, and the Kepler case that fails it, are established in [[philosophy/symmetry-principle/invariance-of-what|invariance of what]].

## Two registers, and the direction of transfer

Invariance is a property of $\mathcal L$ at every point of field space, so it is off shell. Conservation is asserted along solutions, so it is on shell. The theorem is a transfer from the first register to the second.

The transfer back is not blocked — that is the converse in [[variational-versus-dynamical-symmetry]] — but it is not free either: recovering a symmetry from a conservation law requires the system to be variational, normal, and totally nondegenerate, and requires *symmetry* read to include generalized ones. An observed conserved quantity therefore certifies a variational symmetry only once those hypotheses are in hand.

## From current to charge

A conserved current is a local statement. Obtaining a conserved number requires integrating over a slice,

$$
Q_k[\Sigma]=\int_\Sigma j^0_k ,
$$

and controlling the flux through the remaining boundary. The complete form is the flux-inclusive one — charge on a later cut, minus charge on an earlier cut, plus flux through the side boundary, equals zero — set out with its symplectic hypotheses in [[conservation-of-causal-charge/diagonal-charge-balance|Diagonal Charge Balance]]. Declaring a subsystem charge conserved while omitting the flux is an incomplete application of the theorem, and in infinite volume $Q_k$ may fail to converge even where $\partial_\mu j^\mu_k=0$ holds everywhere.

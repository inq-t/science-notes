# What the Synthesis Requires

The theorem is a single identity in which the two axioms enter at two different places. The variational axiom supplies the decomposition of a variation into an equation-of-motion term plus a boundary term; the invariance axiom makes the left-hand side of that decomposition a pure divergence; setting the equation-of-motion term to zero along solutions leaves a conserved current. Neither axiom alone produces either half, and the invariance required is invariance of the action rather than of the laws.

## The setting

Let fields $\phi^a$ on a spacetime $\mathcal M$ have a local action

$$
S[\phi]=\int_{\mathcal M}\mathcal L(\phi^a,\partial_\mu\phi^a,x)\,\mathrm d^dx ,
$$

and let an $r$-parameter Lie group act on $(x,\phi)$ with infinitesimal generators indexed by $k=1,\dots,r$, leaving $S$ invariant up to a boundary term. Write $E_a$ for the Euler--Lagrange expressions,

$$
E_a=\frac{\partial\mathcal L}{\partial\phi^a}-\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi^a)} .
$$

## The identity

For any variation whatever, the variational axiom gives the decomposition

$$
\delta S=\int_{\mathcal M}\Bigl(E_a\,\delta\phi^a+\partial_\mu\Theta^\mu[\delta\phi]\Bigr)\mathrm d^dx ,
$$

which is an identity holding off shell, with $\Theta^\mu$ the boundary term produced by integrating by parts. Now specialize $\delta$ to the symmetry variation $\delta_k$. The invariance axiom says the left side is a pure divergence,

$$
\delta_kS=\int_{\mathcal M}\partial_\mu K^\mu_k\,\mathrm d^dx .
$$

Equating the two expressions and defining

$$
j^\mu_k:=\Theta^\mu[\delta_k\phi]-K^\mu_k
$$

gives the off-shell identity $\partial_\mu j^\mu_k=-E_a\,\delta_k\phi^a$, hence

$$
\boxed{
\partial_\mu j^\mu_k=0
\quad\text{on shell},
\qquad k=1,\dots,r .
}
$$

The whole content of the synthesis is visible in the two substitutions. The variational axiom is what makes $\Theta^\mu$ exist; the invariance axiom is what makes $K^\mu_k$ exist; the passage to solutions is what kills $E_a\,\delta_k\phi^a$. Remove any one and the identity produces nothing.

## Why the invariance must be of the action

The middle step is the demanding one, and it is why [[philosophy/symmetry-principle/invariance-of-what|invariance of what]] had to be settled first. A symmetry of the *equations* guarantees only that solutions map to solutions, which says nothing about $\delta_kS$ and supplies no $K^\mu_k$. A symmetry of the *action*, or of the action up to a divergence, supplies it by definition.

$$
\text{symmetry of the laws}
\;\not\Longrightarrow\;
\text{symmetry of the action}
\;\Longrightarrow\;
\text{conserved current}.
$$

The synthesis is therefore not the conjunction of the two axioms as ordinarily stated. It requires the second to be re-typed onto the object the first introduces, and [[variational-versus-dynamical-symmetry]] shows how far that upgrade can fail.

## Two registers, and the direction of transfer

Invariance is a property of $S$ over all admissible histories, so it is off shell. Conservation is asserted along solutions, so it is on shell. The theorem is a transfer from the first register to the second, and it runs only in that direction: an on-shell statement cannot establish an off-shell one, which is why no observation of a conserved quantity by itself certifies a symmetry of the action. The [[cosmodynamics/registers-and-type-discipline|register discipline]] here is not pedantry but the reason the theorem has the logical shape it has.

## From current to charge

The presymplectic counterpart of the hypotheses assembled here — continuous action, normalized generator, moment map, boundary flux — is listed in [[program-core/symmetry-conservation-and-action|Symmetry, conservation, and action]]; the Lagrangian identity above is the same requirement seen from the action side.

A conserved current is a local statement. Obtaining a conserved *number* requires integrating over a slice,

$$
Q_k[\Sigma]=\int_\Sigma j^0_k ,
$$

and then controlling the flux through the remaining boundary. The honest form is always the flux-inclusive one — charge on a later cut, minus charge on an earlier cut, plus flux through the side boundary, equals zero — set out with its symplectic hypotheses in [[conservation-of-causal-charge/diagonal-charge-balance|Diagonal Charge Balance]]. Declaring a subsystem charge conserved while omitting the flux is an incomplete application of the theorem, and in infinite volume $Q_k$ may fail to converge even where $\partial_\mu j^\mu_k=0$ holds everywhere.

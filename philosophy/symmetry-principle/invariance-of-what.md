# Invariance of What

The symmetry principle is not one claim but a family indexed by the object left invariant. A group may preserve a configuration, the set of solutions, the action up to a boundary term, the Lagrangian strictly, or the functional measure, and these have different consequences. They are nested rather than equivalent, the nesting is strict, and the third module needs a specific one of them: invariance of the *action* is what Noether requires, and invariance of the *laws* is strictly weaker.

## Five targets

Let $G$ act on the objects of a theory. The following are five different assertions.

| Invariant object | Name | What follows |
|---|---|---|
| a particular configuration or state | symmetric configuration | nothing whatever about the law |
| the solution set, equivalently the equations of motion | dynamical symmetry | solutions map to solutions; new solutions from old |
| the action, up to a boundary term | variational (divergence) symmetry | a Noether current |
| the Lagrangian density, strictly | strict symmetry | a Noether current with no boundary correction |
| the functional measure as well | quantum symmetry | Ward identities; failure is an anomaly |

Reading the table downward is not reading one claim in increasing detail. Each row is a distinct hypothesis about a distinct object, and the type declaration in [[program-core/ontological-registers|the register declaration]] applies: a solution, a solution set, a functional, and a measure are different types, and an argument that slides among them has changed its subject.

## The nesting, and that it is strict

Write $\Phi_g$ for the finite action of $g\in G$ on histories, and $\delta_k$ for the infinitesimal generators, $k=1,\dots,r$, in the notation the synthesis will use. If

$$
S[\Phi_g\phi]=S[\phi]
$$

for all $\phi$, then critical points map to critical points, so every variational symmetry is a dynamical symmetry. The same holds when invariance is only up to a boundary term, which at the level of the Lagrangian density reads

$$
\delta_k\mathcal L=\partial_\mu K^\mu_k ,
$$

since a total divergence is annihilated by the Euler operator and the Euler--Lagrange expressions are unchanged. Hence

$$
\boxed{
\text{strict}\subseteq\text{variational}\subseteq\text{dynamical}.
}
$$

The second inclusion is strict, and the standard witness is Kepler. Under

$$
\boldsymbol r\mapsto\lambda^2\boldsymbol r,
\qquad
t\mapsto\lambda^3t,
$$

the Lagrangian $L=\tfrac12m|\dot{\boldsymbol r}|^2+\alpha/|\boldsymbol r|$ scales as $\lambda^{-2}L$ while $\mathrm dt$ scales as $\lambda^3\,\mathrm dt$, so

$$
S\longmapsto\lambda S .
$$

Since $\delta S=0$ and $\delta(\lambda S)=0$ have the same solutions, this maps solutions to solutions — it is Kepler's third law — and is therefore a dynamical symmetry. But the action is *rescaled*, neither preserved nor changed by a divergence, so it is not a variational symmetry and yields no conserved quantity. A symmetry can be real, physically famous, and Noether-inert.

The first inclusion is strict as well, and harmlessly so: a Galilean boost changes the free Lagrangian $\tfrac12m\dot x^2$ by the total derivative of $mvx+\tfrac12mv^2t$, giving a conserved quantity with a boundary correction rather than none.

## Symmetry of the laws is not symmetry of the action

The invariance axiom is most naturally stated about *laws*: the laws of physics are the same under $G$. That is the second row. Noether's theorem needs the third. The second axiom must therefore be re-typed onto the object that the variational axiom introduces:

$$
\text{symmetry of the equations}
\;\longrightarrow\;
\text{symmetry of the action},
$$

an upgrade that is not automatic and that Kepler fails. Until the first axiom has supplied an action, the second cannot even be stated in the form the synthesis requires.

## The measure is a separate hypothesis

The last row is a further condition, not a refinement of the others. A transformation can leave the action exactly invariant while the path-integral measure fails to be, in which case the classical conservation law has no quantum counterpart. This is the anomaly phenomenon; [[philosophy/principle-of-least-action/quantum-action|Quantum Action]] records that a classical symmetry of the action need not survive quantization, and the consequences are taken up in [[philosophy/noether-conservation/where-the-synthesis-fails|where the synthesis fails]].

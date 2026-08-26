# Normal-State Pointing and Factivity

The core spectral wall proves that no nonzero normal state can remain invariant under the full trace-scaling action. This gives a rigorous sense in which normalized statehood necessarily breaks scale covariance, but it does not select a unique state, a preferred cut, an outcome, a record, or an arrow of history. The theorem is a partial explanation of situated presentation, not a completed theory of actuality.

## The exact obstruction

Let $(\mathcal C,\tau)$ be the semifinite core with

$$
\tau\circ\beta_s=e^s\tau.
$$

Every normal positive functional has an $L^1(\mathcal C,\tau)$ density $d$. If the corresponding state were invariant under every $\beta_s$, the density would obey the compensating homogeneity relation

$$
\beta_s(d)=e^s d.
$$

The spectral-tail and layer-cake argument in [[wall-construction-interface/core-spectral-wall|The Core Spectral Wall]] then forces either divergent $L^1$ norm or $d=0$. Hence

$$
\boxed{
\text{no nonzero normal state is invariant under the full trace-scale flow}.}
$$

Singular invariant states are not excluded by this argument. More importantly, the result begins after a normal state has been supplied.

## Five notions that must remain separate

| Notion | Mathematical content | Present status |
|---|---|---|
| Scale non-invariance | $\Omega\circ\beta_s\ne\Omega$ for some $s$ | forced for nonzero normal states |
| Pointed coordinate | a chosen origin or distinguished feature of a filtration | extra data unless constructed from the state |
| State selection | a reason for choosing one $d$ or state orbit | open or member-specific |
| Contextual fact | a character of a commutative readout algebra | exact type, not selected by a state |
| Record and history | persistent, comparable factual structure with an orientation | open construction |

An arbitrary non-invariant state need not have one canonical center. The logistic density $d_{\nu,N_c}$ does, but that is a property of the chosen member. It is therefore safer to say **normalizability forces scale-symmetry breaking** than to say it forces a unique point.

The result can be read philosophically as

> A normalized viewpoint cannot be nowhere.

It cannot be read as

> Scale covariance by itself explains why a fact obtains.

## The unpointed ground

The clean unpointed object is not one selected filtration. It is the canonical core together with the groupoid of faithful weights and their Connes-cocycle comparison data. A filtration is a pointed presentation over that groupoid. The Copernican task is to identify what is natural across the whole groupoid without erasing the real differences among its objects.

This sharpens the phrase *nothing in particular*. The ground is not the zero object and need not be empty. It can be relationally rich while lacking a distinguished global point or section. [[sufficient-reason/facticity-and-pointing|Facticity and Pointing]] and the torsor analogy there own the distinction between non-emptiness and canonical pointing.

## A no-natural-selector theorem target

Normal-state non-invariance is not yet a no-selector theorem. A simple finite prototype shows what such a theorem would look like.

Let a group $G$ act transitively on a set $X$ with no fixed point, and let $\mu$ be a $G$-invariant probability measure. If an equivariant deterministic selector

$$
s:\operatorname{Prob}(X)\longrightarrow X
$$

existed at $\mu$, then

$$
s(\mu)
=s(g_*\mu)
=g\,s(\mu)
$$

for every $g\in G$. Thus $s(\mu)$ would be a $G$-fixed point, a contradiction.

This proves only the declared symmetric prototype. It does not derive the Born rule, exclude every deterministic ontology, or actualize a point. It demonstrates the required theorem shape: an invariant ground may determine a lawful measure while being unable to select a fact naturally.

For a commutative readout algebra $\mathcal D$,

$$
\omega|_{\mathcal D}
\longleftrightarrow
\mu_{\omega,\mathcal D}
\in\operatorname{Prob}(\operatorname{Spec}\mathcal D),
$$

whereas a fact is a character $\chi_x\in\operatorname{Spec}\mathcal D$. [[sufficient-reason/quantum-interpretations|Quantum Interpretation and the Type Change]] proves that restriction supplies the measure, not a map from that measure to one character.

## The factive obligation after no selection

A no-natural-selector result would change, not eliminate, the actuality problem. Cosmodynamics would no longer seek a concealed deterministic function $\mu\mapsto x$. It would seek a factive structure of the form

$$
(\text{state},\text{context},\text{instrument})
\rightsquigarrow
(\text{fact},\text{persistent record}),
$$

whose statistical law respects the local quantum fiber and whose records compose into history. A correspondence, stochastic morphism, completely positive instrument, or coalgebraic process may be a better carrier than an ordinary function; the correct type remains to be constructed.

This preserves the stronger insight of [[sufficient-reason/two-species-of-reason|sufficing and necessitating reason]]: the ground may suffice for the lawful possibility of a fact without containing that fact as an already distinguished point. It also preserves [[program-core/axioms-and-principles|factive completeness]]: absence of a natural deterministic selector is not permission to leave facts and records untyped.

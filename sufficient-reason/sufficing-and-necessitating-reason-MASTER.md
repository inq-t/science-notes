# Sufficing and Necessitating Reason

### A structural account of facticity, observation, and the arrow of time

Thomas Ruble · working document

---

## Thesis

There are two species of ground, and they are not rival answers to one question. They are answers to two questions conflated since 1927.

- A **necessitating reason** determines a point. It is a group action: invertible, functorial, expressible as a statement about *which element*.
- A **sufficing reason** determines a measure on points without determining a point. It is not a group. It is sufficient for **facticity** and insufficient for **content**.

The transition between them is not a process occurring in time. It is a **change of algebraic type**. The standard interpretations of quantum mechanics each assume that exactly one species exists, and each pays a characteristic price for it. The no-go theorems of the last sixty years are best read not as paradoxes but as the *proof* that the two species are irreducible to one another.

> **Status discipline.** This document contains three kinds of claim, and a result in one layer is not evidence for another.
> **(i) Established mathematics.** Gelfand duality, the absence of characters on simple algebras, Gleason, Bell, Kochen–Specker, Lambek's lemma, MASA existence, half-sided modular inclusion. Cited, not claimed.
> **(ii) A proposed reading.** That these results jointly constitute a type distinction between two species of ground, and that the arrow of time is algebraic rather than statistical.
> **(iii) Open targets.** The research programme of §9. None of it is done.

---

## 1. Existence is multiplicativity, not extremality

The sharpest form of the thesis is a fact about states on C\*-algebras.

**Gelfand duality.** For a commutative C\*-algebra $A \cong C_0(X)$, the points of $X$ are exactly the *characters* of $A$ — the nonzero \*-homomorphisms $\chi: A \to \mathbb{C}$. "Point" and "multiplicative functional" are the same thing. A space is recoverable from its algebra of functions, and it is recoverable *as the character space*.

**Pure is not multiplicative.** On a commutative algebra the pure (extremal) states and the characters coincide: both are evaluation at a point, both are Dirac measures. On a noncommutative algebra they come apart. A pure state on $M_n(\mathbb{C})$ is a vector state $\omega_\psi(A) = \langle\psi|A|\psi\rangle$ — extremal in the state space, but **not multiplicative**: $\omega(A^2) \neq \omega(A)^2$ unless $\psi$ is an eigenvector of $A$.

So a maximally definite quantum state is still not a fact. It is extremal without being multiplicative.

**That gap is the predicate.**

**No characters at all.** $M_n(\mathbb{C})$ is simple, so any nonzero homomorphism to $\mathbb{C}$ would be injective — impossible for $n \ge 2$ on dimensional grounds. It has *zero* characters. Not few; none. Local algebras in relativistic QFT are generically hyperfinite type III$_1$ factors, where the situation is stronger: no minimal projections, no normal pure states, no trace. Not merely pointless but **atomless**.

**Why Frege does not touch this.** The standard analysis says existence is the second-order property *this concept is instantiated*. But a torsor **is** instantiated; it has elements in abundance. What it lacks is a *distinguished* element. Non-emptiness and pointedness coincide only in settings where having elements and having a canonical element are the same, and a torsor is precisely where they come apart.

**The obstruction has a home.** Torsors under $G$ are classified by $H^1(\text{base}, G)$, trivial **iff** the torsor has a section. Existence in this sense takes values in a cohomology group rather than in $\{\text{yes},\text{no}\}$. Arithmetic geometry has done this for seventy years: the Selmer curve $3x^3+4y^3+5z^3=0$ has points over $\mathbb{R}$ and over every $\mathbb{Q}_p$ and none over $\mathbb{Q}$ — locally existent everywhere, globally nonexistent — with the failure measured by the Brauer–Manin obstruction.

The quantum instance of the same shape: Kochen–Specker, in the Isham–Butterfield formulation, is exactly the statement that **the spectral presheaf has no global sections**. Points exist context by context and not globally.

---

## 2. The two reasons, defined

Let $\mathcal{M}$ be the pre-observable algebra, $\mathcal{D} \subset \mathcal{M}$ a commutative subalgebra (a *readout context*), and $\omega$ a state.

> **Necessitating reason.** A ground that determines a character; formally, a section of the spectrum. Operationally: *the value was $x$, and the equations carry $x$ forward and backward*. The dynamics is a group, time enters as a free parameter, and the reason is symmetric under its inversion.

> **Sufficing reason.** A ground that determines a probability measure on $\mathrm{Spec}(\mathcal{D})$ and no point of it. Operationally: sufficient *that* a fact occurs in the context, insufficient for *which*.

Two theorems prevent this from being a restatement of ignorance.

**Sufficing reason has a forced form.** By Gleason's theorem, any assignment of probabilities to projections consistent across commuting contexts, in dimension $\ge 3$, must take the form $\mu(P) = \mathrm{Tr}(\rho P)$. The measure is not chosen; it is the unique consistent one. Sufficing reason is as rigid as necessitating reason. It simply terminates in a different kind of object.

**The two species are provably irreducible.** Bell and Kochen–Specker are, in this reading, exactly the theorems that a sufficing reason cannot be upgraded to a necessitating one. You may not add hidden values and retain locality (Bell) or non-contextuality (Kochen–Specker). The distinction is therefore not a philosophical posture about explanation. It is the content of two no-go results.

---

## 3. Two dual formalisms

The distinction has a precise home. Categorical logic and theoretical computer science have spent forty years developing exactly the dual pair required, under the slogan **algebras for construction, coalgebras for observation** (Rutten; Jacobs).

Let $F$ be an endofunctor on a suitable category.

An **$F$-algebra** is an object $X$ with $F(X) \to X$. The *initial* algebra is the least fixed point: well-founded, built from below, finite derivations, proof principle **induction**. Everything in it is reachable by construction.

An **$F$-coalgebra** is an object $X$ with $\gamma: X \to F(X)$ — one step of unfolding, one step of observation. The *final* coalgebra is the greatest fixed point: non-well-founded, potentially infinite behavior, proof principle **coinduction**, identity criterion **bisimulation**: two states are equal precisely when no sequence of observations distinguishes them.

| | Necessitating reason | Sufficing reason |
|---|---|---|
| Formalism | initial algebra | final coalgebra |
| Direction | construction | observation |
| Proof principle | induction | coinduction |
| Identity criterion | structural equality | bisimulation |
| Foundedness | well-founded | non-well-founded |
| Dynamics | group | semigroup |
| Time | free parameter | direction of unfolding |

Note what bisimulation *is*: the identity of indiscernibles, converted from a principle into a definition. Two objects are the same when nothing observable separates them. Leibniz supplied the vocabulary of sufficient reason; the coalgebraists supplied the criterion of sameness that belongs with it.

**Lambek's lemma (1968).** If $(Z,\zeta)$ is a final $F$-coalgebra then $\zeta: Z \to F(Z)$ is an **isomorphism**: $Z \cong F(Z)$. The object is carried into its own unfolding, invertibly.

This is the fold, as a theorem rather than a metaphor. It has an immediately suggestive reading, which belongs in layer (iii):

> Each individual unfolding $\gamma$ is not invertible. The *totality* of behavior is. Irreversibility at every step; reversibility of the whole.

---

## 4. The arrow is a monoid that is not a group

**A correction that matters.** Unitary evolution is noncommutative **and reversible**: $\sigma_t(A) = U_t A U_t^*$ is a one-parameter *group*. Noncommutativity supplies multiplicity, not direction.

What breaks reversibility is the **restriction** $\Pi: \mathcal{M} \to \mathcal{D}$ — the passage to a commutative shadow. Information about non-commuting complements is not hidden by it; it has no image under it.

> **Necessitating reason is a group. Sufficing reason is a monoid that is not a group. The arrow of time is that failure.**

The same statement appears at both levels of the formalism, which is the main structural evidence that they are one claim.

**Operator-algebraic level.** Let $\mathcal{N}\subset\mathcal{M}$ share a cyclic separating vector with $\Delta_\mathcal{M}^{it}\,\mathcal{N}\,\Delta_\mathcal{M}^{-it} \subseteq \mathcal{N}$ for one sign of $t$. Wiesbrock and Borchers show this generates a positive-energy translation with $U(a)\mathcal{M}U(a)^* \subseteq \mathcal{M}$ for $a \ge 0$: a one-parameter **semigroup of endomorphisms**, continuous, detectable by comparing a region with a subregion. Non-invertibility a local observer can feel. Arveson's $E_0$-semigroups are the mature general theory, classified by product systems with a numerical index.

**Coalgebraic level.** A structure map $\gamma: X \to F(X)$ has no inverse in general; unfolding runs one way; composition is a monoid.

**The Keller phenomenon, and why it is a scholium.** Keller maps compose — Jacobian determinants multiply — so if some Keller map is not an automorphism, the monoid of Keller self-maps of $\mathbb{A}^n$ is not a group. Geometric degree is multiplicative under composition, so iterating a degree-3 map gives fibers of size $3^n$: entropy production $\log 3$ per step, in the sense of algebraic entropy.

But a Keller map is **étale**. Every local test says it is invertible. An arrow arising this way would be globally real and *locally undetectable*, which is the opposite of how time is encountered. Coinduction defines identity by what can be observed, so the coalgebraic framing sides with modular inclusion against Keller for a principled reason rather than a preference.

The correct relation is not rivalry, but the identification is not established: half-sided modular inclusion would be the continuous, locally detectable analogue of the discrete, globally hidden Keller structure only after a bridge between the two is constructed — [[sufficient-reason/algebraic-arrow-of-time|the algebraic-arrow note]] records that the two presently share only a formal contrast between ambient reversibility and one-sided global structure. The algebraic side is the one that carries the physics.

---

## 5. Why this is not Boltzmann

The obvious objection: *locally reversible, globally not, because a projection loses information* is coarse-graining, known since 1872.

| | Boltzmann | This account |
|---|---|---|
| Microdynamics | group (Hamiltonian flow) | group (unitary) |
| Loss mechanism | coarse-graining to macrostates | restriction to a commutative subalgebra |
| Reference measure | Liouville | **none available** |
| Arrow is a property of | a *state* (the initial one) | the *algebra* |
| Extra input required | Past Hypothesis | — |

The load-bearing row is the third. Boltzmann's arrow requires a boundary condition: the initial state was low-entropy *relative to Liouville measure*. That reference measure is what makes "special" meaningful.

A type III$_1$ factor **has no trace**. There is no canonical uniform measure, hence no state-independent sense in which one state is special relative to equilibrium. By Connes' cocycle theorem the modular flow $t \mapsto \sigma^\omega_t$ is canonical in $\mathrm{Out}(\mathcal{M}) = \mathrm{Aut}(\mathcal{M})/\mathrm{Inn}(\mathcal{M})$, independent of the state chosen. The flow belongs to the algebra, not to a state on it.

**Statistical versus algebraic asymmetry.** There is a graveyard of attempts to derive time asymmetry from a time-symmetric substrate; Price's critique is the standard statement, and the Boltzmann-brain problem is the standard symptom. If low entropy is *typical from inside* rather than boundary-imposed, isolated observers with false records dominate histories, and the argument undercuts the memories that motivated it.

Every version that dies this way is **statistical** — asymmetry derived from typicality with respect to a measure. The present account is not. $\Delta^{it}\mathcal{N}\Delta^{-it}\subseteq\mathcal{N}$ holds for one sign of $t$ and fails for the other as a structural fact about the inclusion, and the generator is positive — not usually positive. There is no fluctuation into the reverse case, because the reverse case is not a low-probability configuration; it is not a configuration.

**What this reading claims about the past.** Not that a low-entropy region existed, but that *the past is the direction along which records exist*, and records are the residue of a non-invertible restriction. The Past Hypothesis is then not a fact about a region but a condition on the form of appearance. This is Kant's Second Analogy — objective succession is possible only under a rule of irreversibility — argued from an algebra rather than from the unity of apperception.

**What it does not yet buy.** It removes the *foothold* for the Past Hypothesis by removing the reference measure the Hypothesis needs. It does not thereby derive records, memory, or the thermodynamic gradient. And it delivers *an* orientation without delivering that the orientation is **shared**: every observer's records point the same way, and that is a compatibility condition across walls, not a property of any one wall. See target C5.

---

## 6. Whether "nothing" is an option

The metaphysical question — must there be facts? — becomes two mathematical ones. Both have partial answers.

**6.1 Given a commutative context, facts are guaranteed.** A nonzero commutative unital Banach algebra has a nonempty character space. The proof is Zorn: maximal ideals exist, and the quotient by a maximal ideal is $\mathbb{C}$ (Gelfand–Mazur).

This is the fold in miniature, fully rigorous: **the condition for the possibility of facts entails a fact**, as a two-line proof. And it fails exactly where §1 says it must — $M_n(\mathbb{C})$ is simple, has no maximal two-sided ideal of codimension one, and therefore no characters. Noncommutativity is precisely the failure of the guarantee.

**6.2 Every algebra contains such a context.** Every von Neumann algebra contains a maximal abelian self-adjoint subalgebra (Zorn, on the poset of abelian self-adjoint subalgebras). So every wall — including a type III$_1$ factor with no points of its own — necessarily contains commutative subalgebras, which necessarily have characters. **Facticity is entailed by the existence of the algebra.** There is no wall without readouts.

**6.3 The residue, sharply.** A MASA in a type III$_1$ factor is diffuse, $\mathcal{D}\cong L^\infty(X,\mu)$, and its characters are **not normal** — not $\sigma$-weakly continuous, not preparable, not limits of vector states. They exist by Zorn and are invisible to any physical procedure.

So the guarantee delivers: facts exist as characters. It does not deliver: facts are realizable as normal states. This is the right shape of open problem — sharp, and about normality.

**6.4 The general criterion.** Adámek's terminal-sequence construction gives the final coalgebra as the limit of
$$1 \longleftarrow F(1) \longleftarrow F^2(1) \longleftarrow \cdots$$
The sequence *begins* nonempty. But an inverse limit of nonempty sets can be empty — that is where the naive argument dies. The limit is guaranteed nonempty when the stages are **compact Hausdorff and nonempty**.

So *is nothing an option?* becomes: **is the terminal sequence compact?** And by Gelfand duality, compactness is what unitality supplies — a unital commutative C\*-algebra is $C(X)$ with $X$ compact Hausdorff. The unit of the algebra is what forecloses emptiness. That identifies a specific structural feature whose absence would permit nothing, and it is checkable.

**6.5 The form of the argument.** The functor $F$ encodes what one step of observation is, so the fixed point $Z\cong F(Z)$ produces **self-consistency of the observation structure**, not facticity from nothing. Aczel's Anti-Foundation Axiom established that non-well-founded structures are consistent — self-reference is not paradox — and Lambek establishes that the fixed point is genuine. What the construction does not do is dispense with its antecedent.

What it buys is nonetheless substantial: the antecedent is no longer vague (it names a functor), the consequent is no longer a hope (it is a fixed point with an identity criterion), and the nonemptiness question is no longer metaphysical (it is a compactness question).

---

## 7. Diagnosis of the interpretations

Each standard position is a stance on how many species of reason there are.

**Copenhagen** — two species, the second left primitive. Unitary evolution plus a measurement postulate. It correctly recognizes the type distinction and declines to analyze it, which is why the Heisenberg cut is movable and why *when does collapse occur* has no principled answer. On this account it has no answer because it is not a temporal question.

**Many Worlds** — one species, necessitating only. The probability problem is the exact symptom: having removed all contingency, one must manufacture a sufficing reason from necessitating materials (Deutsch–Wallace decision theory; Sebens–Carroll self-locating uncertainty). Gleason already fixes the *form* the measure must take; what Everettianism owes is why a measure is the right object at all in a theory containing no contingency.

**Bohm** — restore the global point by fiat. Add particle positions, recover a global commutative section, and pay the Bell toll in nonlocality rather than disputing the bill.

**GRW / CSL** — make the sufficing reason a *dynamical law*, promoting the non-injective semigroup from emergent to fundamental. Coherent, and the only position here that is empirically distinguishable at the level of mechanism.

**Relational QM / QBism** — facts are pointings relative to a system. Closest to the present account, and constrained by the extended Wigner's-friend results: Frauchiger–Renner, and the Local Friendliness theorem of Bong et al., whose assumptions are strictly weaker than Bell's. Any relative-facts view owes an explicit statement of which assumption it drops.

**This account.** Collapse is not a process. It is a **change of type**: from a state on a noncommutative algebra to a measure on the spectrum of a commutative subalgebra. Asking when it happens is asking for a temporal location for a type change — the category error both Copenhagen and Everett inherit from treating one species of reason as the only species.

**Where decoherence sits.** Environmental einselection explains **which** commutative subalgebra is the readout context — a dynamical answer to *which restriction map*. It does not supply a point of the resulting spectrum. Decoherence is the theory of the choice of $\mathcal{D}$, not the theory of the pointing. Stating this cleanly removes a long-running equivocation.

---

## 8. The research programme

Six targets, ordered by tractability, each stated so that failure is visible.

**C1. Identify the behavior functor.** For a wall $(\mathcal{M},\omega,\mathcal{V}(\mathcal{M}))$, construct $F$ such that a coalgebra $\gamma: X\to F(X)$ is exactly *select a commutative context and obtain a measure on its spectrum*. Abramsky's representation of physical systems as Chu spaces and coalgebras is the existing attempt and the correct starting point. Likely shape: a context-indexed composite of the distribution monad with the spectrum construction.

**C2. Nonemptiness.** Determine whether $F$ admits only nonempty coalgebras, via the terminal sequence and compactness (§6.4). This is the formal version of the fold's payoff.

**C3. Bisimulation equals operational indistinguishability.** Prove that coalgebraic bisimulation on the wall category coincides with physical equivalence of states. Probabilistic bisimulation (Larsen–Skou) is the classical template. If these come apart, the identity criterion is wrong and C1 needs redoing.

**C4. The semigroup bridge.** Match the iterated coalgebra structure to a half-sided modular inclusion or an $E_0$-semigroup. This is the load-bearing link between the behavioral and operator-algebraic halves. *Arveson's theory and the coalgebra literature have never cited each other, and each has what the other lacks: Arveson the classification of irreversible one-parameter quantum dynamics, coalgebra the behavioral identity criterion.* Highest value on this list.

**C5. Orientation as a global section.** Show the arrow is coherently oriented across walls, not merely locally (§5). Failure means regions with opposed arrows and no shared past.

**C6. Normality.** Determine whether the non-normality of characters (§6.3) is eliminable — whether facts can be realized as physically preparable states, or whether the framework is committed to facts that exist without being preparable.

---

## 9. Kill conditions

**K1. A derivation of the Born rule from unitarity alone**, non-circular, would show one species of reason suffices and collapse this account into Everettianism.

**K2. A local non-contextual hidden-variable model** reproducing quantum statistics would show sufficing reason reduces to necessitating reason. Bell and Kochen–Specker currently forbid it; a loophole is fatal here.

**K3. Dimension two.** Gleason fails for $\dim\mathcal{H}=2$; non-Born frame functions exist. The framework *requires* $\dim\ge3$ — a constraint, not an assumption.

**K4. A complete dynamical account of which $\mathcal{D}$**, exhausting the transition, would reduce this to decoherence plus bookkeeping.

**K5. Local Friendliness.** A relative-facts account must name the assumption it abandons. Failure to do so is inconsistency, not an exposition gap.

**K6. No functor satisfying C1** that is both natural under change of wall and recovers quantum statistics. The coalgebraic framing is then a mismatch of level.

**K7. Bisimulation and operational indistinguishability come apart** (C3 fails). Coinduction is then the wrong identity criterion for facts.

**K8. The terminal sequence is non-compact with empty limit** (C2 fails). *Nothing* is then an option for structures of this kind, and the fold delivers no necessity.

**K9. No semigroup bridge** (C4 fails). The behavioral and algebraic accounts of the arrow are two pictures rather than one, and the programme is a pair of analogies.

**K10. Non-normality proves ineliminable** (C6 fails). Facts then exist only in a sense with no physical realization, and §6.2's guarantee is technically true and empty.

---

## 10. What is claimed, and what remains

**Claimed.** That *when does collapse happen* is malformed. That Copenhagen and Everett are answers to a badly typed question. That Bell and Kochen–Specker are not paradoxes but the proof that two species of ground are required. That the arrow of time is the failure of a monoid to be a group — a property of an algebra rather than of a boundary condition, and therefore not vulnerable to the fluctuation objections that kill statistical derivations. That facticity is entailed by the existence of the algebra, via MASA plus Gelfand.

**Remaining.** Three debts, in decreasing size.

*Why a point at all.* Even granting the type distinction, nothing here explains why the measure is realized — why one character rather than the measure itself obtains. Now localized to the normality question of §6.3, which is smaller and better placed than the measurement problem, but not dissolved.

*Which restriction.* The account says facts are relative to a context and does not say what selects it. Decoherence is the leading candidate and is not obviously complete.

*Shared orientation.* An arrow per wall is not yet one arrow. C5.

---

## Appendix A. Dictionary

| Informal | Formal |
|---|---|
| pre-observable | noncommutative algebra $\mathcal{M}$; type III$_1$ in QFT |
| observable context | commutative subalgebra $\mathcal{D}\subset\mathcal{M}$ |
| a fact | a character $\chi:\mathcal{D}\to\mathbb{C}$; a point of $\mathrm{Spec}(\mathcal{D})$ |
| existence | multiplicativity (not extremality) |
| an observer | a choice of trivialization; a pointing |
| necessitating reason | initial algebra; group action; determines a character |
| sufficing reason | final coalgebra; state; determines a measure, no character |
| identity of facts | bisimulation |
| the Born rule | Gleason's theorem, $\dim\ge3$ |
| irreducibility of the two reasons | Bell; Kochen–Specker |
| no global classical section | spectral presheaf has no global points |
| arrow of time | endomorphism semigroup; failure of a monoid to be a group |
| canonical dynamics | Connes' modular flow in $\mathrm{Out}(\mathcal{M})$ |
| the fold | $Z\cong F(Z)$; Lambek's lemma |
| loss per step (discrete) | $\log(\text{geometric degree})$; algebraic entropy |

## Appendix B. Sources

Gelfand & Naimark (1943). — Gleason, *J. Math. Mech.* 6 (1957) 885. — Kochen & Specker (1967). — Bell (1964). — Lambek, *A fixpoint theorem for complete categories*, Math. Z. 103 (1968). — Bisognano & Wichmann, *J. Math. Phys.* 16 (1975). — Connes, cocycle theorem and classification of type III factors. — Aczel, *Non-Well-Founded Sets*, CSLI 1988. — Adámek, terminal sequence construction (1974). — Larsen & Skou, *Inf. Comput.* 94 (1991). — Wiesbrock, *Comm. Math. Phys.* 157 (1993); Borchers. — Connes & Rovelli, *Class. Quantum Grav.* 11 (1994). — Price, *Time's Arrow and Archimedes' Point*, OUP 1996. — Isham & Butterfield, *Topos perspective on the Kochen–Specker theorem* I–IV (1998–2002). — Rutten, *Universal coalgebra*, TCS 249 (2000) 3. — Arveson, *Noncommutative Dynamics and E-Semigroups*, Springer 2003. — Sokolova, *Probabilistic systems coalgebraically*, TCS 412 (2011). — Abramsky, *Big Toy Models*, Synthese 186 (2012) 697; *Coalgebras, Chu spaces, and representations of physical systems*, J. Phil. Logic 42 (2013) 551. — Jacobs, *Introduction to Coalgebra*, CUP 2016. — Bong et al., *A strong no-go theorem on the Wigner's friend paradox*, Nat. Phys. 16 (2020) 1199.

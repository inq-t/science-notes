# The Algebraic Arrow of Time

An algebraic arrow is not produced by noncommutativity or observational restriction alone. It requires a one-sided action—such as an endomorphism semigroup preserving an observable algebra only for one sign of its parameter. Half-sided modular inclusions provide a rigorous candidate, but connecting their parameter and inclusion structure to physical fact formation remains open.

## Three maps that must be distinguished

For a von Neumann algebra $\mathcal M$ with faithful normal state $\omega$, modular evolution is an automorphism group

$$
\sigma_t^\omega(A)
=\Delta_\omega^{it}A\Delta_\omega^{-it},
\qquad t\in\mathbb R.
$$

It is reversible. Noncommutativity supplies incompatibility of observables, not a temporal orientation. This agrees with [[wall-construction-interface/vertical-and-horizontal-motion|the distinction between modular flow and deformation through a family of states]].

For an inclusion $i:\mathcal D\hookrightarrow\mathcal M$, the canonical observational operation is restriction of states,

$$
i^*:S(\mathcal M)\to S(\mathcal D),
\qquad
i^*(\omega)=\omega|_{\mathcal D}.
$$

This map is generally many-to-one, because states differing only on noncommuting observables can agree on $\mathcal D$. It has no canonical inverse. But it is not, merely for that reason, a temporal evolution.

A map $\Pi:\mathcal M\to\mathcal D$ is additional structure, typically a conditional expectation when one exists. Not every inclusion admits a state-preserving conditional expectation, and no canonical choice is supplied by the inclusion alone. The phrases “projection to the commutative shadow” and “restriction to a context” must therefore not be interchanged.

## One-sided endomorphisms

An $E_0$-semigroup is a family of normal unital *-endomorphisms

$$
\alpha_t:\mathcal M\to\mathcal M,
\qquad t\ge0,
$$

with $\alpha_{s+t}=\alpha_s\circ\alpha_t$ and suitable continuity. If the endomorphisms are not automorphisms of the fixed algebra, the parameter has a genuine one-sided algebraic role.

For a half-sided modular inclusion $\mathcal N\subset\mathcal M$ with a common cyclic and separating vector $\Omega$, one has, for one choice of sign,

$$
\Delta_{\mathcal M}^{it}\mathcal N\Delta_{\mathcal M}^{-it}
\subseteq\mathcal N.
$$

Under the standard hypotheses, the inclusion generates a positive-energy translation group $U(a)$ on the Hilbert space. The full $U(a)$ is reversible, but its action preserves a chosen algebra by inclusion only on one half-line. Relative to that algebra, one obtains a semigroup of endomorphic inclusions. This is the precise sense in which a group at the ambient level can induce one-sided action on an observable region.

The observer/wall structures needed to instantiate such an inclusion are part of [[wall-construction-interface/inq|the wall-construction interface]], not consequences of modular theory alone.

## A norm-preserving arrow can still be one-sided

There is an exact Hilbert-space prototype between reversible groups and
record algebras. For any contraction $A:\mathcal H\to\mathcal K$,

$$
V_Ax=Ax\oplus(I-A^*A)^{1/2}x
$$

is an isometry into the survivor-plus-defect carrier. Its codomain is minimal
among isometric completions, and $V_A$ is onto exactly when $A$ is a
coisometry. Hence a nonidentity positive same-carrier transfer has a proper
isometric completion: it preserves norm but does not form a group on the
enlarged carrier. [[directed-isometric-residue-completion/inq|The full
completion theorem]] proves the changing-carrier cascade and its stationary
continuous-depth form.

This sharpens but does not finish the arrow-of-time proposal. A proper
isometry has an adjoint left inverse on its range, so non-surjectivity says
that not every final tuple is a compatible history; it does not prove that a
compatible history is physically unrecoverable. Wold shift structure and
pointwise decay are also weaker than a spectral gap. Ontological time still
requires a physically instantiated record inclusion or another rule that
restricts admissible reversal, while a mass gap requires a uniform residue
floor at finite physical depth.

## Programme claim

The proposed formula is

$$
\text{objective temporal orientation}
\quad\rightsquigarrow\quad
\text{physically instantiated monoid action that does not extend to a group on the accessible algebra}.
$$

To become an account of time, the semigroup must act on physically identified observables or records, its parameter must be related to objective succession, and the direction must be compatible among observers. Without those bridges, “the arrow is a monoid that is not a group” is a structural criterion, not a derivation of the experienced arrow.

## Keller maps as a limiting analogy

Polynomial Keller maps have everywhere nonzero constant Jacobian determinant and are therefore locally invertible in the étale sense. If a non-automorphic Keller self-map exists, iteration would give a monoid with global noninvertibility despite locally invertible tests; geometric degree would multiply under composition.

This illustrates local invertibility without known global invertibility. It does not model a locally detectable arrow, and it supplies no bridge to modular inclusions or quantum observation. Half-sided modular inclusion is therefore not established as a continuous version of the Keller phenomenon; the two share only a formal contrast between ambient reversibility and one-sided global structure.

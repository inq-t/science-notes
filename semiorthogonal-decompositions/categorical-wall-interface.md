# From a Categorical Wall to an Analytic Wall

An admissible semiorthogonal projector is an exact model of categorical selection, but it lacks the operator order, positivity, topology, and state data required of a quantum operation. The programme should therefore seek a realization theorem carrying the categorical decomposition into \(C^*\)- or von Neumann algebraic data, rather than identifying a projection functor with a conditional expectation by analogy.

## What the categorical stage returns

Suppose an enhanced category has an admissible decomposition

$$
\mathcal T=\langle\mathcal A,\mathcal B\rangle.
$$

Then the retained component projection and its endoprojector are

$$
\pi_{\mathcal A}:\mathcal T\longrightarrow\mathcal A,
\qquad
P_{\mathcal A}:=i_{\mathcal A}\pi_{\mathcal A}:\mathcal T\longrightarrow\mathcal T.
$$

They are exact, satisfy \(\pi_{\mathcal A}i_{\mathcal A}\simeq\operatorname{id}_{\mathcal A}\) and \(P_{\mathcal A}^2\simeq P_{\mathcal A}\), and kill \(\mathcal B\). Equivalently, under the standard enhanced hypotheses,

$$
\mathcal T/\mathcal B\simeq\mathcal A.
$$

This is enough to say which categorical sector survives the chosen presentation. It is not enough to assign probabilities, relative entropy, or BKM response.

## Why it is not yet a quantum channel

A dg or triangulated category has addition and exact triangles, but no canonical:

- involution \(*\);
- positive cone;
- operator norm or weak operator topology;
- normal state;
- complete-positivity notion for its projection functors; or
- modular automorphism group.

By contrast, the analytic wall presently used in [[spectral-wall-descent/conditional-expectation-balance|conditional expectation balance]] requires a von Neumann inclusion

$$
\mathcal N\subseteq\mathcal M,
$$

a faithful normal state \(\varphi\), and a normal unital completely positive idempotent

$$
E:\mathcal M\longrightarrow\mathcal N,
\qquad
\varphi\circ E=\varphi.
$$

For the state-preserving conditional expectation supplied by Takesaki's theorem, one must also prove

$$
\sigma_t^\varphi(\mathcal N)=\mathcal N
\qquad(t\in\mathbb R).
$$

Semiorthogonality neither implies nor evades this modular invariance condition.

## The realization obligation

A useful theorem would begin with a concrete enhanced category \(\mathcal T\) attached to the project's degeneration and construct analytic data functorially. Schematically, one needs

$$
\operatorname{Real}:
(\mathcal T;\mathcal A,\mathcal B)
\longrightarrow
(\mathcal M,\mathcal N,E,\varphi)
$$

with proofs of the following compatibilities:

| Categorical datum | Analytic target | Required proof |
|---|---|---|
| dg/stable enhancement | \(C^*\)-, von Neumann, or \(KK\)-theoretic realization | functoriality and completion |
| admissible component \(\mathcal A\) | observable algebra or correspondence | closure under \(*\), products, and topology |
| component projection \(\pi_{\mathcal A}:\mathcal T\to\mathcal A\) | map \(E:\mathcal M\to\mathcal N\) | normality, unitality, complete positivity, and state preservation |
| endoprojector \(P_{\mathcal A}=i_{\mathcal A}\pi_{\mathcal A}\) | \(\iota_{\mathcal N}E:\mathcal M\to\mathcal M\) | compatibility of the two idempotent endomorphisms under realization |
| categorical kernel \(\mathcal B\) | distinctions removed by \(E\) | a typed comparison, not identification with a linear kernel or ideal |
| duality or trace | faithful normal state \(\varphi\) | positivity, normalization, faithfulness |
| equivariance or monodromy | modular covariance | \(\sigma_t^\varphi(\mathcal N)=\mathcal N\) or a declared replacement |
| additive cyclic class | JLO or \(K\)-homology class | spectral triple, summability, domains, and pairing compatibility |

Without this theorem, “categorical wall” is a precise proposal for the first stage and no more.

## Conditional expectation is not a categorical quotient

A Verdier or dg quotient makes every object of \(\mathcal B\) zero and universally inverts the appropriate morphisms. A conditional expectation usually satisfies neither multiplicativity nor a quotient universal property:

$$
E(xy)\ne E(x)E(y)
$$

in general. Its kernel need not be an ideal, and its BKM-orthogonal complement is state-dependent. Consequently,

$$
\mathcal T/\mathcal B\simeq\mathcal A
$$

cannot simply be rewritten as

$$
\mathcal M/\ker E\simeq\mathcal N.
$$

The categorical and analytic arrows may realize the same selection only after a comparison construction proves that they do.

## The BKM obligation

Given a faithful state, BKM geometry lives on tangent directions to the faithful-state manifold of an operator algebra. A categorical projector has no BKM adjoint or Pythagorean law until the state-space realization exists.

The target equality is of the form

$$
g^{\mathrm{BKM},\mathcal M}_\varphi(X,Y)
=
g^{\mathrm{BKM},\mathcal N}_\varphi(EX,EY)
+
g^{\mathrm{BKM},\mathcal M}_\varphi((1-E)X,(1-E)Y),
$$

under the hypotheses that make the expectation orthogonal for the BKM form. Nothing in

$$
\operatorname{RHom}(\mathcal B,\mathcal A)=0
$$

alone implies this equality. Derived orthogonality and information-geometric orthogonality are differently typed relations.

## Additive invariants, JLO, and index

For a smooth proper dg category with a semiorthogonal decomposition, additive invariants can split. In particular, under the standard hypotheses,

$$
HH_*(\mathcal T)
\cong
HH_*(\mathcal A)\oplus HH_*(\mathcal B),
$$

with analogous additivity for algebraic \(K\)-theory.

A JLO cocycle is more specific. It is constructed from a theta-summable analytic cycle or spectral triple using heat operators and commutators. An abstract semiorthogonal component carries no canonical operator \(D\), heat kernel \(e^{-tD^2}\), or representation on a Hilbert space. Therefore the passage

$$
\text{semiorthogonal component}
\dashrightarrow
\operatorname{Ch}_{\mathrm{JLO}}(D)
$$

is an open analytic realization, not a consequence of semiorthogonality.

This makes [[library/hodge-atoms-spectral-triples-bps/entry|the Hodge-atoms source]] relevant but non-load-bearing. It proposes that a Kuznetsov component is a dynamically protected phase and brings JLO language into the same picture. The one-sided Ext vanishing is categorical mathematics; the tunnelling selection rule and the claimed JLO localization are conjectural. [[spectral-wall-descent/index-and-curvature-transgression|Index and curvature transgression]] supplies the canonical analytic target once a suitable spectral triple has actually been constructed.

## The \(A_2\) bridge programme

The following sequence would turn the current analogy into a theorem programme:

1. attach a dg category of vanishing cycles, matrix factorizations, or sheaves to the actual \(A_2\) degeneration in [[algebra/a2-inverse-cover|the inverse-cover geometry]];
2. identify an admissible semiorthogonal component selected by the degeneration or real structure;
3. construct its mutation and monodromy action, distinguishing invertible transport from quotient selection;
4. realize the selected component as an operator algebra, correspondence, or spectral triple;
5. construct a faithful state and prove complete positivity and modular admissibility of the analytic wall; and
6. show that the resulting BKM split, JLO character, and index pairing are compatible images of the same categorical decomposition.

This programme is worth pursuing precisely because it prevents the final operator-algebraic expectation from being chosen arbitrarily. Algebraic geometry would select the sector; analysis would determine whether that selection can become a physical wall.

## Failure tests

The proposed bridge fails if any of the following occurs:

- the relevant subcategory is not admissible, so no functorial projector exists;
- the \(A_2\) category is chosen by analogy rather than constructed from the actual degeneration;
- mutation is called information loss even though it is an equivalence on components;
- the analytic realization does not preserve the \(*\)-operation or positivity;
- no faithful normal state makes the observable algebra modularly invariant;
- the categorical quotient is confused with the kernel of a conditional expectation;
- Hochschild additivity is reported as a JLO or BKM theorem; or
- a one-sided Ext vanishing is promoted to a dynamical tunnelling prohibition without a Hamiltonian, stability condition, or amplitudes.

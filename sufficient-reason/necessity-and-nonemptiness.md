# Necessity, Nonemptiness, and Realizability

Every nonzero unital commutative C\*-algebra has characters, and every nonzero von Neumann algebra contains a maximal abelian subalgebra. These facts guarantee the availability of point-bearing contexts. They do not guarantee that one character is actualized, that it is a normal state, or that a physical procedure can prepare it.

## A context has points

Let $\mathcal D$ be a nonzero unital commutative complex Banach algebra. A maximal ideal exists, and the quotient by a maximal ideal is $\mathbb C$ under the hypotheses used in the Gelfand theory. Equivalently, the character space is nonempty. For a commutative unital C\*-algebra,

$$
\mathcal D\cong C(X)
$$

with $X$ nonempty and compact Hausdorff.

The implication is exact:

$$
\text{nonzero unital commutative observable algebra}
\quad\Longrightarrow\quad
\text{at least one algebraic point}.
$$

## A noncommutative algebra has contexts

Every nonzero unital von Neumann algebra $\mathcal M$ contains a maximal abelian self-adjoint subalgebra $\mathcal D$, obtained by a maximality argument on its unital abelian *-subalgebras. Combining the two results gives

$$
\mathcal M\ne0
\quad\Longrightarrow\quad
\exists\mathcal D\subseteq\mathcal M
\quad\Longrightarrow\quad
\operatorname{Spec}(\mathcal D)\ne\varnothing.
$$

This proves that point-bearing contexts are structurally available. The stronger sentence “the algebra entails that a fact occurs” adds an actuality principle not contained in either theorem.

## Normality is the physical fault line

In a type III factor, a MASA is diffuse: it has no minimal projections. Its characters exist as C\*-algebraic functionals, but they are not normal. A normal pure state on a commutative von Neumann algebra would correspond to an atom, and diffuse algebras have none.

Hence:

$$
\text{character exists}
\not\Longrightarrow
\text{normal character exists}
\not\Longrightarrow
\text{character is preparable or realized}.
$$

The first failure is theorem-level in the diffuse case. The second implication requires a physical theory of preparation and outcome, not only operator algebra.

## Terminal sequences

For an endofunctor $F$ on a category with terminal object $1$, a candidate final coalgebra may be approached through the terminal sequence

$$
1\longleftarrow F(1)\longleftarrow F^2(1)\longleftarrow\cdots.
$$

Nonempty stages do not alone guarantee a nonempty inverse limit in arbitrary categories. In a compact-Hausdorff setting, a directed inverse system of nonempty compact spaces with continuous bonding maps has a nonempty limit. This suggests a precise route:

$$
\text{prove all stages nonempty and compact}
\;\Longrightarrow\;
\text{prove the terminal limit nonempty}.
$$

Unitality makes the spectrum of each nonzero commutative unital C\*-algebra compact and nonempty. It does not by itself prove that the stages of the still-unknown observation functor are such spectra, that $F$ preserves the required structure, or that the limiting coalgebra describes actual facts.

## What becomes of “nothing”

The metaphysical question separates into three mathematical questions:

1. **Availability:** does an algebra contain a point-bearing context? For nonzero unital von Neumann algebras, yes.
2. **Behavioral nonemptiness:** does the proposed observation functor have a nonempty final coalgebra? Open until $F$ is constructed and its terminal sequence controlled.
3. **Actuality:** why is one character realized rather than only a probability law? Not answered by nonemptiness.

The first result sharply constrains the problem. It does not collapse possibility, behavioral existence, and actuality into one notion.

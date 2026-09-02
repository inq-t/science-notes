# Holomorphic Wave Functions and Complex Integrals

Complex geometry can carry quantum states in holomorphic representations, but a complex manifold does not by itself define a quantum theory. The exact connection is representational: after a positive Hilbert norm, bundle, and operator action are supplied, state vectors may be realized as holomorphic functions or sections. Complex amplitudes, integration over a complex domain, holomorphic period integrals, and path integrals over complexified cycles are four different constructions and must not be collapsed into one phrase.

## Four meanings of “complex integral”

The adjective *complex* can modify different parts of an amplitude:

1. A **complex-valued amplitude** is simply a map into \(\mathbb C\); no contour or complex manifold is thereby implied.
2. A **real integral over a complex domain** integrates a nonholomorphic density over the underlying real \(2n\)-manifold of \(\mathbb C^n\). The Bargmann norm is of this type because it contains \(\overline F\) and \(e^{-|z|^2}\).
3. A **holomorphic contour or period integral** pairs a holomorphic form with a real cycle, for example \(\int_\gamma\Omega\). Its periods can undergo monodromy.
4. A **path integral over a complexified cycle** integrates an exponential weight over an infinite-dimensional or finite-dimensional cycle selected after complexification, often using Picard--Lefschetz theory.

Wave functions universally take values in a complex vector space in ordinary quantum theory. They do not universally depend on the last three kinds of integral. The interesting claim is more exact: complex geometry supplies natural representations, sections, cycles, and analytic continuation laws from which such quantum constructions can be built.

## A concrete model: Bargmann--Fock space

For \(n\) oscillator degrees of freedom, the Bargmann--Fock space is

$$
\mathcal H_{\mathrm{BF}}
:=
\left\{
F\in\mathcal O(\mathbb C^n):
\frac{1}{\pi^n}
\int_{\mathbb C^n}
|F(z)|^2e^{-|z|^2}\,\mathrm d^{2n}z
<\infty
\right\}.
$$

Its inner product is

$$
\langle F,G\rangle
=
\frac{1}{\pi^n}
\int_{\mathbb C^n}
\overline{F(z)}G(z)e^{-|z|^2}\,\mathrm d^{2n}z.
$$

The Bargmann transform is a unitary integral transform from an ordinary Schrödinger \(L^2(\mathbb R^n)\) representation to this holomorphic representation. The same abstract quantum state therefore has both a real-coordinate wave function and a holomorphic wave function. Complex analyticity is not an extra force; it organizes the state space, creation and annihilation operators, reproducing kernels, and continuation.

This example makes two points exact:

1. A wave function may genuinely be holomorphic data on a complex space.
2. The Hilbert space comes from holomorphicity **plus** a measure and positivity condition. Holomorphicity alone is insufficient.

## Functions are often the wrong global type

On every connected compact complex manifold, global holomorphic functions are constant. Quantum states on a compact complex phase space are therefore not modeled by arbitrary scalar functions \(X\to\mathbb C\). In conventional geometric quantization they are polarized sections of a prequantum line bundle,

$$
\psi\in\Gamma_{\mathrm{pol}}(X,L),
$$

possibly with a half-form correction. The bundle \(L\), its Hermitian structure and connection, the symplectic integrality condition, the polarization, and the inner product all carry mathematical content.

There is a decisive obstruction for the smooth six-sphere itself. Since

$$
H^2(S^6;\mathbb R)=0,
$$

every closed two-form on \(S^6\) is exact. If a symplectic form obeyed \(\omega=\mathrm d\alpha\), then compactness and Stokes' theorem would give

$$
\int_{S^6}\omega^3
=
\int_{S^6}\mathrm d(\alpha\wedge\omega^2)
=0,
$$

contradicting positivity of the symplectic volume. Thus conventional Kostant geometric quantization cannot take \(S^6\) itself as its symplectic phase space. Holomorphic bundles, torus-fiber periods, boundary state spaces, and operator-algebraic constructions remain possible, but they would be different routes.

Consequently, saying that a complex \(S^6\) “supports wave functions” means only that it supports complex-analytic types from which a state representation might be constructed. Scalar holomorphic functions on \(S^6\) do not already constitute the physical Hilbert space.

## Cycles, monodromy, and complexified paths

A cycle-dependent amplitude can have the schematic form

$$
\mathcal A_\Gamma(\lambda)
=
\int_{\Gamma(\lambda)}
e^{-S(z;\lambda)/\hbar}\Omega(z;\lambda).
$$

As parameters \(\lambda\) move around a discriminant, admissible cycles can undergo Picard--Lefschetz transport. A basis of amplitudes can therefore return mixed by a monodromy matrix even when the local differential expression for the integrand has returned to its original form.

This is the rigorous kernel of the intuition that twisting around a singularity can generate complexity: nontriviality may live in the local system of cycles or branches rather than in a new local equation. Witten's analytic continuation of Chern--Simons theory is a primary physical example in which complexified integration cycles and Picard--Lefschetz theory organize a path integral. It does not imply that the \(S^6\) manuscript realizes that theory.

## What the integrable \(S^6\) geometry supplies

[[algebra/s6-manuscript-branch|The integrable \(S^6\) construction]] supplies:

- a complex threefold, hence a \((p,q)\)-decomposition of differential forms and a Dolbeault complex;
- a holomorphic fibration by complex two-tori over a punctured complex curve;
- explicit period functions and a period matrix;
- monodromy around two elliptic points and a cusp;
- logarithmic transformations and a toric degeneration; and
- a non-normal cusp fiber built from an \(A_2\)-triangulation.

The first item is not automatically a Kähler Hodge decomposition of de Rham cohomology. These structures are natural inputs for sheaves of sections, Gauss--Manin transport, determinant lines, period integrals, and monodromy representations. They are not yet:

- a Hilbert space with positive inner product;
- a represented observable algebra;
- a Hamiltonian, modular generator, or Dirac operator;
- a measure on histories;
- a Born rule or instrument; or
- a physical state-selection operation.

## Atemporal interpretation

The amplitude \(\mathcal A_\Gamma\) may compare complete configurations or assign an amplitude to a boundary-value problem. Its integration variable need not be an ontological clock. Even when a conventional path integral is written using a time-dependent action, its fundamental mathematical return value can be a boundary amplitude or functorial assignment.

The programme may therefore seek an atemporal complex presentation whose spectral and integral structures are later realized as time-indexed predictions. This is compatible with the claim that ordinary QFT equations describe how the deeper structure presents itself in a Lorentzian regime. It is not evidence for that claim until the boundary/state functor and its Lorentzian recovery are constructed.

## Construction target

A precise quantum bridge from a complex threefold \(X\) would have to return at least

$$
\mathfrak Q(X)
=
(\mathcal O_X,\mathcal M_X,\mathcal H_X,\pi_X,D_X,\varphi_X,\mathcal I_X),
$$

where \(\mathcal O_X\) is declared holomorphic coordinate or sheaf data; \(\mathcal M_X\) is a represented \(C^*\)- or von Neumann observable algebra; \(\pi_X\) is the completion or representation map relating them; \(\mathcal H_X\) is a positive Hilbert completion; \(D_X\) is a spectral generator; \(\varphi_X\) is a faithful state in the category where the proposed BKM geometry exists; and \(\mathcal I_X\) is a declared amplitude or integration-cycle construction. Functoriality must show how monodromy and degeneration act on every component.

Without this typed return, “wave functions live on the complex \(S^6\)” is an evocative possibility rather than a theorem.

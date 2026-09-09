# The Oriented Source Lift Is Not Positive Conditional Averaging

The source correction selected by the four-face kinetic operator has a sign-indefinite product defect. A nonnegative invariant square acquires a negative first-order value at one configuration. Consequently this complete multiplier lift cannot be the first jet of a positive conditional comparison on the same commutative configuration algebra. The obstruction appears only when composite sources are retained; it does not challenge positivity of the actual physical transfer.

**Status: exact algebraic positivity obstruction for the specified first source jet.** [[four-face-oriented-normal-form-and-the-universal-source-lift|The universal lift]] constructs the real odd formally skew-adjoint operator \(S_1\) on invariant polynomial-Gaussian vectors. [[four-face-source-products-and-the-oriented-contact|The product calculation]] evaluates its contact. The fixed four-face carrier, comb paths and actual odd kinetic coefficient remain inputs.

## Positivity constrains the first product defect

Let \(\mathscr A\) be a real algebra of configuration functions containing constants and the polynomials below. Suppose \(\Phi_h:\mathscr A\to\mathscr A\) is linear, unital and positive on pointwise nonnegative squares, for \(h>0\). At each configuration \(x\), positivity of \((F-a)^2\) for every real \(a\) gives
\[
\Phi_h(F^2)(x)-2a\Phi_h(F)(x)+a^2\ge0.
\]
Minimizing in \(a\) proves the pointwise Schwarz inequality
\[
\Phi_h(F^2)-(\Phi_hF)^2\ge0.
\tag{PX1}
\]
This argument needs no bounded-operator completion.

If, on the displayed tests and at each fixed configuration,
\[
\Phi_hF=F+h\mathcal D(F)+o(h),\qquad
\mathcal D(1)=0,
\]
then (PX1) forces
\[
\boxed{\Gamma_{\mathcal D}(F,F)
:=\mathcal D(F^2)-2F\mathcal D(F)\ge0.}
\tag{PX2}
\]
Equivalently, a nonnegative \(f\) with \(f(x)=0\) must have \(\mathcal D(f)(x)\ge0\). This is a necessary condition for a positive comparison with the prescribed local jet, not an assertion that an arbitrary formal differential operator generates a process.

## The selected kinetic lift violates that condition

On the four-face polynomial-Gaussian core define
\[
\mathcal D(F)=\Omega^{-1}[S_1,M_F]\Omega,\qquad
[K_0,S_1]=-V_1.
\]
The only third-derivative term in \(S_1\) is
\[
-\frac47\mathcal P,\qquad
\mathcal P=\partial_0\cdot(\partial_1\times\partial_2).
\]
Every other term is a divergence-free first-order vector field. Put
\[
F_0=|Y_0|^2,\qquad F_1=|Y_1|^2,\qquad
T=Y_0\cdot(Y_1\times Y_2).
\]
The exact contact identities are
\[
\Gamma_{\mathcal D}(F_0,F_0)
=\Gamma_{\mathcal D}(F_1,F_1)=0,\qquad
\Gamma_{\mathcal D}(F_0,F_1)=\frac47T.
\tag{PX3}
\]
For \(A=F_0+F_1\), symmetry and bilinearity give
\[
\boxed{\Gamma_{\mathcal D}(A,A)=\frac87T.}
\tag{PX4}
\]
This changes sign on the physical configuration quotient: simultaneous \(SO(3)\) rotations preserve the oriented triple, and configurations of both signs exist.

There is an explicit nonnegative witness. Choose
\[
Y_0=e_1,\qquad Y_1=e_2,\qquad
Y_2=-e_3,\qquad Y_3=0,\qquad f=(A-2)^2.
\]
Here \(A=2\), \(T=-1\), and
\[
\boxed{f=0,\qquad
\mathcal D(f)=2(A-2)\mathcal D(A)+\Gamma_{\mathcal D}(A,A)
=-\frac87.}
\tag{PX5}
\]
Thus \(\Phi_h f=-8h/7+o(h)<0\) at this configuration, contradicting positivity. No unital positive multiplier map has this first jet on these tests.

The witness is invariant under the full simultaneous Gauss action. Its evaluation is a statement about a local polynomial jet. If a bounded smooth version is required, multiply the square by a nonnegative invariant cutoff equal to one near that orbit. Since \(\mathcal D\) is a local differential operator of order three, the value in (PX5) is unchanged. The obstruction does not assume that an unbounded polynomial is a bounded compact observable.

## Quadratic agreement alone would miss the obstruction

For a scalar quadratic \(F\), the third derivative of \(F\) vanishes. Its mixed second derivatives are multiples of the color identity, so their alternating contractions also vanish. Consequently \(\mathcal D\) restricted to all ten scalar quadratics agrees with a first-order vector field. That vector field can have a locally multiplicative coordinate flow even though it gives a different quartic response.

The impossibility therefore concerns the **complete specified source lift**, including \(F^2\), rather than all positive maps matching its quadratic values. The compact mixed-source experiment in [[oriented-source-products-and-the-compact-contact-return]] detects precisely this missing product information. The constant \(4/7\) is fixed by the original kinetic rows, not adjusted after selecting the witness.

## Retaining differential observables preserves composition

The full first-order operator lift is
\[
\mathscr L_h(F)=M_F+h[S_1,M_F].
\]
Because a commutator is a derivation,
\[
\mathscr L_h(FG)
=\mathscr L_h(F)\mathscr L_h(G)+O(h^2)
\tag{PX6}
\]
on the polynomial core. For real \(F\), \([S_1,M_F]\) is formally symmetric. In particular the image of \(F^2\) is the formal square of the image of \(F\), through this order. The contact appears when each differential operator is replaced by a multiplication operator with the same action on \(\Omega\).

Equation (PX6) is an algebraic alternative, not a constructed positive bounded channel or a globally defined unitary. Domain, closure and the compact operator realization still need proof. A first-order deformation of the multiplier product can also retain the contact, as the product owner shows, but its ordinary pointwise positive cone cannot simply be inherited.

The conditional comparison in [[auxiliary-boundary-sufficiency-and-the-wilson-source-algebra|AS]] has a nonnegative same-source variance defect. Its source compression and the present normal-form lift are different maps. Identifying them would fail (PX4)–(PX5). The actual chronological transfer remains unchanged and positive. Within oriented innovation transport, this result requires a candidate complete source law to retain its differential or boundary information, or supply a different justified realization. It supplies no new mass term or physical gap bound.

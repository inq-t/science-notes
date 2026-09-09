# Variance-Completed Descent and Rigidity

A positive algebraic rigidity certificate can lose its gap when a comparison is passed through a completely positive readout. Keeping the discarded variance gives an exact composition law and identifies the additional estimate needed to preserve rigidity. A parallel calculation transports an explicitly constructed repair while retaining the channels discarded from both its analysis and its repair. The resulting mixed term admits two research routes: bound its accumulation or construct a correction that cancels it. The identities below are exact; their uniform realization by a Yang–Mills preparation remains to be constructed.

## The operation retains the failure to preserve multiplication

Let \(\Phi:\mathcal A\to\mathcal B\) be a unital completely positive map between unital \(C^*\)-algebras. For \(a,b\in\mathcal A\), define
\[
\Gamma_\Phi(a,b)=\Phi(a^*b)-\Phi(a)^*\Phi(b).
\tag{VC1}
\]
The matrix \([\Gamma_\Phi(a_i,a_j)]\) is positive for every finite family. In a Stinespring representation \(\Phi(a)=V^*\pi(a)V\), with \(V\) isometric,
\[
d_\Phi(a)=(I-VV^*)\pi(a)V,\qquad
\Gamma_\Phi(a,b)=d_\Phi(a)^*d_\Phi(b).
\tag{VC2}
\]
Thus a crossing can be represented by its retained image and a linear defect map. A minimal Stinespring choice is unique up to the appropriate unitary equivalence; it is not an additional physically selected reservoir.

[[directed-isometric-residue-completion/inq|Directed isometric residue completion]] gives the corresponding retained-plus-defect construction for Hilbert contractions. [[channel-loss-and-recovery/inq|Channel loss and recovery]] treats relative-entropy loss and sufficiency; that state divergence is a different response from the product defect in (VC1).

For another UCP map \(\Psi:\mathcal B\to\mathcal C\), expansion gives
\[
\boxed{\Gamma_{\Psi\Phi}(a,b)
=\Psi\!\left(\Gamma_\Phi(a,b)\right)
+\Gamma_\Psi(\Phi(a),\Phi(b)).}
\tag{VC3}
\]
The earlier loss is transported before the next loss is added. This is the operator-valued counterpart of conditional-variance decomposition. It is the relevant balance law, rather than an assertion that an unspecified scalar called information is conserved.

For self-adjoint \(R\), abbreviate \(V_\Phi(R)=\Gamma_\Phi(R,R)\). Call
\[
\mathfrak D_\Phi^{(2)}(R)
=\bigl(\Phi(R),V_\Phi(R)\bigr)
\tag{VC4}
\]
the **variance-completed readout** of \(R\). Its composition is governed by (VC3). The pair is sufficient for transporting quadratic identities in this one element. It does not retain every higher source product or determine an entire joint law. The source-bearing sewing programme must retain those higher products separately.

## Transport a finite-word certificate

Suppose a bounded positive comparison element \(R\) has an independently derived identity
\[
R^2-\kappa R=\sum_{j=1}^n b_j^*b_j,\qquad \kappa>0.
\tag{VC5}
\]
The \(b_j\) must be explicit finite linear combinations of words in declared primitive comparison generators. Defining one square by spectral functional calculus after assuming a gap would supply no explanation. [[library/noncommutative-real-algebraic-geometry-of-kazhdans-property-t/inq|Ozawa's theorem]] provides an established group-algebra precedent for this form of certificate, not a Yang–Mills construction.

Put \(A=\Phi(R)\). The complete transported pencil is
\[
\boxed{
A^2+V_\Phi(R)-\kappa A
=\Phi(R^2-\kappa R)
=\sum_j\Phi(b_j^*b_j)\ge0.}
\tag{VC6}
\]
Consequently, if the actual composed readout satisfies
\[
0\le V_\Phi(R)\le\varepsilon A,\qquad
0\le\varepsilon<\kappa,
\tag{VC7}
\]
then
\[
A^2\ge(\kappa-\varepsilon)A,\qquad
\sigma(A)\subset\{0\}\cup[\kappa-\varepsilon,\infty).
\tag{VC8}
\]
The proof is substitution in (VC6), followed by the continuous functional calculus of the positive element \(A\). It does not require \(A\) and \(V_\Phi(R)\) to commute.

The variance hypothesis can be as hard as the desired conclusion. For example, if \(R\) is a projection, then \(V_\Phi(R)=A-A^2\), so (VC7) itself becomes \(A^2\ge(1-\varepsilon)A\). The explanatory task is an independent derivation of the variance budget from the primitive relations, or the constructive repair below.

This transports the [[quantitative-descent/rigidity-certificates-and-soft-escape|generic algebraic certificate]] through a nonmultiplicative readout: the missing hypothesis is a bound on the discarded variance relative to the same retained response. The estimate must hold for the whole composed map. By (VC3), a bound paid independently at every cut can accumulate without limit. [[rg-covariance-residue/conditioned-source-transport|Conditioned source transport]] records the related covariance correction for actual renormalized source families.

Even (VC8) leaves the zero sector to be identified. A gauge-averaging action fixes all gauge-invariant observables, so its isolated kernel need not be the vacuum line. Moreover, \(\Phi(R)\) and the square of the compressed primitive analysis map are different objects. The next calculation keeps that distinction explicit.

## Transport the repair itself

Here all operators are bounded; unbounded versions require a common invariant core and separate domain control. Let \(\mathcal H\) have a unit vacuum vector \(\Omega\), put \(Q=I-|\Omega\rangle\langle\Omega|\), and take
\[
\delta:\mathcal H\to\mathcal H^{\oplus m},\qquad
B:\mathcal H^{\oplus m}\to\mathcal H,\qquad
B\delta=Q-E,
\]
\[
\delta\Omega=0,\qquad
\|B\|\le C,\quad C>0,\qquad
\|E\|\le\rho<1.
\tag{VC9}
\]
The intended \(B\) is assembled from local extension operations before any low spectrum is known. [[quantitative-descent/rigidity-certificates-and-soft-escape|The uncompressed repair theorem]] also allows a dense analysis domain; the bounded hypotheses here make the compression products everywhere defined. [[algebra/short-loop-holonomy-and-quantitative-gluing|Short-loop gluing]] is a worked example on a section carrier, including its failure after passage to neutral observables.

Let \(V:\mathcal H_c\to\mathcal H\) be the isometric pullback for an actual retained observable carrier, with \(V\Omega_c=\Omega\). Write \(P=VV^*\), \(V_m=I_m\otimes V\), and \(P_m=V_mV_m^*\). Define the compressed comparison and repair by
\[
\delta_c=V_m^*\delta V,\qquad B_c=V^*BV_m.
\]
Their discarded channels are
\[
L_\delta=(I-P_m)\delta V,\qquad
L_B=(I-P_m)B^*V.
\tag{VC10}
\]
Inserting \(P_m=I-(I-P_m)\) into \(B_c\delta_c\) gives the exact identity
\[
\boxed{
B_c\delta_c
=Q_c-V^*EV-L_B^*L_\delta,
\qquad Q_c=I-|\Omega_c\rangle\langle\Omega_c|.}
\tag{VC11}
\]
Their squared norms are the matrix-amplified compression variances:
\[
L_\delta^*L_\delta
=V^*\delta^*\delta V-\delta_c^*\delta_c,
\qquad
L_B^*L_B
=V^*BB^*V-B_cB_c^*.
\tag{VC12}
\]
The correction in (VC11) is a mixed product of two lost channels, not generally a positive operator. Its norm is at most
\(\eta_B\eta_\delta\), where \(\eta_B=\|L_B\|\) and
\(\eta_\delta=\|L_\delta\|\).

Since \(\|B_c\|\le C\), whenever
\(\rho+\eta_B\eta_\delta<1\), every \(f\perp\Omega_c\) obeys
\[
\boxed{
\|\delta_cf\|^2
\ge
\frac{(1-\rho-\eta_B\eta_\delta)^2}{C^2}\|f\|^2.}
\tag{VC13}
\]
Indeed (VC11) gives
\((1-\rho-\eta_B\eta_\delta)\|f\|
\le\|B_c\delta_cf\|\le C\|\delta_cf\|\).
Because \(\delta_c\Omega_c=0\), this also gives the corresponding operator inequality with \(Q_c\) on the right.

For a sequence of such compressions, a sufficient total budget is
\[
\rho_0+\sum_j\eta_{B,j}\eta_{\delta,j}<1
\tag{VC14}
\]
with a uniform strict margin and an initially uniform \(C\). Each loss is computed from the current inherited comparison and repair. A new access map that is not a compression, or a change of representation, requires its own transport theorem.

There is a constructive alternative to paying this loss at every cut. [[scale-bearing-descent/constructive-descent-division|Descent division]] asks the primitive source relations to factor the actual mixed term as \(L_B^*L_\delta=K_V\delta_c\). Adding \(K_V\) to the compressed repair removes that term from (VC11) exactly. Successive corrections then transport only the seed error, while the rebuilt repair norm becomes the quantity to control. The finite rewrite rule, its coherence across overlapping cuts and its uniform norm are new construction targets; finite matrix factorization alone does not establish them.

[[yang-mills-continuum-crossover/two-scale-rg-descent-and-the-crossover-lemma|The two-scale crossover theorem]] is a distinct analytic implementation of an accumulated-loss budget: it tracks the actual conditional and marginal laws and the mixed score cost. Its constants cannot be substituted into (VC14) without identifying the analysis and repair maps.

The definition of \(\delta_c\) does not prove that it equals the innovation reconstructed from the actual coarse preparation or regional predictor. That identification needs an intertwining or controlled comparison theorem. In particular, [[two-slice-innovation-geometry/regional-innovation-and-exterior-information-balance|regional prediction]] can increase the innovation by discarding exterior information while preserving the original clock.

## Rebuild a finite-word repair after crossing

Compression of a polynomial in primitive comparisons need not equal that polynomial in the compressed comparisons. This difference can also be bounded before any spectral calculation.

For contractions \(a_1,\ldots,a_k\), suppose
\(\|\Gamma_\Phi(a_j,a_j)\|\le\varepsilon^2\) and
\(\|\Gamma_\Phi(a_j^*,a_j^*)\|\le\varepsilon^2\).
Stinespring's construction gives
\[
\Phi(ab)-\Phi(a)\Phi(b)=d_\Phi(a^*)^*d_\Phi(b),\qquad
\|d_\Phi(ab)\|
\le\|d_\Phi(a)\|\|b\|+\|a\|\|d_\Phi(b)\|.
\]
Induction on prefixes and telescoping therefore prove
\[
\left\|\Phi(a_1\cdots a_k)-\Phi(a_1)\cdots\Phi(a_k)\right\|
\le {k\choose2}\varepsilon^2.
\tag{VC15}
\]
For a scalar-coefficient polynomial \(p=\sum_wc_ww\), the corresponding error is bounded by
\(\varepsilon^2\sum_w|c_w|{\,|w|\choose2}\).
Matrix coefficients require the analogous block-norm estimate. Uniform word length, coefficient bounds and overlap congestion can thus connect the inherited repair to a repair built from actual coarse primitive comparisons. Their identification with the selected source law remains an additional condition, and the full accumulated error must fit within the margin in (VC14).

## The proposed constitutive theorem

The research conjecture is that a selected law of complete marked sewing supplies an initial finite-word certificate or repair on its entire neutral observable carrier, and preserves it by either a derived variance or loss budget, or coherent descent division with a uniformly bounded rebuilt repair. Its primitive relations must determine the coefficients, actual state and source transport. [[scale-bearing-descent/minimal-conjectures-and-decisive-returns|Conjecture C2]] separates generating the initial floor from preserving it: exact correction cannot create a seed estimate that was never constructed.

The sourceful innovation carrier matters. Ordinary Čech gluing has every successfully glued global observable in its degree-zero kernel; gauge-transformation differences similarly annihilate every neutral distinction. The analysis map here must instead measure an actual failure of conditional recovery or a comparable state-dependent response. It must annihilate precisely the vacuum in the intended realization.

[[two-slice-innovation-geometry/regional-innovation-and-exterior-information-balance|The exterior-information identity]] already supplies actual positive compression losses, while [[general-causal-action/conditional-boundary-translation-and-source-products|conditional boundary messages]] demonstrate why source products must accompany elimination. These are inputs to a possible proof of the budget, not proof that its sum is small.

Three controls can reject a proposed law early: [[quantitative-descent/rigidity-certificates-and-soft-escape|the concentrating non-Abelian comparison family, QD6a–c]]; the loss of the Pauli holonomy obstruction on the neutral carrier; and [[general-causal-action/conditional-influence-soft-band-and-chronological-filters|the actual chronological soft filters]]. A successful new relation must explain its different outcome on these controls through a calculable change in the inherited law. [[physical-response-coercivity/physical-distinction-coercivity|Physical distinction coercivity]] specifies the complete carrier on which the resulting response must act.

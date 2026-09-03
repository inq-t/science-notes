# Pointed Facts and the Shorted Response

A local fact has two logically independent contrasts: observable alternatives of which one is obtained, and globally different antecedents that the local presentation cannot distinguish. Finite probability theory makes the second contrast an exact conditional relative-entropy residue. Positive-operator theory then supplies the reversal demanded by the programme: eliminate the hidden antecedent directions and obtain a **shorted response operator on the retained local distinction**. A positive lower edge of that operator is a precise candidate for dimensionless fact-persistence stiffness, although it becomes energy or mass only after the existing clock, action, carrier, and Poincare solders.

**Status: [EXACT] for the finite readout decomposition, background-fibre saturation lemma, and bounded positive-block theorem; [DEFINITION] for a Copernican fact requiring both observable contrast and antecedent ambiguity; [CONDITIONAL CONSTRUCTION] for the shorted operator as a fact-persistence generator; [OPEN] for its Yang--Mills realization, Type-III naturality, continuum lower bound, and physical calibration.**

## Pointing and forgetting are two axes

Let \(X\) be a finite whole-register sample space, let \(Y\) be a finite readout space, and let

$$
q:X\longrightarrow Y
\tag{PF1}
$$

be a surjective coarse-graining. If the obtained value is \(y\in Y\), two different complements appear:

$$
F_y:=q^{-1}(y),
\qquad
C_y:=Y\setminus\{y\}.
\tag{PF2}
$$

The antecedent fibre \(F_y\) contains differences in the whole that the local fact does not resolve. The counterfactual set \(C_y\) contains locally expressible alternatives that were not obtained. They are not the same background.

The independence is exact. If \(q=\mathrm{id}_X\) and \(|X|>1\), then \(F_y\) is a singleton while \(C_y\) is nonempty: there is observable contrast without hidden antecedent ambiguity. If \(q\) is constant and \(|X|>1\), then the unique fibre is all of \(X\) while \(C_y\) is empty: much is forgotten but no local distinction is made. Therefore neither pointing nor forgetting implies the other.

The commutative observable algebra is \(C(Y)\). A probability state \(p_Y\) weights alternatives, while the obtained value defines the character

$$
\chi_y(f)=f(y).
\tag{PF3}
$$

If \(H(p_Y)>0\), at least two outcomes have positive weight before conditioning. The conditioned state at the obtained value is the point mass \(\delta_y\), whose Shannon entropy is zero. Thus “ambiguity before, point after” is an exact change in the state description. It is not a Hamiltonian support gap: an instrument and record are needed to say that \(y\) actually occurred, and a continuum outcome space can also admit point evaluation.

The user's stronger ontological proposal can now be adopted without equivocation as a declared definition:

> A **Copernican fact** is a recorded local point for which both the observable contrast and the whole-register antecedent fibre are nontrivial.

This is not a theorem about every mathematical fact. It is a candidate physical criterion for facts whose locality is constituted by a genuine whole-to-part passage.

## The forgotten background has an exact information decomposition

Let \(p,r\) be strictly positive probability distributions on \(X\), and write

$$
\bar p=q_*p,
\qquad
\bar r=q_*r.
$$

For each \(y\in Y\), let \(p(\cdot\mid y)\) and \(r(\cdot\mid y)\) be the corresponding conditional distributions on \(F_y\). Expanding the logarithm into marginal and conditional parts gives

$$
\boxed{
D(p\Vert r)
=
D(\bar p\Vert\bar r)
+
\sum_{y\in Y}\bar p(y)
D\!\left(p(\cdot\mid y)\Vert r(\cdot\mid y)\right).}
\tag{PF4}
$$

Consequently the descent residue is

$$
\boxed{
D(p\Vert r)-D(q_*p\Vert q_*r)
=
\sum_y\bar p(y)
D\!\left(p(\cdot\mid y)\Vert r(\cdot\mid y)\right)
\geq0.}
\tag{PF5}
$$

This is a literal measure of relative distinction remaining inside the antecedent fibres after the visible readout has been fixed. It vanishes exactly when the two hypotheses have the same conditional distribution in every \(p\)-occupied fibre. It can therefore vanish even when the fibres contain many points. Fibre multiplicity, uncertainty, and positive information loss are three different statements.

Equation (PF5) is the finite commutative specialization of the relative-entropy decrement in [[cosmic-geon-hypothesis-and-horizon-rate-ledger]]. In a general von Neumann algebra, data processing still gives a nonnegative Araki relative-entropy decrement, but the explicit conditional-fibre sum requires additional commutative or sufficient-channel structure.

There is, however, an exact noncommutative saturation statement. Let \(r:\mathsf S_{\mathrm n}(M)\to\mathsf S_{\mathrm n}(N)\) be restriction along a normal unital inclusion, let \(\Phi_*\) be any downstream local predual channel, and suppose

$$
r\rho=r\sigma,
\qquad
D_M(\rho\Vert\sigma)<\infty.
$$

Then

$$
\boxed{
\mathfrak R_r(\rho:\sigma)=D_M(\rho\Vert\sigma),
\qquad
\mathfrak R_{\Phi_*}(r\rho:r\sigma)=0,
\qquad
\mathfrak R_{\Phi_*\circ r}(\rho:\sigma)=D_M(\rho\Vert\sigma).}
\tag{PF5a}
$$

The proof is immediate but load bearing: the restricted states coincide, so their relative entropy is zero; every later local channel receives identical states; and the additive residue law allocates the entire distinction loss to the first restriction. Thus all relative distinction between same-fibre antecedents is exhausted at carrier formation, and no downstream local readout can recover or separately charge that vertical distinction.

For a dynamically admissible whole-state family \(\mathfrak S_{\mathrm{adm}}\), the physically relevant background should be narrowed to

$$
[\omega]_{O,\mathrm{adm}}
:=
[\omega]_O\cap\mathfrak S_{\mathrm{adm}},
\qquad
\mathfrak S_{\mathrm{adm}}/{\sim_{r_O}}
\cong
\operatorname{im}\!\left(r_O|_{\mathfrak S_{\mathrm{adm}}}\right).
\tag{PF5b}
$$

Every local state statistic factors through this quotient. Formal normal-state extensions outside \(\mathfrak S_{\mathrm{adm}}\) are mathematical alternatives, not automatically physically available backgrounds.

## Reversal: eliminate the background, then operate on the point

The raw forgetting operator does not act as mass on what survives. Let a Hilbert response carrier split as

$$
\mathcal H_W
=
\mathcal K_O\oplus\mathcal K_B,
\tag{PF6}
$$

where \(\mathcal K_O\) carries retained local distinctions and \(\mathcal K_B\) carries hidden compatible extensions. Let \(e\) be the projection onto \(\mathcal K_O\). Then \(1-e\) vanishes on every retained vector. This is the range--kernel no-go in [[causal-patch-boundary-and-two-times]] and [[cosmic-geon-hypothesis-and-horizon-rate-ledger]].

Now supply a different object: a bounded positive whole-response operator

$$
A
=
\begin{pmatrix}
G&B\\
B^*&C
\end{pmatrix}
\geq0,
\qquad
C\geq c_BI>0.
\tag{PF7}
$$

Here \(A\) acts on **whole-compatible variations** \(x\oplus z\), not on outcomes and not on the discarded fibre alone. Completing the square gives, for every \(x\in\mathcal K_O\),

$$
\begin{aligned}
&\left\langle x\oplus z,
A(x\oplus z)\right\rangle\\
&\quad=
\left\langle z+C^{-1}B^*x,
C\left(z+C^{-1}B^*x\right)\right\rangle
+\left\langle x,S_Ax\right\rangle,
\end{aligned}
\tag{PF8}
$$

where

$$
\boxed{
S_A:=G-BC^{-1}B^*\geq0.}
\tag{PF9}
$$

Therefore

$$
\boxed{
\left\langle x,S_Ax\right\rangle
=
\inf_{z\in\mathcal K_B}
\left\langle x\oplus z,A(x\oplus z)\right\rangle,}
\tag{PF10}
$$

with minimizing hidden extension \(z_*=-C^{-1}B^*x\).

On \(\mathcal H_W\), the operator \(S_A\oplus0\) is the short of \(A\) to \(\mathcal K_O\): the largest positive operator below \(A\) whose range lies in the retained subspace. [[spectral-wall-descent/hidden-resolvent-and-seesaw|The hidden-resolvent note]] owns the broader Schur-complement grammar. Its new use here is ontological and carrier-specific:

> \(S_A\) charges a retained local distinction by the least whole-register response cost among all hidden backgrounds compatible with it.

This answers “what does the operator operate on?” It operates on \(x\in\mathcal K_O\), the retained distinction. The forgotten background enters through the minimization over \(z\in\mathcal K_B\); it is implicated without being mistaken for the operator's physical carrier.

## What elimination can and cannot generate

The inequalities

$$
0\leq S_A\leq G
\tag{PF11}
$$

are immediate. Allowing the hidden background to relax can only soften a positive static response relative to holding it fixed. More sharply, if \(G=0\), positivity of \(A\) forces \(B=0\), hence \(S_A=0\). A positive hidden block and coupling cannot manufacture tangential stiffness from none.

This corrects the slogan “the leak is the cost of mass.” The transverse act of forgetting supplies the relation in which a local point exists, but the mass candidate is the residual tangential cost after the forgotten background has been allowed to adjust. A nonzero floor must already be enforced by the whole response, a constraint, a paired descent, a boundary Dirichlet-to-Neumann form, or another independently constructed positive structure. The shorting operation reveals that residual; it does not create it by notation.

The existing [[descent-loss-cocycle-and-recovery-fork|output-transgression theorem]] makes the warning sharper. If \(A\) is taken to be only the loss Hessian of one state-preserving expectation with its adapted BKM geometries, the retained minimum-lift transgression is identically zero. A nonzero shorted response must therefore come from a non-adapted metric comparison, a jointly transverse family, or an independent whole/boundary response—not from relabeling the canonical vertical loss.

Let \(\Omega\in\mathcal K_O\) be a proposed invariant or vacuum vector and \(P_0\) its projection. The exact dimensionless stopping condition is

$$
\boxed{
S_A\Omega=0,
\qquad
S_A\geq\kappa_O(I-P_0)
\quad\text{for some }\kappa_O>0.}
\tag{PF12}
$$

If \(S_A\) is the generator of a canonically normalized symmetric contraction semigroup, (PF12) is a dimensionless relaxation or persistence gap on the complete retained complement. It is not yet the Yang--Mills mass gap. [[mass-as-a-calibrated-distinction-rate]] and [[hbar-clock-and-the-calibration-firewall]] give the further clock, action, OS, Poincare, and Casimir arrows.

## Type III supplies the setting, not the floor

The restriction fibre of normal states and the Araki decrement remain meaningful when the local algebra is Type III, without a density matrix or tracial state. Standard form also supplies Hilbert carriers on which local subspaces can be represented. But Type III does not canonically supply the projection \(e\), the whole response \(A\), the invertibility of the hidden block, or the floor in (PF12). A state-preserving expectation gives one exact projection model; without it, the retained carrier may have to be constructed by a \(W^*\)-correspondence or a closed quotient form.

Nor can the canonical core's trace-scaling action be substituted for \(A\). The [[library/noncommutative-flow-of-weights/inq|canonical core]] carries that vertical presentation structure even in a static world. The physical proposal needs a horizontal whole-to-local response and an independent solder to clock dynamics.

## The revised Copernican claim

The most defensible form of the insight is now:

$$
\boxed{
\begin{array}{c}
\text{whole-compatible alternatives}
\xrightarrow{\text{restriction}}
\text{local equivalence class}
\xrightarrow{\text{instrument + record}}
\text{pointed fact},\\[4pt]
\text{whole response}
\xrightarrow{\text{minimize hidden extensions}}
\text{shorted tangential response}
\xrightarrow{\text{uniform floor + solders}}
\text{candidate mass gap}.
\end{array}}
\tag{PF13}
$$

Mass is therefore not the background, the information lost about it, or the bare quotient map. The live conjecture is subtler: **mass is the calibrated lower rate-cost of making a retained distinction persist under every compatible relaxation of the background that its local presentation forgets.**

This is close enough to the measurement analogy to be useful and different enough to avoid equivocation. “Collapse” names pointing and conditioning; the descent residue names lost relative distinction; the shorted response names the least surviving dynamical cost; the mass gap names the Poincare-invariant spectral floor after reconstruction.

## Construction obligations

A physical realization must still:

1. construct the whole carrier, accessible carrier, and their comparison without assuming the desired local theory;
2. derive \(A\) independently of the Yang--Mills Hamiltonian or observed glueball spectrum;
3. show that the shorted form exists on the relevant changing or Type-III carriers;
4. prove that its kernel is exactly the physical vacuum and that (PF12) holds in every nonvacuum direction;
5. keep the floor uniform through infinite volume and continuum removal;
6. reconstruct locality, a positive-energy Poincare representation, and the invariant Casimir; and
7. obtain the clock/action/length normalization without fitting the desired mass.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/pointed-background-short-receipt.py|The finite receipt]] and [[contemporary-puzzles/yang-mills-mass-gap/receipts/pointed-background-short-receipt-output.txt|its stored output]] verify (PF4), (PF8)--(PF11), and the fact that the raw forgetting projection vanishes on the retained carrier. They do not verify any Type-III, continuum, fact-selection, or mass-gap claim.

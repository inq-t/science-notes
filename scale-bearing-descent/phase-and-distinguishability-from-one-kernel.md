# Phase and Distinguishability from One Kernel

A phase can constrain distinguishability when both belong to the same positive comparison kernel. A three-history Gram identity supplies a finite example: a cyclic relation prevents all three histories from having nearly identical rays. Its weaker, unequal-overlap form also constructs an initial repair without a spectral inverse, provided the history differences factor through the actual innovation. The proposed discovery is a finite source law that forces these relations on the complete centered carrier.

## A phase is part of a positive comparison

Begin with a positive history kernel. The Hermitian-line kernel in [[scale-bearing-descent/anomaly-lines-and-the-yang-mills-phase-test|the relative-evaluation proposal]] is one possible source; an anomaly is not a prerequisite for the following lemma. The Gram construction gives history vectors in a common Hilbert carrier. Choose three unit vectors \(u_1,u_2,u_3\), write \(G_{ij}=\langle u_i,u_j\rangle\), and assume their three pairwise overlap moduli equal \(r>0\). The cyclic phase
\[
\phi=\arg(G_{12}G_{23}G_{31})
\tag{PN1}
\]
is unchanged when the individual vectors are multiplied by phases. Positivity of \(G\) implies
\[
\det G=1-3r^2+2r^3\cos\phi\ge0.
\tag{PN2}
\]
This follows by expanding the determinant of the Hermitian matrix with unit diagonal. It is an exact algebraic compatibility between phase and norm, not a postulated energy inequality.

For \(\phi=\pi\), it gives
\[
\det G=(1-2r)(1+r)^2\ge0,
\qquad r\le\tfrac12.
\tag{PN3}
\]
The three rays therefore cannot all become indistinguishable. At the endpoint \(r=1/2\), however, \(G\) has eigenvalues \(0,3/2,3/2\). The separation of the rays is not a positive lower eigenvalue for the whole Gram matrix. Its null quotient is part of the history realization.

An anomaly-line holonomy is not automatically the cyclic phase in (PN1). The former concerns compatibility of background presentations; the latter concerns overlaps of three histories in one positive kernel. A comparison law must construct the map between them if an anomaly is to constrain this geometry. A flat torsion anomaly need not have nonzero differential curvature, and an arbitrary phase inserted into a positive kernel can destroy positivity.

[[scale-bearing-descent/cyclic-phase-realizations-and-exclusion-tests|The realization tests]] identify (PN1) as a Bargmann phase and distinguish its valid exclusions from false ones. Commuting preparations can have nonzero cyclic phase. Charge conjugation makes suitable real-source overlaps real, but does not force their negative cyclic sign or quantize every complex-source phase.

## Conjecture: the phase relation covers actual sources

Let \(\mathcal H_0\) be the complete centered physical source carrier at a declared regulator and relational duration. Seek linear isometries
\[
V_i:\mathcal H_0\longrightarrow\mathcal H_{\mathrm{hist}},
\qquad i=1,2,3,
\]
constructed by three admissible ways of preparing and sewing the same marked experiment. For every nonzero \(f\), their normalized Gram entries are
\[
G_{ij}(f)=\frac{\langle V_if,V_jf\rangle}{\|f\|^2}.
\tag{PN4}
\]
The first candidate relation is deliberately strong: the primitive source identities force equal nonzero overlap moduli and cyclic phase \(\pi\) for these triples. A more flexible version can use several triples and a quantitative coverage estimate; the single-triple version makes the first test explicit.

Define the stacked comparison
\[
\mathcal A f=
(V_1f-V_2f,\ V_2f-V_3f,\ V_3f-V_1f).
\]
Under that candidate relation, (PN3) gives
\[
\|\mathcal A f\|^2
=6\|f\|^2-2\operatorname{Re}\!\sum_{\mathrm{cyc}}\langle V_if,V_jf\rangle
\ge3\|f\|^2.
\tag{PN5}
\]
The phase is independent of the three line frames. The difference operator uses the particular lifts and identifications supplied by the sewing; the lower estimate holds for any choices with those overlap moduli.

This is the first conjectural leap: a finite relation among actual source operations could enforce phase separation for every centered source, rather than only for three selected vectors. No Yang–Mills identity with this property is presently known. The point is to search for a finite source relation and test its complete representation before attempting a continuum estimate.

There is a weaker sufficient verification target. If the preparations intertwine common antiunitary involutions, proving the cyclic estimate on all sources in the fixed real subspace gives the full complex quadratic bound by (CR6) in [[scale-bearing-descent/cyclic-phase-realizations-and-exclusion-tests|the real-core extension theorem]]. The cyclic product itself may fail the premise on complex combinations. The real structure and its compatibility with the chosen lifts must be supplied by the same source law.

## The comparison must be made by the physical chronology

The second leap is a constructive factorization through the actual innovation,
\[
\mathcal A=\mathcal K\delta_{\mathrm{phys}},
\qquad \|\mathcal K\|^2\le B<\infty.
\tag{PN6}
\]
The map \(\mathcal K\) must be assembled from the same preparation, boundary transports and source identities as the \(V_i\). Equations (PN5)–(PN6) then imply
\[
\|\delta_{\mathrm{phys}}f\|^2\ge\frac3B\|f\|^2.
\tag{PN7}
\]
The implication is exact. The substantive conjecture is that actual sewing constructs (PN4) and (PN6) with one bound through the required enlargement and refinement. For a normalized innovation, \(0\le\delta_{\mathrm{phys}}^*\delta_{\mathrm{phys}}\le I\), these hypotheses necessarily require \(B\ge3\).

[[algebra/short-loop-holonomy-and-quantitative-gluing|Short-loop gluing]] supplies the relevant proof pattern: bounded loop congestion factors a complete comparison through edge discrepancies. Its Pauli-to-adjoint example also exposes the central difficulty. A phase visible to transported sections can disappear on gauge-invariant observables. The present conjecture concerns the complete neutral source carrier from the outset.

## The first experiment can fail decisively

Construct the \(V_i\) for three overlapping prepared comparisons with one shared boundary, using the complete mixed-source algebra. Compute their Gram matrices from the original amplitude. The question is whether changing the sewing order forces a phase relation that cannot be removed by changing line frames or independently rescaling a source.

Then derive the factorization in (PN6) from the actual conditional predictor. Artificial lifts \(V_if=u_i\otimes f\) can manufacture the desired Gram matrix for any dynamics whatsoever. They count for nothing unless the physical sewing supplies the factorization. A pseudoinverse of \(\delta_{\mathrm{phys}}\) defined after assuming its gap is equally uninformative.

Test the candidate against [[quantitative-descent/rigidity-certificates-and-soft-escape|the concentrating non-Abelian family]] and [[general-causal-action/conditional-influence-soft-band-and-chronological-filters|actual soft chronological filters]]. A valid new law must identify which of its independently specified relations those examples fail. Test its behavior under subdivision as well: fixed nontrivial phase on every shrinking spatial plaquette need not admit a finite-curvature continuum return.

The attainable first result is a finite source identity that forces a comparison floor and is realized by one actual sewn law. [[scale-bearing-descent/constructive-descent-division|Descent division]] then asks whether that rigidity can be repaired through changes of access. [[scale-bearing-descent/minimal-conjectures-and-decisive-returns|The conjectural chain]] places these as separate steps toward a single stable physical return.

## A weaker cyclic relation already forces separation

The equal-modulus, phase-\(\pi\) hypothesis can be relaxed. For any normalized three-history Gram matrix, write
\[
z=G_{12}G_{23}G_{31},\qquad
s=|G_{12}|^2+|G_{23}|^2+|G_{31}|^2.
\]
Its positivity gives the exact identity and inequality
\[
\det G=1-s+2\operatorname{Re}z\ge0.
\tag{PN8}
\]
Consequently a **nonpositive cyclic interference** relation suffices:
\[
\operatorname{Re}z\le0
\quad\Longrightarrow\quad
s\le1+2\operatorname{Re}z\le1.
\tag{PN9}
\]
This permits unequal and zero overlaps; no phase is assigned to a zero product. Like the cyclic phase, \(z\) is unchanged by individual line-frame changes.

In fact, \(0\le G\le2I\). The one-by-one and two-by-two principal minors of \(2I-G\) equal those of \(G\), while
\[
\det(2I-G)=1-s-2\operatorname{Re}z
=\det G-4\operatorname{Re}z\ge0.
\]
Thus every principal minor of the Hermitian matrix \(2I-G\) is nonnegative, which proves its positivity.

Suppose the actual isometric history lifts in (PN4) satisfy (PN9) for every nonzero centered source \(f\). With \(\mathbf1=(1,1,1)^T\), this gives
\(\|\sum_iV_if\|^2=\mathbf1^*G(f)\mathbf1\,\|f\|^2\le6\|f\|^2\).
Expanding the three pair differences therefore yields
\[
\boxed{\|\mathcal A f\|^2
=9\|f\|^2-\|\textstyle\sum_iV_if\|^2
\ge3\|f\|^2.}
\tag{PN10}
\]
If physical sewing also supplies (PN6), the actual innovation has lower bound
\(3/B\) on this carrier. These implications are exact conditional statements.

The sharper conjectural target is a finite source identity that forces (PN9) in the selected branch. It could be a positive-word certificate for the negative real cyclic product in the algebra of three marked copies, derived before evaluating the source matrices. No such identity has been constructed here. It is not a universal principle of facts or a consequence of anomaly matching alone. It must cover the complete centered source carrier of the same positive kernel; the physical factorization and artificial-tensor-lift test above remain essential. The gain is a seed criterion without equal overlap magnitudes or one prescribed nonzero phase.

### The same words construct a seed repair

Because the three \(V_i\) are isometries, direct expansion gives
\[
\boxed{\mathcal A^*\mathcal A
=9I-(V_1+V_2+V_3)^*(V_1+V_2+V_3),
\qquad 3I\le\mathcal A^*\mathcal A\le9I.}
\tag{PN11}
\]
The lower bound uses (PN9); the identity and upper bound use only the isometries. Suppose the bounded actual innovation is
\(\delta:\mathcal H_0\to\mathcal X\), and physical sewing constructs
\(\mathcal K:\mathcal X\to\mathcal H_{\mathrm{hist}}^{\oplus3}\)
with \(\mathcal A=\mathcal K\delta\) and \(\|\mathcal K\|\le L\).
Define a return map without inverting either analysis:
\[
\begin{aligned}
B_0&=\tfrac19\mathcal A^*\mathcal K:
\mathcal X\longrightarrow\mathcal H_0,
& E_0&=I-\tfrac19\mathcal A^*\mathcal A,\\
B_0\delta&=I-E_0,
&0\le E_0&\le\tfrac23I,
\qquad \|B_0\|\le L/3.
\end{aligned}
\tag{PN12}
\]
Thus the same source expressions supply the initial bounded repair required by [[scale-bearing-descent/constructive-descent-division|descent division]]. If the \(V_i\) and \(\mathcal K\) are admissible finite-word expressions, so is \(B_0\): only adjoints, composition and linear combinations have been used. The constant \(1/9\) comes from the elementary upper bound in (PN11), not from the sought spectrum.

On \(\mathcal H=\mathbb C\Omega\oplus\mathcal H_0\), extend \(\mathcal A\) and \(E_0\) by zero on the vacuum and include the range of \(B_0\) in \(\mathcal H_0\). If the actual innovation satisfies \(\delta\Omega=0\), then (PN12) becomes \(B_0\delta=Q-E_0\), with \(Q=I-|\Omega\rangle\langle\Omega|\). This is the required vacuum-preserving seed. Uniform control through further cuts remains the separate division conjecture.

## Approximate preparations retain an explicit margin

Exact isometries are natural for pullback under an inherited law. An approximating construction may instead give bounded linear preparations satisfying
\[
(1-\varepsilon)I\le V_i^*V_i\le(1+\varepsilon)I,
\qquad 0\le\varepsilon<1.
\]
For every nonzero source, normalize its three history vectors individually:
\[
C_{ij}(f)=
\frac{\langle V_if,V_jf\rangle}{\|V_if\|\,\|V_jf\|},
\qquad
\operatorname{Re}(C_{12}C_{23}C_{31})\le\eta,
\qquad 0\le\eta<1.
\]
These \(C(f)\) are correlation matrices even when the \(V_i\) are not isometries. Define
\[
s_\eta=\frac{\sqrt{1+8\eta}-1}{2},\qquad
a=3(1-\varepsilon)(1-s_\eta)>0,\qquad
b=9(1+\varepsilon).
\]
Then
\[
\boxed{aI\le\mathcal A^*\mathcal A\le bI.}
\tag{PN13}
\]

To prove this, \(\det(2I-C)=\det C-4\operatorname{Re}(C_{12}C_{23}C_{31})\ge-4\eta\). If the largest eigenvalue is \(2+s>2\), the other two sum to \(1-s\), since \(\operatorname{Tr}C=3\). Positivity gives
\[
(2-\lambda_2)(2-\lambda_3)
=2+2s+\lambda_2\lambda_3\ge2+2s.
\]
Thus \(s(1+s)\le2\eta\), and \(C\le(2+s_\eta)I\). Apply this bound to the coefficient vector \((\|V_1f\|,\|V_2f\|,\|V_3f\|)\):
\[
\|\mathcal Af\|^2
=3\sum_i\|V_if\|^2-\Big\|\sum_iV_if\Big\|^2
\ge(1-s_\eta)\sum_i\|V_if\|^2\ge a\|f\|^2.
\]
Dropping the last squared norm gives the upper bound. If only the raw entries \(G_{ij}(f)=\langle V_if,V_jf\rangle/\|f\|^2\) are available with \(\operatorname{Re}(G_{12}G_{23}G_{31})\le\theta\), \(\theta\ge0\), take \(\eta=\theta/(1-\varepsilon)^3<1\).

An exact source factorization \(\mathcal A=\mathcal K\delta\), \(\|\mathcal K\|\le L\), still constructs
\[
B_0=b^{-1}\mathcal A^*\mathcal K,\qquad
B_0\delta=I-E_0,\qquad
0\le E_0\le(1-a/b)I,\qquad
\|B_0\|\le L/\sqrt b.
\tag{PN14}
\]
Thus exact algebraic realization is not required for the comparison margin, provided the errors are controlled in the complete source norm. Uniform bounds are still needed through refinement.

## The direct factorization gives the stronger response bound

The constructed repair is useful for descent, but estimating only its norm loses information already present in \(\mathcal A\). If
\[
\|\mathcal A-\mathcal K\delta\|\le\zeta<\sqrt a,
\qquad \|\mathcal K\|\le L,\qquad L>0,
\]
then \(\sqrt a\,\|f\|\le L\|\delta f\|+\zeta\|f\|\), hence
\[
\boxed{\delta^*\delta\ge\frac{(\sqrt a-\zeta)^2}{L^2}I.}
\tag{PN15}
\]
For exact isometries, nonpositive interference and exact factorization, this is \(3/L^2\). The generic repair estimate from (PN12) gives the weaker \(1/L^2\). Approximate factorization with the full error range above proves the response bound; it does not automatically preserve the finite seed formula's strict error margin.

When this same analysis is the complete chronological innovation,
\(\delta^*\delta=I-e^{-2\ell H}\), \(H\ge0\) self-adjoint, choose
\[
0<\kappa<\min\left\{1,\frac{(\sqrt a-\zeta)^2}{L^2}\right\}.
\]
Spectral calculus gives
\[
\boxed{\inf\sigma(H|_{\Omega^\perp})
\ge-\frac{\log(1-\kappa)}{2\ell}.}
\tag{PN16}
\]
Here \(\ell>0\) and all error and norm bounds use the inherited chronology. This is a conditional lower bound, not a computed mass or glueball/string-tension ratio.

For exact factorization followed by a [[scale-bearing-descent/coherent-comparison-lifts-and-bounded-descent|comparison lift]] of norm at most \(M\), the retained response has the direct bound \(a/(L^2M^2)\). Regional restriction has \(M=1\). General mixed-term division and new-source extension do not reduce to the original \(L\) without a new constructed factorization or a separate rebuilt-repair estimate. Nor does a regional response alone define an autonomous regional Hamiltonian.

The [[scale-bearing-descent/receipts/cyclic-comparison-audit.py|finite audit receipt]] checks the exact endpoints and perturbed Gram inequalities numerically. The proofs above carry the infinite-family implications; the receipt does not select their Yang–Mills realization.

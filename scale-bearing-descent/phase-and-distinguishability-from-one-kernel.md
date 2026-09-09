# Phase and Distinguishability from One Kernel

A phase can constrain distinguishability when both belong to the same positive comparison kernel. A three-history Gram identity supplies a finite example: a nontrivial cyclic phase prevents all three histories from having nearly identical rays. The proposed extension is to force such separation on a complete family of actual source histories and reconstruct it from their physical innovation. This would turn a phase relation into a response bound without first choosing a spectrum.

## A phase is part of a positive comparison

Use the Hermitian-line kernel in [[scale-bearing-descent/anomaly-lines-and-the-yang-mills-phase-test|the relative-evaluation proposal]]. Its positive Gram construction gives history vectors in a common Hilbert carrier. Choose three unit vectors \(u_1,u_2,u_3\), write \(G_{ij}=\langle u_i,u_j\rangle\), and assume their three pairwise overlap moduli equal \(r>0\). The cyclic phase
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

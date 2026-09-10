# Cyclic Phase Realizations and Exclusion Tests

The cyclic Gram condition is a sufficient source-separation criterion whose realizations must be tested before it can explain a mass gap. Scalar rephasings and strictly positive chronological translates cannot supply its nonzero phase, but commuting preparations can. A compatible real structure offers a useful reduction: proving separation on real sources can establish the quadratic bound on the full complex carrier, without quantizing every complex-source phase. These distinctions sharpen the construction problem and correct several stronger exclusions in the received commentary.

## The invariant belongs to overlaps

For three unit histories in one positive kernel, define
\[
\Delta_3=G_{12}G_{23}G_{31},\qquad
G_{ij}=\langle u_i,u_j\rangle.
\tag{CR1}
\]
This is the three-vertex Bargmann invariant. When all overlaps are nonzero, its argument is the cyclic Pancharatnam phase. Under the usual nonorthogonality and geodesic-closure assumptions it represents geometric holonomy in projective Hilbert space, with the orientation convention fixing its sign. [[library/bargmann-invariants-null-phase-curves-and-a-theory-of-the-geometric-phase/inq|The Bargmann formulation]] relates it to the ray-space symplectic form; a general Fubini–Study metric area is not the invariant being integrated. [[library/measuring-geometric-phases-with-a-dynamical-quantum-zeno-effect/inq|Geometric phases from projection sequences]] gives a corresponding experimental setting.

The inequality \(\operatorname{Re}\Delta_3\le0\) places that argument in a closed half-circle, when the product is nonzero. If an overlap vanishes, the product is zero and its phase is undefined. The inequality still makes sense. [[scale-bearing-descent/phase-and-distinguishability-from-one-kernel|The Gram theorem]] uses the product itself.

This is geometry of prepared rays. It is not yet a Wilson-loop area law, an area bound in spacetime, or a proof that confinement implies a mass gap. Such a return needs a map between the source preparations and those observables, followed by the actual-innovation factorization. A geometric interpretation of a known algebraic identity does not supply that map.

## Rephasing is narrower than a commuting action

For nonzero overlaps, put \(c_{ij}=G_{ij}/|G_{ij}|\), with \(c_{ji}=\overline{c_{ij}}\). On a triangle,
\[
\boxed{
c_{12}c_{23}c_{31}=1
\quad\Longleftrightarrow\quad
c_{ij}=\overline{a_i}a_j
\text{ for vertex phases }a_i.}
\tag{CR2}
\]
Choose \(a_1=1,a_2=c_{12},a_3=c_{12}c_{23}\); the triangle equation verifies the third edge. The reverse implication telescopes.

The \(c_{ij}\) form an edge **1-cochain**; its triangle product is its multiplicative coboundary. A nonunit triangle product obstructs removing these edge phases by vertex rephasing. It does not, by itself, define a nontrivial group-cohomology class or a field-theoretic anomaly. A filled simplex has no nontrivial second cohomology, and this particular triangle product is already a coboundary.

Scalar preparations \(u_i=e^{i\alpha_i}u\) give \(\Delta_3=1\). A center action on one fixed charge character has the same limitation. But a matrix coefficient of an abelian representation is generally a weighted sum of characters, not a character. Its normalized phase need not multiply under group composition.

**Exact commuting counterexample.** Let \(\omega=e^{2\pi i/3}\), \(U=\operatorname{diag}(1,\omega)\), \(f=(1,1)/\sqrt2\), and \(u_i=U^{i-1}f\). Then
\[
G_{12}=G_{23}=G_{31}=\frac{1+\omega}{2},
\qquad
\boxed{\Delta_3=-\frac18.}
\tag{CR3}
\]
The preparations all belong to one commuting unitary action, yet their cyclic phase is \(\pi\). Group elements telescope; their expectation values do not. Thus the received assertion that every commuting family has trivial cyclic phase is false.

There is a narrower complete-source exclusion. Suppose the \(V_i\) are commuting unitaries on the common source Hilbert space, or restrictions to a common reducing source subspace. Their joint spectral measure supplies approximate common eigenvectors. On those vectors every overlap approaches \(\overline{\lambda_i}\lambda_j\), so \(\Delta_3\to1\). The nonpositive cyclic condition therefore cannot hold on **every complex source** in that representation. This argument does not cover arbitrary isometric embeddings into a larger history space, nor does it rule out a positive quadratic comparison bound.

Indeed \(V_if=f\otimes R(2\pi(i-1)/3)e_1\) gives isometries into a larger history space related by commuting target rotations, with \(\Delta_3=-1/8\) for every complex source. The source image is not invariant under those target rotations. This is another artificial-lift control: the phase criterion alone can be supplied independently of the dynamics.

## A real structure reduces the proof without quantizing every source

For a charge-conjugation invariant measure, a natural real structure on source functions is
\[
Jf=\overline{f\circ C}.
\]
It is an antiunitary involution. A \(J\)-real source obeys \(f\circ C=\bar f\). If the source and history involutions satisfy
\[
J_{\rm hist}V_i=V_iJ_{\rm src},
\tag{CR4}
\]
then the histories of a \(J_{\rm src}\)-real source are \(J_{\rm hist}\)-real, and all their overlaps are real. A nonzero cyclic product then has phase \(0\) or \(\pi\). Charge conjugation does not select its sign.

Covariance of the sewing alone does not make the overlaps real for arbitrary complex sources. For example, on \(\mathbb C^3\), take
\[
\Omega=(1,1,1)/\sqrt3,\quad
U(x_1,x_2,x_3)=(x_3,x_1,x_2),\quad
f=(1,i,-1-i)/2.
\]
The source is centered and normalized. The maps \(I,U,U^2\) preserve the vacuum and commute with ordinary conjugation, but
\[
G_{12}=G_{23}=G_{31}=-\frac12-\frac{3i}{4},
\qquad
\Delta_3=\frac{23}{32}-\frac{9i}{64}.
\tag{CR5}
\]
Thus zero theta and conjugation-covariant sewing do not confine every complex-source cyclic phase to \(\{0,\pi\}\). Even within the real sector, identical sewings give positive product. A negative product remains a source relation to derive.

**Exact real-core extension.** There is nevertheless a useful sufficient condition for the full programme. Suppose the isometries intertwine the involutions in (CR4), the centered source carrier is \(J_{\rm src}\)-invariant, and the cyclic premise is proved for every centered \(J_{\rm src}\)-real source. Fixing the vacuum under \(J_{\rm src}\) suffices for this invariance. The Gram lemma gives \(\|\mathcal Aa\|^2\ge3\|a\|^2\) on that real subspace. Every centered complex source decomposes uniquely as
\[
f=a+ib,\qquad J_{\rm src}a=a,\quad J_{\rm src}b=b.
\]
Since \(\mathcal A\) also intertwines the real structures, its real-source cross inner products are real. Therefore
\[
\boxed{
\|\mathcal Af\|^2
=\|\mathcal Aa\|^2+\|\mathcal Ab\|^2
\ge3(\|a\|^2+\|b\|^2)
=3\|f\|^2.}
\tag{CR6}
\]
This proves the full complex operator floor and the same finite seed repair. It does not prove the cyclic premise separately for each complex \(f\).

The difference matters constructively. Let \(R\) be rotation by \(2\pi/3\) on \(\mathbb R^2\), complexified to \(\mathbb C^2\), and take \(V_i=I,R,R^2\). Every real source has the three overlaps \(-1/2\), so its cyclic product is \(-1/8\). Moreover \(I+R+R^2=0\), hence \(\mathcal A^*\mathcal A=9I\). Complex eigenvectors of \(R\) instead have \(\Delta_3=1\). The real-core proof obtains the complete quadratic bound even though the stronger all-complex cyclic criterion fails.

This reduces one possible source-coherence task: derive the real-source sign from the actual law and prove the intertwining, then recover complex separation by polarization. It supplies no physical factorization on its own; the rotation example can be attached to arbitrary dynamics.

The common real structure is part of this argument. Arbitrary independent complex rephasings of the preparations need not preserve (CR4), even though they preserve the Bargmann product.

## A common modulus floor is an optional stronger test

Write \(a=|G_{12}|,b=|G_{23}|,c=|G_{31}|\). The exact determinant constraint is
\[
a^2+b^2+c^2-2\operatorname{Re}\Delta_3\le1.
\]
When \(abc>0\), \(\operatorname{Re}\Delta_3=abc\cos\phi\). Under nonpositive cyclic interference, a common lower floor \(a,b,c\ge\gamma\) requires
\[
\gamma\le1/\sqrt3.
\]
For a real negative cyclic product it instead requires
\[
3\gamma^2+2\gamma^3\le1,
\qquad \gamma\le\tfrac12.
\tag{CR7}
\]
Both ceilings are attainable. The phase-\(\pi\), equal-modulus ceiling \(r\le1/2\) was already proved in (PN3).

These are ceilings on the **common lower floor**, not upper bounds on every individual overlap. The real Gram matrix with cyclic overlaps \((0.9,0.1,-0.1)\) is positive definite: its determinant is \(0.152\), and all two-index principal minors are positive. One overlap exceeds \(1/2\). The received receipt's final individual-overlap requirement is therefore false.

A positive \(\gamma\) would test a proposed phase mechanism while keeping overlaps nonzero. It is not a cost-free addition to the conjecture, and it does not establish noncircularity: artificial histories \(V_if=u_i\otimes f\) can satisfy it for any dynamics. The decisive condition remains a source-defined factorization through the actual innovation.

The numerical \(-1/2\) in [[rg-covariance-residue/wilson-frustration-and-joint-escape|the central \(SU(3)\) plaquette context]] is a normalized real trace, not this overlap ceiling. At cyclic phase \(2\pi/3\), the equal-modulus Gram endpoint instead solves \(r^3+3r^2-1=0\). Frustration of an action and frustration of a triangle of overlaps are different objects until an actual construction relates them.

Near-orthogonality of three preparations at one separation is not exponential clustering. Even overlap decay at increasing separation need not be exponential. Small positive \(\Delta_3\) also does not satisfy the exact inequality merely because it approaches zero. These observations remove the claimed dichotomy between a necessarily circular decorrelation branch and an automatically explanatory phase branch.

## Positive chronological translates are a genuine negative control

For a stationary positive self-adjoint transfer \(T\), the same source inserted at times \(n_i\) has
\[
G_{ij}=\frac{\langle f,T^{|n_i-n_j|}f\rangle}{\|f\|^2}\ge0.
\tag{CR8}
\]
If \(T=e^{-\ell H}\), with \(H\ge0\) self-adjoint and finite \(\ell>0\), every displayed overlap is strictly positive for nonzero \(f\). Spectral calculus proves this even if the spectrum reaches zero energy. Thus plain time translates cannot produce the proposed nonpositive product at finite separation.

If a positive transfer has a kernel, some overlaps may vanish; then the weak nonpositive condition can hold at zero product. Neither statement excludes all preparations assembled with chronological operations. They exclude this particular same-source translate construction. Other sewing operations may involve the same chronology without being its simple translates.

The received strong-coupling table does not independently compute such a construction. Its script inserts the ansatz \(C(R)=Ku^{4R}\) and prints powers of \(u\). It contains no gauge integration, character coefficients, vacuum subtraction, source normalization or expansion-remainder estimate. [[library/strong-coupling-expansion-for-finite-temperature-yang-mills-theory-in-the-confined-phase/inq|The expansion paper]], §4, equation (4.3), explicitly gives this form as a lowest-order contribution in its specified geometry. Such a positive leading term controls the sign for sufficiently small positive \(u\) when the remainder is controlled; it is not an exact identity throughout \(0<u<1\). The triangle also has unequal path lengths, so a common overlap floor cannot be checked from \(u^4\) alone.

[[library/existence-of-glueballs-in-strongly-coupled-lattice-gauge-theories/inq|The strong-coupling glueball theorem]] remains a useful target regime. Testing a specified preparation there can reject that preparation, not every possible realization of the module's three sewn histories. The transfer argument above already gives a rigorous negative control without interpreting a table of assumed powers as a Yang–Mills receipt.

## What the received numerical checks establish

Claude's [[scale-bearing-descent/inbox/claude/2026-09-09/commentary/2026-09-09T18H45 CST.md|first commentary]] and [[scale-bearing-descent/inbox/claude/2026-09-09/commentary/2026-09-09T19H10 CST.md|follow-up]] correctly recognize the finite seed construction and the Bargmann invariant. Their [[scale-bearing-descent/inbox/claude/2026-09-09/receipts/strong-coupling-bargmann-obstruction.md|received receipt]] and [[scale-bearing-descent/inbox/claude/2026-09-09/receipts/bargmann-delta3-checks.py|original script]] are preserved unchanged, with [[scale-bearing-descent/inbox/claude/2026-09-09/archive-provenance.json|archive hashes]]. Their asserted commuting-family and unrestricted reality exclusions are replaced by (CR2)–(CR6).

The original random scans test the determinant identity, the Gram implication and attainable modulus floors. They print numerical findings; they do not test the exclusions above or construct a gauge-theory realization. The imaginary circulant example saturates \(\lambda_{\max}(G)=2\), but has \(\|\mathcal Af\|^2/\|f\|^2=6\), so it does not saturate the lower comparison constant \(3\). The cyclic entries \(1/2+i/(2\sqrt3)\) do saturate that lower bound.

The [[scale-bearing-descent/receipts/cyclic-comparison-audit.py|reviewed receipt]] uses explicit assertions for these endpoints, the counterexamples and the real-core extension, together with bounded numerical checks of the exact and perturbed Gram implications. Those checks supplement the proofs; no numerical result here supplies a Yang–Mills preparation or a uniform physical gap.

The executable audit passed 20,000 determinant checks, 4,766 sampled positive Gram matrices satisfying the exact premise, and four perturbed batches, in addition to the explicit examples. The original large random scan was inspected rather than rerun; its reported extrema are not treated as independently reproduced values.

The Michelson–Morley analogy in [[scale-bearing-descent/mass-from-the-algebra-of-changing-access|the article]] remains an invitation to change explanatory categories. It does not identify a gauge-fixed perturbative propagator pole with the gauge-invariant physical spectrum, or make lattice calculations a falsification of the Yang–Mills theory they calculate. A dimensionless glueball/string-tension ratio would be a valuable independent return of a selected source law. A bound on \(\|\mathcal K\|\) and a modulus floor alone do not determine that ratio: they supply an inequality for one response, not the second observable or an equality for the mass.

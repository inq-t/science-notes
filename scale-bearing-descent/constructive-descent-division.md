# Constructive Division Through Descent

Descent division is a proposed operation that reconstructs a comparison repair after a boundary channel is forgotten. It expresses the lost mixed term using retained comparisons, then adds the resulting correction to the repair. An exact operator lemma shows what this would accomplish. The conjectural advance is a finite source-defined division rule that composes coherently and keeps the rebuilt repair bounded. Such a rule would derive stability from relations among comparisons; it is stronger than estimating discarded variance and is not known to be easier.

## The lost term can ask for a correction

Use the bounded setting of [[scale-bearing-descent/variance-completed-rigidity|variance-completed rigidity]]. On a Hilbert carrier with unit vacuum \(\Omega\), let
\[
Q=I-|\Omega\rangle\langle\Omega|,\qquad
\delta:\mathcal H\longrightarrow\mathcal H^{\oplus m},\qquad
B\delta=Q-E,\qquad \delta\Omega=0,
\]
with \(\|E\|\le\rho<1\). The initial repair \(B\) must already have an independent construction. [[scale-bearing-descent/phase-and-distinguishability-from-one-kernel|The cyclic-comparison seed, PN11–12]], constructs one by a finite word when its source-coherence and actual-innovation hypotheses hold. For a vacuum-preserving isometry \(V:\mathcal H_c\to\mathcal H\), put
\[
V_m=I_m\otimes V,\qquad P_m=V_mV_m^*,\qquad
\delta_c=V_m^*\delta V,\qquad B_c=V^*BV_m.
\]
The lost channels and their mixed term are
\[
L_\delta=(I-P_m)\delta V,\qquad
L_B=(I-P_m)B^*V,\qquad
C_V=L_B^*L_\delta.
\tag{DD1}
\]
The compression identity is
\[
B_c\delta_c=Q_c-V^*EV-C_V.
\tag{DD2}
\]
The subscript \(V\) specifies the actual carrier compression, not an arbitrary channel sharing its name.

**Exact correction lemma.** If a bounded map \(K_V:\mathcal H_c^{\oplus m}\to\mathcal H_c\) satisfies
\[
\boxed{C_V=K_V\delta_c,}
\tag{DD3}
\]
then the rebuilt repair \(\widehat B_c=B_c+K_V\) obeys
\[
\boxed{\widehat B_c\delta_c=Q_c-V^*EV.}
\tag{DD4}
\]
This follows by substitution. If \(\|\widehat B_c\|\le C_*\), \(C_*>0\), then on the vacuum complement
\[
\|\delta_cf\|^2\ge
\frac{(1-\rho)^2}{C_*^2}\|f\|^2.
\tag{DD5}
\]
The correction removes the compression term from the repair identity. It does not remove the need to control the repair norm.

The innovation carrier need not be \(\mathcal H^{\oplus m}\). For \(\delta:\mathcal H\to\mathcal X\) and \(B:\mathcal X\to\mathcal H\), specify the actual retained-innovation isometry \(S:\mathcal X_c\to\mathcal X\) as well as the vacuum-preserving \(V\). Replacing \(V_m,P_m\) by \(S,SS^*\) proves (DD1)–(DD5) unchanged. Thus the cyclic-comparison seed can be transported on its own innovation carrier; no arbitrary identification with copies of the source space is required.

## Division means a rule on source expressions

Regard \(\delta_c\) as a column of retained comparison expressions. The proposed division operation rewrites \(C_V\) as a row of coefficients multiplying that column. The coefficients must be finite words in declared preparation, source-transport and boundary-extension operations, with their adjoints and permitted linear combinations. Their construction precedes spectral analysis.

**Finite division conjecture.** A selected presentation of complete sourced sewing admits a terminating rewrite rule for (DD3), compatible with elementary assembly and refinement. Its relations determine the coefficients, word degrees and admissible supports. A geometric overlap estimate then bounds the operator norm of the assembled repair uniformly on the intended family.

The degree and coefficient bounds alone do not control an increasing number of terms. Bounded overlap, orthogonality, or another proved summation estimate must do that work. The rule acts on the actual neutral observable carrier and its state norm. Gauge averaging and ordinary gluing do not qualify merely because they have finite presentations: their comparison defects can vanish on every successfully glued observable. [[algebra/short-loop-holonomy-and-quantitative-gluing|Short-loop repair]] exhibits the distinction between a section-level obstruction and its disappearance on neutral observables.

This is a proposed mathematical operation beyond a new name for an inverse. A spectral pseudoinverse would presuppose the estimate the operation is meant to explain. [[scale-bearing-descent/minimal-conjectures-and-decisive-returns|The minimal conjectural programme]] places finite division between primitive source relations and a reconstructed physical threshold.

## Two successive cuts test coherence

Let \(V:\mathcal H_1\to\mathcal H_0\) and \(W:\mathcal H_2\to\mathcal H_1\) preserve their vacua. Starting with \((\delta_0,B_0,E_0)\), define
\[
\delta_1=V_m^*\delta_0V,\qquad
B_1=V^*B_0V_m+K_V,\qquad E_1=V^*E_0V.
\]
The second lost term must use the **already corrected** \(B_1\):
\[
C_W=W^*B_1(I-W_mW_m^*)\delta_1W,
\qquad C_W=K_W\delta_2,
\qquad \delta_2=W_m^*\delta_1W.
\tag{DD6}
\]
Then
\[
B_2=(VW)^*B_0(VW)_m+W^*K_VW_m+K_W,
\qquad
B_2\delta_2=Q_2-(VW)^*E_0(VW).
\tag{DD7}
\]
For a separately constructed direct correction \(K_{VW}\), the minimum coherence condition is
\[
\bigl(K_{VW}-W^*K_VW_m-K_W\bigr)\delta_2=0.
\tag{DD8}
\]
Successful direct and sequential corrections automatically satisfy this equality; it does not select a rewrite algorithm. A coherent construction must either make their coefficient rows agree or specify how their difference, which annihilates the retained analysis, is identified. It must handle overlapping rewrite paths as well as linear towers.

Iterating exact corrections keeps the inherited error bounded by \(\rho\). It can still make \(\|B_n\|\) diverge. The conjectured finite grammar and overlap estimate must establish \(\sup_n\|B_n\|<\infty\); removing accumulated error is only one part of stable descent.

## A failure identifies what the readout cannot retain

A necessary condition for division is
\[
\ker\delta_c\subseteq\ker C_V.
\tag{DD9}
\]
If \(\delta_cf=0\) but \(C_Vf\ne0\), no correction exists. In finite dimensions the kernel condition permits an unrestricted linear factorization, but says nothing about a primitive-word construction or its norm. In infinite dimensions even a bounded factor requires control of \(\|C_Vf\|/\|\delta_cf\|\); an algebraic factor need not extend continuously.

With the seed hypotheses above, (DD9) is equivalent to \(\ker\delta_c=\mathbb C\Omega_c\): the vacuum lies in both kernels, and (DD2) excludes a further centered kernel vector because \(\rho<1\). Thus finite matrix solvability alone only restates absence of an extra zero mode. The proposed advance is a formula from primitive relations that works across changing carriers with a uniform rebuilt norm.

The [[quantitative-descent/rigidity-certificates-and-soft-escape|concentrating comparison family and triangular gluing matrices]] test the quantitative conjecture. A rule whose coefficients diverge on these families has detected unstable division, not established a uniform bound. A failed factorization suggests a concrete fork: retain the boundary variable responsible for the missing channel, or revise the primitive source law so that its actual retained analysis changes. Renaming the lost channel cannot repair it.

## The first decisive computation

Choose three overlapping finite preparations with a nonproduct joint law from [[conditional-preparation-sewing/inq|conditional preparation sewing]]. Retain every source on the finite carrier, including mixed products. Construct a seed repair directly from the elementary comparison operations, then eliminate two boundary registers in both orders. Compute \(C_V\), \(C_W\), the retained analyses and the proposed coefficient rows from the same law.

The first target is one genuinely lossy family with \(C_V\ne0\), explicit finite-word division and a verified two-cut coherence relation. The rewrite identity must come from formal source relations before matrix evaluation and be reused across the family. An arbitrary finite inverse has finite coefficients and may have a polynomial expression by Cayley–Hamilton; neither fact supplies this construction. Repeated copies sharing boundaries then test whether one rule controls the rebuilt norm. A chosen finite approximation to a continuous gauge carrier must be identified as such; success on its finite source space does not establish completeness in the continuum.

This would construct a mechanism by which remembered residue repairs local comparison. The separate [[two-slice-innovation-geometry/inq|innovation identification]] must show that the retained analysis is the response of the actual chronology. A Yang–Mills return further needs its continuum law and clock. The proposed gain is a finite relation that can be tested before those limits, whose success would explain why stability survives a change of access.

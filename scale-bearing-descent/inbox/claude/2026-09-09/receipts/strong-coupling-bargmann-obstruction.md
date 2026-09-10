# Cyclic-Phase Realizations: What Is Excluded

Three candidate realizations of the (PN1)/(PN9) cyclic premise are tested. Preparations related by any commuting family are excluded exactly, because the cyclic phase is then a coboundary. Charge conjugation of the Wilson measure at zero theta forces the cyclic phase into \(\{0,\pi\}\), which makes the \(\phi=\pi\) hypothesis of (PN1) the only nontrivial value available and (PN3) the sharp ceiling. Euclidean time translates are excluded by transfer-matrix positivity, but that family is not what (PN4) proposes. The strong-coupling plaquette evaluation applies only to translate realizations and is recorded as a negative control.

**Status: [EXACT] for C1–C3 and the Gram optimum; [NEGATIVE CONTROL ONLY, NOT A TEST OF (PN4)] for the strong-coupling evaluation.**

## What the module actually proposes

(PN4) takes \(V_i:\mathcal H_0\to\mathcal H_{\mathrm{hist}}\) to be *three admissible ways of preparing and sewing the same marked experiment*, not three positions of one source. The chronological requirement falls on \(\delta_{\mathrm{phys}}\) through (PN6), not on the \(V_i\). Any test that fixes the \(V_i\) to be spacetime translates is testing a different object.

## C1 — commuting preparations are excluded exactly

Write \(c_{ij}=G_{ij}/|G_{ij}|\) for nonzero overlaps. The cyclic phase \(\phi=\arg(G_{12}G_{23}G_{31})\) is the evaluation of the \(U(1)\)-valued 2-cochain \(c\) on the 2-simplex \(\{1,2,3\}\), and it is invariant under \(V_i\mapsto e^{i\alpha_i}V_i\). Elementary consequence:
\[
\phi=0\iff c_{ij}=\overline{a_i}\,a_j\ \text{for some phases }a_i,
\]
i.e. \(\phi\neq0\) **iff the phase assignment is not a coboundary of any common frame.**

If the three preparations are related by an action of a commuting family — spacetime translations, center twists \(z^{k_i}\), momentum labels, any abelian group — then \(c_{ij}\) depends only on \(g_jg_i^{-1}\) and the three group elements compose to the identity around the triangle. The phases telescope and \(\phi=0\). Center twists in particular: \(c_{ij}=z^{\,q(k_j-k_i)}\) gives \(\sum_{\mathrm{cyc}}(k_j-k_i)=0\).

**A nonzero cyclic phase requires preparations not related by any common frame.** This is the necessity half of the bridge that [[scale-bearing-descent/anomaly-lines-and-the-yang-mills-phase-test|the anomaly-line note]] says is missing: it does not show that an anomaly produces a given phase, but it does show that a nonzero cyclic phase cannot come from data trivializable by line-frame changes. It is also exactly the content of that note's own first experiment — whether *changing the sewing order* forces a phase that cannot be removed by changing line frames.

## C2 — at zero theta the cyclic phase is quantized, which supports (PN1)

The Wilson measure is real and positive and the action is invariant under charge conjugation \(U\mapsto U^{*}\). For gauge-invariant \(A,B\) with \(A\circ C=\bar A\),
\[
\langle A,B\rangle=\int\bar AB\,d\mu
=\int A\bar B\,d\mu=\overline{\langle A,B\rangle},
\]
so the pairing is real. If the three sewings are \(C\)-covariant, every \(G_{ij}\) is real and
\[
\phi\in\{0,\pi\}.
\]
The consequence is not an objection. **The \(\phi=\pi\) hypothesis of (PN1) is the only nontrivial value the theory admits at \(\theta=0\)** — it is forced, not chosen — and (PN3), \(r\le\tfrac12\), is therefore the sharp ceiling. Conjecture I accordingly does not need the anomaly-line bridge: the two hard problems decouple.

Escaping \(\{0,\pi\}\) requires \(C\)-non-covariant sewing, a complex measure (\(\theta\neq0\)), or genuinely line-valued evaluation.

## The Gram optimum over all admissible phases

With equal moduli, \(\det G=1-3r^{2}+2r^{3}\cos\phi\ge0\), and \(\operatorname{Re}\Delta_3\le0\) means \(\cos\phi\le0\):
\[
\cos\phi=-1:\ (2r-1)(r+1)^{2}\le0\Rightarrow r\le\tfrac12
\qquad\text{(this is (PN3))},
\]
\[
\cos\phi=0:\ 1-3r^{2}\ge0\Rightarrow r\le\tfrac1{\sqrt3}\quad\text{(the optimum over }\cos\phi\le0).
\]
Fubini–Study angle floors \(60^\circ\) and \(54.74^\circ\). By C2 the second is unreachable in pure Yang–Mills at \(\theta=0\): **the whole cash value of a continuous phase is the factor \(2/\sqrt3\approx1.155\), and the theory does not offer it.**

## C3 — chronological translates are excluded, but are not the proposal

If \(V_i\) were Euclidean time translates of one centered source, positivity of the Osterwalder–Seiler transfer matrix would give \(G_{ij}=\langle f,T^{|n_i-n_j|}f\rangle/\|f\|^{2}\ge0\) and \(\Delta_3\ge0\) at every coupling and for every compact group. Recorded because it excludes an inviting shortcut, not because (PN4) proposes it. It does mean the chronology entering through (PN6) cannot also be used to generate the three lifts.

## Negative control: translates of a plaquette source at strong coupling

Wilson action, character parameter \(u=c_f/c_0\to0\), centered plaquette source, parallel translates. Leading connected kernel \(C(R)=Ku^{4R}\), \(K>0\) (minimal tube, four plaquettes per step). For the triangle \(x_1=0,x_2=e_1,x_3=e_2\),
\[
\operatorname{Re}\Delta_3=K^{3}u^{16}>0\quad\text{strictly for every }u\in(0,1),
\]
and \(|G_{ij}|\sim u^{4}\ge\tfrac12\) needs \(u\ge2^{-1/4}=0.8409\), the weak-coupling end. The premise fails for this realization at every strong coupling, and its whole domain lies in the branch where the moduli vanish. **This bears on translate realizations only.**

## A rhyme that is not a relation

\([[rg-covariance-residue/wilson-frustration-and-joint-escape|The two-well context]]\) has \(\phi_p=\operatorname{Re}(e^{2\pi i/3})=-\tfrac12\); (PN3) has \(r\le\tfrac12\). These are unrelated: one is a cosine value, the other the root of \((2r-1)(r+1)^{2}\). At cyclic phase \(2\pi/3\) the Gram ceiling is the root of \(r^{3}+3r^{2}-1\), namely \(0.5321\ldots\), not \(\tfrac12\). Recorded under PC1 so the coincidence is not promoted later.

## Numerical receipts

`bargmann-delta3-checks.py`, seed 20260909. Realization-independent; these test the algebra of (PN8)–(PN12).

- **R1** \(\det(2I-G)=\det G-4\operatorname{Re}\Delta_3\): 200 000 random Hermitian unit-diagonal matrices, max residual \(1.56\times10^{-13}\).
- **R2** the (PN9) implication: 400 000 positive semidefinite unit-diagonal samples satisfying the premise. Violations of \(G\le2I\): **0**, largest eigenvalue 1.999998. Violations of \(3\le\mathcal A^{*}\mathcal A\le9\): **0**, range \([3.0525,\,8.9953]\).
- **R3** sharpness: \(G_{ij}=i/\sqrt3\) gives spectrum \(\{0,1,2\}\), \(\operatorname{Re}\Delta_3=0\), \(\mathcal A^{*}\mathcal A=6\).
- **R4** ceilings, \(8\times10^{6}\) samples: \(\cos\phi=-1\) gives 0.498958 against exact \(\tfrac12\); free phase gives 0.576584 against exact \(1/\sqrt3=0.577350\); no sample with \(\cos\phi\le0\) exceeds \(1/\sqrt3\). The \((+\tfrac12,+\tfrac12,-\tfrac12)\) endpoint has spectrum \(\{0,\tfrac32,\tfrac32\}\), matching (PN3).
- **R5** strong-coupling table above (negative control).

## What a surviving realization must satisfy

Not related by any commuting family (C1). Cyclic phase exactly \(\pi\) at \(\theta=0\), hence an odd number of strictly negative real overlaps (C2). Every overlap modulus at or below \(\tfrac12\) (PN3). Not generated by the chronology that (PN6) later consumes (C3).

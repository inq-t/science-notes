---
inq.module: "reverse-prediction-residue-archive"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Reverse-Prediction Residue Archive

A stationary Markov path gives an exact, concrete realization of transfer defect as orthogonal **retrospective prediction residue**: as progressively more of the near future is forgotten, the successive losses in the best prediction of an initial observable form an orthogonal ledger.  In the reversible positive-transfer case this ledger is exactly the defect cascade of the normalized transfer operator; a uniform fixed-slab lower bound on the ledger is equivalent—not merely related—to a transfer gap.  The construction supplies a path-space carrier for residue, but it does not derive the lower bound or turn probabilistic representation into stochastic ontology.

**Typed status.**  The reverse-martingale identities, defect telescopes, tail statement, and fixed-slab equivalence below are **exact**.  The finite Wilson specialization is **exact under the stated transfer-kernel and outer-vacuum-preparation hypotheses**.  Reading an innovation as an emitted physical record is **interpretive**.  A regulator-uniform innovation floor on the complete physical vacuum complement, followed by continuum and Poincare reconstruction, remains **open**.

## 1. The nested carrier is the future, not a single time slice

Let \((X_k)_{k\in\mathbb Z}\) be a stationary Markov chain on a standard Borel state space \(S\), with invariant probability measure \(\nu\).  Write

\[
\mathcal H=L^2(S,\nu),
\qquad
(Pf)(x)=\mathbb E[f(X_1)\mid X_0=x],
\]

and let \(P^*\) denote the Hilbert-space adjoint in \(L^2(\nu)\).  The coordinate maps

\[
J_k:\mathcal H\longrightarrow L^2(\Omega_{\rm path},\mathbb P),
\qquad
J_kf=f(X_k),
\tag{RP1}
\]

are isometries by stationarity.

The relevant decreasing filtration is

\[
\mathcal F_k=\sigma(X_k,X_{k+1},X_{k+2},\ldots),
\qquad
\mathsf E_k=\mathbb E[\,\cdot\mid\mathcal F_k].
\tag{RP2}
\]

It is essential to use the full future tail.  The one-time algebras \(\sigma(X_k)\) are generally not nested, so their conditional expectations do not themselves form a reverse martingale.

## 2. General stationary chain: the archive follows \(P^*\)

For every \(f\in\mathcal H\), stationarity and the Markov property give

\[
M_k^f
:=
\mathsf E_kJ_0f
=
J_k(P^*)^kf.
\tag{RP3}
\]

Thus \((M_k^f)_{k\ge0}\) is a reverse martingale.  Define its innovation at depth \(k\) by

\[
\Delta_k^f
:=
M_k^f-M_{k+1}^f
=
(\mathsf E_k-\mathsf E_{k+1})J_0f.
\tag{RP4}
\]

Because \(\mathsf E_k-\mathsf E_{k+1}\) are mutually orthogonal projections, the increments \(\Delta_k^f\) are pairwise orthogonal.  They need not be probabilistically independent.

The finite-depth decomposition and norm ledger are

\[
J_0f=M_n^f+\sum_{k=0}^{n-1}\Delta_k^f,
\tag{RP5}
\]

\[
\|f\|_\nu^2
=
\|(P^*)^nf\|_\nu^2
+
\sum_{k=0}^{n-1}\|\Delta_k^f\|_{L^2(\mathbb P)}^2.
\tag{RP6}
\]

One step has the exact defect form

\[
\|\Delta_k^f\|^2
=
\left\langle
(P^*)^kf,
(I-PP^*)(P^*)^kf
\right\rangle,
\tag{RP7}
\]

and hence

\[
I-P^n(P^*)^n
=
\sum_{k=0}^{n-1}
P^k(I-PP^*)(P^*)^k.
\tag{RP8}
\]

This orientation matters: the future-filtration archive realizes the defect completion of the **backward contraction** \(P^*\).  For a nonreversible chain it is false to replace \(I-PP^*\) by \(I-P^*P\), or \((P^*)^k\) by \(P^k\), without changing the construction.

## 3. Reversible chain: transfer defect becomes prediction residue

Suppose now that the chain is reversible, so \(P=P^*\).  Then

\[
M_k^f=P^kf(X_k),
\qquad
\Delta_k^f=P^kf(X_k)-P^{k+1}f(X_{k+1}),
\tag{RP9}
\]

and

\[
\|\Delta_k^f\|^2
=
\|(I-P^2)^{1/2}P^kf\|_\nu^2.
\tag{RP10}
\]

Consequently,

\[
I-P^{2n}
=
\sum_{k=0}^{n-1}P^k(I-P^2)P^k,
\tag{RP11}
\]

and the path-space decomposition realizes the abstract isometry

\[
f
\longmapsto
P^nf
\oplus
\bigoplus_{k=0}^{n-1}(I-P^2)^{1/2}P^kf
\tag{RP12}
\]

from [[directed-isometric-residue-completion/inq|Directed Isometric Residue Completion]].  What is new is the carrier: the abstract defect coordinates are represented by successive conditional-prediction losses on a stationary path.

Compression back to the initial slice gives the operator-valued form

\[
J_0^*\mathsf E_kJ_0=P^{2k},
\qquad
J_0^*(\mathsf E_k-\mathsf E_{k+1})J_0
=
P^k(I-P^2)P^k.
\tag{RP13}
\]

[[bridge-score-fusion-geometry/inq|The bridge-score construction]] gives a
different compression of the same stationary path. It inserts a distinction
at the middle of a $2n$-step bridge and conditions on both endpoints. Its
Gramian lies below $I-P^{2n}$, because two endpoints predict at least as
well as one. The reverse archive therefore realizes the full transfer defect
with equality, whereas the bridge score gives a smaller fusion-residue form
whose independently proved lower frame would still suffice for a gap.

This is the same transfer defect isolated by [[vacuum-aligned-transfer-cocycle/inq|Vacuum-Aligned Transfer Cocycle]] and [[two-slice-innovation-geometry/inq|Two-Slice Innovation Geometry]], now resolved by prediction depth.

### Positivity warning

Reversibility makes \(P\) selfadjoint, but it does **not** imply Hilbert-space positivity \(0\le P\le I\).  A reversible period-two chain has an eigenvalue \(-1\), zero defect \(I-P^2\) on that mode, and no positive Hamiltonian logarithm.  Positivity preservation of functions and operator positivity are different predicates.

When \(0\le P\le I\),

\[
I-P\ \le\ I-P^2\ \le\ 2(I-P),
\tag{RP14}
\]

so the innovation defect and the ordinary Dirichlet defect are comparable.  Without spectral nonnegativity, that comparison fails.

## 4. Tail residue is not a gap

Let

\[
\mathcal F_\infty=\bigcap_{k\ge0}\mathcal F_k.
\]

The reverse-martingale theorem gives

\[
M_k^f
\longrightarrow
M_\infty^f
:=
\mathbb E[f(X_0)\mid\mathcal F_\infty]
\quad\text{in }L^2,
\tag{RP15}
\]

and therefore

\[
\|f\|^2
=
\|M_\infty^f\|^2
+
\sum_{k=0}^{\infty}\|\Delta_k^f\|^2.
\tag{RP16}
\]

For selfadjoint \(P\), the compressed tail satisfies

\[
P^{2k}\xrightarrow[s]{k\to\infty}
\mathbf 1_{\{-1,1\}}(P).
\tag{RP17}
\]

If \(0\le P\le I\), only the \(+1\) space remains.  If the chain is ergodic in the fixed-space sense, that fixed space consists of constants.  Fixed-space or shift ergodicity alone does not remove a \(-1\) mode: an irreducible period-two chain is the elementary counterexample.  Some probability texts build aperiodicity into the word “ergodic”; no such convention is being assumed here.

Even when every centered vector has vanishing tail prediction, there need not be a uniform decay rate.  Spectrum may accumulate at \(1\).  Thus tail triviality or strong convergence \(P^nf\to0\) on each centered vector is strictly weaker than a spectral gap.

## 5. A fixed-slab innovation floor is exactly a transfer gap

Let

\[
\mathcal H_0=\operatorname{Fix}(P)^\perp.
\tag{RP18}
\]

Only after ergodicity may this be identified with the mean-zero space \(L^2_0(\nu)\).  In the reversible case define the innovation captured through depth \(n\) by

\[
\mathfrak I_n(f)
:=
\sum_{k=0}^{n-1}\|\Delta_k^f\|^2
=
\|f\|^2-\|P^nf\|^2.
\tag{RP19}
\]

Then the optimal fixed-slab floor is

\[
\inf_{\substack{f\in\mathcal H_0\\ \|f\|=1}}
\mathfrak I_n(f)
=
1-\|P^n|_{\mathcal H_0}\|^2.
\tag{RP20}
\]

Therefore, for \(0<\kappa<1\),

\[
\mathfrak I_n(f)\ge\kappa\|f\|^2
\quad(f\in\mathcal H_0)
\quad\Longleftrightarrow\quad
\|P^n|_{\mathcal H_0}\|
\le\sqrt{1-\kappa}.
\tag{RP21}
\]

If Osterwalder-Schrader reconstruction identifies

\[
P=e^{-a_\tau(H-E_0)/(\hbar c)},
\qquad
\ell=na_\tau,
\tag{RP22}
\]

then (RP21) gives

\[
\Delta_E
\ge
-\frac{\hbar c}{2\ell}\log(1-\kappa).
\tag{RP23}
\]

Conversely, an energy gap \(\Delta_E\) gives the optimal floor

\[
\kappa_n
=
1-e^{-2\ell\Delta_E/(\hbar c)}.
\tag{RP24}
\]

The factor \(1/2\) is forced by the squared norm in (RP20).  A proof of an innovation floor is therefore a proof of the corresponding transfer contraction; the archive does not make the analytic estimate easier by definition.  It may, however, expose a more geometric object on which to seek the estimate.

This equivalence is the filtration form of the past-future contraction studied in [[contemporary-puzzles/yang-mills-mass-gap/past-future-angle-and-the-transfer-gap|Past-Future Angle and the Transfer Gap]].

## 6. Finite Wilson specialization: prepare the vacuum at the outer walls

At a fixed finite spatial lattice and regulator, let \(T\) be the physical one-step Wilson transfer operator on the gauge-invariant slice carrier.  Assume:

- \(T\) is compact, selfadjoint, injective, and spectrally positive;
- its kernel \(K_T(U,V)\) is symmetric and nonnegative;
- positivity improvement gives a simple top eigenvalue \(\lambda_0>0\) with a strictly positive, normalized, gauge-invariant eigenfunction \(\psi_0\).

Set

\[
\widehat T=T/\lambda_0,
\qquad
d\nu(U)=\psi_0(U)^2\,d\mu_H(U),
\tag{RP25}
\]

and define the Doob transform

\[
(Pf)(U)
=
\frac{\widehat T(\psi_0f)(U)}{\psi_0(U)}.
\tag{RP26}
\]

Then \(P\) is a reversible Markov contraction on \(L^2(\nu)\), unitarily equivalent to \(\widehat T\) through multiplication by \(\psi_0\).  Its consecutive-slice edge law is

\[
d\mathsf J_P(U,V)
=
\psi_0(U)\,\widehat K(U,V)\,\psi_0(V)
\,d\mu_H(U)d\mu_H(V),
\tag{RP27}
\]

where \(\widehat K=K_T/\lambda_0\).  This is the solder supplied by [[markov-edge-measure-solder/inq|Markov Edge-Measure Solder]].

The stationary path should be obtained from **outer vacuum preparation**, not from a periodic two-cut law.  Let nonnegative outer boundary vectors \(b_\pm\) have nonzero vacuum overlap and write

\[
F_{\pm,N}=\widehat T^Nb_\pm.
\]

For a fixed central window \((U_0,\ldots,U_r)\), its finite-volume density is proportional to

\[
F_{-,N}(U_0)
\left(\prod_{j=0}^{r-1}\widehat K(U_j,U_{j+1})\right)
F_{+,N}(U_r)
\prod_{j=0}^{r}d\mu_H(U_j).
\tag{RP28}
\]

As both outer walls recede, vacuum dominance gives

\[
F_{\pm,N}\longrightarrow c_\pm\psi_0,
\qquad c_\pm>0,
\tag{RP29}
\]

and the normalized central-window law converges to

\[
\nu(dU_0)
P(U_0,dU_1)\cdots P(U_{r-1},dU_r).
\tag{RP30}
\]

Indeed, the factors of \(\psi_0\) telescope exactly under (RP26).  This is the stationary Doob path to which (RP1)-(RP24) apply.  The preparation theorem and its boundary hypotheses are developed in [[contemporary-puzzles/yang-mills-mass-gap/vacuum-boundary-gluing-and-wall-response|Vacuum Boundary Gluing and Wall Response]].

A periodic two-cut density proportional to

\[
|K_N(U,V)|^2
\tag{RP31}
\]

describes two cuts separated around a periodic cylinder.  It tends toward a product of vacuum marginals as the separation grows.  It is not the consecutive-slice transition law (RP27), and using it for the reverse-prediction archive would erase precisely the finite-step correlation being resolved.

The Wilson archive is consequently exact at finite regulator:

\[
f(U_0)
=
P^nf(U_n)
+
\sum_{k=0}^{n-1}
\bigl(P^kf(U_k)-P^{k+1}f(U_{k+1})\bigr),
\tag{RP32}
\]

with orthogonality and norm ledger (RP10)-(RP11).  It remains a gap reformulation until a regulator-uniform lower bound is proved.

## 7. Stochastic-ontology firewall

Nothing in this construction says that nature chooses outcomes by an ontologically random mechanism.

Here the probability law is a representation of a positive transfer kernel and its vacuum state.  Conditional expectation is the orthogonal projection associated with partial path information.  The increment \(\Delta_k^f\) records what ceases to be predictable about the initial observable when the first \(k\) slices have been discarded.  It is a **retrospective information residue**, not a microscopic event, a wave-function collapse, an entropy production theorem, or an autonomous causal carrier.

The archive is also not automatically the complete physical complement.  Gauge, boundary, balance, sector, and global tail directions must be controlled rather than silently omitted; [[vacuum-aligned-innovation-completion/inq|Vacuum-Aligned Innovation Completion]] isolates that completeness issue.  A genuinely noncommutative or Type III realization would require additional operator-algebraic work beyond this commutative path-space model.

## 8. Exact open stopping condition

Let \(P_{a,L,\mathsf s}\) be the stationary physical Doob operator at regulator \(a\), spatial size \(L\), and allowed sector/boundary label \(\mathsf s\).  Let

\[
Q_{a,L,\mathsf s}
=
I-\Pi_{\operatorname{Fix}(P_{a,L,\mathsf s})}
\tag{RP33}
\]

be the **complete** orthogonal complement of all fixed directions.  Choose \(n(a)\) so that

\[
n(a)a_\tau\longrightarrow\ell_*>0.
\tag{RP34}
\]

The archive closes the transfer-gap step precisely when one proves, from gauge geometry rather than an assumed gap, constants \(\kappa_*>0\) and \(a_0>0\) such that

\[
\inf_{0<a<a_0}
\inf_{L,\mathsf s}
\inf_{\substack{f\in\operatorname{Ran}Q_{a,L,\mathsf s}\\\|f\|=1}}
\sum_{k=0}^{n(a)-1}
\|\Delta_{k,a,L,\mathsf s}^{f}\|^2
\ge
\kappa_*.
\tag{RP35}
\]

By the exact ledger, (RP35) is equivalent to

\[
\limsup_{a\downarrow0}
\sup_{L,\mathsf s}
\left\|
P_{a,L,\mathsf s}^{\,n(a)}Q_{a,L,\mathsf s}
\right\|
\le
\sqrt{1-\kappa_*}<1.
\tag{RP36}
\]

Under a uniform Osterwalder-Schrader transfer identification this yields

\[
\Delta_E
\ge
-\frac{\hbar c}{2\ell_*}\log(1-\kappa_*)>0.
\tag{RP37}
\]

This is the exact stopping condition for the archive, not the full Yang-Mills stopping condition.  One must still prove the independent estimate (RP35), construct the continuum theory, and identify the reconstructed energy threshold with a positive Poincare mass.  Strong-coupling estimates that collapse under continuum scaling do not suffice; see [[strong-coupling-gap-and-continuum-crossover/inq|Strong-Coupling Gap and Continuum Crossover]].

The finite-state calculation in [[reverse-prediction-residue-archive/receipts/reverse_prediction_residue_receipt.py|reverse-prediction residue receipt]] checks the conditional formula, orthogonality, both operator orientations, the fixed-slab optimum, and the reversible period-two obstruction.  Its stored result is [[reverse-prediction-residue-archive/receipts/reverse_prediction_residue_receipt-output.txt|receipt output]].

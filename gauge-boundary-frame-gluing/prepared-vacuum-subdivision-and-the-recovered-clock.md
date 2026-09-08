# Subdivision Erases the Prepared-Vacuum Fisher Correction

Rebuilding independent paired-path sources after inserting physically redundant vertices changes the prepared-vacuum Fisher response, even when the complete physical state, Hamiltonian and observable carrier are unchanged. On an arbitrary finite gauge graph, uniform subdivision makes the correction vanish and recovers the already supplied electric ground-state form in norm resolvent. The construction therefore gives a useful finite-presentation comparison, but its subdivision completion does not select a new dynamics from the vacuum. The defect concerns source preparation, not nonassociative multiplication.

**Status: exact finite-graph identities and a redundant-subdivision limit.** The Hamiltonian and vacuum are inputs. This limit introduces no new physical degrees of freedom and is not a four-dimensional continuum limit or a mass-gap construction.

## Fix the physical theory before changing its presentation

Let \(\Gamma\) be a finite connected oriented graph with no self-loops,
\(G=SU(2)\), \(Q=-2\operatorname{Tr}\), and normalized product Haar
measure. Allow a smooth real gauge-invariant potential \(V\). Set
\[
H=\sum_e\kappa_eD_{Q,e}+V,\qquad \kappa_e>0,
\qquad H\psi=E_0\psi,\qquad w=\psi^2,
\tag{PS1}
\]
where \(\psi\) is the normalized smooth strictly positive ground
vector. Compact ellipticity and positivity improvement give this
vector, and uniqueness makes it gauge invariant, as in
[[coarse-response-memory/interacting-gauge-vacuum-and-local-memory|the finite physical-vacuum construction]].
The full physical ground-state carrier and form are
\[
\mathcal H_w=L^2(w\,dY)^{G^{V(\Gamma)}},\qquad
\mathcal E_{\rm phys}(f)=\sum_e\kappa_e
 \mathbb E_w|\nabla_e f|_Q^2.
\tag{PS2}
\]
The domain is the inherited invariant \(H^1\), not a newly selected
domain on singular orbit coordinates.

Replace each edge by a chain of \(n\) segments and write
\(\pi_n\) for their ordered products. Introduce no extra loops or
interactions. On the fine graph choose
\[
H_n=\sum_e\sum_{j=1}^n\frac{\kappa_e}{n}D_{Q,e,j}
       +V\circ\pi_n,\qquad J_nf=f\circ\pi_n.
\tag{PS3}
\]
The product-Haar pushforward is Haar. Internal vertex invariance
makes every fine physical function depend only on these products.
Thus \(J_n\) is onto the complete fine gauge-invariant carrier,
not merely an embedding of selected loops.

Bi-invariance gives
\(D_{Q,e,j}J_n=J_nD_{Q,e}\), so
\[
H_nJ_n=J_nH,\qquad \psi_n=\psi\circ\pi_n,
\qquad w_n=w\circ\pi_n.
\tag{PS4}
\]
The displayed \(\psi_n\) is normalized, positive and an eigenvector;
it is therefore the actual fine ground vector, including on the raw
compact configuration space. This proves the vacuum relation rather
than assuming matching marginals for independently chosen vacua.
The invariant physical operators are unitarily equivalent, and
their ground-state forms agree exactly under \(J_n\).
[[holonomy-refinement-and-clock-compatibility#A product holonomy has an additive diffusion budget|Additive electric weights]]
are essential to this assertion.

## Rebuild the source, keeping its calibration explicit

Give original edge \(e\) a heat age \(t_e>0\) and equal endpoint
splits. Fix a single \(E_*>0\) such that
\[
\kappa_e=2E_*t_e.
\tag{PS5}
\]
Each fine segment has heat age \(t_e/n\), again with equal splits.
At each presentation prepare the actual endpoint law by the
paired bridges and density ratio in
[[physical-vacuum-lift-and-fisher-comparison|the physical-vacuum lift]].
The reference densities cancel to give exactly \(w_n\).
This rebuilds independent source controls on the fine segments;
it does **not** transport the complete original source action.

For an original invariant function define its two endpoint slots by
\[
p_f=(\nabla_{L,e}f,-\nabla_{R,e}f)_e,
\quad D_0=\operatorname{diag}_e(t_e,t_e)\otimes I_3,
\quad \mathsf I_w=\mathbb E_w[p_{\log w}p_{\log w}^*],
\quad \mathsf B=D_0^{1/2}\mathsf I_wD_0^{1/2}.
\tag{PS6}
\]
The original source response is
\(\mathbb E_w\langle D_0^{1/2}p_f,(I+\mathsf B)^{-1}
D_0^{1/2}p_f\rangle\). The same formula defines the fine response
\(\mathcal E_{{\rm F},n}\) using \(w_n,D_{0,n}\).
All one-link marginals are Haar, including the fine ones, so the
preparation's reference-density Hessian vanishes. The remaining
positive correction is exactly the density-score covariance.

Write \(\mathcal F_n(f)=\mathcal E_{{\rm F},n}(J_nf)\) and
\[
\mathcal E_{\rm ref}(f)=2\sum_et_e\mathbb E_w|\nabla_e f|^2,
\qquad E_*\mathcal E_{\rm ref}=\mathcal E_{\rm phys}.
\tag{PS7}
\]
The comparison uses one fixed calibration. Changing it separately
at each presentation would be a different test.

## The complete Fisher inverse splits into vertex blocks

Independent vertex gauge covariance kills score covariance between
different vertices. At an original vertex, the fine endpoint
covectors coincide with their coarse counterparts, while their
heat variances are divided by \(n\). Hence that block of the fine
dimensionless Fisher correction is exactly \(\mathsf B_v/n\).

At a new bivalent vertex, Gauss invariance makes the two slot
covectors opposite. They are transported copies of the same
coarse-edge derivative. Put
\[
s_e=\frac13\mathbb E_w|\nabla_e\log w|^2\ge0.
\tag{PS8}
\]
Invariance under the vertex's adjoint rotations gives its score
covariance and dimensionless correction:
\[
\mathsf I_{e,\rm int}
=s_e\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\otimes I_3,
\qquad
\mathsf B_{e,\rm int}^{(n)}
=\frac{t_es_e}{n}
 \begin{pmatrix}1&-1\\-1&1\end{pmatrix}\otimes I_3.
\tag{PS9}
\]
The factor \(1/3\) is the adjoint multiplicity, not an adjustable
coefficient. The norm of this block is \(2t_es_e/n\).

Let \(q_{f,v}\) denote the original vertex slots of
\(D_0^{1/2}p_f\). Inverting every block before contracting gives
the exact full-carrier formula
\[
\boxed{
\begin{aligned}
\mathcal F_n(f)
={}&\frac1n\sum_{v\in V(\Gamma)}
 \mathbb E_w\langle q_{f,v},
       (I+\mathsf B_v/n)^{-1}q_{f,v}\rangle\\
 &+\sum_e\frac{2t_e(1-1/n)}{1+2t_es_e/n}
       \mathbb E_w|\nabla_e f|^2.
\end{aligned}}
\tag{PS10}
\]
The second line sums the \(n-1\) new vertices along each edge.
Each has physical slot vector proportional to \((a,-a)\), the
nonzero-eigenvalue direction in (PS9). Transport rotations drop
out of its norm. The original vertices retain all their mixed
incident-edge blocks; no diagonal approximation is made.

## Redundant refinement recovers the supplied physical clock

Set
\[
C=\max\left\{\|\mathsf B\|,\max_e2t_es_e\right\}<\infty.
\tag{PS11}
\]
The complete fine correction has norm at most \(C/n\). Positivity,
full matrix inversion and the additive gradient identity imply
\[
\boxed{
\frac{\mathcal E_{\rm ref}(f)}{1+C/n}
\le\mathcal F_n(f)\le\mathcal E_{\rm ref}(f).
}
\tag{PS12}
\]
These inequalities extend from invariant smooth functions to the
same complete invariant \(H^1\) domain. In particular the closed
forms converge in relative form norm to \(\mathcal E_{\rm ref}\).
The state and physical spectrum have not changed anywhere in this
sequence.

Let \(L_n\) be the operator of \(E_*\mathcal F_n\) on
\(\mathcal H_w\), and \(L_{\rm phys}\) the operator of (PS2).
For \(z>0\), put \(\alpha_n=(1+C/n)^{-1}\). Form order and
resolvent monotonicity give
\[
\begin{aligned}
0&\le(L_n+z)^{-1}-(L_{\rm phys}+z)^{-1}\\
 &\le(\alpha_n L_{\rm phys}+z)^{-1}
             -(L_{\rm phys}+z)^{-1},\\
\left\|(L_n+z)^{-1}-(L_{\rm phys}+z)^{-1}\right\|
 &\le\frac{1-\sqrt{\alpha_n}}{z(1+\sqrt{\alpha_n})}.
\end{aligned}
\tag{PS13}
\]
For the last bound maximize
\((\alpha_n x+z)^{-1}-(x+z)^{-1}\) over \(x\ge0\).
No commutation of \(L_n\) with \(L_{\rm phys}\) is assumed.
Thus the recovered clock is precisely the supplied physical
ground-state clock, in norm resolvent, not a newly selected operator.

For original open cubical boxes with uniform \(t_e=t\),
\(\kappa_e=\kappa\), and the Wilson magnetic potential
\(V=\lambda\sum_p(1-q_p)\), \(\lambda\ge0\), the earlier
local kinetic estimate gives
\(2ts_e\le(32/3)t\lambda/\kappa\). Together with the equal-split
vertex estimate, one may take
\[
C\le32t\lambda/\kappa.
\tag{PS14}
\]
This is uniform in the original box volume at fixed coupling
ratio. It still is not uniform along an unspecified running-coupling
limit. Subdividing the edges of a fixed box without adding
plaquettes is not spatial continuum Yang--Mills refinement.

## Exact naturality and dilution force the reference form

There is a general consequence, independent of the one-cycle
calculation below. If \(w\) is nonconstant, the actual original
Fisher form has the strictly positive defect
\[
\mathcal E_{\rm ref}(\log w)-\mathcal F_1(\log w)
=\operatorname{Tr}[\mathsf B^2(I+\mathsf B)^{-1}]>0.
\tag{PS17}
\]
Exact naturality under all redundant subdivisions would require
\(\mathcal F_n=\mathcal F_1\) on the identified full carrier.
Equation (PS12) would then imply
\(\mathcal F_1=\mathcal E_{\rm ref}\), contradicting (PS17).
This proves failure somewhere along every such tower for any
nonconstant prepared vacuum, without selecting a trial loop.

More generally, an exactly subdivision-natural response family
cannot retain a nonzero correction if it also obeys a uniform
relative squeeze toward the reference form with error tending
to zero on this unchanged carrier. Naturality makes its pulled-back
form constant along the tower; the squeeze identifies that
constant with the reference form. This is a rigidity implication,
not a uniqueness theorem for all possible source constructions.

Consequently a nontrivial replacement must change at least one
of those hypotheses. Coherently transported cross-segment data
could prevent the correction from being diluted; an additional
physical datum could instead distinguish the presentations.
These possibilities require construction. Merely inserting new
coefficient counterterms would not derive their selection.

## An interacting cycle makes the mismatch explicit

On a simple \(N\)-edge cycle, \(N\ge3\), full gauge reduction
is the space of class functions of \(W=Y_1\cdots Y_N\).
Choose total electric weight \(K\), total heat age \(L\), and
\(V=\lambda(1-q(W))\), with \(q=\tfrac12\operatorname{Tr}\).
The exact physical reduction and its vacuum are
\[
H_{\rm cl}=KD_Q+\lambda(1-q),\qquad
H_{\rm cl}\psi=E_0\psi,\qquad w=\psi^2.
\tag{PS15}
\]
Take equal edge ages \(L/N\), weights \(K/N\), and endpoint splits.
All vertex blocks have the same scalar
\(s=\mathbb E_w|\nabla\log w|^2/3\). Their complete inverse gives
\[
\boxed{
\mathcal E_{{\rm F},N}(f)
=\frac{2L}{1+2sL/N}\mathbb E_w|\nabla f|^2,
\qquad E_*=\frac K{2L}.
}
\tag{PS16}
\]
For \(\lambda>0\), the vacuum is nonconstant, hence \(s>0\).
Increasing \(N\) by uniform subdivision strictly changes the
response for every nonconstant class observable, while preserving
the complete physical operator. At \(\lambda=0\), \(s=0\) and
the defect vanishes. The equal-subdivision qualification matters;
arbitrary simultaneous changes of endpoint splits need not have
this monotonicity.

An actual-vacuum numerical test uses the orthonormal characters
\(\chi_j=U_j(q)\), \(j=0,1,\ldots\). Here
\(D_Q\chi_j=j(j+2)\chi_j/4\) and
\(q\chi_j=(\chi_{j+1}+\chi_{j-1})/2\), with \(\chi_{-1}=0\).
Thus the finite character truncation of (PS15) is tridiagonal,
not a chosen exponential tilt. Its convergence and the
full vertex-matrix inversion are checked by
[[receipts/prepared_vacuum_subdivision_receipt.py|the prepared-vacuum receipt]].
Numerical convergence is evidence for the calculation; (PS4),
(PS9) and (PS16), not a cutoff diagonalization, prove the result.

At \(K=L=1\), \(\lambda=0.7\), the character cutoffs
\(4,8,16,32\) give \(E_0\simeq0.553855620218\) and
\(s\simeq0.158829082712\). The full character-space residual,
including the omitted neighbor of the last retained character,
decreases from \(1.145\times10^{-4}\) to floating-point scale.
Positive Haar quadratures at \(96,192,384\) nodes agree on the
score integral. For the same \(q\) observable and vacuum norm:

| Cycle edges | Calibrated Fisher energy | Physical energy |
| --- | --- | --- |
| 4 | 0.157861541576 | 0.170398043498 |
| 8 | 0.163890402909 | 0.170398043498 |
| 16 | 0.167080880622 | 0.170398043498 |

Actual Pauli derivatives and vertex rotations check the score
blocks before the full \(24,48,96\)-dimensional inversions.
These are floating-point finite-model checks, not rigorous
interval enclosures or evidence of a newly generated physical gap.

## What must change in the primitive law

The original state, its physical spectrum and the additive heat
budget survive subdivision. The rebuilt comparison experiment
does not: it installs fresh independent controls and performs
fresh gauge averaging at the new vertices. That makes the
averaged score correction small without making the physical
state less interacting. Static state gluing therefore does not
fix the comparison law.

[[source-action-transport-through-ordered-cuts|Transporting complete source actions]]
preserves an already chosen response, but that covariance theorem
does not select the action. Taking the subdivision completion
studied here instead returns the independently supplied electric
geometry. Neither operation derives the vacuum or the gap.

[[source-action-transport-through-ordered-cuts#Coherent spatial extension retains its reference experiment|The coherent spatial extension]]
now proves the distinction on the same fine output law. Cutting
complete retained paths and adding Haar interface frames gives
exactly the fine physical vacuum and preserves the original
response. But extensions from four and eight cycle edges retain
different responses on the same sixteen-edge presentation.
Covariance repairs transport, not reference-experiment selection.

This calculation is not an associator: all holonomy products and
source transformations used in it are associative. The
[[algebra/octonionic-associator-and-branch-forgetting|projected-product associator]]
concerns discarded intermediate multiplication channels, a
different operator type. A nonassociative replacement would need
to constrain admissible comparison actions or interaction data
and preserve the required observable carrier; the present
presentation defect alone is not evidence for that replacement.

The next selecting test must therefore act on the **joint law of
comparison and readout**, rather than independently rebuilding
an entropy Hessian from a static density at every presentation.
It must specify which source changes are genuine equivalences,
which additional channels are physical, and how the compatible
response constrains the state rather than merely accepting it.

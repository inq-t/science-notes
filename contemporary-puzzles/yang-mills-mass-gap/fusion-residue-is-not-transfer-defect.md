# Fusion Residue Is Not Yet Transfer Defect

A pointed CP composition and a Euclidean transfer both admit exact notions of
what is forgotten, but the two residues live on different carriers.  The
fusion residue removes intermediate factorization directions when a fused
correspondence is compressed to the minimal correspondence of the composite
channel.  The transfer defect measures loss of norm of physical slice
distinctions across a slab. A stationary commutative path supplies a bounded
middle-insertion solder for the upper comparison, but the existence of either
residue by itself does not provide the regulator-uniform lower frame needed
for a positive edge.

**Status: [EXACT] for the carrier and operator distinction, cyclic-lift
no-go, path-space transfer defect, and stationary commutative middle-insertion
upper solder; [CONDITIONAL THEOREM] for a fusion-response lower frame implying
a transfer gap; [OPEN CONSTRUCTION/ESTIMATE] for its gauge/OS realization and
regulator-uniform lower bound in Yang--Mills theory.**

## The categorical residue acts on fused histories

Let

$$
\Phi:A\longrightarrow B,
\qquad
\Psi:B\longrightarrow C
$$

be normal UCP maps, and let $E_\Phi,E_\Psi,E_{\Psi\Phi}$ be their pointed
self-dual GNS correspondences.  The canonical isometry

$$
v_{\Phi,\Psi}:E_{\Psi\Phi}\longrightarrow
E_\Phi\bar\otimes_BE_\Psi,
\qquad
v_{\Phi,\Psi}\xi_{\Psi\Phi}=\xi_\Phi\otimes\xi_\Psi
$$

has cyclic range.  Its adjoint

$$
U_{\Phi,\Psi}:=v_{\Phi,\Psi}^*
$$

is a coisometry.  Put

$$
p_{\mathrm{cyc}}:=v_{\Phi,\Psi}v_{\Phi,\Psi}^*,
\qquad
r_{\mathrm{fus}}:=I-p_{\mathrm{cyc}}.
\tag{FRT1}
$$

Then

$$
\ker U_{\Phi,\Psi}
=r_{\mathrm{fus}}
\bigl(E_\Phi\bar\otimes_BE_\Psi\bigr).
\tag{FRT2}
$$

For every fused-history vector $z$, orthogonality gives the exact
$C$-valued ledger

$$
\boxed{
\langle z,z\rangle_C
=
\langle U_{\Phi,\Psi}z,U_{\Phi,\Psi}z\rangle_C
+
\langle r_{\mathrm{fus}}z,r_{\mathrm{fus}}z\rangle_C.}
\tag{FRT3}
$$

Thus the minimal composite channel forgets the component orthogonal to the
cyclic endpoint correspondence.  In the commutative finite-state model,
the fused carrier distinguishes paths $i\to j\to k$, while the composite
channel retains only the weighted endpoint direction $i\to k$.  Orthogonal
contrasts among different intermediate $j$'s form the fusion residue.

This is an exact algebraic form of forgotten intermediate ambiguity.  It is
not yet temporal attenuation: $r_{\mathrm{fus}}$ acts on a fused
correspondence, not on the Hilbert carrier of physical slice observables.

## The canonical endpoint lift cannot witness its own fusion residue

The decisive no-go is immediate:

$$
\boxed{r_{\mathrm{fus}}v_{\Phi,\Psi}=0.}
\tag{FRT4}
$$

Consequently the most obvious attempt to pull the residue back to the
minimal composite carrier gives zero,

$$
v_{\Phi,\Psi}^*r_{\mathrm{fus}}v_{\Phi,\Psi}=0.
\tag{FRT5}
$$

No positive gap on endpoint distinctions can therefore follow merely from
the fact that the fusion inclusion is proper.  A history-sensitive analysis
must enter the noncyclic directions before projection onto
$r_{\mathrm{fus}}$ can have a nonzero pullback.  This is the precise place
where a carrier-changing realization, rather than another scalar analogy,
is required; the stationary commutative construction below supplies one
without supplying its lower frame.

The commutative model identifies the mismatch even more sharply.  The fused
carrier resolves triples $i\to j\to k$, and its cyclic range consists of the
weighted functions of the two endpoints $(i,k)$.  Therefore
$r_{\mathrm{fus}}$ is the conditional-mean-zero **bridge** carrier: it
distinguishes alternative middle routes after both endpoints are fixed.  It
is not the residue of predicting the initial endpoint from the final one.

### The Wilson bridge cancels Perron dressing only fiberwise

For a finite regulated Wilson sandwich
\(T=cM_aKM_a\), the conditional middle-slice law of two vacuum-aligned
Doob steps is

$$
\boxed{
\beta_T^{U,Z}(\mathrm dY)
=
\frac{k(U,Y)a(Y)^2k(Y,Z)}
{\int k(U,Y')a(Y')^2k(Y',Z)\,\mathrm d\mu_{\mathrm H}(Y')}
\,\mathrm d\mu_{\mathrm H}(Y).}
\tag{FRT5a}
$$

The Perron vector, maximal eigenvalue, scalar normalization, and endpoint
weights cancel from this conditional fiber; the middle weight \(a(Y)^2\)
does not. The cancellation does **not** remove Perron weighting from the
endpoint law or the global direct-integral norm. An endpoint-only factor
depending on \((U,Z)\) also cancels from (FRT5a), so its bridge score is zero.

On a stationary path, however, the middle embedding
\(J_nf=f(X_n)\) supplies the missing history-sensitive analysis:

$$
\boxed{
L_n^{\mathrm{br}}
:=(I-\mathsf E_{0,2n})J_n,
\qquad
(L_n^{\mathrm{br}})^*L_n^{\mathrm{br}}
\leq I-(P^*)^nP^n,}
\tag{FRT5b}
$$

and the right side is \(I-P^{2n}\) for reversible \(P\). Thus the stationary
commutative specialization canonically realizes the **upper** comparison in
(FRT11), with \(\Gamma=J_n\) and bridge-residue projection
\(I-\mathsf E_{0,2n}\). Its endpointwise exponential-tilt score is
\(L_n^{\mathrm{br}}f\), while the normalized half-density Gramian is one
quarter of the score Fisher Gramian. The lower frame in (FRT11) remains a
separate sufficient estimate; it is neither a consequence of the upper
bound nor of nonzero fusion residue. [[bridge-score-fusion-geometry/inq|Bridge-Score Fusion Geometry]]
proves these statements, their support caveats, and the exact kernel and
minorization criteria.

Nor can the rank or mere nonvanishing of this bridge carrier supply a rate.
For

$$
\Theta_t^{(\varepsilon)}
=e^{-\varepsilon t}\operatorname{id}
+(1-e^{-\varepsilon t})E
$$

on $\mathbb C^2$, with $E$ the average onto constants, every
$\varepsilon>0$ gives a rank-four two-stage fusion residue for positive
times, while the centered generator edge is $\varepsilon$ and can approach
zero.  The projection norm remains one throughout.  Qualitative route
multiplicity is therefore not quantitative coercivity; a metric-weighted
analysis and a uniform lower frame are indispensable.

The local-unitarity clue must be typed with the same care.  A carrier is not
itself unitary or nonunitary; those predicates belong to arrows.  The descent
$U_{\Phi,\Psi}$ can be a proper coisometry while an independently supplied
unitary $q$ acts on $E_{\Psi\Phi}$.  Indeed

$$
\widetilde q
:=
v_{\Phi,\Psi}qv_{\Phi,\Psi}^*+r_{\mathrm{fus}}
\tag{FRT6}
$$

is a unitary on the fused carrier and

$$
U_{\Phi,\Psi}\widetilde q=qU_{\Phi,\Psi}.
\tag{FRT7}
$$

Local unitarity is therefore compatible with a noninvertible endpoint
descent, but it is not manufactured by the forgotten complement.  Equation
(FRT7), not the phrase “nonunitary so that unitary,” is the exact connective.

## The dynamical residue acts on physical slice distinctions

Let $P$ be the contraction induced by a stationary slice transfer on
$\mathcal H=L^2(\nu)$, and let $J_0:\mathcal H\to L^2(\mathbb P)$ embed an
initial-slice function in the stationary path carrier.  For the decreasing
future filtration

$$
\mathcal F_k=\sigma(X_k,X_{k+1},\ldots),
$$

write $\mathsf E_k$ for conditional expectation onto
$L^2(\mathcal F_k)$.  In the reversible case,

$$
J_0^*(\mathsf E_0-\mathsf E_n)J_0
=I-P^{2n}.
\tag{FRT8}
$$

This operator has the correct type.  It acts on the same slice Hilbert
carrier as $P^n$ and equals the canonical transfer defect

$$
D_n^{\mathrm{tr}}
:=I-(P^n)^*P^n.
\tag{FRT9}
$$

The path-space filtration therefore supplies a genuine realization of the
abstract defect.  It is distinct from (FRT1):

| residue | operator carrier | what is forgotten |
|---|---|---|
| $r_{\mathrm{fus}}$ | $E_\Phi\bar\otimes_BE_\Psi$ | intermediate correspondence directions absent from the minimal composite |
| $\mathsf E_0-\mathsf E_n$ | $L^2(\mathbb P)$ | initial distinctions no longer predictable from the remote future |
| $D_n^{\mathrm{tr}}$ | $L^2(\nu)$ | squared-norm survival under the physical slab transfer |

The second pulls back exactly to the third.  There is no canonical equality
between the first and either of the other two.

## The missing solder and the stopping condition

For a general noncommutative fusion residue, one must first scalarize or
represent the fused correspondence on a Hilbert carrier
$\mathcal K_{a,L}^{\mathrm{fus}}$, then construct a bounded,
history-sensitive analysis. The stationary commutative bridge specialization
above supplies the canonical choice \(\Gamma=J_n\); outside it, this remains
an additional construction:

$$
\Gamma_{a,L}:\mathcal H_{0,a,L}\longrightarrow
\mathcal K_{a,L}^{\mathrm{fus}},
\qquad
L_{a,L}:=r_{\mathrm{fus},a,L}\Gamma_{a,L},
\tag{FRT10}
$$

on the complete gauge-invariant vacuum complement.  The domain-correct
comparison and lower frame are

$$
\boxed{
L_{a,L}^*L_{a,L}
\leq I-P_{a,L}^{2n(a)},
\qquad
L_{a,L}^*L_{a,L}
\geq\kappa_*I,
\qquad
\kappa_*>0.}
\tag{FRT11}
$$

If $n(a)a_{\tau,a}\to\ell_*>0$ and both inequalities are uniform in
volume, admissible boundary or flux sector, and regulator removal, then

$$
\|P_{a,L}^{n(a)}|_{\mathcal H_{0,a,L}}\|
\leq\sqrt{1-\kappa_*}.
\tag{FRT12}
$$

After the independent positive-transfer, OS, and Poincare identifications,
this gives

$$
\Delta_E
\geq
-\frac{\hbar c}{2\ell_*}\log(1-\kappa_*).
\tag{FRT13}
$$

The first inequality in (FRT11) is the carrier solder; the second is the
coercive geometric theorem.  Proper fusion, a nonzero categorical dimension,
or a finite-state path multiplicity proves neither.  Conversely, the
reverse-prediction archive supplies the first inequality with equality but
does not independently prove the second.  This isolates the remaining
Yang--Mills problem without asking a local QFT Hamiltonian to explain the
pre-QFT origin of its own carrier.

## Dependencies

[[pointed-cp-fusion-residue/inq|Pointed CP Fusion Residue]] proves the
correspondence inclusion, coisometric descent, and subproduct-system law.
[[bridge-score-fusion-geometry/inq|Bridge-Score Fusion Geometry]] proves the
commutative direct-integral bridge residue, its score normalization, and the
middle-insertion upper comparison.
[[reverse-prediction-residue-archive/inq|The Reverse-Prediction Residue
Archive]] proves (FRT8) and the finite-slab equivalence.
[[directed-isometric-residue-completion/inq|Directed Isometric Residue
Completion]] supplies the universal Hilbert transfer-defect completion.
[[transported-response-observability-solder/inq|Transported Response
Observability Solder]] supplies the general comparison pattern used in
(FRT11).  [[spectral-wall-descent/scale-correspondence-stack|The
scale-correspondence stack]] records the still-open realization from abstract
correspondences to causal cuts, states, and physical response carriers.

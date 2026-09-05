# Finite-Patch Coercivity from the Algebra of Conditional Projections

For a finite Wilson law, conditional expectations give bounded orthogonal projections on one common \(L^2\) carrier. Their noncommutation is confined to links sharing a plaquette. Cubes containing whole links then have an exact overlap identity: a conditional patch gap above \(1/n\) forces a volume-independent gap for the sum of single-link innovations. This is a concrete local-to-global criterion on the actual law, not a physical mass theorem or a claim that finite-volume positivity alone survives the continuum.

**Status: exact projection theorem and finite Wilson specialization; fixed-patch weak-coupling obstructions and open physical reconstruction.** The method is an adaptation of Knabe-type projection counting; [[library/spectral-gaps-and-incompressibility-in-a-fractional-quantum-hall-system/inq|Nachtergaele--Warzel--Young, Section 3.5, Theorem 3.10]] supplies a primary account of the cyclic version. The plaquette-incidence geometry and same-law application below are proved explicitly.

## What the operator operates on

Let \(\mu\) be a smooth strictly positive Gibbs law on a finite product of compact link groups, relative to product Haar measure. For a link set \(B\), define
\[
P_Bf=\mathbb E_\mu[f\mid U_{B^c}],\qquad
Q_e=I-P_{\{e\}},\qquad
H_{\rm hb}=\sum_e Q_e.
\tag{FP1}
\]
All these operators act on \(L^2(\mu)\). The nonnegative generator \(H_{\rm hb}\) returns the rate-one-per-link conditional-refresh form
\[
\langle f,H_{\rm hb}f\rangle=\sum_e\|Q_ef\|^2.
\]
It is not the generator of spacetime translation. Normalizing by the number of links would divide its gap by that number and change the rate convention.

If no interaction term meets both \(e\) and \(f\), their conditional joint law given the other variables factors, so
\[
P_{\{e\}}P_{\{f\}}=P_{\{f\}}P_{\{e\}}=P_{\{e,f\}}.
\tag{FP2}
\]
Thus \(Q_e,Q_f\) commute. Shared **undifferentiated** neighbors do not defeat this conditional independence. For Wilson plaquette interactions, only plaquette-sharing pairs can fail to commute.

Put \(h_B=\sum_{e\in B}Q_e\). Equivalence to product Haar measure gives
\[
\ker h_B=L^2(U_{B^c}),\qquad
\gamma_B(I-P_B)\le h_B\le |B|(I-P_B),
\tag{FP3}
\]
where the first inequality is an additional spectral estimate. The kernel identity follows because a common fixed vector of the single-coordinate expectations is independent of each coordinate in \(B\). It does not assert a positive \(\gamma_B\) by notation.

The patch operator is a direct integral over its frozen exterior. Consequently the needed \(\gamma_B\) is the essential-infimum of the **actual conditional patch** gaps. All plaquettes touching \(B\) remain in that conditional action. A free-boundary or marginal patch sampler, or an average of conditional gaps, is a different input.

## The weighted-patch identity

Let \(\{Q_e\}_{e\in E}\) be any finite family of orthogonal projections on any Hilbert space; no finite-dimensional tensor product is required. Choose patches \(B\) with positive weights \(w_B\). Suppose
\[
\sum_{B\ni e}w_B=\rho,\qquad
c_{ef}:=\sum_{B\ni e,f}w_B
\begin{cases}
=\kappa,&[Q_e,Q_f]\ne0,\\
\le\kappa,&[Q_e,Q_f]=0,
\end{cases}
\quad e\ne f,\qquad \rho,\kappa>0.
\tag{FP4}
\]
Assume \(h_B^2\ge\gamma h_B\) for every patch. With \(H=\sum_eQ_e\), expansion of the bounded squares yields
\[
A:=\sum_Bw_Bh_B^2
=\rho H+\sum_{e<f}c_{ef}\{Q_e,Q_f\}.
\]
For commuting projections, \(\{Q_e,Q_f\}=2Q_eQ_f\ge0\); for noncommuting pairs the coefficients agree exactly. Hence
\[
\rho\gamma H\le A\le
\kappa H^2+(\rho-\kappa)H,
\]
and therefore
\[
\boxed{
H^2\ge\left[1+\frac{\rho}{\kappa}(\gamma-1)\right]H.}
\tag{FP5}
\]
If the bracket is \(\eta>0\), the spectral theorem gives
\(H\ge\eta(I-P_{\ker H})\). This controls the entire complement, including collective directions. The invariant here is an **overlap ratio of compatible projections**, not a count of spacetime pixels.

## Whole-link cubes match the Wilson noncommutation geometry

Use a periodic \(d\)-dimensional cubic lattice, \(d\ge2\), with each side longer than \(2n\), \(n\ge2\). For each translate of a vertex cube containing \(n\) vertices in each direction, let \(B\) contain every positively oriented link whose **both endpoints** are in that cube. This is not the patch of links whose initial vertices alone lie in a cube.

Each link belongs to
\[
\rho=(n-1)n^{d-1}
\]
patches. Every pair sharing a plaquette has a bounding box of one lattice unit in two axes, and belongs to exactly
\[
\kappa=(n-1)^2n^{d-2}
\tag{FP6}
\]
patches. Every other pair has overlap at most \(\kappa\): distinct perpendicular links span at least two axes; distinct parallel links either span two axes or span at least two units in their common direction. The latter case obeys
\((n-2)n^{d-1}\le(n-1)^2n^{d-2}\).
Pairs too far apart have zero overlap. The side-length restriction excludes competing wrapped short intervals in this counting.

Thus the complete conditional patch bound
\[
h_B\ge\gamma_n(I-P_B),\qquad \gamma_n>1/n
\quad\text{uniformly over translates and exterior data}
\tag{FP7}
\]
implies
\[
\boxed{
H_{\rm hb}\ge
\frac{n\gamma_n-1}{n-1}(I-P_0),\qquad
P_0f=\mu f.}
\tag{FP8}
\]
This threshold is dimension independent for this **plaquette-sharing** graph. Other interaction graphs require their own overlap counts; the criterion cannot be imported merely from the phrase "nearest neighbor." Single-site heat-bath projections for nearest-neighbor interactions on the same cubic lattice also yield \(1/n\), now using vertex patches with \(\rho=n^d\) and \(\kappa=(n-1)n^{d-1}\). None of these counting identities selects the dimension four.

Gauge invariance of the law makes all conditional projections preserve the gauge-invariant subspace. Its restriction inherits (FP8). The groups may be continuous: bounded projection algebra did not replace \(SU(3)\) by a finite-state model.

At \(\beta=0\), product Haar has \(\gamma_n=1\), and the bound returns the sharp global heat-bath gap one. More generally, if the actual conditional density has maximum/minimum ratio at most \(e^{a_n}\) relative to product Haar, the variational formulas for variance and conditional variance give \(\gamma_n\ge e^{-a_n}\). Thus \(a_n<\log n\) is a sufficient, generally very restrictive certificate. The criterion is not vacuous, but this elementary bounded-density estimate does not reach weak-bare-coupling continuum physics.

## An enlarged remainder is not absorbed by declaring its coefficient small

For a family of blocks \(K_i\), define
\[
\mathcal H_{\rm block}[f]=\sum_i\|(I-P_{K_i})f\|^2.
\]
Suppose every coordinate lies in exactly \(r\) blocks. Any full-carrier comparison
\(\mathcal H_{\rm block}\le C\mathcal H_{\rm hb}\) requires \(C\ge r\): test a nonconstant function of one coordinate \(e\). Its other single-coordinate innovations vanish, while \(I-P_K\ge Q_e\) whenever \(e\in K\).

There is a neutral-sector test for the parallel-link families in [[rg-covariance-residue/wilson-frustration-and-joint-escape|joint Wilson escape]]. Let \(f=\operatorname{ReTr}U_p/3\) be a plaquette observable. Only its four links contribute to \(\mathcal H_{\rm hb}[f]\), and a parallel-link block contains at most two of them. Therefore
\[
\mathcal H_{\rm block}[f]\ge\frac r2\mathcal H_{\rm hb}[f]>0.
\tag{FP9}
\]
Indeed, each block variance dominates every included single-link variance, hence at least half their sum. Summing counts each plaquette link \(r\) times.

The seven-link remainder with coefficient \(6/7\) therefore cannot be directly absorbed through any such scalar comparison: already \((6/7)(r/2)=3>1\). Changing the block-rate convention only moves the factor \(r\). This rules out that absorption route, not localized remainders, different derivatives or a physical gap.

The three-link family in [[rg-covariance-residue/coherent-staple-localization|coherent staple localization]] has an even sharper incidence test. Write \(K_e=\{e,e\pm\hat\tau(\mu)\}\) for an active link of orientation \(\mu\), with one fixed transverse choice \(\tau(\mu)\). Four directed choices cover at most four of the six coordinate planes. Choose a plaquette in a plane \(\{\mu,\nu\}\) with \(\tau(\mu)\ne\nu\) and \(\tau(\nu)\ne\mu\). Every block contains at most one of its links, and each link belongs to exactly three blocks. Its gauge-invariant trace therefore gives
\[
\mathcal H_{\mathrm{block}}[f]\ge3\mathcal H_{\mathrm{hb}}[f]>0,
\qquad C\ge3
\quad\text{whenever }\mathcal H_{\mathrm{block}}\le C\mathcal H_{\mathrm{hb}}
\text{ on the invariant carrier}.
\tag{FP10}
\]
This uses projection order, not independence of the Wilson links. At product Haar the ratio is exactly three: integrating any one plaquette link kills its trace, and twelve blocks meet the plaquette once.

No stronger negative cut margin repairs direct scalar absorption of that same estimate. Testing \(U=W_1\) in the two-staple support gives
\[
h_3(W_1+W_2)\ge1+\tfrac13\operatorname{ReTr}(W_1^*W_2)\ge\tfrac12.
\]
The ten exterior traces are each at least \(-1/2\), so \(T_I\ge-9/2\). Every nonempty fixed cut \(T_I\le-r\) thus has \(r\le9/2\), and its residual coefficient obeys
\[
b=\frac{12}{r+12}\ge\frac8{11},\qquad bC\ge\frac{24}{11}>1.
\tag{FP11}
\]
The conclusion concerns this unlocalized scalar block comparison, with its stated family and rate convention. It does not forbid weighted/localized remainders or different derivatives. [[rg-covariance-residue/second-ring-commuting-escape|A second-ring derivative]] in fact removes the enlarged remainder on a new cut containing the displayed coherent-support example.

The former 73-link remainder had the same problem, but [[rg-covariance-residue/critical-context-and-collective-escape|commuting collective escape]] removes it entirely. Its active conditional is unchanged by the selected derivatives, so its localizer retains \(Q_e\), not \(I-P_{K_e}\). If complementary contexts are controlled, [[lyapunov-localization-certificate#Commuting escape preserves the original innovation|same-innovation absorption]] then uses (FP8) in the correct direction to obtain a gradient Poincare bound.

## The quotient test and the physical limit

The full-carrier condition (FP7) is sufficient, but [[gauge-reduced-patch-coercivity|interior gauge reduction]] proves that it is too strong along weak coupling for every fixed \(n\ge3\). An interior gauge-dependent link retains a Haar marginal while a complementary plaquette path predicts it increasingly well. Its Rayleigh quotient forces the essential-uniform full conditional gap to be \(O_B(\log\beta/\beta)\), so it eventually falls below \(1/n\). This does not test the physical invariant sector.

The correctly typed sufficient input is the actual conditional patch bound on **interior-gauge-invariant** functions, retaining all boundary data. Such a bound implies the squared patch inequality on the globally invariant carrier; the same counting then gives (FP8) on that carrier with the reduced patch constant. A gauge-refresh completion supplies an equivalent full conditional test without changing the invariant dynamics. Neither boundary averaging nor deletion of physical low modes is allowed.

[[weak-coupling-patch-threshold|Testing this reduced input]] now gives an actual nonlinear obstruction. For every fixed \(n\ge3\), its essential-uniform gap has weak-coupling limsup at most \(1-\cos(\pi/(n+1))<1/n\). A quadratic loop test also rules out the patch inequality on the global invariant carrier for every fixed \(n\ge8\). Thus the corresponding fixed-size input is false, not merely unverified. The Gaussian bound at \(n=2\) reaches the threshold without deciding a finite-coupling margin. Growing patches, different patch geometries and sharper comparison thresholds remain separate possibilities; none has been certified here.

Even success here proves an auxiliary whole-law inequality, not the existence of a continuum Yang--Mills theory. [[global-local-response-reconstruction/exceptional-context-analysis-of-gauge-gradients|The differentiated-context analysis]] and [[global-local-response-reconstruction/quantitative-descent-and-the-shape-of-a-gap|quantitative descent]] retain the physical carrier, boundary-response, scale and reconstruction obligations. No choice of units identifies \(H_{\rm hb}\) with the Wilson transfer Hamiltonian.

[[tensor-local-refresh-and-inverse-square-patches|Tensor-local refresh]] now provides an inverse-square replacement criterion on a different assigned-star patch family. It does not invalidate the fixed-cube obstruction or certify the new regional margin.

The [[receipts/finite_patch_projection_receipt.py|finite receipt]] checks projection counting, noncommutative matrix inequalities and actual finite conditional laws. It does not certify the \(SU(3)\) patch gap (FP7).

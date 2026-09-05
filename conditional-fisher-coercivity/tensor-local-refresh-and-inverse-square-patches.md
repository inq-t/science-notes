# Tensor-Local Refresh and an Inverse-Square Patch Criterion

The Wilson conditional-refresh operator becomes genuinely tensor-local after multiplication by the square root of its Gibbs density. Its projection geometry therefore admits an inverse-square finite-region criterion, with no finite-dimensional approximation of the compact gauge group. This replaces the scale dependence of the earlier sufficient threshold, but requires different, precisely assigned patches and their actual invariant-sector gaps. Those estimates and the physical continuum comparison remain unproved.

**Status: exact finite-Wilson conjugation and geometric assignment; an adaptation of an established projection criterion without finite local Hilbert dimension; no certified weak-coupling patch margin or physical gap.**

## Locality survives the change of Hilbert norm

On a finite nondegenerate periodic lattice, write
\[
d\mu(U)=\rho(U)\,dm(U),\qquad
\rho=Z^{-1}e^{-S(U)},
\]
where \(m\) is product Haar, \(S\) is the Wilson action at finite coupling, and
\[
P_ef=\mathbb E_\mu[f\mid U_{e^c}],\qquad Q_e=I-P_e.
\]
The map
\[
J:L^2(\mu)\longrightarrow L^2(m),\qquad Jf=\sqrt\rho\,f
\tag{TP1}
\]
is unitary. Split \(S=S_e+S_{\neg e}\), with \(S_e\) the sum of plaquette terms touching \(e\). For retained variables \(R=U_{e^c}\), set
\[
z_e(R)=\int e^{-S_e(v,R)}\,dm_e(v),\qquad
q_e(u\mid R)=z_e(R)^{-1}e^{-S_e(u,R)}.
\]
Direct cancellation of \(S_{\neg e}\) gives
\[
\boxed{
(\widetilde P_e\psi)(u,R)
=\sqrt{q_e(u\mid R)}
\int\sqrt{q_e(v\mid R)}\,\psi(v,R)\,dm_e(v),\qquad
\widetilde P_e=JP_eJ^{-1}.}
\tag{TP2}
\]
Only the plaquette-star neighbors occur in \(q_e\). Thus \(\widetilde P_e\), and its defect \(\widetilde Q_e\), act on that star's tensor factors and as identity elsewhere. The star can overlap another star through control variables even when the two projections commute. Tensor support and actual noncommutation are different graphs.

The operator \(\widetilde H=\sum_e\widetilde Q_e\) is frustration free, with common zero line \(\mathbb C\sqrt\rho\). This line is the transformed constant of the auxiliary Gibbs process, not an independently identified physical Yang--Mills vacuum. Neither (TP1) nor (TP2) identifies sampler time with physical clock time.

## Assign each term to one coarse cell

Assume even fine torus side lengths \(2N_\nu\), and group the outgoing-link variables at each \(2^d\)-site block into one tensor factor. No group variable or observable is removed.

For \(e=(x,\mu)\), plaquette-star link origins range within
\[
[x_\mu,x_\mu+1]\quad\text{along }\mu,\qquad
[x_\nu-1,x_\nu+1]\quad\text{along }\nu\ne\mu.
\]
Each interval meets at most two adjacent side-two blocks. Assign the term the padded elementary coarse cube with anchor
\[
a_\mu(e)=\lfloor x_\mu/2\rfloor,\qquad
a_\nu(e)=\lfloor(x_\nu-1)/2\rfloor\quad(\nu\ne\mu),
\tag{TP3}
\]
with indices interpreted periodically. Its declared support is
\(a(e)+\{0,1\}^d\). Padding an unused axis is allowed; assigning a term twice is not. There are exactly \(d\,2^d\) original projections per anchor cube, and they remain separate projections.

For a coarse rectangle \(R\), define
\[
B_R=\{e:a(e)+\{0,1\}^d\subset R\},\qquad
h_R=\sum_{e\in B_R}Q_e.
\tag{TP4}
\]
A rectangle of \(t^d\) coarse vertices has \(|B_R|=d\,2^d(t-1)^d\). This active set is not the old whole-link cube of [[weak-coupling-patch-threshold|the path obstruction]]. Its undeleted star variables form a retained collar. The conditional law keeps all original plaquettes touching \(B_R\); there is no free-boundary action substitution.

Each projection fails to commute with at most
\[
g_d=6(d-1)
\]
others, by plaquette sharing. On this even torus,
\[
\operatorname{color}(x,\mu)
=2\mu+\left(\sum_{\nu\ne\mu}x_\nu\bmod2\right)
\tag{TP5}
\]
gives \(L_d=2d\) commuting layers. Parallel links in one plaquette have opposite parity; perpendicular links have different orientation labels. These bounds do not depend on color-group dimension.

## The quantitative criterion

Fix either the complete \(L^2(\mu)\) carrier or its globally gauge-invariant reducing subspace \(\mathcal K\). Let \(\gamma\) be the gap of \(H_{\rm hb}|_{\mathcal K}\), and let
\[
a_t=\min_{R:\,\operatorname{side}(R)=t}
\operatorname{gap}(h_R|_{\mathcal K}).
\tag{TP6}
\]
Every regional gap is measured above that regional operator's **full kernel**, not merely above constants. A proved lower certificate may replace \(a_t\).

[[library/improved-local-spectral-gap-thresholds/inq|Anshu, Appendix C, Theorem C.1]], gives the inverse-square estimate below; Appendix B permits multiple terms per neighboring-cell interaction. Apply its projection proof to (TP2)--(TP5). For
\[
t>\max\{8L_d^2,\,64\,4^dL_d\},\qquad
t<\tfrac15\min_\nu N_\nu,\qquad
C_d^{\rm patch}=200L_d^2g_d^2\,6^d,
\]
the resulting sufficient bound is
\[
\boxed{
\gamma\ge
\min\left\{\frac{g_d^2}{16^d},
\frac{a_t-C_d^{\rm patch}/t^2}{6^d}\right\}.}
\tag{TP7}
\]
It is positive only when the displayed margin is positive.

### Why no finite color cutoff is needed

This is an adaptation of the proof, not a claim that its spin-space statement literally names \(L^2(SU(q))\). The argument uses finite products of bounded projections, spectral functional calculus, spatial commutation and absorption by regional kernel projections. These operations are valid here. Spectral infima and approximate Rayleigh vectors replace smallest-eigenvalue wording.

The two-layer converse also needs no finite Jordan decomposition. For orthogonal projections \(A,B\), put \(a=\|(I-A)x\|^2\), \(b=\|(I-B)x\|^2\). Then
\[
\|x\|^2-\|BAx\|^2
\le a+(\sqrt a+\sqrt b)^2
\le3(a+b).
\tag{TP8}
\]
For each commuting layer its complement is bounded above by the sum of the layer's defects. Thus the same factor three survives.

At each finite Wilson regulator, the positive bounded density relative to product Haar gives strictly positive complete finite-subset refresh gaps, albeit with constants that can deteriorate badly. No infinite-volume positivity is inferred from this preliminary fact.

Finally, gauge invariance makes \(J\) intertwine the gauge actions. Each \(Q_e\), each \(h_R\), and each regional kernel projection reduces the global invariant subspace. The bounded projection argument therefore restricts to \(\mathcal K\) even though \(\mathcal K\) itself is not a tensor product. Independent regional boundary averaging would be a different operation.

To see the two branches of (TP7), when \(\gamma>g_d^2/16^d\) use that bound directly. Otherwise the adapted finite-size estimate is
\(a_t\le6^d\gamma+C_d^{\rm patch}/t^2\).
Rearrangement gives the second branch. Taking a minimum combines them without assuming an unproved small global gap.

## What has improved, and what has not

The old \(1/n\) threshold is not a necessary local signature of a gapped system. Inverse-square thresholds fit the scaling of long-wavelength quadratic modes. However, equal scaling exponents do not establish a numerical margin, and (TP7)'s constants are deliberately conservative. The new patches also differ from the ones in the previous obstruction; that theorem cannot be transplanted with \(n=t\).

The criterion still requires the least actual regional gap, not an average over favorable exteriors. It establishes an auxiliary whole-law bound if its premises are proved. A gauge completion may help with redundant directions but cannot change invariant dynamics.

[[rg-covariance-residue/gaussian-harmonic-refresh-lifting|The harmonic-lift construction]] supplies a complementary Gaussian route: retain slow data and compare a joint fine/coarse response in one step. Its independence and uniform lift estimates do not yet extend to the nonlinear Wilson law.

The [[receipts/tensor_local_patch_receipt.py|finite receipt]] checks the density transform on actual finite Gibbs laws, the support assignment, layer counts and elementary projection estimates. It does not test a weak-coupling margin or the large-volume hypotheses of (TP7).

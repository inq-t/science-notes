# Additive Neutral Sources and the Pairing-Range Test

Arbitrary sums of one-face quadratic observables retain a uniform positive OI floor in the harmonic planar vacuum, even when every face participates and the coefficients vary with the patch. The known soft collective source therefore requires mixed bilinears between faces. This identifies pairing range, rather than the number of local readouts alone, as the next discriminating source variable.

**Status: exact additive-quadratic bound and a defined mixed-range test in the harmonic law.** [[gaussian-collar-memory-and-the-complete-radial-source|GC]] controls each complete one-face radial algebra. The calculation here controls the growing linear span of their quadratic elements, which is a different source space. [[inherited-planar-vacuum-and-the-regional-time-law|IR]] fixes the covariance, full chronology and common color frame.

## The full quadratic response is a matrix form

On the open \(L\times L\) face grid let \(A=4I-\operatorname{Adj}\), \(C=\sqrt A\), and let \(X_\alpha\) have covariance \(C\), independently for the three colors. For a real symmetric matrix \(B\), define
\[
F_B=\sum_{\alpha=1}^3 X_\alpha^{\mathsf T}B X_\alpha
       -3\operatorname{Tr}(BC).
\]
These are physical invariants under the common color rotation. Wick contraction gives, for \(D_t=Ce^{-tC}\),
\[
\boxed{
\mathcal B_t(B,N):=\langle F_B,P_tF_N\rangle
=6\operatorname{Tr}(BD_tND_t),\qquad
\|F_B\|^2=6\operatorname{Tr}(BCBC).}
\tag{AR1}
\]
In particular the vacuum centering and all mixed source terms are fixed. Differentiating at zero gives
\[
\boxed{\langle F_B,K_0F_B\rangle
=12\operatorname{Tr}(BABC).}
\tag{AR2}
\]
Here \(K_0\) denotes the nonnegative ground-transformed harmonic generator. In its normal coordinates, \(F_B\) is pure Hermite degree two. Its spectral support consists of sums of two frequencies of \(C\), hence lies in \((0,2\sqrt8)\).

## Additive local sources have a uniform lower mean energy

For \(B=\operatorname{diag}(d)\), equations (AR1)–(AR2) reduce to
\[
\|F_B\|^2=6d^{\mathsf T}(C\circ C)d,\qquad
\langle F_B,K_0F_B\rangle=12d^{\mathsf T}(A\circ C)d,
\]
where \(\circ\) is the entrywise product. The matrix inequality \(C\ge A/\sqrt8\) gives
\[
A\circ C\ge\frac{A\circ A}{\sqrt8}
=\frac{16I+\operatorname{Adj}}{\sqrt8}
\ge\frac{12}{\sqrt8}I.
\]
The entrywise product preserves positivity because a product of two Gram matrices is the Gram matrix of their tensor-product vectors. Meanwhile \(C\circ C\) has nonnegative entries and every row sum is
\(\sum_q C_{pq}^2=(C^2)_{pp}=4\). Its operator norm is therefore at most four. It follows that
\[
\boxed{
\frac{\langle F_B,K_0F_B\rangle}{\|F_B\|^2}
\ge\frac6{\sqrt8}=\frac3{\sqrt2},
\qquad B=\operatorname{diag}(d)\ne0.}
\tag{AR3}
\]
There is no positivity requirement on \(d\), and its support need not remain fixed as \(L\) grows.

Let \(\nu_B\) be the normalized spectral measure of \(F_B\), put
\(r_t(\lambda)=1-e^{-2t\lambda}\), and set \(M=2\sqrt8\). The original OI quotient is
\[
\mathfrak q_t(F_B)
=\frac{\int r_t^2\,d\nu_B}{\int r_t\,d\nu_B}
\ge\int r_t\,d\nu_B
\ge\frac{1-e^{-2tM}}{M}\int\lambda\,d\nu_B.
\]
The first inequality is Cauchy–Schwarz, and the second is the chord bound for the concave function \(r_t\) on \([0,M]\). Combining this with (AR3) proves
\[
\boxed{
\mathfrak q_t(F_{\operatorname{diag}(d)})
\ge\frac38(1-e^{-4\sqrt8t})>0,\qquad t>0,}
\tag{AR4}
\]
uniformly in \(L\) and every nonzero coefficient vector. This is a quotient estimate on a source subspace, not a claim that this subspace is invariant under \(P_t\).

## Vary the range of the relational bilinears

For integer \(R\ge0\), define the exact harmonic discriminator
\[
\boxed{
c_R(t)=\inf_{\substack{L,\ B=B^{\mathsf T}\ne0\\
 B_{pq}=0\ \mathrm{if}\ |p-q|_\infty>R}}
\frac{\mathcal B_0(B,B)-2\mathcal B_{2t}(B,B)+\mathcal B_{4t}(B,B)}
     {\mathcal B_0(B,B)-\mathcal B_{2t}(B,B)}.}
\tag{AR5}
\]
Equation (AR4) gives \(c_0(t)>0\). With unrestricted range, the rank-one matrix of the lowest spatial mode gives the already-known quotient tending to zero in [[planar-patch-confinement-and-the-spatial-soft-mode|PP]]. Finite-box matrices are all eventually admitted as \(R\) grows, so \(c_R(t)\) is nonincreasing and tends to zero. The unanswered question is whether it is positive for each fixed finite \(R\), and at what rate the best bound deteriorates.

This test retains off-diagonal \(X_p\cdot X_q\), not merely correlations between scalar readouts. [[fixed-regional-sources-and-the-compact-vacuum-return|FR15]] supplies fixed mixed compact marks; a growing matrix inventory would require its own uniform return. [[conditional-vacuum-rigidity-and-the-physical-gap|CV]] owns the complete mixed-source obligation, and [[spatial-block-sewing-and-the-vacuum-cap-response|SB]] owns the additional history terms. No compact growing-source theorem or four-dimensional physical gap is asserted here.

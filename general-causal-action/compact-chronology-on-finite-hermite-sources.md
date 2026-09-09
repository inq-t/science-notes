# Compact Chronology on Finite Hermite Sources

The actual vacuum-subtracted compact planar evolution returns the harmonic chronology on every fixed Hermite-degree physical subspace, with an explicit error uniform in patch size. The proof compares the actual generators after the exact Haar-density cutoff and then applies Duhamel along the degree-preserving harmonic evolution. Centered harmonic vectors admit an error bound uniform over all scaled times. The comparison retains the actual vacuum energy and does not identify the two complete Hilbert spaces.

**Status: proved finite-degree chronological return on the confinement window.** Use the full Gauss carrier and comb coordinates of [[planar-patch-confinement-and-the-spatial-soft-mode|PP]] and [[comb-face-transport-and-the-first-nonlinear-jet|FJ]]. [[compact-operator-taylor-remainder-on-planar-wells|OT]] supplies the interior operator estimate, [[compact-cutoffs-and-uniform-polynomial-quasimodes|CQ]] supplies the physical cutoff, and [[uniform-nonlinear-planar-gap-and-marked-response|UN]] supplies the actual vacuum-energy return.

## Retain the actual vacuum subtraction and cutoff

Put \(n=L+1\), \(h=(\kappa/g)^{1/4}\), and
\[
\epsilon=hn^{10},\qquad
\theta=hn^{11/2},\qquad
\tau=hn^{3/2}.
\]
Work throughout \(0<\epsilon\le\eta\), for a sufficiently small constant independent of \(L,h\). Let
\[
\widehat H=h^2\mathsf C_{\rm raw}+h^{-2}W,\qquad
\widehat K=\widehat H-E_0(L,h),\qquad
K_0=V_0-e_0(L),
\tag{HC1}
\]
where \(E_0\) is the actual scaled vacuum energy and \(e_0\) is the absolute oscillator vacuum energy. Both subtracted operators are nonnegative. Their semigroups act on the compact Haar physical space and invariant oscillator space, respectively.

Let \(P_{m,L}\) be the oscillator projector onto total Hermite degree at most fixed \(m\), restricted to simultaneous color invariants. Let \(\mathcal J=\mathcal J_{L,h}\) be CQ3's exact density transform with its magnetic cutoff of original radius \(\delta_*/\sqrt n\). Thus \(\|\mathcal J\|\le1\), and \(\mathcal J P_{m,L}\) consists of smooth physical compact vectors in \(\operatorname{Dom}\widehat H\). No degree bound independent of \(m\) is asserted.

The vacuum branch in UN4–UN5, with UC20's coefficient bounds and parity, gives
\[
\boxed{|E_0(L,h)-e_0(L)|\le Ch^2n^{10}.}
\tag{HC2}
\]
Indeed the subsequent \(h^4,h^6\) terms and sixth-order residual, divided by \(h^2n^{10}\), are bounded by \(C(\theta^2+\theta^4+\theta^5)\). The absolute energy \(e_0=O(n^2)\) has not been bounded by a small quantity or replaced by a gap.

## The generator defect is an actual norm estimate

For \(u\in\operatorname{ran}P_{m,L}\), use CQ11 with \(M=1\), cutoff tail order \(q=1\), scalar \(z=E_0\), and forcing \(f=K_0u\). Since
\[
(V_0+hV_1-E_0)u-K_0u
=hV_1u-(E_0-e_0)u,
\]
UC15, OT8 and CQ9 give
\[
\begin{aligned}
\|(\widehat K\mathcal J-\mathcal J K_0)u\|
\le C_m\bigl(
hn^{9/2}+h^2n^{10}+h^2n^7+h^3n^5
\bigr)\|u\|.
\end{aligned}
\tag{HC3}
\]
The four terms retain the first jet, actual vacuum shift, interior operator remainder and cutoff commutator. The last term is \(hn^2\tau^2\). In the stated window each term is bounded by a constant times the first, so
\[
\boxed{
\|(\widehat K\mathcal J-\mathcal J K_0)P_{m,L}\|
\le \alpha_{m,L,h},\qquad
\alpha_{m,L,h}=C_mhn^{9/2}.}
\tag{HC4}
\]
This is a norm of a map from the indicated finite-degree subspace into the actual compact Hilbert space. It is not a norm bound for a difference of the full unbounded generators. The estimate is linear in \(\|u\|\), including when a family of inputs has norm \(O(n)\).

## Duhamel follows the complete harmonic time evolution

The harmonic semigroup preserves \(P_{m,L}\) and contracts its norm. For every \(t\ge0\), differentiation on this finite-dimensional smooth domain gives
\[
\begin{aligned}
e^{-t\widehat K}\mathcal Ju-\mathcal J e^{-tK_0}u
={}&-\int_0^t e^{-(t-s)\widehat K}
(\widehat K\mathcal J-\mathcal J K_0)
e^{-sK_0}u\,ds .
\end{aligned}
\tag{HC5}
\]
For fixed \(L,h\), the curve \(s\mapsto\mathcal J e^{-sK_0}u\) is continuously differentiable in the compact operator domain with its graph norm. This justifies the identity at the endpoints as well as in the interior. Nonnegativity of the actual vacuum-subtracted generator bounds the left semigroup in the integrand by one.

Consequently
\[
\boxed{
\|(e^{-t\widehat K}\mathcal J-\mathcal J e^{-tK_0})P_{m,L}\|
\le \min\{C_m t\,hn^{9/2},\,2\}.}
\tag{HC6}
\]
The second bound uses only the two contractions and \(\|\mathcal J\|\le1\). In particular the error on \(0\le t\le T\), for fixed scaled \(T\), is at most \(C_mT\epsilon n^{-11/2}\). The constant in (HC6) does not depend on a chosen time interval.

There is a useful refinement for centered physical vectors. Write \(Q_0=I-|\Omega\rangle\langle\Omega|\). The complete physical oscillator gap in [[planar-physical-cluster-separation-and-the-uniform-window|PS]] is
\[
c_L=4\sqrt2\sin\frac{\pi}{2n}\ge\frac8n.
\]
For \(u\in\operatorname{ran}(P_{m,L}Q_0)\), the norm in the Duhamel integrand therefore decays as \(e^{-c_Ls}\). Hence
\[
\boxed{
\|(e^{-t\widehat K}\mathcal J-\mathcal J e^{-tK_0})
P_{m,L}Q_0\|
\le C_mhn^{9/2}\frac{1-e^{-c_Lt}}{c_L}
\le C_m\theta,\qquad t\ge0.}
\tag{HC7}
\]
The embedded vector need not be exactly centered in the actual vacuum. Any such component remains included in this estimate. The bound does not justify integrating a uniform error over an infinite time interval.

## Matrix elements retain the embedding and source burden

CQ5 with \(q=1\), applied to both vectors in the cutoff tail, gives
\[
|\langle\mathcal Ju,\mathcal Jv\rangle-\langle u,v\rangle|
\le C_m\tau^4\|u\|\|v\|,
\qquad u,v\in\operatorname{ran}P_{m,L}.
\tag{HC8}
\]
Indeed \(1-\chi^2\) is supported in that tail, and each tail norm is at most \(C_m\tau^2\) times its full norm. Combining this with (HC6) yields
\[
\begin{aligned}
&|\langle\mathcal Ju,e^{-t\widehat K}\mathcal Jv\rangle
-\langle u,e^{-tK_0}v\rangle|\\
&\qquad\le
\bigl[\min\{C_mt\,hn^{9/2},2\}+C_m\tau^4\bigr]\|u\|\|v\|.
\end{aligned}
\tag{HC9}
\]
If \(v\) is centered, the semigroup term can instead be bounded by the right side of (HC7). These estimates apply to arbitrary physical vectors of the prescribed degree, including quadratic neutral profiles that are superpositions of many oscillator energies.

To use (HC9) as an actual vacuum correlation theorem, the centered compact source vector must separately be compared with \(\mathcal Jv\), retaining its actual mean and variance. The chronological estimate itself changes neither the source nor its preparation. Likewise, it provides no physical tensor factorization across a spatial cut and does not reset an inherited region to an independent block. [[inherited-planar-vacuum-and-the-regional-time-law|IR]] identifies the harmonic regional memory that such a marked return must preserve.

[[centered-compact-chronology-and-integrable-source-return|Centering the comparison map in the actual vacuum]] now strengthens HC7 to an integrable error: both semigroups in Duhamel's formula decay on their vacuum complements. That theorem also verifies the weighted-character extension and retains its source-vector comparison requirements. HC7's uncentered bound itself is still not integrable.

Time in these formulas is scaled time: physical duration is \(t/\sqrt{\kappa g}\). The confinement window, fixed Hermite degree and prescribed physical carrier remain part of every bound.

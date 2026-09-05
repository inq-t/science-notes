# Spatial Elimination and Self-Return

Integrating hidden temporal columns retains their mediated influence among the columns left behind. A hidden excursion can return to the very column being updated, so the induced response has a diagonal even though a conditional interdependence matrix does not. Correcting for this self-return preserves a subcritical comparison bound; it cannot make a spectrally supercritical bound subcritical merely by algebraic elimination. A sharper calculation of the actual marginal law can do better.

**Status: [EXACT FINITE-LAW COMPARISON] under the compact conditional-law hypotheses below; [EXACT MATRIX IDENTITIES] for the elimination criterion; [OPEN] for a continuum-improving spatial Wilson blocking.**

## Retain coordinates of the actual law

Use a finite set of compact metric column spaces as in [[temporal-column-response/inq|Temporal Column Response]], with continuous positive conditional densities. Let \(C\ge0\), \(C_{ii}=0\), majorize the single-column Wasserstein interdependence coefficients in their declared path metrics. Partition the coordinates into retained \(R\) and hidden \(H\), assume \(\rho(C_{HH})<1\), and define
\[
G_H=(I-C_{HH})^{-1},\qquad
E=C_{RR}+C_{RH}G_HC_{HR},\qquad d_i=E_{ii}.
\tag{SE1}
\]
The expansion \(G_H=\sum_{n\ge0}C_{HH}^n\) retains arbitrarily many internal hidden interactions. The matrix \(E\) counts their returns to the retained coordinates. It is not yet a conditional interdependence matrix.

Let \(\mu_R\) be the actual marginal, with all induced interactions included. For each \(i\) with \(d_i<1\), its single-column conditional influences obey
\[
\boxed{
C^{\mathrm{actual},R}_{ij}\le\bar C_{ij}
:=\frac{E_{ij}}{1-d_i}\quad(i\ne j),\qquad
\bar C_{ii}=0.}
\tag{SE2}
\]
To prove this, change only exterior retained coordinate \(j\), keeping every other coordinate in \(R\setminus\{i\}\) fixed. Apply [[library/comparison-theorems-for-gibbs-measures/inq|the finite Dobrushin comparison theorem]] to the joint conditional block \(I_i=\{i\}\cup H\). Its perturbation vector is bounded by \(C_{I_i j}\) times the input distance. Eliminating the hidden rows of \((I-C_{I_iI_i})^{-1}C_{I_i j}\) gives exactly \(E_{ij}/(1-d_i)\) in row \(i\).

The assumptions \(\rho(C_{HH})<1,\ d_i<1\) ensure \(\rho(C_{I_iI_i})<1\); this also follows from the positive-vector argument below. Finite compact metric diameters make the comparison remainder vanish. No infinite-horizon path metric is used. Formula (SE2) is a deduction from the comparison theorem, not a displayed elimination formula quoted from its source.

Equivalently, coupled conditional distances satisfy
\[
u_H\le C_{HH}u_H+C_{Hi}u_i+C_{Hj}a_j,\qquad
u_i\le C_{iH}u_H+C_{ij}a_j.
\]
Substitution yields \(u_i\le d_i u_i+E_{ij}a_j\), explaining the denominator.

## Elimination preserves the certified basin

If \(C\mathbf1\le q\mathbf1\), \(q<1\), then \(G_HC_{HR}\mathbf1\le\mathbf1\): the hidden affine map sends \(\mathbf1\) below itself. Therefore \(E\mathbf1\le q\mathbf1\), and
\[
\sum_{j\ne i}\bar C_{ij}
\le\frac{q-d_i}{1-d_i}\le q.
\tag{SE3}
\]
Thus coordinate deletion preserves the horizon- and volume-uniform bound from the column theorem. It does not require an extensive density comparison. This supplies a static retained-law certificate; obtaining a gradient bound still needs the actual retained metric and conditional form estimates.

More generally, under \(\rho(C_{HH})<1\),
\[
\boxed{
\rho(C)<1
\iff \rho(E)<1
\iff \big[d_i<1\ \forall i,\ \rho(\bar C)<1\big].}
\tag{SE4}
\]
For a finite nonnegative matrix \(M\), \(\rho(M)<1\) is equivalent to the existence of \(v>0\) with \(Mv<v\). Block elimination in \((I-C)v>0\) proves the first equivalence. Conversely solve
\[
v_R=(I-E)^{-1}(\mathbf1_R+C_{RH}G_H\mathbf1_H),\qquad
v_H=G_H(\mathbf1_H+C_{HR}v_R);
\]
then \((I-C)v=\mathbf1\). For the second equivalence use
\[
I-E=\operatorname{diag}(1-d_i)(I-\bar C)
\tag{SE5}
\]
and the same positive-vector criterion. No irreducibility is needed.

When subcritical, the full retained response is
\[
[(I-C)^{-1}]_{RR}
=(I-E)^{-1}
=(I-\bar C)^{-1}\operatorname{diag}(1-d_i)^{-1}.
\tag{SE6}
\]
Consequently recycling this same majorant cannot escape its spectral contraction threshold. An unweighted row sum above one is not spectral supercriticality; weighted estimates may still improve it. Nor does (SE4) prohibit an independently sharper analysis of the exact marginal.

## A diagonal that cannot simply be erased

For Ising spins \(h,s_1,s_2\in\{-1,1\}\), let
\[
\mu\propto e^{Jh(s_1+s_2)},\qquad t=\tanh J,\qquad J>0.
\tag{SE7}
\]
In the discrete metric the exact full conditional coefficients are \(C_{s_i h}=t\) and \(C_{h s_i}=t/(1+t^2)\). Eliminate \(h\). Every entry of \(E\) equals \(t^2/(1+t^2)\), whereas the exact off-diagonal retained coefficient is \(t^2\). Erasing the diagonal of \(E\) underestimates the true influence. Dividing by \(1-d_i\) gives exactly \(t^2\).

## Actual marginalization can improve what the majorant misses

Now use three leaves:
\[
\mu\propto e^{Jh(s_1+s_2+s_3)}.
\tag{SE8}
\]
Every spoke coefficient of the exact full interdependence matrix is \(t\), so \(\rho(C)=\sqrt3\,t\). Elimination by the same comparison gives
\[
E=t^2\mathbf1\mathbf1^\top,\qquad
\rho(\bar C)=\frac{2t^2}{1-t^2}.
\]
But direct summation over \(h\) gives
\[
\mu_R(s)\propto\cosh[J(s_1+s_2+s_3)],\qquad
\mathbb E[s_i\mid s_j,s_k]=t\tanh[J(s_j+s_k)].
\]
Hence every exact retained off-diagonal coefficient is \(t^2/(1+t^2)\), and
\[
\rho(C^{\mathrm{actual},R})=\frac{2t^2}{1+t^2}<1.
\tag{SE9}
\]
At \(J=\log3\), \(t=4/5\), the full comparison is supercritical but the actual retained radius is \(32/41\). The valid lesson is to recompute the joint conditional response after elimination, not to delete its self-return terms. This finite example demonstrates improvement of a sufficient mixing certificate, not a thermodynamic phase transition or Yang--Mills gap.

## The actual whole-column marginal

For the open-time, temporally gauge-fixed Wilson history law used in [[strong-coupling-gap-and-continuum-crossover/wilson-temporal-column-coercivity|the column construction]], choose a fixed spatial orientation \(i\) and the spatial checkerboard \(\sum_{j\ne i}x_j\) even, where this sum includes only spatial coordinates. Select the complete temporal columns based on those spatial links. No spatial plaquette contains two selected columns. Temporal plaquettes still give bonds between successive times within each selected column.

With free or conditionally factorized temporal-end weights, fixing all retained histories \(R\) therefore makes the selected columns independent **as whole chains**. Their conditional partition functions are
\[
Z_e[R]=\int b_e^-(u_0;R)b_e^+(u_N;R)
\prod_{t=0}^{N-1}k_t(u_t,u_{t+1})
\exp\!\left[\sum_{t=0}^{N}a_{e,t}(R)\cdot u_t\right]
\prod_{t=0}^N d\sigma(u_t).
\tag{SE10}
\]
The field \(a_{e,t}\) is the weighted spatial staple sum at that time; \(k_t\) contains the actual temporal kinetic coupling. Constants independent of the retained histories may be placed in the overall normalization. The exact retained density has the form
\[
\mu_R(dR)\propto w_R(R)\prod_{e\in H}Z_e[R]\,dR,
\tag{SE11}
\]
where \(w_R\) includes every retained temporal bond, retained-only spatial plaquette and retained end factor. A nonfactorizing endpoint preparation changes (SE10)--(SE11) and cannot be silently replaced by this law.

For each finite slab this is finite-range in **space** at one elimination layer: with local or free end factors, \(Z_e\) sees one column's spatial staple neighborhood. It is generally nonlocal in **time**. With endpoints held fixed and the linear fields varied independently,
\[
\frac{\partial\log Z_e}{\partial a_{e,t}}=\mathbb E[u_t\mid R],
\qquad
\frac{\partial^2\log Z_e}
{\partial a_{e,t}^\alpha\partial a_{e,s}^\beta}
=\operatorname{Cov}(u_t^\alpha,u_s^\beta\mid R).
\tag{SE12}
\]
Additional chain-rule terms arise when differentiating their actual nonlinear dependence on \(R\). Thus the generated interaction is a whole-history response functional, not the sum of its one-time values. [[rg-covariance-residue/su2-staple-elimination-and-response|The one-link Bessel factor]] does not evaluate an interacting temporal chain.

This selection is independent of time and hence respects temporal reflection geometrically. If the original prepared law is reflection positive, the retained readout commutes with that reflection, and its positive-half observables pull back to the original positive-half algebra, reflection positivity is inherited by direct pullback of the defining quadratic form. This is not a proof of an autonomous nearest-time effective action or of a new one-step transfer logarithm.

## What spatial blocking still has to do

The theorem covers coordinate deletion with inherited metrics. A nonlinear block holonomy or average is a different readout: its posterior fiber law and metric must be constructed. [[rg-covariance-residue/wilson-path-product-fibers|Exact path-product fibers]] and [[rg-covariance-residue/normalized-gauge-kernels-and-markov-residues|normalized probabilistic readouts]] supply particular maps, not their required new influence constants.

Even exact marginal mixing is not a proof about the original dynamics. The hidden sector and its return coupling must remain controlled; [[coarse-response-memory/inq|coarse response memory]] gives the dynamical counterpart. In growing systems, merely having an invertible \(I-C_{HH}\) in every finite volume is insufficient: the relevant weighted resolvent and self-return margins need uniform estimates.

For the current Wilson trajectory, a useful next step must therefore exploit structure of the *actual* eliminated law beyond repeated application of (SE1). The star calculation supplies a concrete reason to pursue joint conditional estimates rather than abandon spatial blocking when a single-column majorant fails.

[[temporal-column-response/receipts/spatial_elimination_receipt.py|The finite receipt]] enumerates both Ising laws and checks the matrix identities, induced denominator, subcritical row preservation and exact-marginal improvement.

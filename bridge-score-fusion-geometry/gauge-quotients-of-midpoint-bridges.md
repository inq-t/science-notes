# Gauge Quotients of Midpoint Bridges

Restricting midpoint observables to gauge invariants is not the same as forgetting the gauge frame independently at both endpoints. Exact one-step lumpability constructs a physical quotient process, but its two-ended predictor can contain strictly less information than the raw predictor restricted to invariant midpoint functions. Positive upper envelopes descend by order; exact diagonalization need not.

**Status: [EXACT] for the stated Markov quotient and finite examples; [CONDITIONAL] for an application to a supplied physical gauge path law.** [[two-boundary-multiplication-and-predictive-tails|The multiplication theorem]] owns the raw midpoint predictor; [[bridge-data-augmentation-solder/relative-boundary-leakage|relative boundary leakage]] owns the general cost of removing endpoint information.

## Quotient dynamics and quotient prediction

Let a compact group act measurably on a standard Borel probability space \((X,\nu)\), preserving \(\nu\). Assume a standard Borel orbit quotient \(q:X\to\bar X\) and that the reversible transition \(P\) maps invariant functions into invariant functions. Define the isometric pullback \(J_0:L^2(\bar\nu)\to L^2(\nu)\), where \(\bar\nu=q_*\nu\).

The restricted operator \(\bar P=J_0^*PJ_0\) gives the exact Markov quotient. Invariance is the lumpability hypothesis; it is stronger than merely defining a compressed one-step operator.

For the stationary raw triple \((X_-,Y,X_+)\), let \(K\) predict midpoint functions from raw endpoints. Let \(J_\partial\) pull functions of the pair \((q(X_-),q(X_+))\) back to the raw endpoint carrier, in the actual pair measure. Then
\[
\boxed{\bar K=J_\partial^*KJ_0,\qquad
\bar S=\bar K^*\bar K
=J_0^*K^*R_\partial KJ_0
\le J_0^*SJ_0,}
\tag{GQ1}
\]
where \(R_\partial=J_\partial J_\partial^*\) is conditional expectation onto the two independent endpoint orbits and \(S=K^*K\).

The difference is exactly
\[
J_0^*SJ_0-\bar S
=\bigl[(I-R_\partial)KJ_0\bigr]^*
\bigl[(I-R_\partial)KJ_0\bigr].
\tag{GQ2}
\]
Equality requires an additional two-ended sufficiency condition. Diagonal equivariance under one common group action on all three slices is not that condition. The quotient of the entire pair by a common gauge frame can retain relative information that the pair of separate quotients forgets.

## Exact dynamics does not imply exact bridge retention

Take \(X=S_3\) with uniform law, quotient by conjugacy class, and the genuine continuous semigroup
\[
P_t=\alpha I+(1-\alpha)\Pi,\qquad \alpha=e^{-t},
\]
where \(\Pi\) averages over all six group elements. Let \(C\) be the three transpositions and \(f=1_C-\tfrac12\). At \(\alpha=\tfrac12\),
\[
Kf(x,z)=
\begin{cases}
4/9,&x=z\in C,\\
1/3,&x\ne z,\ x,z\in C.
\end{cases}
\tag{GQ3}
\]
The two endpoint conjugacy classes are identical in both cases. The raw predictor is therefore not measurable in the separately quotiented endpoints, and (GQ2) is nonzero on this invariant observable.

The arithmetic uses the raw transition entries \(7/12\) on the diagonal and \(1/12\) elsewhere. Identical transposition endpoints give posterior weights \(51:3\) between \(C\) and its complement; distinct transpositions give \(15:3\). It is an exact information-loss example, not a gauge anomaly.

## Quotient prediction can mix different transfer eigenvalues

A second \(S_3\) process takes \(L=I-T\), where \(T\) averages left translations by the three transpositions, and \(P_t=e^{-tL}\). The sign and standard irreducible sectors have eigenvalues \(2\) and \(1\) for \(L\). On the conjugacy classes \(E,T,R\), the stationary weights are \(\pi=(1,3,2)/6\). At \(t=\log2\), the quotient density kernels relative to \(\pi\) are
\[
p_t=\frac14
\begin{pmatrix}13&3&1\\3&5&3\\1&3&7\end{pmatrix},\qquad
p_{2t}=\frac1{16}
\begin{pmatrix}33&15&9\\15&17&15\\9&15&21\end{pmatrix}.
\tag{GQ4}
\]
The characters \(\chi_s=(1,-1,1)\), \(\chi_v=(2,0,-1)\) are orthonormal in \(L^2(\pi)\). Applying the weighted insertion formula yields
\[
\boxed{\langle\chi_s,\bar S\chi_v\rangle_\pi
=\frac7{99}-\frac4{63}=\frac5{693}\ne0.}
\tag{GQ5}
\]
Thus \(\bar S\) does not commute with the quotient generator or its separating spectral cutoff, although the process is reversible, positive and exactly lumpable. The matrices in (GQ4) are densities, not row-stochastic matrices until their columns are multiplied by \(\pi\).

## The useful comparison still descends

Suppose \(L\ge0\) commutes with the gauge action and an actual raw bridge satisfies \(S\le e^{-bL}\). Then the invariant subspace reduces \(L\), and (GQ1) proves
\[
\boxed{\bar S\le e^{-b\bar L},\qquad \bar L=L|_{\mathrm{GI}}.}
\tag{GQ6}
\]
It follows that \(\|\bar KQ_\Lambda\|^2\le e^{-b\Lambda}\) for a spectral tail \(Q_\Lambda\) of \(\bar L\). No commutation between \(\bar S\) and \(Q_\Lambda\) is required.

For a product Haar heat law on a finite gauge graph, [[volume-uniform-fusion-envelopes|the unit-prefactor envelope]] applies with \(L=\sum_eL_e\). Under the full-vertex, independent-link hypotheses of [[contemporary-puzzles/yang-mills-mass-gap/gauge-descent-flux-fisher-coercivity|the existing girth--Casimir theorem]],
\[
\bar L\ge g(\Gamma)c_{\min}Q_0,\qquad
I-\bar S\ge\bigl(1-e^{-b\,g(\Gamma)c_{\min}}\bigr)Q_0.
\tag{GQ7}
\]
Here \(g(\Gamma)\) is actual graph girth and \(c_{\min}\) uses the declared group and metric. A fully gauged tree has only the constant carrier. Matter, charges, fixed links, sector restrictions or constrained holonomy can invalidate the quoted support theorem.

This is an operator-order consequence for the specified quotient law. It neither gives a four-dimensional interacting vacuum nor identifies an arbitrary gauge-averaged joint law with a physically reconstructed one. The [[compact-heat-bridge-fusion-tail|one-group character restriction]] likewise retains raw endpoints; passing each endpoint separately to its conjugacy class is a further quotient, not the same calibration.

## The boundary cannot be chosen just to improve the bound

In this exact Markov quotient, the endpoint pair still contains each separate physical endpoint. The tower property gives
\[
\mathbb E[f(q(Y))\mid q(X_+)]=\bar P f,
\qquad
\boxed{\bar P^*\bar P\le\bar K^*\bar K=\bar S.}
\tag{GQ8}
\]
Thus a bound on \(\bar S\) controls the same quotient transfer, provided that transfer has independently been identified with the physical one. Reversibility changes the left side to \(\bar P^2\); the quotient's one-step lumpability and physical identification are essential.

An arbitrary coarse readout need not retain this comparison. Forget both endpoints while keeping a nontrivial centered midpoint carrier: its predictor is zero and its residual is the identity, irrespective of the original dynamics, including gapless dynamics. That manufactured unit response proves nothing about physical mass because the readout no longer contains a physical one-boundary predictor. [[bridge-data-augmentation-solder/relative-boundary-leakage|Relative boundary leakage]] measures the omitted information when a legitimate comparison is available.

This is the observation-context counterpart of [[vacuum-aligned-innovation-completion/heat-envelopes-and-the-vacuum-vector|the vacuum-vector obstruction]]. The relevant invariant belongs to a specified law, state and observation maps. It survives compatible changes of presentation; changing the accessible algebra can change the response itself.

[[receipts/volume_uniform_envelope_receipt.py|The finite receipt]] checks both \(S_3\) examples, the quotient isometries, the exact loss square, one-boundary domination and the failure of commutation.

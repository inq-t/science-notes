# The Sewn Transfer Clock and the Rotor Limit

The sewn group law has a consistent interpretation as two successive steps of a stationary path. Its transfer clock is the logarithm of the one-step convolution, while the conditional-update clock acts on a different, two-context carrier. Their continuum limits share a Casimir normalization but are not the same dynamics. In the transfer interpretation, a normalized short-interval difference is a path fluctuation; preserving it as an independent finite-rate state is not an additional Yang–Mills requirement.

**Status: exact transfer and refinement statements for the supplied anchored \(SU(2)\) family; conditional interpretation as slices of a path.** This constructs a compact-group rotor limit. It supplies neither a spatial gauge field nor a four-dimensional continuum theory. The two-context obstruction remains true for its stated conditional-update law.

## One state permits two different processing questions

Use \(B_k=C_{p_k}\), \(q_k=p_k*p_k\), and the multipliers \(b_{k,n}\) from [[sewn-overlap-refinement|the complete character calculation]]. Declare a stationary chain with Haar one-slice law and one-step transition

\[
\Pr(X_{j+1}\in dy\mid X_j=x)=p_k(x^{-1}y)\,dy.
\tag{TR1}
\]

The joint law of \((X_0,X_2)\) is exactly \(q_k(x^{-1}y)dxdy\). Centrality and inversion symmetry identify it with the previously sewn density \(q_k(xy^{-1})\). Thus the same two-context law is realized as endpoints separated by two steps. The Markov path completion and the choice of which index is duration are explicit additional structure.

The transfer operator acts on \(L^2(G,dg)\). In contrast,
\(L_k=2-P_x-P_y\) acts on \(L^2(q_k(xy^{-1})dxdy)\) and repeatedly replaces one endpoint conditional on the other. This is a continuous-time two-block Gibbs update, with total update rate two. [[library/covariance-structure-of-the-gibbs-sampler-with-applications-to-the-comparisons-of-estimators-and-augmentation-schemes/inq|Liu, Wong and Kong]] own the conditional-expectation and maximal-correlation precedent. Drawing a fresh endpoint and advancing along the chain are different operations.

The [[two-slice-innovation-geometry/past-future-angle-and-the-transfer-gap|past–future transfer theorem]] already distinguishes the full history shift, one-slice transfer and reconstructed clock. Neither a one-time density nor a two-variable law, without that path and duration structure, selects which operation is physical time.

For these endpoints, maximal correlation is \(a_k=\|B_k^2\|_0\), and the continuous conditional-update gap is \(1-a_k\). A complete sequential conditional sweep instead has the squared-correlation contraction \(a_k^2\) on its collapsed readout. The square already present in \(B_k^2\) comes from the two path steps. These three uses of composition should not be conflated.

## The finite transfer has an exact nullspace

Let \(\Pi_k\) project onto Peter–Weyl degrees \(0\le n\le k\). The anchored kernel is a character polynomial, so

\[
1=b_{k,0}>b_{k,1}>\cdots>b_{k,k}>0,
\qquad B_k(I-\Pi_k)=0.
\tag{TR2}
\]

Pointwise strict positivity of \(p_k\) does not make its convolution injective. Consequently \(-k\log B_k\) is not a densely defined self-adjoint operator on the entire \(L^2(G)\): it would assign infinite energy to the nonzero subspace \((I-\Pi_k)L^2(G)\). Its finite supported clock is well defined on \(\Pi_kL^2(G)\):

\[
H_k^{\rm tr}\Pi_n=-k\log(b_{k,n})\Pi_n,
\qquad 0\le n\le k.
\tag{TR3}
\]

An endpoint reflection form \(\langle f,B_kf\rangle\) removes this nullspace by its Hilbert quotient. Such a quotient must be stated; it does not automatically preserve every time-zero multiplication operator. The increasing supported carriers suffice for the following spectral limit. Integer powers \(B_k^j\) are actual Markov transfers on the full slice space. Arbitrary fractional powers need not be pointwise Markov; no infinite-divisibility assertion is needed.

This differs from the injective Wilson transfer in [[strong-coupling-gap-and-continuum-crossover/finite-spacing-transfer-and-bounded-flux-solder|the finite-spacing Wilson analysis]]. The latter owns the temporal-continuum relation to the electric Hamiltonian; its strict-positivity hypotheses cannot be imported into this finite-rank kernel.

## The whole supported spectrum converges to the rotor

Assign one comparison step the duration \(\delta_k=1/k\). This fixes dimensionless clock units; a physical conversion remains separate. With \(c_n=n(n+2)/4\), the established expansion is

\[
b_{k,n}=1-\frac{6c_n}{k}+O_n(k^{-2}),
\qquad -k\log b_{k,n}\longrightarrow6c_n.
\tag{TR4}
\]

Therefore the limit is \(H^{\rm tr}=6D_Q\), where \(D_Q=-\Delta_Q\) on the full Peter–Weyl carrier. Its centered gap is \(6c_1=9/2\). There is full operator convergence, not just fixed-mode convergence:

\[
\left\|\Pi_k(z+H_k^{\rm tr})^{-1}\Pi_k
-(z+6D_Q)^{-1}\right\|\longrightarrow0,
\quad z>0,
\tag{TR5}
\]
\[
\left\|B_k^{\lfloor kt\rfloor}-e^{-6tD_Q}\right\|
\longrightarrow0,\qquad t>0.
\tag{TR6}
\]

For sufficiently large \(k\), the integer exponent in (TR6) is positive. To prove both limits, split at a fixed degree \(M\). Equation (TR4) controls the finite head. The strict ordering in (TR2) bounds the remaining supported tail by its degree-\(M+1\) resolvent or transfer multiplier. The unsupported transfer tail is zero, while the limiting tail tends to zero as \(M\to\infty\). Taking \(k\to\infty\) first proves the assertions, uniformly for \(t\ge\tau>0\). Unlike the singular full two-context limit, (TR5) returns a genuine resolvent on the complete limiting slice carrier.

The same ratio estimate used for the conditional clock gives a uniform supported transfer edge:

\[
\operatorname{gap}H_k^{\rm tr}
\ge k\log\left(1+\frac9{2k}\right)
\ge\log(11/2)>0.
\tag{TR7}
\]

The last inequality follows because \(s\log(1+a/s)\) increases for \(s>0\). These are rotor units, not a regulator-uniform physical mass estimate for a spatial theory.

## Why the factor two does not identify the clocks

For a fixed nontrivial degree, compare the three rates:

\[
\begin{array}{c|c|c}
\text{operation}&\text{rate}&k\to\infty\\\hline
\text{one-step transfer}&-k\log b_{k,n}&6c_n\\
\text{collective conditional update}&k(1-b_{k,n}^2)&12c_n\\
\text{relative conditional update}&k(1+b_{k,n}^2)&+\infty.
\end{array}
\tag{TR8}
\]

The two-step transfer is \(B_k^2\). Dividing \(-\log B_k^2\) by its actual elapsed duration \(2/k\) again gives \(H_k^{\rm tr}\), not twice that clock. The collective conditional rate has the factor two because its prescribed update normalization is \(k\). The small-defect relation \(1-b^2\sim-2\log b\) explains their common Casimir dependence; it does not identify the operations at finite refinement or their full carriers.

For a slice function \(f\), the two-step path law gives exactly

\[
\mathbb E|f(X_2)-f(X_0)|^2
=2\langle f,(I-B_k^2)f\rangle.
\tag{TR9}
\]

For a fixed smooth \(f\), dividing by \(2/k\) tends to
\(2\langle f,6D_Qf\rangle\). Its normalized difference is a short-duration increment. No implication makes the conditional-update rate of that history observable a separate eigenvalue of the slice Hamiltonian. In particular, no lattice-doubler claim follows without an actual physical dispersion relation and reconstruction map.

The [[resolved-relative-boundary-and-two-clock-limits|resolved-boundary theorem]] is therefore retained with its declared scope. It obstructs a full two-context response under that update law. It does not obstruct the transfer realization (TR1)–(TR6), and it does not impose a universal requirement that every normalized regulator-scale history variable remain a finite-energy physical observable.

Reading the two variables instead as spatial links would require a spatial graph, gauge action, plaquette interactions and a specified running coupling. None is supplied by merely relabeling (TR1). The electric/magnetic coefficient relation of a lattice gauge Hamiltonian cannot be inferred from the two conditional rates alone.

## The next return must carry an interaction and a spatial limit

This positive control returns compact-group quantum mechanics. With conjugation as the gauge action, its character subspace retains the first Casimir mode. Independent endpoint gauge transformations on a lone open edge would leave only constants, so the phrase “one-link physical gap” requires its gauge carrier to be declared too.

[[interacting-comparison-refinement|Interacting comparison refinement]] tests how explicit elementary kernels can compose in a limit without demanding closure of the same finite-width ansatz. The [[coarse-response-memory/correlated-interface-tangent|two-plaquette tangent]] remains a finite gauge-invariant interaction benchmark, rather than a continuum theorem. Its full angular response must be recovered when that spatial member is claimed.

[[receipts/sewn_transfer_clock_receipt.py|The transfer-clock receipt]] checks the supported/null split exactly and encloses selected logarithmic rates by rational series. Its convergence values are diagnostics; (TR4)–(TR7) supply the complete-tail arguments.

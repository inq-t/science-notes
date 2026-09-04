# Regular Gauge Averages and the Selection Obstruction

Several open gauge transports can be averaged into one transport on an explicit regular domain. A smooth anchored continuation extends this readout to all configurations, and a common-pivot architecture supplies an exact product-Haar conditional carrier. But no equal-weight, permutation-symmetric, endpoint-equivariant group-valued mean exists on every input: the global continuation keeps a distinguished transport. This is an exact selection-map distinction, not evidence for ontological randomness, chirality, or a physical mass gap.

## What the map acts on

Let \(W_i\in SU(r)\), \(r\ge2\), represent open parallel transports with the same source and target. These might be path products of fine lattice links. Independent endpoint transformations act by

$$
W_i\longmapsto g_sW_ig_t^{-1}.
\tag{GA1}
$$

The proposed coarse variable is another transport with this same transformation law. The use of \(SU(r)\) supplies a finite matrix example; it neither selects this group from a deeper theory nor covers every compact simple group.

Closed holonomies have only conjugation covariance automatically. The independent-left-action obstruction below must not be applied to them unchanged.

## A definite output cannot always preserve the input symmetries

Suppose \(h\in G\) has finite order \(m>1\). There is no map \(M:G^m\to G\) that is both permutation symmetric and left equivariant on all inputs.

Indeed, for \(\mathbf W=(1,h,\ldots,h^{m-1})\), multiplication by \(h\) cyclically permutes the entries. Therefore

$$
hM(\mathbf W)=M(h\mathbf W)=M(\mathbf W),
\tag{GA2}
$$

which contradicts cancellation in the group. No continuity assumption is used.

For \(SU(r)\), already an equal-weight pair suffices:

$$
h=\operatorname{diag}(-1,-1,1,\ldots,1),\qquad
\mathbf W=(I,h).
\tag{GA3}
$$

Their arithmetic matrix mean has two zero eigenvalues. The obstruction is not a failure to find a clever enough normalization. The symmetry of the input demands a fixed point of a nontrivial left translation, and the requested output space has none.

A deterministic construction can instead restrict its domain, distinguish an input, relax equivariance, or return a different object. An orbit, a set of possible transports, or a probability measure is a different codomain; none is automatically a selected transport. A probability-valued return also requires its own weight rule.

This is the precise connection to [[basic-concepts/torsors/inq|torsors]]: relative data need not choose a preferred point. It is not a theorem that every physical observation is this averaging operation. As in [[higgs-reduction-as-local-shadow/symmetry-without-a-random-trigger|the invariant-state obstruction]], symmetry alone cannot supply a unique asymmetric return when equivariance is required and the output has no compatible fixed point.

## An explicit regular-domain construction

Choose positive weights \(w_i\) summing to one, and distinguish a supplied transport \(W_0\). Define

$$
Z=\sum_iw_iW_i,\qquad C=W_0^*Z.
\tag{GA4}
$$

On the open domain

$$
\|C-I\|_{\rm op}<\varepsilon<1,
\tag{GA5}
$$

the matrix \(Z\) is invertible with \(\sigma_{\min}(Z)>1-\varepsilon\), and the principal matrix logarithm of \(C\) exists. Put

$$
\begin{aligned}
P&=Z(Z^*Z)^{-1/2},\\
\theta&=\operatorname{Im}\operatorname{tr}\operatorname{Log}C,\\
\boxed{\mathcal Q(W)=e^{-i\theta/r}P.}
\end{aligned}
\tag{GA6}
$$

The first line is the nonsingular unitary polar factor. [[library/computing-the-polar-decomposition-with-applications/inq|Higham's polar-decomposition work]] provides matrix-analysis background; the gauge and selection claims here are established directly.

Since \(\det W_0=1\),
\(\det P=\det C/|\det C|=e^{i\theta}\), so \(\mathcal Q\in SU(r)\).
All operations are smooth on (GA5). Under (GA1),

$$
C\longmapsto g_tCg_t^{-1},\qquad
\theta\longmapsto\theta,\qquad
\mathcal Q\longmapsto g_s\mathcal Qg_t^{-1}.
\tag{GA7}
$$

Thus the anchor supplies a covariant chart, not an absolute external frame. Its role and the domain restriction cannot be erased from the input signature. A determinant root without a branch choice has an \(r\)-fold central ambiguity; the logarithm fixes a lift on this domain. Do not claim unrestricted permutation symmetry for this anchored construction.

For \(SU(2)\), real weighted sums retain quaternion form. Whenever \(Z\ne0\), the polar factor is already special unitary. The determinant correction is unnecessary there, but the singular-input obstruction remains.

## The derivative and its conditioning

Keep the weights fixed when differentiating. At coincident inputs \(W_i=W\), let \(\delta W_i=WX_i\) with \(X_i\in\mathfrak{su}(r)\). Then

$$
\delta Z=W\overline X,\qquad
\overline X=\sum_iw_iX_i,\qquad
\delta(Z^*Z)=0,\qquad\delta\theta=0,
$$

and hence

$$
\boxed{D\mathcal Q(\delta W_i)=W\sum_iw_iX_i.}
\tag{GA8}
$$

For actual path products at the identity connection, each \(X_i\) is the oriented fine-link sum along that path. The derivative is therefore a weighted path-incidence operator.

There is also a local derivative bound. Write \(Z=PH\), \(H>0\), \(E=\delta Z\), and \(K=P^*\delta P\). Differentiating and taking the anti-Hermitian part gives

$$
HK+KH=P^*E-E^*P.
\tag{GA9}
$$

In an eigenbasis of \(H\), every denominator is \(h_i+h_j\ge2\sigma_{\min}(Z)\). With Frobenius norm,

$$
\|\delta P\|_F=\|K\|_F
\le\frac{\|E\|_F}{\sigma_{\min}(Z)}.
\tag{GA10}
$$

On a fixed smooth determinant branch,
\(\mathcal Q^*\delta\mathcal Q=K-(\operatorname{tr}K/r)I\).
Even a moving anchor contributes no trace term because
\(\operatorname{tr}(W_0^*\delta W_0)=0\).
The correction is thus the Frobenius-orthogonal projection onto the traceless part. Consequently,

$$
\|D\mathcal Q(\delta W)\|_F
\le\frac{\|\sum_iw_i\delta W_i\|_F}{\sigma_{\min}(Z)}
\le\frac{\sum_iw_i\|\delta W_i\|_F}{1-\varepsilon}.
\tag{GA11}
$$

This bounds differentiation of the finite matrix readout. It does not bound the inverse conditional response or an RG source envelope.

## A global continuation that keeps the anchor

The regular-domain restriction can be removed without deleting configurations. Choose fixed \(0<r_0<r_1<1\) and a smooth function \(\chi:[0,\infty)\to[0,1]\), equal to one on \([0,r_0^2]\) and zero on \([r_1^2,\infty)\). For \(D=C-I\), put

$$
C_{\rm safe}=I+\chi(\|D\|_F^2)D,\qquad
\mathcal Q_{\rm anc}
=W_0\,\operatorname{polar}(C_{\rm safe})
\exp\!\left[-\frac{i}{r}
\operatorname{Im}\operatorname{tr}\operatorname{Log}C_{\rm safe}\right].
\tag{GA12}
$$

One explicit choice uses \(\eta(u)=e^{-1/u}\) for \(u>0\) and zero otherwise:
\(\chi(s)=\eta(r_1^2-s)/[\eta(r_1^2-s)+\eta(s-r_0^2)]\).
The denominator never vanishes.

Everywhere \(\|C_{\rm safe}-I\|_{\rm op}\le r_1<1\). Thus the polar and logarithm operations are globally smooth on this input manifold and
\(\sigma_{\min}(C_{\rm safe})\ge1-r_1\). Conjugation covariance of all factors proves endpoint covariance of \(\mathcal Q_{\rm anc}\).

For \(\|D\|_F\le r_0\), this agrees exactly with (GA6). For \(\|D\|_F\ge r_1\), it returns \(W_0\). Its diagonal derivative remains (GA8). The anchor, weights, and cutoff function are supplied scheme choices, not new physical constants or a symmetry-selection theorem.

For
$$
M_\chi=\sup_{s\ge0}\{\chi(s)+2s|\chi'(s)|\}<\infty,
$$
differentiation gives \(\|\delta C_{\rm safe}\|_F\le M_\chi\|\delta D\|_F\). Since \(\|Z\|_{\rm op}\le1\), (GA10) and the traceless projection imply

$$
\|\delta\mathcal Q_{\rm anc}\|_F
\le
\left(1+\frac{M_\chi}{1-r_1}\right)\|\delta W_0\|_F
+\frac{M_\chi}{1-r_1}\sum_iw_i\|\delta W_i\|_F.
\tag{GA13}
$$

This is a global finite readout-conditioning bound. Composing it with paths still introduces their lengths and occurrences; it is not automatically uniform in physical refinement.

## A common pivot recovers exact Haar fibers

Suppose the transports share one final fine link:

$$
W_i=A_i(Y)U_*,\qquad W_0=A_0(Y)U_*,
\tag{GA14}
$$

where all prefixes depend only on the independent nonpivot fine variables \(Y\). Prefixes may overlap within \(Y\). Then
\(C=U_*^*C_0(Y)U_*\), with
\(C_0=A_0^*\sum_iw_iA_i\).
The conjugation-covariant construction (GA12) consequently has the form

$$
V=\mathcal Q_{\rm anc}=K(Y)U_*,\qquad
U_*=K(Y)^*V,\qquad
\mathrm dU_*\,\mathrm dY=\mathrm dV\,\mathrm dY.
\tag{GA15}
$$

This is a smooth global product-Haar chart. Its pivot derivative is an isometry. For several outputs, require distinct pivots and prefixes depending only on the shared nonpivot variables, not on other pivots; a triangular dependence would need a separate invertibility argument.

The finite Wilson conditional density is therefore exactly (WP4) in [[wilson-path-product-fibers|Wilson path-product fibers]], with inverse pivot \(K(Y)^*V\). Smoothness and compactness prove a strictly positive smooth retained density. At fixed \(Y\), a right variation of \(V\) varies only its pivot, so the retained score is still the pivot plaquette derivative (WP8). Hidden derivatives now also differentiate \(K(Y)\). The full inherited metric is not the chart product metric.

This establishes a full finite-law averaged carrier for the common-pivot architecture. It does not establish that a particular spatially adequate family admits that architecture; the geometry and product-chart conditions must hold simultaneously, not in two different examples.

## What remains before this is a useful block

If all \(W_i\) are the same thin path, (GA6) returns that path exactly. Thus endpoint covariance and smooth averaging alone do not defeat [[thin-skeleton-and-block-average-coercivity|the thin-skeleton counterexample]]. Spatial coverage, compatible gauge constraints, and the constrained tangent metric still determine whether the linearization separates ultraviolet fluctuations.

For arbitrary averaged path families, the common-pivot hypothesis need not hold; their conditional measure remains to be constructed. The regular formula (GA6) alone still cannot justify deleting the excluded configurations. The anchored continuation (GA12) includes them but changes the readout there.

[[normalized-gauge-kernels-and-markov-residues|A normalized probability-valued block]] is another full-domain option: it keeps symmetry among equal-weight paths by returning a measure instead of a definite group element. Its exact conditional law needs no pivot chart. Neither option supplies the needed susceptibility.

The useful advance is a finite, differentiable, gauge-covariant candidate together with its exact selection obstruction and an explicit anchored global continuation. A singular undamped average is a failure of that chart, not yet a causal wall; its determinant is not an energy, and its branch ambiguity supplies no mass scale.

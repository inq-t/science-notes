# Index, Not Entropy

The type-I product-edge model bounds a chosen edge state's entropy by half the log Watatani index. Combining that identity with a channel model converts the reproduced cosmological matching-ratio profile into a conditional bound on the cell dimension. Extending the comparison to the sub-4 Jones spectrum requires a separate entropy–index bound for the proposed subfactor wall; the index theorem supplies neither that bound nor a selection of the gravitational coupling.

## The retyping

For the type-I product-edge inclusion with auxiliary tracial expectation constructed in [[spectral-wall-descent/finite-index-area-weld|the finite-index area weld]], the exact receipt-verified identity is

$$
S(\chi)+D(\chi\Vert\tau)=\tfrac12\log\operatorname{Ind}_W(E_\tau)
$$

and therefore $s_*:=S(\chi)\le\tfrac12\log\operatorname{Ind}_W(E_\tau)$, with equality at maximal mixing. Multiplicatively, in this model:

$$
\boxed{\operatorname{Ind}\;\ge\;e^{2s_*},}
$$

an inequality between unit-free invariants. The log base drops out; "nat" was bookkeeping, the index is the object.

## What the direct profile constrains in the channel model

**[CONDITIONAL — channel additivity, unit rate branch, and model-to-wall identification]** On a wall of $n$ identical balanced channels at the reference cut, the horizontal response is $G^{\perp}_{NN}(N_c)=n\nu^2$ and the entropy is $S_c/k_B=n s_*$, so the integrated matching ratio of [[causal-scale-theory/reference-cut-matching-ratio|homogeneous capacity]] reads

$$
\mathfrak R_c=\frac{\nu^2}{s_*}.
$$

On the unit-rate branch $\nu=1$, [[causal-scale-theory/receipts/fit-generalized-background|the reproduced direct profile on fully released 2025 data]] gives

$$
\mathfrak R_c=1.014104,
\qquad
\Delta\chi^2\le1:[0.941572,1.089954],
\qquad
\Delta\chi^2\le3.84:[0.875271,1.165563].
$$

Under the additional channel map $s_*=1/\mathfrak R_c$, monotonic inversion gives

$$
\boxed{
s_*=0.9861\ \text{nat},
\qquad
\Delta\chi^2\le1:[0.9175,1.0621]\ \text{nat},
\qquad
\Delta\chi^2\le3.84:[0.8580,1.1425]\ \text{nat}.}
$$

The likelihood profiles \(\mathfrak R_c\); the entropy numbers are conditional pushforwards through the displayed channel model, not an independent entropy measurement or a posterior distribution.

## The Jones wall

Jones (Invent. Math. **72**, 1 (1983)) proved that the Jones trace index of an inclusion of \(\mathrm{II}_1\) factors takes values

$$
\operatorname{Ind}\in\Bigl\{4\cos^2\!\frac{\pi}{n}:n\ge3\Bigr\}\cup[4,\infty],
$$

with a discrete allowed series below 4 and every value above 4 realized by some inclusion. The corresponding half-log values are $h_n=\tfrac12\log\operatorname{Ind}_n=\log\bigl(2\cos\frac{\pi}{n}\bigr)$. These are transforms of index values; Jones's theorem does not identify them with maximal edge-state entropies. Moreover, categorical dimension squared is the minimal index and equals the Jones trace index only for extremal \(\mathrm{II}_1\) inclusions, as stated in [[library/dualizability-and-index-of-subfactors/inq|Bartels--Douglas--Henriques, Warning 5.11]] and distinguished in [[finite-index-distinction/finite-index-duality-and-the-square-response|the chosen/minimal-index normalization]].

| n | Jones index | Half-log h_n | Reciprocal 1/h_n |
|---|---|---|---|
| 3 | 1 | 0 | infinite |
| 4 | 2 | 0.3466 | 2.885 |
| 5 | 2.618 (golden) | 0.4812 | 2.078 |
| 6 | 3 | 0.5493 | 1.821 |
| 8 | 3.414 | 0.6140 | 1.629 |
| limit | 4 | 0.6931 = ln 2 | 1.4427 |

Suppose a proposed subfactor wall independently satisfies \(s_*\le\tfrac12\log\operatorname{Ind}_J\), where \(\operatorname{Ind}_J\) is its Jones trace index. Together with channel additivity and the unit-rate assumption, every sub-4 value then implies

$$
\mathfrak R_c\ge\frac1{\ln2}=1.4427,
$$

which lies above the reproduced $\Delta\chi^2\le3.84$ upper endpoint $1.165563$. This rules out the sub-4 ladder only conditional on the additional entropy–index bound. [[finite-index-distinction/two-sided-index-capacity-and-the-cosmic-weld|The general log-index capacity theorem]] concerns maximal relative-entropy loss and does not establish that half-log bound.

For the literal type-I product cell, the auxiliary Watatani index is \(d^2\) with integer \(d\); the available values are already \(1,4,9,\ldots\). The inferred entropy excludes \(d\le2\) and permits \(d\ge3\). A maximally mixed qutrit predicts

$$
\mathfrak R_c=\frac1{\ln3}=0.91024.
$$

It lies below the $\Delta\chi^2\le1$ endpoint $0.941572$ but inside the $\Delta\chi^2\le3.84$ interval $[0.875271,1.165563]$: it is mildly disfavored, not excluded at the wider contour. The central value is compatible with a nonmaximally mixed type-I cell of dimension $d\ge3$. If the separate half-log bound is established for a proposed \(\mathrm{II}_1\) wall, the central-profile inequality would instead read

$$
\operatorname{Ind}_J\ge \exp\!\left(\frac{2}{1.014104}\right)\approx7.186>4.
$$

An unrestricted \(\mathrm{II}_1\) inclusion with index \(e^2\) is algebraically admissible, but admissibility supplies no edge state or entropy weld; [[deriving-value-of-g/spectral-index-area-route#The exact cell model|the spectral-index area route]] keeps those data separate.

## Two consequences

**The sub-4 comparison needs an entropy bound.** **[CONDITIONAL]** Under the channel, unit-rate, fit, and an independently established half-log Jones-index bound, the inferred lower bound lies above 4. The literal type-I result is \(d\ge3\), hence \(\operatorname{Ind}_W\ge9\). An extension to other subfactor indices needs its own state and entropy theorem; neither Jones's spectrum nor the full log-index relative-entropy capacity provides it. The comparison supplies no continuity theorem for a physical index or for \(G\).

**The unit candidate still needs selection.** **[OPEN]** In the unit-rate convention, \(\mathfrak R_c=1\) requires \(s_*=1\) nat. A literal finite product cell can realize that entropy with \(d\ge3\), but cannot saturate it at \(\operatorname{Ind}_W=e^2\), since \(d=e\) is not an integer. A different subfactor model would nominate \(e^2\) only after proving the additional equality \(s_*=\tfrac12\log\operatorname{Ind}\). This algebraic nomination is not a fixed-point or state-selection theorem; those remain among the open requirements in [[program-core/claim-and-failure-contract|the claim contract]].

## Assumptions, and how this dies

The product-cell chain requires a physical realization of the edge factor and its state, channel additivity of the BKM response, and the unit-rate branch ($\nu\ne1$ changes the reading to $\nu^2/s_*$). The subfactor comparison additionally requires a half-log entropy bound for that wall and a declared index convention; equality at \(e^2\) further requires saturation. The reproduced background likelihood does not validate any of these maps. A failed entropy–index bound invalidates the Jones-ladder comparison while leaving the finite-cell identity intact; failed channel additivity invalidates the profile-to-entropy conversion. Restricting the admissible inclusions may also exclude \(e^2\): the unrestricted realization of every index in \([4,\infty)\) does not assert realization in a selected irreducible or finite-depth class.

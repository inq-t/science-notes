# Index, Not Entropy

The unit of the wall ledger looked like an arbitrary choice — nats against bits — and the cosmological matching-ratio profile looked like a measurement of an entropy. In the exact type-I product-edge model, the entropy bound can be retyped through the Watatani index; conditional on the channel model and the reproduced direct background profile, the resulting candidate lies above the discrete sub-4 Jones spectrum. This removes one possible rigidity obstruction but neither selects an index nor explains the value or continuity of the gravitational coupling.

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

Jones (Invent. Math. **72**, 1 (1983)) proved the index of a subfactor takes values

$$
\operatorname{Ind}\in\Bigl\{4\cos^2\!\frac{\pi}{n}:n\ge3\Bigr\}\cup[4,\infty],
$$

rigid and quantized below 4, continuous above. The corresponding maximal entropies $s_n=\tfrac12\log\operatorname{Ind}_n=\log\bigl(2\cos\frac{\pi}{n}\bigr)$:

| n | Index | s_n (nats) | Matching ratio 1/s_n |
|---|---|---|---|
| 3 | 1 | 0 | infinite |
| 4 | 2 | 0.3466 | 2.885 |
| 5 | 2.618 (golden) | 0.4812 | 2.078 |
| 6 | 3 | 0.5493 | 1.821 |
| 8 | 3.414 | 0.6140 | 1.629 |
| limit | 4 | 0.6931 = ln 2 | 1.4427 |

Under the channel-additivity and unit-rate assumptions, every rigid sub-4 value predicts

$$
\mathfrak R_c\ge\frac1{\ln2}=1.4427,
$$

which lies above the reproduced $\Delta\chi^2\le3.84$ upper endpoint $1.165563$. The rigid ladder therefore remains outside the wider profile contour. A maximally mixed qutrit instead predicts

$$
\mathfrak R_c=\frac1{\ln3}=0.91024.
$$

It lies below the $\Delta\chi^2\le1$ endpoint $0.941572$ but inside the $\Delta\chi^2\le3.84$ interval $[0.875271,1.165563]$: it is mildly disfavored, not excluded at the wider contour. Remaining candidates include $s_*\approx1$ nat on a nonmaximally mixed type-I cell of dimension $d\ge3$, or a suitable II$_1$-type inclusion satisfying

$$
\operatorname{Ind}\ge e^{2s_*}\approx e^2=7.389>4 .
$$

## Two consequences

**The sub-4 rigidity obstruction is conditionally excluded.** **[CONDITIONAL]** Below index 4 the allowed subfactor indices form a discrete series. Under the channel, unit-rate, fit, and state–geometry-weld hypotheses, the inferred bound lies above 4, where Jones's spectrum permits a continuum of index values. This does not show that the physical index varies continuously, select its value, or explain a measured continuity of $G$; it only says that this candidate is not forced onto the sub-4 discrete ladder. Had the fit landed on one of those ladder values, the same model would instead nominate a discrete index candidate.

**The self-normalizing selection.** **[OPEN]** $s_*=1$ nat is the unique fixed point where the channel carries exactly one unit of the ledger it is written in — $\operatorname{Ind}=e^2$, the index whose half-log is the unit itself. The unit matching law $\mathfrak R_c=1$ thereby acquires a candidate algebraic meaning beyond normalization: the wall is the channel at its own measure. Whether anything *selects* $e^2$ — a variational principle, a maximality property, a fixed point of the descent — is a new open problem, added to the ledger of the several meanings of "one" in [[program-core/claim-and-failure-contract|the claim contract]].

## Assumptions, and how this dies

The chain assumes the exact type-I/tracial identity can be connected to the physical wall, channel additivity of the BKM response, the unit-rate branch ($\nu\ne1$ changes the reading to $\nu^2/s_*$), and saturation only for the *equality* $\operatorname{Ind}=e^2$ (the bound $>4$ needs no saturation). The reproduced input is still only a background likelihood for an effective source family; it does not validate the channel map. Kill conditions: a future direct profile landing at a ladder value would restore a discrete index candidate within this model; a proof that the physical wall inclusion is irreducible with index in a gap region above 4 would kill the specific value $e^2$ while leaving only above-four admissibility; a demonstrated failure of channel additivity retires the whole note to the junk drawer. For possibly reducible inclusions every value in $[4,\infty)$ is realized (Jones 1983), so $e^2$ is admissible; admissibility is not selection, and the finer spectrum of irreducible hyperfinite subfactors is a separate question.

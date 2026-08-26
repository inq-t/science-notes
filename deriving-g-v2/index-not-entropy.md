# Index, Not Entropy

The unit of the wall ledger looked like an arbitrary choice — nats against bits — and the reported matching-ratio fit looked like a measurement of an entropy. Retyped multiplicatively, both statements sharpen: the invariant is the *index* of the wall inclusion, a unit-free positive number, and the fit becomes a lower bound $\operatorname{Ind}\ge e^2>4$. By Jones's rigidity theorem the index spectrum below 4 is a quantized ladder whose entropies never exceed $\ln 2$; the fit therefore excludes the entire rigid series, places the wall above the Jones wall in the continuum regime, and thereby *explains why the gravitational constant is continuous rather than quantized*. Everything below is conditional on the channel reading and on a reported-limited fit, and says so.

## The retyping

For a finite-index inclusion cell, the exact type-I identity (first pass; receipt-verified)

$$
S(\chi)+D(\chi\Vert\tau)=\tfrac12\log\operatorname{Ind}_W(E_\tau)
$$

gives $s_*:=S(\chi)\le\tfrac12\log\operatorname{Ind}$, with equality at maximal mixing. Multiplicatively:

$$
\boxed{\operatorname{Ind}\;\ge\;e^{2s_*},}
$$

an inequality between unit-free invariants. The log base drops out; "nat" was bookkeeping, the index is the object.

## What the fit measures

**[CONDITIONAL — channel additivity, unit rate branch]** On a wall of $n$ identical balanced channels at the reference cut, the horizontal response is $G^{\perp}_{NN}(N_c)=n\nu^2$ and the entropy is $S_c/k_B=n s_*$, so the integrated matching ratio of [[causal-scale-theory/reference-cut-matching-ratio|homogeneous capacity]] reads

$$
\mathfrak R_c=\frac{\nu^2}{s_*}.
$$

On the unit-rate branch $\nu=1$, the reported fit $\mathfrak R_c=1.025$, 68% interval $[0.941,1.088]$ ([[deriving-value-of-g/reported-cosmological-fit|status: reported, limited, not fully reproduced]]) is a *measurement of the entropy per channel*:

$$
s_*\in[0.919,\,1.063]\ \text{nat}.
$$

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

Every rigid value predicts $\mathfrak R_c\ge1.4427$ — the qubit ceiling — and the fit interval $[0.941,1.088]$ excludes them all. The maximally mixed qutrit ($s_*=\ln3$, $\mathfrak R_c=0.910$) is excluded from below. What survives is $s_*\approx1$ nat on a *nonmaximally mixed* cell of dimension $d\ge3$, exactly the region the first pass's $d=e$ analysis left open, or a genuine II$_1$-type inclusion with

$$
\operatorname{Ind}\ge e^{2s_*}\approx e^2=7.389>4 .
$$

## Two consequences

**Continuity of the constant, explained.** **[CONDITIONAL]** Below index 4 the algebra is rigid: a sub-4 wall would force $\mathfrak R_c$ — and through the weld, $G$ at fixed ruler — onto a discrete series. The fit says the cosmos sits on the continuum side, where no rigidity theorem pins the value: the observed *continuity* of Newton's constant is what a wall above the Jones wall looks like. Had the fit landed on 1.44 or 2.08, this programme would be predicting a quantized gravitational constant.

**The self-normalizing selection.** **[OPEN]** $s_*=1$ nat is the unique fixed point where the channel carries exactly one unit of the ledger it is written in — $\operatorname{Ind}=e^2$, the index whose half-log is the unit itself. The unit matching law $\mathfrak R_c=1$ thereby acquires a candidate algebraic meaning beyond normalization: the wall is the channel at its own measure. Whether anything *selects* $e^2$ — a variational principle, a maximality property, a fixed point of the descent — is a new open problem, added to the ledger of the several meanings of "one" in [[program-core/claim-and-failure-contract|the claim contract]].

## Assumptions, and how this dies

The chain assumes channel additivity of the BKM response, the unit rate branch ($\nu\ne1$ changes the reading to $\nu^2/s_*$), saturation only for the *equality* $\operatorname{Ind}=e^2$ (the bound $>4$ needs no saturation), and the reported fit itself, which remains unreproduced. Kill conditions: a reproduced fit landing at a ladder value revives the rigid series and predicts quantized $G$; a proof that the physical wall inclusion is irreducible with index in a gap region above 4 would kill the specific value $e^2$ while leaving the continuum conclusion; a demonstrated failure of channel additivity retires the whole note to the junk drawer. For possibly reducible inclusions every value in $[4,\infty)$ is realized (Jones 1983), so $e^2$ is admissible; the finer spectrum of *irreducible* hyperfinite subfactors is a separate mathematical question this note does not need.

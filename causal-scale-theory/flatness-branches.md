# CST-B2 Present Flatness and Candidate-Crossing Branches

Present flatness turns the CST-B2 response into a branch-valued equation for the distinguished reference date. Here \(\mathfrak R_c\) is the integrated reference ratio defined by [[program-core/ruble-equations|the programme core]], \(\nu>0\) is CST-B2's constant scale-state rate and inverse profile width in logarithmic scale, and every root labels a distinct conditional background rather than another crossing within one history. Calling a selected root a physical crossing additionally requires the member's wall and source realization.

Use

$$
N:=\ln\frac a{a_0},
\qquad
x_c:=-N_c=\ln(1+z_c),
$$

so \(x_c>0\), \(x_c=0\), and \(x_c<0\) denote past, present, and future candidate-crossing references. For declared present abundances, set

$$
D:=1-\Omega_{m0}-\Omega_{r0}>0,
$$

$$
F_\nu(x)
:=\left(\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}\right)
\operatorname{sech}^2(\nu x),
\qquad
T_{\mathfrak R}
:=D\frac{2-\mathfrak R_c}{\mathfrak R_c}.
$$

Under spatially flat \(3+1\)-dimensional GR--FLRW, matter, radiation, the rigid CST-B2 response, and no residual sector, [[causal-scale-theory/theorems/present-flatness-closure|present-flatness closure]] proves the **[CONDITIONAL MEMBER THEOREM]**

$$
\boxed{F_\nu(x_c)=T_{\mathfrak R}},
\qquad
0<\mathfrak R_c<2.
$$

The theorem owns the elimination and its failure boundary. Curvature, interactions, a residual vacuum, an additional component at the reference cut, or a different source-to-horizon conversion changes the equation.

Root choice is therefore member data. If a past late-time candidate crossing is imposed, the conventional branch is the smallest positive root unless a different prior or selection principle is declared. A likelihood must say whether it selects that branch, profiles over all roots, or assigns branch weights.

## Unit-rate sign rule

For \(\nu=1\), [[causal-scale-theory/theorems/unit-rate-crossing-sign|the unit-rate theorem]] proves global uniqueness and

$$
\boxed{
\begin{aligned}
\mathfrak R_c<2D&\Longleftrightarrow x_c>0,\\
\mathfrak R_c=2D&\Longleftrightarrow x_c=0,\\
\mathfrak R_c>2D&\Longleftrightarrow x_c<0.
\end{aligned}}
$$

For the inherited abundances,

$$
2D=1.378621.
$$

This is a theorem about the CST-B2 unit-rate branch, not a general family sign rule and not evidence that \(\mathfrak R_c\) is a universal constant. [[causal-scale-theory/receipts/background.json|The background receipt]] checks representative amplitudes on both sides of the threshold.

## Nonunit rates and folds

For \(\nu\ne1\), root number and sign depend jointly on

$$
(\nu,\mathfrak R_c,\Omega_{m0},\Omega_{r0})
$$

and on the admitted domain for \(x_c\). [[causal-scale-theory/theorems/flatness-tail-and-fold|The tail-and-fold theorem]] proves the relevant asymptotic and double-root criteria. With radiation present, the far-tail classes change at \(\nu=2\); without radiation, the analogous dust threshold is \(\nu=3/2\). Neither threshold is an amplitude-independent root-existence bound.

For

$$
\Omega_{m0}=0.310598,
\qquad
\Omega_{r0}=9.15\times10^{-5},
\qquad
\mathfrak R_c=1,
$$

the inherited numerical continuation reports:

| Rate \(\nu\) | Positive-root structure |
|---|---|
| \(0<\nu<1.558402308\) | one late root |
| \(\nu\simeq1.558402308\) | one simple late root and a high-\(x\) double root at \(x\simeq6.10687\) |
| \(1.558402308<\nu<1.814657\) | three roots |
| \(\nu\simeq1.814657\) | a late double root near \(x\simeq0.64905\) and one high-\(x\) root |
| \(1.814657<\nu<2\) | one high-radiation root |
| \(\nu\geq2\) | no positive root for these benchmark inputs |

The fold anchors and selected sample rates are independently recomputed by [[causal-scale-theory/receipts/background.json|the local receipt]], but the preserved continuation does not certify that no additional folds occur anywhere inside every displayed interval. The table is therefore a reviewed numerical atlas, not an exhaustive theorem. Its last row is also benchmark-specific: the same abundances with \(\mathfrak R_c=1.9\) have positive roots at \(\nu=2\) and \(\nu=2.2\).

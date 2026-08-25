# The CST-B2 Unit Branch

The CST-B2 unit branch evaluates the balanced-binary conditional background at \((\nu,\mathfrak R_c)=(1,1)\), selects its unique unit-rate candidate-crossing root, and sets the residual floor to zero. Here \(\nu=1\) is the proposed unit-rate principle and \(\mathfrak R_c=1\) is the independent weak matching principle for the integrated reference ratio; neither unity follows from normalization convention or binary algebra, and neither defines the wider [[causal-scale-theory/response-family-interface|CST response family]].

Under the hypotheses of [[causal-scale-theory/generalized-background|the CST-B2 background]], the branch has

$$
\rho_X(x)
=\frac12\rho_{\mathrm{crit},c}\operatorname{sech}^2x,
\qquad
w_X(x)
=-1+\frac23\tanh x.
$$

[[causal-scale-theory/theorems/rigid-sech-response-identities|The CST-B2 rigid-sech theorem]] owns the conservation calculation and shape invariant. At the selected reference \(x=0\), several statements coincide but have different grounds:

- the reduced binary polarization is \(m=0\), and [[binary-information-geometry/balanced-exponential-family|the balanced binary metric]] is maximal;
- the explicit response density is maximal, and separate conservation gives \(w_X=-1\);
- in flat \(3+1\) dimensions with no residual or additional crossing component, \(\mathfrak R_c=1\) makes the response equal the total non-\(X\) complement.

The first statement is exact after balanced binary reduction, the second is conditional on the rigid pulse and conservation, and the third follows from the constitutive amplitude plus the declared background contents. They are not independent predictions.

## Benchmark

For

$$
\Omega_{m0}=0.310598,
\qquad
\Omega_{r0}=9.15\times10^{-5},
$$

[[causal-scale-theory/theorems/unit-rate-crossing-sign|the unit-rate theorem]] guarantees one root. The positive benchmark root is

$$
x_c\simeq0.2940066,
\qquad
z_c=e^{x_c}-1\simeq0.3417927.
$$

The resulting conditional cosmography is

$$
\begin{array}{rcl}
w_0&\simeq&-0.8094545,\\
w_a&\simeq&-0.6122053,\\
q_0&\simeq&-0.3369025,\\
j_0&\simeq&-0.1112465.
\end{array}
$$

The benchmark enters acceleration at

$$
z_{\mathrm{acc,in}}\simeq0.7856935
$$

and exits in the future at

$$
\frac{a_{\mathrm{acc,out}}}{a_0}\simeq11.7865.
$$

These numbers are arithmetic consequences of the abundances, two unit principles, selected branch, flatness, separate conservation, and zero residual. [[causal-scale-theory/receipts/README|The receipt suite]] is their recomputation owner and should be rerun before they are used in a fit.

## Why acceleration ends

[[causal-scale-theory/theorems/future-response-classes|The CST-B2 future-class theorem]] shows that the unit response approaches coasting while diluting as \(a^{-2}\). [[causal-scale-theory/theorems/acceleration-condition|The active-mass theorem]] then explains the finite exit: the response remains energetically dominant, but its negative active-mass contribution scales as \(a^{-4}\), while positive matter active mass scales as \(a^{-3}\). Matter therefore retakes control of the acceleration sign before the background reaches its coasting limit.

This is an application of the two theorems, not a second proof of them.

## Evidential status

The benchmark displays internal rigidity and supplies regression targets. It is not a cosmological likelihood and does not confirm the microscopic wall, either unit principle, or a covariant perturbation completion. Primary CMB, lensing, growth, and response-sector stability remain outside this background calculation; [[causal-scale-theory/observables|the observable hierarchy]] states what can presently be tested.

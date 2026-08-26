# Higher-Point Dictionary

Holographic cosmology relates cosmological bispectra to analytically continued three-dimensional stress-tensor correlators, but the map includes semilocal metric-variation terms and inverse two-point response factors. The dictionary is therefore a response theorem inside a specified holographic member, not the claim that every third derivative of a scalar functional is a cosmological three-point function.

## Why two-point substitution is insufficient

Let the cosmological canonical momentum be expanded in perturbations,

$$
\Pi
=\Omega_{[2]}\zeta
+\Omega_{[3]}\zeta^2+\cdots.
$$

The nonlinear response functions determine tree-level in-in correlators. On the domain-wall side, the corresponding radial response functions determine metric derivatives of the renormalized QFT generating functional. The domain-wall/cosmology continuation maps the two response hierarchies under the hypotheses in [[vendor/holographic-cosmology/analytic-continuation-and-state|the continuation note]].

Metric differentiation produces more than separated-point stress correlators because the stress tensor itself depends on the metric. Define schematically

$$
\Upsilon_{ijkl}(x,y)
:=\frac{\delta T_{ij}(x)}
{\delta g^{kl}(y)}.
$$

Terms containing \(\langle T\Upsilon\rangle\) are semilocal: two insertions coincide. They can contribute to observable local-type non-Gaussianity and cannot generally be deleted as contact conventions.

## Scalar bispectrum

In the conventions of [[library/cosmological-3-point-correlators-from-holography/entry|McFadden and Skenderis]], with momentum delta functions stripped and all QFT quantities continued before taking the imaginary part,

$$
\begin{aligned}
\langle\!\langle
\zeta(q_1)\zeta(q_2)\zeta(q_3)
\rangle\!\rangle
=-{1\over256}
\left(\prod_i\operatorname{Im}B(\bar q_i)\right)^{-1}
\operatorname{Im}\Bigl[
&\langle\!\langle T(\bar q_1)T(\bar q_2)T(\bar q_3)\rangle\!\rangle\\
&+4\sum_i B(\bar q_i)\\
&-2\bigl(
\langle\!\langle
T(\bar q_1)\Upsilon(\bar q_2,\bar q_3)
\rangle\!\rangle
+\text{cyclic}
\bigr)
\Bigr].
\end{aligned}
$$

Here every barred momentum and every theory parameter is continued with the registered prescription. The same paper supplies scalar--scalar--tensor, scalar--tensor--tensor, and tensor--tensor--tensor dictionaries with their helicity contractions. Their common structure is

$$
\text{cosmological three-point function}
=\frac{\operatorname{Im}\!\left[
\text{continued }\langle TTT\rangle
+\text{semilocal terms}\right]}
{\text{products of continued two-point responses}}.
$$

## State and 1PI qualifications

The cosmological side is an in-in expectation value in a selected Lorentzian state. The QFT side is a Euclidean metric-response functional continued with the complete prescription. This is not the same operation as differentiating relative entropy three times, and it is not determined by the two-point kernel alone.

Equivalently, if cosmological correlations are organized through a probability-1PI functional,

$$
\Gamma[\zeta]
=\frac12\zeta\mathcal K_\zeta\zeta
+\frac1{3!}\Gamma_3[\zeta^3]+\cdots,
$$

then the leading connected bispectrum is schematically

$$
\langle\zeta_1\zeta_2\zeta_3\rangle_c
=-\mathcal C_1\mathcal C_2\mathcal C_3
\Gamma_3(1,2,3)+\cdots.
$$

The holographic dictionary must calculate the appropriate \(\Gamma_3\), including its semilocal completion. A large spin-zero two-point coefficient alone supplies no universal higher-point factorization law.

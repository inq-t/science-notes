# Normalized Heat Entropy Does Not Return the Einstein Term

The simplest attempt to identify spectral entropy with gravity fails at the first curvature-sensitive order. For a four-dimensional heat trace, the normalized Gibbs entropy cancels the term linear in \(a_2\) that contains the Einstein--Hilbert action; \(a_2\) re-enters only quadratically at the next order. An unnormalized resolution-weighted spectral multiplicity retains \(a_2\) linearly, but it is not von Neumann entropy and requires a separate wall interpretation.

## Heat trace and normalized state

Let \(P=D_A^2\geq0\) be a Laplace-type operator on a compact four-dimensional observable geometry without boundary. Write

$$
Z(t)
:=\operatorname{Tr}e^{-tP}
\sim
a_0t^{-2}+a_2t^{-1}+a_4+O(t).
$$

Define

$$
b:=\frac{a_2}{a_0},
\qquad
c:=\frac{a_4}{a_0}.
$$

Then

$$
Z(t)
=a_0t^{-2}
\left(1+bt+ct^2+O(t^3)\right)
$$

and

$$
\log Z(t)
=\log a_0-2\log t
+bt
+\left(c-\frac{b^2}{2}\right)t^2
+O(t^3).
$$

The normalized heat state is

$$
\rho_t:=\frac{e^{-tP}}{Z(t)}.
$$

Its von Neumann entropy is exactly

$$
S(\rho_t)
=\log Z(t)-t\partial_t\log Z(t).
$$

Substitution gives

$$
\boxed{
S(\rho_t)
=\log a_0-2\log t+2
+\left(\frac{b^2}{2}-c\right)t^2
+O(t^3).}
$$

The term linear in \(t\), and hence the contribution linear in \(a_2\), cancels exactly. The combination \(a_2^2/a_0^2\) reappears at order \(t^2\), where it is mixed with \(a_4/a_0\); it is not the Einstein--Hilbert term of the spectral action.

## Physical meaning of the cancellation

In the observable four-dimensional spectral action, \(a_0\) carries the volume term, \(a_2\) carries the Einstein--Hilbert and mass sector, and \(a_4\) carries curvature-squared, gauge, and Higgs structures. Therefore

$$
\boxed{
\text{ordinary normalized heat entropy does not reproduce
the linear Einstein term at first subleading order}.}
$$

This is an **[EXACT ASYMPTOTIC NO-GO]** under the stated heat-kernel hypotheses. It does not say that no entropy--gravity relation exists. It says that the most immediate identification \(S(\rho_t)\leftrightarrow S_{\mathrm{EH}}\) has the wrong expansion.

The reason is structural. Since

$$
\partial_t\log Z(t)=-\langle P\rangle_t,
$$

the entropy adds the mean-energy term through

$$
-t\partial_t\log Z
=t\langle P\rangle_t,
$$

whose asymptotic contribution \(-bt\) cancels the \(+bt\) contribution in \(\log Z\). This removes the first relative correction to the leading Weyl density.

## An unnormalized anti-information candidate

Define instead

$$
\mathfrak E(t)
:=\operatorname{Tr}\left[(1+tP)e^{-tP}\right]
=Z(t)-tZ'(t).
$$

Then

$$
\boxed{
\mathfrak E(t)
\sim
3a_0t^{-2}
+2a_2t^{-1}
+a_4
+O(t^2).}
$$

This functional is additive under direct sums and retains the Einstein coefficient. It measures a resolution-weighted spectral multiplicity rather than the entropy of a normalized state.

[[spectral-wall-descent/receipts/verify-spectral-wall.py|The verification receipt]] checks the cancellation of the linear \(a_2\) coefficient, the surviving quadratic coefficient, and the \((3,2,1)\) weights of \((a_0,a_2,a_4)\) in \(Z-tZ'\).

It is therefore reasonable to investigate \(\mathfrak E\) as **defect anti-information**, particularly on a relative or mapping-cone spectral triple associated with a wall. The proposal would have the form

$$
\mathfrak E_{\mathrm{wall}}(t)
=\operatorname{Tr}_{\mathcal H_{\mathrm{rel}}}
\left[
(1+tD_{\mathrm{rel}}^2)e^{-tD_{\mathrm{rel}}^2}
\right].
$$

This is an **[OPEN CONSTRUCTION]**. A relative Hilbert space, trace, spectrum, locality theorem, and relation to the BKM wall defect must first be supplied.

## Relation to the spectral action

For a Laplace transform representation of the cutoff function, the spectral action is assembled from heat traces \(Z(t)\), not from normalized heat-state entropy. That is why it retains \(a_2\). The action and entropy can arise from the same spectrum while remaining different functionals with different physical types.

This supports the register order in [[spectral-wall-descent/observable-spectral-action|the observable spectral-action note]]:

$$
\text{spectrum}
\longrightarrow
\begin{cases}
\text{observable action},\\
\text{normalized state entropy},\\
\text{relative wall response},
\end{cases}
$$

with no automatic equality among the three.

## Failure conditions

- A different spacetime dimension changes the powers but not the need to perform the normalization calculation.
- Zero modes and boundaries can add terms and must be treated separately; they do not restore the missing \(a_2\) term by declaration.
- \(\mathfrak E\) is not entropy merely because it is positive for \(P\geq0\).
- A relative spectral triple is required before \(\mathfrak E_{\mathrm{wall}}\) is defined.
- Retaining \(a_2\) does not determine its coefficient or prove the Einstein universality class.

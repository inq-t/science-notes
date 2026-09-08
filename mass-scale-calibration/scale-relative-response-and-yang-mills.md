# Scale-Relative Response and Yang–Mills

A dimensionless response floor can yield an energy gap across a scale family only when its comparison map reaches a complex form core of the complete physical nonvacuum carrier and uses the pulled-back physical norm. The relative gap is invariant under matched scale transport. Its positivity and its survival after the regulator and finite causal patch are removed remain substantive construction requirements.

## The conditional Copernican theorem

Let \(\mathfrak d_s\) be a nonnegative dimensionless Hermitian response form on a complex linear domain \(\mathcal D_s\) in an upstream carrier \(\mathcal W_s\). Suppose this family has the [[scale-torsor-and-the-global-local-gap-invariant#A scale-equivariant family|declared scale transport]] compatible with physical translation and form domains. Each physical presentation has a unique normalized vacuum \(\Omega_s\); alternatively replace its orthogonal complement throughout by the complete zero-spectral complement and prove coverage there. Let \(H_s\geq0\) be the vacuum-normalized reconstructed energy generator, with \(\ker H_s=\mathbb C\Omega_s\) in the unique-vacuum case. Its closed energy form is \(\mathfrak h_s[\psi]=\|H_s^{1/2}\psi\|^2\). Construct an injective complex linear map

$$
J_s:\mathcal D_s\longrightarrow
D(H_s^{1/2})\cap\Omega_s^\perp
$$

whose image is a **form core** for the energy form on the complete physical nonvacuum carrier. Upstream gauge-null directions have already been quotiented. Normalize the response against the pulled-back physical norm,

$$
g_s[\xi]:=\|J_s\xi\|^2.
$$

If, uniformly through volume and regulator removal,

$$
\mathfrak d_s[\xi]\geq
\kappa g_s[\xi]
\quad(\xi\in\mathcal D_s),
\qquad
\mathfrak h_s[J_s\xi]\geq
\eta E_s\mathfrak d_s[\xi],
\tag{S9}
$$

with \(\kappa,\eta>0\), fixed normalization, and an independently selected reference energy \(E_s>0\) satisfying \(E_{\lambda s}=\lambda^{-1}E_s\) in the presentation family (with \(\hbar,c\) held fixed), then

$$
\frac{\Delta_{E,s}}{E_s}\geq\eta\kappa>0.
\tag{S10}
$$

This is the [[measured-response-carriers/response-to-energy-comparison|response-to-energy comparison theorem]] on the represented image: write \(\psi=J_s\xi\) and define the response there by \(q_s[\psi]=\mathfrak d_s[J_s^{-1}\psi]\). The injectivity of \(J_s\) makes that form well-defined, and the physical norm supplies its reference metric. The theorem closes the resulting lower bound in the physical energy-form norm. Mere Hilbert-space density does not replace this form-core condition; no self-adjoint response generator is claimed without a separate closure argument.

The normalization is essential. On a one-dimensional nonvacuum carrier take \(H=\varepsilon I\), \(\mathfrak d[\xi]=|\xi|^2\), and \(J=\varepsilon^{-1/2}I\), with \(\eta=E=1\) and \(0<\varepsilon<1\). Then \(J\) is onto and \(\mathfrak h[J\xi]=\mathfrak d[\xi]\), but the physical gap is \(\varepsilon\), not the unit floor of \(\mathfrak d\) in the upstream norm. The correct reference is \(g[\xi]=\varepsilon^{-1}|\xi|^2\), giving the relative edge \(\kappa=\varepsilon\). More generally a bound against the upstream norm incurs a factor \(\|J\|^{-2}\) when \(J\) is bounded; without norm control it gives no stated physical constant.

The ratio in (S10) is invariant under the specified family comparison; \(E_s\) is the reference energy in that member. Choosing the member and choosing reporting units are separate operations. This is the conditional content available in the thought that mass is a rate of factification. The response and comparison map must be constructed independently of the target spectral edge, and the energy comparison must not define \(\mathfrak d_s[\xi]:=\mathfrak h_s[J_s\xi]/E_s\) after the fact. The reference metric specifies the denominator of the problem; it does not prove the lower response bound.

## A causal patch is not an ordinary resonant box

If the only confinement scale is a causal-diamond radius \(R\), an ordinary box mode gives

$$
K_R\sim\frac{1}{R},
\tag{S11}
$$

which vanishes as \(R\to\infty\). That cannot prove the Clay gap on \(\mathbb R^4\). A causal-patch construction remains viable only if its boundary or descent law yields a coercive invariant uniform under enlargement of the patch, and if an atlas of such patches reconstructs locality, Poincare covariance, and the same infinite-volume vacuum representation. [[global-local-response-reconstruction/causal-patch-boundary-and-two-times]] states those recovery conditions.

Thus “confinement” in the proposed wave picture cannot merely mean a finite spatial cavity. It must mean an admissibility, gluing, or closed-range condition on the global carrier that continues to exclude arbitrarily soft physical distinctions after the apparent box has been removed.

## The fresh problem

The new question is not “which constant should multiply a guessed mass operator?” It is:

$$
\boxed{
\begin{gathered}
\text{Construct one scale-equivariant whole whose local presentations}\\
\text{recover pure Yang--Mills and whose natural dimensionless response}\\
\text{has a uniform positive floor on the complete vacuum complement.}
\end{gathered}}
\tag{S12}
$$

This abandons pre-given metric scale as an explanatory primitive. It does not abandon the continuum, locality, unitarity, or Poincare symmetry that must reappear as properties of the local physical presentation. “The whole is not unitary” is best typed as: *unitarity is not yet a predicate of the upstream object*. It becomes meaningful only after a Hilbert carrier and a reversible clock action have been reconstructed.

[[global-local-response-reconstruction/inq|Global--Local Response Reconstruction]] packages this torsor statement with the concrete two-boundary response operator and the QFT recovery contract.

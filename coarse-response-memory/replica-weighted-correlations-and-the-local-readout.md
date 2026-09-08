# Replica-Weighted Correlations and the Local Readout

Squaring the prepared Gram amplitude produces an exact mixture of identical one-loop laws, weighted by their squared overlap. Its relative harmonic moments are nonnegative, but neither positivity nor an estimate on each hidden contribution controls their nonlinear comparison after averaging. The local marginal has a sharper identity: its logarithmic curvature is the posterior mean curvature plus a positive posterior score variance. The preparation must constrain that balance; replacing its state by a convolution average changes the dynamics being tested.

**Status: exact fixed-system identities and a componentwise obstruction; numerical global-moment checks; open local curvature estimate.** The graph, metric, Hamiltonian and initial Haar vector remain the inputs of [[positive-amplitude-kernel-and-preparation|the positive-amplitude construction]]. Probability here represents the supplied heat equation, not an assertion about ontological randomness.

## Squaring changes the source weights

Fix a finite preparation time \(t\), \(G=SU(2)\), normalized Haar measure, and the features \(f_S=f_{t,S}\) in (PK2). Let \(S,T\) be independent copies of the shared path, with common law \(\nu_t\). Put
\[
g_{ST}(x)=f_S(x)f_T(x),\qquad
Z_{ST}=\int_Gg_{ST}(x)\,dx,\qquad
\mathcal N_t=\mathbb E_{S,T}Z_{ST}^{\,2}.
\tag{RW1}
\]
The normalized squared amplitude and its complete marginal are
\[
\boxed{
\psi_t(x,y)^2=\mathbb E_{\widehat\nu_t}[p_{ST}(x)p_{ST}(y)],
\qquad R_t(x)=\mathbb E_{\widehat\nu_t}p_{ST}(x),
}
\tag{RW2}
\]
where
\[
p_{ST}=g_{ST}/Z_{ST},\qquad
d\widehat\nu_t(S,T)=\frac{Z_{ST}^{\,2}}{\mathcal N_t}
\,d\nu_t(S)d\nu_t(T).
\tag{RW3}
\]
Indeed, expanding \(P_t(x,y)^2\) introduces two independent shared paths. Integrating both output variables gives exactly \(\|P_t\|_2^2=\mathbb E Z_{ST}^2\). Normalizing each product density then forces (RW3). The mixing law is not the unweighted product Brownian law. Both the features and their weights are outputs of the same declared preparation.

For \(\lambda\ge0\), \(e^{-2\lambda t}\le f_S\le1\), so all the normalizers and weights are strictly positive. In particular,
\(e^{-4\lambda t}\le p_{ST}\le e^{4\lambda t}\).

## The relative moments are harmonic squares

For an irreducible unitary representation \(\pi_n\) of dimension \(d_n=n+1\), define
\[
\alpha_n(t)=\mathbb E_{\psi_t^2}
\frac{\chi_n(xy^{-1})}{d_n}.
\]
The product law in each replica component gives
\[
\boxed{
\alpha_n(t)=\frac1{d_n}\mathbb E_{\widehat\nu_t}
\left\|\int_G\pi_n(x)p_{ST}(x)\,dx\right\|_{\rm HS}^2\ge0.
}
\tag{RW4}
\]
This follows by expanding the character as
\(\operatorname{Tr}[\pi_n(x)\pi_n(y)^*]\). It uses no assumption that an individual feature is central.

Represent a unit quaternion \(x\) by \(X\in S^3\subset\mathbb R^4\). For a component \(p=p_{ST}\), set
\[
m=\mathbb E_pX,\quad \Theta=\mathbb E_pXX^{\mathsf T},\quad
r=|m|^2,\quad
s=\frac{4\operatorname{tr}\Theta^2-1}{3}
=\frac43\|\Theta-I_4/4\|_F^2.
\tag{RW5}
\]
Here \(\Theta\) is a second moment, not a covariance. Since \(q(xy^{-1})=X\cdot Y\), (RW4) gives \(\alpha_1=\mathbb E r\) and \(\alpha_2=\mathbb E s\). Consequently
\[
\boxed{
\alpha_2-\alpha_1^2
=\mathbb E_{\widehat\nu_t}(s-r^2)
+\operatorname{Var}_{\widehat\nu_t}(r).
}
\tag{RW6}
\]
Even a componentwise inequality \(s\le r^2\) would not suffice to prove \(\alpha_2\le\alpha_1^2\): its averaged margin would have to dominate the added mixture variance. In fact that componentwise inequality fails for reachable hidden contributions.

## An opposite-feature pair defeats the componentwise bound

Take \(\kappa,\lambda>0\). First use the ideal shared controls \(S_s=1\) and \(T_s=-1\). The second is not based at \(1\); a based approximation is supplied below. With \(a=q(x)\) and \(D\chi_n=n(n+2)\chi_n/4\), their features are
\[
f_+(a)=e^{-t(3\kappa D+\lambda(1-a))}1,\qquad
f_-(a)=f_+(-a),\qquad p(a)\propto f_+(a)f_+(-a).
\tag{RW7}
\]
This is the product of two features, not the squared scalar amplitude. It is central and even, hence \(m=0\) exactly. The outer path uses speed \(3\kappa\), not the four-link marginal speed.

The scalar heat equation, with
\(D=-[(1-a^2)\partial_a^2-3a\partial_a]/4\), gives
\[
\begin{aligned}
\log f_+(a)={}&-\lambda t+\lambda at
-\frac{9\kappa\lambda}{8}at^2\\
&+\left[\frac{27\kappa^2\lambda}{32}a
+\frac{\kappa\lambda^2}{4}(1-a^2)\right]t^3+O(t^4).
\end{aligned}
\tag{RW8}
\]
For example, insert a power series into
\(\partial_t\log f=(3\kappa/4)[(1-a^2)((\log f)''+((\log f)')^2)-3a(\log f)']-\lambda(1-a)\).
The expansion is uniform on the closed latitude interval for fixed coefficients. Adding its two signs and normalizing yields
\[
p(a)=1-\frac{\kappa\lambda^2}{2}(a^2-\tfrac14)t^3+O(t^4),
\qquad
\beta_2:=\mathbb E_p\chi_2/3
=-\frac{\kappa\lambda^2}{24}t^3+O(t^4).
\tag{RW9}
\]
The coefficient uses Haar moments \(\mathbb E a^2=1/4\), \(\mathbb E a^4=1/8\). For central \(p\), its spin-one Fourier matrix is \(\beta_2I_3\). Thus the relative moment of two independent draws from \(p\) is
\[
r=0,\qquad s=\beta_2^2
=\frac{\kappa^2\lambda^4}{576}t^6+O(t^7)>0
\tag{RW10}
\]
at sufficiently small positive \(t\). A negative single-density quadrupole has produced a positive squared relative harmonic.

Now fix such a time and replace \(T\) by a smooth based path \(T_\delta\) going from \(1\) to \(-1\) during \([0,\delta]\), then remaining there. Boundedness of \(V=\lambda(1-q)\) gives
\[
\sup_x|f_{T_\delta}(x)-f_-(x)|\le2\lambda\delta.
\]
The feature map is continuous in the shared path's uniform topology. Normalizers stay positive, so strict \(s>r^2\) survives sufficiently small \(\delta\) and then open neighborhoods of both based paths. The nondegenerate group Brownian law gives these neighborhoods positive probability: its right-invariant diffusion fields span every tangent space, so every smooth based control lies in its support. This is the compact-group application of the Stroock--Varadhan support theorem; [Stroock's account](https://celebratio.org/Varadhan_SRS/article/117/) identifies the original result. Positive overlap weights preserve positive measure under \(\widehat\nu_t\).

Thus no almost-everywhere replica-by-replica proof of \(s\le r^2\) is available. This does **not** refute the corresponding inequality for the actual weighted average, nor the local curvature of the actual prepared state.

## Averaging to convolution does not transport the evolution

Let the common-left average of a density be
\[
(\mathcal T\rho)(x,y)=\int_G\rho(hx,hy)\,dh.
\tag{RW11}
\]
For the gauge-invariant actual state this is a central relative-convolution density, with both full marginals Haar. Every relative character moment is preserved, since \(\chi_n(xy^{-1})\) is invariant under simultaneous conjugation. But its amplitude is \(\sqrt{\mathcal T(\psi_t^2)}\), not \(\mathcal T\psi_t\).

Linear averaging commutes with the electric operator \(H_0\), not the magnetic one. On the constant function,
\[
(\mathcal T H_\lambda-H_\lambda\mathcal T)1
=\lambda(a+b).
\tag{RW12}
\]
Nor does density averaging intertwine the normalized squared-amplitude evolution. Starting from the actual Haar vector gives
\(\mathcal T(\psi_t^2)=1+\lambda^2t^2q(xy^{-1})+O(t^3)\).
By contrast, averaging the magnetic multiplication potential first makes it the constant \(2\lambda\); that averaged Hamiltonian leaves the normalized Haar vector unchanged.

The convolution criterion (PK13) therefore tests a **restart** from the averaged density's square root. It is not automatically a necessary condition on the original nonconvolution trajectory. Even a proof of \(\alpha_2\le\alpha_1^2\) along that trajectory would not by itself prove its local marginal concavity.

## The actual local target uses a posterior law

Write \(\omega=(S,T)\). Conjugation-average each component density,
\[
\bar p_\omega(a)=\int_Gp_\omega(hxh^{-1})\,dh,
\qquad q(x)=a.
\]
The actual marginal is central, hence \(R(a)=\mathbb E_{\widehat\nu_t}\bar p_\omega(a)\). These are densities relative to Haar; do not include the latitude Jacobian \(\sqrt{1-a^2}\) in \(\bar p\) or \(R\). Put \(\ell_\omega=\log\bar p_\omega\). At fixed preparation time,
\[
d\widehat\nu_{t,a}(\omega)
=\frac{\bar p_\omega(a)}{R(a)}d\widehat\nu_t(\omega),\qquad
\boxed{
(\log\sqrt R)''(a)
=\frac12\left[
\mathbb E_{\widehat\nu_{t,a}}\ell_\omega''(a)
+\operatorname{Var}_{\widehat\nu_{t,a}}(\ell_\omega'(a))
\right].
}
\tag{RW13}
\]
Differentiate \(R=\int e^\ell d\widehat\nu_t\) twice. This is the scalar log-normalizer form of [[rg-covariance-residue/conditioned-source-transport|conditioned source differentiation]], applied to the actual replica representation. The local posterior, not the prior \(\widehat\nu_t\), supplies both terms.

For finite bounded times, differentiation is justified uniformly in the paths: start outer Brownian motion as \(xB_s\), so spatial derivatives fall on the smooth bounded potential. Feynman--Kac differentiation gives uniform \(C^m(G)\) bounds. Conjugation averaging preserves them; uniform \(C^4\) class bounds and even geodesic Taylor expansions at the two poles give \(C^2\) latitude extensions. Strict positive lower bounds justify the logarithms. Formula (RW13) consequently extends to one-sided endpoint limits. These are continuous density versions, not conditioning on a positive-probability pole event. No infinite-time uniformity is asserted.

The local proof obligation is
\[
\mathbb E_{\widehat\nu_{t,a}}\ell_\omega''(a)
\le-\operatorname{Var}_{\widehat\nu_{t,a}}(\ell_\omega'(a)).
\tag{RW14}
\]
This is an equivalent expression of the desired latitude concavity, **not a proof**. It exposes the missing channel: variation of the source score after the readout has reweighted the source law. It neither identifies that score variance with the [[conditional-fisher-coercivity/moving-fiber-connection|raw conditional information metric]] nor replaces the separate full-carrier comparison by a scalar identity.

[[path-source-tilts-and-the-curvature-budget|Resolving the outer paths as well]]
now makes each component curvature explicit and nonpositive.
The remaining posterior variance is measured against that
geometric term. At late preparation time the two grow together,
so a fixed fractional margin is impossible; the finite correlated
difference, not separate relative bounds, is the target.
[[certified-ground-marginal-and-late-preparation|The full-trajectory certificate]]
now proves its sign at \(\kappa=\lambda=1\), including the ground
limit; arbitrary couplings and spatial extension remain open.

## Focused checks and the remaining selection problem

For actual Haar preparation, harmonic degree counting in the time expansion gives
\[
\alpha_1=\lambda^2t^2/4+O(t^3),\qquad
\alpha_2=\lambda^4t^4/36+O(t^5),\qquad
\alpha_2-\alpha_1^2=-5\lambda^4t^4/144+O(t^5).
\tag{RW15}
\]
The electric operator preserves each loop's representation degree. The leading first and second relative harmonics require respectively two and four magnetic insertions across the two loops, so their leading coefficients equal those of the product magnetic amplitude. This checks the initial sign of the **global** comparison, not (RW14) at later times.

The [[receipts/two_plaquette_vacuum_receipt.py|full interacting receipt]] keeps every relational channel. At \(\kappa=1,t=0.2\), its global defects \(\alpha_2-\alpha_1^2\) are approximately \(-1.28213020\,10^{-6}\) for \(\lambda=0.5\) and \(-0.08237947\) for \(\lambda=16\). Separate cutoff and quadrature refinements agree within \(5\,10^{-13}\). The independent scalar check of (RW9), at \(\kappa=\lambda=1\) and \(t=0.2,0.1,0.05\), gives ratios \(\beta_2/(-t^3/24)\) approximately \(0.539473,0.730794,0.853775\), approaching one. That scalar check uses the ideal opposite control; the based-path support argument is analytic.

The preparation supplies more than a positive cone. Its quantitative benefit in (RW14) is now certified throughout preparation at equal unit coefficients, but is not proved for the general family. A proposed deeper algebra must constrain this shared state-and-readout law, not merely embed its supplied positive kernel in a larger carrier. The [[algebra/octonionic-associator-and-branch-forgetting|octonionic comparison]] remains a different possible primitive: no multiplication associator has been identified with either variance above. Any extension of the estimate must retain the overlap weights, the local posterior and the original dynamics together.

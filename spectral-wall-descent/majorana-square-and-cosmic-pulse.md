# The Majorana Square and the Cosmic Pulse

The Majorana contribution to the observable spectral action separates exactly into a positive square about the central point \(r\mathbf1\) and an \(R\)-independent residual. The source varies only the scale of a fixed Majorana matrix, whereas a broader project extension admits a traceless hyperbolic orbit that leaves the spectral Newton coefficient constant while producing an exact \(\operatorname{sech}^2\) deficit in the cosmological coefficient. This is a genuine common-shape construction for a candidate CST-B2-shaped spectral member, but it neither selects that member, fixes the residual cosmological constant, nor solves the amplitude hierarchy.

## Exact square completion

In [[library/ncg-standard-model-neutrino-mixing/entry|the local noncommutative Standard Model source]], let

$$
R:=M_R^*M_R,
\qquad
c=\operatorname{Tr}R,
\qquad
d=\operatorname{Tr}R^2,
$$

on an \(n\)-generation space. In the Euclidean spectral action, the constant-density coefficient is

$$
\gamma_0(R)
=\frac{1}{\pi^2}
\left(
48f_4\Lambda^4
-f_2\Lambda^2\operatorname{Tr}R
+\frac{f_0}{4}\operatorname{Tr}R^2
\right).
$$

Define

$$
r:=\frac{2f_2\Lambda^2}{f_0}.
$$

Completing the square gives the **[EXACT SPECTRAL-ACTION IDENTITY]**

$$
\boxed{
\gamma_0(R)
=\frac{f_0}{4\pi^2}
\operatorname{Tr}(R-r\mathbf1)^2
+\gamma_{\mathrm{res}},}
$$

where

$$
\boxed{
\gamma_{\mathrm{res}}
=\frac{\Lambda^4}{\pi^2}
\left(
48f_4-\frac{nf_2^2}{f_0}
\right).}
$$

If \(R\) is varied freely over the positive Hermitian cone, the positive square vanishes at \(R=r\mathbf1\). This is the unrestricted project minimizer. It does not remove \(\gamma_{\mathrm{res}}\). Vanishing of the residual requires the independent moment relation

$$
48f_4=\frac{nf_2^2}{f_0}.
$$

Imposing that equation without deriving the cutoff moments is tuning, not a solution of the cosmological-constant problem.

The source calculation varies only a fixed Majorana ray,

$$
M_R=xk_R,
\qquad
A:=k_R^*k_R,
\qquad
R(x)=x^2A.
$$

Its stationary equation is derived in flat space with the Higgs vacuum expectation value neglected relative to the unification scale. Under those hypotheses, \(x=0\) is the unstable solution; for \(f_0,f_2>0\) and \(A\ne0\), write

$$
n_{\mathrm{eff}}
:=\frac{(\operatorname{Tr}A)^2}{\operatorname{Tr}A^2},
\qquad
1\leq n_{\mathrm{eff}}
\leq\operatorname{rank}(A)
\leq n,
$$

the stationary point on that ray is

$$
\boxed{
x_*^2
=r\frac{\operatorname{Tr}A}{\operatorname{Tr}A^2},
\qquad
R_*
=rA\frac{\operatorname{Tr}A}{\operatorname{Tr}A^2}.}
$$

It reaches \(r\mathbf1\) only when \(A\) is full rank and proportional to the identity. More generally, the upper equality \(n_{\mathrm{eff}}=\operatorname{rank}(A)\) holds exactly when the nonzero eigenvalues of \(A\) are equal. The source-aligned residual is

$$
\boxed{
\gamma_{\mathrm{res}}^{\mathrm{ray}}
=\frac{\Lambda^4}{\pi^2}
\left(
48f_4-\frac{n_{\mathrm{eff}}f_2^2}{f_0}
\right).}
$$

## The source-ray Newton coefficient

The same source gives

$$
\kappa_0^{-2}
=\frac{96f_2\Lambda^2-f_0\operatorname{Tr}R}
{12\pi^2}.
$$

At the source-ray stationary point,

$$
\boxed{
\kappa_{*,\mathrm{ray}}^{-2}
=\frac{(48-n_{\mathrm{eff}})f_2\Lambda^2}{6\pi^2}.}
$$

Using natural units and the standard GR convention \(\kappa^2=8\pi G\), this implies

$$
\eta_{\mathrm{spec}}
:=2\pi\kappa_{*,\mathrm{ray}}^{-2}
=\frac{(48-n_{\mathrm{eff}})f_2\Lambda^2}{3\pi},
$$

$$
\boxed{
G_{\mathrm{spec}}^{\mathrm{ray}}
=\frac{3\pi}
{4(48-n_{\mathrm{eff}})f_2\Lambda^2}.}
$$

For the special isotropic three-generation choice \(A\propto\mathbf1\), one has \(n_{\mathrm{eff}}=n=3\), so

$$
G_{\mathrm{spec}}
=\frac{\pi}{60f_2\Lambda^2}.
$$

These are exact consequences of the displayed observable spectral-action coefficients and the source's fixed-ray stationary equation in its flat-space, negligible-Higgs regime. They are not a first-principles prediction of \(G\), because \(f_2\), \(\Lambda\), the cutoff normalization, the matrix shape \(A\), and the stationary-point selection remain inputs. Curvature and Higgs-dependent terms alter the stationarity equation outside that approximation. A completed wall theory would have to derive the independent equality

$$
\eta_*=\eta_{\mathrm{spec}},
$$

with \(\eta_*\) calculated from [[deriving-value-of-g/spectral-index-area-route|the spectral index--area route]].

## A project constant-\(G\), \(\operatorname{sech}^2\) orbit

The following orbit belongs to the larger project extension in which \(R\) is allowed to change shape; it is not the source's one-parameter ray \(x^2A\). Let \(Q=Q^*\) satisfy

$$
\operatorname{Tr}Q=0,
\qquad
\operatorname{Tr}Q^2=q_2,
$$

and define

$$
R(N)
=r\mathbf1
+s\tanh\!\left(\nu(N-N_c)\right)Q,
$$

with

$$
r>|s|\lVert Q\rVert
$$

so that \(R(N)>0\) throughout the orbit. Tracelessness gives

$$
\operatorname{Tr}R(N)=nr,
$$

so \(\kappa_0^{-2}\) and hence the spectral Newton coefficient are exactly constant. The square completion gives

$$
\gamma_0(N)
=\gamma_{\mathrm{res}}
+\frac{f_0s^2q_2}{4\pi^2}
\tanh^2\!\left(\nu(N-N_c)\right).
$$

If

$$
\gamma_\infty
:=\gamma_{\mathrm{res}}
+\frac{f_0s^2q_2}{4\pi^2},
$$

then

$$
\boxed{
\gamma_\infty-\gamma_0(N)
=\frac{f_0s^2q_2}{4\pi^2}
\operatorname{sech}^2\!\left(\nu(N-N_c)\right).}
$$

This is an exact identity for the displayed project orbit and realizes the shape used by [[causal-scale-theory/response-law|the causal-scale response law]]. The coefficient \(\gamma_0\) here is a Euclidean constant-density term, not yet an observed Lorentzian cosmological constant or dark-energy density. A consumer map must fix the continuation, sign, units, stress tensor, conservation law, and relation between the algebraic coordinate \(N\) and cosmological scale.

## The hierarchy audit

The amplitude is

$$
\Gamma_*
=\frac{f_0s^2q_2}{4\pi^2}.
$$

If it is directly identified in natural units with an observed dark-energy density of order \(E_\Lambda^4\), then

$$
\sqrt{|s|}
\sim
\left(\frac{4\pi^2}{f_0q_2}\right)^{1/4}
E_\Lambda.
$$

For order-one \(f_0q_2\) and \(E_\Lambda\) of a few meV, \(\sqrt{|s|}\) is also of meV order. Against a conventional heavy Majorana scale \(\sqrt r\sim10^{14}\,\mathrm{GeV}\), this is schematically

$$
\frac{|s|}{r}\sim10^{-52}.
$$

The direct identification therefore moves the hierarchy into the traceless-orbit amplitude. A viable construction needs a protected normalization, Schur suppression, determinant renormalization, or another independently derived wall mechanism.

## Why the residual is a separate register

Three structures are blind to a common scalar shift:

1. normalized state families under \(K\mapsto K+c\mathbf1\);
2. null focusing through \(R_{ab}k^ak^b\), since \(g_{ab}k^ak^b=0\); and
3. the traceless orbit above, which leaves \(\operatorname{Tr}R\) fixed.

The transient response and the residual cosmological constant therefore belong to different theorem targets. The pulse may live in a noncentral response sector, while \(\gamma_{\mathrm{res}}\) requires a global central class, cutoff-moment relation, boundary condition, stack cocycle, or volume constraint. [[contemporary-puzzles/dark-energy-and-acceleration/entry|The dark-energy reclassification]] already requires this separation.

## Claim boundary

- The square completion is an exact algebraic calculation from the displayed spectral coefficients; the source-ray stationary coefficient additionally assumes flat space and a Higgs vacuum expectation negligible against the unification scale.
- The hyperbolic profile is an exact identity on a project-chosen orbit in the positive Majorana cone; the source theory derives neither that orbit nor its cosmological parametrization.
- The construction leaves \(G\) constant by tracelessness; it does not show that the observed \(G\) has the calculated value.
- Matching the pulse amplitude directly does not solve the hierarchy.
- The spectral action is downstream observable dynamics and is not used as the ontological law that creates the wall.

[[spectral-wall-descent/receipts/verify-spectral-wall.py|The spectral-wall receipt]] separately verifies the square completion, source-ray stationary coefficient, and the project orbit's constant trace and \(\operatorname{sech}^2\) deficit numerically.

Primary source: [gravity and the Standard Model with neutrino mixing](https://arxiv.org/abs/hep-th/0610241).

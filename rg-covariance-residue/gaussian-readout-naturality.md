# Gaussian Readout Naturality

A finite Gaussian law admits one reversible diffusion rule that treats every surjective linear observation as an autonomous presentation with the same clock: its mobility is its covariance, up to one common rate. Within the class of state-only constant-mobility rules, compatibility under changes of coordinates and reductions determines this choice. The resulting generator splits exactly into equally normalized retained and conditional-residual generators. For two increasingly correlated contexts, both normalized collective and relative distinctions keep their full Hermite response; this changes the processing law rather than rescaling the conditional-refresh clock.

## A state-only reversible diffusion rule

For every finite real coordinate space of dimension \(n\ge1\), let
\(\mu_\Sigma=N(0,\Sigma)\), with \(\Sigma>0\). Consider a rule assigning a constant symmetric nonnegative mobility \(B_\Sigma\), depending only on this covariance. Its nonnegative reversible generator is
\[
L_{\Sigma,B}f
=-\operatorname{Tr}(B_\Sigma\nabla^2f)
+(B_\Sigma\Sigma^{-1}x)\cdot\nabla f
=-\mu_\Sigma^{-1}\operatorname{div}
  (\mu_\Sigma B_\Sigma\nabla f).
\tag{GN1}
\]
The displayed density notation uses Lebesgue coordinates. The associated form is
\[
\mathcal E_{\Sigma,B}(f,g)
=\int (\nabla\overline f)^TB_\Sigma\nabla g\,d\mu_\Sigma.
\tag{GN2}
\]
Its Markov generator is \(-L_{\Sigma,B}\). The instantaneous noise covariance is \(2B_\Sigma\,dt\); the form co-metric is \(B_\Sigma\), without that factor two. Reversibility in the given Gaussian law fixes the drift in (GN1). Invariance of a law alone would allow additional stationary circulation.

For a surjective linear map \(A:\mathbb R^n\to\mathbb R^m\), put
\[
\Sigma_A=A\Sigma A^T,\qquad
J_A f=f\circ A.
\tag{GN3}
\]
The map \(J_A:L^2(\mu_{\Sigma_A})\to L^2(\mu_\Sigma)\) is an isometry. Call the rule natural if its semigroups satisfy
\[
e^{-tL_{\Sigma,B}}J_A
=J_Ae^{-tL_{\Sigma_A,B}},\qquad t\ge0,
\tag{GN4}
\]
for every such map, including invertible changes of coordinates. No Euclidean metric independent of the state, preferred direction, or readout-dependent rate is among the inputs.

## Naturality fixes the mobility up to a common rate

**Finite-dimensional characterization.** A rule of the stated class satisfies (GN4) in every dimension if and only if
\[
\boxed{B_\Sigma=c\Sigma}
\tag{GN5}
\]
for one constant \(c\ge0\) shared by all covariances and dimensions. Nontriviality of the rule makes \(c>0\).

To prove necessity, differentiate (GN4) on polynomial tests. Comparing its second-order terms gives
\[
B_{A\Sigma A^T}=AB_\Sigma A^T.
\tag{GN6}
\]
This identity can also be read off at \(x=0\) using every quadratic test. For \(\Sigma=I_n\), invariance under every orthogonal change of coordinates makes \(B_{I_n}=c_nI_n\). Applying (GN6) with the invertible matrix \(\Sigma^{1/2}\) gives \(B_\Sigma=c_n\Sigma\). Coordinate projections from dimension \(n\) to dimension \(m\) then give \(c_n=c_m\). Projection to dimension one fixes a common \(c\) for every dimension.

These are distinct requirements. Symmetries preserving one Gaussian state constrain its mobility to a scalar multiple of that state's covariance. Covariance under all invertible readouts identifies those scalars across different states in the same dimension; surjective reductions identify them across dimensions. Detailed balance is the separate condition fixing the drift once the mobility and state are given.

For sufficiency, write
\[
L_\Sigma=c\big[-\operatorname{Tr}(\Sigma\nabla^2)+x\cdot\nabla\big].
\tag{GN7}
\]
Its conservative reversible semigroup is the explicit Gaussian kernel
\[
(P_t^\Sigma f)(x)
=\int f\big(e^{-ct}x+\sqrt{1-e^{-2ct}}\,u\big)\,d\mu_\Sigma(u).
\tag{GN8}
\]
Pushing its noise through \(A\) gives exactly \(\mu_{\Sigma_A}\), proving (GN4) on the complete \(L^2\) spaces. Thus \(J_A\) intertwines the closed generators and their domains, as well as the semigroups. Taking adjoints shows that the conditional expectation \(J_AJ_A^*\) commutes with the whole semigroup: each linear readout is a reducing observable subspace. Successive readouts compose without changing the rate.

For \(c>0\), whitening \(x=\Sigma^{1/2}z\) identifies \(L_\Sigma\) with \(c\mathcal N_n\), where \(\mathcal N_n=-\Delta_z+z\cdot\nabla_z\). If \(f=\sum_{q\ge0}f_q\) is its orthogonal Hermite-degree decomposition, then
\[
L_\Sigma f_q=cqf_q,\qquad
\operatorname{Dom}L_\Sigma
=\left\{f:\sum_{q\ge0}q^2\|f_q\|_2^2<\infty\right\}.
\tag{GN9}
\]
Finite Hermite spans are operator and form cores. Constants give the unique vacuum, the complete centered gap is \(c\), and all degrees, including mixed observables, are present. The case \(c=0\) is the identity semigroup and has no positive response gap.

This characterization does not obtain an absolute duration. It determines relative normalization across states, directions and dimensions. If one instead assumes at the outset that every scalar linear readout has precisely the rate-\(c\) Ornstein–Uhlenbeck law, tests of its first and second powers already force the drift and mobility in (GN7). That stronger formulation places most of the conclusion directly in the assumption; (GN4) starts with an unspecified state-only rule in the declared diffusion class.

## The harmonic residual carries the same clock

Use the existing [[gaussian-harmonic-refresh-lifting|Gaussian harmonic lift]] for the observation \(A\). Its retained lift and residual covariance are
\[
M=\Sigma A^T\Sigma_A^{-1},\qquad
R=I-MA,\qquad V=\ker A,
\]
\[
\Sigma_V=R\Sigma R^T
=\Sigma-M\Sigma_AM^T.
\tag{GN10}
\]
Here \(\Sigma_V\) is positive definite on \(V\); its displayed ambient matrix vanishes on \(V^\perp\). The harmonic-lift theorem owns the independence, precision-orthogonal energy decomposition and exact composition of the lifts. For \(X\sim\mu_\Sigma\), its independent coordinates are \(\zeta=RX\) and \(Z=AX\), with \(X=\zeta+MZ\).

The additional dynamical statement follows from the same matrix calculation:
\[
\begin{pmatrix}R\\ A\end{pmatrix}
\Sigma
\begin{pmatrix}R^T&A^T\end{pmatrix}
=\begin{pmatrix}\Sigma_V&0\\0&\Sigma_A\end{pmatrix}.
\tag{GN11}
\]
The drift \(cx\) transforms into \(c(\zeta,Z)\). Consequently the unitary
\(Uf(\zeta,z)=f(\zeta+Mz)\) satisfies
\[
\boxed{UL_\Sigma U^{-1}
=L_{\Sigma_V}\otimes I+I\otimes L_{\Sigma_A}.}
\tag{GN12}
\]
The equality holds for the closed operators defined by the product form or Hermite spectral calculus. A retained degree \(p\) and residual degree \(q\) have rate \(c(p+q)\). Both nontrivial factors have gap \(c\); a zero-dimensional residual contributes only constants. There is no independent residual-rate choice. Unlike the physical Euclidean-mobility comparison in the harmonic-lift note, (GN12) uses covariance mobility on every factor and is an exact equality of the complete forms.

## Two narrowing contexts retain both resolved modes

Let \(x,y\in\mathbb R^d\), \(-1<\rho<1\), and prescribe the common law
\[
\Sigma_\rho=
\begin{pmatrix}I&\rho I\\\rho I&I\end{pmatrix}.
\tag{GN13}
\]
Its covariance generator is
\[
L_\rho=c\big[-\Delta_x-\Delta_y
-2\rho\nabla_x\cdot\nabla_y
+x\cdot\nabla_x+y\cdot\nabla_y\big].
\tag{GN14}
\]
The mixed mobility is part of the same state-derived tensor. In particular each one-context observation has generator \(c[-\Delta+x\cdot\nabla]\). Conditioning on \(y\) gives the independent standard coordinates
\(y\) and \((x-\rho y)/\sqrt{1-\rho^2}\), which realize (GN12).

For the collective and relative presentation, define
\[
w_+=\frac{x+y}{\sqrt{2(1+\rho)}},\qquad
w_-=\frac{x-y}{\sqrt{2(1-\rho)}}.
\tag{GN15}
\]
These are independent standard \(d\)-dimensional Gaussians. The explicitly fixed coordinate map
\[
W_\rho F(x,y)=F(w_+,w_-)
\]
is unitary from \(L^2(\gamma_d\otimes\gamma_d)\) onto \(L^2(\mu_{\Sigma_\rho})\), and
\[
\boxed{W_\rho^*L_\rho W_\rho
=c(\mathcal N_+\otimes I+I\otimes\mathcal N_-).}
\tag{GN16}
\]
This is exact for every \(\rho\), with the domain in (GN9); it is not merely an asymptotic equality of the first modes. Under this specified whitening, all heat operators, resolvents and unitary clocks are independent of \(\rho\). Every normalized collective or relative linear distinction has rate \(c\), while a mixed Hermite polynomial of degrees \((p,q)\) has rate \(c(p+q)\). For example, \(w_{+,i}w_{-,j}\) has rate \(2c\).

As \(\rho\uparrow1\), the raw law nevertheless converges to the diagonal law \(x=y\). Indeed \(\mathbb E|x-y|^2=2d(1-\rho)\to0\). The resolved relative observable in (GN15) has a diverging raw coefficient. At exactly \(\rho=1\), that coordinate is absent from the unrescaled diagonal carrier. Equation (GN16) preserves it on the declared resolved carrier, and does not assert that every fixed raw observable retains a relative distinction.

Two negative tests identify the work done by the rule. First, mobility \(B=I_{2d}\) has collective and relative linear rates \((1+\rho)^{-1}\) and \((1-\rho)^{-1}\). Their ratio diverges as \(\rho\uparrow1\), so no common scalar clock change keeps both rates finite and nonzero. Its first-coordinate drift is
\[
L_{\Sigma_\rho,I}x_i
=\frac{x_i-\rho y_i}{1-\rho^2},
\tag{GN17}
\]
which also violates autonomous one-context reduction when \(\rho\ne0\). Second, complete conditional refresh is a different operator with a different degree spectrum. The [[general-causal-action/resolved-relative-boundary-and-two-clock-limits|resolved conditional-clock obstruction]] is not overturned by (GN16): covariance diffusion changes the processing rule rather than selecting a successful scalar rescaling of the old rule.

## State covariance, process selection and physical scope

Covariance is a tensor on linear observable cotangents. For the Gaussian location family \(N(m,\Sigma)\), its dual is the Fisher metric \(I_{\rm loc}=\Sigma^{-1}\) on mean displacements. Thus (GN5) is inverse-location-Fisher mobility in this precise sense; it is not an identification with the Fisher metric on covariance parameters, quantum BKM geometry, or an unspecified conditional Fisher tensor. The [[algebra/jordan-covariance-and-the-entropy-weighted-ball|Jordan covariance characterization]] similarly separates a selected co-metric from the symmetry condition fixing its reversible drift.

The diffusion restriction matters. For example, the state-preserving full refresh
\[
\mathcal R_\Sigma f=f-\int f\,d\mu_\Sigma
\tag{GN18}
\]
commutes with every linear readout and is natural under all invertible changes of coordinates. It gives every centered Hermite degree the same rate, rather than the degree ladder (GN9). Hence state and readout naturality do not uniquely select a process among all reversible Markov rules. Within the constant-mobility diffusion class they do select the covariance tensor, while the common rate remains free.

The demand on readouts is also stronger than [[general-causal-action/research-schema|a common whole/local construction]] with controlled defects or memory. It forces scalar drift on the entire first Hermite sector. For any two linear observations \(A,D\), the stationary time correlation is
\[
\mathbb E[(AX_t)(DX_0)^T]
=e^{-ct}A\Sigma D^T.
\tag{GN19}
\]
All spatial or contextual structure in this correlation sits in the static covariance; its temporal factor is common. More strongly, (GN4) removes hidden-mode memory from the full observable algebra of every linear readout. This is a discriminating hypothesis for this Gaussian family, not every notion of global/local compatibility and not a model of a general interacting interface with nontrivial retained memory. Nonlinear readouts are outside that autonomous-reduction assertion.

## All linear readouts being autonomous also restricts the state

The Gaussian hypothesis can itself be recovered from a strong autonomy requirement, provided the configuration dimension is at least two. Let \(d\ge2\), \(B>0\) be constant, and \(\rho=Z^{-1}e^{-U}>0\) be a normalizable smooth density on all of \(\mathbb R^d\). Its reversible differential expression is
\[
L=-B:\nabla^2+b(x)\cdot\nabla,\qquad b=B\nabla U.
\tag{GN20}
\]
Suppose for every nonzero linear functional \(a\), the drift \(a\cdot b(x)\) depends only on \(a\cdot x\). This is necessary for that readout to carry an autonomous diffusion, and is weaker than demanding its complete semigroup in advance. Then
\[
\boxed{b(x)=c(x-m),\qquad \rho=N(m,B/c),\qquad c>0.}
\tag{GN21}
\]

Indeed, differentiating the readout drift along every vector perpendicular to \(a\) gives \(a^T(Db)v=0\). Thus \((Db)^Ta\) is parallel to every \(a\); a linear map with every vector an eigenvector is scalar, so \(Db(x)=c(x)I\). The vanishing off-diagonal derivatives make each \(b_i\) depend only on \(x_i\). Equality of the diagonal derivatives for independently varying coordinates, using \(d\ge2\), forces their common value to be a constant \(c\). Hence \(b=cx+d_0\) and \(\nabla^2U=cB^{-1}\). Normalizability on the whole Euclidean space excludes \(c\le0\), and completing the square proves (GN21). In dimension one this argument does not apply: nonzero linear readouts are invertible and impose no Gaussian restriction.

Consequently extending all-readout autonomy unchanged would exclude the smooth non-Gaussian states of [[general-causal-action/interacting-comparison-refinement|the interacting refinement]]. A common whole/local law may instead retain their explicitly derived memory. This is a restriction of constant mobility and complete linear-readout autonomy, not a theorem excluding interacting theories with other readout or response structures.

## Distinct parents and the physical clock

There are separate constructive routes into this class. The [[algebra/partial-trace-clock-consistency-and-the-fluctuation-limit|purification fluctuation calculation]] derives the limiting differential expression \(G:\nabla^2-\xi\cdot\nabla\) with stationary covariance \(G\) from one supplied parent; the [[algebra/purification-response-normalization-and-the-full-clock-limit|full purification clock theorem]] proves the corresponding complete spectral convergence. The [[general-causal-action/gaussian-overlap-balancing-and-clock-sewing|Gaussian overlap balancing construction]] instead starts with finite-width comparisons: within its balanced Gaussian proximity family, exact composition under one scalar clock forces the proximity cometric to be proportional to the state covariance. That is an independent selecting condition on a declared kernel family, not a consequence of (GN4) or Gaussian shape alone.

The rule is local as a second-order differential operator on this finite configuration space. It need not be local in a physical spatial decomposition: a field covariance can connect variables assigned to distant spatial regions, and using it as mobility changes the physical Euclidean-gradient dynamics. In particular, choosing inverse precision as mobility removes the precision-dependent relaxation rates by construction; it does not establish a mass gap for the original Maxwell or Yang–Mills clock. Infinite-dimensional existence, physical locality, interacting observable recovery and calibration of \(c\) require their own constructions.

# Vacuum Boundary Gluing and the Wall-Response Operator

The most literal mathematical version of “crossing a wall and paying a residue cost” is Euclidean boundary reduction. A restriction map sends bulk histories to their boundary data; integrating over each fiber produces a half-space amplitude; gluing two halves multiplies those amplitudes and integrates over the boundary; and infinite Euclidean depth prepares the vacuum density \(\psi_0^2\). Under explicit reflection-Markov and separator hypotheses, conditional expectation onto a reflection-fixed separator factors the Osterwalder--Schrader form exactly: after quotienting its null subspace, the reconstructed carrier embeds isometrically—and, with dense interface insertions, unitarily—into the gauge-invariant interface \(L^2\) space. A closable invariant interface derivative then supplies a complex-linear, phase-sensitive analysis operator; it is complete only if its kernel is proved to contain nothing beyond the constant line. Identifying a thick interface with the canonical transfer slice and its electric-flux calculus requires another geometric map. In the Gaussian member, the logarithmic residue is governed by a Dirichlet-to-Neumann operator whose positive lower edge is precisely the oscillator or field mass gap after the kinetic unit is restored. The first genuinely open Yang--Mills estimate is therefore a volume-, depth-, and boundary-uniform cylinder Poincare bound together with an independently proved comparison to the transfer or Kogut--Susskind form along the asymptotically free trajectory. None of these statements identifies the mass gap with wave-function collapse.

**Status: [EXACT ABSTRACT GLUING THEOREM; EXACT GAUSSIAN DIRICHLET-TO-NEUMANN MODEL; STANDARD FINITE-LATTICE TRANSFER INPUT; OPEN INTERACTING YANG--MILLS BOUNDARY ESTIMATE].** The fiber integration, transfer limit, Gaussian boundary action, and Poincare calculation below are exact under their stated hypotheses. The required nonlinear boundary-response bound for four-dimensional Yang--Mills is a proposed theorem target, not a result.

## The reversal

The usual question asks what dynamical mechanism gives a nominally massless field a mass. The boundary-first reversal asks instead:

> After all unobserved Euclidean depth has been eliminated, what operator sends a variation of boundary configuration to the conjugate flux required to extend it into the bulk, and is that response uniformly bounded away from zero on physical directions?

The operator does not act on “reality,” “possibilities,” or bare numbers. Classically it acts on tangent variations of boundary data and returns normal flux. After quantization, the logarithmic boundary action determines a boundary measure; a separately declared flux calculus and metric determine a weighted form on that measure. Only after the physical energy form is identified with or compared to this coordinate form does its lower bound acquire energy meaning.

This is the same carrier-first discipline as [[carrier-first-reversal]], but it supplies a concrete candidate source for the interacting vacuum measure used in [[gauge-descent-flux-fisher-coercivity]].

## The wall is a restriction map with fibers

Let a Euclidean region be split along a codimension-one interface,

$$
M=M_-\cup_\Sigma M_+.
$$

Write \(\mathcal H(M_-)\) for an appropriate space, groupoid, or stack of bulk histories on the negative side and \(\mathcal C(\Sigma)\) for boundary configurations. Restriction is a typed map

$$
r_-:\mathcal H(M_-)\longrightarrow\mathcal C(\Sigma).
$$

At a finite regulator, assume a disintegration of the history measure along \(r_-\) and an action/measure factorization compatible with cutting. For \(\varphi\in\mathcal C(\Sigma)\), the fiber \(r_-^{-1}(\varphi)\) then consists of all negative-side histories with that boundary value, and integration over it gives the boundary amplitude

$$
Z_-[\varphi]
:=
\int_{r_-^{-1}(\varphi)}
e^{-S_E[\Phi]/\hbar}\,\mathcal D\Phi.
$$

There is a corresponding \(Z_+[\varphi]\). In a complex theory the gluing law is the appropriate dual pairing,

$$
\boxed{
Z[M_-\cup_\Sigma M_+]
=
\int_{\mathcal C(\Sigma)}
\overline{Z_-[\varphi]}Z_+[\varphi]\,\mathrm d\mu_\Sigma(\varphi).
}
$$

For the real nonnegative reflection-symmetric bosonic amplitudes used below, the bar makes no numerical difference. This answers “what is forgotten” without metaphor. The complete interior history is eliminated by integration along the fiber of \(r_\pm\); what remains is a function of boundary data. Nothing here selects one realized outcome. Histories in a fiber are summed, not collapsed into one of their members.

When the product is nonnegative, the normalized time-zero marginal is

$$
\boxed{
\mathrm d\nu_\Sigma(\varphi)
=
\frac{\overline{Z_-[\varphi]}Z_+[\varphi]}
{\int\overline{Z_-}Z_+\,\mathrm d\mu_\Sigma}
\,\mathrm d\mu_\Sigma(\varphi).
}
$$

The preceding integral is its scalar normalization, not the marginal itself.

For gauge theory the displayed spaces are not generally honest manifolds. Boundary fields have stabilizers, and gluing includes residual gauge symmetry and Gauss matching. A groupoid or stack formulation requires homotopy fibers, automorphism weights or gauge-volume data, and an actual measure/disintegration theorem. Gauge-fixed representatives may present the same structure only after their equivalence to the gauge-invariant amplitude is proved. A [[basic-concepts/torsors/inq|torsor]] by itself does not forget information: it retains exact relative differences while lacking a preferred origin. Genuine forgetting belongs to the many-to-one restriction or marginalization map, not to torsorhood as such.

## Seven maps that must not be called one descent

| Map | Input and output | What can be lost or selected |
|---|---|---|
| boundary restriction \(r\) | bulk history \(\to\) boundary configuration | interior detail is absent from the output; fibers collect compatible interiors |
| fiber integration \(r_!\) | bulk weight \(\to\) boundary amplitude | histories are marginalized; the result is still an amplitude over all boundary data |
| gluing pairing | two boundary amplitudes \(\to\) a partition function or boundary state | no individual outcome is selected |
| transfer semigroup \(T^N\) | boundary-slice functions \(\to\) boundary-slice functions | finite depth can be injective; normalized infinite depth can converge to the vacuum projection |
| conditional expectation \(E:\mathcal M\to\mathcal N\) | ambient observables \(\to\) an accessible subalgebra | components in \(\ker E\) become operationally inaccessible; no outcome is thereby obtained |
| OS quotient | positive-time functionals \(\to\) physical Hilbert vectors | null directions of the reflection-positive form are identified |
| measurement instrument | state \(\to\) outcome-labelled conditional states | a declared readout has discrete alternatives; factive realization additionally requires an obtained value or actuality rule and a stable record |

Strict [[basic-concepts/descent/inq|descent]] can instead be an equivalence that reconstructs a global object from compatible local objects. It need not forget anything. The phrase “descent residue” is therefore useful only after one of these nonfaithful arrows and its carrier have been named.

## Exact transfer-gluing theorem

The boundary construction becomes elementary operator theory at a finite regulator. Let \((X,\mu)\) be a probability space and let

$$
T:L^2(X,\mu)\longrightarrow L^2(X,\mu)
$$

be compact and self-adjoint, spectrally positive \(T\geq0\), injective \(\ker T=0\), and order-positivity improving. Spectral positivity makes the logarithm below real; order positivity maps the positive cone into itself and supplies Perron--Frobenius control. Let \(\lambda_0>0\) be the largest eigenvalue and \(\psi_0>0\) its normalized eigenfunction. Positivity improvement and compactness make the top eigenspace simple. Define

$$
\widehat T:=\lambda_0^{-1}T,
\qquad
P_0:=|\psi_0\rangle\langle\psi_0|.
$$

For nonnegative boundary vectors \(b_\pm\in L^2(X,\mu)\) with

$$
c_\pm:=\langle\psi_0,b_\pm\rangle>0,
$$

set

$$
F_{\pm,N}:=\widehat T^N b_\pm,
\qquad
\mathrm d\nu_N
:=
\frac{F_{-,N}F_{+,N}}{\int_XF_{-,N}F_{+,N}\,\mathrm d\mu}
\,\mathrm d\mu.
$$

Then

$$
\widehat T^N\longrightarrow P_0
\quad\text{in operator norm},
$$

and consequently

$$
\boxed{
\nu_N\longrightarrow\nu_0,
\qquad
\mathrm d\nu_0=\psi_0^2\,\mathrm d\mu,
}
$$

in total variation.

Indeed, compactness and simplicity of the top eigenvalue give

$$
\left\|\widehat T^N-P_0\right\|
\leq r^N,
\qquad
r:=\left\|\widehat T(1-P_0)\right\|<1.
$$

Thus \(F_{\pm,N}\to c_\pm\psi_0\) in \(L^2\). The product converges in \(L^1\) because

$$
\|fg-f'g'\|_1
\leq
\|f-f'\|_2\|g\|_2
+
\|f'\|_2\|g-g'\|_2,
$$

and normalization gives total-variation convergence.

Suppose some fixed power \(T^m\) is trace class. Then, for all sufficiently large \(N\), a separate periodic-cylinder marginal is

$$
\nu_N^{\mathrm{per}}(A)
=
\frac{\operatorname{Tr}\!\left(M_{\mathbf1_A}T^{2N}\right)}
{\operatorname{Tr}(T^{2N})}
\longrightarrow
\langle\psi_0,M_{\mathbf1_A}\psi_0\rangle.
$$

If \(T^{2N}\) has a suitably regular diagonal kernel—for example, a continuous kernel on compact \(X\)—then

$$
\mathrm d\nu_N^{\mathrm{per}}(x)
=
\frac{K_{2N}(x,x)}{\operatorname{Tr}(T^{2N})}
\,\mathrm d\mu(x).
$$

On a gauge-invariant carrier, multiplication observables and measurable sets in this formula are understood on the quotient, or with the gauge projection inserted.

The standard-library [[contemporary-puzzles/yang-mills-mass-gap/receipts/vacuum_boundary_gluing_receipt.py|finite-state receipt]] checks an invertible positive transfer matrix, convergence of reflected sewing and the periodic marginal to \(\psi_0^2\), and reversibility of the vacuum Doob transform. Its stored output is [[contemporary-puzzles/yang-mills-mass-gap/receipts/vacuum-boundary-gluing-receipt-output.txt|recorded beside it]].

### Where exact forgetting enters

This theorem separates three notions that are easily conflated.

- At each finite depth, a strictly positive transfer operator can be injective. Its inverse is usually unbounded, but there need be no algebraic kernel and hence no exact loss of a Hilbert-space component.
- Integrating bulk histories over \(r^{-1}(\varphi)\) is genuinely many-to-one at the history level.
- Infinite normalized depth has the rank-one limit \(P_0\). It forgets every component orthogonal to \(\psi_0\). The convergence rate is \(r^N\), and

Writing \(a_\tau\) for Euclidean temporal **length** and \(\delta\tau=a_\tau/c\) for clock duration,

$$
-\frac{\hbar c}{a_\tau}\log r
$$

is the finite-regulator energy gap when \(T=e^{-a_\tau H/(\hbar c)}=e^{-\delta\tau H/\hbar}\).

In infinite volume compactness is lost. A unique ground vector can still give strong convergence \(e^{-\tau(H-E_0)/\hbar}\to P_0\) as \(\tau\to\infty\) without norm convergence. If positive spectrum accumulates at zero, then

$$
\left\|e^{-\tau(H-E_0)/\hbar}-P_0\right\|=1
$$

for every finite \(\tau>0\). Operator-norm convergence is equivalent to a positive gap and is then exponential. Vacuum preparation and gap positivity are therefore related but not identical.

### The temporal conditional law

The vacuum also converts transfer into an exact stationary Markov operator:

$$
(Pf)(x)
:=
\frac{T(\psi_0f)(x)}
{\lambda_0\psi_0(x)}.
$$

If \(T\) has symmetric kernel \(K(x,y)\), then

$$
P(x,\mathrm dy)
=
\frac{K(x,y)\psi_0(y)}
{\lambda_0\psi_0(x)}
\,\mathrm d\mu(y)
$$

is reversible for \(\nu_0=\psi_0^2\mu\), since

$$
\nu_0(\mathrm dx)P(x,\mathrm dy)
=
\frac{\psi_0(x)K(x,y)\psi_0(y)}{\lambda_0}
\,\mathrm d\mu(x)\mathrm d\mu(y).
$$

This Doob transform operates on functions of one boundary slice and gives their conditional transport to the next slice. Its contraction coefficient on centered functions is \(r\), so \(1-r\) is the discrete-time relaxation gap; the physical energy gap is the logarithmic rate \(-\hbar c a_\tau^{-1}\log r=-\hbar\delta\tau^{-1}\log r\). It is a temporal conditional law, not a measurement instrument and not a spatial Dobrushin specification.

## The logarithmic residue is a boundary potential

Whenever \(\psi_0>0\), the glued vacuum measure has logarithmic density

$$
\mathrm d\nu_0=e^{-W}\,\mathrm d\mu,
\qquad
\boxed{W:=-2\log\psi_0+\text{constant}.}
$$

For real strictly positive unequal halves one has \(W=W_-+W_+\), where \(W_\pm=-\log Z_\pm\) after normalization. In a complex theory the logarithm of a product amplitude is not automatically a real probability potential. This additive logarithm, when defined, is a precise candidate for a gluing residue: the negative log Radon--Nikodym density, modulo constants. Calling it a boundary *effective action* is conventional. It is dimensionless and need not be positive. It is not yet an energy, a cohomology class, an entropy loss, or a factive record; only an independently constructed Hessian or form estimate can supply a positive cost.

The negative log-density \(W\) alone does not determine a carré du champ. After independently choosing a boundary metric or flux derivatives, define the coordinate form

$$
\mathcal E_W(f,f)
=
\int_X|\nabla f|^2e^{-W}\,\mathrm d\mu.
$$

Its optimal Poincare constant is

$$
\lambda_W
:=
\inf_{\int f\,\mathrm d\nu_0=0}
\frac{\mathcal E_W(f,f)}{\|f\|_{L^2(\nu_0)}^2}.
$$

Let

$$
\widetilde h[f]
:=
\langle\psi_0f,(H-E_0)\psi_0f\rangle.
$$

Only if a ground-state-transform theorem identifies

$$
\widetilde h[f]=\kappa\mathcal E_W(f,f)
$$

does the min--max principle give

$$
\Delta_E=\kappa\lambda_W.
$$

More generally, \(\widetilde h\geq\kappa c_{\mathrm{form}}\mathcal E_W\) gives only

$$
\Delta_E\geq\kappa c_{\mathrm{form}}\lambda_W.
$$

[[gauge-descent-flux-fisher-coercivity]] proves the equality for the canonical finite Kogut--Susskind flux form. Gluing derives the vacuum weight entering that theorem; it does not derive the flux calculus or the energy-form identity.

## Flux matching is first variation; response is second variation

For a classical local action evaluated on the bulk solution with boundary value \(\varphi\), its first variation is a boundary pairing,

$$
\delta S_-^{\mathrm{on}}[\varphi]
=
\langle\Pi_-(\varphi),\delta\varphi\rangle_\Sigma.
$$

Here

$$
\Pi_-(\varphi)
:=
\frac{\delta S_-^{\mathrm{on}}}{\delta\varphi}
$$

is the conjugate outward normal flux. Varying the glued action gives

$$
\delta\!\left(S_-^{\mathrm{on}}+S_+^{\mathrm{on}}\right)
=
\langle\Pi_-+\Pi_+,\delta\varphi\rangle_\Sigma,
$$

so stationarity of the classically glued action gives the matching condition

$$
\boxed{\Pi_-+\Pi_+=0.}
$$

The sign comes from the opposite boundary orientations. This is a variational flux-matching condition. It is not yet a Noether conservation law: that additionally requires a common continuous symmetry, invariant action or symplectic dynamics, normalized generator, and boundary control. Its linearization,

$$
\mathcal N_-
:=
\frac{\delta\Pi_-}{\delta\varphi}
=
\frac{\delta^2S_-^{\mathrm{on}}}{\delta\varphi^2},
$$

is the boundary-response operator. Its Hessian need not be positive in a general interacting problem; positivity or a lower bound is a theorem to prove. Thus flux and coercive cost are adjacent but differently typed: flux is a signed first variation, while response is a quadratic second variation that may or may not be coercive. This is exactly the distinction already required by [[conservation-of-causal-charge/causal-individuation-balance|causal-individuation balance]].

For gauge theory, Gauss law and boundary gauge transformations organize the allowed flux sectors. Gluing must match those sectors before integrating over boundary fields. If a proposed causal symmetry and common moment map are independently constructed, these boundary fluxes give it a mathematically serious place to enter. They do not make the charge equal to \(W\), its Hessian, or the mass gap.

## Exact Gaussian model: the response is a square root

Let \(q\in\mathbb R^n\), let \(\Omega\) be a positive symmetric matrix, and consider

$$
H
=
\frac12\left(-\hbar^2\Delta_q+q^{\mathsf T}\Omega^2q\right).
$$

Its normalized ground state and glued boundary measure are

$$
\psi_0(q)
\propto
\exp\!\left[-\frac{1}{2\hbar}q^{\mathsf T}\Omega q\right],
$$

$$
\mathrm d\nu_0(q)
\propto
\exp\!\left[-\frac{1}{\hbar}q^{\mathsf T}\Omega q\right]\mathrm dq.
$$

Writing \(\omega_{\min}=\min\sigma(\Omega)\), the sharp Gaussian Poincare constant for the unscaled gradient is

$$
\lambda_W
=
\frac{2\omega_{\min}}{\hbar}.
$$

The kinetic coefficient is \(\kappa=\hbar^2/2\), so

$$
\boxed{
\kappa\lambda_W
=
\hbar\omega_{\min},
}
$$

which is exactly the first excitation gap.

Now derive the same operator from Euclidean geometry. On the half-line \(\tau\leq0\), fix \(q(0)=\varphi\) and minimize

$$
S_-[q]
=
\frac12\int_{-\infty}^{0}
\left(|\dot q|^2+q^{\mathsf T}\Omega^2q\right)\mathrm d\tau.
$$

The decaying solution is

$$
q_{\mathrm{cl}}(\tau)=e^{\Omega\tau}\varphi.
$$

Its outward normal derivative and on-shell action are

$$
\partial_nq_{\mathrm{cl}}|_\Sigma=\Omega\varphi,
\qquad
S_-[q_{\mathrm{cl}}]
=
\frac12\varphi^{\mathsf T}\Omega\varphi.
$$

Thus

$$
\boxed{
\mathcal N_-=\Omega
}
$$

is the Dirichlet-to-Neumann operator: it sends boundary displacement to the normal flux needed to extend that displacement through the half-space. The positive half supplies a second copy. Therefore

$$
W(\varphi)
=
\frac{2S_-[q_{\mathrm{cl}}]}{\hbar}
=
\frac{1}{\hbar}\varphi^{\mathsf T}\Omega\varphi,
\qquad
\operatorname{Hess}W=\frac{2\Omega}{\hbar}.
$$

In this model the following are calibrated appearances of the same underlying eigenmode and frequency \(\omega_{\min}\) in three registers:

| Register | Operator or form | Lower edge |
|---|---|---|
| Euclidean boundary geometry | Dirichlet-to-Neumann map \(\Omega\) | \(\omega_{\min}\) |
| dimensionless boundary probability | \(\operatorname{Hess}W=2\Omega/\hbar\) | \(2\omega_{\min}/\hbar\) |
| physical time evolution | \((H-E_0)|_{\psi_0^\perp}\) | \(\hbar\omega_{\min}\) |

The equations relate these concepts; they do not identify them. Energy is the generator dual to time translation, the boundary response is normal flux per boundary displacement, and \(W\) is a logarithmic density. The constants carry one register into another.

## Free fields expose both the clue and the obstruction

For a free scalar field, take \(c=1\) and let \(m\) denote an inverse-length or angular-frequency spectral parameter, so the rest-energy gap is \(\hbar m\). Set

$$
A=-\Delta_x+m^2,
\qquad
\Omega=A^{1/2}=\sqrt{-\Delta_x+m^2}.
$$

This is the same extension principle formalized for fractional Laplacians by [[library/an-extension-problem-related-to-the-fractional-laplacian/inq|Caffarelli--Silvestre]]: a local equation in one more dimension induces a nonlocal Dirichlet-to-Neumann operator on its boundary.

Eliminating a Euclidean half-space produces

$$
\psi_0[\varphi]
\propto
\exp\!\left[-\frac{1}{2\hbar}
\langle\varphi,\Omega\varphi\rangle\right].
$$

In spatial Fourier variables the wall-response symbol is

$$
\Omega(k)=\sqrt{|k|^2+m^2}.
$$

Hence

$$
\inf_k\Omega(k)=m>0
$$

for a massive field, whereas the massless symbol \(|k|\) approaches zero in infinite volume. With periodic or Neumann conditions, the finite box still contains the \(k=0\) mode and the massless vacuum Gaussian is nonnormalizable along it. A finite-size lower edge of order \(L^{-1}\) occurs only with boundary conditions such as Dirichlet, or after the zero mode is explicitly removed or conditioned. In either case it vanishes as the box grows. This is exactly why the Yang--Mills estimate must be uniform in volume.

The boundary action is spatially nonlocal even though the bulk action is local: a square root of an elliptic operator is pseudodifferential. Nonlocality of \(W\) is therefore not itself pathological. But it blocks an easy Dobrushin proof. Integrating out arbitrarily deep bulk degrees of freedom generically induces long-range boundary interactions; assuming their exponential decay would risk assuming the very bulk gap being proved.

The finite-dimensional differentiation rule makes the source of this nonlocality explicit. If boundary variables are \(x\), hidden bulk variables are \(y\), and

$$
W_B(x)
=
-\log\int e^{-S(x,y)}\,\mathrm dy,
$$

then, whenever differentiation under the integral is justified,

$$
\partial_i\partial_jW_B
=
\mathbb E_x[\partial_i\partial_jS]
-
\operatorname{Cov}_x(\partial_iS,\partial_jS).
$$

The covariance term couples boundary directions through all hidden bulk fluctuations. For a quadratic kernel split into boundary and interior blocks, the exact effective Hessian is the Schur complement

$$
K_{\mathrm{eff}}
=
K_{BB}-K_{BI}K_{II}^{-1}K_{IB}.
$$

Even sparse \(K\) generally has dense \(K_{II}^{-1}\). A local bulk action therefore does not imply a local boundary potential.

### The nonlinear residue has a fixed sign

The preceding identity gives an exact meaning to the cost of forgetting, but it also prevents a misleading conclusion. Let \(B\) be the retained boundary manifold, let \(F\) be a closed hidden-fibre manifold, take \(\beta>0\), and use a fixed Riemannian product \(B\times F\) whose fibre metric and volume are independent of \(x\). Put

$$
Z_\beta(x)
:=
\int_F e^{-\beta V(x,y)}\,\mathrm d\operatorname{vol}_F(y),
\qquad
A_\beta(x)
:=
-\frac1\beta\log Z_\beta(x).
\tag{VB24a}
$$

Assume \(V\in C^2(B\times F)\), \(Z_\beta>0\), and sufficient domination to differentiate twice under the integral. For a genuinely varying fibre metric, horizontal-connection, fibre-volume, and mean-curvature terms must be added. With

$$
\mathrm d\mu_x(y)
:=
Z_\beta(x)^{-1}e^{-\beta V(x,y)}
\,\mathrm d\operatorname{vol}_F(y),
\tag{VB24b}
$$

one obtains, for \(u,v\in T_xB\),

$$
\boxed{
\nabla_B^2A_\beta(u,v)
=
\mathbb E_{\mu_x}
\!\left[\nabla_{BB}^2V(u,v)\right]
-
\beta\operatorname{Cov}_{\mu_x}
\!\left(\mathrm d_BV(u),\mathrm d_BV(v)\right).}
\tag{VB24c}
$$

The covariance is positive semidefinite. Marginalization therefore never adds pointwise curvature beyond the conditional mean visible Hessian. It can discard globally soft directions and thereby leave a better retained spectral constant, but every hidden direction coupled to the retained score subtracts from the local effective stiffness. This is the potential-theoretic analogue of “observed information = complete information minus missing information.”

Suppose more quantitatively that every conditional law \(\mu_x\) obeys the fibre Poincare inequality

$$
\operatorname{Var}_{\mu_x}(h)
\leq
\lambda_x^{-1}
\int_F\lvert\nabla_Fh\rvert^2\,\mathrm d\mu_x.
\tag{VB24d}
$$

Then (VB24c), applied to \(h=\mathrm d_BV(u)\), gives

$$
\boxed{
\nabla_B^2A_\beta(u,u)
\geq
\mathbb E_{\mu_x}
\!\left[
\nabla_{BB}^2V(u,u)
-
\frac{\beta}{\lambda_x}
\left\lvert\nabla_F\!\left(\mathrm d_BV(u)\right)\right\rvert^2
\right].}
\tag{VB24e}
$$

Thus the nonlinear descent obstruction is not “information was lost” by itself. It is the product of hidden susceptibility \(\lambda_x^{-1}\) and the mixed derivative that tells how strongly a retained variation moves the hidden conditional law.

When the fibre Bakry--Emery tensor

$$
\mathcal R_x
:=
\operatorname{Ric}_F
+\beta\nabla_{FF}^2V(x,\cdot)
\tag{VB24f}
$$

is positive definite, the Riemannian Brascamp--Lieb inequality sharpens (VB24e) to

$$
\nabla_B^2A_\beta(u,u)
\geq
\mathbb E_{\mu_x}
\!\left[
\nabla_{BB}^2V(u,u)
-
\beta
\left\langle
\mathcal R_x^{-1}
\nabla_F\!\left(\mathrm d_BV(u)\right),
\nabla_F\!\left(\mathrm d_BV(u)\right)
\right\rangle
\right],
\tag{VB24g}
$$

with the displayed convention that \(\mathcal R_x\) includes the factor \(\beta\) in its Hessian term. In a flat Euclidean fibre, if

$$
\nabla^2V
=
\begin{pmatrix}
A&M\\
M^{\mathsf T}&D
\end{pmatrix},
\qquad D\succ0,
\tag{VB24h}
$$

the equivalent cancellation of the \(\beta\) factors gives the clean shorting bound

$$
\boxed{
\nabla^2A_\beta
\succeq
\mathbb E_{\mu_x}
\!\left[A-MD^{-1}M^{\mathsf T}\right].}
\tag{VB24i}
$$

For a Gaussian action this is equality and recovers \(K_{BB}-K_{BI}K_{II}^{-1}K_{IB}\). For a nonlinear action it is a sufficient lower estimate: visible curvature must dominate the susceptibility-weighted hidden coupling.

There is also an exact nonlinear Schur expression, but its hidden block is a Witten operator rather than the pointwise matrix \(D\). Put \(S=\beta V\), \(W=\beta A_\beta\), and

$$
\mathcal K_x^{\mathrm{ex}}
:=
\overline{\operatorname{Ran}\mathrm d_F}
\subset L^2(T^*F,\mu_x).
\tag{VB24ia}
$$

For \(u\in T_xB\), define the conditional hidden score one-form

$$
\mathcal B_xu
:=
\mathrm d_F\!\left(\mathrm d_BS(u)\right)
\in\mathcal K_x^{\mathrm{ex}},
\tag{VB24ib}
$$

and let \(C_x\) be the conditional one-form Witten operator restricted to that exact-form subspace,

$$
C_x
=
\left(
\mathrm d_F\mathrm d_{\mu_x}^*
+\mathrm d_{\mu_x}^*\mathrm d_F
\right)\big|_{\mathcal K_x^{\mathrm{ex}}}
=
\nabla_{\mu_x}^*\nabla
+\operatorname{Ric}_F
+\nabla_{FF}^2S.
\tag{VB24ic}
$$

Under the standard self-adjointness, domain, conditional Poincare, and closed-range hypotheses, the Helffer--Sjostrand covariance identity gives

$$
\operatorname{Cov}_{\mu_x}
\!\left(\mathrm d_BS(u),\mathrm d_BS(v)\right)
=
\left\langle
\mathcal B_xu,C_x^{-1}\mathcal B_xv
\right\rangle_{L^2(T^*F,\mu_x)}.
\tag{VB24id}
$$

Consequently,

$$
\boxed{
(\operatorname{Ric}_B+\nabla_B^2W)_x(u,v)
=
\operatorname{Ric}_B(u,v)
+\mathbb E_{\mu_x}[\nabla_{BB}^2S(u,v)]
-
\left\langle
\mathcal B_xu,C_x^{-1}\mathcal B_xv
\right\rangle.}
\tag{VB24ie}
$$

This is the genuine nonlinear Schur expression. The inverse operates on conditional hidden score one-forms; the resulting form operates on retained boundary tangents; its curvature consequence governs functions in \(L^2(\bar\mu)\). None of those carriers is automatically the OS or Kogut--Susskind Hilbert carrier. In the constant quadratic Gaussian, \(C_x^{-1}\) reduces on linear scores to the inverse hidden Hessian and (VB24ie) becomes the ordinary matrix Schur complement. Outside that case, the effective Hessian is not generally the Anderson--Trapp short of a pointwise Hessian matrix.

To call it an operator short in the Anderson--Trapp sense requires the additional positivity and form-domain hypotheses for

$$
\mathbb A_x
=
\begin{pmatrix}
G_x^\sharp&\mathcal B_x^*\\
\mathcal B_x&C_x
\end{pmatrix}
\geq0,
\qquad
G_x(u,v)
=
\operatorname{Ric}_B(u,v)
+\mathbb E_{\mu_x}[\nabla_{BB}^2S(u,v)].
\tag{VB24if}
$$

Without this block positivity, (VB24ie) remains an exact covariance/Schur formula but is not a positive operator short.

The primary mathematical precedents are [Brascamp--Lieb's covariance inequality](https://doi.org/10.1016/0022-1236(76)90004-5), the [Helffer--Sjostrand inverse-Witten covariance formula](https://doi.org/10.1007/BF02186817), and the [Riemannian weighted-curvature extension](https://arxiv.org/abs/1310.2526). Their hypotheses are part of the statement; none licenses an inverse of a gauge-degenerate pointwise Hessian on a stratified quotient.

The corresponding sufficient boundary-gap criterion is tensorial. The marginal measure

$$
\mathrm d\bar\mu(x)
\propto
e^{-\beta A_\beta(x)}\,\mathrm d\operatorname{vol}_B(x)
\tag{VB24j}
$$

has Bakry--Emery tensor

$$
\operatorname{Ric}_B
+\beta\mathbb E_{\mu_x}[\nabla^2_{BB}V]
-\beta^2\operatorname{Cov}_{\mu_x}(\mathrm d_BV).
\tag{VB24k}
$$

If \(B\) is closed and (VB24d) together with the corresponding mixed-derivative estimate makes this tensor at least \(\rho g_B\) everywhere for some \(\rho>0\), the Bakry--Emery criterion gives \(\lambda_{\mathrm P}(\bar\mu)\geq\rho\). With boundary, the corresponding Neumann/convex-boundary hypotheses are required. This is a valid whole-to-boundary stopping condition, not a necessary characterization.

There is a decisive compact-group firewall. No smooth function on a closed connected Riemannian manifold can satisfy \(\nabla^2W\succeq\kappa g\) globally for \(\kappa>0\): tracing and integrating would give \(0=\int\Delta W\geq\kappa\dim(B)\operatorname{vol}(B)>0\). Therefore no proof on \(SU(3)^E\) can rest on a globally positive Hessian of a smooth Wilson or effective boundary potential. Exponential coordinates do not evade the topology, and the gauge quotient is generally stratified. The global objects that remain viable are \(\operatorname{Ric}+\operatorname{Hess}W\), conditional or global Poincare and logarithmic-Sobolev inequalities, or block-influence estimates formulated upstairs on \(SU(3)^E\) and then restricted to gauge-invariant functions.

This also explains why the direct marginal-inheritance theorem below is stronger than the Hessian diagnostic on the compact lattice carrier. If the full Euclidean measure already has a uniform Poincare inequality for the product carré du champ, its coordinate marginal inherits that bound by testing functions constant in the forgotten variables. No globally convex effective potential is needed. Equations (VB24c)--(VB24k) are most useful for diagnosing or constructing the bulk/conditional coercivity; they do not replace it.

## Concept ledger in the boundary construction

| Concept | Algebraic or geometric role here | What it is not |
|---|---|---|
| space | incidence and locality of boundary variables, together with the spatial operator inside the bulk extension problem; a configuration metric may be induced by the flux form | a container through which already-individuated things move |
| time | the composition parameter of transfer kernels; Lorentzian time is the positive-energy one-parameter group recovered after OS reconstruction | identical to energy merely because \(a_\tau H/(\hbar c)=\delta\tau H/\hbar\) is dimensionless |
| energy | the self-adjoint generator of transfer composition and its quadratic form on the physical carrier | a synonym for mass or information |
| mass gap | the positive lower edge of that generator above the vacuum; in the Gaussian member it is equivalently a calibrated lower edge of boundary response | a finite outcome set, a spacetime pixel, or a gauge-field mass term |
| causality | the admissible composition, reflection, locality, and later Lorentzian commutation structure that makes boundary preparations compatible | observation itself, an entropy number, or a selected detector result |

This ledger makes the reversal exact without turning equations of dimensions into equations of concepts. The dimensionless exponent \(a_\tau H/(\hbar c)=\delta\tau H/\hbar\) relates a temporal interval and an energy generator. It does not say that time *is* energy. Likewise, \(\Omega=\sqrt{-\Delta+m^2}\) relates spatial extension to boundary response. It does not say that mass *is* spatial curvature in every geometric register.

## What this says about “here and now”

A wall \(\Sigma\) is a chosen Euclidean interface, not a realized event or a factive “now.” It declares boundary data and separates two Euclidean depths. The half-space construction then answers a structural question that may later serve as an analogue of “here and now”: which boundary variations extend into the bulk at what response cost?

The vacuum itself remains translation invariant when the theory is. It does not select one spacetime point or one detector result. Thus three distinct structures must remain separate:

1. **Pointing gap:** an unpointed object or torsor acquires a distinguished point. This is a change of type, not a positive real number.
2. **Information defect:** a nonfaithful channel or conditional expectation removes accessible distinctions; relative entropy can quantify this under declared state and algebra hypotheses.
3. **Spectral gap:** a positive generator obeys \(H\geq\Delta_E(1-P_0)\). This is an energetic coercivity inequality.

Outcome discreteness is a fourth fact about the target readout algebra, not a numerical distance between alternatives. These structures can participate in one architecture only through explicit maps. A finite outcome set does not force a spectral gap: a detector with two outcomes can be coupled to a massless field. Conversely, a massive free field has a spectral gap before anyone measures it.

For photon polarization, a fixed analyzer defines two orthogonal output channels. A state supplies probabilities for those channels; it is not a classical continuum of pre-existing polarities that the glass literally rounds to one of two real numbers. Bell inequalities constrain possible joint probability models for separated measurements. They do not turn outcome discreteness into an energy gap.

More exactly, a finite POVM \((E_i)_{i=1}^n\) gives the affine map

$$
\omega
\longmapsto
p(\omega):=(\omega(E_1),\ldots,\omega(E_n))
\in\Delta_{n-1}.
$$

An instrument additionally gives conditional states \(\omega_i\). A realized readout is a character \(\delta_i\) of the finite commutative algebra \(\mathbb C^n\). Thus the mathematical passage is not “phase space to a finite set of real numbers” but

$$
\text{noncommutative state }\omega
\longrightarrow
\bigl((p_i,\omega_i)\bigr)_{i=1}^n
\longrightarrow
\text{obtained character }\delta_i
\longrightarrow
\text{stable record}.
$$

The instrument fixes the first arrow, including its probability-simplex marginal. It does not by itself add an actuality rule for the second arrow. None of these types contains an energy unit.

[[physical-distinction-coercivity]] separates projections, instruments, state changes, and physical energy coercivity. The quantitative frame theorem is owned by [[causal-frame-coercivity]]: if outcome- or wall-derived distinction maps \(D_\alpha\) detect every centered physical direction,

$$
\sum_\alpha\|D_\alpha\xi\|^2
\geq
\kappa_{\mathrm{fr}}\|\xi\|^2,
$$

and the physical energy form pays for those same distinctions,

$$
h[\xi]
\geq
\eta_{\mathrm{sol}}E_*
\sum_\alpha\|D_\alpha\xi\|^2,
$$

then \(\Delta_E\geq\kappa_{\mathrm{fr}}\eta_{\mathrm{sol}}E_*\). The wall construction above is valuable because it may construct the \(D_\alpha\), their vacuum state, and their response form. It does not make either inequality automatic.

There is also a codimension firewall. The present sewing surface is a codimension-one Euclidean time slice. The programme's causal-wall constructions often use codimension-two Lorentzian cuts. Analytic continuation alone preserves codimension. Their identification therefore requires an additional corner, intersection, thickening, or carrier-changing functor, together with the OS continuation; vocabulary does not supply it.

## The OS quotient factors exactly through a reflection interface

The first reconstructed-to-wall map need not remain abstract at finite regulator. Let \(\mu_\rho\) be a normalized reflection-invariant Euclidean lattice probability measure, let \(\vartheta\) reverse Euclidean time, and let

$$
(\Theta F)(\Phi)
:=
\overline{F(\vartheta\Phi)}
$$

act on the gauge-invariant positive-side cylinder functions \(\mathcal A_{\rho,+}^{\mathrm{GI}}\). Their reflection/OS sesquilinear form is

$$
\langle F,G\rangle_{\mathrm{OS}}
:=
\int(\Theta F)G\,\mathrm d\mu_\rho.
\tag{OS1}
$$

Choose a reflection-invariant separator \(I\), with sigma-algebra \(\mathcal F_I\), so that every interaction crossing the reflection plane is carried by \(I\). On a periodic cylinder, \(I\) must contain every cut needed to separate the two reflected regions, generally including both fixed cuts. For the untwisted \(L^2\) factorization below, assume additionally that reflection fixes the interface variables pointwise after the residual gauge quotient. If reflection induces a nontrivial involution on \(I\), (OS3) instead contains that involution and the ordinary \(L^2\) conclusion requires a further positive factorization. Assume the **reflection-Markov property**: conditioned on \(\mathcal F_I\), the strictly positive- and strictly negative-time variables are independent, with their conditional laws exchanged by reflection. Let

$$
b_\rho F
:=
\mathbb E_{\mu_\rho}[F\mid\mathcal F_I]
\tag{OS2}
$$

and let \(\nu_{\rho,I}\) be the interface marginal of \(\mu_\rho\). Conditional independence and reflection symmetry give the exact factorization, which in particular proves positivity of this form,

$$
\boxed{
\langle F,G\rangle_{\mathrm{OS}}
=
\int_I
\overline{b_\rho F}\,
b_\rho G\,
\mathrm d\nu_{\rho,I}.}
\tag{OS3}
$$

Consequently,

$$
\mathcal N_{\mathrm{OS}}
:=
\{F:\langle F,F\rangle_{\mathrm{OS}}=0\}
=
\ker b_\rho,
\tag{OS4}
$$

and \(b_\rho\) descends to an isometry

$$
B_\rho^{\mathrm{OS}}:
\overline{
\mathcal A_{\rho,+}^{\mathrm{GI}}/
\mathcal N_{\mathrm{OS}}
}
\longrightarrow
L^2(\nu_{\rho,I})^{\mathrm{GI}},
\qquad
B_\rho^{\mathrm{OS}}[F]=b_\rho F.
\tag{OS5}
$$

If gauge-invariant interface insertions belong to the positive-side class and are dense in \(L^2(\nu_{\rho,I})^{\mathrm{GI}}\), then \(b_\rho f=f\) for those insertions, the isometric range is both dense and closed, and \(B_\rho^{\mathrm{OS}}\) is unitary. Write \(\Omega_\rho:=[1]\) for the distinguished normalized OS reference vector and define

$$
P_{\Omega,\rho}:=|\Omega_\rho\rangle\langle\Omega_\rho|.
$$

Since \(B_\rho^{\mathrm{OS}}[1]=1\),

$$
J_{\Omega,\rho}
:=
B_\rho^{\mathrm{OS}}(1-P_{\Omega,\rho})
$$

has exact reference-complement coverage one:

$$
\|J_{\Omega,\rho}\Psi\|
=
\|(1-P_{\Omega,\rho})\Psi\|.
\tag{OS6}
$$

For a general reflection-Markov measure, \(\Omega_\rho\) is a distinguished reference vector, not yet a theorem about the complete zero-energy subspace. Only after the Euclidean state is identified with an infinite-depth vacuum state and that vacuum is proved unique may one rename \(P_{\Omega,\rho}\) as the physical vacuum projection \(P_{0,\rho}\).

This theorem identifies what the OS quotient forgets. Its null set is a seminorm-null linear subspace. For every bounded interface multiplier \(h\) that preserves the chosen positive-side domain, \(b_\rho(hF)=h\,b_\rho(F)\), so the null set is a module over that declared multiplier algebra; no closure under all of \(L^\infty(\mathcal F_I)\) has been assumed, and it is not thereby a two-sided algebra ideal. Gauge reduction is already built into the invariant function class and residual interface quotient. A naive one-slice interface is insufficient whenever the action contains couplings that cross it, and a thick interface is not automatically the canonical transfer slice.

The theorem also distinguishes a joint reflection interface from a one-slice marginal, and finite periodic preparation from the vacuum limit. For the kernel formulas, assume that the transfer operator is compact, nonnegative, and self-adjoint and that one of its positive integer powers is Hilbert--Schmidt, so every sufficiently deep \(T^{n_\tau}\) has an \(L^2\) kernel \(K_{n_\tau}\) and \(T^{2n_\tau}\) is trace class. In the simplest periodic geometry with two cuts carrying configurations \((U,V)\), the joint separator marginal has the form

$$
\mathrm d\nu_{\rho,I}^{(n_\tau)}(U,V)
=
\frac{|K_{n_\tau}(U,V)|^2}
{\|T^{n_\tau}\|_{\mathrm{HS}}^2}
\,\mathrm d\mu_{\mathrm{Haar}}(U)
\,\mathrm d\mu_{\mathrm{Haar}}(V).
$$

By contrast, the separate one-slice marginal at finite temporal depth is

$$
\mathrm d\nu_{\rho,\Sigma}^{(n_\tau)}(U)
=
\frac{
\int |K_{n_\tau}(U,V)|^2
\,\mathrm d\mu_{\mathrm{Haar}}(V)}
{\|T^{n_\tau}\|_{\mathrm{HS}}^2}
\mathrm d\mu_{\mathrm{Haar}}(U).
$$

When a regular composition-kernel representative exists, the numerator is \(K_{2n_\tau}(U,U)\), and \(\|T^{n_\tau}\|_{\mathrm{HS}}^2=\operatorname{Tr}(T^{2n_\tau})\). Under the Hilbert--Schmidt-power condition and the simple-top-eigenvalue hypotheses of the transfer-gluing theorem, the normalized kernels converge in Hilbert--Schmidt norm to \(\psi_{0,\rho,L}(U)\overline{\psi_{0,\rho,L}(V)}\). Their squared moduli therefore converge in \(L^1\), so after \(n_\tau\to\infty\) this **one-slice** marginal converges in total variation to

$$
\psi_{0,\rho,L}^2\,\mathrm d\mu_{\mathrm{Haar}}.
$$

The two-cut joint marginal instead tends in total variation to the corresponding product of vacuum slice marginals. It must not be identified with the one-slice law by suppressing one of its boundary variables.

Thus \(B_\rho^{\mathrm{OS}}\) is the exact OS-to-interface leg of the sought carrier map. It is not yet the map from interface configurations to the logistic core-scale shadow.

## The Yang--Mills boundary construction at finite regulator

For Wilson lattice gauge theory, reflection positivity supplies a spectrally positive self-adjoint transfer matrix on the gauge-invariant carrier; [[library/construction-of-a-selfadjoint-strictly-positive-transfer-matrix-for-euclidean-lattice-gauge-theories/inq|Luscher's construction]] and [[library/gauge-field-theories-on-a-lattice/inq|Osterwalder--Seiler positivity]] are the canonical sources. Reflection positivity alone does not select a one-dimensional vacuum space. For the formulas below, additionally assume that the finite-spatial-lattice transfer operator is compact, injective, and positivity improving, so its maximal eigenvalue is simple with \(\psi_0>0\). The [[library/the-schrodinger-functional-a-renormalizable-probe-for-non-abelian-gauge-theories/inq|Schrodinger functional]] is a lattice gauge-theory amplitude with fixed fields at temporal boundaries and a perturbatively controlled continuum renormalization framework.

On a finite spatial graph, let \(U\in G^{E(\Gamma)}\) denote time-zero link data, with Gauss invariance imposed. For a far-wall boundary vector \(b_B\), a slab amplitude of \(n_\tau\) time steps has the form

$$
Z_{n_\tau,B}[U]
=
\int_{\Phi|_{\Sigma}=U}^{B\text{ at the far wall}}
e^{-S_{E,a}[\Phi]/\hbar}\,\mathcal D\Phi.
$$

If \(c_B:=\langle\psi_0,b_B\rangle\neq0\), transfer projection gives

$$
\lambda_0^{-n_\tau}Z_{n_\tau,B}[U]
\longrightarrow c_B\psi_{0,a,L}(U)
\quad\text{in }L^2(\mu_{\mathrm{Haar}})
\qquad(n_\tau\to\infty).
$$

After normalizing the glued finite-depth amplitudes and taking this infinite-depth limit, their squared densities converge in \(L^1\) to the equal-time vacuum measure

$$
\boxed{
\mathrm d\nu_{a,L}(U)
=
\psi_{0,a,L}(U)^2\,\mathrm d\mu_{\mathrm{Haar}}(U).
}
$$

This limiting law is exactly the ground-state measure for the Hamiltonian

$$
H_T:=-\frac{\hbar c}{a_\tau}\log T.
$$

It is the measure in the Kogut--Susskind ground-state-transform theorem only if \(T=e^{-a_\tau H_{\mathrm{KS}}/(\hbar c)}\) was defined from that Hamiltonian, or after a controlled temporal-continuum theorem identifies \(H_T\) with \(H_{\mathrm{KS}}\). The ordinary isotropic finite-spacing Wilson transfer matrix does not make that identification automatic. At fixed regulator, Euclidean sewing and ground-state transformation meet exactly for the same transfer Hamiltonian; changing Hamiltonians requires a comparison theorem.

Define the quantum boundary effective action

$$
W_{a,L}(U):=-2\log\psi_{0,a,L}(U)+\text{constant}.
$$

After choosing the invariant Lie-algebra metric and its normalized flux derivatives \(X_e^A\), define the boundary coordinate form

$$
\mathcal E_{a,L}(f,f)
=
\sum_{e,A}
\int|X_e^Af|^2e^{-W_{a,L}}\,\mathrm d\mu_{\mathrm{Haar}}.
$$

This form operates on gauge-invariant functions of boundary link configuration; its first-order calculus probes infinitesimal electric-flux directions. The measure does not make it the ground-state form of \(H_T\). A nonlinear Dirichlet-to-Neumann construction would have to show how a boundary link variation changes the conjugate normal electric flux of the integrated half-space theory and then prove the required form identity or domination.

The exact OS map first makes an **interface** analysis operator explicit. Let \(\mathcal K_{\rho,I}\) be the Hilbert direct sum of the \(L^2(\nu_{\rho,I})\) derivative components indexed by \((j,A)\), with their natural residual-gauge covariance retained. Assume that the invariant gradient on smooth gauge-invariant interface functions, formed from normalized derivatives \(X_j^A\) on every continuous interface variable, is closable from \(L^2(\nu_{\rho,I})^{\mathrm{GI}}\) to \(\mathcal K_{\rho,I}\). Let \(D_{\rho,I}\) denote its closure, so on the smooth core

$$
D_{\rho,I}:
\operatorname{Dom}D_{\rho,I}
\subset L^2(\nu_{\rho,I})^{\mathrm{GI}}
\longrightarrow\mathcal K_{\rho,I},
\qquad
D_{\rho,I}f
:=
\bigl(X_j^Af\bigr)_{j,A},
\qquad
\|D_{\rho,I}f\|^2
=
\mathcal E_{\rho,I}(f,f),
$$

and define

$$
\boxed{
J_{\mathrm{int},\rho,I}
:=
D_{\rho,I}B_\rho^{\mathrm{OS}},
\qquad
\operatorname{Dom}J_{\mathrm{int},\rho,I}
=
(B_\rho^{\mathrm{OS}})^{-1}\operatorname{Dom}D_{\rho,I}.}
\tag{OS7}
$$

This complex-linear map kills the constant reference line and is sensitive to complex phase directions that a probability-density tangent can miss. At the prequotient level, \(D_{\rho,I}b_\rho\) vanishes on \(\mathcal N_{\mathrm{OS}}=\ker b_\rho\), so it descends to the OS quotient; the later derivative may have an additional kernel. It is not yet known to be complete on the reference complement: that would require, in particular, \(\ker D_{\rho,I}=\mathbb C1\) on every relevant connected or gauge-reduced component. Its norm is the declared interface coordinate form; it is not automatically the spatial electric-flux form.

To make that latter identification, require one more geometric input: the separator must be identifiable with the canonical transfer slice \(\Sigma\), its infinite-depth marginal must be

$$
\nu_{\rho,I}
=
\nu_{\rho,L}
=
\psi_{0,\rho,L}^2\mu_{\mathrm{Haar}},
$$

and its derivative metric must be the Kogut--Susskind link metric. Only in this specialization may one write

$$
D_{\rho,I}=D_{\rho,L},
\qquad
J_{\mathrm{int},\rho,I}=J_{\mathrm{flux},\rho,L}.
$$

For a genuinely thick interface, an additional domain-compatible map \(C_{\rho,I\to\Sigma}\) from interface data to the canonical slice is required before composing with \(D_{\rho,L}\); conditional expectation alone does not supply it.

In the canonical-slice, infinite-depth specialization, define the boundary-to-canonical-carrier unitary

$$
U_{0,\rho}:
L^2(\nu_{\rho,L})^{\mathrm{GI}}
\longrightarrow
L^2(\mu_{\mathrm{Haar}})^{\mathrm{GI}},
\qquad
(U_{0,\rho}f)(U):=\psi_{0,\rho,L}(U)f(U),
$$

and \(\mathcal U_\rho^{\mathrm{OS}\to\mathrm{Sch}}:=U_{0,\rho}B_\rho^{\mathrm{OS}}\). If the Kogut--Susskind Hamiltonian acts on the target canonical carrier, transport it rather than silently letting it act on \(\mathcal H_{\mathrm{OS}}\):

$$
H_{\mathrm{KS},\rho,L}^{\mathrm{OS}}
:=
(\mathcal U_\rho^{\mathrm{OS}\to\mathrm{Sch}})^{-1}
H_{\mathrm{KS},\rho,L}
\mathcal U_\rho^{\mathrm{OS}\to\mathrm{Sch}}.
$$

Its centered closed quadratic form is

$$
h_{\mathrm{KS},\rho,L}^{\mathrm{OS}}[\Psi]
:=
\left\|
(H_{\mathrm{KS},\rho,L}^{\mathrm{OS}}-E_{0,\rho,L})^{1/2}\Psi
\right\|_{\mathcal H_{\mathrm{OS}}}^2
$$

on the transported form domain.

Suppose now that its kinetic term is exactly the normalized invariant-link Laplacian with coefficient \(\kappa_\rho\), that \(\psi_{0,\rho,L}\) is its positive ground state, and that the ground-state transform carries the full form domain to the declared coordinate-form domain. Then integration by parts gives the same-carrier identity

$$
h_{\mathrm{KS},\rho,L}^{\mathrm{OS}}[\Psi]
=
\kappa_\rho
\|J_{\mathrm{flux},\rho,L}\Psi\|^2.
\tag{OS8}
$$

The coincidence of a vacuum vector and an invariant metric alone would not establish this intertwining or form identity. For the isotropic Wilson transfer Hamiltonian \(H_{T,\rho}=-(\hbar c/a_\tau)\log T_\rho\), similarly set

$$
H_{T,\rho,L}^{\mathrm{OS}}
:=
(\mathcal U_\rho^{\mathrm{OS}\to\mathrm{Sch}})^{-1}
H_{T,\rho,L}
\mathcal U_\rho^{\mathrm{OS}\to\mathrm{Sch}}
$$

when the carriers and vacuum preparation have been identified, and define

$$
h_{T,\rho,L}^{\mathrm{OS}}[\Psi]
:=
\left\|
(H_{T,\rho,L}^{\mathrm{OS}}-E_{0,T,\rho,L})^{1/2}\Psi
\right\|^2
$$

on its transported form domain. Equation (OS8) is not automatic for this transfer generator. The required statement is the domain inclusion

$$
\operatorname{Dom}h_{T,\rho,L}^{\mathrm{OS}}
\subseteq
\operatorname{Dom}J_{\mathrm{flux},\rho,L}
$$

together with an independently proved form solder

$$
h_{T,\rho,L}^{\mathrm{OS}}[\Psi]
\geq
\epsilon_\rho
\|J_{\mathrm{flux},\rho,L}\Psi\|^2,
\qquad
\Psi\in
\operatorname{Dom}h_{T,\rho,L}^{\mathrm{OS}},
\tag{OS9}
$$

or a controlled temporal-continuum theorem identifying the transfer and Kogut--Susskind forms. The stated reflection-interface hypotheses construct \(B_\rho^{\mathrm{OS}}\); reflection positivity by itself proves neither that factorization, the interface-to-slice identification, nor (OS9).

## A direct route that does not require a local boundary action

There is a stronger way to exploit Euclidean locality. Let \(\mu_{a,L,n_\tau}^{\mathrm{per}}\) be the measure on a periodic temporal cylinder with \(n_\tau\) slices and spatial size \(L\), and let \(\pi_0\) be its time-zero projection. Suppose the bulk measure obeys a Poincare inequality

$$
\operatorname{Var}_{\mu_{a,L,n_\tau}^{\mathrm{per}}}F
\leq
C_a
\int\left(
|\nabla_0F|^2+|\nabla_{\mathrm{hidden}}F|^2
\right)\mathrm d\mu_{a,L,n_\tau}^{\mathrm{per}}
$$

with \(C_a\) uniform in spatial volume \(L\) and temporal depth \(n_\tau\). A reflected slab route would instead have to state a boundary family \(b_\pm\) and prove uniformity over that declared family. For \(F=f\circ\pi_0\), every hidden derivative vanishes. Hence the slice marginal \(\nu_{a,L,n_\tau}:=(\pi_0)_*\mu_{a,L,n_\tau}^{\mathrm{per}}\) obeys the exact inherited inequality

$$
\operatorname{Var}_{\nu_{a,L,n_\tau}}f
\leq
C_a\int|\nabla f|^2\,\mathrm d\nu_{a,L,n_\tau}.
$$

For a fixed compact spatial carrier and \(f\in C^1\), weak convergence

$$
\nu_{a,L,n_\tau}\longrightarrow
\nu_{a,L}:=\psi_{0,a,L}^2\mu_{\mathrm{Haar}}
$$

already passes both the variance and the continuous gradient integral to the limit. Hence

$$
\boxed{
\operatorname{Var}_{\nu_{a,L}}f
\leq
C_a\int|\nabla f|^2\,\mathrm d\nu_{a,L}.
}
$$

Closure extends the inequality from the \(C^1\) core to its coordinate-form domain. This marginal-inheritance theorem needs neither a local expression for \(W_{a,L}\) nor a boundary DLR theorem. The same restriction argument passes a logarithmic-Sobolev inequality. It applies to a coordinate marginal equipped with the inherited product carré du champ, not to an arbitrary marginal carrying an unrelated form.

[[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen--Zhu--Zhu]] prove a sharp fixed-spacing strong-coupling precedent. With normalization

$$
\mathrm d\mu_{\Lambda,N,\beta}
\propto
\exp\!\left(
N\beta\operatorname{Re}\sum_p\operatorname{Tr}Q_p
\right)
\prod_e\mathrm d\sigma_N(Q_e),
$$

their volume-uniform Bakry--Emery constant on unit-spacing periodic \(d\)-tori, \(d>1\), is

$$
K_{\mathrm{SZZ}}
=
\begin{cases}
\dfrac{N-2}{4}-8N|\beta|(d-1),&G=SO(N),\\[1mm]
\dfrac N2-8N|\beta|(d-1),&G=SU(N).
\end{cases}
\tag{VB36a}
$$

Hence they obtain

$$
\operatorname{Ent}_\mu(F^2)
\leq\frac{2}{K_{\mathrm{SZZ}}}\mathcal E(F,F),
\qquad
\operatorname{Var}_\mu(F)
\leq\frac{1}{K_{\mathrm{SZZ}}}\mathcal E(F,F)
\tag{VB36b}
$$

when

$$
|\beta|<\frac{N-2}{32N(d-1)}
\quad\text{for }SO(N),
\qquad
|\beta|<\frac1{16(d-1)}
\quad\text{for }SU(N).
\tag{VB36c}
$$

The same constants pass to their unique infinite-volume measure. Their separate covariance theorem gives exponential decay for disjoint smooth cylinder observables, with a rate depending on \(K_{\mathrm{SZZ}},N,d\). This is a genuine fixed-spacing strong-coupling Euclidean mass-gap result. For \(\beta\geq0\), connecting it to a fixed-lattice transfer gap still requires Wilson reflection positivity, an explicit OS transfer identification, and density of the local physical core. It does not control the anisotropic Kogut--Susskind limit or the asymptotically free \(a\to0\) trajectory. Their normalization obeys \(\beta_W=N^2\beta_{\mathrm{SZZ}}\) relative to the conventional Wilson exponent \((\beta_W/N)\sum_p\operatorname{ReTr}U_p\); this parameter is unrelated to the exceptional-model parameter satisfying \(\beta_W=144\beta_{\mathrm{exc}}\). Three gaps remain:

1. uniformity in temporal depth and in the precise boundary/cylinder family must match the sewing limit;
2. the inherited coordinate-gradient form must be compared with the ground-state form of \(H_T\), or a temporal-continuum limit must identify it with the Kogut--Susskind flux form; and
3. the constants must survive the four-dimensional asymptotically free continuum trajectory in physical RG units.

This is preferable to assuming that the nonlocal boundary action is quasilocal. [[library/projections-of-gibbs-measures-may-be-non-gibbsian/inq|Schonmann's low-temperature Ising counterexample]] proves that an infinite-volume local Gibbs measure can have a lower-dimensional marginal with no quasilocal DLR specification. Every strictly positive finite-dimensional marginal can still be written \(e^{-W}\mathrm d\mu\); the pathology concerns the infinite-volume specification. Boundary Dobrushin control is one possible route, not a consequence of bulk locality.

### The regulator and order of limits

The symbol \(a\) hides too much for this construction. Separate the UV data

$$
\rho=(a_s,a_\tau,\beta,N_c,G)
$$

from spatial size \(L\) and temporal depth \(n_\tau\). A finite system is therefore labelled by

$$
(\rho,L,n_\tau).
$$

where \(N_c\) is color rank and \(n_\tau\) is temporal depth. Two routes must not be mixed:

- **Isotropic Wilson route:** take \(a_s=a_\tau\to0\), keep the transfer generator \(H_{T,\rho}\), and identify the Lorentzian theory through OS reconstruction.
- **Hamiltonian route:** first take \(n_\tau a_\tau\to\infty\) to prepare the vacuum; then take \(a_\tau\to0\) at fixed \(a_s\) and identify the Kogut--Susskind Hamiltonian; only afterward take \(La_s\to\infty\) and \(a_s\to0\).

The functional-inequality constant must be independent of \(L\) and \(n_\tau\) before those limits. The Hamiltonian route is anisotropic; an isotropic small-\(\beta\) theorem does not automatically control it. Finally, an independent renormalization condition must fix

$$
\widehat\Lambda_\rho^{(s)}
\longrightarrow
\Lambda_{\mathrm{YM}}^{(s)}>0.
$$

## The exact new theorem target

The boundary perspective turns the open mechanism into a specific chain.

**B1. Construct the half-space carrier.** For every finite \((\rho,L,n_\tau)\), construct the gauge-reduced boundary configuration carrier, a reflection-Markov separator carrying every crossing interaction, reference Haar measure, reflection-positive transfer system, and normalized finite-slab amplitude without using a spectral-gap assumption. For the untwisted \(L^2\) factorization, prove that reflection fixes the separator after residual gauge reduction; on a periodic cylinder include every separating cut. Then control the limit \(n_\tau\to\infty\) that prepares the half-space vacuum amplitude.

**B2. Identify the gluing residue and quotient map.** Use reflection-Markov factorization to prove that conditional expectation onto the interface descends to the unitary \(B_\rho^{\mathrm{OS}}:\mathcal H_{\mathrm{OS}}\to L^2(\nu_{\rho,I})^{\mathrm{GI}}\), with the OS null subspace exactly its kernel before quotienting and exact coverage on the complement of the distinguished reference vector. Do not call that vector the complete vacuum or identify this interface carrier with a one-slice link carrier by notation alone.

**B2a. Reach the canonical transfer slice.** Either choose a reflection geometry for which \(I=\Sigma\) is the canonical transfer slice, or construct a domain-compatible interface-to-slice map \(C_{\rho,I\to\Sigma}\). Prove that infinite-depth gluing prepares \(\nu_{\rho,L}=e^{-W_{\rho,L}}\mu_{\mathrm{Haar}}\), rather than identifying a finite periodic marginal with that limit. Then prove that multiplication \(U_0f=\psi_{0,\rho,L}f\) is the unitary intertwining this weighted slice carrier and form with the centered transfer-Hamiltonian carrier and form.

**B3. Control the response without circularity.** Preferably prove a bulk Poincare or logarithmic-Sobolev inequality uniform in volume, temporal depth, and boundary conditions, and pass it to the slice marginal. Alternatively, for a fixed physical block size, prove uniform conditional Poincare bounds for \(\nu_{\rho,L}\) and a subcritical block-influence estimate. Either route must follow from the bulk action, reflection positivity, gauge geometry, and renormalization estimates—not from assumed exponential clustering or an assumed Hamiltonian gap.

**B4. Solder to energy on one carrier.** Define

$$
\widetilde h_{\rho,L}[f]
:=
\left\|
(H_{\mathrm{phys},\rho,L}-E_{0,\rho,L})^{1/2}
(\psi_{0,\rho,L}f)
\right\|^2,
\qquad
D(\widetilde h_{\rho,L})
:=
\left\{
f:
\psi_{0,\rho,L}f
\in
D\!\left((H_{\mathrm{phys},\rho,L}-E_{0,\rho,L})^{1/2}\right)
\right\},
$$

Require first that

$$
\ker(H_{\mathrm{phys},\rho,L}-E_{0,\rho,L})
=
\mathbb C\psi_{0,\rho,L},
\qquad
D(\widetilde h_{\rho,L})
\subseteq
D(\mathcal E_{\rho,L}),
$$

so centering against \(\nu_{\rho,L}\) is exactly orthogonality to the complete physical vacuum line and the response form is defined throughout the pulled-back physical form domain. Then, for every gauge-invariant

$$
f\in D(\widetilde h_{\rho,L}),
\qquad
\int f\,\mathrm d\nu_{\rho,L}=0,
$$

prove

$$
\widetilde h_{\rho,L}[f]
\geq
\kappa_\rho c_{\mathrm{form}}(\rho,L)\mathcal E_{\rho,L}[f].
$$

Then

$$
\Delta_{\rho,L}
\geq
\kappa_\rho c_{\mathrm{form}}(\rho,L)\lambda_{\mathrm{boundary}}(\rho,L).
$$

For the canonical Kogut--Susskind flux form, \(c_{\mathrm{form}}=1\) only when the invariant Lie-algebra metric and electric-flux normalization agree exactly with those defining \(\mathcal E_{\rho,L}\). If two Hamiltonians have different vacua, Hilbert carriers, centered subspaces, or form domains, a scalar \(c_{\mathrm{form}}\) is not enough; first construct norm- and domain-compatible comparison maps or complete the temporal-continuum identification. The bulk-marginal route gives \(\lambda_{\mathrm{boundary}}\geq C_\rho^{-1}\). The conditional-block route gives

$$
\Delta_{\rho,L}
\geq
\kappa_\rho c_{\mathrm{form}}(\rho,L)\,
\underline b(\rho)\,\underline\lambda_{\mathrm{loc}}(\rho)
\bigl[1-\overline q(\rho)\bigr].
$$

**B5. Use a physical yardstick.** Let \(\rho_j\) denote a declared UV regulator trajectory, after obtaining estimates uniform in \(L\) and \(n_\tau\). For a declared renormalization scheme \(s\), prove

$$
\liminf_{j\to\infty}
\frac{
\kappa_{\rho_j}
\inf_L\!\left[
c_{\mathrm{form}}(\rho_j,L)\lambda_{\mathrm{boundary}}(\rho_j,L)
\right]
}{\widehat\Lambda_{\mathrm{YM},\rho_j}^{(s)}}
>0.
$$

**B6. Pass to the theory.** Establish generalized Mosco convergence, or an equivalent identified strong-resolvent framework, together with convergence of vacuum projections and passage of the uniform lower-form bound to the entire limiting physical complement. Add OS reconstruction or an equivalent Hamiltonian identification, nontriviality, and the Yang--Mills axioms. Only then does the limit inherit a positive gap in physical units.

Strong-coupling Euclidean lattice results show that volume-uniform Poincare and logarithmic-Sobolev estimates can be proved from local gauge interactions. Marginalization can transfer such an estimate to a slice measure, but identifying the relevant transfer or Kogut--Susskind energy form and carrying the calibrated constant along the asymptotically free continuum trajectory remain open.

## A geometric sufficient condition, not a definition

On a complete weighted manifold satisfying the needed domain hypotheses—or on a compact smooth finite-dimensional boundary quotient without a problematic boundary—a Bakry--Emery \(CD(\rho_{\rho,L},\infty)\) estimate

$$
\operatorname{Ric}+\operatorname{Hess}W_{\rho,L}
\geq
\rho_{\rho,L}g
$$

implies a Poincare lower bound \(\lambda_{\rho,L}\geq\rho_{\rho,L}\) when \(\rho_{\rho,L}>0\). In the Gaussian model this is sharp. Singular quotients or boundaries require an appropriate extension of the curvature-dimension theorem and boundary conditions; the displayed smooth criterion cannot simply be applied across orbit-space strata. For Yang--Mills it is only one sufficient route:

- the gauge orbit space has singular strata;
- \(W_{\rho,L}\) is a quantum, generally nonlocal boundary action;
- its Hessian can have negative directions even when the total measure is gapped; and
- a global curvature lower bound may fail while block coercivity and weak influence still succeed.

Thus “spatial curvature defines mass” can be made exact only after naming which configuration-space metric, which measure, which connection, and which physical form are involved. Spacetime curvature is not the curvature in this inequality. The reversal is valid; the noun “curvature” is not interchangeable across its registers.

## Stopping rule

The construction has made a real dent only when it returns a lower bound not inserted in its definition. A valid stopping certificate must contain:

1. a declared boundary carrier and gauge quotient;
2. an independently constructed half-space amplitude and gluing measure;
3. a response or distinction operator with explicit domain and codomain;
4. a noncircular volume-uniform coercivity theorem at each regulator and continuum-uniform positivity of its calibrated physical product on all non-gauge directions;
5. the kinetic solder and independently calibrated RG yardstick;
6. infinite-volume and continuum stability; and
7. an OS or direct Hamiltonian theorem identifying the resulting lower edge with the physical Yang--Mills spectrum.

This is the Schrödinger stopping rule from the operator-signature verdict, specialized to the mass gap. The Gaussian model is a worked member that demonstrates the signature. Four-dimensional Yang--Mills still owes the independent return value.

## Claim ledger

| Status | Claim |
|---|---|
| Exact under finite-regulator hypotheses | with a disintegrable measure and cutting-compatible action/measure, bulk restriction has boundary-condition fibers and fiber integration/gluing produce boundary amplitudes and states |
| Exact, abstract | a compact positivity-improving self-adjoint transfer operator prepares \(\psi_0\), and two-sided gluing converges in total variation to \(\psi_0^2\mu\) |
| Exact under reflection-interface hypotheses | conditional expectation onto a reflection-fixed Markov separator factors the OS form; after quotient completion and dense interface insertions it gives a unitary \(B_\rho^{\mathrm{OS}}\) with reference-complement coverage one, and a closable interface derivative gives a complex-linear, phase-sensitive analysis map; calling the reference vector the unique vacuum or the derivative complete requires additional theorems |
| Exact, Gaussian | the half-space Dirichlet-to-Neumann operator is \(\Omega\), the glued logarithmic Hessian is \(2\Omega/\hbar\), and kinetic solder returns the gap \(\hbar\omega_{\min}\) |
| Standard, finite lattice | reflection-positive Wilson gauge theory admits a positive transfer construction; temporal boundary amplitudes are Schrodinger functionals |
| Exact, finite transfer regulator | the glued vacuum measure is the carrier of the ground-state transform for \(H_T=-(\hbar c/a_\tau)\log T\), with \(a_\tau\) a Euclidean length |
| Conditional identification | this is the Kogut--Susskind flux form only for a semigroup built from \(H_{\mathrm{KS}}\), or after a controlled Hamiltonian limit and form comparison |
| Carrier firewall | a thick OS separator is not automatically the canonical transfer slice; identifying its derivative with electric flux requires a special reflection geometry or a domain-compatible interface-to-slice map |
| Exact marginal theorem | a bulk Poincare or logarithmic-Sobolev inequality for a product carré du champ passes to a coordinate marginal equipped with its inherited coordinate form |
| Exact nonlinear marginal identity; conditional lower bounds | the retained effective Hessian is conditional mean visible Hessian minus conditional score covariance; under the Helffer--Sjostrand domain and closed-range hypotheses this is the Witten short \(G-B^*C^{-1}B\), while conditional Poincare and Riemannian Brascamp--Lieb inequalities give sufficient estimates |
| Compact-carrier no-go | no smooth potential on a closed connected manifold such as \(SU(3)^E\) has globally positive Hessian; a global proof must use weighted Ricci curvature, a functional inequality, or another topology-compatible estimate |
| Interpretation | the boundary effective action is a precise candidate for a wall residue; a causal-charge interpretation additionally requires a common continuous action, a normalized generator, a moment map or covariant boundary charge, and a proved flux law |
| Typed no-go | a torsor, strict descent, finite outcome algebra, OS quotient, transfer contraction, and mass gap are not the same construction |
| Open theorem target | derive regulator- and volume-uniform boundary coercivity and weak influence from the Yang--Mills bulk theory along the continuum trajectory |
| Open construction | pass the estimate to a nontrivial four-dimensional Yang--Mills theory satisfying the required axioms |

# Preserving-Expectation Loss

A state-preserving conditional expectation splits regular BKM tangents into recovered and forgotten components. Its loss Hessian is exactly the squared norm of the forgotten component, while the minimum quadratic loss over lifts of any retained tangent is zero. This gives a unit bound on the incoming vertical quotient, not a positive output stiffness. A separate fixed-index example shows why varying the reference state also defeats an index-only uniform bound.

## The preserving-expectation Hessian is vertical

Suppose \(E:\mathcal M\to\mathcal N\) is a faithful normal conditional expectation and the faithful normal reference state obeys \(\sigma\circ E=\sigma\). Let

$$
\operatorname{res}:\mathcal M_*\to\mathcal N_*,
\qquad
\operatorname{res}\rho=\rho|_{\mathcal N},
\qquad
j_E:\mathcal N_*\to\mathcal M_*,
\qquad
j_E\eta=\eta\circ E.
\tag{D5h.1}
$$

Then \(\operatorname{res}j_E=1\). For a faithful normal state \(\rho\) with finite \(S_{\mathcal M}(\rho\Vert\sigma)\), data processing also makes the restricted entropy finite. [[library/approximate-recoverability-and-relative-entropy-ii/inq|Faulkner--Hollands]] give, in this specialization, the general-von-Neumann chain rule without an undefined infinity-minus-infinity subtraction:

$$
\boxed{
S_{\mathcal M}(\rho\Vert\sigma)
-
S_{\mathcal N}(\operatorname{res}\rho\Vert\operatorname{res}\sigma)
=
S_{\mathcal M}(\rho\Vert\rho\circ E).}
\tag{D5h.2}
$$

Every regular faithful output curve \(\eta_s\) within this finite-entropy comparison domain therefore has a recovered lift \(\rho_s=j_E\eta_s\) whose loss vanishes identically. On a common Araki/BKM tangent domain preserved by restriction and recovery, with the quadratic Hessians specified in [[channel-loss-and-recovery/bkm-loss-operators|BKM loss operators]],

$$
P_E:=j_E\operatorname{res}
\tag{D5h.3}
$$

is the BKM-orthogonal projection onto the recovered tangents and

$$
\boxed{
q_{\sigma,\mathcal N}[\xi]
=
\|(1-P_E)\xi\|_{\mathrm{BKM},\sigma}^2
=
\operatorname{dist}_{\mathrm{BKM}}
(\xi,\operatorname{ran}P_E)^2.}
\tag{D5h.4}
$$

Thus the incoming quotient estimate is exact and needs no finite-index hypothesis; its constant one is sharp when the forgotten tangent space is nonzero. But its output transgression is

$$
\boxed{
\tau_{\operatorname{res}}(y)
:=
\inf_{\operatorname{res}\xi=y}q_{\sigma,\mathcal N}[\xi]
=0}
\tag{D5h.5}
$$

for every retained tangent \(y\). The form measures only the **vertical distinction forgotten by this one expectation**. It gives no stiffness to what survives.

The unit-quotient identity above assumes that the reference is \(E\)-invariant. A separate counterexample keeps the expectation and its index fixed while varying references that are not preserved by \(E\). For the Watatani-index-\(4\) factor inclusion

$$
M_2\otimes1
\subset
M_2\otimes M_2,
\qquad
E=\operatorname{id}\otimes\tau_2,
\tag{D5h.6}
$$

write \(I_2\) for the identity and \(X,Z\) for the Pauli matrices, and take

$$
\sigma_t
=
\frac{I_2\otimes I_2+tX\otimes X}{4},
\qquad
0<t<1,
\qquad
\xi=\frac{Z\otimes I_2}{4}.
$$

Here \(\sigma_t\circ E\ne\sigma_t\) for \(t>0\). Relative to the upstairs BKM norm of this tangent, the restriction-loss ratio is

$$
1-\frac{t}{\operatorname{artanh}t}
=
\frac{t^2}{3}+O(t^4)
\longrightarrow0.
\tag{D5h.7}
$$

This tangent is a nonzero eigenvector of the input BKM loss operator, not merely a vector approaching its kernel. Indeed, the logarithmic-mean map obeys \(\Omega_{\sigma_t}(Z\otimes I_2)=t(Z\otimes I_2)/(4\operatorname{artanh}t)\), so the restriction adjoint formula gives
\[
L_{\operatorname{res}}^{\sigma_t}\xi
=\left(1-\frac{t}{\operatorname{artanh}t}\right)\xi.
\]
Self-adjointness in the BKM metric makes \(\xi\) orthogonal to the loss kernel. Thus (D5h.7) also measures the loss relative to squared distance from that kernel.

Tensoring with a \(\sigma\)-finite Type III factor equipped with a fixed faithful normal state, and using the product reference and tangent, preserves both index and ratio. Hence there is no state-uniform positive Hessian floor depending only on the index. [[finite-index-distinction/gauge-index-no-go-and-four-dimensional-center-square]] gives the gauge-theoretic consequence: index is a capacity or sector-count datum, whereas physical coercivity needs normalized pullbacks and transverse relative position among a family of descents. This is distinct from varying the angle of two fixed-state projections, whose shared owner is [[trace-dirichlet-descent/subfactor-angle-coercivity-and-the-index-firewall|subfactor-angle coercivity]].

## The sufficiency--carrier fork

Two exact observations block the most tempting identification.

First, suppose a smooth state family $\rho_\theta$ is exactly recoverable by one channel $\mathcal R$:

$$
\mathcal R\Phi(\rho_\theta)=\rho_\theta.
$$

Data processing through $\Phi$ and then $\mathcal R$ forces equality throughout, so

$$
\ell_\Phi^{\rho_0}[\dot\rho_0]=0.
\tag{D6}
$$

Thus the relative-entropy residue cannot positively charge a tangent whose entire statistical model is exactly sufficient through the wall.

Second, if

$$
\Phi X=0,
$$

then

$$
\ell_\Phi^\sigma[X]
=
g_\sigma^{\mathrm{BKM}}(X,X),
$$

but the output tangent is zero. This is real lost distinction on the input carrier, not a mass form on an observable excitation.

Hence the **[EXACT RECOVERY FORK]** is

$$
\boxed{
\begin{array}{ccl}
\text{recoverable direction}&\Longrightarrow&\text{zero residue},\\[2mm]
\text{erased direction}&\Longrightarrow&\text{positive upstream residue but zero output}.
\end{array}}
\tag{D7}
$$

This sharpens the range--kernel no-go in [[global-local-response-reconstruction/causal-patch-boundary-and-two-times]]. The loss and its BKM derivative are defined in [[channel-loss-and-recovery/bkm-loss-operators|BKM loss operators]]. If a wall is to contribute to a mass-gap form, it needs a further construction that acts on retained physical directions; [[channel-loss-and-recovery/minimum-lift-output-forms|minimum-lift output forms]] distinguishes a general channel's contraction from this adapted expectation case.

# Boundary-Action Fixed Points and Physical Linearization

A positive transfer law builds its vacuum by repeatedly integrating one more layer of a finite history. On logarithmic boundary actions this operation is nonlinear, concave and defined modulo additive constants; its derivative at the vacuum is exactly the physical Doob transfer on centered observables. This makes the gap a stability rate of a boundary-action fixed point, but does not prove that rate uniform. The complete tangent space, its vacuum norm and the calibrated layer thickness are essential parts of the statement.

**Status: [EXACT] for the finite positive compact-kernel construction and its derivatives; [EXACT CALIBRATION] for the Gaussian recursion; [OPEN] for continuum-uniform physical stability.** The [[local-perron-oscillation-and-conditional-coercivity|local Perron note]] owns spatial score derivatives. The derivatives with respect to an entire boundary action below are different operators.

## Integrating a layer acts on a boundary action

Use product Haar probability on a finite compact configuration space and
\[
T=M_aKM_a,\qquad a=e^{-V_{\rm sp}/2}>0.
\]
Assume its continuous kernel is strictly positive and symmetric; for differential conclusions assume \(C^2\) regularity. Let \(f_n=T^n1\), up to positive scalar normalization, and \(V_n=-2\log f_n\). Then
\[
\boxed{\mathscr R(V)(U)
=V_{\rm sp}(U)-2\log\int k(U,Y)
e^{-[V_{\rm sp}(Y)+V(Y)]/2}\,dY,\qquad
[V_{n+1}]=[\mathscr R(V_n)].}
\tag{BF1}
\]
Brackets denote the quotient of continuous real actions by constants. This is an exact reformulation of the specified transfer, not a new independently selected dynamics.

For \(N\ge1\), the underlying one-sided path weight is
\[
a(U_0)\left[\prod_{t=0}^{N-1}k(U_t,U_{t+1})\right]
\left[\prod_{t=1}^{N-1}e^{-V_{\rm sp}(U_t)}\right]
a(U_N)\prod_{t=1}^N dU_t.
\tag{BF2}
\]
Internal slices receive the full potential, endpoints its halves. Its first conditional marginal at fixed \(U_0=U\) uses \(f_{N-1}\), not the stationary vacuum unless the limit has been taken.

Strict compact-kernel positivity gives a unique positive Perron vector \(\psi\) and convergence of normalized \(T^n1\) at each fixed finite configuration space. With the stated smoothness, one further kernel application upgrades \(L^2\) convergence to \(C^2\) convergence. Thus \([V_n]\) tends to \([V_*]\), where \(V_*=-2\log\psi\). No uniform rate in volume or regulator has been used.

## An exact entropy identity, with a specified reference law

Define the actual finite-action posterior
\[
\eta^V_U(dY)=
\frac{k(U,Y)e^{-[V_{\rm sp}(Y)+V(Y)]/2}\,dY}
{\int k(U,Y')e^{-[V_{\rm sp}(Y')+V(Y')]/2}\,dY'}.
\tag{BF3}
\]
For bounded \(h\),
\[
\mathscr R(V+h)(U)-\mathscr R(V)(U)
=-2\log\mathbb E_{\eta^V_U}e^{-h/2}
=\inf_{\rho\ll\eta^V_U}
\left\{\rho(h)+2D(\rho\Vert\eta^V_U)\right\}.
\tag{BF4}
\]
The infimum is over probability measures \(\rho\). Here \(D\) uses natural logarithms, and both terms are dimensionless. To prove the last equality, put \(d\rho_h=e^{-h/2}d\eta/Z_h\) and expand \(2D(\rho\Vert\rho_h)\ge0\). Equality holds at \(\rho_h\). This entropy is the cost of changing a declared conditional law; it is not a new conserved charge, horizon entropy or mass.

Differentiating on bounded action directions gives
\[
D\mathscr R_V[h]=\eta^V h,\qquad
D^2\mathscr R_V[h_1,h_2]
=-\tfrac12\operatorname{Cov}_{\eta^V}(h_1,h_2).
\tag{BF5}
\]
Consequently \(\mathscr R\) is order preserving, additively homogeneous and concave. The covariance's minus sign and factor \(1/2\) differ from the spatial Hessian's factor \(2\); the differentiated variables are different.

## The fixed-point derivative is the physical operator

Normalize \(\int\psi^2\,dU=1\). At the Perron class, \(\eta^{V_*}_U=P_T(U,\cdot)\). Identify the action quotient's tangent with centered functions in \(L^2(\nu)\), where \(\nu=\psi^2dU\). Differentiation followed by centering gives
\[
\boxed{D[\mathscr R]_{[V_*]}=P_T|_{L^2_0(\nu)}.}
\tag{BF6}
\]
The nonlinear map is defined on continuous or bounded actions, not asserted to be defined on arbitrary \(L^2\) actions. Its derivative extends by contraction to the \(L^2\) completion of bounded tangents. Gauge-invariant tangents give the physical subspace because the original law and vacuum are gauge invariant.

If the transfer is also positive and injective as a Hilbert-space operator, so that its spectral logarithm is densely defined, then on this physical carrier
\[
\rho_{\rm lin}=\|P_TQ_0\|,\qquad
\Delta_E=-\frac{\hbar c}{\ell_\tau}\log\rho_{\rm lin}.
\tag{BF7}
\]
This is the [[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder|transfer logarithm]], with one step representing Euclidean length \(\ell_\tau\). Equivalently, mass after the further Poincare identification is \(\Delta_E/c^2\). Uniform fixed-physical-depth linear stability would prove the corresponding spectral exclusion; assuming that stability merely assumes an equivalent form of the gap.

## Projective convergence has a volume cost

For a positive kernel \(t\), set
\[
\mathfrak D(t)=
\sup_{U,V,Y,Z}\log
\frac{t(U,Y)t(V,Z)}{t(U,Z)t(V,Y)}.
\tag{BF8}
\]
Then the classical projective oscillation estimate, proved directly below, is
\[
\operatorname{osc}(\mathscr R(V)-\mathscr R(W))
\le\tanh\!\left(\frac{\mathfrak D(t)}4\right)
\operatorname{osc}(V-W).
\tag{BF9}
\]
Indeed, normalized positive laws whose likelihood ratio has log-oscillation at most \(D\) differ in total variation, defined as \(\sup_A|p(A)-q(A)|\), by at most \(\tanh(D/4)\). For a likelihood ratio in \([m,M]\) of mean one, convexity bounds its mean absolute deviation by the two-endpoint law. The resulting total variation is at most \((M-1)(1-m)/(M-m)\); maximizing with \(M/m\le e^D\) gives the stated bound. Apply it to two rows of (BF3), bound their expectation difference by this coefficient times \(\operatorname{osc}h\), and integrate (BF5) along the segment from \(W\) to \(V\).

The multipliers \(a\) cancel from every cross ratio. For product Wilson kernels on \(SU(2)\),
\[
\mathfrak D(T)=\sum_e4x_e,\qquad
\tau_{\rm proj}=\tanh\!\left(\sum_e x_e\right).
\tag{BF10}
\]
In unit-quaternion coordinates the one-link log cross ratio is \(x\langle u-v,y-z\rangle\), with maximum \(4x\). At fixed positive couplings the certificate approaches one exponentially in total link count. This is a statement on the raw product carrier; gauge fixing does not preserve that product formula automatically. Finite projective contraction is not a thermodynamic mass-gap proof.

The local estimate is better behaved. With \(D_I\) from the local Perron note, positivity gives
\[
\operatorname{osc}_I V_n\le D_I\quad(n\ge1).
\]
The block-conditional potential of \(\eta^{V_n}_U\) is
\(-\log k(U,Y)+(V_{\rm sp}(Y)+V_n(Y))/2\); its oscillation is also at most \(D_I\), including the seed \(V_0=0\). Hence its conditional block Poincare constant is at least \(e^{-D_I}\lambda_{{\rm H},I}\), uniformly in horizon and \(U\). Collective dependence and refinement uniformity do not follow.

## Gaussian curvature shows what a restricted ansatz omits

On the different carrier \(\mathbb R^r\), take
\[
k_B(U,Y)\propto e^{-(Y-U)^{\mathsf T}B(Y-U)/2},\quad
V_{\rm sp}(U)=\tfrac12U^{\mathsf T}AU,\quad
V_n(U)=\tfrac12U^{\mathsf T}R_nU+\text{constant},
\]
where \(B>0\) and initially \(A>0,\ R_n\ge0\). Gaussian integration gives
\[
D_n=B+\tfrac12(A+R_n),\qquad
\eta_U^{V_n}=N(D_n^{-1}BU,D_n^{-1}),\qquad
\boxed{R_{n+1}=A+2B-2BD_n^{-1}B.}
\tag{BF11}
\]
The score covariance is \(BD_n^{-1}B\), which checks the sign in the spatial Hessian recurrence. Writing \(\bar A=B^{-1/2}AB^{-1/2}\), the positive fixed precision is
\[
R_*=B^{1/2}\sqrt{\bar A^2+4\bar A}\,B^{1/2}.
\tag{BF12}
\]
In whitened coordinates the precision-map derivative sends \(H\) to \(\bar D^{-1}H\bar D^{-1}\). If \(\bar A\ge a_0I>0\), its norm is at most \((1+a_0/2)^{-2}<1\) throughout the positive precision cone. This uses an independently supplied confinement floor.

It is not the full action-space rate. At an eigenvalue \(a>0\) of \(\bar A\), the first-chaos Doob eigenvalue is
\[
g(a)=\frac{2}{2+a+\sqrt{a^2+4a}};
\]
quadratic precision perturbations contract with products \(g(a_i)g(a_j)\). An even quadratic ansatz misses slower linear directions. At \(A=0\), the fixed precision vanishes and no normalizable whole-space vacuum results, although the local posterior precision remains at least \(B\). The flat seed on \(\mathbb R^r\) is not \(L^2\); for \(A>0\) it becomes normalizable after one step, or one may start with \(R_0>0\).

For \(B=bI\) and \(A=\mu I+\Delta_{\rm lattice}\), (BF12) is generally nonlocal. As \(\mu\downarrow0\), its Fourier symbol has a \(|p|\) behavior, excluding a uniform exponentially localized limiting kernel. [[contemporary-puzzles/yang-mills-mass-gap/vacuum-boundary-gluing-and-wall-response|The half-space response owner]] explains the corresponding continuum Dirichlet-to-Neumann square root.

The next theorem must therefore control the actual joint response rather than assume local effective curvature. [[strong-coupling-gap-and-continuum-crossover/wilson-slab-conditional-fisher-certificate|The Wilson slab certificate]] supplies that control in a specified small-parameter regime. [[receipts/boundary_action_fixed_point_receipt.py|The finite receipt]] checks the action derivatives, projective constants, finite-horizon convergence and Gaussian precision calculation.

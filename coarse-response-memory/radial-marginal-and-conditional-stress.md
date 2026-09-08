# The Radial Marginal and Its Conditional Metric Stress

The actual marginal of an interacting gauge vacuum contains both conditional kinetic costs. Their first variation depends on the full conditional information tensor, including orbit stress invisible to the scalar coupling estimate. Exact small-coupling expansions expose cancellations between these costs and show that the actual radial stress takes both signs. A favorable marginal estimate therefore requires a comparison of their magnitudes, not merely positive local response or a separately favorable stress sign.

**Status: exact fixed-regulator identities and small-coupling deductions; finite numerical diagnostics; no continuum mass-gap theorem.** Use the supplied operator, complete invariant coordinates, cometric and vacuum expansion in [[two-plaquette-vacuum-and-relational-state|the full two-plaquette construction]] (TP1--TP19). Its raw link metric and Hamiltonian remain inputs.

## The actual marginal retains both fiber costs

Retain the left square's four raw links as \(A\), and the
remaining three as \(B\). This is a disjoint raw product split,
not two independent plaquette holonomies. In
[[conditional-fisher-coercivity/moving-fiber-connection#The actual ground state returns coupled fiber equations|the exact conditional-amplitude equations]],
take
\[
H_A=-\kappa\Delta_A+\lambda(1-a),\quad
H_B=-\kappa\Delta_B,\quad W=\lambda(1-b),
\qquad \psi=\chi(a)\Phi,\quad \int_B\Phi^2\,dB=1.
\]
The positive marginal \(\chi=\sqrt{\rho_A}\) is a class function
of the retained holonomy by gauge invariance. Set
\(\mathcal F(a)=\epsilon(a)+\kappa T(a)\), where
\(\epsilon=\langle\Phi,(H_B+W)\Phi\rangle_B\) and
\(T=\int_B|\nabla_A\Phi|^2dB\). Its exact equation is
\[
\left[-\kappa(1-a^2)\partial_a^2+3\kappa a\partial_a
+\lambda(1-a)+\mathcal F(a)\right]\chi=E_0\chi.
\tag{TP24}
\]

There is a useful expression keeping all the shared-edge
geometry visible. Write \(I_a\) for conditional **product-Haar**
integration over \(B\), not conditional expectation under
\(\psi^2\). For invariant integrands it is the \(b,u\) integral
in (TP14), with \(z=\sqrt{(1-a^2)(1-b^2)}u\). Then
\[
\boxed{
\mathcal F(a)=\lambda[1-I_a(b\Phi^2)]
+\kappa I_a\!\left[g_{ij}\Phi_i\Phi_j\right].
}
\tag{TP25}
\]
Here \(g\) is the full dimensionless cometric (TP4), and
\(\Phi_i\) are fixed-\((a,b,z)\) coordinate partials. There is
no extra \(\Phi^2\) weight in the gradient integral: it is
the energy of the amplitude itself. The formula adds the
raw \(A\) and \(B\) kinetic costs before reduction; it does
not replace their sum by an independent two-loop metric.

The normalized expansion (TP9) gives
\[
\Phi=1+\frac r3b+
r^2\left[\frac{b^2}{24}-\frac7{288}
+\frac{ab+4z}{351}\right]+O(r^3),
\qquad r=\lambda/\kappa.
\tag{TP26}
\]
At fixed \(a\), the Haar moments are
\(I_ab=I_az=I_a(bz)=0\),
\(I_ab^2=1/4\), and \(I_az^2=(1-a^2)/4\).
Using them and the full cometric gives
\[
\begin{aligned}
I_a(b\Phi^2)&=\frac r6+\frac{r^2a}{702}+O(r^3),\\
T&=\frac{r^2}{48}-\frac{r^3a}{936}+O(r^4),\\
\kappa^{-1}\langle\Phi,H_B\Phi\rangle_B
&=\frac{r^2}{16}+\frac{r^3a}{936}+O(r^4),\\
\mathcal F(a)/\kappa
&=r-\frac{r^2}{12}-\frac{r^3a}{702}+O(r^4).
\end{aligned}
\tag{TP27}
\]
For the third line the three hidden edges give \(3D_y\):
their cometric entries are
\(g^B_{bb}=3(1-b^2)/4\),
\(g^B_{bz}=-3bz/4\), and
\(g^B_{zz}=3(1-a^2-z^2)/4\).
Subtracting this from the full cometric gives the second line.
The cubic kinetic terms cancel in their sum, not in either
piece separately. Dropping the conditional orientation or one
fiber cost would miss that identity.

The remainders in the marginal scalar formulas are controlled
in \(C^1([-1,1])\) for this fixed compact graph. One can
differentiate the analytic ground vector in high raw Sobolev
norms, integrate its smooth invariant scalar expressions,
and use smooth radial invariance at \(a=\pm1\). This does
not assert bounded partial derivatives of every orbit-coordinate
expression at all singular strata, or uniformity over graphs.
Explicitly, for an invariant scalar remainder \(f(a)\), put
\(j(\theta)=f(\cos\theta)\). Smoothness gives
\(j'(0)=j'(\pi)=0\), and
\[
\|f'\|_\infty\le\frac{\pi}{2}\|j''\|_\infty.
\]
This controls the endpoint division by \(\sin\theta\) using
the raw second-derivative remainder. No numerical
small-coupling threshold is asserted.

For \(g_{\rm marg}(\theta)=\sin\theta\,\chi(\cos\theta)\),
(TP24) becomes
\[
-\kappa g_{\rm marg}''
+V_{\rm eff}(\theta)g_{\rm marg}=(E_0+\kappa)g_{\rm marg},
\quad
V_{\rm eff}=\lambda(1-\cos\theta)+\mathcal F(\cos\theta).
\]
In particular,
\[
V_{\rm eff}'(\theta)
=\sin\theta[\lambda-\mathcal F'(\cos\theta)]
=\kappa\sin\theta\left[r+\frac{r^3}{702}+O(r^4)\right]>0
\tag{TP28}
\]
for every interior \(\theta\) at sufficiently small positive
\(r\). The remainder inside the brackets is uniform.
The
[[algebra/partial-bochner-and-ground-state-score#The invariant plaquette quotient has positive weighted curvature|radial Riccati argument]]
therefore proves strict log-concavity of the **actual**
\(g_{\rm marg}\) in this regime, not just of a product reference.
It gives a positive weighted-curvature bound for its inherited
one-dimensional conservative form.

No all-coupling conclusion follows: positivity of
\(\epsilon\) and \(T\) does not control
\(\mathcal F'(a)\). The conditional vector obeys the coupled
fiber equation, not an instantaneous hidden ground-state
equation. Moreover, a marginal Poincare bound is not a
bound on the full physical generator. The hidden response
in (TP11)--(TP22) remains nonzero in this small-\(r\) regime;
replacing that generator
by a closed one-variable clock would change the theory.

## Radial force retains orbit stress

The
[[conditional-fisher-coercivity/moving-fiber-connection#The effective force is a weighted metric divergence|conditional first-variation identity]]
specifies the additional all-coupling obligation. On the raw
four-link region write
\[
X=\nabla_Aa,\quad h=|X|^2=1-a^2,\quad
\rho=\chi^2,\quad w(a)=\frac2\pi\sqrt h,\qquad
s=M(X,X),\quad
\tau=\langle M,\operatorname{Hess}_Aa\rangle.
\]
Here \(M\) is the actual conditional-amplitude tensor (MF13),
not an independently fitted scalar response. On \(|a|<1\),
\[
\boxed{
\frac{\langle X,\operatorname{div}_A(\rho M)\rangle}{\rho}
=\frac{(\rho ws)'}{\rho w}-\tau .
}
\tag{TP29}
\]
To prove the reduction, expand
\(\operatorname{div}_A(\rho MX)\).
Gauge invariance makes this scalar a function of \(a\).
Integration against arbitrary smooth compactly supported
functions of \(a\), followed by Haar coarea, gives
\(\operatorname{div}_A(\rho MX)=w^{-1}(\rho ws)'\).
The product rule subtracts precisely \(\rho\tau\).
This proves the interior identity without assigning a
smooth quotient chart at the endpoints.

The potential derivative contracts as
\(\langle X,\nabla_AW\rangle=-\lambda z/4\), using the
shared coefficient \(g_{ab}=z/4\). Therefore
\[
\boxed{
h\mathcal F'(a)
=-\frac{\lambda}{4}\mathbb E_\beta[z\mid A]
+2\kappa\left[
s'+\left(\frac{\rho'}{\rho}-\frac a h\right)s-\tau
\right].
}
\tag{TP30}
\]
The expectation here uses the **actual** conditional law
\(\beta=\Phi^2dB\), unlike the unweighted amplitude integrals
in (TP25). The same identity can be integrated using (MF21)
instead of differentiating sampled covariance data.

The shape coefficient in (BC21) is \(c=4\kappa s/h\).
Its value does not determine \(\tau\), even if one also
knows \(T=\operatorname{tr}M\). An exact geometric
counterexample makes this distinction explicit. Choose two
distinct retained edges and let \(V\) have components
\((\nabla_{e_1}a,-\nabla_{e_2}a,0,0)\).
Each edge contributes \(h/4\) to \(|X|^2\), so
\[
\langle X,V\rangle=0,\qquad |V|^2=h/2,\qquad
\operatorname{Hess}_Aa(V,V)=0.
\]
For the last equality, the two edge geodesics insert
opposite commuting holonomy-gradient generators; their
holonomy product remains fixed. Define symmetric tensors
using the raw metric identification,
\[
M_1=hI-X\otimes X,\qquad M_2=22V\otimes V.
\]
Both are globally smooth, gauge equivariant and positive
semidefinite. The raw dimension is twelve, and
\(\Delta_Aa=-3a\),
\(\operatorname{Hess}_Aa(X,X)=-ah\). Hence
\[
\boxed{
s_1=s_2=0,\qquad T_1=T_2=11h,\qquad
\tau_1=-2ah,\quad \tau_2=0.
}
\tag{TP31}
\]
Adding the same positive constant times \(I\) makes both
tensors positive definite without changing this discrepancy.
These are geometric tensors, not asserted Wilson conditional
covariances. They rule out recovering the stress from shape
response, trace, positivity and equivariance alone.

This does not retract the sharp physical coupling estimate
in
[[boundary-interaction-and-conditional-score-budget#The physical estimate sees only the shape component|the shape-compression theorem]].
That estimate concerns a different operation. Orbit
components can be invisible to a retained scalar gradient
yet enter the variation of the joint state's effective
potential. Their tensor contraction cannot be removed as
a gauge redundancy at this step.

There is already a decisive check at small coupling:
(TP26) makes \(M\), to order \(r^2\), equal to
\(r^2I_3/144\) on the shared edge and zero on the other
retained edges. Thus
\[
s=\frac{hr^2}{576}+O(r^3),\qquad
\tau=-\frac{ar^2}{192}+O(r^3).
\]
The stress bracket in (TP30) cancels at order \(r^2\).
Keeping only the orbit-normal part of \(M\) would miss
that cancellation and create a spurious force.

## The radial stress takes both signs in the actual vacuum

One tempting sufficient route would prove
\(\mathbb E_\beta[z\mid A]\ge0\) and nonpositive radial
weighted stress divergence separately. The second condition
is false already at small positive coupling. Define
\[
\mathcal J(a,r)
=\frac{\langle X,\operatorname{div}_A(\rho M)\rangle}{\rho}
=\frac{h\mathcal F'(a)+\lambda\mathbb E_\beta[z\mid A]/4}
       {2\kappa}.
\]
The normalized vacuum has third coefficient
\[
\begin{aligned}
\psi_3={}&\frac{a^3+b^3}{360}
+\frac{739(a^2b+ab^2)}{50544}\\
&+\frac{263(a+b)z}{101088}
-\frac{20069(a+b)}{1010880}.
\end{aligned}
\tag{TP32}
\]
Writing \(K=H_0/\kappa\), direct application of (TP3) verifies
\(K\psi_3=(a+b)\psi_2-\psi_1/6\); odd parity gives the
normalization condition at this order.
Expand \(\Phi=\psi/\sqrt{I_a\psi^2}\), retaining the
normalization through order three. The Haar moments in
(TP27), together with
\(I_ab^4=1/8\), \(I_a(b^2z^2)=h/24\),
and \(I_az^4=h^2/8\), give
\[
\begin{aligned}
\mathcal F(a)/\kappa
={}&r-\frac{r^2}{12}-\frac{r^3a}{702}
+r^4\left[\frac{48089}{31539456}
+\frac{1285a^2}{7884864}\right]+O(r^5),\\
\mathbb E_\beta[z\mid A]
={}&\frac{2h}{351}r^2-\frac{121ah}{202176}r^3+O(r^4).
\end{aligned}
\tag{TP33}
\]
The first line needs only \(\Phi_1,\Phi_2,\Phi_3\):
the potential has a factor \(r\), and the leading
amplitude has zero gradient. The full mixed cometric
in (TP25) remains essential.

Substitution cancels the cubic stress identically and gives
\[
\boxed{
\mathcal J(a,r)=\frac{5561}{63078912}
\,r^4a(1-a^2)+O(r^5).
}
\tag{TP34}
\]
The remainder is uniform on each fixed compact interior
interval by the same analytic compact-carrier argument as
(TP27). Thus at any fixed \(a\in(0,1)\) it is positive
for sufficiently small positive \(r\), and at any fixed
\(a\in(-1,0)\) it is negative. This is a sign obstruction
for the **actual** conditional vacuum, unlike the
arbitrary-tensor comparison (TP31).

There is no contradiction with (TP28). The interaction
term controls \(\mathcal F'\) at order \(r^3\), while this
signed correction first appears at order \(r^4\).
The next monotonicity proof must compare their magnitudes,
not require each contribution separately to have a useful
sign. An exact sufficient target for
\(\mathcal F'(a)<\lambda\) remains
\[
2\kappa\mathcal J(a,r)
<\lambda\left[h+\frac14\mathbb E_\beta[z\mid A]\right].
\tag{TP35}
\]
Writing this comparison does not prove it at arbitrary
coupling or along a continuum trajectory.

## Preparation and the inherited marginal estimate

[[heat-preparation-and-latitude-coercivity|The actual Haar preparation]]
now supplies a stronger small-coupling marginal result: its latitude
logarithm stays concave for all preparation times, with an inherited
Poincare gap at least \(\kappa\) throughout a fixed small-coupling
range. The proof controls the combined conditional source, even
though conditional convexity itself fails. It retains the full
relational state and does not close the physical generator on the
marginal. The time-dependent force includes conditional relaxation;
the stationary stress identity above does not describe it alone.

## Numerical tests preserve the discarded directions

The [[receipts/two_plaquette_vacuum_receipt.py|existing interacting receipt]]
computes the actual marginal without fitting a density.
Let \(c_{nmk}\) be the vacuum coefficients in the normalized
basis (TP15), with norms from (TP17), and set
\[
R_{nk}(a)=\frac{(1-a^2)^{k/2}C_{n-k}^{k+1}(a)}
 {\sqrt{h_{n-k,k}}}.
\]
Hidden harmonic orthogonality then gives
\[
\rho_A(a)=\sum_{m,k}\left|\sum_n c_{nmk}R_{nk}(a)\right|^2.
\]
Each summand is \(h^k\) times a squared polynomial. Its
first three derivatives can therefore be evaluated
analytically, including endpoints, before dividing by the
marginal. Independent positive hidden quadrature checks
the marginal and its first derivative.

At \(\kappa=1\), a 2001-point grid supports
\(dV_{\rm eff}/da<0\) and positive angular weighted
curvature at \(\lambda=0.5,1,2,4,8,16\).
At \(\lambda=16\), cutoffs 14 and 16 give sampled maximum
derivative approximately \(-16.20307586\) and minimum
curvature \(2.256388329\); their changes are below
\(9.6\,10^{-7}\) and \(5.4\,10^{-9}\), respectively.
These are converged finite diagnostics, not certified signs
between nodes or an all-coupling theorem. The minimum
marginal density is already about \(5.96\,10^{-6}\);
derivative ratios require tail resolution, not merely a
converged ground-state energy.

An independent weak test uses (MF21) with
\(Z=a^j\nabla a\), \(0\le j\le4\). It contracts the
actual amplitude gradients with the raw holonomy Hessian,
without differentiating \(M\) numerically. At
\(\lambda=0.5,1,4\), refined residuals are below
\(4\,10^{-16}\). Omitting orbit stress instead leaves
errors approximately \(0.000422,0.001553,0.008995\).
The observed failure matches the exact second-order
cancellation and tensor obstruction above.

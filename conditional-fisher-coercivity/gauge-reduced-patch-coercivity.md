# Coercivity After Interior Gauge Reduction

A fixed Wilson patch can have a vanishing full conditional-refresh gap because a gauge-dependent link becomes almost predictable from its neighbors while retaining a Haar marginal. That slow variation is removed by the interior Gauss constraint. The local-to-global projection criterion therefore needs to be tested on the gauge-invariant whole, using regional carriers that impose interior Gauss law but preserve boundary data. An auxiliary gauge refresh realizes this reduction exactly without changing the invariant dynamics or creating a physical mass.

**Status: exact finite-Wilson obstruction, exact gauge-completion identities, and conditional quotient-patch theorem.** The sufficient fixed-patch threshold below is ruled out at weak coupling for \(n\ge3\) by [[weak-coupling-patch-threshold|a surviving path response]]. Physical transfer comparison and continuum construction remain open.

## A full-carrier obstruction from almost-flat plaquettes

Let \(B\) contain all links with both endpoints in a vertex cube of fixed side \(n\ge3\), in the finite torus of [[finite-patch-projection-coercivity|the projection theorem]]. For \(SU(q)\), \(q\ge2\), put
\[
\phi_p(U)=q^{-1}\operatorname{ReTr}U_p,\qquad
V_B(U;\eta)=\sum_{p:\,p\cap B\ne\varnothing}(1-\phi_p(U,\eta)),
\]
\[
\mu_{\beta,\eta}(dU_B)
=Z_{\beta,\eta}^{-1}e^{-\beta V_B(U;\eta)}\,dU_B.
\tag{GR1}
\]
Here \(\eta\) is the frozen exterior, \(dU_B\) is normalized product Haar, and the action includes boundary plaquettes. The nonnegative auxiliary operator is
\(h_B^\eta=\sum_{e\in B}(I-P_e^\eta)\), with actual conditional expectations. No clock time has been assigned to it.

Choose an edge \(e\) incident to a strictly interior vertex. Gauge transformation at that vertex leaves every exterior link fixed. Invariance of (GR1) makes \(U_e\) exactly Haar-distributed for every \(\eta\). For the matrix-valued test \(F(U)=U_e\),
\[
\mathbb E_{\beta,\eta}F=0,\qquad
\mathbb E_{\beta,\eta}\|F\|_{\rm HS}^2=q,\qquad
Q_j^\eta F=0\quad(j\ne e).
\tag{GR2}
\]
Matrix notation only packages \(q^2\) ordinary complex scalar probes.

For any plaquette \(p\) containing \(e\), the complementary three-link path, suitably oriented, gives a matrix \(W_p\) measurable without \(U_e\), with
\[
\|U_e-W_p\|_{\rm HS}^2=2q(1-\phi_p).
\]
Conditional expectation is the least-squares predictor. Summing a scalar spectral-gap inequality over the entries of \(F\) therefore proves
\[
\boxed{
\gamma_B^{\rm full}(\beta;\eta)
\le
\frac{\mathbb E_{\beta,\eta}\|Q_e^\eta F\|_{\rm HS}^2}{q}
\le2\,\mathbb E_{\beta,\eta}(1-\phi_p).}
\tag{GR3}
\]
The predictor uses the actual retained links; it is not fitted to a presumed gap.

At identity exterior, \(V_B\ge0\) has an attainable minimum zero. Compactness and positivity of Haar measure on every open set imply concentration near this zero set as \(\beta\to\infty\). In particular the right side of (GR3) tends to zero.

An elementary quantitative version needs no classification of the flat set. Let \(D=(q^2-1)|B|\). A product exponential chart around all-identity links has \(V_B(X;\mathbf1)\le C_B|X|^2\); its ball of radius proportional to \(\beta^{-1/2}\) gives
\[
Z_{\beta,\mathbf1}\ge c_B\beta^{-D/2},\qquad 0<c_B\le1
\]
for sufficiently large \(\beta\). Relative-entropy positivity against normalized product Haar yields
\[
0\le D(\mu_{\beta,\mathbf1}\Vert dU_B)
=-\beta\mathbb E_{\beta,\mathbf1}V_B-\log Z_{\beta,\mathbf1}.
\]
Consequently
\[
2\mathbb E_{\beta,\mathbf1}(1-\phi_p)
\le\frac{D\log\beta-2\log c_B}{\beta}
=O_B(\log\beta/\beta).
\tag{GR4}
\]
This is not a sharp \(O(1/\beta)\) claim.

Identity exterior itself has measure zero, but the obstruction is not confined to that point. For each finite \(\beta\), the expectation in (GR3) is continuous in the finitely many relevant exterior links. The exterior marginal has full support. Taking positive-measure neighborhoods of identity and then shrinking them gives
\[
\boxed{
\Gamma_B^{\rm full}(\beta):=
\operatorname*{ess\,inf}_{\eta}\gamma_B^{\rm full}(\beta;\eta)
\le2\mathbb E_{\beta,\mathbf1}(1-\phi_p)\longrightarrow0.}
\tag{GR5}
\]
No continuity theorem for the spectral gap is used. Thus the fixed-\(n\ge3\) **full-carrier** threshold \(\Gamma_B^{\rm full}>1/n\) eventually fails. The constants are patch dependent; this does not rule out growing patches, different auxiliary normalization, or other criteria.

The witness is gauge dependent: averaging its interior endpoint annihilates it. It is not a physical state becoming massless, nor an obstruction to the gauge-invariant patch criterion below. The related [[compact-su2-fisher-calibration|compact conditional calibration]] likewise distinguishes fixed Haar marginals from vanishing innovation response, but does not itself supply the Wilson argument (GR3).

## An exact completion that leaves invariant dynamics unchanged

On one finite gauge-invariant law \(\mu\), let \(A_v\) Haar-average the gauge action at vertex \(v\). Distinct vertex actions commute, including on shared links where they act from opposite ends. Thus
\[
A=\prod_vA_v,\qquad
G_{\rm orb}=\sum_v(I-A_v),\qquad
G_{\rm orb}\ge I-A,
\tag{GR6}
\]
where \(A\) projects onto \(\mathcal H_{\rm inv}=L^2(\mu)^{G^V}\). Every coordinate conditional expectation is equivariant, so \(H_{\rm hb}\) commutes with every \(A_v\).

For any auxiliary rate \(a>0\), define
\[
\widehat H_a=H_{\rm hb}+aG_{\rm orb}.
\]
The orthogonal decomposition into invariant and noninvariant carriers reduces this operator:
\[
\widehat H_a|_{\mathcal H_{\rm inv}}
=H_{\rm hb}|_{\mathcal H_{\rm inv}},\qquad
\widehat H_a|_{\mathcal H_{\rm inv}^{\perp}}\ge aI.
\tag{GR7}
\]
In particular, for \(0<\gamma\le a\),
\[
\boxed{
\widehat H_a\ge\gamma(I-P_0)
\quad\Longleftrightarrow\quad
H_{\rm hb}|_{\mathcal H_{\rm inv}}
\ge\gamma(I-P_0)|_{\mathcal H_{\rm inv}}.}
\tag{GR8}
\]
The full positive semigroups also agree exactly on invariant observables. These are legitimate reversible auxiliary refresh dynamics with the same stationary law, not a new field or a change of the Wilson density.

The freely chosen \(a\) cannot set any invariant-sector gap. [[contemporary-puzzles/yang-mills-mass-gap/gauge-dirichlet-trace-carrier#Gauge averaging is a projection to the carrier, not its defect|Gauge averaging has the wrong kernel to be a physical gap operator]]: its defect kills all invariant excitations. Here that property is precisely why it can complete the redundant directions without altering the intended dynamics.

## Reduce inside a patch, not separately at its boundary

Let \(K_B\) be the product of gauge groups at vertices whose entire incident star lies in \(B\). These transformations preserve every frozen exterior. Let
\[
\mathcal K_{B,\eta}=L^2(\mu_{\beta,\eta})^{K_B},\qquad
h_{B,\rm inv}^{\eta}=h_B^\eta|_{\mathcal K_{B,\eta}}.
\tag{GR9}
\]
Its kernel consists of constants, because the full patch operator already has that kernel at finite positive density. A sufficient input is
\[
h_{B,\rm inv}^{\eta}\ge
\gamma_n^{\rm int}(I-P_{\mathbf1}^{\eta})
\quad\text{essential-uniformly in }\eta\text{ and patch translates}.
\tag{GR10}
\]
Equivalently, for any \(a\ge\gamma_n^{\rm int}\), one may prove the same bound on the full conditional carrier for
\[
\widehat h_{B,a}^{\eta}
=h_B^\eta+a\sum_{v:\,\operatorname{star}(v)\subset B}(I-A_v).
\tag{GR11}
\]
This is (GR8) applied to the interior gauge group. If there are no interior vertices, the completion adds nothing.

A globally invariant function restricts, at fixed exterior, to a member of \(\mathcal K_{B,\eta}\). Integrating (GR10) therefore gives
\(h_B\ge\gamma_n^{\rm int}(I-P_B)\) on the reducing global invariant carrier. There its equivalent squared inequality can be used in the original projection-counting proof, without any new overlap factors:
\[
\boxed{
\gamma_n^{\rm int}>1/n
\quad\Longrightarrow\quad
H_{\rm hb}|_{\mathcal H_{\rm inv}}
\ge\frac{n\gamma_n^{\rm int}-1}{n-1}
(I-P_0)|_{\mathcal H_{\rm inv}}.}
\tag{GR12}
\]
The full-carrier slow mode of (GR2) is not an admissible test of (GR10).

This is not permission to impose independent Gauss constraints on the regional boundary. [[gauge-boundary-frame-gluing/inq|Gauss gluing]] retains charged regional paths and pairs their boundary representations in the whole. Boundary gauge transformations generally move \(\eta\), so averaging them inside one frozen fiber need not preserve its law and can discard global loop information.

There is also a useful distinction between a sufficient regional carrier and the exact fiber of global observables. A restriction of a global invariant function is invariant under the full exterior stabilizer
\[
\mathscr G_\eta=\{g:g\cdot\eta=\eta\},
\]
not just \(K_B\). This can be a stricter condition. For an \(SU(2)\) triangle with two patch edges, interior invariance retains an arbitrary function of their open path product; the exterior stabilizer still conjugates the completed loop, whose global observables are class functions. Thus (GR10) is a valid sufficient hypothesis without claiming these two spaces always coincide.

Maximal-tree coordinates can help express that stabilizer, but they do not independently close every loop. [[library/deformation-quantization-and-homological-reduction-of-a-lattice-gauge-model/inq|Pflaum--Rudolph--Schmidt, Section 2]] identify the pointed finite-graph quotient with \(G^{|E|-|V|+1}\), retaining simultaneous root conjugation. This is a kinematic coordinate theorem, not a locality or spectral estimate for the pushed-forward conditional operator.

## A finite witness separating the two gaps

For one four-link \(\mathbb Z_2\) plaquette, take \(x_i=\pm1\), \(h=\prod_i x_i\), and
\(\mu_\beta(x)\propto e^{\beta h}\). Its invariant functions depend only on \(h\). With \(t=\tanh\beta\),
\[
H_{\rm hb}(h-t)=4(h-t),\qquad
\operatorname{gap}(H_{\rm hb}|_{\rm inv})=4.
\]
For a Walsh character \(\chi_S=\prod_{i\in S}x_i\),
\[
H_{\rm hb}\chi_S=|S|(\chi_S-t\chi_{S^c}).
\]
The complementary-character pairs give
\[
\boxed{
\operatorname{gap}(H_{\rm hb})=2-\sqrt{1+3t^2}\longrightarrow0,
\qquad
\operatorname{gap}(H_{\rm hb}|_{\rm inv})=4.}
\tag{GR13}
\]
The global gauge-orbit generator has floor two on its noninvariant complement. In this example
\[
\operatorname{gap}(\widehat H_a)
=\min\{4,\;2a+2-\sqrt{1+3t^2}\}.
\tag{GR14}
\]
At \(a=2\) the enlarged gap is four for every finite \(\beta\), while the invariant operator was unchanged. These exact finite-state numbers are not an \(SU(3)\) discretization or a physical mass prediction.

The [[receipts/gauge_reduced_patch_receipt.py|finite receipt]] verifies the complete plaquette spectra, gauge projections, unchanged quotient operator and compact-group complementary-path identity. [[weak-coupling-patch-threshold|The next test of (GR10)]] finds a different slow mode: a boundary-to-boundary path survives interior reduction and prevents \(\gamma_n^{\rm int}>1/n\) at sufficiently weak coupling for each fixed \(n\ge3\). A globally invariant loop test also defeats that patch threshold on the global invariant carrier for fixed \(n\ge8\). Gauge completion remains exact, but cannot accelerate these retained modes. The remaining route needs a different comparison or genuinely multiscale control, followed by physical reconstruction.

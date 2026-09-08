# Cycle Determinants and the Pure-Gauge Return

The Gaussian cycle action has a calculable restoring curvature and an exact finite-graph route to a pure Wilson gauge law. Neither gives its four-dimensional physical mass gap. A long cycle makes the curvature arbitrarily weak, while the Wilson return requires a growing number of auxiliary copies and leaves physical refinement unselected. These two controls delimit what the determinant mechanism actually supplies.

**Status: exact finite-graph identities and probability-law limits; open physical continuum construction and gap.** The Gaussian integration and closed-walk expansion belong to [[determinant-response-sewing-and-relational-rigidity|determinant–response sewing]]. The induced-gauge mechanism itself has established precedents.

## A single cycle has an exact response

Take a cycle of length \(L\ge3\), nearest-neighbor weights \(1/2\), and U(1) holonomy \(e^{i\theta}\). Gauge transformation distributes the phase uniformly. The eigenvalues of the twisted adjacency are

\[
\lambda_j(\theta)=\cos\frac{2\pi j+\theta}{L},
\qquad j=0,\ldots,L-1.
\tag{CY1}
\]

For \(0<r<1\), set \(a=\operatorname{arcosh}(1/r)>0\). The Chebyshev polynomial identity
\(\prod_j(x-\lambda_j)=2^{1-L}[T_L(x)-\cos\theta]\) gives

\[
\det(I-rP_\theta)
=2(r/2)^L[\cosh(La)-\cos\theta].
\tag{CY2}
\]

With \(\nu\) complex Gaussian copies, the normalized action is therefore

\[
\boxed{S_L(\theta)
=\nu\log\frac{\cosh(La)-\cos\theta}{\cosh(La)-1}.}
\tag{CY3}
\]

It has a compatible minimum at the flat holonomy. Its curvatures are

\[
S_L''(0)=\frac{\nu}{\cosh(La)-1}>0,
\qquad
S_L''(\pi)=-\frac{\nu}{\cosh(La)+1}<0.
\tag{CY4}
\]

Thus cycle integration really creates restoring holonomy response. Positive Gaussian precision does not imply a globally convex action. At fixed \(r,\nu\), the positive curvature decays exponentially as \(L\to\infty\). This is not merely a change of coordinate units: the uniform edge variation \(A_e=\theta/L\) has squared edge norm \(\theta^2/L\), so the curvature relative to that norm is \(L S_L''(0)\), which also tends to zero.

For SU(2) in the defining representation with total holonomy \(\operatorname{diag}(e^{i\theta},e^{-i\theta})\), the two conjugate determinants coincide and the action is twice (CY3). This is a finite holonomy calculation, not a theorem about the full neutral field Hamiltonian.

## Backtracking changes the zeta parameter

Let \(s=e^{-a}\), so \(r=2s/(1+s^2)\). The same cycle determinant becomes

\[
\det(I-rP_\theta)
=\frac{(1-s^Le^{i\theta})(1-s^Le^{-i\theta})}
{(1+s^2)^L}.
\tag{CY5}
\]

The nonbacktracking cycle factors use \(s\), not the original vertex parameter \(r\). On a general unweighted graph, the Ihara–Bass vertex expression also contains a degree-matrix correction. A single edge already distinguishes the raw objects: \(\det(I-qA)=1-q^2\), although there is no closed nonbacktracking prime cycle.

[[library/graph-zeta-functions-and-wilson-loops-in-a-kazakov-migdal-model/inq|Matsuura and Ohta]] treat the matrix-weighted Bartholdi determinant formula in equations (20) and (22). Its bump-counting specialization, rather than a naive same-parameter Ihara product, is the appropriate comparison to a direct adjacency determinant. Replacing the Hermitian adjacency by the generally non-self-adjoint directed-edge operator also requires a new positivity argument; it is not a harmless substitution inside a Gaussian precision.

## Many small comparisons return a Wilson law

Fix a finite open hypercubic graph in spatial notation dimension \(d\ge2\), with \(M\) vertices and edge weights \(1/(2d)\). Here \(d\) is just the graph dimension; no clock direction is yet designated. Let \(d_\rho\) be the dimension of its supplied unitary representation and set

\[
V_W(U)=\sum_p[d_\rho-\operatorname{Re}\chi_\rho(U_p)],
\qquad
b_\nu=\frac{2\nu r_\nu^4}{(2d)^4}.
\tag{CY6}
\]

The exact expansion separates the first plaquettes from all longer walks:

\[
S_\nu(U)=b_\nu V_W(U)+R_\nu(U),
\qquad
0\le R_\nu(U)
\le\frac{\nu M d_\rho}{3}\frac{r_\nu^6}{1-r_\nu}.
\tag{CY7}
\]

Indeed, odd closed walks are absent, length-two walks have trivial holonomy, and the length-four coefficient is the eight rooted orientations per plaquette divided by four. Every remaining trace difference is nonnegative and at most \(2Md_\rho\), since both adjacencies have norm at most one. Summing \(\sum_{n\ge6}r_\nu^n/n\le r_\nu^6/[6(1-r_\nu)]\) proves the bound.

Consequently,

\[
\boxed{
r_\nu\to0,\quad b_\nu\to b<\infty
\quad\Longrightarrow\quad
\mu_\nu\longrightarrow
Z_b^{-1}e^{-bV_W(U)}\prod_e dU_e
\quad\text{in total variation}.}
\tag{CY8}
\]

The convergence is uniform in the link configuration before normalization: \(\nu r_\nu^6=(\nu r_\nu^4)r_\nu^2\to0\). For SU(\(N_c\)) in the defining representation, the ordinary Wilson convention is \(b=\beta/N_c\).

The comparison also permits a growing Wilson coefficient on this fixed graph. If \(b_\nu\to\infty\) and \(\nu r_\nu^6\to0\), then the determinant law approaches the *matching varying* Wilson law in total variation. For example \(r_\nu=\nu^{-1/5}\), \(\nu\ge2\), gives \(b_\nu=2\nu^{1/5}/(2d)^4\) and a remainder tending to zero. If the bound in (CY7) is \(\epsilon_\nu\), the normalized density ratio to the matching Wilson law lies between \(e^{-\epsilon_\nu}\) and \(e^{\epsilon_\nu}\).

This supplies an alternative to forcing \(r\to1\): the auxiliary precision tends to the identity while the copy number grows. Related many-heavy-field constructions are already mentioned in [[library/howe-duality-for-an-induced-model-of-lattice-u-n-yang-mills-theory/inq|Budczies and Zirnbauer's induced-gauge paper]]. Their different finite-flavor critical construction should not be conflated with this elementary fixed-graph limit. [[library/induced-qcd-i-theory/inq|Brandt, Lohmayer and Wettig]] prove a two-dimensional return for another induced discretization and explicitly distinguish higher-dimensional conjectures.

No uniform volume estimate is claimed in (CY8): \(M\) appears in (CY7). Choosing \(\nu\) even larger can control finite boxes, but does not prove existence, nontriviality or a physical gap of the continuum Wilson theory. In the four-dimensional compact-simple Yang–Mills case, that construction remains the Clay target. The present result only shows that a blanket obstruction to a pure-gauge return from Gaussian auxiliaries would be too strong.

## The multiplication must enter the amplitude

In the graph member as currently defined, fixing the graph, \(h\), \(\rho(G)\), \(r\) and \(\nu\) fixes every link expectation. If two multiplication tensors have the same stabilizer action on that data, exchanging them changes nothing: the graph precision contains no further multiplication invariant.

This is an exact limitation of that member. It is not a limitation of Gaussian dependence on auxiliary variables. The block discrepancy \([I,-\mu]\), or a precision with coefficients depending on contractions of \(\mu\), can contain multiplication while remaining quadratic on its declared enlarged carrier. [[multiplication-reassociation-and-the-process-metric|The reassociation construction]] makes the iterated multiplication appear in an actual open amplitude. A map from those amplitudes to the graph law and its physical transfer is still missing.

## What the gauge–Higgs comparison does and does not settle

[[library/phase-diagrams-of-lattice-gauge-theories-with-higgs-fields/inq|Fradkin and Shenker]] study fixed-length Higgs fields and distinguish fundamental from other representations. Their stated analytic connection between Higgs and confinement regimes cannot, without checking hypotheses, be substituted for a theorem about every Gaussian determinant law, every faithful representation or every decoupling limit. The scalar fields must be accounted for in any claimed pure-gauge physical return.

Likewise, a small first plaquette coefficient does not bound the renormalized coupling obtained after summing every longer loop, especially near \(r=1\). Positivity and a minimum at flat connections determine features of the finite supplied density; they do not select a reconstructed quantum vacuum or prove its physical gap. Strong-coupling, constrained-amplitude and lower-dimensional models remain useful controls when their precise source hypotheses have been checked.

The research question is now sharper: can a law of multiplication and full boundary sewing select the representation, comparison multiplicities and refinement that produce the required nontrivial physical theory? Equations (CY3) and (CY8) are discriminating examples for that law, not substitutes for it.

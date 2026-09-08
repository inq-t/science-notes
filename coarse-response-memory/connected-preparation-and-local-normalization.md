# Connected Preparation and Local Normalization

The logarithm of a prepared amplitude can be decomposed into contributions indexed by sets of interactions. Contributions joining independent raw-link systems vanish exactly, while an adjacent plaquette pair first contributes its genuine relative orientation at cubic preparation order. This replaces a globally growing normalization by an exact connected assembly law. Retaining kinetic smoothing makes its local derivative sums controllable at a small interaction-to-kinetic ratio; continuing that control beyond the smallness condition remains open.

**Status: exact finite-system decomposition and evolution; uniform
connected-derivative estimate proved separately in a specified
small-interaction regime.** The graph, kinetic operator, interaction
functions and Haar preparation are supplied. This is a comparison
coordinate for their assembly, not a new derivation of those inputs.

## Compare preparations on one carrier

Fix a finite product of compact connected Lie groups \(G^E\),
with product Haar measure and supplied bi-invariant factor
metrics. Let
\[
K=-\sum_{e\in E}\kappa_e\Delta_e,\qquad \kappa_e>0.
\tag{CP1}
\]
Each smooth real interaction \(q_p\) depends on a specified raw-link
support \(E(p)\subseteq E\). For a finite family \(\Lambda\), real
couplings \(\lambda_p\), and \(B\subseteq\Lambda\), put
\[
P_B(t)=e^{-t(K-\sum_{p\in B}\lambda_pq_p)}1,
\qquad w_B(t)=\log P_B(t),\qquad t\ge0.
\tag{CP2}
\]
Strict positivity of the compact heat preparation makes the logarithm
well-defined and smooth at finite time. Every comparison uses the
**same padded kinetic operator** (CP1). Removing an interaction does
not remove its links, change their speeds or replace the reduced
kinetic operator by independently chosen loop Laplacians. Gauge-invariant
interactions keep these functions in the invariant carrier without
altering the raw-link factorization used below.

Define the finite subset transform
\[
U_C(t)=\sum_{B\subseteq C}(-1)^{|C|-|B|}w_B(t),
\qquad w_\Lambda(t)=\sum_{C\subseteq\Lambda}U_C(t).
\tag{CP3}
\]
The second identity is elementary Möbius inversion. Since
\(e^{-tK}1=1\), \(w_\varnothing=U_\varnothing=0\).
There is no infinite cluster expansion in this identity, and
no convergence assertion has been hidden in the notation.

## Independent systems have no joined contribution

Suppose \(C=C_1\sqcup C_2\), both parts nonempty, and
\(E(C_1)\cap E(C_2)=\varnothing\), where
\(E(D)=\bigcup_{p\in D}E(p)\). For every \(B\subseteq C\),
the two kinetic-plus-potential operators act on disjoint
variables. Their product heat evolution and constant initial
condition give
\[
P_B=P_{B\cap C_1}P_{B\cap C_2},\qquad
w_B=w_{B\cap C_1}+w_{B\cap C_2}.
\tag{CP4}
\]
Unused links contribute the constant factor one. Inserting
this sum in (CP3), each term contains an alternating sum over
the nonempty other family, hence
\[
\boxed{U_C=0\quad\text{whenever the interaction family }C
\text{ is raw-link disconnected}.}
\tag{CP5}
\]
The interaction graph here joins two interactions when their
raw-link supports overlap. Shared vertices alone are not
shared kinetic variables. Cross derivatives appearing after
coordinate reduction must still be retained.

This vanishing holds at every finite preparation time and
coupling, not only to some perturbative order. Accordingly,
adding independent copies leaves each anchored connected
contribution unchanged. This directly addresses
[[pointed-preparation-stability-and-the-volume-test#Independent copies defeat a global vacuum-normalized norm|the exponential growth of global pointing]].
Adding constants to the individual interaction potentials
changes only singleton terms by scalar functions of time.
An arbitrary preparation-dependent scalar normalization may
also change higher terms by spatial constants; spatial
derivatives see neither change.

## The connected law is forced by the same kinetic form

For this positive kinetic operator define
\[
\Gamma_K(f,g)=\tfrac12\{fKg+gKf-K(fg)\}
=\sum_e\kappa_e\langle\nabla_ef,\nabla_eg\rangle.
\tag{CP6}
\]
The logarithmic heat equation is
\[
\partial_tw_B=-Kw_B+\Gamma_K(w_B,w_B)
+\sum_{p\in B}\lambda_pq_p.
\tag{CP7}
\]
Substitute (CP3). In the alternating sum, a quadratic pair
\(U_A,U_D\) has coefficient
\(\sum_{B:A\cup D\subseteq B\subseteq C}(-1)^{|C|-|B|}\),
which is one when \(A\cup D=C\) and zero otherwise. Thus
\[
\boxed{
\partial_tU_C=-KU_C+\mathbf1_{C=\{p\}}\lambda_pq_p
+\sum_{\substack{A,D\subseteq C\\A\cup D=C}}
\Gamma_K(U_A,U_D),\qquad U_C(0)=0.
}
\tag{CP8}
\]
The singleton forcing means zero unless \(C\) has the displayed
single element. The quadratic sum is over ordered pairs; no
extra factor of two should be inserted. It contains terms
involving \(U_C\) itself and is not a linear recursion.
This is an exact finite assembly equation, not a proof that
an infinite hierarchy has a controlled solution.

## The first joined term retains relative orientation

For \(M=\sum_p\lambda_pq_p\), expand (CP7) from \(w(0)=0\):
\[
w=tM-\frac{t^2}{2}KM+\frac{t^3}{6}K^2M
+\frac{t^3}{3}\Gamma_K(M,M)+O(t^4).
\tag{CP9}
\]
All remainders here are in any fixed smooth norm for the
specified finite system; their constants are not claimed
uniform in volume. Subtracting the two singleton logarithms
from the pair logarithm removes the terms linear in \(M\):
\[
U_{\{1,2\}}=
\frac23\lambda_1\lambda_2\Gamma_K(q_1,q_2)t^3+O(t^4).
\tag{CP10}
\]
For [[two-plaquette-vacuum-and-relational-state|the actual adjacent squares]],
\(q_1=a,q_2=b\), and (TP4) gives
\(\Gamma_K(a,b)=\kappa z/4\). Consequently
\[
\boxed{U_{\{1,2\}}=\frac{\kappa\lambda_1\lambda_2}{6}
zt^3+O(t^4).}
\tag{CP11}
\]
The coefficient agrees with the exact coordinate Taylor
calculation underlying
[[certified-ground-marginal-and-late-preparation#The initial layer retains its cubic zero|the initial-layer certificate]].
The relative invariant \(z\) was forced by a shared kinetic
variable. Replacing the joint preparation by the product of
singletons deletes precisely this connected term.

## The remaining local estimate is not automatic

Because scalar normalizations disappear on differentiation,
the actual local prepared score satisfies exactly
\[
\nabla_ew_\Lambda
=\sum_{C:\,e\in E(C)}\nabla_eU_C.
\tag{CP12}
\]
Only interactions supported on that connected set can occur
in each summand; the finite identity requires no decay bound.
A candidate stronger obligation, for bounded-degree graph
families and fixed coefficients, is to prove for some
\(\mu>0\)
\[
\sup_{\Lambda,\,t\ge0,\,e}
\sum_{\substack{C\ \mathrm{connected}\\e\in E(C)}}
e^{\mu\operatorname{diam}C}
\left(\|\nabla_eU_C(t)\|_\infty
+\sum_{f\in E(C)}\|\nabla_f\nabla_eU_C(t)\|_\infty\right)
<\infty.
\tag{CP13}
\]
Only connected sets enter, by (CP5). Use their induced
overlap-graph diameter, zero for a singleton, and
the supplied product connections and norms. This is an
**sufficient control target**, not a necessary condition for
a gap. [[kinetic-smoothing-and-connected-fourier-control|The kinetic Fourier estimate]]
now proves it for the actual preparation under its explicit
small source condition. Its nonabelian Casimir denominators
control derivative activity before supports are summed.
It also gives exponential stability of a local score under
removal of distant interactions. Changing cutoff-dependent
coefficients still requires a separate scaling analysis.

The existing [[algebra/partial-bochner-and-ground-state-score|partial Bochner estimate]]
bounds the total one-link ground score without an explicit
vacuum, but not this sum of connected derivative norms or
its mixed-Hessian term. Positivity of the kinetic form and
(CP5) alone likewise supply no bound on connected sets of
large diameter. A connected estimate must still be compared
with the actual conditional covariance and spectral response.
[[boundary-interaction-and-conditional-score-budget#The exact defect is differentiation against forgetting|The differentiation--forgetting identity]]
specifies that bridge; an upper response estimate alone is
not a lower mass bound.
[[kinetic-hessian-bootstrap-and-uniform-response|The direct Hessian bootstrap]]
supplies a complementary uniform conditional-response bound
in a stated small \(SU(2)\) regime, without using connected
summability as an assumption.

## Connectedness is not nonassociativity

The full transform (CP3) is invertible and forgets nothing;
pointwise multiplication and heat-operator composition remain
associative. \(\Gamma_K\) measures the failure of a second-order
kinetic operator to obey a first-order Leibniz rule, not a
multiplication associator. A projection discarding connected
data could define a different retained product, but that
product and projection would have to be specified first.
[[algebra/octonionic-associator-and-branch-forgetting|The octonionic comparison]]
owns that separate question. Neither nonlinear evolution nor
the nonzero joined term (CP11) identifies its multiplication
defect with the present kinetic and readout defects.

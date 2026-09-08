# Normalized Fusion Actions

A family of state-preserving completely positive operations can realize normalized fusion identities on one observable algebra. Its GNS contractions then rescale to an algebraic fusion representation, but categorical property \((T)\) applies only after annular or tube admissibility is proved. A selected Kazhdan average has a dimensionless edge above its invariant vectors; identifying those vectors with a physical vacuum and comparing the defect with clock energy are further constructions.

## State-preserving fusion operations

Let \(\mathcal C\) be a rigid \(C^*\)-tensor category with simple unit,
irreducible labels \(\alpha\), fusion multiplicities
\(N_{\alpha\beta}^{\ \ \gamma}\), and intrinsic dimension \(d(\alpha)\).
On a von Neumann algebra \(\mathcal A\) with faithful normal state
\(\omega\), choose normal unital completely positive maps
\(\Phi_\alpha:\mathcal A\to\mathcal A\) preserving \(\omega\).
Require the [[measured-response-carriers/measured-operations-and-gns-defects|measured-operation adjoint]] for each label:

\[
\omega\!\left(a^*\Phi_\alpha(b)\right)
=
\omega\!\left(\Phi_{\bar\alpha}(a)^*b\right),
\qquad a,b\in\mathcal A.
\]

Thus \(\Phi_\alpha^\sharp=\Phi_{\bar\alpha}\). The existence of this
normal UCP adjoint is a substantive hypothesis for a nontracial state.
Require also \(\Phi_{\mathbf1}=\operatorname{id}\) and

\[
\Phi_\alpha\Phi_\beta
=
\sum_\gamma
\frac{N_{\alpha\beta}^{\ \ \gamma}d(\gamma)}
{d(\alpha)d(\beta)}
\Phi_\gamma.
\tag{MC22}
\]

The coefficients are nonnegative and sum to one because \(d\) is a fusion
character. This is a normalized fusion action by measured operations. The
formula specifies the CP maps and their multiplication; it does not by
itself construct an action on categorical intertwiners or annular data.

## GNS fusion representation and tube admissibility

On the standard GNS carrier
\((\mathcal H_\omega,\Omega_\omega)\), put

\[
V_{\Phi_\alpha}(a\Omega_\omega)
:=
\Phi_\alpha(a)\Omega_\omega.
\]

The measured-operation theorem makes these contractions fixing
\(\Omega_\omega\), with
\(V_{\Phi_\alpha}^*=V_{\Phi_{\bar\alpha}}\). Their composition obeys
(MC22), so

\[
\Theta([\alpha]):=d(\alpha)V_{\Phi_\alpha}
\tag{MC23}
\]

is an algebraic fusion-\(*\)-representation. Indeed, multiplication by
\(d(\alpha)d(\beta)\) cancels the normalization in (MC22), while the
adjoint identity implements fusion conjugation. No gap theorem enters
this step.

To invoke categorical property \((T)\), require \(\Theta\) to be
unitarily equivalent to the weight-zero restriction of a nondegenerate
full annular or tube-algebra representation, possibly on a larger graded
Hilbert space. [[library/annular-representation-theory-for-rigid-c-star-tensor-categories/inq|Annular representation theory]]
identifies this with Popa--Vaes admissibility. It is an additional
positivity and extension condition, not a consequence of the CP identities
in (MC22). Admissibility depends on the tensor category, not just its
fusion ring.

## A categorical averaging edge

For a symmetric finitely supported probability measure \(\mu\) on the
simple objects, set

\[
\Phi_\mu:=\sum_\alpha\mu_\alpha\Phi_\alpha,
\qquad
V_\mu:=\sum_\alpha\mu_\alpha V_{\Phi_\alpha},
\qquad
\mu_{\bar\alpha}=\mu_\alpha.
\tag{MC23a}
\]

Then \(\Phi_\mu\) is state-preserving UCP and \(V_\mu\) is a
self-adjoint contraction. To use the universal categorical averaging
theorem, choose a nonempty finite symmetric tensor-generating set
\(S\subset\operatorname{Irr}(\mathcal C)\setminus\{\mathbf1\}\),
strictly positive symmetric weights \(\nu\), and

\[
Z_{S,\nu}:=\sum_{\alpha\in S}\nu(\alpha)d(\alpha),
\qquad
\mu_\alpha:=\frac{\nu(\alpha)d(\alpha)}{Z_{S,\nu}},
\qquad
h_{S,\nu}:=\frac1{Z_{S,\nu}}\sum_{\alpha\in S}\nu(\alpha)[\alpha].
\]

Thus \(V_\mu=\Theta(h_{S,\nu})\). The fixed vectors are the joint
invariants of the fusion action. For an admissible representation,
[[library/property-t-discrete-quantum-groups-and-subfactors-with-triangle-presentations/inq|Vaes--Valvekens, Lemma 3.3]]
identifies property \((T)\) with an isolated trivial endpoint for this
selected average. If, in addition,

\[
\operatorname{Fix}(V_\mu)
=
\{\xi:V_{\Phi_\alpha}\xi=\xi\text{ for every }\alpha\}
=
\mathbb C\Omega_\omega,
\]

then the represented Kazhdan projection is \(P_{\Omega_\omega}\), and

\[
I-V_\mu
\geq
\kappa_{\mathcal C}(I-P_{\Omega_\omega}),
\qquad
\kappa_{\mathcal C}=\kappa_{\mathcal C,S,\nu}>0.
\tag{MC24}
\]

The numerical edge depends on the chosen generating set and weights. For a
single self-dual simple tensor generator \(X\), the choice
\(\mu=\delta_X\) requires verification of those generating hypotheses and
the corresponding universal Kazhdan estimate; an arbitrary fusion element
does not inherit that estimate merely from its name.

## The edge has no clock

Equation (MC24) is a Hilbert-space defect bound. State preservation supplies
a normalizable fixed vector, while vacuum-only invariance and identification
of the GNS carrier with the full intended physical carrier must be proved
separately. An abstract realization on some factor does not select a
physical net, state, or regulator family.

[[measured-response-carriers/lazification-and-clock-calibration|Lazification]]
can turn the self-adjoint average into a positive contraction, and
[[measured-response-carriers/observable-bkm-gap-transfer|Markov gap transfer]]
can move its decay bound to observable information norms under the stated
semigroup hypotheses. Neither construction turns the iteration or Markov
parameter into physical time, or identifies observable scores with state
tangents. A physical mass bound still requires
[[measured-response-carriers/response-to-energy-comparison|a same-core energy comparison]],
complete physical coverage, and an independently normalized duration or
localization width.

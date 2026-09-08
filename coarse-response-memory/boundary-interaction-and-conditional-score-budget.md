# Boundary Interaction and Conditional Score Budget

Coupling two regions deforms their product vacuum and introduces conditional score fluctuations that neither region retains alone. For a finite Wilson Hamiltonian, the crossing interaction pays for both that deformation and the lowering of the vacuum energy. An exact Fisher decomposition separates changes of the regional marginals from genuinely relational response. The resulting upper bound counts crossing plaquettes, not the volume of either region; it controls integrated response, not yet the stronger energy-domain multiplier needed for a uniform gap argument.

**Status: [EXACT] under the finite compact-product hypotheses below; [NUMERICAL DIAGNOSTIC] for the displayed two-plaquette values; [OPEN] for boundary-uniform form control and the Clay limits.** The Hamiltonian and its metric remain supplied data. This is a ground-state transform and conditional-score identity, not a new definition of mass or a claim of novel general Fisher calculus.

## Cut the raw links, not the separately neutral observables

Partition the links of a finite open cubical graph into disjoint sets
\(E=A\sqcup B\). Work on the raw product carrier
\[
\mathcal H=L^2(SU(2)^A,dU_A)\otimes L^2(SU(2)^B,dU_B),
\qquad Q=-2\operatorname{Tr}.
\tag{BC1}
\]
The normalized Haar measures and the product Riemannian metric are
part of the data. The physical gauge-invariant subspace sits inside
this carrier. It is not identified with a tensor product of
separately gauge-neutral regional spaces. The
[[gauge-boundary-frame-gluing/inq|boundary-frame construction]]
explains why regional boundary transformation data must remain
available for global pairing.

Let \(H_A,H_B\) contain the kinetic terms of their own links and
the plaquettes lying wholly in their respective link sets. For
\(\kappa>0\), \(\lambda\ge0\), put
\[
\begin{aligned}
H_{\rm full}&=\kappa\sum_{e\in E}D_{Q,e}
             +\lambda\sum_p(1-q_p),
&q_p&=\tfrac12\operatorname{Tr}\operatorname{Hol}_p,\\
H_{\rm dec}&=H_A\otimes I+I\otimes H_B,
&\phi&=\phi_A\phi_B,
\end{aligned}
\tag{BC2}
\]
where \(\phi_A,\phi_B\) are the normalized positive regional
ground vectors. All these elliptic operators have their inherited
compact-product \(H^2\) domains and \(H^1\) form domains. Their
ground vectors are smooth and strictly positive; uniqueness makes
them gauge invariant. Denote the ground energies by
\(E_{\rm full}\) and \(E_{\rm dec}=E_A+E_B\), and the full
ground vector by \(\psi\).

Write \(\partial\) for the plaquettes touching both link sets and
\(N_\partial=|\partial|\). For a clean comparison subtract only
their constant terms:
\[
H=H_{\rm full}-\lambda N_\partial=H_{\rm dec}+W,
\qquad W=-\lambda\sum_{p\in\partial}q_p,
\qquad E=E_{\rm full}-\lambda N_\partial.
\tag{BC3}
\]
This shift changes no vacuum vector or spectral gap. It must not
be omitted when comparing energies of the coupled and decoupled
systems.

## The crossing interaction has an exact energy budget

Define the relative half-density score and its energy by
\[
u=\log(\psi/\phi),\qquad \rho=\psi^2,
\qquad R=\kappa\int|\nabla u|^2\rho\,dU.
\tag{BC4}
\]
The ground-state transform of \(H_{\rm dec}\) gives
\[
\boxed{
R=\langle\psi,(H_{\rm dec}-E_{\rm dec})\psi\rangle
 =E-E_{\rm dec}-\langle W\rangle_\rho\ge0.
}
\tag{BC5}
\]
Indeed, write \(\psi=\phi e^u\), integrate the kinetic term
by parts, and use \(H_{\rm dec}\phi=E_{\rm dec}\phi\).
The remaining term is \(\kappa\phi^2|\nabla e^u|^2\).
This proof uses no lower bound on an excited spectrum.

Every crossing square satisfies
\(\langle q_p\rangle_{\phi^2}=0\). Around its boundary choose
a transition vertex at which exactly one incident square edge
belongs to \(A\). Apply the center element \(-I\) as a gauge
transformation to the \(A\)-region at that vertex, leaving the
\(B\)-links fixed. It preserves Haar measure and \(\phi_A^2\),
but reverses the sign of \(q_p\). Edges elsewhere in the
\(A\)-region may also transform; invariance of its whole vacuum
law is what licenses this argument.

[[product-boundary-frames-and-crossing-susceptibility|A full transition-vertex average]]
strengthens this sign test: the crossing holonomy is Haar under
the product reference, and its actual neutral inverse response
has a lower bound independent of internal coupling. The
infinitesimal cost is therefore not removed by solving the two
regions exactly before coupling them.

Testing \(H\) on \(\phi\) therefore gives \(E\le E_{\rm dec}\).
With \(\delta=E_{\rm dec}-E\), (BC5) becomes
\[
\boxed{
\lambda\sum_{p\in\partial}\langle q_p\rangle_\rho
 =R+\delta,\qquad
R,\delta\ge0,\qquad R+\delta\le\lambda N_\partial.
}
\tag{BC6}
\]
Thus an aggregate crossing alignment pays simultaneously for
relative vacuum deformation and the variational energy lowering.
It does not prove positivity of each separate plaquette mean.
This is a static energy comparison, not a derived law of entropy
production, irreversible time or fundamental conservation.

There is a reusable version without the Wilson sign symmetry.
For a compact product Schrödinger operator
\(H_{\rm dec}+W\) with bounded real potential \(W\), the same
argument gives
\[
0\le R\le\langle W\rangle_{\phi^2}-\langle W\rangle_\rho
\le\operatorname{osc}W.
\tag{BC7}
\]
Unequal positive link coefficients replace \(R\) by
\(\sum_e\kappa_e\int|\nabla_eu|^2\rho\).
The sharper \(\lambda N_\partial\) in (BC6) uses the stated
zero-mean property, rather than the generic oscillation bound.

## Separate marginal deformation from hidden correlation

Let \(\rho_A,\rho_B\) be the **actual** marginals of \(\rho\)
with respect to product Haar. They need not equal
\(\phi_A^2,\phi_B^2\). For the full regional readout define
\[
\begin{aligned}
P_AF&=\mathbb E_\rho[F\mid U_A],
&s_A&=\nabla_A\log\psi,\\
\bar s_A&=\mathbb E_\rho[s_A\mid U_A]
       =\tfrac12\nabla_A\log\rho_A,
&M_A(U_A)&=\operatorname{Cov}_\rho(s_A\mid U_A),\\
J_A&=\int\operatorname{Tr}M_A\,\rho_A\,dU_A,
&D_A&=\int\left|\nabla_A\log
                 \frac{\sqrt{\rho_A}}{\phi_A}\right|^2
                 \rho_A\,dU_A.
\end{aligned}
\tag{BC8}
\]
Use the analogous definitions for \(B\). The trace is the
finite-dimensional tangent-fiber trace of a covariance tensor,
not a trace-class assertion about multiplication on \(L^2\).
Product coordinates identify the tangent fiber while integrating
out the other region; no unspecified horizontal connection is
being used.

Orthogonal conditional averaging of each score gives
\[
\boxed{R=\kappa(D_A+D_B+J_A+J_B).}
\tag{BC9}
\]
For example,
\(s_A-\nabla_A\log\phi_A=(s_A-\bar s_A)
+(\bar s_A-\nabla_A\log\phi_A)\), and the two terms are
orthogonal in \(L^2(\rho)\). Combining (BC6) and (BC9),
\[
\lambda\sum_{p\in\partial}\langle q_p\rangle_\rho
 =\delta+\kappa(D_A+D_B+J_A+J_B).
\tag{BC10}
\]
All four response terms share **one** boundary budget; it cannot
be spent independently on each.

For the usual density-relative Fisher convention
\(I(p\mid q)=\int|\nabla\log(p/q)|^2p\),
\[
I(\rho\mid\phi_A^2\phi_B^2)=4R/\kappa,
\qquad I(\rho\mid\rho_A\rho_B)=4(J_A+J_B).
\tag{BC11}
\]
These are configuration-law Fisher quantities. They are neither
von Neumann entanglement entropy nor quantum Fisher information.

For \(\lambda>0\) and \(N_\partial>0\), both \(R\) and
\(\delta\) are strictly positive. Otherwise either the
ground-state transform or equality in the Rayleigh principle
would make \(\phi\) a ground vector of \(H\), forcing the
nonconstant \(W\) to be constant.

The actual vacuum is also nonproduct across this raw cut.
A factorization \(\psi=\alpha(U_A)\beta(U_B)\) would, after
division of its eigen-equation, force
\(W=W_A(U_A)+W_B(U_B)\). But integrating any crossing plaquette
over either region's **product Haar** kills it: a once-occurring
link matrix in that region has zero Haar integral. Thus both
partial Haar averages of \(W\) vanish. An additive \(W\) with
this property is zero, whereas
\(W(I,\ldots,I)=-\lambda N_\partial\ne0\).
On the connected regional products, \(J_A=0\) or \(J_B=0\)
would likewise force \(\log\psi\) to split into an \(A\)-part
and a \(B\)-part. Consequently \(J_A,J_B>0\).
None of these strict inequalities provides a uniform positive
floor as the graph, coupling or regulator changes. Positive
\(J_A\) ensures a hidden response on some raw, potentially
boundary-charged regional variation, not necessarily on a
separately neutral observable: a cut into two trees can leave
both neutral regional algebras constant.

## What this actually bounds as an operator

Let \(K=\psi^{-1}(H_{\rm full}-E_{\rm full})\psi\ge0\)
in \(L^2(\rho)\), and \(Q_A=I-P_A\). For smooth regional
\(f(U_A)\), the kinetic principal part already lies in the
readout. Its hidden part is exactly first order:
\[
B_Af:=Q_AKf=-2\kappa\langle s_A-\bar s_A,\nabla_Af\rangle.
\tag{BC12}
\]
Here \(B_A\) carries retained variations into hidden
\(L^2(\rho)\); it does not select measurement outcomes.
The covariance identity and boundary budget yield
\[
\begin{aligned}
\|B_Af\|^2
 &=4\kappa^2\int
     \langle\nabla_A f,M_A\nabla_A f\rangle\rho_A\,dU_A,\\
\|B_Af\|^2
 &\le4\kappa^2J_A\|\nabla_Af\|_\infty^2
 \le4\kappa\lambda N_\partial\|\nabla_Af\|_\infty^2.
\end{aligned}
\tag{BC13}
\]
Pairings are Hermitian and linear in the second slot; in (BC12)
the first slot is real. This is boundary-scaled control in a
gradient-sup norm.
It is not the bound \(\|B_Af\|^2\le\beta^2a_A[f]\), where
\(a_A[f]=\kappa\int|\nabla_Af|^2\rho_A\).
An integral of \(\operatorname{Tr}M_A\) does not bound its
essential supremum; gradients can concentrate on a small set
where the conditional covariance is large.

There is separately a valid, volume-scaled form estimate.
[[algebra/partial-bochner-and-ground-state-score|The partial Bochner bound]]
gives, with \(n_e\) the number of plaquettes incident to \(e\),
\[
\|B_Af\|^2\le\beta_A^2a_A[f],\qquad
\beta_A^2=\frac{4\lambda^2}{\kappa}\sum_{e\in A}n_e^2.
\tag{BC14}
\]
For a smooth whole variation \(F\), direct differentiation gives
\[
\nabla_A(P_AF)=\mathbb E_\rho[\nabla_AF\mid U_A]
       +2\operatorname{Cov}_\rho(F,s_A\mid U_A),
\qquad
\sqrt{a_A[P_AF]}
\le\sqrt{\mathcal E_A[F]}+\beta_A\|Q_AF\|.
\tag{BC15}
\]
Smooth conditional integration and \(\rho_A>0\) give a smooth
core. Approximation extends \(P_A,Q_A\) to the full form
domain, and (BC14) extends \(B_A:D(a_A)\to\operatorname{Ran}Q_A\)
continuously for the form norm. Thus
[[local-score-bounds-and-the-order-of-hidden-response#The memory law exists as a form-valued resolvent|the existing form-Schur construction]]
applies with this \(\beta_A\), not with a presumed boundary
replacement. Conditional covariance also need not inherit
unconditional gauge-induced block sparsity after \(U_A\) is fixed.

## The exact defect is differentiation against forgetting

Conditional differentiation also identifies a bounded comparison
operator, initially on smooth whole functions:
\[
\begin{aligned}
\mathcal C_A&=\nabla_AP_A-P_A\nabla_A:
 L^2(\rho)\longrightarrow L^2(\rho_A;T_A),\\
\mathcal C_AF&=2\mathbb E_\rho[(s_A-\bar s_A)F\mid U_A],\\
\mathcal C_A^*v&=2\langle s_A-\bar s_A,v(U_A)\rangle.
\end{aligned}
\tag{BC16}
\]
Here \(T_A\) denotes the complexified regional tangent bundle,
and conditional expectation on gradients is componentwise in
an orthonormal link frame. The score bound extends the initially
defined difference of unbounded operations to all of \(L^2\).
Direct conditional integration gives
\[
\boxed{\mathcal C_A\mathcal C_A^*=4M_A,\qquad
B_A=-\kappa\mathcal C_A^*\nabla_A.}
\tag{BC17}
\]
The first equality is an operator identity on regional vector
fields: \(M_A\) acts by multiplication. In particular
\(\|\mathcal C_A\|^2=4\operatorname*{ess\,sup}_{U_A}
\|M_A(U_A)\|\). This makes explicit why the integrated budget
and an operator-norm bound are different requirements.

On this full raw scalar carrier, the optimal first-energy
constant is in fact exactly
\[
\boxed{
\sup_{\substack{f\in H^1(\rho_A)\\a_A[f]>0}}
\frac{\|B_Af\|^2}{a_A[f]}
=4\kappa\operatorname*{ess\,sup}_{U_A}\|M_A(U_A)\|
=\kappa\|\mathcal C_A\|^2.
}
\tag{BC18}
\]
The upper bound is immediate from (BC13). For the reverse bound,
choose a coordinate neighborhood near a point and direction
approaching the maximal eigenvalue, and use
\(f_N(x)=\chi(x)e^{iN\xi\cdot x}\). At fixed smooth cutoff the
leading gradient is \(iN\chi\xi\); let \(N\) grow and then shrink
the neighborhood. Smoothness and strict positivity of the
marginal justify the localization. Subtracting the mean changes
neither form. Thus a capacity argument cannot bypass pointwise
covariance control while claiming this same first-order estimate.
It could instead supply a genuinely different, weaker
memory/resolvent topology.

## The physical estimate sees only the shape component

Equation (BC18) is the optimal estimate on **all raw regional
functions**. It is stronger than the corresponding estimate
on retained physical observables. Let the whole density be
gauge invariant, and restrict the whole carrier to
\(\mathcal H_{\rm phys}=L^2(\rho)^{G^V}\).
Conditional expectation commutes with this gauge action, and
\[
P_A\mathcal H_{\rm phys}=L^2(\rho_A)^{G^V}.
\]
The action on the right is restricted to the retained links.
Conversely, every such invariant regional function lifts to a
whole invariant function, so this is an equality of carriers.
The hidden space \(Q_A\mathcal H_{\rm phys}\) is not replaced
by a product of separately neutral regional spaces.

At a regular retained configuration \(a\), let
\(\mathsf G_A(a):\mathfrak g^V\to T_aG^A\) be the gauge-orbit
tangent map and put
\[
\Pi_{\rm sh}(a)=I-\mathsf G_A(a)\mathsf G_A(a)^\dagger,\qquad
M_A^{\rm sh}=\Pi_{\rm sh}M_A\Pi_{\rm sh}.
\tag{BC19}
\]
This orthogonal projection selects shape tangents normal to
the gauge orbit, not a choice of hidden transport. Gauge
covariance makes \(M_A\) an equivariant tensor, while every
invariant \(f\) has \(\nabla_Af=\Pi_{\rm sh}\nabla_Af\).
Consequently (BC13) proves the upper bound in the exact identity
\[
\boxed{
\beta_{\rm phys}^2:=
\sup_{\substack{f\in H^1(\rho_A)^{G^V}\\a_A[f]>0}}
\frac{\|B_Af\|^2}{a_A[f]}
=4\kappa\operatorname*{ess\,sup}_{a}
\|M_A^{\rm sh}(a)\|.
}
\tag{BC20}
\]
Use zero when this invariant form domain contains only constants.

For the reverse bound, work on the principal stratum, where
the quotient is smooth and its tangent lifts are precisely the
orbit-normal tangents. The principal isotropy acts trivially
on the normal slice; otherwise nearby slice vectors would have
smaller isotropy. The tensor \(M_A^{\rm sh}\) therefore descends
to the quotient. Choose a compactly supported quotient chart
and invariant functions
\(f_N=(\chi e^{iN\eta\cdot q})\circ\pi\).
Their leading gradients are \(iN\chi\,d\pi^*\eta\).
Let \(N\) grow and then localize the chart to obtain the
maximal horizontal Rayleigh quotient, just as in (BC18).
Such smooth localized functions extend by zero off their
saturated chart and lie in the original form core.

For finite \(SU(2)\) graphs this stratum has full Haar measure.
Tree gauge reduces each connected component to simultaneous
conjugation of its cycle holonomies: a tree has no shape
variable; one generic noncentral holonomy has a one-dimensional
radial quotient; two nonparallel imaginary holonomies have
only the central stabilizer. The exceptional configurations
have Haar measure zero. Smooth positive \(\rho_A\) preserves
this null-set statement. For another group or a different
measure, (BC20) requires the corresponding principal-stratum
and quotient hypotheses; it must not be extended unchanged
to a measure supported on singular orbits.

Thus the physical obligation is an estimate on
\(M_A^{\rm sh}\), not necessarily every component of \(M_A\).
No smooth projector across the singular strata is asserted,
and no bound on its derivative is used.
[[conditional-fisher-coercivity/measure-preserving-horizontal-lifts#The metric-selected gauge lift can diverge at a stabilizer|The gauge-lift test]]
shows why this matters: a chosen frame transport can diverge
at a stabilizer even when a neutral response coefficient has
a finite limit. This sharpening controls the retained-to-hidden
coupling on the stated physical subspace; it still supplies
no gap for the complementary neutral excitations.

This is the required tensor compression for the **coupling
estimate**, not a claim that the joint state is determined
by that compression.
[[radial-marginal-and-conditional-stress#Radial force retains orbit stress|The effective-force identity]]
contains a contraction of the full conditional tensor with
the retained holonomy Hessian. Its orbit contribution is
not determined even by the shape coefficient together with
the full trace.

## A complete neutral readout becomes one scalar multiplier

For the adjacent-square member, retain the left square and
write \(a=q(\operatorname{Hol}_A)\), \(h=1-a^2\). On
\(-1<a<1\), the orbit-normal tangent is spanned by
\(n_A=\nabla_Aa/\sqrt h\), since \(|\nabla_Aa|^2=h\).
Define the **unweighted** metric contraction
\(S=\langle\nabla_Aa,\nabla_A\log\psi\rangle\);
the coefficient \(\kappa\) is not included in \(S\).
For any retained physical readout \(f(a)\),
\[
B_Af=-2\kappa f'(a)(S-P_AS),\qquad
a_A[f]=\kappa\int h|f'(a)|^2\,d\rho_A.
\]
Gauge invariance makes the scalar conditional moments of
\(S\) depend only on \(a\), even when conditioning on all
four raw links. Therefore
\[
\boxed{
c(a)=\frac{4\kappa\,\operatorname{Var}(S\mid a)}{1-a^2},
\qquad
\beta_{\rm phys}^2=\operatorname*{ess\,sup}_{|a|<1}c(a).
}
\tag{BC21}
\]
Localizing \(f'\) in an interior interval proves sharpness.
This is the complete one-plaquette invariant readout family,
not only a finite polynomial test space. It is still an
upper-coupling constant, not a lower spectral edge.

The apparent endpoint division has a removable scalar limit.
In the full invariant coordinates \((a,b,z)\), put
\(z=\sqrt h\sqrt{1-b^2}\,t\), \(-1\le t\le1\). The actual
seven-link cometric gives
\[
\frac{S}{\sqrt h}
=\sqrt h\,\frac{\psi_a-b\psi_z/4}{\psi}
+\sqrt{1-b^2}\,t\,\frac{\psi_b/4-a\psi_z}{\psi}.
\tag{BC22}
\]
Derivatives here hold the other two invariant coordinates
fixed, not the relative angle \(t\). At \(a=s=\pm1\), the
limiting density is proportional to
\(\psi(s,b,0)^2\,d{\rm Haar}(b)\,dt/2\).
Its angular mean is zero and its second moment is \(1/3\).
For the smooth positive vacuum this proves
\[
\boxed{
c(s)=\frac{4\kappa}{3}
\frac{\int(1-b^2)(\psi_b/4-s\psi_z)^2\,d{\rm Haar}(b)}
{\int\psi^2\,d{\rm Haar}(b)},\qquad s=\pm1,
}
\tag{BC23}
\]
with all endpoint quantities evaluated at \((s,b,0)\).
Smooth gauge invariants admit local smooth invariant-coordinate
representatives here; equivalently their expansion in the
left holonomy's imaginary vector has a smooth linear term
parallel to the right vector, which defines \(\psi_z\).
Strict positivity keeps the denominators nonzero.
Exactly at the wall \(\nabla_Aa=0\); neither \(n_A\) nor the
random variable \(S/\sqrt h\) has a canonical value there.
Only the scalar one-sided limit (BC23) is asserted.

The existing receipt evaluates the profile and endpoint
integrals using the full joint vacuum, retaining the relative
angle. Refining the retained grid samples the complete
multiplier more directly than eight test functions; a sampled
maximum is not a certified supremum or infinite-cutoff bound.

With \(\kappa=1\), the 257-point grid including the analytic
endpoint limits has its sampled maximum at \(a=-1\):
approximately \(0.001952517397\) for \(\lambda=0.5\), and
\(0.008586613757\) for \(\lambda=1\). The corresponding
eight-polynomial Rayleigh maxima are \(0.001923415312\) and
\(0.008293765672\); those probes do not attain the sampled
full-multiplier edge. Cutoffs 6 and 8 and separate hidden
quadratures agree at fixed retained nodes, and the interior
profile approaches the independently calculated endpoint
values. No claim that the sampled maximum is the exact
continuous supremum follows.

The associated one-plaquette reference also has
[[algebra/partial-bochner-and-ground-state-score#The invariant plaquette quotient has positive weighted curvature|positive neutral quotient curvature]]
at every finite coupling, despite failure of the raw weighted
tensor. That sign proof incorporates the Haar orbit-volume
factor. It does not yet estimate the joint conditional
coefficient (BC21).

This is a **differentiation–forgetting commutator**, not a
multiplication associator. For retained functions \(f,g\),
\(P_A(fg)=fg\), so their projected product is associative.
[[algebra/octonionic-associator-and-branch-forgetting#A retained product can become nonassociative|The projected-product identity]]
locates a different possible defect when the retained range is
not a subalgebra. The octonionic positive associator response
in that note is another precisely typed construction; no map
presently identifies it with (BC17).

The next analytic obligation is precise: bound the relevant
pointwise conditional covariance by the crossing interactions,
using its shape compression (BC20) for the retained physical
estimate, or prove that the intended argument works in a
different topology.
An assumed hidden gap or spatial-decay estimate would be new
input, not a consequence of (BC10).

[[algebra/partial-bochner-and-ground-state-score#A product reference turns the force into a boundary force|The reference-weighted Bochner test]]
now supplies such a boundary form bound **conditionally** on a
positive full regional weighted-curvature tensor. Its explicit
single-plaquette test disproves automatic positivity of that
tensor at all couplings. More generally,
[[conditional-fisher-coercivity/bounded-coupling-and-conditional-score-concentration|an exact bounded-coupling family]]
has vanishing integrated cost and unbounded conditional covariance
on a fixed positive-Ricci carrier, even with coupling tending to
zero in \(C^2\). Its reference develops an explicit soft mode
and unbounded regional forces. Thus controlling the crossing
force alone is insufficient; the example does not refute a
Wilson-specific estimate also controlling the regional reference.

[[kinetic-hessian-bootstrap-and-uniform-response|The actual-preparation bootstrap]]
now supplies such a Wilson-specific estimate when the local absolute
magnetic strength obeys \(\ell/\kappa\le1/32\). It proves the
full bound \(\|\operatorname{Hess}\log\psi\|\le\delta\) and
conditional curvature \(c=1/2-2\delta\ge1/4\), rather than
assuming reference curvature. Consequently
\(M_A\le\delta^2/c\) and
\(\|B_Af\|^2\le(4\kappa\delta^2/c)a_A[f]\), uniformly for
raw regions of any size. This bound uses all local forces,
not only crossing terms, and does not contradict the
soft-reference counterexample. It does not extend unchanged
to strong magnetic coupling or an incomplete scalar join.

[[conditional-fisher-coercivity/moving-fiber-connection#The actual ground state returns coupled fiber equations|The normalized conditional-vacuum equations]]
identify \(M_A\) as the metric of the moving positive fiber
vector. The scalar equation bounds its trace at maxima of the
marginal ratio, not at its own maximum. Its positive geometric
term cancels as a separate potential after the retained ground-
state transform; the hidden coupling remains. It cannot be
inserted again as an independently derived mass.

## A genuine seven-link computation

In the [[two-plaquette-vacuum-and-relational-state|adjacent pair]],
take \(A\) to be the left square's four links, including the
shared link, and \(B\) the right square's other three links.
The latter is a tree. Consequently
\(\phi=\phi_A(a)\), where \(\phi_A\) is the ground vector
of \(4\kappa D_Q+\lambda(1-a)\); the decoupled tree vector
is constant. Using \(\phi_A(a)\phi_B(b)\) would duplicate
the shared link and is not this cut.

The raw tree marginal is Haar by gauge invariance, so \(D_B=0\).
The right-loop trace \(b\) is **not** Haar-distributed: that loop
also contains the shared link in \(A\). With \(\kappa=1\),
\(N_\partial=1\), the computed diagnostics are

| \(\lambda\) | \(R\) | \(\delta\) | \(\lambda\langle b\rangle\) | \(J_A\) | \(J_B\) |
| --- | --- | --- | --- | --- | --- |
| 0.5 | 0.02057349887 | 0.02075100171 | 0.04132450058 | 0.00513458803 | 0.01543890837 |
| 1 | 0.07935720380 | 0.08204717426 | 0.16140437806 | 0.01971063765 | 0.05964643530 |

The small but nonzero \(D_A\) values are approximately
\(2.47345\times10^{-9}\) and \(1.30847\times10^{-7}\).
[[receipts/two_plaquette_vacuum_receipt.py|The existing receipt]]
compares the full relative-score integral, the Hamiltonian matrix
expectation and the energy-difference identity independently.
It also checks (BC9), using the full mixed cometric and the
raw-tree partial kinetic form \(3D_y\). Cutoffs 6 and 8 and
independently refined quadratures agree. These are floating-point
finite diagnostics, not certified infinite-cutoff enclosures.

The foundational consequence is limited but useful: relative
vacuum information and boundary coupling are no longer freely
retunable once this full Hamiltonian and raw cut are fixed.
They satisfy (BC10). The stronger selecting problem remains:
the graph, metric and Hamiltonian are still inputs, and neither
that identity nor positive conditional response establishes the
four-dimensional translation representation or excludes soft
excitations in the continuum and infinite-volume limits.

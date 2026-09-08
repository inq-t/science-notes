# The Physical Vacuum Gives a Fisher Comparison, Not the Same Clock

Supplying the exact finite-regulator Yang--Mills vacuum to the retained-path construction does not make its Fisher-dual clock equal to physical electric evolution. It does give an exact one-sided form comparison after an explicit calibration. Local gauge symmetry makes the vacuum's parameter-Fisher tensor block diagonal by vertex, allowing the comparison constants to be controlled by local kinetic expectations rather than the box volume. This identifies a possible auxiliary role for the response without claiming that the vacuum, physical time or mass gap has been derived.

**Status: exact finite-regulator identities and form comparisons on the complete gauge-invariant carrier.** The physical Hamiltonian and its actual vacuum are supplied for this recovery test. No continuum limit or new mass gap is constructed.

## Use the actual vacuum and declare the calibration

Take a finite open three-dimensional cubical box with no periodic
edge identifications and at least one plaquette. Use
\[
H_\lambda=\kappa\sum_eD_{Q,e}
+\lambda\sum_p(1-q_p),\qquad
Q=-2\operatorname{Tr},\quad
D_Q=-\Delta_Q,\quad
q_p=\tfrac12\operatorname{Tr}\operatorname{Hol}_p,
\quad \kappa>0,\quad\lambda\ge0.
\tag{PV1}
\]
[[coarse-response-memory/interacting-gauge-vacuum-and-local-memory|The finite physical-vacuum construction]]
provides its normalized strictly positive smooth gauge-invariant
ground vector \(\psi\), ground energy \(E_0\), and density
\(w=\psi^2\) relative to product Haar. The ground-state-transformed
physical form is
\[
\mathcal E_{\rm phys}(f)
=\kappa\int\sum_e|\nabla_ef|_Q^2\,w\,dY
\tag{PV2}
\]
on invariant \(H^1\), with operator unitarily equivalent to
\(H_\lambda-E_0\).

Fix a dimensionless edge heat age \(t>0\), a path horizon \(T>0\),
and splits \(0<\theta_e<1\). Choose
\(Tc_e^U=t\theta_e\), \(Tc_e^V=t(1-\theta_e)\).
Let
\[
D_0=\operatorname{diag}_{e}(2t\theta_e,2t(1-\theta_e))
\otimes I_{\mathfrak g},\qquad
E_*=\frac{\kappa}{2t}.
\tag{PV3}
\]
The reference source response is \(2t\sum_e|\nabla_e f|^2\).
Thus \(E_*\), with the units of \(\kappa\), is the declared conversion
to the physical electric form. Neither \(t\) nor \(E_*\) is inferred
from the mass gap.

## Lift the state without pretending to construct it

Lift \(w\,dY\) through the actual paired heat bridges of
[[local-interaction-cocycle-and-global-source-response|the local interaction construction]].
On this finite graph the corresponding source potential is exactly
\[
W(Y)=\sum_e\log p_t(Y_e)-\log w(Y).
\tag{PV4}
\]
Indeed \(e^{-W(Y)}\prod_ep_t(Y_e)=w(Y)\), with normalization one.
The potential is smooth and bounded at fixed regulator. It need
not be gauge invariant or finite range, but it is invariant under
common conjugation. That is sufficient for the finite retained-path
entropy identity; the stronger gauge-invariant potential assumption
used for other endpoint-density formulas is not needed here.

Independent Haar vertex frames still have zero score. Their
readout \(x_e=B_{s(e)}Y_eB_{t(e)}^{-1}\) has precisely the physical
law \(w\,dx\), since this law is already gauge invariant. The
construction has imported \(\psi\); it has not solved the vacuum
equation by choosing (PV4).

## Haar marginals remove the reference Hessian

Every raw link has distinct endpoints. Gauge invariance makes each
one-link marginal of \(w\,dY\) Haar: rotate its source vertex and
integrate all other links, whose Haar reference measures are unchanged.
Consequently
\[
\mathbb E_w\sum_e\log p_t(k_eY_el_e^{-1})
=\sum_e\int_G\log p_t(y)\,dy
\tag{PV5}
\]
for arbitrary fixed \(k_e,l_e\). Its parameter Hessian is zero.
This step would fail for a general self-loop marginal.

For a smooth real endpoint function put
\[
p_f(Y)_e=(\nabla_{L,e}f(Y),-\nabla_{R,e}f(Y)),\qquad
\mathsf I_w=\mathbb E_w[p_{\log w}p_{\log w}^{*}].
\tag{PV6}
\]
The action \(Y_e\mapsto e^{\epsilon\xi_e}Y_e e^{-\epsilon\eta_e}\)
preserves product Haar. Integration by parts therefore gives
\[
\operatorname{Hess}_0\,
\mathbb E_w[-\log w((e^{\xi_e}Y_e e^{-\eta_e})_e)]
=\mathsf I_w.
\tag{PV7}
\]
For a single combined direction \(X\), this is
\(-\int wX^2\log w=\int w(X\log w)^2\); polarization gives the
displayed real symmetric Hessian. The mean first derivative
vanishes, so no second-order chart correction is missing.

The exact source entropy Hessian hence reduces to
\[
\boxed{
\mathsf M=D_0^{-1}+\mathsf I_w,\qquad
\mathsf B=D_0^{1/2}\mathsf I_wD_0^{1/2}\ge0,\qquad
\mathsf C=D_0^{1/2}(I+\mathsf B)^{-1}D_0^{1/2}.
}
\tag{PV8}
\]
No small-interaction hypothesis is needed at this finite regulator.
The potential Hessian here is positive after averaging because it
is the Fisher tensor of the actual physical density.

## There is an exact physical comparison and a strict clock defect

The retained-source form is
\[
\mathcal E_{\rm F}(f)
=\mathbb E_w\langle D_0^{1/2}p_f,
 (I+\mathsf B)^{-1}D_0^{1/2}p_f\rangle.
\tag{PV9}
\]
This is an integrated comparison on invariant observables; a
source tensor is not declared basic before averaging through the
readout. Positivity in (PV8) gives
\[
\boxed{
\frac{\mathcal E_{\rm phys}(f)}{1+\|\mathsf B\|}
\le E_*\mathcal E_{\rm F}(f)
\le\mathcal E_{\rm phys}(f).
}
\tag{PV10}
\]
All forms have the inherited invariant \(H^1\) domain on this
finite compact graph.

Take the legitimate invariant probe \(f=\log w\), or its centered
version. Since
\(\mathbb E_w[(D_0^{1/2}p_f)(D_0^{1/2}p_f)^*]=\mathsf B\),
\[
\boxed{
\mathcal E_{\rm phys}(\log w)-E_*\mathcal E_{\rm F}(\log w)
=E_*\operatorname{Tr}\!\left[\mathsf B^2(I+\mathsf B)^{-1}\right].
}
\tag{PV11}
\]
The right side is strictly positive when \(w\) is nonconstant:
then \(p_{\log w}\) is not identically zero, so
\(\mathsf B\ne0\). For \(\lambda>0\) in (PV1), a constant ground
vector would make the nonconstant magnetic potential constant
through the eigenvalue equation, which is impossible.

Thus the same exact state does not identify the two clocks at the
declared calibration. Nevertheless the inequality has the useful
direction: a lower Poincare bound proved for \(E_*\mathcal E_{\rm F}\)
in this same vacuum norm would also bound the physical form below.
The trace defect is not itself such a Poincare bound.

## Gauge symmetry makes the comparison volume-uniform

Anchor the \(U_e\) slot at \(s(e)\) and the \(V_e\) slot at \(t(e)\).
For invariant \(f\), its slot cotangent transforms by
\[
p_f(g\cdot Y)_i=\operatorname{Ad}_{g_{v(i)}}p_f(Y)_i.
\tag{PV12}
\]
The state \(w\,dY\) is invariant under *independent* vertex gauges,
not just common conjugation. Averaging at one vertex therefore
kills a Fisher block between slots with distinct anchors:
\(\mathsf I_{w,ij}=0\) if \(v(i)\ne v(j)\).
Thus \(\mathsf B=\bigoplus_v\mathsf B_v\).
This is a covariance identity of the physical state, not a
factorization of that state across vertices.

It also strengthens the pointwise statement in (PV9). The slot
rotations in (PV12) commute with \(D_0\) and \(\mathsf B\), so the
contracted response is gauge invariant before integrating. This
is proved for the prepared physical vacuum; it must not be
assumed for the general common-conjugation-invariant source.

At a fixed vertex, the real adjoint representation of \(SU(2)\)
is the three-dimensional irreducible rotation representation.
Each intertwining block is a real scalar times \(I_3\).
Hence \(\mathsf B_v=\mathsf M_v\otimes I_3\), with
\(\mathsf M_v\ge0\), and
\(\|\mathsf B_v\|\le\operatorname{Tr}(\mathsf B_v)/3\).

Let \(n_e\) count elementary plaquettes incident on link \(e\).
The one-link variational comparison in
[[coarse-response-memory/interacting-gauge-vacuum-and-local-memory#Uniform upper bounds from one-link comparisons|the actual-vacuum bound]]
gives
\[
\mathbb E_w|p_{\log w,i}|^2
=4\langle D_{Q,e}\rangle_\psi
\le4(\lambda/\kappa)n_e.
\tag{PV13}
\]
Set \(\omega_{ve}=\theta_e\) at the source and
\(\omega_{ve}=1-\theta_e\) at the target. Using \(d_i=2t\omega_{ve}\)
in the trace estimate yields
\[
\boxed{
\|\mathsf B\|
\le C_{\rm vac}:=
\frac{8t}{3}\frac{\lambda}{\kappa}
\max_v\sum_{e\ni v}\omega_{ve}n_e
\le64t\,\frac{\lambda}{\kappa}.
}
\tag{PV14}
\]
An open three-dimensional cubical box has degree at most six and
\(n_e\le4\), giving the last bound. For equal splits
\(\theta_e=1/2\), it improves to \(32t\,\lambda/\kappa\).
No factor counting all links or plaquettes appears.

Combining (PV10) and (PV14) supplies a two-sided comparison,
uniform over these finite spatial boxes:
\[
\boxed{
\frac{\mathcal E_{\rm phys}}{1+C_{\rm vac}}
\le E_*\mathcal E_{\rm F}\le\mathcal E_{\rm phys}.
}
\tag{PV15}
\]
This holds at every fixed finite \(\lambda/\kappa\) and \(t\).
It proves neither a uniform positive Poincare constant nor a
nontrivial limit of the vacua. The constant is not uniform as
\(\lambda/\kappa\) diverges with \(t\) held fixed.

## The score energy is a plaquette-corner response

There is a stronger comparison using the actual vacuum equation.
Set \(u=\log\psi\), and let \(r_{i,a}\) be the components of
\(p_u\) in the endpoint slots of (PV6). Define the real matrices
\[
\mathsf G_{ia,jb}=\mathcal E_K(r_{i,a},r_{j,b}),\qquad
\mathsf C_{ia,jb}=\mathbb E_w(r_{i,a}r_{j,b}),
\quad \mathsf I_w=4\mathsf C.
\tag{PV16}
\]
Here \(K=\psi^{-1}(H_\lambda-E_0)\psi\) acts on the **raw**
\(L^2(w)\) carrier, not only its neutral physical subspace.
The scores are centered and adjoint-charged at their anchors.
The same independent gauge averaging as in (PV12) makes both
matrices block diagonal by vertex, with scalar Lie blocks.

The [[algebra/partial-bochner-and-ground-state-score#Killing derivatives give an exact energy-weighted response|Killing-score sum rule]]
identifies \(\mathsf G\) with one half of the averaged potential
Hessian under the endpoint controls. If \(i(p),j(p)\) are the
two slots at corner \(v\) of plaquette \(p\), and
\(\mathbf e_i\) are slot-coordinate vectors, it gives exactly
\[
\boxed{
\mathsf G_v=\frac{\lambda}{8}
\sum_{p\ni v}\langle q_p\rangle_\psi
(\mathbf e_{i(p)}-\mathbf e_{j(p)})
(\mathbf e_{i(p)}-\mathbf e_{j(p)})^{\mathsf T}
\otimes I_3,\qquad
0\le\mathsf G_v\le\lambda I.
}
\tag{PV17}
\]
To check the coefficient, the second derivative in a single slot
is \(X^2q_p=-q_p/4\). Gauge averaging makes each Lie block scalar;
the simultaneous Gauss direction at that corner annihilates
\(q_p\), fixing the off-diagonal sign. Blocks between distinct
vertices vanish by their independent adjoint actions.
For the upper bound, use \(\langle q_p\rangle\le1\),
\(|\xi_i-\xi_j|^2\le2(|\xi_i|^2+|\xi_j|^2)\), and at most four
incident plaquettes per slot. Positivity comes from the Gram
identity, not a premise that every plaquette expectation is
positive. The common Gauss slot direction is an exact kernel;
it is not the physical vacuum direction.

Let \(\mathcal G_{v,a}\) be the full vertex Gauss derivatives.
Their Casimir has value \(c_{\rm ad}=2\) on the score span,
in the declared \(Q=-2\operatorname{Tr}\) normalization.
For every smooth function \(F\) in that span,
\[
2\|F\|_w^2=\sum_a\|\mathcal G_{v,a}F\|_w^2
\le\frac{d_v}{\kappa}\mathcal E_K(F).
\]
The inequality is pointwise Cauchy--Schwarz over the \(d_v\)
incident links followed by integration. Since \(d_v\le6\),
\[
\boxed{
\mathsf C_v\le\frac{d_v}{2\kappa}\mathsf G_v
\le\frac{3\lambda}{\kappa}I,\qquad
\|\mathsf B\|\le24t\,\frac{\lambda}{\kappa}.
}
\tag{PV18}
\]
For equal splits the last constant is \(12t\lambda/\kappa\).
These replace the weaker \(64t\lambda/\kappa\) and
\(32t\lambda/\kappa\) bounds in (PV14)--(PV15), respectively;
the earlier estimates remain valid.

This also locates a legitimate inverse: \(K\) preserves each
vertex's adjoint isotypic sector and obeys \(K\ge2\kappa/d_v\)
there. Both \(Xu\) and \(XV\) belong to that sector, so
\(Xu=-K^{-1}XV\) on it does not assume the unknown **neutral**
physical gap. Gauge-invariant excitations instead have zero
Gauss Casimir, and this argument gives them no positive bound.

Neither improvement controls a pointwise conditional tensor.
Define \(M_A=\operatorname{Cov}_w(\nabla_{A,L}\log\psi\mid A)\)
in the half-density convention; subtracting a retained reference
score leaves this covariance unchanged. For constant
left-trivialized regional controls, total covariance
gives \(\mathbb E_w M_A\le\mathsf C_{A,L}\), a principal restriction
of \(\mathsf C\). But conditioning on the retained links fixes
boundary frames; the gauge averaging above is no longer internal
to each conditional fiber. The
[[algebra/partial-bochner-and-ground-state-score#Conditioning retains a divergence that averaging removes|retained divergence identity]]
records precisely what survives. An integrated bound is not
the essential-supremum bound required for arbitrary
configuration-dependent regional gradients.

## What the comparison leaves open

[[prepared-vacuum-subdivision-and-the-recovered-clock|The exact prepared-vacuum subdivision test]]
now fixes one such limit question. Pure bivalent subdivision leaves
the entire physical vacuum and Hamiltonian unchanged, but rebuilding
independent source controls dilutes the Fisher correction as
\(O(1/n)\). Its calibrated operators converge in norm resolvent to
the supplied physical operator. Thus this finite-presentation
comparison is not itself an intrinsic interacting refinement law.
Exact refinement naturality and this dilution rule would force the
correction to vanish already at the starting presentation.

This test fixes the state, observable algebra, heat ages and clock
conversion before comparing the responses. It disproves literal
clock identification for this prescribed construction, not every
possible choice of primitives or recalibration.

It also explains why a valid auxiliary response need not be rejected
merely because it is not physical evolution. What is required is a
same-carrier comparison with an explicit calibration and sufficient
control through the physical limits. The physical vacuum has been
supplied here, not derived. The required positive bound on all
centered observables, and its survival along a nontrivial
four-dimensional continuum construction, remain open.

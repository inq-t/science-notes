# Charged Link Probes and Vacuum Spectral Width

A single-link representation probe has a fixed mean electric energy under every finite Wilson vacuum, but its spectral width measures the vacuum's logarithmic gradient on that link. Independent endpoint gauge symmetry makes the entire matrix-entry family share one spectral measure. This gives an exact, all-spin and all-coupling relation between a charged readout, the actual state and its returned dynamics, without diagonalizing the charged Hamiltonian or replacing its response by a single frequency.

**Status: exact finite-graph spectral identities and upper-tail bounds
on the full raw carrier; numerical checks at one fixed plaquette
coupling.** The Hamiltonian and kinetic metric are supplied. These
charged probes are ingredients for boundary gluing, not stand-alone
gauge-invariant particles, and their moments do not prove a mass gap.
No novelty claim is made.

## The same charged readout sees one spectral law

Use a finite open \(SU(2)\) lattice graph with distinct endpoints
for every link, elementary four-distinct-link plaquettes and
\[
H=\kappa\sum_e(-\Delta_{Q,e})+
\lambda\sum_p(1-q_p),\qquad
Q=-2\operatorname{Tr},\quad \kappa>0,\quad\lambda\ge0.
\tag{CW1}
\]
Let \(\psi>0\) be its normalized gauge-invariant ground vector,
\(E_0\) its ground energy, and
\[
d\nu=\psi^2dU,\quad u=\log\psi,\qquad
L=\psi^{-1}(H-E_0)\psi
=-\kappa\sum_e(\Delta_{Q,e}+2\nabla_eu\cdot\nabla_e).
\tag{CW2}
\]
All operators below act on full raw \(L^2(\nu)\), with the
compact elliptic operator domain and weighted \(H^1\) form
domain. Smooth matrix-entry functions lie in every domain
needed for their first two spectral moments.

For spin \(j\in\{0,\tfrac12,1,\ldots\}\), put
\(d_j=2j+1\), \(c_j=j(j+1)\), and define
\[
\Phi^{e,j}_{mn}(U)=\sqrt{d_j}\,D_j(U_e)_{mn}.
\tag{CW3}
\]
Gauge invariance makes the one-link marginal exactly Haar:
rotate its source vertex and integrate the other link variables.
This is the
[[gauge-boundary-frame-gluing/physical-vacuum-lift-and-fisher-comparison#Haar marginals remove the reference Hessian|existing marginal identity]].
Thus the \(d_j^2\) entries in (CW3) are orthonormal.
For \(j>0\), they are orthogonal to the constant vacuum.

The span \(V_{e,j}\) transforms irreducibly as
\(j\otimes j^*\) under the two independent endpoint gauge groups.
The whole spectral projection \(\mathsf E_L(B)\) commutes with
those groups. Therefore its compression to \(V_{e,j}\) is
scalar, by Schur's lemma:
\[
J_{e,j}^*\mathsf E_L(B)J_{e,j}
=\sigma_{e,j}(B)I_{d_j^2}.
\tag{CW4}
\]
Here \(J_{e,j}\) is the isometric inclusion of that entry space,
and \(\sigma_{e,j}\) is a normalized positive scalar measure.
Every unit linear combination of its entries has the same
spectral measure. This does not mean that \(V_{e,j}\) is
invariant under \(L\): the spectral projection can return
from other copies of the same endpoint representation.
[[spectral-readout-and-the-visible-gap|Spectral readout]]
owns this compression-versus-reduction distinction.

Distinct endpoints are essential. A self-loop has only the
diagonal conjugation action at its vertex; the irreducibility
argument above must not be copied to it.

## The Casimir fixes the mean; the vacuum score fixes the width

Choose the \(Q\)-orthonormal frame acting by left multiplication
on link \(e\):
\[
X_af(U_e)=\left.\frac{d}{dt}f(e^{tT_a}U_e)\right|_{t=0},
\qquad T_a=-i\sigma_a/2,\quad a=1,2,3.
\]
Set \(s_a=X_au\). With this explicit frame convention, the
pointwise matrix identity is
\[
LD_j(U_e)=
\left[\kappa c_jI-2\kappa\,dD_j(s)\right]D_j(U_e),
\qquad
dD_j(s)=\sum_as_a\,dD_j(X_a).
\tag{CW5}
\]
It follows by differentiating the same supplied kinetic
operator, not by prescribing a spectral frequency.
The matrices \(dD_j(X_a)\) are anti-Hermitian and traceless.
Their invariant trace form is
\[
\frac1{d_j}\operatorname{Tr}
[dD_j(s)^*dD_j(s)]
=\frac{c_j}{3}|s|^2.
\tag{CW6}
\]
Indeed the trace form is invariant on the irreducible adjoint
three-space, while its contraction is
\(\sum_a-dD_j(X_a)^2=c_jI\).

Define the actual half-density score energy on the link,
\[
I_e=\int|\nabla_e\log\psi|^2\,d\nu
=\langle\psi,(-\Delta_{Q,e})\psi\rangle.
\tag{CW7}
\]
Averaging over the \(d_j^2\) normalized entries in (CW3)
is equivalent to the normalized Hilbert--Schmidt trace of
the matrix in (CW5). The linear drift trace vanishes.
For the centered second moment use unitarity of \(D_j(U_e)\)
and (CW6). Since (CW4) makes every entry's moments equal,
\[
\boxed{
\int E\,d\sigma_{e,j}(E)=\kappa c_j,\qquad
\int(E-\kappa c_j)^2\,d\sigma_{e,j}(E)
=\frac{4\kappa^2c_j}{3}I_e.}
\tag{CW8}
\]
These identities hold at every finite coupling, graph size
and spin. They keep all spectral channels; neither a cutoff
nor an isolated interacting eigenbranch enters the proof.

For \(j>0\), the representation-independent comparison is
\[
\frac{\operatorname{Var}_{\sigma_{e,j}}(E)}
     {\int E\,d\sigma_{e,j}}
=\frac{4\kappa}{3}I_e,
\tag{CW9}
\]
independent of \(j\). The quotient has energy units. Dividing
once more by \(\kappa\) makes it dimensionless; neither quotient
derives \(\kappa\) or selects a physical clock.

The same statement has a readout-operator form. The compressed
first moment is \(\kappa c_jI\), but its hidden response satisfies
\[
\left[(I-J_{e,j}J_{e,j}^*)LJ_{e,j}\right]^*
\left[(I-J_{e,j}J_{e,j}^*)LJ_{e,j}\right]
=\frac{4\kappa^2c_j}{3}I_e\,I_{d_j^2}.
\tag{CW10}
\]
This is a bounded operator from the finite-dimensional entry
space, although \(L\) itself is unbounded. It is the actual
second-moment defect, not a new autonomous local Hamiltonian.

## A representation-uniform upper tail, not a lower mass edge

For \(j>0\) and \(R>0\),
\[
|E-\kappa c_j|
=|\sqrt E-\sqrt{\kappa c_j}|
 (\sqrt E+\sqrt{\kappa c_j}).
\]
Hence (CW8) gives
\[
\boxed{
\sigma_{e,j}\!\left(
|\sqrt E-\sqrt{\kappa c_j}|\ge R\right)
\le\min\left(1,\frac{4\kappa I_e}{3R^2}\right).}
\tag{CW11}
\]
The center is the square root of the **mean energy**, not
the mean of \(\sqrt E\).
[[interacting-gauge-vacuum-and-local-memory#Uniform upper bounds from one-link comparisons|The actual one-link variational bound]]
supplies \(I_e\le\lambda n_e/\kappa\), where \(n_e\) counts
incident plaquettes. Consequently the right side is at most
\(\min(1,4\lambda n_e/(3R^2))\), with no graph-volume or
representation-dimension factor. It need not stay bounded
under a continuum scaling in which \(\lambda\) diverges.

At \(\lambda=0\), \(I_e=0\) and the measure is the single
electric atom at \(\kappa c_j\). For one isolated plaquette
and \(\lambda>0\), \(I_e>0\): its positive ground is a class
function of the holonomy, and the four link scores are
transported copies. If one score vanished identically,
the ground would be constant, contrary to the nonconstant
potential in its eigenvalue equation. Thus every nontrivial
spin probe on this plaquette has positive spectral variance
and spectral weight both below and above \(\kappa c_j\).

This is charged spectral broadening, not gaplessness.
Nor do the charged probes cover the neutral physical
excitation carrier. Their nonzero gauge Casimirs provide
sector-specific estimates that cannot be transferred to
the neutral sector by discarding the charge labels.

## Exact charge selection survives broadened energy

Multiplication by a fundamental link matrix coefficient is a
component of a tensor operator under its endpoint gauge groups.
On the full charged block, its only possible endpoint charge
changes are
\[
j_{s(e)}\longmapsto j_{s(e)}\pm\tfrac12,\qquad
j_{t(e)}\longmapsto j_{t(e)}\pm\tfrac12,
\tag{CW12}
\]
omitting negative spins; other vertex charges are unchanged.
This is the exact \(SU(2)\) tensor-product selection rule.
It remains true at arbitrary internal coupling because
the Hamiltonian and its positive ground remain gauge invariant.
A fixed entry is a tensor component, not an intertwiner alone.

Thus charge bandwidth can stay exact while energy bandwidth
is only quantitatively controlled. Replacing charge fusion
by a rigid energy triangle confuses these two structures.
[[first-order-lift-and-spectral-product-tails|The first-order spectral-tail theorem]]
gives a separate all-input-energy bound for these same fixed
multipliers, without a block-gap or score hypothesis.
Neither that bound nor (CW8) yet controls arbitrary two-input
multiplication in the connected nonlinear equation.

## A fixed-coupling numerical check

For one plaquette, write its ground as \(f(a)\), with
\(a=\tfrac12\operatorname{Tr}\operatorname{Hol}\) and
normalized radial Haar measure
\(d\mu_H=(2/\pi)\sqrt{1-a^2}\,da\).
Then
\[
I_e=\frac14\int(1-a^2)(f'(a))^2\,d\mu_H(a),
\qquad
4\kappa I_e=E_0-\lambda(1-\langle a\rangle).
\tag{CW13}
\]
Normalization is \(\int f^2d\mu_H=1\). The second identity
is the ground energy decomposition, independent of the
spectral-variance calculation.

The [[receipts/charged_probe_spectral_width_receipt.py|focused charged-probe receipt]]
uses the actual character Jacobi operator at \(\kappa=\lambda=1\).
It compares the two evaluations of \(I_e\) and evaluates the
matrix differential in (CW5) for several spins, checking its
mean and centered second moment. At character cutoff sixteen,
it gives \(E_0\approx0.918058176624\) and
\(I_e\approx0.0198159912184\). Independent full four-link
finite differences agree with the charged differential expression
within \(7.5\times10^{-9}\) for the tested spins
\(\tfrac12,1,2,4\). Cutoff and quadrature
refinements are numerical diagnostics, not interval tail
certificates. The all-spin and full-spectrum assertions are
the analytic identities above.

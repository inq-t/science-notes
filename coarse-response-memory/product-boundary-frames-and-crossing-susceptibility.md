# Independent Boundary Frames Do Not Weaken the Crossing Response

Replacing small blocks by their exact interacting vacua does not automatically make the remaining interface interaction weak. Independently gauge-invariant block vacua leave every genuinely crossing plaquette holonomy Haar-distributed. Its first spectral moment and its nonzero response to switching on that interaction are consequently fixed at the electric scale, regardless of internal coupling or block size. This identifies a missing joint boundary state, not a defect cured merely by projecting the product vacuum onto whole gauge invariants.

**Status: exact on finite raw compact \(SU(2)\) blocks, including
one globally neutral crossing probe and its actual ground-state
tangent.** The estimate diagnoses this product-reference strategy.
It is neither a no-go theorem for correlated block constructions
nor a continuum mass-gap result. The Hamiltonian remains supplied;
no novelty claim is made.

## Internal exactness leaves the interface frames independent

Use the [[interacting-reference-and-spectral-product-control|actual interacting reference]]
on a finite open graph. Partition its links
into disjoint blocks \(E_b\), retain the full raw carriers, and let
\[
H_{\rm ref}=\sum_bH_b,\qquad
\psi_{\rm ref}=\prod_b\psi_b,\qquad
d\nu_{\rm ref}=\psi_{\rm ref}^2dU,\qquad
L=\psi_{\rm ref}^{-1}(H_{\rm ref}-E_{\rm ref})\psi_{\rm ref}.
\tag{PS1}
\]
Each \(H_b\) has common electric coefficient \(\kappa>0\), metric
\(Q=-2\operatorname{Tr}\), and smooth real gauge-invariant internal
potential. Its normalized positive ground \(\psi_b\) is invariant
under its own vertex gauge transformations, including those at
the block boundary. Internal Wilson couplings may be arbitrary
finite nonnegative numbers. The weighted elliptic domains are
the actual \(H^2\) operator and \(H^1\) form domains.

Let \(p\) be a simple elementary square, with four distinct links
and vertices, whose links meet more than one reference block.
Put \(q=\tfrac12\operatorname{Tr}\operatorname{Hol}_p\).
At some vertex, the two incident square edges belong to different
blocks. Apply a gauge transformation \(g\) there in only one block.
The product law is invariant, but exactly one square edge changes.
For each fixed configuration the new holonomy has the form
\(A(U)g^{\pm1}B(U)\). Averaging \(g\) over normalized Haar measure
therefore proves the full marginal statement
\[
(\operatorname{Hol}_p)_*\nu_{\rm ref}=\operatorname{Haar}_{SU(2)},
\qquad
\nu_{\rm ref}(q)=0,\qquad \|q\|_2^2=\tfrac14.
\tag{PS2}
\]
This strengthens the
[[boundary-interaction-and-conditional-score-budget#The crossing interaction has an exact energy budget|crossing sign argument]]
from a zero mean to an entire holonomy law. It uses a private
block transformation, not a gauge symmetry of the coupled
Hamiltonian with the crossing term already present.

## A neutral excitation retains an electric first moment

For each link in this square,
\(|\nabla_eq|^2=(1-q^2)/4\); all other derivatives vanish.
The actual weighted Dirichlet form thus gives
\[
\langle q,Lq\rangle_\nu
=\kappa\int\sum_{e\in p}|\nabla_eq|^2\,d\nu
=\frac{3\kappa}{4}.
\tag{PS3}
\]
Consequently \(v=2q\) is a unit centered vector with spectral
probability measure \(\sigma_v\) satisfying
\[
\int E\,d\sigma_v(E)=3\kappa.
\tag{PS4}
\]
Moreover \(q\psi_{\rm ref}\) is invariant under the **whole**
vertex gauge group. This is already a neutral loop probe,
not an isolated colored state removed by the final Gauss law.
The law \(L\) commutes with that whole group, so its spectral
and inverse images remain in the same invariant sector.

All spectra here are those of a fixed compact operator with
simple constant kernel. Its centered inverse is bounded.
Jensen's inequality for \(E^{-1}\) and \(E^{-2}\), or the
corresponding spectral Cauchy--Schwarz inequalities, yields
\[
\boxed{
\langle q,L^{-1}q\rangle_\nu\ge\frac1{12\kappa},
\qquad
\|L^{-1}q\|_2\ge\frac1{6\kappa}.}
\tag{PS5}
\]
These are lower bounds on the actual response of this source,
not estimates obtained by replacing the inverse with the
inverse of the block gap.

## The exact infinitesimal cost of introducing one crossing

Vary just this crossing coupling:
\[
H(t)=H_{\rm ref}-t\lambda_\times q,\qquad \lambda_\times\ge0.
\tag{PS6}
\]
The omitted scalar \(t\lambda_\times\) would change only the
linear ground energy, not the statements below. The bounded
perturbation of a simple isolated ground state has a normalized
real analytic ground vector near zero. Choose its positive phase,
and write its ground energy as \(\mathcal E(t)\).
Differentiating the eigenvalue equation and its normalization gives
\[
\mathcal E'(0)=0,\qquad
\frac{\dot\psi(0)}{\psi_{\rm ref}}
=\lambda_\times L^{-1}q,\qquad
\mathcal E''(0)
=-2\lambda_\times^2\langle q,L^{-1}q\rangle_\nu .
\tag{PS7}
\]
The tangent is centered by normalization. It is also the first
derivative of the logarithmic relative ground amplitude at zero.
Together with (PS5),
\[
\boxed{
\|\dot\psi(0)\|_{L^2(dU)}
\ge\frac{\lambda_\times}{6\kappa},
\qquad
\mathcal E''(0)\le-\frac{\lambda_\times^2}{6\kappa}.}
\tag{PS8}
\]
Increasing internal coupling or enlarging the independent blocks
cannot make this tangent arbitrarily small at fixed
\(\lambda_\times/\kappa\). A different perturbative organization
may still succeed. These derivatives do not give a convergence
radius, an estimate at \(t=1\), or an uncancelled lower bound for
a sum of many crossing directions.

## One internal plaquette gives an exact spectral comparison

Suppose one reference block is an isolated plaquette and \(p\)
shares exactly one of its links; the other three crossing links
are Haar electric rotors in a tree block. The internal plaquette's
magnetic coupling is arbitrary. Its single-link fundamental
probe has the measure \(\sigma_{e,1/2}\) from
[[charged-link-probes-and-vacuum-spectral-width|the charged-link identity]].
Every external open-word matrix coefficient is an eigenfunction
of the three-link kinetic operator with energy \(9\kappa/4\).

Expanding \(2q\) into paired matrix entries, orthogonality of the
external entries and the scalar internal compressed measure give
\[
\sigma_{2q}=(E\mapsto E+9\kappa/4)_*\sigma_{e,1/2}.
\tag{PS9}
\]
This is an exact product spectral statement, not a truncation
to one interacting frequency. In particular,
\[
\langle q,L^{-1}q\rangle_\nu
=\frac14\int\frac{d\sigma_{e,1/2}(E)}{E+9\kappa/4},
\qquad
\frac1{12\kappa}\le\langle q,L^{-1}q\rangle_\nu
\le\frac1{9\kappa}.
\tag{PS10}
\]
The lower bound is an equality for the Haar internal block.
It is strict for positive internal plaquette coupling, since
the charged measure then has positive variance and the
integrand is strictly convex. This does not assert monotonicity
in the internal coupling. The internal state changes the spectral
width, while the crossing first moment remains \(3\kappa\).

## What a genuinely different boundary construction must change

There is also a simpler norm obstruction. The
[[charged-link-probes-and-vacuum-spectral-width#The Casimir fixes the mean; the vacuum score fixes the width|single-link Rayleigh test]]
gives \(\operatorname{gap}(L_b)\le3\kappa/4\) for every nonempty
raw block with distinct link endpoints. Full support of the
reference density gives
\(\inf_{c\in\mathbb R}\|-\lambda_\times M_q-cI\|
=\lambda_\times\).
Thus internal interactions alone cannot improve the raw gap
enough to rescue a small crossing-operator-norm/gap criterion
when \(\lambda_\times/\kappa\) is large. The actual neutral
tangent (PS8) shows why this is not just a pessimistic choice
of operator norm.

The product vector already obeys every whole Gauss constraint:
\(P_{\rm Gauss}\psi_{\rm ref}=\psi_{\rm ref}\).
Projecting it again, or merely choosing a different boundary gauge,
does not add a shared interface state. A stronger reference would
have to retain nontrivial paired boundary amplitudes or other
correlations before the remaining interaction is treated as small.
[[gauge-boundary-frame-gluing/inq|Charged gluing]] supplies the carrier
on which that is possible; it does not select those amplitudes.

The freedom left by the local states can be exhibited explicitly:
\[
d\nu_s=(1+s q)\,d\nu_{\rm ref},\qquad |s|<1.
\tag{PS11}
\]
These are smooth positive normalized whole-gauge-invariant laws.
Every individual block marginal is still exactly \(\nu_b\).
For a block touched by \(p\), hold that block fixed and average a
different block's private gauge transformation at a transition
vertex; this kills the conditional mean of \(q\). A block not
touched by \(p\) is already independent of it. Nevertheless
\[
\int q\,d\nu_s=s/4.
\tag{PS12}
\]
Thus all individual-block laws, positivity and whole gauge invariance
leave the crossing correlation independently adjustable.
This is not a family of vacua for the fixed coupled Hamiltonian.

Nor does fitting this one scalar correlation reproduce its
actual tangent. The relative half-density tangent of (PS11) is \(q/2\).
In the positive-internal-coupling example of (PS9), \(q\) has
nonzero spectral variance, so \(L^{-1}q\) is not proportional
to \(q\). For \(\lambda_\times>0\), no differentiable
reparametrization of \(s\) makes that one-dimensional ansatz
reproduce (PS7). A shared boundary law must constrain
the complete response channels, not merely the marginal states
and one measured alignment. This is the constructive
whole-to-local obligation exposed here.

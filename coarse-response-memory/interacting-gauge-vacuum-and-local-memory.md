# The Interacting Gauge Vacuum and Local Memory

A single plaquette's exact physical return depends on fluctuations of the vacuum's logarithmic score that its holonomy does not retain. This conditional variance has a local, explicitly computable leading coefficient at the Haar vacuum. One-link variational estimates also bound it uniformly in spatial volume, without knowing the interacting vacuum explicitly. These are upper bounds on short-time memory, not lower bounds on the physical spectral gap.

**Status: [EXACT] for the finite open-box identities and bounds below; [PERTURBATIVE] for the fixed-box expansion.** No uniform expansion remainder or continuum estimate is asserted.

## The actual vacuum supplies the score

Let \(E,\mathcal P\) be the links and elementary squares of a finite open three-dimensional cubical box, without periodic identifications. On \(L^2(SU(2)^E,dU)\), with normalized product Haar measure, put
\[
Q=-2\operatorname{Tr},\quad D_Q=-\Delta_Q,\quad
q_p=\tfrac12\chi_p=\tfrac12\operatorname{Tr}\operatorname{Hol}_p,
\qquad
H_\lambda=\kappa\sum_eD_{Q,e}
 +\lambda\sum_{p\in\mathcal P}(1-q_p),
\quad \kappa>0,\ \lambda\ge0.
\tag{IV1}
\]
The fundamental Casimir is \(c=3/4\). The unit-round \(S^3\) Laplacian is \(4D_Q\), so the kinetic convention in [[strong-coupling-gap-and-continuum-crossover/wilson-to-hamiltonian-vacuum-limit|the Wilson-to-Hamiltonian limit]] is \(\kappa=2\). This is its Hamiltonian limit, not an identification of a fixed-step Wilson logarithm with (IV1).

Compact ellipticity and positivity improvement give a unique normalized smooth strictly positive ground vector \(\psi_\lambda\). Gauge covariance makes it invariant; hence the raw and gauge-invariant ground energies coincide. Set
\[
d\nu_\lambda=\psi_\lambda^2dU,\qquad
\mathcal L_\lambda=-\psi_\lambda^{-1}(H_\lambda-E_\lambda)\psi_\lambda
=\kappa\sum_e\bigl[\Delta_{Q,e}
 +2D_e\log\psi_\lambda\cdot D_e\bigr].
\tag{IV2}
\]
Here \(D_e\) without a \(Q\) subscript denotes the gradient in a \(Q\)-orthonormal left frame. The generator is nonpositive and self-adjoint in \(L^2(\nu_\lambda)\). Its operator and form domains are the transported \(H^2\) and \(H^1\) domains; multiplication by the smooth positive vacuum preserves them at each fixed box. Smooth gauge-invariant functions give cores on the invariant carrier.

Retain the **entire** one-plaquette class algebra \(f(q_p)\). Let \(J_p\) be its isometric inclusion and
\(P_p^\lambda=J_pJ_p^*=\mathbb E_{\nu_\lambda}[\cdot\mid q_p]\).
This is not projection onto the span of one character. Conditioning invariant functions on the based holonomy matrix gives the same result: gauge covariance makes that conditional readout a class function.

Define the scalar score contraction
\[
S_{p,\lambda}
=\sum_{e\in p}\langle D_e\log\psi_\lambda,D_eq_p\rangle_Q.
\tag{IV3}
\]
An elementary plaquette has four distinct links, so
\(\sum_e|D_eq_p|^2=1-q_p^2\) and
\(\sum_e\Delta_{Q,e}q_p=-3q_p\).
The chain rule gives, for real smooth \(f\),
\[
\mathcal L_\lambda f(q_p)
=\kappa[(1-q_p^2)f''(q_p)-3q_pf'(q_p)]
 +2\kappa f'(q_p)S_{p,\lambda}.
\tag{IV4}
\]
Consequently the exact hidden first-drift coefficient is
\[
\boxed{\mathcal D_p[f]
:=\|(I-P_p^\lambda)\mathcal L_\lambda J_pf\|_{\nu_\lambda}^2
=4\kappa^2\mathbb E_{\nu_\lambda}
\bigl[(f'(q_p))^2\operatorname{Var}_{\nu_\lambda}
(S_{p,\lambda}\mid q_p)\bigr].}
\tag{IV5}
\]
In particular, with the unnormalized fundamental character \(\chi_p=2q_p\),
\[
\boxed{\mathcal D_p:=\mathcal D_p[2q]
=16\kappa^2\mathbb E_{\nu_\lambda}
\operatorname{Var}_{\nu_\lambda}(S_{p,\lambda}\mid q_p).}
\tag{IV6}
\]
The logarithm here is that of the vacuum vector. Replacing it by the density score \(D\log(\psi_\lambda^2)\) doubles the score and requires dividing the corresponding squared prefactor by four.

## The marginal fixes mean drift, not memory

Write the actual \(q_p\)-marginal as \(m_\lambda(q)d\mu_H(q)\), where
\(d\mu_H(q)=\frac2\pi\sqrt{1-q^2}\,dq\) on \([-1,1]\).
The pulled-back physical form is exactly
\[
\mathcal E_{p,\lambda}(f)
=\kappa\int(1-q^2)|f'(q)|^2m_\lambda(q)\,d\mu_H(q).
\tag{IV7}
\]
Integration by parts in this marginal, compared with the conditional mean of (IV4), yields
\[
\boxed{2\mathbb E_{\nu_\lambda}[S_{p,\lambda}\mid q_p=q]
=(1-q^2)\partial_q\log m_\lambda(q),\qquad -1<q<1.}
\tag{IV8}
\]
The radial domain is inherited from the compact-group form; no independent boundary condition is chosen at \(q=\pm1\). Thus the actual marginal determines the returned mean generator, but not the conditional variance in (IV5).

For the actual physical compression
\(C_t=J_p^*e^{t\mathcal L_\lambda}J_p\), the
[[spectral-readout-and-the-visible-gap|spectral-readout identity]] gives
\[
\langle f,(C_{2t}-C_t^2)f\rangle
=\|(I-P_p^\lambda)e^{t\mathcal L_\lambda}J_pf\|^2,\qquad
\lim_{t\downarrow0}\frac{\langle f,(C_{2t}-C_t^2)f\rangle}{t^2}
=\mathcal D_p[f].
\tag{IV9}
\]
Strong differentiation only requires \(J_pf\in D(\mathcal L_\lambda)\). It does not require a second operator derivative or the bounded off-diagonal block assumptions of [[inq#What the operator operates on|the general memory-kernel theorem]]. Equation (IV9) supplies its physical local coefficient, not those additional block hypotheses.

## The first interacting term counts adjacent plaquettes

Fix the box and let \(r=\lambda/\kappa\to0\). Analytic perturbation of the isolated Haar ground vector, with elliptic regularity, gives in each fixed smooth norm
\[
\psi_\lambda
=1+\frac{\lambda}{3\kappa}\sum_q q_q
 +O_{\rm box}(r^2).
\tag{IV10}
\]
Indeed each elementary \(q_q\) has electric energy \(3\kappa\), zero Haar mean, and the nonconstant part of the perturbing potential is \(-\lambda\sum_q q_q\).

For distinct plaquettes \(q\sim p\) sharing an edge \(e\), put
\[
Z_{pq}=4\langle D_eq_p,D_eq_q\rangle_Q.
\]
Distinct elementary squares in this open box share at most one edge. From (IV4) and (IV10),
\[
\mathcal L_\lambda\chi_p
=-3\kappa\chi_p+\lambda\left[
\tfrac43(1-q_p^2)+\tfrac13\sum_{q\sim p}Z_{pq}\right]
 +O_{\rm box}(\lambda^2/\kappa).
\tag{IV11}
\]
The self term is retained and contributes no hidden variance.

The following conditional moments are **Haar identities**, not identities of the interacting vacuum. For distinct neighbors \(q,r\) of \(p\), there is an edge of \(q\) outside \(p\cup r\): each other square shares at most one of \(q\)'s four edges. Multiplying that edge by the central element \(-I\) preserves all \(p\)-links, flips \(Z_{pq}\), and leaves \(Z_{pr}\) unchanged. Consequently, conditional on all \(p\)-links,
\[
\mathbb E_HZ_{pq}=0,\qquad
\mathbb E_H(Z_{pq}Z_{pr})=0\quad(q\ne r).
\tag{IV12}
\]
Conditional on the shared edge, the complementary three-link products are independent Haar variables. Quaternion coordinates therefore identify \(Z_{pq}\), up to harmless orientation signs and rotations, with \(\mathbf x\cdot\mathbf y\), where \(|\mathbf x|^2=1-q_p^2\) and the Haar vector part satisfies \(\mathbb E[y_ay_b]=\delta_{ab}/4\). Hence
\[
\mathbb E_H[Z_{pq}^2\mid p\text{-links}]
=\frac{1-q_p^2}{4},\qquad
\mathbb E_HZ_{pq}^2=\frac3{16}.
\tag{IV13}
\]
The actual density is \(1+O_{\rm box}(r)\), so its conditional expectations differ from Haar ones by \(O_{\rm box}(r)\) on these bounded smooth functions. Applying the actual \(P_p^\lambda\) in (IV6), not replacing the vacuum in advance, now gives
\[
\boxed{\mathcal D_p
=\frac{N_p}{48}\lambda^2
 +O_{\rm box}(\lambda^3/\kappa),\qquad
N_p=\#\{q\ne p:q\sim p\}
=\sum_{e\in p}(n_e-1),}
\tag{IV14}
\]
where \(n_e\) counts plaquettes incident on \(e\). An interior plaquette has \(n_e=4\), so \(N_p=12\) and the coefficient is \(1/4\). The isolated two-square calibration is \(1/48\). Locality of this leading coefficient does not make its perturbative remainder volume-uniform.

## Uniform upper bounds from one-link comparisons

No explicit solution for \(\psi_\lambda\) is needed for the next estimates. Reset one link \(e\) to its constant Haar vector and leave the reduced density matrix of the remaining links unchanged:
\(\rho'_e=|1_e\rangle\langle1_e|\otimes\operatorname{Tr}_e|\psi_\lambda\rangle\langle\psi_\lambda|\).
Other kinetic expectations and nonincident plaquettes remain unchanged; each incident \(q_q\) now has mean zero. This mixed trial state has finite energy. It need not be gauge invariant, because the actual raw ground energy equals the physical one. Variational minimality gives
\[
\kappa\langle D_{Q,e}\rangle_{\psi_\lambda}
\le\lambda\sum_{q\ni e}\langle q_q\rangle_{\psi_\lambda}
\le\lambda n_e.
\tag{IV15}
\]
Since \(\sum_{e\in p}|D_e\chi_p|^2=4(1-q_p^2)\le4\), Cauchy--Schwarz and conditional-variance contraction imply
\[
\boxed{\mathcal D_p
\le16\kappa^2\sum_{e\in p}\langle D_{Q,e}\rangle_{\psi_\lambda}
\le16\kappa\lambda\sum_{e\in p}n_e
\le256\kappa\lambda.}
\tag{IV16}
\]
This is uniform over all finite open three-dimensional boxes and all \(\lambda\ge0\).

A quadratic small-coupling bound holds when \(b_e=\lambda n_e<\kappa c\), \(c=3/4\). Let \(\Pi_e\) project link \(e\) onto constants and \(\Pi_e^\perp=I-\Pi_e\). After subtracting the incident constant \(\lambda n_e\), decompose
\[
\widetilde H=H_{\rm rest}+\kappa D_{Q,e}+V_e,\qquad
V_e=-\lambda\sum_{q\ni e}q_q,\quad
\|V_e\|\le b_e,\quad \Pi_eV_e\Pi_e=0.
\tag{IV17}
\]
The product of \(1_e\) with a ground vector of \(H_{\rm rest}\) shows
\(\widetilde E\le E_{\rm rest}\).
The projection preserves the domain of \(H_{\rm rest}+\kappa D_{Q,e}\). Thus the following compression is its self-adjoint restriction plus a bounded potential, not an assumed unbounded block decomposition. On \(\operatorname{Ran}\Pi_e^\perp\),
\(B_e=\Pi_e^\perp(\widetilde H-\widetilde E)\Pi_e^\perp\) satisfies
\[
B_e\ge\kappa D_{Q,e}-b_e
\ge\kappa c-b_e,\qquad
B_e\ge\frac{\kappa c-b_e}{c}D_{Q,e}.
\tag{IV18}
\]
These are form inequalities. The projected ground equation is
\(\Pi_e^\perp\psi_\lambda=-B_e^{-1}w_e\), where
\(w_e=\Pi_e^\perp V_e\Pi_e\psi_\lambda\) and \(\|w_e\|\le b_e\).
Therefore
\[
\langle D_{Q,e}\rangle_{\psi_\lambda}
\le\frac{c}{\kappa c-b_e}\langle w_e,B_e^{-1}w_e\rangle
\le\frac{c\,b_e^2}{(\kappa c-b_e)^2},
\quad
\boxed{\mathcal D_p\le16\kappa^2
\sum_{e\in p}\frac{c\,b_e^2}{(\kappa c-b_e)^2}.}
\tag{IV19}
\]
Only a one-link bounded perturbation and its free Casimir were used, not a global retained/hidden block decomposition. Since \(n_e\le4\), this is a volume-uniform \(O(\lambda^2)\) upper bound whenever \(\lambda/\kappa<3/16\) stays away from the endpoint.

[[gauge-boundary-frame-gluing/physical-vacuum-lift-and-fisher-comparison|The physical-vacuum Fisher comparison]]
uses (IV15) for a different purpose. Independent vertex gauge
symmetry makes the density-score covariance block diagonal by
vertex. The local kinetic bound then controls the full source
Fisher correction without a volume factor, giving a calibrated
comparison of its reconstructed form with the physical electric
form. Neither this comparison nor the local memory bound is
itself a lower spectral estimate.

The bounds (IV16) and (IV19) control one specified character's hidden drift. They neither control the whole unbounded off-diagonal map on arbitrary readouts nor provide a positive memory floor, a uniform remainder in (IV14), or long-time return estimates. At \(\lambda=0\), a single plaquette has zero hidden drift while the physical electric theory is gapped: this memory coefficient is not itself mass. The exact [[gauge-boundary-frame-gluing/holonomy-refinement-and-clock-compatibility#Individually autonomous loop readouts can have a nonautonomous join|two-plaquette free return]] also shows that separate autonomy does not imply joint autonomy.

[[local-score-bounds-and-the-order-of-hidden-response|The pointwise-score extension]]
supplies the previously missing full single-plaquette form-domain
estimate. Partial Bochner gives
\(\|\nabla_e\log\psi_\lambda\|_\infty\le\lambda n_e/\kappa\)
at every coupling and without a volume factor. It bounds the hidden
drift for every retained finite-energy function and proves conditional
projection preserves the inherited form domain. The same note also
proves why these first-order bounds do not compose under a join of
two trace algebras: a discarded mixed response supplies a hidden
second derivative. Neither result is a physical gap lower bound.

The [[gauge-boundary-frame-gluing/receipts/overlapping_plaquette_transfer_receipt.py|overlapping-plaquette receipt]] checks link derivatives, Haar moments and open-box incidence underlying (IV11)--(IV14). It does not approximate the finite-\(\lambda\) vacuum or certify a uniform perturbative expansion. The finite-box analytic arguments above, rather than the numerical checks, establish the exact score identities and bounds.

[[two-plaquette-vacuum-and-relational-state|The complete interacting pair]]
now computes that vacuum on the isolated two-square graph without
omitting its relative-angular channels. Its exact eigenvalue
equation excludes trace-only vacuum states at every positive
magnetic coupling. The complete invariant harmonic basis gives
finite-coupling values of (IV6), and its perturbative spectral
return retains two hidden rates at finite time. These tests extend
the local coefficient beyond its first Haar expansion; they do
not promote it to a uniform mass-gap bound.

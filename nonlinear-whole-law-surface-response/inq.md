---
inq.module: "nonlinear-whole-law-surface-response"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Nonlinear Whole-Law Surface Response

The flat Wilson-action Hessian cannot be the carrier of a four-dimensional
Yang--Mills gap: its two-jet is exactly a lattice Maxwell cochain Laplacian,
repeated once per color, and a gauge-invariant quadratic transverse mode has
a bridge floor that vanishes as the spatial volume grows. The viable
Copernican reversal is to integrate and glue the full nonlinear Wilson law
first, then form a bounded response on its complete \(L^2\) distinction
carrier. Finite boundary likelihoods give an exact Radon--Nikodym cocycle and
an exact frame factorization of the bridge defect; because that factorization
is the defect itself, the noncircular comparison object must instead descend
from an independently normalized Dirichlet response of the whole law.

**Status: [EXACT -- FINITE REGULATOR] for the flat-Hessian abelianization,
the soft gauge-reduced witness, the likelihood-cocycle identities, the full
likelihood-frame factorization, and the whole-heat compression; [EXACT --
TYPED] for the standard-form projection and Stinespring residue identities;
[CONDITIONAL] for the edge-measure comparison route; [OPEN] for its uniform
Wilson estimate, continuum survival, Osterwalder--Schrader reconstruction,
and Poincare mass interpretation.**

## The flat Wilson two-jet abelianizes

Let \(G=SU(N)\), put the invariant norm
\(\lVert X\rVert^2=-\operatorname{Tr}(X^2)\) on
\(\mathfrak{su}(N)\), and use the Wilson action

\[
S_W(U)
=
\beta\sum_p
\left(1-\frac1N\operatorname{ReTr}U_p\right).
\tag{NW1}
\]

Perturb the identity connection by \(U_e(t)=e^{tX_e}\). If \(d_1\) is the
oriented edge-to-plaquette coboundary, then

\[
\operatorname{ReTr}U_p(t)
=
N-\frac{t^2}{2}\lVert(d_1X)_p\rVert^2+O(t^3),
\tag{NW2}
\]

and therefore

\[
\boxed{
D^2S_W\big|_I(X,X)
=
\frac{\beta}{N}\lVert d_1X\rVert^2,
\qquad
\operatorname{Hess}_I S_W
=
\frac{\beta}{N}d_1^*d_1\otimes I_{\mathfrak{su}(N)}.}
\tag{NW3}
\]

No structure constants occur in (NW3). At a flat presentation the complete
quadratic response is the Abelian Maxwell response with a color
multiplicity. This is not merely the observation that perturbation theory
has massless gluons: the two-jet itself has forgotten the Lie bracket.

On a periodic four-dimensional lattice, write

\[
q_\mu(k)=e^{ik_\mu}-1,
\qquad
\widehat k^2
=
\sum_\mu|q_\mu(k)|^2
=
4\sum_\mu\sin^2\frac{k_\mu}{2}.
\tag{NW4}
\]

For a Fourier one-form \(v=(v_\mu)\),

\[
\sum_{\mu<\nu}|q_\mu v_\nu-q_\nu v_\mu|^2
=
\widehat k^2|v|^2-|q^*v|^2.
\tag{NW5}
\]

Thus every nonzero momentum has a longitudinal gauge zero direction and
three transverse eigenvalues \((\beta/N)\widehat k^2\); all four eigenvalues
vanish at \(k=0\). Constant commuting links are exact flat torons. For
constant noncommuting \(X_\mu\), the first nonzero term is quartic,

\[
S_W(e^{tX_\mu})
=
\frac{\beta t^4}{2N}
\sum_{\mu<\nu}\lVert[X_\mu,X_\nu]\rVert^2+O(t^5).
\tag{NW6}
\]

The non-Abelian stabilization of the zero modes is therefore invisible to
the Hessian. [[library/confinement-of-quarks/inq|Wilson's action]] supplies
the regulator, while
[[library/the-dynamics-of-zero-modes-in-lattice-gauge-theory/inq|Asano and
Nishimura]] analyze the nonperturbative toron sector and its different
\(SU(2)\) and \(SU(3)\) scaling.

## Gauge reduction leaves a soft physical witness

Deleting the longitudinal directions does not give (NW3) a uniform positive
edge. After linearized Coulomb reduction, choose a spatial transverse mode
of smallest nonzero momentum on a spatial \(M^3\) torus. Its spatial
eigenvalue is

\[
\lambda_M=4\sin^2\frac{\pi}{M}.
\tag{NW7}
\]

For one color coordinate, the quadratic Euclidean-time action is a harmonic
chain,

\[
S_M^{(2)}
=
\frac{\beta}{2N}\sum_t
\left(|x_{t+1}-x_t|^2+\lambda_M|x_t|^2\right),
\tag{NW8}
\]

whose inverse correlation length in lattice units is

\[
\omega_M
=
\operatorname{arcosh}\!\left(1+\frac{\lambda_M}{2}\right)
=
2\operatorname{arsinh}\!\left(\sin\frac{\pi}{M}\right).
\tag{NW9}
\]

If the two endpoints lie \(n\) time steps from the midpoint, the normalized
conditional-variance floor of the scalar first-chaos mode is

\[
\kappa_1(M,n)=\tanh(n\omega_M).
\tag{NW10}
\]

A colored first-chaos vector is not itself a physical singlet. Contracting
the mode over an orthonormal color basis gives the residual-adjoint-invariant
quadratic distinction

\[
F_M
=
\sum_a\left(|x^a|^2-\mathbb E|x^a|^2\right).
\tag{NW11}
\]

Its exact Gaussian bridge quotient is

\[
\boxed{
\kappa_{\mathrm{sing}}(M,n)
=
1-
\left(
\frac{2e^{-2n\omega_M}}{1+e^{-2n\omega_M}}
\right)^2
=
2\kappa_1-\kappa_1^2.}
\tag{NW12}
\]

With \(L=Ma\) and fixed physical half-depth \(\ell=na\),

\[
n\omega_M\longrightarrow\frac{2\pi\ell}{L},
\qquad
\kappa_{\mathrm{sing}}(M,n)
\sim\frac{4\pi\ell}{L}\longrightarrow0.
\tag{NW13}
\]

The overall coefficient \(\beta/N\) changes the fluctuation amplitude but
cancels from this dimensionless prediction angle. Equation (NW13) is a
no-go for the flat local two-jet, its Gaussian Schur complement, and every
continuous bounded transform \(f(\mathcal N_{\mathrm{Hess}})\) with
\(f(0)=0\). The continuum Dirichlet-to-Neumann symbol says the same thing:
its symmetric boundary eigenvalue
\(|p|\tanh(|p|\ell)\) tends to zero. Replacing the continuous transform by
the support projection would simply insert a discontinuous spectral wall
and erase the rate.

This is not a theorem that the nonlinear Wilson theory is gapless. It is a
carrier firewall: local normal curvature at one flat presentation cannot
distinguish confining Yang--Mills from a colored collection of massless
Maxwell theories. Orbit-space curvature can still contribute after the
full measure and quotient are constructed, but a
[[library/orbit-space-curvature-as-a-source-of-mass-in-quantum-gauge-theory/inq|ground-state-weighted
Bakry--Emery curvature]] is not an independent derivation until that weight
is controlled from the bare theory.

The arithmetic in (NW7)--(NW13) is checked by
[[receipts/nonlinear-whole-law-surface-response-receipt-output.txt|the
soft-mode receipt]].

## The finite likelihood cocycle retains the whole action

Let \(Y\) denote a complete midpoint or interface state and \(Z\) the retained
two-ended boundary data. After integrating every hidden bulk variable, the
finite Wilson law pushes forward to a strictly positive joint probability

\[
\mathsf R(\mathrm dy,\mathrm dz)
=
Z_{\mathrm{tot}}^{-1}e^{-S_{\mathrm{eff}}(y,z)}
m(\mathrm dy)n(\mathrm dz).
\tag{NW14}
\]

Write \(\nu\) and \(\pi\) for its two marginals and \(\beta_z\) for the
conditional law of \(Y\) given \(Z=z\). Put

\[
Z(z)=\int e^{-S_{\mathrm{eff}}(y,z)}m(\mathrm dy),
\qquad
W(y)=\int e^{-S_{\mathrm{eff}}(y,z)}n(\mathrm dz).
\tag{NW15}
\]

The boundary likelihood relative to the midpoint marginal is

\[
\ell_z(y)
:=
\frac{\mathrm d\beta_z}{\mathrm d\nu}(y)
=
\frac{Z_{\mathrm{tot}}e^{-S_{\mathrm{eff}}(y,z)}}{Z(z)W(y)}.
\tag{NW16}
\]

Consequently every pair of boundary presentations has the exact finite
Radon--Nikodym cocycle

\[
\frac{\ell_{z'}(y)}{\ell_z(y)}
=
\frac{\mathrm d\beta_{z'}}{\mathrm d\beta_z}(y)
=
\frac{Z(z)}{Z(z')}
e^{-[S_{\mathrm{eff}}(y,z')-S_{\mathrm{eff}}(y,z)]},
\tag{NW17}
\]

and these ratios multiply along \(z\to z'\to z''\). Unlike (NW3), (NW17)
contains the finite effective action at all orders. This is the precise
commutative meaning of the statement that a finite presentation change
retains information that its infinitesimal Hessian forgets.

## The likelihood frame is exactly the bridge response

Define the conditional-transport contraction

\[
K:L^2(\nu)\longrightarrow L^2(\pi),
\qquad
(Kf)(z)=\int f(y)\,\beta_z(\mathrm dy)
=\langle\ell_z,f\rangle_\nu.
\tag{NW18}
\]

It fixes constants. On the centered carrier
\(\mathcal H_0=L^2_0(\nu)\), put \(h_z=\ell_z-1\) and

\[
(Af)(z)=\langle h_z,f\rangle_\nu.
\tag{NW19}
\]

Then \(A=K|_{\mathcal H_0}\), and, as a weak operator integral,

\[
\boxed{
A^*A
=
\int |h_z\rangle\langle h_z|\,\pi(\mathrm dz),
\qquad
B_{\mathrm{surf}}
:=
I_{\mathcal H_0}-A^*A.}
\tag{NW20}
\]

The boundary Gram kernel

\[
G(z,z')=\langle h_z,h_{z'}\rangle_\nu
\tag{NW21}
\]

represents \(AA^*\), so \(G\) and \(A^*A\) have the same nonzero spectrum.
Moreover,

\[
\boxed{
\langle f,B_{\mathrm{surf}}f\rangle_\nu
=
\int\operatorname{Var}_{\beta_z}(f)\,\pi(\mathrm dz),
\qquad
\kappa_{\mathrm{br}}
=
1-\lVert A\rVert^2
=
1-\lVert G\rVert.}
\tag{NW22}
\]

Here the common fixed algebra must first be removed if it is larger than the
constants. This is the same squared Friedrichs-angle constant
\(1-c_F^2\) isolated in
[[collared-quasi-factorization-and-surface-response/inq|the collared
reduction]].

There is also an exact full score factorization. For every bounded real
\(f\), tilt each conditional bridge by

\[
\frac{\mathrm d\beta^z_{\theta,f}}{\mathrm d\beta_z}(y)
=
\frac{e^{\theta f(y)}}{\int e^{\theta f}\,\mathrm d\beta_z}.
\tag{NW23}
\]

The score at \(\theta=0\) extends to the bounded complex-linear map

\[
L_{\mathrm{br}}f(y,z)
=
f(y)-(Kf)(z),
\qquad
L_{\mathrm{br}}^*L_{\mathrm{br}}
=
B_{\mathrm{surf}}.
\tag{NW24}
\]

Thus arbitrary midpoint insertions give a complete nonparametric likelihood
frame. A finite list of endpoint scores or parameter derivatives need not.
But (NW24) is an exact identification, not an independent coercivity proof:
using this score as the proposed comparison response reduces to
\(B_{\mathrm{surf}}\geq B_{\mathrm{surf}}\).

The operator typing is now explicit:

- \(A\) operates on centered midpoint distinctions and returns their
  boundary-predictable amplitudes;
- \(A^*A\) measures recoverability from the retained boundary;
- \(L_{\mathrm{br}}\) returns the irreducible conditional residue;
- \(B_{\mathrm{surf}}\) measures squared forgetting after every boundary
  predictor has been allowed.

None of these operators selects a measurement outcome, creates a fact,
carries energy units, or supplies a clock.

## The independent response must descend from the whole law

Let \(\mu_W\) be the complete finite-cylinder Wilson law and
\(\mathcal H_W=L^2(\mu_W)\). Let \(\delta_W\) be the invariant link-gradient
derivation and

\[
\mathcal E_W(F)=\lVert\delta_WF\rVert^2,
\qquad
L_W=\delta_W^*\delta_W.
\tag{NW25}
\]

This is an auxiliary symmetric Dirichlet generator determined by the whole
Euclidean law. Its parameter is not physical clock time. For the complete
core map \(\pi_C\), define the isometry

\[
J_C:L^2(\nu_C)\longrightarrow L^2(\mu_W),
\qquad
J_Cf=f\circ\pi_C.
\tag{NW26}
\]

Two related descendants must not be conflated. First, the direct whole-heat
compression is

\[
Q^{\leftarrow}_{C,s}
=
J_C^*e^{-sL_W}J_C,
\qquad
R^{\leftarrow}_{C,s}
=
I-Q^{\leftarrow}_{C,s}.
\tag{NW27}
\]

It is a bounded self-adjoint Markov defect on the same \(L^2(\nu_C)\)
carrier as \(B_{\mathrm{surf}}\). Its stationary edge law is exactly the
pushforward of the whole heat edge law by
\(\pi_C\times\pi_C\). The family \(Q^{\leftarrow}_{C,s}\) need not be a
semigroup; no lumpability is needed for a one-step comparison.

Second, restrict the whole form to core observables,

\[
\mathcal E_C(f)=\mathcal E_W(J_Cf).
\tag{NW28}
\]

This closed Dirichlet form has a generator \(D_C\) and a genuine semigroup
\(e^{-sD_C}\). The two constructions have the same infinitesimal form,

\[
\lim_{s\downarrow0}
\frac1s\langle f,R^{\leftarrow}_{C,s}f\rangle
=
\mathcal E_C(f),
\tag{NW29}
\]

but they need not agree at finite \(s\) unless
\(J_CL^2(\nu_C)\) reduces the whole semigroup. The direct compression is the
better collared comparison object because its edge law visibly comes from
the full action; the restricted form is the better object when a genuine
local auxiliary process is required.

There is a sharper least-cost interpretation. For
\(C_s=I-e^{-sL_W}\) and a closed centered retained subspace
\(E\subset\mathcal H_W\), let \(S_E(C_s)\) be the operator short,

\[
\langle x,S_E(C_s)x\rangle
=
\inf_{y\in E^\perp}
\langle x+y,C_s(x+y)\rangle,
\qquad x\in E.
\tag{NW30}
\]

It is the least whole-law response after every hidden lift has been allowed
to relax. For a fixed \(\gamma>0\),

\[
\boxed{
S_E(C_s)\geq\gamma I_E
\iff
C_s\geq\gamma P_E.}
\tag{NW31}
\]

The Douglas range criterion gives the correctly quantified companion:

\[
\boxed{
\exists\gamma>0:\ S_E(C_s)\geq\gamma I_E
\iff
E\subseteq\operatorname{Ran}C_s^{1/2}.}
\tag{NW31a}
\]

The range inclusion does not preserve a preassigned numerical \(\gamma\); its
best value is controlled by the norm of the corresponding Douglas factor.
This branch can ignore
globally soft directions that are uniformly invisible to \(E\), but the
short need not be Markov and has no automatic edge-measure certificate.

## The smallest noncircular comparison theorem

Let \(\mathfrak r=(a,L,p,\xi,\mathfrak s)\) collect lattice spacing, spatial
volume, preparation depth, exterior data, and a proved reducing physical
sector. At fixed physical collar and midpoint depths, the next theorem is

\[
\boxed{
B_{\mathrm{surf},\mathfrak r}
\geq
\eta_*R^{\leftarrow}_{C,\mathfrak r,s_*},
\qquad
R^{\leftarrow}_{C,\mathfrak r,s_*}
\geq
\gamma_*Q_{\mathfrak r},}
\tag{NW32}
\]

with \(\eta_*,\gamma_*>0\) uniform in every component of \(\mathfrak r\).
The response depth \(s_*\) must be fixed by an action or RG normalization
independent of the unknown transfer spectrum. Equation (NW32) implies

\[
B_{\mathrm{surf},\mathfrak r}
\geq
\eta_*\gamma_*Q_{\mathfrak r}.
\tag{NW33}
\]

One concrete sufficient certificate for the first inequality compares
stationary off-diagonal edge measures:

\[
\boxed{
\mathsf J_{K_{\mathfrak r}^*K_{\mathfrak r}}^{\circ}
\geq
\eta_*
(\pi_C\times\pi_C)_*
\mathsf J_{e^{-s_*L_{W,\mathfrak r}}}^{\circ}.}
\tag{NW34}
\]

The edge-measure theorem in
[[markov-edge-measure-solder/inq|Markov Edge-Measure Solder]] then gives the
first operator inequality. A whole-law Poincare estimate

\[
L_{W,\mathfrak r}
\geq
\lambda_*(I-P_0)
\tag{NW35}
\]

would give the second with
\(\gamma_*=1-e^{-s_*\lambda_*}\). Known strong-coupling functional
inequalities establish such control only in their fixed-regulator regime,
not along the asymptotically free four-dimensional continuum trajectory.

This is deliberately stronger than a parameter Hessian and weaker than
assuming the desired transfer gap. It compares how much the actual
two-ended Wilson bridge forgets with how much an independently constructed
whole-law heat step moves the same distinction. It can fail by an explicit
sequence \(f_{\mathfrak r}\) for which the whole-law response stays positive
while the bridge residue tends to zero.

## The carrier must be complete before the cut is closed

At a gauge boundary, separate regional gauge closure erases charged edge
data and crossing-loop distinctions. The retained carrier must instead be
formed from extended boundary frames and only then diagonally glued:

\[
\mathcal H_{\mathrm{GI}}
\cong
\left(
\mathcal H_A^{\mathrm{ext}}
\widehat\otimes
\mathcal H_B^{\mathrm{ext}}
\right)^{G^\partial}
\cong
\widehat\bigoplus_\lambda
M_{A,\lambda}\widehat\otimes M_{B,\lambda^*}.
\tag{NW36}
\]

The response in (NW32) must cover paired boundary charges, every independent
cycle innovation, crossing loops, and the vacuum-relative balance block.
[[gauge-boundary-frame-gluing/inq|Boundary-frame gluing]] constructs the
carrier, while
[[gauge-cycle-innovation-filtration/inq|cycle innovations]] give a finite
complete filtration of its holonomy data. Gauge averaging itself vanishes
on the gauge-invariant carrier and cannot be the coercive response. Knots,
fluxes, and holonomies may label distinctions; the whole-law Dirichlet form
must still price all of them.

## Type III descent is projection geometry, not clock dynamics

The finite likelihood ratios in (NW17) are the commutative shadow of a
noncommutative change of faithful state presentation. Let \(M\) be a von
Neumann algebra with faithful normal state \(\varphi\), and suppose retained
and boundary subalgebras \(N_C,N_\partial\subset M\) are invariant under
\(\sigma^\varphi\). Takesaki's theorem then supplies
\(\varphi\)-preserving expectations. Their standard-form implementations
\(e_C,e_\partial\) are orthogonal projections on the one carrier
\(L^2(M,\varphi)\). With

\[
R=e_C\wedge e_\partial,
\qquad
E=(e_C-R)L^2(M,\varphi),
\qquad
K_{\mathrm{III}}=(e_\partial-R)|_E,
\tag{NW37}
\]

the trace-free surface response is exactly

\[
\boxed{
B_{\mathrm{surf}}^{\mathrm{III}}
=
I_E-K_{\mathrm{III}}^*K_{\mathrm{III}}.}
\tag{NW38}
\]

This construction is admissible only where the preserving expectations
exist. Proper ordinary vacuum local-algebra inclusions do not supply them
under the Reeh--Schlieder hypotheses; regulator, RG, or differently pointed
inclusions are required. If a modular completely Dirichlet whole form is
independently given, its standard-form restriction can supply the analogue
of (NW28); [[library/modular-completely-dirichlet-forms-as-squares-of-derivations/inq|Wirth's
derivation theorem]] supplies one exact nontracial construction class.

When two presentations instead admit isometries
\(J^\pm:\mathcal H\to\mathcal K\) into one common correspondence, put

\[
A=(J^+)^*J^-,
\qquad
L=(I-J^+(J^+)^*)J^-.
\tag{NW39}
\]

Pythagoras gives the representation-free residue identity

\[
\boxed{I-A^*A=L^*L.}
\tag{NW40}
\]

Connes cocycles can compare faithful state presentations and identify their
common centralizer, as developed in
[[modular-cocycle-tomography/inq|Modular Cocycle Tomography]]. They do not
by themselves supply the noninjective presentation map, the lower frame,
the Dirichlet normalization, or the Hamiltonian. Their cocycle parameter is
not automatically clock time.

The strict Copernican statement is therefore not “the whole is
nonunitary.” A law, an algebra, an inclusion, or a correspondence is not an
evolution operator, so *unitary* and *nonunitary* are not yet predicates of
the right type. Descent is directed because projection or conditioning
forgets a fibre and is generally noninvertible. Reflection-positive
Osterwalder--Schrader reconstruction separately produces a local Hilbert
carrier, a positive Euclidean semigroup, and then a reversible Lorentzian
unitary clock. A proved bridge floor constrains that generator only after
the reconstruction and carrier-identification theorem; forgetting does not
manufacture unitarity.

## What has changed

The programme can now reject one tempting category error and state one
minimal constructive target.

1. **Exact no-go.** The local flat Wilson Hessian is an Abelianized tangent
   probe and has gauge-reduced soft singlets with no volume-uniform surface
   floor.
2. **Exact replacement carrier.** The full finite Wilson likelihood family
   produces the complete recoverability operator \(A^*A\) and bridge residue
   \(I-A^*A\) on all midpoint \(L^2\) distinctions.
3. **Noncircular comparison object.** The whole-law heat defect in (NW27)
   is action-derived without reading the transfer spectrum, and (NW34) is a
   checkable kernel-level sufficient condition.
4. **Open theorem.** No known result proves (NW32) uniformly in volume,
   exterior data, physical sector, and continuum removal for four-dimensional
   \(SU(N)\) Wilson theory.
5. **Separate physical obligations.** Continuum existence, reflection
   positivity, unique vacuum, exact observable Poincare covariance, and the
   Casimir identification remain necessary before the response can be called
   a mass gap.

The reversal is precise: do not ask a local quadratic shadow to generate the
whole's non-Abelian obstruction. Construct the nonlinear whole, descend it
to the complete surface carrier, and then prove that no normalized physical
distinction can become simultaneously invisible to its boundary residue and
its independently normalized whole-law response.

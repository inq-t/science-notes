# Mass and \(G\) as Dual Exchange Rates

Mass and Newton's constant admit a precise conditional composition as two exchange rates through one dimensionless ledger. On an already reconstructed quantum carrier, mass is the action-calibrated logarithmic transfer rate per clock time; in the Einstein horizon presentation, \(G\) is the mechanical-unit expression of area compliance per entropy-ledger unit. If, and only if, a same-carrier theorem identifies those two ledger differentials on every physical nonvacuum direction, their composition retypes mass as an areal presentation rate. A nonzero compliance does not imply a mass gap: the Clay problem still requires a uniform positive lower ledger rate over the complete vacuum complement and its survival through continuum reconstruction.

**Status: [EXACT] for the transfer Rayleigh-rate formula; [STANDARD] for the Jacobson and Einstein area-law inputs in their stated regimes; [CONDITIONAL THEOREM] for the dual-exchange-rate composition; [NO-GO] for inferring a gap from nonzero \(G\), one nonzero direction, unitarity, conservation, or continuity alone; [OPEN CONSTRUCTION] for the same-ledger identification and its regulator-uniform Yang--Mills realization.**

## The two exchange rates have a common middle type

Let \(H\geq0\) be the reconstructed clock-energy generator, let

\[
P_0=E_H(\{0\}),
\qquad
\mathcal K=(1-P_0)\mathcal H,
\]

and let \(\psi\in D(H^{1/2})\cap\mathcal K\) be nonzero. Define the projective logarithmic transfer depth

\[
R_\psi(\tau)
:=
-\log
\frac{\lVert e^{-\tau H/\hbar}\psi\rVert}
{\lVert\psi\rVert},
\qquad \tau\geq0.
\tag{DG1}
\]

Spectral calculus gives the right derivative

\[
\boxed{
\dot R_\psi(0+)
=
\frac{\lVert H^{1/2}\psi\rVert^2}
{\hbar\lVert\psi\rVert^2}.}
\tag{DG2}
\]

Indeed, differentiating the squared norm first produces the factor two,

\[
\left.\frac{\mathrm d}{\mathrm d\tau}
\lVert e^{-\tau H/\hbar}\psi\rVert^2
\right|_{0+}
=
-\frac{2}{\hbar}\lVert H^{1/2}\psi\rVert^2,
\]

which is cancelled by the factor \(1/2\) in the logarithm of the norm. Thus \(R_\psi\) is dimensionless and \(\dot R_\psi\) is an inverse-time rate. If

\[
\Delta_E
:=
\inf\sigma(H|_{\mathcal K}),
\]

then the variational principle yields

\[
\boxed{
\inf_{0\ne\psi\in D(H^{1/2})\cap\mathcal K}
\dot R_\psi(0+)
=
\frac{\Delta_E}{\hbar}.}
\tag{DG3}
\]

After a Poincare-covariant joint-spectrum theorem has established \(\Delta_E=m_{\mathrm{gap}}c^2\),

\[
\boxed{
m_{\mathrm{gap}}
=
\frac{\hbar}{c^2}
\inf_{0\ne\psi\in D(H^{1/2})\cap\mathcal K}\dot R_\psi(0+).}
\tag{DG4}
\]

Here and below, an infimum over the vacuum complement means the infimum over nonzero vectors in \(D(H^{1/2})\cap\mathcal K\). This allows a degenerate zero-energy sector; when the vacuum is known to be unique, it is equivalent to writing \(\psi\perp\Omega\).

This is the all-direction version of [[mass-as-a-calibrated-distinction-rate]]. It says that mass is a rate of dimensionless **transfer attenuation** on the physical carrier. It does not yet say that the attenuated depth is entropy, a produced fact, or a unit of area.

The independent Einstein-horizon input is the dimensionless entropy ledger

\[
\iota:=\frac{S}{k_B},
\qquad
\mathrm d\iota=\eta_{\mathrm E}\,\mathrm dA,
\qquad
\eta_{\mathrm E}=\frac{c^3}{4\hbar G}.
\tag{DG5}
\]

Equivalently, its areal compliance is

\[
\boxed{
\alpha_A
:=
\frac{\mathrm dA}{\mathrm d\iota}
=
\frac{4\hbar G}{c^3}.}
\tag{DG6}
\]

This is the exchange-rate reading of [[deriving-g-v2/the-g-free-first-law]]. The area in (DG5)--(DG6) is already metric area in a supplied Einstein-class horizon realization. The coefficient is a differential compliance, not an area quantum, a pixel, or evidence that spacetime is discrete.

## Same-ledger composition theorem

The repeated symbol “dimensionless” is not a license to identify \(R\) and \(\iota\). Their meanings and carriers differ:

- \(R_\psi\) is logarithmic Euclidean transfer attenuation on the physical vacuum representation;
- \(\iota\) is an entropy, index, or distinguishability ledger assigned to a causal boundary; and
- \(A\) is metric area after a geometric realization.

The missing bridge must therefore be stated as a map rather than a metaphor.

There is also an algebraic-order obstruction. The Clausius differential \(\mathrm d\iota\) and the area differential \(\mathrm dA\) are ordinarily one-forms, hence linear in an infinitesimal variation. The transfer rate in (DG2) is a positive projective quadratic form. If a real-linear functional \(L\) satisfied

\[
L(\psi)
=
\frac{\lVert H^{1/2}\psi\rVert^2}
{\hbar\lVert\psi\rVert^2}
\tag{DG6a}
\]

on a sign-symmetric set of nonzero tangents, then evaluation at \(-\psi\) would make the left side change sign while the right side remained fixed. Both sides could agree for every direction only in the trivial zero case. Thus the same-ledger bridge cannot be the untyped substitution \(\mathrm d\iota=\mathrm dR\).

There are two type-correct possibilities:

1. assign to each **projective ray** \([\psi]\) a distinguished ledger path \(\iota_\psi(\tau)\), nonlinearly in \(\psi\), whose positive velocity is compared with (DG2); or
2. compare a positive second-order ledger response—such as a relative-entropy/BKM Hessian or another closed quadratic form—with the Hamiltonian form on one linear carrier.

The first presentation makes the exchange-rate chain rule transparent. The second is structurally stronger and is the form actually needed for a full-complement gap theorem.

**Proposition (dual exchange rates).** Suppose a wall-to-physical realization assigns to every nonzero \(\psi\in D(H^{1/2})\cap\mathcal K\) a boundary-ledger curve \(\iota_\psi(\tau)\) and an areal presentation \(A_\psi(\tau)\) such that, at \(\tau=0+\),

\[
\dot\iota_\psi
=
Z_\iota\,\dot R_\psi,
\qquad
\dot A_\psi
=
\alpha_A\dot\iota_\psi,
\tag{DG7}
\]

where \(Z_\iota>0\) and \(\alpha_A\) are fixed independently of \(H\)'s desired gap, the same tangent \(\psi\) is used in every term, and the clock parameter is the one reconstructed for \(H\). Then

\[
\boxed{
\dot A_\psi(0+)
=
\frac{4GZ_\iota}{c^3}
\frac{\lVert H^{1/2}\psi\rVert^2}
{\lVert\psi\rVert^2}.}
\tag{DG8}
\]

Consequently,

\[
\boxed{
\inf_{0\ne\psi\in D(H^{1/2})\cap\mathcal K}\dot A_\psi(0+)
=
\frac{4GZ_\iota}{c^3}\Delta_E
=
\frac{4GZ_\iota}{c}\,m_{\mathrm{gap}}.}
\tag{DG9}
\]

For an exact same-ledger identification, \(Z_\iota=1\), so

\[
\boxed{
m_{\mathrm{gap}}
=
\frac{c}{4G}
\inf_{0\ne\psi\in D(H^{1/2})\cap\mathcal K}\dot A_\psi(0+).}
\tag{DG10}
\]

The proof is the chain rule applied to (DG2), (DG6), and (DG7), followed by the Rayleigh--Ritz identity (DG3). No field equation is used in this algebraic composition beyond the supplied Einstein compliance.

If Euclidean length \(\ell=c\tau\) is used instead, the same statement is

\[
\frac{\mathrm dA_\psi}{\mathrm d\ell}
=
\frac{4GZ_\iota}{c^4}
\frac{\lVert H^{1/2}\psi\rVert^2}
{\lVert\psi\rVert^2},
\qquad
\inf_{0\ne\psi\in D(H^{1/2})\cap\mathcal K}
\frac{\mathrm dA_\psi}{\mathrm d\ell}
=
\frac{4GZ_\iota}{c^2}m_{\mathrm{gap}}.
\tag{DG11}
\]

For one sharp rest-mass direction with \(Z_\iota=1\), the last slope is \(4Gm/c^2=2r_s(m)\), where \(r_s(m):=2Gm/c^2\) is merely the associated Schwarzschild length. This does not make the excitation a black hole or assert that a surface literally expands as it propagates. It says that, under the same-ledger theorem, the mechanical mass rate and Einstein areal compliance compose to the same quantity-valued slope.

## What the area rate means

The curve \(A_\psi(\tau)\) in the proposition is an **areal presentation of response**, not automatically the area of a moving material surface. It is the geometric image of the same physical tangent whose transfer attenuation is measured by \(R_\psi\). This distinction prevents three equivocations:

\[
\text{area response}
\ne
\text{cosmic expansion}
\ne
\text{horizon entropy production}.
\tag{DG12}
\]

A static black hole may have very large entropy capacity without a large entropy-production rate. A cosmological horizon may have a nonzero area velocity without that velocity being a Yang--Mills excitation rate. Equation (DG10) becomes physical only when one construction proves that the boundary ledger and the transfer ledger are natural images of one process on one tangent.

The strongest version is measure- or form-valued. Let \(\mathfrak r_H\) be the positive projective form

\[
\mathfrak r_H[\psi]
:=
\frac{\lVert H^{1/2}\psi\rVert^2}
{\hbar\lVert\psi\rVert^2}.
\tag{DG13}
\]

A common-ledger construction must supply a positive boundary response \(\mathfrak r_\iota\) and a same-carrier map satisfying

\[
\mathfrak r_\iota[\psi]
=Z_\iota\mathfrak r_H[\psi]
\quad
\text{for every physical nonvacuum direction},
\tag{DG14}
\]

or at minimum two regulator-uniform comparison inequalities. Equality of one integrated scalar, one preferred tangent, or one fitted cosmological history is not enough.

In bilinear language, the desired response weld has the form

\[
g_A(v,w)
=
\alpha_A\,g_\iota(v,w),
\qquad
g_\iota(v,w)
=
\frac{Z_\iota}{\hbar}
\operatorname{Re}
\left\langle H^{1/2}Jv,H^{1/2}Jw\right\rangle,
\tag{DG14a}
\]

for tangents with \(Jv,Jw\in D(H^{1/2})\), with a declared real-linear tangent map \(J\), domain compatibility, lower carrier coverage, and a fixed normalization. This is the same-tangent architecture of [[program-core/causal-capacity-equivalence]]. It is not implied by the first-order Clausius equality, even if both use the same scalar entropy function.

## A static ledger does not determine a rate

There is a second exact obstruction. Let \(\nu\) be a probability measure and let \(L\geq0\) be any self-adjoint Markov generator on \(L^2(\nu)\) with \(L1=0\). For every \(\varepsilon>0\),

\[
P_t^{(\varepsilon)}
:=
e^{-t\varepsilon L}
\tag{DG14b}
\]

has the same invariant measure \(\nu\), hence the same static logarithmic density, entropy functional, and any area compliance assigned only from that one-slice law. Its positive spectral rate is nevertheless multiplied by \(\varepsilon\). Therefore

\[
\boxed{
\text{one-slice ledger or area law}
\not\Longrightarrow
\text{transfer rate}.}
\tag{DG14c}
\]

The minimal rate-bearing datum is a two-slice edge law. Let \(P_a=P_a^*\) be a reversible Markov operator on \(L^2(\nu)\), with \(0\leq P_a\leq I\) in operator order and \(P_a1=1\), and define

\[
\mathrm d\eta_a(x,y)
:=
\mathrm d\nu(x)\,P_a(x,\mathrm dy).
\tag{DG14d}
\]

Then

\[
\boxed{
\frac12
\int\lvert f(y)-f(x)\rvert^2\,\mathrm d\eta_a(x,y)
=
\langle f,(I-P_a)f\rangle_{L^2(\nu)}.}
\tag{DG14e}
\]

If, for every centered \(f\),

\[
\frac12
\int\lvert f(y)-f(x)\rvert^2\,\mathrm d\eta_a
\geq
\varepsilon_a\lVert f\rVert_{L^2(\nu)}^2,
\qquad
0<\varepsilon_a<1,
\tag{DG14f}
\]

then \(\lVert P_a|_{1^\perp}\rVert\leq1-\varepsilon_a\). To compare this Markov carrier with the physical carrier, suppose the positive ground state supplies an explicit unitary

\[
U_0:L^2(\nu)\longrightarrow\mathcal H,
\qquad
U_0f=\psi_0f,
\tag{DG14g}
\]

and

\[
P_a
=
U_0^{-1}e^{-a(H-E_0)/\hbar}U_0
=e^{-a\mathcal L/\hbar}
\tag{DG14h}
\]

when \(a\) is a clock duration. Equivalently, for a transfer matrix \(T_a\) with leading eigenvalue \(\lambda_0\), \(P_a=U_0^{-1}(T_a/\lambda_0)U_0\). Only after this ground-state representation do \(\mathcal L\) and \(H-E_0\) have the same nonzero spectrum. The edge inequality then gives

\[
\boxed{
\Delta_E
\geq
-\frac{\hbar}{a}\log(1-\varepsilon_a).}
\tag{DG14i}
\]

If \(a\) is a Euclidean length, replace \(\hbar/a\) by \(\hbar c/a\), and the small-spacing scaling is \(\varepsilon_a\sim a\Delta_E/(\hbar c)\); for a clock duration it is \(\varepsilon_a\sim a\Delta_E/\hbar\). This edge form operates on **differences between successive slice values**; it is the rate-bearing object absent from a static entropy--area law. The calibrated logarithmic rate—not a raw adjacent-slice deficit—is the invariant target.

## Why nonzero \(G\) does not imply a gap

Equation (DG6) says that \(G>0\) makes the ledger-to-area compliance positive. A mass gap instead asks whether the ledger-to-clock rate has a uniform positive floor:

\[
\alpha_A>0
\quad\not\Longrightarrow\quad
\inf_{0\ne\psi\in D(H^{1/2})\cap\mathcal K}\dot\iota_\psi>0.
\tag{DG15}
\]

Even \(\dot\iota_{\psi_*}>0\) for one direction says nothing about a sequence of other normalized directions whose rates tend to zero. The distinction is the operator-level version of the difference between a nonzero exchange rate and a minimum transaction rate across every admissible account.

Continuity is not the obstruction either. A continuous configuration or phase space can support a gapped generator: the harmonic oscillator and a free massive quantum field are elementary witnesses. Conversely, a cavity can have a lowest nonzero normal-mode frequency while the classical energy of that mode tends continuously to zero with amplitude. The spectral gap requires a positive quadratic form on a normalized carrier, not merely a preferred frequency or a discrete list of labels.

The precise Yang--Mills consequence can be read from [[exceptional-wilson-same-carrier-factorization]]. On a connected finite graph containing a cycle, put \(\mathcal K_\Gamma=(1-P_{0,\Gamma})\mathcal H_\Gamma\). Then

\[
\Delta_\Gamma
=
\kappa_N\frac{g(\Gamma)}{18}\Theta_\Gamma.
\tag{DG16}
\]

If the same-ledger theorem held there, its areal-rate shadow would be

\[
\inf_{0\ne\psi\in D(H_\Gamma^{1/2})\cap\mathcal K_\Gamma}\dot A_{\Gamma,\psi}
=
\frac{4GZ_{\iota,\Gamma}}{c^3}
\kappa_N\frac{g(\Gamma)}{18}\Theta_\Gamma.
\tag{DG17}
\]

Positive \(G\) supplies no lower bound on the interacting-vacuum distortion \(\Theta_\Gamma\), does not fix the kinetic energy coefficient \(\kappa_N\), and does not prove that \(Z_{\iota,\Gamma}\) remains nondegenerate. The open theorem remains a physical-unit lower bound that survives volume growth, continuum tuning, OS reconstruction, and Poincare realization. Gravity may provide a common-origin presentation; it cannot be inserted as a substitute for the gravity-free pure-Yang--Mills estimate.

## What unitarity and Noether conservation do not do

Unitarity is compatible with both gapped and gapless Hamiltonians. It preserves the Hilbert norm under an already supplied clock evolution; it does not choose the Hilbert carrier, vacuum representation, clock normalization, or lower spectral edge. The Euclidean contraction in (DG1) is not nonunitary Lorentzian time evolution. Reflection-positive reconstruction is the bridge between those two presentations.

Noether's first theorem likewise begins with an action, a continuous variational symmetry, and a spacetime or parameter domain. It returns an on-shell conserved current; a conserved charge additionally needs boundary and flux control. Noether's second theorem turns gauge redundancy into differential identities rather than a new bulk physical charge. Thus it is too strong to say that Noether conservation applies only to “local, bounded frames.” The exact Copernican criticism is different:

\[
\boxed{
\text{Noether constrains a supplied realization;
it does not construct its carrier, clock, wall ledger, or metric compliance.}}
\tag{DG18}
\]

The G-free Clausius law makes the same order visible. Given local causal horizons, Unruh temperature, matter boost flux, focusing, stress-energy conservation, and a universal ledger-per-area coefficient, [[library/thermodynamics-of-spacetime-the-einstein-equation-of-state/inq|Jacobson's theorem]] recovers the Einstein equation. The ledger law does not construct those premises. Likewise, a Yang--Mills action and gauge symmetry organize a supplied local field realization, but neither Noether identity nor gauge invariance explains why its completed physical vacuum carrier has a uniform positive transfer rate.

## The actual Copernican theorem target

The proposed reversal can now be stated without identifying concepts that merely share units:

\[
\begin{array}{ccccc}
&\text{primitive whole response or process}\\[2mm]
&\swarrow && \searrow\\[-1mm]
\text{boundary ledger }\iota
&&&&
\text{physical transfer depth }R\\[1mm]
\downarrow\;\mathrm dA/\mathrm d\iota
&&&&
\downarrow\;\mathrm dR/\mathrm d\tau\\[1mm]
\text{metric area response}
&&\xleftrightarrow{\quad\text{same-ledger/same-tangent theorem}\quad}&&
\text{clock-energy response}.
\end{array}
\tag{DG19}
\]

The left branch is the open area weld of [[program-core/causal-capacity-equivalence]]. The right branch is the transfer/OS construction of [[vacuum-boundary-gluing-and-wall-response]]. [[program-core/record-scale-soldering]] gives the categorical grammar: a common additive cocycle can have record, scale, entropy, and geometric representations only through explicit natural maps. The bridge in the centre—not dimensional substitution—is the sought explanation.

A promising finite-regulator route is to integrate hidden bulk variables at fixed interface data. The negative logarithm of the resulting marginal density is a boundary effective action; its Hessian measures retained stiffness after hidden fluctuations have softened the bare response. In the Gaussian member this is exactly a Schur complement or Dirichlet-to-Neumann form. A nonlinear, gauge-invariant marginal-Hessian estimate could therefore be the common object whose two realized readings are boundary ledger response and transfer coercivity. It would still have to cover the full vacuum complement and remain uniform on the continuum trajectory.

## Stopping condition

The dual-rate proposal becomes more than a conditional retyping only when one construction proves all of the following:

1. **Ledger:** a dimensionless additive or quadratic response \(\iota\) is constructed before metric units are inserted.
2. **Same carrier:** its tangent is identified with every physical nonvacuum transfer direction, not merely one homogeneous or cosmological tangent.
3. **Same clock:** the parameter in \(\dot\iota\) is soldered noncircularly to the reconstructed clock of \(H\).
4. **Area map:** \(\mathrm dA/\mathrm d\iota\) is obtained from independently normalized geometry rather than measured \(G\).
5. **Uniform positivity:** \(\inf_{0\ne\psi\in D(H^{1/2})\cap\mathcal K}\dot\iota_\psi>0\), with no invisible soft sector.
6. **Continuum survival:** the lower rate remains positive through infinite volume and cutoff removal in fixed physical units.
7. **Casimir realization:** the clock-energy floor becomes the invariant Poincare mass floor.

The conceptual payoff is exact even before those open steps are solved:

\[
\boxed{
G\text{ answers “how much metric area per ledger unit?”};
\qquad
m\text{ answers “how many calibrated ledger units per clock time?”}.}
\]

Their composition can explain how mass and geometry are two presentations of one deeper response. It cannot manufacture the positive all-direction rate that the mass-gap theorem asks us to prove.

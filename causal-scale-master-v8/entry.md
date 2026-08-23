# Causal Scale Dynamics v8 — Exploratory Synthesis

Causal Scale Dynamics asks whether late cosmic acceleration can be retyped as the information-geometric response of causal quantum states to changing metric scale, rather than assigned to a permanent vacuum energy or a freely chosen dark fluid. Standard causal and tractor geometry supply the kinematic language; a proposed scale-indexed wall state, binary normal reduction, two unit principles, and a constitutive free-energy law supply the new physics. The resulting homogeneous history is unusually rigid and falsifiable, while the wall construction, covariant perturbations, global vacuum sector, and any recovery of QFT or the Standard Model remain open.

The central conjecture can be said in one line:

> **[CONJECTURE — PROGRAMME]** Physical scale parameterizes horizontal transport, defined by a connection on a family of causal quantum states, and the late homogeneous gravitational response is the entropy-normalized BKM squared tangent—or free-energy Hessian—along that transported path.

The labels below are part of the content. An equation may be exact after its hypotheses are granted without those hypotheses being physically established.

| Label | Meaning |
|---|---|
| **[STANDARD]** | Established result in its stated regime. |
| **[ALGEBRA]** | Exact consequence of displayed definitions. |
| **[EXACT REFORMULATION]** | Existing physics written in new variables, with no new empirical content. |
| **[CONDITIONAL THEOREM]** | Mathematical implication of explicit assumptions whose physical realization remains open. |
| **[INTERPRETATION]** | Conceptual reading that adds no mathematical or empirical result by itself. |
| **[IDENTIFICATION]** | Proposed correspondence between independently meaningful structures. |
| **[ASSUMPTION]** | Premise adopted for a declared model or regime, without claiming universality. |
| **[PRINCIPLE]** | New falsifiable law, deliberately postulated rather than derived. |
| **[CONSTITUTIVE LAW]** | Rule translating kinematics or information geometry into physical response. |
| **[SECTOR]** | Choice among allowed global or solution branches. |
| **[DEDUCTION]** | Consequence of the principles, identifications, and sector assumptions already declared. |
| **[CONJECTURAL ROUTE]** | Concrete research direction with an upgrade test and a failure condition. |
| **[CONJECTURE]** | Bold physical claim not yet established, stated with a possible test. |
| **[OPEN]** | Required structure or calculation not presently supplied. |

A dash qualifies a canonical label without changing its type: for example, **[PRINCIPLE — WIDTH]** is a particular **[PRINCIPLE]**.

The AI proposal's useful repairs, mathematical corrections, withheld empirical claims, and withdrawn arguments are recorded in [[revision-audit]]; the raw proposal remains untouched in the inbox.

## Causal order leaves a calibration register

**[STANDARD]** Under the usual causality and regularity hypotheses, causal order determines a Lorentzian metric only up to conformal scale. A positive section chooses the physical representative,

$$
g_{\mathrm{phys}}=\sigma^{-2}\boldsymbol g,
\qquad
\sigma\in\Gamma(\mathcal E[1]).
$$

For homogeneous cosmology the observational e-fold and the displacement from the proposed self-dual crossing must remain distinct:

$$
N:=\ln\frac{a}{a_0},
\qquad
N_c:=\ln\frac{a_c}{a_0},
\qquad
x:=N-N_c
=\ln\frac{a}{a_c}
=-\ln\frac{\sigma}{\sigma_c}.
$$

Thus $N=0$ today and $x=0$ at the crossing. Matter and radiation dilute with $N$; the binary response is centered in $x$.

**[INTERPRETATION]** The pair $([g],\sigma)$ carries no more kinematic information than a metric. The useful conceptual move is not to pretend otherwise, but to ask whether causal structure and scale calibration may have different dynamical sources. Causal order is the relational skeleton; scale is the state-dependent calibration placed on it.

The theorem-backed hypotheses and the limits of this interpretation are developed in [[causal-order|causal order and metric scale]].

## Einstein gravity already admits a scale-transport reading

In four dimensions the scale two-jet is packaged by

$$
I_A=\frac14D_A\sigma.
$$

The Einstein equations may be split into

$$
\left(\nabla_a\nabla_b\sigma+P_{ab}\sigma\right)_0
=\frac{4\pi G}{c^4}\sigma T^\circ_{ab},
$$

$$
I^2=\frac{2\pi G}{3c^4}T-\frac{\Lambda_g}{3}.
$$

**[EXACT REFORMULATION]** Trace-free stress is an obstruction to parallel scale transport, while the scalar trace data live in a separate equation. This is GR in tractor language, not a modification of GR. It makes one structural split conspicuous:

$$
T_{ab}\mapsto T_{ab}+\lambda g_{ab}
\quad\Longrightarrow\quad
(T_{ab}+\lambda g_{ab})^\circ=T^\circ_{ab}.
$$

The local transport channel is blind to metric-proportional shifts. What happens to the global scalar lift is a different question; [[horizon-and-vacuum|local blindness is not yet a solution of the cosmological-constant problem]].

The complete tractor rewriting is kept in [[scale-tractor|scale-tractor transport]].

## Scale change is horizontal, not elapsed modular time

For a fixed algebra and faithful state, Tomita–Takesaki modular flow is

$$
\sigma_s^\omega(A)=\Delta_\omega^{is}A\Delta_\omega^{-is}.
$$

This is **vertical** automorphism flow at fixed $(\mathcal A,\omega)$. The proposed cosmological structure is instead a horizontal family

$$
N\longmapsto(\mathcal A_N,\omega_N).
$$

Comparing different fibers requires specified transports, inclusions, or a common algebra, together with relative modular data. Horizontal state displacement cannot be identified with vertical modular time merely because both use logarithmic parameters.

The underlying type distinction is expanded in [[modular-flow|modular flow and state deformation]].

**[OPEN]** No dynamical FLRW family $(\mathcal A_N,\omega_N)$ has yet been constructed. The programme must define the wall region, algebra, faithful state, comparison between scales, and Connes cocycle independently of the desired $H(z)$. This gives the decisive anti-circularity test:

$$
\text{independently constructed state deformation}
\Longrightarrow \text{new physical structure},
$$

$$
\text{state coordinate reconstructed only from }H(z)
\Longrightarrow \text{effective fluid in modular notation}.
$$

The minimum data and the cleanest possible falsifiers are developed in [[wall-state-construction]].

## A binary normal channel supplies the universal pulse shape

A spacelike codimension-two cut has two null-normal orientations. Introduce

$$
Q=P_+-P_-,
\qquad Q^2=1,
\qquad
J_{\rm refl}QJ_{\rm refl}^{-1}=-Q.
$$

Here $J_{\rm refl}$ is geometric normal reflection, not automatically Tomita modular conjugation. **[IDENTIFICATION]** The homogeneous, reflection-odd horizontal response is assumed to factor through a balanced binary normal channel. Two geometric null rays do not by themselves prove that the full wall algebra reduces to this channel; the channel, conditional expectation, or quotient must be constructed. Nor does $Q^2=1$ enforce equal reference weights: reflection must derive balance, or balance is an additional premise. Without it, the center and log-partition function shift.

**[ALGEBRA — BALANCED BINARY REDUCTION]** In the canonical normalization,

$$
p_\pm(\theta)=\frac{e^{\pm\theta}}{2\cosh\theta},
\qquad
\eta:=p_+-p_-=\langle Q\rangle=\tanh\theta,
$$

$$
G^{\mathrm{BKM}}_{\theta\theta}
=\operatorname{sech}^2\theta,
\qquad
\eta^2+G^{\mathrm{BKM}}_{\theta\theta}=1.
$$

The symmetrized relative entropy of the reflected states is

$$
\mathfrak S_{\rm refl}(\theta)=4\theta\tanh\theta,
$$

with a unique minimum at $\theta=0$. The center is therefore intrinsic inside the reduced family. This is a state-space self-duality, not yet a constructed self-dual surface in FLRW spacetime.

The finite binary identities and their full-theory caveats are developed in [[binary-geometry|normal chirality and binary information geometry]].

## Relative modular composition fixes the form, not the slope

**[CONDITIONAL THEOREM]** Suppose the noncentral reduced comparison between two scales depends only on their ratio, is generated by one fixed $Q$, composes additively after central phases are removed, has no relevant holonomy, and is measurable. The multiplicative Cauchy equation then yields

$$
\theta=\varrho_\perp x.
$$

Reversing the names of the two null orientations sends $Q\mapsto-Q$ and $\varrho_\perp\mapsto-\varrho_\perp$. The physical width is therefore

$$
\nu:=|\varrho_\perp|>0.
$$

**[PRINCIPLE — WIDTH]** After fixing orientation, the fundamental normal character is identified with the fundamental scale/inverse-scale character:

$$
\boxed{\nu=1}
\qquad
(\varrho_\perp=+1\text{ by convention}).
$$

Real conformal weights do not quantize $\nu$, and a two-dimensional normal plane does not supply a chiral CFT. Those proposed derivations are invalid. Unit width remains a physical principle unless an explicit cocycle calculation derives it.

The precise conditional Cauchy argument is recorded in [[scale-soldering|scale–state soldering]].

## Scale capacity fixes a second, independent number

Let the extensive pullback BKM metric be

$$
G^\perp_{NN}(N)
=C_{\perp,c}\nu^2
\operatorname{sech}^2(\nu x),
$$

and define the entropy-normalized peak squared speed

$$
\mathfrak R_c
:=\frac{k_B}{S_c}G^\perp_{NN}(N_c)
=\frac{k_BC_{\perp,c}}{S_c}\nu^2.
$$

**[PRINCIPLE — SCALE–CAPACITY]**

$$
\boxed{\mathfrak R_c=1}.
$$

One Weyl e-fold then carries one horizon-entropy unit of squared BKM distance at self-duality. This is a bold equivalence principle, not an identity of information geometry. Capacity equals entropy in some controlled Einstein-holographic settings, which motivates an “Einstein-capacity universality class”; no calculation yet places the dynamical FLRW wall in it.

The two unit laws do different work. $\nu=1$ fixes the width in scale; $\mathfrak R_c=1$ fixes the entropy-normalized peak. Neither law alone fixes the full response profile. [[closure-stack]] keeps this accounting explicit.

The capacity precedents and their limits are assessed in [[scale-capacity|scale–capacity equivalence]].

## Free-energy curvature becomes matter only by a constitutive step

For states on a common algebra with a fixed KMS reference,

$$
F_c(\rho)-F_c(\omega_c)
=k_BT_cS(\rho\Vert\omega_c),
$$

and locally

$$
S(\omega_{c+\delta N}\Vert\omega_c)
=\frac12G^\perp_{NN}(N_c)\delta N^2
+O(\delta N^3).
$$

**[ALGEBRA]** Relative entropy fixes the local quadratic free-energy stiffness. It does not itself create a spacetime energy density.

**[CONSTITUTIVE LAW]** The programme proposes the anchored all-history source

$$
\boxed{
\rho_X(N):=
\frac{k_BT_c}{2V_c}G^\perp_{NN}(N).
}
$$

The factor $1/2$ is the Taylor coefficient, but identifying that coefficient per crossing volume with an energy density, holding $T_c$ and $V_c$ fixed away from the crossing, and extending the local Hessian over the full path are physical choices. An instantaneous $T(N),V(N)$ prescription would define a different theory.

The local theorem and all-history extension are separated in [[free-energy-source|the modular free-energy source law]].

## Horizon marginality supplies units

At a flat $3+1$ Einstein-FLRW apparent horizon, stipulate the crossing data

$$
R_c=\frac{c}{H_c},
\qquad
\frac{S_c}{k_B}=\frac{\pi R_c^2c^3}{G\hbar},
\qquad
k_BT_c=\frac{\hbar c}{2\pi R_c}.
$$

Then

$$
k_BT_c\frac{S_c}{k_B}
=\frac{c^4R_c}{2G}
=E_{\mathrm{MS},c}
=\rho_{\mathrm{crit},c}V_c.
$$

**[ALGEBRA — STIPULATED HORIZON DATA]** The conversion is exact given the area law, Friedmann marginality, and the canonical horizontal $2\pi$ normalization. **[IDENTIFICATION — HORIZONTAL TEMPERATURE] [OPEN]** The horizontal modular temperature has not been derived for a dynamical FLRW wall and must not be silently replaced by the generally different Kodama–Hayward temperature. The signed distinction is recorded in [[horizon-and-vacuum]].

The dimensional conversion is derived step by step in [[hawking-friedmann|the Hawking–Friedmann bridge]].

## The generalized homogeneous response

Combining the binary family, affine soldering, capacity normalization, constitutive law, and horizon conversion gives

$$
\boxed{
\rho_X(N)
=\frac{\mathfrak R_c}{2}\rho_{\mathrm{crit},c}
\operatorname{sech}^2(\nu x).
}
$$

**[DEDUCTION — SEPARATE CONSERVATION]** If

$$
\rho_X'=-3(1+w_X)\rho_X,
$$

where a prime means $\mathrm d/\mathrm dN$, then

$$
w_X(N)
=-1+\frac{2\nu}{3}\tanh(\nu x),
$$

and the entire orbit obeys

$$
\boxed{
9(1+w_X)^2+6w_X'=4\nu^2.
}
$$

The corresponding CPL tangent lies on

$$
w_a=\frac32(1+w_0)^2-\frac{2\nu^2}{3}.
$$

Amplitude and date drop out of the differential invariant; the width does not. These are useful phenomenological tests even before the microscopic construction is complete.

At this stage $\rho_X$ and the pressure inferred from conservation are effective homogeneous variables. They are not yet components of a derived physical stress tensor; that status requires a covariantly conserved $T^X_{ab}$.

At the crossing, suppose the critical density splits only into the response and an “ordinary” component. Equivalently, any residual is either zero or included inside the nonresponse component. Flatness then gives

$$
\Omega_{X,c}=\frac{\mathfrak R_c}{2},
\qquad
\frac{\rho_{X,c}}{\rho_{\mathrm{ordinary},c}}
=\frac{\mathfrak R_c}{2-\mathfrak R_c},
\qquad
0<\mathfrak R_c<2.
$$

Exact dark–ordinary equality follows only from the unit-amplitude principle $\mathfrak R_c=1$.

The unit branch is therefore

$$
\boxed{
\rho_X(N)=\frac12\rho_{\mathrm{crit},c}\operatorname{sech}^2x,
\qquad
w_X(N)=-1+\frac23\tanh x.
}
$$

At $x=0$, self-duality, the density maximum, and $w_X=-1$ coincide. The last two are already equivalent for any positive separately conserved component; the extra content is their identification with state self-duality and, on $\mathfrak R_c=1$, with dark–ordinary equality.

The crossing date is solution data fixed by present flatness, not a new universal constant. The exact matter–radiation equation can possess multiple roots, so the phenomenological branch must be declared. [[generalized-background]] defines the late branch as the smallest positive root continuously connected to the unit-width solution and corrects the proposed-v8 “absolute width ceiling.”

The unit profile's original background deductions are retained in [[self-dual-response|the self-dual response]].

## The coasting future is a sector, not a theorem of local blindness

Let $\Lambda_{\rm res}$ denote the curvature-valued scalar lift that survives renormalization and whatever global completion is chosen. It may combine the bare tractor datum $\Lambda_g$, vacuum counterterms, and an integration or flux constant; the present framework does not derive that combination. In Einstein units its constant energy density is

$$
\rho_{\rm res}=\frac{c^4}{8\pi G}\Lambda_{\rm res}.
$$

**[SECTOR]** The sharp transient-acceleration story chooses

$$
\Lambda_{\mathrm{res}}=0
$$

and assumes spatial flatness plus separately conserved ordinary and response sectors. In that branch

$$
\rho_X\sim a^{-2\nu},
\qquad
w_X\longrightarrow-1+\frac{2\nu}{3}.
$$

For $\nu=1$, a response-dominated future coasts, $a(t)\sim t$, with no permanent event horizon. A positive constant residual eventually restores de Sitter acceleration. Local information geometry and the trace-free tractor equation are blind to central offsets, but neither selects nor radiatively stabilizes the global residual.

## The same binary geometry contains an exact internal Witten pair

On $L^2(\mathbb R,\mathrm d\theta)$, the binary score factorizes an exact pair:

$$
\mathcal A=\partial_\theta+\tanh\theta,
\qquad
\mathcal H_-=\mathcal A^\dagger\mathcal A
=-\partial_\theta^2+1-2\operatorname{sech}^2\theta,
\qquad
\mathcal H_+=\mathcal A\mathcal A^\dagger
=-\partial_\theta^2+1.
$$

**[ALGEBRA]** It has one normalizable zero mode $\psi_0=2^{-1/2}\operatorname{sech}\theta$, with $2|\psi_0|^2=G^{\mathrm{BKM}}_{\theta\theta}$, and a reflectionless continuum beginning at $E=1$. This is elegant internal state-space operator geometry. The coordinate $\theta$ is not time, its scattering label is not comoving momentum, and the Witten index is not a Weyl fermion.

The factorization and scattering formulas are developed in [[witten-pair|the binary Witten–Darboux pair]].

## Completion means more than background compatibility

A physical spacetime lift must supply a covariantly conserved response $T^X_{ab}$, gauge-invariant scalar/vector/tensor variables, constraints, spatial gradients, characteristic cones, regularity at $w=-1$, hyperbolicity, absence of ghosts and gradient instabilities, matter coupling, and CMB/lensing/growth transfer functions. [[perturbation-and-qft-interface]] separates the internal spectral clue from these obligations.

Ordinary QFT or the Standard Model may be **imported** on the background as an external fiber theory. That is coexistence, not recovery. A recovery claim would need, at minimum, locality, unitarity, stress conservation, gauge and BRST identities, the Standard Model gauge algebra and representations, fermions and Yukawas, anomaly cancellation, renormalization, and convergence of accessible correlators or amplitudes to their established low-energy values.

The strongest defensible present claim is therefore not that the programme has replaced GR, QFT, or $\Lambda$CDM. It is that a small, auditable stack of new bridges turns a striking binary information geometry into a rigid background cosmology. Whether that stack describes nature is concentrated in a few hard calculations rather than hidden in a flexible function.

## What would decisively move the programme

The highest-value calculation is not another background fit. It is an explicit FLRW wall-state construction that computes both

$$
\frac{\mathrm d\theta}{\mathrm dN}
\quad\text{and}\quad
\frac{k_B}{S}G^\perp_{NN}
$$

without using the target expansion history. That one construction could derive, modify, or kill both unit principles.

At the phenomenological level, the clean tests are the generalized invariant, the single-pulse topology, the $w=-1$ density maximum, the unit crossing fraction, and the predicted non-$\Lambda$CDM cosmography. Background data cannot observe modular self-duality while the wall state is unconstructed; identifying the maximum with self-duality is a separate microscopic wall test. Background fits are provisional until their data and likelihood pipeline are reproducible, and perturbation observables are undefined until the spacetime lift exists. [[observational-programme]] distinguishes mathematical receipts, benchmark evaluations, and actual empirical evidence.

The bolder research routes—Euclidean character quantization, near-horizon Virasoro structure, a covariant Witten lift, a complementary global vacuum mechanism, and genuine QFT reconstruction—are retained in [[conjecture-ledger]] with explicit upgrade and failure conditions. Their purpose is not to decorate the argument. Each is a way the current postulates might become calculable, or be shown wrong.

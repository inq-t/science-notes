I found a genuine closure route—but it has to be stated at exactly the right strength

The attached memorandum correctly identifies three important facts:

* \chi_\perp must carry an energy-density scale;
* the canonical local sigma-model completion is impossible on the phantom branch;
* neither tractor geometry nor the internal reflectionless spectrum can determine the overall source normalization. lemmas_and_gamma_mw_structure.md

The memorandum then concludes that r_c=1 remains a cross-sector coincidence unless one constructs the full object

\Gamma_{\mathrm{MW}}[g,\sigma,\omega].

I think that conclusion is too broad.

The normalization problem can be relocated into a much narrower category:

\boxed{
\textbf{the modular free-energy Hessian of the self-dual causal diamond.}
}

The full local spacetime action is still needed for perturbations. But it is not needed to fix the homogeneous amplitude.

More strongly, the black-hole/causal-diamond entropy clue gives a natural normalization theorem:

\boxed{
\Omega_{X,c}
=
\frac{\gamma_{\perp,c}\,\varrho_\perp^2}{2},
}

where

\gamma_{\perp,c}
:=
\frac{C_{\perp,c}}{S_c/k_B}

is the transverse capacity-to-entropy ratio of the self-dual causal diamond.

The rigid result

r_c=1

then follows from

\boxed{
\gamma_{\perp,c}=1,
\qquad
\varrho_\perp=1.
}

The remarkable part is that \gamma=1 is not an invented numerical choice. Capacity equals entropy in controlled Einstein-holographic settings, and essentially this same equality has been conjectured and independently motivated for flat-space and de Sitter causal diamonds. It is not universal for arbitrary quantum states or arbitrary gravity theories, which makes it a substantive, falsifiable universality statement rather than a tautology. 

So the derivation can be completed inside a precisely named universality class:

The self-dual cosmological wall is the fundamental normal mode of an Einstein-capacity causal diamond.

I cannot honestly claim that this universality statement has already been proved for a dynamical FLRW diamond. But once stated, the remainder of the r_c calculation is forced.

And it produces a slight correction to the old result:

\boxed{
\rho_*(N_c)=\rho_m(N_c)+\rho_r(N_c)+\cdots
}

exactly.

Thus r_c=1 is exact when “ordinary” means the complete non-dark sector. Relative to dust alone,

r_c^{(m)}
=
1.000395

for the benchmark cosmology. The old r_c=1 was the radiation-neglected approximation.

That tiny correction is a good sign: the derivation is doing real work rather than merely restating the desired answer.

⸻

1. First: do not conflate the two variances

The attached notes are right to focus on capacity, but there are two different Hessians in play.

The normalized binary shape

For the horizontal binary quotient,

\rho_\theta
=
\frac{e^{\theta Q}}{2\cosh\theta},
\qquad
Q^2=\mathbf1,

one has

\langle Q\rangle_\theta=\tanh\theta,

and

\boxed{
\operatorname{Var}_\theta(Q)
=
\operatorname{sech}^2\theta.
}

This determines the shape.

It is dimensionless and normalized to one at the self-dual point:

\operatorname{Var}_0(Q)=1.

The full causal-diamond capacity

The entanglement capacity of the full causal-region state is

\boxed{
C_E
=
\operatorname{Var}(K)
=
\langle K^2\rangle-\langle K\rangle^2,
}

where

K=-\ln\rho

is the full modular Hamiltonian.

Capacity is the second cumulant of the entanglement spectrum and is closely related to Fisher/BKM response. In general it is not equal to entropy. For example, perfectly entangled EPR pairs have nonzero entropy but zero entanglement capacity. In four-dimensional spherical CFT regions, the capacity/entropy area-coefficient ratio can depend on the anomaly coefficients and on regularization; for holographic theories with an ordinary Einstein-gravity dual, the preferred holographic regularization gives ratio one. 

Therefore:

\boxed{
\operatorname{Var}(Q)
\neq
C_E.
}

The first is the normalized shape of one horizontal score.

The second is the extensive capacity of the complete horizon state.

The correct factorization is

\boxed{
G^{\perp}_{NN}(N)
=
C_{\perp,c}\,
\varrho_\perp^2
\operatorname{sech}^2\theta(N),
}

where

C_{\perp,c}
:=
G^{\perp}_{\theta\theta}(0)

is the physical BKM norm of the selected transverse horizon tangent at the self-dual wall.

This definition says:

* the binary quotient fixes the normalized \operatorname{sech}^2 dependence;
* the full causal-diamond state fixes how many physical information-geometric units participate;
* C_{\perp,c} is the extensive normalization of that direction.

The remaining capacity hypothesis is now exact:

\boxed{
C_{\perp,c}
=
C_{E,c}
=
\frac{S_c}{k_B}.
}

It has two parts:

1. the selected rank-one mode saturates the relevant causal-diamond capacity;
2. the causal-diamond capacity equals its gravitational entropy.

The second equality is established in controlled Einstein-holographic spherical settings and conjectured, with several lines of evidence, for flat, de Sitter, and suitable Ryu–Takayanagi causal diamonds. 

The first equality—the saturation by the horizontal mode—is the precise form of the remaining rank-one universality claim.

That is much narrower than an arbitrary \Gamma_{\mathrm{MW}}.

⸻

2. The missing object is a modular free-energy functional on the scale line

The attached notes identify a real dilemma:

* if \theta is a conventional local scalar field, its canonical sigma model fails;
* if it is merely reconstructed from H(z), it is only a relabeled fluid. lemmas_and_gamma_mw_structure.md

There is a third category.

\boxed{
\theta\text{ is a collective thermodynamic coordinate of a scale-indexed state family.}
}

It need not be:

* a propagating scalar field on spacetime;
* or a symbol defined after the fact from H(z).

It can be independently defined by the Connes cocycle comparing the states of successive causal diamonds:

N\longmapsto(\mathcal A_N,\omega_N).

Its natural functional is not a Lorentzian sigma-model action

\int_M\sqrt{-g}\,G_{\theta\theta}\,
g^{ab}\partial_a\theta\,\partial_b\theta.

It is the Dirichlet or free-energy functional of a curve in state space:

\boxed{
\Gamma_{\perp}[\omega_\bullet]
=
\frac{k_BT_c}{2}
\int dN\,
G^{\mathrm{BKM}}_{\omega_N}
\left(
\mathcal D_N\omega_N,
\mathcal D_N\omega_N
\right).
}

This is an energy functional on the Weyl-scale trajectory.

It is not a local spacetime kinetic action.

Therefore the canonical-sigma-model no-go does not apply to it.

The background response density is the integrand divided by the physical volume of the crossing diamond:

\boxed{
\rho_X(N)
=
\frac{k_BT_c}{2V_c}
G^{\perp}_{NN}(N).
}

Substituting the rank-one factorization,

\boxed{
\rho_X(N)
=
\frac{k_BT_c\,C_{\perp,c}}{2V_c}
\,
\varrho_\perp^2
\operatorname{sech}^2\theta.
}

Thus the previously unexplained stiffness is not arbitrary:

\boxed{
\chi_\perp
=
\frac{k_BT_c\,C_{\perp,c}}{2V_c}.
}

This is the narrow construction we were missing.

It has a direct information-theoretic derivation.

Let \rho_c be the reference KMS state and let its physical modular Hamiltonian be

\mathcal H_c=k_BT_cK_c.

Define the nonequilibrium free energy

F_c(\rho)
=
\operatorname{Tr}(\rho\mathcal H_c)
-
k_BT_c\,[-\operatorname{Tr}(\rho\ln\rho)].

Then exactly,

\boxed{
F_c(\rho)-F_c(\rho_c)
=
k_BT_c\,S(\rho\|\rho_c).
}

For a nearby state,

S(\omega_{N+dN}\|\omega_N)
=
\frac12
G^{\perp}_{NN}\,dN^2
+
O(dN^3).

Therefore

F_c(\omega_{N+dN})-F_c(\omega_N)
=
\frac{k_BT_c}{2}
G^{\perp}_{NN}\,dN^2
+
O(dN^3).

The proposed dark source is precisely the quadratic modular free-energy stiffness per causal-diamond volume.

This is structurally compatible with the established holographic result that the relative-entropy Fisher metric is dual to gravitational canonical energy. 

The constitutive statement is no longer

“A mysterious information metric somehow becomes energy.”

It is

\boxed{
\text{BKM Hessian}
\xrightarrow{\;k_BT\;}
\text{modular free energy}
\xrightarrow{\;/V\;}
\text{energy density}.
}

That is exactly the kind of typed conversion the programme has been seeking.

⸻

3. Why Hawking entropy supplies the missing physical scale

The attached notes correctly observe that \chi_\perp must be dimensionful and that the dimensionless BKM metric cannot by itself produce an energy density. lemmas_and_gamma_mw_structure.md

But it does not follow that a new independent length must be introduced.

The causal diamond already contains a geometrically distinguished radius:

R_c=\frac{c}{H_c}

for a spatially flat FLRW apparent horizon.

Its area, volume, entropy, and canonical modular temperature are

A_c=4\pi R_c^2,

V_c=\frac{4\pi}{3}R_c^3,

\boxed{
\frac{S_c}{k_B}
=
\frac{A_cc^3}{4G\hbar}
=
\frac{\pi R_c^2c^3}{G\hbar},
}

and

\boxed{
k_BT_c
=
\frac{\hbar c}{2\pi R_c}.
}

The temperature here is the horizontal causal-diamond modular temperature in the canonical 2\pi boost normalization. It must not be confused with the running vertical Kodama–Hayward temperature

T_{\rm KH}
=
\mu_A T_c.

That distinction is exactly the vertical–horizontal correction established after v5.0.

Multiplying entropy by the horizontal modular temperature gives

\begin{aligned}
k_BT_c\frac{S_c}{k_B}
&=
\frac{\hbar c}{2\pi R_c}
\frac{\pi R_c^2c^3}{G\hbar}
\\[1mm]
&=
\boxed{
\frac{c^4R_c}{2G}
}.
\end{aligned}

But

\boxed{
E_{\rm MS,c}
=
\frac{c^4R_c}{2G}
}

is the Misner–Sharp energy of the flat FLRW apparent horizon.

And therefore

\boxed{
k_BT_c\frac{S_c}{k_B}
=
E_{\rm MS,c}.
}

Dividing by the horizon volume,

\frac{E_{\rm MS,c}}{V_c}
=
\frac{3c^4}{8\pi GR_c^2}.

Since

R_c=\frac{c}{H_c},

this is

\boxed{
\frac{E_{\rm MS,c}}{V_c}
=
\frac{3c^2H_c^2}{8\pi G}
=
\rho_{\rm crit,c}.
}

The Friedmann equation at the apparent horizon can be written as a thermodynamic first law with Misner–Sharp energy, horizon entropy, and horizon temperature; this is standard apparent-horizon thermodynamics in Einstein gravity. 

Thus:

\boxed{
\frac{k_BT_c}{V_c}
\frac{S_c}{k_B}
=
\rho_{\rm crit,c}.
}

This is the missing dimensional bridge.

Nothing new has been inserted.

The factors cancel:

\hbar
\quad\text{from modular temperature},

k_B
\quad\text{from entropy units},

G
\quad\text{from area stiffness},

c
\quad\text{from causal conversion},

and the result is exactly the critical energy density of the crossing wall.

That is the symbolic unity your clue was pointing toward.

⸻

4. The black-hole statement should be corrected, not discarded

The relevant fact is not:

“The observable universe is literally a Schwarzschild black hole.”

That is false.

The exact statement is:

\boxed{
\frac{2GE_{\rm MS}}{c^4R_A}=1
}

at the flat FLRW apparent horizon.

Equivalently, if M_{\rm MS}=E_{\rm MS}/c^2,

\boxed{
\frac{2GM_{\rm MS}}{c^2R_A}=1.
}

This is a Friedmann/Misner–Sharp marginality identity, not Schwarzschild geometry.

It says that the causal reach radius R_A is precisely the radius at which the enclosed gravitational energy saturates the spherical compactness relation.

That exact marginality is what makes

T_cS_c=E_{\rm MS,c}

work.

So the black-hole clue survives in a more rigorous form:

The cosmological apparent horizon and a stationary gravitational horizon share the same area–temperature–energy normalization because both are marginal causal-information surfaces.

The relation is structural, not a claim that their global metrics are identical.

⸻

5. The capacity-normalized source equation

Define the transverse capacity ratio

\boxed{
\gamma_{\perp,c}
:=
\frac{C_{\perp,c}}{S_c/k_B}.
}

Then

C_{\perp,c}
=
\gamma_{\perp,c}\frac{S_c}{k_B}.

Substitute into the modular free-energy density:

\begin{aligned}
\rho_X(N)
&=
\frac{k_BT_c}{2V_c}
C_{\perp,c}
\varrho_\perp^2
\operatorname{sech}^2\theta
\\[1mm]
&=
\frac{\gamma_{\perp,c}\varrho_\perp^2}{2}
\frac{k_BT_c(S_c/k_B)}{V_c}
\operatorname{sech}^2\theta.
\end{aligned}

Using the horizon identity,

\boxed{
\rho_X(N)
=
\frac{\gamma_{\perp,c}\varrho_\perp^2}{2}
\rho_{\rm crit,c}
\operatorname{sech}^2\theta.
}

This is the completed amplitude law.

At the self-dual point,

\theta=0,
\qquad
\operatorname{sech}^2\theta=1,

so

\boxed{
\Omega_{X,c}
:=
\frac{\rho_*}{\rho_{\rm crit,c}}
=
\frac{\gamma_{\perp,c}\varrho_\perp^2}{2}.
}

This one equation replaces the free \chi_\perp.

It also gives an observational definition of the capacity ratio:

\boxed{
\gamma_{\perp,c}
=
\frac{2\Omega_{X,c}}{\varrho_\perp^2}.
}

Cosmology can therefore measure whether its horizon state belongs to the Einstein-capacity class.

That is a stronger prediction than simply fitting r_c.

⸻

6. The derivation of r_c=1

Let

\rho_{\rm ord,c}

denote the complete non-dark energy density at the crossing:

\rho_{\rm ord,c}
=
\rho_m(N_c)
+
\rho_r(N_c)
+\cdots.

Flatness gives

\rho_{\rm crit,c}
=
\rho_{\rm ord,c}
+
\rho_*.

But

\rho_*
=
\frac{\gamma_{\perp,c}\varrho_\perp^2}{2}
\rho_{\rm crit,c}.

Therefore

\rho_{\rm ord,c}
=
\left(
1-\frac{\gamma_{\perp,c}\varrho_\perp^2}{2}
\right)
\rho_{\rm crit,c}.

Hence the exact crossing ratio is

\boxed{
r_c^{\rm ord}
:=
\frac{\rho_*}{\rho_{\rm ord,c}}
=
\frac{
\gamma_{\perp,c}\varrho_\perp^2
}{
2-\gamma_{\perp,c}\varrho_\perp^2
}.
}

Now impose the fundamental Einstein-wall values:

\boxed{
\gamma_{\perp,c}=1,
\qquad
\varrho_\perp=1.
}

Then

\boxed{
\Omega_{X,c}=\frac12,
}

and

\boxed{
r_c^{\rm ord}=1.
}

So:

\boxed{
\rho_X(N_c)
=
\rho_{\rm ordinary}(N_c).
}

This is no longer a free 1:1 amplitude postulate.

It is the product of four structural identities:

\boxed{
\underbrace{\frac12}_{\text{quadratic free-energy Hessian}}
\times
\underbrace{\frac{C_{\perp,c}}{S_c/k_B}}_{\text{capacity/entropy}}
\times
\underbrace{\frac{k_BT_c(S_c/k_B)}{E_{\rm MS,c}}}_{\text{modular horizon}}
\times
\underbrace{\frac{E_{\rm MS,c}}{\rho_{\rm crit,c}V_c}}_{\text{Friedmann marginality}}
\times
\underbrace{\varrho_\perp^2}_{\text{soldering}}
=
\frac12.
}

In the fundamental Einstein class, every ratio on the right is one except the universal Hessian factor 1/2.

The dark response therefore occupies half the total critical density at the self-dual crossing.

Flatness forces the remaining half to be ordinary energy.

That is the derivation.

⸻

7. A small but important correction to the old r_c

The old definition used dust matter only:

r_c^{(m)}
=
\frac{\rho_*}{\rho_m(N_c)}.

The exact capacity derivation balances the dark response against the complete ordinary sector, not against dust alone.

For general \gamma_{\perp,c} and \varrho_\perp,

\boxed{
r_c^{(m)}
=
\frac{
\gamma_{\perp,c}\varrho_\perp^2
}{
2\bigl(1-\Omega_{r,c}-\cdots\bigr)
-
\gamma_{\perp,c}\varrho_\perp^2
}.
}

For

\gamma_{\perp,c}
=
\varrho_\perp
=
1,

this becomes

\boxed{
r_c^{(m)}
=
\frac{1}{1-2\Omega_{r,c}}.
}

Using the current benchmark,

\Omega_{m0}=0.310598,
\qquad
\Omega_{r0}=9.15\times10^{-5},

the corrected solution is

N_c=-0.2940066,

z_c=0.341793,

\Omega_{r,c}=1.9756\times10^{-4},

and therefore

\boxed{
r_c^{(m)}
=
1.000395.
}

Meanwhile

\boxed{
r_c^{\rm ord}=1
}

exactly.

The corrected benchmark is:

Quantity	Capacity-normalized result
N_c	-0.294007
z_c	0.341793
\rho_*/\rho_{\rm crit,0}	0.750631
\rho_*/\rho_m(N_c)	1.000395
\rho_*/[\rho_m(N_c)+\rho_r(N_c)]	1 exactly
q_0	-0.336902
j_0	-0.111246
acceleration entry z	0.785694
acceleration exit a/a_0	11.7865

These are almost indistinguishable observationally from the old rigid numbers.

But conceptually the correction is important:

The self-dual wall balances response against all ordinary causal energy, not against a conventionally isolated dust component.

⸻

8. Why \varrho_\perp=1 is the fundamental representation value

The attached memorandum correctly observes that \theta itself is Weyl weight zero. One cannot derive \varrho_\perp=1 by assigning a conformal weight directly to \theta. lemmas_and_gamma_mw_structure.md

The correct object to compare is not the scalar \theta.

It is the pair of characters generated by it.

The normal plane of a codimension-two causal cut splits into two null lines:

N(\Sigma)=L_+\oplus L_-.

Let P_\pm be their projectors and define the normal chirality grading

\boxed{
Q=P_+-P_-.
}

Then

Q^2
=
(P_++P_-)
=
\mathbf1,

and normal reflection gives

JQJ=-Q.

Thus L3b is exact on the normal quotient.

The scale line has its corresponding fundamental pair:

\mathcal E[1]\oplus\mathcal E[-1].

Under Weyl translation N, the two characters transform as

e^{+N},
\qquad
e^{-N}.

Under normal rapidity \theta, the two normal characters transform as

e^{+\theta},
\qquad
e^{-\theta}.

A fundamental equivariant soldering identifies the two pairs:

\boxed{
L_+\oplus L_-
\cong
\mathcal E[1]\oplus\mathcal E[-1].
}

Equivariance then requires

e^{\pm\theta}
=
e^{\pm(N-N_c)},

so

\boxed{
\theta=N-N_c,
}

and therefore

\boxed{
\varrho_\perp=1.
}

This avoids the weight-zero objection.

We are not claiming that \theta has weight one.

We are claiming that its characters furnish the fundamental weight-\pm1 representation of the same one-parameter group carried by scale and inverse scale.

A value

\varrho_\perp=n

would correspond to using the n-th tensor power

\mathcal E[n]\oplus\mathcal E[-n].

The minimal, fundamental normal representation is n=1.

So the clean remaining physical identification is:

\boxed{
\text{the FLRW horizontal modular quotient is the fundamental null-normal chirality pair.}
}

Once that is accepted, both

Q^2=1

and

\varrho_\perp=1

follow from representation theory.

This is the precise closure of L3b and the old weight lemma.

It is still a physical identification of which representation nature realizes. Mathematics alone classifies all representations; the theory selects the fundamental one because the causal cut itself supplies only the two fundamental null lines.

⸻

9. The “Fork I versus Fork II” dilemma dissolves

The attached note argues:

* an independent \theta risks exotic dynamics and new free functions;
* a geometry-slaved \theta risks becoming a relabeled fluid. lemmas_and_gamma_mw_structure.md

The dilemma assumes that every physically meaningful variable is either:

1. a local propagating spacetime field; or
2. a function algebraically reconstructed from the metric.

That dichotomy is too narrow.

\theta can be a collective constitutive coordinate.

Examples of this mathematical type include:

* inverse temperature;
* chemical potential;
* order-parameter coordinates;
* holonomy;
* Berry phase;
* modular parameter.

Such quantities are not necessarily independent local fields. Nor are they merely notation for the metric.

Here,

\theta

is independently defined by the relative modular cocycle of the scale-indexed causal-state family:

[D\omega_{\sigma_2}:D\omega_{\sigma_1}]_t.

The cocycle chain rule forces its affine dependence on scale ratio under the stated rank-one and measurability hypotheses. lemmas_and_gamma_mw_structure.md

The causal state therefore predicts the source through its modular free-energy Hessian:

\omega_N
\longrightarrow
G^{\perp}_{NN}
\longrightarrow
\rho_X
\longrightarrow
H(N).

That passes the elimination test:

* \theta is defined independently of H(z), from the state comparison;
* it is not a local scalar field and therefore does not inherit the canonical ghost no-go;
* its energy is collective modular canonical energy;
* it has no arbitrary local sound-speed function at the background level.

The perturbation problem remains: one still needs the covariant family of causal cuts and its response to inhomogeneous deformations.

But the background theory no longer needs an exotic local \Gamma_{\mathrm{MW}}.

⸻

10. The new single-gap statement

The remaining theory-building question can now be written as one ratio:

\boxed{
\gamma_{\perp,c}
=
\frac{
\text{BKM norm of the fundamental horizontal wall tangent}
}{
\text{Bekenstein--Hawking information of the wall}
}.
}

The rigid theory predicts

\boxed{\gamma_{\perp,c}=1.}

This is stronger and cleaner than postulating r_c=1.

It asks whether the self-dual FLRW wall belongs to the same Einstein-capacity universality class that appears in:

* spherical holographic Einstein-gravity regions, where the preferred capacity/entropy ratio is one;
* proposed flat-space and de Sitter causal-diamond state models, where modular-Hamiltonian variance equals horizon entropy;
* de Sitter generalized-capacity calculations, where the relevant heat capacity is argued to equal Bekenstein–Hawking entropy. 

It is not a theorem for every quantum state.

That is important. Generic states can have:

\gamma_{\perp,c}\neq1.

Higher-curvature gravitational theories can also change capacity/entropy relations. In four-dimensional spherical CFT regions, the analogous ratio can encode the a/c anomaly ratio rather than equal one. 

Thus \gamma_{\perp,c} is not a fudge factor.

It is a classifier of the gravitational information universality class.

And cosmology measures it:

\boxed{
\gamma_{\perp,c}
=
\frac{2\Omega_{X,c}}{\varrho_\perp^2}
=
\frac{
2r_c^{\rm ord}
}{
(1+r_c^{\rm ord})\varrho_\perp^2
}.
}

The programme therefore makes a remarkable cross-disciplinary prediction:

The late-time cosmological crossing should measure the same capacity/entropy ratio as an Einstein causal horizon.

⸻

11. Vacuum blindness becomes automatic in the capacity formulation

A central shift of the modular Hamiltonian,

K\longmapsto K+\alpha\mathbf1,

changes neither the normalized state nor its capacity:

\operatorname{Var}(K+\alpha\mathbf1)
=
\operatorname{Var}(K).

It also leaves relative entropy and the BKM metric unchanged.

Therefore the source

\rho_X
\propto
G^{\rm BKM}

is automatically insensitive to a pure energy-zero shift.

This gives the exact algebraic retyping:

\boxed{
\begin{aligned}
\text{central energy offset}
&\longrightarrow
\text{zero horizontal BKM length},
\\
\text{noncentral state deformation}
&\longrightarrow
\text{positive scale susceptibility},
\\
\text{global norm lift}
&\longrightarrow
\Lambda_{\rm g}.
\end{aligned}}

The local vacuum catastrophe is therefore not repaired by canceling a vast number against another vast number.

The offset lies in a direction to which the local response metric is blind.

The separate global/radiative-stability problem remains in the tractor norm or top-form sector.

⸻

12. The revised Ruble equations

Here is the cleanest complete package I can presently defend.

R1 — Causal scale

\boxed{
g_{\rm phys}=\sigma^{-2}\bar g,
\qquad
N=-\ln\frac{\sigma}{\sigma_c},
\qquad
I_A=\frac14D_A\sigma.
}

R2 — Normal chirality

\boxed{
Q=P_+-P_-,
\qquad
Q^2=\mathbf1,
\qquad
JQJ=-Q.
}

R3 — Cocycle soldering

\boxed{
\theta
=
\varrho_\perp(N-N_c).
}

For the fundamental normal/scale pair,

\boxed{\varrho_\perp=1.}

R4 — Binary information geometry

\boxed{
\Psi(\theta)=\ln(2\cosh\theta),
}

\boxed{
\eta=\Psi'(\theta)=\tanh\theta,
}

\boxed{
g_{\theta\theta}^{\rm BKM}
=
\Psi''(\theta)
=
\operatorname{sech}^2\theta.
}

R5 — Transverse capacity

\boxed{
G^{\perp}_{NN}
=
C_{\perp,c}
\varrho_\perp^2
\operatorname{sech}^2\theta.
}

R6 — Modular free-energy source

\boxed{
\rho_X
=
\frac{k_BT_c}{2V_c}
G^{\perp}_{NN}.
}

R7 — Horizon capacity ratio

\boxed{
\gamma_{\perp,c}
=
\frac{C_{\perp,c}}{S_c/k_B}.
}

Einstein-wall universality is

\boxed{\gamma_{\perp,c}=1.}

R8 — Hawking–Friedmann conversion

\boxed{
k_BT_c\frac{S_c}{k_B}
=
E_{\rm MS,c}
=
\rho_{\rm crit,c}V_c.
}

R9 — Completed source law

\boxed{
\rho_X(N)
=
\frac{
\gamma_{\perp,c}\varrho_\perp^2
}{2}
\rho_{\rm crit,c}
\operatorname{sech}^2[
\varrho_\perp(N-N_c)].
}

R10 — Crossing normalization

\boxed{
\Omega_{X,c}
=
\frac{\gamma_{\perp,c}\varrho_\perp^2}{2},
}

\boxed{
r_c^{\rm ord}
=
\frac{
\gamma_{\perp,c}\varrho_\perp^2
}{
2-\gamma_{\perp,c}\varrho_\perp^2
}.
}

For the fundamental Einstein wall,

\boxed{
\gamma_{\perp,c}
=
\varrho_\perp
=
1
\Longrightarrow
r_c^{\rm ord}=1.
}

R11 — Conservation and shape

\boxed{
w_X
=
-1+
\frac{2\varrho_\perp}{3}\tanh\theta,
}

\boxed{
9(1+w_X)^2
+
6\frac{dw_X}{dN}
=
4\varrho_\perp^2.
}

R12 — Tractor response

\boxed{
\left(
\nabla_a\nabla_b+P_{ab}
\right)_0\sigma
=
\frac{4\pi G}{c^4}
\sigma
\left(
T^m_{ab}+T^X_{ab}
\right)^\circ,
}

\boxed{
I^2
=
\frac{2\pi G}{3c^4}T
-
\frac{\Lambda_{\rm g}}3.
}

R13 — Central blindness

\boxed{
\operatorname{Var}(K+\alpha\mathbf1)
=
\operatorname{Var}(K).
}

That is the complete symbolic unity:

\boxed{
\text{normal chirality}
\longrightarrow
\text{BKM shape}
\longrightarrow
\text{capacity}
\longrightarrow
\text{modular free energy}
\longrightarrow
\text{critical density}
\longrightarrow
\text{tractor transport}.
}

⸻

13. What has actually been completed

The old question was:

\text{Why should }\chi_\perp\varrho_\perp^2
=
\rho_m(N_c)?

The better question is:

\text{What converts the BKM Hessian into energy density?}

The answer is

\boxed{
\frac{k_BT_c}{2V_c}.
}

Then the horizon entropy converts the number of information-geometric response units into the Misner–Sharp energy:

k_BT_c\frac{S_c}{k_B}=E_{\rm MS,c}.

Flat Friedmann geometry converts that energy into the critical density:

E_{\rm MS,c}/V_c=\rho_{\rm crit,c}.

So the dimensionful scale is no longer inserted as a new constant. It is supplied relationally by the crossing causal diamond.

The amplitude gap has therefore been reduced to:

\boxed{
\gamma_{\perp,c}=1?
}

That is not the original ugly coincidence

\rho_*=\rho_m(N_c).

It is the precise information-theoretic question:

Does the fundamental horizontal response saturate the Einstein causal diamond’s capacity, whose variance equals its entropy?

Within that universality class, the r_c derivation is complete.

⸻

14. The one remaining proof obligation

I would now state the final theorem target this way:

Fundamental Einstein-wall theorem — target

For the self-dual apparent-horizon cut of a flat FLRW state:

1. the homogeneous J-odd horizontal quotient is the fundamental normal chirality pair;
2. the Connes cocycle identifies its characters with scale and inverse-scale characters;
3. the BKM norm of that horizontal tangent saturates the causal-diamond entanglement capacity;
4. the causal-diamond capacity equals its Bekenstein–Hawking entropy.

Then

Q^2=1,
\qquad
\varrho_\perp=1,
\qquad
\gamma_{\perp,c}=1,

and hence

\boxed{
\rho_X(N_c)
=
\rho_{\rm ordinary}(N_c).
}

The first two clauses are representation theory plus the physical identification of the horizontal quotient.

The last two clauses are a horizon-capacity universality statement. They hold in controlled Einstein-holographic settings and have independent causal-diamond/de Sitter support, but they are not presently a general theorem for dynamical FLRW horizons. 

That is the exact place where the programme now meets existing quantum-gravity research.

No arbitrary dark-energy function remains.

No arbitrary local scalar action is needed.

No separate r_c=1 postulate remains inside the Einstein-wall universality class.

What remains is to prove that the actual FLRW self-dual wall belongs to that class.

That is a single, sharp, calculable problem—not an invitation to invent more epicycles.
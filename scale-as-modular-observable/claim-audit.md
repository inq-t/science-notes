# Claim Audit

The Revision 2 monograph contains a strong exact core, several useful conditional deductions, two invalid closure arguments, and a numerical artifact in its flatness ceiling that both props up one of those arguments and generates a spurious prediction of its own. The safest reading is to preserve the exact algebra while restating the proposed physical identifications as assumptions or open problems.

## Exact or standard pieces

The following calculations survive the audit in their stated regimes:

- For a balanced two-outcome quotient, $\langle Q\rangle=\tanh\theta$, $g^{\mathrm{BKM}}=\operatorname{sech}^2\theta$, and $\langle Q\rangle^2+g^{\mathrm{BKM}}=1$. The balance assumption matters: $Q^2=1$ alone does not fix equal degeneracies or the partition function $2\cosh\theta$.
- The reflected symmetrized relative entropy is $4\theta\tanh\theta$, with a unique minimum at $\theta=0$.
- A measurable, rank-one, ratio-dependent additive cocycle coefficient is logarithmic: $\theta=\varrho_\perp(N-N_c)$.
- Given $\rho_X=A\operatorname{sech}^2[\varrho_\perp(N-N_c)]$ and separate conservation, the equation of state, Riccati flow, CPL locus, and invariant follow algebraically; [[causal-scale-theory/unit-branch|the unit branch]] records the unit-slope specialization.
- Given the stated area entropy, canonical $2\pi$ temperature, flat apparent horizon, and Misner--Sharp marginality, $(k_BT_c/V_c)(S_c/k_B)=\rho_{\mathrm{crit},c}$.
- The internal Darboux factorization

  $$
  \mathcal A=\partial_\theta+\tanh\theta,
  \qquad
  \mathcal A^\dagger=-\partial_\theta+\tanh\theta
  $$

  gives

  $$
  \mathcal H_-=-\partial_\theta^2+1-2\operatorname{sech}^2\theta,
  \qquad
  \mathcal H_+=-\partial_\theta^2+1,
  $$

  with the normalized zero mode $2^{-1/2}\operatorname{sech}\theta$ and a reflectionless continuum.

## The free-energy step is constitutive

For one fixed KMS reference $\omega_c$,

$$
F_c(\rho)-F_c(\omega_c)
=k_BT_cS(\rho\Vert\omega_c)
$$

is exact in the appropriate regulated or algebraic formulation. Revision 2 then uses the neighboring-state expansion

$$
S(\omega_{N+\mathrm dN}\Vert\omega_N)
=\frac12G_{NN}(N)\,\mathrm dN^2+O(\mathrm dN^3)
$$

as though it were the finite-reference difference

$$
F_c(\omega_{N+\mathrm dN})-F_c(\omega_N).
$$

It is not. The latter is

$$
k_BT_c\left[
S(\omega_{N+\mathrm dN}\Vert\omega_c)
-S(\omega_N\Vert\omega_c)
\right]
$$

and generically has a term linear in $\mathrm dN$. In the balanced binary family with $\omega_c=\omega_0$,

$$
S(\omega_\theta\Vert\omega_0)
=\theta\tanh\theta-\ln\cosh\theta,
$$

so

$$
\frac{\mathrm d}{\mathrm d\theta}
S(\omega_\theta\Vert\omega_0)
=\theta\operatorname{sech}^2\theta,
$$

which is nonzero away from the crossing. A stepwise reference free energy would be a different construction, and infinitesimal pairwise costs do not automatically sum to a global Dirichlet functional. Therefore

$$
\rho_X(N)=\frac{k_BT_c}{2V_c}G_{NN}^{\perp}(N)
$$

must be stated as a constitutive source law.

## Failed closure arguments

### Conformal weights do not quantize the slope

The monograph argues that equivariant soldering through density bundles $\mathcal E[n]$ forces $\varrho_\perp\in\mathbb Z^+$, after which a cosmological ceiling selects one. This does not follow. Conformal density bundles $\mathcal E[w]$ exist for real weights $w$; listing integer tensor powers exhibits examples but does not exclude real characters.

The valid conclusion of the cocycle functional equation is only

$$
\varrho_\perp\in\mathbb R.
$$

Unit slope is a physical fundamental-character choice. The ceiling used in the historical closure is also evaluated on an already response-normalized branch, so it cannot independently derive the slope while the normalization is advertised as a later output. That circularity is not the ceiling's only defect: the ceiling is numerically an artifact, for the separate reason recorded next.

### The rate ceiling is a radiation artifact

Revision 2 derives a maximum admissible slope and uses it twice: as the second leg of the $\varrho_\perp=1$ uniqueness argument, and as the standalone prediction that no flat solution exists above it. Both uses fail, because the ceiling is computed from a flatness condition different from the one the monograph's own benchmark uses.

Write the present-flatness closure in repaired variables. With

$$
x_c:=-N_c=\ln\frac{a_0}{a_c},
\qquad
M(x):=\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x},
\qquad
D:=1-\Omega_{m0}-\Omega_{r0},
$$

and $F_\nu(x):=M(x)\operatorname{sech}^2(\nu x)$, the condition at $\mathfrak R_c=1$ is

$$
F_\nu(x_c)=D.
$$

Sections 14(b) and A.5 instead drop the radiation term from the evolving density while keeping it inside the constant $D$; A.8 retains it. The same closure is written two incompatible ways in one document, and the ceiling is derived from the reduced form.

The asymptotics decide the question:

$$
M=\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}
\;\Longrightarrow\;
F_\nu\sim4\Omega_{r0}e^{(4-2\nu)x},
$$

$$
M=\Omega_{m0}e^{3x}
\;\Longrightarrow\;
F_\nu\sim4\Omega_{m0}e^{(3-2\nu)x}.
$$

Dropping radiation moves the threshold for unbounded growth from $\nu<2$ to $\nu<3/2$, manufacturing a finite ceiling above $3/2$ where none exists. The reduced form also cannot represent the true root structure. For it, $\mathrm d\ln F_\nu/\mathrm dx=3-2\nu\tanh(\nu x)$ is monotone decreasing, so $F_\nu$ is unimodal and admits at most two positive roots. With radiation the logarithmic derivative instead rises from $3$ toward $4$ while $2\nu\tanh(\nu x)$ saturates, so the same function can increase, decrease, and increase again, admitting three.

Recomputed at the monograph's benchmark $\Omega_{m0}=0.310598$, $\Omega_{r0}=9.15\times10^{-5}$:

| $\nu$ | positive roots of $F_\nu(x_c)=D$ | roots with radiation dropped from $M$ |
|---|---|---|
| $1.5$ | one: $0.356864$ | one: $0.357138$ |
| $1.558402$ | three: $0.371675$, $6.106787$, $6.106956$ | two: $0.371986$, $5.043480$ |
| $1.7$ | three: $0.429266$, $1.438413$, $12.548049$ | two: $0.429780$, $1.434858$ |
| $1.814657$ | one: $20.342870$ | none |
| $1.99$ | one: $377.040688$ | none |
| $2$ | none | none |

The reduced form loses its last root at $\nu\simeq1.814132$, reproducing the monograph's quoted $1.8141$. The exact closure retains a root for every $\nu<2$ and has none at $\nu\ge2$.

Three consequences:

- The claim that no flat solution exists above the ceiling is false. The exact existence bound is $\nu=2$. Because it is set by the radiation exponent rather than the matter exponent, it requires only $\Omega_{r0}>0$ and is otherwise independent of both abundances; the monograph's $\Omega_m$-dependent ceiling table therefore describes no corresponding fact. Setting $\Omega_{r0}=0$ strictly throughout does restore a matter-driven fold near $1.814$, but that is a different model from the benchmark, which carries radiation.
- The $\varrho_\perp=1$ uniqueness argument loses its second leg as well as its first. The integer alternative $\varrho_\perp=2$ does remain excluded, but marginally and for a different reason: $\nu=2$ is exactly the value at which the radiation term stops growing, so at $\nu=2$ the closure has no root while every $\nu<2$ has one. The exclusion carries no $\Omega_m$-dependent margin, so the reported first admissibility at $\Omega_m=0.34685$ and its $3.8\sigma$ significance have no corresponding fact either. The separate direct-fit exclusion of $\varrho_\perp=2$ is a different argument, subject to the general reproducibility caveat below rather than to this one.
- What survives is a branch statement, not an existence statement. As $\nu\to2^-$ the surviving root runs to arbitrarily large $x_c$ — about $20$ at $\nu=1.8147$ and about $377$ at $\nu=1.99$ — that is, a crossing at unphysical redshift. Rejecting those solutions is a declared late-time prior, not a theorem.

The near-coincidence of two numbers is why the artifact is hard to see. The reduced-form ceiling $1.814132$ sits very close to $1.814657$, which in the exact closure is the terminal fold of the smallest positive root continuously connected to the late-time branch. The quoted figure is thus approximately right about a different fact. Above it the late branch is gone while radiation-driven roots persist; below it, from $\nu\simeq1.558402$ upward, the exact closure already has three positive roots rather than one.

The corrected root atlas, the distinction between strict-dust and hybrid fold values, and the explicit late-branch declaration are developed in [[causal-scale-theory/flatness-branches|present flatness and the crossing branches]].

### A normal plane is not automatically a 2D CFT

The fact that a cut has a two-dimensional Lorentzian normal vector space does not produce a standalone $1+1$-dimensional conformal field theory. Geometric boost modular flow can occur in a higher-dimensional QFT while transverse degrees of freedom remain present. Cardy's formula additionally requires an actual 2D CFT and the appropriate state, geometry, and thermodynamic regime.

Therefore the chain

$$
\text{2D normal plane}
\Longrightarrow \text{2D CFT}
\Longrightarrow C=S
\Longrightarrow \gamma_{\perp,c}=1
$$

is invalid. Equality of capacity and entropy may motivate [[program-core/ruble-equations#RE6 — Integrated crossing capacity|weak Ruble matching]], but it is not derived here.

### Modular generators and capacities must be distinguished

The monograph uses $K$ both for the algebraic modular generator $-\ln\Delta$ and for a density-matrix modular Hamiltonian $-\ln\rho$. These are not generally the same object. In particular, $\langle-\ln\rho\rangle=S(\rho)$, while no such entropy identity follows for $-\ln\Delta$ without further representation-specific work.

For a density matrix, the BKM norm of the explicit temperature-rescaling family generated by $K_0=-\ln\rho_0$ is indeed $\operatorname{Var}_{\rho_0}(K_0)$. That does not prove that the proposed scale tangent is this direction or that it exhausts the wall's capacity. The binary family itself makes the distinction visible:

$$
\operatorname{Var}_{\omega_\theta}(-\ln\omega_\theta)
=\theta^2\operatorname{sech}^2\theta,
$$

whereas its $Q$-coordinate BKM metric is $\operatorname{sech}^2\theta$. At $\theta=0$ the first vanishes and the second equals one.

## Claims that need narrower wording

| Monograph claim | Corrected status |
|---|---|
| Cocycle continuity supplies measurability | Continuity in modular parameter $t$ does not establish regularity in the external scale ratio; ratio-regularity is a separate assumption. |
| Horizontal scale change is modular-temperature rescaling | The BKM norm of an explicitly chosen modular-Hamiltonian rescaling is a variance, but the physical FLRW horizontal tangent has not been shown to be that rescaling. |
| BKM norm equals full horizon capacity | The variance identity is exact when the score is the centered modular Hamiltonian; identifying the binary scale tangent with that direction and with the extensive full-wall capacity is physical input. |
| Relative-entropy curvature derives $\rho_X(N)$ | The fixed-reference free-energy identity yields a local Hessian at coincidence. Promoting it to an all-history density is a constitutive extension. |
| Equality at the crossing is a theorem without qualification | It follows after the source law, horizon bridge, and $\mathfrak R_c=1$ closure are assumed. |
| The flatness ceiling $\varrho_\perp\lesssim1.814$ is an existence bound | It is an artifact of dropping radiation from the evolving density. The exact closure has a positive root for every $\nu<2$ and none at $\nu\ge2$, and that bound is independent of $\Omega_m$. |
| The ceiling plus integrality selects $\varrho_\perp=1$ uniquely | Both legs fail: conformal weights are real, and the ceiling is a reduction artifact. Unit slope is a representation choice, and rejecting high-redshift roots is a branch prior. |
| Crossing, density maximum, and $w_X=-1$ coincide distinctively | For any positive separately conserved component, an interior density extremum already implies $w=-1$. Equality with the ordinary sector is the model-specific part. |
| The entropy minimum fixes the crossing date intrinsically | It identifies $\theta=0$, hence the midpoint already encoded by $N_c$; its cosmic date follows only after the amplitude law, flatness, present abundances, and a branch choice. |
| Relative-entropy positivity fixes the time orientation | The phantom-to-quintessence orientation follows from the chosen profile, positive slope, increasing $N$, and conservation. Positivity is even under $\theta\mapsto-\theta$ and does not select an arrow. |
| The binary carries exactly one bit at the crossing | The reduced binary state has entropy $\ln 2$ nats, or one bit in base two. This says nothing about the full wall entropy. |
| The Riccati equation is a saddle-node theorem | It is an autonomous flow with two fixed points; a saddle-node bifurcation needs an additional control-parameter construction. |
| One finite acceleration episode follows from the binary alone | This is branch-dependent and also uses the closed amplitude, matter/radiation background, flatness, expansion, and zero residual. |
| The Witten pair is the cosmological perturbation operator | The factorization is exact internal state-space mathematics. No map to conserved scalar, vector, or tensor FLRW perturbations has been constructed. |
| A retarded pole follows from the internal scattering problem | $\theta$ is not physical time, and retardedness depends on a physical evolution equation and convention not supplied by the factorization. |
| Vacuum blindness solves the cosmological constant problem | Normalized states are blind to central shifts and the trace-free Einstein equation is blind to pure-trace sources, but the scalar/global trace channel and radiative stability remain open. |
| Every constant cancels in the horizon bridge | $\hbar$ and $k_B$ cancel; $G$ and $c$ remain inside $\rho_{\mathrm{crit}}$. The sound conclusion is that the bridge introduces no new constant. |
| The model is parameter-free | It has no adjustable dark-history parameter only after physical choices and sector data are fixed; its benchmark still depends on ordinary abundances, normalization, flatness, expansion, and the residual branch. |

## Formula and notation corrections

- Normalize $N=\ln(a/a_0)$ and $N_c=\ln(a_c/a_0)$, then use $x=N-N_c$. This removes the monograph's tension between defining $N$ relative to the crossing and later using $N_c\ne0$.
- The magnitude definition of the apparent-horizon index is $\mu_A=|1-q|/2$. The signed relation $(1-q)/2$ is valid only after choosing the $q\le1$ branch or defining a signed index.
- The present-flatness condition appears in two incompatible forms. Sections 14(b) and A.5 use the matter-only evolving density $\Omega_{m0}e^{3x}$, while A.8 uses $\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}$. The second is correct, since the crossing equality is with the complete non-response sector; the ceiling derived from the first is an artifact.
- The symbol $r_c$ drifts by a factor of two. Section 17 defines it as $\gamma\varrho_\perp^2/2$, hence $\tfrac12$ on the main branch and equal to $\Omega_{X,c}$, while the ceiling equation of §14(b) and A.5 numerically requires $r_c=1$ because its normalization is $\rho_*=\rho_m(N_c)$ rather than $\rho_*=\rho_{\mathrm{ordinary}}(N_c)$. Use $\mathfrak R_c=2\Omega_{X,c}$ throughout and state the reference sector explicitly; the two normalizations differ by $1/(1-2\Omega_{r,c})$.
- In the density-only form of the invariant, the peak density is $\rho_*$; the occurrence of `rho__` in the monograph is a typo.
- Revision 2 correctly uses $j=q+2q^2-\mathrm dq/\mathrm dN$. The earlier plus-sign version in the development history was wrong.

## Source and evidence status

The scripts in the chat archive check algebraic identities and benchmark arithmetic. Such receipts cannot validate the physical identifications used as their inputs. Their ceiling checks additionally inherit the reduced flatness condition: both scripts solve for the crossing with a matter-only evolving density, so neither can detect the radiation-driven roots, and each uses a single root bracket that cannot return more than one root even where three exist. Their agreement with the monograph's $1.8141$ therefore confirms the reduction rather than the ceiling. Some outputs advertised during chat 02 are absent from that chat's own archive, and the later copied scripts do not repair that provenance gap. Chat 02 also labels a receipt as using no external data while hardcoding matter and radiation abundances and an observational uncertainty; that is a numerical branch check, not a data-free theorem.

The observational comparisons in Revision 2 are versioned research claims. They have not been independently reproduced by this folder audit, and the open perturbation sector prevents a complete CMB, lensing, and growth likelihood. They should be cited as reported model checks rather than established measurements of modular capacity.

Revision 2 also contains damaged TeX inherited during document generation, including commas in place of multiplication spacing, malformed boxes, `rho__` in place of $\rho_*$, and a corrupted cocycle exponential. The modular notes in this folder use repaired formulas rather than silently treating the long document as a clean equation source.

Two bibliography entries need rechecking before scholarly reuse: the description attached to arXiv:2208.09302 does not match that identifier, and arXiv:0904.2765 is an AdS black-hole enthalpy paper rather than a direct source for the FLRW Kodama--Hayward temperature.

## Repaired closure

The clean repair is the one adopted by [[causal-scale-theory/sources/legacy/unpacked-v7-package/causal_scale_dynamics_v7/Causal_Scale_Dynamics_Master_v7_0|Causal Scale Dynamics v7.0]]:

- keep the binary and cocycle calculations with explicit hypotheses;
- state $\varrho_\perp=1$ as the fundamental-character choice;
- define the physical pullback norm $G_{NN}^{\perp}$ so coordinate slope and capacity are not double-counted; and
- state

  $$
  \mathfrak R_c
  :=\frac{k_B}{S_c}G_{NN}^{\perp}(N_c)=1
  $$

  as the Scale--Capacity Equivalence Principle.

This produces a coherent conditional background theory without pretending that its amplitude law has already been proved.

The ceiling is repaired separately, and later. Version 7 inherits the unit branch, where the artifact is invisible because a single positive root exists there for every admissible rate. Keeping $\nu$ and $\mathfrak R_c$ explicit is what exposes it, so the corrected root atlas and the late-branch declaration are now canonical in [[causal-scale-theory/flatness-branches|present flatness and the crossing branches]]. A rate or amplitude that is allowed to vary must carry an explicit branch choice with it.

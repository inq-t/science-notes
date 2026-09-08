# The Scale Torsor and the Global--Local Gap Invariant

A scale family can preserve a dimensionless transfer depth while its dimensional spectral edge changes between members. This covariance concerns matched operators, lengths and Hilbert carriers; it does not assert dilation symmetry within one fixed theory. A scale torsor supplies relative scale ratios, while selection of a physical member, a change of reporting units and a choice of conformal metric section remain different operations.

**Status: [EXACT] for the torsor covariance and spectral consequences under the stated hypotheses; [CONDITIONAL] for the global--local reconstruction schema; [OPEN] for the upstream Yang--Mills carrier, scale selector, uniform coercivity, and continuum reconstruction.**

## “No scale” has two inequivalent meanings

Let \(\mathcal S\) be a principal \(\mathbb R_{>0}\)-torsor. Here its points label the family parameter, and

$$
(\lambda,s)\longmapsto \lambda s
\tag{S1}
$$

is free and transitive. There is no distinguished point in \(\mathcal S\), but ratios of two points are defined. This is the type of an **unpointed scale family**. Interpreting its members as physical theories or only as presentations requires a separate comparison contract.

It must be distinguished from **no intrinsic physical scale**. A conformal theory may have the latter property. A massive theory can lack a preferred numerical unit while still possessing invariant dimensionless ratios and a nonzero element of an inverse-length quantity line. Changing metres to centimetres changes its numerical representative, not the theory.

[[conformal-scale-geometry/causal-order-and-metric-scale|Causal order and metric scale]] gives the corresponding spacetime statement: causal order determines a conformal class under its hypotheses, while a positive scale section selects a metric representative. It does not select that section.

## What “invariant yardstick” must mean

Three distinct questions sit behind the word invariant:

- Does the number survive a change of measurement units?
- Does it survive a coordinate change on its mathematical carrier?
- Is it unchanged under the physical frame transformations of the theory?

The quotient \(v/c\) passes the first test but generally not the third: different inertial observers assign different velocities to the same massive trajectory. A Poincare mass ratio passes the third when both masses are scalars of the reconstructed representation. A bare dimensionless Hessian eigenvalue can fail the second; [[hessian-response-geometry/relative-response-spectrum|the relative-response spectrum]] shows why both the response and its reference metric must be transported.

The role of \(c\) is particularly instructive. It relates length and duration, but the simultaneous calibration change \(\ell\mapsto a\ell,\ t\mapsto at\) leaves \(\ell/t\) unchanged. It therefore cannot select either scale by itself. Choosing a numerical unit for either quantity is a metrological operation; it is not a proof that every conceivable length comparison requires light signals. Geometrically, the stronger relevant statement remains that causal cones do not choose a conformal scale section.

For a Yang--Mills prediction the target is correspondingly a relation

$$
\frac{m_{\mathrm{gap}}c^2}{E_*}=C_{\mathrm{gap}},
\tag{S1a}
$$

where the upstream geometry must determine the normalized coefficient and independently construct or select the reference energy \(E_*\). A lower-bound theorem returns \(\geq\underline C>0\), not equality with the lightest glueball mass. Identifying a particular glueball also requires the appropriate gauge-invariant channel and spectral support; an all-channel gap theorem is a different result.

An integer such as \(3\) or \(8\) can constrain \(C_{\mathrm{gap}}\) through representation geometry or a proved response spectrum. It cannot be inserted as that coefficient merely because it occurs in the carrier's dimension. Likewise, \(G\), a horizon temperature, and a cosmological rate are admissible **candidate calibration data**, but their relevance must be established by a comparison law rather than by their ability to repair units.

## The actions and their conventions

For (S2)–(S8), hold the reporting units and \(\hbar,c\) fixed and use the active family convention \(\ell_{\lambda s}=\lambda\ell_s\). A corresponding inverse-length generator scales as \(K_{\lambda s}=\lambda^{-1}K_s\) after unitary transport. By contrast, replacing a passive length-unit basis by \(u_L^{\prime}=\lambda u_L\) sends the numerical coefficient of a fixed length to \(\ell_{\mathrm{num}}/\lambda\), and the coefficient of a fixed inverse length to \(\lambda K_{\mathrm{num}}\). The invariant product is unchanged in either case, but the parameter actions are inverse. Neither action selects a physical member.

The [[quantity-lines-and-conformal-scales|quantity-line comparison]] keeps these unit changes distinct from choosing a geometric scale section. Differentiation between moving Hilbert carriers needs the separate [[scale-score-connection/inq|connection and domain data]].

## A scale-equivariant family

Suppose every \(s\in\mathcal S\) gives a pointed complex Hilbert presentation

$$
(\mathcal H_s,\Omega_s,K_s,\mathfrak A_s),
\tag{S2}
$$

where \(K_s\geq0\) is a self-adjoint inverse-length Euclidean generator, \(\|\Omega_s\|=1\), and \(\ker K_s=\mathbb C\Omega_s\). Write \(P_{0,s}=|\Omega_s\rangle\langle\Omega_s|\). Assume \(\Omega_s^\perp\ne0\) to discuss a nontrivial excitation edge. The uniqueness assumption makes the single-vacuum complement and full zero-spectral complement agree. Suppose scale transport is implemented by unitaries \(U_{\lambda,s}:\mathcal H_s\to\mathcal H_{\lambda s}\) satisfying \(U_{\mu,\lambda s}U_{\lambda,s}=U_{\mu\lambda,s}\), \(U_{1,s}=I\), and

$$
U_{\lambda,s}\Omega_s=\Omega_{\lambda s},
\qquad
K_{\lambda s}U_{\lambda,s}
=\lambda^{-1}U_{\lambda,s}K_s.
\tag{S3}
$$

Equation (S3) means the self-adjoint operator equality \(K_{\lambda s}=\lambda^{-1}U_{\lambda,s}K_sU_{\lambda,s}^*\), with \(U_{\lambda,s}D(K_s)=D(K_{\lambda s})\). Functional calculus then also transports their form domains. No algebra or field transport follows merely from the tuple (S2); an application must supply it.

For matched lengths \(\ell_{\lambda s}=\lambda\ell_s\), the dimensionless transfer is natural:

$$
U_{\lambda,s}e^{-\ell_sK_s}U_{\lambda,s}^*
=e^{-\ell_{\lambda s}K_{\lambda s}}.
\tag{S4}
$$

Consequently the dimensionless form

$$
\widehat{\mathfrak h}_s[\psi]
:=\ell_s\|K_s^{1/2}\psi\|^2,
\qquad \psi\in D(K_s^{1/2}),
\tag{S5}
$$

and its vacuum-complement floor

$$
\boxed{
\widehat\Delta
:=
\inf_{\substack{\psi\in D(K_s^{1/2}),\ \psi\perp\Omega_s\\\|\psi\|=1}}
\ell_s\|K_s^{1/2}\psi\|^2}
\tag{S6}
$$

are independent of the chosen presentation. Equation (S6), or equivalently the matched-slab attenuation

$$
-\log\|e^{-\ell_sK_s}(I-P_{0,s})\|,
\tag{S7}
$$

is a candidate invariant between the “globaled” and “localed” registers. The global object can carry its natural equivalence class without carrying one preferred numerical ruler.

After a physical clock and Osterwalder--Schrader or direct Hamiltonian reconstruction have been proved,

$$
H_s=\hbar cK_s,
\qquad
\Delta_{E,s}=\frac{\hbar c}{\ell_s}\widehat\Delta.
\tag{S8}
$$

Only after a positive-energy Poincare representation is reconstructed may the same lower edge be called a mass gap. The factors \(c\) and \(\hbar\) convert registers; they do not create (S6).

A section may itself be selected by a [[the-grain-of-causal-scale/relational-grain-construction|matched-ledger construction]], but there is no reason for two different carriers to select the same member. The cosmological common-count length is therefore a model of the method, not a default Yang--Mills input. A Yang--Mills yardstick must be reconstructed from ledgers natural to its own whole-law carrier, or derived with both theories from one proved common upstream object.


## A one-scale family and its coefficient

The [[dilation-covariant-spectra/inq|dilation no-gap theorem]] applies to one operator on one Hilbert carrier. It does not forbid covariance of a *family* of theories carrying different nonzero scale parameters. Let

$$
\mathfrak T_\Lambda
=
(\mathfrak A_\Lambda,\omega_\Lambda,U_\Lambda),
\qquad
\Lambda>0,
$$

denote a putative one-scale family, with \(\Lambda\) energy-valued and the unit basis suppressed. If enlarging lengths by \(e^s\) induces comparison isomorphisms

$$
\mathfrak D_s^\Lambda:
\mathfrak T_\Lambda
\longrightarrow
\mathfrak T_{e^{-s}\Lambda},
\qquad
\mathfrak D_s^{e^{-t}\Lambda}
\circ
\mathfrak D_t^\Lambda
=
\mathfrak D_{s+t}^\Lambda,
\tag{D1}
$$

after the domains and identifications have been made precise, then (D1) relates *different members*. It is not the forbidden internal relation \(V_sH_\Lambda V_s^*=e^{-s}H_\Lambda\) on one fixed carrier. A fixed member with \(\Lambda>0\) can therefore be gapped even while the unpointed family is covariant under changes of scale.

Suppose the comparison maps also transport the physical translation spectrum. Homogeneity then requires

$$
\Delta_E(e^{-s}\Lambda)
=
e^{-s}\Delta_E(\Lambda).
\tag{D2}
$$

For a genuinely one-scale family this gives

$$
\boxed{
\Delta_E(\Lambda)
=
\kappa\Lambda,}
\tag{D3}
$$

where \(\kappa\) is dimensionless. Equation (D3) separates two questions that are often blurred. Family covariance explains why any gap, if present, scales linearly with the sole yardstick. It does not prove \(\kappa>0\). That strict inequality is precisely the infrared coercivity theorem still owed.

Here all other dimensionless parameters, such as a theta angle when admitted, are held fixed; otherwise \(\kappa\) may depend on them. Selecting \(\Lambda\) relative to another physical sector fixes a member, while reporting that selection in MeV chooses a unit. A renormalization-scheme change is a third operation: it reparametrizes the same physical member. For a positive dimensionless conversion constant,

$$
\Lambda_{\mathsf s'}
=
C_{\mathsf s'\mathsf s}\Lambda_{\mathsf s}
$$

must be accompanied by

$$
\kappa_{\mathsf s'}
=
C_{\mathsf s'\mathsf s}^{-1}\kappa_{\mathsf s}
$$

so that \(\Delta_E\) is unchanged. Neither selection of a member, choice of units nor reparametrization proves \(\kappa>0\). The [[yang-mills-scale-and-gravity-decoupling|Yang–Mills scale and decoupling contract]] retains the quantum anomaly and pure-gauge recovery requirements.


## Positivity is an additional construction

The exact family identities permit \(\widehat\Delta=0\). A state, boundary law or independently normalized reference quantity may select a member, but positivity requires an estimate on its full physical carrier. Merely specifying a quantity line does not choose a nonzero element of that line. The [[scale-relative-response-and-yang-mills|scale-relative response construction]] states a sufficient form-core comparison, its normalization counterexample and the condition for a causal-patch limit.

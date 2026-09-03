# The \(\hbar\), Clock, and Calibration Firewall

Planck's constant does not by itself supply time: it is an action-to-phase conversion, equivalently an energy-to-frequency or momentum-to-wavenumber comparison only after the corresponding clock or spatial translation parameter exists. This distinction becomes decisive in any proposal that places mass upstream of observable spacetime. Such a proposal may use \(E=\hbar\omega\) and \(m=\hbar\omega/c^2\) as downstream reconstruction identities, but it cannot use them to explain the primitive origin of mass unless it independently constructs the one-parameter clock, its normalization, and the comparison between its generator and physical energy.

**Status: [EXACT] for the parameter-rescaling and quantity-line statements; [CONDITIONAL THEOREM] for the clock and length solders; [OPEN CONSTRUCTION] for deriving \(\hbar\), a clock normalization, or a Yang--Mills scale from pregeometric algebra.**

## A spectrum is not yet a frequency

Let

$$
S_s=e^{-sK},
\qquad s\geq0,
\tag{HC1}
$$

be a strongly continuous self-adjoint contraction semigroup with \(K\geq0\) on an analytic Hilbert carrier \(\mathcal H_K\). If \(s\) is only an abstract dimensionless order parameter, then every \(\lambda>0\) gives the equally valid presentation

$$
s'=\lambda s,
\qquad
S_s=e^{-s'K'},
\qquad
K'=\lambda^{-1}K.
\tag{HC2}
$$

Therefore the numerical gap of \(K\) is not an absolute physical rate until the parameter normalization has been selected independently. The semigroup can supply a kernel, spectral ratios, an additive depth, or an order. It does not supply seconds merely by being parameterized. Moreover, the positive Hilbert carrier and self-adjoint semigroup in (HC1) are an analytic scaffold; they may be pre-spacetime without thereby being pre-quantum, pre-observable, or ontologically primitive.

The same point applies to a unitary group. A self-adjoint operator \(A\) has a spectrum before its parameter has been interpreted as physical time. Only a declared representation

$$
U(\tau)=e^{-i\tau H/\hbar}
\tag{HC3}
$$

of clock translations makes the spectrum of \(H/\hbar\) an angular frequency spectrum. Calling an eigenvalue a frequency before constructing \(\tau\) reverses the dependency.

For a photon in reconstructed spacetime, the frequency measured by an observer is, up to the declared normalization conventions,

$$
\omega_{(u)}=-k_a u^a,
\tag{HC3a}
$$

where \(k_a\) is the null wave covector and \(u^a\) is the observer's timelike four-velocity. This genuinely presupposes causal geometry, an observer worldline, and a calibrated clock. It does not follow that every abstract spectral parameter presupposes spacetime; it follows that calling such a parameter a measured photon frequency does.

## What \(\hbar\) converts

As a typed quantity,

$$
[\hbar]
=
[\text{action}]
=
[\text{energy}]\,[\text{time}]
=
[\text{momentum}]\,[\text{length}].
\tag{HC4}
$$

Thus \(\hbar\) supports two familiar comparisons,

$$
E=\hbar\omega,
\qquad
p=\hbar k.
\tag{HC5}
$$

The first uses a clock-translation parameter; the second uses a spatial-translation parameter. Neither factorization says that \(\hbar\) contains an ontologically prior clock. More invariantly, a quantum phase is a character of action modulo \(2\pi\hbar\):

$$
\mathcal A
\longmapsto
e^{i\mathcal A/\hbar}.
\tag{HC6}
$$

This makes \(\hbar\) the comparison between action and dimensionless phase. Energy and momentum arise when that action is differentiated along already supplied temporal or spatial translation directions.

The reconstructed Poincare spectrum can even be stated without putting \(\hbar\) inside its generator. Fix signature \((+,-,-,-)\), let the self-adjoint translation generators \(\Pi_\mu\) strongly commute, and suppose their joint spectrum lies in the closed forward cone. With length-valued spacetime translation \(x^\mu\), joint spectral calculus then defines

$$
U(x)=e^{-ix^\mu\Pi_\mu},
\qquad
[\Pi_\mu]=L^{-1},
\qquad
\mu:=\bigl(\Pi^\mu\Pi_\mu\bigr)^{1/2}\geq0.
\tag{HC6a}
$$

The invariant spectral gap may then be stated as a positive lower edge for \(\mu\) off the vacuum. Planck's constant enters only when inverse length is expressed as momentum or mass:

$$
P_\mu=\hbar\Pi_\mu,
\qquad
m=\frac{\hbar}{c}\mu.
\tag{HC6b}
$$

This does not make the construction pregeometric—\(x^\mu\), the Poincare action, and its length calibration are already present—but it proves that \(\hbar\) is not what creates the spectral exclusion. [[mass-as-casimir-and-realization#Unit scale and conformal scale are different torsors]] gives the underlying quantity-line theorem.

There is nevertheless a real circularity hazard. If a proposed theory says that mass constitutes the clock and then obtains mass by multiplying an assumed clock frequency by \(\hbar/c^2\), it has borrowed the structure it meant to derive. The safe use of \(\hbar\) is on the reconstruction side, after the clock and translation representation exist. The same firewall applies to \(c\) if spatial and temporal quantity lines are themselves supposed to emerge: \(c\) may compare those reconstructed lines without serving as their unexplained upstream cause.

## The exact solder ladder and its missing data

Suppose the abstract parameter in (HC1) receives an independently constructed Euclidean-clock solder

$$
\tau_E=\beta s,
\qquad
[\beta]=T,
\qquad
\nu:=\frac{\mathrm ds}{\mathrm d\tau_E}=\beta^{-1},
\qquad
[\nu]=T^{-1}.
\tag{HC7}
$$

It first produces a frequency-typed generator,

$$
\Omega_K:=\nu K,
\qquad
e^{-sK}
=
e^{-\tau_E\Omega_K}.
\tag{HC8}
$$

This Euclidean equality does not alone produce reversible Lorentzian phase evolution or identify carriers. Let \(\mathcal H_K^{\mathrm{supp}}\subseteq\mathcal H_K\) be a declared closed reducing subspace for \(K\) generated by the endpoint data; if no endpoint reduction is needed, take \(\mathcal H_K^{\mathrm{supp}}=\mathcal H_K\). Write \(E_K\) for the spectral measure of the restricted generator. Reflection positivity and OS reconstruction, or another declared bridge, must construct a physical Hilbert carrier and, in the exact-equivalence case, a unitary endpoint identification

$$
W:\mathcal H_{\mathrm{phys}}\longrightarrow\mathcal H_K^{\mathrm{supp}},
\qquad
\Omega_{\mathrm{phys}}:=W^*\Omega_KW,
\qquad
U(t):=e^{-it\Omega_{\mathrm{phys}}}.
\tag{HC8a}
$$

Let \(P_K:=E_K(\{0\})\) on the supported analytic carrier and let \(P_0\) be the physical vacuum projection. The exact gap conversion below additionally assumes

$$
WP_0W^*=P_K,
\qquad
W(1-P_0)\mathcal H_{\mathrm{phys}}
=
(1-P_K)\mathcal H_K^{\mathrm{supp}}.
\tag{HC8aa}
$$

A further action solder \(\mathfrak a_Q>0\), with \([\mathfrak a_Q]=[\mathrm{action}]\), then defines, on the physical carrier,

$$
H:=\mathfrak a_Q\Omega_{\mathrm{phys}}
=
\frac{\mathfrak a_Q}{\beta}W^*KW.
\tag{HC8b}
$$

If reconstruction supplies only an isometry or a genuinely different carrier rather than this unitary equivalence, (HC8b) must be replaced by a cross-carrier quadratic-form comparison and a lower coverage bound; the equality may not be asserted.

Ordinary quantum theory identifies \(\mathfrak a_Q=\hbar\). Put \(\mathcal K_K:=(1-P_K)\mathcal H_K^{\mathrm{supp}}\). After Poincare reconstruction and the Casimir equivalence, a positive dimensionless edge \(\kappa=\inf\sigma(K|_{\mathcal K_K})\) becomes

$$
\Delta_E
=
\mathfrak a_Q\nu\kappa,
\qquad
m_{\mathrm{gap}}
=
\frac{\mathfrak a_Q\nu}{c^2}\kappa.
\tag{HC9}
$$

The length version additionally solders Euclidean duration and length by \(\tau_E=\ell/c\). Thus \(\ell=L_*s\) implies \(\beta=L_*/c\), and

$$
\Delta_E
=
\frac{\mathfrak a_Qc}{L_*}\kappa,
\qquad
m_{\mathrm{gap}}
=
\frac{\mathfrak a_Q}{cL_*}\kappa.
\tag{HC10}
$$

These are conditional conversion theorems, not origins of scale. If \(\beta\) or \(L_*\) is chosen from the desired mass, the construction is circular. If the primitive theory yields only \(K\) up to the rescaling (HC2), then it has not yet yielded an absolute mass. [[causal-patch-boundary-and-two-times]] gives the same normalization firewall for causal semigroups, and [[mass-as-a-calibrated-distinction-rate]] identifies the physical-side transfer depth to which a successful solder must connect.

## What can be pregeometric

A pregeometric construction can coherently supply any of the following without already supplying spacetime:

- an ordered family of algebras, carriers, or correspondences;
- a dimensionless composable cocycle or attenuation depth;
- a spectral order, kernel, index, or ratio invariant;
- an intrinsically normalized dimensionless modular parameter, while leaving its conversion to clock time open; or
- a relational comparison between two primitive rates in which arbitrary reparameterization cancels.

The last possibility is especially important. Absolute dimensionful numbers require a yardstick, but a ratio such as \(\gamma_1/\gamma_2\), a product fixed by an intrinsic duality, or a scale-free spectral inequality can be meaningful before seconds, metres, or kilograms are assigned. No operational claim that \(\hbar\) varies or has a uniquely predicted numerical value can be made without specifying a dimensionless observable ratio that changes; a coordinated unit redefinition is not physics. A viable Copernican programme should therefore derive the dimensionless invariant and the clock/length solder as separate arrows. It may then test whether \(\hbar\) is fundamental, emergent, or simply the universal conversion constant of the reconstructed quantum presentation.

## Three candidate mechanisms, correctly typed

Spectral action, Q-balls, and geons each demonstrate part of the desired reversal, but all three begin downstream of the proposed pre-spacetime ground.

1. In the [[library/the-spectral-action-principle/inq|Chamseddine--Connes spectral action]], \(\operatorname{Tr}f(D/\Lambda)\) turns the spectrum of a supplied Dirac operator and cutoff into observable gravitational, gauge, Higgs, and mass terms. It shows how geometry can organize matter coefficients, but \(D\), its represented carrier, and \(\Lambda\) are inputs. Its even bosonic trace is blind to \(D\mapsto-D\); this statement does not apply unchanged to the full fermionic-plus-bosonic action. The even trace therefore cannot select primitive orientation. [[spectral-wall-descent/observable-spectral-action]] owns this downstream boundary.
2. A [[library/q-balls/inq|Coleman Q-ball]] is a charge-constrained, nontopological soliton. Its standard stationary ansatz already uses a spacetime field, a global \(U(1)\) charge, a potential, and a phase frequency. That frequency is a reversible internal phase or chemical-potential parameter at fixed charge, not an irreversible factification rate. The construction proves that coherent phase rotation plus a nonlinear energy functional can make a localized massive object, not that frequency, charge, or spacetime has been generated. Its low-lying collective modes also warn that a stable soliton sector need not give a uniform vacuum-complement gap.
3. Wheeler's original [[library/geons/inq|geon]] construction treats electromagnetic radiation held together for many characteristic periods by its own gravitational attraction; later gravitational-geon work broadens the family. It is a clean “mass without material substance” precedent: field energy and geometry jointly create a rest-like localized configuration. But it assumes classical spacetime, Einstein dynamics, \(G\), and a clock with which lifetime and oscillation are measured; ordinary geon trapping is not by itself a topological knot and can be metastable.

The Q-ball and geon precedents share a recurrent-confinement grammar; spectral action contributes spectral organization but does not itself supply recurrence or confinement. The extractable confinement grammar is not “a wave becomes mass” but

$$
\boxed{
\text{recurrent phase or flux}
+
\text{a conserved or slowly leaking invariant}
+
\text{self-consistent confinement}
+
\text{scale balance}
\longrightarrow
\text{a localized stationary or metastable recurrent sector}.}
\tag{HC11}
$$

That grammar is a plausible realization target for a more primitive algebra. It is not yet a knot theorem. A geon may be dynamically trapped without a topological knot, while a Q-ball is explicitly nontopological. A knot, flux, or homotopy class can obstruct unwinding, but only a positive scale-balancing form can make that class energetically costly; even then, soft fluctuations in the trivial sector may remain. [[knotting-as-dimensional-presentation/inq]] owns this separation between three-dimensional presentation, topological sector labels, localized soliton energy, and a full vacuum gap.

A further no-go is decisive: a cavity can have a lowest nonzero normal-mode frequency while the classical energy of that mode tends continuously to zero with its amplitude. Mode spacing becomes a one-quantum energy floor only after an action/occupation normalization such as \(\mathfrak a_Q\), or after a nonlinear constraint such as fixed charge supplies a nonzero minimum. Confinement and resonance therefore do not by themselves create mass. The grammar remains weaker than a Yang--Mills mass-gap theorem, which must exclude arbitrarily low energy in **every** nonvacuum direction of the reconstructed infinite-volume carrier, including the topologically trivial sector.

## Stopping condition

An upstream use of \(\hbar\) is noncircular only if the construction states:

1. what dimensionless or action-valued object exists before clock time;
2. which operator acts on which carrier;
3. what fixes its parameter against the rescaling (HC2);
4. how a clock or length parameter is reconstructed;
5. why the action-to-phase comparison is \(\hbar\), if \(\hbar\) is claimed to be derived rather than calibrated;
6. how the resulting clock-energy generator becomes the Poincare mass Casimir; and
7. why the positive edge covers the complete Yang--Mills vacuum complement and survives continuum removal.

The sharpened category rule is

$$
\boxed{
\text{pregeometric spectrum}
\neq
\text{frequency}
\neq
\text{energy}
\neq
\text{mass},}
$$

with independently constructed comparison arrows required between each type.

Equivalently, the noncircular construction ladder is

$$
\boxed{
\text{primitive distinction exponent}
\xrightarrow{\text{clock solder}}
\text{frequency gap}
\xrightarrow{\text{action solder}}
\text{energy gap}
\xrightarrow{\text{Poincare realization}}
\text{mass gap}.}
$$

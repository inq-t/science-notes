# Regional Relative-Entropy Frames

A relative-entropy Hessian can act on Yang--Mills excitations only after a family of observable-access channels pulls state tangents back to the physical vacuum carrier. The global pure vacuum does not itself support a finite BKM Hessian in transverse directions, while faithful regional restrictions can. Their joint pullback is a dimensionless quadratic form whose positive lower-frame bound is exactly an infinitesimal informational-completeness condition. Local channels alone can miss phase, loop, or topological directions; nonlocal flux or boundary channels may be required to close that kernel. For arbitrary channels, a mass gap still needs a separate clock-energy comparison. For localized local-unitary state paths, however, a finite-width QFT theorem now supplies that comparison: the remaining hard gate is a uniform lower frame on a Hamiltonian form core.

**Status: [EXACT FINITE-DIMENSIONAL PULLBACK AND FRAME THEOREM; EXACT TWO-QUBIT BLIND-DIRECTION WITNESS; CONDITIONAL TYPE-III EXTENSION; EXACT LOCALIZED ENTROPY--ENERGY DEDUCTION; OPEN YANG--MILLS REALIZATION].** The finite statements below are elementary consequences of the BKM metric and finite-dimensional frame theory. They do not construct continuum Yang--Mills. The physical energy comparison is established only for the localized state-path specialization stated below.

## The global pure-vacuum Hessian is not the carrier

Let \(\mathcal H\) be a finite-dimensional physical Hilbert space with normalized vacuum \(\Omega\), and write

$$
P_0:=|\Omega\rangle\langle\Omega|.
$$

For \(\Psi\perp\Omega\), the normalized path

$$
\Omega_t
:=
\frac{\Omega+t\Psi}
{\sqrt{1+t^2\lVert\Psi\rVert^2}}
$$

has density tangent

$$
\dot P_0(\Psi)
=
|\Psi\rangle\langle\Omega|
+
|\Omega\rangle\langle\Psi|.
\tag{R1}
$$

For every \(t\neq0\), the one-dimensional supports of \(P_t\) and \(P_0\) differ. Hence

$$
D(P_t\Vert P_0)
=
D(P_0\Vert P_t)
=
+\infty.
\tag{R2}
$$

There is therefore no finite Umegaki/BKM coincidence Hessian at the rank-one global vacuum in a nontrivial projective direction. This is a carrier failure, not an ultraviolet divergence. [[library/relative-entropy-for-states-of-von-neumann-algebras-ii/inq|Araki's extension to nonfaithful states]] makes support part of the definition; it does not turn (R2) into a finite quadratic form.

One can avoid (R2) by choosing a faithful Gibbs state \(e^{-\beta H}/Z\), but that imports \(H\) into the reference state and is circular when the aim is to derive a lower bound on \(H\). An arbitrary full-rank admixture is noncanonical and its metric constants depend on the admixture. The faithful state must instead be constructed by the proposed observable presentation.

## Observable channels produce the correctly typed tangent maps

Use the projective tangent in the vacuum gauge

$$
\mathcal T_\Omega
:=
\{\Psi\in\mathcal H:\langle\Omega,\Psi\rangle=0\},
$$

regarded as a real Hilbert space. Let

$$
\mathcal R_\alpha:
\mathcal T_1(\mathcal H)
\longrightarrow
\mathcal T_1(\mathcal K_\alpha)
$$

be completely positive trace-preserving observable-access channels: regional restrictions, gauge-invariant readouts, boundary channels, or loop/flux measurements. Suppose

$$
\sigma_\alpha
:=
\mathcal R_\alpha(P_0)
>0
$$

on its declared output support. Differentiating the channel along (R1) gives the real-linear map

$$
\boxed{
J_\alpha\Psi
:=
\mathcal R_\alpha
\left(
|\Psi\rangle\langle\Omega|
+
|\Omega\rangle\langle\Psi|
\right).}
\tag{R3}
$$

Its output is a self-adjoint trace-zero tangent at \(\sigma_\alpha\). Define the Kubo--Mori operator

$$
\Omega_{\sigma_\alpha}(A)
:=
\int_0^1
\sigma_\alpha^sA\sigma_\alpha^{1-s}
\,\mathrm ds
$$

and the density-tangent BKM metric

$$
g^{\mathrm{BKM}}_{\sigma_\alpha}(X,Y)
:=
\operatorname{Tr}
\left[
X\,\Omega_{\sigma_\alpha}^{-1}(Y)
\right].
\tag{R4}
$$

Faithfulness makes (R4) finite and positive definite in finite dimensions. It is the coincidence Hessian of relative entropy and contracts under further stochastic coarse-graining. [[library/monotone-riemannian-metrics-and-relative-entropy/inq|Lesniewski--Ruskai]] supply the relative-modular and monotonicity framework; [[basic-concepts/hessians/symmetrized-relative-entropy-hessian|the Hessian note]] fixes the orientation and factor conventions used here.

The inverse in (R4) matters. The BKM pairing on self-adjoint observable or exponential-family perturbations is the dual form

$$
\langle A,B\rangle_{\sigma,\mathrm{BKM}}
:=
\operatorname{Tr}\!\left[A\,\Omega_\sigma(B)\right],
\tag{R4a}
$$

whereas (R4) acts on density tangents and contains \(\Omega_\sigma^{-1}\). These are Legendre-dual descriptions, not interchangeable formulas. Nor is monotonicity alone enough to select BKM from the Petz family of monotone quantum metrics; the present choice is licensed specifically by taking Umegaki relative entropy as the distinction functional.

For positive declared weights \(w_\alpha\), pull the metrics back to the physical projective tangent:

$$
\boxed{
\mathfrak d_{\mathcal R}[\Psi]
:=
\sum_\alpha
w_\alpha
g^{\mathrm{BKM}}_{\sigma_\alpha}
(J_\alpha\Psi,J_\alpha\Psi).}
\tag{R5}
$$

This answers the operator question exactly:

| Object | Operates on | Returns |
|---|---|---|
| \(\mathcal R_\alpha\) | global trace-class states | one accessible output state |
| \(J_\alpha=D\mathcal R_\alpha|_{P_0}\) | global projective vacuum tangents | output-state tangents |
| \(g^{\mathrm{BKM}}_{\sigma_\alpha}\) | two tangents at one faithful output state | a dimensionless inner product |
| \(\mathfrak d_{\mathcal R}\) | global projective vacuum tangents | total accessible distinction cost |
| \(H\) and \(\mathfrak h\) | the physical Hilbert carrier and form domain | clock evolution and energy cost |

The first four rows contain no energy unit.

## Finite-dimensional regional-frame theorem

Let the channel family be finite and let \(\mathcal T\subseteq\mathcal T_\Omega\) be a finite-dimensional real tangent sector. Then

$$
\boxed{
\ker\mathfrak d_{\mathcal R}|_{\mathcal T}
=
\bigcap_\alpha
\ker J_\alpha|_{\mathcal T}.}
\tag{R6}
$$

Indeed, every summand in (R5) is nonnegative and vanishes exactly when \(J_\alpha\Psi=0\). Compactness of the unit sphere then gives the equivalence

$$
\boxed{
\bigcap_\alpha\ker J_\alpha|_{\mathcal T}
=
\{0\}
\quad\Longleftrightarrow\quad
\exists\,\kappa_{\mathcal R}>0:
\mathfrak d_{\mathcal R}[\Psi]
\geq
\kappa_{\mathcal R}\lVert\Psi\rVert^2.}
\tag{R7}
$$

Thus the lower frame constant is the least singular value of the joint, BKM-weighted first-order observation map. It measures whether the entire declared tangent sector is visible somewhere in the atlas.

This equivalence is special to finite dimension. In an infinite-dimensional carrier, injectivity does not imply a positive lower bound: the joint observation map can have singular values tending to zero. The continuum target is closed range, or directly a uniform lower-frame estimate, not merely separation of every individual vector.

## Local marginals can miss a phase wall

The smallest witness already displays why loops or other nonlocal channels may matter. On two qubits define

$$
|\Phi_\pm\rangle
:=
\frac{|00\rangle\pm|11\rangle}{\sqrt2},
\qquad
\Omega:=|\Phi_+\rangle,
$$

and take the real tangent plane of the encoded two-branch carrier,

$$
\Psi(a,b)
:=
a|\Phi_-\rangle
+
b\,i|\Phi_-\rangle,
\qquad
a,b\in\mathbb R.
\tag{R8}
$$

The one-qubit restrictions both have faithful vacuum state \(I/2\). For the amplitude and relative-phase directions,

$$
\begin{array}{c|cc}
&|\Phi_-\rangle&i|\Phi_-\rangle\\
\hline
J_A&Z&0\\
J_B&Z&0
\end{array}
\tag{R9}
$$

because partial trace erases the off-diagonal global phase response. At \(\sigma=I/2\),

$$
\Omega_\sigma(Y)=\frac12Y,
\qquad
g^{\mathrm{BKM}}_\sigma(Z,Z)=4,
$$

so the two local channels give

$$
\mathfrak d_{\mathrm{loc}}[\Psi(a,b)]
=
8a^2.
\tag{R10}
$$

They distinguish changing branch weights but are blind to changing relative phase.

Now add the binary readout of

$$
O:=X\otimes Y,
\qquad
\Pi_\pm:=\frac{I\pm O}{2}.
$$

At the vacuum its two probabilities are \((1/2,1/2)\). The amplitude tangent leaves them stationary to first order, whereas the phase tangent has probability derivative \((-1,1)\), up to ordering of the two outcomes. Its classical Fisher/BKM cost is therefore

$$
\mathfrak d_O[\Psi(a,b)]
=
4b^2.
\tag{R11}
$$

The completed atlas obeys

$$
\boxed{
\mathfrak d_{\mathrm{atlas}}[\Psi(a,b)]
=
8a^2+4b^2
\geq
4(a^2+b^2)
=
4\lVert\Psi(a,b)\rVert^2.}
\tag{R12}
$$

[[contemporary-puzzles/yang-mills-mass-gap/receipts/regional_entropy_frame_receipt.py|The regional-frame receipt]] checks (R9)--(R12). The number \(4\) depends on the chosen channel weights and tangent normalization; it is a dimensionless frame constant, not a mass prediction.

The nonlocal Pauli readout is only a finite witness. In gauge theory its structural analogues are Wilson loops, 't Hooft operators, boundary charges, and other gauge-invariant channels that can distinguish holonomy or topological information invisible to a fixed family of local marginals. This does not prove that ordinary knots cause the Yang--Mills gap. It identifies a precise possible job for loop and knot data: remove the common kernel of a causal or regional distinction frame.

## The commutative ground-state transform is one exact member

At finite lattice regulator, suppose the positive vacuum wavefunction gives

$$
\mathrm d\nu
=
\psi_0^2\,\mathrm d\mu_{\mathrm{Haar}}.
$$

The multiplication algebra \(L^\infty(X,\nu)\) has the faithful state \(f\mapsto\int f\,\mathrm d\nu\), even though the original vector vacuum is pure on \(B(L^2)\). For a centered real score \(f\) and probability path

$$
\mathrm d\nu_t
=
(1+tf)\,\mathrm d\nu,
$$

one has

$$
\left.
\frac{\mathrm d^2}{\mathrm dt^2}
D(\nu_t\Vert\nu)
\right|_{t=0}
=
\int f^2\,\mathrm d\nu.
\tag{R13}
$$

If \(\mathcal R_\alpha\) is restriction to a sub-\(\sigma\)-algebra \(\mathcal G_\alpha\), the output score is the conditional expectation

$$
J_\alpha f
=
\mathbb E_\nu[f\mid\mathcal G_\alpha],
$$

and its relative-entropy Hessian is

$$
\left\|
\mathbb E_\nu[f\mid\mathcal G_\alpha]
\right\|_{L^2(\nu)}^2.
\tag{R14}
$$

Thus a classical regional entropy frame is literally a continuous-frame operator assembled from conditional-expectation projections. [[gauge-descent-flux-fisher-coercivity]] identifies (R13) with the real-amplitude denominator of the regulated mass-gap Rayleigh quotient. It also proves the limitation exposed by (R9): the multiplication carrier cannot see pure phase directions.

The reflection-positive boundary construction supplies a useful contrast. Under its reflection-Markov, reflection-fixed-separator, and dense-insertion hypotheses, [[vacuum-boundary-gluing-and-wall-response#The OS quotient factors exactly through a reflection interface|the OS interface map]] \(B_\rho^{\mathrm{OS}}:\mathcal H_{\mathrm{OS}}\to L^2(\nu_{\rho,I})^{\mathrm{GI}}\) is a complex-linear unitary after quotient completion, so it retains every phase direction present in the reconstructed interface carrier. A closable interface derivative composed with it is therefore phase-sensitive, but is complete on the reference complement only if its kernel is proved to be exactly \(\mathbb C1\). Any later interface-to-log-scale map \(S_\rho\), including any thick-interface-to-slice leg, must preserve the required directions or declare and repair its kernel. A real state-density Hessian cannot substitute for this complex carrier map merely because both use the same probability measure.

## Type III locality repairs faithfulness, not completeness or energy

In continuum AQFT the global vacuum is pure, but under the usual Reeh--Schlieder hypotheses its restriction to a local von Neumann algebra is represented by a cyclic-separating vector and is faithful normal. Araki relative entropy can therefore replace matrix relative entropy without introducing a thermal mixture. For a declared differentiable perturbation class, one may seek regional maps

$$
J_{\mathcal O}:
\mathcal T_\Omega
\longrightarrow
T_{\omega_{\mathcal O}}
\mathcal S(\mathfrak A(\mathcal O))
$$

and a renormalized or finite pullback

$$
\mathfrak d_{\mathrm{mod}}[\Psi]
:=
\int_{\mathfrak R}
g^{\mathrm{Araki}}_{\omega_{\mathcal O}}
(J_{\mathcal O}\Psi,J_{\mathcal O}\Psi)
\,\mathrm d\mu(\mathcal O).
\tag{R15}
$$

Every symbol in (R15) is an obligation: the region site \(\mathfrak R\), measure and normalization, perturbation class, common domain, relative-entropy differentiability, measurability, closability, and treatment of gauge centers or edge data. A collection of local restrictions may still possess globally or topologically invisible tangents. Reeh--Schlieder cyclicity does not itself give the uniform lower frame bound, and the impossibility of a proper vacuum-preserving conditional-expectation tower between ordinary nested local algebras remains untouched.

The Connes cocycle can compare faithful state presentations on one algebra.
Once such a family is supplied, [[modular-cocycle-tomography/inq|the modular
tomography theorem]] computes its exact common local-unitary kernel as the
intersection of its centralizers, or equivalently as one reference
centralizer intersected with the commutant of all relative cocycles. A
type-III\(_1\) factor with separable predual even admits faithful states with scalar
centralizer. This sharpens the injectivity question, but it neither selects
the physical family \(J_{\mathcal O}\), makes (R15) coercive, nor turns a
modular generator into the physical Hamiltonian.
[[wall-construction-interface/half-sided-modular-tunnel]] gives a
particularly sharp warning: its invariant reference state has zero
horizontal BKM response, and a nonzero response requires an independent
state path.

## Entropic geometry becomes a gap only through a second inequality

Let the Yang--Mills Hamiltonian form be

$$
\mathfrak h_{\mathrm{YM}}[\Psi]
:=
\lVert H_{\mathrm{YM}}^{1/2}\Psi\rVert^2.
$$

The completed entropy-frame route requires, on one common form domain,

$$
\mathfrak d_{\mathcal R}[\Psi]
\geq
\kappa_{\mathcal R}
\lVert(1-P_0)\Psi\rVert^2,
\qquad
\mathfrak h_{\mathrm{YM}}[\Psi]
\geq
\eta_{\mathrm{sol}}E_*
\mathfrak d_{\mathcal R}[\Psi].
\tag{R16}
$$

Only their composition gives

$$
\boxed{
H_{\mathrm{YM}}
\geq
\eta_{\mathrm{sol}}
\kappa_{\mathcal R}
E_*
(1-P_0)}
\tag{R17}
$$

in quadratic-form sense. Equation (R7) addresses the first inequality at finite regulator. It does no work on the second for an arbitrary channel family.

There is now one important carrier-correct specialization. For a wedge-dual positive-energy translation-covariant QFT, a state localized in a region of width \(2R\) obeys Longo's bound

$$
S_B(\varphi\Vert\omega)
\leq
\frac{2\pi R}{\hbar c}\langle H\rangle_\varphi.
$$

Along a twice differentiable local-unitary path \(\varphi_s\) through the vacuum, define both entropy forms with the half-Hessian convention. Then [[localized-relative-entropy-and-the-energy-solder]] proves

$$
0\leq
q_{B\to\mathcal N}^{\mathrm{loss}}
\leq
q_B
\leq
\frac{2\pi R}{\hbar c}\mathfrak h_{\mathrm{YM}}.
\tag{R17a}
$$

Consequently, if the loss frame itself satisfies

$$
q_{B\to\mathcal N}^{\mathrm{loss}}[\Psi]
\geq
\kappa_B\|(1-P_0)\Psi\|^2
\tag{R17b}
$$

on a complexified Hamiltonian form core, then

$$
\Delta_E
\geq
\frac{\hbar c}{2\pi R}\kappa_B.
\tag{R17c}
$$

This does not follow for an arbitrary family \(\mathcal R_\alpha\), and Reeh--Schlieder norm density does not supply the required form-core property. But it replaces the formerly free solder in (R16) by an established locality-and-positive-energy theorem on the declared localized carrier.

Quantum Markov-semigroup theory can relate entropy convexity, Dirichlet forms, logarithmic-Sobolev inequalities, and spectral gaps for an independently specified dissipative generator. [[library/gradient-flow-and-entropy-inequalities-for-quantum-markov-semigroups-with-detailed-balance/inq|Carlen--Maas]] provide a finite-dimensional detailed-balance construction. Its generator acts on an open-system or relaxation algebra; it is not the Lorentzian Yang--Mills Hamiltonian. To use it here one must prove either a ground-state-transform/OS identification with the physical Euclidean Hamiltonian form or the explicit domination in (R16). Calling Markov time “causal time” does not supply that theorem.

There is an exact rate-rescaling obstruction to asking bare entropy geometry for the missing energy scale. Fix a faithful \(\sigma\), and on observables put

$$
E_\sigma(A):=\operatorname{Tr}(\sigma A)\mathbf 1,
\qquad
\mathcal L_\varepsilon
:=
\varepsilon(E_\sigma-\operatorname{id}),
\qquad \varepsilon>0.
\tag{R18}
$$

All members have the same invariant state, relative entropy, and BKM tangent metric, but their nonzero relaxation rate is \(\varepsilon\). Hence

$$
\inf_{\varepsilon>0}\operatorname{gap}(-\mathcal L_\varepsilon)=0
\tag{R19}
$$

while the entire state-space distinction geometry is unchanged. Equivalently, rescaling a Dirichlet derivation \(\partial\mapsto\sqrt\varepsilon\,\partial\) rescales \(\partial^*\partial\) without changing BKM geometry. Entropy can provide the denominator and sometimes a coercivity theorem for a *specified and normalized* generator; it cannot select the generator's clock rate. [[library/exponential-relative-entropy-decay-along-quantum-markov-semigroups/inq|Wirth's von Neumann-algebra result]] extends the entropy-decay/modified-logarithmic-Sobolev equivalence and an intertwining route to general von Neumann algebras, but it remains a theorem about a supplied quantum Markov semigroup.

Modular theory sharpens the same boundary from the other side. A Connes Radon--Nikodym cocycle \([D\varphi:D\psi]_t\) generally obeys a *twisted* cocycle law relative to \(\sigma_t^\psi\), not the group law of a unitary representation of \(\mathbb R\); Stone's theorem therefore supplies no canonical “relative Hamiltonian” in general. Even in the exceptional commuting-state case, Pedersen--Takesaki theory gives \([D\varphi:D\psi]_t=h^{it}\) with \(\psi(h)=1\). If \(\log h\) has either sign, normalization forces \(h=1\) and \(\varphi=\psi\). Thus a nontrivial relative modular logarithm between faithful normalized states cannot be a positive energy by this route. For a type-\(\mathrm{III}_1\) factor, the modular logarithm has spectrum \(\mathbb R\), which is a still stronger warning against reading it as a positive physical Hamiltonian.

A half-sided modular inclusion adds enough ordered-inclusion data to reconstruct a positive translation generator, but exact modular dilation covariance forces every nonzero such generator to have spectrum \([0,\infty)\). The promising reversal is consequently not to call one modular logarithm mass. It is to reconstruct several gapless translation directions and seek mass only in their joint Poincare invariant. In \(1+1\) notation and natural units, for example, positive null generators may each be gapless while a massive irreducible sector obeys

$$
P_+P_-=m^2\mathbf 1
\tag{R20}
$$

up to the chosen light-cone normalization. This is a theorem-shaped bridge target, not a result: one must reconstruct a common Poincare representation, show that the joint spectrum avoids the nonvacuum light cone and arbitrarily small timelike hyperboloids, and compare that Casimir with the Yang--Mills carrier. [[wall-construction-interface/half-sided-modular-tunnel|The half-sided modular tunnel]] supplies orientation and transport but is response-null in its invariant state.

## Continuum stopping condition

For regulators \(r=(a,L)\), a genuine construction must provide:

1. gauge-invariant carriers \((\mathcal H_r,\Omega_r)\) and channels \(\mathcal R_{r,\alpha}\) defined without nonvacuum spectral data;
2. faithful output states, or controlled Araki-relative-entropy forms, with fixed channel weights and normalization;
3. a regional-plus-flux family whose pulled-back form is closable and obeys \(\mathfrak d_r\geq\kappa_r(1-P_{0,r})\) with \(\liminf_r\kappa_r>0\);
4. an independently proved, physical-unit comparison \(\mathfrak h_r\geq\eta_rE_{*,r}\mathfrak d_r\) with positive limiting product;
5. explicit identifications of the varying carriers, generalized Mosco convergence of both forms, and generalized-strong convergence of the vacuum projections;
6. recovery of the \(G\)-free local Yang--Mills net, Poincare action, spectrum condition, gauge identities, nontriviality, and unique vacuum.

The Copernican contribution is therefore narrower and stronger than “entropy creates mass.” Observable locality becomes an atlas of information channels rather than a primitive container; global flux or topology may be required for that atlas to distinguish every physical direction; and mass is attached only after the reconstructed clock form charges the complete atlas. The decisive unknown is now a pair of uniform form estimates with explicit carriers, not an unexplained particle mass term.

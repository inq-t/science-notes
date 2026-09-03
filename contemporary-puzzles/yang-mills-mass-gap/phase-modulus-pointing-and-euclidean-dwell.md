# Phase, Modulus, Pointing, and Euclidean Dwell

The polar decomposition of the separated past--future transfer identifies three structures that must not be collapsed into one: its partial isometry carries directed presentation and possible phase data, its positive modulus carries attenuation and hence the transfer-generator gap, and an obtained character or stable record supplies factual pointing. On the vacuum complement, a positive clock-energy gap is exactly equivalent to a finite uniform ceiling on integrated Euclidean transfer persistence. This becomes a relativistic mass-gap statement only after Poincare reconstruction and Casimir identification; it makes the gap an inverse dwell scale without making spacetime discrete, turning a Born weight into an outcome, or claiming that the imaginary unit causes mass.

**Status: [EXACT] for the spectral-support, polar-decomposition, complexification-angle, and Euclidean-dwell theorems; [EXACT UNDER THE STATED READOUT] for the alternatives/weighting/pointing type ledger; [IDENTIFICATION] for calling transfer persistence ambiguity or dwell; [OPEN CONSTRUCTION] for deriving the modulus bound, phase data, actuality rule, and Poincare realization from one pre-QFT Yang--Mills construction.**

## Alternatives, weights, points, and gaps

Let \(H\geq0\) be self-adjoint on a Hilbert space \(\mathcal H\), let

$$
P_0:=E_H(\{0\}),
\qquad
\mathcal K:=(1-P_0)\mathcal H,
\tag{PMP1}
$$

and let \(\mathcal D\subseteq B(\mathcal H)\) be a declared unital commutative \(C^*\)-readout algebra. Four objects then have different types:

1. the spectral projections \(E_H(B)\) are available energy propositions;
2. a vector \(\psi\) supplies the Born spectral measure \(\mu_\psi(B)=\langle\psi,E_H(B)\psi\rangle\);
3. an obtained character \(\chi_x\) of \(\mathcal D\), together with a stable record, supplies a fact; and
4. a gap is the state-independent support exclusion

$$
E_H((0,\Delta))=0.
\tag{PMP2}
$$

Restriction of a state to \(\mathcal D\cong C(X)\) gives a probability measure on \(X\), not one selected \(x\). An instrument can give the conditional state for each result without choosing which result is obtained. This contextual fact need not be an energy fact: that requires a bounded or coarse-grained spectral readout in which the relevant \(E_H(B)\) belongs to \(\mathcal D\). These are the type distinctions in [[sufficient-reason/facticity-and-pointing]] and [[physical-distinction-coercivity]].

The rigorous core of “distinction requires ambiguity” is correspondingly modest. A nontrivial informational distinction requires a possibility space with at least two alternatives. In the binary case, a nontrivial projection \(e\in\mathcal D\) brings its contrary \(1-e\), and

$$
\omega\longmapsto(\omega(e),1-\omega(e)),
\qquad
\chi_x(e)\in\{0,1\}.
\tag{PMP3}
$$

The obtained fact need not itself have positive entropy: a character can be definite while the ambient algebra still contains alternatives. Conversely, \(\mathcal D\cong\mathbb C\) has a unique character but no nontrivial informational distinction. The spectrum \(X\) is the possibility structure; probabilistic ambiguity belongs to a non-Dirac weighting on \(X\); pointing belongs to a realized value.

The vacuum projection in (PMP1) is a distinguished common subspace. Only under vacuum uniqueness, \(P_0=|\Omega\rangle\langle\Omega|\), does it determine one vacuum ray; it is still not an obtained character. Pointing alone cannot imply coercivity: one can have \(\ker H=\mathbb C\Omega\) while \(\sigma(H|_{\mathcal K})\) accumulates at zero. [[pointing-coercivity-and-the-flat-partner-law]] gives an explicit normalizable-pointing counterexample. The gap is not the zero-mode subspace; it is the uniform exclusion, or equivalently the uniform decay rate, on its orthogonal complement.

A pointedness firewall is therefore necessary. A pointed cone obeying \(C\cap(-C)=\{0\}\), a categorical pointed object \((X,x_0)\), a character \(\chi_x\), a vacuum projection \(P_0\), and an obtained fact with a persistent record are five different structures. Each can be useful, but no one of them supplies the other four without explicit maps and additional hypotheses. [[pointed-facts-and-the-shorted-response]] separately distinguishes the visible counterfactual complement of a point from its hidden whole-register antecedent fibre.

## Mass is not a canonical phase-space coordinate

After positive-energy Poincare reconstruction, the mass-squared operator is the joint invariant

$$
M^2=\frac{H^2-c^2\mathbf P^2}{c^4}.
\tag{PMP4}
$$

On an irreducible massive sector it is a scalar label, while momentum varies along the corresponding orbit. There is no universal canonical coordinate \(Q_M\) with \([Q_M,M]=i\hbar\). This is the valid content of saying that mass is not another phase-space coordinate. It does **not** mean that every state has sharp mass: reducible representations can have mass distributions, and unstable resonances have spectral widths. Nor can fixed mass inside a sector be used circularly to prove that the vacuum representation has a mass gap. [[mass-as-casimir-and-realization]] owns the full distinction.

Thus the Heisenberg relations and the mass-gap statement ask different questions. The former concern noncommuting observables on an already supplied carrier. The latter asks whether the reconstructed joint spectrum contains any nonvacuum sector arbitrarily close to the vacuum.

## What \(i\) supplies

On a real Hilbert space \(\mathcal H_{\mathbb R}\), a compatible complex structure is an orthogonal operator

$$
J^2=-I,
\qquad
J^*=-J,
\tag{PMP5}
$$

with \(a+ib\) represented by \(aI+bJ\). It supplies a quarter-turn and the phase rotations \(e^{\theta J}\). Let \(H\) be real self-adjoint and assume \(J\operatorname{Dom}H=\operatorname{Dom}H\) with \(HJ=JH\), equivalently that \(J\) commutes with the spectral resolution of \(H\). Then \(JH\) is skew-adjoint and the same generator has the two presentations

$$
C_s=e^{-sH/\hbar},
\qquad
U_t=e^{-tJH/\hbar}.
\tag{PMP6}
$$

The first is positive Euclidean attenuation; the second is reversible unitary clock evolution. Identifying them by analytic continuation requires the Osterwalder--Schrader hypotheses or another reconstruction theorem. The symbol \(i\) does not perform that reconstruction.

There is also a short no-go. If \(M,N\subseteq\mathcal H_{\mathbb R}\) are closed real subspaces, their complexifications have projections \((P_M)_{\mathbb C}\) and \((P_N)_{\mathbb C}\), so

$$
c_F(M_{\mathbb C},N_{\mathbb C})
=
c_F(M,N).
\tag{PMP7}
$$

Adjoining \(i\) cannot open a Friedrichs-angle gap. In [[hessian-response-geometry/tangent-bundle-complexification]], the exact formula \(J(X,Y)=(-Y,X)\) on the tangent bundle of a flat Hessian manifold gives a useful geometric meaning to \(i\): it exchanges horizontal/base and vertical/fiber variations. But it complexifies an already chosen real Hessian carrier and supplies neither its physical state nor its energy.

An integrable complex structure is likewise not a phase space. A phase space needs a closed nondegenerate two-form and usually a polarization before quantization; [[complex-presentation-without-polarization/inq]] and [[polarization-and-positive-state-geometry]] keep these obligations separate. In particular, complex structure by itself supplies no Hilbert norm, Born rule, Hamiltonian, or factual point.

## Polar decomposition separates orientation from magnitude

For the disjoint-cut construction in [[past-future-angle-and-the-transfer-gap]], write \(J_-^0,J_+^0:\mathcal K\to\mathscr H\) for the centered past and future endpoint isometries. The reduced ordered transfer has polar decomposition

$$
A_\ell=pq=V_\ell|A_\ell|,
\qquad
|A_\ell|
=J_+^0e^{-\ell H/(\hbar c)}(J_+^0)^*,
\qquad
V_\ell=J_-^0(J_+^0)^*.
\tag{PMP8}
$$

The partial isometry \(V_\ell\) identifies the ordered endpoint presentations. It is the slot in which orientation, holonomy, or a projective cocycle could live. The modulus acts on the future endpoint and contains the singular-value attenuation. Reversing the arrow replaces it by \(|A_\ell^*|\) on the past endpoint; the two positive operators have the same nonzero spectrum and are canonically intertwined by \(V_\ell\). Thus the singular-value magnitude, rather than either endpoint operator taken in isolation, is reversal-even. For any unitary \(U\),

$$
(UA_\ell)^*(UA_\ell)=A_\ell^*A_\ell,
\qquad
\|UA_\ell\|=\|A_\ell\|.
\tag{PMP9}
$$

A flat phase decoration therefore cannot create a positive-modulus or transfer-generator gap. Multiple-path interference can change a modulus only after a specific coherent sum of transfer amplitudes has been constructed; a bare \(U(1)\) label does not do so.

The same parity split appears directly in the two projections. Restrict them to the reduced carrier \(\mathscr H_0=\overline{\operatorname{Ran}p+\operatorname{Ran}q}\) and write \(I_0\) for its identity. If a conjugation \(K\) commutes with \(p\) and \(q\), then

$$
K(2I_0-p-q)K=2I_0-p-q,
\qquad
K\!\left(\frac{[p,q]}{2i}\right)\!K
=-\frac{[p,q]}{2i}.
\tag{PMP10}
$$

The positive distinction floor is conjugation-even; the ordered commutator is conjugation-odd. This makes primitive chirality compatible with an observed positive energy without deriving one from the other.

Two exponentials should also not be called the same residue. Slab concatenation gives the nonnegative real character

$$
R(\ell):=-\log c_F(\ell)
=\frac{\ell\Delta_E}{\hbar c},
\qquad
R(\ell_1+\ell_2)=R(\ell_1)+R(\ell_2),
\tag{PMP11}
$$

whereas Lorentzian clock evolution gives the unitary phase \(e^{-itH/\hbar}\). With endpoint labels aligned, a nontrivial projective law would have the form

$$
V_{ij}V_{jk}
=\omega_{ijk}V_{ik},
\qquad i<j<k,
\tag{PMP12}
$$

Such a law would require an actual cocycle and representation. The stationary Markov witness has trivial cocycle. The raw braid-center exploration in inbox/supplying-complex-numbers/the-necessity-of-i.md identifies a possible phase slot, but neither a canonical character nor its normalization; its complex-number pincer is conditional, not a derivation of physical \(i\). More generally, effective descent may erase distinctions without selecting an outcome or producing time. A “residue cost” becomes mathematics only after it is typed as an obstruction class, monodromy, kernel or cokernel, entropy defect, record increment, or positive transfer modulus.

## Positive return and Born form

The polar-factor-free positive return on the chosen future endpoint associated with (PMP8) is

$$
E_\ell:=A_\ell^*A_\ell
=J_+^0e^{-2\ell H/(\hbar c)}(J_+^0)^*.
\tag{PMP13}
$$

It is a positive contraction on its supported endpoint carrier. For a normalized endpoint vector \(\phi\in\mathcal K\), put \(\psi=J_+^0\phi\). Then

$$
b_\phi(\ell)
:=\langle\psi,E_\ell\psi\rangle
=\left\|e^{-\ell H/(\hbar c)}\phi\right\|^2
=\int_{(0,\infty)}e^{-2\ell E/(\hbar c)}\,\mathrm d\mu_\phi(E).
\tag{PMP14}
$$

This is a Born-form weight and a Laplace transform of the energy spectral measure. Writing \(I_+=s(E_\ell)\) for the supported carrier's identity, declaration of the two-effect POVM \(\{E_\ell,I_+-E_\ell\}\) already makes it the probability of one branch. An instrument, for example one with \(A_\ell\) as a Kraus operator, is additionally needed for posterior maps and a record. The positive return alone supplies no physically selected POVM or instrument, obtained value, or record. It measures persistence of a supplied distinction through the slab, not “collapse.”

## The Euclidean-dwell theorem

Put \(H_{\mathcal K}:=H|_{\mathcal K}\). On \(\mathcal K\), define the extended positive quadratic form

$$
\mathfrak d_{\mathrm{E}}[\psi]
:=
\int_0^\infty
\left\|e^{-\ell H/(\hbar c)}\psi\right\|^2\,\mathrm d\ell.
\tag{PMP15}
$$

Tonelli's theorem and spectral calculus give

$$
\boxed{
\mathfrak d_{\mathrm{E}}[\psi]
=
\frac{\hbar c}{2}
\int_{(0,\infty)}\frac{1}{E}\,\mathrm d\mu_\psi(E).}
\tag{PMP16}
$$

Equivalently, spectral calculus defines the possibly unbounded positive dwell operator

$$
\mathcal D_{\mathrm E}
:=
\frac{\hbar c}{2}H_{\mathcal K}^{-1},
\qquad
\operatorname{Dom}\mathcal D_{\mathrm E}^{1/2}
=\operatorname{Dom}H_{\mathcal K}^{-1/2}.
\tag{PMP17}
$$

The improper semigroup integral in (PMP15) converges to its quadratic form monotonically and may take the value \(+\infty\). The operator is bounded exactly when \(H_{\mathcal K}\) has a positive lower bound. Consequently, for every \(\Delta>0\),

$$
\boxed{
H_{\mathcal K}\geq\Delta I
\quad\Longleftrightarrow\quad
\mathcal D_{\mathrm E}
\leq
\frac{\hbar c}{2\Delta}I.}
\tag{PMP18}
$$

Assume \(\mathcal K\neq\{0\}\). If \(\Delta_E=\inf\sigma(H_{\mathcal K})>0\) is the optimal gap, then

$$
\boxed{
\|\mathcal D_{\mathrm E}\|
=\frac{\hbar c}{2\Delta_E},
\qquad
\Delta_E
=\frac{\hbar c}{2\|\mathcal D_{\mathrm E}\|}.}
\tag{PMP19}
$$

If the Euclidean parameter is a duration \(\tau\), replace \(\ell/c\) by \(\tau\) and \(\hbar c\) by \(\hbar\). The theorem gives an exact sense in which a clock-energy gap is a time or length gap: it is the reciprocal of the supremal, or worst-case, integrated Euclidean persistence over normalized nonvacuum directions. It does **not** give a smallest spatial interval, a duration between facts, or a grain of observation. A gapless theory can have finite dwell for particular states while lacking a uniform ceiling over the whole vacuum complement. Only after the Poincare reconstruction and Casimir identification may this clock-energy statement be called a relativistic mass gap.

[[mass-as-a-calibrated-distinction-rate]] gives the differential companion: the same gap is \(\hbar c\) times the logarithmic attenuation per Euclidean length, or \(\hbar\) times the attenuation per Euclidean duration. It also states the additional carrier and record obligations required before that exact attenuation rate may be interpreted as a rate of factification.

Under the stationary reversible Hilbert-positive Markov--OS and endpoint-identification hypotheses of [[past-future-angle-and-the-transfer-gap]], combine this with the exact angle identity

$$
c_F(\ell)
=\left\|e^{-\ell H/(\hbar c)}(1-P_0)\right\|
=e^{-\ell\Delta_E/(\hbar c)},
\tag{PMP20}
$$

the gap is the uniform logarithmic attenuation, or persistence-decay, rate of all centered distinctions. The finite-depth endpoint semigroup is injective and does not forget by identifying two endpoint inputs; the ambient projection product still kills directions outside its support. This statement concerns an operator norm over every direction in the endpoint vacuum complement, not one correlation channel or one selected glueball state.

## What the box and Jordan clues do and do not supply

[[inbox/the-box-spectrum-functor/the-box-spectrum-functor]] contains a useful semiclassical analogy, but its advertised identity between Born density and conformal dwell needs a measure choice. For the displayed ordering \(-\hbar^2(2a)^{-1}\partial_a^2\), the formally symmetric measure is \(a\,\mathrm da\), not \(\mathrm da\). The WKB envelope \(|\psi|^2\propto1/p\) then gives

$$
a|\psi(a)|^2\,\mathrm da
\propto
\frac{a}{p}\,\mathrm da,
\tag{PMP21}
$$

which is the declared proper/dust-clock dwell rather than \(\mathrm d\eta=\mathrm da/p\). More generally, for a self-adjoint ordering with the same principal symbol \(p^2/(2a)\), fixed-flux WKB gives \(w(a)|\psi(a)|^2\,\mathrm da\propto a\,\mathrm da/p\) in the Hilbert measure \(w(a)\,\mathrm da\). Obtaining conformal dwell requires changing the lapse, hence the clock Hamiltonian being quantized; factor ordering alone cannot do it. A self-adjoint-domain and current theorem would still be needed. The numerical standing-wave receipt checks a WKB envelope, not a probability current, normalized resonance, or Born rule. Equation (PMP16) is a spectral-calculus identity for whichever positive self-adjoint \(H\) has actually been constructed; its numerical content depends on that \(H\).

The Jordan material supplies exact finite witnesses of invariant spectrum versus ambiguous presentation. In \(\mathfrak h_3(\mathbb O)\), the orbit of an ordered Jordan frame—or of an element with one fixed simple spectrum—is \(F_4/\mathrm{Spin}(8)\), not a torsor, phase space, or groupoid. The eigenvalue-discriminant wall and determinant/rank wall are distinct: \(\operatorname{diag}(1,1,2)\) has repeated spectrum and full rank, while \(\operatorname{diag}(1,2,0)\) has simple spectrum and deficient rank. [[inbox/black-holes-as-jordan-spectra/black-holes-as-jordan-spectra]] therefore models distinctions forgotten by a spectral quotient but supplies neither a degeneration process nor a positive transfer gap. Its black-hole dictionary remains model-dependent. Moreover, the compact real form used here and the split-octonionic/noncompact real forms used in important black-hole charge models cannot be merged without an explicit real-form bridge.

There is nevertheless an exact Copernican precedent. The nested selection

$$
X\cong\mathfrak h_2(\mathbb C)
\subset
B\cong\mathfrak h_3(\mathbb C)
\subset
\mathfrak h_3(\mathbb O)
\tag{PMP22}
$$

obeys

$$
\operatorname{Stab}_{F_4}(X)
\cap
\operatorname{Stab}_{F_4}(B)_0
\cong
S(U(2)\times U(3))
\cong
\frac{U(1)\times SU(2)\times SU(3)}{\mathbb Z_6}
\tag{PMP22a}
$$

for \(X\cong\mathfrak h_2(\mathbb C)\subset B\cong\mathfrak h_3(\mathbb C)\), in the theorem recorded by [[library/standard-model-from-exceptional-jordan-algebra/inq]]. This identity-component-restricted stabilizer intersection is not the full flag stabilizer, which has an additional antiunitary component. Here the familiar symmetry is the symmetry of a selected complex presentation, not primitive input. This is evidence for the order of explanation, not a Yang--Mills carrier, Hamiltonian, or gap theorem.

## The sharpened construction target

The current chain is now exact through its middle:

$$
\begin{gathered}
\text{ordered disjoint cuts}
\longrightarrow
A_\ell=V_\ell|A_\ell|,\\
\text{directed presentation}\quad\ \text{positive attenuation},\\
|A_\ell|
\longrightarrow
E_\ell=A_\ell^*A_\ell
\longrightarrow
\mathcal D_{\mathrm E}
\longleftrightarrow
\text{spectral gap}.
\end{gathered}
\tag{PMP23}
$$

The hard noncircular step is still on the left of the positive modulus: construct the disjoint-cut carrier and prove a fixed-thickness contraction, or its calibrated infinitesimal rate, from gauge geometry, entropy contraction, a wall obstruction, or a complete regional frame **without** reading the desired spectrum from \(H\). Then identify its modulus with the OS transfer semigroup, reconstruct the local Poincare theory, and solder the clock gap to the mass Casimir. Phase, knot, monodromy, Jordan-frame, or octonionic data contribute only if they control that all-direction modulus or construct one of those missing maps.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/past_future_angle_receipt.py|The finite past--future receipt]] also checks (PMP19) for its three-state transfer generator. This is a spectral-calculus identity check, not an independent gap proof.

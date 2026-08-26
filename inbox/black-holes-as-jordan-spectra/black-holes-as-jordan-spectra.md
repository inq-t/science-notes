# Black Holes as Jordan Spectra

The proposed thought — black holes are particles, hidden by uncertainty; wave harmonics form them inside the boxed wedge of an observable cosmos; the phase space of spacetime is octonionic; black holes are its resonance packets; the horizon's two-dimensional area is a shadow of the underlying ontology — decomposes under typing into a set of exact statements, one candidate bridge that meets the vault's own published bridge test, two firewalls that stay up, and clearly marked open constructions. The load-bearing exact finding: the spectral theory of the exceptional Jordan algebra $\mathfrak h_3(\mathbb O)$ maps onto exactly the $A_2$ discriminant base owned by [[algebra/a2-inverse-cover|the $A_2$ inverse cover]], with the coincident-eigenvalue locus landing on $4p^3+27q^2=0$ and eigenvalue monodromy $W(A_2)=S_3$ — the "resonance locus" of the thought is the Keller cusp, functionally rather than numerologically. Receipts: `bh_jordan_receipts.py` (numpy; 32 checks; PASS/FAIL per claim; nonzero exit on failure).

## 1. The thought, typed

| Fragment of the thought | Typed form | Status |
|---|---|---|
| black holes are particles | no-hair triple $(M,J,Q)$; rank-degenerate charge orbits are the perturbative-state stratum; Kerr–Newman $g=2$ | [CITED]; [EXACT] for $g=2$ |
| hidden by Heisenberg uncertainty | $r_s<\lambda_C$ below $M_*=\sqrt{\hbar c/2G}$; categorically: $\mathfrak h_3(\mathbb O)$ has no Hilbert-space wave representation | [EXACT] both |
| wave harmonics form the particle | Jordan spectral theorem $X=\sum_i\lambda_ie_i$; the three eigenvalues are the harmonics | [EXACT] in the model |
| trapped in a Wheeler box / wedge, limited DOF | wedge algebras are type III$_1$: no minimal projections, no localized number operator | [STANDARD], decoration here |
| octonionic phase space | Freudenthal triple system $\mathfrak M(\mathfrak h_3(\mathbb O))$: 56-dimensional, symplectic, quartic invariant, $E_7$-type duality | [EXACT] object; [CITED] physics role |
| resonance packets | coincident-eigenvalue locus = the $A_2$ cusp $4p^3+27q^2=0$ | [EXACT], receipt |
| horizon area = 2d shadow of the ontology | attractor mechanism: area is the duality-invariant of the charge orbit, moduli forgotten | [CITED]; typed below |

The physical identification of black-hole observables with $\mathfrak h_3(\mathbb O)$ is a **[MODEL CONJECTURE]** of this note. Everything below separates what is exact inside that model from what the model would still owe physics.

## 2. The no-wave theorem

The Jordan–von Neumann–Wigner classification of finite-dimensional formally real Jordan algebras leaves exactly one member that is not the self-adjoint part of an associative operator algebra: $\mathfrak h_3(\mathbb O)$, the $3\times3$ Hermitian octonionic matrices (Albert's theorem). It therefore admits **no representation by operators on any complex Hilbert space**: no wavefunction, no Schrödinger presentation, categorically rather than practically. Its state space is the Moufang plane $\mathbb{OP}^2=F_4/\mathrm{Spin}(9)$, and [[library/standard-model-from-exceptional-jordan-algebra/entry|Baez and Schwahn]] already read it as the observable algebra of an "octonionic qutrit." The thought's *we can't see them because of uncertainty* thus has two typed versions, both exact:

- **Arithmetic.** $r_s=2GM/c^2$ falls below $\lambda_C=\hbar/Mc$ for $M<M_*=\sqrt{\hbar c/2G}\approx1.54\times10^{-8}\,$kg. A sub-Planckian black hole sits inside its own position uncertainty; for the electron the burial depth is $r_s/\lambda_C=2(m/M_P)^2\approx3.5\times10^{-45}$. Receipts: `Heisenberg regime`, `electron`.
- **Categorical.** If the observable triple of a black hole is modeled in $\mathfrak h_3(\mathbb O)$, there is *no wave presentation to see* — invisibility as a representation-theoretic fact, not an instrument limit.

The Kerr–Newman electron sharpens the particle direction: with the electron's $(M,J,Q)$ the solution is super-extremal ($a\approx1.93\times10^{-13}\,$m against $GM/c^2\approx6.8\times10^{-58}\,$m — naked by 44 orders), and its gyromagnetic ratio is exactly $g=2$, from $\mu=Qa$ and $J=Ma$ alone. Receipt: `Kerr-Newman: g = 2`. [CITED — Carter 1968.]

One wedge sentence, typed and then set aside: a wedge or horizon-complement algebra in QFT is type III$_1$, which has no minimal projections and hence no localized particle-number observable — "limited degrees of freedom in the box" is real, but its owner is [[wall-construction-interface/entry|the wall-construction interface]], not this note.

## 3. The harmonics and the $A_2$ cusp

$\mathfrak h_3(\mathbb O)$ has an exact spectral theorem. Every element satisfies its characteristic cubic

$$
\lambda^3-T(X)\lambda^2+S(X)\lambda-N(X)=0,
\qquad
T=\operatorname{tr}X,\quad
S=\tfrac12\bigl(T^2-\operatorname{tr}X^2\bigr),\quad
N=\det X,
$$

(Cayley–Hamilton; receipt to $10^{-15}$), the spectrum is real, and $X=\sum_{i=1}^3\lambda_ie_i$ over a Jordan frame of orthogonal idempotents (receipt via Lagrange interpolation). The three eigenvalues are the model's harmonics; a Jordan frame is the "standing-wave" decomposition; collapse-talk types as the passage from $X$ to $(\lambda_i,e_i)$ with $e_i\in\mathbb{OP}^2$.

Depressing the cubic by $\lambda=\mu+T/3$ gives $\mu^3+p\mu+q$ with

$$
p=S-\tfrac{T^2}{3},
\qquad
q=-N+\tfrac{TS}{3}-\tfrac{2T^3}{27},
$$

and the locus of coincident eigenvalues — the thought's *resonance* — is exactly

$$
\boxed{4p^3+27q^2=0,}
$$

the cusp of [[algebra/a2-inverse-cover|the $A_2$ inverse cover]]. Receipt: a doubly-degenerate Jordan spectrum lands on it to $10^{-15}$. Away from the cusp, analytic continuation of the three eigenvalues realizes full $S_3=W(A_2)$ sheet monodromy: a loop around one branch of the discriminant is a transposition, a loop around both is a 3-cycle, a loop around neither is the identity (receipts: `monodromy`, all three). The trace-zero triple $(\mu_1,\mu_2,\mu_3)$, $\sum\mu_i=0$, is a Cartan of $\mathfrak{sl}_3$, and the six differences $\mu_i-\mu_j$ are the six $A_2$ root values — the same package as the inverse cover's pushforward algebra, produced here by a *different* cubic.

[[nilpotency-and-the-wall/a2-the-fourth-register|The rank-two motif note]] states the vault's bridge demand: to select $A_2$, a bridge "must recover stronger data such as the cubic map-germ $u^3+au+b$, its contact-equivalence class, Milnor or Tjurina number, discriminant cusp, vanishing-cycle pairing, or the relevant Weyl action." The characteristic-cubic map

$$
\mathrm{ch}:\mathfrak h_3(\mathbb O)\longrightarrow\mathbb R^2,
\qquad
X\longmapsto(p(X),q(X)),
$$

recovers the map-germ, the discriminant cusp, and the Weyl action simultaneously, and it is invariant under $\operatorname{Aut}(\mathfrak h_3(\mathbb O))=F_4$ — receipt-verified on the $O(3)$-conjugation subgroup, [CITED] for full $F_4$. The eigenvalue cover of $\mathfrak h_3(\mathbb O)$ is the pullback along $\mathrm{ch}$ of the degree-three cover over the discriminant complement. This is a **fifth register** for the $A_2$ motif, and the first one that arrives with its comparison map already constructed. What it does *not* do: satisfy [[algebra/a2-inverse-cover|the inverse cover's]] own bridge test verbatim, which demands a functor from *the foundational moduli problem*; $\mathrm{ch}$ is a functor from a physical model's observable space, and importing that model into the foundation remains [OPEN]. The firewall of [[algebra/entry|the algebraic pre-core]] is untouched: nothing here equates $|S_3|=6$, the six roots, $\dim_{\mathbb R}S^6$, or KO-dimension — the bridge is a map of covers, not an integer.

## 4. The octonionic phase space: charge, spin, mass, area

The honest referent for "the phase space of spacetime includes the octonions" exists and is classical mathematics: the Freudenthal triple system $\mathfrak M(\mathfrak h_3(\mathbb O))$, the 56-dimensional space $\mathbb R\oplus\mathbb R\oplus\mathfrak h_3(\mathbb O)\oplus\mathfrak h_3(\mathbb O)$ carrying an invariant **symplectic form** and an invariant **quartic form** $I_4$, with automorphism group of type $E_7$. It is a phase space in the literal sense — symplectic, with electric–magnetic duality as its linear symplectomorphisms. In extremal black-hole physics [CITED — attractor mechanism; Ferrara–Günaydin orbit classification; the black-holes/qubits literature] the dictionary is:

- **charge**: $X\in\mathfrak h_3(\mathbb O_s)$ — the 27 electric charges of the five-dimensional theory are exactly $\dim\mathfrak h_3=27$ — or a dyonic $x\in\mathfrak M$ in four dimensions;
- **spin**: $J$, entering under the radical;
- **mass**: the BPS bound $M=|Z(x,\text{moduli})|$ — mass depends on where the observer stands in moduli space;
- **area**: $S_5=2\pi\sqrt{N(X)-J^2}$ (BMPV, whose STU truncation is the diagonal: receipt `N(diag(Q1,Q2,Q3)) = Q1Q2Q3`), and $S_4=\pi\sqrt{|I_4(x)|}$ — functions of duality invariants alone.

Two receipts pin the structure without importing the supergravity derivations. In the STU/three-qubit realization $I_4=-\mathrm{Det}$, Cayley's $2\times2\times2$ hyperdeterminant: it is $SL(2)^3$-invariant to $10^{-11}$; the GHZ class has $\mathrm{Det}\neq0$ (large black hole, nonzero area) while the W class has $\mathrm{Det}=0$ (the *small*-black-hole stratum, which the string literature identifies with perturbative particle states — the thought's *black holes are particles*, located exactly on the rank-degenerate orbits; its Jordan shadow is the receipt `rank-2 element has det N = 0`). And **Freudenthal duality** — the nonlinear map $\tilde x=\Omega\,\nabla\sqrt{I_4}$ — satisfies $\tilde{\tilde x}=-x$ and $I_4(\tilde x)=I_4(x)$ (receipts to $10^{-11}$): the octonionic phase space carries a genuine nonlinear duality that fixes the horizon-area shadow while moving everything else. If the thought wants a wave–particle-like involution on the phase space, this is the exact candidate it already owns.

The real-form choice is not decoration: five-dimensional maximal supergravity uses the *split* octonions ($E_{6(6)}$ on $\mathfrak h_3(\mathbb O_s)$), the exceptional magic $\mathcal N=2$ theory the compact ones. Which real form is a semilinear datum of exactly the kind [[algebra/real-forms-and-factive-spacetime|the real-forms note]] says must be supplied and cannot be inferred from the complexification — the $\tau$-grammar applies to $\mathbb O$ itself.

## 5. The horizon as invariant shadow

In the attractor mechanism the scalar moduli flow to horizon values fixed by the charges alone, and the area is a function of the duality invariant only. Typed in this vault's grammar: the flow from asymptotic data to horizon data is a **noninvertible arrow that forgets moduli and retains the invariant** — the same shape as the conditional-expectation wall of [[semiorthogonal-decompositions/entry|the categorical-wall reading]] and [[wall-construction-interface/entry|the wall interface]], with $(T,S,N)$ or $I_4$ the retained central data. Mass is moduli-dependent; area is not. That contrast is the precise content of *the horizon is a shadow of the ontology*: the ontology is the orbit $E_7\cdot x$ together with the moduli, the shadow is the invariant the quotient map keeps. And the shadow is areal — an $L^2$ object, landing on the same side of the dimensional joint as [[program-core/descent-response-geometry|the core's areal modulus]]. Nothing here feeds the CWST spectral arrow, and this note claims no wall construction: the attractor flow is a *worked instance of the type*, in someone else's theory.

A paragraph the thought is owed on harmonics-as-physics, kept at its grade: quasinormal modes are the ringdown harmonics of an actual horizon, and Bekenstein–Mukhanov/Hod area quantization reads them as an evenly spaced area spectrum — a hydrogen-like tower for black holes. **[HEURISTIC — CITED]**; nothing in this note depends on it. Wheeler's geons — wave packets confined by their own gravity — are the ancestral form of the whole thought. [CITED — Wheeler 1955.]

## 6. Which $S^6$, and the positivity–integrability dichotomy

The octonionic content of the six-sphere is already canonical in [[algebra/algebra-before-geometry|algebra-before-geometry]]: $S^6=\{u\in\operatorname{Im}\mathbb O:\|u\|=1\}\cong G_2/SU(3)$, and the almost complex structure $J_u(v)=u\cdot v$ is not integrable. This note adds receipts and one sharpening. Receipts: $J_u$ preserves the tangent space; $J_u^2=-1$ *by alternativity* — the identity that fails one rung up the Cayley–Dickson tower, where sedenions lose norm composition (receipt: violation $0.61$; Hurwitz ends the tower at $\mathbb O$); the round metric is Hermitian for it; the Nijenhuis tensor is nonzero (numeric, with a $C^3$ control at $10^{-15}$). The sharpening, found by the fit and then checked: in this normalization

$$
\boxed{N_J(v,w)=2\,[u,v,w]}
$$

— the integrability obstruction *is* the associator, coefficient two, with no $J$-component (receipt: residual $10^{-11}$, coefficients $(2,0)$). Nonassociativity is not an analogy for nonintegrability here; it is the same tensor.

The manuscript's integrable structure on $S^6$, if it survives review, is a *different* geometry on the same smooth manifold: non-Kähler because $b_2=0$, without monodromy-compatible polarization (its own Remark 3.23; signature $(1,1)$, receipt of 2026-08-24), automorphisms $\mathbb C^*$ rather than $G_2$ — everything [[algebra/s6-manuscript-branch|the branch note]] and [[complex-presentation-without-polarization/entry|complex presentation without polarization]] already record. The clean statement the thought runs into is a dichotomy: **on $S^6$, positivity and integrability cannot be held together** — $b_2=0$ forbids any Kähler structure outright, and LeBrun forbids an integrable orthogonal $J$ for the round metric. The octonionic geometry takes positivity with torsion (nearly Kähler); the manuscript takes integrability without positivity. A wave–particle duality *between the two geometries* would be a functor trading integrability for positivity on one underlying sphere. That arrow is **[OPEN CONSTRUCTION]**, nothing in this note builds it, and the sixfold firewall stands as written.

## 7. Obligations

1. The identification of black-hole observables with $\mathfrak h_3(\mathbb O)$ is a modeling conjecture; the exact content is the algebra and the maps above.
2. Journal references are unverified in this session; per [[library|library]] discipline, verify before any citation is promoted (Carter 1968; BMPV 1996; Ferrara–Günaydin 1997; Duff 2006; Borsten–Dahanayake–Duff–Rubens 2009; Jordan–von Neumann–Wigner 1934; Albert 1934; Frölicher 1955; LeBrun 1987; Wheeler 1955).
3. No dynamics is constructed on $\mathfrak M(\mathfrak h_3(\mathbb O))$: the phase space, its symplectic form, quartic, and F-duality are kinematics. A flow whose resonances sit on the $A_2$ cusp is the natural next construction target, and it must come with its own site and state, not by renaming.
4. The wedge/degrees-of-freedom sentence stays decoration until typed against [[wall-construction-interface/entry|the wall interface]].
5. The receipts require numpy; a stdlib rewrite is owed on promotion into any module with a stdlib receipt contract.
6. $N_J=2[u,v,w]$ is receipt-grade at sampled points; a symbolic proof (or a source locating it in the nearly-Kähler literature) is owed before it is called a theorem of the vault.

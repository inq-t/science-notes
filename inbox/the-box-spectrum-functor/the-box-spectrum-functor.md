# The Box-Spectrum Functor

The functor asked for exists at the $A_2$ level, and it comes with three theorems the request did not anticipate. Exactly: the map sending a de Sitter black hole to its Jordan spectrum is canonical **into the $F_4$-quotient** of $\mathfrak h_3(\mathbb O)$, its realization fibre is $F_4/\mathrm{Spin}(8)$ — twenty-four hidden octonionic directions governed by local triality, receipted here by numerically rediscovering $\dim\mathrm{Der}(\mathfrak h_3(\mathbb O))=52$ — and that fibre is *absorbed in stages at the $A_2$ strata* ($24\to16\to0$), which is the exact form of "the algebra of nothing in particular passing into scaled, relational facts." The spectral ladder then provably caps at three ($\mathfrak h_4(\mathbb O)$ fails the Jordan identity), so hair cannot be a fourth eigenvalue; it enters by Freudenthal doubling, where duality washes out the box frame and reads only the hair intensity. And the Schrödinger equation of the cosmos is delivered at citation grade with the same $A_2$ cubic inside it: for dust plus $\Lambda$, the Wheeler–DeWitt constraint becomes an eigenvalue problem $\hat H\psi=m\psi$ whose potential peaks **exactly at the Nariai point** — mass is the eigenvalue, the Born density is conformal-time dwell, $|\psi|^2\,da=C\,d\eta$, and de Sitter black holes are literally *resonances* of $\hat H_{\mathrm{cosmos}}$ with width $\sim e^{-2\Theta(m)}$. Receipts: `box_spectrum_receipts.py` (numpy; 25 checks; nonzero exit on failure).

## 1. What is delivered

| Asked | Delivered | Status |
|---|---|---|
| the box-spectrum functor | $F:\mathrm{SdS}(\Lambda)\to\mathfrak h_3(\mathbb O)/F_4$, spectra = horizons; fibre $F_4/\mathrm{Spin}(8)$, local triality | [EXACT — receipts at Lie-algebra grade] |
| hair as non-diagonal directions | impossible as a fourth eigenvalue ($\mathfrak h_4(\mathbb O)$ fails Jordan — receipt); hair lives in the Freudenthal double, duality-invariantly as $a^2+q_e^2$ | [EXACT obstruction + model move] |
| "algebra of nothing in particular" → "scaled relational facts" | homogeneous fibre (groupoid) over discriminant-stratified base (monoid); fibre collapse $24\to16\to0$ receipted | [EXACT structure; reading PROPOSED] |
| Schrödinger equation of the cosmos | $i\hbar\,\partial_\tau\psi=\hat H\psi$, $\hat H=\frac{p_a^2}{2a}+\frac12\bigl(a-\frac{a^3}{L^2}\bigr)$, dust as relational clock | [CITED framework; identities EXACT] |
| Born rule as gradient / mass | $\lvert\psi\rvert^2da=C\,d\eta$ (conformal dwell; exact WKB identity $d\eta/da=1/p$, Numerov-receipted to $0.14\%$); mass = the eigenvalue of $\hat H$ | [EXACT under declared ordering] |

## 2. The functor at the $A_2$ level

$F_4=\operatorname{Aut}(\mathfrak h_3(\mathbb O))$ acts transitively on Jordan frames, and an element with distinct eigenvalues determines its frame; so the fibre of the spectral map $\mathrm{ch}$ over a distinct-root point of the $A_2$ base is **one $F_4$-orbit**. The functor is therefore canonical into the quotient:

$$
F:\;(\Lambda,m)\;\longmapsto\;\bigl[X\bigr]\in\mathfrak h_3(\mathbb O)_0/F_4,
\qquad
\operatorname{spec}(X)=(r_c,\,r_h,\,-(r_c{+}r_h)),
\qquad
m=-\frac{\det X}{2L^2},
$$

landing in the trace-zero slice with $S(X)=-L^2$. Choosing an actual element — a *presentation* — costs exactly the homogeneous space $F_4/\mathrm{Spin}(8)$. Receipts, by solving the derivation equations of $\mathfrak h_3(\mathbb O)$ numerically (10206 linear conditions on $\mathrm{End}(\mathbb R^{27})$):

- $\dim\mathrm{Der}(\mathfrak h_3(\mathbb O))=52$ — the algebra $\mathfrak f_4$, found by nullity, not imported;
- derivations fixing a frame: dimension $28=\mathfrak{so}(8)$; fibre dimension $52-28=24=3\times8$: three hidden octonions;
- **local triality**: the frame-fixing algebra preserves each of the three off-diagonal octonion slots, acts skewly on each, and each slot restriction is an *isomorphism onto* $\mathfrak{so}(8)$ — one $\mathfrak{so}(8)$, three inequivalent faces (receipts i–iv). The three hidden octonions of a de Sitter black hole's presentation are a triality triple.

## 3. The fibre is the algebra of nothing in particular

The radical-copernicanism audit (2026-08-25) concluded that Copernican democracy holds *within* a level while the passage between levels is one-sided: **a groupoid fibered over a monoid**. The functor realizes that shape exactly. The fibre $F_4/\mathrm{Spin}(8)$ is a homogeneous space — no point distinguished, every presentation reachable from every other by an invertible symmetry: the groupoid level, and the precise sense in which the phase space is "nothing in particular." The base is the $A_2$ chamber with its stratification, and motion onto the strata is noninvertible degeneration: the monoid level, the "scaled, relational facts" ($r_c$, $r_h$, their differences = temperatures). The receipted bridge between the two is the **fibre collapse**: stabilizer dimensions across the strata are

$$
28\;(\mathfrak{so}(8))
\;\longrightarrow\;
36\;(\mathfrak{so}(9))
\;\longrightarrow\;
52\;(\mathfrak f_4),
\qquad\text{orbits}\qquad
24\;\longrightarrow\;16\;\longrightarrow\;0,
$$

so at the fold one hidden octonion's worth of presentation-freedom is absorbed into fact ($16=\dim F_4/\mathrm{Spin}(9)=\dim\mathbb{OP}^2$), and at the cusp all of it is. This is the derivation-side mirror of [[algebra/a2-positive-completion|the positive-completion fibre types]] $\mathbb C^3\to\mathbb C^2\to\mathbb C$, and it echoes the no-response lemma of [[program-core/common-response-form|the common response form]]: a fully symmetric datum plus symmetry-equivalent presentations yields no fact; facts appear exactly where the symmetry fails to act freely. Typing hazard honored: everything here is *horizontal* (state/presentation transport); no modular or weight-side claim is made, and the radical-copernicanism gating question — whether the wall family is a chain of half-sided modular inclusions — is untouched by this note.

## 4. The cap at three, and where the hair goes

$\mathfrak h_4(\mathbb O)$ violates the Jordan identity (receipt: defect $\sim21$, against $10^{-15}$ for $\mathfrak h_3(\mathbb O)$ and for $\mathfrak h_4(\mathbb H)$): the octonionic spectral ladder ends at three eigenvalues, so the KN–dS quartic **cannot** be a bigger octonionic spectrum. The hair must enter by doubling — the Freudenthal system $\mathfrak M=\mathbb R\oplus\mathbb R\oplus\mathfrak h_3\oplus\mathfrak h_3$ with quartic $I_4$ — and there the box pays a price stated by the receipts: on the four-weight normal-form slice, $\mathrm{Det}=4ABCD$, and the residual duality torus rescales $(A,B,C,D)$ freely at fixed product. Assigning the four horizon roots as the four weights [MODEL MOVE] gives

$$
I_4\;\propto\;\prod_i\rho_i\;=\;s\;=\;-(a^2+q_e^2)L^2:
$$

**duality reads only the hair intensity $a^2+q_e^2$; the box radius and the mass — $(p,q)$ — are frame data.** This is the same split as note one's mass-versus-area contrast, now derived rather than observed; and the hairless box ($s=0$) sits on the $I_4=0$ small/particle stratum, closing the loop with the small-black-hole reading. The A₂-level functor is faithful on facts; the A₃-level one is faithful only on hair — a genuine asymmetry the construction discovered, not assumed.

## 5. The Schrödinger equation of the cosmos

Dust plus $\Lambda$ in a closed FLRW universe obeys $\dot a^2=-f(a)$ with $f$ *the SdS lapse* — the Oppenheimer–Snyder identity: one cubic read from inside is a cosmos, read from outside is a black hole in a box, which is the Copernican move in its sharpest exact form. With $p=a\dot a$ the constraint is $p^2=aP(a)/L^2$, and dust is precisely the matter that supplies a relational clock [CITED — Brown–Kuchař; Husain–Pawłowski]. The constraint then linearizes in the dust momentum and becomes an honest Schrödinger equation,

$$
i\hbar\,\frac{\partial\psi}{\partial\tau}=\hat H\psi,
\qquad
\hat H=\frac{p_a^2}{2a}+V_0(a),
\qquad
V_0(a)=\frac12\Bigl(a-\frac{a^3}{L^2}\Bigr),
$$

with ordering declared ($-\hbar^2\tfrac{1}{2a}\partial_a^2$; alternatives shift $O(\hbar^2)$). Its stationary sector is an eigenvalue problem, and the eigenvalue is the mass: $\hat H\psi=m\psi$. Two receipted identities give the equation its content:

- $V_0$ has its **maximum at $a=L/\sqrt3=r_{\mathrm{Nariai}}$ with height $V_0=L/(3\sqrt3)=m_{\mathrm{Nariai}}$** — the Nariai data are the critical point of the cosmic Hamiltonian, and the $A_2$ chamber is exactly the sub-barrier regime;
- the turning points solve $V_0(a)=m$ and are exactly $r_h$ and $r_c$: the two horizons are where the mass eigenvalue meets the barrier.

So a de Sitter black hole is, in the cosmos's own Schrödinger equation, a **resonance**: an interior branch $(0,r_h]$ coupled to the exterior $[r_c,\infty)$ through the $A_2$ barrier, with width $\sim e^{-2\Theta(m)}$. The exponent is receipted: $\Theta(m)$ decreases strictly from $\Theta(0)=L^2/3\hbar$ (the empty-box nucleation exponent, exact) to $0$ at Nariai — the box nucleates its resonant, cusp-sitting black hole most easily, and at the cusp the resonance dissolves into the continuum. Three notes ago this was the sentence "black holes are the particle packets where it resonates"; it is now a statement about the spectrum of a named operator.

## 6. The Born rule is conformal dwell

Under the declared ordering the exact classical identity $d\eta/da=1/p(a)$ holds (receipt), so the WKB Born density of the cosmos is

$$
\boxed{\;|\psi(a)|^2\,da\;=\;C\,d\eta\;}
$$

— the amplitude at scale $a$ is the **conformal time the cosmos dwells there** ([[conformal-time/inq|the conformal-time module]] owns $\eta$). Receipt: a Numerov integration of $\hat H\psi=m\psi$ in the exterior region yields $243$ envelope peaks with $|\psi|^2\!\cdot\!p(a)$ constant to $0.14\%$. The requested clauses then type as follows. *The Born rule is how spacetime has a gradient*: probability is literally the reciprocal gradient — where $\dot a\to0$ (the horizons, the roots, the facts) the dwell diverges; amplitude condenses on the $A_2$ discriminant. *The Born rule is how spacetime has mass*: mass is the spectral parameter of $\hat H_{\mathrm{cosmos}}$, and mass is also what opens the interior branch at all — at $m=0$ the allowed region begins at the box wall $a=L$ (nucleation from nothing; receipt), while any $m>0$ creates an interior allowed region reaching the Schwarzschild radius $r_h\to2m$ (receipt). The ordering-dependence of the dwell density is real and declared: choosing a different factor ordering reweights $|\psi|^2$ by powers of $a$, i.e. chooses a different clock density — the ambiguity *is* the clock choice, which is where [[misner-log-time/inq|Misner's log-time]] and the dust clock live.

## 7. Obligations

1. The physical identification of box data with Jordan spectra remains the [MODEL CONJECTURE] it was; what this note removes is its arbitrariness at the $A_2$ level (canonical into the quotient; fibre computed) and its extendability at the $A_3$ level (duality keeps hair only — the functor cannot be faithful on $(p,q)$ in the double). A construction wanting the full quartet duality-invariantly must change category, not enlarge the matrix.
2. Local triality is receipted at the Lie-algebra level (rank and skewness), not proven symbolically; Chevalley–Schafer ($\mathrm{Der}=\mathfrak f_4$) and the principle of local triality are the classical sources to verify and cite on promotion.
3. The Schrödinger form leans on dust as clock matter [CITED — Brown–Kuchař 1995; Husain–Pawłowski 2011]; radiation or other matter changes the polynomial and the clock, and the boundary condition at $a=0$ (Vilenkin vs Hartle–Hawking) is cited, not adjudicated. Resonance widths are WKB estimates; no exact resonance is computed.
4. The vertical/horizontal firewall of the radical-copernicanism audit is respected; nothing here touches weights, modular flow, or the h.s.m.i. gate. The "groupoid over monoid" reading is structural correspondence, graded [PROPOSED] as ontology.
5. Receipts require numpy; a stdlib rewrite is owed on promotion. Citations unverified this session: DeWitt 1967; Oppenheimer–Snyder 1939; Brown–Kuchař 1995; Husain–Pawłowski 2011; Vilenkin 1984; Hartle–Hawking 1983; Chevalley–Schafer 1950; Jacobson (local triality); Baez 2002.
6. Named next target, inherited and sharpened: compute one resonance of $\hat H_{\mathrm{cosmos}}$ beyond WKB, and ask whether its width law $e^{-2\Theta}$ survives the passage to the Freudenthal double where only hair is duality-visible.

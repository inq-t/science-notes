# Audit: "Λ Is the Inverse Quadratic Casimir"

A parallel line of work proposed that the cosmological constant has an exact algebraic meaning as the reciprocal quadratic Casimir of the trace-zero Jordan cell, \(\Lambda=6/|X|^2\); that a dimensional reduction anchored at the \(\Lambda\)-horizon yields \(\Lambda=64\ell_P^4/(3\lambda_\Lambda^6)\) "exactly, with no free modulus"; and that this dissolves the vacuum-energy problem. The audit finds one exact identity that the vault already holds under another name, one floating-point check of an algebraic inversion mislabeled as a derivation, one function of epoch mistaken for two objects, one exponent error, and one word — *Casimir* — used against the programme's own taxonomy. What survives is stated at the end. Claim labels follow [[program-core/axioms-and-principles#Status vocabulary|the status vocabulary]]; the governing commitments are PC1, *algebraic rearrangeability does not establish ontological identity*, and PC5, *a quantity counts as derived only if its construction does not use it as normalization data*.

## 1. The identity is Vieta, and the vault already has it

**[EXACT]** The Schwarzschild–de Sitter horizon equation \(1-2m/r-r^2/L^2=0\), with \(L^2=3/\Lambda\), is the depressed cubic

$$
r^3-L^2r+2mL^2=0,\qquad(p,q)=(-L^2,\,2mL^2),
$$

with no \(r^2\) term, so its three roots — the black-hole horizon, the cosmological horizon, and one negative root — sum to zero. Vieta's formulas then give \(\sigma_2=r_br_c+r_br_-+r_cr_-=-L^2\) and \(\sum r_i^2=\sigma_1^2-2\sigma_2=2L^2\), **for every \(m\) below the Nariai value**. If the roots are read as the eigenvalues of a trace-zero Jordan element \(X\), then \(|X|^2:=\operatorname{tr}X^2=2L^2\) and \(\Lambda=3/L^2=6/|X|^2\). The receipt verifies this at five values of \(m/m_N\).

This is already in the vault. [[the-grain-of-causal-scale/inbox/de-sitter-box-and-the-octonionic-ladder/de-sitter-box-and-the-octonionic-ladder|The de Sitter box note]] boxes \((p,q)=(-L^2,2mL^2)\), writes the horizon triple as \(X=\mathrm{diag}(r_c,r_h,r_3)\) with \(T(X)=0\) and \(S(X)=-L^2\), and notes that the Jordan spectral map and the box map land in the same base. "\(\Lambda=6/|X|^2\)" is \(S(X)=-L^2\) with both sides multiplied by \(-2\) and inverted. The parallel derivation is correct and not new, and its content is that **the de Sitter radius squared is half the sum of the squared horizon roots** — a statement about SdS, not about \(\Lambda\)'s origin.

## 2. *Casimir* is the wrong word in this programme's own taxonomy

**[NO-GO — PC1]** A Casimir, in the sense the programme fixed in [[inbox/the-constants-of-nature/entry|the constants-of-nature synthesis]], is an invariant of a *representation*: a number fixed by representation theory, the same for every state in the irrep, a *law*. The quadratic invariant \(\sigma_2(X)\) of a Jordan element is an \(F_4\)-invariant *function on the algebra*: it varies from element to element and coordinatizes the orbit space. Under the synthesis's three-way partition — Casimirs, addresses, exchange rates — a quantity that varies with the cell and whose value the algebra does not fix is an **address**. The parallel note concedes exactly this in its own boundary paragraph ("the algebra tells you \(\Lambda\) is \(1/\)Casimir; it doesn't by itself tell you the Casimir's value"), which is the definition of an address, not a Casimir. Renaming \(L^2\) as \(|X|^2/2\) moves nothing between the three columns. The vault's [[algebra/type-ledger|type ledger]] states the rule for integers — "equal integers without \(F\) and \(\varphi\) are salience, not derivation" — and the same discipline extends without change to equal expressions: no functor, no identification.

## 3. The "exact, no-modulus" inversion is an identity check

**[RECEIPT]** — an identity check; calling it a derivation violates PC5. Anchoring [[the-grain-of-causal-scale/inq|the common-count lemma]] \(\lambda^3=\tfrac83\ell_P^2R\) at the \(\Lambda\)-horizon \(R_\Lambda=c/H_\Lambda=\sqrt{3/\Lambda}\) and inverting gives

$$
\Lambda=\frac{64\,\ell_P^4}{3\,\lambda_\Lambda^6},\qquad\lambda_\Lambda=\Bigl(\tfrac83\ell_P^2\sqrt{3/\Lambda}\Bigr)^{1/3}.
$$

Substituting the second into the first returns the first. The reported residual of \(-1.1\times10^{-14}\) is double-precision rounding of that substitution. The receipt performs the same inversion on an arbitrary fake value \(\Lambda=7.3\times10^{-50}\,\mathrm{m^{-2}}\) and obtains a residual of \(-1.1\times10^{-14}\) as well. The check carries no information about \(\Lambda\). It is the grain module's own "direction of explanation, case 3": both dimensionful inputs inserted, an exact consistency diagnostic, circular if called a derivation. Nothing was dissolved; the free modulus was renamed \(\lambda_\Lambda\).

## 4. The "\(\Lambda\)-grain" is one function at a second epoch

**[EXACT — already typed]** The lemma gives \(\lambda\propto R^{1/3}\propto H^{-1/3}\), hence \(E\propto H^{1/3}\). Evaluating at the crossing rate \(H_c=83.1\,\mathrm{km\,s^{-1}Mpc^{-1}}\) gives \(46.3\,\mathrm{MeV}\); evaluating at the asymptotic de Sitter rate \(H_\Lambda=55.7\) gives \(40.5\,\mathrm{MeV}\). These are not two grains in tension; they are the single diagnostic function \(m_{\mathrm{cap}}(N)=(3\hbar^2H(N)/8cG)^{1/3}\) that [[the-grain-of-causal-scale/inq#A crossing value is not a running particle mass|the grain module]] already defines and already warns is "a presentation scale, not automatically a running Standard Model pole mass," evaluated at \(N_c\) and at \(N\to\infty\); [[crossing-evaluated-flat-modulus/inq|the crossing-evaluated flat modulus]] owns the formalism under which such a value is evaluated once at a selected event and pulled back flat. Their ratio is forced by the lemma:

$$
\frac{E_c}{E_\Lambda}=\Bigl(\frac{H_c}{H_\Lambda}\Bigr)^{1/3}=1.142.
$$

The parallel note writes this as \(n_c^{2/3}\); with \(n_c:=H_c/H_\Lambda\) the correct exponent is \(1/3\) (the \(2/3\) value is \(1.305\)). The "checkable question" it poses — does the freezing law connect the two grains by exactly this factor — is the lemma applied twice, not a test. The question of which epoch the closure is evaluated at is real, and it is owned by the event-selector problem, not by the algebra.

## 5. Declining to compute the vacuum energy does not remove it

**[STANDARD]** The parallel note concludes that because \(\Lambda\) is "a Casimir, not a vacuum energy," there is no \(10^{120}\) to explain. The zero-point contributions of quantized fields are not removed by not computing them; renormalized \(\langle T_{\mu\nu}\rangle\) in curved spacetime is a source, and the Casimir *effect* — the other meaning of the word this note has been using — is the laboratory demonstration that vacuum-energy differences are physical. Any account in which \(\Lambda\) is set by a horizon invariant inherits the obligation to say why the field zero-point sector does not also contribute to that invariant. The vault already states this correctly and more carefully: [[coincidence-reframed]] says the tuning is "traded rather than eliminated," and the constants-of-nature synthesis marks the \(10^{122}\) as "not answered — retyped." The parallel note's stronger claim is withdrawn here in favour of the vault's weaker one.

## What survives

Two things, both already held. The mass-independence of the quadratic invariant — \(\sum r_i^2=2L^2\) for every SdS black hole at fixed \(\Lambda\) — is a clean exact fact and a correct statement that the Jordan quadratic norm of the horizon triple reads only the cosmological register, never the mass register; the cubic norm \(\det X=-2mL^2\) reads the mass. That partition of the two invariants across the two registers is worth keeping and is not in the box note in those words. And the two positive roots as "two area-writing horizons" is the typed rhyme [[the-grain-of-causal-scale/causal-spectrum|the causal-spectrum note]] already records as the rank-jump prototype, with its firewall: writing rank two does not derive \(\gamma=2\).

## What would upgrade it

**[OPEN]** A construction that fixes \(|X|\) — equivalently \(L\), equivalently \(\Lambda\) — without inserting \(\Lambda\), \(H\), or \(G\) anywhere upstream. That is the event selector and absolute address the grain module lists as open, restated. The algebra supplies the Nariai ratio \(m_N/L=1/3\sqrt3\), the two-positive-root count, and the discriminant's exponent six; it has never supplied \(L\). Until it does, \(\Lambda=6/|X|^2\) is a true sentence about how to read a number the universe handed us.

## Receipt

[[contemporary-puzzles/dark-energy-and-acceleration/receipts/lambda_casimir_audit.py|lambda_casimir_audit.py]] verifies the Vieta identities at five masses; checks the recomputed \(\Lambda=1.0891\times10^{-52}\,\mathrm{m^{-2}}\), \(\lambda_\Lambda=4.872\,\mathrm{fm}\), and \(E_\Lambda=40.51\,\mathrm{MeV}\) against the parallel note's stated values to \(0.03\%\) and asserts the residual is at round-off; runs the fake-\(\Lambda\) negative control; and checks the \(1/3\) exponent, reporting the 14% miss the \(2/3\) claim would incur. Standard library only, nonzero exit on failure.

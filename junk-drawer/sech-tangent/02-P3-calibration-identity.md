# P3: the calibration is not free

### A theorem from your own definitions, and what it costs

---

## 1. The identity

Two exact relations, both already implicit in the note.

**Thermodynamic side.** Let $K$ be the modular Hamiltonian, $\rho_\beta = e^{-\beta K}/\mathcal{Z}(\beta)$, and $S(\beta)$ its von Neumann entropy. Then $S = -\beta\,\partial_\beta\ln\mathcal{Z} + \ln\mathcal{Z}$, and

$$\frac{dS}{d\beta} = -\beta\,\partial_\beta^2\ln\mathcal{Z} = -\beta\,\mathrm{Var}_\beta(K) \quad\Longrightarrow\quad \left.\frac{dS}{d\beta}\right|_{\beta=1} = -C_E.$$

**Geometric side.** With $\mathfrak{C} = \pi/(Ht_P)^2$ and $d\ln H/dN = -(1+q)$,

$$\frac{d\ln \mathfrak{C}}{dN} = 2(1+q). \qquad \text{(your Prop 2)}$$

**Now impose what D7 and D9 already assert** — that the horizon capacity *is* the modular entropy, $\mathfrak{C} = S/k_B$, and $n = C_E/\mathfrak{C}$. Chain rule:

$$\boxed{\;\frac{d\beta}{dN} \;=\; -\,\frac{2\,(1+q)}{n}\;}$$

This is not a new assumption. It follows from definitions the note already makes. **P3 is therefore not an independent postulate — it is a constraint linking the calibration, the spectral index, and the deceleration parameter.**

Two immediate consequences.

**The sign is forced.** $d\beta/dN < 0$ unless $q < -1$, which Prop 15 forbids. So the correct global form is $\beta - \beta_c = -(N - N_c)$. The note's hedge ("a signed dimensionless deformation, not an ordinary positive inverse temperature") is doing real work and should be made explicit.

**Unit calibration is a spectral condition.** $|d\beta/dN| = 1 \iff n = 2(1+q)$. Equivalently, in the cleanest form:

$$\frac{d\mathfrak{C}}{dN} = C_E.$$

> **One e-fold is the scale increment over which the horizon's capacity grows by its own modular fluctuation.**

That sentence contains no metric. It is a definition of scale written entirely in algebraic quantities, and it is what P3 amounts to.

---

## 2. It predicts $\nu_c$ instead of postulating it

Combine $n_c = 2(1+q_c)$ with your (3.12), $q_c = \tfrac12 - \tfrac34\nu_c$ and $\nu_c = f_c n_c$:

$$n_c = \frac{3}{1 + \tfrac32 f_c}, \qquad \nu_c = \frac{3f_c}{1+\tfrac32 f_c}.$$

| Closure | $f_c$ | $n_c$ | $\nu_c$ | $r$ | $q_c$ | $z_c$ | $w_0$ | vs DESI |
|---|---|---|---|---|---|---|---|---|
| Cai–Kim + unit calibration | 1 | 1.200 | 1.200 | 1.500 | $-0.400$ | 0.148 | $-0.909$ | 1.62σ |
| Kodama–Hayward + unit calibration | 0.608 | 1.570 | **0.954** | 0.911 | $-0.215$ | 0.397 | $-0.785$ | 0.66σ |
| *(current postulate $\nu_c=1$)* | — | — | 1.000 | 1.000 | $-0.250$ | 0.344 | $-0.809$ | 0.23σ |

The Kodama–Hayward row is self-consistent: $f_c = (1-q_c)/2 = 0.6076$ and $n_c = 2(1+q_c) = 1.5695$ simultaneously, from the quadratic $2.25\nu^2 + \nu - 3 = 0$.

**Read this carefully.** The calibration identity turns P7 from a postulate into a *prediction*, and the prediction is $\nu_c = 0.954$ (dynamical horizon) or $1.200$ (equilibrium horizon) — not exactly 1. The dynamical branch lands within 5% of unit response, which is either a striking near-coincidence or the correct answer with a small correction.

Either way, this is progress of the kind you want: two of your nine postulates (P3, P7) collapse into one, and the survivor is computable.

The cost is honest: the derived closures fit slightly worse than the postulated one (0.66σ and 1.62σ versus 0.23σ). That is information. If the data eventually pin $\nu_c = 1.00 \pm 0.05$, the unit-calibration hypothesis is *excluded* and $|d\beta/dN| \neq 1$.

---

## 3. The reframing you asked for

Stop trying to prove that geometric $N$ matches algebraic $\beta$. Invert it.

1. Take the wall algebra as primitive. The capacity $\mathfrak{C}$ is a modular entropy — algebraic, no metric.
2. **Define** logarithmic scale by $d\mathfrak{C}/dN = C_E$. Scale is now the parameter in which capacity grows at the rate set by its own fluctuation. Purely informational.
3. The geometry is then not assumed but *tested*: by Cai–Kim (your A8), the first law at the apparent horizon with quarter-area entropy already yields Friedmann. So the metric side is fixed independently.
4. The content of P3 becomes the consistency condition $n(N) = 2(1+q(N))$ — one relation between an algebraic quantity and a geometric one, holding at every $N$.

This is exactly the move your programme wants: geometry is derived, and the residual conjecture is a matching condition rather than a postulated identification. It is also strictly stronger than the current P3, because it must hold globally, not just at the crossing.

---

## 4. Three problems the identity exposes

Being creative here means also being willing to find that the box has a hole in it.

### 4.1 $\beta = 1$ and $\beta = \beta_c$ cannot be the same point

For a two-level sector with gap $\Delta K$, the occupation is $p_\beta = [1+e^{-\beta\Delta K}]^{-1}$, which equals $1/2$ **only at $\beta = 0$**. So the crossing sits at $\beta_c = 0$ — the infinite-modular-temperature, maximally-mixed point, which is also where $\mathrm{Var}(K)$ is maximal. Good: the pulse peak has a natural spectral meaning.

But $C_E$ is *defined* at $\beta = 1$ by the KMS condition. With $\beta - \beta_c = -(N-N_c)$ and $\beta_c = 0$, the physical wall sits at $N - N_c = -1$: **exactly one e-fold before the crossing.**

Observationally, $N_0 - N_c = +0.295$. So either the identification is off by an e-fold, or $C_{E,c}$ in §3.5 is not the capacity of entanglement of the physical state, or the two-grade Boltzmann reading is wrong. The note conflates $\beta = 1$ (where $C_E$ lives) with $\beta = \beta_c$ (where the pulse peaks), and they are different points.

This must be resolved before P3 can be stated precisely. It is the sharpest technical problem in the note.

### 4.2 Theorem 3.2 and §4 assume incompatible spectra

Theorem 3.2 takes $\ln\mathcal{Z}(\beta) = A\beta^{-n}$. Then $\mathrm{Var}_\beta(K) = n(n+1)A\beta^{-n-2}$ — **monotonically decreasing in $\beta$, with no maximum.** A pure power-law spectrum produces no pulse.

§4's two grades produce a pulse peaked at $\beta = 0$. These are different spectral models, and the note uses the first to fix the amplitude ($n_c$) and the second to fix the shape.

The reconciliation is available and should be written: the power law describes the **bulk** spectrum (area law, entropy, $C_E = nS$), while the two grades describe a **distinguished sector** whose occupation crosses. Then

$$C_E^{\rm tot} = C_E^{\rm bulk} + C_E^{\rm binary},$$

only the second varies, and $n_c = C_E^{\rm tot}/\mathfrak{C} \neq C_E^{\rm binary}/\mathfrak{C}$.

That is a coherent picture, but it is a *third* postulate (this is your unstated P2 in a sharper form), and it means the $n_c$ entering the amplitude and the $g$ entering the shape refer to different parts of the spectrum. Say which is which.

### 4.3 A pure CFT gives no pulse — and that is a feature

For a conformal theory, the modular Hamiltonian of a ball is invariant under simultaneous dilation of region and state: the weight scales as $\lambda$, $T_{00}$ as $\lambda^{-d}$, the measure as $\lambda^{d-1}$, product $\lambda^0$. So $dK/dN = 0$, hence $d\beta/dN = 0$, hence no pulse.

**The pulse therefore requires conformal breaking**, which in FLRW is supplied by pressureless matter. This is a genuine structural statement and it explains something the note currently treats as coincidence: the susceptibility maximum sits near matter–defect comparability *because matter is what makes the modular Hamiltonian scale-dependent in the first place*.

It also supplies a sharp check. In the radiation era the source is conformal, so the pulse should switch off — consistent with $\rho_X/\rho_m \sim 10^{-14}$ at recombination, but now for a reason rather than by arithmetic.

---

## 5. What to do

**Immediately.** Add the calibration identity as a proposition. It is three lines, it eliminates a postulate, and it converts $\nu_c$ from a closure into a prediction with a number attached.

**Then decide 4.1.** Where does the physical state sit relative to the crossing in $\beta$? Until that is fixed, "$\beta - \beta_c = N - N_c$" does not have a determinate meaning, and §3.5's normalization $C_{E,c}$ is ambiguous between two different points.

**Then split the spectrum (4.2).** Bulk power law for the amplitude, distinguished sector for the shape, with the spectral-gap condition written out.

**Then the real target.** The calibration identity says $n(N) = 2(1+q(N))$ globally. Compute $n(N)$ for the FLRW apparent horizon — the bulk part from the area law, the sector part from whatever generates $g$ — and check it against the model's own $q(N)$. That is a self-consistency test of the whole edifice, using only quantities the note already defines, and it does not wait on T4 or on a covariant tensor.

If $n(N) = 2(1+q(N))$ holds, P3 is discharged and the sech² is derived rather than inserted. If it fails, you learn the calibration is not affine, and the exact sech² becomes an approximation with a computable correction.

Either outcome is worth more than the current conjecture.

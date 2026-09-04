---
inq.module: "transported-response-observability-solder"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Transported Response Observability Solder

A geometric response need not be the physical transfer defect in order to
force a transfer gap. If each independently constructed bounded response is
dominated by the defect of the positive transfer at that stage, then the
responses pulled back along the preceding transfers form an observability
Gramian on the initial vacuum complement. A uniform lower frame for that
transported family forces the ordered product to contract even when every
single stage has blind nonvacuum directions. This identifies an explicit
analysis operator for the vacuum-aligned transfer cocycle, keeps formation,
Euclidean attenuation, and Lorentzian unitarity in different types, and
reduces the Yang--Mills problem to a noncircular kernel comparison plus a
uniform fixed-slab frame theorem.

**Status: [EXACT] for the contraction-defect ledger, two-slice residual,
bounded-response solder, transported Gramian, kernel formula,
complementary-stage theorem, and fixed-slab implication; [CONSTRUCTION] for
flux, expectation, and closed Hessian response operators on a common
physical carrier; [OPEN] for an
action-derived interacting Yang--Mills comparison uniform in volume and
regulator, Osterwalder--Schrader identification, continuum existence, and
Poincare-Casimir reconstruction.**

## Three operators with three different jobs

The phrase “the operator” hides the present category error. There are three
operators before there is a mass:

1. a transfer arrow propagates a vector between pointed carriers;
2. a response operator detects a declared geometric distinction on the
   carrier at one stage; and
3. a transported analysis operator asks whether those stagewise responses
   collectively see every initial nonvacuum direction.

Let

$$
A_k:\mathcal K_k\longrightarrow\mathcal K_{k+1},
\qquad
\|A_k\|\leq1,
\tag{TR1}
$$

be contractions on vacuum-complement carriers. These may be the centered
arrows supplied by [[vacuum-aligned-transfer-cocycle/inq|the pointed transfer
cocycle]]. Put

$$
B_{k:m}
:=
\begin{cases}
I_{\mathcal K_m},&k=m,\\
A_{k-1}\cdots A_m,&k>m,
\end{cases}
\qquad
D_k:=I_{\mathcal K_k}-A_k^*A_k\geq0.
\tag{TR2}
$$

The operator $D_k$ is the exact squared-norm defect of the transfer. It is
not yet a Hessian, flux, entropy, observation, or mass.

Independently choose a bounded positive response

$$
0\leq R_k\leq I_{\mathcal K_k}
\tag{TR3}
$$

and a coefficient $\eta_k>0$. The **same-carrier response solder** is the
operator inequality

$$
\boxed{D_k\geq\eta_kR_k.}
\tag{TR4}
$$

It says that every distinction charged by the declared geometry pays at
least the stated amount of actual transfer defect. It does not require the
two operators to be equal. Define

$$
L_k:=\sqrt{\eta_k}\,R_k^{1/2}:
\mathcal K_k\longrightarrow\mathcal K_k,
\qquad
S_k:=D_k-L_k^*L_k\geq0.
\tag{TR5}
$$

Now the answer to “what does the operator operate on?” is explicit:
$R_k$ and $L_k$ act on the distinction as it exists at stage $k$, whereas
$L_kB_{k:m}$ acts on the initial distinction after propagating it to that
stage. The residual $S_k$ is transfer loss not yet accounted for by the
chosen geometry.

There is also an exact carrier meaning. With
$\delta_k=D_k^{1/2}$ and
$\mathcal D_k=\overline{\operatorname{Ran}\delta_k}$, Douglas
factorization says that (TR4) is equivalent to the existence of a
contraction

$$
C_k:\mathcal D_k\longrightarrow
\overline{\operatorname{Ran}L_k},
\qquad
L_k=C_k\delta_k.
\tag{TR5a}
$$

The solder is therefore a map from the canonical physical transfer-defect
carrier to the declared geometric response carrier. It remains an existence
theorem until the action or wall construction supplies the comparison and
identifies $C_k$ naturally.

## The exact response-and-residual ledger

The adjacent identity

$$
B_{k:m}^*B_{k:m}-B_{k+1:m}^*B_{k+1:m}
=B_{k:m}^*D_kB_{k:m}
\tag{TR6}
$$

telescopes. Substituting (TR5) yields

$$
\boxed{
I-B_{n:m}^*B_{n:m}
=
\sum_{k=m}^{n-1}B_{k:m}^*L_k^*L_kB_{k:m}
+
\sum_{k=m}^{n-1}B_{k:m}^*S_kB_{k:m}.}
\tag{TR7}
$$

For every $x\in\mathcal K_m$ this is the norm identity

$$
\boxed{
\|x\|^2
=
\|B_{n:m}x\|^2
+\sum_{k=m}^{n-1}\|L_kB_{k:m}x\|^2
+\sum_{k=m}^{n-1}\|S_k^{1/2}B_{k:m}x\|^2.}
\tag{TR8}
$$

This is a conservation-shaped theorem, but what is conserved is the initial
Hilbert norm on a declared carrier. The three summands are surviving norm,
the portion of the defect witnessed by the chosen response, and the
uninterpreted positive remainder. Calling the middle term causal charge or
the last term entropy requires another theorem.

Define the transported response analysis map and its Gramian by

$$
\mathcal O_{n:m}x
:=
\left(L_kB_{k:m}x\right)_{k=m}^{n-1},
\qquad
\mathcal G_{n:m}^{\mathrm{resp}}
:=
\mathcal O_{n:m}^*\mathcal O_{n:m}
=
\sum_{k=m}^{n-1}
\eta_kB_{k:m}^*R_kB_{k:m}.
\tag{TR9}
$$

Equation (TR7) gives the exact order comparison

$$
0\leq
\mathcal G_{n:m}^{\mathrm{resp}}
\leq
I-B_{n:m}^*B_{n:m}.
\tag{TR10}
$$

Therefore the **transported-response theorem** is

$$
\boxed{
\mathcal G_{n:m}^{\mathrm{resp}}\geq\kappa I,
\quad 0<\kappa<1
\quad\Longrightarrow\quad
\|B_{n:m}\|\leq\sqrt{1-\kappa}<1.}
\tag{TR11}
$$

No stage is required to have a vacuum-only kernel. For a finite chain,

$$
\boxed{
\ker\mathcal G_{n:m}^{\mathrm{resp}}
=
\bigcap_{k=m}^{n-1}
\ker\!\left(R_k^{1/2}B_{k:m}\right).}
\tag{TR12}
$$

In finite dimension, a trivial intersection gives a positive smallest
eigenvalue. In infinite dimension, injectivity alone is insufficient: the
range of $\mathcal O_{n:m}$ must be closed, or a uniform lower-frame constant
must be proved directly. This is the difference between algebraic
discernibility and a spectral gap.

For countably many stages the positive partial Gramians have a strong limit,
but an infinite-horizon floor need not occur on any uniformly bounded finite
horizon. The shift of a tail projection supplies the standard obstruction.
The Yang--Mills condition must therefore hold across a finite physical slab,
uniformly in the regulator, rather than only after an infinite number of
steps.

## The analysis map is forced to be bounded

The bounded transform is not cosmetic. Because $A_k$ is a contraction,

$$
0\leq D_k=I-A_k^*A_k\leq I.
\tag{TR12a}
$$

If a densely defined map $L_k$ satisfies the form inequality
$L_k^*L_k\leq D_k$ on a dense domain, then
$\|L_kx\|\leq\|x\|$ there, so $L_k$ extends uniquely to an everywhere
defined bounded contraction. A raw unbounded gradient, differential,
precision square root, or Dirac-type operator therefore cannot be the
analysis map in (TR4). It must first be normalized and boundedly transformed.

## A bounded response comes from an unbounded geometry

Let $G_k\geq0$ be self-adjoint on $\mathcal K_k$. It may be unbounded. For a
declared dimensionless response depth $\tau_k>0$, functional calculus gives

$$
R_k
:=
I-e^{-\tau_kG_k},
\qquad
0\leq R_k\leq I,
\qquad
\ker R_k=\ker G_k.
\tag{TR13}
$$

The bounded transform preserves exactly which directions the geometry fails
to distinguish while removing a domain mismatch with bounded transfer. The
parameter $\tau_k$ is not clock time merely because it occurs in an
exponential. It is a response-resolution parameter until an independent
physical identification says otherwise.

At this point the missing analysis map in the transfer-cocycle programme is
no longer formal:

$$
\boxed{
L_k
=
\sqrt{\eta_k}
\left(I-e^{-\tau_kG_k}\right)^{1/2}.}
\tag{TR14}
$$

The real work is not taking this square root. It is deriving $G_k$ and
$\eta_k$ without reading the unknown transfer edge backward, and proving
(TR11) uniformly on the complete physical carrier.

The heat defect is not the only safe transform. Any bounded Borel function
$f_k(G_k)$ with $f_k(0)=0$ and no further zeros may preserve the same
radical. [[contemporary-puzzles/yang-mills-mass-gap/resolvent-logistic-scale-transform|The
resolvent-logistic transform]] supplies the log-scale windows

$$
Q_N(\widehat G)
=(e^N\widehat G)^{1/2}(I+e^N\widehat G)^{-1},
\qquad \|Q_N\|\leq\tfrac12.
\tag{TR14a}
$$

It can replace $R_k^{1/2}$ if an independent inequality
$D_k\geq w_kQ_{N_k}(\widehat G_k)^2$ is proved. Its full log-scale Parseval
integral equals the support projection of $G_k$ and is generally too large
to assign to a single transfer stage. A window selection and its
normalization remain part of the physical construction. The exponential
response is primary here because it is itself the defect of a positive
contraction and interfaces directly with reversible kernels.

## Positive transfer converts the kernel comparison into the defect solder

The kernel-level estimates already available in the workspace normally have
the form $I-A_k\geq\eta_kR_k$, not (TR4). There is an exact bridge when the
stage is a positive self-adjoint transfer contraction on one carrier:

$$
0\leq A_k\leq I.
\tag{TR15}
$$

Functional calculus gives

$$
D_k
=I-A_k^2
=(I-A_k)+A_k(I-A_k)
\geq I-A_k.
\tag{TR16}
$$

Consequently,

$$
\boxed{
I-A_k\geq\eta_k
\left(I-e^{-\tau_kG_k}\right)
\quad\Longrightarrow\quad
D_k\geq L_k^*L_k,}
\tag{TR17}
$$

with $L_k$ given by (TR14). This is the desired noncircular route from a
bounded geometric response to the transported defect frame.

No commutation between $A_k$ and $R_k$ is used. In particular, one must not
square $A_k\leq I-\eta_kR_k$: squaring is not operator monotone. The safe
argument is exactly (TR16). The solder implies only

$$
\ker(I-A_k)\subseteq\ker R_k=\ker G_k;
\tag{TR17a}
$$

the response may miss directions that transfer nevertheless attenuates.

Positivity in (TR15) is a same-carrier statement. A rectangular map between
changing carriers is neither self-adjoint nor positive. One may apply
(TR17) only after independently supplied unitary identifications have put
that stage on one carrier and positivity has been proved there. Without such
identifications, the general theorem remains valid with the direct
source-carrier comparison (TR4).

## Complementary blind responses can force a joint gap

On a two-dimensional nonvacuum carrier, take

$$
A_0=\operatorname{diag}(1,r),
\qquad
A_1=\operatorname{diag}(r,1),
\qquad
0<r<1,
\tag{TR18}
$$

and let

$$
G_0=\operatorname{diag}(0,g),
\qquad
G_1=\operatorname{diag}(g,0),
\qquad g>0.
\tag{TR19}
$$

Writing $\rho=1-e^{-\tau g}$ and
$\eta=(1-r)/\rho$, one has

$$
I-A_k=\eta\left(I-e^{-\tau G_k}\right).
\tag{TR20}
$$

Each $A_k$ has norm one. Each $G_k$ has a nonvacuum zero mode. Yet, with
$B_0=I$ and $B_1=A_0$,

$$
\mathcal G_{2:0}^{\mathrm{resp}}
=
\eta R_0+A_0^*\eta R_1A_0
=(1-r)I.
\tag{TR21}
$$

Thus (TR11) proves

$$
\|A_1A_0\|\leq\sqrt r<1,
\tag{TR22}
$$

while direct multiplication gives the sharper value
$\|A_1A_0\|=r$. The response certificate is deliberately weaker than the
full defect: its positive residual is $r(1-r)I$, and (TR7) restores the exact
total defect $(1-r^2)I$. The example proves the logical point without
pretending that the geometric response exhausts all transfer loss.

This is the finite algebraic form of the reversal tactic. One does not ask
one locally smooth stage to contain a gap. One asks whether differently
oriented responses, transported through the whole ordered relation, leave
any normalized distinction invisible throughout the slab.

## Four noncircular sources for the response

### A joint correspondence residual

The most Copernican source begins with a whole relation rather than an
endpoint operator. Let

$$
J_k^-:\mathcal K_k\longrightarrow\mathscr K_k,
\qquad
J_k^+:\mathcal K_{k+1}\longrightarrow\mathscr K_k
\tag{TR22a}
$$

be isometries of two local carriers into one joint two-slice carrier. Define

$$
A_k:=(J_k^+)^*J_k^-:
\mathcal K_k\longrightarrow\mathcal K_{k+1},
\qquad
L_k:=(I-J_k^+(J_k^+)^*)J_k^-.
\tag{TR22b}
$$

Then

$$
\boxed{
I-A_k^*A_k=L_k^*L_k.}
\tag{TR22c}
$$

The proof is one line:

$$
L_k^*L_k
=(J_k^-)^*(I-J_k^+(J_k^+)^*)J_k^-
=I-A_k^*A_k.
$$

Here $L_kx$ is literally the part of the first local presentation that the
second local subspace cannot carry inside the joint whole. This is an exact
residue, not a metaphor and not a random variable. It sets $S_k=0$ in
(TR7).

[[two-slice-innovation-geometry/inq|Two-Slice Innovation Geometry]] gives
the commutative conditional-transport instance, while
[[contemporary-puzzles/yang-mills-mass-gap/past-future-angle-and-the-transfer-gap#The noncommutative lift|the
Stinespring correspondence]] gives a Type-III-compatible completely
positive instance. A bare scale correspondence does not yet supply the
isometries, their pointed states, or a physical endpoint transfer. Those
must come from an expectation, Q-system with chosen standard solution,
normal UCP map, or another independently specified joint construction.

This exact route and the bounded-response route answer different questions.
The correspondence residual derives $A_k$ and $L_k$ together from one
whole carrier. Equations (TR13)--(TR17) instead compare an already physical
transfer with an independently constructed geometry. The first is more
economical when its whole relation is available; the second is the required
firewall when the physical transfer and geometric response have distinct
origins.

### A reversible two-slice kernel

Suppose a ground-state-transformed physical transfer $A_k$ and an auxiliary
reversible response kernel $Q_k=e^{-\tau_kG_k}$ act on the same
$L^2$ carrier. [[markov-edge-measure-solder/inq|The edge-measure solder]]
gives an action-level sufficient condition for

$$
I-A_k\geq\eta_k(I-Q_k)
=\eta_k\left(I-e^{-\tau_kG_k}\right).
\tag{TR23}
$$

It compares stationary two-slice conductance, not merely a one-slice vacuum
density. Tensor formation, gauge restriction, and deterministic blocking
preserve a comparison already proved. They do not create it or lift it back
through forgotten fibres.

The pure product-Wilson calculation in
[[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder|Finite-Spacing
Transfer and the Bounded Flux Solder]] is an exact regulated example. Its
interacting-vacuum and continuum-uniform extension is still open.

### A conditional-expectation disagreement

For an orthogonal conditional expectation $E_k$, the projection

$$
G_k=I-E_k
\tag{TR24}
$$

charges precisely the distinctions discarded by that presentation, and

$$
I-e^{-\tau_kG_k}
=(1-e^{-\tau_k})(I-E_k).
\tag{TR25}
$$

Families of expectations can have complementary kernels, as in
[[contemporary-puzzles/yang-mills-mass-gap/two-expectation-angle-process|the
two-expectation angle process]]. But $E_k$ itself is noninjective and cannot
be a finite-thickness physical transfer of the form $e^{-\ell H}$. It is an
auxiliary response operator. The physical content begins only after an
independent comparison of the strictly positive transfer defect with
$I-E_k$.

### A flux form or Hessian

A closed densely defined nonnegative form on the actual complex Hilbert
carrier determines a positive self-adjoint $G_k$ and hence (TR13). Electric
flux Dirichlet forms provide one such regulated carrier in
[[contemporary-puzzles/yang-mills-mass-gap/gauge-descent-flux-fisher-coercivity|Gauge-Descended
Flux Coercivity]].

A parameter Hessian does not automatically do so. It is naturally a map
$T_\lambda M\to T_\lambda^*M$. Before it can enter (TR13), one must supply:

- a map from the complete physical vacuum complement into the tangent
  carrier;
- a source inner product or Riesz identification;
- a closed positive Hermitian extension on the complex carrier; and
- normalization stable under changes of parameter coordinates.

[[measured-response-carriers/inq|Measured Response Carriers]] proves the
pullback-radical and finite-rank obstructions. A finite family of
finite-dimensional Hessian readouts cannot cover an unrestricted
infinite-dimensional physical carrier. The transported family may solve a
stagewise kernel problem, but it does not evade the need for a uniform
infinite-dimensional lower frame.

## The whole/local reversal without a unitarity equivocation

The Copernican order is

$$
\text{whole relation}
\longrightarrow
\text{nonfaithful formation or selected response carrier}
\longrightarrow
\text{positive Euclidean transfer}
\longrightarrow
\text{Lorentzian clock group}.
\tag{TR26}
$$

These arrows are not four descriptions of one map. A quotient, conditional
expectation, or response radical may forget distinctions. The transfer
$A_k$ attenuates norm but may remain injective. A later unitary group
$e^{-itH/\hbar}$ preserves the reconstructed physical inner product.

Accordingly, “the whole is not unitary so that the local can appear
unitary” has a precise surviving form. Unitarity is not a well-typed
predicate of a whole-to-local diagram before one carrier and one
endomorphism have been selected. A nonfaithful formation can select a
quotient response form; transformations stabilizing its radical then act
unitarily on the quotient completion, as proved in
[[algebra/quotient-unitarity-and-kernel-stabilization|Quotient Unitarity and
Kernel Stabilization]]. Separately, Osterwalder--Schrader reconstruction can
turn a positive transfer generator into a Lorentzian unitary clock group.

[[directed-isometric-residue-completion/inq|A third exact construction]]
retains rather than forgets: every declared contraction has a minimal
isometric column consisting of its endpoint and defect output. Any soldered
response here factors contractively through that canonical defect carrier.
For a stationary reconstructed generator, the residue completion and the
Lorentzian clock obey an exact intertwiner on survivor-plus-residue output.
This proves compatibility of a proper completion with unitary clock dynamics;
it neither turns the defect output into a record nor says that loss causes
unitarity.

What cannot be claimed is that faithful lossy compression manufactures an
exact unitary: a unitary compression of a contraction is already a reducing
noiseless sector. Nor does strict categorical descent necessarily forget;
effective descent may glue without losing anything. The loss must be typed
as a quotient, expectation, instrument, radical, or other nonfaithful
realization. [[conservation-of-causal-charge/unitarity-and-ontological-time|Why
Unitarity Is Not the Wall Symmetry]] owns this separation.

The response ledger nevertheless expresses the important asymmetry. The
local clock can obey reversible conservation laws on its reconstructed
carrier while the ordered formation-and-transfer diagram is not itself a
unitary group on that carrier. Symmetry is then the stabilizer grammar of
what survived the wall, not a symmetry assumed of the entire prior
structure.

## Fixed-slab rate, energy, and mass

Assign positive physical thicknesses $\ell_k$ and consider a nonempty family
of products with one fixed total thickness $\ell_*>0$. Suppose the response
Gramian has the uniform floor

$$
\inf_{(m,n)\in\mathcal I_{\ell_*}}
\inf_{\|x\|=1}
\left\langle x,
\mathcal G_{n:m}^{\mathrm{resp}}x
\right\rangle
\geq\kappa_*,
\qquad
0<\kappa_*<1.
\tag{TR27}
$$

Then every complete nonvacuum product obeys

$$
\|B_{n:m}\|\leq q_*:=\sqrt{1-\kappa_*}<1,
\tag{TR28}
$$

and the certified inverse-length attenuation rate is

$$
\boxed{
\gamma_{\mathrm{resp}}
:=
-\frac{1}{\ell_*}\log q_*
=
-\frac{1}{2\ell_*}\log(1-\kappa_*)>0.}
\tag{TR29}
$$

This is a rate at which every normalized initial distinction must pay
geometrically witnessed transfer defect across the slab. It contains no
mass and no $\hbar$.

Only if an independently constructed unitary identification with the
vacuum-reduced Osterwalder--Schrader transfer proves

$$
B_{n:m}
\simeq
e^{-\ell_*(H-E_0)/(\hbar c)}(I-P_0)
\tag{TR30}
$$

does functional calculus give

$$
\Delta_E
\geq
\hbar c\,\gamma_{\mathrm{resp}}.
\tag{TR31}
$$

Only after positive-energy Poincare reconstruction identifies the rest-frame
spectral threshold does this become

$$
m_{\mathrm{gap}}
\geq
\frac{\hbar}{c}\gamma_{\mathrm{resp}}.
\tag{TR32}
$$

Thus $\hbar$ converts a reconstructed inverse clock duration to energy; it
does not generate the pre-clock response. The physical slab scale and the
dimensionless floor must arise upstream.

## The Yang--Mills stopping condition

For a regulator indexed by lattice spacing $a$, spatial volume $L$, and
admissible boundary condition $b$, a whole-first route may directly supply
pointed joint carriers and pairs $(A_{a,L,b,k},L_{a,L,b,k})$ satisfying
(TR22c). The independent-response route instead seeks a family

$$
(A_{a,L,b,k},G_{a,L,b,k},\eta_{a,L,b,k},\tau_{a,L,b,k})
\tag{TR33}
$$

on the complete gauge-invariant vacuum complement, including its
[[vacuum-aligned-innovation-completion/inq|vacuum-balance sector]], such
that:

1. the $A$ stages are the actual normalized reflection-positive transfer,
   or are unitarily identified with it;
2. every $L$ is either the exact residual of an independently constructed
   pointed joint correspondence, or every $G$ is derived from flux,
   boundary, expectation, Hessian, or descent geometry independently of the
   unknown nonvacuum transfer spectrum;
3. the same-carrier solder (TR4) or the positive-transfer precursor (TR17)
   holds with controlled normalization;
4. the fixed-physical-slab Gramian in (TR27) has one lower bound
   $\kappa_*>0$ uniform in $a,L,b$; and
5. the carriers, vacua, transfer products, and Poincare action survive the
   continuum limit.

Items 2--4 are the central analytic problem. Stagewise coercivity is not
required. The transported response must collectively cover every physical
direction.

The following failures kill the proposed inference:

- defining $G_k$, $R_k$, or $\eta_k$ from the desired spectral gap;
- calling a real parameter Hessian an operator on the physical complex
  carrier without a realization and Riesz theorem;
- using a noninjective expectation as finite-thickness Euclidean transfer;
- replacing a uniform lower frame by a merely trivial algebraic kernel;
- obtaining coverage only at infinite horizon rather than uniformly on a
  finite physical slab;
- omitting vacuum-balance or boundary-charge directions from the carrier;
- proving the comparison at one regulator while its coefficient vanishes
  at fixed physical thickness in the continuum limit;
- naming $\tau_k$ clock time, $\gamma_{\mathrm{resp}}$ energy, or an energy
  floor mass before the corresponding reconstruction; or
- claiming that descent itself forgets when the actual gluing functor is
  faithful.

## Receipt and dependencies

[[transported-response-observability-solder/receipts/transported_response_solder_receipt.py|The
finite receipt]] checks the exact joint-correspondence residual, two positive
stages that are separately gapless,
two complementary response generators with nonvacuum kernels, the bounded
solder, the transported Gramian, the positive unsoldered residual, and the
exact three-term ledger.
[[transported-response-observability-solder/receipts/transported-response-solder-receipt-output.txt|The
stored output]] records the constants.

[[vacuum-aligned-transfer-cocycle/inq|The Vacuum-Aligned Transfer Cocycle]]
supplies the changing-carrier defect identity.
[[directed-isometric-residue-completion/inq|Directed Isometric Residue
Completion]] assembles the survival, response, and residual coordinates into
one proper norm-preserving causal column.
[[two-slice-innovation-geometry/inq|Two-Slice Innovation Geometry]] supplies
the exact joint-carrier residual construction.
[[markov-edge-measure-solder/inq|Markov Edge-Measure Solder]] supplies an
action-derived route to the kernel comparison.
[[measured-response-carriers/inq|Measured Response Carriers]] supplies the
response-carrier and Hessian typing rules.
[[gauge-cycle-innovation-filtration/inq|Gauge-Cycle Innovation Filtration]]
supplies a complete regulated gauge distinction family; its expectations
are analyses rather than physical transfer.
[[contemporary-puzzles/yang-mills-mass-gap/mass-as-casimir-and-realization|Mass
as Casimir and Realization]] owns the final energy-to-mass step.

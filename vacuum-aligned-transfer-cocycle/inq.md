---
inq.module: "vacuum-aligned-transfer-cocycle"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Vacuum-Aligned Transfer Cocycle

A chain of pointed Hilbert carriers has an exact operator-valued composition law, while the matrix of observable block norms is only a submultiplicative shadow of that law. For contractive stages, the surviving squared norm plus all transported stage defects obeys an exact telescoping ledger, so joint contraction is precisely a lower-frame condition for what the stages collectively detect. The scalar shadow forgets direction, phase, and cancellation, and an intermediate visible compression acquires a leave-and-return memory term from the discarded carrier. Complementary stages can therefore each be gapless while their ordered product contracts the complete vacuum complement. This yields a changing-carrier stopping theorem without assuming a global unitary clock; it becomes an energy or mass gap only after an independent Euclidean-transfer and Poincare reconstruction theorem.

**Status: [EXACT] for the centered carrier cocycle, countable block-majorant theorem, lax-composition defect, transported defect-frame identity, complementary-stage example, compression-memory identity, standard-form realignment obstruction, and fixed-slab implication; [INTERPRETATION] for scalarization as observable forgetting; [OPEN] for the Yang--Mills block bounds, physical scale correspondence, Type-III boundary realization, continuum transport, and Poincare-Casimir solder.**

## Pointed carriers, not one silently fixed Hilbert space

Let

$$
(\mathcal H_k,\Omega_k),
\qquad
\|\Omega_k\|=1,
\qquad
\Pi_k:=I-P_{\Omega_k},
\qquad
\mathcal H_k^0:=\Omega_k^\perp
\tag{VC1}
$$

be a finite or countable sequence of pointed Hilbert spaces. On every
vacuum complement choose a finite or countable complete orthogonal
resolution

$$
\Pi_k
=
\sum_{a\in I_k}^{\mathrm s}Q_a^{(k)}.
\tag{VC2}
$$

For the gauge carrier, the family must contain both the internally centered
charge-and-innovation blocks and the vacuum-balance block constructed in
[[vacuum-aligned-innovation-completion/inq|Vacuum-Aligned Innovation
Completion]]. The label sets may change with the scale, cut, state, or
regulator.

Let

$$
P_k:\mathcal H_k\longrightarrow\mathcal H_{k+1}
\tag{VC3}
$$

be bounded and satisfy $P_k\Omega_k=\Omega_{k+1}$. Its centered compression
is

$$
A_k:=\Pi_{k+1}P_k\Pi_k.
\tag{VC4}
$$

Forward vacuum preservation already gives the exact composition law

$$
\boxed{
A_{n:m}
:=
A_{n-1}\cdots A_m
=
\Pi_nP_{n-1}\cdots P_m\Pi_m.}
\tag{VC5}
$$

Indeed,
$\Pi_{k+1}P_kP_{\Omega_k}=0$, so every intermediate $\Pi_k$ may be inserted
without changing the final centered compression. This is an exact cocycle
of rectangular operators between changing carriers.

If also

$$
P_k^*\Omega_{k+1}=\Omega_k,
\tag{VC6}
$$

then $P_k\mathcal H_k^0\subseteq\mathcal H_{k+1}^0$, and $A_k$ is the
literal restriction of $P_k$ to the vacuum complement. Condition (VC6) is
automatic when $P_k$ is a contraction: equality
$\|P_k\Omega_k\|=\|\Omega_k\|$ forces
$P_k^*P_k\Omega_k=\Omega_k$. Without (VC6), one must say centered
compression rather than centered restriction. The matrix

$$
P=
\begin{pmatrix}
1&1\\
0&0
\end{pmatrix},
\qquad
\Omega=e_1,
\tag{VC7}
$$

is the minimal warning: it fixes $\Omega$ forward but sends the other basis
vector into the vacuum line.

No global unitary group has been assumed. The $P_k$ may be transfer maps,
scale correspondences after Hilbert realization, or declared comparison
arrows. Calling them one evolution before that role has been constructed
would already confuse the category of the whole with the category of a
local clock.

## The block-norm shadow is a lax cocycle

Choose nonnegative numbers

$$
c_{ab}^{(k)}
\geq
\left\|
Q_a^{(k+1)}P_kQ_b^{(k)}
\right\|
\tag{VC8}
$$

and let $C_k=(c_{ab}^{(k)})$. In the countable case require that

$$
C_k:\ell^2(I_k)\longrightarrow\ell^2(I_{k+1})
\tag{VC9}
$$

be bounded. This is an independent hypothesis: boundedness of $P_k$ does
not imply boundedness of the matrix of its block norms.

For $x\in\mathcal H_k^0$, define its block-magnitude vector by

$$
r_k(x)_b:=\|Q_b^{(k)}x\|.
\tag{VC10}
$$

Orthogonality gives $\|r_k(x)\|_2=\|x\|$, and the triangle inequality gives
the componentwise relation

$$
\boxed{
r_{k+1}(A_kx)
\leq
C_kr_k(x).}
\tag{VC11}
$$

Iteration proves

$$
r_n(A_{n:m}x)
\leq
C_{n-1}\cdots C_mr_m(x)
\tag{VC12}
$$

and therefore

$$
\boxed{
\|A_{n:m}\|
\leq
\|C_{n-1}\cdots C_m\|_{2\to2}
\leq
\prod_{k=m}^{n-1}\|C_k\|_{2\to2}.}
\tag{VC13}
$$

Taking $x$ in one initial block also gives the endpoint-block theorem

$$
\boxed{
\left\|
Q_a^{(n)}P_{n-1}\cdots P_mQ_b^{(m)}
\right\|
\leq
\left(C_{n-1}\cdots C_m\right)_{ab}.}
\tag{VC14}
$$

For countable families and each finite chain $m<n$, the path expansion is
absolutely convergent in operator norm for every fixed pair of endpoint
blocks because the
corresponding nonnegative matrix-product entry is finite. Strong
completeness of the $Q_a^{(k)}$ alone would not be enough: coordinate
partial sums converge strongly to the identity on $\ell^2$, while the norm
of every omitted tail is still one.

Let $\mathscr B(P)$ denote the minimal matrix of exact centered block norms.
For two composable forward-vacuum-preserving arrows between pointed
carriers,

$$
\boxed{
\mathscr B(RP)
\leq
\mathscr B(R)\mathscr B(P)}
\qquad
\text{entrywise}.
\tag{VC15}
$$

The operator arrows compose exactly; their scalar norm shadow composes only
laxly. In categorical language, $\mathscr B$ is an order-enriched lax
functor wherever its countable matrices are bounded. It forgets the
directions on which block norms are attained, complex phases, and
interference among intermediate paths.

The entrywise nonnegative slack

$$
\mathfrak F(R,P)
:=
\mathscr B(R)\mathscr B(P)-\mathscr B(RP)
\tag{VC16}
$$

is therefore an exact scalarization defect. It is not an additive cocycle,
an entropy, a physical charge, or a mass. For the normalized Walsh matrix

$$
W
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
W^2=I,
\tag{VC17}
$$

with coordinate blocks,

$$
\mathscr B(W)=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
\mathscr B(W)^2=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
\mathscr B(W^2)=I.
\tag{VC18}
$$

The off-diagonal paths cancel in the exact whole operator and survive in
the scalar shadow. This is a rigorous instance in which the whole is more
determinate than its coarse presentation.

The countable hypothesis has real force. A direct sum of normalized Walsh
matrices of orders $2^r$ is unitary, while its coordinate block-norm matrix
is the direct sum of $2^{-r/2}J_{2^r}$ and has norms $2^{r/2}$. No bounded
$\ell^2$ majorant exists. A continuum proof must establish a Schur-type or
weighted estimate rather than cite boundedness of the physical transfer.

## Complementary descents can be jointly coercive

A one-step stopping condition is stronger than necessary. On a
two-dimensional centered carrier, let

$$
A_0=
\begin{pmatrix}
1&0\\
0&r
\end{pmatrix},
\qquad
A_1=
\begin{pmatrix}
r&0\\
0&1
\end{pmatrix},
\qquad
0<r<1.
\tag{VC19}
$$

Each stage has norm one and leaves a nonvacuum direction fixed. Nevertheless

$$
\boxed{
A_1A_0=rI,
\qquad
\|A_1A_0\|=r<1.}
\tag{VC20}
$$

The two stages are complementary: the direction missed by one is charged
by the other. This is the multiplicative counterpart of a joint-frame or
paired-wall lower bound. It also gives a precise version of the earlier
causal-generator clue: an individual directional generator may be
gapless, while a joint invariant of complementary directions has a positive
floor.

Once each arrow has been assigned a declared positive physical thickness
$\ell_k>0$, put

$$
\ell_{n:m}:=\sum_{k=m}^{n-1}\ell_k.
\tag{VC20a}
$$

For the exact fixed-slab statement, declare a nonempty admissible set

$$
\mathcal I_{\ell_*}
:=
\{(m,n):m<n,\ \ell_{n:m}=\ell_*\}
\neq\varnothing.
\tag{VC20b}
$$

The correct nonstationary certificate is consequently the ordered product

$$
M_{n:m}:=C_{n-1}\cdots C_m,
\qquad
\sup_{(m,n)\in\mathcal I_{\ell_*}}
\|M_{n:m}\|_{2\to2}
\leq q_*<1.
\tag{VC21}
$$

Applying a Schur estimate directly to $M_{n:m}$ may be much sharper than
multiplying one-step Schur bounds. Individual spectral radii are
insufficient: $E_{12}$ and $E_{21}$ each have spectral radius zero, while
$(E_{21}E_{12})^N=E_{22}$ has norm one.

If a regulator partition does not hit $\ell_*$ exactly, it must instead
declare a nonempty slab window or a sequence of products whose total
thickness converges to $\ell_*$. The approximation and its uniformity then
become additional hypotheses; the empty supremum is never a certificate.
[[strong-coupling-gap-and-continuum-crossover/inq|Strong-Coupling Gap and
Continuum Crossover]] owns the corresponding fixed-slab regulator logic.

For a nonnegative rectangular matrix, the ordinary Schur test gives

$$
R:=\sup_a\sum_b c_{ab},
\qquad
S:=\sup_b\sum_a c_{ab},
\qquad
\|C\|_2\leq\sqrt{RS}.
\tag{VC22}
$$

Weighted Schur tests are available when the channel populations are highly
unequal. A diagonal/off-diagonal split across changing label sets requires
an explicit matching of labels; there is no canonical diagonal between
different decompositions.

## The exact defect ledger is a transported frame

Suppose now that every centered arrow $A_k$ is a contraction. Define

$$
B_{k:m}
:=
\begin{cases}
I_{\mathcal H_m^0},&k=m,\\
A_{k-1}\cdots A_m,&k>m,
\end{cases}
\qquad
D_k:=I_{\mathcal H_k^0}-A_k^*A_k\geq0.
\tag{VC22a}
$$

The adjacent difference

$$
B_{k:m}^*B_{k:m}
-
B_{k+1:m}^*B_{k+1:m}
=
B_{k:m}^*D_kB_{k:m}
\tag{VC22b}
$$

telescopes. Therefore

$$
\boxed{
I_{\mathcal H_m^0}
-
B_{n:m}^*B_{n:m}
=
\sum_{k=m}^{n-1}
B_{k:m}^*D_kB_{k:m}.}
\tag{VC22c}
$$

Equivalently, for every initial nonvacuum vector $x$,

$$
\boxed{
\|x\|^2
=
\|B_{n:m}x\|^2
+
\sum_{k=m}^{n-1}
\left\|
D_k^{1/2}B_{k:m}x
\right\|^2.}
\tag{VC22d}
$$

This is an exact Hilbert-norm ledger. The stage defect $D_k$ operates on the
current carrier $\mathcal H_k^0$; composition pulls it back to the initial
carrier before the costs can be added. Nothing random has been introduced.
The sum is not a conserved physical charge unless a separate physical
interpretation of the norm and arrows is proved.

Define the transported defect analysis operator

$$
\mathcal W_{n:m}x
:=
\left(
D_k^{1/2}B_{k:m}x
\right)_{k=m}^{n-1}
\in
\widehat\bigoplus_{k=m}^{n-1}\mathcal H_k^0.
\tag{VC22e}
$$

Then

$$
\mathcal W_{n:m}^*\mathcal W_{n:m}
=
I-B_{n:m}^*B_{n:m},
\tag{VC22f}
$$

and, for $0\leq\kappa\leq1$,

$$
\boxed{
\mathcal W_{n:m}^*\mathcal W_{n:m}
\geq\kappa I
\quad\Longleftrightarrow\quad
\|B_{n:m}\|
\leq\sqrt{1-\kappa}.}
\tag{VC22g}
$$

Thus joint attenuation is exactly a lower-frame or observability inequality:
the transported stage defects must collectively see every initial
nonvacuum direction with a uniform floor. Each $D_k$ may have a large
kernel. In finite dimension, a trivial common kernel of the transported
analysis maps gives a positive floor; in infinite dimension, injective
coverage is insufficient and closed range or an explicit lower-frame
constant is required.

For the complementary example (VC19),

$$
D_0=
\begin{pmatrix}
0&0\\
0&1-r^2
\end{pmatrix},
\qquad
A_0^*D_1A_0=
\begin{pmatrix}
1-r^2&0\\
0&0
\end{pmatrix},
\tag{VC22h}
$$

so their transported sum is $(1-r^2)I$ and (VC22g) recovers
$\|A_1A_0\|=r$ exactly.

This suggests a noncircular theorem target for the geometric programme.
Construct independently normalized bounded response maps

$$
L_k:\mathcal H_k^0\longrightarrow\mathcal Y_k
\tag{VC22i}
$$

from wall Hessians, fluxes, or boundary data, and prove on the actual
physical transfer carrier that

$$
D_k\geq L_k^*L_k.
\tag{VC22j}
$$

If the transported family has the lower-frame bound

$$
\sum_{k=m}^{n-1}
\|L_kB_{k:m}x\|^2
\geq
\kappa\|x\|^2,
\tag{VC22k}
$$

then (VC22c) gives
$\|B_{n:m}\|\leq\sqrt{1-\kappa}$. Defining $L_k$ from
$D_k$ or from the desired Hamiltonian would be circular; the advance is
only real when (VC22j) is a separately derived same-carrier comparison.

There is one exact whole-first realization. If two endpoint carriers embed
isometrically as $J_k^-,J_k^+$ in a joint correspondence, then

$$
A_k=(J_k^+)^*J_k^- ,
\qquad
L_k=(I-J_k^+(J_k^+)^*)J_k^- ,
\qquad
I-A_k^*A_k=L_k^*L_k.
$$

The residue is the component of one endpoint presentation orthogonal to the
other inside the joint carrier. This is noncircular when the correspondence,
isometries, and pointing are independently constructed; identifying its
compression with physical Yang--Mills transfer remains a separate theorem.

[[transported-response-observability-solder/inq|Transported Response
Observability Solder]] now supplies one explicit, independently typable
choice. If a positive stage obeys

$$
I-A_k\geq\eta_k(I-e^{-\tau_kG_k}),
$$

for a geometry-derived $G_k\geq0$, then
$I-A_k^2\geq I-A_k$ and hence

$$
L_k=\sqrt{\eta_k}(I-e^{-\tau_kG_k})^{1/2}
$$

satisfies (VC22j). Its transported Gramian may have a uniform floor even
when every $G_k$ has a nonvacuum kernel. The theorem also retains the exact
positive residual $D_k-L_k^*L_k$, so a response certificate is not silently
identified with the whole transfer defect.

[[directed-isometric-residue-completion/inq|Directed Isometric Residue
Completion]] packages the same ledger as a universal minimal completion of
the declared transfer. The column consisting of the survivor and every
transported defect is an isometry; it is onto exactly when all minimal stage
columns are coisometric. For a stationary positive transfer, its Schäffer
dilation separates a unitary Wold part from a pure shift part, but pure shift
and pointwise fading do not imply a gap. The missing quantitative predicate
remains (VC22k) on a finite physical slab. Under $L_k^*L_k\leq D_k$, Douglas
factorization also shows that each selected response is a contractive
readout of the canonical stage-defect carrier.

## Forgetting an intermediate carrier produces exact memory

Let

$$
U_k:\mathcal K_k\longrightarrow\mathcal H_k
\tag{VC23}
$$

be isometries selecting visible subspaces, and put
$E_k=U_kU_k^*$ and $F_k=I-E_k$. Define the one-step visible compressions

$$
\widehat P_k:=U_{k+1}^*P_kU_k.
\tag{VC24}
$$

For two steps there is an exact identity

$$
\boxed{
U_2^*P_1P_0U_0
=
\widehat P_1\widehat P_0
+
U_2^*P_1F_1P_0U_0.}
\tag{VC25}
$$

The last term is the leave-and-return residue. It vanishes if the incoming
map never leaves the retained intermediate carrier, if the discarded
carrier cannot return to the final readout, or by a special cancellation.
Otherwise the compressed arrows fail the memoryless
Chapman--Kolmogorov composition law. No positivity or unitality has been
assumed that would by itself make them Markov operators.

For one self-adjoint transfer $T$ and one fixed visible projection $E$,

$$
\boxed{
ET^2E
=
(ETE)^2
+
ETFTE
=
(ETE)^2+(FTE)^*(FTE).}
\tag{VC26}
$$

The memory residue is then positive. This is the two-step core of the
projection-operator mechanism developed by
[[library/transport-collective-motion-and-brownian-motion/inq|Mori]]: exact
whole dynamics becomes a visible equation with orthogonal dynamics and
memory after projection. A later stochastic approximation is one possible
presentation of unresolved variables; neither (VC25) nor Mori's exact
projection identity entails stochastic ontology.

There is a useful rigidity firewall. If $T$ is a contraction and
$U^*TU$ is unitary, then $U\mathcal K$ reduces $T$ and there is no leakage
between it and its orthogonal complement. Indeed,

$$
\|\xi\|
=
\|U^*TU\xi\|
\leq
\|TU\xi\|
\leq
\|\xi\|,
\tag{VC26a}
$$

so equality forces $TU\xi\in U\mathcal K$; applying the same argument to
$T^*$ gives reduction. Thus an exactly unitary local
clock cannot be an accidental compression of a genuinely leaking
contractive whole. It must instead be a reducing noiseless sector, a
quotient flow, or a separately reconstructed Lorentzian group. The exact
quotient mechanism is proved in
[[algebra/quotient-unitarity-and-kernel-stabilization|Quotient Unitarity and
Kernel Stabilization]].

## A state change requires vacuum realignment

The pointed decompositions at two scales must not be identified by a fake
state-changing unitary. Here one adds structure not present in (VC1): let
each relevant carrier be a specified standard form
$(M_s,\mathcal H_s,J_s,\mathcal P_s)$, let $\varphi_s$ be faithful and
normal, and require $\Omega_s=\xi_{\varphi_s}\in\mathcal P_s$. Haagerup's
standard-form theorem says that a normal $*$-isomorphism

$$
\alpha_{t:s}:M_s\longrightarrow M_t
\tag{VC27}
$$

has a unique unitary implementation $U_{t:s}$ preserving the standard cones
and modular conjugations. It sends the natural-cone vector of
$\varphi_s$ to

$$
U_{t:s}\xi_{\varphi_s}
=
\xi_{\varphi_s\circ\alpha_{t:s}^{-1}}.
\tag{VC28}
$$

It equals the separately chosen target vector $\xi_{\varphi_t}$ only when
$\varphi_t=\varphi_s\circ\alpha_{t:s}^{-1}$. The unitary can transport raw channel
projections, but a changed target state requires the vacuum-aligned
rank-one corrections and balance sector to be recomputed.

Real Connes cocycles do not evade this obstruction. In the Hilbert--Schmidt
standard form of $M_2$, take

$$
\rho_\psi=\frac12I,
\qquad
\rho_\varphi=
\begin{pmatrix}
p&0\\
0&1-p
\end{pmatrix},
\qquad
0<p<1,
\qquad
p\neq\frac12.
\tag{VC29}
$$

Then

$$
\xi_\psi=\frac1{\sqrt2}I,
\qquad
\xi_\varphi=
\begin{pmatrix}
\sqrt p&0\\
0&\sqrt{1-p}
\end{pmatrix},
\tag{VC30}
$$

while every real-time cocycle

$$
[D\varphi:D\psi]_t
=
\rho_\varphi^{it}\rho_\psi^{-it}
\tag{VC31}
$$

is unitary and leaves the two diagonal moduli of
$[D\varphi:D\psi]_t\xi_\psi$ equal to $1/\sqrt2$. It cannot produce
$\xi_\varphi$. The nonunitary half-density
$\rho_\varphi^{1/2}\rho_\psi^{-1/2}$ does map $\xi_\psi$ to
$\xi_\varphi$ here; it is the finite-dimensional Radon--Nikodym amplitude,
not a real modular-time unitary.

The exact two-stage rule is therefore:

$$
\boxed{
\text{transport raw carrier data by a genuine standard-form unitary;}
\quad
\text{then realign the block resolution to the target pointed state}.}
\tag{VC32}
$$

The target Connes cocycle records the residual modular state mismatch; it
does not provide one universal unitary that changes both carrier and
pointing. This is why (VC1)--(VC14) allow independently pointed carriers at
every stage.

There is nevertheless an exact nonunitary pointed cocycle under a bounded
domination hypothesis. For a composable family of the specified standard
forms, let $U_{t:s}:=U_{\alpha_{t:s}}$ and suppose the scale isomorphisms
compose as
$\alpha_{u:s}=\alpha_{u:t}\alpha_{t:s}$. Transport the source state to

$$
\widehat\varphi_{t:s}
:=
\varphi_s\circ\alpha_{t:s}^{-1}.
\tag{VC32a}
$$

For every real modular parameter $r$, the residual state cocycle

$$
c_{t:s}(r)
:=
[D\varphi_t:D\widehat\varphi_{t:s}]_r
\in\mathcal U(M_t)
\tag{VC32b}
$$

obeys, by Connes covariance and the state-label chain rule,

$$
\boxed{
c_{u:s}(r)
=
c_{u:t}(r)\,
\alpha_{u:t}\!\left(c_{t:s}(r)\right).}
\tag{VC32c}
$$

This is a genuine horizontal groupoid cocycle, but $r$ is a modular
parameter, not physical clock time, and the unitary $c_{t:s}(r)$ does not in
general carry the pushed natural-cone vector to the independently chosen
target vector. [[modular-cocycle-tomography/inq|Modular Cocycle Tomography]]
separates this modular comparison parameter from physical clock time.

If

$$
\varphi_t\leq C\,\widehat\varphi_{t:s},
\tag{VC32d}
$$

the bounded Araki Radon--Nikodym amplitude

$$
\mathsf R_{t:s}
:=
A(\varphi_t/\widehat\varphi_{t:s})
\tag{VC32e}
$$

exists and is unique. Araki's theorem gives, for $x\in M_t$,

$$
\mathsf R_{t:s}U_{t:s}\xi_{\varphi_s}
=
\xi_{\varphi_t},
\qquad
\varphi_t(x)
=
\widehat\varphi_{t:s}
\!\left(\mathsf R_{t:s}^*x\mathsf R_{t:s}\right),
\qquad
\|\mathsf R_{t:s}\|^2
=
\inf\{C:\varphi_t\leq C\widehat\varphi_{t:s}\}.
\tag{VC32f}
$$

Under the corresponding two-sided domination hypotheses on the faithful
states it is boundedly invertible on the full standard carrier, and Araki's
chain rule gives

$$
\mathsf R_{u:s}
=
\mathsf R_{u:t}\alpha_{u:t}(\mathsf R_{t:s}).
\tag{VC32g}
$$

Consequently

$$
T_{t:s}^{\mathrm{point}}
:=
\mathsf R_{t:s}U_{t:s}
\tag{VC32h}
$$

maps source pointing to target pointing and composes exactly. It is
generally nonunitary. If a raw orthogonal projection $E$ is transported by
the similarity $\mathsf R E\mathsf R^{-1}$, the result is orthogonal exactly
when

$$
[\mathsf R^*\mathsf R,E]=0.
\tag{VC32i}
$$

Thus even the strongest bounded pointed transport does not preserve an
arbitrary orthogonal channel resolution. It confirms rather than removes
the need to recompute the target vacuum-aligned resolution.

## The Copernican meaning of unitarity

The whole/local reversal is now type-correct. The pre-observable structure
may be a diagram of correspondences, quotients, and pointed transfer arrows
between different carriers. Such a diagram is not an endomorphism group on
one Hilbert space, so calling it unitary or nonunitary before choosing a
carrier is ill typed. Its exact predicate is composition.

After a nonfaithful realization has selected a quotient and positive form,
the stabilizer of the kernel can act unitarily on the quotient completion.
After Osterwalder--Schrader reconstruction, a positive Euclidean transfer
may yield a Lorentzian unitary group on a reconstructed fixed carrier.
Those local unitarities are compatible with directed, noninvertible
formation arrows because they are predicates of different arrows.

The word *because* also needs a firewall. Under faithful expected descent,
[[algebra/faithful-descent-rigidity-and-noiseless-unitarity|exact local
automorphisms identify an already invariant noiseless sector]]; forgetting
does not manufacture them. A genuinely new local unitary carrier therefore
requires a nonfaithful quotient, a separate reconstruction, or an explicitly
retained reversible component.

Strict [[basic-concepts/descent/inq|descent]] itself remains coherent gluing
and forgets nothing when it is effective and faithful. The loss enters only
through a declared quotient, expectation, instrument, compression, or
scalarization. This preserves the useful poetic clue without assigning
forgetfulness to the wrong mathematical operation.

## From a distinction rate to energy and mass

Let $\ell_*>0$ and $0<q_*<1$, and suppose the nonempty admissible family
$\mathcal I_{\ell_*}$ obeys (VC21). This gives a dimensionless certified
lower attenuation exponent per length,

$$
\gamma_{\mathrm{coc}}
:=
\frac{-\log q_*}{\ell_*}.
\tag{VC33}
$$

For every admissible product, (VC13) and (VC21) imply
$-\ell_*^{-1}\log\|A_{n:m}\|\geq\gamma_{\mathrm{coc}}$. Thus
$\gamma_{\mathrm{coc}}$ is a lower bound on the slowest inverse-length
attenuation rate of the complete pointed vacuum complement; it equals the
optimal rate only when $q_*$ is sharp at the operator level. It contains
neither $\hbar$ nor a mass by definition.
[[contemporary-puzzles/yang-mills-mass-gap/mass-as-a-calibrated-distinction-rate|Mass
as a Calibrated Distinction Rate]] owns the full conversion and calibration
firewalls.

Assume, independently, that there is one reconstructed pointed physical
carrier $(\mathcal K,\Omega)$, unitary vacuum-aligning identifications
$V_j:\mathcal H_j\to\mathcal K$ with $V_j\Omega_j=\Omega$, and a
self-adjoint energy operator with $K:=H-\varepsilon_0\geq0$. Define

$$
Z_0:=\mathbf1_{\{0\}}(K),
\qquad
\Delta_E
:=
\inf\sigma\!\left(K|_{Z_0^\perp\mathcal K}\right),
\qquad
Z_0=P_\Omega.
\tag{VC33a}
$$

The last equality is the unique-vacuum hypothesis needed for the standard
mass-gap statement. For every $(m,n)\in\mathcal I_{\ell_*}$, the
physical-transfer solder is the separately proved identity

$$
V_nA_{n:m}V_m^*
=
e^{-\ell_*K/(\hbar c)}(I-Z_0),
\qquad
V_m^*V_m=I_{\mathcal H_m},\quad V_n^*V_n=I_{\mathcal H_n}.
\tag{VC34}
$$

Functional calculus then gives the exact implication

$$
\boxed{
\Delta_E
\geq
\hbar c\,\gamma_{\mathrm{coc}}
=
\frac{\hbar c}{\ell_*}\log\frac1{q_*}.}
\tag{VC35}
$$

For clock duration $\tau_*=\ell_*/c$,

$$
\frac{\Delta_E}{\hbar}
\geq
\frac{-\log q_*}{\tau_*}.
\tag{VC36}
$$

Only after positive-energy Poincare reconstruction, with
$K$ the normalized time-translation generator and
$\mathcal C=K^2-c^2\mathbf P^2$, may one define the invariant joint-spectrum
threshold

$$
m_{\mathrm{gap}}
:=
\inf_{(E,\mathbf p)\in\Sigma_{\mathrm{nv}}}
\frac{\sqrt{E^2-c^2|\mathbf p|^2}}{c^2},
\tag{VC36a}
$$

where $\Sigma_{\mathrm{nv}}$ is the nonvacuum part of the joint spectrum of
$(K,\mathbf P)$. When the reconstructed Poincare theorem proves
$\Delta_E=c^2m_{\mathrm{gap}}$, as detailed in
[[contemporary-puzzles/yang-mills-mass-gap/mass-as-casimir-and-realization|Mass
as Casimir and Realization]], (VC35) becomes

$$
m_{\mathrm{gap}}=\frac{\Delta_E}{c^2}
\geq
\frac{\hbar}{c}\gamma_{\mathrm{coc}}
\tag{VC37}
$$

This statement uses an infimum and does not assume that a lowest massive
sector is attained. It is the precise surviving content of “mass is a
rate”: mass is the Poincare image of a
uniform lower attenuation exponent. The algebraic construction supplies
the dimensionless ordered product; $c$ converts the slab scale to clock
duration and $\hbar$ converts inverse duration to energy. None of those
unit conversions derives the physical slab scale.

A lossy carrier-changing cocycle with no identification (VC34) has no
Hamiltonian logarithm. Two complementary projections can even have zero
product, whereas $e^{-\ell K}$ for finite $\ell$ is injective. The physical
transfer solder is therefore indispensable.

At adjacent lattice spacing $a$, a finite continuum gap has
$\|T_a|_{\Omega^\perp}\|\to1$. The invariant target is the product across a
fixed physical slab, not a regulator-independent one-link defect. A
continuum theorem must additionally prove convergence of pointed carriers
and vacua, complete coverage of limiting physical directions, the
Osterwalder--Schrader axioms, and Poincare reconstruction.

## Operator type ledger

| Object | Operates on | Exact role | Does not yet supply |
|---|---|---|---|
| $P_k$ | $\mathcal H_k\to\mathcal H_{k+1}$ | whole carrier comparison or declared transfer arrow | one fixed clock dynamics |
| $A_k=\Pi_{k+1}P_k\Pi_k$ | pointed vacuum complements | centered operator cocycle | positivity, self-adjointness, or energy |
| $C_k$ | nonnegative block-magnitude vectors in $\ell^2(I_k)$ | scalar majorant for propagation of block norms | phase, direction, cancellation, or a physical channel |
| $D_k=I-A_k^*A_k$ | current pointed vacuum complement | one-stage squared-norm defect | an independently derived geometric response |
| $\mathcal W_{n:m}$ | initial vacuum complement to the direct sum of stage carriers | exact transported-defect frame and product stopping criterion | physical normalization or a Hamiltonian solder |
| $U_2^*P_1F_1P_0U_0$ | initial visible carrier to final visible carrier | exact intermediate leave-and-return memory | stochastic ontology |
| $U_{t:s}$ | standard Hilbert carriers | unitary transport of algebraic frame and pushed state | an independently changed pointing |
| $\mathsf R_{t:s}$ | target standard Hilbert carrier | generally nonunitary change of faithful pointing under domination | physical clock time or mass |
| $e^{-\ell K/(\hbar c)}$ | one reconstructed physical Hilbert space | positive Euclidean attenuation generated by normalized energy | the formation quotient or an actuality rule |
| $e^{-itK/\hbar}$ | the same reconstructed physical carrier | Lorentzian unitary clock group | ontological descent or record direction |

## Stopping and kill conditions

The carrier theorem advances the programme only if all of the following
survive:

1. the vacuum-aligned block family is complete, including the balance
   sector;
2. every countable block majorant is bounded, preferably by a uniform
   weighted Schur estimate;
3. complementary stages yield a uniform transported-defect lower frame, or
   equivalently a subunit product at fixed physical thickness, even though
   individual stages may have norm one;
4. state changes use standard-form transport followed by target
   realignment rather than a real modular cocycle advertised as a
   state-changing unitary;
5. the scale product is independently intertwined with the actual
   reflection-positive Yang--Mills transfer;
6. the bound remains uniform in spatial volume and along regulator removal;
   and
7. the final reconstructed carrier has only the vacuum in the null sector
   and supports the Poincare-Casimir identification.

Failure of any item kills the proposed mass-gap inference while leaving the
abstract block theorem true. In particular, the scalarization slack
$\mathfrak F$, the leave-and-return residue, a Connes cocycle, or a
dimensionless product norm must not be renamed entropy, causal charge,
energy, or mass without a separate same-carrier theorem.

## Receipt and dependencies

[[vacuum-aligned-transfer-cocycle/receipts/transfer_cocycle_receipt.py|The
 finite receipt]] verifies a rectangular changing-carrier product, exact
forward-only centered composition without adjoint vacuum preservation,
strict Walsh scalarization, the complementary two-stage transported-defect
ledger, a nonzero leave-and-return term, the $2\times2$ modular state-change
obstruction, and the ordered Araki amplitude chain rule for three
noncommuting faithful density matrices.
[[vacuum-aligned-transfer-cocycle/receipts/transfer-cocycle-receipt-output.txt|The
stored output]] records the values.

[[two-slice-innovation-geometry/inq|Two-Slice Innovation Geometry]] supplies
the one-arrow block-majorant theorem.
[[vacuum-balance-fisher-geometry/inq|Vacuum-Balance Fisher Geometry]]
supplies the fixed-carrier short and semigroup obstruction.
[[transported-response-observability-solder/inq|Transported Response
Observability Solder]] constructs the bounded response maps required by the
defect-frame theorem from an independently proved same-carrier comparison.
[[directed-isometric-residue-completion/inq|Directed Isometric Residue
Completion]] gives the defect ledger its universal minimal isometric carrier
and separates one-sided residue completion from Lorentzian clock unitarity.
[[contemporary-puzzles/yang-mills-mass-gap/descent-loss-cocycle-and-recovery-fork|The
Descent-Loss Cocycle]] is the additive relative-entropy arrow cost; it is
distinct from the multiplicative transfer subcocycle here.
[[spectral-wall-descent/scale-correspondence-stack|The Scale-Correspondence
Stack]] supplies the changing-algebra and Connes-fusion target.
[[library/the-standard-form-of-von-neumann-algebras/inq|Haagerup]] supplies
standard-form uniqueness and the canonical unitary implementation of
isomorphisms.
[[library/some-properties-of-modular-conjugation-and-a-noncommutative-radon-nikodym-theorem-with-a-chain-rule/inq|Araki]]
supplies the natural-cone and noncommutative half-density precedent.

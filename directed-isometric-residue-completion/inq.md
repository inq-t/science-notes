---
inq.module: "directed-isometric-residue-completion"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Directed Isometric Residue Completion

Every contraction has a canonical minimal isometric completion: adjoining
its defect as a new orthogonal coordinate turns the contraction into an
isometry, proper exactly when the contraction is not a coisometry. Cascading
the construction produces a deterministic isometric arrow whose output
contains the surviving presentation together with every transported stage
residue. For a nonidentity positive transfer this arrow is proper; it
preserves a norm while retaining a direction relative to the declared
codomain. When independently constructed geometric responses split the
defects, the completion separates witnessed distinction from an unsoldered
remainder. This is an exact algebraic model for accumulating candidate
record amplitudes, but it becomes ontological time, entropy production, or
physical fact formation only after those output carriers are physically
realized.

**Status: [EXACT] for the one-step defect column, unitary criterion,
changing-carrier cascade, response-residual refinement, stationary
positive-semigroup output completion, and gap equivalences; [INTERPRETATION] for the output defect
spaces as records; [OPEN] for a wall-derived record algebra, factual
instrument, Type-III product system, Yang--Mills transfer realization, and
continuum Poincare reconstruction.**

## A contraction becomes a directed isometry

Let

$$
A:\mathcal H\longrightarrow\mathcal K,
\qquad
\|A\|\leq1,
\qquad
\delta_A:=(I_{\mathcal H}-A^*A)^{1/2},
\tag{DI1}
$$

and let

$$
\mathcal D_A:=\overline{\operatorname{Ran}\delta_A}
\tag{DI2}
$$

be its defect space. The column operator

$$
\boxed{
V_A:\mathcal H\longrightarrow\mathcal K\widehat\oplus\mathcal D_A,
\qquad
V_Ax:=Ax\oplus\delta_Ax}
\tag{DI3}
$$

is an isometry because

$$
V_A^*V_A=A^*A+\delta_A^2=I_{\mathcal H}.
\tag{DI4}
$$

No probability, environment, or hidden ontology is needed for this identity.
The contraction $A$ is the first-coordinate compression of a norm-preserving
arrow; the defect coordinate contains exactly the norm absent from that
presentation.

Isometric is not the same as unitary. The minimal column (DI3) is onto if
and only if $A$ is a coisometry:

$$
\boxed{V_A\text{ is unitary}\quad\Longleftrightarrow\quad AA^*=I_{\mathcal K}.}
\tag{DI5}
$$

If $V_A$ is onto, the upper-left block of $V_AV_A^*$ gives $AA^*=I$. In the
other direction, a coisometry has
$A^*A=P_{(\ker A)^\perp}$,
$\delta_A=P_{\ker A}$, and
$\mathcal H=A^*\mathcal K\widehat\oplus\ker A$; (DI3) is then the obvious
unitary onto $\mathcal K\widehat\oplus\ker A$.

For a positive self-adjoint transfer on one carrier,

$$
0\leq A\leq I_{\mathcal H},
\tag{DI6}
$$

coisometry would imply $A^2=I$ and hence $A=I$. Therefore

$$
\boxed{
0\leq A\leq I,\quad A\neq I
\quad\Longrightarrow\quad
V_A\text{ is a proper non-surjective isometry}.}
\tag{DI7}
$$

This is a precise algebraic form of directedness: norm is preserved, but the
arrow has no inverse on its enlarged codomain. A unilateral shift is the
standard fixed-carrier prototype. Direction here is not spontaneous
symmetry breaking; the group property was never assumed.

## The defect carrier is the universal minimal completion

The carrier in (DI2) is not an arbitrary environment. Suppose

$$
W:\mathcal H\longrightarrow\mathcal K\widehat\oplus\mathcal E
\tag{DI7a}
$$

is any isometry whose first-coordinate compression is $A$:
$P_{\mathcal K}W=A$. Write $Wx=Ax\oplus Cx$. Isometry gives

$$
C^*C=I-A^*A=\delta_A^2.
\tag{DI7b}
$$

The polar decomposition, or equivalently Douglas factorization, produces a
unique isometry

$$
U:\mathcal D_A\longrightarrow\mathcal E,
\qquad
\operatorname{Ran}U=\overline{\operatorname{Ran}C},
\tag{DI7c}
$$

such that

$$
\boxed{W=(I_{\mathcal K}\oplus U)V_A.}
\tag{DI7d}
$$

Thus every isometric completion of $A$ is the canonical defect column
followed by an isometric relabelling of its minimal residue carrier, possibly
with unused ambient coordinates. The theorem establishes uniqueness of the
carrier required by norm completion. It does not establish that this carrier
is a physical environment or record algebra.

## A chain accumulates its residues

Let

$$
A_k:\mathcal H_k\longrightarrow\mathcal H_{k+1},
\qquad
\|A_k\|\leq1,
\qquad
D_k:=I_{\mathcal H_k}-A_k^*A_k,
\tag{DI8}
$$

and define

$$
B_{k:m}
:=
\begin{cases}
I_{\mathcal H_m},&k=m,\\
A_{k-1}\cdots A_m,&k>m.
\end{cases}
\tag{DI9}
$$

The cascade column is

$$
\boxed{
V_{n:m}x
:=
B_{n:m}x
\oplus
\left(D_k^{1/2}B_{k:m}x\right)_{k=m}^{n-1}}
\tag{DI10}
$$

from $\mathcal H_m$ into

$$
\mathcal H_n
\widehat\oplus
\widehat\bigoplus_{k=m}^{n-1}
\overline{\operatorname{Ran}D_k^{1/2}}.
$$

The telescoping defect identity gives

$$
\boxed{V_{n:m}^*V_{n:m}=I_{\mathcal H_m}.}
\tag{DI11}
$$

Thus the full cascade is isometric even though its surviving endpoint
$B_{n:m}$ may be strictly contractive. Composition is coherent. Under the
canonical direct-sum reassociation and permutation that places older residue
coordinates in their declared order,

$$
\mathcal D_{n:m}
:=
\widehat\bigoplus_{k=m}^{n-1}
\overline{\operatorname{Ran}D_k^{1/2}},
$$

$$
V_{p:m}
=
\left(V_{p:n}\oplus I_{\mathcal D_{n:m}}\right)V_{n:m},
\tag{DI12}
$$

where $V_{p:n}$ acts only on the surviving $\mathcal H_n$ coordinate and
the earlier residues pass forward unchanged. This is a deterministic
residue grammar: later stages retain earlier residue coordinates. Calling
them records additionally requires physical persistence and readout.

The chronological archive is not generally the minimal defect carrier of
the endpoint product. Put

$$
\mathcal W_{n:m}x
:=
\left(D_k^{1/2}B_{k:m}x\right)_{k=m}^{n-1},
\qquad
\delta_{B}:=(I-B_{n:m}^*B_{n:m})^{1/2}.
\tag{DI12m}
$$

Since $\mathcal W_{n:m}^*\mathcal W_{n:m}=\delta_B^2$, one-step
minimality gives an isometry

$$
U_{n:m}:\overline{\operatorname{Ran}\delta_B}
\longrightarrow
\overline{\operatorname{Ran}\mathcal W_{n:m}}
$$

such that

$$
\boxed{\mathcal W_{n:m}=U_{n:m}\delta_B.}
\tag{DI12n}
$$

Thus the reachable chronological archive is an isometric relabelling of the
minimal endpoint defect, while the full direct sum in (DI10) may contain
coordinates no initial input can reach. Retaining those ambient coordinates
records the stage decomposition; it is additional structure, not universal
minimality for $B_{n:m}$.

With every defect codomain minimal, the cascade is onto exactly when every
stage is a coisometry:

$$
\boxed{
V_{n:m}\text{ is unitary}
\quad\Longleftrightarrow\quad
A_kA_k^*=I_{\mathcal H_{k+1}}
\text{ for every }m\leq k<n.}
\tag{DI12i}
$$

The forward implication follows because the range of a composite of
isometries lies in the range of its last factor; induction makes every
factor onto. The reverse implication follows from (DI5) stage by stage. For
positive same-carrier stages, the cascade is therefore unitary only when
every $A_k=I$.

This criterion concerns surjectivity onto the full chronological archive.
The minimal completion of the endpoint product is unitary under the weaker
condition $B_{n:m}B_{n:m}^*=I$. For example, with unilateral shift $S$,
$A_0=S$ and $A_1=S^*$ give $B_{2:0}=I$; the endpoint needs no defect, while
the declared two-stage archive still contains an unreachable coordinate
from the nonzero defect space of $S^*$.

Direction and residue are nevertheless different predicates for a general
contraction. The unilateral shift $S$ is proper although
$I-S^*S=0$; the backward shift $S^*$ has a nonzero input defect but is a
coisometry, so its minimal column is unitary. Positivity and
self-adjointness make nontrivial attenuation, nonzero defect, and a proper
completion coincide in the physical-transfer class; abstract operator
theory does not.

This column construction is an **isometric completion**, not yet a
Sz.-Nagy dilation in the technical sense. A dilation of one fixed operator
would require a single iteratable endomorphism on one enlarged carrier and
the compression-of-powers relation
$A^j=P_{\mathcal H}V^j|_{\mathcal H}$. Changing carriers and a finite
cascade do not supply that theorem. A continuous product system or
$E_0$-semigroup is a later construction, not a synonym for (DI10).

## Infinite accumulation is weaker than a finite gap

For a countable cascade with fixed initial stage $m$, the positive
contractions

$$
Q_n:=B_{n:m}^*B_{n:m}
\tag{DI12j}
$$

decrease strongly to a positive contraction $Q_\infty$. Monotone strong
convergence and the finite ledger give

$$
\boxed{
I-Q_\infty
=
\sum_{k=m}^{\infty}
B_{k:m}^*D_kB_{k:m}}
\tag{DI12k}
$$

with strong convergence. Hence

$$
x\longmapsto
Q_\infty^{1/2}x
\oplus
\left(D_k^{1/2}B_{k:m}x\right)_{k=m}^{\infty}
\tag{DI12l}
$$

is an isometry into the asymptotic-survival completion plus all defect
carriers. The operator $Q_\infty$ need not be a projection, so its first
coordinate is not automatically a persistent physical subspace.

Even $Q_\infty=0$ means only that every fixed input is eventually captured
by the defect archive. It does not imply contraction within a uniformly
bounded number of stages. Increasing finite-rank projections can exhaust a
separable Hilbert space strongly while every finite complement retains norm
one. A mass gap requires a response floor on one finite physical slab.

## A stationary completion admits a Wold decomposition

When every stage is one contraction $A:\mathcal H\to\mathcal H$, the extra
construction can be made. On

$$
\widehat{\mathcal H}_A
:=
\mathcal H
\widehat\oplus
\mathcal D_A
\widehat\oplus
\mathcal D_A
\widehat\oplus\cdots,
\tag{DI12a}
$$

define the Schäffer isometry

$$
\boxed{
\widehat V_A(h,d_0,d_1,\ldots)
=
(Ah,\delta_Ah,d_0,d_1,\ldots).}
\tag{DI12b}
$$

It is an isometry, and its powers recover the original stationary transfer:

$$
\boxed{
P_{\mathcal H}\widehat V_A^j|_{\mathcal H}=A^j,
\qquad j\geq0.}
\tag{DI12c}
$$

It is minimal because

$$
\widehat{\mathcal H}_A
=
\overline{\operatorname{span}}
\{\widehat V_A^j\mathcal H:j\geq0\}.
\tag{DI12d}
$$

Indeed, subtracting the embedded vector $Ah$ from $\widehat V_Ah$ isolates
$\delta_Ah$ in the first defect slot, and subsequent shifts generate every
later slot. This is the technical isometric dilation that the finite
changing-carrier column by itself did not supply.

Wold decomposition now applies:

$$
\widehat{\mathcal H}_A
=
\widehat{\mathcal H}_{\mathrm u}
\widehat\oplus
\widehat{\mathcal H}_{\mathrm s},
\qquad
\widehat V_A|_{\widehat{\mathcal H}_{\mathrm u}}
\text{ unitary},
\tag{DI12e}
$$

while the second summand is generated by mutually orthogonal translates of
the wandering space
$\ker\widehat V_A^*$. This decomposes reversible and shift-like structure
without deriving a physical interpretation for either.

For $0\leq A\leq I$, spectral calculus gives

$$
A^j\xrightarrow[,j\to\infty,]{\mathrm s}
P_1:=\mathbf1_{\{1\}}(A).
\tag{DI12f}
$$

On $(I-P_1)\mathcal H$, the stationary transfer therefore fades pointwise
and its minimal isometric dilation is pure shift. But this is not a gap. If
the spectrum of $A$ accumulates at $1$ without a $1$-eigenvector on that
carrier, then

$$
A^jx\to0\quad\text{for every }x,
\qquad
\|A^j\|=1\quad\text{for every }j.
\tag{DI12g}
$$

The mass-gap-strength predicate is the stronger uniform statement

$$
\boxed{
\|A|_{(I-P_1)\mathcal H}\|\leq q<1
\quad\Longleftrightarrow\quad
\|A^j(I-P_1)\|\leq q^j\quad\text{for every }j\geq0.}
\tag{DI12h}
$$

Wold purity separates a reversible fixed core from one-sided presentation;
it does not exclude arbitrarily slow nonvacuum modes. Quantitative residue
production, not shift structure alone, is the gap condition.

The order matters. Reversing the stages changes both the surviving product
and which transported vector reaches each defect space. Replacing the exact
operators by scalar defect sizes forgets that directional information.

## Geometry splits witnessed response from unexplained loss

Suppose an independently constructed analysis $L_k$ satisfies

$$
D_k=L_k^*L_k+S_k,
\qquad
S_k\geq0.
\tag{DI13}
$$

Then the refined cascade

$$
\boxed{
\widetilde V_{n:m}x
=
B_{n:m}x
\oplus
\left(L_kB_{k:m}x\right)_{k=m}^{n-1}
\oplus
\left(S_k^{1/2}B_{k:m}x\right)_{k=m}^{n-1}}
\tag{DI14}
$$

is again an isometry. The three output types are:

| Coordinate | Exact meaning | Additional interpretation required |
|---|---|---|
| $B_{n:m}x$ | surviving endpoint amplitude | observable state or physical transfer |
| $L_kB_{k:m}x$ | geometrically certified part of stage defect | distinction, record, boundary flux, or fact |
| $S_k^{1/2}B_{k:m}x$ | positive transfer defect not certified by $L_k$ | any physical meaning at all |

Douglas factorization makes the word *solder* exact. Write
$\delta_k=D_k^{1/2}$ and
$\mathcal D_k=\overline{\operatorname{Ran}\delta_k}$. The inequality
$L_k^*L_k\leq D_k$ holds if and only if there is a contraction

$$
\boxed{
C_k:\mathcal D_k\longrightarrow
\overline{\operatorname{Ran}L_k},
\qquad
L_k=C_k\delta_k.}
\tag{DI14a}
$$

Thus the chosen geometric response is a contractive readout of the canonical
transfer-defect carrier. When $L_k^*L_k=D_k$, the map $C_k$ is isometric on
$\mathcal D_k$ and no defect norm remains unexplained. The factorization
constructs the carrier map implied by a proved comparison; it does not prove
that comparison or select $C_k$ physically.

[[transported-response-observability-solder/inq|Transported Response
Observability Solder]] constructs

$$
L_k=\sqrt{\eta_k}(I-e^{-\tau_kG_k})^{1/2}
$$

from an independently proved response comparison, or obtains $L_k$ exactly
as the orthogonal residue of two endpoint isometries in one joint
correspondence. The distinction between $L_k$ and $S_k$ prevents the chosen
geometry from being inflated into a complete explanation of every transfer
loss.

## What is conserved, and what is not

For every input vector, (DI14) gives

$$
\|x\|^2
=
\|B_{n:m}x\|^2
+\sum_k\|L_kB_{k:m}x\|^2
+\sum_k\|S_k^{1/2}B_{k:m}x\|^2.
\tag{DI15}
$$

The conserved object is a Hilbert norm. This is the strongest exact answer
currently available to the question “what is conserved between survival and
residue?” It is not automatically:

- a Noether charge, because no symmetry or signed current has been supplied;
- von Neumann entropy, because an isometry preserves a pure state globally
  and entropy of a reduced state depends on a state and tensor factorization;
- probability of an actual outcome, because no instrument or obtained
  character has been supplied; or
- energy, because no OS or Hamiltonian identification has been supplied.

If a later physical theorem realizes the $L_k$ coordinates as durable record
degrees of freedom, (DI15) still contains the unsoldered $S_k$ sector. A
two-term conservation law between survivor and record amplitude follows only
when $S_k=0$; otherwise the exact ledger has survivor, realized response, and
unexplained residue terms. It still does not imply that record values are
stochastic in ontology. A probabilistic readout begins only after a state and
an instrument turn those coordinates into an outcome law.

Nor does a proper isometry by itself prove absolute irreversibility. It has
the adjoint as a left inverse on its range. Non-surjectivity says that an
arbitrary final-plus-residue tuple is not a compatible history of an initial
state; it does not say that the compatible range is physically unrecoverable.
The isometry can itself be embedded in a unitary dilation after further
enlargement, and even an invertible positive contraction has a proper defect
column unless it is the identity. Properness therefore belongs to the
declared residue archive, not automatically to metaphysics or to
noninvertibility of the original transfer.
Ontological irreversibility requires an additional restriction on admissible
reverse morphisms, stable record inclusion, or operational recovery.

## Continuous depth and a minimum residue-production rate

Let $K\geq0$ be self-adjoint and

$$
T_s:=e^{-sK},
\qquad s\geq0.
\tag{DI16}
$$

For $s_*>0$, define the residue-density map spectrally by

$$
(\mathcal R_{s_*}x)(s)
:=
\sqrt{2K}\,e^{-sK}x,
\qquad 0<s<s_*.
\tag{DI17}
$$

Although $K$ may be unbounded, this is a bounded map
$\mathcal H\to L^2((0,s_*);\mathcal H)$. Spectral calculus gives the
improper strong-operator, equivalently quadratic-form, integral

$$
\mathcal R_{s_*}^*\mathcal R_{s_*}
=
\int_0^{s_*}2e^{-sK}Ke^{-sK}\,\mathrm ds
=
I-e^{-2s_*K}.
\tag{DI18}
$$

Consequently,

$$
\mathcal D_{s_*}
:=
\overline{\operatorname{Ran}\mathcal R_{s_*}}
\subseteq L^2((0,s_*);\mathcal H)
\tag{DI18a}
$$

is the minimal residue-output carrier, and

$$
\boxed{
W_{s_*}x
:=
e^{-s_*K}x\oplus\mathcal R_{s_*}x
}
\tag{DI19}
$$

is an isometry from $\mathcal H$ to
$\mathcal H\widehat\oplus\mathcal D_{s_*}$. Splitting
$L^2(0,s+t)\cong L^2(0,s)\oplus L^2(0,t)$ gives the exact ambient-output
concatenation identity

$$
\mathcal R_{s+t}x
\cong
\mathcal R_sx
\oplus
\mathcal R_t(T_sx).
\tag{DI20}
$$

The earlier residue output is retained and the later output is produced from
the surviving component. This is an identity on the realized image in the
ambient $L^2$ output spaces; it does not identify the minimal carriers as
$\mathcal D_{s+t}\cong\mathcal D_s\oplus\mathcal D_t$ and does not make the
$W_s$ a fixed-carrier semigroup. If $K\neq0$, then $T_s$ is a nontrivial
positive contraction, so each minimal $W_s$ is a proper isometry by (DI7).

Equations (DI17)--(DI20) concern one stationary semigroup on one fixed
carrier. They are not automatically the continuum limit of the
changing-carrier cascade (DI10). That passage requires convergence of
carriers, generators, defects, and the partitioned residue embeddings.

For a stationary partition there is, however, an exact discrete-to-
continuous identification with no mesh limit. If $h>0$, put
$\delta_h=(I-e^{-2hK})^{1/2}$. The rule

$$
J_h(\delta_hy)(u)
:=
\sqrt{2K}e^{-uK}y,
\qquad 0<u<h,
\tag{DI20a}
$$

is well defined and extends to an isometry from
$\overline{\operatorname{Ran}\delta_h}$ into
$L^2((0,h);\mathcal H)$ because both squared norms equal
$\langle y,(I-e^{-2hK})y\rangle$. For a partition
$0=t_0<\cdots<t_N=t$, take

$$
A_k=e^{-(t_{k+1}-t_k)K},
\qquad
B_{k:0}=e^{-t_kK}.
$$

Under the direct sum of the interval translations of $J_{t_{k+1}-t_k}$,
the discrete residue

$$
\delta_{t_{k+1}-t_k}B_{k:0}x
$$

maps exactly to
$s\mapsto\sqrt{2K}e^{-sK}x$ on $(t_k,t_{k+1})$. Thus the stationary
discrete cascade gives exactly (DI17) on the image of the initial carrier,
independent of the partition. It does not identify the entire archive
codomains across partitions: an $N$-stage archive may contain more
unreachable directions than the minimal one-interval output. Varying
generators and carriers remain the unsolved continuum problem.

Letting $s_*\to\infty$ gives

$$
\boxed{
\mathcal R_\infty^*\mathcal R_\infty
=I-P_{\ker K}.}
\tag{DI20b}
$$

On a kernel-free vacuum complement, the infinite residue map is therefore
isometric even when $\inf\sigma(K)=0$. Complete eventual accumulation is
not a gap; a gap is the uniform positive residue fraction at finite depth.

On a declared $K$-reducing vacuum complement, the following are equivalent
for $\Delta>0$, with the first inequality understood in quadratic-form
sense:

$$
\boxed{
K\geq\Delta I}
\tag{DI21a}
$$

$$
\boxed{
\|T_sx\|^2\leq e^{-2s\Delta}\|x\|^2
\quad(s\geq0)}
\tag{DI21b}
$$

and

$$
\boxed{
\|\mathcal R_sx\|^2
\geq
(1-e^{-2s\Delta})\|x\|^2
\quad(s\geq0).}
\tag{DI21c}
$$

On $\operatorname{Dom}K^{1/2}$, the infinitesimal form version is

$$
-\left.\frac{\mathrm d}{\mathrm ds}\right|_{s=0+}
\|T_sx\|^2
=2\|K^{1/2}x\|^2
\geq2\Delta\|x\|^2.
\tag{DI22}
$$

This supplies a rigorous candidate behind “mass is a rate.” Before physical
calibration, $\Delta$ is the amplitude attenuation exponent and
$2\Delta$ is the minimum instantaneous squared-norm residue-production rate.
Neither is yet a frequency of facts.

For one fixed depth $s_*$, a residue floor

$$
\|\mathcal R_{s_*}x\|^2\geq\kappa\|x\|^2,
\qquad 0<\kappa<1,
\tag{DI23}
$$

is equivalent to

$$
K\geq
-\frac1{2s_*}\log(1-\kappa)I.
\tag{DI24}
$$

The factor $1/2$ records that $\kappa$ measures squared norm.

## Local clock unitarity is a different arrow

The directed completion does not make a unitary clock by throwing away its
residue. Its algebraic types are

$$
\boxed{
V_{n:m}:\text{isometric residue completion},
\qquad
B_{n:m}:\text{contractive endpoint product},
\qquad
U_t:\text{reconstructed unitary clock}.}
\tag{DI25}
$$

The first arrow is proper on the full chronological archive when at least
one stage is not a coisometry; it is not unconditionally proper. The second
is its endpoint compression and becomes Euclidean survival only after a
transfer identification. The third exists only after a fixed physical
carrier, a self-adjoint generator, and clock parameter have been
reconstructed. If
$K=(H-E_0)/(\hbar c)$ and $s$ is physical Euclidean length, then

$$
T_s=e^{-s(H-E_0)/(\hbar c)},
\qquad
U_t=e^{-it(H-E_0)/\hbar}
\tag{DI26}
$$

are different functional-calculus faces of the reconstructed generator.
$U_t$ is neither the inverse nor the compression of $V_{n:m}$.

In the stationary reconstructed case their compatibility is an exact
intertwiner rather than a causal implication. Let
$U_t^{\mathrm{res}}$ act pointwise on
$L^2((0,s);\mathcal H)$ by

$$
(U_t^{\mathrm{res}}f)(u):=U_tf(u).
\tag{DI26a}
$$

Functional calculus gives
$\mathcal R_sU_t=U_t^{\mathrm{res}}\mathcal R_s$, so
$\mathcal D_s$ is invariant and

$$
\boxed{
W_sU_t
=
(U_t\oplus U_t^{\mathrm{res}}|_{\mathcal D_s})W_s.}
\tag{DI26b}
$$

A proper positive-transfer residue completion can therefore be equivariant
under a distinct unitary clock group. Neither arrow manufactures the other.

There is a second exact route to observable unitarity. A nonfaithful
formation may select a semidefinite response quotient; transformations that
preserve its radical and form descend to unitaries on its completion.
[[algebra/quotient-unitarity-and-kernel-stabilization|Quotient Unitarity and
Kernel Stabilization]] proves that result. Again the unitary belongs to the
selected quotient carrier, not to the prior formation arrow.

The Copernican statement can therefore be made without contradiction. A
primitive formation diagram need not be an automorphism diagram--and may not
yet admit a notion of unitarity at all--while a physical carrier selected
from it may later support a unitary clock group. If the declared transfer is
independently realized by the residue completion above, (DI26b) supplies the
required compatibility. It is too strong to say that nonunitarity causes
unitarity: the connective is an intertwiner between different arrows and
carriers. Nothing in the abstract Hilbert theorem yet derives spatial
locality or a measurement operation; those require a local net and an
instrument, respectively.

## The physical-carrier obligation

Every contraction admits (DI3). Therefore the existence of an abstract
defect completion explains no particular physics. It becomes a principled
mass-gap construction only if all of the following are derived rather than
named:

1. the pointed transfer or joint correspondence from regulator Yang--Mills;
2. a complete physical vacuum complement, including balance, boundary, and
   global tail sectors;
3. the geometric meaning and normalization of the selected $L_k$ response
   coordinates;
4. a fixed-physical-slab lower frame for those coordinates, uniform in
   spatial volume, boundary data, and regulator removal;
5. a record algebra or instrument if the residue is to mean a fact rather
   than attenuation;
6. Osterwalder--Schrader reconstruction and a nontrivial continuum local net;
   and
7. positive-energy Poincare reconstruction before the generator edge is
   called mass.

For a fixed physical slab $\ell_*$ with a full-defect or soldered-response
floor $\kappa_*$ on the same OS-identified transfer, the conditional energy
and mass bounds are

$$
\Delta_E
\geq
-\frac{\hbar c}{2\ell_*}\log(1-\kappa_*),
\tag{DI27}
$$

and, only after the Casimir theorem,

$$
m_{\mathrm{gap}}
\geq
-\frac{\hbar}{2c\ell_*}\log(1-\kappa_*).
\tag{DI28}
$$

The response floor is the dimensionless structural input. The physical
length, $c$, and $\hbar$ are downstream calibration maps. None may be hidden
inside $L_k$ while claiming that the scale was derived.

## Receipt and dependencies

[[directed-isometric-residue-completion/receipts/directed_residue_completion_receipt.py|The
finite receipt]] verifies a proper one-step positive-transfer isometry, a
unitary coisometric column, universal residual factorization, the distinction
between an endpoint-minimal defect and a larger chronological archive, the
discrete cascade, Schäffer compression of powers, the response-residual
refinement, stationary partition Gramian, continuous fixed-depth gap
equivalence, and residue-clock intertwiner.
[[directed-isometric-residue-completion/receipts/directed-residue-completion-receipt-output.txt|The
stored output]] records the numerical values.

[[vacuum-aligned-transfer-cocycle/inq|The Vacuum-Aligned Transfer Cocycle]]
supplies the changing-carrier telescoping identity.
[[transported-response-observability-solder/inq|Transported Response
Observability Solder]] supplies the independently typable response split.
[[two-slice-innovation-geometry/inq|Two-Slice Innovation Geometry]] supplies
the canonical endpoint-embedding residual.
[[bridge-score-fusion-geometry/inq|Bridge-Score Fusion Geometry]] supplies a
complete middle-slice analysis into the centered two-ended fusion residue and
proves that its Gramian is bounded by the corresponding transfer defect.
[[reverse-prediction-residue-archive/inq|The Reverse-Prediction Residue
Archive]] realizes the full stationary defect cascade as orthogonal
conditional-prediction innovations in one path carrier and proves the same
finite-slab floor equivalence without adding stochastic ontology.
[[library/on-majorization-factorization-and-range-inclusion-of-operators-on-hilbert-space/inq|Douglas]]
supplies the factorization theorem used to type the response readout.
[[library/on-unitary-dilations-of-contractions/inq|Schäffer]] supplies the
explicit contraction-dilation precedent and compression-of-powers grammar.
[[library/continuous-analogues-of-fock-space/inq|Arveson]] supplies the
product-system and endomorphism-semigroup standard that the additive residue
outputs do not yet meet.
[[flux-record-and-top-form-realizations/inq|Flux, Records, Top Forms, and
Assembly]] owns the distinction among record persistence, boundary flux,
top-form sectors, and index transport.
[[conservation-of-causal-charge/unitarity-and-ontological-time|Why Unitarity
Is Not the Wall Symmetry]] owns the formation/transfer/clock firewall.

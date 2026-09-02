# Octonionic and Integrable Complex Geometry on $S^6$ and the Determinant Fork

The established existence of an integrable complex structure on the smooth six-sphere makes the octonionic proposal sharper, but it does not identify the canonical octonionic almost-complex structure with the new integrable one. The strongest exact numerical chain is instead $3\to6\to6^2$: complex rank three gives a determinant amplitude of scale weight three, its Hermitian square gives an invariant density of weight six, and a second-order operator on that density would have threshold thirty-six. Ordinary Hilbert-space use of the density takes its square root back to weight three and threshold nine. Deciding whether the primitive physical object is an amplitude, a density, or a squared-line section is therefore the decisive $9$-versus-$36$ question.

**Status: [EXPLORATORY PHYSICAL BRIDGE].** The existence of an integrable complex structure on $S^6$ is established: it has a self-contained geometric proof and a separate Lean proof artifact in addition to the original long construction. Every proposed relation to octonionic ontology, local QFT, causal scale, or Yang--Mills remains an open carrier-changing construction.

## One smooth sphere, two inequivalent complex geometries

The canonical octonionic description is

$$
S^6
=
\left\{
u\in\operatorname{Im}\mathbb O:\lVert u\rVert=1
\right\}
\cong
G_2/SU(3).
$$

For $v\in T_uS^6$, left multiplication defines

$$
J_{\mathrm{oct},u}(v):=uv,
\qquad
J_{\mathrm{oct}}^2=-1.
$$

Alternativity makes this an almost-complex structure, and the round metric is Hermitian for it. It is not integrable. In the normalization used in [[the-grain-of-causal-scale/inbox/black-holes-as-jordan-spectra/black-holes-as-jordan-spectra|the Jordan-spectrum exploration]],

$$
N_{J_{\mathrm{oct}}}(v,w)
=
2[u,v,w],
$$

so octonionic nonassociativity appears as Nijenhuis torsion.

The new construction starts elsewhere. It builds a compact complex threefold $X$, proves that its underlying smooth manifold is diffeomorphic to $S^6$, and transports its complex structure across a diffeomorphism:

$$
J_{\mathrm{int}}
:=
\phi_*J_X,
\qquad
N_{J_{\mathrm{int}}}=0,
\qquad
\bar\partial_{J_{\mathrm{int}}}^{\,2}=0.
$$

[[library/complex-structure-on-s6/inq|The original construction]], [[library/complex-structures-on-s6-engel/inq|Engel's self-contained proof]], and [[library/formalization-of-the-hopf-problem/inq|the formalization]] provide distinct proof presentations of the existence theorem.

These structures cannot be the same structure in different coordinates. Integrability is natural under diffeomorphism: a diffeomorphism transports a zero Nijenhuis tensor to zero and a nonzero one to nonzero. Moreover, $J_{\mathrm{int}}$ cannot be Kähler because $H^2(S^6;\mathbb R)=0$, and none of the constructions presents it as round-compatible, $G_2$-invariant, or homogeneous. The long manuscript reports its connected holomorphic automorphism group as $\mathbb C^\times$, not $G_2$; that auxiliary invariant is source-specific.

The disciplined form of the philosophical proposal is therefore not an identity but an open comparison:

$$
\boxed{
(S^6,J_{\mathrm{oct}})
\dashrightarrow
(S^6,J_{\mathrm{int}}).
}
$$

The left side carries the canonical octonionic, metric-compatible, nearly Kähler geometry with torsion. The right side carries an integrable holomorphic presentation without Kähler polarization. A functor trading nonassociative torsion for integrable complex gluing would be a major construction; the common underlying smooth manifold does not provide it automatically.

## What integrability contributes to local appearance

Integrability gives a sheaf of local holomorphic functions and a Dolbeault complex,

$$
U\longmapsto\mathcal O_{(S^6,J_{\mathrm{int}})}(U),
\qquad
\bar\partial^2=0.
$$

This is an exact grammar for compatible local complex presentation. It is a serious candidate for the mathematical meaning of a locally complex *face* of a more primitive object: local descriptions glue holomorphically even though the global complex manifold is assembled by nontrivial monodromy and singular-fiber data.

It is not yet the algebra of local quantum field theory. A QFT local net has the different type

$$
O\longmapsto\mathcal A(O)\subset B(\mathcal H),
$$

with associative generally noncommutative operator algebras, an adjoint operation, positivity, a state or vacuum, isotony, causal locality, and a translation or modular dynamics. By contrast, $\mathcal O_X(U)$ is commutative and is not naturally a $C^*$-algebra because complex conjugation does not preserve holomorphicity.

The required bridge has at least the form

$$
\mathcal O_X
\xrightarrow{\ \mathfrak Q\ }
(\mathcal A,\omega,\mathcal H)
\xrightarrow{\ \mathfrak L\ }
\left(O\mapsto\mathcal A(O),H_{\mathrm{phys}}\right),
$$

where $\mathfrak Q$ supplies quantization, adjoints, positivity, and a GNS carrier, while $\mathfrak L$ supplies Lorentzian localization and physical time translation. Both arrows are open. Integrability can therefore be the grammar of local complex appearance without already being the operator algebra of measured facts. [[complex-presentation-without-polarization/inq|Complex presentation without polarization]] owns this firewall.

## The exact determinant weight: three before six

An integrable complex structure on $S^6$ makes it a complex threefold. Its holomorphic tangent bundle has rank three,

$$
\operatorname{rank}_{\mathbb C}T^{1,0}X=3,
$$

and therefore has the determinant line

$$
K_X^{-1}
=
\det T^{1,0}X
=
\Lambda^3T^{1,0}X.
$$

Under a scalar action $v\mapsto zv$ on a local complex frame,

$$
v_1\wedge v_2\wedge v_3
\longmapsto
z^3(v_1\wedge v_2\wedge v_3).
$$

Thus the determinant *amplitude* has character weight three. A Hermitian square has weight six:

$$
\left\lVert
z^3(v_1\wedge v_2\wedge v_3)
\right\rVert^2
=
|z|^6
\left\lVert
v_1\wedge v_2\wedge v_3
\right\rVert^2.
$$

This is the first principled route from the complex dimension of $S^6$ to a sixth-degree positive quantity:

$$
\boxed{
\text{complex rank }3
\longrightarrow
\text{determinant amplitude of weight }3
\longrightarrow
\text{positive density of weight }6.
}
$$

It is not a mere equation of integers. Exterior power and Hermitian squaring are named operations. It is also not yet a physical derivation. The scalar action, Hermitian structure, and object on which the action is physical still have to be selected.

## The same fork in the $A_2$ Weyl measure

For $SU(3)$, the $A_2$ Weyl denominator is the alternating cubic

$$
\Delta_W(r_1,r_2,r_3)
:=
\prod_{i<j}(r_i-r_j).
$$

It has homogeneous degree three. The Weyl-orbit Jacobian used in diagonalization is its invariant square,

$$
J_W
:=
|\Delta_W|^2,
$$

which has degree six. Along the radial scale path $r_i(N)=e^{-N}r_i(0)$,

$$
|\Delta_W(N)|=e^{-3N}|\Delta_W(0)|,
\qquad
J_W(N)=e^{-6N}J_W(0).
$$

This is exactly the same amplitude--density distinction as for the determinant line. It is stronger than noticing that $A_2$, $SU(3)$, and six recur: it identifies the algebraic operation that produces the six.

The manuscript's use of $A_2$ does not yet establish this bridge. Its $A_2$ is a triangular lattice and fan used to fill the toric cusp; the quotient has a hexagonal $dP_6$ normalization. That construction does not by itself provide eigenvalues $r_i$, the cubic characteristic map, $S_3$ Weyl monodromy, or the analytic discriminant cusp

$$
4a^3+27b^2=0.
$$

Its global monodromy is the $(3,4,\infty)$ triangle-group representation, and its local central fiber is normal-crossing rather than the analytic $A_2$ cusp. The exact bridge target is consequently

$$
\text{toric }A_2\text{ lattice in the }S^6\text{ construction}
\dashrightarrow
A_2\text{ determinant line}
\dashrightarrow
SU(3)\text{ Weyl measure}.
$$

Neither dashed arrow has been constructed. The stabilizer $SU(3)$ in $S^6=G_2/SU(3)$, the color group $SU(3)$, and the compact real form of an $A_2$ inverse cover are also three typed occurrences until a representation-preserving map identifies them.

## Why the natural Hilbert-space branch gives nine

Suppose a positive quantity has scale profile

$$
q_w(N)=e^{-wN},
\qquad
N\in\mathbb R_+.
$$

If $q_w$ is declared to be a Hilbert amplitude, the one-sided Witten operator

$$
A_w=\partial_N+w,
\qquad
L_w=A_w^\dagger A_w=-\partial_N^2+w^2
$$

with the induced Robin boundary condition has

$$
\sigma(L_w)=\{0\}\cup[w^2,\infty).
$$

The possible inputs are not interchangeable:

| Primitive object | Scale weight used as amplitude | Second-order threshold |
|---|---:|---:|
| scale coordinate $e^{-N}$ | $1$ | $1$ |
| determinant or Weyl amplitude $|\Delta_W|=e^{-3N}$ | $3$ | $9$ |
| squared determinant $J_W=e^{-6N}$ treated as an amplitude | $6$ | $36$ |

In the standard Weyl integration formula, $J_W$ is a **measure density**. A Hilbert state belongs to

$$
L^2(J_W\,\mathrm dr),
$$

and flattening the measure multiplies its amplitude by $J_W^{1/2}=|\Delta_W|$. The natural first-order slope is therefore three and the corresponding second-order threshold is nine. Treating $J_W$ itself as a wave amplitude squares twice: once in forming $J_W=|\Delta_W|^2$, and again in the Born norm.

Thirty-six remains possible only through an additional theorem. Examples of correctly typed possibilities are:

- the primitive causal object is the invariant discriminant itself as a charge amplitude rather than as a probability or orbit-measure density;
- physical states are sections of a squared determinant line such as $K_X^{\otimes2}$, whose amplitude has absolute weight six;
- the physical transfer generator acts on densities, as in a Fokker--Planck-type carrier, rather than on ordinary Hilbert amplitudes; or
- an independent quadratic operation acts after the weight-six density has been selected.

Each option changes the carrier. None follows merely from complex dimension three, real dimension six, or the existence of an integrable $J$.

The operator order remains a second independent fork. If

$$
H_{\mathrm{phys}}/E_*=L_w,
$$

then the energy threshold is $w^2E_*$. If instead

$$
(H_{\mathrm{phys}}/E_*)^2=L_w,
$$

then it is $wE_*$. Thus even a justified weight-six amplitude yields either $36E_*$ or $6E_*$, depending on the physical generator theorem.

## The round-sphere spectrum is a separate occurrence

The unit round metric on the smooth six-sphere has the exact scalar-Laplacian spectrum

$$
\sigma(-\Delta_{S^6})
=
\left\{
\ell(\ell+5):
\ell=0,1,2,\ldots
\right\}.
$$

Thus $6$ occurs at $\ell=1$ and $36$ at $\ell=4$. The round Dirac spectrum is

$$
\sigma(D_{S^6})
=
\left\{
\pm(\ell+3):
\ell=0,1,2,\ldots
\right\},
$$

so the lowest eigenvalue of $D_{S^6}^2$ is $9$. These are genuine geometric appearances of the same three numbers, but they do not decide the determinant fork. They arise from the round metric and representation degree, whereas $J_{\mathrm{int}}$ is not supplied with the round Hermitian geometry and the Yang--Mills Hamiltonian has not been identified with either round-sphere operator. In particular, $36$ is the fourth scalar harmonic here, not a lowest nonzero eigenvalue.

## A genuine descent obstruction on the complex sphere

The manuscript reports a particularly suggestive distinction:

$$
H^2(S^6;\mathbb Z)=0,
\qquad
c_1(K_X)=0,
$$

so the canonical line is topologically trivial, while holomorphically

$$
K_X
\simeq
f^*\mathcal O_{\mathbb P^1}(-1)
\otimes
\mathcal O_X(2S_2)
$$

is non-torsion. The same construction has $h^{3,0}=0$, so there is no global nonzero holomorphic volume form trivializing $K_X$.

This is an exact model of *local availability without global holomorphic descent*. Local holomorphic volume amplitudes exist as frames

$$
\Omega_i\in\Gamma(U_i,K_X),
$$

but on overlaps they glue by a nontrivial cocycle

$$
\Omega_i=g_{ij}\Omega_j,
\qquad
g_{ij}\in\mathcal O_X^\times.
$$

Topological triviality says the underlying continuous line can be globally trivialized. Holomorphic nontriviality says the local complex presentations cannot be made into one global holomorphic amplitude. This is close to the proposed meaning of scale as an obstruction in descent: local frames exist, but their comparisons carry irreducible transition data.

The caution is decisive. The cocycle is not yet physical scale, causal charge, or mass. To make that interpretation one must construct a positive real character

$$
|g_{ij}|:
U_i\cap U_j\longrightarrow\mathbb R_{>0}
$$

with a named relation to the causal-scale valuation, and then show how its determinant density enters the physical state or transfer carrier. Without this lift, the canonical bundle is an illuminating geometric analogue rather than the origin of $E_*$ or the Yang--Mills gap.

## The construction chain to test

The strongest current programme can be written as

$$
\boxed{
\begin{aligned}
(S^6,J_{\mathrm{oct}})
&\dashrightarrow
(S^6,J_{\mathrm{int}}),\\
(S^6,J_{\mathrm{int}})
&\xrightarrow{\ \det\ }
K_X^{\pm1}\quad\text{of weight }3,\\
K_X^{\pm1}
&\xrightarrow{\ \lVert\cdot\rVert^2\ }
\text{positive density of weight }6,\\
\text{density}
&\dashrightarrow
\text{gauge-invariant OS carrier},\\
\text{OS carrier}
&\dashrightarrow
H_{\mathrm{YM}}/E_*,\\
H_{\mathrm{YM}}
&\ge
\gamma E_*(1-P_\Omega).
\end{aligned}
}
$$

Only the determinant and Hermitian-square arrows in the middle are presently exact once the relevant structures are chosen. The first arrow, the QFT carrier change, the time-translation identification, the exclusion of lower sectors, and the uniform coercivity theorem are open.

The number to pre-register is therefore not just $36$. It is a fork:

$$
\boxed{
\gamma
\in
\{9,36\}
}
$$

for the determinant-amplitude and discriminant-amplitude branches of the one-sided second-order model, respectively. A derivation must decide the branch before comparing either number with a glueball mass.

## Failure conditions

- If an auxiliary invariant from one construction fails separate audit, only the bridge using that invariant closes; the existence of $J_{\mathrm{int}}$ remains available from the other proof routes.
- If no natural comparison relates $J_{\mathrm{oct}}$ and $J_{\mathrm{int}}$, their coexistence on one smooth sphere is not a physical duality.
- If no quantization or factorization functor takes $\mathcal O_X$ to a positive local operator net, integrable complex presentation is not the algebra of QFT.
- If the manuscript's toric $A_2$ cannot be mapped to the analytic or Weyl $A_2$ discriminant, its hexagon does not support the gauge-measure bridge.
- If the discriminant is the ordinary Weyl measure density, the natural Hilbert-amplitude threshold is $9$, not $36$.
- If no physical state lives in a squared determinant or density carrier, the weight-six-amplitude branch has no owner.
- If the physical Hamiltonian is the square root of the constructed second-order operator, the energy factor is $3$ or $6$, not $9$ or $36$.
- If lower gauge-invariant sectors survive, none of these weights is the mass gap merely because it occurs in the geometry.
- If the holomorphic canonical cocycle has no map to causal scale, its nontrivial descent is not a mass-generating obstruction.

## Provisional verdict

The integrable $S^6$ result materially strengthens the philosophical architecture. One and the same smooth six-sphere can support a canonical octonionic almost-complex geometry and a different integrable complex presentation. That makes the phrase “octonionic ground, locally complex appearance” mathematically imaginable in a way it was not before.

The result does not supply the bridge between those structures, and integrability does not itself supply QFT. Its most concrete contribution to the mass-gap exploration is the determinant fork:

$$
\boxed{
\text{rank-three complex amplitude}
\xrightarrow{\text{Hermitian square}}
\text{sixth-weight invariant density}
\xrightarrow{\text{second-order dynamics?}}
6^2.
}
$$

The first arrow is geometry. The second is a proposed dynamics. Standard Hilbert-space typing takes the square root of the density and predicts $3^2=9$, so $6^2=36$ requires a nonstandard but precisely specifiable carrier. That is now the clean theorem target.

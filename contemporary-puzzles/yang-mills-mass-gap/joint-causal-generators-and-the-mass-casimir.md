# Joint Causal Generators and the Mass Casimir

A positive mass need not be a gap in any single causal generator. In $1+1$ dimensions, oppositely scaling null-translation generators can each have spectrum down to zero while their product, the mass Casimir in that setting, stays uniformly positive. In higher dimensions the full invariant requires all translation components. This supplies a precise Copernican reversal for the modular programme: use modular inclusions, if possible, to reconstruct causal translation kinematics; define mass only from the completed joint representation; and prove a full-Casimir coercivity estimate on the physical vacuum complement. A one-line operator arithmetic--geometric-mean argument then converts that estimate into the Hamiltonian mass gap.

**Status: [EXACT MODULAR NO-GO BOUNDARIES; EXACT JOINT-SPECTRAL THEOREM; EXACT MASSIVE REPRESENTATION WITNESS; OPEN YANG--MILLS RECONSTRUCTION].** Nothing below derives the Yang--Mills scale or constructs its continuum carrier. It identifies the first modular route that is not ruled out by the dilation no-gap theorem.

## Why one modular operator is the wrong target

For faithful normal weights \(\varphi,\psi\) on a von Neumann algebra, the Connes derivative

$$
u_t:=[D\varphi:D\psi]_t
$$

generally satisfies the twisted law

$$
u_{s+t}
=
u_s\,\sigma_s^\psi(u_t),
\tag{J1}
$$

not \(u_{s+t}=u_su_t\). It is transition data between modular presentations, not generally a unitary representation of \(\mathbb R\), so Stone's theorem supplies no single self-adjoint generator. [[library/une-classification-des-facteurs-de-type-iii/inq|Connes's type-III classification]] is the primary source for the cocycle and modular-spectrum framework.

Even the exceptional group case cannot produce a nontrivial positive Hamiltonian between normalized faithful states. If \(u_t\) is an ordinary group, [[library/the-radon-nikodym-theorem-for-von-neumann-algebras/inq|Pedersen--Takesaki theory]] gives

$$
u_t=h^{it},
\qquad
h\ \text{affiliated with the }\psi\text{-centralizer},
\qquad
\psi(h)=1.
\tag{J2}
$$

Put \(K=\log h\). If \(K\geq0\), then \(h\geq1\), and faithfulness plus \(\psi(h-1)=0\) gives \(h=1\). The same argument applied to \(-K\) handles \(K\leq0\). Therefore

$$
\boxed{
K\ \text{semidefinite}
\quad\Longrightarrow\quad
K=0,
\quad
\varphi=\psi.}
\tag{J3}
$$

Relative-entropy positivity is a scalar expectation inequality; it does not make the relative modular logarithm a positive operator. For a \(\sigma\)-finite type-\(\mathrm{III}_1\) factor, Connes's invariant gives \(\sigma(\Delta_\psi)=[0,\infty)\) and hence \(\sigma(\log\Delta_\psi)=\mathbb R\) for every faithful normal state. An ordinary modular logarithm is therefore intrinsically two-sided and gapless.

A half-sided modular inclusion contains more data than a state pair and does reconstruct a positive generator \(P\). But its modular covariance has the form

$$
\Delta_M^{it}P\Delta_M^{-it}
=
e^{-2\pi t}P.
\tag{J4}
$$

Consequently \(P=0\) or \(\sigma(P)=[0,\infty)\). [[library/extension-of-borchers-structure-theorem/inq|Araki--Zsido]] therefore supplies an oriented null-translation skeleton, not a massive clock Hamiltonian. This is not a failure of the construction. It is evidence that mass has been sought at the wrong algebraic level.

## The joint-null theorem

Work first in natural units in $1+1$ dimensions, or on a declared zero-transverse-momentum sector. Let \(P_+,P_-\geq0\) be strongly commuting self-adjoint operators on \(\mathcal H\). Their products and square roots are defined by the joint spectral calculus. Suppose a vacuum projection \(P_0\) reduces both generators and

$$
P_+P_0=P_-P_0=0.
$$

Define

$$
H:=\frac{P_++P_-}{2},
\qquad
M^2:=P_+P_-.
\tag{J5}
$$

For nonnegative numbers \(x,y\), \((x+y)/2\geq\sqrt{xy}\). Joint functional calculus therefore gives the operator inequality

$$
H\geq M.
\tag{J6}
$$

If the joint Casimir has the vacuum-complement lower bound

$$
M^2
\geq
m_*^2(1-P_0),
\qquad m_*>0,
\tag{J7}
$$

then operator monotonicity of the square root and (J6) yield

$$
\boxed{
H
\geq
m_*(1-P_0).}
\tag{J8}
$$

Thus two individually gapless positive generators can jointly force an ordinary energy gap. In this low-dimensional realization (J7) is the mass-Casimir bound. In $3+1$ dimensions, $P_+P_-=H^2-P_z^2=\mathcal C+\mathbf P_\perp^2$ in natural units, so the Yang--Mills target is instead the full-Casimir estimate (J15), not merely (J7) for one null pair and not a positive lower edge for either \(P_+\) or \(P_-\) separately.

## Exact massive witness

On \(L^2(\mathbb R,\mathrm d\theta)\), let

$$
(P_+f)(\theta)=m e^\theta f(\theta),
\qquad
(P_-f)(\theta)=m e^{-\theta}f(\theta),
\qquad m>0.
\tag{J9}
$$

Each spectrum is \([0,\infty)\), but

$$
P_+P_-=m^2I,
\qquad
H=m\cosh\theta,
\qquad
\sigma(H)=[m,\infty).
\tag{J10}
$$

The boost shifts rapidity and rescales the two generators reciprocally. Hence the separate value of either null component is frame-dependent, while their product is invariant. [[library/modular-localization-and-wigner-particles/inq|Brunetti--Guido--Longo modular localization]] is useful here as a boundary marker: it constructs localization from an already supplied positive-energy Poincare representation and therefore does not derive the mass parameter in (J9). [[contemporary-puzzles/yang-mills-mass-gap/receipts/joint_null_casimir_receipt.py|The joint-null receipt]] checks the finite arithmetic witness and reciprocal-rescaling invariance; it is not a spectral proof.

Equation (J10) distinguishes two rescalings that are often conflated:

$$
(P_+,P_-)
\mapsto
(e^sP_+,e^{-s}P_-)
\tag{J11}
$$

is a boost/frame change and preserves \(M^2\), whereas

$$
(P_+,P_-)
\mapsto
(aP_+,aP_-)
\tag{J12}
$$

changes \(M\) by \(a\). The first is kinematics. The second requires the dimensional yardstick. A dimensionless geometry may fix an invariant ratio, but it cannot fix the common physical scale merely by choosing a frame.

## Casimir solder to a distinction frame

The regional distinction construction supplies a dimensionless form \(\mathfrak d\) on physical vacuum tangents. Let the reconstructed translation representation have commuting generators \((H,\mathbf P)\) and positive-energy joint spectrum. Its energy-squared Casimir is

$$
\mathcal C
:=
H^2-c^2\mathbf P^2
=
M^2c^4.
\tag{J13}
$$

Suppose, on one common form domain, that the observable atlas is complete and the reconstructed Casimir charges it:

$$
\mathfrak d[\Psi]
\geq
\kappa\lVert(1-P_0)\Psi\rVert^2,
\qquad
\langle\Psi,\mathcal C\Psi\rangle
\geq
\eta_C E_*^2\mathfrak d[\Psi],
\tag{J14}
$$

where \(\kappa,\eta_C>0\) are dimensionless and \(E_*\) is fixed independently. Then

$$
\mathcal C
\geq
\eta_C\kappa E_*^2(1-P_0).
\tag{J15}
$$

The spectrum condition gives \(H^2=\mathcal C+c^2\mathbf P^2\geq\mathcal C\), so

$$
\boxed{
H
\geq
E_*\sqrt{\eta_C\kappa}\,(1-P_0).}
\tag{J16}
$$

This is the Casimir version of the energy-solder theorem. It says exactly what the proposed geometric operator must operate on and what it must return: \(\mathfrak d\) acts on the full physical vacuum tangent carrier and returns dimensionless distinguishability; \(\mathcal C\) acts on the reconstructed Poincare carrier and returns invariant energy squared; the solder compares their quadratic forms; the yardstick supplies units only once.

## Yang--Mills stopping condition

A modular execution of this route must construct, rather than assume:

1. a coherent family of modular inclusions or intersections on one physical carrier, sufficient to reconstruct all translation generators and their strong commutation relations;
2. a unique invariant vacuum, a positive-energy Poincare representation, and an observable net with locality and gauge compatibility;
3. identification of that carrier and clock with the Osterwalder--Schrader or other constructive Yang--Mills carrier;
4. a canonical regional-plus-flux distinction form such as [[regional-relative-entropy-frames]], with a regulator-uniform lower frame bound;
5. the Casimir-form comparison in (J14), normalized without the desired spectrum; and
6. persistence of the product \(E_*\sqrt{\eta_C\kappa}\) through infinite volume and continuum removal.

One half-sided inclusion supplies only an affine translation--dilation pair. A coherent family may reconstruct more kinematics, but it does not automatically remove the nonvacuum null cone or timelike hyperboloids accumulating at zero mass. Those exclusions are precisely the full-carrier coercivity theorem. The Copernican gain is not that the theorem disappears; it is that its correct object is exposed. Mass is not friction in one causal direction. It is the invariant lower bound produced only after the causal directions have become one mutually compatible spacetime representation.

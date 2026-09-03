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

## Several modular directions require a compatibility theorem

Constructing several half-sided modular inclusions in one environment does not automatically produce one translation representation. [[library/relative-positions-of-half-sided-modular-inclusions/inq|Koot's relative-position analysis]] characterizes when inclusions among the corresponding standard subspaces have the stronger half-sided property and exhibits cases where an ordinary inclusion does not. The associated positive one-parameter groups commute only under additional relative-position compatibility. Thus independently writing \(P_+\) and \(P_-\) is not yet permission to multiply them.

The positive precedent is [[library/modular-theory-and-the-reconstruction-of-four-dimensional-quantum-field-theories/inq|Kähler--Wiesbrock reconstruction]]: a finite constellation of von Neumann algebras in specified mutual modular position can reconstruct a \(3+1\)-dimensional Poincare representation and a local observable net. Its lesson is the order of construction

$$
\boxed{
\text{modular constellation}
\longrightarrow
U(a,\Lambda)
\longrightarrow
(P_\mu)\text{ with joint spectral measure}
\longrightarrow
\mathcal C
\longrightarrow
\text{Casimir coercivity}.}
\tag{J4a}
$$

The first three arrows are kinematic reconstruction. They do not select a massive representation, remove the null cone, or bound the positive Casimir spectrum away from zero. Indeed, [[library/modular-localization-and-wigner-particles/inq|Brunetti--Guido--Longo]] also construct localization from a Poincare representation whose Wigner mass and spin data are already supplied. Type-\(\mathrm{III}_1\) locality is compatible with both massless and massive input representations; it cannot choose between them.

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

[[paired-scale-filtrations-and-the-invariant-incidence-wall#Every spatial direction recovers the full Casimir|The all-direction theorem]] closes this directional loophole exactly. For every unit vector \(\mathbf n\), put \(P_\pm(\mathbf n)=H\pm c\mathbf P\cdot\mathbf n\). Then

$$
P_+(\mathbf n)P_-(\mathbf n)
=
\mathcal C+c^2\bigl(|\mathbf P|^2-(\mathbf P\cdot\mathbf n)^2\bigr).
$$

A common lower floor for these products in every direction of any countable dense subset of \(S^2\) is equivalent to the full Casimir floor. One null pair gives only a directional overestimate; the all-cut family is tomographically complete. The theorem still does not create the positive constant: that must come from the proposed incidence wall or another non-spectral geometric construction.

## Energy gap and Casimir floor are equivalent only after Lorentz reconstruction

Let \(U(a,\Lambda)\) be a unitary representation of the connected Poincare group with unique invariant vacuum projection \(P_0\), and assume the full joint spectrum condition

$$
\operatorname{supp}E_{(H/c,\mathbf P)}
\subseteq
\overline V_+.
$$

Let \((H,\mathbf P)\) be its strongly commuting translation generators and

$$
\mathcal C=H^2-c^2\mathbf P^2\geq0.
$$

Then, for every \(\Delta>0\),

$$
\boxed{
H\geq\Delta(1-P_0)
\quad\Longleftrightarrow\quad
\mathcal C\geq\Delta^2(1-P_0).}
\tag{J8a}
$$

The reverse implication is immediate from \(H^2=\mathcal C+c^2\mathbf P^2\) and positivity of \(H\). For the forward implication, use the Lorentz-invariant support of the joint spectral measure. A nonvacuum null orbit contains energies arbitrarily close to zero under boosts, contradicting the Hamiltonian lower bound. A timelike orbit with invariant energy-squared \(m^2c^4<\Delta^2\) contains its rest point, and hence spectral-support points with energy below \(\Delta\), again contradicting the bound. Therefore every nonvacuum orbit has \(\mathcal C\geq\Delta^2\).

This equivalence does not exist at a generic finite lattice regulator, which has a transfer or Hamiltonian generator but no exact Poincare joint spectrum. The regulator proof should therefore establish a Hamiltonian-form bound first, reconstruct Lorentz covariance in the continuum, and only then retype the result as a Casimir floor. Introducing a “lattice Casimir” by notation would assume the missing kinematics.

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

[[resolvent-logistic-scale-transform]] gives this witness an exact scale-coordinate reading. Applying the effect--odds transform to \(P_+/E_*\) and \(P_-/E_*\) assigns center operators

$$
N_{c,+}=-\log(P_+/E_*),
\qquad
N_{c,-}=-\log(P_-/E_*)
$$

on their joint positive spectral carrier. Under (J11) the first center shifts by \(-s\) and the second by \(+s\), but

$$
\boxed{
\frac{N_{c,+}+N_{c,-}}2
=
-\log(M/E_*)}
\tag{J12a}
$$

is invariant. Thus each causal generator may remain gapless and have centers extending without bound, while a mass floor is exactly a ceiling on their invariant mean center. The universal logistic width of the scale readout does not supply that ceiling.

[[compensated-incidence-response-and-four-dimensional-balance]] shows that an exact ceiling is only the neutral-response member of a larger theorem. If an independently constructed response \(R\) acts on the image of the invariant presentation \(e^{-pA_M}\), the relevant joint object is the closed pullback \(C=\overline{R^{1/2}e^{-pA_M}}\). Its lower singular-value bound can survive even when \(A_M\) is unbounded, provided the response compensates every escaping scale channel. When \(R\) is a function of \(A_M\), this construction retains reciprocal frame invariance because \(A_M\) does. It still requires a separate comparison with the physical Casimir: a frame-invariant response operator is not thereby a translation generator or mass.

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
\|\mathcal C^{1/2}\Psi\|^2
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

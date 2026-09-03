# Jordan Idempotency and the Stabilizer Gap

Jordan idempotency supplies an exact finite model of the proposed Copernican turn. A point-like alternative is constrained by \(e\circ e=e\); the Hessian of its squared constraint defect has zero modes precisely along changes of presentation within the idempotent orbit and a unit positive edge normal to that orbit. In the exceptional Jordan algebra, an order-three orientation \(w\) and a trace-two idempotent \(\ell\) have the faithfully acting Standard Model gauge group as their stabilizer. An exact modular-rank calculation shows that the natural continuous constraints on \((\ell,B)\) have no infinitesimal zero modes beyond the forty-dimensional flag orbit, while a reduced oriented bundle has canonical Hessian spectrum \(0^{(40)}\oplus1^{(4)}\). The deeper product therefore gives the observed stabilizer, an explicit orientation residue, and finite normal rigidity. What remains open is the physical synthesis: justify the response carrier, realize a flag or normal-holonomy field on a Type-III/OS Yang--Mills carrier, and prove a regulator-uniform comparison with the physical mass Casimir.

**Status: [EXACT] for the Peirce linearization, idempotency-defect Hessian, order-three orientation consequences, and reduced oriented-flag spectrum; [EXACT COMPUTER-ASSISTED] for the kernel of the displayed exceptional continuous-flag constraint at the standard flag; [EXACT CITED] for the exceptional-Jordan stabilizer, order-three centralizer, transitivity, and triality statements; [CONSTRUCTION] for the physical response carrier and normal-holonomy use; [OPEN] for physical chirality, Type-III realization, four-dimensional Yang--Mills recovery, continuum coercivity, and dimensional calibration.**

## Pointing begins with an idempotent equation

Let \(J\) be a finite-dimensional Euclidean Jordan algebra with product \(x\circ y\), unit \(1\), and associative inner product

$$
\langle x\circ y,z\rangle
=
\langle x,y\circ z\rangle.
\tag{JI1}
$$

An idempotent is an element

$$
e\circ e=e.
\tag{JI2}
$$

In the usual Jordan interpretation, idempotents are yes--no alternatives. A primitive idempotent is an algebraic point or pure alternative. This does not make it an actually obtained fact: a state, instrument, outcome, and persistent record are still separate structures. The useful claim is narrower:

> Idempotency is an algebraic equation for being sharply pointed rather than a probability law over possible pointings.

Define the idempotency defect and its squared norm by

$$
C(x):=x\circ x-x,
\qquad
V(x):=\frac12\lVert C(x)\rVert^2.
\tag{JI3}
$$

The defect vanishes on every idempotent and measures departure from the algebraic point locus. No clock, energy, \(\hbar\), or spacetime metric occurs.

## The Peirce Hessian theorem

Let \(L_e:J\to J\) denote Jordan multiplication by \(e\):

$$
L_eh=e\circ h.
\tag{JI4}
$$

Peirce theory gives the orthogonal decomposition

$$
\boxed{
J
=
J_1(e)\oplus J_{1/2}(e)\oplus J_0(e),
\qquad
L_e|_{J_\lambda(e)}=\lambda I,
\quad
\lambda\in\left\{1,\frac12,0\right\}.}
\tag{JI5}
$$

The linearization of (JI3) at an idempotent is

$$
\boxed{
\mathrm DC_e
=
2L_e-I.}
\tag{JI6}
$$

Since \(C(e)=0\), the Hessian of \(V\) contains no second-derivative remainder:

$$
\operatorname{Hess}_eV(h,k)
=
\langle \mathrm DC_eh,\mathrm DC_ek\rangle.
\tag{JI7}
$$

Its associated positive operator is therefore

$$
\boxed{
A_e
:=
(\mathrm DC_e)^*\mathrm DC_e
=
(2L_e-I)^2
=
P_1+P_0
=
I-P_{1/2},}
\tag{JI8}
$$

where \(P_\lambda\) is the Peirce projection onto \(J_\lambda(e)\). Consequently,

$$
\boxed{
\ker A_e=J_{1/2}(e),
\qquad
A_e|_{J_1(e)\oplus J_0(e)}=I.}
\tag{JI9}
$$

This is an exact dimensionless normal gap. It is forced by the polynomial \(x^2-x\), not inferred from a spectral fit.

For a fixed-rank idempotent orbit, differentiating \(e(t)^2=e(t)\) gives

$$
(2L_e-I)\dot e(0)=0,
\tag{JI10}
$$

so every tangent direction lies in \(J_{1/2}(e)\). In the simple Euclidean Jordan examples used here, the automorphism group acts transitively on the fixed-rank idempotents and

$$
T_e(\operatorname{Aut}(J)\cdot e)
=
J_{1/2}(e).
\tag{JI11}
$$

Thus the zero modes of \(A_e\) move one valid pointing to another. They do not leave the algebraic fact locus. The normal directions \(J_1(e)\oplus J_0(e)\) change the eigenvalues away from \(0\) and \(1\), and the Hessian charges them with unit stiffness.

The exact quotient statement is

$$
\boxed{
J/T_e(\operatorname{Aut}(J)\cdot e)
\cong
J_1(e)\oplus J_0(e),
\qquad
\overline A_e=I.}
\tag{JI12}
$$

The unpointed orbit is therefore degenerate while the normal quotient is gapped. This is a finite theorem-shaped instance of

$$
\text{scale-free or presentation-degenerate whole}
\longrightarrow
\text{positive pointed quotient}.
\tag{JI13}
$$

The normalization firewall remains. Replacing \(V\) by \(\alpha V\) replaces \(A_e\) by \(\alpha A_e\). The Jordan product and trace form may select a preferred dimensionless convention, but they do not turn its unit edge into MeV or inverse seconds.

## The exceptional idempotent witness

For

$$
J=\mathfrak h_3(\mathbb O),
\qquad
\operatorname{Aut}(J)=F_4,
\tag{JI14}
$$

a primitive idempotent has Peirce dimensions

$$
\dim J_1(e)=1,
\qquad
\dim J_{1/2}(e)=16,
\qquad
\dim J_0(e)=10.
\tag{JI15}
$$

The primitive-idempotent orbit is

$$
\mathbb OP^2
\cong
F_4/\operatorname{Spin}(9),
\tag{JI16}
$$

whose dimension \(52-36=16\) agrees with the Hessian kernel. Hence

$$
\operatorname{spec}(A_e)
=
\{0^{(16)},1^{(11)}\}.
\tag{JI17}
$$

This is not yet the Standard Model flag and not a Yang--Mills Hamiltonian. It is the cleanest exceptional finite witness that **a point, its presentation orbit, its stabilizer, and a positive normal response arise from one algebraic product**.

An ordered complete Jordan frame \((e_1,e_2,e_3)\) has orbit

$$
F_4/\operatorname{Spin}(8).
\tag{JI18}
$$

The three off-diagonal Peirce slots are copies of \(\mathbb O\), and the frame stabilizer acts on them as the vector, left-handed real-spinor, and right-handed real-spinor representations

$$
8_v\oplus8_s\oplus8_c.
\tag{JI19}
$$

The total tangent dimension \(8+8+8=24\) equals \(52-28\). The setwise stabilizer of an unordered frame also contains a finite permutation/triality extension, which does not change this dimension. This is a rigorous place where left and right occur as distinct representation slots before any four-dimensional field theory is written. Triality and the words *left* and *right* do not by themselves select weak chirality, a Lorentzian \(\gamma_5\), or a chiral fermion spectrum.

## The familiar gauge group is stabilizer data

[[library/standard-model-from-exceptional-jordan-algebra/inq|Baez and Schwahn]] prove that for a nested complex Jordan flag

$$
X\cong\mathfrak h_2(\mathbb C)
\subset
B\cong\mathfrak h_3(\mathbb C)
\subset
\mathfrak h_3(\mathbb O),
\tag{JI20}
$$

one has

$$
\boxed{
\operatorname{Stab}_{F_4}(X)
\cap
\operatorname{Stab}_{F_4}(B)_0
\cong
S(U(2)\times U(3))
\cong
\frac{U(1)\times SU(2)\times SU(3)}{\mathbb Z_6}.}
\tag{JI21}
$$

The quotient by \(\mathbb Z_6\) is the faithfully acting group; writing the direct product alone suppresses a real global distinction.

This is the desired order-of-explanation reversal:

$$
\boxed{
\text{exceptional Jordan whole}
+\text{selected complex flag}
\longrightarrow
\text{observed connected stabilizer}.}
\tag{JI22}
$$

The group is no longer inserted as the primordial grammar and then asked to explain why nature departs from it. It is the automorphism group that remains after an algebraic presentation has been pointed.

The identity-component qualifier is informative. The full intersection with \(\operatorname{Stab}(B)\) contains another component acting antiunitarily on the complex subalgebra. Passing to \(\operatorname{Stab}(B)_0\) removes that antiunitary component. This orientation is realized explicitly below by Yokota's order-three automorphism \(w\): the antiunitary component exchanges \(w\) with \(w^{-1}\) while leaving \(B\) fixed. It is an exact asymmetric datum, not yet a derivation of physical CP violation or weak chirality.

Calling this “spontaneous symmetry breaking” is optional language imposed after the fact. The exact mathematics says only:

1. the unpointed whole admits \(F_4\) automorphisms;
2. a pointed complex flag is preserved by the subgroup (JI21); and
3. all flags in the declared orbit are related by the whole action.

A dynamical symmetry-breaking claim additionally requires a potential, state, selection process, and physical fields. The stabilizer theorem itself is kinematic and prior to that story.

## A transparent associative shadow

The same stabilizer and Hessian pattern appears in the ordinary Euclidean Jordan algebra \(\mathfrak h_5(\mathbb C)\). Let

$$
p=
\operatorname{diag}(1,1,0,0,0).
\tag{JI23}
$$

Its preimage stabilizer under the \(SU(5)\) conjugation action is \(S(U(2)\times U(3))\). The action has kernel \(\mathbb Z_5\), so the faithfully acting group is \(PSU(5)\) and the faithful stabilizer is the corresponding quotient by \(\mathbb Z_5\). The rank-two projector orbit nevertheless has dimension

$$
\dim SU(5)-\dim S(U(2)\times U(3))
=
24-12
=12.
\tag{JI24}
$$

Relative to \(\mathbb C^5=\mathbb C^2\oplus\mathbb C^3\), a Hermitian perturbation has blocks

$$
h=
\begin{pmatrix}
a&b\\
b^*&d
\end{pmatrix},
\tag{JI25}
$$

and

$$
\mathrm DC_p(h)
=
ph+hp-h
=
\begin{pmatrix}
a&0\\
0&-d
\end{pmatrix}.
\tag{JI26}
$$

The twelve real off-diagonal directions \(b\) are tangent to the orbit and have zero Hessian cost. In the full twenty-five-dimensional ambient algebra, the \(4+9=13\) block-diagonal directions are normal and have unit Hessian cost. Restricting instead to the trace-two affine slice removes one scalar normal direction. This is only an associative shadow—the exceptional theorem (JI21) is stronger—but it displays the stabilizer/quotient/gap mechanism without octonionic calculation.

## The constraint-orbit Hessian theorem

The preceding calculation is an instance of a general exact lemma. Let a compact group \(G\) act orthogonally on finite-dimensional inner-product spaces \(E\) and \(F\). Let

$$
\mathcal C:E\longrightarrow F
\tag{JI27}
$$

be a smooth equivariant constraint map, let \(x\in\mathcal C^{-1}(0)\), and suppose

$$
\ker\mathrm D\mathcal C_x
=
T_x(G\cdot x).
\tag{JI28}
$$

For

$$
\mathcal V(y)=\frac12\lVert\mathcal C(y)\rVert^2,
\tag{JI29}
$$

one has

$$
\boxed{
\operatorname{Hess}_x\mathcal V
=
(\mathrm D\mathcal C_x)^*
\mathrm D\mathcal C_x.}
\tag{JI30}
$$

Its kernel is the orbit tangent. On the orthogonal normal space

$$
N_x:=T_x(G\cdot x)^\perp,
\tag{JI31}
$$

finite dimensionality and (JI28) give

$$
\boxed{
\operatorname{Hess}_x\mathcal V|_{N_x}
\geq
\kappa_x I_{N_x},
\qquad
\kappa_x
=
\sigma_{\min}\!\left(
\mathrm D\mathcal C_x|_{N_x}
\right)^2
>0.}
\tag{JI32}
$$

If \(H=G_x\) is the stabilizer, equivariance makes the Hessian \(H\)-equivariant. Along the entire orbit it is transported by conjugation, so the normal spectrum and \(\kappa_x\) are the same at every pointing. The whole retains covariance without turning every local presentation into the same object.

This theorem says exactly what a wall or obstruction must do: its linearized failure map is first order and may retain orientation; its square is a positive response whose kernel contains only presentation changes.

Existence alone would be cheap. After choosing any invariant ambient metric, squared distance to a compact orbit already has the normal projection as its Hessian. Such a manufactured potential merely restates that the orbit has a normal bundle. The explanatory burden is to derive \(\mathcal C\), its relative weights, and its orientation data from the algebraic product itself, as idempotency does in (JI3)--(JI9).

## Exact quotient-response corollary

There is an exact finite answer to how this whole response can descend without choosing a representative. Rename the constrained point \(f\) and put \(A_f=(\mathrm D\mathcal C|_f)^*(\mathrm D\mathcal C|_f)\). Let

$$
q_O:E\twoheadrightarrow K_O
\tag{JI32a}
$$

be a coisometric quotient, so \(q_Oq_O^*=I_{K_O}\), and define the response of a retained class by

$$
a_O(y)
:=
\inf_{q_Ox=y}\langle x,A_fx\rangle.
\tag{JI32b}
$$

If \(L_O=\operatorname{Ran}q_O^*\), then Anderson--Trapp shorting gives

$$
\boxed{
A_O
=
q_OS_{L_O}(A_f)q_O^*,
\qquad
a_O(y)=\langle y,A_Oy\rangle.}
\tag{JI32c}
$$

For a further quotient \(q_1=r_{12}q_2\), fibrewise infima associate:

$$
a_1(z)
=
\inf_{r_{12}y=z}a_2(y).
\tag{JI32d}
$$

The positive-floor condition is equally sharp:

$$
\boxed{
A_O\geq\kappa I_{K_O}
\iff
A_f\geq\kappa q_O^*q_O
\iff
\operatorname{Ran}q_O^*
\subseteq
\operatorname{Ran}A_f^{1/2}.}
\tag{JI32e}
$$

Under the constraint-orbit hypothesis (JI28), \(\operatorname{Ran}A_f^{1/2}=T_f(G\cdot f)^\perp\). Hence a quotient can retain a positive edge only if

$$
\boxed{
T_f(G\cdot f)\subseteq\ker q_O.}
\tag{JI32f}
$$

Every zero-cost change of presentation must be genuinely invisible in the retained class; mere transversality is insufficient. If \(q_O\) intertwines the stabilizer action, \(A_O\) is stabilizer-equivariant. This is already a clean whole-to-part theorem, but it does not construct the quotient that represents a physical local fact.

## The missing exceptional-flag operator

The next non-numerological construction is not to guess another group. It is to construct \(\mathcal C_{\mathrm{flag}}\) whose clean or Morse--Bott zero locus is the desired oriented flag orbit. Surjectivity of its generally overdetermined Jacobian is unnecessary; the needed condition is local constant rank with kernel equal to the orbit tangent.

The Baez--Schwahn proof gives a more economical encoding than two independent subspace projections. If \(X\subset B\) is a flag of the required type and \(\ell\) is the unit of \(X\), then \(\ell\) is a trace-two idempotent and

$$
\boxed{
X
=
E_1^B(\ell)
:=
\{x\in B:\ell\circ x=x\}.}
\tag{JI33}
$$

Conversely, a trace-two idempotent in \(B\cong\mathfrak h_3(\mathbb C)\) determines such an \(X\cong\mathfrak h_2(\mathbb C)\). Thus \(P_X\) is redundant. Preserving \(X\) preserves its unit \(\ell\), while preserving \(B\) and \(\ell\) preserves (JI33). The connected stabilizer intersection in (JI21) can therefore be read as the stabilizer of the pointed pair \((\ell,B)\) inside \(\operatorname{Stab}(B)_0\).

Use the canonical trace inner product on \(J\) and take \(B\) directly in the Grassmannian \(\operatorname{Gr}_9(J)\), with orthogonal projection \(P_B\). The continuous flag variable is

$$
f_{\mathrm c}=(\ell,P_B).
\tag{JI34}
$$

A candidate equivariant constraint package is

$$
\begin{aligned}
\ell\circ\ell-\ell&=0,
&
\operatorname{tr}\ell-2&=0,
\\
P_B1-1&=0,
&
P_B\ell-\ell&=0,
\\
(I-P_B)m(P_B\otimes P_B)&=0,
&&
\end{aligned}
\tag{JI35}
$$

where \(m(u,v)=u\circ v\). Grassmannian membership already fixes an orthogonal rank-nine projection, so no projector-defect term is counted twice. The equations enforce a unital nine-dimensional Jordan subalgebra containing \(\ell\); one must still restrict to or characterize the stratum \(B\cong\mathfrak h_3(\mathbb C)\), rather than assume every solution has that type.

[[order-three-orientation-and-the-exceptional-stabilizer]] supplies the missing orientation explicitly. Yokota's real-linear order-three Jordan automorphism \(w\in F_4\) obeys

$$
\operatorname{Fix}_J(w)=B,
\qquad
C_{F_4}(w)=\operatorname{Stab}_{F_4}(B)_0,
\qquad
P_B=\frac{1+w+w^2}{3}.
\tag{JI36}
$$

The inverse \(w^2\) fixes the same \(B\), while the antiunitary component exchanges \(w\leftrightarrow w^2\). The signed residue

$$
I_B=\frac{w-w^2}{\sqrt3},
\qquad
I_B^2=-(1-P_B),
\tag{JI36i}
$$

is the orthogonal complex structure on \(B^\perp\) that the cyclic average forgets. Thus the orientation lift is not an added label: the two oriented points are \((\ell,w)\) and \((\ell,w^2)\). The real pair \((\ell,P_B)\) is their common unoriented image. Moreover,

$$
P_X=P_B\bigl(2L_\ell^2-L_\ell\bigr),
\tag{JI36j}
$$

so the entire oriented flag is generated by \((\ell,w)\). The algebra canonically supplies the two-sheeted lift and an orientation-odd tensor; it does not select one sheet as physically actual or turn that orientation into weak chirality.

The dimensions now expose the geometry. The \(B\)-subalgebra orbit has dimension \(52-16=36\), while the trace-two idempotents inside a fixed \(B\cong\mathfrak h_3(\mathbb C)\) form \(\operatorname{Gr}_2(\mathbb C^3)\cong\mathbb CP^2\), of real dimension four. Hence the pointed-pair orbit has dimension

$$
36+4=40=52-12,
\tag{JI36a}
$$

as required by the twelve-dimensional connected stabilizer (JI21).

Denote the continuous defect in (JI35), restricted to the correct algebra-type stratum, by \(\mathcal C_{\mathrm{flag}}(\ell,P_B)\). It pulls back to either sheet of the \(w\)-orientation cover but does not distinguish those sheets.

The proposed whole response is

$$
\boxed{
A_{\mathrm{flag},f}
:=
\left(\mathrm D\mathcal C_{\mathrm{flag}}|_f\right)^*
\left(\mathrm D\mathcal C_{\mathrm{flag}}|_f\right).}
\tag{JI37}
$$

It operates on infinitesimal deformations of the continuous **pointing structure** \(f_{\mathrm c}=(\ell,P_B)\), not on particles moving in a pre-existing spacetime. Globally, (JI37) is an equivariant field of conjugate Hessians over the flag orbit. The orientation-odd datum \(I_B\) lives on its double cover and is not recovered by this even response.

For the standard \(B=\mathfrak h_3(\mathbb C)\subset\mathfrak h_3(\mathbb O)\) and \(\ell=\operatorname{diag}(1,1,0)\), the continuous ambient tangent has dimension

$$
\dim J+\dim\operatorname{Hom}(B,B^\perp)
=
27+9\cdot18
=
189.
\tag{JI37a}
$$

[[contemporary-puzzles/yang-mills-mass-gap/receipts/exceptional_flag_linearization_receipt.py|The exact modular-rank receipt]] constructs the octonionic Jordan table, linearizes every constraint in (JI35), and obtains an integral \(874\times189\) Jacobian of rank \(149\) modulo the prime \(1{,}000{,}003\). A nonzero modular minor is a nonzero integer minor, so the real rank is at least \(149\) and the real nullity is at most forty. Equivariance puts the forty-dimensional \(F_4\)-orbit tangent inside the kernel. Therefore

$$
\boxed{
\ker D_{\mathrm{flag},f}
=
T_f(F_4\cdot f),
\qquad
\dim\ker D_{\mathrm{flag},f}=40.}
\tag{JI37b}
$$

Selecting \(149\) independent constraint components and applying the implicit-function theorem shows that the continuous zero locus is locally the flag orbit. By equivariance the same holds along that orbit. Consequently every positive weighting of the displayed residual summands gives some positive normal edge.

This closes the finite **kernel** problem, not the normalization problem for this redundant ambient constraint. Different relative weights on idempotency, unit, membership, and closure residuals change the nonzero singular values.

There is now a clean complementary answer. On the oriented associated bundle

$$
\mathcal E_{\mathrm{or}}
=F_4\times_{C_{F_4}(w)}
\{b\in B:\operatorname{tr}b=2\},
\tag{JI37c}
$$

the single canonical potential \(V([g,b])=\frac12\lVert b\circ b-b\rVert^2\) has

$$
\boxed{
V^{-1}(0)\cong F_4/S(U(2)\times U(3)),
\qquad
\operatorname{Spec}(\operatorname{Hess}V)
=\{0^{(40)},1^{(4)}\}.}
\tag{JI37d}
$$

This fixes the finite spectrum by restricting the ambient carrier to Yokota's orientation orbit. Its four-dimensional normal is not a faithful representation of the surviving group: color and \(U(1)\) act trivially. Conversely, the 149-dimensional normal quotient of the full defining-data carrier is faithful but inherits no singular spectrum from the redundant constraint rows. [[exceptional-normal-holonomy-and-the-residual-gauge-form]] develops this exact carrier fork. Compatibility with a physical local carrier remains open in both branches.

## First-order asymmetry and positive mass are different faces

The factorization

$$
A_{\mathrm{flag},f}
=
D_{\mathrm{flag},f}^*D_{\mathrm{flag},f},
\qquad
D_{\mathrm{flag},f}
:=
\mathrm D\mathcal C_{\mathrm{flag}}|_f,
\tag{JI38}
$$

separates two structures:

- \(D_{\mathrm{flag},f}\) retains signed first-order constraint residuals and left-polar/codomain data;
- \(A_{\mathrm{flag},f}\) retains only their positive even response.

Squaring forgets more than a sign: it forgets the left polar factor and every codomain-unitary presentation of the same modulus. But the flag's complex orientation is even more prior: it is carried by \(w\), or equivalently by \(I_B=(w-w^2)/\sqrt3\), and is already lost under the average \(w\mapsto P_B\). Neither \(D_{\mathrm{flag},f}\) nor its square recovers it from \((\ell,P_B)\). Therefore a positive Hessian cannot by itself explain chirality, and an orientation-bearing first-order operator cannot by itself prove a positive mass floor. In finite dimensions \(D_{\mathrm{flag},f}\) is automatically Fredholm and its index is only a dimension count; a physically meaningful chiral index would have to arise from a later infinite-dimensional graded Fredholm realization. The asymmetry-first programme needs the primitive orientation and the positive modulus together, but not identified.

The same firewall separates three uses of the word *gap*:

1. an idempotent has Jordan spectral values \(0\) and \(1\);
2. the idempotency-defect Hessian has a normal response edge \(1\);
3. a Yang--Mills vacuum representation has a positive Poincare mass-Casimir edge.

The first two are exact algebra. The third follows only after carrier realization and a uniform physical comparison.

## The normal gap is not yet an excitation gap

The idempotency theorem penalizes motion **away from** the valid projector locus and vanishes along motion **within** that locus. This is exactly right for normal rigidity, but it creates a decisive typing question. If physical field excitations are tangent variations among valid configurations, then \(A_e\) charges constraint violations while vanishing on the prospective physical sector. Quotienting the orbit would then discard the physical directions rather than prove them massive.

The exceptional flag construction becomes physically relevant only if a realization map turns every gauge-invariant nonvacuum excitation into a nonzero normal flag response. A single finite-dimensional normal space cannot cover an infinite-dimensional regulated OS Hilbert space with a uniform lower bound. The finite fibre must instead be deployed over field configurations, regions, links, or boundary data, producing an infinite-dimensional response carrier before a full-sector coverage estimate can even be stated.

This gives a useful no-shortcut result:

$$
\boxed{
\text{finite Jordan normal edge}
\not\Rightarrow
\text{Yang--Mills excitation edge}.}
\tag{JI38a}
$$

The missing bridge is not merely multiplication by an energy unit. It is a carrier-changing analysis map, a proof that its kernel is exactly the vacuum, and a kinetic comparison with the physical clock generator.

## Shorting turns the flag response toward a local fact

Suppose a physical realization transports or extends the finite Hessian to a bounded positive operator \(\widetilde A_{\mathrm{flag},f}\) on a common Hilbert carrier \(\widetilde{\mathcal H}_f\), and assigns the oriented flag a closed retained subspace \(L_f\subseteq\widetilde{\mathcal H}_f\). Only then does [[shorted-response-filtration-and-the-leak-cocycle]] supply

$$
S_{L_f}(\widetilde A_{\mathrm{flag},f})
\tag{JI39}
$$

as the least flag-response cost after every locally invisible deformation is allowed to relax. If both \(L_f\) and \(\widetilde A_{\mathrm{flag},f}\) are stabilizer-invariant, the short remains \(S(U(2)\times U(3))\)-equivariant. Let \(L_{f,\mathrm{exc}}=L_f\cap\ker P_0\). In the bounded common-carrier setting, a positive lower edge is equivalent to the Douglas condition

$$
L_{f,\mathrm{exc}}
\subseteq
\operatorname{Ran}\widetilde A_{\mathrm{flag},f}^{1/2}.
\tag{JI40}
$$

An unbounded OS or Hamiltonian form requires the corresponding form-domain version; (JI40) cannot simply be copied across carriers.

This gives a precise division of labor:

$$
\begin{array}{rcl}
\text{selected oriented flag}
&\longrightarrow&
\text{observed stabilizer and first-order asymmetry},
\\
\text{constraint Jacobian}
&\longrightarrow&
\text{obstruction to leaving the flag orbit},
\\
\text{Jacobian square}
&\longrightarrow&
\text{positive normal stiffness},
\\
\text{shorting}
&\longrightarrow&
\text{least stiffness visible to a local fact}.
\end{array}
\tag{JI41}
$$

The remaining physical solder must not run backward from the known Yang--Mills spectrum.

At a finite regulator \(r=(a,L)\), the smallest honest comparison theorem would use the OS/transfer carrier \((\mathcal H_r,\Omega_r,H_r)\), its form

$$
h_r[\psi]=\lVert H_r^{1/2}\psi\rVert^2,
\tag{JI41a}
$$

and an independently constructed infinite-dimensional flag-response carrier \(\mathcal K_r\), for example a square-integrable field of normal spaces. A closed gauge-invariant analysis map

$$
J_r:\operatorname{Dom}h_r\longrightarrow\mathcal K_r,
\qquad
J_r\Omega_r=0,
\tag{JI41b}
$$

would have to satisfy both coverage and kinetic-solder inequalities,

$$
\lVert J_r\psi\rVert^2
\geq
b_r\lVert(1-P_{\Omega_r})\psi\rVert^2,
\qquad
h_r[\psi]
\geq
\eta_rE_{*,r}\langle J_r\psi,A_{\mathrm{flag},r}J_r\psi\rangle.
\tag{JI41c}
$$

If \(A_{\mathrm{flag},r}\geq\kappa_{\mathrm{flag}}I\), these imply, in quadratic-form notation,

$$
\boxed{
H_r
\geq
\eta_rE_{*,r}\kappa_{\mathrm{flag}}b_r
(1-P_{\Omega_r}).}
\tag{JI41d}
$$

Here the last juxtaposition is scalar multiplication: equivalently,

$$
h_r[\psi]
\geq
\eta_rE_{*,r}\kappa_{\mathrm{flag}}b_r
\lVert(1-P_{\Omega_r})\psi\rVert^2.
\tag{JI41e}
$$

Coverage says that no physical direction hides in the Jordan tangent/kernel sector; the kinetic solder says that flag stiffness is genuinely bounded by clock energy; \(E_{*,r}\) supplies units independently. The continuum target additionally requires a positive regulator-uniform lower limit of their product and OS/Poincare reconstruction.

For a Type-III realization, the missing arrow should first be nonlinear and only then differentiated. Schematically one needs

$$
\mathcal R_r:
\mathsf{FlagField}_r
\longrightarrow
\bigl(\{\mathcal A_r(O)\}_O,\omega_r\bigr),
\tag{JI41f}
$$

followed by local tangent maps

$$
q_{r,O}
:=
\mathrm d\!\left(\operatorname{res}_O\circ\mathcal R_r\right)_f:
\mathcal K_r^{\mathrm{flag}}
\twoheadrightarrow
\mathcal T^{\mathrm{phys}}_{\omega_{r,O}}.
\tag{JI41g}
$$

They must compose under nested restriction, intertwine the stabilizer action, kill the zero-cost orbit tangent, and obey a regulator-uniform domination such as

$$
D_{\mathrm{flag},r}^*D_{\mathrm{flag},r}
\geq
\kappa_*q_{r,O}^*q_{r,O}.
\tag{JI41h}
$$

Type-III standard form canonically represents positivity after an algebra and normal state have been supplied; it does not construct \(\mathcal R_r\), \(q_{r,O}\), a preserving expectation, or the floor. [[library/a-note-on-the-exceptional-jordan-algebra/inq|Albert's non-speciality theorem]] says precisely that there is no nonzero product-preserving Jordan homomorphism from the simple Albert algebra into an associative operator algebra with symmetrized product. It does **not** forbid operator carriers altogether. The regular multiplication map

$$
x\longmapsto L_x\in B(J_{\mathbb C})_{\mathrm{sa}}
\tag{JI41i}
$$

is [[library/general-representation-theory-of-jordan-algebras/inq|Jacobson's regular representation]]. It is faithful, positive, order preserving, and \(F_4\)-equivariant, but is not a Jordan homomorphism; indeed a primitive idempotent has \(L_e\)-eigenvalue \(1/2\), so \(L_e\) is not an operator projection. The finite Hessian \((2L_e-I)^2\) is already an ordinary bounded positive operator. What remains unavailable is the net-compatible nonlinear realization (JI41f), not a bare map into matrices. A successful physical realization must declare which product, orbit, representation, and response structures it preserves or forgets.

## What would count as a Copernican replacement

The exceptional construction now replaces two parts of the gauge-theory epicycle at finite regulator: local lifts of the oriented-flag orbit derive the \(H\)-valued gauge-coordinate law, and the full normal character pulls back to exactly the fundamental color Wilson action. A full Copernican replacement still requires:

1. a principled carrier choice between the reduced oriented bundle, whose canonical normal is not faithful, and the full defining-data quotient, whose 149-dimensional normal is faithful but whose physical status must be justified;
2. a principle selecting the color-only member, its state and coupling trajectory, rather than merely declaring the exact pullback along \(SU(3)_{\mathrm c}\hookrightarrow H\);
3. a continuum map from the finite flag-comparison carrier to a net of Type-III local observable algebras, or a complete OS limit of the recovered Wilson measures;
4. a first-order realization yielding physical Lorentz chirality and passing local and global anomaly tests;
5. a proof that the resulting holonomy or shorted response detects every gauge-invariant nonvacuum direction uniformly through infinite volume and continuum removal;
6. a fixed comparison with the OS Hamiltonian form and, after Poincare reconstruction, the full mass Casimir; and
7. a dimensional yardstick derived independently of the observed glueball spectrum.

The finite identities are now stronger than a spectrum target: (JI36)--(JI37d) give an explicit orientation lift and a canonically normalized reduced Hessian, while [[exceptional-normal-holonomy-and-the-residual-gauge-form]] derives the stabilizer torsor, shows that the 149-dimensional defining-data normal is faithful, and proves the exact color identity \(Q_N=288Q_W\) with \(\beta_W=144\beta\). The next nontrivial theorem is consequently physical and regulator dependent:

$$
\boxed{
\inf_r
\left(
\eta_rE_{*,r}\kappa_rb_r
\right)_{\mathrm{physical\ units}}
>0,}
\tag{JI42}
$$

together with the required OS and Poincare convergence. Here the factors must arise from one declared carrier and cannot be chosen to fit the known spectrum. Even before that bridge, (JI21), (JI36), (JI37b), and (JI37d) derive symmetry, orientation loss, and dimensionless normal rigidity from the same pointed whole. That is a pre-QFT Copernican advance rather than a fit to the epicycles; it is not yet a theorem about the Yang--Mills spectrum.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/jordan_idempotency_gap_receipt.py|The Peirce receipt]] and [[contemporary-puzzles/yang-mills-mass-gap/receipts/jordan-idempotency-gap-receipt-output.txt|its stored output]] verify the idempotency spectra and dimension balances. [[contemporary-puzzles/yang-mills-mass-gap/receipts/exceptional_flag_linearization_receipt.py|The flag-linearization receipt]] and [[contemporary-puzzles/yang-mills-mass-gap/receipts/exceptional-flag-linearization-receipt-output.txt|its stored output]] prove the standard continuous constraint's kernel dimension by exact modular rank plus the cited orbit dimension. The [[contemporary-puzzles/yang-mills-mass-gap/receipts/exceptional_normal_holonomy_receipt.py|normal-holonomy receipt]] checks the reduced Hessian ledger, faithful-normal representation arithmetic, and exact color-Wilson normalization. These receipts do not prove physical chirality, select a Yang--Mills carrier or state, or imply a continuum gap.

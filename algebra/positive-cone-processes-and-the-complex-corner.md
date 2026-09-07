# Positive Cone Processes and the Complex Corner

A selected complex rank-two Jordan corner supplies a Lorentz cone, while first and second derivatives of its logarithmic determinant supply the scale differential and positive response metric together. Exceptional descent variance gives an actual positive input to that cone and therefore forces the proposed causal bound. This is an exact finite construction; physical context selection, spacetime gluing, dynamics and the continuum Yang–Mills gap remain open.

The preserved [associative-descent packet](../inbox/causal-grain-cmb-spectroscopy/octonionic-associative-descent.md) and [causal order before clock time](../inbox/causal-grain-cmb-spectroscopy/causal-order-before-clock-time.md) contain the original corner/cone clue. This note lifts its reusable mathematics and adds the response and process comparisons without changing those historical sources.

## The corner belongs to the selected exceptional flag

Use the [[algebra/exceptional-context-response|positive exceptional retraction]]
\[
E=\frac{I+w+w^2}{3}:J=\mathfrak h_3(\mathbb O)
\longrightarrow B=\operatorname{Fix}(w)\cong\mathfrak h_3(\mathbb C).
\tag{PC1}
\]
For a selected trace-two idempotent \(p\in B\), define
\[
X=pBp\cong\mathfrak h_2(\mathbb C),\qquad Q(a)=pE(a)p.
\tag{PC2}
\]
Compression occurs inside the associative complex matrix presentation of \(B\). Both maps are positive. Their composite retracts onto \(X\), with retained unit \(p\), and is not a product-preserving embedding of the exceptional algebra.

These are the same \(w,p\) data underlying [[contemporary-puzzles/yang-mills-mass-gap/jordan-idempotency-and-the-stabilizer-gap|the exceptional flag stabilizer]]. No additional three-dimensional subspace is chosen after (PC2). Physical selection of the complex context and rank-two corner remains open.

Write \(I\) for \(p\) in a matrix chart. The Pauli decomposition gives
\[
x=tI+\mathbf v\cdot\boldsymbol\sigma,\qquad
t=\tfrac12\operatorname{Tr}x,\qquad
\det x=t^2-|\mathbf v|^2.
\tag{PC3}
\]
Its eigenvalues are \(t\pm|\mathbf v|\), so
\[
\boxed{x\in X_+\setminus\{0\}
\quad\Longleftrightarrow\quad t\geq|\mathbf v|,\quad t>0.}
\tag{PC4}
\]
The full cone \(X_+\), including zero, is closed, convex and pointed. Its rank-one boundary and rank-two interior are continuous; rank alone supplies no positive determinant floor.

## One determinant supplies response and scale

On the open cone \(X_{++}\), put
\[
\mathcal F(u)=-\tfrac12\log\det u.
\tag{PC5}
\]
For constant affine variations \(x,y\in T_uX_{++}\cong X\),
\[
\begin{aligned}
\theta_u(x)&=-d\mathcal F_u(x)
=\tfrac12\operatorname{Tr}(u^{-1}x),\\
h_u(x,y)&=D^2\mathcal F_u(x,y)
=\tfrac12\operatorname{Tr}(u^{-1}x\,u^{-1}y).
\end{aligned}
\tag{PC6}
\]
The Hessian uses the Jordan vector space's [[hessian-response-geometry/affine-hessian-structure|affine structure]]. It is positive definite: conjugating by \(u^{-1/2}\) turns its quadratic form into \(\operatorname{Tr}(z^2)/2\) for Hermitian \(z\). [[spectral-wall-descent/response-determinant|The shared determinant calculus]] owns the first/second derivative relation and its sign. This complex-corner response is not thereby the BKM metric of a normalized quantum state.

The potential is fixed up to a constant once its congruence character is required:
\[
\mathcal F(SuS^*)=\mathcal F(u)-\log|\det S|.
\tag{PC6a}
\]
Indeed choose \(u=I\), \(S=v^{1/2}\), to obtain (PC5) at every \(v>0\). This excludes adding an arbitrary affine function while claiming the same transformation law. The character and its normalization remain declared structural requirements; Hessian positivity alone does not select them.

Directly,
\[
h_u(u,x)=\theta_u(x),\qquad h_u(u,u)=1,\qquad
h_u^{-1}(\theta_u,\theta_u)=1.
\tag{PC7}
\]
Thus [[algebra/directed-response-and-lorentzian-signature|directed-response reflection]] no longer receives an independently appended covector: line and metric come from the same function.

Let \(D(x,y)=\tfrac12[\det(x+y)-\det x-\det y]\). The \(2\times2\) trace identity gives
\[
\boxed{g_u(x,y)=h_u(x,y)-2\theta_u(x)\theta_u(y)
=-\frac{D(x,y)}{\det u}.}
\tag{PC8}
\]
Indeed for \(z=u^{-1/2}xu^{-1/2}\),
\(\det z=[(\operatorname{Tr}z)^2-\operatorname{Tr}(z^2)]/2\); polarizing proves (PC8). Its signature is \((3,1)\), and its conformal class is independent of \(u\). At \(\det u=1\), the Lorentzian form itself is independent of the positive order-unit frame.

The half-normalization in (PC5) is declared; it makes (PC7) a unit statement, not a physical clock calibration. The determinant has degree two. Neither its degree nor the relative coefficients may be silently changed in a comparison.

## Positivity forces the causal bound

For nonzero \(x\geq0\), the matrix \(z=u^{-1/2}xu^{-1/2}\) has eigenvalues \(\lambda_1,\lambda_2\geq0\). Hence \(\theta_u(x)>0\) and
\[
\boxed{
\mathscr Q_u(x)=\frac{h_u(x,x)}{\theta_u(x)^2}
=\frac{2(\lambda_1^2+\lambda_2^2)}
{(\lambda_1+\lambda_2)^2}\in[1,2].}
\tag{PC9}
\]
The upper bound is exactly the reflection's causal-cone condition. Rank one saturates two; \(x\propto u\) gives one. No separate propagation bound was inserted after positivity.

Under simultaneous congruence \(u\mapsto SuS^*\), \(x\mapsto SxS^*\), both (PC6) and (PC9) are natural. Determinant scales by \(|\det S|^2\). Determinant-preserving congruences supply proper orthochronous Lorentz transformations; connected unit-preserving Jordan automorphisms supply rotations, while the full unit-preserving group also has spatial reflections. Boosts are not compact \(F_4\) automorphisms of the selected flag.

These Lorentz congruences and the familiar internal gauge stabilizer are different actions. A spacetime realization must distinguish internal gauge transformations from changes of spacetime frame; a common algebraic package does not identify weak isospin with spatial rotation.

## An actual descent residue lands in the cone

Write \(a=b+y\in J\), where \(b=Ea\), \(Ey=0\). Exceptional variance gives \(E(a^2)-(Ea)^2=E(y^2)\geq0\). The complete variance of (PC2) is
\[
\begin{aligned}
\Delta_Q(a)&:=Q(a^2)-Q(a)^2\\
&=pE(y^2)p+p\,b(1-p)b\,p\in X_+.
\end{aligned}
\tag{PC10}
\]
The terms are respectively transported exceptional loss and additional corner loss. The latter is \([(1-p)bp]^*[(1-p)bp]\). Every nonzero \(\Delta_Q(a)\) therefore obeys (PC9): the same finite descent really produces a cone-valued response.

For composable unital completely positive maps of associative algebras, define \(\Delta_\Phi(a)=\Phi(a^2)-\Phi(a)^2\), \(a=a^*\). Expansion gives the transported variance balance
\[
\Delta_{\Psi\Phi}(a)
=\Psi(\Delta_\Phi(a))+\Delta_\Psi(\Phi(a)).
\tag{PC11}
\]
The Jordan step in (PC10) uses its separately proved variance theorem; no undeclared complete positivity on \(J\) is invoked. Equation (PC11) is a compositional positive-residue law, not a physical energy identity.

The image can reach the null boundary. In the standard context with \(p=\operatorname{diag}(1,1,0)\), take \(a\) with only an octonionic \(13\) entry \(z\perp\mathbb C\) and its conjugate nonzero. Then
\[
Ea=0,\qquad a^2=\operatorname{diag}(|z|^2,0,|z|^2),
\qquad \Delta_Q(a)=\operatorname{diag}(|z|^2,0)
\tag{PC12}
\]
in the retained corner. Nonzero descent cost can have zero determinant. Conversely \(\Delta_Q(a)=0\) for every retained \(a\in X\). This variance is not an excitation-gap form on that retained carrier.

## A directed ledger is not a density trajectory

In a fixed copy of \(X\), increments \(c_j\in X_+\) define
\[
r_{j+1}=r_j+c_j.
\tag{PC13}
\]
Pointedness excludes both a nonzero increment and its negative from being admissible. Differentiable realizations with \(\dot r\in X_+\setminus\{0\}\) obey the future cone bound. On the open cone,
\[
s(r)=\tfrac12\log\det r,\qquad
\frac{ds}{d\lambda}=\theta_r(\dot r)>0.
\tag{PC14}
\]
The determinant therefore supplies an integrable increasing scale variable. The increments can be responses from (PC10), but their selection, common-carrier transport and factual interpretation remain additional process data.

A nonzero difference of equal-trace density matrices cannot be positive. Also, \(r\mapsto\Phi(r)+c\), with \(\Phi\) completely positive and \(c\geq0\), need not increase \(r\): \(\Phi=0,c=0\) is a counterexample. Transported variance (PC11) and an enduring additive ledger (PC13) require a comparison before being identified.

Translations in (PC13) are invertible on the unrestricted vector space. Their **admissible order** is one-sided; literal erasure resides in a noninjective readout such as \(Q\), not in positive translation alone. No persistent factual record has been constructed merely by adding matrices.

## The new spectral question

The corner, cone, determinant response, scale differential and causal bound now belong to one finite package. Its \(3+1\) signature follows from the selected complex rank-two type. Real, quaternionic and octonionic rank-two corners instead give \(2+1\), \(5+1\) and \(9+1\).

[[determinant-preparation-positivity-and-the-rank-threshold|Exponentiating determinant comparison]]
tests whether this response admits a positive preparation pairing at all.
On the full complex rank-two cone, the inverse-determinant exponent must
be zero or at least one, despite a positive local Hessian at every
positive exponent. The restriction vanishes at fixed trace. The
[[directed-analytic-realization/determinant-cone-preparation-and-the-gapless-return|admissible cone return]]
then constructs positive preparation and Lorentz-covariant translations
on the same carrier, with a gapless joint invariant spectrum.

[[algebra/qubit-cone-interiorization-and-the-clock-gap|Cone interiorization]] gives a same-carrier spectral test: uniform inward contraction of this normalized positive base controls its specified self-adjoint transfer generator. Static cone membership does not. [[algebra/determinant-scale-clock-and-the-hyperbolic-threshold|The determinant-scale clock]] separately tests whether a geometrical hyperbolic threshold survives the conformal return.

[[peirce-context-averaging-and-the-emergent-qubit-process|Averaging moving Peirce contexts]] now determines an explicit local depolarizing return from the rank-two octonionic whole, without first selecting a qubit generator. Its invariant context weighting fixes a dimensionless contraction; it does not determine a physical duration. [[short-loop-holonomy-and-quantitative-gluing|Short-loop transport]] separately shows how the corner's Pauli algebra can enforce a volume-uniform section bound, and exactly how that bound can disappear under an adjoint observable realization.

The next construction must preserve these relationships in a common field realization, select compatible dynamics and frames, and control every physical nonvacuum direction through the Yang–Mills limits. The finite determinant is not being assigned a particle mass.

[[directed-analytic-realization/positive_cone_process_receipt.py|The shared cone receipt]]
checks exact rational complex-matrix identities, cone saturation and
associative variance composition. Its isolated octonionic test uses the
specific norm products in (PC12), not a full Albert CP simulation.
[[directed-analytic-realization/positive-cone-process-receipt-output.txt|The saved output]]
marks derivative estimates and quadrature as numerical checks rather than
proofs.

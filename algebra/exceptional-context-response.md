# Exceptional Context Retraction and Its Positive Response

An order-three automorphism of the Albert algebra determines a positive retraction onto a complex Jordan context, an exact variance of what that context discards, and a uniformly positive response when all exceptional contexts are compared with normalized Haar weight. Its regular multiplication representation also realizes this response as the Hessian of an ordinary matrix relative-entropy loss. These are finite carrier-changing constructions, independent of complex integrability on \(S^6\). They neither select a physical distribution of contexts nor establish a gap on the full matrix-state or Yang--Mills carrier.

## A positive map selected by an oriented operation

Use the compact Euclidean Albert algebra
\[
J=\mathfrak h_3(\mathbb O),\qquad
\langle x,y\rangle_J=\operatorname{tr}_J(x\circ y),\qquad
\operatorname{tr}_J\mathbf1=3.
\]
Its cone \(J_+=\{x^2:x\in J\}\) is the closed convex cone of nonnegative Jordan spectra. The trace form is positive definite. Let \(w\) be
[[contemporary-puzzles/yang-mills-mass-gap/order-three-orientation-and-the-exceptional-stabilizer|Yokota's order-three automorphism]], and put
\[
B=\operatorname{Fix}(w)\cong\mathfrak h_3(\mathbb C),\qquad
E=\frac{I+w+w^2}{3},\qquad q=I-E.
\tag{EC1}
\]
The dimensions are \(\dim J=27\), \(\dim B=9\), and \(\dim B^\perp=18\).

**Positive-retraction theorem.** \(E\) is the trace-orthogonal projection onto \(B\), is unital and trace-preserving, and maps \(J_+\) into \(B_+\). For \(b\in B\) and \(x\in J\),
\[
E(b\circ x)=b\circ E(x).
\tag{EC2}
\]
Indeed, each \(w^k\) preserves the Jordan product, squares, unit, and trace. Averaging preserves the convex positive cone, while \(w^*=w^{-1}\) makes the cyclic average an orthogonal projection. Equation (EC2) follows by fixing \(b\) inside the average. The positive cone inherited by this Jordan subalgebra is its ordinary Hermitian-matrix cone.

Write \(x=b+y\) with \(b=Ex\) and \(y=qx\). Then
\[
\boxed{
E(x^2)-(Ex)^2=E(y^2)\in B_+,
\qquad
\operatorname{tr}_J\!\left(E(x^2)-(Ex)^2\right)=\|qx\|_J^2.}
\tag{EC3}
\]
This follows by expanding \(x^2=b^2+2b\circ y+y^2\), applying (EC2), and taking the trace. Equivalently,
\[
\|x\|_J^2=\|Ex\|_J^2+\|qx\|_J^2.
\tag{EC4}
\]
Here the operator acts on Jordan observables. Its residue is a lost quadratic distinction, not yet energy or a count of actual events.

The signed datum survives separately:
\[
I_w=\frac{w-w^2}{\sqrt3},\qquad
I_w^*I_w=q,\qquad I_{w^{-1}}=-I_w.
\tag{EC5}
\]
Thus the even response in (EC3) is the squared norm of an orientation-bearing map, but cannot recover its sign. A cyclic orientation is not an irreversible chronology; the noninvertible operation here is \(E\). The cone, orientation, retraction, and quadratic response are related operations, not four names for one object.

## A complete family has a strict finite lower frame

Let \(G=F_4\) act by Jordan automorphisms. For \(g\in G\), define
\[
E_g=gEg^{-1},\qquad q_g=I-E_g,\qquad
P_{\mathbf1}x=\frac{\operatorname{tr}_Jx}{3}\mathbf1,\qquad
J_0=\ker\operatorname{tr}_J.
\]
Use normalized Haar measure \(dg\). This is the invariant geometrical weighting of the context orbit, not a postulate that nature randomly samples contexts.

**Context-frame theorem.**
\[
\boxed{
\int_G q_g\,dg=\frac9{13}(I-P_{\mathbf1}),\qquad
\int_G\|q_gx\|_J^2\,dg=\frac9{13}\|x-P_{\mathbf1}x\|_J^2.}
\tag{EC6}
\]
The averaged self-adjoint operator commutes with \(G\) and vanishes on \(\mathbf1\). The real \(26\)-dimensional representation \(J_0\) is irreducible, so its self-adjoint commuting operator is scalar there. Every \(q_g\) has rank eighteen. Taking the operator trace therefore fixes that scalar to \(18/26=9/13\). The irreducibility input is recorded in [[library/stability-of-compact-symmetric-spaces/inq|Semmelmann--Weingart, Section 4 after equation (32)]].

In particular,
\[
\bigcap_{g\in G}\operatorname{Ran}E_g=\mathbb R\mathbf1.
\]
One context misses an entire subspace; the compatible family does not miss a nonconstant Jordan observable. This is a genuine whole--part distinction that uses no spatial distance.

For the analysis map
\[
\mathcal T:J_0\longrightarrow L^2(G,dg;J),\qquad
(\mathcal T x)(g)=q_gx,
\]
one has \(\mathcal T^*\mathcal T=(9/13)I\), and hence the explicit bounded left inverse
\[
\mathcal B=\frac{13}{9}\mathcal T^*,\qquad
\mathcal B\mathcal T=I,\qquad
\|\mathcal B\|=\sqrt{\frac{13}{9}}.
\tag{EC7}
\]
This is a finite constructive example of
[[global-local-response-reconstruction/quantitative-descent-and-the-shape-of-a-gap|quantitative gluing]], not only a kernel-separation theorem.

The retained family is also quantitatively complete:
\[
\int_G E_g\,dg=P_{\mathbf1}+\frac4{13}(I-P_{\mathbf1}).
\tag{EC8}
\]
Thus all contexts together can reconstruct what an individual retraction forgets. Neither (EC6) nor (EC8) selects an actually realized context.

If a different probability measure \(\mu\) satisfies \(\mu\ge\alpha\,dg\), then its response has lower bound \(\alpha(9/13)\) on \(J_0\). Without such coverage, a measure concentrated on one context has the nonconstant kernel \(B\cap J_0\). Context coverage, not the word positivity, is the load-bearing condition.

[[hessian-response-geometry/response-rigidity-and-multiplicity|Response rigidity and multiplicity]] isolates why the scalar trace fixes the whole operator here: the actual averaged response acts on an irreducible comparison carrier. A fixed trace and even an entire selected entropy profile do not force this conclusion without that relation. Passing to fields introduces physical multiplicity spaces which internal equivariance does not control.

## An associative completely positive realization

The exceptional Jordan product cannot be faithfully identified with the symmetrized product of an associative operator algebra. There is nevertheless a useful linear realization. On the complex Hilbert space
\[
\mathcal H_J=J\otimes_{\mathbb R}\mathbb C,\qquad \dim_{\mathbb C}\mathcal H_J=27,
\]
let \(L_x(y)=x\circ y\). For real \(x\), \(L_x\) is self-adjoint and
\[
U_gL_xU_g^*=L_{gx}.
\tag{EC9}
\]
The regular map \(x\mapsto L_x\) is injective since \(L_x\mathbf1=x\). It preserves positivity: in a Jordan frame with eigenvalues \(\lambda_i\), \(L_x\) has eigenvalues \(\lambda_i\) on the three diagonal directions and \((\lambda_i+\lambda_j)/2\) on the eight-dimensional off-diagonal Peirce spaces. It does not preserve the Jordan product: generally \(L_{x^2}\ne L_x^2\).

With \(U=w\) on \(\mathcal H_J\), define the ordinary matrix conditional expectation
\[
\mathscr E(T)=\frac13\sum_{k=0}^2U^kTU^{-k},
\qquad T\in B(\mathcal H_J).
\tag{EC10}
\]
It is unital, completely positive, trace-preserving, and idempotent. Equivariance gives a commuting square:
\[
\boxed{\mathscr E(L_x)=L_{Ex}.}
\tag{EC11}
\]
Thus exceptional retraction has a genuine associative CP implementation on its regular image. No claim of complete positivity on an undeclared matrix ordering of \(J\) is needed.

The return type matters. \(U\) has eigenvalues \(1,\omega,\bar\omega\), each of multiplicity nine, so
\[
\operatorname{Ran}\mathscr E\cong M_9(\mathbb C)\oplus M_9(\mathbb C)\oplus M_9(\mathbb C).
\tag{EC12}
\]
This is not \(M_3(\mathbb C)\), the familiar associative envelope of the retained Jordan context \(B\). The regular realization adds operator directions; it is not already the desired QFT algebra.

## The response is an entropy-loss Hessian

Peirce eigenvalues also give, for every real \(x\),
\[
\operatorname{Tr}_{\mathcal H_J}L_x=9\operatorname{tr}_Jx,\qquad
\operatorname{Tr}_{\mathcal H_J}L_x^2
=3\operatorname{tr}_J(x^2)+2(\operatorname{tr}_Jx)^2.
\tag{EC13}
\]
For \(x\in J_0\) and \(|\varepsilon|\|L_x\|<1\), use the faithful state
\[
\rho_\varepsilon(x)=\frac{I+\varepsilon L_x}{27},\qquad \tau=\frac I{27}.
\]
Relative entropy uses natural logarithms. The conditional-expectation identity yields
\[
\begin{aligned}
\mathcal L_{\mathscr E}(\rho)
&:=D(\rho\|\tau)-D(\mathscr E\rho\|\tau)\\
&=D(\rho\|\mathscr E\rho)
=S(\mathscr E\rho)-S(\rho)\ge0.
\end{aligned}
\tag{EC14}
\]
To check the equality, \(\log(\mathscr E\rho)\) belongs to the fixed algebra, so trace duality replaces \(\rho\) by \(\mathscr E\rho\) against that logarithm. This is an information loss under a declared readout, not thermodynamic entropy production.

For \(T=T^*\) with \(\operatorname{Tr}T=0\), the matrix expansion around \(\tau\) gives
\[
D\!\left(\frac{I+\varepsilon T}{27}\middle\|\tau\right)
=\frac{\varepsilon^2}{54}\operatorname{Tr}T^2+O(\varepsilon^3)
\quad(\operatorname{Tr}T=0).
\]
Applying (EC11), (EC13), and (EC3),
\[
\boxed{
\mathcal L_{\mathscr E}\bigl(\rho_\varepsilon(x)\bigr)
=\frac{\varepsilon^2}{18}\|qx\|_J^2+O(\varepsilon^3).}
\tag{EC15}
\]
Conjugate the expectation as well as its context and average over \(G\). Compactness makes the Taylor remainder uniform for fixed \(x\). Then
\[
\boxed{
\int_G\mathcal L_{\mathscr E_g}\bigl(\rho_\varepsilon(x)\bigr)\,dg
=\frac{\varepsilon^2}{26}\|x\|_J^2+O(\varepsilon^3).}
\tag{EC16}
\]
The second derivative is \(\|x\|_J^2/13\). This explicitly connects the Jordan quadratic residue to positive quantum information geometry on a specified state submanifold; it does not identify a Hodge polarization with BKM or a state Hessian with energy.

## The added carrier has an explicit unseen direction

Strictness on \(L(J_0)\) does not extend to every matrix-state tangent. The representation splits as
\[
\mathcal H_J=\mathbb C\mathbf1\oplus J_{0,\mathbb C}.
\]
Every \(U_g\) preserves this decomposition. Consequently the nonzero traceless operator
\[
T_{\mathrm{bal}}=26P_{\mathbb C\mathbf1}-P_{J_{0,\mathbb C}}
\tag{EC17}
\]
is fixed by every \(\mathscr E_g\). For sufficiently small \(\varepsilon\), the state \((I+\varepsilon T_{\mathrm{bal}})/27\) has exactly zero loss for the entire family.

This is a concrete reason not to infer full physical coverage from the finite Jordan frame. A later construction must say whether such balance directions are physical, constrained, separately observed, or removed by a justified quotient. They cannot be deleted merely to preserve a desired edge.

[[primitive-peirce-response|The primitive Peirce completion]] now takes the separately observed branch: it adds the readouts determined by all primitive Jordan idempotents. Their averaged loss has a certified lower bound on the entire traceless matrix carrier and detects (EC17), without quotienting it out. This is a genuinely enlarged family, not a retroactive claim that the cyclic family already had complete coverage.

## What this contributes to the mass-gap search

The same prior \(w\), supplemented by a trace-two idempotent, has
[[contemporary-puzzles/yang-mills-mass-gap/order-three-orientation-and-the-exceptional-stabilizer|the exceptional Standard-Model flag stabilizer]]. It now also supplies a positive retraction and a computable information-response realization. The link is therefore stronger than matching a group name to a number.

Still missing are a law selecting physical contexts and states, their spacetime localization, a faithful action on the complete neutral gauge carrier, and a uniform comparison with the physical transfer or mass Casimir. [[contemporary-puzzles/yang-mills-mass-gap/exceptional-wilson-same-carrier-factorization|The exceptional Wilson construction]] is a separate existing route to an actual finite Euclidean gauge measure; it must not be identified with (EC10) by terminology alone.

There is now a concrete partial bridge: [[global-local-response-reconstruction/exceptional-context-analysis-of-gauge-gradients|differentiating the representation]] makes the cyclic contexts an exact frame for gradients of scalar gauge-invariant observables under a specified Wilson law. It does not act on their scalar values as an internal channel. This factors the field Dirichlet form, but leaves its state-dependent coercivity and the physical slab comparison unproved.

The coefficient \(9/13\) in (EC6) is a normalized finite frame ratio, and \(1/13\) in the second derivative of (EC16) is a Hessian coefficient in the explicitly selected state chart. Neither is a glueball coefficient or an inverse clock time. Their value is methodological: an algebraically specified relation really can force a quantitative bound, while the operator's domain says exactly which distinctions it bounds.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/positivity_rigidity_audit_receipt.py|The finite audit receipt]] checks the Jordan variance, regular traces, CP intertwining, entropy expansion, and unseen balance direction. The Haar identity is proved above using the cited representation input, not established by finite sampling.

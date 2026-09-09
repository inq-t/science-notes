# Multiplication, Reassociation and the Process Metric

Associativity of a multiplication does not make arbitrary Gaussian comparisons independent of their parenthesization. Giving every intermediate tensor its own positive clock norm fails for every nontrivial finite unital algebra. A constructive replacement keeps clock norms at the endpoints and carries all intermediate innovations: its complete Gaussian amplitude and transported sources agree across every sequential reduction order. Exact identity transitions impose an additional obstruction, so this construction selects neither a unital process functor nor a physical clock.

## The tensor carriers are part of the statement

Let \(V\) be a finite-dimensional complex unital associative algebra with positive Hermitian pairing \(h\). Put \(d=\dim V\), use the tensor pairings, and write
\[
X=V^{\otimes3},\quad Y=V^{\otimes2},\quad Z=V,
\qquad
A_L=\mu\otimes I,\quad A_R=I\otimes\mu,\quad B=\mu.
\]
Associativity says
\[
BA_L=BA_R=:F:X\longrightarrow Z.
\tag{MR1}
\]
The input \(x\in X\) is one arbitrary tensor. It is not a Cartesian triple of independently varying elements of \(V\). Restricting to decomposable tensors \(a\otimes b\otimes c\) makes multiplication nonlinear in those three Cartesian variables; the Gaussian calculations below do not describe that different model.

All interior integrations use the fixed reference measure from \(h\), namely \(\prod_jd^2y_j/\pi\) in orthonormal complex coordinates. We retain both the determinant factor and the entire boundary quadratic form, as in [[determinant-response-sewing-and-relational-rigidity|determinant–response sewing]]. Statements for \(\nu\) independent copies raise determinant factors to the power \(-\nu\).

## An intermediate clock norm obstructs reassociation

For \(p=L,R\), consider the positive quadratic action
\[
E_p(z)=z(\|x\|^2+\|y\|^2+\|v\|^2)
+\|y-A_px\|^2+\|v-By\|^2,\qquad z>0.
\tag{MR2}
\]
Eliminating \(y\) uses the same positive block
\[
M_z=(1+z)I_Y+B^\dagger B
\tag{MR3}
\]
and hence the same determinant in both presentations. The retained \(vv\) blocks and cross terms also coincide: \(M_z^{-1}B^\dagger=B^\dagger((1+z)I_Z+BB^\dagger)^{-1}\), so their dependence on \(A_p\) is only through \(BA_p=F\).

The \(xx\) block is \(zI_X+A_p^\dagger(I-M_z^{-1})A_p\). The identity
\[
I-M_z^{-1}
=\frac{z}{1+z}I_Y+
\frac1{1+z}B^\dagger((1+z)I_Z+BB^\dagger)^{-1}B
\]
therefore gives the exact retained difference
\[
\boxed{
S_L(z)-S_R(z)=
\begin{pmatrix}
\displaystyle\frac{z}{1+z}
\big(A_L^\dagger A_L-A_R^\dagger A_R\big)&0\\
0&0
\end{pmatrix}_{X\oplus Z}.}
\tag{MR4}
\]

**Theorem.** If \(d>1\), no positive pairing \(h\) makes (MR2) reassociation-invariant on the complete boundary carrier at any \(z>0\).

**Proof.** With \(K=\mu^\dagger\mu\) on \(V\otimes V\), vanishing of (MR4) requires
\[
K\otimes I=I\otimes K.
\tag{MR5}
\]
The right side commutes with every matrix on the first tensor factor. Thus so does \(K\) on its first factor, and the matrix-unit identities give \(K=I\otimes R\). Substitution in (MR5) forces \(R=cI\), hence \(K=cI_{V\otimes V}\). Unitality makes \(\mu\) surjective, so \(c>0\) and \(\operatorname{rank}K=d\). The scalar identity has rank \(d^2\), forcing \(d=1\). \(\square\)

The failure is in the complete boundary response, even though the multiplication means and normalization agree. Restricting the boundary tests to hide this difference would change the claim.

## Zero interior clock weight gives an exact positive repair

Replace (MR2) by
\[
E_p^0(z)=z(\|x\|^2+\|v\|^2)
+\|y-A_px\|^2+\|v-By\|^2.
\tag{MR6}
\]
Its spectral coefficient is \(\Gamma=\operatorname{diag}(I_X,0_Y,I_Z)\); its full quadratic form remains positive for \(z>0\). Completing the square gives, for one copy,
\[
\boxed{
\int e^{-E_p^0(z)}\,dy
=
\frac{
\exp\!\left[-z(\|x\|^2+\|v\|^2)
-(v-Fx)^\dagger R_3^{-1}(v-Fx)\right]
}{\det R_3},
\qquad
R_3=I_Z+BB^\dagger.}
\tag{MR7}
\]
Here \(dy\) denotes the normalized complex reference measure above. The interior determinant is \(\det(I_Y+B^\dagger B)=\det R_3\). Both outputs agree under reassociation.

There is also an exact identification before integration. Put \(\Delta=A_R-A_L\), so \(B\Delta=0\). Then
\[
y_R=y_L+\Delta x
\tag{MR8}
\]
preserves both discrepancy terms, fixes \(x,v\), and has Jacobian one. Thus the full joint laws agree after this change of variables. A source \(2\operatorname{Re}\langle j,y_L\rangle\) becomes
\[
2\operatorname{Re}\langle j,y_R\rangle
-2\operatorname{Re}\langle\Delta^\dagger j,x\rangle.
\tag{MR9}
\]
Sources attached to internal variables must be transported, including the induced boundary source. Keeping their coordinate labels fixed generally distinguishes the presentations.

## Every sequential reduction order has the same amplitude

This repair extends beyond the three-input test. Set \(X_m=V^{\otimes m}\). A reduction history chooses, for each \(m=n,\ldots,2\), one adjacent contraction
\[
A_m:X_m\longrightarrow X_{m-1},
\qquad
A_m=I^{\otimes j}\otimes\mu\otimes I^{\otimes(m-j-2)}.
\]
Let \(\mu_m:X_m\to V\) be the iterated multiplication, with \(\mu_1=I\). Associativity makes it independent of parenthesization. For \(x_n=x\), \(x_1=v\), define
\[
E_{\boldsymbol A}(z)=z(\|x\|^2+\|v\|^2)
+\sum_{m=2}^n\|x_{m-1}-A_mx_m\|^2.
\tag{MR10}
\]

**Theorem.** For every \(n\ge2\), integration over \(x_2,\ldots,x_{n-1}\) gives the same full boundary amplitude for every such reduction history:
\[
\boxed{
\int e^{-E_{\boldsymbol A}(z)}
\prod_{m=2}^{n-1}dx_m
=
\frac{
e^{-z(\|x\|^2+\|v\|^2)
-(v-\mu_nx)^\dagger R_n^{-1}(v-\mu_nx)}
}{\det R_n},
\qquad
R_n=\sum_{r=1}^{n-1}\mu_r\mu_r^\dagger.}
\tag{MR11}
\]
The reference measures remain fixed. In particular \(R_n\ge I\); no singular Gaussian integration is used.

**Proof.** Define the innovations
\[
e_m=x_{m-1}-A_mx_m\in X_{m-1}.
\]
At fixed input \(x\), the triangular change from \((x_1,\ldots,x_{n-1})\) to \((e_2,\ldots,e_n)\) has Jacobian one. Under the normalized product of discrepancy factors alone, these innovations are independent standard complex Gaussians. Recursion gives
\[
v=\mu_nx+\sum_{m=2}^n\mu_{m-1}e_m,
\tag{MR12}
\]
because every suffix of the contraction history is the same iterated multiplication on its current tensor carrier. The terminal Gaussian therefore has covariance \(R_n\) and the displayed normalized density. The endpoint weights factor out of the interior integration. \(\square\)

Identifying the same innovations at each arity produces a determinant-one linear change between any two histories. Equation (MR12) shows that it fixes both endpoints. These changes compose exactly through the common innovation coordinates, so transported source functionals are coherent through arbitrary sequences of reassociations. If \(T\) sends old coordinates to new, a new source pulls back as \(T^\dagger j_{\rm new}\), while an old source carried forward becomes \((T^{-1})^\dagger j_{\rm old}\). Derivatives of the generating amplitude must use that same transport.

If \(\mu\mu^\dagger=I\), induction gives \(\mu_r\mu_r^\dagger=I\), hence \(R_n=(n-1)I\). This calibrates the chosen innovation rule; it does not identify arity with physical time.

The multiplication is load-bearing in (MR11): it determines both \(\mu_n\) and the entire covariance sum. This is an exact result for the declared sequential grammar of whole tensor carriers. It does not establish parallel tensor composition of Gaussian channels, a Cartesian many-body model, or the frame-graph law in the determinant–response proposal.

## A leaf identity is different from an identity transition

[[transparent-units-and-hidden-determinants|Transparent unit elimination]] proves that an unconstrained auxiliary leaf with factor \(e^{-\|y-x\|^2}\) integrates to one. The same factor inserted along a transition wire convolves with the neighboring kernel and adds covariance. It is therefore not the identity kernel. The identity transition is the Dirac kernel \(\delta(y-x)\), with zero innovation covariance.

For normalized linear Gaussian transitions, write the mean map and covariance as \((A,R_A)\), where \(R_A\ge0\). Their exact composition law is
\[
(B,R_B)\circ(A,R_A)
=(BA,\ R_B+BR_AB^\dagger),
\qquad
R_I=0.
\tag{MR13}
\]
The covariance recursion is already present in [[rg-covariance-residue/soft-gaussian-gauge-blocking|soft Gaussian blocking]]. It follows here directly by composing independent innovations; singular covariances are understood as Gaussian probability measures.

If a unit insertion \(U:V\to V\otimes V\) satisfies \(\mu U=I\), exact functoriality of (MR13) would require
\[
0=R_\mu+\mu R_U\mu^\dagger.
\tag{MR14}
\]
Both terms are nonnegative, so \(R_\mu=0\). Thus multiplication cannot have independent positive output noise while satisfying its exact unit relation as a Gaussian transition. The positive covariance in (MR11) has not passed that unit test.

## One common Gaussian state cannot repair both units

A stronger obstruction applies to a proposed state-determined covariance rule. Let
\[
Lx=1\otimes x,\qquad Rx=x\otimes1,\qquad
\mu L=\mu R=I.
\]
Choose a covariance \(G>0\) on \(V\) and a common covariance \(C\ge0\) on \(V\otimes V\). No tensor-product form of \(C\) is assumed. Suppose all three covariance differences are nonnegative:
\[
D_\mu=G-\mu C\mu^\dagger\ge0,\qquad
D_E=C-EGE^\dagger\ge0,\quad E=L,R.
\tag{MR15}
\]
These are the noises that would make multiplication and both unit insertions Gaussian transitions preserving the declared object states.

**Theorem.** Conditions (MR15) force \(\dim V=1\).

**Proof.** For either \(E\),
\[
0=G-\mu EGE^\dagger\mu^\dagger
=D_\mu+\mu D_E\mu^\dagger.
\]
Positivity makes both terms zero. Since \(D_E\ge0\), \(\mu D_E\mu^\dagger=0\) implies \(D_E\mu^\dagger=0\). Consequently
\[
C\mu^\dagger=EGE^\dagger\mu^\dagger=EG,
\qquad
E=C\mu^\dagger G^{-1}.
\tag{MR16}
\]
Both units equal this same map, so \(L=R\). Choose a linear functional \(\ell\) with \(\ell(1)=1\); applying \(\ell\otimes I\) to \(1\otimes x=x\otimes1\) gives \(x=\ell(x)1\). \(\square\)

This does not obstruct arbitrary deterministic Gaussian transitions, whose covariances can all vanish. It obstructs a single common covariance assignment of the specified form that makes both unit embeddings and multiplication state-preserving positive transitions. The workspace's [[spectral-wall-descent/scale-correspondence-stack|Frobenius/Q-system construction]] concerns different carriers and retains an inclusion and expectation as data; its existence does not supply the missing Gaussian state here.

## States attached to marked carriers give a conditional return

There is a positive finite construction after changing the common-state hypothesis. Treat a Gaussian carrier as a pair \((X,G)\), including its covariance. For a linear map \(A:X\to Y\), set \(H=AGA^\dagger\), and define
\[
K_{A,t}(x,dy)=
\mathcal N_{\mathbb C}\!\left(e^{-t}Ax,\ (1-e^{-2t})H\right)(dy),
\qquad t\ge0.
\tag{MR17}
\]
Here \(\mathcal N_{\mathbb C}(0,H)\) is the centered circular complex Gaussian with covariance \(E[\eta\eta^\dagger]=H\). Singular covariance means the pushforward Gaussian measure on its support; at \(t=0\) this is the deterministic kernel \(\delta_{Ax}\). The source state \(\mathcal N_{\mathbb C}(0,G)\) is carried to \(\mathcal N_{\mathbb C}(0,H)\). If the next map \(B\) carries \(H\) to \(H'=BHB^\dagger\), covariance addition gives exactly
\[
\boxed{K_{B,s}K_{A,t}=K_{BA,s+t}.}
\tag{MR18}
\]
The product here means first apply \(A,t\), then \(B,s\).

In particular, use distinct state-labelled tensor carriers
\[
C_L=LGL^\dagger,\qquad C_R=RGR^\dagger.
\tag{MR19}
\]
Both satisfy \(\mu C_L\mu^\dagger=\mu C_R\mu^\dagger=G\); for \(d>1\), they are singular and distinct. With zero duration, each unit insertion followed by multiplication is exactly the identity transition. For a nontrivial algebra, (MR15)'s common-state requirement has therefore been explicitly relaxed. The source covariance and the duration in (MR17) are still supplied. This is a compositional calibration, not their selection from multiplication.

## Correlated innovations can preserve a nontrivial unit

The independence assumption in (MR13) has a concrete alternative. Let \(U:V\to W\), \(\mu:W\to V\), with \(\mu U=I\). For a centered Gaussian \(\xi\in W\) of covariance \(C\ge0\), choose the two innovations jointly:
\[
e_U=\xi,\qquad e_\mu=-\mu\xi,\qquad
\mathsf C_U=
\begin{pmatrix}
C&-C\mu^\dagger\\
-\mu C&\mu C\mu^\dagger
\end{pmatrix}
=
\begin{bmatrix}I\\-\mu\end{bmatrix}
C
\begin{bmatrix}I&-\mu^\dagger\end{bmatrix}
\ge0.
\tag{MR20}
\]
Then \(y=Ux+\xi\), \(v=\mu y-\mu\xi=x\), and
\[
[\,\mu,I\,]\mathsf C_U[\,\mu,I\,]^\dagger=0.
\tag{MR21}
\]
The individual multiplication noise may be nonzero while the endpoint transition is exactly the Dirac unit. Its conditional rule retains the earlier innovation; it is outside the independent composition law (MR13). Normalized \(\xi\) gives total endpoint weight one, but internal sources still detect it. This alone does not prove the fixed-reference determinant and source identities required of a presentation unit.

There is a specific selection conjecture to test. From a whole marked diagram \(\mathcal D\), construct its linear presentation-relation rows \(\mathscr R_{\mathcal D}\) using multiplication, units and orientation. With the declared pairing on the joint innovation space, propose
\[
\boxed{\mathsf C_{\mathcal D}=\Pi_{\ker\mathscr R_{\mathcal D}}.}
\tag{MR22}
\]
This is an innovation covariance, not the spectral coefficient \(\Gamma\) in (MR6). For the single relation row \([\,\mu,I\,]\), the orthogonal projector is exactly (MR20) with \(C=(I_W+\mu^\dagger\mu)^{-1}\): the map \(J=\left[\begin{smallmatrix}I\\-\mu\end{smallmatrix}\right]\) spans the kernel and \(J^\dagger J=I_W+\mu^\dagger\mu\).

The raw projector already fails a refinement test if the standard metric is reset at each presentation. For scalar relation rows \(r_2=(1,1)\), \(r_3=(1,1,1)\), group the first two innovations with \(P=\left(\begin{smallmatrix}1&1&0\\0&0&1\end{smallmatrix}\right)\). Then
\[
P\Pi_{\ker r_3}P^\dagger
=\frac23\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
\ne
\Pi_{\ker r_2}
=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\tag{MR23}
\]
Both laws have zero total endpoint innovation, but their coarse source covariances differ.

Ordinary Gaussian conditioning gives an exact repair when the background covariance is transported. For \(G>0\), full-row-rank \(R\), and \(PGP^\dagger>0\), define the covariance conditioned on \(R\xi=0\). If \(R_f=R_cP\) and \(R_c\) has full row rank, direct substitution gives
\[
\Pi(G,R)=G-GR^\dagger(RGR^\dagger)^{-1}RG,
\qquad
\boxed{P\Pi(G,R_f)P^\dagger=\Pi(PGP^\dagger,R_c).}
\tag{MR24}
\]
In (MR23), the inherited background covariance is \(PP^\dagger=\operatorname{diag}(2,1)\), and the right side of (MR24) recovers the \(2/3\) coefficient. [[rg-covariance-residue/gaussian-harmonic-refresh-lifting|Gaussian harmonic lifting]] owns the corresponding covariance pushforward and conditional split.

The complete fixed-reference extension is now given by [[marked-gaussian-constraints-and-sewing-measures|marked Gaussian constraints]]. Coarsening carries a determinant ratio and, for arbitrary fine sources, a hidden-source scalar. Constraint-row densities and the actual integration fiber must also be transported; an intrinsic volume on the whole constraint surface is not automatically an identity-kernel normalization.

[[whole-multiplication-preparations-and-state-shape|A whole multiplication preparation]] imposes both units and both parenthesizations simultaneously. Its determinant-preserving family changes the output response while retaining the same multiplication, pairing and presentation identities. Thus the next selector must supply and transport the background covariance \(G_{\mathcal D}\); coherent conditioning alone does not select its shape. [[multiplication-sensitive-cycle-preparations|The commutator preparation]] supplies one explicit algebra-sensitive candidate. A genuine cycle readout \(T_\gamma\) would retain covariance \(T_\gamma\Pi(G_{\mathcal D},\mathscr R_{\mathcal D})T_\gamma^\dagger\); deriving its diagram grammar, physical transfer and uniform vacuum-sector rigidity remains open.

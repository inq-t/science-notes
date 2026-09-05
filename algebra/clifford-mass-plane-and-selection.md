# The Clifford Mass Plane and Its Selection Obstruction

A local first-order square root of the three-dimensional scalar Laplacian exists on four real components. Its constant skew mass terms form a two-dimensional plane: every nonzero member opens the corresponding free spectral edge, but automorphisms of the original Clifford triple rotate all normalized choices. The triple therefore selects neither a nonzero mass direction nor its magnitude. This is an exact statement about one constant-coefficient operator signature, not a claim that physical mass must be a Dirac term or that nature has four components.

## The operator signature

On real \(L^2(\mathbb R^3,\mathbb R^N)\), take constant matrices and the closure from Schwartz functions

\[
D=\sum_{j=1}^3 C_j\partial_j,\qquad
C_j^T=C_j,\qquad
C_iC_j+C_jC_i=2\delta_{ij}I.
\tag{CM1}
\]

Then \(D\) is skew-adjoint with domain \(H^1\), and

\[
D^2=\Delta I,\qquad |D|=\sqrt{-\Delta}\,I.
\tag{CM2}
\]

The latter is the componentwise Dirichlet-to-Neumann response of harmonic extension into \(\mathbb R^3\times\mathbb R_{\tau,+}\). A real scalar operator \(v\cdot\nabla\) cannot supply this square root: its squared principal symbol is \((v\cdot p)^2\), not \(|p|^2\). For dimension greater than one, choose nonzero \(p\perp v\).

For a **constant** real zero-order matrix \(M\) and \(m\geq0\), the conditions

\[
(D+M)^*=-(D+M),\qquad
(D+M)^2=(\Delta-m^2)I
\tag{CM3}
\]

are equivalent to

\[
M^T=-M,\qquad \{M,C_j\}=0\quad(j=1,2,3),\qquad
M^2=-m^2I.
\tag{CM4}
\]

Indeed the square contains \(\sum_j\{C_j,M\}\partial_j+M^2\); equality on every test function identifies each coefficient. Boundedness of the constant matrix preserves the skew-adjoint domain.

## Four real components suffice and are minimal

Write

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
E=XZ=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

On \(\mathbb R^2\otimes\mathbb R^2\), choose

\[
C_1=X\otimes I,\qquad C_2=Z\otimes X,\qquad C_3=Z\otimes Z.
\tag{CM5}
\]

These symmetric involutions anticommute. Two compatible skew matrices are

\[
M_1=E\otimes I,\qquad M_2=Z\otimes E.
\tag{CM6}
\]

They anticommute with every \(C_j\), satisfy \(M_1^2=M_2^2=-I\), and obey \(M_1M_2=-M_2M_1\).

There are no other independent mass directions. Expand any real \(4\times4\) matrix in the first-factor basis \(I,X,Z,E\). Anticommutation with \(C_1\) forces

\[
M=Z\otimes B+E\otimes F.
\]

The other two conditions give

\[
\{B,X\}=\{B,Z\}=0,\qquad [F,X]=[F,Z]=0.
\]

For real \(2\times2\) matrices these imply \(B=bE\) and \(F=aI\). Thus the complete classification is

\[
\boxed{M=aM_1+bM_2,\qquad M^2=-(a^2+b^2)I.}
\tag{CM7}
\]

Skewness follows automatically in this classified plane.

Minimality already follows from (CM1). The involution \(C_2\) exchanges the positive and negative eigenspaces of \(C_1\); both have dimension \(r\). After an orthogonal basis change, \(C_2\) is the off-diagonal identity. Symmetry and anticommutation then force \(C_3\) to have off-diagonal blocks \(B,B^T\), where \(B^T=-B\) and \(B^2=-I_r\). Such a real complex structure requires even \(r\). Hence \(N=2r\) is divisible by four.

A normalized nonzero \(M\) supplies a negative-square Clifford generator alongside the three positive-square generators: the signature is \(\mathrm{Cl}_{3,1}\), in that convention. This is not a fourth symmetric Euclidean generator; (CM7) shows that no such generator exists on this carrier. Carrier size, signature and [[ko-dimension-as-morita-class/two-tens|graded Morita class]] are different data.

## What the original triple cannot select

The oriented product

\[
P=C_1C_2C_3=X\otimes E=M_1M_2
\tag{CM8}
\]

commutes with every \(C_j\) and satisfies \(P^2=-I\). The same matrix expansion shows that the entire real commutant is \(\{aI+bP\}\). Its orthogonal elements are \(e^{\theta P}\), and

\[
e^{\theta P}M_1e^{-\theta P}
=\cos(2\theta)M_1+\sin(2\theta)M_2.
\tag{CM9}
\]

Thus automorphisms fixing the Clifford triple also fix its orientation \(P\), but rotate the mass plane. A rule selecting \(M\) equivariantly from that triple alone would have to return a fixed point of every rotation. Only \(M=0\) qualifies.

This is a concrete instance of [[ko-dimension-as-morita-class/what-commutes-with-everything|the commutant retaining undetected structure]]. Additional wall or pointing data could select a direction. The radius \(m=\sqrt{a^2+b^2}\) remains continuous, including zero. Declaring a matrix normalized to square to \(-I\) does not determine the inverse-length coefficient needed beside \(D\).

## Polarization and the boundary response change together

For \(m>0\), (CM3) gives

\[
A_m=|D+M|=\sqrt{-\Delta+m^2}\,I,\qquad
J_m=-(D+M)A_m^{-1},\qquad J_m^2=-I.
\tag{CM10}
\]

Then \(D+M=-J_mA_m\) and \(A_m\geq mI\). As in [[directed-analytic-realization/harmonic-boundary-realization|the harmonic boundary construction]], the complex structure and positive modulus are linked. They are not unchanged inputs: \(M\) anticommutes with the old polar structure \(J_0=-D|D|^{-1}\), defined by its bounded Fourier multiplier away from \(p=0\). Consequently \(D+M\) is not complex-linear for \(J_0\). If the skew generator defines the local pairing, that pairing also changes from \((f,Dg)\) to \((f,(D+M)g)\).

Likewise, \(A_m\) is the DN operator of \((-\partial_\tau^2-\Delta+m^2)u=0\), not of the unchanged harmonic half-space. Deriving this response from another geometry requires an actual construction of its additional term.

Finally, for smooth \(M(x)\) obeying the pointwise anticommutation conditions and \(M(x)^2=-m(x)^2I\),

\[
(D+M(x))^2
=\Delta-m(x)^2I+\sum_j C_j\partial_jM(x).
\tag{CM11}
\]

Even constant magnitude does not remove the last term. A wall-residue proposal must therefore establish its operator, normalization and spatial compatibility, not merely its Clifford type. The free signature proves an edge once these data supply it; it supplies neither a nonzero amplitude nor a Yang–Mills existence or mass-gap theorem.

The constructive target is a residue \(M\) returned by the same primitive law as \(D\), rather than independently prescribed: prove anticommutation, derive its norm in the common metric, and control the derivative term if it varies. This target is sufficient within the displayed free signature. It neither excludes other mass mechanisms nor derives the three boundary coordinates that the signature already assumes.

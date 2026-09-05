# Projection-Conditioned Coercivity

A positive contraction has a full lower bound when it controls a discarded subspace as an operator inequality and its compression controls the retained subspace. The two constants multiply, with no separate off-diagonal estimate. This is stronger than knowing the two diagonal compressions: the discarded-subspace hypothesis must hold against every vector, including mixtures of retained and discarded directions.

**Status: [EXACT SHARP OPERATOR THEOREM].** No finite-dimensionality, probability law, auxiliary clock, or physical interpretation is assumed.

## The full-space condition

Let \(P\) be an orthogonal projection on a Hilbert space \(\mathcal H\), put \(Q=I-P\), and let \(B\) be bounded and self-adjoint. Suppose
\[
0\le B\le I,\qquad
B\ge bQ,\qquad
PBP\ge aP,\qquad 0<a,b\le1.
\tag{PC1}
\]
Then
\[
\boxed{B\ge abI.}
\tag{PC2}
\]
The upper normalization \(B\le I\) is load bearing. For \(0\le B\le MI\), with \(M>0\) and lower constants \(0<a,b\le M\) in the original units, the corresponding conclusion is \(B\ge (ab/M)I\).

To prove (PC2), take \(f=x+y\), where \(x=Pf\), \(y=Qf\). If either component vanishes, the result follows directly. Otherwise compress \(B\) to the span of the orthonormal vectors \(x/\|x\|\), \(y/\|y\|\). The resulting matrix
\[
M_f=\begin{pmatrix}A&C\\\overline C&D\end{pmatrix}
\]
satisfies \(A\ge a\), \(0\le M_f\le I_2\), and
\[
M_f\ge\begin{pmatrix}0&0\\0&b\end{pmatrix}.
\]
The last inequality gives
\(\det M_f=AD-|C|^2\ge bA\ge ab\).
Since its largest eigenvalue is at most one, its smallest is at least \(ab\). Apply this compression bound to \(f\). The argument works in an arbitrary Hilbert space because only a two-dimensional compression was used.

## Sharpness and the missing mixed directions

For \(0<a,b<1\), the matrix
\[
B_{a,b}=
\begin{pmatrix}
a&\sqrt{a(1-a)(1-b)}\\
\sqrt{a(1-a)(1-b)}&1-a+ab
\end{pmatrix}
\tag{PC3}
\]
has eigenvalues \(ab,1\). Both \(I-B_{a,b}\) and
\(B_{a,b}-\operatorname{diag}(0,b)\) are positive rank-one matrices, so all hypotheses hold and the bound is sharp.

Replacing \(B\ge bQ\) by \(QBQ\ge bQ\) invalidates the theorem. For example,
\[
B=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}
\]
has both diagonal compressions equal to \(1/2\), but its difference direction has zero response. The full inequality in (PC1) rules out exactly this cancellation. Without it, [[inq|the complete innovation-block method]] requires a separate cross-block estimate.

[[bridge-data-augmentation-solder/coarse-boundary-leakage-and-response-lifting|Conditional discarded-mode control]] supplies (PC1) directly from a joint law. Its strength comes from conditioning on both the retained core and the complete boundary before estimating what remains.

# Transparent Units and Hidden Determinants

A pure identity insertion should preserve both the complete boundary response and the weight returned by elimination. For the elementary comparison \(x-y\), these two requirements select a degenerate spectral metric: the inserted variable carries no independent clock norm. The complete boundary response alone permits an arbitrary hidden rate. This is an exact finite selection theorem under a fixed comparison and integration normalization; it does not select the full physical clock.

## The unit cell and its admissible metrics

Let \(V\) be a complex Hermitian space of dimension \(d\ge1\). Its declared pairing fixes adjoints, orthonormal coordinates and the reference measure \(\prod_jd^2y_j/\pi\). On two copies, set
\[
D=[\,I,-I\,],\qquad
K=D^\dagger D=
\begin{pmatrix}I&-I\\-I&I\end{pmatrix}.
\tag{TU1}
\]
A unital multiplication restricts to this comparison through \(\mu(v\otimes1)=v\). Here \(K\) is fixed. Vary only a \(z\)-independent Hermitian matrix
\[
\Gamma=
\begin{pmatrix}A&B\\B^\dagger&C\end{pmatrix}\ge0,\qquad
Q_\Gamma(z)=z\Gamma+K,\quad z>0.
\tag{TU2}
\]
The declared reference pairing remains positive; \(\Gamma\) is the coefficient of the spectral parameter and may be degenerate. It need not equal the inherited product metric.

The interior block \(I+zC\) is positive. For \(\nu\in\mathbb N_{>0}\) independent complex Gaussian copies, elimination of \(y\) returns
\[
\mathcal Z_\Gamma(z)=
\left(
\det(I+zC)^{-\nu},
\ S_\Gamma(z)
\right),
\]
\[
S_\Gamma(z)=I+zA-
(-I+zB)(I+zC)^{-1}(-I+zB^\dagger).
\tag{TU3}
\]
The second entry is the retained form for each copy. [[determinant-response-sewing-and-relational-rigidity|Determinant–response sewing]] owns the Gaussian elimination identity. When \(S_\Gamma(z)>0\), the full pencil is positive and defines the corresponding Gaussian integral.

The uninserted boundary datum is \((1,zI)\). **Strict unit transparency** requires \(\mathcal Z_\Gamma(z)=(1,zI)\) for every \(z>0\), with the reference measure fixed and no compensating \(z\)-dependent scalar prefactor. Retaining this normalization is part of the proposed unit law.

## Joint transparency selects the unit metric

**Theorem.** Within (TU1)–(TU3), strict unit transparency holds exactly when
\[
\boxed{\Gamma_{\mathrm{unit}}=
\begin{pmatrix}I&0\\0&0\end{pmatrix}.}
\tag{TU4}
\]

**Proof.** Since \(C\ge0\), all eigenvalues of \(I+zC\) are at least one. The determinant requirement forces \(C=0\). Positivity of \(\Gamma\) then forces \(B=0\): otherwise its quadratic form on \((x,ty)\) takes negative values for some complex \(t\). With \(B=C=0\), (TU3) becomes \(S_\Gamma(z)=zA\), so \(A=I\). Conversely,
\[
Q_{\mathrm{unit}}(z)=
\begin{pmatrix}(z+1)I&-I\\-I&I\end{pmatrix},
\qquad
\langle(x,y),Q_{\mathrm{unit}}(z)(x,y)\rangle
=z\|x\|^2+\|y-x\|^2.
\tag{TU5}
\]
This is positive for \(z>0\); its interior determinant is one and its Schur complement is \(zI\). \(\square\)

No positive-definite \(\Gamma\) on both copies passes this test. The inserted variable is an algebraic auxiliary with no independent spectral norm. This is a positive matrix pencil with a degenerate coefficient, not yet an ordinary Hamiltonian on the enlarged space. In particular, \(K\) does not descend automatically to the quotient by \(\ker\Gamma\); eliminate the auxiliary before claiming a physical carrier.

## The entire boundary response can miss a soft mode

For \(V=\mathbb C\), requiring only \(S_\Gamma(z)=z\) admits exactly the family
\[
\boxed{
\Gamma_c=
\begin{pmatrix}1+c&-c\\-c&c\end{pmatrix},
\qquad c\ge0.
}
\tag{TU6}
\]
To prove completeness, write \(\Gamma=\left(\begin{smallmatrix}a&b\\\bar b&c\end{smallmatrix}\right)\ge0\). Comparing the two coefficients of \(z\) in \(\det Q_\Gamma(z)=z(1+cz)\) gives
\[
a+c+2\operatorname{Re}b=1,\qquad ac-|b|^2=c.
\tag{TU7}
\]
If \(c=0\), positivity gives \(b=0,a=1\). If \(c>0\), put \(u=a-1=|b|^2/c\ge0\). Then
\[
(u+c)^2=4(\operatorname{Re}b)^2
\le4|b|^2=4cu,
\]
so \(u=c\) and \(b=-c\). Conversely, (TU6) is nonnegative and satisfies the response identity.

In the coordinates \(s=y-x\),
\[
\langle(x,y),Q_{\Gamma_c}(z)(x,y)\rangle
=z|x|^2+(1+cz)|s|^2,
\qquad
\mathcal Z_{\Gamma_c}(z)=\big((1+cz)^{-\nu},z\big).
\tag{TU8}
\]
For \(c>0\), the generalized eigenvalue problem \(Kv=E\Gamma_cv\) has rates \(0\) and \(1/c\). The relative mode can therefore be arbitrarily soft while the full retained response is unchanged at every frequency. Its normalization factor still detects it. Normalizing each boundary law separately would erase this distinction.

This supplements [[coarse-response-memory/inq|coarse response memory]]: its full Schur response captures hidden modes that return to the selected readout, whereas this relative mode is completely decoupled after the change of variables. The determinant retains information beyond that readout. The inherited product metric \(\Gamma=I\), by contrast, changes both entries:
\[
\mathcal Z_I(z)=
\left((1+z)^{-\nu d},\frac{z(z+2)}{z+1}I\right).
\tag{TU9}
\]

## A transparent unit remains transparent inside a context

Let \(Q(z)>0\) act on any finite boundary space \(W\), and let \(P:W\to V\) select the attachment data. Adding an auxiliary through \(\|Px-y\|^2\), with no additional spectral norm, gives
\[
\widetilde Q(z)=
\begin{pmatrix}
Q(z)+P^\dagger P&-P^\dagger\\
-P&I
\end{pmatrix}.
\qquad
\boxed{\mathfrak S_y(\widetilde Q(z))=(1,Q(z)).}
\tag{TU10}
\]
The identity follows directly from the interior block \(I\). Thus a finite forest of these unit insertions can be removed in any order without changing the full amplitude. This is compatible with [[holonomy-state-refinement/overlap-kernels-and-face-refinement|full boundary integration]], which already retains exposed arguments and partition factors. The extra restriction here is transparency under an algebraic presentation identity.

The next construction is simultaneous compatibility of this unit rule with multiplication, reassociation and orientation, while preserving genuine relational cycles. The theorem fixes only the unit sector after \(D\), the reference pairing and normalization have been declared. It supplies neither the non-unit comparison metric nor the state family, physical transfer direction, vacuum sector or uniform mass gap.

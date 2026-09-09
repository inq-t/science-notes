# Marked Gaussian Constraints and Sewing Measures

Conditioning a complex Gaussian on linear relations has an exact amplitude that retains its determinant, linear sources and quadratic insertions. These data compose under linear coarsening, with a scalar factor absent from normalized probability laws. Constraint-coordinate Jacobians can be tracked by density lines, but an intrinsic volume on the whole constraint surface is not automatically the measure appropriate to a retained-boundary identity.

## Fix the delta and the marked amplitude

Let \(E=\mathbb C^n\) have its declared Hermitian pairing and normalized reference measure \(d_E\xi=d^{2n}\xi/\pi^n\). Let \(G>0\), and let \(R:E\to\mathbb C^m\) have full row rank. Use
\[
\delta_{\mathbb C}^m(u)=\pi^m\delta_{\mathbb R}^{2m}(u),
\qquad
\int\delta_{\mathbb C}^m(u)\,\frac{d^{2m}u}{\pi^m}=1.
\tag{MC1}
\]
For a source \(j\in E\) and a Hermitian quadratic mark \(T\), assume \(Q=G^{-1}+T>0\), and define
\[
\mathcal A_R(G;j,T)=
\int_E e^{-\xi^\dagger G^{-1}\xi+2\operatorname{Re}(j^\dagger\xi)-\xi^\dagger T\xi}
\delta_{\mathbb C}^m(R\xi)\,d_E\xi.
\tag{MC2}
\]
Zero-dimensional determinants equal one. Redundant constraint rows are outside (MC2): replacing determinants by pseudodeterminants does not by itself define a product of redundant delta functions.

Put \(H=Q^{-1}\), and use the conditioned covariance from [[multiplication-reassociation-and-the-process-metric|marked multiplication, MR24]]:
\[
\Pi(H,R)=H-HR^\dagger(RHR^\dagger)^{-1}RH.
\tag{MC3}
\]
The complete amplitude is
\[
\boxed{
\mathcal A_R(G;j,T)
=\frac{\det H}{\det(RHR^\dagger)}
\exp\!\big[j^\dagger\Pi(H,R)j\big].}
\tag{MC4}
\]
Indeed, completing the square gives a Gaussian of mean \(Hj\), covariance \(H\), and total factor \(\det H\,e^{j^\dagger Hj}\). Its \(R\)-image has covariance \(RHR^\dagger\). Evaluating that image density at zero gives (MC4), with the convention (MC1).

In particular, the unmarked closed normalization is
\[
Z_R(G)=\mathcal A_R(G;0,0)
=\frac{\det G}{\det(RGR^\dagger)}.
\tag{MC5}
\]
For \(C=\Pi(G,R)\), division by this factor gives the normalized conditional generating function
\[
\boxed{
\frac{\mathcal A_R(G;j,T)}{Z_R(G)}
=\frac{\exp\!\left[j^\dagger(I+CT)^{-1}Cj\right]}{\det(I+CT)}.}
\tag{MC6}
\]
Here \((I+CT)^{-1}C=C^{1/2}(I+C^{1/2}TC^{1/2})^{-1}C^{1/2}\). The determinant is positive under the stated hypothesis, even though \(CT\) need not be Hermitian. Equivalently, (MC6) is Gaussian integration on \(\ker R\); the directions in \(\ker C\) contribute unit determinant factors. Sources and quadratic marks probe the complete conditioned covariance, whereas (MC5) retains its unnormalized weight.

## Coarsening carries a scalar as well as a state

Let \(P:E\to E_c\) be onto, put \(G_c=PGP^\dagger\), and suppose \(R_f=R_cP\), with \(R_c\) of full row rank. For marks that are actual coarse readouts,
\[
j_f=P^\dagger j_c,\qquad T_f=P^\dagger T_cP,
\]
the full identity is
\[
\boxed{
\mathcal A_{R_f}(G;j_f,T_f)
=\frac{\det G}{\det G_c}\,
\mathcal A_{R_c}(G_c;j_c,T_c).}
\tag{MC7}
\]
This follows by pushing the unnormalized Gaussian measure forward:
\[
P_*\!\left(e^{-\xi^\dagger G^{-1}\xi}d_E\xi\right)
=\frac{\det G}{\det G_c}
e^{-y^\dagger G_c^{-1}y}d_{E_c}y.
\tag{MC8}
\]
The determinant ratios telescope through successive onto maps. Dividing both sides of (MC7) by their unmarked factors recovers the normalized conditional-law identity. [[rg-covariance-residue/gaussian-harmonic-refresh-lifting|Gaussian harmonic lifting]] owns the corresponding retained/fiber split; (MC7) keeps the normalization that is absorbed in its probability-law formulation.

Arbitrary fine marks must also retain their hidden-source contribution. Set
\[
H=(G^{-1}+T)^{-1},\quad H_c=PHP^\dagger,
\quad j_c=H_c^{-1}PHj,\quad V_P=\Pi(H,P).
\tag{MC9}
\]
Then
\[
\boxed{
\mathcal A_{R_cP}(G;j,T)
=\frac{\det H}{\det H_c}
e^{j^\dagger V_Pj}\,
\mathcal A_{R_c}(H_c;j_c,0).}
\tag{MC10}
\]
The coarse covariance now includes the quadratic mark. Completing the square before pushing forward proves (MC10). The scalar \(e^{j^\dagger V_Pj}\) records sources in the discarded conditional directions; carrying only \(j_c\) would lose them. Repeated use is associative by finite Gaussian disintegration, including these scalar factors.

There is an analogous normalization identity for successive independent constraint rows. If \(R=\left[\begin{smallmatrix}R_1\\R_2\end{smallmatrix}\right]\) has full row rank and \(C_1=\Pi(G,R_1)\), then
\[
\det(RGR^\dagger)
=\det(R_1GR_1^\dagger)\det(R_2C_1R_2^\dagger).
\tag{MC11}
\]
The second matrix is positive. This is the ordinary block determinant identity; it shows why imposing these constraints sequentially retains the same closed factor. Linear independence is a rank condition here, not statistical independence of the constraints.

## Constraint coordinates and the integration fiber are different

For an invertible complex \(m\times m\) matrix \(S\),
\[
\delta_{\mathbb C}^m(Su)=|\det S|^{-2}\delta_{\mathbb C}^m(u),
\qquad
\mathcal A_{SR}(G;j,T)=|\det S|^{-2}\mathcal A_R(G;j,T).
\tag{MC12}
\]
Thus the amplitude is naturally a coefficient of a density on the constraint-value space. Under the coordinate change \(u'=Su\), its reference density gains \(|\det S|^2\). Retaining this density line makes the pair covariant without setting any physical partition factor to one.

The declared ambient metric gives another precise scalarization. Let \(L:\mathbb C^{n-m}\to E\) be an isometry onto \(\ker R\). Complex coarea gives
\[
\boxed{
\mathcal A_R(G;j,T)
=\frac{
\exp\!\left[j^\dagger L(L^\dagger QL)^{-1}L^\dagger j\right]
}{\det(RR^\dagger)\det(L^\dagger QL)}.}
\tag{MC13}
\]
The real coarea Jacobian of a complex linear surjection is \(\det(RR^\dagger)\), not its square root. Multiplying (MC13) by this Jacobian yields the Gaussian partition with intrinsic volume on \(\ker R\). It is invariant under replacing \(R\) by \(SR\) and still contains the restricted precision determinant.

But this intrinsic surface volume is not a universal identity normalization. If \(x\in\mathbb C^d\) is retained, then
\[
\int \delta_{\mathbb C}^d(y-x)\,\frac{d^{2d}y}{\pi^d}=1,
\qquad
\det\!\left([\,-I,I\,][\,-I,I\,]^\dagger\right)=2^d.
\tag{MC14}
\]
Multiplying this boundary kernel by the whole-surface Jacobian would change the unit weight. At fixed boundary, coarea instead uses the restriction of the constraint map to the integrated variables; that restriction is \(I\) in (MC14). [[transparent-units-and-hidden-determinants|Transparent units]] therefore requires a declared integration fiber and reference measure, not just the name of a constraint subspace.

A useful graph presentation makes this cancellation explicit. For \(B=\left[\begin{smallmatrix}I\\M\end{smallmatrix}\right]\) and \(R=[\,-M,I\,]\), direct delta integration gives
\[
\boxed{
\mathcal A_R(G;j,T)
=\frac{\exp\!\left[(B^\dagger j)^\dagger(B^\dagger QB)^{-1}(B^\dagger j)\right]}
{\det(B^\dagger QB)}.}
\tag{MC15}
\]
Here \(\det(B^\dagger B)=\det(RR^\dagger)\), so the graph-volume factor cancels the coarea Jacobian. The remaining determinant is the actual Gaussian weight on its marked source coordinates.

These identities separate a change of presentation from a change of physical amplitude. If the precision, constraint or fiber determinants depend on retained frame variables, dropping them changes the returned law. A whole-diagram construction can preserve them by carrying the declared densities, the retained/integrated split and all marks through sewing. The formulas do not select that preparation law, nor identify its parameter with a physical clock or its spectrum with a Yang–Mills mass gap.

# Preparation Compression and the Returned Potential

A relative multiplication transfer can retain every frame harmonic while normalized conditional preparations contribute an additional response under repeated composition. The resulting generator contains a positive potential equal to the trace of the preparation metric. This follows from a specified compression law, rather than from changing density coordinates. Its tracial two-by-two member is explicit and changes both the vacuum and excitation rates; its first vacuum-centered gap initially decreases. The construction is quantum mechanics on a compact frame space, with no four-dimensional Yang–Mills return yet.

## Compare normalized preparations while retaining the whole frame

Use \(M=SU(2)\), normalized Haar measure \(dU\), and the round unit-three-sphere metric. Thus \(-\Delta\) has eigenvalues \(n(n+2)\), while the earlier convention is \(D_Q=-\Delta/4\). Use the tracial algebra, covariance \(G=g_0P_0+gP_1>0\) and \(\beta\ge0\) of [[multiplication-sensitive-cycle-preparations|the commutator preparation]]. In \(\mathcal K=L^2(P_G)\), define
\[
f_U(\xi)=e^{-\beta\|[U,\xi]\|^2/2},\qquad
w_\beta(U)=\mathbb E_G f_U^2,\qquad
\varphi_U=f_U/\sqrt{w_\beta(U)}.
\tag{PC1}
\]
The vectors are real, positive, normalized and smooth as \(\mathcal K\)-valued functions. Compactness and Gaussian moments control all their derivatives. Their overlap is
\[
s_\beta(U,V)=\langle\varphi_U,\varphi_V\rangle_{\mathcal K}
=\frac{K_\beta(U,V)}{\sqrt{w_\beta(U)w_\beta(V)}},
\qquad 0<s_\beta\le1.
\tag{PC2}
\]
It is a positive kernel with unit diagonal. Its own frame quotient still loses multiplication information, as proved in [[commutator-overlap-nullspace-and-angular-coverage|the angular-coverage theorem]].

Let \(R_\epsilon\) be the normalized relative multiplication transfer of [[relative-multiplication-transfer-and-the-rotor-limit|the rotor construction]], with its parameter \(\alpha=\epsilon^{-1}\). On smooth functions,
\[
R_\epsilon=I+\epsilon D_G\Delta+O(\epsilon^2),\qquad
D_G=\frac14\frac{\mathbb E_G S^{-5/2}}{\mathbb E_G S^{-3/2}},
\quad S=\|\xi\|^2.
\tag{PC3}
\]
That owner supplies its positive contraction property, full harmonic support and fourth-moment remainder. The time unit \(\epsilon=1/\alpha\) is a declared calibration.

Define an isometry into a larger preparation carrier,
\[
(W\psi)(U,\xi)=\psi(U)\varphi_U(\xi),
\qquad W^\dagger W=I,
\]
\[
\boxed{F_\epsilon=W^\dagger(R_\epsilon\otimes I_{\mathcal K})W,
\qquad
F_\epsilon(U,V)=R_\epsilon(U,V)s_\beta(U,V).}
\tag{PC4}
\]
This rule uses a separate preparation for the relative transfer and for the normalized overlap. The two have the same declared covariance, but their Gaussian variables are independent. The single-preparation determinant proposed in the relative-transfer owner is a different, more tightly coupled candidate.

Every \(F_\epsilon\) is a positive self-adjoint contraction. Its continuous kernel is strictly positive and positive definite, so it is trace class with trace equal to its integrated diagonal, \(R_\epsilon(I)\). It is also injective: for \(\psi\ne0\), the functions \(\varphi_\bullet(\xi)\psi\) are nonzero for almost every \(\xi\), and strict positive definiteness of \(R_\epsilon\) gives
\[
\langle\psi,F_\epsilon\psi\rangle
=\int\langle\varphi_\bullet(\xi)\psi,
R_\epsilon[\varphi_\bullet(\xi)\psi]\rangle\,dP_G(\xi)>0.
\tag{PC5}
\]
Thus the commutator's missing frame sectors are retained by this combined transfer. Positivity of a pointwise kernel alone would not prove this operator statement.

## Repeated compression returns a definite generator

For smooth \(\psi\), differentiate \(W\psi\) in the fixed product carrier. Since \(\langle\varphi_U,\nabla\varphi_U\rangle=0\),
\[
\boxed{
\mathfrak h_\beta[\psi]
=D_G\int_M\left(|\nabla\psi|^2+q_\beta|\psi|^2\right)dU,
\qquad
q_\beta(U)=\|\nabla\varphi_U\|_{\mathcal K}^2.}
\tag{PC6}
\]
The form domain is \(H^1(M)\). Smoothness and compactness make \(q_\beta\) bounded; its closed operator is
\[
H_\beta=D_G(-\Delta+q_\beta),\qquad
\boxed{F_{t/n}^{\,n}\psi\longrightarrow e^{-tH_\beta}\psi.}
\tag{PC7}
\]
The convergence is strong, uniformly for \(t\) in bounded nonnegative intervals.

Here is a direct product proof in this setting. The fourth-moment estimate underlying (PC3) also holds for smooth Hilbert-valued functions, by Taylor expansion under the same centered relative measure. Hence
\[
F_\epsilon u=u-\epsilon H_\beta u+O_u(\epsilon^2)
\]
on the smooth core. The estimate is uniform for \(u=e^{-sH_\beta}\psi\), \(0\le s\le t\), when \(\psi\) is smooth: the smooth bounded potential preserves the required Sobolev norms on compact time intervals. Subtract the semigroup's corresponding expansion and telescope the \(n\) products. Contractivity bounds the error by \(C_{\psi,t}n(t/n)^2\). Density and contractivity extend the result to all of \(L^2(M)\). No exact finite-width semigroup identity is imposed on \(F_\epsilon\).

The repeated operation contains a projection between steps:
\[
F_\epsilon^2
=W^\dagger(R_\epsilon\otimes I)
WW^\dagger(R_\epsilon\otimes I)W.
\tag{PC8}
\]
It therefore differs from advancing once in the larger carrier and reading out only at the end. This is a constitutive processing rule. [[conditional-fisher-coercivity/moving-fiber-connection|Moving-fiber transport]] explains why a mere unitary change of density representation would instead carry its score connection and could cancel the apparent Fisher term. Equation (PC6) changes the processing law explicitly; it is not that coordinate argument.

## The conditional Gaussian metric gives the potential

The actual density \(\varphi_U^2dP_G\) is the conditional Gaussian with precision
\[
Q_U=G^{-1}+\beta C_U^\dagger C_U,\qquad C_U\xi=[U,\xi].
\]
For tangent variations \(X,Y\) of \(U\), its real preparation metric is
\[
\boxed{
g^{\mathrm{prep}}_U(X,Y)
=\frac14\operatorname{Re}\operatorname{Tr}
(Q_U^{-1}Q_{U,X}Q_U^{-1}Q_{U,Y}),
\qquad q_\beta=\operatorname{tr}_{M}g^{\mathrm{prep}}.}
\tag{PC9}
\]
Differentiate the normalized Gaussian log density; its centered quadratic score has covariance equal to the displayed trace before the factor \(1/4\). Since \(\partial\varphi=\tfrac12\varphi\,\partial\log(\varphi^2)\), this proves (PC9). [[algebra/determinant-preparation-positivity-and-the-rank-threshold|The determinant preparation metric]] owns the corresponding local metric formula. This is classical Gaussian Fisher information, not an identification with every quantum state metric.

Write \(U=\cos\theta\,I+i\sin\theta\,\mathbf n\cdot\boldsymbol\sigma\), and put \(b=4\beta g\), \(p=b\sin^2\theta\). The tracial block has precision \(g^{-1}[I+p(I-\mathbf n\mathbf n^T)]\). Equation (PC9) gives
\[
g^{\mathrm{prep}}
=\frac{(p')^2}{2(1+p)^2}\,d\theta^2
+\frac{p^2}{2(1+p)}\,d\mathbf n^2,
\]
\[
\boxed{
q_\beta(\theta)
=\frac{b^2\sin^2\theta\,[3+(b-2)\sin^2\theta]}
{(1+b\sin^2\theta)^2}.}
\tag{PC10}
\]
The trace uses \(d\theta^2+\sin^2\theta\,d\mathbf n^2\). The apparent polar singularities cancel; \(q_\beta\) is a smooth nonnegative class function, invariant under the center and inversion. At \(G=G_{\rm ad}\), \(D_G=9/10\) and \(b=4\beta/9\).

## The vacuum and the first gap are outputs of this rule

The compact elliptic operator \(H_\beta\) has compact resolvent and a simple strictly positive normalized ground vector \(\psi_0\). Positivity follows from the positive scalar heat evolution with bounded real potential; connectedness makes it improving. Its vacuum-centered generator is \(H_\beta-E_0\), and the corresponding ground transform is conservative on \(L^2(\psi_0^2dU)\). The returned frame state \(\psi_0^2dU\) is generally different from the original commutator marginal \(w_\beta dU/\int w_\beta dU\).

All frame functions remain in the carrier. In particular, center-odd functions have not been removed. The first gap is positive for each fixed finite \(\beta\); for example its weighted Poincare form gives the finite bound
\[
\operatorname{gap}(H_\beta-E_0)
\ge3D_G\frac{\min_M\psi_0^2}{\max_M\psi_0^2}>0.
\tag{PC11}
\]
This uses the round-sphere Poincare inequality and the actual ground density. It gives no uniform field-theory or refinement estimate.

The weak-comparison expansion shows why a positive potential is not automatically gap enhancement. With \(\chi_n\) the \(SU(2)\) characters of degree \(n\),
\[
q_\beta=b^2\left[1-\frac{\chi_2+\chi_4}{8}\right]+O(b^3),
\]
\[
\frac{E_0}{D_G}=b^2+O(b^3),\qquad
\psi_0=1+b^2\left(\frac{\chi_2}{64}+\frac{\chi_4}{192}\right)+O(b^3).
\tag{PC12}
\]
The \(n=1\) eigenspace of \(-\Delta\) is spanned by \(a=\cos\theta\) and the three vector coordinates of the unit sphere. Conjugation separates its scalar and vector parts. The leading potential expectations on these parts are \(7/8\) and \(25/24\), respectively. Thus, for sufficiently small \(b>0\),
\[
\boxed{\operatorname{gap}(H_\beta-E_0)
=D_G\left[3-\frac{b^2}{8}+O(b^3)\right].}
\tag{PC13}
\]
For verification, Haar moments are \(\mathbb E a^2=1/4\), \(\mathbb E a^4=1/8\), \(\mathbb E a^6=5/64\); conditioned on \(a\), each vector coordinate has squared mean \((1-a^2)/3\). Bounded analytic perturbation of the isolated ground and \(n=1\) eigenspaces proves the expansions. The positive cost raises both raw levels, while the vacuum rises faster than the lowest excitation.

## Normalization is part of the chosen amplitude

Let \(\zeta_\alpha=\int k_\alpha(U,V)dV\) be the relative-transfer normalization. For a closed \(N\)-step chain, \(U_N=U_0\), the actual finite trace is
\[
\operatorname{Tr}F_{\alpha^{-1}}^N
=\zeta_\alpha^{-N}
\int\prod_{i=0}^{N-1}
\frac{k_\alpha(U_i,U_{i+1})K_\beta(U_i,U_{i+1})}
{w_\beta(U_i)}\,\prod_i dU_i.
\tag{PC14}
\]
The \(w_\beta^{-1}\) factors are frame-dependent. They implement the declared normalization of preparation vectors; dropping them would change the law. Pure presentation identity is supplied by \(F_0=I\), not by calling a finite-width kernel an identity.

Arbitrary sources can be inserted in the Gaussian edge preparations using [[commutator-preparation-transfer-and-marked-gluing|the complete marked gluing formula]]. Keep the normalization factors at their declared source-free background when differentiating that experiment. Renormalizing the feature vectors after each source insertion defines a different experiment and changes its closed response. If a homogeneous parameter varies \(G\), \(\beta\) or the normalization prescription, all those factors must be differentiated.

The gain is a specified algebra-sensitive route from comparisons to a full frame carrier, a potential, a vacuum and a dynamical response. Its group, independent preparation roles, covariance rule, comparison strength and duration calibration remain inputs. A common cosmological source is still to be derived. [[shared-preparation-state-and-mobility|The single-preparation alternative]] now has its own limit calculation: negative moments of the same local preparation determine both stationary density and mobility under degree normalization. It supplies a different law from (PC7), with the normalization choice kept explicit.

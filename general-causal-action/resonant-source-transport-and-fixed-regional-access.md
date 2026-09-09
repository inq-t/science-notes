# Resonant Source Transport Moves Fixed Regional Access

A resonant change of the five-by-five source normal form preserves complete chronological operator histories, but it moves a fixed one-face source out of its original conditional subspace. The inherited Gaussian gives an exact positive norm for that change. Every nonzero combination of the five resonant generators is detected at a corner face. Thus a spatial comparison must transport its regional source embeddings together with its operators; vacuum and clock matching alone do not specify that comparison.

**Status: exact inherited-Gaussian source-access test.** [[oriented-triad-resonance-and-the-physical-source-block|RT]] constructs the resonant generators and proves chronological-word invariance. [[five-by-five-resonance-and-the-source-selection-test|RF]] proves compatibility of all actual first-jet resonances at this size. The regional projection below belongs to the containing vacuum, as in [[localized-relational-sources-in-the-inherited-vacuum|LR]]; it is not the vacuum of a detached face.

## A resonant generator acts on one physical face

Let \(Y_\ell\) be the independent Lie-algebra-valued Gaussian modes with component variances \(\omega_\ell\), in a fixed invariant metric \(Q\). Choose a resonant triple \(i,j,k\) with
\[
a=\omega_i,\qquad b=\omega_j,\qquad c=\omega_k=a+b.
\]
Use RT's real, odd, formally skew generator
\[
N=aU_i+bU_j-cU_k-4abcP,\qquad
[K_0,N]=0,\qquad N\Omega=0.
\tag{RG1}
\]
For an invariant quadratic pairing \(F\), its vacuum-equivalent multiplier change is
\[
\boxed{\mathcal D_N(F)
=\Omega^{-1}[N,M_F]\Omega
=-2c\,Q([Y_i,Y_j],\nabla_kF).}
\tag{RG2}
\]
To verify this, write \(N=-2\sqrt{abc}(W-W^\dagger)\) as in RT10. On a quadratic invariant times \(\Omega\), the two annihilators in \(W^\dagger\) contract a scalar Hessian against the alternating tensor and give zero. The derivative terms from the two creators in \(W\) vanish for the same reason. The remaining term gives (RG2).

In the actual sine coordinates, a physical face has
\[
X_p=\sum_\ell O_{p\ell}Y_\ell,\qquad
v_p=\mathbb E_0[(X_p^\alpha)^2]
=\sum_\ell\omega_\ell O_{p\ell}^2.
\]
Its radius \(R_p=Q(X_p,X_p)\) is neutral under the full simultaneous Gauss action. Equation (RG2) gives
\[
\boxed{\mathcal D_N(R_p)
=-4cO_{pk}\,T_G(Y_i,Y_j,X_p).}
\tag{RG3}
\]
The original source is assigned to one face; its correction need not have that access footprint.

## Conditioning retains the actual exterior modes

Let \(\Pi_p=\mathbb E_0[\,\cdot\mid X_p]\), restricted to invariant sources when taking the physical carrier. Put \(o_i=O_{pi}\), \(o_j=O_{pj}\). Conditional on \(X_p=x\), the means of \(Y_i,Y_j\) are respectively \(ao_i x/v_p\) and \(bo_j x/v_p\). Their residual component covariance matrix is
\[
\Sigma_{ij\mid p}
=\begin{pmatrix}a&0\\0&b\end{pmatrix}
-\frac1{v_p}
\begin{pmatrix}ao_i\\bo_j\end{pmatrix}
\begin{pmatrix}ao_i&bo_j\end{pmatrix}.
\]
Thus
\[
\det\Sigma_{ij\mid p}
=ab\left(1-\frac{ao_i^2+bo_j^2}{v_p}\right).
\tag{RG4}
\]
Mean terms disappear from \(T_G(Y_i,Y_j,x)\) because they repeat \(x\). The residual mean is also zero by antisymmetry. Wick contraction gives its variance as
\[
\det\Sigma_{ij\mid p}
\sum_{\alpha,\beta}Q([e_\alpha,e_\beta],x)^2
=\det\Sigma_{ij\mid p}\,
\frac{\mathfrak F_Q}{d}Q(x,x).
\]
The final identity follows from simplicity: the invariant symmetric tensor obtained by contracting two structure constants is scalar, and its trace is \(\mathfrak F_Q\). Here \(d=\dim\mathfrak g\).

Consequently,
\[
\boxed{\Pi_p\mathcal D_N(R_p)=0,}
\]
\[
\boxed{\operatorname{Var}_0(\mathcal D_N(R_p)\mid X_p)
=16c^2O_{pk}^2ab
\left(1-\frac{aO_{pi}^2+bO_{pj}^2}{v_p}\right)
\frac{\mathfrak F_Q}{d}Q(X_p,X_p).}
\tag{RG5}
\]
Integrating \(Q(X_p,X_p)\), whose mean is \(dv_p\), gives
\[
\boxed{\|\mathcal D_N(R_p)\|_{L^2(\mu_0)}^2
=16c^2O_{pk}^2ab\,\mathfrak F_Q
\left(v_p-aO_{pi}^2-bO_{pj}^2\right).}
\tag{RG6}
\]
If \(O_{pk}\ne0\), the final bracket includes \(cO_{pk}^2>0\). For a non-Abelian simple algebra this norm is strictly positive: the change lies wholly outside the original one-face conditional source subspace.

## One corner detects the entire resonant family

On the five-by-five patch take \(i=(1,1)\), \(k=(5,5)\), and \(j=m\) in RF's frequency-two set \(\mathcal M\). Thus \(a=\sqrt3-1\), \(b=2\), \(c=\sqrt3+1\). For real coefficients \(\theta_m\), put
\[
N_\theta=\sum_{m\in\mathcal M}\theta_mN_m,\qquad
Z_\theta=\sum_m\theta_mY_m,\qquad
o_\theta=\sum_m O_{pm}\theta_m .
\]
For \(\theta\ne0\), applying the preceding contraction to \(Z_\theta\) gives
\[
\boxed{
\|\mathcal D_{N_\theta}(R_p)\|^2
=32ac^2O_{pk}^2\,\mathfrak F_Q
\left[
\|\theta\|^2(v_p-aO_{pi}^2)-2o_\theta^2
\right].}
\tag{RG7}
\]
Cauchy–Schwarz bounds \(o_\theta^2\) by
\(\|\theta\|^2\sum_{m\in\mathcal M}O_{pm}^2\). The remaining variance includes \(cO_{pk}^2\), so the right side is strictly positive whenever \(O_{pk}\ne0\). At the corner \(p=(1,1)\), the normalized sine basis has \(O_{pk}=1/12\).

No nonzero member of this five-dimensional resonant family therefore stabilizes that fixed one-face source subspace. This does not prove that a chosen particular normal form already preserves it, or that one choice makes every overlapping region local.

## The comparison includes its regional embedding

RT's chronological cancellation remains valid when the complete differential operator experiment is transported consistently. Equation (RG7) detects something more specific: keeping the original face conditional projection fixed while changing the normal-form identification changes which sources count as accessible there. A quotient by resonant presentation changes must transport that projection too.

[[regional-conditional-projection-and-the-vacuum-score|The actual projection derivative]] now constructs this square on fixed polynomial source families. [[two-face-source-access-and-the-normal-form-obstruction|The five-by-five aggregate test]] proves that no invariant odd normal-form choice matches the full fixed one- and two-face inventory, including choices beyond the explicit five resonant generators. The resulting embedding response must be retained; it is not an adjustable clock. [[covariant-boundary-source-and-the-oriented-return|An actual covariant conditional source]] supplies a separate response fixed by the vacuum score. No positive conditional norm here is identified with a new Hamiltonian term or an OI gap bound; [[spatial-block-sewing-and-the-vacuum-cap-response|the vacuum caps, source exchange and changed-history lag]] still belong to that estimate.

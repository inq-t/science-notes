# Regional Preparation Algebras and Vacuum Support

A charged regional tensor carrier supplies proper operator algebras, but the interacting vacuum is cyclic and separating only when its Schmidt support fills both sides in every boundary sector. The genuine four-link/three-link cut of the two-plaquette system fails this criterion at every coupling: its tree side cannot support the other side's independent loop multiplicities. A balanced cut removes that obstruction and admits explicit faithful preparations. The support criterion isolates the separate proof required for the actual vacuum; neither criterion nor calibration gives a relativistic modular inclusion or a physical gap.

## Keep the boundary representation before sewing

Use the edge partition and interior Gauss averages of [[gauge-boundary-frame-gluing/finite-gauss-gluing|finite Gauss gluing]]. Write the retained charged carriers as \(\mathcal H_A,\mathcal H_B\), their compact boundary group as \(K\), and
\[
\mathcal H_{\rm ext}=\mathcal H_A\widehat\otimes\mathcal H_B,\qquad
\mathcal H_{\rm phys}=\mathcal H_{\rm ext}^{K}.
\tag{RV1}
\]
Here the tensor factors correspond to disjoint raw edge sets. Two tree-reduced loop coordinates sharing a raw link are not automatically such a regional partition.

Take the actual positive normalized gauge-invariant vacuum amplitude \(\Omega\) in the product-Haar presentation. For a weighted presentation, [[gauge-boundary-frame-gluing/faithful-state-gluing|the correlation half-density unitary]] transports this vector and every operator together; it does not replace \(\Omega\) by a product state. Define
\[
\mathcal F_A=B(\mathcal H_A)\otimes I,\qquad
\mathcal F_B=I\otimes B(\mathcal H_B)=\mathcal F_A'.
\tag{RV2}
\]
These are proper noncommutative algebras if both regional dimensions exceed one. On the product-group carriers below, all regional multiplication readouts together with one regional strictly positive heat step generate (RV2): apply [[prepared-sources-and-the-modular-wall|the heat-kernel commutant argument]] in that factor alone. The regional heat step specifies an operator algebra; it is not identified with the whole interacting clock.

Charged operators in \(\mathcal F_A\) generally do not preserve \(\mathcal H_{\rm phys}\). Joint source products can be gauge averaged after sewing, whereas compression \(A\mapsto Q_{\rm phys}AQ_{\rm phys}\) is not generally a representation of the charged algebra. This is why the boundary ports must remain available.

## The exact charged Schmidt criterion

Decompose the boundary representations and the invariant vector as
\[
\begin{aligned}
\mathcal H_A&=\widehat\bigoplus_\lambda M_{A,\lambda}\otimes V_\lambda,
&\mathcal H_B&=\widehat\bigoplus_\mu M_{B,\mu}\otimes V_\mu,\\
\Omega&=\widehat\bigoplus_\lambda
\omega_\lambda\otimes c_\lambda,
&c_\lambda&=d_\lambda^{-1/2}\sum_{j=1}^{d_\lambda}e_j\otimes e^j,
\end{aligned}
\tag{RV3}
\]
where \(\omega_\lambda\in M_{A,\lambda}\otimes M_{B,\lambda^*}\), \(d_\lambda=\dim V_\lambda\), and \(\sum_\lambda\|\omega_\lambda\|^2=1\). An unmatched sector has zero vacuum component. Put
\[
r_{A,\lambda}=\operatorname{Tr}_{M_{B,\lambda^*}}
|\omega_\lambda\rangle\langle\omega_\lambda|,\qquad
r_{B,\lambda^*}=\operatorname{Tr}_{M_{A,\lambda}}
|\omega_\lambda\rangle\langle\omega_\lambda|.
\]
Partial tracing the normalized boundary coevaluation gives the full regional density operators
\[
\boxed{\rho_A=\bigoplus_\lambda r_{A,\lambda}\otimes I_{V_\lambda}/d_\lambda,\qquad
\rho_B=\bigoplus_\lambda r_{B,\lambda^*}\otimes I_{V_{\lambda^*}}/d_\lambda.}
\tag{RV4}
\]
The blocks are unnormalized: their traces are the actual sector weights.

**Support theorem.** On \(\mathcal H_{\rm ext}\),
\[
\boxed{
\begin{array}{ll}
\Omega\text{ separating for }\mathcal F_A
&\Longleftrightarrow\ker\rho_A=0,\\
\Omega\text{ cyclic for }\mathcal F_A
&\Longleftrightarrow\ker\rho_B=0.
\end{array}}
\tag{RV5}
\]
Thus both properties require every regional sector to have a paired partner and every reduced multiplicity block in (RV4) to have full support. In finite multiplicities this means full Schmidt rank on both sides, hence equal multiplicity dimensions. In infinite multiplicities the coefficient map must have zero kernel and dense range; invertibility with bounded inverse is not required.

For the proof, Schmidt expansion gives
\[
\overline{\mathcal F_A\Omega}
=\mathcal H_A\otimes\operatorname{supp}\rho_B,\qquad
\|(A\otimes I)\Omega\|^2=\operatorname{Tr}(\rho_AA^*A).
\tag{RV6}
\]
Finite-rank operators produce the first closure; the second identity gives separatingness. A nonzero projection onto \(\ker\rho_A\) annihilates \(\Omega\). Conversely zero expectation with faithful \(\rho_A\) implies \(A=0\). This extends the [[algebra/local-vacuum-faithfulness-and-the-loss-carrier|finite faithful-vacuum criterion]] to the exposed boundary multiplicities.

The boundary-preserving part of \(\mathcal F_A\) does descend. On the physical carrier its image and commutant are
\[
\begin{aligned}
\mathcal N_A&=\bigoplus_{\lambda}^{\ell^\infty}
B(M_{A,\lambda})\otimes I_{M_{B,\lambda^*}},\\
\mathcal N_A'&=\bigoplus_{\lambda}^{\ell^\infty}
I_{M_{A,\lambda}}\otimes B(M_{B,\lambda^*}),
\qquad
\mathcal H_{\rm phys}\cong\widehat\bigoplus_\lambda
M_{A,\lambda}\otimes M_{B,\lambda^*}.
\end{aligned}
\tag{RV7}
\]
Only paired nonzero carrier sectors occur here. The central sector projections belong to both algebras. Applying (RV6) in each block proves the same support criterion for their represented blocks; a missing vacuum sector defeats both cyclicity and separatingness. These are algebras with a boundary center, not the charged factors in (RV2).

For the smooth configuration amplitudes below, the two regional objects are
\[
\rho_A(a,a')=\int\Omega(a,b)\overline{\Omega(a',b)}\,db,\qquad
p_A(a)=\int|\Omega(a,b)|^2\,db=\rho_A(a,a).
\tag{RV7a}
\]
The probability marginal \(p_A\) is only the diagonal of the Schmidt reduced operator. Haar probability marginals or strictly positive joint configuration density do not imply (RV5). Nor does nonzero correlation imply full Schmidt support. In infinite dimension a faithful trace-class density has eigenvalues approaching zero, so (RV5) supplies no uniform lower bound on responses or on modular logarithms.

## The actual asymmetric two-plaquette cut cannot be separating

Use [[coarse-response-memory/two-plaquette-vacuum-and-relational-state|the actual two-plaquette vacuum]] \(\psi_\lambda>0\), with \(\kappa>0\) and magnetic strength \(\lambda\ge0\). Assign the left square, including the shared link, to \(A\), and the right square's other three links to \(B\). This is the [[coarse-response-memory/boundary-interaction-and-conditional-score-budget#A genuine seven-link computation|genuine seven-link cut]].

After interior Gauss averaging, let \(p,s\) denote the left outer path and shared link, and \(q\) the right outer path, all oriented between the same exposed endpoints. Then
\[
\mathcal H_A=L^2(G^2,dp\,ds),\qquad
\mathcal H_B=L^2(G,dq),\qquad K=G\times G,
\]
\[
\Omega_\lambda(p,s;q)=\psi_\lambda(ps^{-1},qs^{-1}),
\qquad G=SU(2).
\tag{RV8}
\]
The endpoint group acts by common left and right multiplication on each path. Product Haar and the displayed coordinate change preserve the vacuum norm.

Peter--Weyl decomposition makes \(\mathcal H_B\) multiplicity-free under \(G\times G\): each occurring boundary representation \(V_j\otimes V_j^*\) has multiplicity one. In contrast, the trivial boundary sector of \(\mathcal H_A\) is
\[
M_{A,\mathbf1}\cong L^2(G)^{\operatorname{Ad}G},
\qquad M_{B,\mathbf1}=\mathbb C.
\tag{RV9}
\]
Indeed \(ps^{-1}\) transforms by conjugation, and its characters give infinitely many orthogonal invariant functions. The vacuum's trivial-sector vector is
\[
\phi_\lambda(p,s)=\int_G\Omega_\lambda(p,s;q)\,dq,
\qquad \phi_\lambda>0.
\tag{RV10}
\]
It lies in \(M_{A,\mathbf1}\) by gauge invariance and Haar integration. Thus its reduced block is rank one, \(r_{A,\mathbf1}=|\phi_\lambda\rangle\langle\phi_\lambda|\). The operator equal to
\[
I_{M_{A,\mathbf1}}
-\frac{|\phi_\lambda\rangle\langle\phi_\lambda|}{\|\phi_\lambda\|^2}
\tag{RV11}
\]
in this block and zero elsewhere is nonzero, bounded, boundary invariant, and annihilates the full vacuum. Consequently \(\Omega_\lambda\) is not separating for either \(\mathcal F_A\) on the charged carrier or \(\mathcal N_A\) on the physical carrier, at every \(\lambda\ge0\).

At \(\lambda=0\), the vacuum is the product constant and has rank-one reduced densities on both complete regional carriers. The positive-coupling theorem that the vacuum depends on relative orientation does not repair (RV11). This obstruction comes from the proposed region and its multiplicities, not a failure of the interacting vacuum to be positive.

## A balanced charged preparation does pass the support test

Subdivide the shared edge at one vertex \(m\) and assign one half to each region, retaining all three common vertices \(u,v,m\) as charged boundary. Each region is now a tree joining these vertices. Pure subdivision transports the original amplitude and clock as in [[preparation-transport-through-spatial-subdivision|preparation transport]]; it does not reset their law.

After interior averaging, take \(A\)-coordinates \((p:u\to v,s:u\to m)\) and \(B\)-coordinates \((q:u\to v,t:m\to v)\). The map
\[
(q,t)\longmapsto(q,qt^{-1})
\tag{RV12}
\]
is Haar preserving and \(G^3\)-equivariant to the same two-path carrier as \(A\). The two representations therefore have matching dual multiplicities. For \(SU(2)\), the multiplicity of a boundary triple is the dimension of its trivalent invariant tensor space, zero or one: the usual tensor-product rule \(V_j\otimes V_k=\bigoplus_{\ell=|j-k|}^{j+k}V_\ell\) proves this statement. The asymmetric obstruction has disappeared.

Here is a nontrivial state that demonstrably passes. On the common carrier \(\mathcal K=L^2(G^2)\), choose \(D_A=D_p+D_s\) from a fixed bi-invariant metric, and \(\tau>0\). Its heat operator \(C_\tau=e^{-\tau D_A}\) is positive, injective, trace class and boundary equivariant. Identify the opposite carrier with \(\overline{\mathcal K}\) through (RV12), and set
\[
\Omega_\tau=\frac{\operatorname{vec}C_\tau}
{\sqrt{\operatorname{Tr}C_\tau^2}},\qquad
\rho_A=\rho_B=\frac{e^{-2\tau D_A}}{\operatorname{Tr}e^{-2\tau D_A}},
\tag{RV13}
\]
where the second equality uses the conjugate-carrier identification. Equivariance makes the vector boundary invariant; the strictly positive heat kernel makes it a positive configuration amplitude. Both reduced operators are faithful, so (RV5) proves cyclicity and separatingness for both proper charged factors. On their natural tensor spectral domain,
\[
\Delta_{\mathcal F_A,\Omega_\tau}
=\rho_A\otimes\rho_B^{-1};
\tag{RV14}
\]
its logarithm carries energy differences. This is modular dynamics of a specified preparation, not a positive physical Hamiltonian.

The heat state (RV13) is a calibration construction, not a claim that it equals the transported two-plaquette vacuum. For that actual vacuum at the balanced cut, (RV5) reduces to nonvanishing of every admissible trivalent-sector coefficient. [[interacting-vacuum-support-at-the-balanced-cut|The actual-vacuum support theorem]] proves this for \(SU(2)\) at every positive magnetic coupling, using nonnegative magnetic amplitudes and connected character fusion. Strict pointwise positivity and relational dependence alone would not prove it. The descended algebras (RV7) remain abelian in this multiplicity-one example, even when every sector is occupied: retaining the charged factors before sewing is essential to the noncommutative candidate.

These finite-regulator support tests neither demand nor establish exact relativistic modular geometry. [[modular-recurrence-and-the-regional-limit|Modular recurrence]] gives a sharper boundary: faithful type-I Schmidt preparations have recurrent modular flow, which cannot exactly dilate a nonzero positive translation generator. A limit programme must transport regional algebras, their common vacuum and source actions coherently, and then prove the required relative modular positions. It must also identify the returned physical clock with the reconstructed translation clock. [[prepared-sources-and-the-modular-wall|The modular-wall construction boundary]] and [[conditional-vacuum-rigidity-and-the-physical-gap|the complete-source gap criterion]] remain separate obligations on that same limit.

# Primitive Peirce Response on the Complete Matrix Carrier

The primitive idempotents of the Albert algebra determine a family of matrix readouts whose common invisible algebra is only the scalars. Their averaged loss has a certified positive lower bound on every traceless matrix, including the balance direction missed by the earlier cyclic contexts. The construction also gives a global finite-state entropy contraction. This is a complete finite response theorem, not a continuum Yang--Mills gap: field-dependent scalar observables require an additional, field-sensitive analysis map.

**Status: [EXACT FINITE, COMPUTER-ASSISTED] for the regular-multiplier bound; [EXACT CONSEQUENCES] for Peirce coverage and entropy contraction; [OPEN] for a physically selected context law, state, clock, and continuum comparison.** The certificate checks integer identities, not rounded numerical eigenvalues.

## The operator and its carrier

Let \(J=\mathfrak h_3(\mathbb O)\), with canonical trace metric
\(\langle x,y\rangle_J=\operatorname{tr}_J(x\circ y)\) and
\(\operatorname{tr}_J\mathbf1=3\). On \(\mathcal H_J=J_{\mathbb C}\), use the regular operators \(L_xy=x\circ y\). The Hilbert--Schmidt carrier is the entire
\[
\mathscr H=\operatorname{End}_{\mathbb C}(\mathcal H_J)
\cong M_{27}(\mathbb C),\qquad
P_{\rm sc}T=\frac{\operatorname{Tr}T}{27}I.
\tag{PP1}
\]
The Jordan unit \(\mathbf1\in J\) and matrix identity \(I=L_{\mathbf1}\) are different objects. Likewise \(P_{\mathbf1}\), the rank-one projection in \(\mathcal H_J\), differs from the superoperator \(P_{\rm sc}\).

For a real trace-orthonormal basis \((e_a)_{a=1}^{27}\), define
\[
\mathcal D T=\sum_a[L_{e_a},[L_{e_a},T]],\qquad
q(T)=\langle T,\mathcal DT\rangle_{\rm HS}
=\sum_a\|[L_{e_a},T]\|_{\rm HS}^2.
\tag{PP2}
\]
This definition is basis-independent. It operates on failure of a matrix operator to commute with Jordan multiplication, not on displacement through spacetime. Each real multiplier is self-adjoint, so \(\mathcal D\) is positive and self-adjoint.

The trace identity in [[exceptional-context-response|exceptional context response]] gives
\[
S:=\sum_aL_{e_a}^2=3I+6P_{\mathbf1},\qquad
\mathcal DT=ST+TS-2\sum_aL_{e_a}TL_{e_a}.
\tag{PP3}
\]
Indeed,
\(\langle x,Sx\rangle=\sum_a\|L_xe_a\|^2
=\operatorname{Tr}L_x^2
=3\|x\|_J^2+2(\operatorname{tr}_Jx)^2\).
Polarization proves (PP3). In particular \(-\mathcal D\) generates a finite unital trace-preserving completely positive semigroup. Its parameter has no supplied physical time unit.

## Scalar kernel and a certified quantitative bound

If \(q(T)=0\), then \(T\) commutes with every \(L_x\). Set \(b=T\mathbf1\). For each \(x\),
\[
Tx=TL_x\mathbf1=L_xb=L_bx,
\]
so \(T=L_b\). This argument allows complex \(b\).

Fix a Jordan frame \(p_1,p_2,p_3\). Applying \([L_b,L_{p_i}]=0\) to \(p_i\) gives
\((L_{p_i}-L_{p_i}^2)b=0\). Its Peirce eigenvalues eliminate every off-diagonal component of \(b\), so \(b=\sum_i\lambda_i p_i\). For nonzero \(x\in J_{ij}\),
\[
[L_b,L_x]p_i=\frac{\lambda_j-\lambda_i}{4}x.
\]
All \(\lambda_i\) are equal. Therefore
\[
\ker\mathcal D=\mathbb CI.
\tag{PP4}
\]
This proves separation; finite dimensionality then gives some positive edge. The following exact certificate supplies a specific edge:
\[
\boxed{\mathcal D(\mathcal D-3I)(\mathcal D-5I)
(\mathcal D-6I)(\mathcal D-12I)(\mathcal D-18I)=0.}
\tag{PP5}
\]

[[contemporary-puzzles/yang-mills-mass-gap/receipts/primitive_peirce_response_receipt.py|The reproducible certificate]] builds (PP5) from the existing integer Albert multiplication table. In its original coordinate basis \(b_i\), the trace metric has diagonal \(n_i=1,1,1,2,\ldots,2\), and \(M_i=2L_{b_i}\) is integral. Put
\[
A_8=\sum_i\frac2{n_i}M_i^2,\qquad
Z=A_8\otimes I+I\otimes A_8^{\mathsf T}
-2\sum_i\frac2{n_i}M_i\otimes M_i^{\mathsf T}.
\tag{PP6}
\]
Row-major vectorization identifies \(Z=8\mathcal D\). Direct integer multiplication proves
\[
Z(Z-24I)(Z-40I)(Z-48I)(Z-96I)(Z-144I)=0.
\]
The \(729\times729\) matrix has \(10{,}653\) nonzero entries and infinity row norm \(192\). The implemented partial sums are bounded by
\(\prod_r(192+|r|)=223{,}452{,}887{,}777{,}280<2^{63}\), with
\(r=0,24,40,48,96,144\); integer overflow is excluded. The receipt also verifies self-adjointness in the correctly weighted matrix-coordinate metric. This is a finite computer-assisted algebraic proof conditional on the displayed multiplication table, not a formal proof-assistant verification or a spectral fit.

By self-adjoint functional calculus, (PP5) restricts the spectrum to its six real roots. Combining with (PP4) gives
\[
\boxed{\mathcal D\ge3(I-P_{\rm sc}).}
\tag{PP7}
\]
The coefficient \(3\) is sharp. If \(Z_0\) is a nonzero Jordan derivation, then
\([Z_0,L_x]=L_{Z_0x}\) and \(\operatorname{tr}_J(Z_0x)=0\), whence
\[
q(Z_0)=\sum_a\|L_{Z_0e_a}\|_{\rm HS}^2
=3\|Z_0\|_{\rm HS}^2.
\]
Moreover \(\mathcal D\) preserves derivations because commutators of Jordan multipliers are derivations. Thus \(\mathcal DZ_0=3Z_0\). This is also checked on an explicit nonzero commutator. The regular image obeys a separate identity: using inner derivations, (PP3), and \(\sum_a e_a^2=S\mathbf1=9\mathbf1\),
\[
\mathcal D(L_x)
=L_{\,x\circ\sum_a e_a^2-\sum_a e_a\circ(x\circ e_a)}
=L_{9x-Sx}=6L_{x-P_{\mathbf1}x}.
\]

Normalization is part of the theorem: using a basis orthonormal for
\(\operatorname{tr}_J/3\) would multiply \(\mathcal D\) and its edge by three.

## Primitive readouts cover the added directions

For a primitive idempotent \(p\), \(\operatorname{tr}_Jp=\|p\|_J^2=1\).
The [[contemporary-puzzles/yang-mills-mass-gap/jordan-idempotency-and-the-stabilizer-gap|Peirce decomposition]] of \(L_p\) has eigenvalues \(1,\tfrac12,0\), with dimensions \(1,16,10\). Its orthogonal projections are
\[
\begin{aligned}
Q_1(p)&=2L_p^2-L_p,\\
Q_{1/2}(p)&=4L_p-4L_p^2,\\
Q_0(p)&=I-3L_p+2L_p^2.
\end{aligned}
\tag{PP8}
\]
They determine an ordinary matrix conditional expectation
\[
\Pi_p(T)=\sum_{\lambda\in\{1,1/2,0\}}Q_\lambda(p)TQ_\lambda(p).
\tag{PP9}
\]
It is a unital, completely positive, trace-preserving Hilbert--Schmidt projection. It removes coherence between Peirce sectors; it does not select one sector or actualize an outcome.

Orthogonality of matrix blocks gives
\[
\|[L_p,T]\|_{\rm HS}^2
\le\|(I-\Pi_p)T\|_{\rm HS}^2
\le4\|[L_p,T]\|_{\rm HS}^2.
\tag{PP10}
\]
The factors follow from the nonzero eigenvalue differences \(1/2\) and \(1\).

Average over the normalized invariant measure \(dp\) on the primitive orbit
\(\mathbb OP^2=F_4/\operatorname{Spin}(9)\). Since
\(\|p-\mathbf1/3\|_J^2=2/3\), irreducibility of \(J_0\), as recorded in
[[library/stability-of-compact-symmetric-spaces/inq|Semmelmann--Weingart]], implies
\[
\int\left|p-\frac{\mathbf1}3\right\rangle
\left\langle p-\frac{\mathbf1}3\right|\,dp
=\frac1{39}I_{J_0}.
\tag{PP11}
\]
The trace fixes the coefficient: \((2/3)/26=1/39\). Because \(L_{\mathbf1}\) commutes with every matrix, (PP11) yields
\(\int\|[L_p,T]\|^2dp=q(T)/39\).
Consequently
\[
\boxed{
\int\|(I-\Pi_p)T\|_{\rm HS}^2\,dp
\ge\frac1{13}\|(I-P_{\rm sc})T\|_{\rm HS}^2.}
\tag{PP12}
\]
This lower bound is sufficient, not asserted sharp for the pinching family. It controls the full \(728\)-dimensional complex traceless matrix carrier, not just \(L(J_0)\). A context measure \(\mu\ge\alpha\,dp\) retains the bound \(\alpha/13\); an arbitrary concentrated context law need not.

The previous unseen balance
\(T_{\rm bal}=27P_{\mathbf1}-I\) is now detected. For every primitive \(p\),
\[
\frac{\|(I-\Pi_p)T_{\rm bal}\|^2}{\|T_{\rm bal}\|^2}
=\frac6{13}.
\tag{PP13}
\]
To check it, write \(\mathbf1=p+(\mathbf1-p)\) in the orthogonal eigenvalue-\(1\) and eigenvalue-\(0\) Peirce sectors. Pinching removes the off-diagonal blocks of \(P_{\mathbf1}\), of total squared norm \(4/9\). Multiplication by \(27^2\) gives \(324\); \(\|T_{\rm bal}\|^2=702\). No direction has been deleted to obtain coverage.

## A global finite-state entropy contraction

Let \(\tau=I/27\), and use natural logarithms in quantum relative entropy. Trace-preserving conditional expectation gives
\[
D(\rho\|\tau)-D(\Pi_p\rho\|\tau)
=D(\rho\|\Pi_p\rho)=S(\Pi_p\rho)-S(\rho).
\tag{PP14}
\]
For faithful density matrices, the Hessian of \(\operatorname{Tr}\rho\log\rho\) dominates the Hilbert--Schmidt metric: the divided differences of \(\log\) on \((0,1]\) are at least one. Integrating along the line between two states gives
\(D(\rho\|\sigma)\ge\tfrac12\|\rho-\sigma\|_{\rm HS}^2\).
Support limits extend its use to \(\sigma=\Pi_p\rho\); pinching does not remove the support needed for this relative entropy.

Also, \(\log u\le u-1\), applied to \(u=27\rho\) in an eigenbasis, gives
\[
D(\rho\|\tau)\le27\operatorname{Tr}\rho^2-1
=27\|\rho-\tau\|_{\rm HS}^2.
\]
Together with (PP12),
\[
\boxed{
\int D(\rho\|\Pi_p\rho)\,dp
\ge\frac1{26}\|\rho-\tau\|_{\rm HS}^2
\ge\frac1{702}D(\rho\|\tau).}
\tag{PP15}
\]
Thus the averaged channel \(\mathcal M=\int\Pi_p\,dp\) satisfies
\[
D(\mathcal M\rho\|\tau)\le\frac{701}{702}D(\rho\|\tau).
\tag{PP16}
\]
Convexity of relative entropy proves this last step. These deliberately nonsharp constants apply to all finite density matrices, not only infinitesimal perturbations. For \(T=T^*\), \(\operatorname{Tr}T=0\), and \(|\varepsilon|\|T\|<1\), the path \(\rho_\varepsilon=(I+\varepsilon T)/27\) is faithful; its averaged loss Hessian at zero more precisely dominates \(1/13\) of the tracial BKM metric.

The invariant averaging is a specified analysis or coarse-description operation. It does not assert that nature makes random choices, that entropy is produced thermodynamically, or that this channel is a physical clock.

## The remaining change of carrier

The completion is geometric: primitive idempotents already belong to the Jordan algebra, and their Peirce sectors determine the readouts. But choosing all such readouts with invariant weight is additional response data; the original cyclic automorphism alone did not force this enlargement. The positive trace and averaged loss also do not derive an ontological time direction.

Most importantly, a fiberwise unital map on matrix-valued functions fixes every \(f(U)I\), even when \(f\) is a nonconstant gauge-invariant field observable. Matrix completeness is therefore not field completeness. [[global-local-response-reconstruction/exceptional-context-analysis-of-gauge-gradients|The differentiated-context construction]] supplies a concrete field-sensitive bridge and identifies the remaining measured-law inequality. It is there—not in the finite coefficient \(1/13\)—that the physical continuum problem remains.

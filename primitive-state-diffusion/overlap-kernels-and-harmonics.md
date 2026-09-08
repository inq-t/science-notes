# Overlap Kernels and Harmonics

Tensor powers of the trace pairing define finite-rank positive Markov comparisons on the complete square-integrable function space of a primitive Jordan orbit. Their exact harmonic multipliers distinguish comparison resolution from repeated processing and expose the nonlinear modes that a finite matrix readout cannot represent. The orbit, invariant law and tensor-overlap rule are declared geometric inputs.

**Status: [EXACT GEOMETRIC CONSTRUCTION] given the specified orbit and comparison rule, using standard compact rank-one harmonic analysis.** This is a worked derivation, not a claim of novelty for overlap kernels.

## Two primitive orbits, one comparison rule

Let \(J\) be one of the two Euclidean Jordan algebras below, with canonical trace pairing
\(\langle u,v\rangle_J=\operatorname{tr}(u\circ v)\).
Its primitive states satisfy \(p^2=p\), \(\operatorname{tr}p=1\). Give their orbit \(X\) its normalized invariant measure \(\mu\), and define
\[
t(p,q)=\langle p,q\rangle_J\in[0,1].
\]
For fixed \(p\), the variable \(t(p,q)\) under \(q\sim\mu\) has the indicated beta law.

| Jordan algebra | Primitive orbit \(X\) | \(a\) | \(b\) | \(\rho=a+b\) |
|---|---|---:|---:|---:|
| Selected rank-two corner \(\mathfrak h_2(\mathbb O)\) | \(S^8\) | \(4\) | \(4\) | \(8\) |
| Albert algebra \(\mathfrak h_3(\mathbb O)\) | \(\mathbb OP^2=F_4/\operatorname{Spin}(9)\) | \(4\) | \(8\) | \(12\) |

Thus
\[
dm_{a,b}(t)=
\frac{t^{a-1}(1-t)^{b-1}}{\mathrm B(a,b)}\,dt.
\tag{OR1}
\]
For \(S^8\), write \(p=(\mathbf1+v)/2\) in spin-factor coordinates:
\(t=(1+v\cdot w)/2\), where \(v,w\) are unit nine-vectors. Spherical slicing gives (OR1). On the Cayley plane, \(t=\cos^2\vartheta\), where the standard projective distance lies in \([0,\pi/2]\). Its radial density gives the second row.

The projective radial measure, irreducible harmonics and Jacobi addition formula used here are recorded in §2.1 of [[library/hyperuniform-point-sets-on-projective-spaces/inq|Brauchart–Grabner]]. These are load-bearing geometric inputs, not consequences of positivity alone. The Cayley plane is not being treated as a Hermitian symmetric space.

For an integer \(k\ge1\), choose the tensor-overlap comparison
\[
\kappa_k(p,q)=t(p,q)^k
=\langle p^{\otimes k},q^{\otimes k}\rangle,
\qquad
Z_k=\int_X\kappa_k(p,q)\,d\mu(q)
=\frac{(a)_k}{(\rho)_k}.
\tag{OR2}
\]
Here \((u)_k=u(u+1)\cdots(u+k-1)\) is the rising factorial. These are ordinary tensor powers of the real inner-product space \(J\); no associative multiplication of octonions is assumed.

All comparisons act on the same complex Hilbert carrier:
\[
B_k:L^2(X,\mu)\longrightarrow L^2(X,\mu),
\qquad
(B_kf)(p)=Z_k^{-1}\int_Xt(p,q)^k f(q)\,d\mu(q).
\tag{OR3}
\]
They are Markov operators with stationary law \(\mu\), symmetric by the pairing, and positive as Hilbert operators because
\[
\langle f,B_kf\rangle
=Z_k^{-1}\left\|
\int_Xq^{\otimes k}f(q)\,d\mu(q)
\right\|^2\ge0.
\tag{OR4}
\]
Thus \(0\le B_k\le I\). Each has finite rank and a nontrivial kernel.

The integer \(k\) specifies comparison resolution, not elapsed time or a spacetime lattice spacing. Tensor preparation gives the pointwise identity
\(\kappa_{k+m}=\kappa_k\kappa_m\); it does **not** give
\(B_{k+m}=B_kB_m\). Repeating a comparison means operator composition on \(L^2(X,\mu)\), a different operation.

## Harmonic analysis evaluates every channel

The compact rank-one harmonic decomposition is
\[
L^2(X,\mu)=\widehat{\bigoplus}_{\ell=0}^{\infty}\mathcal V_\ell,
\qquad \mathcal V_0=\mathbb C1.
\tag{OR5}
\]
These are complete, finite-dimensional, pairwise inequivalent irreducible spherical spaces. The normalized zonal function in \(\mathcal V_\ell\) is
\[
\varphi_\ell(t)=
\frac{P_\ell^{(b-1,a-1)}(2t-1)}
{P_\ell^{(b-1,a-1)}(1)},
\qquad
P_\ell^{(b-1,a-1)}(1)=\frac{(b)_\ell}{\ell!}.
\tag{OR6}
\]
Completeness concerns all square-integrable functions on the orbit, not only functions of one chosen radial coordinate. It follows from the compact Laplace spectral decomposition and the spherical-space identification.

Invariance and the addition formula make \(B_k\) scalar on every \(\mathcal V_\ell\). Evaluating on its zonal function at the pole gives
\[
\boxed{
B_k|_{\mathcal V_\ell}=\lambda_{k,\ell}I,\qquad
\lambda_{k,\ell}=
\begin{cases}
\displaystyle\frac{k^{\underline\ell}}{(k+\rho)_\ell},
&0\le\ell\le k,\\[6pt]
0,&\ell>k,
\end{cases}}
\tag{OR7}
\]
where \(k^{\underline\ell}=k(k-1)\cdots(k-\ell+1)\).

To verify the scalar rather than infer it from a spectral fit, use shifted Rodrigues:
\[
t^{a-1}(1-t)^{b-1}P_\ell^{(b-1,a-1)}(2t-1)
=\frac{(-1)^\ell}{\ell!}
\frac{d^\ell}{dt^\ell}
\left[t^{a+\ell-1}(1-t)^{b+\ell-1}\right].
\]
Integrating against \(t^k\), every endpoint term vanishes for the parameters above. After \(\ell\) integrations by parts, division by the zonal normalization and by \(Z_k\) gives
\[
\lambda_{k,\ell}
=\frac{k^{\underline\ell}\mathrm B(k+a,b+\ell)}
{(b)_\ell\mathrm B(k+a,b)}
=\frac{k^{\underline\ell}}{(k+\rho)_\ell}.
\]
For \(\ell>k\), the differentiated polynomial is zero.

The first comparison already exposes a carrier trap. On the Albert orbit, \(B_1\) has eigenvalues \(1\) on constants, \(1/13\) on the \(26\) traceless linear symbols, and zero on their infinite-dimensional orthogonal complement. The same linear moment is [[exceptional-state-comparison/primitive-peirce-response|PP11]], but the pinching loss in PP12 acts on matrices, not on the present function carrier. Matching a coefficient does not identify those operators.

In particular, \(-\log B_1\) is not a densely defined self-adjoint Hamiltonian on the full carrier: \(e^{-H}\) for a nonnegative self-adjoint \(H\) has no kernel. Restricting to the nonzero modes would delete nonlinear distinctions. [[primitive-state-diffusion/comparison-refinement-and-loss-rate|Comparison refinement]] constructs a limiting generator on the whole carrier without that restriction.

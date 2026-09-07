# Primitive Overlap Refinement and the Emergent Diffusion

Tensor powers of the pairing between primitive Jordan states define positive comparison operators. Repeating progressively sharper comparisons constructs a continuous diffusion on the complete state-space carrier, with a determined spectral shape and a positive threshold uniform in that refinement. On the rank-two octonionic corner this produces the spherical generator previously supplied in the sphere-to-ball descent. The primitive orbit, invariant law and comparison rule remain declared inputs; the result constructs a state-space clock, not a Yang–Mills theory or a physical mass.

**Status: [EXACT GEOMETRIC CONSTRUCTION] given the specified orbit and comparison rule, using standard compact rank-one harmonic analysis.** The calculation below is a worked derivation, not a claim of novelty for overlap kernels or diffusion limits.

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

The first comparison already exposes a carrier trap. On the Albert orbit, \(B_1\) has eigenvalues \(1\) on constants, \(1/13\) on the \(26\) traceless linear symbols, and zero on their infinite-dimensional orthogonal complement. The same linear moment is [[primitive-peirce-response|PP11]], but the pinching loss in PP12 acts on matrices, not on the present function carrier. Matching a coefficient does not identify those operators.

In particular, \(-\log B_1\) is not a densely defined self-adjoint Hamiltonian on the full carrier: \(e^{-H}\) for a nonnegative self-adjoint \(H\) has no kernel. Restricting to the nonzero modes would delete nonlinear distinctions. The following construction does not make that restriction.

## Processing at the comparison scale retains the whole carrier

Define
\[
H_k=k(I-B_k).
\tag{OR8}
\]
It is a bounded nonnegative self-adjoint operator on all of \(L^2(X,\mu)\). Its continuous Markov interpolation is
\[
e^{-sH_k}
=e^{-ks}\sum_{j=0}^{\infty}\frac{(ks)^j}{j!}B_k^j,
\qquad s\ge0.
\tag{OR9}
\]
This positive averaging identity is a mathematical representation; it makes no assertion of stochastic ontology. On every harmonic with \(\ell>k\), \(H_k=kI\): those directions have not been removed.

For \(\ell<k\),
\[
\frac{\lambda_{k,\ell+1}}{\lambda_{k,\ell}}
=\frac{k-\ell}{k+\rho+\ell}<1.
\]
Hence \(h_{k,\ell}=k(1-\lambda_{k,\ell})\) increases with \(\ell\) until its constant tail. The complete-carrier edge is therefore
\[
\boxed{
\ker H_k=\mathbb C1,\qquad
\operatorname{gap}H_k=\frac{\rho k}{k+\rho}
\ge\frac{\rho}{1+\rho}.}
\tag{OR10}
\]
Uniformity here is in comparison refinement \(k\), on a fixed compact orbit. It is not spatial-volume uniformity.

The rate \(k\) has a geometric scale explanation. Under the normalized kernel centered at \(p\), \(t\) has law \(\operatorname{Beta}(k+a,b)\). Since \(\|p-q\|_J^2=2(1-t)\),
\[
\boxed{
\mathbb E_k\|p-q\|_J^2=\frac{2b}{k+\rho}.}
\tag{OR11}
\]
The real dimension of \(X\) is \(2b\). A single comparison makes a mean squared displacement of order \(k^{-1}\); order \(k\) repetitions produce a finite diffusive scale. This fixes a relative refinement speed, not seconds.

## The limiting operator and its domain

For each fixed harmonic degree, expansion of the finite product in (OR7) gives
\[
\lambda_{k,\ell}
=1-\frac{\ell(\ell+\rho-1)}{k}+O_\ell(k^{-2}),
\qquad
h_{k,\ell}\longrightarrow E_\ell:=\ell(\ell+\rho-1).
\tag{OR12}
\]
Define the limiting self-adjoint operator by the complete decomposition:
\[
H_\infty f=\sum_{\ell\ge0}E_\ell f_\ell,\qquad
\operatorname{Dom}H_\infty=
\left\{f:\sum_{\ell\ge0}E_\ell^2\|f_\ell\|^2<\infty\right\}.
\tag{OR13}
\]
Its form domain replaces \(E_\ell^2\) by \(E_\ell\). Finite harmonic sums are cores in both graph norms. The ground space is exactly \(\mathbb C1\), and the gap is \(\rho\).

There is more than channelwise convergence:
\[
\boxed{
\|(I+H_k)^{-1}-(I+H_\infty)^{-1}\|\longrightarrow0,\qquad
\|e^{-sH_k}-e^{-sH_\infty}\|\longrightarrow0
\quad(s>0).}
\tag{OR14}
\]
To prove this, split at a fixed degree \(M\). On the finite head, coefficients converge. Monotonicity bounds the resolvent tail by
\[
(1+h_{k,M+1})^{-1}+(1+E_{M+1})^{-1},
\]
and the heat tail by \(e^{-s h_{k,M+1}}+e^{-sE_{M+1}}\).
First let \(k\to\infty\), then \(M\to\infty\). This controls the entire infinite tail, not a truncation chosen to favor the gap. Positivity preservation and the Markov property pass to the heat limit. The Hilbert clocks \(e^{-iuH_k}\) converge strongly to \(e^{-iuH_\infty}\); operator-norm unitary convergence is not asserted.

Ordinary repeated comparison gives the same limit:
\[
\boxed{
\|B_k^{\lfloor ks\rfloor}-e^{-sH_\infty}\|
\longrightarrow0\qquad(s>0).}
\tag{OR15}
\]
For fixed \(\ell\), \(\lfloor ks\rfloor\log\lambda_{k,\ell}\to-sE_\ell\).
For the tail, once \(\lfloor ks\rfloor\ge1\), monotonicity bounds every
\(\lambda_{k,\ell}^{\lfloor ks\rfloor}\), \(\ell>M\), by
\(\lambda_{k,M+1}^{\lfloor ks\rfloor}\). Its limit is \(e^{-sE_{M+1}}\).
The same head-tail argument applies. Thus Poisson interpolation is not an extra choice needed to obtain the limiting dynamics.

The norm assertions are for fixed \(s>0\), not uniformly down to zero. For \(0<s<1/k\), the ordinary iterate is \(I\), whose norm distance from \(e^{-sH_\infty}\) is one.

## The squared-norm loss returns the same rate

The [[directed-isometric-residue-completion/inq|defect composition law]]
can now be evaluated on these geometrically constructed comparisons,
rather than on an arbitrary supplied transfer. On the same function carrier set
\[
D_k=\frac{k}{2}(I-B_k^*B_k)
=H_k-\frac{H_k^2}{2k}.
\tag{OR15a}
\]
Its eigenvalues \(d_{k,\ell}=\tfrac{k}{2}(1-\lambda_{k,\ell}^2)\)
increase with degree, converge to \(E_\ell\) at every fixed degree, and
have full tail \(k/2\). Thus the head-tail proof of (OR14) also gives
norm-resolvent convergence \(D_k\to H_\infty\), and operator-norm
convergence of their heat operators at every fixed positive time.

More precisely,
\[
\tfrac12 H_k\le D_k\le H_k\le H_\infty
\quad\text{as quadratic forms}.
\tag{OR15b}
\]
For the last inequality, when \(\ell\le k\), write each product factor
in (OR7) as \(1-(\rho+2j)/(k+\rho+j)\). The inequality
\(1-\prod_j(1-u_j)\le\sum_j u_j\), for \(0\le u_j\le1\), gives
\(h_{k,\ell}\le\sum_{j=0}^{\ell-1}(\rho+2j)=E_\ell\).
For \(\ell>k\), use \(h_{k,\ell}=k\le E_\ell\).
The other inequalities follow from \(0\le B_k\le I\).

Consequently, for every \(f\in\operatorname{Dom}H_\infty^{1/2}\),
dominated summation over the complete decomposition proves
\[
\boxed{
\lim_{k\to\infty}\frac{k}{2}
\bigl(\|f\|^2-\|B_kf\|^2\bigr)
=\|H_\infty^{1/2}f\|^2.}
\tag{OR15c}
\]
Outside this form domain the limit is \(+\infty\): every finite harmonic
head supplies a lower bound converging to its partial energy sum, and
those sums are unbounded. Thus the extended loss-rate limit recovers the
form domain as well as the form. This is not generator-norm convergence:
on \(\ker B_k\), \(H_k=kI\) but \(D_k=(k/2)I\), so
\(\|H_k-D_k\|=k/2\).

This is a concrete typing of a loss **rate**: the numerator is missing
squared Hilbert norm and the denominator is twice the comparison duration
\(1/k\). It is not Shannon entropy, rest mass or a count of obtained facts.
At finite \(k\), high harmonics are erased while low harmonics are only
attenuated. The positive limiting edge is therefore not simply the presence
of a kernel. Its value comes from the quantitative comparison law.

## Which geometric Laplacian has appeared?

The trace pairing induces a metric \(g_{\rm tr}\) on \(X\). The tangent space at \(q\) is the Peirce half-space \(J_{1/2}(q)\), so
\(\nabla_q t=Q_{1/2}(q)p\). Pairing the identity \(p^2=p\) with \(q\) yields
\[
t=\langle q,p^2\rangle
=\langle q\circ p,p\rangle
=t^2+\frac12\|Q_{1/2}(q)p\|_J^2.
\]
Consequently
\[
|\nabla t|_{g_{\rm tr}}^2=2t(1-t).
\]
Using the invariant radial density (OR1), the nonpositive Laplace operator on radial functions is
\[
\Delta_{g_{\rm tr}}
=2\left[t(1-t)\partial_t^2+(a-\rho t)\partial_t\right].
\]
Its Jacobi eigenvalues, together with (OR5), identify the full operator:
\[
\boxed{H_\infty=-\frac12\Delta_{g_{\rm tr}}.}
\tag{OR16}
\]

On the rank-two sphere, \(g_{\rm tr}=\tfrac12g_{\text{unit }S^8}\), so
\(H_\infty=-\Delta_{\text{unit }S^8}\) and its gap is eight. On the Cayley plane with the standard projective metric of diameter \(\pi/2\), the nonnegative Laplace spectrum is \(4\ell(\ell+11)\); \(H_\infty\) is one quarter of that Laplacian and has gap twelve. These different numerical factors are metric conventions, not different physical predictions.

## The existing ball descent now has an upstream operator construction

Use the fixed projection \(q:S^8\to\overline B^3\) and isometry
\(Uf=f\circ q\) from [[sphere-to-ball-descent-and-the-jacobi-response|sphere-to-ball descent]]. Its retained law is
\[
d\nu(x)=\frac{105}{32\pi}(1-|x|^2)^2\,dx.
\]
The range of \(U\) is the hidden \(SO(6)\)-invariant subspace. Every \(B_k\) commutes with the full sphere rotation group, hence reduces this subspace. Therefore its compressed comparisons act on the **complete** \(L^2(\overline B^3,\nu)\), and the limits in (OR14)–(OR15) pass through the compression.

With its inherited domain, the limiting ball operator is exactly
\[
\boxed{
U^*H_\infty U
=-\sum_{i,j=1}^3(\delta_{ij}-x_ix_j)\partial_i\partial_j
+8x\cdot\nabla.}
\tag{OR17}
\]
Its polynomial degree-\(\ell\) spaces inherit \(\lambda_{k,\ell}\) with \(\rho=8\), not merely the three linear Bloch modes. The earlier note supplies the boundary realization and polynomial core. [[jordan-covariance-and-the-entropy-weighted-ball|Jordan covariance]] then identifies the returned co-metric with symmetrized qubit covariance.

Previously the round generator was an independent starting datum. The overlap rule now constructs it on the same whole carrier and constrains its local return, once the orbit and repeated-comparison law are chosen. It does not derive the chosen complex projection or identify three Bloch parameters with physical space.

## What has not become necessary

The construction fixes a spectral shape from a declared geometric comparison law. It does not prove that positivity, Jordan structure or forgetting uniquely requires that law. Choosing square-integrable functions of primitive states and then complexifying that carrier is also an observable-realization choice; it does not construct the noncommutative physical observable algebra.

For example, \(R=(I+H_\infty)^{-1}=\int_0^\infty e^{-t}e^{-tH_\infty}dt\) is also a symmetric Markov comparison with the same invariant measure. Its jump generator
\(I-R=H_\infty/(I+H_\infty)\) has the same vacuum and symmetries but nonproportional spectral rates. The tensor-overlap refinement assumption excludes this alternative; symmetry and positivity alone do not.

An overall clock scale remains. If the speed in (OR8) is replaced by \(c_k>0\), a finite nonzero limiting first eigenvalue requires \(c_k/k\to c>0\); the limiting operator is then \(cH_\infty\). Comparison geometry provides the relative scale in (OR11), not an identification of its parameter with physical proper time.

Likewise, the invariant law and symmetric pairing supply detailed balance. This is not yet symmetry emerging from arbitrary asymmetric primitives. Increasing comparison resolution is not an inverse to an obtained fact, and the interpolation does not construct records. The hidden-circulation extension of the sphere-to-ball note remains a separate example of a non-detailed-balanced whole with this same local return.

The positive edge survives sharpening comparisons on a fixed compact state geometry. It does not survive an arbitrary expansion of that metric with a fixed Laplace-rate convention: replacing \(g\) by \(R^2g\) scales the edge by \(R^{-2}\). Nothing here supplies a spatially local observable net, a Poincaré representation, an interacting Yang–Mills ultraviolet limit, or a relation between this state-space response and the physical vacuum spectrum. Those are the remaining return obligations, not consequences of (OR10).

The next constructive obligation is a non-product composition law that
determines contextual observable algebras, their compatible positive joint
states and their interacting evolution together. The feature tensors in
(OR2) are not such a law for composing physical subsystems. Placing copies
of \(X\) on a separately chosen graph and appending interactions would
reintroduce the arena and dynamics as independent inputs.
[[gauge-boundary-frame-gluing/overlap-kernels-and-face-refinement|The group-side face-refinement construction]]
is a limited bridge: a faithful trace comparison determines a joint gauge
law on a supplied box through exact boundary integration. Its group and
face-product prescription are explicit additional inputs, not consequences
of the Jordan feature tensors. Full refinement requires the larger
many-channel boundary amplitudes identified there.
The existing [[directed-analytic-realization/three-dimensional-boundary-test|three-dimensional boundary test]]
is a relevant return test: even a genuine infinite-space clock gap can fail
local commutation and the joint mass-invariant condition.

[[directed-analytic-realization/sphere_ball_descent_receipt.py|The shared receipt]] independently integrates shifted Jacobi polynomials against beta moments, checks both parameter rows, and tabulates refinement while retaining the previous ball tests. [[directed-analytic-realization/sphere-ball-descent-receipt-output.txt|Its saved output]] reports finite arithmetic evidence. The complete harmonic decomposition and the tail arguments above, not those samples, establish the infinite-dimensional convergence.

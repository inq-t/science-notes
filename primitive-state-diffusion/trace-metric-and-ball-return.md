# Trace Metric and Ball Return

The primitive-overlap refinement limit equals one half of the nonnegative Laplacian for the Jordan trace metric. On the rank-two octonionic orbit it is the round-sphere generator, whose fixed projection returns the full weighted ball diffusion with its inherited domain. This identifies a geometric state-space response while leaving the physical clock, observable composition and spacetime realization open.

Let \(t(p,q)=\langle p,q\rangle_J\), \(a,b,\rho=a+b\), and \(\mathcal V_\ell\) have the meanings in [[primitive-state-diffusion/overlap-kernels-and-harmonics|overlap kernels and harmonics]], and let \(H_\infty\) be the complete-carrier operator constructed in [[primitive-state-diffusion/comparison-refinement-and-loss-rate|comparison refinement and loss rate]]. Its eigenvalues are \(\ell(\ell+\rho-1)\), with the operator and form domains given there.

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

## The ball descent has an upstream operator construction

Use the fixed projection \(q:S^8\to\overline B^3\) and isometry
\(Uf=f\circ q\) from [[algebra/sphere-to-ball-descent-and-the-jacobi-response|sphere-to-ball descent]]. Its retained law is
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
Its polynomial degree-\(\ell\) spaces inherit \(\lambda_{k,\ell}\) with \(\rho=8\), not merely the three linear Bloch modes. The sphere-to-ball note supplies the boundary realization and polynomial core. [[algebra/jordan-covariance-and-the-entropy-weighted-ball|Jordan covariance]] then identifies the returned co-metric with symmetrized qubit covariance.

The sphere-to-ball descent accepts the round generator as an input. The overlap rule constructs that input on the same whole carrier and constrains its local return, once the orbit and repeated-comparison law are chosen. It does not derive the chosen complex projection or identify three Bloch parameters with physical space.

## What has not become necessary

The construction fixes a spectral shape from a declared geometric comparison law. It does not prove that positivity, Jordan structure or forgetting uniquely requires that law. Choosing square-integrable functions of primitive states and then complexifying that carrier is also an observable-realization choice; it does not construct the noncommutative physical observable algebra.

The [[primitive-state-diffusion/comparison-refinement-and-loss-rate#The comparison law and its clock remain choices|alternative comparison and clock rescaling]] show explicitly why the tensor-overlap law and its time normalization are additional choices.

Likewise, the invariant law and symmetric pairing supply detailed balance. This is not yet symmetry emerging from arbitrary asymmetric primitives. Increasing comparison resolution is not an inverse to an obtained fact, and the interpolation does not construct records. The hidden-circulation extension of the sphere-to-ball note remains a separate example of a non-detailed-balanced whole with this same local return.

The positive edge survives sharpening comparisons on a fixed compact state geometry. It does not survive an arbitrary expansion of that metric with a fixed Laplace-rate convention: replacing \(g\) by \(R^2g\) scales the edge by \(R^{-2}\). Nothing here supplies a spatially local observable net, a Poincaré representation, an interacting Yang–Mills ultraviolet limit, or a relation between this state-space response and the physical vacuum spectrum. Those are the remaining return obligations, not consequences of (OR10).

The next constructive obligation is a non-product composition law that
determines contextual observable algebras, their compatible positive joint
states and their interacting evolution together. The feature tensors in
(OR2) are not such a law for composing physical subsystems. Placing copies
of \(X\) on a separately chosen graph and appending interactions would
reintroduce the arena and dynamics as independent inputs.
[[holonomy-state-refinement/overlap-kernels-and-face-refinement|The group-side face-refinement construction]]
is a limited bridge: a faithful trace comparison determines a joint gauge
law on a supplied box through exact boundary integration. Its group and
face-product prescription are explicit additional inputs, not consequences
of the Jordan feature tensors. Full refinement requires the larger
many-channel boundary amplitudes identified there.
The existing [[directed-analytic-realization/three-dimensional-boundary-test|three-dimensional boundary test]]
is a relevant return test: even a genuine infinite-space clock gap can fail
local commutation and the joint mass-invariant condition.

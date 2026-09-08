# Finite Entropy Cost and Rank-Changing Readout

A readout can forget whole geometric fibers while losing only finite relative distinguishability. Projection of a round sphere onto a ball gives an explicit example: its conditional fibers are normalized spheres, and the entropy deficit is their state-weighted conditional relative entropy. The deficit composes with the processed state, not as an arbitrary fixed charge on each occurrence of a map. Its quadratic response acts on forgotten incoming distinctions and does not automatically create stiffness on retained output directions. This supplies a finite-cost member outside the invertible volume-clock formula, not a rule selecting outcomes or a physical mass.

## The reference law and the actual fibers

Let \(\mu\) be normalized rotation-invariant surface measure on \(S^{n-1}\subset\mathbb R^n\), and let \(q\) retain the first \(k\) coordinates, \(1\le k<n\):
\[
q:S^{n-1}\longrightarrow\overline B^k,\qquad
q(x,y)=x,\qquad |x|^2+|y|^2=1.
\tag{FE1}
\]
The choice of round reference measure is essential. An arbitrary probability measure on the sphere would not generally have the uniform conditional fibers below.

Write \(m=n-k\) and \(\nu=q_*\mu\). Its density on the open unit ball is
\[
\boxed{
d\nu(x)=
\frac{\Gamma(n/2)}{\pi^{k/2}\Gamma(m/2)}
(1-|x|^2)^{(m-2)/2}\,dx.}
\tag{FE2}
\]
For \(|x|<1\), the conditional probability measure \(\mu_x\) is the pushforward of normalized surface measure on \(S^{m-1}\) by
\[
\omega\longmapsto (x,\sqrt{1-|x|^2}\,\omega).
\tag{FE3}
\]
In particular
\(\int h\,d\mu=\int\!\int h\,d\mu_x\,d\nu(x)\).
The fiber measure is normalized, not unnormalized Hausdorff area. [[sphere-to-ball-descent-and-the-jacobi-response|Sphere-to-ball descent, SB1–SB4]] owns the coarea derivation, normalization and observable pullback; the density in (FE2) includes the horizontal Jacobian as well as the fiber volume.

At \(|x|=1\), the fiber collapses and the differential rank drops from \(k\) to \(k-1\). This boundary is \(\nu\)-null, so its conditional measure can be specified separately without changing any integral. When \(m=1\), the regular fiber is the two-point sphere \(S^0\). When \(m>1\), the readout also has a nonzero-dimensional kernel on every regular tangent space.

For the nine-dimensional trace-free corner in
[[exceptional-state-comparison/peirce-context-averaging-and-the-emergent-qubit-process|Peirce context averaging]], projection onto a marked three-plane gives
\[
n=9,\qquad k=3,\qquad
d\nu(x)=\frac{105}{32\pi}(1-|x|^2)^2\,dx,
\qquad \mu_x\text{ supported on a scaled }S^5.
\tag{FE4}
\]
The source is \(S^8\), not \(S^6\). This is a probability model on the corner's direction sphere with a declared invariant law; it does not identify these dimensions with spacetime.

## A bounded input density has finite loss

Take a measurable density \(f\) with
\[
\int f\,d\mu=1,\qquad 0<\alpha\le f\le\beta<\infty.
\]
The readout density relative to the pushed-forward reference is
\[
g(x)=\int f\,d\mu_x,\qquad
q_*(f\mu)=g\nu,\qquad \alpha\le g\le\beta.
\]
For a normalized density \(h\), write
\(\operatorname{Ent}_\lambda(h)=\int h\log h\,d\lambda\):
this is relative entropy against the probability reference \(\lambda\), not differential entropy against an unrelated coordinate volume.

The exact deficit is
\[
\boxed{
\mathcal L_q^\mu(f)
=\operatorname{Ent}_\mu(f)-\operatorname{Ent}_\nu(g)
=\int g(x)\,
\operatorname{Ent}_{\mu_x}\!\left(\frac{f}{g(x)}\right)d\nu(x)
\ge0.}
\tag{FE5}
\]
Indeed \(f/g(x)\) is a normalized density on each fiber. Expanding
\(\log f=\log g(x)+\log(f/g(x))\) proves the identity, and conditional Jensen gives positivity. The bounds on \(f,g\) justify every integral; more sharply,
\[
0\le\mathcal L_q^\mu(f)\le\operatorname{Ent}_\mu(f)\le\log\beta.
\tag{FE6}
\]
Thus geometric dimension loss and the Jacobian's boundary degeneration do not force infinite relative-entropy cost.

Equality holds exactly when \(f=g\circ q\), up to \(\mu\)-null sets. The uniform density \(f=1\), or any already-retained density, has zero deficit despite the same noninjective geometry. Conversely, \(f=1+\epsilon\,\xi_{k+1}\), \(0<|\epsilon|<1\), has \(g=1\) by fiber reflection and strictly positive finite loss. Near zero that loss is \(\epsilon^2/(2n)+O(\epsilon^4)\).

These are state-dependent costs. They compare the specified state to its reference along a deterministic readout; the probability formalism does not assert ontological chance.

## Composition transports the density

For a further measurable readout \(r:\overline B^k\to Y\) into a standard Borel space, put \(\eta=r_*\nu\) and \(h=\mathbb E_\nu[g\mid r]\), expressed as a density on \(Y\). Telescoping gives
\[
\boxed{
\mathcal L_{r\circ q}^\mu(f)
=\mathcal L_q^\mu(f)+\mathcal L_r^\nu(g).}
\tag{FE7}
\]
This is the concrete commutative member of the
[[channel-loss-and-recovery/relative-entropy-loss-and-sufficiency|descent-loss cocycle, D1–D3]].
The second cost is evaluated on the processed density \(g\), with its actual reference \(\nu\).

To discuss repetition without composing maps of incompatible types, pull the readout back to the source:
\[
Q_qf(x)=\int f\,d\mu_x,\qquad
Jg=g\circ q,\qquad E=JQ_q.
\]
This conditional expectation satisfies \(E^2=E\), and
\(\mathcal L_E(f):=\operatorname{Ent}_\mu(f)-\operatorname{Ent}_\mu(Ef)
=\mathcal L_q^\mu(f)\). Therefore
\[
\mathcal L_E(Ef)=0,\qquad
\mathcal L_{E^2}(f)=\mathcal L_E(f).
\tag{FE8}
\]
A first application can cost something; the same application to its already-processed state costs nothing further.

[[octonionic-hopf-descent-and-the-complex-purification|The Hopf/Gram factorization]]
gives a concrete two-stage realization of (FE7): an amplitude first
forgets an octonionic \(S^7\) fiber, then the selected readout forgets a
five-dimensional sphere of retained Hopf presentations. The composite is
the complex qubit partial trace; the loss identity follows the maps and
processed states, not a sum of fiber dimensions.

By contrast, any finite state-independent scalar assignment satisfying
\(c(ba)=c(a)+c(b)\) must obey \(c(E)=2c(E)\), hence \(c(E)=0\). One cannot charge a new identical finite scalar cost on every repetition of an idempotent while retaining this additive law. A changed input, reference or readout would be a different comparison.

## The Hessian remains on incoming distinctions

For bounded real \(h\) with \(\int h\,d\mu=0\), expand at the reference density:
\[
\boxed{
\mathcal L_q^\mu(1+\epsilon h)
=\frac{\epsilon^2}{2}
\left(\|h\|_{L^2(\mu)}^2-\|Eh\|_{L^2(\mu)}^2\right)
+O(\epsilon^3)
=\frac{\epsilon^2}{2}\|h-Eh\|_2^2+O(\epsilon^3).}
\tag{FE9}
\]
The entropy Taylor expansion and orthogonality of conditional expectation suffice. The quadratic form extends as the bounded projection \(I-E\) on \(L^2(\mu)\). These density-function carriers are infinite dimensional even though the sphere and ball have finite geometric dimension.

As in the existing recovery-fork theorem, no retained lower stiffness follows. For every centered retained tangent \(u\in L^2(\nu)\), the lift \(h=u\circ q\) has output \(u\) and zero loss. Consequently
\[
\inf_{Q_qh=u}\|h-Eh\|_2^2=0.
\tag{FE10}
\]
The unit edge on completely forgotten directions is exact, but those directions have zero output tangent. It is not a spectral gap on local physical excitations.

The [[jordan-covariance-and-the-entropy-weighted-ball|retained Jordan-covariance response]] instead differentiates functions across the ball. It is determined by the specified spherical geometry and generator, not by infimizing (FE9) over lifts.

## Why deleting zero singular values is not the same repair

The invertible equal-rank volume cost in
[[moving-response-balance-and-a-ruble-operator-signature|moving response balance, MR12a–MR12b]]
diverges at a singular same-rank arrow. Entropy deficit is a different, state-indexed construction, not its finite continuation obtained by deleting zeros.

A finite matrix witness makes the distinction precise. Let \(P\) project onto \(e_1\in\mathbb R^2\), and \(Q\) onto
\(v=(\cos\theta,\sin\theta)\), \(0<\theta<\pi/2\). Then
\[
\operatorname{pdet}(P^*P)
=\operatorname{pdet}(Q^*Q)=1,\qquad
\boxed{\operatorname{pdet}((QP)^*(QP))=\cos^2\theta.}
\tag{FE11}
\]
Here \(\operatorname{pdet}\) means the product of nonzero eigenvalues of the displayed positive Gram matrix. Thus the proposed scalar
\(-\log\operatorname{pdet}(F^*F)\) assigns zero to each projection but a positive value to their composite: it is not additive. The only nonzero singular value of \(QP\) is \(\cos\theta\), whereas its only nonzero eigenvalue is \(\cos^2\theta\). Squaring the eigenvalue pseudodeterminant of \(QP\) would therefore give \(\cos^4\theta\), not the Gram value in (FE11).

Finite entropy loss therefore supplies a genuine rank-changing readout member, but neither a universal cost per arrow nor a clock for every quotient. No Dirac-delta outcome is covered by the bounded-density hypothesis, and no obtained outcome or Born rule has been derived. The remaining physical construction must relate a specified readout law, its state-dependent loss and its retained carrier to an actual arena and dynamics, rather than identifying a finite entropy deficit with mass by its name.

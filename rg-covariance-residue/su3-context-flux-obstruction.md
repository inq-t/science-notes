# SU(3) Context Response Can Exceed Every Bounded Flux

An actual Wilson exterior variation changes the relative weights of two central conditional wells through an exponentially depleted separator. Every state-preserving single-link transport then has exponentially growing norm, including transports with arbitrary law-preserving circulation. The leading Fisher response belongs to the well label itself. This identifies information that a coarse description must retain or control jointly; it does not prove that the full Wilson law or the physical theory is gapless.

## A source variation made from actual links

Use the \(SU(3)\) metric \(g(X,X)=-\operatorname{ReTr}(X^2)/3\), product metrics on exterior links, and the four-dimensional Wilson convention
\[
dq_{\beta,\alpha}(U)\propto
\exp\!\left[\frac{\beta}{3}\operatorname{ReTr}(U^*S_\alpha)\right]dU.
\tag{SF1}
\]
Put \(D_\alpha=\operatorname{diag}(e^{i\alpha},e^{i\alpha},e^{-2i\alpha})\). Use two copies of each of its three cyclic diagonal permutations as the six complementary staples. Their sum obeys
\[
S_\alpha=2(2e^{i\alpha}+e^{-2i\alpha})I,\qquad
S_\pi=-2I,\qquad S'_\pi=-8iI.
\tag{SF2}
\]
These are compatible exterior links: set transverse links to identity and use the six distinct outer edges parallel to the active link to realize the six oriented path products. Work in an embedded Wilson star, for example a periodic lattice of side at least seven, so no short identification merges the edges or the reference path below.

Each outer path generator is a cyclic permutation of \(i\operatorname{diag}(1,1,-2)\), of squared norm two. The actual exterior curve \(R_\alpha\) therefore has
\[
|\dot R_\pi|^2=12.
\tag{SF3}
\]
The variation is not just an endpoint gauge change: the invariant source determinant has
\(\partial_\alpha\arg\det S_\alpha|_\pi
=\operatorname{ImTr}(S_\pi^{-1}S'_\pi)=12\).

At \(\alpha=\pi\), (SF1) is exactly the law in [[frustrated-su3-conditional-wells|the conditional-well theorem]], with \(\kappa=2\beta/3\). Inversion symmetry makes the normalizing score vanish, leaving
\[
\boxed{
q_{\beta,\pi}=q_\kappa,\qquad
s_\alpha(U):=\partial_\alpha\log q_{\beta,\alpha}(U)|_\pi
=-\frac{8\beta}{3}\operatorname{ImTr}U.}
\tag{SF4}
\]
The all-central staple realization of that earlier note has no such first-order determinant-phase variation along its individual central links. The noncentral realization (SF2) is essential; an arbitrary derivative of a scalar source would not establish an actual exterior obstruction.

## A gauge-invariant test with no omitted frame derivative

Write the active edge as \(x\to x+\mu\). Choose a transverse direction \(\nu\) and the five-link reference path
\[
x\to x+\nu\to x+2\nu\to x+2\nu+\mu
\to x+\nu+\mu\to x+\mu.
\tag{SF5}
\]
It avoids the active edge and all six varied outer parallel edges. Its product \(W_{\rm ref}(R_\alpha)\) stays equal to identity. Let
\[
f(U,R)=h\!\left(\operatorname{ImTr}(U W_{\rm ref}(R)^*)\right),
\tag{SF6}
\]
where \(h\) is smooth, odd, nondecreasing, and equals \(\pm1\) outside a small interval about zero. The relative loop transforms by conjugation, so the probe is gauge invariant. Along the displayed exterior curve its explicit context derivative is zero. Differentiating its conditional mean therefore introduces no missing moving-frame term.

Set \(w=\operatorname{ImTr}U\). The wells have \(w=\pm3\sqrt3/2\), equal asymptotic weights, and \(f=\pm1\). Consequently
\[
\frac{q_\kappa(s_\alpha f)}{\beta}\longrightarrow-4\sqrt3.
\tag{SF7}
\]
For any fixed \(0<\eta<1/2\), choose the transition band using the exact barrier lemma in [[frustrated-su3-conditional-wells|the well theorem]]. Boundedness of \(df\), the barrier on its support and the partition-function lower bound give
\[
q_\kappa(|df|)\le C_\eta\kappa^4e^{-\eta\kappa}.
\tag{SF8}
\]
This is the \(L^1\) gradient bound relevant to flux, distinct from the \(L^2\) bound used for a conditional spectral test.

## The obstruction applies to every connection

Any essentially bounded velocity with
\(\operatorname{div}(q_\kappa v_\alpha)=-q_\kappa s_\alpha\)
obeys the weak identity
\[
|q_\kappa(s_\alpha f)|
=|q_\kappa[df(v_\alpha)]|
\le \|v_\alpha\|_\infty\,q_\kappa(|df|).
\tag{SF9}
\]
Combining (SF7)--(SF8) proves, for all sufficiently large \(\beta\),
\[
\boxed{
\|v_\alpha\|_\infty
\ge c_\eta\beta\,\kappa^{-4}e^{\eta\kappa},
\qquad \kappa=2\beta/3.}
\tag{SF10}
\]
For a connection operator measured per unit exterior tangent, divide this bound by \(\sqrt{12}\). Divergence-free corrections change neither the numerator nor the weak identity. Thus this is not a defect of least-\(L^2\) transport; [[conditional-fisher-coercivity/bounded-transport-and-cut-flux|the exact cut-flux duality]] makes the obstruction intrinsic to this conditional law and source direction.

For each finite \(\beta\), the fixed-probe ratio in (SF9) is continuous near the displayed exterior, and the six-link tangent extends smoothly. The finite Wilson exterior marginal has full support. Positive-measure neighborhoods therefore inherit a comparable lower bound. Their measure may shrink with \(\beta\); no probability estimate is claimed. Both pointwise and essentially uniform one-link transport bounds fail through unbounded coupling.

## What must be retained

There is an exact response decomposition before any attempt to solve transport within the wells. At the displayed reference frame retain
\[
L=\operatorname{sign}\operatorname{ImTr}(U W_{\rm ref}^*),
\qquad \pi_\ell(\alpha)=q_{\beta,\alpha}(L=\ell).
\]
The zero set has Haar measure zero because \(\operatorname{ImTr}\) is a nonzero real-analytic function on connected \(SU(3)\). Along the exterior path the partition is fixed. Disintegration gives, with both derivatives evaluated at \(\alpha=\pi\),
\[
s_\alpha
=\partial_\alpha\log\pi_L
+\partial_\alpha\log q_{\beta,\alpha}(U\mid L),
\qquad
q_\ell\!\left(\partial_\alpha\log q_\ell\right)=0.
\tag{SF11}
\]
The two score terms are orthogonal in \(L^2(q)\), hence
\[
\mathcal I_{\rm full}
=\mathcal I_L+\sum_\ell\pi_\ell\mathcal I_{\mathrm{within},\ell}.
\tag{SF12}
\]
At \(\alpha=\pi\), symmetry gives \(\pi_+=1/2\), while concentration at the wells yields
\[
\frac{\pi'_+}{\beta}\to-2\sqrt3,\qquad
\frac{\mathcal I_L}{\beta^2}\to48,\qquad
\frac{\mathcal I_{\rm full}}{\beta^2}\to48.
\tag{SF13}
\]
Thus the label carries the entire leading-order response, and the within-label Fisher remainder is \(o(\beta^2)\). None of this proves a uniform within-label transport or gap. A hard partition has a boundary, and the retained label's transitions and their energy cost must be represented rather than discarded.

[[trace-dirichlet-descent/well-core-capacity-and-source-response|The well-core construction]] now makes this domain requirement exact. A nontrivial hard finite label is not in the smooth diffusion's \(H^1\) domain. Harmonic interpolation supplies a conductance form and its inherited Gram metric; the binary source-to-rate quotient is fixed by capacity in either the exact or diagonal metric. Its conditional rate remains exponentially small, and its source pairing also forces an exponentially growing minimum \(L^2\) transport cost.

Alternatively enlarge the active carrier to include surrounding links. At either central active well the full action has a nonzero \(\alpha\)-derivative: the active plaquettes contribute \(\pm4\sqrt3\beta\), while the other affected plaquettes have zero derivative at \(\pi\). Thus each frozen well has an actual joint downhill direction. This exterior lies outside the two simpler joint-escape cuts, but the adaptive [[wilson-exterior-force-localization|force--curvature certificate]] already controls it: (EF15) gives \(\chi_\beta=16\beta\). [[coherent-staple-localization|The common-link support bound]] strengthens that estimate and separately constructs a smaller block for a context the adaptive certificate misses. These localization results do not yet control the residual block form by the required global comparison.

The distinction matches [[algebra/local-global-individuation|local--global individuation]] in a precise limited sense: suppressing a label from the retained presentation does not remove its response from the whole law. No ontological outcome selection follows from the disintegration identity.

## Scope of the failed route

The carrier here is one Wilson link conditioned on its complete exterior. It is not the normalized soft posterior of [[nonlinear-gauge-fiber-transport|gauge-fiber transport]], nor an arbitrary larger block. Failure of this uniform certificate does not rule out state-weighted localization, a label-enriched interface, joint block escape, or the physical mass gap. A source-dependent transport quotient is not yet the positive-energy spectrum of a reconstructed four-dimensional theory.

The [[receipts/su3_context_flux_receipt.py|finite receipt]] checks the realizable source path, its metric normalization, the reference-path incidences, the trace barrier and finite Weyl-integral response ratios. The exponential obstruction is proved by (SF7)--(SF10); numerical samples do not establish its asymptotic or a continuum theorem.

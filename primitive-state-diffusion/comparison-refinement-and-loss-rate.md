# Comparison Refinement and Loss Rate

Repeated tensor-overlap comparisons converge on the complete primitive-state function carrier to a self-adjoint diffusion generator, with a positive gap uniform in comparison resolution. The exact harmonic multipliers control both the infinite spectral tail and the limiting squared-norm loss form. This is a state-space clock for a declared comparison law; its refinement parameter has no supplied conversion to physical time.

Use the orbits \(X\), invariant measures \(\mu\), parameters \(a,b,\rho=a+b\), operators \(B_k\), and complete harmonic spaces \(\mathcal V_\ell\) from [[primitive-state-diffusion/overlap-kernels-and-harmonics|overlap kernels and harmonics]]. In particular, (OR7) there gives every multiplier \(\lambda_{k,\ell}\), including the zero tail.

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
applies to these geometrically constructed comparisons. On the same function carrier set
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

## The comparison law and its clock remain choices

For example, \(R=(I+H_\infty)^{-1}=\int_0^\infty e^{-t}e^{-tH_\infty}dt\) is also a symmetric Markov comparison with the same invariant measure. Its jump generator
\(I-R=H_\infty/(I+H_\infty)\) has the same vacuum and symmetries but nonproportional spectral rates. The tensor-overlap refinement assumption excludes this alternative; symmetry and positivity alone do not.

An overall clock scale remains. If the speed in (OR8) is replaced by \(c_k>0\), a finite nonzero limiting first eigenvalue requires \(c_k/k\to c>0\); the limiting operator is then \(cH_\infty\). Comparison geometry provides the relative scale in (OR11), not an identification of its parameter with physical proper time.

The generator's [[primitive-state-diffusion/trace-metric-and-ball-return|trace-metric identification and ball return]] determine its geometric normalization. They also separate this compact-state-space result from the construction of physical observables and spacetime dynamics.

## Finite arithmetic checks

[[directed-analytic-realization/sphere_ball_descent_receipt.py|The shared receipt]] independently integrates shifted Jacobi polynomials against beta moments, checks both parameter rows, and tabulates refinement alongside its ball tests. [[directed-analytic-realization/sphere-ball-descent-receipt-output.txt|Its saved output]] reports finite arithmetic evidence. The complete harmonic decomposition in [[primitive-state-diffusion/overlap-kernels-and-harmonics|overlap kernels and harmonics]] and the tail arguments above establish the infinite-dimensional convergence.

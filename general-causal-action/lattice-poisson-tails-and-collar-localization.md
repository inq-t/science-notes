# Lattice Poisson Tails Localize the Collar Memory

The Poisson evolution on an open planar face grid has a spatial tail bound uniform in the box and source position. Subordination and the second moment of the killed lattice walk suffice: outside a collar of width \(w\), its squared \(\ell^2\) tail is at most \(C\min(1,t^2/w^2)\). Together with a diagonal decay estimate and the exact local innovation denominator, this controls the collar-memory coefficient by \(C/w^2\), uniformly over all scaled times. No assumed Gaussian heat-kernel estimate or exponential locality enters the proof.

**Status: proved lattice bounds for the inherited harmonic law.** [[inherited-planar-vacuum-and-the-regional-time-law|IR]] fixes the covariance and chronological conventions. [[gaussian-collar-memory-and-the-complete-radial-source|The Gaussian collar calculation]] identifies the conditional-response coefficient controlled here. The estimates concern the actual Dirichlet face matrix, with boundary killing retained.

## The killed walk and its Poisson evolution

Let \(\Lambda\subset\mathbb Z^2\) be a finite face box, let \(p\in\Lambda\), and put
\[
A_\Lambda=4I-\operatorname{Adj}_\Lambda,\qquad
C_\Lambda=\sqrt{A_\Lambda},\qquad
a_t^\Lambda(x)=(e^{-tC_\Lambda})_{xp}.
\tag{LP1}
\]
The diagonal of \(A_\Lambda\) remains four at boundary sites. Consequently \(e^{-sA_\Lambda}\) is the continuous-time nearest-neighbor walk, with rate one in each of four directions, killed when it leaves \(\Lambda\).

For a direct verification, expand
\[
e^{-sA_\Lambda}
=e^{-4s}\sum_{j=0}^\infty\frac{s^j}{j!}
\operatorname{Adj}_\Lambda^j.
\]
Its matrix entries count precisely the paths that stay in the box. In particular, if \(Z_s\) is the unrestricted walk started at zero and \(p_s(x)=\mathbb P(Z_s=x)\), then
\[
0\le(e^{-sA_\Lambda})_{xp}\le p_s(x-p),\qquad
\sum_{x\in\Lambda}(e^{-sA_\Lambda})_{xp}\le1.
\tag{LP2}
\]

For \(t>0\), define the probability density
\[
\nu_t(ds)=\frac{t}{2\sqrt\pi}s^{-3/2}
\exp\!\left(-\frac{t^2}{4s}\right)ds.
\]
The exact scalar identity and its operator consequence are
\[
e^{-t\sqrt\lambda}=\int_0^\infty e^{-s\lambda}\nu_t(ds),
\qquad
e^{-tC_\Lambda}=\int_0^\infty e^{-sA_\Lambda}\nu_t(ds).
\tag{LP3}
\]
To verify the identity without importing a kernel theorem, substitute \(u=t/(2\sqrt s)\). The remaining integral is
\((2/\sqrt\pi)\int_0^\infty e^{-u^2-b^2/u^2}du\), where \(b=t\sqrt\lambda/2\). If this last unnormalized integral is \(I(b)\), differentiation followed by \(u=b/v\) gives \(I'(b)=-2I(b)\), while \(I(0)=\sqrt\pi/2\). This proves (LP3), including normalization at \(\lambda=0\). Functional calculus then gives the positive operator integral. In particular \(a_t^\Lambda\ge0\) and its total mass is at most one.

## A second moment gives a uniform spatial tail

Let \(w\ge1\), and let
\[
\mathcal T_w=\{x\in\Lambda:|x-p|_\infty\ge w\}.
\]
The unrestricted walk makes a Poisson number of jumps of mean \(4s\). Its increments have mean zero and squared Euclidean length one, so
\[
\mathbb E|Z_s|_2^2=4s,\qquad
\mathbb P(|Z_s|_\infty\ge w)\le\min\{1,4s/w^2\}.
\tag{LP4}
\]
The killed-walk comparison and subordination therefore give
\[
\begin{aligned}
\sum_{x\in\mathcal T_w}a_t^\Lambda(x)
&\le\int_0^\infty\min\{1,4s/w^2\}\nu_t(ds)\\
&\le\frac{t}{2\sqrt\pi}
\left[
\frac4{w^2}\int_0^{w^2/4}s^{-1/2}ds
+\int_{w^2/4}^\infty s^{-3/2}ds
\right]
=\frac{4t}{\sqrt\pi\,w}.
\end{aligned}
\tag{LP5}
\]
Both displayed integrals contribute \(4/w\) before multiplication by \(t/(2\sqrt\pi)\). Since the kernel is nonnegative and subprobability, this proves
\[
\boxed{
\sum_{x\in\mathcal T_w}|a_t^\Lambda(x)|^2
\le
\left[\sum_{x\in\mathcal T_w}a_t^\Lambda(x)\right]^2
\le \min\left\{1,\frac{16t^2}{\pi w^2}\right\}.}
\tag{LP6}
\]
The same estimate holds for the complement of any retained region containing \(\{|x-p|_\infty<w\}\cap\Lambda\). The constants do not require that the collar fit entirely inside the box. Graph-distance collars obey the same bound after a fixed numerical change of width.

## The local covariance decays uniformly in the containing box

Subordination also compares the killed Poisson diagonal with the unrestricted one. Fourier transformation of the unrestricted adjacency operator gives
\[
a_t^\Lambda(p)\le
\int_{[-\pi,\pi]^2}e^{-t\omega(k)}
\frac{d^2k}{(2\pi)^2},\qquad
\omega(k)=\sqrt{4-2\cos k_1-2\cos k_2}.
\]
On this square, \(\sin(|k_i|/2)\ge |k_i|/\pi\), hence
\(\omega(k)\ge2|k|_2/\pi\). Extending the resulting radial integral to \(\mathbb R^2\) gives \(C/t^2\). Combining it with the subprobability bound yields
\[
\boxed{a_t^\Lambda(p)\le\frac{C}{(1+t)^2}.}
\tag{LP7}
\]
Only the explicit Fourier multiplier and an elementary radial integral were used.

Set
\[
c_\Lambda=(C_\Lambda)_{pp},\qquad
s_\Lambda(t)=
\langle e_p,C_\Lambda e^{-2tC_\Lambda}e_p\rangle
=\langle a_t^\Lambda,C_\Lambda a_t^\Lambda\rangle.
\tag{LP8}
\]
Since \(0<A_\Lambda<8I\) and \((A_\Lambda)_{pp}=4\),
\[
\sqrt2\le c_\Lambda\le2.
\]
The lower bound follows from \(\sqrt{A_\Lambda}\ge A_\Lambda/\sqrt8\); the upper follows from Cauchy–Schwarz. For \(t\ge1\), the scalar inequality
\(\omega e^{-2t\omega}\le (et)^{-1}e^{-t\omega}\), followed by (LP7), gives the required extra inverse power of time. For \(t\le1\), use \(s_\Lambda(t)\le c_\Lambda\). Thus
\[
\boxed{0\le s_\Lambda(t)\le\frac{C}{(1+t)^3}.}
\tag{LP9}
\]
This argument does not differentiate a pointwise comparison between killed and unrestricted kernels.

## The innovation denominator has a uniform lower bound

For \(0\le\omega\le M=\sqrt8\), concavity gives
\[
1-e^{-2t\omega}\ge
\frac{\omega}{M}(1-e^{-2tM}).
\]
The spectral measure of \(e_p\) therefore satisfies
\[
c_\Lambda-s_\Lambda(t)
\ge\frac4{\sqrt8}(1-e^{-2\sqrt8t})
=\sqrt2(1-e^{-2\sqrt8t}).
\]
As \(c_\Lambda+s_\Lambda(t)\ge\sqrt2\), one obtains
\[
\boxed{
c_\Lambda^2-s_\Lambda(t)^2
\ge2(1-e^{-2\sqrt8t})
\ge d_*\min(t,1),\qquad
d_*=2(1-e^{-2\sqrt8})>0.}
\tag{LP10}
\]
Dividing by \(c_\Lambda^2\le4\) gives the analogous lower bound for
\(1-[s_\Lambda(t)/c_\Lambda]^2\). The small-time denominator is retained; replacing it by a constant near \(t=0\) would be incorrect.

Combining (LP6), (LP9) and (LP10) proves
\[
\boxed{
\sup_{\substack{t>0,\ \Lambda,\ p\in\Lambda}}
\frac{2\sqrt8\,s_\Lambda(t)}
     {c_\Lambda^2-s_\Lambda(t)^2}
\sum_{x\in\mathcal T_w}|a_t^\Lambda(x)|^2
\le\frac{C}{w^2},\qquad w\ge1.}
\tag{LP11}
\]
For \(0<t\le1\), the ratio is at most \(Ct/w^2\). For \(t\ge1\), it is at most
\(Ct^2/[w^2(1+t)^3]\). These two bounds prove the uniform statement, including times much larger than the collar width.

The Gaussian conditional covariance obeys
\(s_\Lambda(t)-q_{\Lambda,w}(t)\le
\|C_\Lambda\|\|a^\Lambda_{t,\mathrm{out}}\|_2^2\).
Consequently (LP11) is the analytic coefficient bound needed by [[gaussian-collar-memory-and-the-complete-radial-source|the complete radial-source collar theorem]]. That theorem owns the source-algebra and innovation interpretation; no single-source covariance is substituted for it here.

This estimate is sufficient rather than a sharp pointwise Poisson-kernel asymptotic. It proves polynomial collar control in the inherited harmonic law. Transferring it to the actual compact conditional law, allowing a growing regional source inventory, or holding physical rather than scaled duration fixed requires the corresponding additional estimates.

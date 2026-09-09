# Gaussian Collar Memory on the Complete One-Face Radial Algebra

The exterior memory of a retained Gaussian collar is an exact covariance projection deficit. On the complete centered one-face radial source algebra, its ratio to the original full-predictor innovation is largest for the quadratic source. Higher radial chaoses cannot produce a worse ratio. Thus a spatial bound for that quadratic controls every square-integrable radial observable of the same face in the harmonic law, while leaving arbitrary multi-face sources and the actual compact complete-source problem separate.

**Status: exact harmonic conditional formulas and a sharp complete radial-source comparison.** [[inherited-planar-vacuum-and-the-regional-time-law|IR]] fixes the inherited Gaussian chronology. [[two-slice-innovation-geometry/regional-innovation-and-exterior-information-balance|RI]] fixes the full innovation and its exterior-information term. The common-root framed coordinates are retained before simultaneous color invariants; no independent regional vacuum or facewise Gauss quotient is introduced.

## The collar returns the covariance projection

On a finite planar patch put \(C=\sqrt A\), where \(A=4I-\operatorname{Adj}\), and choose a face \(p\) and a collar \(S\) containing it. At time zero, each of the three colors of \(X\) is Gaussian with covariance \(C\). For \(t>0\), define
\[
c=C_{pp},\qquad a=e^{-tC}e_p,\qquad
s=a^{\mathsf T}Ca=(Ce^{-2tC})_{pp},\qquad
v=(Ca)_S,\qquad q=v^{\mathsf T}C_{SS}^{-1}v.
\tag{GC1}
\]
The notation \(s\) here is a variance, not a second time. The full predictor of the later face vector has mean
\(m=a^{\mathsf T}X\) and independent conditional noise of covariance \((c-s)I_3\). Conditional on the collar, its mean becomes
\[
m_S=v^{\mathsf T}C_{SS}^{-1}X_S,
\qquad \operatorname{Cov}(m_S)=qI_3,
\qquad \operatorname{Cov}(m\mid X_S)=(s-q)I_3.
\tag{GC2}
\]
These follow directly from Gaussian regression. In particular \(0<q\le s<c\). Positivity of \(q\) follows already by retaining \(p\), since \((Ce^{-tC})_{pp}>0\).

For the prescribed normalized neutral quadratic
\[
f(X)=\frac{|X_p|^2-3c}{\sqrt6c},
\]
the whole and collar predictors are
\[
P_tf=\frac{|m|^2-3s}{\sqrt6c},\qquad
\mathsf E_SP_tf=\frac{|m_S|^2-3q}{\sqrt6c}.
\]
Therefore
\[
\boxed{
M_S(t;f):=\|(I-\mathsf E_S)P_tf\|^2
=\frac{s^2-q^2}{c^2},\qquad
\|\delta_tf\|^2=1-\frac{s^2}{c^2}.}
\tag{GC3}
\]
The denominator is the innovation using the full-system predictor. Replacing it by the collar-predictor error would change the comparison.

The missing linear variance is exactly a best approximation in the inherited covariance metric:
\[
\boxed{
\varepsilon_S:=s-q
=\min_{\operatorname{supp}b\subset S}(a-b)^{\mathsf T}C(a-b)
\le\|C\|\,\|a_{S^c}\|_2^2
\le\sqrt8\,\|a_{S^c}\|_2^2.}
\tag{GC4}
\]
Complete the square in the collar coefficients to obtain the minimizer
\(b_S=C_{SS}^{-1}v\). Choosing instead \(b=a1_S\) proves the upper bound. No inverse of the full covariance is needed. Nested collars increase \(q\) and decrease \(\varepsilon_S\), with RI's orthogonal information balance retained.

## Every radial chaos has an exact forecast

The full one-face physical radial space is
\(L^2(\mathbb R^3,N(0,cI_3))^{SO(3)}\). With
\(z=|X_p|^2/(2c)\), its radial probability is Gamma with shape \(3/2\). A normalized orthogonal basis is
\[
f_k^{(c)}(X_p)
=(-1)^k\sqrt{\frac{k!}{(3/2)_k}}
 L_k^{1/2}\!\left(\frac{|X_p|^2}{2c}\right),
\qquad k=0,1,2,\ldots .
\tag{GC5}
\]
Here \((3/2)_k\) is the rising factorial. The first two elements are the constant and the source in (GC3). Laguerre orthogonality follows by integration by parts against the Gamma density; completeness follows from polynomial density, or uniqueness of its analytic Laplace transform. These are radial Hermite chaoses of total degree \(2k\).

The generating function
\[
\sum_{k\ge0}L_k^{1/2}(z)u^k
=(1-u)^{-3/2}\exp[-zu/(1-u)]
\]
and the elementary Gaussian quadratic integral give
\[
\boxed{
P_tf_k^{(c)}=(s/c)^k f_k^{(s)}(m),\qquad
\mathsf E_SP_tf_k^{(c)}=(q/c)^k f_k^{(q)}(m_S).}
\tag{GC6}
\]
For example conditioning a Gaussian of covariance \((c-s)I_3\) changes the generating-function parameter from \(u\) to \((s/c)u\). Comparing coefficients proves the first formula, and a second regression with variance \(s-q\) proves the other.

The whole forecasts are orthogonal for distinct \(k\), as are their collar projections. The discarded forecasts are also orthogonal: conditional expectation is an orthogonal projection, so their Gram matrix is the difference of those two diagonal Gram matrices. Consequently, for arbitrary centered radial sources
\(F=\sum_{k\ge1}\gamma_kf_k^{(c)}\),
\(G=\sum_{k\ge1}\delta_kf_k^{(c)}\),
\[
\boxed{
\begin{aligned}
\langle(I-\mathsf E_S)P_tF,(I-\mathsf E_S)P_tG\rangle
&=\sum_{k\ge1}\overline{\gamma_k}\delta_k
 \bigl[(s/c)^{2k}-(q/c)^{2k}\bigr],\\
\langle\delta_tF,\delta_tG\rangle
&=\sum_{k\ge1}\overline{\gamma_k}\delta_k
 \bigl[1-(s/c)^{2k}\bigr].
\end{aligned}}
\tag{GC7}
\]
The identities extend from polynomials by contraction and Parseval; no boundedness assumption on the individual radial source is required.

## The quadratic is the worst normalized radial source

For \(0\le b\le a<1\) and \(k\ge1\),
\[
\frac{a^k-b^k}{1-a^k}
\le\frac{a-b}{1-a},
\tag{GC8}
\]
because the ratio of the two geometric sums is
\(\sum_{j=0}^{k-1}a^{k-1-j}b^j/\sum_{j=0}^{k-1}a^j\le1\).
Apply this with \(a=(s/c)^2\), \(b=(q/c)^2\). Equation (GC7) then proves the sharp complete-source identity
\[
\boxed{
\sup_{\substack{F\ne0\\F\ \text{centered radial}}}
\frac{\|(I-\mathsf E_S)P_tF\|^2}{\|\delta_tF\|^2}
=\frac{s^2-q^2}{c^2-s^2}
\le\frac{2s\sqrt8}{c^2-s^2}\,\|a_{S^c}\|_2^2.}
\tag{GC9}
\]
The source \(f_1^{(c)}\) attains the supremum. If \(q<s\), higher chaoses have strictly smaller ratios; when \(q=s\), every exterior term is zero. Thus the optimum concerns the entire centered radial \(L^2\) space, not a fixed finite-degree truncation. It is a collar-recovery estimate, not the full OI lower bound.

The same conditioning retains mixed quadratic sources at different profiles. For nonzero real profiles \(b_i\), put
\(c_i=b_i^{\mathsf T}Cb_i\), \(a_i=e^{-tC}b_i\),
\(s_{ij}=a_i^{\mathsf T}Ca_j\), and
\(q_{ij}=(Ca_i)_S^{\mathsf T}C_{SS}^{-1}(Ca_j)_S\).
For their normalized centered quadratics \(f_i\), Wick contraction gives
\[
\boxed{\langle(I-\mathsf E_S)P_tf_i,(I-\mathsf E_S)P_tf_j\rangle
=\frac{s_{ij}^2-q_{ij}^2}{c_ic_j}.}
\tag{GC10}
\]
This is a positive Gram matrix, but its off-diagonal entries need not be positive. Separate diagonal bounds do not discard these mixed source terms or extend (GC9) to arbitrary multi-face observables.

## Complete local OI coercivity still does not give a global gap

There is a second sharp use of (GC8). Put
\(r(t)=[(Ce^{-tC})_{pp}/c]^2\), \(a=r(2t)\), and \(b=r(4t)\).
The one-face Gaussian conditional kernel acts on \(f_k^{(c)}\) by
\(r(t)^k\). Thus the unchanged full OI quotient on that source is
\[
\mathfrak q_t(f_k^{(c)})
=\frac{1-2a^k+b^k}{1-a^k}
=1-\frac{a^k-b^k}{1-a^k}.
\]
Since \(0\le b\le a<1\), equation (GC8) shows that its minimum occurs at \(k=1\). For an arbitrary radial superposition, numerator and denominator are diagonal in the same basis, so the quotient is an average with nonnegative innovation weights. Therefore
\[
\boxed{
\inf_{\substack{F\ne0\\F\ \text{centered radial}}}
\frac{\langle F,(I-P_{2t})^2F\rangle}
     {\langle F,(I-P_{2t})F\rangle}
=\frac{1-2a+b}{1-a}
=1-a+\frac{b-a^2}{1-a}.}
\tag{GC11}
\]
The quadratic again attains the extremum, this time an infimum.

Cauchy–Schwarz for the positive frequency measure gives \(b\ge a^2\). The uniform point-source denominator estimate in [[lattice-poisson-tails-and-collar-localization|LP10]] consequently yields
\[
\boxed{\inf_F\mathfrak q_t(F)
\ge1-a\ge\frac12(1-e^{-2\sqrt8t})>0,\qquad t>0.}
\tag{GC12}
\]
At every fixed \(t\ge t_0>0\), this controls the **complete** centered one-face radial algebra uniformly in patch size. Nevertheless the full harmonic physical gap is \(2\sqrt{\lambda_{\min}(A_L)}\to0\). Complete local scalar coercivity, even together with collar recovery, therefore does not imply global coercivity: the soft sources extend across the growing patch. No full compact radial-algebra return is used in this discriminator.

## Scope of collar enlargement

The formulas also hold for the bulk Gaussian field on \(\mathbb Z^2\) with bounded covariance \(C=\sqrt{4I-\operatorname{Adj}}\), defined through its finite-dimensional Gaussian laws. The vector \(a\) lies in \(\ell^2\), so \(a^{\mathsf T}X\) exists as a Gaussian \(L^2\) limit; every finite principal covariance \(C_{SS}\) is positive definite. There is no infinite-dimensional Lebesgue density or inverse of \(C\) in this assertion. Exhausting collars have \(\|a_{S^c}\|_2\to0\), so (GC9) recovers all radial sources uniformly at each fixed scaled \(t>0\). A quantitative width/time estimate is a separate spatial-kernel calculation.

For the actual compact theory, [[vacuum-hellinger-return-and-regional-conditional-projections|VH]] returns the prescribed quadratic and its conditional action. It does not uniformly return arbitrarily high Laguerre degree. The complete radial supremum in (GC9) is therefore an exact harmonic theorem; extending it to all compact radial observables requires an additional estimate. All sources retain the same based connectors and chronological time unit throughout.

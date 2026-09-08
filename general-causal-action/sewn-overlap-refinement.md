# Refining Sewn Comparisons Returns a Collective Laplacian

The anchored \(SU(2)\) comparison has an exactly ordered spectrum across every representation. Processing at its comparison scale returns the full compact-group Laplacian on the collective readout branch, with a positive gap uniform in refinement and convergence controlling the entire spectral tail. At the same pace, normalized relative modes acquire divergent rates. Thus a uniform sequence of gaps can coexist with failure to retain the full joint dynamics.

**Status: exact for the specified comparison family and its declared conditional-update clock.** This is refinement on a compact group, not a spatial continuum or infinite-volume Yang–Mills theorem. [[sewn-overlap-and-conditional-clock|The sewn-overlap construction]] owns the state, processing axiom, fixed-input selection test and gauge-action distinctions.

## Every multiplier is an exact character coefficient

Take \(G=SU(2)\), \(Q=-2\operatorname{Tr}\), \(D_Q=-\Delta_Q\), and \(a=\chi_1/2\). The character \(\chi_n=U_n(a)\) has dimension \(n+1\) and Casimir \(c_n=n(n+2)/4\). Normalizing the \(k\)-th anchored overlap gives

\[
p_k(a)=\frac{(2+a)^k}{Z_k},\qquad
Z_k=\int(2+a)^k\,d\mu_H(a),\qquad
d\mu_H=\frac2\pi\sqrt{1-a^2}\,da.
\tag{SR1}
\]

Let \(B_k=C_{p_k}\), \(q_k=p_k*p_k\), and \(C_k=B_k^2\). The normalized convolution multiplier on every matrix entry of representation \(n\) is

\[
b_{k,n}=\frac1{n+1}\int p_k\chi_n\,d\mu_H.
\]

Equivalently, expand \((4+\chi_1)^k=\sum_n c_{k,n}\chi_n\). Character fusion gives

\[
c_{0,0}=1,\qquad
c_{k+1,n}=4c_{k,n}+c_{k,n-1}+c_{k,n+1},\qquad
b_{k,n}=\frac{c_{k,n}}{(n+1)c_{k,0}},
\tag{SR2}
\]

with all out-of-range coefficients zero. This specifies the infinite representation tail too: \(b_{k,n}=0\) for \(n>k\).

The [[library/nist-dlmf-classical-rodrigues-formulas/inq|classical Rodrigues normalization]], followed by \(n\) integrations by parts, gives for \(n\le k\)

\[
b_{k,n}=
\frac{k!}{(k-n)!\,2^n(3/2)_n}
\frac{\int_{-1}^1(2+a)^{k-n}(1-a^2)^{n+1/2}\,da}
{\int_{-1}^1(2+a)^k(1-a^2)^{1/2}\,da}.
\tag{SR3}
\]

Endpoint terms vanish because the differentiated weight retains a positive endpoint power at each required integration. For \(n>k\), the differentiated degree-\(k\) polynomial vanishes.

## Ordering supplies a bound on every spectral tail

Let \(\nu_{k,n}\) have density proportional to the numerator integrand in (SR3). A further integration by parts proves

\[
\frac{b_{k,n+1}}{b_{k,n}}=\mathbb E_{\nu_{k,n}}a,
\qquad n<k.
\tag{SR4}
\]

Indeed, integrating the derivative of
\((2+a)^{k-n}(1-a^2)^{n+3/2}\) relates the two numerator integrals with the coefficient \((k-n)/(2n+3)\) appearing in their ratio. Its mean is strictly positive because an even positive weight is tilted by the increasing function \((2+a)^{k-n}\); it is strictly below one by full interval support. Therefore

\[
1=b_{k,0}>b_{k,1}>\cdots>b_{k,k}>0,
\qquad b_{k,n}=0\quad(n>k).
\tag{SR5}
\]

The same derivative identity and \((1+a)/(2+a)\le2/3\) give

\[
(2n+3)\mathbb E a
=(k-n)\mathbb E\frac{1-a^2}{2+a}
\le\frac{2(k-n)}3(1-\mathbb E a).
\]

Consequently

\[
\frac{b_{k,n+1}}{b_{k,n}}
\le\frac{2(k-n)}{2k+4n+9},
\qquad b_{k,1}\le\frac{2k}{2k+9}.
\tag{SR6}
\]

These are analytic inequalities for arbitrary \(k,n\), not extrapolations of finite coefficient tables.

## The collective branch has an unbounded limit

On the fixed carrier \(L^2(G,dg)\), put

\[
A_k=k(I-C_k).
\tag{SR7}
\]

The [[holonomy-state-refinement/overlap-kernels-and-face-refinement#The local Hessian fixes the convolution limit|local overlap expansion]] supplies the scale. In a \(Q\)-orthonormal Lie coordinate \(X\),
\(-\log[(4+\chi_1(\exp X))/6]=|X|^2/24+O(|X|^4)\).
Laplace localization therefore gives covariance \(12I/k\). Equivalently, for \(y=1-a\), \(ky/3\) tends to a gamma law of shape \(3/2\), with convergence of its polynomial moments. Expanding the normalized character gives

\[
\frac{\chi_n(1-y)}{n+1}
=1-\frac{n(n+2)}3y+O_n(y^2),
\quad
b_{k,n}=1-\frac{3n(n+2)}{2k}+O_n(k^{-2}).
\tag{SR8}
\]

The compact complement of any identity neighborhood has exponentially small mass; the nondegenerate local Gaussian expansion controls the stated moments and remainder. Thus

\[
k(1-b_{k,n}^2)\longrightarrow3n(n+2)=12c_n.
\tag{SR9}
\]

Define \(A=12D_Q\) by the full Peter–Weyl decomposition. Its operator domain consists of vectors \(f=\sum_n f_n\) with \(\sum_n[3n(n+2)]^2\|f_n\|^2<\infty\); replacing the squared weights by first powers gives the form domain. Finite representation sums are cores.

There is complete spectral convergence:

\[
\|(z+A_k)^{-1}-(z+A)^{-1}\|\longrightarrow0\quad(z>0),
\qquad
\|e^{-tA_k}-e^{-tA}\|\longrightarrow0\quad(t>0).
\tag{SR10}
\]

To prove it, split at a fixed degree \(M\). The finite head converges by (SR9). Ordering bounds both tails by the degree-\(M+1\) resolvent denominators or heat exponents. First let \(k\to\infty\), then \(M\to\infty\). The heat conclusion is uniform for \(t\ge\tau>0\), but not down to zero. This is the same complete-tail method as [[primitive-state-diffusion/comparison-refinement-and-loss-rate|primitive comparison diffusion]], applied to the newly computed multipliers.

Ordering and (SR6) also give the uniform edge

\[
\boxed{
\operatorname{gap}A_k=k(1-b_{k,1}^2)
\ge\frac{9k(4k+9)}{(2k+9)^2}
\ge\frac{117}{121}\quad(k\ge1),
\qquad\operatorname{gap}A=9.
}
\tag{SR11}
\]

The rational lower expression increases with \(k\). Both the bound and its limit refer to the declared comparison clock, with no conversion to physical mass or time.

## The two branches cannot share one finite limiting pace

On \(\mathcal H_k=L^2(q_k(xy^{-1})dxdy)\), let \(J_x,J_y\) be the readout isometries. The exactly normalized maps are

\[
J_k^+=(J_x+J_y)[2(I+C_k)]^{-1/2},
\qquad
J_k^-=(J_x-J_y)[2(I-C_k)]^{-1/2}.
\tag{SR12}
\]

The first acts on all \(L^2(G)\), including constants; the second acts on its centered subspace. They are isometries with orthogonal ranges. Their remaining orthogonal complement is \(\ker P_x\cap\ker P_y\). The scaled full clock \(kL_k\) is exactly

\[
A_k\quad\text{on }\operatorname{Ran}J_k^+,
\qquad k(I+C_k)\quad\text{on }\operatorname{Ran}J_k^-,
\qquad 2kI\quad\text{on the remainder}.
\tag{SR13}
\]

Thus the uniform edge (SR11) holds on the full finite-\(k\) carrier too. It also survives restriction to simultaneous conjugation invariants, because the first character sum is invariant. Yet every normalized relative branch has rate at least \(k\), so it disappears from the positive-time heat limit at that pace.

This is not fixed by a different common scalar speed \(s_k\). A finite positive limit for even one fixed collective mode requires \(s_k/k\to s>0\), by (SR8). Its paired relative rate \(s_k(1+b_{k,n}^2)\) then diverges. Keeping that relative rate bounded forces \(s_k=O(1)\), making every fixed collective rate vanish.

[[resolved-relative-boundary-and-two-clock-limits|Resolving the relative boundary]] constructs an exact common carrier and proves both clock limits. It shows that relative information can survive in a Gaussian coordinate while still being expelled dynamically by the collective clock. This is a concrete obstruction for the specified resampling law, not a prohibition on every joint realization or on a nonclassical change of variables.

## Exact arithmetic and finite diagnostics

[[receipts/sewn_overlap_refinement_receipt.py|The refinement receipt]] computes integer character coefficients through \(k=1024\), checks them independently by Haar moments at small exponents, and tests the complete finite ordering and paired-rate identities. Its convergence tables are diagnostics; (SR3)–(SR10) prove the all-degree statements.

For the first character at \(k=1024\), the scaled collective rate is approximately \(8.95186749\), approaching \(9\), while its normalized relative partner has rate \(2039.04813251\). A good collective rate and a positive full finite-system edge therefore do not establish preservation of the entire limiting field carrier.

# Cofinal Determinant and Wilson Source Equivalence

The determinant-to-Wilson comparison extends to growing four-dimensional boxes and varying coupling by choosing the auxiliary copy count to dominate an explicit volume factor. It also controls any specified countable family of renormalized source products, provided their finite-regulator moments are bounded. This gives a rigorous identification bridge for a separately constructed limit; it does not construct the continuum theory or its gap, and the copy count remains an unselected microscopic choice.

**Status: exact finite-volume estimates and a conditional limit-identification lemma.** [[general-causal-action/cycle-determinants-and-the-pure-gauge-return|The cycle determinant theorem]] supplies the fixed-graph calculation. The extension here keeps its volume dependence explicit.

## Geometry and normalization

Let \(\Gamma\) be a finite nearest-neighbor box in four dimensions, with open, periodic or mixed boundary conditions. Every periodic extent must be at least six. Let \(M\) be its number of vertices, \(G\) a compact group, and \(\rho:G\to U(d_\rho)\) a fixed finite-dimensional unitary representation. Assign every existing oriented edge weight \(1/8\), including at an open boundary.

For inverse transports on reversed edges, set
\[
(P_Uf)_x=\frac18\sum_{y\sim x}\rho(U_{xy})f_y,\qquad
Q_U=I-rP_U,\qquad 0<r<1.
\]
Then \(P_U=P_U^*\), \(\|P_U\|\le1\), and \(Q_U\ge(1-r)I>0\). The degree bound is eight; replacing the boundary weight by inverse vertex degree would change the calculation.

For an integer number \(\nu\ge1\) of complex Gaussian copies, define
\[
S_{\nu,r}(U)=\nu\log\frac{\det Q_U}{\det Q_{\mathbf1}},
\qquad
V_W(U)=\sum_p[d_\rho-\operatorname{Re}\chi_\rho(U_p)],
\qquad
b=\frac{2\nu r^4}{8^4}.
\tag{CW1}
\]
The sum is over elementary plaquettes, counted once without orientation.

## The complete action has a uniform remainder

The exact decomposition is
\[
\boxed{
S_{\nu,r}=bV_W+R_{\nu,r},\qquad
0\le R_{\nu,r}\le\epsilon_{\nu,r}
=\frac{\nu Md_\rho r^6}{3(1-r)}
=\frac{Md_\rho8^4br^2}{6(1-r)}.}
\tag{CW2}
\]

**Proof.** Absolute convergence of the matrix logarithm gives
\[
S_{\nu,r}
=\nu\sum_{k\ge1}\frac{r^k}{k}
\left(\operatorname{Tr}P_{\mathbf1}^k-\operatorname{Tr}P_U^k\right).
\]
Pairing rooted closed walks with their reversals expresses every trace difference as
\[
8^{-k}\sum_{|\gamma|=k}
[d_\rho-\operatorname{Re}\chi_\rho(U_\gamma)]\ge0.
\]
For the stated geometry, orders one, two, three and five contribute zero. The nontrivial length-four walks are the eight rooted orientations of each elementary plaquette, giving its coefficient in (CW1). Each remaining trace difference is at most \(2Md_\rho\). The estimate
\(\sum_{k\ge6}r^k/k\le r^6/[6(1-r)]\) proves (CW2). \(\square\)

Open boxes are bipartite, as are boxes with all periodic extents even. There the odd orders vanish throughout, and \(1-r\) can be replaced by \(1-r^2\). Periodic extent five introduces an order-five winding term; extent four introduces extra leading order-four terms. They are outside the theorem as stated.

Normalize both laws against the same product Haar measure. Then
\[
\frac{d\mu_{\nu,r}}{d\mu_{W,b}}
=\frac{e^{-R_{\nu,r}}}{\mu_{W,b}(e^{-R_{\nu,r}})},
\qquad
e^{-\epsilon_{\nu,r}}
\le\frac{d\mu_{\nu,r}}{d\mu_{W,b}}
\le e^{\epsilon_{\nu,r}}.
\]
Every complex integrable frame observable therefore satisfies
\[
\boxed{
|\mu_{\nu,r}(F)-\mu_{W,b}(F)|
\le(e^{\epsilon_{\nu,r}}-1)\mu_{W,b}|F|.}
\tag{CW3}
\]
This compares the full probability laws, including their normalizers, rather than only the first curvature coefficient.

## Choosing a cofinal family

Let \(\Gamma_n\) be admissible boxes with \(M_n\) vertices, and prescribe \(b_n>0\). The lattice spacing and physical extent, when present, are additional specified data. Choose integers \(\nu_n\) and put
\[
r_n=\left(\frac{8^4b_n}{2\nu_n}\right)^{1/4}.
\]
If \(r_n\to0\) and
\[
M_nb_nr_n^2\longrightarrow0,
\tag{CW4}
\]
then \(\epsilon_n\to0\). Thus the determinant law approaches the matching Wilson law even while volume and coupling vary. This is a selected diagonal sequence, not a bound uniform in volume at a fixed number of copies.

Renormalized observables can grow with the regulator, so \(\epsilon_n\to0\) alone need not control them. Equation (CW3) specifies the extra condition: its error factor times the relevant absolute moment must tend to zero.

Here is an explicit countable-source version. Suppose frame observables \(F_{n,j}\), \(j\ge1\), and their renormalization maps have been specified, with finite Wilson absolute moments. Choose \(\eta_n\downarrow0\), and finite bounds
\[
L_n\ge\max\left\{1,\max_{j\le n}\mu_{W,b_n}|F_{n,j}|\right\}.
\]
Put
\[
\begin{aligned}
t_n&=\log(1+\eta_n/L_n),&
\alpha_n&=\frac{8^4b_n}{2},&
k_n&=\frac{M_nd_\rho8^4b_n}{6},\\
q_n&=\min\left\{\frac12,\frac1n,
\sqrt{\frac{t_n}{2k_n}}\right\},&
\nu_n&=\max\{1,\lceil\alpha_n/q_n^4\rceil\},&
r_n&=(\alpha_n/\nu_n)^{1/4}.
\end{aligned}
\tag{CW5}
\]
The matching \(b_n\) is exact, \(r_n\le q_n\to0\), and
\(\epsilon_n=k_nr_n^2/(1-r_n)\le2k_nr_n^2\le t_n\). Hence
\[
\max_{j\le n}
|\mu_{\nu_n,r_n}(F_{n,j})-\mu_{W,b_n}(F_{n,j})|
\le\eta_n.
\tag{CW6}
\]
Known sup-norm estimates can provide the \(L_n\) for bounded finite-regulator sources. The list may include products, reflected products and translated insertions. Each fixed enumerated source is controlled eventually. Extending this to distributions on all test functions requires suitable continuity or uniform distributional bounds; an arbitrary countable list is not automatically complete.

## What the bridge does not transport automatically

Reflection positivity is a property of sewing, not a consequence of a positive density or (CW3). For integer copies, [[general-causal-action/reflection-sewing-and-the-auxiliary-boundary-carrier|the auxiliary reflection-sewing theorem]] supplies a positive cross-plane kernel on its reflection-compatible slabs. A periodic temporal direction needs an even extent and both reflection cuts. Boundary factors and source maps must respect that construction.

Likewise, comparison of frame expectations does not itself identify changing auxiliary Hilbert spaces or their transfer spectra. [[general-causal-action/cycle-moments-and-the-pure-gauge-vacuum-return|The separate cycle-moment theorem]] proves convergence of the ordered positive eigenvalues and fixed bounded vacuum source histories at fixed graph and coupling, without identifying the changing Hilbert spaces. Uniform operator identification through growing graphs is a further question.

There is another important distinction for the mass-gap programme. The estimate in (CW3) is controlled by an ordinary probability \(L^1\) norm. An Osterwalder–Schrader norm can be much smaller because its reflected pairing has null directions. A small full-law density error therefore does not, without a relative estimate, carry a uniform inequality on the whole reflected source unit ball.

There is still a useful route: prove a uniform reflected inequality on the source family before the limit, and independently use (CW6) to identify the limits of each of its pairings. [[positive-semigroup-decay/source-pairing-limit-and-the-mass-gap|The source-pairing limit theorem]] then passes the inequality directly. It does not require a finite-regulator operator comparison between the determinant and Wilson carriers.

If either side has a separately established source-complete limit and the errors vanish for all required evaluations, (CW3)–(CW6) identify the corresponding limits. The result supplies no tightness, local regularity, nontriviality, Yang–Mills short-distance theorem or positive gap by itself. Its contribution to [[scale-bearing-descent/pointed-comparison-and-the-yang-mills-return|the backwards programme]] is a concrete complete-law return map whose remaining volume and source costs are explicit.

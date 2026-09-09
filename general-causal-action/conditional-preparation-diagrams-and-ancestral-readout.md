# Conditional Preparation Diagrams and Ancestral Readout

A directed acyclic preparation diagram can add a comparison with several retained parents while preserving the complete marked transfer of every ancestral subdiagram. Its conditional normalizers must travel with the diagram. The general-group return has finite clocks determined by each node's ancestors and unaffected by its descendants. The same theorem exposes two limitations: forgetting an ancestor generally changes the retained experiment, and correlations between preparations do not themselves generate mixed spatial derivatives in independently compared word coordinates.

## A conditional diagram on actual independently variable words

Fix a compact connected group \(G\) with simple Lie algebra of dimension \(d\), a faithful unitary representation \(\rho:G\to U(n)\), and the unnormalized Hilbert–Schmidt convention of [[general-group-preparation-and-the-casimir-return|the general-group preparation theorem]]. Let \(E=\mathbb C^{n\times k}\), \(m=nk\), and \(Q(X,Y)=-\operatorname{Re}\operatorname{Tr}[d\rho(X)d\rho(Y)]\).

Choose a finite directed acyclic graph \(D\) of preparation nodes. For each node \(i\), let \(\operatorname{pa}(i)\) be its parents, choose scalar coefficients \(a_{ij}\in\mathbb C\) and \(\tau_i>0\), and set
\[
\xi_i=\mu_i(\xi_{\operatorname{pa}(i)})+\varepsilon_i,
\qquad \mu_i=\sum_{j\in\operatorname{pa}(i)}a_{ij}\xi_j,
\qquad \varepsilon_i\sim\operatorname{CN}(0,\tau_i^2I_E).
\tag{PD1}
\]
All innovations are independent. A root has \(\mu_i=0\). In any topological ordering, the strictly triangular coefficient matrix \(A=(a_{ij})\) gives the faithful joint covariance
\[
\Gamma_D=(I-A)^{-1}\operatorname{diag}(\tau_i^2)(I-A)^{-\dagger}\otimes I_E,
\qquad \det\Gamma_D=\prod_i\tau_i^{2m}.
\tag{PD2}
\]
The triangular innovation change has determinant one. Thus the complete prior factors as \(P_D(d\xi)=\prod_iP_i(d\xi_i\mid\xi_{\operatorname{pa}(i)})\), independently of the chosen topological evaluation order. Changing the arrows or refactoring the law around a different retained parent is a different question, addressed by [[access-ports-and-conditional-sewing|the conditional-sewing obstruction, AP18–19]].

Assign each node an actual multiplication word \(g_i\) on a declared spatial diagram. For the theorem below, these words must jointly parametrize the retained carrier as \(G^{|D|}\), with product Haar. This may be the complete quotient by specified internal vertex gauges; all remaining vertex actions are retained. Every preparation and its input word occupy one common terminal port, or all words are based loops at one common port. Scalar coefficients in (PD1) are then compatible with the common left action \(\xi_i\mapsto\rho(h)\xi_i\). Correlations across independently gauged ports require transported maps and are outside this fixed-covariance theorem.

These conditions concern actual word maps and measures, not the names of coordinates. The common-endpoint family in [[conditional-access-families-and-the-returned-clock|conditional access]] is one example. Three simultaneously based loop coordinates are another admissible comparison inventory when they give the complete Haar quotient. An overcomplete collection containing algebraically dependent words is not a product-Haar inventory and cannot use the integration theorem below without a new proof.

## Normalize each new comparison over its actual parents

Choose comparison paces \(r_i>0\), and define
\[
q_{i,\alpha}(g_i,g_i';\xi_i)
=\exp\!\left[-\frac\alpha{r_i}
\|[\rho(g_i)-\rho(g_i')]\xi_i\|^2\right],
\qquad
\zeta_{i,\alpha}(\xi_i)=\int_Gq_{i,\alpha}(e,h;\xi_i)dh,
\]
\[
b_{i,\alpha}(\xi_{\operatorname{pa}(i)})
=\mathbb E[\zeta_{i,\alpha}(\xi_i)\mid\xi_{\operatorname{pa}(i)}]>0.
\tag{PD3}
\]
For a root, \(b_{i,\alpha}\) is a scalar. Each fixed-preparation comparison is left invariant, so its row integral is independent of \(g_i\). The complete marked operator kernel is
\[
\boxed{
F_{D,\alpha}^{M}(g,g')
=\mathbb E_{P_D}\!\left[
M(\xi)\prod_{i\in D}
\frac{q_{i,\alpha}(g_i,g_i';\xi_i)}
{b_{i,\alpha}(\xi_{\operatorname{pa}(i)})}\right].}
\tag{PD4}
\]
The source-free denominators stay fixed when differentiating marks. Bounded marks are admissible; arbitrary joint Gaussian linear and quadratic insertions are also admitted when their total precision is positive. Their finite-width integrals include every denominator in (PD4), and generally are not one quadratic determinant. Sources on transported preparation readouts pull back through their actual maps as in [[marked-gaussian-constraints-and-sewing-measures|marked Gaussian sewing]].

A set \(J\subset D\) is ancestral if it contains every parent, hence every ancestor, of each of its nodes. If \(M\) depends only on the preparations in \(J\), then
\[
\boxed{
\int_{G^{D\setminus J}}F_{D,\alpha}^{M}(g,g')
\prod_{i\notin J}dg_i'
=F_{J,\alpha}^{M}(g_J,g_J').}
\tag{PD5}
\]
The right side uses the inherited joint law, word coordinates, paces and normalizers, with no resetting. Marks may also depend on the retained incoming and outgoing word coordinates; the same proof then applies pointwise in those coordinates. A source involving a forgotten readout is not a retained mark. To prove the identity, choose a leaf outside \(J\). Integrating its outgoing word gives \(\zeta_i\); integrating its preparation conditionally gives \(b_i\), cancelling its denominator exactly. No remaining factor depends on that leaf preparation. Remove leaves in reverse topological order. Ancestrality guarantees that this eliminates all and only the forgotten nodes. Every allowed removal order gives the same full amplitude, including its scalar factors.

For \(J=\varnothing\) and no marks, (PD5) gives exact unit row sum. Symmetry is inherited from every distance comparison. Conditioning on the whole faithful preparation gives a Gaussian distance kernel on the product embedding \(g\mapsto(r_i^{-1/2}\rho(g_i)\xi_i)_i\), with positive configuration-independent weight \(\prod b_i^{-1}\). For \(k\ge n\), almost surely all \(\xi_i\) have full row rank; faithfulness makes this embedding injective. The Gaussian Fourier argument therefore proves Hilbert positivity and injectivity on the complete product carrier. Hence \(F_{D,\alpha}\) is a positive self-adjoint Markov contraction, commuting with the stated common endpoint gauge actions.

Equation (PD5) is an exact operator intertwining for retained functions and through arbitrary temporal products with retained marks. It permits a new child with several existing parents, for example \(\xi_2=a_{20}\xi_0+a_{21}\xi_1+\varepsilon_2\) over two roots. It does not permit changing the conditional law of an existing node while claiming the old subdiagram is unchanged.

## A nonancestral readout retains hidden normalization data

For the two-node diagram \(x\to y\), integrating only the old outgoing word leaves
\[
F_{y\leftarrow D}^{M}(B,B')
=\frac1{z_\alpha}\mathbb E\!\left[
M(y)q_{\alpha,y}(B,B')\frac{\zeta_\alpha(x)}{b_\alpha(x)}\right],
\qquad z_\alpha=\mathbb E\zeta_\alpha(x).
\tag{PD6}
\]
This is an exact retained kernel, but it need not equal a freshly normalized one-word kernel for the marginal Gaussian of \(y\). The forgotten ancestor's comparison has left a weight.

There is a strict finite-width example. Use the exchangeable \(SU(2)\) pair of (AP18), with covariance \(\sigma^2\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)\otimes I_E\), \(0<\rho<1\), and equal paces. Put \(\zeta(x)=\zeta_\alpha(\|x\|^2)\), and let \(K\) be the conditional Gaussian operator \((Kf)(y)=\mathbb E[f(x)\mid y]\), on the common marginal Gaussian space. Exchangeability gives \(b=K\zeta\). Complete old mark recovery for \(y\) in (PD6) would require
\[
K\!\left(\frac\zeta{K\zeta}\right)=1.
\tag{PD7}
\]
The Gaussian conditional operator is the Mehler operator: on the complete real Hermite degree-\(j\) subspace it multiplies by \(\rho^j\). This follows by conditioning the Gaussian exponential generating function; the Hermite resolution is used in [[gaussian-overlap-balancing-and-clock-sewing|Gaussian clock sewing]]. Thus \(K\) is injective on \(L^2\), and its only fixed vectors are constants. The ratio \(\zeta/(K\zeta)\) belongs to \(L^2\): \(\zeta\le1\), and the conditional row lower bound in (NA11) bounds \((K\zeta)^{-1}\) by a polynomial in \(\|x\|\).

Equation (PD7) would therefore imply \(\zeta/(K\zeta)=1\), then \(K\zeta=\zeta\), then that \(\zeta\) is constant. But the \(SU(2)\) row integral is strictly decreasing in \(\|x\|^2\) for every \(\alpha>0\), a contradiction. Hence the forgotten ancestor changes the complete retained experiment. For a concrete bounded norm mark, write \(R=K[\zeta/(K\zeta)]-1\) and choose \(M(y)=\operatorname{sgn}R(y)\). At \(B=B'\), the difference from the isolated \(y\) kernel is \(z_\alpha^{-1}\mathbb E|R|>0\). The ordinary marginal Gaussian remains unchanged; its processed readout does not.

One may preserve the nonancestral readout by keeping the induced weight in (PD6), or try to represent that weight by additional retained preparation data. Refactoring the original Gaussian alone does not remove it. This is a directed conditional extension law, with a precisely delimited ancestral consistency theorem.

## Localization returns a recursively weighted conditional law

For each preparation define \(g_{\xi_i}\) and \(w_i=(\det_Qg_{\xi_i})^{-1/2}\) as in (GG4), and set
\[
h_i(\xi_{\operatorname{pa}(i)})
=\mathbb E[w_i\mid\xi_{\operatorname{pa}(i)}],\qquad
d\nu_D(\xi)=\prod_i
\frac{w_i}{h_i(\xi_{\operatorname{pa}(i)})}
P_i(d\xi_i\mid\xi_{\operatorname{pa}(i)}).
\tag{PD8}
\]
Each conditional factor integrates to one. The law \(\nu_D\) is therefore a faithful probability law with exactly the same directed factorization. Its ancestral marginals equal the corresponding \(\nu_J\); its nonancestral marginals need not have the original nodewise form.

An explicit sufficient inventory remains
\[
k>n+\frac d2.
\tag{PD9}
\]
The shifted-Gaussian theorem (CF6–8) supplies, uniformly in the conditional mean \(\mu_i\), the inverse-smallest-eigenvalue moments needed for \(w_i\) and \(w_i\operatorname{tr}_Qg_{\xi_i}^{-1}\). Its polynomially weighted versions and the conditional lower bounds give
\[
h_i\ge(\|\mu_i\|^2+m\tau_i^2)^{-d/2},\qquad
\alpha^{d/2}b_{i,\alpha}\ge
c_i(1+\|\mu_i\|^2+m\tau_i^2)^{-d/2}
\quad(\alpha\ge1).
\tag{PD10}
\]
The pace \(r_i\) changes only the fixed positive constant. Conditional positive moments under (PD8) are bounded by polynomials in the parent norms. Induction through a finite topological ordering proves every joint positive polynomial moment finite.

Here is a common domination for the finite-width return. Put \(\ell_i=\lambda_{\min}(\xi_i\xi_i^\dagger)\). After integrating all outgoing group coordinates, the exact preparation law is
\[
d\nu_{D,\alpha}
=\prod_i\frac{\zeta_{i,\alpha}}{b_{i,\alpha}}\,dP_D,
\qquad
\frac{d\nu_{D,\alpha}}{dP_D}
\le C_D\prod_i\ell_i^{-d/2}
\prod_i(1+\|\mu_i\|^2+m\tau_i^2)^{d/2}.
\tag{PD11}
\]
The first equality is a probability factorization by (PD3); the second uses (GG9) and (PD10). Since the finite joint Gaussian covariance (PD2) is positive, its density is bounded by a constant times that of independent isotropic matrices with one larger variance. This reduces integrability of the right side, with any fixed polynomial factor, to the separate inverse moments of (GG7–9). For a scaled second moment of group increment \(i\), retain its unnormalized moment integral before cancelling \(\zeta_i\); the same bound has only that node's power raised from \(d/2\) to \(d/2+1\). It remains integrable under (PD9).

At fixed full-rank preparations, Laplace localization gives the tangent covariance of each relative group increment. Given all preparations, these increments are independent and each has inversion symmetry. The coefficients of linear and mixed second derivatives therefore vanish. Conditional normalizer asymptotics cancel their separate \(r_i^{d/2}\) factors in the preparation law, yielding (PD8). Consequently
\[
\boxed{H_D=\sum_i\kappa_iD_{Q,g_i},\qquad
\kappa_i=\frac{r_i}{4d}\mathbb E_{\nu_D}\operatorname{tr}_Qg_{\xi_i}^{-1}
\in(0,\infty),}
\]
\[
\alpha(F_{D,\alpha}-I)f\longrightarrow-H_Df,
\qquad F_{D,N/t}^{\,N}\longrightarrow e^{-tH_D}
\quad\text{strongly}.
\tag{PD12}
\]
Simultaneous \(\rho(G)\) invariance makes each averaged inverse metric scalar. The first limit is uniform on smooth functions. The product limit holds on the complete product carrier and its common-gauge invariant subspace, uniformly on bounded nonnegative times, with the identity at zero.

The second-order Taylor remainder needs no additional fourth inverse moment. At fixed preparations, the scaled second-moment tail outside any fixed neighborhood tends to zero. A cross-tail factors into the scaled second moment of one increment and the tail probability of another. The single-raised-power domination following (PD11) then permits averaging. Finite Peter–Weyl sums give a dense invariant core, and contractivity extends the product limit to all vectors. The estimates are for a fixed finite diagram; their constants need not be uniform over growing depth, degree or decreasing innovation variance.

Because the marginal of \(\xi_i\) in (PD8) depends only on its ancestors, \(\kappa_i\) is unchanged when descendants are added. Unlike the sibling theorem, two nodes with different ancestral histories need not share the same coefficient even when their immediate innovation variances agree. The DAG selects a response history as well as a prior covariance.

## Spatial incidence is additional to the preparation arrows

The theorem allows a node to have several Gaussian parents, but its leading operator in the independently compared word coordinates is still the diagonal sum (PD12). Scalar correlations do not produce a mixed tangent covariance there. Any mixed physical derivatives arise from the actual nonlinear word map to the physical coordinates, or from a comparison with additional coupled rows. These must be computed separately.

In particular, assigning three common-base cell-loop coordinates to three preparation nodes is a valid instance of (PD4) on \(G^3\), followed by simultaneous Gauss averaging. [[three-cell-incidence-and-shared-path-motion|Three-cell incidence]] computes the actual shared-path and bridge derivatives; (PD12) does not prove equality with that inherited kinetic operator. Adding extra prefix or bridge words that are functions of those three coordinates can change the kinetic metric, but then their outgoing word integrals are not independent Haar variables. The leaf cancellation in (PD5) cannot be applied as if each extra readout were a new independent physical coordinate.

A finite interacting extension is nevertheless available on any declared word inventory satisfying the theorem. Choose actual closed cell words \(U_c(g)\), transport paths \(W_{ci}(g)\) to the preparation port, and nonnegative incidence strengths \(\beta_{ci}\). Insert weak endpoint factors built from
\[
\mathcal C(g,\xi)=\frac12\sum_{c,i}\beta_{ci}
\|[\rho(U_c(g))-I]\rho(W_{ci}(g))\xi_i\|^2.
\tag{PD13}
\]
Insert \(e^{-\mathcal C(g,\xi)/(2\alpha)}e^{-\mathcal C(g',\xi)/(2\alpha)}\) into (PD4), keeping its source-free denominators fixed. Positivity and domination remain valid. Polynomial moment bounds yield the returned potential
\[
V(g)=\sum_{c,i}\beta_{ci}\operatorname{Tr}
[\overline A_i(I-\operatorname{Re}\rho(U_c(g)))],\qquad
\overline A_i=\mathbb E_{\nu_D}(\xi_i\xi_i^\dagger).
\tag{PD14}
\]
The expected matrices commute with \(\rho(G)\), removing the transport paths only at this leading expected order. Each finite operator \(H_D+V\) has the inherited compact elliptic domains and a simple positive gauge-invariant ground vector. If a cost uses only an ancestral subdiagram's words and preparations, its marked readout still obeys (PD5); an interaction involving a forgotten node generally changes that readout. Gauge covariance of every actual transport row remains required, as in the local-incidence owner.

The directed preparation construction now goes beyond one retained parent without increasing the sufficient matrix rank. Its exact output is an ancestral marked law and an operator with controlled finite coefficients. The selection of arrows, compatibility between different parent choices, the spatial comparison matching actual cell incidence, and uniform interacting source control remain substantive construction tasks. [[prepared-readout-algebra-and-physical-source-completeness|Readout completeness]] transports the physical source test once the word inventory separates the carrier; [[conditional-vacuum-rigidity-and-the-physical-gap|vacuum susceptibility]] then tests the actual returned clock, rather than the Gaussian conditional graph by itself.

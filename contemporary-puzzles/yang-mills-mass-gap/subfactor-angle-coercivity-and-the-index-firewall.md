# Subfactor-Angle Coercivity and the Index Firewall

A finite common Jones index makes the relative algebra of two subfactor expectations finite-dimensional and therefore opens a positive Friedrichs gap after their common range is removed. It does not set the size of that gap: a fixed-index spin-model family has reduced edge \(1-|\cos\delta|\to0\). Index controls the size of an inclusion, whereas coercivity belongs to the relative position of two descents; a Yang--Mills use therefore needs a uniform mixed-projection relation, an exact identification of the common kernel, and a same-carrier comparison with physical energy.

**Status: [EXACT] for the two-projection kernel and reduced spectral edge; [ESTABLISHED MATHEMATICS] for the Sano--Watatani, Jones--Xu, and Bakshi--Guin results; [NO-GO] for any positive lower bound determined only by the displayed Jones indices or by the Q-system of one common inclusion; [OPEN] for a Yang--Mills construction and Poincare-energy solder.**

## The common range is a full-carrier kernel

Let \(M\) be a finite factor with normalized trace \(\tau\), let \(P,Q\subset M\) be finite-index subfactors, and work on

$$
\mathcal H=L^2(M,\tau).
$$

Write

$$
p=e_P,
\qquad
q=e_Q,
\qquad
r=e_{P\cap Q}=p\wedge q
$$

for the trace-preserving Jones projections. The even two-descent form from [[oriented-descent-angle-and-emergent-symmetry]] is

$$
G_{\angle}:=(1-p)+(1-q)=2I-p-q,
$$

with

$$
\langle\xi,G_{\angle}\xi\rangle
=\|(1-p)\xi\|^2+\|(1-q)\xi\|^2.
$$

Consequently,

$$
\boxed{\ker G_{\angle}=\operatorname{Ran}p\cap\operatorname{Ran}q
=\operatorname{Ran}r=L^2(P\cap Q,\tau).}
$$

In particular, the full carrier never has a strictly positive lower bound: the trace vector lies in this kernel, and for a genuine common subfactor the kernel is much larger than a vacuum line. Removing it is a mathematical reduction, not yet a proof that only physically null or vacuum directions were removed.

## The exact reduced gap

On \(\mathcal H_0=(1-r)\mathcal H\), put \(p_0=p-r\) and \(q_0=q-r\). The Friedrichs cosine is

$$
c_F(P,Q)
:=\|p_0q_0\|
=\|pq-r\|
=\sqrt{\|pqp-r\|}.
$$

[[library/angles-between-two-subfactors/inq|Sano and Watatani's angle operator]] is built from the positive compression \((pqp-r)^{1/2}\); its largest cosine is precisely \(c_F\). For a nonzero reduced pair, the two-projection norm identity gives

$$
\|p_0+q_0\|=1+c_F,
$$

and hence

$$
\boxed{
\gamma_{\angle}
:=\inf\operatorname{spec}\!\left(G_{\angle}\!\restriction_{\mathcal H_0}\right)
=1-c_F.}
$$

Thus \(c_F<1\) is exactly positive reduced coercivity, equivalently closedness of \(\operatorname{Ran}p_0+\operatorname{Ran}q_0\). In the degenerate case \(p_0=q_0=0\), the reduced operator is \(2I\); the displayed \(1-c_F\) formula concerns the nontrivial pair. This edge is dimensionless. It is neither a Hamiltonian gap nor a mass until an independent physical comparison and scale calibration are supplied.

## What finite common index actually proves

For a finite family of finite-index subalgebras \(P_i\subset M\), [[library/intersections-of-finite-families-of-finite-index-subfactors/inq|Jones and Xu, Theorem 3.1]] prove in the finite-factor setting that, for \(N=\bigcap_iP_i\),

$$
[M:N]<\infty
\quad\Longleftrightarrow\quad
\dim W^*(e_{P_1},\ldots,e_{P_n})<\infty.
$$

For two subfactors, finite common index therefore makes \(W^*(p,q)\) finite-dimensional. After the meet \(r\) is removed, \(1\) cannot remain as a non-intersection spectral value of \(pqp\); hence \(c_F<1\) and \(\gamma_{\angle}>0\). This is a qualitative existence theorem for each fixed pair. It gives no positive function of the three scalar indices that uniformly bounds \(1-c_F\).

Individual finite indices are weaker still: they do not by themselves force \([M:P\cap Q]<\infty\). For a factor with separable predual, the properly infinite/Type III extension in Jones--Xu Corollary 4.9 also requires one normal faithful state invariant under expectations onto every \(P_i\) and their intersection, together with the separate meet identity

$$
e_{\cap_iP_i}=e_{P_1}\wedge\cdots\wedge e_{P_n}.
$$

Finite index is therefore not a state-free license to import the tracial angle argument into a local Type III carrier.

## Fixed indices with a vanishing edge

[[library/relative-position-between-a-pair-of-spin-model-subfactors/inq|Bakshi and Guin]] give the decisive counterexample. For distinct \(2\times2\) complex Hadamard matrices

$$
u_\alpha=\frac1{\sqrt2}
\begin{pmatrix}1&1\\ e^{i\alpha}&-e^{i\alpha}\end{pmatrix},
\qquad
u_\beta=\frac1{\sqrt2}
\begin{pmatrix}1&1\\ e^{i\beta}&-e^{i\beta}\end{pmatrix},
$$

let \(R_\alpha,R_\beta\subset R\) be the associated spin-model subfactors of the hyperfinite \(II_1\) factor and set \(\delta=\alpha-\beta\ne0\). Their Theorems 1.4/6.12 and 6.23 give

$$
[R:R_\alpha]=[R:R_\beta]=2,
\qquad
[R:R_\alpha\cap R_\beta]=4,
$$

and

$$
\operatorname{Ang}_R(R_\alpha,R_\beta)
=\{\arccos|\cos\delta|\}.
$$

Therefore

$$
c_F(\delta)=|\cos\delta|,
\qquad
\boxed{\gamma_{\angle}(\delta)=1-|\cos\delta|\longrightarrow0}
$$

as \(\delta\to0\) through nonzero values, while all three indices remain \(2,2,4\). The common-index theorem is obeyed at every \(\delta\); what fails is uniform quantitative separation across the family.

Theorem 6.21 makes the firewall stronger. Up to isomorphism the ambient algebra, common inclusion, and one intermediate can be held fixed:

$$
\widetilde M=M_2(\mathbb C)\bar\otimes R,
\qquad
K=\left\{\begin{pmatrix}x&0\\0&\theta(x)\end{pmatrix}:x\in R\right\},
$$

$$
Q=\left\{\begin{pmatrix}x&y\\\theta(y)&\theta(x)\end{pmatrix}:x,y\in R\right\},
\qquad
P_\delta=\operatorname{Ad}\!\begin{pmatrix}1&0\\0&e^{i\delta}\end{pmatrix}(Q),
$$

where \(\theta\) is an outer involution. For the admissible nonzero parameters, \(K=P_\delta\cap Q\), while the relative angle varies with \(\delta\). The common inclusion \(K\subset\widetilde M\), and therefore the standard Q-system that reconstructs that single inclusion, is fixed; it is also reducible, with nontrivial relative commutant. A Q-system for one inclusion does not encode the relative placement of two intermediate subfactors.

## The relation that must be added

The missing datum is a relation on the **ordered pair**, not another scalar size invariant. At minimum, a family needs a physically derived constant \(\varepsilon>0\), uniform in volume and regulator at the declared physical separation, such that

$$
\boxed{
(p-r)(q-r)(p-r)
=pqp-r
\leq(1-\varepsilon)^2(p-r).}
$$

Equivalently, \(\|pq-r\|\leq1-\varepsilon\), so \(G_{\angle}\geq\varepsilon(1-r)\). Such a relation could be expressed by an ordered pair of marked biprojections or Q-systems together with their mixed composition, or by a dynamical rule restricting the relative unitary; it cannot be recovered from the index or from either inclusion separately.

For Yang--Mills, two further identifications remain load bearing. First, \(\operatorname{Ran}r\) must be proved to coincide with precisely the physical vacuum/null sector, or a justified physical quotient must remove it. Second, the mixed form must be transported to the reconstructed gauge-invariant carrier and compared there with the Poincare Casimir or transfer Hamiltonian, with an independent energy yardstick. [[past-future-angle-and-the-transfer-gap]] supplies an exact transfer realization of this comparison under Markov--Osterwalder--Schrader hypotheses; subfactor index alone supplies none of it.

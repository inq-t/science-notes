# Uniform Collar Capture Does Not Assemble a Global Gap

A growing collar recovers the omitted information of every square-integrable one-face radial source in the inherited harmonic law, uniformly in patch size and scaled time. Nevertheless that complete local source algebra has a positive innovation-response floor while the whole patch develops an arbitrarily soft physical mode. This decides the collar test: local completeness and quantitative information recovery are insufficient for global coercivity. The next comparison must retain the mixed relational sources that assemble a collective mode.

**Status: exact harmonic collar and local-coercivity theorems, with an actual compact return for the prescribed quadratic source.** [[gaussian-collar-memory-and-the-complete-radial-source|GC]] owns Gaussian conditioning and the complete radial algebra; [[lattice-poisson-tails-and-collar-localization|LP]] owns spatial localization; [[compact-collar-memory-and-the-returned-response|CL]] owns the compact conditional return. These use the single chronology and innovation balance of [[regional-innovation-and-exterior-information-balance|RI]].

## The collar captures the complete one-face source algebra

On the open face grid let \(P_t\) be the harmonic ground-transformed chronology, with per-color vacuum covariance \(C=\sqrt{4I-\operatorname{Adj}}\). Fix a face \(p\), and retain any set \(S_w\) containing the faces with \(|x-p|_\infty<w\), clipped at the patch boundary. For \(w\ge1\) and a centered radial \(F(X_p)\), put
\[
V_t(F)=\langle F,(I-P_{2t})F\rangle,\qquad
M_{S_w}(t;F)=\|(I-E_{S_w})P_tF\|^2.
\]
These are the original full-predictor innovation and the part of its forecast omitted by the collar. The source remains on the original face when the retained set grows.

GC9 and LP11 give a numerical constant \(C_*\), independent of \(p,L,t,w\), such that
\[
\boxed{
\sup_{\substack{t>0,\ L,\ p\\F\ne0,\ F\ \text{centered radial}}}
\frac{M_{S_w}(t;F)}{V_t(F)}
\le \min\{1,C_*/w^2\}.}
\tag{LC1}
\]
The quadratic \(F=(|X_p|^2-3C_{pp})/(\sqrt6C_{pp})\) attains the exact supremum over sources before the spatial estimate is applied. Higher radial Hermite chaoses have smaller normalized omission. Thus the source statement is complete in radial \(L^2\); it is not a bounded-degree approximation.

The proof requires only the killed-walk second moment, Poisson subordination and a uniform lower bound on the local innovation. It retains polynomial spatial tails, including long times and collars touching the outer boundary. In particular a fixed width \(w\ge\sqrt{C_*/\varepsilon}\) makes this omission fraction at most \(\varepsilon\), independently of volume.

The exterior term in the original OI numerator uses \(2t\), not \(t\). Spectral calculus gives \(V_{2t}(F)\le2V_t(F)\), so
\[
\boxed{
\frac{M_{S_w}(2t;F)}{V_t(F)}
\le\min\{1,2C_*/w^2\}.}
\tag{LC2}
\]
The bound by one follows directly from
\(M_{S_w}(2t;F)\le\|(I-P_{2t})F\|^2\le V_t(F)\).
RI's nested-reveal identity retains this positive term exactly; a small upper bound does not convert it into a new positive lower bound.

## The actual compact collar has a quantified return

Use the same compact family and physical Gauss law as [[uniform-nonlinear-planar-gap-and-marked-response|UN]]. Write
\[
n=L+1,\qquad 0<\epsilon=hn^{10}\le\eta,\qquad
\theta=hn^{11/2},
\]
and let \(f_h\) be CL's actual centered, normalized one-face source. For every fixed \(t_0>0\), CL6–13 and (LC1)–(LC2) prove, when \(\theta\) is sufficiently small,
\[
\boxed{
\sup_{t\ge t_0}
\max\left\{
\frac{M_{h,S_w}(t)}{G_h(t)},
\frac{M_{h,S_w}(2t)}{G_h(t)}
\right\}
\le \frac{2C_*}{w^2}+C_{t_0}\sqrt\theta.}
\tag{LC3}
\]
Here \(G_h(t)\) is the actual full innovation, and all constants are independent of the retained set and patch size. A collar may therefore grow along the controlled compact sequence. The result uses the actual vacuum and source normalization throughout.

The scope is narrower than (LC1): it returns the prescribed compact quadratic, not the complete compact radial unit sphere. The conditional-projection proof uses a source \(L^4\) bound. Its constant absolute error also gives no uniform relative return as \(t\downarrow0\); CL states the sufficient onset condition explicitly. At fixed physical duration the confinement window instead has a diverging physical gap, and CL15 supplies a separate vanishing-memory bound. These time comparisons are not interchangeable.

## A complete local floor can coexist with global softness

Let
\[
r_L(t)=\left[\frac{(Ce^{-tC})_{pp}}{C_{pp}}\right]^2,\qquad
a=r_L(2t),\quad b=r_L(4t).
\]
GC11–12 compute the unchanged OI quotient on the entire one-face radial space:
\[
\boxed{
\inf_F
\frac{\langle F,(I-P_{2t})^2F\rangle}
     {\langle F,(I-P_{2t})F\rangle}
=\frac{1-2a+b}{1-a}
\ge\frac12(1-e^{-2\sqrt8t})>0.}
\tag{LC4}
\]
The quadratic again attains the extremum. This is a uniform positive floor at every fixed positive scaled duration, despite including all radial chaoses.

By contrast the full harmonic physical carrier has gap
\[
\Delta_{0,L}=2\sqrt{\lambda_{\min}(A_L)}\longrightarrow0.
\]
Consequently its optimal OI floor is
\[
\boxed{
\inf_{\text{all centered physical }F}
\frac{\langle F,(I-P_{2t})^2F\rangle}
     {\langle F,(I-P_{2t})F\rangle}
=1-e^{-2t\Delta_{0,L}}\longrightarrow0.}
\tag{LC5}
\]
[[planar-patch-confinement-and-the-spatial-soft-mode|The known collective quadratic]] attains this edge. Written in face variables, it contains cross terms \(X_p\cdot X_q\), with the common based color frame retained. Its support grows with the patch.

Thus even the conjunction of complete local radial coercivity and uniform collar capture does not imply the full-carrier inequality. The counterexample concerns that inference at fixed scaled time. It does not disprove the active conjecture at a fixed physical slab or establish an obstruction for four-dimensional Yang–Mills.

## The next assembly test retains the mixed source matrix

The next comparison should use centered invariant quadratics
\[
F_B(X)=\sum_{\alpha=1}^3 X_\alpha^{\mathsf T}B X_\alpha
       -3\operatorname{Tr}(BC),\qquad B=B^{\mathsf T},
\]
with actual relative color transport. Diagonal \(B\) describes arbitrary sums of one-face quadratic sources; off-diagonal \(B\) retains their relational bilinears. [[additive-neutral-sources-and-the-pairing-range-test|The additive-source theorem]] now proves that every diagonal \(B\), with arbitrary growing support and signed coefficients, still has a uniform positive OI floor. The next test varies the spatial range of the off-diagonal pairings and determines whether each fixed range retains coercivity. Track the mixed innovation Gram form, not only the separate normalized diagonal responses.

This is a discriminating source-assembly test within oriented innovation transport. It can identify which growing relational directions escape the local floor and what a non-Abelian sewing estimate must constrain. The source exchange, vacuum caps and changed-history lag cost of [[spatial-block-sewing-and-the-vacuum-cap-response|SB]] remain part of that eventual estimate. The full continuum and cosmological targets in [[research-schema|the research schema]] are unchanged.

# Endpoint Averages and Quadratic Ultraviolet Control

Endpoint-transported volume averages induce the same map as ordinary volume averages on linear gauge classes, provided one compatible connector rule is used at every block. Coarse curvature is then an average of fine curvature, so its Maxwell form contracts. Exact Gaussian minimization consequently retains a lower bound by the coarse Maxwell form, and a finite-patch estimate gives an ultraviolet fluctuation floor uniform in volume and blocking depth. This is a linear gauge-field theorem, not nonlinear Yang--Mills coercivity or a quantum mass gap.

## The two averages differ by a gauge gradient

Take a periodic \(d\)-dimensional cubical lattice with spacing \(a\), partitioned into translated disjoint blocks \(B_y\) of \(n^d\) sites. Let \(b=na\). Assume enough blocks in each direction that the adjacent two-block patches below do not wrap onto themselves. Let \(A\) be a physical Lie-algebra-valued link potential, with a fixed inner product on its coefficients.

For each \(x\in B_y\), choose a connector \(\gamma_{y,x}\) inside that block, with \(\gamma_{y,y}\) empty. Use the **same rule independently of the outgoing direction** \(\mu\), translated between blocks. A fixed weighted family of connectors may replace each connector. The return path in the destination block reverses that block's rule.

Write \(A(\gamma)\) for the oriented unweighted fine-link sum, and define

$$
\tau_a A(y,x)=aA(\gamma_{y,x}),\qquad
S_y(A)=n^{-d}\sum_{x\in B_y}\tau_a A(y,x).
\tag{EA1}
$$

The normalized linearization of the endpoint-transported path mean is

$$
(M_nA)_\mu(y)=n^{-d-1}\sum_{x\in B_y}
\left[
A(\gamma_{y,x})+
\sum_{j=0}^{n-1}A_\mu(x+je_\mu)
-A(\gamma_{y+ne_\mu,x+ne_\mu})
\right].
\tag{EA2}
$$

The division by \(b\) converts a dimensionless infinitesimal transport into a coarse physical potential. Define the parallel-path volume average

$$
(Q_nA)_\mu(y)
=n^{-d-1}\sum_{x\in B_y}\sum_{j=0}^{n-1}A_\mu(x+je_\mu).
\tag{EA3}
$$

Summing the two connector terms gives the exact identity

$$
\boxed{M_nA=Q_nA-d_bS(A).}
\tag{EA4}
$$

Thus \([M_nA]=[Q_nA]\) on the coarse linear gauge quotient. If the connector rule depends on \(\mu\), the correction need not be a single gradient and this conclusion can fail.

This is the linear counterpart of [[regular-gauge-averages-and-the-selection-obstruction|the regular or anchored nonlinear group average]]. To reproduce a permutation-averaged axial connector, average complete paths over the basepoint and both independent connector permutations. [[library/covariant-axial-gauge/inq|Dimock's equations (25)--(27)]] provide the Abelian averaged-path precedent.

## Gauge fixing does not identify representative norms

For \(A\mapsto A-d_a\varphi\),

$$
M_n(A-d_a\varphi)
=M_nA-d_b(\varphi|_{\rm coarse\ vertices}).
\tag{EA5}
$$

The internal choice \(\varphi(x)=\tau_a A(y,x)\) has \(\varphi(y)=0\). It produces \(A^{\rm ax}\) satisfying \(\tau_a A^{\rm ax}=0\) and leaves \(M_nA\) unchanged. Hence \(M_nA=0\) implies \(Q_nA^{\rm ax}=0\).

If only \([M_nA]=0\), first remove the coarse gradient using a fine gauge function extending its coarse values, then apply this axial fixing.

The relevant norm is

$$
\|[A]\|_a=\inf_\varphi\|A-d_a\varphi\|_a,\qquad
\|A\|_a^2=a^d\sum_{x,\mu}|A_\mu(x)|^2.
\tag{EA6}
$$

An axial representative need not minimize this norm, but
\(\|A^{\rm ax}\|_a\ge\|[A]\|_a\), the direction needed below. A bound for every representative would be false: a nonzero gradient of a function vanishing at all coarse vertices has \(M_nA=0\) and zero curvature.

## A finite-patch ultraviolet estimate

Fix \(n\) and \(d\). On the rectangular cubical complex formed by two adjacent blocks, impose the axial constraints inside both blocks. In unit-spacing norms define

$$
c_{n,d}
=\min_{\substack{\tau A=0\\\|A\|_D=1}}
\left\{\|d_{\rm lat}A\|_D^2+
|(Q_nA)_\mu(y)|^2\right\}.
\tag{EA7}
$$

For connector rules related by coordinate permutations, this is one common constant. Otherwise take the minimum over the finitely many patch orientations.

Then \(c_{n,d}>0\). If the expression vanished, curl zero on the rectangular complex would imply \(A=d_{\rm lat}\psi\). The axial constraints force \(\psi\) to be constant on each block. The vanishing average across their common face makes those constants equal. Thus \(A=0\), contradicting unit norm. Compactness of the finite-dimensional constrained unit sphere gives a strictly positive minimum.

Sum (EA7) over adjacent block pairs. Every fine bond is covered, and every fine plaquette occurs at most \(2d\) times. Some plaquettes crossing four blocks are absent from these patches; omitting their nonnegative contribution only weakens the bound. With
$$
q_a(A)=a^d\sum_{x,\mu<\nu}|(d_aA)_{\mu\nu}(x)|^2,
$$
one obtains

$$
q_a(A)\ge
\frac{c_{n,d}}{2d\,a^2}\|[A]\|_a^2
=\frac{n^2c_{n,d}}{2d\,b^2}\|[A]\|_a^2,
\qquad [M_nA]=0.
\tag{EA8}
$$

This holds in four dimensions. It is uniform in total volume at **fixed blocking factor** \(n\), not a claimed bound on \(c_{n,d}\) as \(n\to\infty\). The constant is a finite-patch spectral minimum, not a measured mass. The [[thin-skeleton-and-block-average-coercivity|composite thin-skeleton obstruction]] concerns a different refinement assertion.

## From hard fibers to a full observation inequality

Before using only the zero-readout case, retain the observation term in (EA7). Choose the minimum-norm coarse representative \(B\) of \([M_nA]\), lift its gauge correction to fine vertices, and then impose internal axial fixing. The latter gauge function vanishes at coarse vertices, so the resulting \(A^{\rm ax}\) still has \(M_nA^{\rm ax}=Q_nA^{\rm ax}=B\). It is gauge equivalent to \(A\).

The same patch sum, now without setting \(B=0\), gives

$$
\boxed{
c_{n,d}\|[A]\|_a^2
\le 2d\,a^2q_a(A)
+n^{-d}\|[M_nA]\|_b^2.}
\tag{EA8a}
$$

The coefficient \(n^{-d}\) is \(a^d/b^d\); the observation is counted once per oriented coarse bond. No bound on the arbitrary fine gauge extension is needed, since the patch inequality controls its final axial representative. This estimate detects all gauge classes, including harmonic ones through the readout term.

For any \(\rho>0\), it implies the soft-observation inequality

$$
q_a(A)+\frac{\rho}{b^2}\|[M_nA]\|_b^2
\ge\frac{c_{n,d}}{b^2}
\min\!\left\{\frac{n^2}{2d},\rho n^d\right\}\|[A]\|_a^2.
\tag{EA8b}
$$

The volume average also contracts the physical \(L^2\) norm. Jensen's inequality in (EA3), followed by summing translated blocks for each longitudinal offset, gives \(\|Q_nA\|_b\le\|A\|_a\). Since
\(Q_nd_a=d_bQ_n^0\), where \(Q_n^0\) is the scalar cell average, it descends to a quotient contraction

$$
\|\mathsf Q_n[A]\|_b
=\|[Q_nA]\|_b
=\|[M_nA]\|_b
\le\|[A]\|_a.
\tag{EA8c}
$$

This is not representative-level contraction for \(M_n\), whose connectors can be large. [[soft-gaussian-gauge-blocking|Soft Gaussian blocking]] uses (EA8a) and (EA8c) to control actual reverse conditional laws, not only a hard fiber.

## Curvature contraction removes the blocking-depth loss

For forward exterior derivatives with their physical spacings, telescoping the coordinate differences in (EA3) yields

$$
\boxed{
(d_bQ_nA)_{\mu\nu}(y)
=n^{-d-2}
\sum_{x\in B_y}\sum_{j,k=0}^{n-1}
(d_aA)_{\mu\nu}(x+je_\mu+ke_\nu).}
\tag{EA9}
$$

This is an average of \(n^{d+2}\) curvature values. Jensen's inequality gives its squared-norm bound. Multiply by \(b^d=n^da^d\) and sum over coarse sites. For each fixed \(j,k\), the translated blocks partition the fine torus; the \(n^2\) shifts cancel the remaining \(n^{-2}\). Therefore

$$
\boxed{q_b(Q_nA)\le q_a(A).}
\tag{EA10}
$$

Because \(d_b^2=0\), (EA4) also gives
\(q_b(M_nA)=q_b(Q_nA)\).

Define the exact Gaussian variational pushforward on gauge classes by

$$
q_{{\rm eff},n}([B])
=\inf_{[M_nA]=[B]}q_a(A).
\tag{EA11}
$$

It follows without a perturbative expansion that

$$
\boxed{q_{{\rm eff},n}([B])\ge q_b(B).}
\tag{EA12}
$$

The map is onto. Given \(B\), set the internal links in every block to zero, and put \(nB_\mu(y)\) on every fine \(\mu\)-link crossing the interface from \(B_y\) to \(B_{y+ne_\mu}\). Each parallel path crosses exactly one such interface. Internal connectors vanish, and \(Q_nA=M_nA=B\).

On a torus, remove gauge volume and fix harmonic modes before interpreting (EA11) as a Gaussian probability density. If harmonic values are retained, the Gaussian statement is conditional in them; the free harmonic sector has no normalized noncompact Gaussian law. The variational inequality itself does not require a probability interpretation. With the zero modes handled, fiber integration returns a density proportional to \(\exp(-q_{{\rm eff},n}/2)\), with a field-independent determinant prefactor.

Aligned averages compose, \(Q_mQ_n=Q_{mn}\): fine and coarse basepoint sums combine into one larger block, and their path offsets combine into one longer path. Equation (EA4) and the cochain identity imply the same composition on gauge classes for the endpoint averages. Iterated Gaussian minimization therefore obeys

$$
q_{{\rm eff},k}\ge q_{b_k}.
\tag{EA13}
$$

Apply (EA8) to the **next fixed factor** \(L\), with \(b_{k+1}=Lb_k\):

$$
\boxed{
q_{{\rm eff},k}([B])
\ge
\frac{L^2c_{L,d}}{2d\,b_{k+1}^2}
\|[B]\|_{b_k}^2,
\qquad [M_LB]=0.}
\tag{EA14}
$$

The coefficient is independent of the fine cutoff, total volume, and number of already completed Gaussian blocking steps. Distinguishing the current mesh \(b_k\) from the next block width \(b_{k+1}\) prevents a spurious scale factor.

## The nonlinear problem has not been replaced by its tangent

The form \(q_{{\rm eff},k}\) acts on classical linear gauge-field variations. It is not the physical quantum Hamiltonian. The construction even starts from a massless Maxwell theory, whose infrared modes remain in the retained field. A uniform ultraviolet shell floor is therefore not evidence of a physical mass gap.

Nor does the quadratic tangent prove the corresponding estimate for the full compact Wilson measure. Noncommuting transports, generated interactions, large-field regions, the conditional metric, spatial response, and the renormalized-source envelope remain to be controlled.

The globally anchored common-pivot chart and this spatial averaging construction also have separate hypotheses. One must show that a chosen nonlinear block satisfies both if using that deterministic route. The probabilistic branch now has [[soft-gaussian-gauge-blocking|an exact soft Gaussian theorem]] and [[compact-gauge-kernel-tangent-response|a normalized near-identity match]] to the compact kernel. The first is uniform in depth; the second is only fixed-regulator and local in the input fields. Neither silently identifies the full nonlinear reverse law with the hard-constrained law in (EA11).

[[receipts/endpoint_average_receipt.py|The finite verification receipt]] checks endpoint identities, gauge covariance, curvature contraction and composition in dimensions two through four, small-patch floors, and finite Gaussian quotient comparisons. Its sampled matrices supplement the proofs; they do not test the interacting law.

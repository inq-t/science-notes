# Coherent Source Subdivision

Cutting the complete retained source and transporting its comparisons preserves the response of an already prepared vacuum through spatial subdivision. Added Haar frames give the fine physical state and its full gauge-invariant carrier. The response nevertheless retains the original preparation: different coarse experiments can return different responses on the same fine vacuum.

## Coherent spatial extension retains its reference experiment

Fix a compact connected group \(G\) with semisimple Lie algebra and a positive
bi-invariant metric \(Q\); let \(p_t\) be its normalized heat density with
generator \(\Delta_Q\). Start with a finite graph, positive edge heat ages
\(t_e\), and an arbitrary smooth strictly positive gauge-invariant density
\(w\) relative to product Haar. Prepare it by the retained paired
bridges of [[prepared-vacuum-fisher-comparison/physical-vacuum-lift-and-fisher-comparison|the actual-vacuum lift]].
The next construction does not require an explicit formula for
\(w\), nor does it select \(w\).

Cut each retained path into finitely many pieces of heat ages
\(t_{e,j}>0\), with \(\sum_jt_{e,j}=t_e\), using the [[gauge-source-action-transport/source-action-transport-through-ordered-cuts#Cut the complete retained paths instead|complete path cut (ST2)]].
Transport its actual comparisons by the same source-cut action (ST5), including their
dependence on the preceding pieces. If \(Z_{e,j}\) are the raw
piece endpoints and \(\pi_eZ=\prod_jZ_{e,j}\), their joint density
is exactly
\[
q_{\rm cut}(Z)
=w(\pi Z)\,
 \frac{\prod_{e,j}p_{t_{e,j}}(Z_{e,j})}
      {\prod_ep_{t_e}(\pi_eZ)}.
\tag{ST11}
\]
The product heat law before the tilt follows from the source-cut
isomorphism. The coarse preparing density ratio simply travels
through it; it is not replaced by a new ratio on each piece.

Add independent Haar frames at the new bivalent vertices. For
one subdivided edge, with its old endpoint frames temporarily
fixed to the identity, the readout is
\(x_j=h_{j-1}Z_jh_j^{-1}\), \(h_0=h_n=1\).
Heat convolution gives
\[
\int_{G^{n-1}}\prod_j
 p_{t_j}(h_{j-1}^{-1}x_jh_j)\,dh_1\cdots dh_{n-1}
=p_{\sum_jt_j}(x_1\cdots x_n).
\tag{ST12}
\]
Consequently Haar averaging cancels the denominator in (ST11).
Restoring the old frames leaves the gauge-invariant density
unchanged. The entire fine endpoint law is
\[
\boxed{w(\pi x)\prod_{e,j}dx_{e,j}.}
\tag{ST13}
\]
Equivalently, the new internal gauge group acts freely and
transitively on each fixed-product fiber, and the **output**
conditional law there is uniform. The posterior distribution
of hidden source frames given the output need not be uniform.

Let \(\Phi\) be the complete path cut, and augment its source law
by the new independent frames. Transport a source comparison as
\(\Phi T\Phi^{-1}\), acting trivially on these extra frames.
Its Radon--Nikodym derivative is still the old \(R_T\circ\Phi^{-1}\),
by [[gauge-source-action-transport/source-action-transport-through-ordered-cuts#What full source covariance proves|source likelihood transport (ST6)]] and product augmentation. All vertex-frame translations
have zero score. These zero directions enforce exactly the fine
Gauss constraint, not separate closure of each piece.

Every fine invariant smooth observable is uniquely
\(Jf=f\circ\pi\). Its lifted value and comparison derivative are
those of the original observable. Thus the full completed score
pairing, its invariant dual response and its own closed form obey
\[
\boxed{\mathcal E_{\rm coherent}(Jf,Jg)
             =\mathcal E_{\rm original}(f,g).}
\tag{ST14}
\]
The inherited physical carriers and closed form domains are
unitarily identified. This is a source-level equality; inverting
a newly averaged fine endpoint Fisher matrix would return to the
different experiment ruled out by
[[prepared-vacuum-fisher-comparison/prepared-vacuum-subdivision-and-the-recovered-clock|the subdivision test]].

The [[prepared-vacuum-fisher-comparison/prepared-vacuum-subdivision-and-the-recovered-clock#An interacting cycle makes the mismatch explicit|interacting cycle comparison]] also resolves whether coherent extension
removes the initial reference. Take \(G=SU(2)\), \(Q=-2\operatorname{Tr}\),
and its same interacting cycle vacuum, with equal edge ages, electric
weights and endpoint splits. Keep total heat age \(L\), total electric
weight \(K\), and
\(s=\mathbb E_w|\nabla\log w|^2/3>0\). Extend both the four-edge
and eight-edge prepared experiments coherently to sixteen edges.
Both give exactly the same law (ST13), the same full physical
carrier and the same physical Hamiltonian. Yet their response
coefficients multiplying \(\mathbb E_w|\nabla f|^2\) remain
\[
c_{4\to16}=\frac{2L}{1+sL/2}
\;<\;
c_{8\to16}=\frac{2L}{1+sL/4}.
\tag{ST15}
\]
Independently preparing sixteen edges gives a third coefficient,
\(2L/(1+sL/8)\). Coherent transport preserves the initial
experiment faithfully; it does not make that experiment intrinsic
to its endpoint law or eliminate its starting graph as input.
Adding a genuine cycle changes the physical carrier and lies outside this
subdivision equivalence.

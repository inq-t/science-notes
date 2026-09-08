# Block Spectral Moments and Connected Assembly

An interacting reference can support the connected inverse estimate if its individual blocks satisfy four absolute spectral product bounds. These bounds allow output channels beyond a Haar spectral triangle; they control their total weighted contribution instead. Contractive multiplication prevents a constant from accumulating once per overlapping block, while two differentiated row bounds supply the precise kinetic compensation needed by the anchored norm.

**Status: [CONDITIONAL ASSEMBLY THEOREM].** The hypotheses below are local, infinite-dimensional block certificates, not results already proved for Wilson blocks. No global interacting gap is assumed. The reference generators, their full boundary-charged carriers and the unit of their energies remain supplied data. This theorem does not select a clock or establish a continuum limit.

## Four one-block certificates

Use the exact interacting reference in
[[interacting-reference-and-spectral-product-control|the change-of-reference construction]].
For each disjoint raw-link block \(b\), let
\[
d\nu_b=\psi_b^2\,dU_b,\qquad
\mathscr K_b=\psi_b^{-1}(H_b-E_b^0)\psi_b\ge0.
\tag{BM1}
\]
The configuration carrier is connected and compact, the metric and
potential are smooth, and \(\psi_b>0\) is the normalized ground vector.
Keep the entire raw block carrier, not only its separately neutral
sector. Choose a real orthonormal eigenbasis in \(L^2(\nu_b)\):
\[
\mathscr K_b\phi_{b,i}=\epsilon_{b,i}\phi_{b,i},\qquad
\phi_{b,0}=1,\quad \epsilon_{b,0}=0,\qquad
\epsilon_{b,i}\ge g_*>0\quad(i>0).
\tag{BM2}
\]
The lower bound is a supplied, uniform **one-block** bound.
Compactness gives a positive gap for each fixed block, but not a
specified uniform number for an unrestricted family of growing blocks.
For a fixed finite family of Wilson blocks,
[[interacting-reference-and-spectral-product-control#A block certificate must retain boundary charges|the raw density comparison (IR21)]]
does supply an explicit \(g_*\), including charged directions.
Its exponential deterioration with block size is retained, not hidden.

Temporarily suppress \(b\), and define
\[
h_i=\sqrt{\epsilon_i},\qquad
c_{ij}^k=\int\phi_i\phi_j\phi_k\,d\nu_b,\qquad
\gamma_{ij}^k=\frac{\epsilon_i+\epsilon_j-\epsilon_k}{2}.
\tag{BM3}
\]
The diffusion product rule gives
\[
\langle\Gamma_b(\phi_i,\phi_j),\phi_k\rangle_{\nu_b}
=\gamma_{ij}^k c_{ij}^k.
\]
Here \(\Gamma_b\) is the inherited kinetic carré du champ, unchanged
by the ground-state drift. In particular a constant input makes this
coefficient zero.

Choose weights \(\omega_{b,0}=1\), \(\omega_{b,i}\ge1\).
Assume finite constants \(A,B,D\), uniform in the reference blocks
and all input indices, such that
\[
\begin{aligned}
\sum_k\omega_k|c_{ij}^k|
&\le\omega_i\omega_j,
&&\text{(P0)},\\
\sum_k\omega_kh_k|c_{ij}^k|
&\le A(h_i+h_j)\omega_i\omega_j,
&&\text{(P1)},\\
\sum_k\omega_k|\gamma_{ij}^k c_{ij}^k|
&\le B h_i h_j\omega_i\omega_j,
&&\text{(G0)},\\
\sum_k\omega_kh_k|\gamma_{ij}^k c_{ij}^k|
&\le D(h_i+h_j)h_i h_j\omega_i\omega_j,
&&\text{(G1)}.
\end{aligned}
\tag{BM4}
\]
All four sums include the constant output. The factors \(h_0=0\)
remove it where appropriate. These are absolute one-block row
moments; a gap alone says nothing about their finiteness or constants.
The
[[interacting-reference-and-spectral-product-control#A positive gap does not preserve spectral fusion|deformed-circle example]]
disproves a pointwise spectral triangle, but does not disprove these
weighted aggregate conditions.

For the derivative interpretation also require, in the declared
block metric,
\[
\|\phi_i\|_\infty\le\omega_i,\qquad
\|\nabla_b\phi_i\|_\infty\le C_{\rm der}h_i\omega_i,\qquad
\|\operatorname{Hess}_b\phi_i\|_\infty
\le C_{\rm der}h_i^2\omega_i
\tag{BM5}
\]
with a uniform \(C_{\rm der}\). The Hessian norm may be the
Hilbert--Schmidt norm. These bounds are additional local hypotheses,
not consequences asserted from (BM4).

## Normalize multiplication once, not once per assembly

The constant one in (P0) matters. A bound with a factor \(C>1\)
at each block would yield \(C\) to the number of active overlapping
blocks in the product proof.

There is a local normalization that avoids this. Suppose weights
\(\omega_i\ge1\) initially satisfy, for \(i,j>0\),
\[
\sum_{k>0}\omega_k|c_{ij}^k|\le C\omega_i\omega_j.
\]
Set
\[
\widetilde\omega_0=1,\qquad
\widetilde\omega_i=r\omega_i\ (i>0),\qquad
r\ge\frac{C+\sqrt{C^2+4}}2.
\tag{BM6}
\]
Since the basis is real orthonormal, \(c_{ij}^0=\delta_{ij}\).
Thus for nonconstant inputs
\[
\sum_k\widetilde\omega_k|c_{ij}^k|
\le1+rC\omega_i\omega_j
\le(1+rC)\omega_i\omega_j
\le\widetilde\omega_i\widetilde\omega_j.
\]
A constant input gives the other input exactly, so (P0) holds
for every pair.

If the other moments in (BM4) already have finite constants,
this rescaling preserves that property: nonconstant output terms
gain only \(r\), whereas two nonconstant input weights gain \(r^2\).
Constant outputs either have \(h_0=0\) or gain no factor.
The trivial-input cases are exact. Bounds (BM5) are preserved as well.
For a uniform original \(C\), one common \(r\) suffices.
This increases the weights of finite-support sources; it does not
insert a fresh multiplicative factor during each later product.

## The anchored product norm

Consider a finite collection of these independent reference blocks,
with
\[
\mathscr K=\sum_b\mathscr K_b,\qquad
\nu=\bigotimes_b\nu_b,\qquad Qf=f-\nu(f).
\]
An interaction label touches every reference block in which it depends
on raw links. Connect two labels when they touch a common block.
For a nonempty connected label set \(C\), let
\(w_\mu(C)=e^{\mu\operatorname{diam}C}\), \(\mu>0\), using this
overlap graph and diameter zero for a singleton.

For a product eigenindex \(\mathbf i=(i_b)\), write
\[
\Phi_{\mathbf i}=\prod_b\phi_{b,i_b},\quad
\Omega_{\mathbf i}=\prod_b\omega_{b,i_b},\quad
h_b(\mathbf i)=\sqrt{\epsilon_{b,i_b}},\quad
h(\mathbf i)=\sum_bh_b(\mathbf i),\quad
E_{\mathbf i}=\sum_b\epsilon_{b,i_b}.
\tag{BM7}
\]
Actual spectral activity \(i_b>0\) need not fill the support of the
interaction label \(C\). Require only \(i_b=0\) outside that support.
Expand centered connected functions as
\[
U_C(t)=\sum_{\mathbf i\ne\mathbf0}
u_{C,\mathbf i}(t)\Phi_{\mathbf i},\qquad
\boxed{
\mathcal N_\mu(U)=
\sup_b\sum_{C,\mathbf i\ne\mathbf0}
w_\mu(C)h_b(\mathbf i)h(\mathbf i)\Omega_{\mathbf i}
\|u_{C,\mathbf i}\|_\infty.
}
\tag{BM8}
\]
Coefficients belong to \(C_b([0,\infty))\), and their norms are
taken **before** summing output channels. The scalar eigenbasis
requires no matrix-valued projective time norm. For a finite
collection of blocks the weighted coefficient completion is a
Banach space, with real-valuedness and zero initial values imposed
as closed conditions when needed.

Under (BM5), absolute differentiation gives
\[
\begin{aligned}
\sup_{t,b}\sum_Cw_\mu(C)\|\nabla_bU_C(t)\|_\infty
&\le\frac{C_{\rm der}}{\sqrt{g_*}}\mathcal N_\mu(U),\\
\sup_{t,b}\sum_Cw_\mu(C)\sum_a
\|\nabla_a\nabla_bU_C(t)\|_\infty
&\le C_{\rm der}^{(2)}\mathcal N_\mu(U),\\
C_{\rm der}^{(2)}&=\max(C_{\rm der},C_{\rm der}^2).
\end{aligned}
\tag{BM9}
\]
For two distinct blocks, differentiate the two separate factors,
which produces \(C_{\rm der}^2h_ah_b\Omega_{\mathbf i}\).
For a same-block Hessian use (BM5). Sum over \(a\), and use
\(h(\mathbf i)\ge\sqrt{g_*}\) for the first line.
The undifferentiated factors require the first bound in (BM5).
These are blockwise estimates. Converting them to summed raw-link
rows introduces only bounded block-size factors when block sizes
are uniformly bounded, not when the blocks grow without control.

## The inverse pays for the shared response

Let \(\Gamma=\sum_b\Gamma_b\), and define
\[
\mathcal B(U,V)_C(t)=
\int_0^t e^{-(t-s)\mathscr K}Q
\sum_{\substack{A_0\cup D_0=C\\A_0,D_0\ {\rm connected}}}
\Gamma(U_{A_0}(s),V_{D_0}(s))\,ds.
\tag{BM10}
\]
Then the one-block hypotheses imply
\[
\boxed{
\mathcal N_\mu(\mathcal B(U,V))
\le\frac{2e^\mu\max(AB,D)}{g_*}
\mathcal N_\mu(U)\mathcal N_\mu(V).
}
\tag{BM11}
\]
The same constant bounds the static map with
\(\mathscr K^{-1}Q\) in place of the time convolution.

To prove it, first use finitely many product eigenmodes.
For an input pair \(\mathbf i,\mathbf j\), an output \(\mathbf k\)
has product coefficient \(\prod_a c_{i_aj_a}^{k_a}\).
The coefficient of its carré du champ is
\[
\sum_f\gamma_{i_fj_f}^{k_f}\prod_a c_{i_aj_a}^{k_a}.
\tag{BM12}
\]
For a fixed anchor block \(b\) and shared response block \(f\),
sum its absolute output coefficient with weight
\(\Omega_{\mathbf k}h_b(\mathbf k)\).
If \(b\ne f\), apply (P1) at \(b\), (G0) at \(f\), and (P0)
everywhere else. The result is at most
\[
AB\,[h_b(\mathbf i)+h_b(\mathbf j)]
h_f(\mathbf i)h_f(\mathbf j)\,
\Omega_{\mathbf i}\Omega_{\mathbf j}.
\]
If \(b=f\), apply (G1) there and (P0) elsewhere, giving the
same expression with \(D\) in place of \(AB\).
This distinction is why a first output moment for ordinary
multiplication alone is insufficient.

Sum over \(f\), and write \(C_0=\max(AB,D)\).
For every nonconstant output,
\[
\frac{h(\mathbf k)}{E_{\mathbf k}}\le\frac1{\sqrt{g_*}},
\tag{BM13}
\]
because each nonzero \(h_a\) satisfies \(h_a^2\ge\sqrt{g_*}h_a\).
For scalar time coefficients \(u(s),v(s)\), the output convolution
has supremum at most
\(\|u\|_\infty\|v\|_\infty/E_{\mathbf k}\).
Thus (BM13) removes the output total-frequency weight in (BM8),
leaving
\[
\frac{C_0}{\sqrt{g_*}}
[h_b(\mathbf i)+h_b(\mathbf j)]
\sum_fh_f(\mathbf i)h_f(\mathbf j)
\Omega_{\mathbf i}\Omega_{\mathbf j}
\|u\|_\infty\|v\|_\infty.
\tag{BM14}
\]
The zero output was removed before division.

A nonzero \(f\)-term has both input indices active in block \(f\);
their label sets therefore have connected union and
\(w_\mu(A_0\cup D_0)\le e^\mu w_\mu(A_0)w_\mu(D_0)\).
Split the anchor in (BM14). For the branch \(h_b(\mathbf i)\),
the sum over the second input at fixed \(f\) obeys
\[
\sum_{D_0,\mathbf j}
w_\mu(D_0)h_f(\mathbf j)\Omega_{\mathbf j}
\|v_{D_0,\mathbf j}\|_\infty
\le g_*^{-1/2}\mathcal N_\mu(V).
\]
The remaining sum over \(f\) is \(h(\mathbf i)\), exactly
restoring the first input's anchored weight in (BM8).
The other branch exchanges \(U,V\). This proves (BM11).
There is no constant raised to the number of active blocks:
all untouched product factors used contractive (P0).

Absolute summability and the resulting bilinear bound extend the
map to the completed space. Under (BM5), the coefficient functions
and their second derivatives converge on every finite product,
so this extension agrees with the actual mild inverse response.
For time-dependent inputs the proof already summed the separate
coefficient suprema; no exchange of a matrix trace norm and time
supremum was used.

## Squared spectral control does not choose an absolute coefficient basis

The hypotheses in (BM4) concern a supplied eigenbasis, not just spectral
projectors. This distinction already matters for the actual raw Haar
\(SU(2)\) block, the zero-magnetic-coupling reference. With
\(Q=-2\operatorname{Tr}\) and unit kinetic coefficient, write
\[
K=-\Delta_Q,\qquad e_n=\frac{n(n+2)}4,\qquad
\dim_{\mathbb R}\ker(K-e_n)=(n+1)^2.
\tag{BM15}
\]
The real character \(\chi_n\) of spin \(n/2\) has Haar norm one,
and the exact product identity is
\[
\chi_1\chi_n=\chi_{n-1}+\chi_{n+1}.
\tag{BM16}
\]

Choose one real orthonormal eigenbasis as follows. Keep \(\chi_1\)
and every \(\chi_{4j}\), \(j\ge1\), as basis vectors. In each
distinct eigenspace of degree \(n+1\), \(n=4j\), choose an
orthonormal basis \((\eta_{n+1,r})_{r=1}^{(n+2)^2}\) such that
\[
\langle\chi_{n+1},\eta_{n+1,r}\rangle=\frac1{n+2}.
\tag{BM17}
\]
Such a real orthogonal rotation exists: it sends the unit coefficient
vector of \(\chi_{n+1}\) to the flat unit vector. These output
eigenspaces never coincide with the retained input eigenspaces, so
the choices define one basis simultaneously for all \(j\).

The upper output channel in (BM16) still has squared norm exactly
one, but its absolute coefficient sum is now \(n+2\). More strongly,
take any finite positive weights constant on each energy eigenspace,
\(W_n=\omega(e_n)\ge1\), nondecreasing with energy. The upper-channel
part of its (P0) row satisfies
\[
\frac{\displaystyle\sum_r W_{n+1}
 |\langle\chi_1\chi_n,\eta_{n+1,r}\rangle|}
 {W_1W_n}
=\frac{(n+2)W_{n+1}}{W_1W_n}
\ge\frac{n+2}{W_1}\longrightarrow\infty.
\tag{BM18}
\]
Thus not even a finite, uniform (P0) constant follows for this basis
from the gap and energy-weighted squared spectral tails. A fixed
rescaling of the active weights cannot remove this growth.

The differentiated row exhibits the same distinction. The two
response multipliers are
\[
\gamma_{1,n}^{n-1}=\frac{n+2}{4},\qquad
\gamma_{1,n}^{n+1}=-\frac n4,
\qquad
\|\Gamma(\chi_1,\chi_n)\|_2^2
=\frac{(n+2)^2+n^2}{16}.
\tag{BM19}
\]
For \(n=4j\), this squared norm is bounded by
\(h_1^2h_n^2\), independently of \(n\). Nevertheless the upper
part of the absolute (G0) row, divided by its input weight, is
at least \(\sqrt{n(n+2)}/(\sqrt3\,W_1)\), which diverges.
Every energy-weighted \(L^2\) moment, including those obtained from
iterated commutators with the fixed multiplier \(\chi_1\), is
unchanged by the rotations. Squared control loses no information
about the spectral projector; it does not control the number of
absolute scalar coordinates used inside that projector.

This does not invalidate the conditional theorem, exclude an
adapted good basis, or disprove other useful coefficient norms.
In particular \(\|\chi_1\|_\infty=2\), so the intrinsic band map
\(\Pi_{n+1}M_{\chi_1}\Pi_n\) has operator norm at most two in
every basis. [[kinetic-smoothing-and-connected-fourier-control|The Haar Fourier construction]]
keeps representation matrices and their
trace norm instead of making these arbitrary scalar coordinates
absolute. For an interacting reference, energy-eigenspace product
maps are likewise basis independent, but their differentiated
summability in a tensor-compatible norm remains an additional
certificate; bounded individual band maps alone do not prove (BM11).

[[first-order-lift-and-spectral-product-tails|The first-order lift]]
now gives a basis-independent alternative for fixed smooth
multipliers: an all-energy quadratic row bound and, separately,
an operator bound between whole spectral windows. Its Wilson
constants use only the inserted word's link gradients and the
supplied kinetic coefficient, not a block gap. These are actual
tail estimates; their conversion into a tensor-compatible
two-input norm is not implicit in (BM11).

## A second-order Hilbert norm still loses concentrated products

Fix one compact connected raw configuration manifold without boundary,
of dimension \(D\), and its actual smooth positive Wilson ground density
\(d\nu=\psi^2\,d\mathrm{vol}\), normalized to one. Keep this state and the
supplied kinetic metric fixed. On centered functions put
\[
L=-\kappa(\Delta+2\nabla\log\psi\cdot\nabla),\qquad
Qf=f-\nu(f),\qquad X(f)=\|Lf\|_{L^2(\nu)},\qquad
\mathcal B(f,g)=L^{-1}Q\Gamma(f,g).
\tag{BM20}
\]
Here \(\Gamma(f,g)=\kappa\langle\nabla f,\nabla g\rangle\).
Compact ellipticity gives a centered inverse and makes \(X\) equivalent
to the \(H^2\) norm for this fixed operator; no uniform block gap is
being assumed.

In normal coordinates about \(x_0\), write \(d\nu=w(x)\,dx\).
For a nonzero real \(\eta\in C_c^\infty(B(0,1))\), extend the following
bump by zero inside a sufficiently small coordinate chart:
\[
F_\delta(x)=\delta^{2-D/2}\eta(x/\delta),\qquad
f_\delta=F_\delta-\nu(F_\delta).
\tag{BM21}
\]
Rescaling the principal differential terms, with all coefficients
smooth and \(w(0)>0\), gives
\[
\begin{aligned}
\|Lf_\delta\|_2^2&\longrightarrow
 \kappa^2w(0)\int|\Delta\eta|^2>0,\\
\|\Gamma(f_\delta,f_\delta)\|_2^2
 &=\kappa^2w(0)\delta^{4-D}\int|\nabla\eta|^4(1+o(1)),\\
\nu(\Gamma(f_\delta,f_\delta))
 &=\kappa w(0)\delta^2\int|\nabla\eta|^2+o(\delta^2).
\end{aligned}
\tag{BM22}
\]
The integrals are over \(\mathbb R^D\). Centering changes no derivatives;
the smooth drift is lower order after rescaling. Moreover
\(\|Q\Gamma\|_2^2=\|\Gamma\|_2^2-|\nu(\Gamma)|^2\), so the subtraction
is only \(O(\delta^4)\). Thus, for \(D>4\),
\[
X(f_\delta)=O(1),\qquad
X(\mathcal B(f_\delta,f_\delta))
=\|Q\Gamma(f_\delta,f_\delta)\|_2
\asymp\delta^{2-D/2}\longrightarrow\infty.
\tag{BM23}
\]
No unrestricted bounded bilinear map \(X\times X\to X\) exists.
The endpoint \(D=4\) is different: for each fixed operator and \(D\le4\),
elliptic regularity and \(H^2\hookrightarrow W^{1,4}\) give
\(\|\nabla f\|_4\le C_L\|Lf\|_2\) on centered functions. Consequently
\(\|Q\Gamma(f,g)\|_2\le\kappa C_L^2X(f)X(g)\).
No uniformity of \(C_L\) across densities or growing blocks follows.

Replacing individual eigenvectors by dyadic spectral shells does not
repair the \(D>4\) example. At a fixed positive energy unit define
\[
P_{<1}=\mathbf1_{[0,1)}(L),\qquad
P_j=\mathbf1_{[2^{2j},\,2^{2j+2})}(L),\quad j\ge0,\qquad
\|f\|_{\mathfrak B}=\|P_{<1}f\|_2+
 \sum_{j\ge0}2^{2j}\|P_jf\|_2.
\tag{BM24}
\]
This is the declared spectral \(B^2_{2,1}(L)\) norm; no uniform
equivalence to coordinate Besov norms is required. Local differentiation
of (BM21), now through order four, gives
\[
\|f_\delta\|_2=O(\delta^2),\qquad
\|L^2f_\delta\|_2=O(\delta^{-2}),\qquad
\|P_jf_\delta\|_2\le
C\min(\delta^2,\delta^{-2}2^{-4j}).
\tag{BM25}
\]
The last bound follows directly from the spectral theorem.
Split the sum at \(2^J\asymp\delta^{-1}\): its low part is bounded
by \(C\delta^2\sum_{j\le J}2^{2j}=O(1)\), and its high part by
\(C\delta^{-2}\sum_{j>J}2^{-2j}=O(1)\). Hence
\[
\|f_\delta\|_{\mathfrak B}=O(1),\qquad
\|Lh\|_2\le4\|h\|_{\mathfrak B}.
\tag{BM26}
\]
Together with (BM23), this disproves unrestricted bilinear closure
in this dyadic norm for \(D>4\), without any choice of eigenbasis.

These dimensions count raw configuration variables: four \(SU(2)\)
links give \(D=12\), and the adjacent two-plaquette graph gives
\(D=21\). They are not spatial or spacetime dimensions. A smaller
neutral quotient cannot silently replace the boundary-charged raw
carrier required for assembly. Unlike
[[../conditional-fisher-coercivity/bounded-coupling-and-conditional-score-concentration|concentration obtained by varying a reference]],
this test keeps the entire reference fixed and concentrates only its
observables. It rules out these unrestricted norm closures, not the
actual reachable class generated by Wilson preparation, stronger
hybrid norms, or the conditional moment theorem (BM11).

[[transition-score-and-lipschitz-product-control|The transition-score estimate]]
supplies a stronger, genuinely two-input control in the homogeneous
Lipschitz quotient, without a choice of eigenbasis. It controls
gradients pointwise rather than only in a second-order Hilbert norm.
Its product-copy uniformity still leaves the edge-anchored
extensive-source estimate to prove.

## What remains to certify on an actual block

With a source satisfying the corresponding finite weighted
eigen-expansion bound, (BM11) can replace the bilinear step in
[[kinetic-smoothing-and-connected-fourier-control#Construct the actual logarithm, rather than assume its bound|the connected fixed-point construction]].
It is not itself a claim that the Wilson source or its reference
blocks meet (BM2), (BM4) and (BM5). Each moment is an infinite sum
over all output channels and a uniform statement over input pairs;
finite spectral tables need analytic tail bounds before they
constitute such a certificate.

Ordinary block \(C^1\)-to-\(C^2\) heat smoothing does not directly
verify these absolute row moments. Differentiating
\(\Gamma_b(f,g)\) twice encounters third derivatives of an input.
A bound that repairs this by a \(t^{-1/2}\) smoothing factor,
combined only with decay \(e^{-ng_*t}\) for \(n\) active blocks,
has integral proportional to \(n^{-1/2}\), not the full
inverse-energy compensation used above. This describes the loss
in that crude proof strategy, not an impossibility theorem for
sharper block heat estimates.

The completed two-plaquette calculation certifies a neutral
relational sector and its actual positive ground vector.
The separate raw comparison supplies a nonsharp block gap, but
neither result certifies the weighted moments and derivative
bounds (BM4)--(BM5) on all boundary-charged block channels
that crossing interactions can excite.
Bounded block size can make uniform constants plausible across a
finite list of block types; it does not supply their values,
their differentiated product bounds, or a new physical clock.

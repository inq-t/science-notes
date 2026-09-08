# Heat-state continuity and response closability

A scale-dependent heat-kernel state changes the response of small loops, but it does not make every compatible finite response into a continuum operator. In a planar gauge construction, nearby loop characters converge to the same observable in the state's Hilbert norm. An additive perimeter response nevertheless makes edge-disjoint loops form-orthogonal. Averaging those nearby loops then proves that this cylinder form is not closable. The state and response must agree about approximate indistinguishability, not only about exact finite-graph gluing.

**Status: [EXACT] for the planar heat-state construction, one-loop estimates, and nonclosability of the specified perimeter response; [OPEN] for a replacement response yielding the required Yang--Mills physical clock. The two-dimensional history state used here is not a four-dimensional vacuum construction.**

## The state is fixed by an additive face law

Use \(G=SU(2)\) with normalized Haar measure and
\[
Q(X,Y)=-2\operatorname{Tr}(XY),\qquad
D=-\Delta_Q,\qquad C_2(j)=j(j+1).
\tag{HS1}
\]
Thus \(Q=4g_{\rm round}\) on the unit-quaternion three-sphere.
It is twice the fundamental trace metric \(Q_R\) used in
[[holonomy-state-refinement/overlap-kernels-and-face-refinement|the overlap construction]].
For \(t>0\), let \(q_t\) be the density of \(e^{-tD}\) started at
the identity. It is smooth, strictly positive, central, normalized, and
\(q_s*q_t=q_{s+t}\).

On a regular finite cellulation of a planar disk with free exterior
boundary, choose \(\sigma>0\) and the state
\[
d\mu_\Gamma(U)=\prod_{p}q_{\sigma A_p}
(\operatorname{Hol}_pU)\prod_e dU_e,
\tag{HS2}
\]
where \(A_p>0\) is the supplied face area. Its partition function is
one: successively integrate interior links and then the remaining
boundary holonomy. The
[[holonomy-state-refinement/overlap-kernels-and-face-refinement#Integrating the shared edge produces a joint law|exact two-face convolution]]
also proves consistency under the disk subdivisions used below.
The heat law and its area assignment are inputs, not derived physical
clock time. This uses regular disk sewing, not a claim that an arbitrary
planar multigraph is determined by one boundary product.

For coherently oriented nested simple loops, transport along compatible
noncrossing tree spokes to one root gives based
holonomies \(X_{t_1},\ldots,X_{t_m}\), with
\(0<t_1<\cdots<t_m\) the enclosed heat-areas \(t_i=\sigma A_i\).
Cut the intervening annuli along tree spokes and integrate their
interiors. The retained joint law is
\[
q_{t_1}(x_1)\prod_{i=2}^m
q_{t_i-t_{i-1}}(x_{i-1}^{-1}x_i)\prod_i dx_i.
\tag{HS3}
\]
Normalized Haar tree gauge introduces no extra determinant here.
Independent heat increments and their product reconstruct (HS3);
integrating an intermediate loop simply convolves its two increments.
Loop characters do not depend on the chosen spokes. Fixing the outer
holonomy instead would give a heat bridge and a different law.

Consequently, for any irreducible character and \(s<t\),
\[
\mathbb E[\chi_j(X_t)\mid X_s]
=e^{-C_2(j)(t-s)}\chi_j(X_s).
\tag{HS4}
\]
This is an area-indexed state identity. It is not an identification of
the proposed response generator with the physical Hamiltonian.

## The concentrated state removes the cheap single-loop test

Keep the additive edge response \(\alpha_e=\kappa\ell_e\),
\(\kappa>0\), from
[[holonomy-state-refinement/holonomy-refinement-and-clock-compatibility|holonomy refinement]].
For an observable \(F\) of one simple loop holonomy, the exact induced
norm and form are those of \(q_tdg\) and
\[
\mathcal E_C(F)=B_C\int_G|\nabla F|_Q^2q_t\,dg,
\qquad B_C=\sum_{e\in C}\alpha_e=\kappa P(C).
\tag{HS5}
\]
Here \(P(C)\) is perimeter. This is a restriction of the full graph
form to loop observables; it need not be an autonomous graph subclock.

Take the real fundamental character \(f=\chi_{1/2}=2\cos\theta\).
The identities \(f^2=1+\chi_1\), \(Df=3f/4\), and
\(|\nabla f|_Q^2=1-f^2/4\) give
\[
\begin{aligned}
\mathbb E_t f&=2e^{-3t/4},\\
V(t):=\operatorname{Var}_t(f)&=1+3e^{-2t}-4e^{-3t/2},\\
J(t):=\mathbb E_t|\nabla f|_Q^2&=\tfrac34(1-e^{-2t}).
\end{aligned}
\tag{HS6}
\]
For example, the gradient identity follows directly from
\(\Gamma(f)=fDf-\tfrac12D(f^2)\). The centered-character quotient is
\[
\mathscr R_C(t)=B_C\frac{J(t)}{V(t)}
=\frac{B_C}{t}\left(1+\frac t6+O(t^2)\right).
\tag{HS7}
\]
The variance is of order \(t^2\), not order one. With
\(y=e^{-t/2}\), its exact factorization
\(V(t)=(1-y)^2(1+2y+3y^2)\) prevents numerical cancellation.

There is also a full one-holonomy lower bound. In this metric
\(\operatorname{Ric}=Q/2\). Bochner's identity for
\(P_s=e^{-sD}\), followed by the maximum principle, gives
\(|\nabla P_sF|^2\le e^{-s}P_s|\nabla F|^2\).
The semigroup variance identity therefore implies
\[
\begin{split}
\operatorname{Var}_{q_t}(F)
&=2\int_0^t P_s|\nabla P_{t-s}F|^2(e)\,ds\\
&\le 2(1-e^{-t})\int|\nabla F|^2q_t\,dg.
\end{split}
\tag{HS8}
\]
For the positive weighted elliptic generator of (HS5), on the entire
class-function carrier \(L^2(G,q_tdg)^{\operatorname{Ad}G}\), this proves
\[
\frac{B_C}{2(1-e^{-t})}
\le\operatorname{gap}L_C\le\mathscr R_C(t).
\tag{HS9}
\]
Its form domain is \(H^1(G)^{\operatorname{Ad}G}\); at fixed positive
\(t\), smooth positivity of \(q_t\) gives the compact elliptic
realization and unique constant kernel. The lower bound actually holds
before restricting to class functions. It is not a lower bound on the
full graph operator.

For a square of side \(a\), \(t=\sigma a^2\) and \(B_C=4\kappa a\),
the isolated-loop threshold is therefore of order \(1/a\), not \(a\).
The state evades the uniformly bounded density hypothesis in (HC17)–(HC18).
This removes the old Haar small-loop witness; it does not establish a
uniform graph gap or even a continuum response operator.

## Nearby loops become the same state-observable

For the same character, put \(M(t)=\mathbb E f_t^2=1+3e^{-2t}\).
Equation (HS4) gives the exact raw crossmoment
\[
\mathbb E[f_sf_t]=e^{-3(t-s)/4}M(s)\quad(s\le t),
\qquad
\|f_t-f_s\|_2^2=M(t)+M(s)-2e^{-3(t-s)/4}M(s).
\tag{HS10}
\]
Thus characters of nested loops converge in the state's \(L^2\) norm
when their annular area tends to zero, even when their edge sets do
not intersect. This conclusion uses raw moments; subtracting the
means is optional and leaves the response unchanged.

An explicit countable graph family makes the issue precise. Take
concentric squares \(C_0,C_1,C_2,\ldots\), of areas
\(A_0>0\) and \(A_k=A_0+\varepsilon_*/k\), with \(\varepsilon_*>0\).
At stage \(N\), include \(C_0,\ldots,C_N\) and four diagonal spokes
joining corresponding corners. The annuli split into ordinary
trapezoidal disk faces. Adding the next square subdivides existing
spokes and faces; every finite stage is a regular cellulation of the
same outer square \(C_1\), whose boundary remains free.

The face laws (HS2) have compatible marginals and hence a projective
state \(\mu\) on
\[
X=\varprojlim_N G^{E_N},\qquad
\mathcal G=G^{\bigcup_N V_N},\qquad
\mathcal H_{\rm phys}=L^2(X,\mu)^{\mathcal G}.
\]
The vertex actions are compatible with edge products: newly introduced
intermediate-vertex transformations cancel in old paths. Each finite
law is invariant, hence so is \(\mu\). Smooth gauge-invariant cylinders
are dense in \(\mathcal H_{\rm phys}\), by cylinder approximation
followed by compact-group averaging. At every stage define the finite form
\[
\mathcal E_{\rm len}(F,G)
=\sum_e\kappa\ell_e\int
\langle\nabla_eF,\nabla_eG\rangle_Q\,d\mu_\Gamma.
\tag{HS11}
\]
Its \(H^1\) domain gives a closed elliptic form at that finite stage,
restricted to gauge invariants for the physical carrier. Additivity of
segment lengths and (HC6) make its values on pulled-back cylinders
consistent. There is therefore a well-defined positive cylinder
preform on the projective state. Closability has not followed.

Write \(f_k=\chi_{1/2}(\operatorname{Hol}_{C_k})\). Characters have no
spoke derivatives, and different square boundaries share no edges.
Thus, pointwise in every common graph,
\[
\mathcal E_{\rm len}(f_i,f_j)=0\quad(i\ne j),\qquad
b_k:=\mathcal E_{\rm len}(f_k)
=\frac{3\kappa}{4}P(C_k)(1-e^{-2\sigma A_k}).
\tag{HS12}
\]
In particular \(b_0>0\) and \(\sup_kb_k=:B<\infty\), while
\(f_k\to f_0\) in \(L^2(\mu)\) by (HS10).

## The cylinder response has no closed realization

Set
\[
F_N=\frac1N\sum_{k=1}^Nf_k,\qquad g_N=f_0-F_N.
\tag{HS13}
\]
Cesaro convergence gives \(g_N\to0\) in \(L^2(\mu)\). In the form,
however,
\[
\begin{aligned}
\mathcal E_{\rm len}(F_N)&=\frac1{N^2}\sum_{k=1}^Nb_k\le B/N,\\
\mathcal E_{\rm len}(g_N)&=b_0+\mathcal E_{\rm len}(F_N)\longrightarrow b_0>0,\\
\mathcal E_{\rm len}(g_N-g_M)&\le2B/N+2B/M\longrightarrow0.
\end{aligned}
\tag{HS14}
\]
This violates the defining closability criterion: a form-Cauchy
sequence converging to zero in the state norm must have energy tending
to zero. Therefore (HS11) has **no closed form extension agreeing on
all these cylinders**, and supplies no positive self-adjoint continuum
generator by form closure. Centering each \(g_N\) by its state mean
gives the same violation on the vacuum-orthogonal physical carrier.

The failure is neither absence of the state nor a small spectral gap.
Every finite state and finite operator exists. Exact finite marginal
and form consistency also hold. The obstruction appears when the state
completion identifies approximate observations that the response
continues to treat as orthogonal. This is a concrete realization of
the [[general-causal-action/carrier-first-reversal#The Copernican criterion: change the primitives|carrier-first closability obligation]].

## What a replacement response must retain

Suppose a replacement is a closed positive form \(\mathcal E\) on
the same state carrier, includes these \(f_k\) in its domain, assigns
\(\mathcal E(f_0)>0\), and has uniformly bounded \(\mathcal E(f_k)\).
Lower semicontinuity of a closed form forces
\[
\boxed{
\mathcal E(f_0)\le
\liminf_{N\to\infty}\frac1{N^2}
\sum_{i,j=1}^N\operatorname{Re}\mathcal E(f_i,f_j).}
\tag{HS15}
\]
The diagonal part tends to zero. A nonzero aggregate of mixed responses
must survive between nearby, edge-disjoint loops. The inequality does
not determine each pair separately or supply the replacement kernel.
Allowing the approximating loop energies to diverge also leaves its
bounded-energy hypothesis. Changing the domain, the readout, or the
state topology is another possible route, but must then reconstruct
the intended observables.

This gives an operator-type constraint: an edge-diagonal response with
uniformly bounded energies for these approximating loops cannot be
retained while the state makes them approximately equal to a
positive-energy observable. It is not an objection to QFT microcausality.
The failed operator was an auxiliary perimeter-gradient process on a
two-dimensional history state, not the reconstructed Yang--Mills
Hamiltonian. A different renormalized or transversely coupled response
requires its own construction, and an independently identified physical
clock would still be needed before reading its threshold as mass.

[[gauge-path-fisher-response/shared-driver-response-and-the-nested-holonomy-clock|The shared-driver
construction]] supplies one explicit repair on the complete nested-holonomy
path carrier. It changes the diagonal as well as the mixed response,
and makes these approximating characters converge in the form norm.
The full invariant unit-OU clock has threshold two, but variable driver
rates give the same state and symmetry with a unique vacuum and no gap.
Thus closure can now be achieved in this sector without settling clock
selection or constructing the response on every planar graph observable.

The existing [[gauge-boundary-frame-gluing/receipts/boundary_charge_gluing_receipt.py|boundary receipt]]
checks the exact character identities and the finite nested-loop Gram
formulas, including \(\|g_N\|_2^2\), \(\mathcal E(g_N)\) and
\(\mathcal E(F_N-F_{2N})\). The limit proof is (HS10)–(HS14), not
extrapolation from the numerical sequence.

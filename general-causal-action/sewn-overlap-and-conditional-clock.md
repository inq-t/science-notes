# A Sewn Overlap Can Fix a Joint State and Its Comparison Clock

Two positive comparisons sewn through a shared boundary determine a correlated state. If processing is then stipulated to consist of the two conditional comparisons, that same state determines a complete generator and its mixed response. The resulting spectrum is constrained by the original overlap. A binary member returns an exact \(\operatorname{sech}^2\) gap, which decreases as the comparison sharpens; a compact \(SU(2)\) member retains its slow mode under simultaneous conjugation. This is an explicit joint-selection construction with declared inputs, not a Yang–Mills realization.

**Status: exact construction and spectral theorem for the stated family.** The conditional-update rule is an additional axiom. The group, overlap, two-context structure and common clock normalization are supplied. The bounded clock does not have the required field-theory ultraviolet behavior. No novelty is claimed for the underlying conditional-expectation or two-projection mathematics.

## Declare a comparison before its state or clock

Let \(G\) be a nontrivial compact group with normalized Haar measure. Choose a continuous strictly positive normalized central density \(p\), with \(p(g^{-1})=p(g)\). A concrete source is [[holonomy-state-refinement/overlap-kernels-and-face-refinement|the anchored representation overlap]], normalized after an integer tensor power. That note owns its representation, anchor and refinement conventions.

Sew the two comparisons through one boundary variable:

\[
q(xy^{-1})=\int_Gp(xu^{-1})p(yu^{-1})\,du,
\qquad d\pi(x,y)=q(xy^{-1})\,dx\,dy.
\tag{SC1}
\]

Centrality and inversion symmetry identify \(q=p*p\). The integral is a Gram kernel. Normalization gives both complete marginals exactly Haar, while fixing their joint correlation. Fubini's theorem makes the evaluation independent of integration order when several such factors are sewn. This is a statement about full factors, not closure of a chosen one-parameter family under arbitrary elimination.

The type of the returned object matters: \(q\) is a **joint probability density**, obtained by normalizing and sewing positive comparison kernels. Its positive amplitude in product-Haar \(L^2\) is \(\sqrt q\). We do not identify \(q\) itself with a normalized physical amplitude. The state carrier is \(\mathcal H=L^2(G^2,\pi)\), with vacuum \(1\).

Define \(P_x=\mathbb E_\pi[\cdot\mid x]\) and \(P_y=\mathbb E_\pi[\cdot\mid y]\). These are orthogonal projections onto the two full readout algebras. Add the explicit process rule

\[
T_\epsilon=(1-2\epsilon)I+\epsilon P_x+\epsilon P_y,
\quad 0\le\epsilon\le\tfrac12,
\qquad L=2I-P_x-P_y.
\tag{SC2}
\]

The discrete rule is a positive Markov operator and a positive Hilbert contraction. Its repeated small steps converge in operator norm:

\[
T_{t/n}^{\,n}\longrightarrow e^{-tL}.
\]

Thus the clock is a return of the declared conditional-comparison protocol. Equality of the two rates respects exchange of contexts. A common rate multiplier remains the unit of this clock; permitting unequal rates would be additional primitive data.

The first-order discrepancy row has a direct realization:

\[
\delta f=((I-P_x)f,(I-P_y)f),\qquad \delta^*\delta=L.
\tag{SC3}
\]

Its pairing, projections and generator use the same \(\pi\). The semigroup satisfies the one-parameter reflection-positivity identity

\[
\sum_{i,j}\langle f_i,e^{-(t_i+t_j)L}f_j\rangle
=\left\|\sum_i e^{-t_iL}f_i\right\|^2\ge0.
\]

This is not the full four-dimensional Osterwalder–Schrader return. It supplies a precisely typed positive process for comparison with [[general-causal-action/research-schema|the joint-realization proposal]].

## One overlap coefficient fixes two dynamical rates

Let \(C_p\) and \(C_q=C_p^2\) be convolution on \(L^2(G)\). The readout isometries \(J_x\phi=\phi(x)\), \(J_y\phi=\phi(y)\) obey

\[
J_x^*J_y=C_q.
\tag{SC4}
\]

For a centered normalized eigenfunction \(C_p\phi=b_\lambda\phi\), write \(a_\lambda=b_\lambda^2\). Then

\[
\begin{aligned}
L[\phi(x)+\phi(y)]&=(1-a_\lambda)[\phi(x)+\phi(y)],\\
L[\phi(x)-\phi(y)]&=(1+a_\lambda)[\phi(x)-\phi(y)].
\end{aligned}
\tag{SC5}
\]

The squared norms of these orthogonal vectors are \(2(1+a_\lambda)\) and \(2(1-a_\lambda)\). Their equal-time covariance is \(a_\lambda\). Every vector with both conditional expectations zero has rate \(2\).

These channels cover the complete carrier. Continuity and strict positivity give \(q\ge m>0\); hence, on centered functions, \(\|C_q\|\le1-m<1\). This angle bound makes the sum of the two centered readout spaces closed. Their orthogonal complement is exactly \(\ker P_x\cap\ker P_y\). Full support makes the intersection of the two readout spaces consist only of constants. Consequently

\[
\boxed{\operatorname{gap}(L)=1-\|C_q\|_{L^2_0(G)}
=1-\sup_{\lambda\ne0}|b_\lambda|^2.}
\tag{SC6}
\]

More explicitly, if \(m_p=\min p\), decomposing
\(p=m_p+(1-m_p)\widetilde p\) gives
\(\operatorname{gap}(L)\ge2m_p-m_p^2\); the case \(p=1\)
has gap one directly. This supplies a sufficient uniform estimate
only when the comparison floor itself stays uniformly positive.

The complete mixed return is also fixed:

\[
\begin{aligned}
\langle\phi(x),e^{-tL}\phi(y)\rangle_\pi
&=\frac{1+a_\lambda}{2}e^{-(1-a_\lambda)t}
-\frac{1-a_\lambda}{2}e^{-(1+a_\lambda)t},\\
\langle\phi(x),L^{-1}\phi(y)\rangle_\pi
&=\frac{2a_\lambda}{1-a_\lambda^2}.
\end{aligned}
\tag{SC7}
\]

Integrating the first line proves the second. This is an actual mixed susceptibility through the full dynamics, in addition to a static covariance. A one-context compressed clock would generally lose one of the two rates; [[coarse-response-memory/inq|coarse response memory]] owns that distinction.

## An explicit compact-group member

For \(G=SU(2)\) in its two-dimensional representation, the first normalized power of the anchored overlap is

\[
p(g)=1+\frac14\chi_1(g),
\qquad q(g)=1+\frac1{32}\chi_1(g).
\tag{SC8}
\]

Here \(\chi_1\) denotes the fundamental character, indexed by twice the spin. Character convolution \(\chi_j*\chi_j=\chi_j/d_j\) gives \(b_1=1/8\) and \(a_1=1/64\). Every higher nonconstant multiplier is zero. The entire spectrum is

\[
\sigma(L)=\left\{0,\frac{63}{64},1,\frac{65}{64},2\right\},
\quad
\mathbb E_\pi[\chi_1(x)\chi_1(y)]=\frac1{64},
\quad
\langle\chi_1(x),L^{-1}\chi_1(y)\rangle=\frac{128}{4095}.
\tag{SC9}
\]

The density and process respect common left and common right translations and context exchange. In particular the slow vector \(\chi_1(x)+\chi_1(y)\) is invariant under simultaneous conjugation. Restricting to that specified invariant carrier preserves the gap \(63/64\). This does not identify simultaneous conjugation with every Gauss constraint of an arbitrary lattice construction.

The rate-one and rate-two spaces are nonempty: witnesses are
\(\chi_2(x)\) and \(\chi_2(x)\chi_2(y)\), respectively,
because \(C_q\chi_2=0\).

The state has Haar individual marginals. It is therefore not the interacting two-plaquette vacuum with nonzero internal plaquette coupling. [[coarse-response-memory/correlated-interface-tangent|The certified interface response]] supplies the more demanding finite Yang–Mills benchmark that a claimed recovery map would have to reach.

## The binary member returns the original sech-squared clue

Take \(G=\mathbb Z_2\), represented by \(x=\pm1\), and the anchored overlap \(\kappa(xu)=(2+xu)/3\). Its normalized integer tensor power is

\[
p_k(xu)=1+r_kxu,\qquad
r_k=\frac{3^k-1}{3^k+1}
=\tanh\!\left(\frac{k\log3}{2}\right).
\tag{SC10}
\]

Sewing gives the four-state probabilities \(\pi_k(x,y)=(1+\rho_kxy)/4\), with \(\rho_k=r_k^2\). The eigenvectors \(1,x+y,x-y,xy-\rho_k\) have rates \(0,1-\rho_k,1+\rho_k,2\). Thus

\[
\boxed{\operatorname{gap}(L_k)
=1-\rho_k
=\operatorname{sech}^2\!\left(\frac{k\log3}{2}\right).}
\tag{SC11}
\]

The exact rational four-state checks are in [[receipts/sewn_overlap_clock_receipt.py|the sewn-overlap receipt]]. The same formulas extend smoothly to real \(k\ge0\) in this binary example; only integer \(k\) has the stated tensor-power interpretation. With \(u=k\log3/2\), the curvature crossing of the extended gap occurs at

\[
\tanh^2u=\frac13,\qquad \operatorname{gap}=\frac23.
\]

It is a change of curvature, not the appearance of a gap. Every finite \(k\) is gapped, while \(k\to\infty\) gives perfect alignment and an arbitrarily soft collective mode. The family therefore derives the proposed shape and simultaneously exhibits failure of a uniform lower bound at fixed update rate.

There is a decisive carrier check. If simultaneous binary flip is made a gauge redundancy, \(x\pm y\) are removed and the invariant nonvacuum mode has rate \(2\). If that flip is a global physical symmetry, the slow modes remain. A gap statement must specify which of these two observable algebras it concerns.

Binary simultaneous flip is a translation action; conjugation on
\(\mathbb Z_2\) is trivial. Likewise the \(SU(2)\) character witness
above does not survive quotienting common left or right translations.
The two examples specify different gauge actions, not a universal
rule that neutralization always retains or always removes the gap.

## Sharpening closes the gap on compact groups too

For the faithful anchored overlap, \(\kappa(e)=1\) is its unique
maximum. Hence normalized \(p_k\propto\kappa^k\) converges weakly
to \(\delta_e\). Indeed, outside any neighborhood of \(e\),
\(\kappa\le c<1\); a smaller neighborhood of positive Haar measure
has \(\kappa\ge d>c\). The ratio of its outside mass to the
normalization is bounded by a constant times \((c/d)^k\).

Every fixed representation multiplier therefore satisfies
\(b_{k,\lambda}\to1\). For any fixed nontrivial representation,

\[
0\le\operatorname{gap}(L_k)
\le1-b_{k,\lambda}^2\longrightarrow0.
\tag{SC13}
\]

In the shared-boundary realization, both retained variables
concentrate at the same Haar-distributed boundary value.
Consequently \(\pi_k\) converges weakly to diagonal Haar measure,
and for a fixed normalized centered representation mode,

\[
\|\phi(x)-\phi(y)\|_{\pi_k}^2
=2(1-b_{k,\lambda}^2)\longrightarrow0.
\tag{SC14}
\]

This proves loss of a relative distinction in that unrenormalized
limit, together with softening of the collective mode. It does
not rule out enlarged carriers, rescaled distinctions or a
different processing law. Such replacements require explicit
comparison maps and an independent clock normalization; weak
convergence of the states alone does not construct their limit.

## The extra law selects something, but does not explain itself

Holding \(G,p\), the two contexts and (SC2) fixed leaves no separate joint-state or generator parameter. Admissible spectra lie in \([0,2]\), their paired rates sum to two, and their separation is fixed by the sewn correlation. This family therefore cannot encode an arbitrary positive Hamiltonian.

The restriction to the two conditional updates is essential. Let \(P_0\) project onto constants. For every \(\theta\ge0\),

\[
L_\theta=L+\theta(I-P_0)
\tag{SC12}
\]

preserves the same state, listed symmetries, Markov property, exact semigroup sewing and temporal reflection positivity, while shifting every nonvacuum rate by \(\theta\). It adds whole-state resampling and so violates (SC2). The independent-retuning test succeeds only with that new constitutive restriction declared.

The construction does not derive its anchor, representation, context structure or processing rule from necessity. Nor does it yet privilege directed multiplication over other ways of selecting a comparison. It does force a joint correlation, discrepancy form and full mixed response from fewer independently adjustable choices. [[sewn-overlap-refinement|Its compact-group refinement]] now returns a collective Laplacian and a uniform comparison gap. [[resolved-relative-boundary-and-two-clock-limits|The exact common-carrier test]] nevertheless shows that the accelerated clock expels relative dynamics. The next constitutive problem is to preserve both kinds of distinction through an unbounded refinement, with a justified normalization and a uniform physical estimate.

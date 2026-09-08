# Octonionic Associators and Branch Forgetting

Two parenthesizations of octonionic multiplication can give different, individually reversible operators. Their discrepancy detects what lies outside a selected quaternion context; comparing every orthonormal imaginary pair gives a positive response on the entire imaginary carrier, with only the real unit line undetected. Discarding a branch label instead produces a noninvertible matrix channel, whose undetected directions are different. Conversely, projecting an associative ambient product can yield a nonassociative retained product. These are exact relationships between multiplication, comparison and forgetting, not yet chronology or a mass gap.

## Fix the multiplication and the selected context

Use the real normed algebra
\[
\mathbb O=\mathbb H\oplus\mathbb H\ell,
\qquad
(p+q\ell)(r+s\ell)
=(pr-\bar s q)+(sp+q\bar r)\ell.
\tag{AF1}
\]
Quaternion multiplication is associative, \(i^2=j^2=k^2=-1\), and \(ij=k=-ji\). The Euclidean norm is
\[
|p+q\ell|^2=|p|^2+|q|^2.
\]
The embedded \(\mathbb H\), its complementary presentation \(\mathbb H\ell\), and the units \(i,j\) are selected data. The calculation does not claim that a physical context or preferred quaternion pair has already been selected by the whole algebra.

For \(a\in\mathbb O\), let \(L_a x=ax\) be a real-linear operator on \(\mathbb O\). Set
\[
U=L_iL_j,\qquad V=L_{ij}=L_k.
\tag{AF2}
\]
The composition in \(L_iL_j\) is ordinary associative composition of linear maps. Norm multiplicativity implies that \(L_i,L_j,L_k\), hence \(U,V\), are orthogonal. No noninvertible map has appeared.

A monoidal associator is an invertible coherence map between two bracketed tensor presentations. The octonionic associator used here is instead the trilinear multiplication defect
\[
[a,b,x]=(ab)x-a(bx).
\tag{AF3}
\]
These are different types. Here \([i,j,\cdot]=V-U\) measures the discrepancy between two actual operations; it is not an arrow that changes one history into another. [[local-global-individuation|Local--global individuation]] distinguishes presentation equivalences from directed processes.

## The relative operator is an exact reflection

Let \(P\) project orthogonally onto \(\mathbb H\) and \(Q=I-P\) onto \(\mathbb H\ell\). For \(h\in\mathbb H\), associativity inside that subalgebra gives
\[
U(h)=i(jh)=kh=V(h).
\tag{AF4}
\]
On the complementary summand, the declared multiplication gives
\[
L_j(h\ell)=(hj)\ell,
\qquad
U(h\ell)=((hj)i)\ell=-hk\ell,
\qquad
V(h\ell)=hk\ell.
\tag{AF5}
\]
Both operators preserve the two summands. Therefore
\[
\boxed{R:=U^*V=P-Q,\qquad V=UR,\qquad R^*=R,\quad R^2=I.}
\tag{AF6}
\]
Their multiplication defect \(D=V-U=U(R-I)=-2UQ\) consequently satisfies
\[
\boxed{D^*D=4Q,\qquad \|[i,j,x]\|^2=4\|Qx\|^2.}
\tag{AF7}
\]
The associator thus supplies an exact positive response: it detects precisely the components outside the selected associative context. Neither branch is irreversible, despite their nonzero discrepancy. More generally, \(L_{ab}-L_aL_b\) retains the original nonassociative multiplication as a defect inside an associative endomorphism algebra. This is compatible with the [[exceptional-state-comparison/cyclic-context-retraction-and-response|exceptional regular realization]], where injectivity and positivity of a linear realization do not imply preservation of the original product.

The result is presentation-covariant. An octonion automorphism \(g\in G_2\) sends the selected units and quaternion subalgebra to \(gi,gj,g\mathbb H\), and \(L_{ga}=gL_ag^{-1}\). Its response is consequently \(g(4Q)g^{-1}\). This covariance does not privilege any one context.

## Complete comparison removes the selected-context blind directions

The multiplication and Euclidean norm in (AF1) determine a single
linear analysis map
\[
\mathcal A_{\rm as}:\mathbb O\longrightarrow
\operatorname{Hom}_{\mathbb R}
  (\Lambda^2\operatorname{Im}\mathbb O,\mathbb O),\qquad
(\mathcal A_{\rm as}x)(u\wedge v)=[u,v,x].
\tag{AF15}
\]
Alternativity makes the associator alternating in \(u,v\).
Give the target its Hilbert--Schmidt norm, with
\(e_i\wedge e_j\), \(i<j\), orthonormal when \(e_1,\ldots,e_7\)
is an orthonormal imaginary basis. Then
\[
\boxed{
\mathcal A_{\rm as}^*\mathcal A_{\rm as}
=\sum_{i<j}D_{e_i,e_j}^*D_{e_i,e_j}
=48P_{\operatorname{Im}\mathbb O}.
}
\tag{AF16}
\]
This sum is independent of the orthonormal basis because it is a
tensor contraction, not a selected multiplication table.

Here is a direct check fixing the constant. In the Cayley basis
of (AF1), each pair generates a quaternion subalgebra. Formula
(AF7) gives zero on its three imaginary basis units and four on
each of the other four. A fixed imaginary basis unit belongs to
nine of the twenty-one pair-generated quaternion subalgebras,
counting the three pairs per quaternion context. The other
twelve contribute four each. The scalar unit contributes zero.
This gives the displayed diagonal operator; basis independence
proves (AF16) in every orthonormal presentation.

Equivalently, normalized \(G_2\) Haar comparison gives
\[
\int_{G_2}D_{gi,gj}^*D_{gi,gj}\,dg
=\frac{16}{7}P_{\operatorname{Im}\mathbb O}.
\tag{AF17}
\]
The average annihilates the unit, commutes with \(G_2\), and is
scalar on its irreducible seven-dimensional imaginary carrier.
Each summand has operator trace sixteen. This is the
[[hessian-response-geometry/response-rigidity-and-multiplicity#A relation that forces the directions together|irreducible-frame argument]]
already used for the
[[exceptional-state-comparison/cyclic-context-retraction-and-response#A complete family has a strict finite lower frame|Albert context response]],
on a different carrier and with a different normalization.
Haar weighting is geometrical comparison, not a claim that
nature samples contexts randomly.

Thus the full multiplication defect detects every non-real
vector, even though any one associative context misses an
entire imaginary three-plane. No preferred quaternion context
is needed for this completed response. The normalized pair
average is \(16/7\), while the unnormalized tensor norm is
forty-eight; these are the same identity, not two predicted
energy scales.

The remaining choices can be exposed exactly. Declaring
\(K=\mathcal A_{\rm as}^*\mathcal A_{\rm as}\) makes a particular
positive operator from this geometry. Declaring instead
\(e^{-t\gamma K}\), for any \(\gamma>0\), preserves the entire
multiplication and comparison structure while changing its
attenuation rate per unit of the independently supplied
parameter \(t\). A law identifying this parameter and generator
with physical translations would have to constrain that choice.

More importantly, a field carrier
\(L^2(X,\mu;\mathbb O)\) with this response acting pointwise
has every \(f(x)\mathbf1\) in its kernel, not just a single
constant vector. The completed internal comparison still
does not see scalar configuration distinctions.
[[global-local-response-reconstruction/exceptional-context-analysis-of-gauge-gradients#Differentiate the representation, not the scalar value|Differentiated context analysis]]
addresses that change of carrier, but introduces a derivative
and a joint law whose coercivity must then be proved. The
constructive question is whether the parent multiplication
can constrain those structures, not merely factor them after
they have been supplied.

### Nonassociativity and complete coverage are different hypotheses

Even with the multiplication, norm and total comparison weight fixed,
nonassociativity alone does not force a uniform response edge. Fix a
Cayley pair \(i,j\), its quaternion context \(H\), and let
\(Q_H=P_{H^\perp}\). Mix its comparison with the normalized complete
comparison:
\[
K_\varepsilon
:=(1-\varepsilon)D_{i,j}^*D_{i,j}
  +\frac{\varepsilon}{21}\mathcal A_{\rm as}^*\mathcal A_{\rm as}
=4(1-\varepsilon)Q_H
  +\frac{16\varepsilon}{7}P_{\operatorname{Im}\mathbb O},
\qquad 0<\varepsilon\le1.
\tag{AF21}
\]
Every one of the twenty-one pair comparisons has strictly positive
weight, and the weights sum to one. Nevertheless the exact spectrum is
\[
\operatorname{spec}K_\varepsilon
=\left\{0^{(1)},\
  \left(\frac{16\varepsilon}{7}\right)^{(3)},\
  \left(4-\frac{12\varepsilon}{7}\right)^{(4)}\right\}.
\tag{AF22}
\]
Indeed \(\mathbb O=\mathbb R\mathbf1\oplus\operatorname{Im}H
\oplus H^\perp\), and the two projections in (AF21) are diagonal on
this splitting. At \(\varepsilon=1\) the positive eigenvalues coincide.
Thus the kernel is exactly the unit line for every positive
\(\varepsilon\), while the edge \(16\varepsilon/7\) tends to zero.
This is not a loss of nonassociativity or a change of octonionic units.
Even \(\operatorname{Tr}K_\varepsilon=16\) stays fixed: the total
response strength has not been rescaled. It is degenerating coverage
of the different associative contexts.

The selected comparison in (AF21) is not \(G_2\)-invariant unless
\(\varepsilon=1\). Consequently this family does not retune the
canonical complete comparison while keeping all its primitive data
fixed. Rather, it identifies a substantive role for such a law:
invariant complete comparison prevents this particular concentration.
A realization claiming an unavoidable scale must establish its
comparison law and uniform coverage, not merely exhibit a nonzero
associator. Even after that finite task, the scalar field kernel and
the unsupplied translation law described above remain separate.

## A retained product can become nonassociative

There is a converse possibility that does not require a
nonassociative ambient algebra. Let \(\mathcal A\) be associative,
let \(E:\mathcal A\to\mathcal A\) be a linear idempotent, and put
\(B=\operatorname{Ran}E\), \(Q_E=I-E\). For \(x,y\in B\), define
\(x\star y=E(xy)\). Then for \(x,y,z\in B\),
\[
\boxed{
(x\star y)\star z-x\star(y\star z)
=E\!\left[xQ_E(yz)-Q_E(xy)z\right].
}
\tag{AF12}
\]
Indeed, insert \(E=I-Q_E\) in the two inner products and cancel
\((xy)z=x(yz)\) in the ambient algebra. The discrepancy is exactly
the difference between two discarded intermediate channels.
The retained binary product can forget data needed to predict a
triple product even though the whole multiplication is associative.

If \(B\) is an associative subalgebra, both discarded terms vanish
for inputs in \(B\). In particular, a conditional expectation onto
a subalgebra does **not** create a nonassociative retained product.
Likewise, representing observables by compressed operators can
fail to preserve multiplication while operator composition
itself remains associative. These are different defects.

For an explicit nonassociative retained product, take
\[
E(A)=\tfrac12(A+A^{\mathsf T}),\qquad A\in M_2(\mathbb C).
\tag{AF13}
\]
This is positive, unital, trace-preserving and idempotent: transpose
preserves the positive cone and squares to the identity.
Its range is the complex symmetric matrices, and there
\(a\star b=(ab+ba)/2=:a\circ b\).
Expanding four ambient products gives
\[
(a\circ b)\circ c-a\circ(b\circ c)
=\tfrac14[b,[a,c]].
\tag{AF14}
\]
For \(a=b=\sigma_z\), \(c=\sigma_x\), the result is \(\sigma_x\):
\(a\circ a=I\) while \(a\circ c=0\).

The map (AF13) is not completely positive. Its Choi matrix is
\(\tfrac12|\Omega\rangle\langle\Omega|+\tfrac12\mathsf F\),
where \(\Omega=|00\rangle+|11\rangle\) and \(\mathsf F\) swaps
the two tensor factors. It has eigenvalue \(-1/2\) on the
antisymmetric vector. Thus this example must not be substituted
for the completely positive conditional expectations elsewhere
in the programme. Nor does it realize the exceptional Albert
product as a matrix Jordan subalgebra.

### Idempotent completely positive readout restores associativity

There is a stronger restriction than the subalgebra case above.
If \(E\) is a unital completely positive idempotent on a unital
\(C^*\)-algebra, its retained product \(x\star y=E(xy)\) is
associative even when its range is not an ambient subalgebra.
This is the associativity part of the Choi–Effros result;
[[library/on-the-choi-effros-multiplication/inq|Prunaru]]
gives a short proof of the general range theorem.
Here the unital associativity mechanism can be checked directly.

For \(z=E(z)\), the Schwarz defect
\(D_z=E(z^*z)-z^*z\) is positive and \(E(D_z)=0\).
Since \(0\le D_z^2\le\|D_z\|D_z\), also \(E(D_z^2)=0\).
Apply complete positivity to the two-by-two Gram matrix of
\((D_z,a)\). Its image has zero upper-left corner, hence zero
off-diagonal entries: \(E(D_za)=E(aD_z)=0\) for every \(a\).
Polarization writes \(E(xy)-xy\), for fixed \(x,y\), as a
linear combination of such \(D_z\). Therefore
\[
\boxed{E(E(xy)z)=E(xyz)=E(xE(yz)),
\qquad x,y,z\in\operatorname{Ran}E.}
\tag{AF20}
\]
This proves associativity without a faithful state assumption.

If \(E\) additionally preserves a faithful state \(\omega\),
then \(\omega(D_z)=0\) already forces \(D_z=0\).
Polarization now gives \(E(xy)=xy\): the range is an ordinary
associative subalgebra. This is the same positive-defect
mechanism used in [[faithful-descent-rigidity-and-noiseless-unitarity|faithful descent rigidity]],
but it concerns the product rather than a returned clock.

Thus nonassociative parent data cannot be supplied merely by
renaming this idempotent completely positive readout.
The parent product, a non-idempotent or history-dependent
comparison, or a different positivity structure would need to
carry the extra law. None of these alternatives is forced by
forgetting alone, and this restriction does not exclude them.

### From a product defect to an actual response

Equation (AF12) contains no chosen norm, time parameter or lower
bound. It supplies a candidate location for nonassociativity:
the operation of retaining a binary product. To obtain a
scale-selecting obstruction, a construction would need to
constrain those discarded channels and compare their response
with the complete relevant carrier. In
[[gauge-source-action-transport/source-action-transport-through-ordered-cuts|the current source-cut programme]],
the cut maps still compose associatively. Their transformation
law has not been identified with the projected product above.

[[coarse-response-memory/boundary-interaction-and-conditional-score-budget#The exact defect is differentiation against forgetting|The actual regional-vacuum construction]]
now supplies a different positive defect:
\(\mathcal C_A=\nabla_AP_A-P_A\nabla_A\) satisfies
\(\mathcal C_A\mathcal C_A^*=4M_A\), where \(M_A\) is the
conditional score covariance on regional tangent fibers.
Its retained function product remains associative. An exceptional
parent proposal would need an explicit compatibility map between
its multiplication defect and this differentiation–forgetting
response; resemblance of positive squares does not supply one.

There is now an exact intermediate bridge:
[[global-local-response-reconstruction/exceptional-context-analysis-of-gauge-gradients#Two comparisons, with different laws|exceptional tangent analysis]]
represents this actual defect as \(T_A\mathcal C_A\), with a
fixed norm factor on its declared carrier. It works for every
admissible state and therefore does not select the response.
To make multiplication constrain scale, choose a comparison
operation from the exceptional product first, then prove that
one state-and-carrier realization intertwines its readout defect
with \(\mathcal C_A\) across the chosen cuts. Defining that
operation afterward by transporting \(\nabla_A\), or by fitting
\(M_A^{1/2}\), would only repackage the supplied dynamics.

## Contextwise products need a genuine gluing defect

There is an exact obstruction to making every quaternion
context an ordinary multiplicative description in one
associative algebra. Suppose each quaternion subalgebra
\(H\subset\mathbb O\) has a unital real-algebra map
\(J_H:H\to\mathcal B\), where \(\mathcal B\) is one nonzero
associative real algebra, and the maps agree on intersections.
They define one unital real-linear map \(J:\mathbb O\to\mathcal B\).
Every two octonions belong to a common quaternion subalgebra,
so \(J(ab)=J(a)J(b)\) for every pair.

Associativity in \(\mathcal B\) would then give
\(J([i,j,\ell])=0\). But (AF1) gives
\([i,j,\ell]=2k\ell\) and \((2k\ell)^2=-4\mathbf1\).
Multiplicativity would force \(0=-4\mathbf1_{\mathcal B}\),
a contradiction. Thus exactly agreeing multiplicative
context maps of this kind do not exist. This does not
exclude Jordan realizations, nonmultiplicative readouts
or distinct local carriers with specified transition data.

For a unital real-linear realization \(J\), its product defect
\(\Delta(a,b)=J(ab)-J(a)J(b)\) necessarily satisfies
\[
\boxed{
J([a,b,c])=\Delta(ab,c)-\Delta(a,bc)
+\Delta(a,b)J(c)-J(a)\Delta(b,c).
}
\tag{AF19}
\]
Expand the four terms and cancel associative operator
products to prove this identity. It is not a nonassociative
composition law for the operators themselves.

This exposes a discriminating construction test: determine
the defect from the actual source/readout comparisons first,
then seek a common \(J\) satisfying (AF19) across overlapping
contexts. Defining \(\Delta\) afterward by the displayed
difference makes the identity tautological and selects
neither the source state nor its dynamics.

Pairwise positivity alone cannot do this. Every
[[coarse-response-memory/positive-amplitude-kernel-and-preparation|prepared positive-feature kernel]]
already admits \(F_S(x)=f_S(x)\mathbf1\in\mathbb O\), with
\(P(x,y)=\mathbb E\,\operatorname{Re}(\overline{F_S(x)}F_S(y))\).
All its multiplication associators vanish. The
[[coarse-response-memory/replica-weighted-correlations-and-the-local-readout|overlap and posterior weights]]
can therefore be represented inside octonions without being
constrained by nonassociativity at all. A genuine parent law
must constrain products across contexts, not merely provide
another Gram factorization of the supplied joint state.

## Keep the label, or discard it

To formulate an ordinary quantum channel, now **supply** the complex Hilbert carrier
\[
\mathcal K=\mathbb O\otimes_{\mathbb R}\mathbb C\cong\mathbb C^8
\tag{AF8}
\]
with the Hermitian extension of the Euclidean metric. Extend \(U,V,P,Q,R\) complex-linearly. The two summands each have complex dimension four. This complexification is a declared realization, not a complex scalar structure derived from the selected octonionic units.

Supply also a two-dimensional label carrier with orthonormal vectors \(|0\rangle,|1\rangle\). The equal-weight map
\[
\Psi:\mathcal K\longrightarrow\mathbb C^2\otimes\mathcal K,
\qquad
\Psi\xi=\frac{|0\rangle\otimes U\xi+|1\rangle\otimes V\xi}{\sqrt2}
\tag{AF9}
\]
is isometric, since
\[
\Psi^*\Psi=\tfrac12(U^*U+V^*V)=I.
\]
The input is recoverable on the image if the complete label-system state is retained. This is not yet a law for persistent historical records: [[local-global-individuation|the record criterion]] requires compatible proper extensions and an admissible process order.

For a density matrix \(\rho\) on \(\mathcal K\), discard the label by partial trace. Equations (AF6) and (AF9) give
\[
\begin{aligned}
\Phi(\rho)
&:=\operatorname{Tr}_{\rm label}(\Psi\rho\Psi^*)\\
&=\tfrac12(U\rho U^*+V\rho V^*)
=U\,E_R(\rho)\,U^*,\\
E_R(T)&:=\tfrac12(T+RTR)=PTP+QTQ.
\end{aligned}
\tag{AF10}
\]
The relative channel \(E_R\) is unital, trace-preserving, completely positive and idempotent. Its range is
\[
B(P\mathcal K)\oplus B(Q\mathcal K)
\cong M_4(\mathbb C)\oplus M_4(\mathbb C).
\tag{AF11}
\]
It kills exactly the off-diagonal operator blocks \(PTQ+QTP\). Thus \(E_R\), and likewise \(\Phi\), is not invertible on the full operator carrier. The genuine loss occurs at this explicitly typed readout, not in either multiplication branch.

The equal amplitudes in (AF9), the label inner product, the state calculus and the partial-trace prescription are inputs. This construction does not derive the Born rule from nonassociativity or postulate ontic randomness. Unequal normalized branch weights would give a different channel and need not produce the idempotent projection in (AF10).

## Distinct responses, not a vacuum or spacetime

The response \(D^*D\) acts on vectors. Its kernel is four-dimensional over \(\mathbb R\) before complexification, and four-dimensional over \(\mathbb C\) afterward. The channel acts on operators and retains both entire diagonal matrix blocks. In particular, a state wholly supported on \(Q\mathcal K\) has zero channel loss even though every nonzero vector there has positive associator response. These are not interchangeable loss functionals.

Even the completed family does not identify these two carriers.
Every \(R_g=2P_{g\mathbb H}-I\) preserves
\(\mathbb C\mathbf1\oplus(\operatorname{Im}\mathbb O)_{\mathbb C}\).
Consequently its relative branch-erasure channel fixes
the nonzero traceless matrix
\[
7P_{\mathbb C\mathbf1}
-P_{(\operatorname{Im}\mathbb O)_{\mathbb C}}.
\tag{AF18}
\]
This is an undetected matrix-state direction despite the
one-dimensional vector kernel in (AF16).

The finite number \(4\) in (AF7) follows from the selected unit normalization and the sign difference between the two branches. Completing the family gives an exact coercive vector comparison modulo the unit line, not a physical vacuum identification, energy unit or translation generator. A nonzero eigenvalue of either finite response is not a mass-gap derivation.

Nor is \(R\) a selected Lorentzian reflection. It has four positive and four negative real directions. The real bilinear form \(\langle x,Ry\rangle\) has signature \((4,4)\), not \((3,1)\) or \((1,3)\). [[algebra/directed-response-and-lorentzian-signature|Directed-response reflection]] instead uses a rank-one negative line. Selecting that line, a four-dimensional realized carrier or a Wick continuation would require additional data and a theorem. The [[general-causal-action/directed-realization-and-foundational-restart|foundational restart]] asks precisely for a common law that constrains those additional choices.

The constructive return is narrower and exact: nonassociativity can supply a distinguishable pair of reversible operations, their positive discrepancy, and a concrete labelled realization whose subsequent coarse readout forgets specified coherences. It supplies material for a process law without already being that law.

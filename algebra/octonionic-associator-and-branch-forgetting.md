# Octonionic Associators and Branch Forgetting

Two parenthesizations of octonionic multiplication can give different, individually reversible operators. For a selected quaternion subalgebra, their exact discrepancy is a positive response supported on its orthogonal complement. Retaining the parenthesization label preserves the input; discarding that label produces a genuinely noninvertible matrix channel. This separates an algebraic source of distinguishability from an operation that forgets distinctions, without identifying either with chronology or a mass gap.

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
The associator thus supplies an exact positive response: it detects precisely the components outside the selected associative context. Neither branch is irreversible, despite their nonzero discrepancy. More generally, \(L_{ab}-L_aL_b\) retains the original nonassociative multiplication as a defect inside an associative endomorphism algebra. This is compatible with the [[exceptional-context-response|exceptional regular realization]], where injectivity and positivity of a linear realization do not imply preservation of the original product.

The result is presentation-covariant. An octonion automorphism \(g\in G_2\) sends the selected units and quaternion subalgebra to \(gi,gj,g\mathbb H\), and \(L_{ga}=gL_ag^{-1}\). Its response is consequently \(g(4Q)g^{-1}\). This covariance does not privilege any one context.

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

The finite number \(4\) in (AF7) follows from the selected unit normalization and the sign difference between the two branches. There is no Hamiltonian, unique vacuum, physical energy unit or vacuum-complement coercivity theorem here. A nonzero eigenvalue of this response is not a mass-gap derivation.

Nor is \(R\) a selected Lorentzian reflection. It has four positive and four negative real directions. The real bilinear form \(\langle x,Ry\rangle\) has signature \((4,4)\), not \((3,1)\) or \((1,3)\). [[algebra/directed-response-and-lorentzian-signature|Directed-response reflection]] instead uses a rank-one negative line. Selecting that line, a four-dimensional realized carrier or a Wick continuation would require additional data and a theorem. The [[contemporary-puzzles/yang-mills-mass-gap/directed-realization-and-foundational-restart|foundational restart]] asks precisely for a common law that constrains those additional choices.

The constructive return is narrower and exact: nonassociativity can supply a distinguishable pair of reversible operations, their positive discrepancy, and a concrete labelled realization whose subsequent coarse readout forgets specified coherences. It supplies material for a process law without already being that law.

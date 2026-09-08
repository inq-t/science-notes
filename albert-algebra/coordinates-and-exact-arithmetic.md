# Coordinates and Exact Arithmetic

The Albert multiplication calculations use one explicit octonion table and one ordered Hermitian basis. Keeping these coordinates separate from any particular constraint or response certificate makes the common algebra reproducible. Integral products refer to twice the Jordan product; Euclidean orthonormalization requires the trace metric and changes the numerical multipliers.

The [[albert-algebra/coordinates.py|coordinate implementation]] labels the octonion unit by 0 and its seven imaginary units by 1 through 7. Its oriented Fano triples are
\[
(1,2,3),\ (1,4,5),\ (1,7,6),\ (2,4,6),\quad
(2,5,7),\ (3,4,7),\ (3,6,5).
\]
Each triple gives the cyclic products; reversing a pair reverses the sign. Every imaginary unit squares to \(-1\), and conjugation negates the seven imaginary components.

The 27 real coordinates are the three diagonal entries followed by the eight octonion components of the upper-triangular entries \((0,1),(0,2),(1,2)\). The lower-triangular entries are their octonion conjugates. For this ordered basis \((b_i)\),
\[
\operatorname{tr}_J(b_i\circ b_j)=n_i\delta_{ij},\qquad
(n_1,\ldots,n_{27})=(1,1,1,2,\ldots,2).
\]
The function `jordan_product_twice` evaluates \(xy+yx=2(x\circ y)\) in those coordinates with integer arithmetic. It does not form an unparenthesized triple octonion product. A trace-orthonormal real basis is \(e_i=b_i/\sqrt{n_i}\); a regular multiplier matrix must be transformed on its input and output coordinates as well as scaled in its argument.

The complex context chooses \(\operatorname{span}_{\mathbb R}(1,e_1)\subset\mathbb O\) in every off-diagonal entry. Its nine coordinate directions are the three diagonals and those two components in each of the three entries; the other eighteen form its trace-orthogonal complement. These are declared coordinates for one standard context, not a measure selecting physical contexts.

Exact certificates built from this table remain conditional on this explicit realization of the Albert algebra. A modular rank is a lower bound on rational rank, while an integer annihilating polynomial constrains an operator's spectrum only together with its declared metric and self-adjointness. Stored numerical output alone does not supply either theorem.

# Oriented Gram Descent and Invariant Coverage

Pairwise inner products determine a configuration only up to an orthogonal transformation; they can forget orientation when the actual equivalence group contains only rotations. This gives an exact gauge-theory counterexample to identifying autonomous spectral readout with complete observable coverage. For four quaternionic links, every pairwise trace and its full electric evolution can be retained while an entire gauge-invariant orientation sector is omitted. The missing sector has an inherited weighted carrier and a computable electric threshold; its orientation is constrained by the determinant, not appended as an independent binary variable.

**Status: [EXACT FINITE CONSTRUCTION] for the orbit separation, carrier decomposition and supplied electric clock below.** The invariant-theory mechanism is elementary; no claim of a new general invariant theorem, fundamental chirality, or a four-dimensional Yang--Mills gap is made.

## A Gram quotient can enlarge the equivalence group

Let \(V:\mathbb R^n\to\mathbb R^d\) have columns \(v_i\), and set
\[
G=V^{\mathsf T}V,\qquad G_{ij}=v_i\cdot v_j.
\tag{OG1}
\]
Equal Gram matrices determine an isometry between the column spans:
\(Vc\mapsto Wc\) is well-defined because their kernels and pairings
agree. Extend that isometry to the orthogonal complements. Thus Gram
data classify configurations up to \(O(d)\).

If the intended equivalences are \(SO(d)\), two cases differ. When
\(\operatorname{rank}V<d\), an orientation-reversing extension can be
corrected by a reflection fixing the target column span. The
\(O(d)\)-orbit is then already one \(SO(d)\)-orbit. At rank \(d\),
there are exactly two \(SO(d)\)-orbits within each Gram fibre.

For \(n=d\), the missing invariant is
\[
\tau=\det V,\qquad \boxed{\tau^2=\det G.}
\tag{OG2}
\]
The pair \((G,\tau)\) separates the rotation orbits. Above positive
definite \(G\) there are two orientation choices; on the rank wall
\(\det G=0\) they coincide. Only the full-rank fibres are two-element
torsors. This is not a free two-element action at every configuration,
and the sign is not independent of the magnitude or rank.

## Four links make the missing observable physical

Take four oriented parallel paths \(u_0,u_1,u_2,u_3\) between two
vertices, with \(u_e\in SU(2)\), normalized product Haar law and full
endpoint gauge action
\[
u_e\longmapsto k u_e\ell^{-1}.
\tag{OG3}
\]
Each path may be subdivided; its supplied electric weight is the sum
of its segment weights as in
[[gauge-boundary-frame-gluing/holonomy-refinement-and-clock-compatibility|holonomy refinement]].

Write \(u_e=(w_e,v_e)\) in unit-quaternion coordinates, with matrix
convention \(u_e=w_eI-i v_e\cdot\sigma\). The two endpoint groups act
as all rotations of \(\mathbb R^4\): their six independent left/right
infinitesimal quaternion rotations span \(\mathfrak{so}(4)\), and their
connected image is \(SO(4)\). Consequently the six pairings
\[
s_{ef}=\tfrac12\operatorname{Tr}(u_eu_f^{-1})
      =u_e\cdot u_f,\qquad e<f,
\tag{OG4}
\]
retain the \(O(4)\) orbit, not the whole endpoint-gauge orbit.

Tree reduction sets \(u_0\) to the identity and gives three based
holonomies \(x_i=u_i u_0^{-1}=(a_i,v_i')\). This is the three-loop
extension of
[[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|the induced theta-loop carrier]].
The physical space becomes \(L^2(SU(2)^3)^{\operatorname{Ad}SU(2)}\).
Single traces fix \(a_i\); relative pair traces fix \(v_i'\cdot v_j'\).
The remaining gauge action is \(SO(3)\), whereas this reduced Gram
information also identifies mirror configurations.

Right multiplication by \(u_0^{-1}\) is an orientation-preserving
orthogonal map sending the first quaternion to \((1,0,0,0)\).
Therefore the actual missing observable is
\[
\boxed{
\tau=\det\begin{pmatrix}u_0\\u_1\\u_2\\u_3\end{pmatrix}
=\det(v_1',v_2',v_3').}
\tag{OG5}
\]
It is the invariant determinant already used in
[[gauge-boundary-frame-gluing/path-shift-fisher-geometry-before-gauge-projection#The choice of handed action remains visible|the three-holonomy response test]],
now identified as missing orbit data.

For example, based vector triples \((e_1,e_2,e_3)\) and
\((-e_1,-e_2,-e_3)\), with all \(a_i=0\), have identical single and
pair traces and opposite \(\tau\). With the stated matrix convention,
\[
\operatorname{Tr}(x_1x_2x_3)
-\operatorname{Tr}(x_1x_3x_2)=-4\tau.
\tag{OG6}
\]
Thus the distinction is already encoded by invariant loop-word
multiplication. Pairings retain the metric tensor; ordered multiplication
also retains the alternating tensor. This is an actual difference of
observable algebras, not merely a choice of basis.

## A proper observable quotient can have perfect clock closure

Let \(\Theta\) pull functions back by a common fixed reflection of
the raw \(\mathbb R^4\) quaternion coordinates. It preserves product
Haar, normalizes \(SO(4)\), and acts on the physical Hilbert space.
Modulo rotations, it is the same nontrivial orientation exchange
as simultaneous inversion of the three based holonomies.

The physical carrier decomposes orthogonally as
\[
\mathcal H_{\mathrm{phys}}=\mathcal H_+\oplus\mathcal H_-,
\qquad \Theta|_{\mathcal H_\pm}=\pm I.
\tag{OG7}
\]
The full measurable algebra of pairwise traces has \(L^2\) closure
exactly \(\mathcal H_+\). The rank-deficient set is Haar-null; it is
the zero set of a nonzero analytic determinant. In particular
\(\tau\in\mathcal H_-\) is nonzero.

Now supply the ordinary electric law
\[
H_0=\sum_{e=0}^3\alpha_eD_{Q,e},\qquad
Q=-2\operatorname{Tr},\quad \alpha_e>0.
\tag{OG8}
\]
Each \(D_Q\) is one quarter of the round unit-\(S^3\) Laplacian.
Hence it commutes with every orthogonal map of the quaternion
coordinates, including the common reflection. Both sectors in (OG7)
reduce \(H_0\), with their inherited invariant \(H^2\) domains and
\(H^1\) form domains.

All heat, unitary, resolvent and spectral readouts starting in
\(\mathcal H_+\) therefore remain there. Their minimal spectral
dilation is \(\mathcal H_+\) itself and cannot reconstruct \(\tau\).
This is a concrete instance of the
[[coarse-response-memory/spectral-readout-and-the-visible-gap#Covering the actual excitation carrier is a separate requirement|separate coverage obligation]]:
perfect all-duration clock compatibility does not certify that the
declared observables cover the intended physical algebra.

Adding any bounded real potential that is a function of the pairwise
traces preserves this even/odd splitting. Its positive ground state
is even, by uniqueness. It does not follow that an arbitrary lattice
interaction or arbitrary effective response has this reflection symmetry.

## The lowest odd excitation is fixed by the supplied edge law

Let \(P_e\) average the \(e\)-th raw link over Haar. It commutes with
the endpoint gauge action and common reflection. If \(F\) is odd and
physical, \(P_eF\) is an odd physical function of the remaining three
quaternions. But three vectors in \(\mathbb R^4\) have rank at most
three, so their \(SO(4)\) and \(O(4)\) orbits coincide by (OG1).
There are no nonzero odd invariant functions of those three vectors.
Thus
\[
P_eF=0\quad\hbox{for every }e,\qquad F\in\mathcal H_-.
\tag{OG9}
\]
The first nonconstant \(D_Q\) eigenvalue is \(3/4\). Its spectral
Poincare inequality on each link gives, as closed forms,
\[
H_0|_{\mathcal H_-}\ge
E_-\ I,\qquad E_-=\tfrac34\sum_{e=0}^3\alpha_e.
\tag{OG10}
\]
The determinant in (OG5) is linear in every raw quaternion. Each
link therefore contributes exactly its first spherical eigenvalue:
\[
H_0\tau=E_-\tau,\qquad
\|\tau\|_{\mathrm{Haar}}^2=\frac{4!}{4^4}=\frac3{32}.
\tag{OG11}
\]
The norm follows by expanding the determinant and using
\(\mathbb E(u_e^a u_e^b)=\delta_{ab}/4\) independently for every row.
Thus (OG10) is the exact bottom of the odd sector, not only a trial
energy.
Its minimizing eigenspace is exactly \(\mathbb C\tau\). Equality forces
every link into its coordinate harmonic. A reflection-odd invariant
multilinear four-tensor is proportional to the alternating tensor:
coordinate reflections require each index to occur once, and coordinate
permutations fix the alternating signs.

This does not make \(E_-\) the full physical gap. The weighted
cycle theorem gives the whole electric gap
\(\tfrac34\min_{e<f}(\alpha_e+\alpha_f)\), attained by an even
two-path character. The omitted sector is physically nonempty, but
its omission does not change that particular lowest numerical gap.

## The rank wall returns a weighted odd carrier

Let \(\mathcal G=(s_{ef})_{e,f=0}^3\), with \(s_{ee}=1\), be the raw
Gram matrix, let \(\nu\) be its Haar pushforward, and set
\(d(\mathcal G)=\det\mathcal G\). On the full-rank set every physical
measurable function has a unique decomposition
\[
F=A(\mathcal G)+\tau B(\mathcal G),\qquad
\|F\|^2=
\int\left(|A|^2+d(\mathcal G)|B|^2\right)d\nu.
\tag{OG12}
\]
Reflection symmetry cancels the cross term. Therefore the missing
coefficient lives in \(L^2(d\,d\nu)\), not generally \(L^2(d\nu)\).
The same conclusion holds for any smooth positive
reflection-invariant reweighting, with its actual Gram pushforward.

Multiplication \(M_\tau B=\tau B\) is a unitary map from this weighted
coefficient space onto the full odd sector. It transports the closed
operator
\[
K_-:=M_\tau^{-1}(H_0|_{\mathcal H_-}-E_-)M_\tau\ge0
\tag{OG13}
\]
and its domain without choosing an independent odd clock:
\[
D(K_-)=\{B:\tau B\in D(H_0)\cap\mathcal H_-\}.
\tag{OG13a}
\]
The form domain uses the inherited \(H^1\) domain in the same way.
Its kernel consists exactly of constant coefficients. For smooth
Gram functions \(B\), integration by parts using (OG11) gives
\[
\langle \tau B,(H_0-E_-)\tau B\rangle
=\int \tau^2\sum_e\alpha_e|\nabla_e B(\mathcal G)|_Q^2\,d\mu_H.
\tag{OG14}
\]

## Polynomial coefficients fix the inherited realization

The rank wall does not prevent an explicit operator and form core.
For each unordered pair \(i<j\), let \(\partial_{ij}\) denote
differentiation in the independent coordinate \(s_{ij}\), with
\(\partial_{ji}=\partial_{ij}\) and \(s_{jj}=1\). On Gram polynomials,
the inherited operator in (OG13) is
\[
\boxed{
K_-p=\frac14\sum_{i=0}^3\alpha_i
\left[
5\sum_{j\ne i}s_{ij}\partial_{ij}p
-\sum_{j,k\ne i}
(s_{jk}-s_{ij}s_{ik})\partial_{ij}\partial_{ik}p
\right].}
\tag{OG15}
\]
The second sum is over ordered \(j,k\); mixed derivatives are
therefore counted with their usual two cross terms. In particular
\(K_-s_{ij}=\frac54(\alpha_i+\alpha_j)s_{ij}\).
The drift coefficient five is derived from the same determinant and
edge law, not selected separately for the odd sector.

To prove (OG15) without dividing a smooth function by a vanishing
determinant, let \(c_i\) be the Euclidean cofactor vector of row \(u_i\)
in (OG5). Then \(c_i\cdot u_j=\delta_{ij}\tau\). Tangential projection
on the unit sphere gives, for \(j,k\ne i\),
\[
\begin{aligned}
\Gamma_{Q,i}(\tau,s_{ij})&=-\tfrac14\tau s_{ij},\\
\Gamma_{Q,i}(s_{ij},s_{ik})&=\tfrac14(s_{jk}-s_{ij}s_{ik}),\\
\Delta_{Q,i}s_{ij}&=-\tfrac34s_{ij}.
\end{aligned}
\tag{OG16}
\]
Here \(\Gamma_{Q,i}\) is the \(Q\)-gradient pairing, one quarter of
the unit-sphere gradient pairing. The product rule and
\(H_0\tau=E_-\tau\) yield
\((H_0-E_-)(\tau p)=\tau K_-p\), with (OG15).
These are polynomial identities on the raw spheres, including
\(\tau=0\); no smooth-division assertion at the rank wall is used.

Let \(\mathscr P_N\) be the restrictions to the compact Gram space
of polynomials in its six independent entries of degree at most \(N\),
viewed in \(L^2(d\,d\nu)\). Their union is dense: coordinate
polynomials separate the points of this compact space and contain
constants, so Stone--Weierstrass gives uniform density in continuous
functions, hence density for this finite Borel measure. Each
\(\mathscr P_N\) is finite-dimensional, belongs to \(D(K_-)\) because
\(\tau p\) is raw-smooth, and is invariant under (OG15).

Let \(\Pi_N\) be its orthogonal projection. Invariance and
self-adjointness imply reduction, including the operator domain.
Indeed \(\Pi_NB\in D(K_-)\) for every \(B\), and for
\(B\in D(K_-)\), testing against any \(p\in\mathscr P_N\) gives
\[
\langle p,\Pi_NK_-B\rangle
=\langle K_-p,B\rangle
=\langle K_-p,\Pi_NB\rangle
=\langle p,K_-\Pi_NB\rangle.
\tag{OG17}
\]
Thus \(K_-\Pi_NB=\Pi_NK_-B\). Since \(\Pi_N\to I\) strongly,
\(\Pi_NB\to B\) in the graph norm for every \(B\in D(K_-)\).
The same reducing projections commute with \(K_-^{1/2}\), giving
form-norm convergence for every \(B\in D(K_-^{1/2})\). Consequently
\[
\boxed{
\bigcup_N\mathscr P_N\ \text{is an operator and form core of }K_-;
\qquad
\{\tau p(\mathcal G):p\text{ polynomial}\}
\ \text{is an operator and form core of }H_0|_{\mathcal H_-}.}
\tag{OG18}
\]
The bounded shift \(E_-\) does not change these core properties.
Equivalently, the polynomial restriction (OG15) is essentially
self-adjoint, and the closure of (OG14) on polynomial coefficients
is exactly the inherited odd form. Ambient smooth Gram functions
also constitute a core because they contain these polynomials and
their raw lifts lie in the inherited domains.

This uses the same finite-dimensional polynomial approximation
mechanism as
[[purification-descent-and-the-matrix-response#Exact polynomial spectrum|the sphere-to-matrix realization]],
but does not require each degree layer here to have a single
eigenvalue. It also does not identify the inherited domain with a
maximal weighted Sobolev space. Coefficients may still have
rank-wall behavior not expressible by smooth division; arbitrary
boundary conditions cannot be appended to the polynomial
realization just proved.

## What the result changes in the programme

A proposed context law must preserve more than positive pairings and
compatible clocks. It must account for the invariant contractions of
the declared multiplication, and prove coverage by its returned
observables. Otherwise an apparently successful quotient can silently
replace the actual equivalence group by a larger one.

The orientation is supplied by the quaternionic invariant algebra;
no preferred handed state or irreversible temporal arrow has been
derived. The scale in (OG10) still comes from the supplied edge law.
[[gauge-boundary-frame-gluing/oriented-context-gluing-and-mixed-response|The further-context test]]
now proves that complete regional orientation still leaves a relative
interface rotation when only two independent links are shared.
Its mixed response recovers the missing cross-pairings, while
response-generated row replacement recovers all alternating minors
without dividing by a rank determinant. The resulting algebra is a
core of the supplied whole electric operator; the law selecting that
shared response remains open.

[[gauge-boundary-frame-gluing/receipts/overlapping_plaquette_transfer_receipt.py|The overlapping-holonomy receipt]]
checks the actual quaternion determinant, four-link Pauli derivatives,
Haar norm and reflection covariance. It supports those finite
identities; the coverage and closed-domain conclusions use the
arguments above, not numerical eigenvalue fitting.

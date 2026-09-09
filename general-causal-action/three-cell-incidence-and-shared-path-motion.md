# Three-Cell Incidence and Shared Path Motion

Three adjacent square cells have two different shared edges and two connecting bridges. Their complete electric response contains both nearest-cell mixed motion and a bridge that rotates a later loop relative to an earlier one. A change of words turns the current common-parent construction into the correct four-path part, but leaves two explicit bridge rows missing. Separate plaquette traces detect the missing middle-cell rate; an angular source detects why adding a middle-loop Casimir alone still fails. This is an exact finite incidence test for the next preparation law.

**Status: exact reduction of a supplied equal-link electric operator, and exact comparisons with the specified common-parent member.** The raw graph and its coefficient are declared. The calculation preserves the full physical carrier, supplies no uniform field gap, and does not exclude all conceivable word transformations or preparation laws. [[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|The induced-clock owner]] supplies the general tree-reduction method; [[conditional-access-families-and-the-returned-clock|conditional access families]] supplies the comparison being tested.

## The chain has two different shared edges

Start with three adjacent unit square plaquettes in one row. There are ten distinct links and eight vertices. Give every link the electric coefficient \(\kappa>0\), with \(D_Q=-\Delta_Q\) for a fixed bi-invariant metric on a compact connected group \(G\). Collapse only the bivalent outer corners, retaining their ordered path products. The additive path theorem in [[holonomy-state-refinement/holonomy-refinement-and-clock-compatibility|holonomy refinement]] gives six paths on four remaining vertices:

| Path | Direction | Number of original links | Electric weight |
|---|---|---:|---:|
| \(p\) | \(v_0\to v_1\) | 1 | \(\kappa\) |
| \(u\) | \(v_0\to v_1\) around the left exterior | 3 | \(3\kappa\) |
| \(q\) | \(v_2\to v_3\) | 1 | \(\kappa\) |
| \(v\) | \(v_2\to v_3\) around the right exterior | 3 | \(3\kappa\) |
| \(a\) | \(v_0\to v_2\), upper bridge | 1 | \(\kappa\) |
| \(b\) | \(v_1\to v_3\), lower bridge | 1 | \(\kappa\) |

Thus \(p,q\) are the two distinct shared vertical edges, while \(a,b\) are the upper and lower edges of the middle cell. On the six-path carrier the supplied operator is
\[
H_{\rm raw}=\kappa(D_p+D_q+D_a+D_b+3D_u+3D_v).
\tag{TC1}
\]
Every path transforms as \(g_e\mapsto h_{s(e)}g_eh_{t(e)}^{-1}\). The path compression here proves equality of this electric operator on the bivalent-Gauss carrier. It does not identify freshly chosen finite-width Gaussian kernels or reset their marked preparations.

Use the tree \(p,a,q\), rooted at \(v_0\). The three actual based cell words are
\[
\boxed{x=up^{-1},\qquad
y=a q b^{-1}p^{-1},\qquad
z=a v q^{-1}a^{-1}.}
\tag{TC2}
\]
The right cell is transported to the root through \(a\). Omitting that transport would put its Lie-algebra derivatives in the wrong frame. The orientations in (TC2) make the first shared-edge contribution have the same sign in \(x,y\), and the second have opposite signs in \(y,z\); reversing a cell word transports these signs with its observables.

Choosing \(h_0=I\), \(h_1=p\), \(h_2=a\), \(h_3=aq\) puts all three tree paths at the identity. The remaining coordinates are \(u=x\), \(b=y^{-1}\), \(v=z\). More generally the inverse coordinate map is
\[
u=xp,\qquad b=p^{-1}y^{-1}aq,\qquad v=a^{-1}zaq.
\tag{TC3}
\]
Iterated Haar invariance proves that the joint measure is product Haar in \((p,a,q,x,y,z)\). The tree gauge acts transitively on the tree fibers, and the remaining root action conjugates \(x,y,z\) simultaneously. The full physical carrier is consequently
\[
\boxed{\mathcal H_{\rm phys}=L^2(G^3,dx\,dy\,dz)^{\operatorname{Ad}G}.}
\tag{TC4}
\]
This is not the product of three one-cell class-function spaces. For \(SU(2)\), three scalar traces and three vector pairings still leave an orientation distinction; [[algebra/oriented-gram-descent-and-invariant-coverage|oriented Gram coverage]] owns the additional triple determinant and its relation to ordered traces. All formulas below act on the entire carrier (TC4).

## Differentiate the words before discarding their frames

For \(X\in\mathfrak g\), define
\[
L_{x,X}F=\left.\frac{d}{dt}F(e^{tX}x,y,z)\right|_0,
\qquad
R_{x,X}F=\left.\frac{d}{dt}F(xe^{tX},y,z)\right|_0,
\qquad C_x=L_x-R_x,
\tag{TC5}
\]
with the analogous fields on the other factors. A Lie-algebra-valued row norm means the sum of squared derivatives over a \(Q\)-orthonormal basis \(e_A\). On invariant functions \((C_x+C_y+C_z)F=0\), but the individual conjugation rows need not vanish.

Apply left multiplication \(g_e\mapsto e^{tX}g_e\) to one raw path in (TC2). Direct differentiation gives:

| Varied path | Induced derivative on \(F(x,y,z)\) |
|---|---|
| \(u\) | \(L_{x,X}\) |
| \(v\) | \(L_{z,\operatorname{Ad}_aX}\) |
| \(p\) | \(-R_{x,X}-R_{y,X}\) |
| \(q\) | \(L_{y,\operatorname{Ad}_aX}-R_{z,\operatorname{Ad}_aX}\) |
| \(a\) | \(L_{y,X}+C_{z,X}\) |
| \(b\) | \(-R_{y,\operatorname{Ad}_pX}\) |

For example, varying \(q\) sends \(y\) to \(e^{t\operatorname{Ad}_aX}y\) and \(z\) to \(ze^{-t\operatorname{Ad}_aX}\). Varying \(a\) sends \(y\) to \(e^{tX}y\) and \(z\) to \(e^{tX}ze^{-tX}\). These are two different responses. In the \(q\)-row the same transported frame occurs in both terms; bi-invariance removes it only after forming their joint norm.

The complete induced form is therefore
\[
\boxed{
\begin{aligned}
\mathcal E_{\rm ch}(F)=\kappa\int_{G^3}\big[&
3|L_xF|^2+3|L_zF|^2+|R_yF|^2\\
&+|(R_x+R_y)F|^2+|(L_y-R_z)F|^2
+|(L_y+L_z-R_z)F|^2\big]\,dx\,dy\,dz.
\end{aligned}}
\tag{TC6}
\]
The same identity after polarization gives every mixed response. It follows first for smooth physical functions by the displayed raw derivatives and product Haar. In tree gauge each displayed row generates a Haar-preserving flow, so its divergence is zero. The corresponding differential operator on the smooth product is
\[
\begin{aligned}
H_{\rm ch}=\kappa\big[3D_x+3D_z+D_y
&-\sum_A(R_{x,A}+R_{y,A})^2
-\sum_A(L_{y,A}-R_{z,A})^2\\
&-\sum_A(L_{y,A}+L_{z,A}-R_{z,A})^2\big].
\end{aligned}
\tag{TC7}
\]
Here \(D_x=-\sum_A L_{x,A}^2=-\sum_A R_{x,A}^2\), and similarly for the other factors. The explicitly positive individual \(x,y,z\) rows make (TC6) uniformly elliptic. Closure gives the inherited invariant \(H^1\) form domain and \(H^2\) operator domain; the tree pullback intertwines the entire physical operator with (TC1), and hence its heat and unitary evolutions. No boundary conditions in singular orbit coordinates are introduced.

A supplied bounded real class potential on each cell, for example \(\sum_i\lambda_i[1-\operatorname{Tr}(x_i)/2]\) for \(SU(2)\), can be added before or after this exact reduction. It gives the corresponding complete interacting operator with a simple positive vacuum on this fixed compact carrier. The [[local-incidence-preparations-and-the-gauge-transfer|local incidence theorem]] can return such a finite Hamiltonian from its declared raw-link preparation; the issue tested here is whether the new access construction returns that same geometry.

## Signed cell pairs expose the incidence immediately

Take \(SU(2)\), \(Q=-2\operatorname{Tr}\), and write
\[
x=c_xI-i\mathbf x\cdot\boldsymbol\sigma,
\quad y=c_yI-i\mathbf y\cdot\boldsymbol\sigma,
\quad z=c_zI-i\mathbf z\cdot\boldsymbol\sigma,
\qquad s_{xy}=\mathbf x\cdot\mathbf y,
\tag{TC8}
\]
and similarly for the other pairings. The scalar functions are individual half traces. They satisfy \(L_xc_x=R_xc_x=-\mathbf x/2\), \(C_xc_x=0\), and \(D_Qc_x=3c_x/4\). Equations (TC6)–(TC7) yield
\[
\boxed{
\begin{gathered}
H_{\rm ch}c_i=3\kappa c_i\quad(i=x,y,z),\\
H_{\rm ch}(c_xc_y)=6\kappa c_xc_y-\frac\kappa2s_{xy},\\
H_{\rm ch}(c_yc_z)=6\kappa c_yc_z+\frac\kappa2s_{yz},\\
H_{\rm ch}(c_xc_z)=6\kappa c_xc_z.
\end{gathered}}
\tag{TC9}
\]
The first shared edge couples the left and middle cells; the second couples the middle and right with the opposite chosen orientation. The separated cell traces have zero instantaneous mixed response. For \(P_t=e^{-tH_{\rm ch}}\), the derivative of \(P_t(fg)-(P_tf)(P_tg)\) at zero is twice the form density \(\Gamma(f,g)\); hence the two adjacent trace covariances start with \(\kappa t s_{xy}/2\) and \(-\kappa t s_{yz}/2\), while the nonadjacent one has no first-order term. This is not a statement that separated cells stay statistically independent in an interacting vacuum.

## A word change recovers four paths, not the two bridges

The physical common-parent family with three accesses is a four-parallel-path electric geometry. Let its actual path variables be \(P_0,P_1,P_2,P_3\) between the same two endpoints, with positive clock weights \(\alpha_0,\alpha_1,\alpha_2,\alpha_3\). Use successive relative cells
\[
x=P_0P_1^{-1},\qquad
y=P_2P_1^{-1},\qquad
z=P_3P_2^{-1}.
\tag{TC10}
\]
Relative to the common reference \(P_1\), the three star coordinates are \((x,y,w)\), with the actual word \(w=zy=P_3P_1^{-1}\). This is a Haar-preserving word change on the complete three-loop carrier. Differentiating the four paths, rather than resetting the loop clocks, gives
\[
\boxed{
\mathcal E_{\parallel}(F)=\int\big[
\alpha_0|L_xF|^2+\alpha_3|L_zF|^2
+\alpha_1|(R_x+R_y)F|^2
+\alpha_2|(L_y-R_z)F|^2\big].}
\tag{TC11}
\]
Thus a legitimate word change does remove the spurious all-to-all trace response of an unchanged star coordinate formula. It retains the two correctly signed neighboring rows. Its single-cell coefficients are \(\alpha_0+\alpha_1\), \(\alpha_1+\alpha_2\), and \(\alpha_2+\alpha_3\).

Matching the two mixed trace terms of (TC9) forces \(\alpha_1=\alpha_2=\kappa\). Matching the left and right one-cell clocks then forces \(\alpha_0=\alpha_3=3\kappa\). The middle coefficient is consequently \(2\kappa\), whereas the actual square has \(4\kappa\). No choice of the four paces in this marked word presentation recovers all the displayed cell responses.

The complete missing form is more informative than this coefficient mismatch. At those forced weights,
\[
\boxed{
\mathcal E_{\rm ch}-\mathcal E_{\parallel}
=\kappa\int\big[|(L_y+C_z)F|^2+|R_yF|^2\big].}
\tag{TC12}
\]
These are exactly the upper and lower raw bridges. Contracting both bridges would identify their endpoint pairs and leave the four-parallel-path graph, but these bridges join accessible trivalent vertices. Their deletion is not a pure bivalent subdivision of the marked graph. Their response must be retained or supplied by a new comparison law.

For individual trace products, replacing (TC12) by \(2\kappa D_y\) happens to repair (TC9), because each conjugation row kills each individual trace. It fails on the full carrier. Consider the gauge-invariant end-to-end angular source
\[
F(x,y,z)=\frac12\operatorname{Tr}(xz^{-1})
=c_xc_z+\mathbf x\cdot\mathbf z.
\tag{TC13}
\]
It is independent of \(y\), so the added middle Casimir has zero form on \(F\). The actual upper bridge instead contributes \(|C_zF|^2=|\mathbf x\times\mathbf z|^2\). For the patched form \(\mathcal E_{\rm patch}=\mathcal E_{\parallel}+2\kappa\int|R_yF|^2\),
\[
\boxed{
\mathcal E_{\rm ch}(F)-\mathcal E_{\rm patch}(F)
=\kappa\int|\mathbf x\times\mathbf z|^2\,dx\,dz
=\frac{3\kappa}{8}>0.}
\tag{TC14}
\]
The last equality uses the Haar identities \(\mathbb E x_ix_j=\delta_{ij}/4\), \(\mathbb E|\mathbf x|^2=3/4\), and independence of the two Haar factors. No numerical approximation is involved. This source compares separated cells through their shared frame; its extra response is invisible to the three separate plaquette traces and their pairwise products.

## The next preparation must carry the bridge action

The required new rows are now explicit:
\[
\mathscr D_{a,X}=L_{y,X}+C_{z,X},\qquad \mathscr D_{b,X}=-R_{y,X},
\qquad
e^{t\mathscr D_{a,X}}:(y,z)\mapsto(e^{tX}y,e^{tX}ze^{-tX}).
\tag{TC15}
\]
This flow transports both a middle-cell increment and the frame in which the later loop is compared. An independently assigned middle-loop clock supplies the scalar middle-cell motion but misses the conjugation of \(z\).

[[conditional-preparation-diagrams-and-ancestral-readout|Ancestral conditional preparations]] can preserve selected marked readouts under a more general parent graph. When their node words remain independent product-Haar coordinates and the leading comparison stays a sum of independent word distances, changing Gaussian correlations adjusts coefficients but does not itself add (TC15). One must change the actual comparison/readout rows or derive a different transported incidence law. Adding overcomplete word comparisons can do more, but then the independent Haar leaf integration used by the current conditional normalization needs a new proof.

The three-cell test therefore gives a concrete target for a multiparent extension: recover (TC6), its complete physical source algebra and the bridge witness (TC14), while retaining the marked normalization and presentation rules. It establishes failure of the specified star member and its scalar middle-loop repair; it does not claim a no-go theorem for arbitrary nonlinear word inventories, covariance rules or reconstruction categories.

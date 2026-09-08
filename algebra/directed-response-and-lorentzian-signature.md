# Directed Response and Lorentzian Signature

A positive response geometry and an oriented covector line determine a reflection whose associated bilinear form has one negative direction. This gives a conditional construction of Lorentzian signature without beginning with a time coordinate. The orientation, integrability of clock slices, compatibility of process arrows with causal cones, and physical scale are distinct outputs to be tested. The construction does not itself supply the response geometry or prove that a factual process selects the required line.

## The directed datum need not begin as a clock

Let \(X\) be a smooth \(n\)-dimensional realization carrier, \(n\geq2\), with positive metric \(h\). Let \([\theta]_+\) be an oriented nowhere-zero cotangent line: local representatives are related by \(\theta'=f\theta\), \(f>0\). Interpret it provisionally as a direction distinguished by the upstream process, not as an already calibrated differential \(dt\).

This is a construction on a supplied smooth intermediary. Obtaining \(X,h,[\theta]_+\) from the process category of [[algebra/local-global-individuation|local–global individuation]] remains a realization problem. In particular, a response metric on quantum state variations is not automatically a metric on spacetime tangents; that carrier-changing map must be constructed.

Write
\[
s^2=h^{-1}(\theta,\theta),\qquad
\Pi=\frac{h^\sharp\theta\otimes\theta}{s^2},
\qquad R=I-2\Pi.
\tag{DS1}
\]
Here \(h^\sharp:T^*X\to TX\), and \(\Pi\) acts on a tangent \(v\) by \(h^\sharp\theta\,\theta(v)/s^2\). Directly,
\[
\Pi^2=\Pi,\qquad R^2=I,\qquad
h(Rv,w)=h(v,Rw).
\tag{DS2}
\]
Thus \(R\) is a positive-metric orthogonal reflection, not an irreversible process map.

## Signature and orientation are different consequences

Define
\[
\boxed{g(v,w)=h(v,Rw)
=h(v,w)-2\frac{\theta(v)\theta(w)}{s^2}.}
\tag{DS3}
\]
Put \(n=h^\sharp\theta/s\), so \(h(n,n)=1\), and decompose \(v=a n+w\), \(h(n,w)=0\). Then
\[
g(v,v)=h(w,w)-a^2,\qquad
\theta(v)=sa,\qquad
g^{-1}(\theta,\theta)=-s^2.
\tag{DS4}
\]
There are exactly \(n-1\) positive directions and one negative direction. The condition \(\theta(v)>0\) selects the future timelike cone. Replacing \(\theta\) by \(-\theta\) preserves \(g\) but reverses that selection.

No magnitude of \(\theta\) appears in (DS3). Changing \(\theta\) by any nonzero scalar function preserves the metric; changing it positively also preserves orientation. Under \(h\mapsto\Omega^2h\), the resulting \(g\) changes to \(\Omega^2g\). The cones therefore depend on relative response and the directed line, not on an absolute ruler.

The formula works in every dimension \(n\geq2\). It provides one exceptional direction after a rank-one line has been selected; it neither selects three spatial dimensions nor proves that every upstream directed structure has rank one. [[algebra/real-forms-and-factive-spacetime|Real-form descent]] is a separate candidate for a three-dimensional spatial carrier.

## A cone bound is stronger than monotonicity

Suppose admissible process arrows have a differentiable realization with tangent \(v\). It is not enough to demand \(\theta(v)>0\). A future causal realization requires
\[
\boxed{
\mathscr Q(v):=
\frac{h(v,v)\,h^{-1}(\theta,\theta)}{\theta(v)^2}
\leq2,\qquad \theta(v)>0.}
\tag{DS5}
\]
This quotient is invariant under regular reparametrization of the arrow, positive rescaling of \(\theta\), and conformal rescaling of \(h\). The future condition also survives when the reparametrization preserves orientation. Equivalently, \(h(w,w)\leq a^2\). With \(h\) Euclidean and \(\theta=dx^0\), the tangent \((1,2,0,\ldots)\) increases \(x^0\) but violates the bound.

Equation (DS5) is the substantive proposed link: derive it for the realized arrows from the **same law** that supplies \(h\) and \([\theta]_+\). It would turn directed response into a restriction on propagation. Monotone labels alone cannot do so.

The coefficient two also has a declared origin. More generally,
\[
g_\beta=h-\beta\frac{\theta\otimes\theta}{s^2},
\qquad \beta>1,
\tag{DS6}
\]
has one negative direction, with \(h(w,w)\leq(\beta-1)a^2\) as its causal bound. Signature does not choose \(\beta=2\). The extra reflection condition does:
\[
(I-\beta\Pi)^2=I+(\beta^2-2\beta)\Pi.
\tag{DS7}
\]
Among \(\beta>1\), this is an involution exactly at two.

Alternatively, a process law might first determine
\[
M=\sup_{\text{admissible forward tangents}}
\frac{h(w,w)}{a^2}.
\tag{DS8}
\]
If \(0<M<\infty\), the smallest aperture of this family containing those tangents has \(\beta=1+M\). This proves containment, not that every tangent in the resulting cone is physically attainable. A sharp reflection realization must establish \(M=1\); it cannot tune \(\beta\) after choosing the processes and then call the answer necessary.

The method resembles the [[deriving-g-v2/the-g-free-first-law|G-free first law]]: identify the common dimensionless relation before calibrating its presentations. Here the common carrier is tangent response, not heat or area. Neither the formula nor its conformal invariance fixes a measured value of \(c\).

## Integrable clock slices are a further property

No closedness condition on \(\theta\) was used above. If the directed line additionally satisfies
\[
\theta\wedge d\theta=0,
\tag{DS9}
\]
Frobenius integrability gives local representatives \(\theta=f\,dr\), with \(f>0\) after choosing orientation. Then \(r\) is a local temporal function for \(g\), and its level sets are spacelike. A global temporal valuation and a global Cauchy foliation require further hypotheses.

Without (DS9), the selected hyperplanes \(\ker\theta\) do not form clock slices. For example, on \(\mathbb R^3\), \(\theta=dz-x\,dy\) has
\(\theta\wedge d\theta=-dz\wedge dx\wedge dy\neq0\), yet (DS3) still constructs a Lorentzian metric. That metric can have other local temporal functions; the conclusion is only that this chosen directed line is not proportional to their differential.

This separates an upstream direction from its integrable presentation without naming a fifth coordinate. It does not identify Frobenius failure with entropy production. Likewise, persistent record extension, erasure of accessible distinctions, and invertibility of a clock remain different maps, as in [[global-local-response-reconstruction/causal-patch-boundary-and-two-times|the two-time analysis]].

## The next common-object test

[[algebra/positive-cone-processes-and-the-complex-corner|The complex-corner construction]]
now closes this comparison for a concrete finite member. A logarithmic
determinant supplies \(h\) and \(\theta\) together, and a positive
exceptional-descent variance supplies inputs that automatically satisfy
(DS5). The selected complex rank-two corner fixes the \(3+1\) signature;
the bare Albert algebra has not yet selected that corner.
[[algebra/qubit-cone-interiorization-and-the-clock-gap|Dynamic cone interiorization]]
then measures a specified transfer gap on that finite ordered carrier,
while [[algebra/determinant-scale-clock-and-the-hyperbolic-threshold|the hyperbolic test]]
distinguishes its scale geometry from a physical mass threshold.

For a candidate master object, first construct the smooth response carrier and its directed line. Then test (DS5), its behavior under composition and gluing, and whether a suitable clock presentation is available. [[algebra/wick-real-forms-and-positive-preparation|Positive preparation and Wick real forms]] separately constructs a reversible positive-frequency clock from a positive boundary response.

The decisive bridge would identify that clock's causal structure with (DS3) on the **same realized geometry**. Appending either construction to an unrelated carrier does not supply this identification. Neither the reflection nor the cone bound alone implies a spectral gap; they can coexist with arbitrarily soft excitations.

[[directed-analytic-realization/real_form_response_receipt.py|The finite receipt]] checks the reflection identities, rescaling laws, aperture freedom and monotonicity counterexample. [[directed-analytic-realization/real-form-response-receipt-output.txt|Its output]] verifies finite algebra, not a physical realization or continuum theorem.

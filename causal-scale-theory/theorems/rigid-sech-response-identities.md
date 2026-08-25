# CST-B2 Rigid Sech Response Identities

A positive \(\operatorname{sech}^2\) density with constant scale-state rate and separate homogeneous conservation has a uniquely determined equation of state, Riccati flow, and differential invariants. These are exact consequences of the stipulated profile used by CST-B2; they do not derive that member, its amplitude, or a covariant stress tensor, and they are not identities of [[causal-scale-theory/response-family-interface|the response-family interface]] in general.

Let \(I\subseteq\mathbb R\) be an interval in logarithmic scale age \(N\), and suppose

$$
x:=N-N_c,
\qquad
\rho_X(N)=A\operatorname{sech}^2(\nu x),
\qquad
A>0,
\quad
\nu>0.
$$

Assume the component is separately conserved on a homogeneous expanding background:

$$
\rho_X'+3(1+w_X)\rho_X=0,
\qquad
'=\frac{\mathrm d}{\mathrm dN}.
$$

These are the complete load-bearing hypotheses. In CST-B2 the value of \(A\) comes from the constitutive and horizon bridges in [[causal-scale-theory/response-law|the balanced-binary response note]], but that provenance is not needed for the following theorem.

## Equation of state and Riccati flow

Direct differentiation gives

$$
\frac{\rho_X'}{\rho_X}
=-2\nu\tanh(\nu x).
$$

The continuity equation therefore fixes

$$
\boxed{
w_X(N)
=-1+\frac{2\nu}{3}\tanh(\nu x).}
$$

Writing \(X:=1+w_X\), one obtains

$$
\boxed{
X'
=\frac{2\nu^2}{3}-\frac32X^2.}
$$

Thus the equation-of-state history is a translated heteroclinic orbit between \(X=-2\nu/3\) and \(X=+2\nu/3\). It is not a saddle-node flow.

Eliminating \(x\) gives the amplitude- and crossing-independent identity

$$
\boxed{
9(1+w_X)^2+6w_X'=4\nu^2.}
$$

For the local CPL convention \(w(a)=w_0+w_a(1-a)\), so that \(w_a=-w'_0\), this implies

$$
\boxed{
w_a
=\frac32(1+w_0)^2-\frac{2\nu^2}{3}.}
$$

The relation concerns the separately identified \(X\)-sector and its local tangent at the present epoch. A posterior for a total effective equation of state need not measure this object.

## Equivalent density identities

Normalize the density by its crossing value:

$$
y:=\frac{\rho_X}{\rho_X(N_c)}
=\operatorname{sech}^2(\nu x).
$$

Then

$$
\boxed{
y+\frac{1}{4\nu^2}
\left(\frac{\mathrm d\ln y}{\mathrm dN}\right)^2
=1,}
$$

and

$$
\boxed{
\frac{\mathrm d^2\ln y}{\mathrm dN^2}
+2\nu^2y=0.}
$$

Equivalently, for \(\Delta:=-(\ln y)'=3(1+w_X)\),

$$
\boxed{
\Delta'=2\nu^2-\frac12\Delta^2.}
$$

These are forward consequences of the declared positive pulse. A converse requires positivity, initial data, and a uniqueness theorem and is not asserted here.

## Crossing result

The explicit pulse has its unique global maximum at \(N=N_c\). At that point

$$
\rho_X'(N_c)=0,
\qquad
w_X(N_c)=-1.
$$

For an arbitrary separately conserved positive component, a stationary density implies \(w=-1\); it does not by itself prove that the stationary point is a maximum. Maximality here follows from the explicit \(\operatorname{sech}^2\) profile.

## Failure boundary

A scale-dependent extensive factor, an exchange current, or another density shape changes these identities even if the normalized binary state geometry remains exact. The theorem supplies no local action, sound speed, anisotropic stress, perturbation equation, or microscopic wall construction.

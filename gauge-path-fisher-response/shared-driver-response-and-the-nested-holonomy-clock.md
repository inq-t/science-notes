# Shared-driver response and the nested-holonomy clock

The planar heat state admits a closed response that couples nearby nested loops through their shared driving path. This repairs the perimeter form's nonclosability without changing the nested-loop state. Its full clock and its character correlations can be computed exactly. The construction also isolates a remaining choice: the same state, carrier, and residual gauge symmetry admit both gapped and gapless clocks. Consistency of observation and response does not by itself select a positive decay rate.

**Status: [EXACT] application of established path-space calculus to the specified nested-holonomy carrier; [EXACT] character responses and clock-selection tests; [OPEN] extension to the whole planar graph carrier and identification of a four-dimensional Yang--Mills physical clock.**

## The whole carrier retains the driving path

Let \(G\) be a nontrivial compact connected semisimple Lie group with
bi-invariant metric \(Q\), orthonormal Lie basis \(T_a\), and
\(d=\dim G\). Fix \(0<T<\infty\). Develop standard
\(\mathfrak g\)-valued Brownian motion by
\[
dX_t=\sqrt2\sum_a X_tT_a\circ dB_t^a,\qquad X_0=e.
\tag{SD1}
\]
The generator in the index \(t\) is \(\Delta_Q\). Its finite-dimensional
laws are exactly the heat-increment laws (HS3) of
[[holonomy-state-refinement/heat-state-continuity-and-response-closability|the nested-loop state]],
with \(t=\sigma A\) the supplied heat-area. Use the continuous realization
\[
\mathscr X=C_e([0,T],G),\qquad
\mu=\operatorname{Law}(X),\qquad
\mathcal H=L^2(\mathscr X,\mu),\qquad
\mathcal H_{\rm inv}=\mathcal H^{\operatorname{Ad}G}.
\tag{SD2}
\]
Here invariance means one simultaneous conjugation of the entire based
path. It is the residual root action on these jointly based holonomies,
not an independent gauge action at every value of \(t\).

The Itô map \(\mathcal I:B\mapsto X\) has the almost-sure inverse
given by its stochastic logarithm,
\[
B_t=\frac1{\sqrt2}\int_0^t X_s^{-1}\circ dX_s.
\tag{SD3}
\]
Thus \(UF=F\circ\mathcal I\) is a unitary from \(\mathcal H\) onto
Euclidean Wiener \(L^2\). This uses the full continuous path; dense
readout times suffice, but an endpoint or the sparse square sequence in
(HS13) does not supply this inverse. Nor does (SD2) contain every
trapezoid-face observable of the earlier planar graph construction.

The probability law is a mathematical state representation, not a claim
that randomness is ontologically primitive. The whole Itô identification
is invertible modulo null sets. Forgetting occurs on a further restricted
readout, not in this identification itself.

## A closed response from shared variations

Let \(\mathsf D\) be the closed Wiener Malliavin derivative, with values
in \(L^2(\text{Wiener}\times[0,T];\mathfrak g)\). Its domain is
\(\mathbb D^{1,2}\). Define
\[
\operatorname{Dom}\mathcal E=U^{-1}\mathbb D^{1,2},\qquad
\mathcal E(F,G)=\langle\mathsf D UF,\mathsf D UG\rangle.
\tag{SD4}
\]
This is a closed positive Dirichlet form, not an identification of a
state covariance matrix with a response matrix. For clarity use real
functions below, with the usual sesquilinear extension for complex ones.
Fix the derivative convention
\[
L_af(g)=\left.\frac d{dv}f(e^{vT_a}g)\right|_{v=0},\qquad
\nabla_L f=\sum_a(L_af)T_a.
\]
Under a Cameron--Martin shift \(B+\varepsilon h\), differentiating
(SD1) gives
\[
\delta X_tX_t^{-1}
=\sqrt2\int_0^t\operatorname{Ad}_{X_s}\dot h_s\,ds.
\]
Consequently, for \(F=f(X_{t_1},\ldots,X_{t_m})\),
\[
\mathsf D_s UF
=\sqrt2\operatorname{Ad}_{X_s}^{-1}
\sum_{i:s\le t_i}\nabla_{L,i}f,
\qquad
\Gamma(F,G)
=2\sum_{i,j}\min(t_i,t_j)
Q(\nabla_{L,i}f,\nabla_{L,j}g).
\tag{SD5}
\]
The response is \(\mathcal E(F,G)=\mathbb E_\mu\Gamma(F,G)\).
The common adjoint rotation cancels by bi-invariance of \(Q\).
The minimum kernel is therefore derived from overlapping variations of
one driver. It is not postulated from a resemblance to Brownian covariance.

Smooth finite-holonomy cylinders are a form core, not only an
\(L^2\)-dense readout. The precise source is
[[library/ito-maps-and-analysis-on-path-spaces/inq|Elworthy--Li]],
§4's cylinder-closure definition and §9, Theorem 9.1 and Remark 9.2:
injective-noise Itô maps intertwine the Sobolev derivatives onto the
Wiener ones and conjugate their Ornstein--Uhlenbeck operators. Here each
noise map \(\sqrt2\,L_{x*}:\mathfrak g\to T_xG\) is an isomorphism,
so there is no redundant noise. The theorem concerns the full path and
its Sobolev domain, not an endpoint readout. Remark 9.2 supplies Markov
uniqueness in this injective case without the source's condition
\((M_0)\). This applies to the invariant connection induced by (SD1), with its adjoint
right-invariant tangent connection. It does **not** identify (SD4) with
an arbitrary Levi--Civita or Ricci-damped path gradient. The displayed
derivative has no additional Ricci damping.

## The response repairs the nearby-loop failure

Specialize to \(SU(2)\), \(Q=-2\operatorname{Tr}\), and
\(f_t=\chi_{1/2}(X_t)\). Write
\[
c=\tfrac34,\qquad m(t)=2e^{-ct},\qquad
J(t)=\tfrac34(1-e^{-2t}).
\]
Bi-invariance makes the heat semigroup commute with the \(L_a\).
Conditioning the later gradient on the earlier holonomy in (SD5) gives
\[
\boxed{\mathcal E(f_s,f_t)
=2u\,e^{-c|t-s|}J(u),\qquad u=\min(s,t).}
\tag{SD6}
\]
The diagonal is now \(2tJ(t)\), not the perimeter expression
\(B_CJ(t)\) in (HS5). This replaces the response law, rather than only
inserting off-diagonal entries while retaining the old diagonal.
For \(s\le t\),
\[
\mathcal E(f_t-f_s)
=2tJ(t)+2sJ(s)-4s e^{-c(t-s)}J(s)\longrightarrow0
\quad(t\downarrow s).
\tag{SD7}
\]
State continuity was already established in (HS10). Thus
\(f_{t_k}\to f_{t_0}\) now holds in the form norm as well. For
\(g_N=f_{t_0}-N^{-1}\sum_{k=1}^N f_{t_k}\), Cesaro convergence of
the derivatives proves \(\mathcal E(g_N)\to0\). The mixed responses
retain exactly the limiting energy that the edge-diagonal form lost.

## The whole clock and its complete invariant threshold

Let \(\mathsf N=\mathsf D^*\mathsf D\) be the Wiener number operator.
On Wiener chaos \(\mathcal C_n\) it acts by \(n\). Equivalently, its
semigroup is the Mehler operator
\[
\mathsf M_\tau V(B)
=\mathbb E_{B'}V\!\left(e^{-\tau}B+
\sqrt{1-e^{-2\tau}}B'\right),\qquad
L=U^{-1}\mathsf N U,\qquad
\mathsf P_\tau=U^{-1}\mathsf M_\tau U=e^{-\tau L}.
\tag{SD8}
\]
Here \(B'\) is independent with the same Wiener law. This constructs a
strongly continuous, positive, self-adjoint Markov semigroup for every
\(\tau\ge0\). Its form domain has
\(\sum_n n\|(UF)_n\|^2<\infty\); its generator domain has
\(\sum_n n^2\|(UF)_n\|^2<\infty\). The standard Hermite mechanism is
also used in [[gaussian-bridge-gap-calibration/inq|Gaussian bridge-gap
calibration]], but (SD8) acts on a full group-valued path carrier.

Conjugation of \(X\) corresponds to the orthogonal transformation
\(B\mapsto\operatorname{Ad}_g B\). It commutes with (SD8) and each
chaos projection. Semisimplicity gives
\[
\mathcal C_1^G
=\bigl(L^2([0,T])\otimes\mathfrak g\bigr)^G=0.
\]
The centered invariant quadratic
\(W(X)=|B_T(X)|_Q^2-dT\) belongs to the second chaos and satisfies
\[
LW=2W,\qquad \|W\|_2^2=2dT^2,\qquad
\mathcal E(W)=4dT^2.
\]
It follows on the **entire** invariant path carrier that
\[
\ker L=\mathbb C\mathbf1,\qquad
\boxed{\inf\operatorname{spec}
\left(L\big|_{\mathcal H_{\rm inv}\ominus\mathbb C\mathbf1}\right)=2.}
\tag{SD9}
\]
Compact-group averaging preserves the cylinder core. The full, unprojected
carrier instead has threshold one. A positive-dimensional central torus
would retain invariant first-chaos vectors, so semisimplicity matters.
There is no claim that all higher invariant chaoses are even.

The number two is an exact threshold for the **chosen unit OU clock**.
The area index \(t\), response duration \(\tau\), and physical clock
have not been identified. Multiplying \(L\) by a positive constant
multiplies this threshold by that constant.

There is a stronger obstruction to identifying those clocks:
[[mass-scale-calibration/mass-as-casimir-and-realization#A Poincare Hamiltonian has no positive eigenvalues|boost covariance excludes positive Hamiltonian eigenvalues]]
in any strongly continuous positive-energy Poincare representation.
The explicit eigenvector \(LW=2W\) therefore rules out every positive
rescaling of this \(L\) as that same Hamiltonian, despite its infinite
path carrier and unbounded spectrum. Any scalar \(f(L)\) retaining a
positive eigenvalue has the same obstruction. An auxiliary response or
an internal mass operator on a separately constructed continuous-momentum
carrier remains possible; neither is a same-clock identification.

## Exact correlations for every clock duration

For \(SU(2)\), let \(\rho=e^{-\tau}\) and develop
\(B^\rho=\rho B+\sqrt{1-\rho^2}B'\) by (SD1). The joint fundamental
tensor moment has generator
\[
K_\rho=-\tfrac32I+2\rho\sum_a T_a\otimes T_a.
\]
The decomposition \(\tfrac12\otimes\tfrac12=0\oplus1\) gives its
eigenvalues \(-3/2+3\rho/2\) and \(-3/2-\rho/2\), of
multiplicities one and three. Taking the tensor trace at the common
duration \(u=\min(s,t)\), and conditioning over the later independent
increment, gives the centered readout
\[
\boxed{
\langle f_s-m(s),\mathsf P_\tau(f_t-m(t))\rangle
=e^{-c(s+t)}
\left[e^{3\rho u/2}+3e^{-\rho u/2}-4\right].}
\tag{SD10}
\]
At \(\tau=0\) this is the heat-state covariance. Its negative clock
derivative at zero is (SD6). Expanding the exponentials gives
\[
e^{-c(s+t)}\sum_{n\ge2}
\frac{3^n+3(-1)^n}{2^n n!}\,u^n e^{-n\tau}.
\tag{SD11}
\]
Every displayed coefficient is positive; the first-chaos term cancels,
and the coefficient of \(e^{-2\tau}\) is
\(3u^2e^{-c(s+t)}/2>0\) for positive readout times. Thus these
characters detect the full invariant threshold through their long-duration
correlations. This is not a finite harmonic cutoff.

These are readouts of the whole semigroup. A finite-holonomy subspace
need not be invariant under it. Neither its compression nor the generator
obtained by restricting the quadratic form may be silently identified
with the whole clock; see
[[holonomy-state-refinement/holonomy-refinement-and-clock-compatibility#The tensor condition is stronger than a scalar normalization|the clock-compression distinction]].

## The same state also admits a gapless closed response

Replace the unit driver rate by any bounded measurable
\(a:[0,T]\to[0,\infty)\), with positivity required almost everywhere.
Initially take \(UF\) to be a finite Gaussian polynomial cylinder and set
\[
\mathcal E_a(F)=
\mathbb E\int_0^T a(s)|\mathsf D_s UF|_Q^2\,ds,
\qquad A(t)=\int_0^t a(s)\,ds.
\tag{SD12}
\]
Take its closure. On the Wiener side its generator is
\(d\Gamma(M_a\otimes I_{\mathfrak g})\): on the \(n\)-th chaos the
operator \(A_n\) multiplies kernels by \(\sum_{j=1}^n a(s_j)\).
Writing \(v_n=(UF)_n\), the closed form domain is
\(\sum_n\langle v_n,A_nv_n\rangle<\infty\), and the generator domain
is \(\sum_n\|A_nv_n\|^2<\infty\). When the essential infimum vanishes,
the form domain can be larger than \(U^{-1}\mathbb D^{1,2}\); retaining
that smaller domain would not generally give a closed form. The
semigroup is the Gaussian second quantization of \(e^{-\tau M_a}\).

Chaos truncation followed by finite-rank approximation, using
\(A_n\le n\|a\|_\infty I\), proves that finite Gaussian polynomials
form a core. Their unit-OU form approximations
by holonomy cylinders also converge in \(\mathcal E_a\), because
\(\mathcal E_a\le\|a\|_\infty\mathcal E\) on that domain. Thus
holonomy cylinders remain a core for this closure. Formula (SD5) holds
with \(2\min(t_i,t_j)\) replaced by \(2A(\min(t_i,t_j))\).

Put \(\alpha=\operatorname*{ess\,inf}a\). Every nonconstant invariant
chaos has degree at least two, giving the lower bound \(2\alpha\).
For a normalized real time mode \(h\), set
\[
W_h=\left|\int_0^T h(s)\,dB_s\right|_Q^2-d.
\]
This is an invariant second-chaos vector, with
\[
\frac{\mathcal E_a(W_h)}{\|W_h\|_2^2}
=2\int_0^T a(s)|h(s)|^2\,ds.
\]
Concentrating \(h\) on sets where \(a\) approaches its essential
infimum proves the exact identity
\[
\boxed{\delta_a=2\operatorname*{ess\,inf}a.}
\tag{SD13}
\]
Positivity almost everywhere keeps constants as the unique kernel even
when \(\delta_a=0\). For example, \(a(s)=s/T\) and
\(h_n=\sqrt{n/T}\,1_{(0,T/n)}\) give the exact invariant quotients
\(1/n\). The state and residual gauge action have not changed.
Nearby-loop form continuity still holds because \(A\) is continuous.

This is a non-selection theorem within a stated family, not a universal
objection to a physical gap: even a closed shared response and a unique
vacuum leave the uniform clock intensity undetermined.

## A same-clock restart law selects constant intensity

There is a precise additional condition that removes the arbitrary
area dependence in this family. For \(SU(2)\), use the actual annular
readout
\[
z_{s,t}=\chi_{1/2}(X_s^{-1}X_{s+t}),\qquad
s\ge0,\quad t>0,\quad s+t\le T.
\]
It is invariant under the residual simultaneous conjugation and has the
same state distribution as \(f_t\). For
\(f(x,y)=\chi_{1/2}(x^{-1}y)\), common left multiplication gives
\(\nabla_{L,1}f+\nabla_{L,2}f=0\). The two-by-two response kernel
therefore cancels the variations before \(s\), leaving
\[
\boxed{\mathcal E_a(z_{s,t})
=2[A(s+t)-A(s)]J(t).}
\tag{SD14}
\]
At \(s=0\), the first coordinate is fixed and its response row is zero;
the same formula gives \(2A(t)J(t)\).

Impose **response homogeneity under restarting an annulus, in the same
clock**:
\[
\mathcal E_a(z_{s,t})=\mathcal E_a(z_{0,t})
\quad\text{for every admissible }s,t.
\tag{SD15}
\]
Since \(J(t)>0\), (SD15), using (SD14), is equivalent to
\(A(s+t)=A(s)+A(t)\). Absolute continuity of \(A\) then yields
\[
A(t)=\lambda t,\qquad a=\lambda\ \text{a.e.},\qquad
\delta_a=2\lambda>0.
\tag{SD16}
\]
This selects a constant response without presupposing a uniform lower
bound. It uses an independently stated **response law**, not merely the
stationarity of the heat-state increments. The conversion factor
\(\lambda\) remains free. To retain one positive rate on all horizons,
the family must also agree on interval restrictions in this same clock;
choosing a different \(\lambda_T\to0\) for each horizon would not do.

Interval restriction, independent state increments, and concatenation
with shifted response weights all hold for nonconstant \(a\) too.
They do not imply (SD15). Allowing a restart-dependent clock rescaling
also weakens it: \(a(s)=e^{-s}\) gives
\(\mathcal E_a(z_{s,t})=e^{-s}\mathcal E_a(z_{0,t})\), with threshold
\(2e^{-T}\) on \([0,T]\). The compatible infinite-horizon extension
has unique vacuum and threshold zero. Its response shape restarts after
retiming, but it has no single uniformly positive clock intensity.

The selection is consequently conditional, not circular and not yet
physical: one can name the extra whole-to-local compatibility law, prove
what it forces, and then ask what construction justifies that law.

[[gauge-path-fisher-response/path-shift-fisher-geometry-before-gauge-projection|Path-shift Fisher
geometry]] supplies a conditional selection beyond this restart test.
For specified deterministic path-left translations, the actual relative
entropy fixes a tangent metric whose dual is (SD5), selecting \(a=1\)
in (SD12). The translation action and this dualization prescription are
additional structure. Quotienting its state scores before dualization
erases their first-order metric; choosing the opposite handed action
gives a different invariant response detectable with three holonomies,
although path inversion relates the two clocks and their thresholds.

[[gauge-path-fisher-response/two-sided-fisher-completion-and-the-neutral-carrier|The joint
two-sided Fisher construction]] retains both actions and computes their
cross-score covariance. Its finite-response cylinders determine the
neutral carrier, and its own closed operator has non-attained threshold
two, compatible with terminal enlargement. However, its actual annular
response violates (SD15), even after allowing a constant rescaling at
each restart. Handedness removal and restart homogeneity are different
compatibility requirements.

## What this construction discharges

The construction supplies an actual mixed response, a cylinder-core
closure, its all-duration clock, and an exact full-carrier threshold for
the nested-loop path state. It repairs the specific approximate-gluing
failure in (HS14). Established Wiener calculus supplies the operator;
the selected number-operator rate supplies its positive threshold.

The remaining selection question is sharper than finding another
positive finite matrix: what law constrains the driver response together
with the state, instead of merely choosing \(a\)? Same-clock restart
homogeneity is one sufficient law within this family. Fisher dualization
now derives it from a specified path action and response prescription,
not from the state alone or the Yang--Mills return requirements. Extending it to
all graph observables, controlling the four-dimensional continuum and
infinite-volume limits, recovering the Yang--Mills ultraviolet structure,
and identifying the physical Hamiltonian are separate unfinished
obligations. This auxiliary clock has not discharged them.

The [[gauge-boundary-frame-gluing/receipts/boundary_charge_gluing_receipt.py|shared boundary receipt]]
checks the nested character Gram formulas, the explicit Pauli-tensor
clock calculation, finite rate-selection quotients, and annular
left-gradient cancellation with the restart tests. Its
[[gauge-boundary-frame-gluing/receipts/boundary-charge-gluing-receipt-output.txt|stored output]]
does not replace the full-domain arguments above.

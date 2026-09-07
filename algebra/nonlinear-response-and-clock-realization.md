# Nonlinear Response and Classical Clock Realization

A closed gradient response determines two invariant normal-response graphs and, under an explicit normal-to-clock prescription, a classical stationary action with potential equal to half the squared response. The construction constrains nonlinear interactions when the response is independently selected. It does not automatically extend the linear boundary construction's conserved Hilbert norm, unitary clock or Fock realization.

## The response and its two graphs

Let \(U\) be an open subset of a finite-dimensional real inner-product space \(Q\). Fix this metric, take \(W\in C^3(U;\mathbb R)\), and define

\[
N(q)=\nabla W(q),\qquad
V(q)=\frac12\|N(q)\|^2.
\tag{NR1}
\]

The response operates on configurations, not on quantum states. Its derivative \(DN(q)\) is symmetric, and

\[
\nabla V(q)=DN(q)^*N(q)=DN(q)N(q).
\tag{NR2}
\]

Use the metric to identify the cotangent carrier \(T^*U\) with pairs \((q,p)\), with canonical form

\[
\sigma((v,w),(v',w'))=\langle v,w'\rangle-\langle w,v'\rangle.
\tag{NR3}
\]

The two response graphs \(\mathcal L_\pm=\{(q,\pm N(q))\}\) are exact Lagrangian: the canonical one-form \(\langle p,dq\rangle\) restricts to \(\pm dW\). Consider the Euclidean normal equations

\[
q'=p,\qquad p'=+\nabla V(q),\qquad
H_E(q,p)=\frac12\|p\|^2-V(q).
\tag{NR4}
\]

Both graphs are invariant wherever their flows exist. Indeed, on either graph,

\[
q'=\pm N(q),\qquad
p'=\pm DN(q)q'=DN(q)N(q)=\nabla V(q).
\tag{NR5}
\]

They lie on \(H_E=0\). This proves invariance, not completeness, attraction or the existence of a decaying trajectory from every configuration.

If one starts only with a closed response one-form \(N^\flat\), these statements hold locally with a potential \(W\). Globally, closedness still makes the graphs Lagrangian, but exactness of \(N^\flat\) is needed for a single-valued global \(W\) and the endpoint formulas below.

Unlike the linear [[algebra/cauchy-response-and-local-action|opposed-boundary construction]], nonlinear graphs are not vector subspaces whose sum supplies a canonical linear pair decomposition. Here the cotangent carrier and its canonical pairing are explicit inputs.

## A selected decaying bulk branch supplies the response

There is a converse interpretation of (NR1) that identifies the response with an actual boundary derivative. Suppose a smooth bulk potential \(V_{\rm bulk}\), a fixed critical point \(q_*\), and a regular branch of trajectories \(\gamma_q\) satisfy

\[
\gamma_q''=\nabla V_{\rm bulk}(\gamma_q),\qquad
\gamma_q(0)=q,\qquad
(\gamma_q,\gamma_q')\longrightarrow(q_*,0).
\tag{NR6}
\]

Assume their subtracted Euclidean actions are finite and depend smoothly enough on \(q\) to differentiate the improper integral. More precisely, require local convergence of the action and its first variation, and the terminal condition
\(\langle\gamma_q'(T),\partial_q\gamma_q(T)[v]\rangle\to0\).
Define

\[
W(q)=\int_0^\infty
\left[\frac12\|\gamma_q'\|^2+
V_{\rm bulk}(\gamma_q)-V_{\rm bulk}(q_*)\right]d\tau.
\tag{NR7}
\]

Integration by parts, using (NR6), leaves only the initial endpoint:

\[
dW(q)[v]=-\langle\gamma_q'(0),v\rangle,
\qquad N(q)=-\gamma_q'(0).
\tag{NR8}
\]

The conserved Euclidean energy gives the Hamilton–Jacobi identity

\[
\boxed{\frac12\|N(q)\|^2
=V_{\rm bulk}(q)-V_{\rm bulk}(q_*).}
\tag{NR9}
\]

The vacuum subtraction is essential: a boundary velocity cannot select an additive constant in the bulk potential. To apply the preceding smooth-graph theorem, require the selected response to be \(C^2\). If the selected branch is also consistent under restriction to a later starting time, then \(\gamma_q'=-N(\gamma_q)\). Uniqueness within the selected class is one sufficient condition for this consistency.

A global branch is not supplied by positivity of a potential. Multiple decay endpoints, competing trajectories, loss of smooth projection to \(q\), and escape can prevent a single smooth response map. The theorem applies on a domain where its branch assumptions hold.

The [[algebra/positive-boundary-response-from-decaying-extensions|decaying-extension construction]] proves these branch assumptions locally for an analytic finite-dimensional potential with positive nondegenerate quadratic stiffness. Its Green contraction constructs the gradient and fixes all higher coefficients together. Its nonzero quadratic scale and configuration metric remain inputs; the result is not a branch theorem at a quartic gauge origin.

Conversely, start with (NR1) and suppose the gradient trajectory \(\gamma'=-N(\gamma)\) exists for all \(\tau\geq0\), stays in the domain, and converges to a response zero \(q_*\). It then obeys (NR6) with \(V_{\rm bulk}=V\). For any admissible curve from \(q\) to that same endpoint, with finite action, the chain rule gives

\[
\begin{aligned}
E[\gamma]
&=\int_0^\infty\left[\frac12\|\gamma'\|^2
+\frac12\|N(\gamma)\|^2\right]d\tau\\
&=W(q)-W(q_*)+
\frac12\int_0^\infty\|\gamma'+N(\gamma)\|^2d\tau.
\end{aligned}
\tag{NR10}
\]

Thus an existing gradient-decay trajectory minimizes this specified action and has cost \(W(q)-W(q_*)\). The minimization statement does not select an upstream ontology by itself; it is a consequence of the supplied gradient response and metric.

## The clock prescription and its action

Keep the same kinetic metric but reverse the potential sign in the normal Hamiltonian:

\[
H_C(q,p)=\frac12\|p\|^2+\frac12\|N(q)\|^2,
\qquad
\dot q=p,\quad \dot p=-DN(q)^*N(q).
\tag{NR11}
\]

This is the proposed normal-to-clock prescription, not an inference that every directed process must realize it. Its flow is locally Hamiltonian and reversible under \((t,q,p)\mapsto(-t,q,-p)\). Global evolution needs its own completeness assumptions. The normal graphs generally are not invariant under this clock: their tangent acceleration in (NR5) has the opposite sign.

For smooth paths on a finite interval, with variations of \(q\) fixed at the endpoints and arbitrary variations of \(p\), the canonical action is

\[
S[q,p]=\int dt\left[
\langle p,\dot q\rangle-\frac12\|p\|^2
-\frac12\|N(q)\|^2\right].
\tag{NR12}
\]

Variation gives exactly (NR11). Eliminating \(p=\dot q\) yields

\[
\boxed{S[q]=\frac12\int dt
\left[\|\dot q\|^2-\|N(q)\|^2\right].}
\tag{NR13}
\]

This is an exact classical action, local in its chosen parameter. It is not yet a spatially local field action, and \(t\) has not been calibrated as physical duration. On a curved configuration manifold, the metric, covector momentum and covariant derivatives must be retained; the fixed-metric formulas cannot simply be copied unchanged.

There are two different achievements. Defining \(V\) from an independently selected \(N\) is a response-to-clock realization. Starting from \(V_{\rm bulk}\), computing its decaying response, and returning (NR9) recovers the original potential up to its constant; it does not independently explain why that bulk potential was selected.

## A cubic response constrains three potential coefficients

Take one real configuration coordinate and

\[
N(q)=a q+\lambda q^3,\qquad
W(q)=\frac a2q^2+\frac\lambda4q^4,
\qquad a>0,\quad\lambda\geq0.
\tag{NR14}
\]

Every initial value has a global forward gradient decay to zero:

\[
q(\tau)=\frac{q_0e^{-a\tau}}
{\sqrt{1+(\lambda/a)q_0^2(1-e^{-2a\tau})}}.
\tag{NR15}
\]

The returned potential and clock equation are

\[
V(q)=\frac{a^2}{2}q^2+a\lambda q^4+
\frac{\lambda^2}{2}q^6,
\qquad
\ddot q+a^2q+4a\lambda q^3+3\lambda^2q^5=0.
\tag{NR16}
\]

Writing \(V=c_2q^2+c_4q^4+c_6q^6\), this forces

\[
c_4^2=4c_2c_6,\qquad c_2>0,\quad c_4,c_6\geq0.
\tag{NR17}
\]

This is a genuine coefficient restriction within the cubic-response family. It becomes predictive only when the cubic response is selected independently of a desired sextic potential. The linear rate \(a\) is still an input; setting it to one would choose units, not derive a nonzero physical scale.

Branch selection also matters in the simpler formal example \(N(q)=q^2\), \(W=q^3/3\), \(V=q^4/2\). The curve \(q_0/(1+q_0\tau)\) decays for \(q_0>0\), but blows up in finite positive time for \(q_0<0\). The actual zero-energy decay on the negative side instead obeys \(q'=+q^2\). Combining both stable sides gives

\[
N_{\rm st}(q)=q|q|,\qquad W_{\rm st}(q)=\frac13|q|^3.
\tag{NR18}
\]

The stable response is only \(C^1\) at zero, and its value function is only \(C^2\). Squaring the response therefore forgets information about the smoothness and orientation of its decaying branch. The original polynomial response is not the globally selected stable response of its squared potential.

## A moving Hessian is not a conserved Hilbert metric

At a response zero \(q_*\),

\[
\operatorname{Hess}V(q_*)=DN(q_*)^*DN(q_*).
\tag{NR19}
\]

The classical linearized clock frequencies are the singular values of \(DN(q_*)\). This local statement neither supplies a quantum Hamiltonian nor proves an energy gap on a complete state carrier. In particular, \(DN(q_*)=0\) means a zero linearized classical frequency, not a theorem of quantum gaplessness.

Even strict positivity of a nonlinear slope does not preserve the linear construction. In one dimension, put \(\alpha(q)=N'(q)>0\) and copy its tangent metric and complex structure:

\[
G(q)=\begin{pmatrix}\alpha&0\\0&\alpha^{-1}\end{pmatrix},
\qquad
J_q(v,w)=(-\alpha^{-1}w,\alpha v).
\tag{NR20}
\]

They satisfy \(J_q^2=-1\) and \(G(J_q\cdot,J_q\cdot)=G\) pointwise. But for the clock vector field \(B(q,p)=(p,-\alpha N)\), direct differentiation gives

\[
\boxed{\mathcal L_B G=
\begin{pmatrix}
p\alpha'&-\alpha'N/\alpha\\
-\alpha'N/\alpha&-p\alpha'/\alpha^2
\end{pmatrix}.}
\tag{NR21}
\]

For (NR14) with \(\lambda>0\), the off-diagonal entry is nonzero at every \(q\neq0\). The derivative of the nonlinear clock therefore does not preserve this candidate tangent metric. Replacing the fixed linear response operator by \(DN(q)\) has not produced a fixed Hermitian state space with unitary evolution.

The [[algebra/opposed-response-polarization-and-kahler-completion|opposed-pair construction]] supplies two explicit alternatives to that pointwise substitution. Its polar completion uses the geometric mean of the two response Hessians, while a constant exchange prescription gives an integrable Kähler metric. For the same convex-quartic response family, the latter admits a complete isometric circle action whose moment function fixes a different Hamiltonian and action. This is a constructive compatible clock, but not a proof that the present squared-response clock preserves that geometry or that either clock is uniquely selected.

The [[algebra/quotient-clock-and-stationary-action|stationary state-action theorem]] starts with an already selected complex positive realization and linear quotient clock. Equations (NR11)–(NR13) instead return a classical nonlinear phase flow. A Hilbert carrier, quantum generator, operator domains, quantization and vacuum require additional construction; none follows merely from the exact Lagrangian graphs or the squared-response identity.

[[algebra/response-factorization-and-the-vacuum|Response factorization]]
provides one declared quantum realization and its divergence correction.
[[directed-analytic-realization/chern-simons-response-and-gauge-action|Gauge transgression]]
supplies a different, independently defined nonlinear response. Its
[[algebra/absolute-hessian-and-response-integrability|positive-Hessian test]]
shows why pointwise linear algebra cannot replace a compatible response
over the configuration carrier.

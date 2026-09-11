---
inq.module: "coarse-response-memory"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
keywords: [hidden response, memory kernel, compression, spectral measure, visible gap]
---
# Coarse Response Memory

Removing hidden variables from an evolution does not generally produce another autonomous evolution on the retained variables. It produces a frequency-dependent response: the hidden sector can receive a disturbance, retain it, and return it later. The static least-cost response is only its zero-frequency limit. This distinction gives both a quantitative gap criterion and an explicit example where an apparently fast local rate misses a slow physical mode.

**Status: [EXACT] for the stated self-adjoint block setting and the finite reversible and compact-group examples; [CONDITIONAL] for a physical application supplying that block decomposition and uniform estimates; [OPEN] for the Yang--Mills continuum construction or a cosmological realization.** No assumption about fundamental randomness is made.

## What the operator operates on

Let \(\mathcal H\) be a Hilbert space of variations, with a specified nonnegative self-adjoint generator \(L\). A chosen readout is an isometry \(J:\mathcal H_R\to\mathcal H\). Write
\[
P=JJ^*,\qquad Q=I-P,\qquad
\mathcal H=\mathcal H_R\oplus\mathcal H_H,\qquad
L=\begin{pmatrix}A&B^*\\B&C\end{pmatrix}.
\tag{CM1}
\]
Thus \(B:\mathcal H_R\to\mathcal H_H\) carries a retained variation into its hidden response, and \(B^*\) carries a hidden response back. These are maps of variations, not maps selecting measurement outcomes.

For the theorem below assume \(A,C\ge0\) self-adjoint, \(B\) bounded, and \(D(L)=D(A)\oplus D(C)\). Every bounded nonnegative \(L\) with an orthogonal readout satisfies this setting. An unbounded field generator with a general conditional expectation need not: projection invariance of its form domain and the off-diagonal extension must be checked.

[[local-score-bounds-and-the-order-of-hidden-response|The physical plaquette application]]
now proves those form-domain controls in a different, explicitly
unbounded setting. Its hidden coupling is bounded from the retained
energy domain to hidden \(L^2\), giving a form-valued memory resolvent
without assuming a hidden gap. Joining two trace readouts can raise
the hidden differential order, so this is not a license to use the
bounded-block theorem on arbitrary regional joins.

[[boundary-interaction-and-conditional-score-budget|Retaining the full regional links]]
instead gives a first-order hidden response. The crossing Wilson
interaction bounds its integrated conditional score covariance,
through an exact split into relative vacuum deformation and energy
lowering. That boundary budget controls gradient-sup readouts;
the available full form-domain bound still counts retained links.
The covariance is exactly a squared differentiation–forgetting
defect, not a multiplication associator or a positive mass floor.

For a reversible Markov law \(\mu\) and measurable readout \(r\), the canonical example is
\[
\mathcal H=L^2(\mu),\quad
\mathcal H_R=L^2(r_*\mu),\quad Jf=f\circ r.
\tag{CM2}
\]
Here \(P\) is conditional expectation onto the readout algebra. For a spectral-gap statement, remove the actual vacuum first, retain its orthogonal complement, and require that the readout preserve the vacuum splitting. A chosen reference constant is not automatically the physical vacuum.

## Eliminating the hidden evolution leaves a memory kernel

Let \(R_t=J^*e^{-tL}J\). Starting from \((f,0)\), the block equations are
\[
\dot x=-Ax-B^*y,\qquad
\dot y=-Bx-Cy,\qquad x(0)=f,\quad y(0)=0.
\]
Variation of constants gives
\[
y(t)=-\int_0^t e^{-(t-s)C}Bx(s)\,ds.
\]
Consequently
\[
\boxed{\dot R_t=-AR_t+\int_0^t M(t-s)R_s\,ds,\qquad
M(t)=B^*e^{-tC}B,\qquad R_0=I.}
\tag{CM3}
\]
The derivative equation holds on the generator domain; the corresponding integrated mild equation holds on all retained vectors. For nonzero initial hidden data \(y_0\), add the forcing \(-B^*e^{-tC}y_0\). A statistical treatment of that forcing requires a state or preparation law; the algebra does not declare it ontically random.

For real \(z>0\), its Laplace transform is the exact Schur resolvent
\[
\boxed{\widehat R(z)=J^*(z+L)^{-1}J
=\big[z+A-\Sigma(z)\big]^{-1},\qquad
\Sigma(z)=B^*(z+C)^{-1}B.}
\tag{CM4}
\]
This follows either by eliminating the hidden block of \(z+L\) or by transforming (CM3). It is an operator identity, not a fitted memory ansatz. If \(\mathsf E_C\) is the spectral measure of \(C\), the same hidden response measure determines
\[
M(t)=\int e^{-t\lambda}\,B^*d\mathsf E_C(\lambda)B,\qquad
\Sigma(z)=\int\frac{B^*d\mathsf E_C(\lambda)B}{z+\lambda}.
\tag{CM5}
\]
In particular \(M(t)\ge0\), and the derivatives of \(\Sigma\) alternate in operator order. This positivity concerns response on a Hilbert space, not pointwise positivity of every matrix entry.

[[library/optimal-prediction-and-the-mori-zwanzig-representation-of-irreversible-processes/inq|Chorin, Hald and Kupferman]] give the projection/Dyson memory construction in a more general dynamical setting. Equations (CM3)--(CM5) are the explicit self-adjoint specialization proved here, not a new attribution of a Wilson estimate to that source.

[[spectral-readout-and-the-visible-gap|The complete spectral readout]]
retains the whole generator's compressed spectral measure, even without
the block-domain assumptions used for (CM3)--(CM5). Its first moment is
the pulled-back form, while its full support controls the visible
threshold. [[algebra/expected-inclusions-and-mirror-clock-consistency|A correlated matrix inclusion]]
realizes this distinction explicitly: exactly matching local forms
coexist with two-frequency return and a centered readout with a
persistent zero-frequency component.

[[algebra/occupation-conditioned-clocks-and-the-vacuum-boundary|Occupation-conditioned clocks]]
give another exact source of this distinction: one whole spectral law
supplies the conditioned rates, but forgetting their label produces a
nonautonomous mixture. Its spectral-minimal carrier can have a unique
vacuum while failing to reduce the specified visible observable algebra.

## Zero frequency and the first retained metric

Suppose \(C\ge c_HI\) for \(c_H>0\). The symbol \(c_H\) is a hidden-generator bound, not the speed of light. Define
\[
S=A-B^*C^{-1}B,\qquad
Z_0=I+B^*C^{-2}B.
\tag{CM6}
\]
The static short \(S\) minimizes the whole quadratic form over hidden representatives:
\[
\langle(x,y),L(x,y)\rangle
=\langle x,Sx\rangle+
\|C^{1/2}(y+C^{-1}Bx)\|^2.
\tag{CM7}
\]
[[trace-dirichlet-descent/inq|Trace Dirichlet descent]] owns this least-cost construction and its distinction from the pullback \(A\). Neither \(S\) nor \(A\) is generally the generator of \(R_t\).

The new metric has an exact geometric meaning. The harmonic lift is \(h x=(x,-C^{-1}Bx)\), so \(h^*Lh=S\) as a form and \(h^*h=Z_0\). Thus the whole norm of a least-cost representative is \(\langle x,Z_0x\rangle\), not \(\|x\|^2\). Its Rayleigh quotient is \(\langle x,Sx\rangle/\langle x,Z_0x\rangle\). Restricting to this harmonic graph does not find the full spectrum, but it explains why a static response must be paired with an induced norm before being read as a rate.

The first frequency correction is a positive metric, not another arbitrary scalar rate. Spectral calculus gives, for real \(z\ge0\),
\[
\begin{aligned}
z+A-\Sigma(z)&=S+zZ_0-\mathcal R(z),\\
\mathcal R(z)&=z^2B^*C^{-2}(C+z)^{-1}B,\\
0\le\mathcal R(z)&\le\frac{z^2}{c_H+z}(Z_0-I).
\end{aligned}
\tag{CM8}
\]
Thus \(S+zZ_0\) is a controlled low-frequency response denominator when \(z/c_H\) is small. This is not yet a uniform error bound for its inverse or for long-time trajectories: inverse estimates also require distance from the relevant spectrum.

The same denominator continued to \(z=-E\), for \(0<E<c_H\), is
\[
A-E-B^*(C-E)^{-1}B.
\tag{CM9}
\]
Its singularities detect retained spectral modes. A static positive number from \(S\) is therefore not, by itself, their physical decay exponent.

## A sharp three-quantity lower bound

On the complete nonvacuum splitting, assume
\[
C\ge c_HI,\qquad S\ge sI,\qquad
k=\|C^{-1}B\|<\infty,\qquad c_H,s>0.
\tag{CM10}
\]
Then
\[
\boxed{
L\ge\delta I,\qquad
\delta=\frac{s+c_H+c_Hk^2-\sqrt{(s+c_H+c_Hk^2)^2-4sc_H}}2>0.}
\tag{CM11}
\]
To prove this when \(k>0\), test \(L-\delta I\) by its hidden Schur complement. Put \(D=C^{-1}B\). For \(0<\delta<c_H\),
\[
\begin{aligned}
A-\delta-B^*(C-\delta)^{-1}B
&=S-\delta-\delta D^*C(C-\delta)^{-1}D\\
&\ge\left[s-\delta-\frac{\delta c_H k^2}{c_H-\delta}\right]I.
\end{aligned}
\]
The smaller root in (CM11) makes the last bracket zero. If \(k=0\), the blocks decouple and the bound is \(\min(s,c_H)\). The scalar blocks \(C=c_H,\ B=c_Hk,\ A=s+c_Hk^2\) attain (CM11), so the bound cannot be improved using only these three quantities.

Equivalently,
\[
\frac{\delta}{c_H}
=\frac{r+1+k^2-\sqrt{(r+1+k^2)^2-4r}}2,\qquad r=s/c_H.
\tag{CM12}
\]
This is the useful quotient: static retained stiffness and hidden relaxation must be compared together with their coupling. Under \(L\mapsto aL\), \(r,k,\delta/c_H\) are unchanged. Geometry may constrain those dimensionless relations; it does not thereby select the dimensional clock.

The scalar root is the existing [[yang-mills-continuum-crossover/two-scale-rg-descent-and-the-crossover-lemma#A conditional-Fisher version for Poincare bounds|two-scale Fisher budget]] with \((\rho,\lambda,C_{\mathrm{Fisher}})=(c_H,s,c_Hk^2)\), not a new numerical constant. The additional content here is its operator-memory interpretation and the positive metric \(Z_0\). It assumes estimates for \(S,C,B\); positivity or elimination alone supplies none of the required uniform constants.

There is also a direct static-approximation check. Since
\(0\le\Sigma(0)-\Sigma(z)\le zk^2I\), inverse order gives
\[
[(1+k^2)z+S]^{-1}\le\widehat R(z)\le[z+S]^{-1},
\qquad
\|\widehat R(z)-(z+S)^{-1}\|
\le\frac{zk^2}{(z+s)^2}.
\tag{CM12a}
\]
The norm estimate follows by the resolvent identity. These are resolvent bounds, not pointwise bounds between exponential semigroups: the exponential is not operator monotone.

## A fast instantaneous rate with a slow observable tail

Consider the symmetric three-state chain, in orthonormal coordinates for its uniform stationary Hilbert space,
\[
L_\varepsilon=
\begin{pmatrix}
1&-1&0\\
-1&1+\varepsilon&-\varepsilon\\
0&-\varepsilon&\varepsilon
\end{pmatrix},\qquad \varepsilon>0.
\tag{CM13}
\]
Retain only whether the state is \(1\) or in \(\{2,3\}\). The normalized centered retained and hidden vectors are
\[
f=(2,-1,-1)/\sqrt6,\qquad h=(0,1,-1)/\sqrt2.
\]
On the centered space,
\[
A=\frac32,\quad B=-\frac{\sqrt3}{2},\quad
C=\frac12+2\varepsilon,\quad
S=\frac{6\varepsilon}{1+4\varepsilon}.
\tag{CM14}
\]
The exact centered return is
\[
\begin{aligned}
r_\varepsilon(t)&=\alpha e^{-\lambda_-t}+(1-\alpha)e^{-\lambda_+t},\\
\lambda_\pm&=1+\varepsilon\pm\sqrt{1-\varepsilon+\varepsilon^2},\\
\alpha&=\frac{\lambda_+-3/2}{\lambda_+-\lambda_-}.
\end{aligned}
\tag{CM15}
\]
As \(\varepsilon\downarrow0\), the actual gap is \(\lambda_-\sim3\varepsilon/2\), with retained weight \(\alpha\to1/4\), although \(A=3/2\) never changes. The static short behaves as \(6\varepsilon\); dividing by \(Z_0\to4\) recovers the leading slow exponent. Formula (CM11) is exact in this scalar block example.

Each full-space readout compression is reversible and Markov, but its family is not a semigroup:
\[
r_\varepsilon(2t)-r_\varepsilon(t)^2
=\alpha(1-\alpha)
\big(e^{-\lambda_-t}-e^{-\lambda_+t}\big)^2>0
\tag{CM16}
\]
for \(t>0\). A smaller state space did not eliminate the physical slow mode; it placed that mode in a memory-dependent return.

[[gauge-star-state-and-hidden-clock|The compact gauge-star example]] makes
the distinction on an actual \(SU(2)\) profile and Haar-reference source.
Its entire output state and rebuilt clock remain fixed, while the
visible spectral edge tends to zero with a nonvanishing character
weight. The two-leaf extension preserves this failure after endpoint
charges are paired into a neutral relative loop: a fixed positive
amount of spectral weight enters a shrinking energy interval.
For general finite stars, the first compression defect is the
conditional covariance of the hidden drift. This calculation uses
strong differentiation on smooth readouts rather than assuming the
bounded off-diagonal block required by (CM3).

[[interacting-gauge-vacuum-and-local-memory|The actual interacting gauge
vacuum]] now supplies a physical version of this coefficient. It is
the conditional variance of the vacuum's logarithmic score along a
retained plaquette. The leading term counts adjacent plaquettes, and
one-link variational and resolvent comparisons give volume-uniform
upper bounds without an explicit vacuum solution. Those bounds do not
supply the hidden and retained lower bounds in (CM10).

[[two-plaquette-vacuum-and-relational-state|The interacting two-plaquette state]]
cannot close on separate traces at any positive magnetic coupling.
Its complete relational basis supplies actual finite-coupling
conditional-memory calculations and a two-rate finite-time
perturbative return. The vacuum and its moving readout projection
are retained together; replacing that return by the exponential
of its first moment would lose the derived hidden channels.

[[radial-marginal-and-conditional-stress|Its radial marginal]]
has a positive-curvature result at small coupling, but
its effective force retains the divergence of the full
conditional information tensor. Orbit stress is invisible
to the scalar coupling coefficient and can take either
sign. Thus a positive local metric alone cannot replace
the joint state or close the memory-dependent return.
[[heat-preparation-and-latitude-coercivity|Its actual Haar preparation]]
has a marginal Poincare bound at least the electric coefficient
for every preparation time and at the ground-state limit,
throughout a fixed small-coupling range. The proof controls a
combined source from the full evolution, despite failure of
conditional convexity itself. At sufficiently large coupling,
the same bound also holds throughout each prescribed bounded
interval of magnetic preparation time; this separate theorem
does not reach the large-coupling ground state.
Neither argument freezes the hidden
state or turns the marginal into an autonomous physical clock.
An explicit conditional holonomy bound and the existing
two-scale comparison lift the ground-state marginal estimate
to the full finite carrier in that regime. The hidden bound
deteriorates with coupling; it supplies no continuum margin.

[[positive-amplitude-kernel-and-preparation|The shared-path kernel realization]]
then exposes a stronger state constraint: the amplitude itself
is a positive Gram kernel, and the physical marginal is the
diagonal of its normalized square. The same supplied evolution
is completely positive on kernels. Yet a rank-ten positive-feature
kernel with both marginals exactly Haar develops positive
latitude curvature. A concrete inequality between its first
two relative moments detects that failure. Positivity and
matched local laws do not replace the actual preparation.

[[replica-weighted-correlations-and-the-local-readout|Squaring that prepared kernel]]
forces an overlap-weighted mixture of one-loop laws.
Some admissible hidden contributions violate the proposed
relative-moment bound, so a componentwise proof is excluded.
The actual local curvature is a posterior mean curvature
plus a positive source-score variance. Its sign remains an
estimate on the prepared mixture, not a consequence of
averaging to a convolution state or of kernel positivity.

[[path-source-tilts-and-the-curvature-budget|The fully resolved path sources]]
make the component curvature explicit: each conjugation-averaged
spherical tilt is log-concave. The actual posterior variance and
geometric curvature can be computed separately at the poles.
Both grow quadratically at late preparation times while their
difference converges, ruling out any time-uniform fractional
separation. A successful estimate must keep their correlated
cancellation, even in this finite compact system.

[[certified-ground-marginal-and-late-preparation|An additive remainder certificate]]
now proves the needed marginal shape at \(\kappa=\lambda=1\)
for the full ground vector and every positive preparation time.
A cubic initial-layer bound, exact time--latitude rectangles
and contraction toward the ground cover the complete trajectory.
This closes the fixed-system estimate left open by the source
budget; neither sampling nor separate source positivity proves it.
[[pointed-preparation-stability-and-the-volume-test|The reusable pointed-flow estimate]]
also exposes its limitation: global comparison norms grow on
independent copies even while the gap stays fixed.
[[connected-preparation-and-local-normalization|Connected log-preparation]]
removes those disconnected contributions exactly and gives their
assembly equation.
[[kinetic-smoothing-and-connected-fourier-control|Retaining kinetic smoothing]]
now closes a representation-weighted connected norm at an explicit
small interaction-to-kinetic ratio, uniformly in volume and time.
It constructs the actual prepared logarithm and bounds how its local
score changes when distant interactions are removed. The instantaneous
quadratic map fails in the same norm; its kinetic inverse is essential.

[[kinetic-hessian-bootstrap-and-uniform-response|A complementary geometric bootstrap]]
controls the actual full logarithmic Hessian and conditional covariance
for every raw cut in a stated small \(SU(2)\) regime. Its ground limit
gives an operator bound for hidden response without an extensive
boundary factor. The point is explicit state-and-readout control,
not a newly discovered existence of a strong-coupling lattice gap.
Extending either estimate beyond its smallness condition and through
the continuum trajectory remains open.

[[interacting-reference-and-spectral-product-control|The interacting-reference test]]
now identifies what such an extension costs. Re-centering on actual
block grounds preserves the connected law, and a small reference
drift gives a sufficient derivative bound. But a block gap alone
does not preserve the spectral product inequalities: a gapped
compact counterexample develops a forbidden Haar energy channel.
Crossing interactions also require the full boundary-charged block
carrier, not only its separately neutral spectrum.
[[block-spectral-moments-and-connected-assembly|Four local spectral product moments]]
give a precise sufficient replacement: if certified on the complete
blocks, they imply the connected inverse estimate uniformly in the
number of blocks. But absolute eigenbasis sums can acquire unbounded
degeneracy costs even on the Haar block; those hypotheses are not
basis-independent consequences of squared spectral control.

[[first-order-lift-and-spectral-product-tails|Factoring the actual kinetic operator]]
instead controls fixed-multiplier transfer between entire energy
windows, at every internal Wilson coupling and input energy, without
a gap assumption or a count of eigenvectors. For a single charged
link probe, [[charged-link-probes-and-vacuum-spectral-width|the exact spectral width]]
is proportional to the link's vacuum score energy, with the same
ratio for every spin. These constrain readout, state and supplied
dynamics together. Closing arbitrary two-input products under block
assembly, and selecting those supplied dynamics, remain separate
obligations; upper spectral tails do not exclude soft excitations.

For arbitrary two inputs, the second-order Hilbert norm and its
dyadic spectral variant fail by concentration on one fixed raw
Wilson block. [[transition-score-and-lipschitz-product-control|Transition-score covariance]]
instead gives a bounded nonlinear response in the homogeneous
Lipschitz quotient, uniformly over independent copies of fixed
blocks. Its constants are explicit finite block data; they do not
control an extensive source or remain uniform along the continuum
trajectory.

[[product-boundary-frames-and-crossing-susceptibility|The crossing-state test]]
exposes a separate structural cost. Exact independent regional
vacua still give Haar crossing holonomy and a nonzero neutral
susceptibility at the electric scale. Final whole-gauge projection
leaves that product vector unchanged. A reference that improves
this cost must include actual shared boundary correlations, not
only better internal spectra and separately neutral states.

## Use the physical bounded defect when domains are difficult

For an actual positive injective physical transfer
\[
T_\tau=e^{-\tau(H-E_0)/\hbar},\qquad L=I-T_\tau,
\tag{CM17}
\]
all blocks in (CM1) are bounded. If (CM10) is proved for this \(L\) on the full physical vacuum complement, then (CM11) gives, for \(0<\delta<1\),
\[
H-E_0\ge-\frac{\hbar}{\tau}\log(1-\delta)\,Q_{\mathrm{vac}}.
\tag{CM18}
\]
Here \(e^{-tL}\) is an auxiliary bounded-defect evolution, not physical clock time. The physical conclusion follows from functional calculus of the supplied \(T_\tau\), not from renaming the memory parameter. If the slab is calibrated by length \(\ell=c\tau\), replace \(\hbar/\tau\) by \(\hbar c/\ell\).

This gives a domain-safe operator signature for the next Yang--Mills estimate: a derived readout, a hidden defect floor \(c_H\), a retained short floor \(s\), and a bounded return coupling \(k\), all controlled along the actual continuum trajectory. The [[temporal-column-response/spatial-elimination-and-self-return|static column comparison]] is a different estimate on conditional laws; it does not supply these physical blocks.

Nothing in the construction privileges large or small systems. A cosmological application would still need its own state, readout and evolution before the same response signature could be compared with the vacuum one. [[global-local-response-reconstruction/cosmological-reconvergence-contract|Cosmological reconvergence]] owns that additional common-source requirement.

[[coarse-response-memory/receipts/coarse_response_memory_receipt.py|The finite receipt]] checks the block resolvent, memory equation, frequency remainder, sharp gap bound and full three-state conditional readout. It tests algebraic calibrations, not the missing continuum estimates.

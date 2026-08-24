# Record--Scale Soldering

The tick of ontological time, cosmic expansion, entropy increase, and gravitational area can be representations of one mathematical process only if their separate orders and cocycles are joined by explicit natural maps. A strict record--scale criterion is available: an exact additive logarithmic scale cocycle orients factual history when it is presentation-invariant, path-independent, and strictly positive on every proper record extension. Entropy, horizon area, and acceleration require further welds; monotone expansion alone does not imply a metric clock, an entropy law, gravity, or accelerated expansion.

## The proposed common process

Let \(W\subseteq\mathsf P\) be the subgroupoid of reversible presentation changes inside a category of admissible physical processes, and let

$$
\mathcal R:\mathsf P\longrightarrow\mathsf{Rec}
$$

be a record functor that sends \(W\) to record isomorphisms. A fact-producing process \(p:x\to y\) should induce a proper inclusion

$$
\mathcal R(p):
\mathcal R(x)\lhook\joinrel\longrightarrow\mathcal R(y)
$$

that preserves the earlier values. This is the candidate order of ontological time.

Independently, suppose a scale realization assigns each process a positive scale ratio

$$
r(p)>0
$$

with

$$
r(q\circ p)=r(q)r(p),
\qquad
r(w)=1\quad(w\in W).
$$

Its logarithm

$$
n(p):=\ln r(p)
$$

is an additive one-cocycle:

$$
\boxed{
n(q\circ p)=n(q)+n(p),
\qquad
n(w)=0.}
$$

In an FLRW realization this becomes \(n=N_y-N_x\) with \(N=\ln(a/a_*)\), but the categorical definition does not presuppose FLRW.

## Record--scale orientation theorem

**Proposition.** Suppose the cocycle is exact: there is an object function \(N\) such that \(n(p)=N(y)-N(x)\) for every \(p:x\to y\). Suppose every arrow in the factual process category preserves prior records, \(n(p)\geq0\), and \(n(p)>0\) whenever \(\mathcal R(p)\) is a proper extension. Suppose also that every zero-increment arrow reachable in both directions is a declared physical equivalence. Then \(N\) descends through presentation equivalence to a strictly order-preserving function on proper extensions in the quotient factual reachability poset. In particular, no directed cycle can contain a proper record extension.

**Proof.** Since \(n(w)=0\) for \(w\in W\), exactness gives \(N(\operatorname{source}w)=N(\operatorname{target}w)\), so \(N\) is presentation-invariant. For a composable chain, additivity gives the sum of its nonnegative increments; if one arrow is a proper record extension, that sum is strictly positive. A directed cycle based at \(x\) has total increment \(N(x)-N(x)=0\), so it cannot contain a proper extension. Quotienting zero-increment two-way reachability by physical equivalence leaves a poset, and \(N\) is strictly increasing on every proper extension. \(\square\)

The exactness premise is substantive. A merely additive cocycle can have nonzero holonomy around an endomorphism and need not assign a unique scalar to an object. Equivalently, exactness requires path independence:

$$
n(p_1)=n(p_2)
$$

for any two admissible paths \(p_1,p_2:x\to y\), subject to the declared quotient. Without exactness or such a path-independence theorem, the cocycle grades arrows but does not define a global scalar time on objects.

This theorem states exactly what it would mean for cosmic scale to orient record time:

$$
\boxed{
\text{proper factual extension}
\Longrightarrow
\Delta N>0.}
$$

It does not prove the premise. A contracting branch, a bounce, a cyclic realization, or a fact-producing process at fixed scale would refute this minimal identification while leaving record order itself possible.

## Order is not yet tick rate

An order parameter does not determine elapsed proper time. A metric clock requires a further positive cocycle or one-form \(\mathrm d\tau\) and a soldering relation such as

$$
H
:=\frac{\mathrm dN}{\mathrm d\tau}.
$$

The value of \(H\) is the rate at which scale changes per realized proper-time interval. Neither composition of scale ratios nor record inclusion fixes it. Cosmic acceleration is one derivative further:

$$
\frac{\ddot a}{a}
=\dot H+H^2.
$$

It depends on a connection or dynamics on the realized history. In an imported GR--FLRW branch it is governed by the active stress-energy combination, as stated by [[causal-scale-theory/theorems/acceleration-condition|the CST acceleration theorem]]. Thus

$$
\text{record orientation}
\not\Longrightarrow
\text{clock rate}
\not\Longrightarrow
\text{acceleration}.
$$

A successful common construction may derive all three, but none is a change of notation for the previous one.

## Entropy is a second cocycle candidate

For a compatible tower of state-preserving conditional expectations, [[spectral-wall-descent/conditional-expectation-balance|the conditional-expectation theorem]] supplies nonnegative entropy gains and an exact orthogonal BKM split. In the finite tracial case,

$$
\Sigma_E(\rho)
:=S(E\rho)-S(\rho)
=D(\rho\Vert E\rho)
\geq0.
$$

For nested expectations satisfying the required common-reference and orthogonality conditions, the lost response increments add. Under stronger state and Markov compatibility, categorical log-dimensions and selected edge-entropy data may also compose. These are genuine algebraic candidates for a scale valuation.

They are not automatically functions of \(n\). The strong entropy--scale weld would require a natural law on one process family, for example

$$
\boxed{
\Sigma(p)=\kappa_S n(p)}
$$

or a more general natural transformation between the entropy-valued and scale-valued cocycles. The coefficient and domain must be derived; state dependence, correlations, changing centers, and infinite-index factual readout can obstruct scalar additivity.

The distinction also resolves the apparent qubit/bit paradox. A nonfaithful observational realization may erase distinctions and increase the entropy of its unconditioned output law without placing the erased distinctions in a unitary environmental register. [[algebra/nonfaithful-realization|The nonfaithfulness theorem]] shows why a genuinely forgetful cross-register map cannot be an equivalence.

## The exact FLRW shadow

On a spatially flat expanding \(3+1\)-dimensional FLRW apparent horizon with area-law entropy, [[conformal-scale-geometry/horizon-allocation|the horizon-allocation theorem]] gives

$$
\boxed{
\mathrm dN
=\mathrm d\widehat\zeta_A
+\frac14\,\mathrm d\ln S_A.}
$$

This is already an exact equality of additive differentials reconstructed from one history. It shows that scale, signed horizon motion, and logarithmic area growth possess the correct algebraic grammar to be shadows of one cocycle. It does not derive that history, make the terms independent charges, or identify \(\widehat\zeta_A\) with record time.

The upstream theorem target is a commutative realization diagram in which record growth, scale transport, and horizon geometry are natural images of the same process:

$$
\begin{array}{ccc}
\mathsf P_{\mathrm{fact}}
&\xrightarrow{\mathcal R}&
\mathsf{Rec}\\
{\scriptstyle\mathcal S}\downarrow
&&
\downarrow{\scriptstyle\mathrm{grade}}\\
\mathsf{ScaleHist}
&\xrightarrow{\ln r}&
(\mathbb R,+).
\end{array}
$$

The diagram must commute on physical arrows, not merely on one fitted FLRW trajectory. A future connection-level refinement may then lift the horizon allocation from a kinematic identity to a reduction of one common causal connection.

## Gravity and mass require a common carrier

The mathematical unity sought is not an untyped equality

$$
\text{lost information}
=\text{time}
=\text{space}
=\text{gravity}.
$$

It is a family of representations of one process law. The gravitational leg must place state response and geometry on the same realized tangent. The controlled AdS relation maps retained Fisher response to gravitational canonical energy in its declared regime; the independent central weld seeks to map selected edge entropy to spectral area. Neither theorem identifies the lost BKM block with curvature.

Mass-energy and curvature likewise meet through a covariant field equation or variational identity, not through semantic equivalence. Source-free gravitational degrees of freedom show that curvature is not generally reducible to local matter content. A stronger first-principles theory may derive both as images of one underlying process, but it must reproduce this distinction in its observable realization.

## Consequences for the causal programmes

The soldering criterion narrows several open problems.

- The CWST common-clock conjecture should first construct a record--scale natural transformation. A shared material clock is a later statement about the Lorentzian realization and its constrained matter sector.
- CST may use \(N\) as a homogeneous scale coordinate after FLRW is granted, but calling \(N\) ontological time requires positivity on proper record extensions, exactness or path independence, and observer-compatible records.
- The exact horizon allocation is a serious common shadow of scale and area growth, but it cannot derive dark-energy acceleration without a covariant response source.
- Entropy increase can accompany a nonunitary wall exactly in finite conditional-expectation models. Factual pointing and record stability remain distinct.

The brave claim is therefore mathematically admissible: time, expansion, entropy, and gravity may be aspects of one structure. The rigorous version is a programme of natural transformations and common cocycles, with acceleration supplied by the realized dynamics rather than by order alone.

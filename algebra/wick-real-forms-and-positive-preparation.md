# Wick Real Forms and Positive Preparation

For one positive boundary-response operator, Euclidean attenuation and reversible positive-frequency evolution are two analytic presentations of the same generator. Wick continuation changes both the parameter and the real slice of the value–response pair; its sign is not a declaration that irreversible record production has become reversible. A reflection-positive preparation kernel gives an explicit positive quotient and clock. These constructions clarify what a deeper process law would need to select, without presupposing that they already model factual directedness.

## One response, two real dynamical presentations

Let \(A\) be positive, injective and self-adjoint on a real Hilbert space. Work first on spectral subspaces bounded above and away from zero, so all expressions below have a common analytic domain. Use the [[algebra/cauchy-response-and-local-action|opposed-response pair]] \((q,p)\), where \(q\) is a boundary value and \(p\) its normal or canonical response.

On the complexified pair carrier define
\[
B_E=\begin{pmatrix}0&I\\A^2&0\end{pmatrix},
\qquad
B_L=\begin{pmatrix}0&I\\-A^2&0\end{pmatrix},
\qquad
C=\begin{pmatrix}I&0\\0&-iI\end{pmatrix}.
\tag{WR1}
\]
Multiplication gives
\[
\boxed{C^{-1}B_EC=-iB_L,\qquad
C^{-1}e^{itB_E}C=e^{tB_L}.}
\tag{WR2}
\]
The continuation is \(\tau=it\) together with \(p_E=-ip_L\). It is not a real coordinate change of the original pair. The equally valid conjugate convention must change both signs consistently.

The stable Euclidean graph has \(p_E=-Aq\) and \(q_E(\tau)=e^{-\tau A}q_0\). Under (WR2),
\[
p_L=-iAq,\qquad q_L(t)=e^{-itA}q_0.
\tag{WR3}
\]
This is the complex positive-frequency sector. A nonzero real classical wave includes its conjugate sector; it does not obey \(p_L=-iAq\) with both entries real.

For unbounded \(A\), growing Euclidean continuation is not bounded on the full pair completion. Formula (WR2) is first an analytic-core identity. The real-time group itself extends on the positive response completion by the unitary construction in the Cauchy note.

## The action sign follows from the same continuation

For analytic paths and the quadratic response potential, use the complex-bilinear continuations of the real pairings:
\[
S_E=\frac12\int
\big[(q_\tau,q_\tau)+(q,A^2q)\big]\,d\tau,
\qquad
S_L=\frac12\int
\big[(\dot q,\dot q)-(q,A^2q)\big]\,dt.
\tag{WR4}
\]
With \(\tau=it\), \(q_\tau=-i\dot q\), so on the corresponding contour
\[
S_E=-iS_L,\qquad e^{-S_E}=e^{iS_L}.
\tag{WR5}
\]
Using a Hermitian absolute square during this substitution would invalidate the calculation. The Green form also transforms bilinearly:
\[
\sigma(Cu,Cv)=-i\sigma(u,v).
\tag{WR6}
\]
These are identities of analytically continued expressions, not a theorem that an interacting path-integral measure exists or that its integration contour can be deformed without obstruction.

If \(A^2=-\Delta+m^2\) on a supplied spatial manifold, the equations are
\[
(-\partial_\tau^2-\Delta+m^2)q_E=0,
\qquad
(\partial_t^2-\Delta+m^2)q_L=0.
\tag{WR7}
\]
Their principal parts are respectively elliptic and hyperbolic. The opposite sign distinguishes the geometry of the returned differential equation. Locality depends on the square \(A^2\), not on the positivity of \(A\) alone. A gapped nonlocal response can fail the [[directed-analytic-realization/three-dimensional-boundary-test|local-propagation test]].

## Positive preparation constructs a quotient with that clock

On the complexified base Hilbert space, consider
\[
K(\tau)=\frac{e^{-|\tau|A}}{2A}.
\tag{WR8}
\]
For compactly supported positive-half test functions \(f(t)\) with values in a spectral subspace as above, define
\[
jf=\int_0^\infty (2A)^{-1/2}e^{-tA}f(t)\,dt.
\tag{WR9}
\]
Then the reflected form is exactly
\[
\begin{aligned}
Q(f)&=\int_0^\infty\!\!\int_0^\infty
\langle f(s),K(s+t)f(t)\rangle\,ds\,dt\\
&=\|jf\|^2\geq0.
\end{aligned}
\tag{WR10}
\]
The null space is \(\ker j\). The quotient completion is the base Hilbert space: the range of \(j\) is dense, since positive scalar time profiles give an invertible positive spectral multiplier on each bounded spectral band.

Delay a test function by \(a\geq0\), setting \((D_af)(t)=0\) for \(t<a\) and \(f(t-a)\) otherwise. Direct substitution gives
\[
jD_af=e^{-aA}jf.
\tag{WR11}
\]
Thus the quotient's positive semigroup is forced by its preparation kernel and delay law. The holomorphic family \(e^{-zA}\), \(\operatorname{Re}z>0\), has the strongly continuous boundary group \(e^{-itA}\). No second generator has been selected for this continuation.

This proves a particular positive-kernel quotient and clock, not the full Osterwalder–Schrader reconstruction of a four-dimensional interacting field theory. Its additional covariance, locality, distributional and limiting requirements remain those of [[algebra/os-descent-naturality-and-clock-no-go|OS descent naturality]] and [[lorentzian-spectral-envelope/inq|the Lorentzian spectral envelope]].

## What is lost, and what is not

The preparation map \(j\) can forget distinct half-histories: its kernel is generally nontrivial. For a scalar response \(A=a>0\), two different positive-half profiles with equal weighted integral have the same image. By contrast, \(e^{-sA}\) is injective at every finite \(s\geq0\), because its spectral multiplier never vanishes. For \(s>0\) and unbounded \(A\), its range is the dense proper domain \(\operatorname{Dom}(e^{sA})\), and its inverse there is unbounded. At \(s=0\) it is the identity. Unstable recovery is not literal many-to-one erasure.

Consequently three different operations coexist:

- quotienting preparation histories by \(\ker j\);
- attenuation of their retained data by \(e^{-sA}\);
- reversible clock evolution of those data by \(e^{-itA}\).

This is a constructive model of compatible operations, not a reason to identify them. The [[directed-analytic-realization/inq|analytic-tail member]] separately gives a noninjective upstream process intertwining a reversible quotient clock.

Nothing in (WR8)–(WR11) requires a positive lower spectral edge. For example, \(Ae_n=n^{-1}e_n\) gives the same positive-kernel construction on the band-limited test domain, with no gap. Also, the scalar models \(A^2=-\Delta+m^2\) have the same principal signature whether \(m=0\) or \(m>0\). Signature and reflection positivity therefore constrain a candidate realization without deciding its gap.

[[directed-analytic-realization/preparation-overlaps-and-the-transition-algebra|Preparation-overlap transitions]]
extract a reusable algebraic consequence of this method. A normalized
spectral readout gives a bounded overlap kernel for preparation labels,
including the zero sector. Transitions between its quotient classes
multiply by contracting that kernel and complete to the compact
operators, carrying the same clock. This extends the positive
preparation method to a whole operator algebra; it does not select the
physical local algebra or turn the preparation quotient into clock
evolution.

## The joint selection problem

The [[algebra/directed-response-and-lorentzian-signature|directed-response reflection]] offers a different construction: a positive tangent response and oriented covector line give signature and a proposed causal-cone bound. To connect these routes, one prior object must supply compatible carriers, pairings and localization, and identify the resulting clocks and cones. The two occurrences of a reflection are not automatically the same operator.

This is the appropriate meaning of investigating why the temporal direction receives special treatment. The next task is not to declare Wick rotation illegitimate, but to derive the data that make its positive local presentation possible from the same law that constrains directed processes. The [[contemporary-puzzles/yang-mills-mass-gap/clay-contract-and-scale-assumptions|Clay return]] remains the interacting four-dimensional Yang–Mills theory and its uniform vacuum gap.

[[directed-analytic-realization/real_form_response_receipt.py|The finite receipt]] checks the matrix signs, stable sector and sampled preparation Gram factorization. [[directed-analytic-realization/real-form-response-receipt-output.txt|The stored result]] does not certify analytic continuation of an interacting theory.

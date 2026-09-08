# A Resolved Relative Boundary Has Two Distinct Clock Limits

A narrowing joint comparison can retain its relative distinctions through a change of variables: its relative group element becomes an independent Gaussian tangent coordinate. An exact unitary comparison makes this more than a weak-limit analogy. On that common carrier, the original processing clock retains relative dynamics while freezing collective motion; the accelerated clock returns collective diffusion while projecting away relative dynamics. The state resolution works, but one common clock scaling does not preserve both sectors.

**Status: exact carrier construction and two limiting process theorems for the declared \(SU(2)\) family.** The Gaussian coordinate is a resolved boundary distinction, with no assigned matter content or gravitational coupling. [[sewn-overlap-refinement|The refinement theorem]] owns the multiplier estimates, normalization and uniform finite-system gap. Neither result supplies a four-dimensional field theory.

The process here conditionally resamples two contexts. [[sewn-transfer-clock-and-the-rotor-limit|The transfer interpretation]] instead treats them as successive endpoints of a path and returns a consistent rotor on its slice carrier. The present theorem does not require every normalized short-interval fluctuation to survive as an independent physical state. Its two-clock restriction remains exact for the declared conditional-update dynamics.

## Resolve the joint state before taking its clock limit

Use \(p_k,q_k,\pi_k,L_k\) from [[sewn-overlap-and-conditional-clock|the sewn comparison]]. In the coordinates \(g=xy^{-1}\) and \(y\), Haar invariance gives exactly

\[
d\pi_k=q_k(g)\,dg\,dy.
\tag{RB1}
\]

The retained base \(y\) is independent Haar. In a \(Q=-2\operatorname{Tr}\) orthonormal Lie coordinate, the local overlap expansion gives

\[
\sqrt{k}\log g\Rightarrow N(0,12I_3)\quad(g\sim p_k),
\qquad
\sqrt{k}\log g\Rightarrow\gamma:=N(0,24I_3)
\quad(g\sim q_k).
\tag{RB2}
\]

The second covariance comes from adding two independent increments in the convolution. The Baker–Campbell–Hausdorff correction is smaller by \(k^{-1/2}\) after rescaling. The principal logarithm has a Haar-null cut at \(-I\). Laplace localization at the unique overlap maximum supplies every fixed polynomial moment; mass away from that maximum is exponentially small. The squared group distance of a product is bounded by twice the sum of the two squared increment distances, which transfers the needed moment bounds to \(q_k\).

There is an exact common carrier. Let \(F_k\) be the distribution function of \(\sqrt{k}|\log g|\) under \(q_k(g)dg\), and let \(F_\gamma\) be the radial distribution function of \(\gamma\). Put

\[
\rho_k(R)=F_k^{-1}(F_\gamma(R)),\qquad
g_k(Y)=\exp\left[\frac{\rho_k(|Y|)}{\sqrt{k}}\frac{Y}{|Y|}\right].
\tag{RB3}
\]

Set \(g_k(0)=e\). Strict positivity and centrality make these radial distributions continuous and strictly increasing on their supports, with uniform angular laws. Therefore \((g_k)_*\gamma=q_kdg\), and \(g_k\) is invertible modulo null sets. Quantile convergence gives \(\rho_k(R)\to R\) for \(R>0\); the moment bounds also give convergence in every finite radial \(L^p\).

On

\[
\mathcal H_\infty=L^2(G\times\mathbb R^3,dy\,d\gamma),
\qquad
(U_kF)(x,y)=F\bigl(y,g_k^{-1}(xy^{-1})\bigr),
\tag{RB4}
\]

\(U_k:\mathcal H_\infty\to\mathcal H_k\) is unitary, with
\((U_k^*f)(y,Y)=f(g_k(Y)y,y)\). It preserves the full state and norm at every finite \(k\). This specifies the maps that an assertion of equivalent presentations requires.

## The normalized relative distinction remains nonzero

For a normalized centered representation mode \(\phi\) with Casimir \(c_n=n(n+2)/4\), write
\(X_a\phi(y)=\frac{d}{dt}|_{t=0}\phi(e^{tT_a}y)\).
The normalized collective and relative maps in [[sewn-overlap-refinement#The two branches cannot share one finite limiting pace|the branch decomposition]] satisfy

\[
U_k^*J_k^+\phi\longrightarrow\phi(y),\qquad
U_k^*J_k^-\phi\longrightarrow
\frac{\sum_aY_aX_a\phi(y)}{\sqrt{24c_n}}
\quad\text{in }L^2(dy\,d\gamma).
\tag{RB5}
\]

Taylor expansion and \(1-b_{k,n}^2=12c_n/k+O_n(k^{-2})\) give the formulas. Uniform moment control justifies their \(L^2\) limit. The second limit has norm one because
\(\mathbb E_\gamma Y_aY_b=24\delta_{ab}\) and
\(\sum_a\|X_a\phi\|^2=c_n\). It is orthogonal to all functions of \(y\).

For a character, the relative profile is invariant under
\((y,Y)\mapsto(hyh^{-1},\operatorname{Ad}_hY)\).
For \(y=bI-i\mathbf y\cdot\boldsymbol\sigma\) and the fundamental character it is explicitly \(-Y\cdot\mathbf y/\sqrt{18}\). Thus the relative witness survives the same simultaneous-conjugation restriction as the collective character. Its disappearance from the accelerated clock cannot be explained by deleting a colored gauge mode.

## The original clock retains a full relative process

Let \(P_\gamma\) average over the Gaussian variable, retaining the complete \(y\)-algebra. Conditional expectations transform exactly as

\[
U_k^*P_{y,k}U_k=P_\gamma,
\]

\[
(U_k^*P_{x,k}U_kF)(y,Y)
=\int F\bigl(g_k(Y')^{-1}g_k(Y)y,Y'\bigr)d\gamma(Y').
\tag{RB6}
\]

Since \(g_k(Y)\to e\), dominated convergence on bounded continuous functions, followed by density and the contraction bound, gives strong convergence of the second projection to \(P_\gamma\). Hence

\[
\boxed{
U_k^*L_kU_k\longrightarrow2(I-P_\gamma),\qquad
U_k^*e^{-tL_k}U_k\longrightarrow
P_\gamma+e^{-2t}(I-P_\gamma)
\quad\text{strongly}.}
\tag{RB7}
\]

Uniform boundedness of these generators justifies passing to their exponential series. Every centered relative function relaxes at rate two; all functions of the base remain stationary. This is conditional refresh, not an Ornstein–Uhlenbeck process. A Gaussian state by itself does not imply an oscillator ladder. The limiting kernel is infinite-dimensional, despite uniqueness of the finite-\(k\) vacuum.

This convergence is not in operator norm for \(t>0\). Choose a normalized character of degree \(n>k\). Its convolution multiplier is zero, so \(\phi_n(y)\) has finite-clock rate one. It is nevertheless a base function on \(\mathcal H_\infty\), where the limiting clock has rate zero. The semigroup norm error is at least \(1-e^{-t}\).

The [[receipts/sewn_overlap_refinement_receipt.py|refinement receipt]] checks
this moving high-mode witness exactly. Its low-mode convergence tables
cannot substitute for this distinction between strong and norm limits.

## The accelerated clock returns a reduced diffusion

Let \(V\phi(y,Y)=\phi(y)\), and \(V_k=U_k^*J_k^+\). These are isometries from the base carrier; \(V_k\to V\) strongly. With \(A_k=k(I-C_k)\), the exact complete branch decomposition gives

\[
U_k^*e^{-tkL_k}U_k
=V_ke^{-tA_k}V_k^*+R_k(t),\qquad
\|R_k(t)\|\le e^{-kt}.
\tag{RB8}
\]

[[sewn-overlap-refinement#The collective branch has an unbounded limit|The complete spectral-tail proof]] gives \(e^{-tA_k}\to e^{-12tD_Q}\) in norm. On the compact base, the latter heat operator is compact for \(t>0\). Finite-rank approximation and strong convergence of \(V_k\) therefore show

\[
\boxed{
U_k^*e^{-tkL_k}U_k
\longrightarrow V e^{-12tD_Q}V^*
\quad\text{in operator norm for each }t>0.}
\tag{RB9}
\]

For example, split the difference into the base heat error, \(V_kTV_k^*-VTV^*\) with fixed compact \(T=e^{-12tD_Q}\), and the remainder (RB8). Each tends to zero independently.

The same proof for compact base resolvents gives, for \(z>0\),

\[
U_k^*(z+kL_k)^{-1}U_k
\longrightarrow V(z+12D_Q)^{-1}V^*
\quad\text{in operator norm}.
\tag{RB10}
\]

The discarded-sector resolvent is bounded by \(1/(z+k)\). The limit in (RB10) has a nontrivial kernel and is therefore a reduced resolvent, not the resolvent of a densely defined self-adjoint operator on all \(\mathcal H_\infty\). Likewise (RB9), extended by the identity at zero, is not strongly continuous there: its right limit at zero is \(P_\gamma\). It is a genuine heat semigroup after restricting to the base.

## What must change in the next composition law

The two limits belong to one sequence of fully specified states and processes. The resolved relative information survives statically, but wholesale conditional replacement makes its relaxation fast compared with collective motion. The [[sewn-overlap-refinement#The two branches cannot share one finite limiting pace|scalar-speed obstruction]] proves that a common change of time units cannot keep both rates finite and nonzero.

A next construction must therefore constrain how comparisons process the resolved relative variable. A covariant local comparison in that variable could differ from replacing its entire conditional state at once. Its mobility, pairing and clock weights must be derived from declared primitive rules and tested for independent retuning. Appending separate collective and relative generators would supply the desired answer as new input.

The [[conditional-fisher-coercivity/moving-fiber-connection|moving-fiber connection]]
requires transporting the derivative with its state and
carrier; a bare Fisher term cannot be appended after changing variables.
The [[directed-analytic-realization/purification-fluctuation-and-the-oscillator-return|purification fluctuation construction]]
provides a different declared parent whose
Gaussian return does possess a full oscillator clock. Comparing the
primitive operations responsible for these different returns is more
specific than inferring dynamics from Gaussian shape alone.

The common-carrier calculation gives a mathematical place to investigate the proposed duality between identity and difference: collective and relative descriptions have explicit maps and different dynamical limits. Assigning either branch a cosmological or dark-sector interpretation would additionally require observable algebras, physical translations and the appropriate gravitational or cosmological return. The two numerical rates are not yet quantities in one reconstructed physical clock.

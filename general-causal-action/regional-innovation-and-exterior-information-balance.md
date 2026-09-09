# Regional Innovation Retains an Exterior Information Term

Restricting the actual chronological law to a region changes its predictor but does not change the underlying clock. The additional prediction error is an exact positive exterior-information term. The same term, at twice the duration, supplies the part of the full oriented-innovation surplus lost by squaring a compressed response. Revealing nested regions splits this information budget orthogonally. The compact one-face calculation already detects a nonzero instance; no gap estimate is inferred from its sign alone.

**Status: exact conditional-compression identities, with a proved actual compact witness.** [[oriented-innovation-and-finite-temporal-repair|OI]] fixes the full chronological innovation and surplus. [[vacuum-hellinger-return-and-regional-conditional-projections|VH]] supplies the actual regional witness. [[spatial-block-sewing-and-the-vacuum-cap-response|SB]] retains the spatially sewn history and its vacuum caps. The identities below keep that inherited law; they introduce no regional reset or independent clock.

## Retain the full stationary chronology

Let \(P_t=e^{-tH}\) be the self-adjoint Markov semigroup on \(\mathscr H=L^2(\pi)\) obtained from the actual vacuum by the ground transform. Thus \(H\ge0\), \(P_t1=1\), and \(0\le P_t\le I\). All times use one specified full-system clock.

Let \(\mathsf E_B\) be conditional expectation onto the actual regional observable sigma algebra \(\mathcal B\), and let \(\mathscr H_B=\operatorname{ran}\mathsf E_B\). In a framed presentation this is restricted to the physical invariant carrier as in VH; it requires no physical tensor product across the cut. Define
\[
Q_B(t)=\mathsf E_BP_t|_{\mathscr H_B},\qquad
D_B(t)=Q_B(2t)-Q_B(t)^2.
\tag{RI1}
\]
Each \(Q_B(t)\) is a positive self-adjoint Markov contraction in the inherited regional marginal. It need not form a semigroup. The elementary compression identity is
\[
\boxed{
D_B(t)=
\mathsf E_BP_t(I-\mathsf E_B)P_t|_{\mathscr H_B}
=L_B(t)^*L_B(t)\ge0,\qquad
L_B(t)=(I-\mathsf E_B)P_t|_{\mathscr H_B}.}
\tag{RI2}
\]
Indeed \(P_{2t}=P_t^2\), and inserting
\(I=\mathsf E_B+(I-\mathsf E_B)\) between its factors gives the formula. The operator identity needs only orthogonal compression. The Markov and predictor interpretation additionally uses the actual conditional expectation, not an arbitrary projector containing constants.

For \(f,g\in\mathscr H_B\),
\[
\langle f,D_B(t)g\rangle
=\langle (I-\mathsf E_B)P_tf,(I-\mathsf E_B)P_tg\rangle.
\tag{RI3}
\]
Thus the entire mixed exterior response, including its signs between different sources, is fixed by the same law.

## Regional and full predictors have different innovations

Use the stationary pair law \(\pi(dx)P_t(x,dy)\). A regional source \(f\) at the later endpoint has two actual predictors:
\[
\mathbb E[f(X_t)\mid X_0]=P_tf(X_0),\qquad
\mathbb E[f(X_t)\mid\mathcal B_0]=Q_B(t)f(\mathcal B_0).
\]
Here \(f\in\mathscr H_B\) is pulled back to the full configuration; notation \(\mathcal B_0\) denotes the retained regional information at time zero. Put
\[
\delta_t f=f(X_t)-P_tf(X_0),\qquad
\delta_{B,t}f=f(X_t)-Q_B(t)f(\mathcal B_0).
\]
Then
\[
\boxed{
\delta_{B,t}f=
\delta_tf+\bigl[(I-\mathsf E_B)P_tf\bigr](X_0),}
\tag{RI4}
\]
and the two terms are orthogonal. The first has conditional mean zero given the complete \(X_0\); the second is a function of \(X_0\).

The full predictor's response, restricted to regional sources, is therefore
\[
R_{B,t}:=(\delta_t|_{\mathscr H_B})^*
                    (\delta_t|_{\mathscr H_B})
=I_B-Q_B(2t).
\tag{RI5}
\]
The response using only a regional predictor is
\[
\boxed{
\widetilde R_{B,t}:=\delta_{B,t}^*\delta_{B,t}
=I_B-Q_B(t)^2
=R_{B,t}+D_B(t).}
\tag{RI6}
\]
This is an exact Pythagorean decomposition of prediction error. Restricting the predictor discards exterior information and increases its error. It does not replace \(Q_B(2t)\) by \(Q_B(t)^2\) in the actual full-predictor response.

## The full OI surplus contains the exterior channel

On the full carrier let \(R_t=I-P_{2t}\). OI's source surplus is
\(\langle f,R_t^2f\rangle\), with normalization
\(\langle f,R_tf\rangle\). Its restriction to regional sources obeys
\[
\boxed{
\mathsf E_BR_t^2|_{\mathscr H_B}
=I_B-2Q_B(2t)+Q_B(4t)
=R_{B,t}^2+D_B(2t).}
\tag{RI7}
\]
Equivalently, the squared full response vector splits as
\[
\|R_tf\|^2
=\|R_{B,t}f\|^2
+\|(I-\mathsf E_B)P_{2t}f\|^2,\qquad f\in\mathscr H_B.
\]
The sign in the exterior component of \(R_tf\) is negative, but disappears in its squared norm.

For a centered regional source with nonzero response, the unchanged full OI quotient is exactly
\[
\boxed{
\mathfrak q_{B,t}(f)=
\frac{\|R_{B,t}f\|^2+\|L_B(2t)f\|^2}
     {\langle f,R_{B,t}f\rangle}
=
\frac{\langle f,(I_B-2Q_B(2t)+Q_B(4t))f\rangle}
     {\langle f,(I_B-Q_B(2t))f\rangle}.}
\tag{RI8}
\]
The denominator condition excludes the full invariant directions. In the finite irreducible compact theory every nonzero centered source satisfies it. Spectral calculus gives \(0\le\mathfrak q_{B,t}(f)\le1\), since \(R_t^2\le R_t\).

Dropping \(D_B(2t)\) loses the positive compression remainder of the full squared response. Using \(I_B-Q_B(t)^2\) instead also changes the predictor and its denominator. These are separate changes; no general ordering between the resulting normalized quotients is asserted.

The inherited data \((R_{B,t},D_B(2t))\) preserve the full quotient of every retained source exactly. Positivity of the second term alone supplies no lower bound on that quotient over a complete source family. In particular, small response directions can coexist with nonzero exterior memory.

[[covariant-source-memory-and-the-first-chronological-response|The first nonlinear mixed exterior test]] evaluates (RI3) on two physical scalar sources in the actual four-face vacuum. Retaining \(abc\), the radius \(Q(X_a,X_a)\) and Cartan triple \(T(X_a,X_b,X_c)\) have a nonzero mixed first correction, while each diagonal first correction vanishes by parity. The calculation transports the generator, regional projection and changing measure together. It supplies a fixed-patch entry of \(D_B(t)\); its sign does not determine the generalized quotient in (RI8).

## Nested regions split the same information budget

Let \(\mathcal B\subset\mathcal C\) be actual nested regional sigma algebras, so
\(\mathsf E_B\le\mathsf E_C\). For \(f\in\mathscr H_B\),
\[
(I-\mathsf E_B)P_tf
=(I-\mathsf E_C)P_tf
+(\mathsf E_C-\mathsf E_B)P_tf.
\]
The two summands are orthogonal. Hence
\[
\boxed{
\|L_B(t)f\|^2
=\|L_C(t)f\|^2
+\|(\mathsf E_C-\mathsf E_B)P_tf\|^2.}
\tag{RI9}
\]
At the operator level on \(\mathscr H_B\),
\[
D_B(t)=
\mathsf E_BD_C(t)|_{\mathscr H_B}
+\mathsf E_BP_t(\mathsf E_C-\mathsf E_B)P_t|_{\mathscr H_B}.
\tag{RI10}
\]
Revealing the larger region accounts for part of the exterior information; it does not change its total. Along a finite nested chain, these nonnegative terms telescope, with the final exterior remainder retained. At duration \(2t\), this is precisely the channel decomposition needed by (RI7).

For nonnested sibling regions there is no corresponding orthogonal partition without extra conditional structure. Their cross terms are part of the mixed response (RI3). The nested identity therefore supplies a compositional check without discarding sibling correlations.

## The actual compact one-face law has a nonzero remainder

Retain VH's one-face compact source \(f_h\), centered and normalized in the actual regional vacuum marginal. Its harmonic comparison has
\[
r_L(t)=
\left[
\frac{(\sqrt{A_L}e^{-t\sqrt{A_L}})_{pp}}
     {(\sqrt{A_L})_{pp}}
\right]^2,\qquad
d_L(t)=r_L(2t)-r_L(t)^2.
\]
VH proves on \(0<hn^{10}\le\eta\), with \(\theta=hn^{11/2}\),
\[
\sup_{t\ge0}
\|D_{B,h}(t)f_h-d_L(t)f_h\|
\le C\sqrt\theta .
\tag{RI11}
\]
For a nontrivial connected patch and every fixed \(t>0\), the harmonic frequency mixture gives \(d_L(t)>0\). It stays positive in the bulk limit at fixed scaled duration, when the retained face recedes from the exterior boundary. Thus the actual compact source detects a nonzero term in (RI6), and, by replacing \(t\) with \(2t\), in (RI7). This is an actual conditional-projection theorem, not an inference from a mixture of autocorrelation exponentials alone.

At fixed \(L>1,t>0\), or along the stipulated bulk sequences at fixed scaled \(t>0\), (RI8) consequently returns
\[
\boxed{
\mathfrak q_{B,t}(f_h)=
\frac{1-2r_L(2t)+r_L(4t)}
     {1-r_L(2t)}
+O_t(\sqrt\theta).}
\tag{RI12}
\]
The displayed denominators are positive and remain bounded away from zero along those sequences. The leading expression is
\[
1-r_L(2t)+\frac{d_L(2t)}{1-r_L(2t)}.
\]
The second summand is exactly the exterior contribution that a squared regional compression misses. Its known positivity does not establish a uniform full-carrier floor or a fixed-physical-time infinite-volume limit.

## Spatial sewing must transport these channels with their source factors

Equations (RI6)–(RI10) are forced by the original probability law and chronological composition. A proposed regional realization must return these identities and the mixed source pairings, with the inherited vacuum and the same time unit. Neither a reset block nor an independently selected correction can stand in for the exterior term.

This single-time regional projection is different from SB's three-slab outer/middle history projections. SB compares norms under distinct pair laws and includes transported-source exchange terms and the OI lag cost. The quantity \(D_B(t)\) is not automatically any one of those history terms. Identifying them requires an explicitly compatible history map and its full marked law.

[[uniform-collar-capture-and-the-local-gap-limitation|The collar test]] now bounds the omitted fraction by \(C/w^2\) on the complete one-face radial harmonic algebra, with a uniform compact return for the prescribed quadratic away from zero scaled time. It also proves that complete local coercivity can coexist with a closing global floor. [[finite-pairing-range-and-the-harmonic-innovation-floor|The range theorem]] now controls the full quadratic matrix, and [[compact-quadratic-carrier-and-the-pairing-range-return|its actual compact return]] retains the same order of response. [[four-face-diagonal-sources-and-the-relational-schur-defect|The four-face Schur separation]] computes that mixed deficit, while [[four-face-oriented-source-extension-and-the-schur-surplus|the oriented source extension]] removes the quadratic readout's leakage and follows the negative physical-gap correction. The required strict OI bound must still control the complete response ratio through the physical limits. The exact positive budget specifies what sewing must preserve; it does not supply that missing estimate.

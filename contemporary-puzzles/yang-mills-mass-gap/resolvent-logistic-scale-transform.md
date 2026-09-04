# The Resolvent--Logistic Scale Transform

Every nonnegative self-adjoint operator has a canonical scale-resolved presentation once its positive spectrum is converted into bounded effects by the odds map \(X\mapsto X(1+X)^{-1}\). Differentiating that effect along logarithmic scale produces an exactly normalized logistic profile with rate \(\nu=1/2\), and its square root gives an isometric, complex-linear Calderon-type analysis transform on the complement of the kernel. This closes part of the boundary-to-scale carrier problem without spectral fitting. It also proves a decisive no-go: the universal logistic edge \(1/4\) is a shape constant shared by gapped and gapless operators. A positive lower spectral edge is instead an upper bound on the log-scale **center**. This becomes a mass statement only after the supplied operator is noncircularly identified with the physical Casimir. For two oppositely scaling causal generators, their separate centers move in opposite directions while their mean is the negative logarithm of the joint positive invariant.

**Status: [EXACT FUNCTIONAL-CALCULUS THEOREM]; [EXACT JOINT-CENTER THEOREM]; [CANDIDATE INTERFACE ANALYSIS MAP]; [OPEN YANG--MILLS OPERATOR SELECTION AND CASIMIR COMPARISON].** The transform below parses the spectrum of a supplied operator. It neither constructs that operator nor proves its positive lower edge.

## The operator must already have a carrier

Let \(\mathcal H\) be a complex Hilbert space and let \(L\geq0\) be self-adjoint. If \(L\) has physical units, first choose an independently fixed reference \(L_*>0\) of the same type and put

$$
\widehat L:=L/L_*.
\tag{RL1}
$$

Everything through the scale-center theorem is dimensionless. Changing \(L_*\) translates the origin of logarithmic scale; it cannot change whether zero is an accumulation point of the spectrum. Write

$$
P_0:=E_{\widehat L}(\{0\}),
\qquad
P_+:=1-P_0,
\qquad
\mathcal H_+:=P_+\mathcal H.
\tag{RL2}
$$

The typed question is not merely “what is the operator?” but:

$$
\boxed{
\widehat L\text{ operates on vectors in }\mathcal H;
\quad
\text{the transform below returns their resolution by logarithmic spectral scale}.}
\tag{RL3}
$$

If \(\mathcal H\) is the gauge-invariant interface carrier, plausible inputs include an independently constructed boundary response operator, a closed gauge-invariant coordinate Laplacian, or an RG scale operator. Taking \(L\) to be the already reconstructed Hamiltonian or Poincare Casimir is legitimate for re-expression but circular if the purpose is to prove its gap.

## Effects, odds, and the forced logistic profile

For \(N\in\mathbb R\), define bounded positive operators

$$
X_N:=e^N\widehat L,
\qquad
Z_N:=X_N(1+X_N)^{-1},
\qquad
Q_N:=X_N^{1/2}(1+X_N)^{-1}.
\tag{RL4}
$$

The map \(X\mapsto X(1+X)^{-1}\) is the effect--odds bijection from positive operators to positive contractions below the identity. On the positive spectral subspace its inverse is

$$
Z_N(1-Z_N)^{-1}=e^N\widehat L.
\tag{RL5}
$$

The family \(N\mapsto Z_N\) is differentiable in operator norm, and functional calculus gives

$$
\boxed{
\partial_NZ_N
=Z_N(1-Z_N)
=Q_N^2.}
\tag{RL6}
$$

For a spectral value \(\lambda>0\),

$$
Z_N(\lambda)
=\frac{e^N\lambda}{1+e^N\lambda}
=\frac{1}{1+e^{-(N+\log\lambda)}},
\tag{RL7}
$$

and hence

$$
q_\lambda(N)
:=Q_N(\lambda)^2
=\frac14\operatorname{sech}^2
\!\left(\frac{N+\log\lambda}{2}\right).
\tag{RL8}
$$

This is exactly the normalized logistic density

$$
q_{\nu,N_c}(N)
=\frac\nu2\operatorname{sech}^2\!\bigl(\nu(N-N_c)\bigr)
\tag{RL9}
$$

with

$$
\boxed{
\nu=\frac12,
\qquad
N_c(\lambda)=-\log\lambda.}
\tag{RL10}
$$

Thus the projection-coded log-odds branch in [[wall-construction-interface/scale-character-solder]] is not merely numerically compatible with \(\nu=1/2\). It is the exact scalar shadow of the positive-operator effect transform (RL5), once \(N\) is normalized as the natural logarithm of multiplicative scale. This does not prove that this effect is the physical wall readout; it identifies the operator-theoretic construction that would make that branch canonical.

Positive self-adjointness alone does not select this window. Many normalized functions \(\psi(e^N\widehat L)\) give Calderon frames. The rate \(\nu=1/2\) is forced only after choosing the effect--odds transform and the unit log-scale action \(e^N\). Replacing it by \(e^{\alpha N}\) gives \(\nu=\alpha/2\), but then \(\partial_NZ_N=\alpha Q_N^2\) and the normalized analysis window is \(\sqrt\alpha Q_N\). The claimed canonicality is therefore typed and conditional, not absolute.

On \(\mathcal H_+\), Borel functional calculus also gives the unbounded identity

$$
\boxed{
\log\!\left(Z_N(1-Z_N)^{-1}\right)
=N+\log\widehat L}
\tag{RL11}
$$

on its natural domain. No equality of units or concepts is being used: \(N\) and \(\log\widehat L\) are dimensionless scale coordinates, while \(L_*\) carries any eventual physical unit.

## Exact coverage by a continuous scale frame

Define

$$
\mathscr S_{\widehat L}:\mathcal H\longrightarrow
L^2(\mathbb R,\mathrm dN;\mathcal H),
\qquad
(\mathscr S_{\widehat L}f)(N):=Q_Nf.
\tag{RL12}
$$

For every \(\lambda>0\), substitution \(x=e^N\lambda\) gives

$$
\int_{\mathbb R}q_\lambda(N)\,\mathrm dN
=\int_0^\infty\frac{1}{(1+x)^2}\,\mathrm dx
=1.
\tag{RL13}
$$

Tonelli's theorem and the spectral theorem therefore imply

$$
\boxed{
\int_{\mathbb R}\|Q_Nf\|^2\,\mathrm dN
=\|P_+f\|^2,
\qquad
\mathscr S_{\widehat L}^*\mathscr S_{\widehat L}=P_+.}
\tag{RL14}
$$

Equivalently,

$$
\int_{\mathbb R}Q_N^2\,\mathrm dN=P_+
\tag{RL15}
$$

in the strong operator sense. Hence \(\mathscr S_{\widehat L}\) is an isometry on \(\mathcal H_+\), has closed range, and has kernel exactly \(\ker L\). It is complex-linear and retains phase information; only replacing \(Q_Nf\) by the scalar probabilities \(\|Q_Nf\|^2\) forgets that information.

There is also an exact Sobolev identity. Since

$$
\partial_NQ_N
=Q_N\left(\frac12-Z_N\right),
\tag{RL16}
$$

the same spectral calculation yields

$$
\boxed{
\int_{\mathbb R}
\|\partial_NQ_Nf\|^2\,\mathrm dN
=\frac1{12}\|P_+f\|^2.}
\tag{RL17}
$$

Thus the transform lands continuously in \(H^1(\mathbb R;\mathcal H)\) and has exact lower coverage one on the positive spectral subspace. These are genuine carrier results, not asymptotic estimates.

Differentiation also supplies a normalized signed detail window,

$$
\Phi_N
:=-2\sqrt3\,\partial_NQ_N
=\sqrt3\,
\frac{X_N^{1/2}(X_N-1)}{(1+X_N)^2}.
\tag{RL17a}
$$

For every \(\lambda>0\),

$$
\int_{\mathbb R}\Phi_N(\lambda)\,\mathrm dN=0,
\qquad
\int_{\mathbb R}|\Phi_N(\lambda)|^2\,\mathrm dN=1,
\tag{RL17b}
$$

and therefore \(f\mapsto(N\mapsto\Phi_Nf)\) is another Parseval transform on \(\mathcal H_+\). It resolves changes across the channel center rather than positive scale occupancy. Its vanishing moment is with respect to log-Haar measure \(\mathrm dN\), not the mean-zero condition for one fixed weighted logistic probability carrier; it narrows but does not erase the codomain mismatch below.

## The scale observable is a logistic smearing of \(-\log\widehat L\)

The positive operator-valued measure

$$
\Pi_{\widehat L}(B)
:=\int_BQ_N^2\,\mathrm dN
\tag{RL18}
$$

is normalized by \(\Pi_{\widehat L}(\mathbb R)=P_+\). It is a fuzzy logarithmic-scale observable on \(\mathcal H_+\). In a spectral channel \(\lambda\), its outcome density has mean and variance

$$
\mathbb E_\lambda[N]
=-\log\lambda,
\qquad
\operatorname{Var}_\lambda(N)
=\frac{\pi^2}{3}.
\tag{RL19}
$$

Consequently, on the appropriate form domains,

$$
\int_{\mathbb R}N\,\mathrm d\Pi_{\widehat L}(N)
=-\log\widehat L,
\tag{RL20}
$$

and

$$
\int_{\mathbb R}N^2\,\mathrm d\Pi_{\widehat L}(N)
=(\log\widehat L)^2+\frac{\pi^2}{3}P_+.
\tag{RL21}
$$

The conditional profile has differential entropy \(2\) nats, location Fisher information \(1/3\), and half-density Dirichlet energy \(1/12\), independently of \(\lambda\). These constants describe the **shape and resolution noise** of the canonical odds readout. They do not locate the channel on scale.

This is also why the construction is not a wave-function-collapse mechanism. It supplies an effect-valued scale readout and an isometric dilation. It does not choose an outcome, form a record, or turn a possibility into a fact. [[physical-distinction-coercivity]] keeps pointing, actualization, and spectral coercivity in separate slots.

## A lower spectral edge is a center ceiling; mass requires a Casimir solder

Let

$$
A_{\widehat L}:=-\log\widehat L
\tag{RL22}
$$

on \(\mathcal H_+\). It is the latent center operator measured with the fixed logistic blur (RL19). For any \(\lambda_*>0\), the spectral theorem gives the exact equivalence

$$
\boxed{
\widehat L\geq\lambda_*P_+
\quad\Longleftrightarrow\quad
\sup\sigma(A_{\widehat L})\leq-\log\lambda_*.}
\tag{RL23}
$$

If positive spectral values of \(\widehat L\) approach zero, their profiles retain exactly the same width and simply move to \(N_c\to+\infty\). Therefore

$$
\boxed{
\text{the logistic shape edge }\frac14
\text{ does not imply a lower edge of }\widehat L.}
\tag{RL24}
$$

Indeed, (RL14) and (RL17) hold unchanged when \(\sigma(\widehat L)=[0,\infty)\). Any argument that reads \(1/4\) directly as a Yang--Mills mass gap would prove the same “gap” for an arbitrarily gapless input and is therefore invalid.

The correct geometric retyping is subtler. A positive lower edge says that no spectral center on the chosen positive carrier can recede indefinitely toward the large-\(N\), or infrared, end of logarithmic scale. This is an exact reformulation of a supplied lower edge, not yet its sufficient reason and not yet a statement about mass. The explanatory task becomes: what independent wall, descent, compactness, or RG-stopping law imposes the center ceiling uniformly as the regulator and volume are removed, and what same-carrier theorem identifies that operator with the physical Casimir?

When \(P_+\neq0\), there is an equivalent uniform-saturation criterion. Functional calculus gives

$$
\|P_+-Z_N\|
=
\sup_{\lambda\in\sigma(\widehat L)\setminus\{0\}}
\frac{1}{1+e^N\lambda}.
\tag{RL24a}
$$

Strongly, \(Z_N\to P_+\) as \(N\to+\infty\) for every nonnegative \(\widehat L\). In operator norm, however,

$$
\boxed{
Z_N\longrightarrow P_+\text{ uniformly}
\quad\Longleftrightarrow\quad
\inf\bigl(\sigma(\widehat L)\setminus\{0\}\bigr)>0.}
\tag{RL24b}
$$

If the lower edge is \(\lambda_*>0\), the norm in (RL24a) is \((1+e^N\lambda_*)^{-1}\). If positive spectrum accumulates at zero, it equals \(1\) for every finite \(N\). This is a particularly clean “finite bandwidth” formulation: every fixed vector can eventually be resolved even in a gapless theory, but one common finite scale resolves the entire nonzero carrier uniformly only when a gap already exists.

If \(\widehat L=\mathcal C/E_*^2\) is the dimensionless Poincare Casimir after Lorentz reconstruction and its kernel has first been proved to be exactly the vacuum line \(P_{\mathrm{vac}}\), then (RL23) says

$$
\mathcal C\geq\Delta_E^2(1-P_{\mathrm{vac}})
\quad\Longleftrightarrow\quad
A_{\mathcal C/E_*^2}
\leq
-2\log(\Delta_E/E_*)(1-P_{\mathrm{vac}}).
\tag{RL25}
$$

Using \(\mathcal C\) here clarifies the meaning of a known mass gap. It cannot prove the gap unless the kernel identity and \(A_{\mathcal C/E_*^2}\)'s ceiling are obtained from independent pre-spectral geometry. If nonvacuum massless sectors lie in \(\ker\mathcal C\), the transform kills them and cannot certify the Clay condition.

## Opposite causal directions and the invariant mean center

The reminder in [[joint-causal-generators-and-the-mass-casimir]] now has an exact scale-coordinate form. Let \(K_+,K_-\geq0\) be strongly commuting dimensionless self-adjoint operators, and let

$$
P_{\leftrightarrow}
:=E_{(K_+,K_-)}((0,\infty)^2).
\tag{RL26}
$$

Their bivariate scale transform is

$$
(\mathscr S_{+,-}f)(N_+,N_-)
:=
Q_{N_+}(K_+)Q_{N_-}(K_-)f.
\tag{RL27}
$$

Joint functional calculus and two applications of (RL13) give

$$
\boxed{
\int_{\mathbb R^2}
\|\mathscr S_{+,-}f(N_+,N_-)\|^2
\,\mathrm dN_+\mathrm dN_-
=\|P_{\leftrightarrow}f\|^2.}
\tag{RL28}
$$

On this joint positive subspace define center operators

$$
A_+:=-\log K_+,
\qquad
A_-:=-\log K_-,
\tag{RL29}
$$

and their mean and difference

$$
A_M:=\frac{A_++A_-}{2},
\qquad
A_{\mathrm{fr}}:=\frac{A_+-A_-}{2}.
\tag{RL30}
$$

If a unitary scale or boost action obeys

$$
U_sK_+U_s^*=e^sK_+,
\qquad
U_sK_-U_s^*=e^{-s}K_-,
\tag{RL31}
$$

then

$$
U_sA_MU_s^*=A_M,
\qquad
U_sA_{\mathrm{fr}}U_s^*=A_{\mathrm{fr}}-s.
\tag{RL32}
$$

Moreover,

$$
\boxed{
A_M
=-\log\sqrt{K_+K_-}.}
\tag{RL33}
$$

Thus the separate logistic centers slide oppositely under the causal-frame change, while their mean is invariant. The joint lower bound

$$
K_+K_-\geq m_*^2P_{\leftrightarrow}
\tag{RL34}
$$

is equivalent to

$$
\boxed{
A_M\leq-\log m_*\,P_{\leftrightarrow}.}
\tag{RL35}
$$

This is only a floor on the joint-positive carrier. It yields a vacuum-complement floor only after proving \(P_{\leftrightarrow}=1-P_0\), or equivalently excluding every nonvacuum sector on which either causal generator vanishes.

This is the rigorous version of the upside-down claim: a single causal generator can remain scale-covariant and gapless, while a lower edge can reside in the frame-invariant mean address of two reciprocal directions. In \(1+1\) dimensions this product is the mass Casimir after normalization, provided the joint-positive carrier is the vacuum complement. In \(3+1\) dimensions one null pair gives \(H^2-P_z^2=\mathcal C+\mathbf P_\perp^2\), so the product is not identical to the full Casimir. Yet (RL34) for one chosen direction does prove the Clay Hamiltonian gap if \(K_\pm\) have first been identified with that fixed physical null pair on the entire vacuum complement of a positive-energy Poincare representation. For an abstract or sector-restricted pair, a full-carrier fixed-pair, all-direction, or direct-Casimir solder remains necessary.

## Naturality and the candidate boundary-to-scale map

The construction has two exact covariance laws. If \(V:\mathcal H\to\mathcal H'\) is unitary and \(\widehat L'=V\widehat LV^*\), then

$$
\mathscr S_{\widehat L'}V
=(1\otimes V)\mathscr S_{\widehat L}.
\tag{RL36}
$$

For \(a>0\), if \((T_sF)(N):=F(N+s)\), then

$$
\mathscr S_{a\widehat L}
=T_{\log a}\mathscr S_{\widehat L}.
\tag{RL37}
$$

Multiplying the input operator by a common scale therefore translates its analysis profile; it does not change the logistic shape. This is the correct torsor behavior of scale origin.

At a finite Yang--Mills regulator, the exact interface theorem in [[vacuum-boundary-gluing-and-wall-response]] supplies

$$
B_r^{\mathrm{OS}}:
\mathcal H_{\mathrm{OS},r}
\longrightarrow
L^2(\nu_{r,I})^{\mathrm{GI}}.
\tag{RL38}
$$

Suppose a geometrically defined nonnegative self-adjoint \(L_{r,I}\) on the target satisfies

$$
\ker L_{r,I}=\mathbb C1
\tag{RL39}
$$

and is natural under the regulator, regional, and gauge comparison maps. Then

$$
\boxed{
S_r^{\mathrm{res}}
:=\mathscr S_{L_{r,I}/L_{*,r}}}
\tag{RL40}
$$

is a canonical candidate for the previously open interface-to-log-scale analysis leg. It is complex-linear, has exact lower coverage one on the constant complement, and is defined without choosing eigenvectors or inspecting whether a gap exists.

This is real progress but not a completed identification with the map in [[pointing-coercivity-and-the-flat-partner-law#The wall--Casimir sandwich|the wall--Casimir sandwich]]. Its natural codomain is the half-density carrier

$$
L^2(\mathbb R,\mathrm dN;
L^2(\nu_{r,I})^{\mathrm{GI}}),
\tag{RL41}
$$

not the earlier fixed-center weighted probability carrier \(\mathcal V^{\mathrm{sc}}_{1/2,N_c}\widehat\otimes\mathcal K_r\). In a direct-integral spectral representation, every \(\lambda\)-fiber can be recentered to the same logistic half-density, but the spectral center \(-\log\lambda\) must remain as a multiplicity label. Erasing that label would erase precisely the information that distinguishes a gapped operator from a gapless one.

The existing RG martingale decomposition supplies a discrete companion once its shell addresses have been fixed independently. For vacuum-preserving nested regulator algebras with orthogonal shell differences \(D_{r,j}\),

$$
S_r^{\mathrm{disc}}f
:=(D_{r,j}f)_j,
\qquad
\sum_j\|D_{r,j}f\|^2=\|f\|^2
\tag{RL42}
$$

on the centered carrier. If geometry or RG supplies log-scale addresses \(N_{r,j}\), then [[paired-scale-filtrations-and-the-invariant-incidence-wall]] defines

$$
A_{r,\mathcal F}=\sum_jN_{r,j}D_{r,j},
\qquad
L_{r,\mathcal F}=0\oplus e^{-A_{r,\mathcal F}},
$$

and the present resolvent calculus continuously interpolates that positive shell operator without erasing multiplicities. This also sharpens the obstruction: an unbounded one-sided spatial-resolution address forces \(L_{r,\mathcal F}\) to be gapless. A mass-like floor can survive only in an invariant joint relation between oppositely transforming filtrations, where it is equivalent to a diagonal ceiling on their incidence support. The next construction problem is therefore not to truncate one tower, but to derive the paired incidence wall and its physical Casimir solder. Choosing shell weights from the desired logistic profile would be fitting; deriving the addresses and forbidden incidences from independently given gauge, flux, boundary, or RG geometry would be a construction.

[[library/scaling-algebras-and-renormalization-group-in-algebraic-quantum-field-theory/inq|Buchholz--Verch scaling algebras]] show how scale transformations can act canonically on a family of local observables, but do not supply this \(L_{r,I}\) or a mass floor. Their [[library/scaling-algebras-and-renormalization-group-in-algebraic-quantum-field-theory-ii-instructive-examples/inq|free-field examples]] make the center warning concrete: massive free nets in two and three spatial dimensions have massless short-distance scaling limits. Ultraviolet scale structure can forget an infrared mass even when the original theory is gapped. [[library/properties-and-uses-of-the-wilson-flow-in-lattice-qcd/inq|Luscher's Wilson flow]] gives a gauge-covariant family of renormalized probes with smoothing radius of order \(\sqrt{8t}\), but its nonlinear smoothing flow is not automatically the isometry (RL14). On a finite lattice the flow itself is an invertible diffeomorphism of field space, so it is not a noninjective descent or collapse; loss enters only after a restricted readout, discarded inverse, or singular limiting operation. Its normalization also reenacts the factor-of-two fork: if \(N=\log(t/t_*)\), a second-order flow generator gives \(\nu=1/2\), whereas for the log-length coordinate \(N_\ell=\log(\sqrt{8t}/\ell_*)\) the effect depends on \(e^{2N_\ell}L\), the normalized window is \(\sqrt2Q\), and \(\nu=1\). [[library/calderon-reproducing-formulas-and-applications-to-hardy-spaces/inq|Auscher--McIntosh--Morris]] supply the closest general reproducing-formula setting, while [[library/quadratic-estimates-and-functional-calculi-of-perturbed-dirac-operators/inq|Axelsson--Keith--McIntosh]] supply its harder perturbed-Dirac context. The special isometry above follows directly from self-adjoint spectral calculus.

## What the construction changes

The earlier architecture localized the missing map as \(S_r\). The resolvent transform divides that obligation into two cleaner questions:

1. **Carrier parsing:** once \(L_{r,I}\) is supplied, (RL40) gives exact coverage, complex phases, and scale-translation covariance.
2. **Geometric selection:** construct \(L_{r,I}\) from boundary, flux, descent, or RG data, with kernel exactly the vacuum line and with the required comparison naturality.
3. **Center confinement:** prove, without using the desired spectrum, that the invariant center is uniformly bounded above in physical continuum units.
4. **Casimir solder:** prove that this center or its underlying positive operator controls the full reconstructed Poincare Casimir on the same physical carrier.

The distinction between shape and center is load bearing. Equation (RL17) makes the scale derivative uniformly coercive for every positive operator, including a gapless one. Therefore a comparison

$$
\langle f,\mathcal Cf\rangle
\gtrsim
E_*^2
\int\|\partial_N\mathscr S_{\widehat L}f\|^2\,\mathrm dN
\tag{RL43}
$$

is already, up to the universal factor \(1/12\), the desired Casimir gap estimate. The transform cannot make that comparison free. Its useful new return value is the scale-center observable (RL20), where the missing infrared obstruction becomes visible rather than hidden in a universal profile constant.

For the causal grain, this changes the viable interpretation. A grain cannot be the logistic width, a \(4.264\,\mathrm{fm}\) pixel, or the number \(1/4\). It could only be a historical reason that the physical carrier acquires an invariant center ceiling, an admissible-sector boundary, or an RG stopping class whose dimensionful presentation is fixed later. [[causal-grain-as-a-mass-engagement-fossil]] owns that conjectural historical claim.

## Compatibility and recovery

The transform is an exact functional representation of an operator on an already declared carrier. Used that way, it is compatible with local QFT and adds no new local particle or stochastic dynamics. It is not by itself a recovery theorem. [[library/short-distance-analysis-for-algebraic-euclidean-field-theory/inq|Schlingemann's Euclidean scaling analysis]] supplies a rigorous precedent that, under its hypotheses, scaling limit and Euclidean-to-Minkowski reconstruction commute at the level of nets. It presupposes the Euclidean net, reflection-positive functional, and scaling limit; it does not choose \(L_{r,I}\) or prove a gap. If the pre-QFT programme claims that the Yang--Mills carrier emerges from wall data, it must still construct the Euclidean measures, reflection-positive quotient, local net, positive-energy Poincare representation, gauge observables, and continuum limits described in [[compatible-with-existing-physics/relations-among-theories]] and [[compatible-with-existing-physics/local-physics-interface]].

The abstract transform does not alter the input algebra merely by re-expressing its Hilbert vectors, but it does not automatically preserve localization either. A global function \(Q_N(L)\) can mix regions; Wilson-flow observables at positive flow time are nonlocal from the four-dimensional viewpoint over their smoothing radius. Genuine Buchholz--Verch-style naturality therefore requires regional intertwining or quantitative off-diagonal/quasilocal bounds, not only the scalar covariance (RL37). Applying a parabolic four-dimensional flow before OS reconstruction may also smear across the reflection plane; applying a slice operator after \(B_r^{\mathrm{OS}}\) avoids that issue but is a different construction. Calling the transform “prelocal” does not waive the requirement that its recovered observable image satisfy the Clay axioms.

## Stopping and kill conditions

The candidate becomes physically useful only if all of the following survive scrutiny:

1. \(L_{r,I}\) is constructed from independent boundary or RG geometry, not from the Hamiltonian gap, glueball eigenvectors, or a fitted mass;
2. its kernel is exactly the constant or vacuum line on every relevant connected gauge-reduced component;
3. regulator and regional comparison maps intertwine \(L_{r,I}\) strongly enough to imply (RL36)--(RL37), or a controlled approximate version;
4. its functional-calculus windows obey the localization or quasilocal tail bounds needed by the recovered observable net;
5. a center ceiling is uniform in volume and in physical units along continuum removal;
6. the same-carrier comparison to the transfer Hamiltonian and eventually the full Poincare Casimir is proved;
7. in the paired route, the causal generators strongly commute and belong to one reconstructed translation representation; and
8. in \(3+1\) dimensions, either one fixed physical null-pair floor is proved on the whole vacuum complement after Poincare reconstruction, or an all-direction/direct-Casimir solder is supplied; the directional product itself is not relabeled as the Casimir.

The route is killed if the universal \(1/4\), \(1/12\), \(2\)-nat entropy, or \(\pi^2/3\) variance is called a mass scale; if the reference \(L_*\) is chosen from the observed gap; if the spectral center is discarded during recentering; or if the scale POVM is called an actuality selector. Each error confuses an equation of numbers with an identity of concepts.

## Claim ledger

| Status | Claim |
|---|---|
| Exact | the effect family (RL4) obeys the odds and derivative identities (RL5)--(RL6) |
| Exact | every positive spectral channel has a normalized \(\nu=1/2\) logistic profile centered at \(-\log\lambda\) |
| Exact | \(\mathscr S_{\widehat L}\) is an isometry on \((\ker L)^\perp\), preserves complex phases, and has the Sobolev identity (RL17) |
| Exact | the associated scale POVM measures \(-\log\widehat L\) with universal logistic variance \(\pi^2/3\) |
| Exact no-go | the universal logistic shape edge \(1/4\) and half-density energy \(1/12\) occur even for gapless \(L\), so neither is a mass gap |
| Exact | a lower spectral edge is equivalent both to an upper bound on the latent log-scale center and to norm-uniform saturation \(Z_N\to P_+\); strong saturation alone always occurs |
| Exact, joint spectral calculus | reciprocal rescaling moves the two causal centers oppositely and preserves their mean \(-\log\sqrt{K_+K_-}\) |
| Candidate construction | \(S_r^{\mathrm{res}}\) closes the coverage and phase-preservation part of the boundary-to-scale map once an independent natural \(L_{r,I}\) with kernel \(\mathbb C1\) is constructed |
| Open | selection of \(L_{r,I}\), RG-shell interpolation, uniform center confinement, transfer/Casimir comparison, and the four-dimensional continuum Yang--Mills construction |

[[contemporary-puzzles/yang-mills-mass-gap/receipts/resolvent_logistic_scale_receipt.py|The numerical receipt]] checks the scalar logistic, moment, entropy, Fisher, half-density, finite spectral-isometry, and reciprocal-center identities; [[contemporary-puzzles/yang-mills-mass-gap/receipts/resolvent-logistic-scale-receipt-output.txt|its stored output]] records the passing run. It does not prove the spectral theorem, choose \(L_{r,I}\), or test a Yang--Mills gap.

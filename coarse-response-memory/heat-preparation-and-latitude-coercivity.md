# Haar Preparation and Marginal Coercivity

The actual two-plaquette heat preparation admits a marginal Poincare bound in two controlled regimes: small coupling for all preparation times, including the ground-state limit, and sufficiently large coupling throughout each prescribed bounded interval of magnetic preparation time. Both proofs extract a positive coefficient from the full interacting evolution and control its remainder. The same evolution disproves broader positivity and convexity shortcuts. The result constrains the actual marginal and conditional source together; it does not replace the full physical dynamics by a marginal clock.

**Status: exact fixed-system preparation theorems, a finite full-carrier comparison, exact obstruction calculations, and numerical diagnostics; no continuum mass-gap theorem.** Supply the complete operator and physical carrier in [[two-plaquette-vacuum-and-relational-state|the two-plaquette construction]] (TP1--TP19). The actual conditional cost \(\mathcal F\), inherited marginal form and raw product split are those of [[radial-marginal-and-conditional-stress|the stationary marginal analysis]] (TP24--TP35). Graph, metric, Hamiltonian and Haar preparation remain inputs.

[[certified-ground-marginal-and-late-preparation|A separate exact-arithmetic certificate]]
now covers the explicit coupling \(\kappa=\lambda=1\): the actual
ground marginal and every positive preparation duration satisfy
\((\log\chi_t)''<0\) at every latitude, hence the same marginal
form bound. A cubic initial-layer estimate, full-residual time
rectangles and a contractive final tail cover the complete
trajectory. The bound strengthens to \(-1/1000\) for \(t\ge4\).
This does not assign a numerical value to the small-coupling
threshold below or establish the claim at every coupling.

## A uniform bound along the actual small-coupling preparation

Put \(\tau=\kappa t\), \(r=\lambda/\kappa\), and use the normalized
positive vector
\[
\psi_{r,\tau}=
\frac{e^{-\tau[K+r(2-a-b)]}1}
 {\|e^{-\tau[K+r(2-a-b)]}1\|},\qquad K=H_0/\kappa.
\]
Let \(\chi_{r,\tau}(a)=\sqrt{I_a\psi_{r,\tau}^2}\), where \(I_a\)
is the actual conditional product-Haar integral, and write
\[
p=\partial_a\log\chi,\quad
v=\partial_a^2\log\chi,\quad
\mathscr S=\mathcal F_t''+2\kappa p^2.
\tag{HP1}
\]
Primes are latitude derivatives; the subscript \(t\) on
\(\mathcal F_t\) denotes preparation time, not differentiation.
There exists \(r_*>0\), depending on this fixed compact system
but not on \(\tau\), such that for \(0<r\le r_*\) and every
\(\tau>0\),
\[
\boxed{
v(a,r,\tau)\le-\tfrac12r^2D(\tau)<0,\qquad
\mathscr S(a,r,\tau)/\kappa\ge r^2A(\tau)^2>0
}
\tag{HP2}
\]
uniformly for \(-1\le a\le1\). The functions \(A,D\) below are
computed from the full operator, not fitted to a marginal.

Consequently, for every \(0\le r\le r_*\), every \(t\ge0\),
and also the actual ground-state marginal,
\[
\boxed{
\kappa\int_{-1}^1(1-a^2)|f'(a)|^2\,d\nu_{r,t}
\ge\kappa\,\operatorname{Var}_{\nu_{r,t}}f,\qquad
d\nu_{r,t}\propto\chi_{r,\kappa t}^2\sqrt{1-a^2}\,da.
}
\tag{HP3}
\]
The implication is the existing
[[conditional-fisher-coercivity/linear-tilted-sphere-coercivity#Concave radial amplitudes retain the same bound|concave-amplitude latitude inequality]].
It extends from the smooth invariant core to the inherited
conservative form domain. It imposes no absorbing endpoint
condition on observables. At \(r=0\) or \(t=0\), use the Haar
law directly.

This is a bound on the form pulled back to the **complete**
one-plaquette readout. That readout is not invariant under the
full interacting generator: the hidden response in (TP11)
is nonzero. Thus (HP3) does not assert a gap \(\kappa\) for
the complete two-plaquette Hamiltonian. The small range is
in the ratio \(r\); no numerical \(r_*\), all-coupling/all-time
extension, uniform graph-size estimate or continuum limit
has been supplied. The distinct large-coupling initial-layer
result below has a time-dependent range of validity.

## The positive coefficient comes from the full shared evolution

For this coefficient calculation at fixed \(\tau\), discard
the scalar factor \(e^{-2r\tau}\) and expand
\[
P=e^{-\tau(K-rS)}1=1+rP_1+r^2P_2+O(r^3),\qquad S=a+b.
\]
Let
\[
A(\tau)=\frac{1-e^{-3\tau}}3,\qquad
B_c(\tau)=\int_0^\tau e^{-c(\tau-s)}A(s)\,ds.
\]
Since \(KS=3S\), \(P_1=AS\). The full second coefficient is
\[
\begin{aligned}
P_2={}&\tfrac12B_0+B_8(a^2+b^2-\tfrac12)\\
&+\tfrac12B_{9/2}(ab+z)
 +\tfrac32B_{13/2}(ab-z/3).
\end{aligned}
\tag{HP4}
\]
This follows by decomposing \(S^2\) into the constant mode,
the eigenvalue-eight mode, and both relational eigenchannels
of (TP6). In particular, the relative variable is present.
Its conditional mean vanishes; it has not been removed
from the state or evolution.

Expansion of \(\tfrac12\log I_aP^2\) gives
\[
v=r^2(2B_8-A^2)+O(r^3)=-r^2D(\tau)+O(r^3).
\]
Because \(A'=1-3A\) and \(B_8'=A-8B_8\),
\[
\boxed{
D'+8D=2A^2,\qquad D(0)=0,\qquad
D(\tau)=2\int_0^\tau e^{-8(\tau-s)}A(s)^2\,ds.
}
\tag{HP5}
\]
The coefficient is therefore strictly positive for every
\(\tau>0\). Explicitly,
\[
D=\frac1{36}-\frac4{45}e^{-3\tau}
+\frac19e^{-6\tau}-\frac1{20}e^{-8\tau},
\quad D\sim\tfrac23\tau^3,\quad D(\infty)=\tfrac1{36}.
\]
The integral is preferable for evaluating very small times.
It also gives
\[
D(\tau)\ge D(1)\min(\tau^3,1),\qquad
A(\tau)^2\ge A(1)^2\min(\tau^2,1).
\]
For the first inequality, \(D\) is increasing. On \(0<\tau\le1\),
write
\(D/\tau^3=2\int_0^1e^{-8\tau(1-s)}[A(\tau s)/\tau]^2ds\);
both factors decrease as \(\tau\) increases. The second
inequality follows similarly from concavity of \(A\).

Finally (TP40), after changing to \(\tau\), gives exactly
\[
\mathscr S/\kappa
=h v_{aa}+(2hp-7a)v_a+(-8-8ap)v+2hv^2-\partial_\tau v.
\]
Using \(p=rA+O(r^2)\), its quadratic coefficient is
\(8D+D'=2A^2\). This is the combined source, not an assertion
that \(\mathcal F_t''\) is nonnegative.

## The remainder is uniform from zero to infinite time

A fixed-time perturbation series would not prove (HP2).
For this fixed system, there are finite constants \(C_v,C_S\)
and a fixed parameter neighborhood such that
\[
\begin{aligned}
|v+r^2D|&\le C_v|r|^3\min(\tau^3,1),\\
|\mathscr S/\kappa-2r^2A^2|
 &\le C_S|r|^3\min(\tau^2,1)
\end{aligned}
\tag{HP6}
\]
uniformly in latitude. Here is why both ends of the time
interval are controlled.

For \(0\le\tau\le1\), bounded smooth magnetic multiplication
and the compact elliptic heat equation give all required
mixed \(r,\tau\) derivatives in fixed high raw Sobolev norms.
The first three time jets of \(v\), of orders zero, one and
two, vanish identically for every \(r\): through order
\(\tau^2\), \(\log P\) is affine in \(a+b\), and the hidden
normalizer contributes only a scalar to the marginal.
Likewise \(\mathscr S(0)=\partial_\tau\mathscr S(0)=0\).
Taylor's integral remainder in \(r\), applied after these
time-jet cancellations, gives the factors \(\tau^3\) and
\(\tau^2\). No convergence of an infinite time series is
assumed.

For \(\tau\ge1\), use the isolated simple zero mode of the
**unperturbed** \(K\). Since \(S\) is bounded, the resolvent
Neumann expansion on a separating contour produces the
analytic eigenvalue \(e(r)\) and rank-one projection
\(\Pi(r)\) of \(K-rS\), for a fixed sufficiently small
complex \(r\)-disk. Its shifted complementary semigroup
has a uniform positive decay margin. Hence
\[
e^{\tau e(r)}e^{-\tau(K-rS)}1
=\Pi(r)1+\mathcal R(r,\tau),\qquad
\|\mathcal R(r,\tau)\|_{H^m}\le C_m e^{-\delta\tau}
\]
for each needed fixed \(m\), uniformly on a smaller disk.
A fixed positive smoothing interval gives the same
uniform bounds for the time derivatives used in
\(\mathscr S\). These estimates use bounded perturbation
of a known finite compact operator, not the sought
interacting field-theory gap.

The shifted vector is uniformly close to \(1\) after the
disk is reduced. Conditional integration, square root and
logarithm therefore have uniformly bounded parameter
derivatives. For this analytic extension use the bilinear
square \(I_aP^2\), not \(I_a|P|^2\); on the real axis it
gives the physical marginal after scalar normalization. The time-dependent
scalar shift does not affect \(p,v\), or \(\mathscr S\).
Smooth radial invariance converts sufficiently high raw
bounds into the required latitude bounds, including
endpoints. This proves the time-uniform \(O(r^3)\) parts
of (HP6).

Choose a single positive \(r_*\) inside that neighborhood
with
\(C_vr_*\le D(1)/2\) and \(C_Sr_*\le A(1)^2\).
The lower bounds after (HP5) then prove (HP2).
Taking the fixed-system normalized ground-state limit
preserves the inequalities and gives (HP3). No
preparation-time-dependent coupling threshold is used.

## Large magnetic coupling also preserves the marginal on its initial layer

The opposite parameter regime has its own positive coefficient.
Put
\[
\epsilon=\kappa/\lambda,\qquad s=\lambda t,\qquad
P_\epsilon(s)=e^{s(S-\epsilon K)}1,\qquad S=a+b.
\]
Only a scalar magnetic factor has been removed from the
actual Haar preparation. For each fixed finite \(S_0>0\),
there exists \(\epsilon_*(S_0)>0\) such that, for
\(0<\epsilon\le\epsilon_*(S_0)\) and \(0<s\le S_0\),
\[
\boxed{
v(a,\epsilon,s)\le-\tfrac13\epsilon s^3<0,\qquad
\mathscr S(a,\epsilon,s)/\kappa\ge s^2>0.
}
\tag{HP15}
\]
The bounds are uniform in latitude, including endpoints.
Consequently the inherited marginal form satisfies (HP3)
throughout this interval, now at sufficiently large \(r\).
No numerical value of \(\epsilon_*(S_0)\) is asserted.

The first coefficient is explicit. For the full shared
operator,
\[
\Gamma(S)=2-a^2-b^2+z/2,\qquad
K e^{uS}=e^{uS}\{3uS-u^2\Gamma(S)\}.
\]
A one-sided Duhamel derivative at \(\epsilon=0\) gives
\[
\log P_\epsilon(s)
=sS+\epsilon\left[-\tfrac32s^2S+
                    \tfrac13s^3\Gamma(S)\right]
+O(\epsilon^2).
\tag{HP16}
\]
At zero diffusion the conditional hidden density is
proportional to \(e^{2sb}\) against product Haar.
Its mean of \(z\) is zero, and its moments of \(b\) do not
depend on \(a\). Since
\(\log\chi=\tfrac12\log I_aP_\epsilon^2\) up to a scalar,
two latitude derivatives of the first coefficient give
\(-2s^3/3\). The relative variable has been integrated in
the actual state, not deleted from its dynamics.

Uniformity down to \(s=0\) requires more than a fixed-time
expansion. On the original seven-link product, let
\(U_j=\partial_\epsilon^jP_\epsilon\). For \(j=1,2\),
\[
\partial_sU_j=(S-\epsilon K)U_j-jKU_{j-1},\qquad
U_j(0)=0,\qquad U_0(0)=1.
\]
Raw link Killing derivatives commute with the free sum of
edge Casimirs \(K\). This assertion is made before reduction:
arbitrary independent derivatives in the two-holonomy
coordinates need not commute with its shared terms.
After raw differentiation, multiplication by \(S\) produces
only lower-order commutator sources. The homogeneous
propagator has sup norm at most \(e^{2s}\), uniformly for
real \(\epsilon\ge0\). Iterated Duhamel estimates therefore
bound the required mixed parameter, time and raw spatial
derivatives on \(0\le s\le S_0\), \(0\le\epsilon\le\epsilon_0\).
Each parameter derivative uses two additional spatial
derivatives of the preceding solution; the smooth data
supply them. Difference quotients justify the right
parameter derivatives at zero. No negative-diffusion
evolution or complex \(\epsilon\)-disk is used.

Also \(e^{-2s}\le P_\epsilon(s)\le e^{2s}\). Conditional
integration and logarithms preserve these finite-time smooth
bounds. Radial invariance converts sufficiently high raw
bounds to latitude bounds at both endpoints. For every
\(\epsilon\), the time jets \(v(0),v_s(0),v_{ss}(0)\)
vanish. Applying Taylor's parameter remainder after these
cancellations yields, with constants depending on \(S_0\),
\[
\begin{aligned}
\|v+\tfrac23\epsilon s^3\|_{C_a^2}
 &\le C\epsilon^2s^3,\\
\|\partial_s(v+\tfrac23\epsilon s^3)\|_\infty
 &\le C\epsilon^2s^2,\\
\left|\mathscr S/\kappa-2s^2\right|
 &\le C'\epsilon s^2.
\end{aligned}
\tag{HP17}
\]
For the last line use (TP40) in \(s\)-time:
\[
\mathscr S/\kappa
=hv_{aa}+(2hp-7a)v_a+(-8-8ap)v+2hv^2
 -\epsilon^{-1}\partial_sv.
\]
Here \(p=O(s)\), \(v=O(\epsilon s^3)\), with the required
latitude derivatives controlled by the first line of (HP17).
The time derivative supplies the leading \(2s^2\); all other
terms are \(O(\epsilon s^2)\) on the specified interval.
Reducing \(\epsilon_*(S_0)\) proves (HP15).

The quantifiers are essential. At fixed \(\kappa\), the
physical heat window \(0<t\le S_0/\lambda\) shrinks with
increasing \(\lambda\). Constants may deteriorate with \(S_0\);
this argument neither controls growing \(S_0\) as
\(\epsilon\to0\) nor reaches a large-coupling ground state.
The zero-diffusion law used to compute the coefficient is
an auxiliary limit, not a field-theory construction.
Nevertheless the result proves marginal coercivity in the
same actual preparation regime where (TP38) disproves
angular-curvature and reconstructed stationary-shape
preservation. Those stronger geometric signs are unnecessary.

## The full ground-state comparison needs a genuine hidden bound

The inherited marginal estimate can be lifted without
replacing the compressed evolution by a semigroup. This
requires additional data about the actual hidden law.
At the ground-state limit, retain the four raw left-square
links \(A\) and all three other links \(B\). On the full
physical carrier, write \(P=E[\cdot\mid A]\),
\(\mathcal E=\mathcal E_A+\mathcal E_B\), and
\(a[P F]=\kappa\int h|(PF)'|^2d\nu\).
Whole gauge invariance makes \(PF\) a function of \(a\).
The
[[local-score-bounds-and-the-order-of-hidden-response#Conditional projection preserves the inherited domain|actual conditional derivative estimate]]
gives
\[
\sqrt{a[PF]}\le\sqrt{\mathcal E_A[F]}+\beta\|F-PF\|,
\qquad \beta^2\le25\kappa r^2.
\tag{HP9}
\]
The incidence sum is five: the shared link meets two
plaquettes and each of the other retained links meets one.

At fixed retained links, hidden internal-vertex invariance
reduces physical functions of the hidden path to its
full holonomy \(y\in SU(2)\), not just its trace.
Its energy is \(3\kappa\int|\nabla_yF|_Q^2d\beta_A\).
The
[[algebra/partial-bochner-and-ground-state-score#Compact gauge normalization|local ground-score bound]]
gives \(|\nabla_y\log\psi|_Q\le r\). Since the diameter
in \(Q=-2\operatorname{Tr}\) is \(2\pi\),
\(\operatorname{osc}_y\log\beta_A\le4\pi r\).
Comparing the maximum and minimum density with the Haar
\(D_Q\)-gap \(3/4\) proves
\[
\mathcal E_B[F]\ge\rho\|F-PF\|^2,
\qquad \rho=\frac{9\kappa}{4}e^{-4\pi r}>0.
\tag{HP10}
\]
This controls all conditional holonomy functions, including
the relational channel. It is a vertical estimate, not an
assumption on the hidden block of the full Hamiltonian.

Combining (HP3), (HP9), (HP10) and total variance is exactly
the existing
[[yang-mills-continuum-crossover/two-scale-rg-descent-and-the-crossover-lemma|two-scale Fisher--Poincare argument]]:
\[
\operatorname{gap}(H-E_0)\ge
\frac{\gamma+\rho+\beta^2-
\sqrt{(\gamma+\rho+\beta^2)^2-4\gamma\rho}}2>0,
\quad \gamma=\kappa,\quad 0\le r\le r_*.
\tag{HP11}
\]
Indeed the variance is at most
\(\mathcal E_B/\rho+
(\sqrt{\mathcal E_A}+\beta\sqrt{\mathcal E_B/\rho})^2/\gamma\);
the largest eigenvalue of this two-dimensional quadratic
comparison gives (HP11). No condition \(\beta^2<\rho\)
or memoryless projection is required. Smooth physical
functions form the inherited core, so the inequality passes
to the whole physical form domain.

This is a quantitative compatibility check on a supplied
finite system, not a new proof of finite-gap existence:
(HP6) already uses fixed-system perturbative spectral
isolation. It supplies neither arbitrary-coupling marginal
coercivity nor graph-size/continuum uniformity. In particular
the hidden lower bound (HP10) deteriorates exponentially in
\(r\). The preparation parameter is not an additional
physical clock for (HP11).

## The actual heat trajectory can leave the stationary shape class

Start the full seven-link heat evolution at the Haar amplitude,
\(\psi_t=e^{-tH_\lambda}1/\|e^{-tH_\lambda}1\|\), and use
its actual factors \(\chi_t,\Phi_t\). The
[[conditional-fisher-coercivity/moving-fiber-connection#Conditional relaxation supplies the time-dependent force|time-dependent conditional balance]]
gives, with \(q_t=\partial_t\log\chi_t\),
\[
\mathcal U_t:=\kappa\frac{h\chi_t''-3a\chi_t'}{\chi_t}
=\lambda(1-a)+\mathcal F_t+q_t-\bar E(t).
\tag{TP36}
\]
Thus a potential reconstructed by treating a snapshot as a
stationary eigenvector differs from the actual instantaneous
potential by \(q_t\), up to a scalar. Only at stationarity
may one omit its spatial derivative. Likewise (TP30) acquires
\(-2\langle\nabla_A\Phi(\nabla a),\dot\Phi\rangle_B\).

There is an exact actual-trajectory obstruction to preserving
either the decreasing-\(\mathcal U_t\) cone or positive angular
curvature. Put \(H_\lambda=\kappa K+\lambda V\), where
\(V=2-a-b\), fix \(s>0\), and take \(t=s/\lambda\).
As \(\lambda\to\infty\) at fixed \(\kappa\),
\[
e^{-(s/\lambda)H_\lambda}1
\longrightarrow e^{-s(2-a-b)},\qquad
\chi_{s/\lambda}(a)\longrightarrow C_s e^{sa}.
\tag{TP37}
\]
Here \(C_s>0\) is the marginal normalization constant. The
second limit uses the actual product-Haar hidden integration:
\(I_ae^{2sb}\) is independent of \(a\).

The first limit holds with error \(O(\kappa/\lambda)\) in
every fixed raw smooth norm on a bounded \(s\)-interval.
Indeed, for \(\eta=\kappa/\lambda\) and
\(T_\eta(s)=e^{-s(\eta K+V)}\), Duhamel gives
\[
T_\eta(s)1-e^{-sV}
=-\eta\int_0^s T_\eta(s-r)K e^{-rV}\,dr.
\]
Raw Killing derivatives commute with \(K\); differentiating
the evolution and bounding the fixed smooth potential terms
gives uniform finite-time smooth bounds for the integral.
Also \(e^{-4s}\le T_\eta(s)1\le1\). Thus normalization,
hidden integration and square roots preserve smooth convergence,
including the fixed interior derivatives used below.

Consequently, at each fixed interior \(a\),
\[
\begin{aligned}
\partial_a\mathcal U_{s/\lambda}
 &\longrightarrow\kappa(-3s-2as^2),\\
-2\partial_\theta^2\log[\sin\theta\,
 \chi_{s/\lambda}(\cos\theta)]
 &\longrightarrow\frac{2}{1-a^2}+2as.
\end{aligned}
\tag{TP38}
\]
For \(s=4\), \(a=-1/2\), these limits are \(4\kappa>0\)
and \(-4/3<0\). Both adverse signs therefore occur in the
actual full evolution at sufficiently large **finite** magnetic
coupling. They are not artifacts of an endpoint chart or of
discarding the relational channel.

This disproves the proposed stationary-shape preservation
strategy. It does **not** disprove
\(\mathcal F_t'<\lambda\), since (TP36) contains the
additional derivative \(q_t'\). Nor does negative angular
curvature imply a vanishing marginal gap. The limit in (TP37)
is precisely a linear-tilted latitude law for which a different
Poincare estimate survives.

## Latitude concavity is a sharper remaining target

For any actual smooth positive marginal amplitude \(\chi(a)\),
the latitude probability density is proportional to
\(\chi(a)^2\sqrt{1-a^2}\), not to \(\chi(a)^2\) alone.
The
[[conditional-fisher-coercivity/linear-tilted-sphere-coercivity#Concave radial amplitudes retain the same bound|concave-amplitude latitude estimate]]
therefore gives
\[
\boxed{
(\log\chi)''\le0
\quad\Longrightarrow\quad
\kappa\int h|f'|^2d\nu\ge\kappa\operatorname{Var}_\nu f.
}
\tag{TP39}
\]
This is sufficient, not necessary. It follows because the
negative log density has second derivative
\((1+a^2)/h^2-2(\log\chi)''\ge1/h\). Unlike angular
curvature, this condition holds in the rapidly tilted limit
(TP37). The
[[algebra/partial-bochner-and-ground-state-score#A latitude estimate is uniform in magnetic coupling|single-plaquette heat argument]]
proves it at every finite coupling for that supplied scalar
model, giving a coupling-uniform bound. For the **actual
two-plaquette marginal**, (HP2) proves preservation on a fixed
small-coupling range for all preparation times, and (HP15)
proves it at sufficiently large coupling on each prescribed
bounded magnetic-time interval. Arbitrary-coupling/all-time
preservation remains open.

The exact evolution exposes that extension's extra term. With
\(p=\partial_a\log\chi_t\), \(v=\partial_a^2\log\chi_t\),
\[
\partial_tv=\kappa\left[
h v''+(2hp-7a)v'+(-8-8ap)v+2hv^2-2p^2\right]
-\mathcal F_t''.
\tag{TP40}
\]
Thus \(\mathcal F_t''\ge0\) throughout preparation would
be a sufficient additional hypothesis for the scalar maximum
argument. The weaker first-contact condition compares
\(\mathcal F_t''\) with \(-2\kappa p^2\), not with zero.
Neither follows from positivity of \(\epsilon_t,T_t,M_t\)
or from the integrated dissipation law (MF25). This identifies
the conditional Hessian estimate needed beyond (HP2), without
replacing the actual fiber equation by an instantaneous hidden
eigenproblem.

Ordinary joint log-concavity is not a ready-made replacement.
Set \(c=ab+z\). The orbit body becomes the convex set where
the matrix with diagonal \(1\) and off-diagonal entries
\(a,b,c\) is positive semidefinite. Even on this body, the
full diffusion need not preserve Euclidean log-concavity.
Take the smooth positive initial amplitude
\(u_0=\exp[-\alpha(a+b)^2/2]\), \(\alpha>0\), and
\(\xi=(1,-1,0)\) in \((a,b,c)\). Its logarithmic Hessian
vanishes in direction \(\xi\). Along
\((a,b,c)=(r,-r,0)\), the logarithmic gradient vanishes,
and (TP3)--(TP4) give
\[
\left.\partial_\xi^2\partial_t\log u_t\right|_{t=0,(0,0,0)}
=3\kappa\alpha>0.
\tag{TP41}
\]
Explicitly the kinetic contribution there is
\(-\kappa\alpha[2-a^2-b^2+(c-ab)/2]\); the magnetic
term is linear and contributes no Hessian. This counterexample
uses another initial vector, not the Haar trajectory. It rules
out proving (TP39) by a general joint-concavity preservation
axiom. The missing statement must use the actual preparation
or a more specific compatible class.

## The density contact equation keeps the local loss curvature

Apply the
[[conditional-fisher-coercivity/moving-fiber-connection#A local loss density exposes the unclosed shape source|raw local-loss identities]]
to this actual preparation. Write \(R=\chi^2\),
\(q=R'/R=2p\), and let \(\mathcal J\) include all seven
raw kinetic derivatives and \(V=\lambda(2-a-b)\).
With \(U=\mathcal J/R\) and \(N=RR''-(R')^2\),
\[
\begin{aligned}
R_t&=\kappa(hR''-3aR')-2\mathcal J+2\bar E R,\\
N_t&=\kappa hN''
 -\kappa(7a+2hq)N'\\
&\quad+\left[2\kappa hR''/R-8\kappa
             +4(\bar E-U)\right]N
 -2R^2\left[U''+\kappa q^2\right].
\end{aligned}
\tag{HP18}
\]
This follows by differentiating the first line and
substituting \(N=R^2(\log R)''\). It is an identity for
the actual density, not an autonomous replacement clock.
No coefficient divides by \(h\).

At an interior first contact with \(N=0\) from \(N\le0\),
one has \(N'=0,N''\le0\). Since
\(U=\kappa hp^2+\lambda(1-a)+\mathcal F\), the source
at contact is exactly
\[
U''+\kappa q^2=\mathcal F''+2\kappa p^2=\mathscr S.
\tag{HP19}
\]
At a latitude endpoint the same equality holds: \(h=0\)
and \(p'=N/(2R^2)=0\). The remaining endpoint drift
\(-7\kappa aN'\) is nonpositive by the one-sided maximum
condition. Thus regularizing the derivatives has not
removed the combined-source obligation in (TP40).

Applying (RD5) to the actual loss integrand
\(\kappa g_{ij}\psi_i\psi_j+V\psi^2\) makes
\(\mathcal J''\) regular, but generally requires mixed
invariant derivatives of \(\psi\) through order five.
The next local-loss row (MF28) adds a flux and conditional
speed rather than closing these derivatives from the
marginal. This identifies where the proposed finite
shape closure stops; it is not a proof that no
whole-state estimate can control that source.

## A flat marginal does not select its compatible hidden state

Even latitude concavity itself is not preserved for arbitrary
positive initial vectors under this same Hamiltonian. Choose
\(0<d<1\) and set
\[
R(a)=1+\frac{d^2(1-a^2)}4,\qquad
\psi_{\rm in}=\frac{1+dz}{\sqrt{R(a)}}.
\]
This is a smooth strictly positive full-carrier invariant
vector. Since \(I_az=0\) and \(I_az^2=h/4\), it is already
normalized and its marginal satisfies \(\chi_{\rm in}\equiv1\).
Thus its initial \(p=v=0\), just as for the Haar vector,
but its conditional state is different.

Formula (TP25), with \(\Phi=\psi_{\rm in}\), gives exactly
\[
\mathcal F(a)=\lambda+\kappa\left[
\frac{d^2(1-a^2/4)}{R}
-\frac{d^4a^2h}{16R^2}\right],\qquad
\mathcal F''(0)=-\frac{\kappa d^2(2-d^2)}{4(1+d^2/4)^2}<0.
\tag{HP7}
\]
Indeed, \(\Phi_a=d^2a\Phi/(4R)\), \(\Phi_b=0\),
and \(\Phi_z=d/\sqrt R\). The conditional contractions
are \(I_ag_{zz}=1-a^2/4\) and
\(I_a[g_{az}(1+dz)]=-dah/4\); their mixed contribution
must be included. Also \(I_a(b\Phi^2)=0\).
By (TP40),
\[
\left.\partial_tv\right|_{t=0,a=0}=-\mathcal F''(0)>0.
\]
The marginal therefore leaves the latitude-concavity class
immediately. This is a loss of that sufficient shape
condition, not a proof that its Poincare gap vanishes.

Requiring nonnegative harmonic coefficients does not repair
this counterexample. The power series of
\[
R^{-1/2}=(1+d^2/4)^{-1/2}
\left[1-\frac{d^2}{4+d^2}a^2\right]^{-1/2}
\]
has positive coefficients and converges in every smooth norm.
Multiplication by \(a\) has nonnegative matrix entries in
(TP19), and both \(1\) and \(z=B_{111}\) are positive
multiples of their respective normalized basis vectors.
Consequently \(\psi_{\rm in}\) has nonnegative coefficients
in the complete physical harmonic basis as well.

This initial vector is neither the Haar vector nor exchange
symmetric. It excludes a preservation law based only on a
flat retained marginal and coefficient positivity; it does
not contradict (HP2). The prepared **joint** state is an
essential input to that theorem, not information recoverable
from the marginal alone.

[[positive-amplitude-kernel-and-preparation#A positive-feature Gram kernel can still lose marginal concavity|The positive-kernel control]]
strengthens this obstruction. It is exchange symmetric,
has both complete configuration marginals exactly Haar,
and is a Gram average of strictly positive features.
Nevertheless its marginal curvature becomes positive
under the same full heat equation. The actual preparation
has this Gram property, but its entire Gram cone cannot
replace the distinguished initial state.

[[replica-weighted-correlations-and-the-local-readout#The actual local target uses a posterior law|The prepared replica decomposition]]
now gives an exact alternative expression for \(v\):
one half of the posterior mean component log-curvature
plus its posterior score variance. Both weights come from
the actual squared amplitude. A global relative-harmonic
inequality or a pointwise feature bound does not supply
this local estimate; the latter proposed bound has an
explicit admissible-path obstruction.

[[path-source-tilts-and-the-curvature-budget#A uniform fractional margin is impossible at late time|The resolved source budget]]
also excludes a fixed fractional curvature margin across all
preparation times. Both positive terms grow like \(t^2\),
although their difference tends to the finite ground-state
curvature. This does not contradict (HP2); it prevents proving
that result by separate estimates with a fixed percentage slack.

## The actual joint logarithm need not be concave

The actual Haar trajectory also defeats a joint-concavity
shortcut in fixed hidden-integration coordinates. On an
interior latitude, write \(z=\sqrt h\,\eta\). The hidden
labels satisfy \(b^2+\eta^2\le1\), with conditional Haar
measure \(db\,d\eta/\pi\), independent of \(a\).
This \(\eta\) is not the Gram coordinate \(c=ab+z\)
used in (TP41).

For \(P=e^{2\lambda t}e^{-tH_\lambda}1\), put
\(\phi=\log P\). The full generator gives
\[
\begin{aligned}
\phi={}&\lambda(a+b)t-\tfrac32\kappa\lambda(a+b)t^2\\
&+\left[\tfrac32\kappa^2\lambda(a+b)
+\tfrac{\kappa\lambda^2}{3}(2-a^2-b^2+z/2)\right]t^3
+O(t^4).
\end{aligned}
\]
At \((a,b,\eta)=(1/2,0,0)\), its mixed derivative is
\(\phi_{a\eta}=-\kappa\lambda^2t^3/(6\sqrt3)+O(t^4)\),
while \(\phi_{\eta\eta}=O(t^4)\) and
\(\phi_{aa}=O(t^3)\). Therefore
\[
\det\begin{pmatrix}\phi_{aa}&\phi_{a\eta}\\
\phi_{a\eta}&\phi_{\eta\eta}\end{pmatrix}
=-\frac{\kappa^2\lambda^4}{108}t^6+O(t^7)<0
\tag{HP8}
\]
at sufficiently small positive time for fixed positive
\(\kappa,\lambda\). The joint Hessian is indefinite even
though the actual marginal is latitude-concave there.

The direct conditional differentiation identity is instead
\[
(\log\chi)''=\mathbb E_\beta[\phi_{aa}]
+2\operatorname{Var}_\beta(\phi_a),\qquad
d\beta\propto e^{2\phi}\,db\,d\eta.
\]
It is the scalar case of
[[rg-covariance-residue/conditioned-source-transport|conditional score response]].
Any estimate must compare these terms together. The fixed
disk chart degenerates at \(a=\pm1\); bounding the terms
separately need not preserve their endpoint cancellations.
Neither a joint log-concavity theorem in this chart nor an
arbitrary conditional-variance bound proves the needed sign.

## A regular curvature formula keeps the hidden derivatives

[[algebra/radial-conditional-differentiation|Spherical conditional differentiation]]
removes the endpoint divisions before making an estimate.
With \(F=\psi_t^2\), \(q=1-b^2-\eta^2\) and
\(I=\pi^{-1}\int_{b^2+\eta^2\le1}db\,d\eta\), let
\(R(a)=I F(a,b,\sqrt h\eta)\). The shared identities give
\[
\begin{aligned}
R'&=I[F_a-aqF_{zz}/2],\\
R''&=I[F_{aa}-aqF_{azz}-qF_{zz}/2+a^2q^2F_{zzzz}/8],
\end{aligned}
\tag{HP12}
\]
with every derivative at fixed \((a,b,z)\). The actual
latitude curvature is \((RR''-(R')^2)/(2R^2)\).
Consequently an all-coupling extension can target this
combined expression without separately singular score
bounds. The fourth-jet control in that note shows why
endpoint conditional laws and lower jets alone do not
determine its sign. This is a sharper estimate to prove,
not the estimate's proof.

There is a direct regularity justification for the actual
finite-time Haar preparation, rather than an inference from
converged Hilbert-space approximants. Write
\[
P_t=e^{-t(\kappa K-\lambda(a+b))}1
=\sum_{n\ge0}\lambda^nP_n(t),\quad P_0=1,
\quad P_n(t)=\int_0^t e^{-\kappa(t-s)K}(a+b)P_{n-1}(s)\,ds.
\tag{HP13}
\]
The full \(K\) preserves weighted polynomial degree, with
weights one for \(a,b\) and two for \(z\). Thus \(P_n\)
has ordinary degree at most \(n\). Free Markov contraction
and \(|a+b|\le2\) give
\(\|P_n(t)\|_{\infty,\mathcal B}\le(2t)^n/n!\),
where \(\mathcal B\) is the orbit body (TP2).

The cube \([-1/2,1/2]^3\) lies inside \(\mathcal B\).
Its tensor Chebyshev expansion has coefficients at most
eight times this norm and only indices of total degree
at most \(n\). For any fixed \(L>0\), the elementary
recurrence bound \(|T_j(2z)|\le(1+4L)^j\) on
\(|z|\le L\) therefore yields
\[
\sup_{|a|,|b|,|z|\le L}|P_n(t)|
\le8(n+1)^3(1+4L)^n(2t)^n/n!.
\tag{HP14}
\]
This is a bound on a complex polydisk. Factorial decay
gives an entire invariant representative for \(P_t\), with
uniform convergence of every fixed invariant derivative
on compact sets and bounded time intervals. Squaring and
physical scalar normalization then supply the \(C^4\)
representative needed by (HP12), including its endpoint
limits. At zero time all \(P_n\), \(n\ge1\), vanish.
Positivity gives a zero-free neighborhood for logarithms
near the real orbit body; the logarithm need not be entire.
These estimates do not justify a uniform \(t\to\infty\)
passage in invariant jets without another bound.

## Conditional convexity already fails at short times

The simpler sufficient condition \(\mathcal F_t''\ge0\)
in (TP40) is false in the actual Haar preparation, not just
for arbitrary initial vectors. An exact finite Taylor
calculation gives the obstruction for every fixed
\(\kappa,\lambda>0\).

Drop the harmless scalar factor \(e^{-2\lambda t}\) and
write \(P(t)=e^{2\lambda t}e^{-tH_\lambda}1\). The finite
Taylor coefficients are determined by
\[
P_0=1,\qquad
P_n=\frac{[-\kappa K+\lambda(a+b)]P_{n-1}}{n},
\qquad K=H_0/\kappa.
\tag{TP42}
\]
The operator \(K\) is exactly (TP3), including the shared
derivatives. Conditional integration of these polynomials
uses
\[
I_a[b^{2m}z^{2j}]
=h^j\frac{(2m)!(2j)!}
 {4^{m+j}m!j!(m+j+1)!};
\]
every odd power of \(b\) or of \(z\) has zero mean. Put
\(R_n=\sum_{j=0}^nI_a(P_jP_{n-j})\), \(R_0=1\).
For the logarithm coefficients,
\[
\ell_0=0,\qquad
\ell_n=R_n-\frac1n\sum_{j=1}^{n-1}j\ell_jR_{n-j},
\qquad w_n=\ell_n/2.
\]
The \(w_n\) are the latitude-dependent coefficients of
\(\log\chi_t\), up to scalar functions of time. By
(TP36), the coefficient of \(t^n\) in \(\mathcal F_t''\)
is
\[
\partial_a^2\left\{
\kappa\left[h\left(w_n''+
 \sum_{j=0}^n w_j'w_{n-j}'\right)-3aw_n'\right]
 -(n+1)w_{n+1}\right\}.
\]
Thus coefficients through \(P_7\) suffice to obtain
\[
\boxed{
\mathcal F_t''(a)
=-\frac{\kappa^2\lambda^4}{60}t^5
 +\frac{241\kappa^3\lambda^4}{720}t^6+O(t^7).
}
\tag{TP43}
\]
All earlier orders vanish identically. An independent
coefficient check in (TP25), using
\(\Phi=P/(I_aP^2)^{1/2}\), separates the two costs:
at order five the potential curvature is
\(-\kappa^2\lambda^4/60\) and the kinetic curvature is
zero; at order six they are respectively
\(119\kappa^3\lambda^4/720\) and
\(61\kappa^3\lambda^4/360\). The latter sum gives (TP43).
No extra \(\Phi^2\) is inserted in the amplitude kinetic
integral.

Only a finite Taylor expansion is used, not convergence of
an infinite heat series at zero. Smooth compact initial data
lie in every required operator domain; the integral semigroup
remainder is bounded in any fixed raw smooth norm. Conditional
integration and radial endpoint regularity then control the
displayed remainder uniformly in \(a\) for fixed
\(\kappa,\lambda\). Hence \(\mathcal F_t''<0\) for all
sufficiently small positive times at those fixed coefficients.

The same recursion proves the positive counterbalance:
\[
\boxed{
(\log\chi_t)''=-\frac23\kappa\lambda^2t^3+O(t^4),\qquad
\mathcal F_t''+2\kappa[(\log\chi_t)']^2
=2\kappa\lambda^2t^2+O(t^3).
}
\tag{TP44}
\]
Thus the actual marginal satisfies latitude concavity at
sufficiently short positive time, and the weaker source
comparison has the favorable sign there. Those short-time
formulas alone do not control the full preparation. The
uniform remainder argument (HP4)--(HP6) supplies that control
on a fixed small-coupling range. Equations (HP15)--(HP17)
give the distinct large-coupling initial-layer extension.
The uncontrolled intermediate and late-time regimes still
require the combined source, or another sufficient estimate,
not either discarded separate-sign condition.

## Numerical controls on the actual preparation

The [[receipts/two_plaquette_vacuum_receipt.py|interacting receipt]]
evolves the full Haar amplitude with every relational harmonic
retained within each cutoff. For the coefficients in (HP5),
it compares the positive integral for \(D\) with the closed
formula and checks zero time separately. On cutoffs 6 and 8,
at \(r=0.05,0.1,0.2\) and
\(\tau=0.03,0.1,0.5,2,8\), the largest relative error in
\(v/[-r^2D]\) is respectively about
\(0.01340,0.02692,0.05434\); for
\(\mathscr S/[2\kappa r^2A^2]\) it is
\(0.007514,0.015055,0.030214\). The errors decrease
approximately linearly with \(r\), as the uniform cubic
remainder predicts. Latitude endpoints are included for
\(v\); the source uses interior finite differences of the
time-corrected slope. This finite list does not prove the
uniform remainder or estimate a valid \(r_*\).

For the opposite-regime coefficients in (HP17), use
\(\kappa=1\), \(\lambda=32,64,128\) and \(s=0.5,1,2\).
On cutoffs 16 and 18, the maximum relative errors in
\(v/[-2\epsilon s^3/3]\) are respectively
\(0.393032,0.232636,0.127813\); for
\(\mathscr S/[2\kappa s^2]\) they are
\(0.264314,0.148501,0.079116\).
The errors decrease toward the predicted linear dependence
on \(\epsilon\). The largest cutoff changes in these ratios
are below \(1.1\,10^{-8}\) and \(1.6\,10^{-9}\).
The curvature includes analytic endpoint jets; the source
uses the actual temporal correction and interior slope
differences. These finite tests do not estimate
\(\epsilon_*(S_0)\) or extend the theorem to late time.

At \(\kappa=1,\lambda=16,t=0.2\),
the sampled maximum reconstructed slope is \(+2.927893896\),
whereas including the temporal correction gives a maximum
instantaneous slope \(-16.069801515\). Cutoffs 14 and 16
change either profile by less than \(10^{-8}\). At
\(\lambda=64,t=1/16\), sampled angular curvature reaches
\(-0.970433914\), with refinement change below
\(1.3\,10^{-5}\). Thus the code separates the two quantities
in (TP36) and independently witnesses (TP38).

Latitude log-concavity survives the sampled preparations at
\(\lambda=2,16,64\); this remains evidence, not a proof of
(TP39)'s interacting hypothesis. Independent positive hidden
quadrature at \(\lambda=16,t=0.2\) gives
\(\|\dot\chi\|^2\approx1.901526029\) and
\(\int\rho\|\dot\Phi\|^2\approx1.982225509\), whose
doubled sum agrees with \(-\dot{\bar E}\approx7.767503075\).
Direct conditional-cost integration also checks the temporal
correction without reconstructing it from the scalar equation.

At \(\lambda=64,t=3/64\), finite differences of the
time-corrected slope on \(|a|\le0.9\) give
\(\mathcal F_t''\) between \(-0.01588143\) and
\(-0.00565991\). Cutoffs 16 and 18 change this profile by
less than \(5.1\,10^{-7}\); grids of 2001 and 4001 points
change it by less than \(6.7\,10^{-9}\). The sampled minimum
of \(\mathcal F_t''+2p^2\) is about \(13.5784\).
This finite check distinguishes the failed stronger condition
from the surviving weaker one. The exact small-time signs in
(TP43)--(TP44), not finite differences, supply the theorems.
At \(\lambda=128,t=4/128\), cutoffs 20 and 22 give
\(\mathcal F_t''\in[-0.039548,-0.014960]\) on the same
sampled interior and a combined-source minimum about
\(25.5257\). Cutoff and grid changes are below
\(1.1\,10^{-7}\) and \(9.0\,10^{-8}\). These resolved
larger-coupling controls do not extend (HP2)'s analytic range.

The regular conditional derivatives in (HP12) are checked
independently by expanding every retained Legendre channel
into polynomials in \((a,b,z)\), then differentiating before
hidden integration. At \(\lambda=16,t=0.2\), the values of
\(R,R',R''\), including both latitude endpoints, agree with
the separate harmonic marginal jets within
\(5.7\,10^{-14}\). Cutoff and quadrature changes are below
\(3.3\,10^{-10}\) and \(5.7\,10^{-14}\).
At \(a=0.9999\), the two terms in the singular chart
formula are approximately \(-19.85591332\) and
\(+19.57126055\), leaving \(-0.2846527764\); the regular
formula agrees without subtracting those divergent terms.
The polynomial test (RD9) checks the fourth-jet obstruction
separately. These are finite diagnostics; derivative
convergence of the actual heat state is supplied by
(HP13)--(HP14), not by agreement of two cutoffs.

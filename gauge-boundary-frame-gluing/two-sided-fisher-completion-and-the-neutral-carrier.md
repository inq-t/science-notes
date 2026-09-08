# Two-Sided Fisher Completion and the Neutral Carrier

The joint entropy of left and right path shifts determines a response whose finite smooth cylinders are exactly the simultaneous-conjugation invariants. Their closure supports an actual Markov generator with a unique constant vacuum and exact threshold two, not attained by an excited eigenvector. This constrains the observable carrier and its response together, conditional on a specified compact-group heat state, transformation family, and Fisher-dual prescription. The construction is compatible with longer path horizons and changes of heat-time coordinates, but not with the separate same-clock annular restart law.

**Status: [EXACT] for the declared path-state construction, finite-cylinder domain, closed realization, and auxiliary spectral threshold; [OPEN] for selection of the underlying state and transformation family, a spacetime-local observable net, and the Yang--Mills physical clock.**

## The joint action has an actual state cost

Let \(G\) be compact and connected with nonabelian simple Lie algebra
\(\mathfrak g\). Fix a bi-invariant metric \(Q\), a \(Q\)-orthonormal
basis \(T_a\), and \(0<T<\infty\). On
\(\mathscr X_T=C_e([0,T],G)\), use the law \(\mu_T\) of
\[
dX_s=\sqrt2 X_s\circ dB_s,\qquad X_0=e,\qquad
-\sum_a\operatorname{ad}(T_a)^2=c_A I,\qquad
r(s)=e^{-c_As}.
\tag{JF1}
\]
Here \(c_A>0\), and the heat generator is \(\Delta_Q\). Applying it to
the adjoint representation gives
\(\mathbb E_{\mu_T}\operatorname{Ad}_{X_s}=r(s)I\).
The index \(s\) is the supplied heat-area coordinate of
[[shared-driver-response-and-the-nested-holonomy-clock|the nested-holonomy
carrier]], not a physical clock.

Declare the two-sided multiplication family
\[
\mathcal T_{k,l}X(s)=k(s)X_s l(s)^{-1},\qquad
k(0)=l(0)=g\in G,
\tag{JF2}
\]
where \(k,l\) are absolutely continuous with square-integrable logarithmic
velocities. This is a group action, with pairwise pointwise multiplication.
The common initial value preserves \(X_0=e\). The based-pair subgroup
has \(g=e\); it will give the same finite cylinder response.
Write
\[
u_k=\dot k k^{-1},\quad v_k=k^{-1}\dot k,
\qquad u_l=\dot l l^{-1},\quad v_l=l^{-1}\dot l .
\]

For the right stochastic logarithm
\(\beta^R(X)=2^{-1/2}\int\circ dX\,X^{-1}\), the transformed path
\(Y=\mathcal T_{k,l}X\) obeys
\[
d\beta^R(Y)=\operatorname{Ad}_k d\beta^R(X)
+\frac{u_k-\operatorname{Ad}_Y u_l}{\sqrt2}\,ds.
\tag{JF3}
\]
The rotated noise is Brownian. For a reference path \(\gamma\), put
\(a_s(\gamma)=(u_k-\operatorname{Ad}_{\gamma_s}u_l)/\sqrt2\).
Girsanov gives
\[
\frac{d\mu_{k,l}}{d\mu_T}(\gamma)
=\exp\left\{\int_0^T Q(a_s(\gamma),d\beta^R_s(\gamma))
-\frac12\int_0^T|a_s(\gamma)|^2ds\right\},
\qquad \mu_{k,l}=(\mathcal T_{k,l})_*\mu_T .
\tag{JF4}
\]
The integral in this exponential is **Itô**; the stochastic logarithm
itself was defined by a Stratonovich integral. The deterministic bound
\(\int|a_s|^2ds\le\frac12\int(|u_k|+|u_l|)^2ds<\infty\)
ensures Novikov's condition and finite entropy. Uniqueness of the
drifted group SDE identifies this density with the actual pushed law.
This uses [[library/analysis-on-wiener-space-and-applications/inq|the
Girsanov and group-path translation results]] also used in
[[path-shift-fisher-geometry-before-gauge-projection|the one-sided
construction]], with the side and normalization computed in (JF3).

Under the pushed law,
\(\mathbb E\operatorname{Ad}_{Y_s}
=\operatorname{Ad}_{k_s}r(s)\operatorname{Ad}_{l_s}^{-1}\).
Taking the expectation of the logarithm in (JF4) therefore yields
\[
\boxed{
D(\mu_{k,l}\Vert\mu_T)
=\frac14\int_0^T
\bigl(|v_k|^2+|v_l|^2-2r(s)Q(v_k,v_l)\bigr)ds .}
\tag{JF5}
\]
Natural logarithms fix the information normalization. The exact cost is
quadratic in **body velocities**, not in arbitrary coordinates on the
group of paths. With one row zero it reduces to the one-sided quarter
energy. Reverse relative entropy need not have the same cross term.
The action is invertible: positive (JF5) is reference-state
distinguishability, not information destroyed by the action.

For \(s>0\), \(0<r(s)<1\). Thus (JF5) vanishes exactly when both
velocities vanish. Within (JF2), the state stabilizer consists of constant
diagonal conjugations \(k=l=g\), modulo the central kernel of the action.
This identifies a stabilizer of the **given** state and action, not a
gauge group derived from no inputs.

## Dualization must respect the score radical

For infinitesimal pairs \(h,j\) with \(h(0)=j(0)=\xi\), the score and
its squared Fisher norm are
\[
Z_{h,j}=\frac1{\sqrt2}\int_0^T Q(\dot h,d\beta^R)
-\frac1{\sqrt2}\int_0^T Q(\dot j,dB),
\qquad
g_2(h,j)=\frac12\int_0^T
\bigl(|\dot h|^2+|\dot j|^2-2r\,Q(\dot h,\dot j)\bigr)ds .
\tag{JF6}
\]
Here \(d\beta^R=\operatorname{Ad}_X dB\); its expected cross covariance
is \(r(s)I\). Formula (JF6) is the second derivative of (JF5), not
its quadratic Taylor coefficient.

Use real smooth finite cylinders
\(F=f(X_{t_1},\ldots,X_{t_m})\), at distinct positive times. Discard
any deterministic time-zero argument. Fix
\[
L_af(x)=\left.\partial_v f(e^{vT_a}x)\right|_0,\quad
R_af(x)=\left.\partial_v f(xe^{vT_a})\right|_0,\quad
p_L(s)=\sum_{i:s\le t_i}\nabla_{L,i}f,\quad
p_R(s)=\sum_{i:s\le t_i}\nabla_{R,i}f .
\]
The pointwise action derivative is
\[
V_{h,j}F
=Q\!\left(\sum_i(\nabla_{L,i}-\nabla_{R,i})f,\xi\right)
+\int_0^T\bigl(Q(p_L,\dot h)-Q(p_R,\dot j)\bigr)ds .
\tag{JF7}
\]
The minus sign belongs to the inverse right action.

Constant pairs \((\xi,\xi)\) are a genuine score radical. Avoid
undefined quotients with denominator zero by declaring the extended norm
\[
\Gamma_2(F)(X)
=\inf\{C\ge0:\ |V_{h,j}F(X)|^2\le Cg_2(h,j)
\text{ for every admissible pair}\},
\qquad \inf\varnothing=\infty .
\tag{JF8}
\]
This is the [[measured-response-carriers/inq#Fisher-invisible actions and finite observable response|stabilizer-annihilation rule]]
for a specified observable cotangent, not inversion of a projected
zero metric. The pointwise derivative in (JF7) is not the derivative of
the expectation of \(F\).

For based pairs, the velocity Fisher block is
\(\frac12\left(\begin{smallmatrix}I&-rI\\-rI&I\end{smallmatrix}\right)\);
the covector is \((p_L,-p_R)\). Inverting this block gives
\[
\boxed{
\Gamma_2(F)
=\int_0^T\left\{
\frac{|p_L-p_R|^2}{1-r(s)}
+\frac{|p_L+p_R|^2}{1+r(s)}
\right\}ds .}
\tag{JF9}
\]
The right side may be infinite. Truncate an inverse-metric maximizing
control to \(s\ge\varepsilon>0\), and then decrease \(\varepsilon\),
to justify the extended supremum without a bounded inverse at zero.
For the full family (JF2), (JF9) also applies whenever (JF7) annihilates
the initial-value radical. If it does not, both expressions are infinite.
Complex forms below mean sesquilinear extension from the real form,
not a new supremum over complex-valued variations.

## Finite cylinder response determines the neutral carrier

Before \(t_1\),
\[
p_L-p_R=\sum_i(\nabla_{L,i}-\nabla_{R,i})f,\qquad
1-r(s)=c_As+O(s^2).
\]
The first term of (JF9) therefore diverges logarithmically unless the
displayed conjugation derivative vanishes. If it vanishes, the remaining
early term is bounded, and both weights are bounded after \(t_1\).
The finite heat-increment law has strictly positive density on \(G^m\).
Continuity then upgrades almost-everywhere vanishing to everywhere.
Since \(G\) is connected,
\[
\boxed{
\mathbb E_{\mu_T}\Gamma_2(F)<\infty
\quad\Longleftrightarrow\quad
f(gx_1g^{-1},\ldots,gx_mg^{-1})=f(x_1,\ldots,x_m)
\quad\text{for all }g .}
\tag{JF10}
\]
This is a theorem about **smooth finite cylinders**. Their finite-response
algebra has \(L^2\) completion
\(\mathcal H_{T,\mathrm{inv}}=L^2(\mu_T)^{\operatorname{Ad}G}\).
It is not dense in the nonneutral full carrier. Nor does (JF10) say that
every invariant \(L^2\) vector has finite response.

The based subgroup recovers the same constraint without an exact constant
radical. Choose \(g=e^\xi\), \(0<\varepsilon<\delta<t_1\), and the
logarithmic ramp
\[
b_{\varepsilon,\delta}(s)=
\begin{cases}
0,&s\le\varepsilon,\\
\log(s/\varepsilon)/\log(\delta/\varepsilon),&\varepsilon<s<\delta,\\
1,&s\ge\delta .
\end{cases}
\]
For \(k=l=e^{b_{\varepsilon,\delta}\xi}\), put
\(L=\log(\delta/\varepsilon)\). Its exact entropy satisfies
\[
D(\mu_{k,k}\Vert\mu_T)
=\frac{|\xi|^2}{2L^2}
\int_\varepsilon^\delta\frac{1-e^{-c_As}}{s^2}\,ds
\le\frac{c_A|\xi|^2}{2L}\longrightarrow0 .
\tag{JF11}
\]
Every readout after \(\delta\) undergoes exact conjugation by \(g\).
Each ramp has finite ordinary control energy
\(|\xi|^2(\varepsilon^{-1}-\delta^{-1})/L^2\), although these energies
diverge along the sequence. Cheapness is specific to the joint entropy
geometry. It is not cheapness in the ordinary Cameron--Martin norm or
an infinite physical energy of a colored excitation.

Neutrality was not separately imposed on cylinder readouts, but the group
and its state symmetry were present in the declared action. The mechanism
does not derive confinement. Enlarging the transformation family could
enlarge its score radical and discard still more observables; (JF2)
must not be read as all automorphisms of the probability space.

## A closed operator on that carrier

Let \(\mathcal K_T=L^2(\mu_T\times[0,T];\mathfrak g)\).
The one-sided constructions give closed gradients
\(\mathsf G_L,\mathsf G_R:L^2(\mu_T)\supset\operatorname{Dom}\mathsf G_{L,R}
\to\mathcal K_T\), represented on cylinders by \(p_L,p_R\).
Their forms are \(2\|\mathsf G_LF\|^2\) and
\(2\|\mathsf G_RF\|^2\). Their closed realizations follow from
[[library/ito-maps-and-analysis-on-path-spaces/inq|Elworthy--Li's
injective-noise path-space theorem]], as applied in (SD4)--(SD9);
path inversion exchanges the two constructions.

On the intersection of these domains in \(\mathcal H_{T,\mathrm{inv}}\),
put \(\mathsf G=(\mathsf G_L,\mathsf G_R)\) and define the multiplication
operator
\[
\mathsf B(s)=\frac{2}{1-r(s)^2}
\begin{pmatrix}I&-r(s)I\\-r(s)I&I\end{pmatrix},
\qquad
\mathsf A_{\max}=\mathsf B^{1/2}\mathsf G ,
\tag{JF12}
\]
with domain requiring \(\mathsf B^{1/2}\mathsf GF\in
\mathcal K_T\oplus\mathcal K_T\). Its eigenvalues are
\(2/(1+r)\) and \(2/(1-r)\), so \(\mathsf B\ge I\).
This proves closedness: if \(F_n\to F\) and
\(\mathsf A_{\max}F_n\to y\), then
\(\mathsf GF_n\to\mathsf B^{-1/2}y\). Closedness of \(\mathsf G\)
and of multiplication by \(\mathsf B^{1/2}\) identifies
\(F\in\operatorname{Dom}\mathsf A_{\max}\) and
\(\mathsf A_{\max}F=y\).

Invariant smooth cylinders are dense in \(\mathcal H_{T,\mathrm{inv}}\)
and belong to this domain by (JF10). Hence their response preform is
closable. Define \(\mathsf A_T\) as the graph closure of
\(\mathsf A_{\max}\) restricted to these cylinders, and set
\[
\mathcal E_T(F,G)=\langle\mathsf A_TF,\mathsf A_TG\rangle,\qquad
H_T=\mathsf A_T^*\mathsf A_T,\qquad
P_\tau^T=e^{-\tau H_T}\quad(\tau\ge0).
\tag{JF13}
\]
The generator acts on \(\mathcal H_{T,\mathrm{inv}}\), with
\(\operatorname{Dom}H_T=\{F\in\operatorname{Dom}\mathsf A_T:
\mathsf A_TF\in\operatorname{Dom}\mathsf A_T^*\}\).
The gradient chain rule gives contraction under smooth normal
contractions; approximation and closure give a Dirichlet form.
Thus (JF13) is an all-duration, strongly continuous self-adjoint Markov
semigroup, and \(H_T\mathbf1=0\).

This construction uses its **own cylinder closure**. Equality with the
maximal weighted domain is not assumed or proved. The inclusion
\(\mathsf A_T\subseteq\mathsf A_{\max}\) suffices for every estimate below.
Path inversion preserves the state and exchanges \(p_L,p_R\), so it
preserves this joint form; no handed response is selected.

## The complete threshold is two, but two is not an eigenvalue

The algebraic identities
\[
\begin{aligned}
\Gamma_2(F)-2\int_0^T|p_L|^2ds
&=2\int_0^T\frac{|p_R-rp_L|^2}{1-r^2}\,ds,\\
\Gamma_2(F)-2\int_0^T|p_R|^2ds
&=2\int_0^T\frac{|p_L-rp_R|^2}{1-r^2}\,ds
\end{aligned}
\tag{JF14}
\]
remain valid for the closed gradients on \(\operatorname{Dom}\mathsf A_T\).
Both one-sided invariant forms have lower edge two: their Wiener
realizations have no invariant first chaos, because
\(\mathfrak g^{\operatorname{Ad}G}=0\). Consequently
\[
\mathcal E_T(F)\ge2\|F-\mathbb E F\|_2^2
\quad\text{on the whole closed form domain}.
\tag{JF15}
\]
This is not a lower bound checked only on characters.

To prove sharpness for every \(G\) under (JF1), take the real adjoint
character \(f(g)=\operatorname{Tr}\operatorname{Ad}_g\), with \(d=\dim G\).
Its invariant Hessian and heat equation are
\[
f(e)=d,\quad \nabla f(e)=0,\quad
\operatorname{Hess}f(e)=-c_AQ,\quad \Delta_Q f=-c_A f.
\]
Indeed, the Hessian is
\(\operatorname{Tr}(\operatorname{ad}_X\operatorname{ad}_Y)\);
the invariant trace identity and the Casimir normalization give the
coefficient \(-c_A\). Put \(J_f=|\nabla f|^2\). Bochner's formula at
the critical point gives \(\Delta_QJ_f(e)=2dc_A^2\).
Using \(\Delta_Q f^2=-2c_Af^2+2J_f\) gives
\(\Delta_Q^2 f^2(e)=4c_A^2d^2+4dc_A^2\). Therefore
\[
\operatorname{Var}(f(X_t))=2dc_A^2t^2+O(t^3),\qquad
\mathbb E J_f(X_t)=2dc_A^2t+O(t^2).
\tag{JF16}
\]
These are heat-semigroup Taylor expansions of smooth functions on compact
\(G\); the next power of \(\Delta_Q\) bounds each remainder uniformly.
No informal replacement of the group by a Gaussian tangent is needed.

For this central one-time readout \(p_L=p_R\). Its response is
\[
\mathcal E_T(f(X_t))=b(t)\mathbb E J_f(X_t),\qquad
b(t)=4\int_0^t\frac{ds}{1+e^{-c_As}}
=2t+\frac4{c_A}\log\cosh(c_At/2)=2t+O(t^2).
\tag{JF17}
\]
The centered Rayleigh quotient tends to two as \(t\downarrow0\).
All these trials belong to the actual cylinder core, so (JF15) and
(JF16)--(JF17) prove
\[
\boxed{\ker H_T=\mathbb C\mathbf1,\qquad
\inf\operatorname{spec}(H_T|_{\mathbf1^\perp})=2.}
\tag{JF18}
\]

If a centered nonzero vector attained equality in (JF15), both
one-sided lower bounds and both excess squares in (JF14) would be
equalities. Thus \(p_R=rp_L\) and \(p_L=rp_R\) almost everywhere.
Since \(r(s)<1\) for \(s>0\), both gradients vanish, forcing the vector
to be constant. This is a contradiction. Hence **two is in the spectrum
but is not an eigenvalue**. An isolated vacuum with a positive
non-attained threshold is a genuine gap; no discrete ladder above it
has been proved or needed.

For the explicit \(SU(2)\), \(Q=-2\operatorname{Tr}\) check, use the
fundamental character from the earlier notes:
\[
c_A=2,\quad J(t)=\tfrac34(1-e^{-2t}),\quad
V(t)=1+3e^{-2t}-4e^{-3t/2},\quad b(t)=2t+2\log\cosh t .
\]
Then \(b(t)J(t)/V(t)\) is an actual invariant trial quotient.
At \(t=10^{-5}\) it is \(2.0000133334\), above and approaching
the proved edge, not a numerical determination of that edge.

## Terminal enlargement preserves the complete clock

For \(T_1<T_2\), restriction of paths gives an isometry
\(J:\mathcal H_{T_1,\mathrm{inv}}\to\mathcal H_{T_2,\mathrm{inv}}\).
Let \(C=\mathbb E[\cdot\mid\mathscr F_{T_1}]\), identified with its
shorter-path readout. Independent bi-invariant heat increments imply,
for smooth cylinders \(G\),
\[
p_L(CG)(s)=C p_L(G)(s),\qquad
p_R(CG)(s)=C p_R(G)(s)\quad(s\le T_1).
\tag{JF19}
\]
To verify this, extend each deterministic shift constantly beyond
\(T_1\). Given the past, transformed future increments are conjugated
by the constant right endpoint; their law is unchanged. Differentiate
the finite smooth increment integral, then test arbitrary control
velocities supported before \(T_1\). Both shorter gradients vanish
after \(T_1\).

Because \(\mathsf B(s)\) is deterministic, conditional Jensen gives
form contraction by \(C\), and the mixed identity is
\[
\mathcal E_{T_2}(JF,G)=\mathcal E_{T_1}(F,CG).
\tag{JF20}
\]
These relations extend to the cylinder closures. Thus the embedded
shorter carrier reduces \(H_{T_2}\), and
\(P_\tau^{T_2}J=JP_\tau^{T_1}\) for every duration.
This proves more than agreement of finite diagonal forms.

On \(C_e([0,\infty),G)\), use the compatible Wiener law and close the
union of finite-time invariant cylinders. The same closed-gradient
construction works in \(L^2(\mu_\infty\times[0,\infty);\mathfrak g)^2\),
with \(\mathsf B^{-1/2}\) still bounded. The invariant one-hand Wiener
bound, the small-time trials, and the excess-square proof remain valid.
The infinite-horizon generator therefore also has the unique constant
vacuum and non-attained threshold two. This is an actual auxiliary
path-horizon limit, **not** the four-dimensional infinite-volume limit.

## Heat-time coordinates do not calibrate the threshold

Let \(a\in C^1([0,T])\) be strictly positive and replace (JF1) by
\(dX_s=\sqrt{2a(s)}X_s\circ dB_s\). Put
\(q(s)=\int_0^s a(u)du\) and \(r_a(s)=e^{-c_Aq(s)}\).
Repeating (JF3)--(JF9) gives
\[
\begin{aligned}
D(\mu^a_{k,l}\Vert\mu^a)
&=\frac14\int_0^T
\frac{|v_k|^2+|v_l|^2-2r_a Q(v_k,v_l)}{a(s)}ds,\\
\Gamma_2^a(F)
&=\int_0^T a(s)\left\{
\frac{|p_L-p_R|^2}{1-r_a(s)}
+\frac{|p_L+p_R|^2}{1+r_a(s)}\right\}ds .
\end{aligned}
\tag{JF21}
\]
The Fisher metric has the same reciprocal factor \(a^{-1}\) as the
entropy. Under \(u=q(s)\), the map \(Z\mapsto Z\circ q\) takes unit
heat law on \([0,q(T)]\) to \(\mu^a\), and its pullback is an
equivariant unitary. Substitution in (JF21), including the transformed
control velocities, identifies the forms exactly. It also identifies
their cylinder closures and generators.

Thus the threshold remains two under this change of the state schedule.
This is different from choosing a different **response intensity at a
fixed state**, as in (SD12)--(SD13). It establishes coordinate covariance,
not a physical conversion factor. The response parameter \(\tau\) in
(JF13) still has no identification with observable time or energy.

## Annular restart is a different law, and it fails here

The [[shared-driver-response-and-the-nested-holonomy-clock#A same-clock restart law selects constant intensity|earlier restart test]]
compares equal-duration annular readouts after deleting their past.
Terminal consistency (JF20) does not imply that law.

For \(SU(2)\), let \(z_{s,t}=\chi_{1/2}(X_s^{-1}X_{s+t})\).
Both gradient tails vanish before \(s\). If
\(Z=X_s^{-1}X_{s+t}\) and \(w=\nabla\chi_{1/2}(Z)\), the remaining
tails are \(p_L=\operatorname{Ad}_{X_s}w\), \(p_R=w\).
The increment \(Z\) is independent of \(X_s\), so
\(\mathbb E|p_L|^2=\mathbb E|p_R|^2=J(t)\) and
\(\mathbb E Q(p_L,p_R)=r(s)J(t)\). Consequently
\[
\boxed{
\mathcal E(z_{s,t})
=4J(t)\int_s^{s+t}
\frac{1-r(u)r(s)}{1-r(u)^2}\,du,\qquad r(u)=e^{-2u}.}
\tag{JF22}
\]
At \(s=0\), this is \(b(t)J(t)\). As \(s\to\infty\), it tends to
\(4tJ(t)>b(t)J(t)\) for \(t>0\). The state laws of these annular
characters agree, but their joint responses do not.

The failure is strict for every \(s,t>0\). Write the integral in (JF22)
as \(I_s(t)\), put \(p=e^{-2c_As}\), and substitute \(u=s+v\).
Its integrand is
\((1-pe^{-c_Av})/(1-pe^{-2c_Av})\); its derivative in \(p\) is
\(-e^{-c_Av}(1-e^{-c_Av})/(1-pe^{-2c_Av})^2<0\) for \(v>0\).
Thus \(I_0(t)<I_s(t)<t\). Even a restart-dependent constant clock
multiplier cannot identify all durations. For fixed \(s>0\),
\[
I_s(t)=t-\frac{c_Ap}{2(1-p)}t^2+O(t^3),\qquad
I_0(t)=\frac t2+\frac{c_A}{8}t^2+O(t^4),
\]
so
\[
\frac{\mathcal E(z_{s,t})}{\mathcal E(z_{0,t})}
=\frac{I_s(t)}{I_0(t)}
=2-\frac{c_A(1+p)}{2(1-p)}t+O(t^2).
\tag{JF23}
\]
The discrepancy changes shape with the annular duration, not merely its
unit. The \(t\downarrow0\) expansion here holds at fixed \(s>0\);
it is not uniform as \(s\downarrow0\).

The cost remembers the original root through the cross-score covariance
\(\mathbb E\operatorname{Ad}_{X_s}\). This precisely locates the
remaining choice: the two-sided Fisher prescription removes handedness
and determines a neutral carrier, but it does not preserve the
one-sided construction's same-clock annular homogeneity. If that
additional response law is required, this candidate fails it. Calling
the whole-to-local relation covariant cannot replace checking which
restriction and restart maps it actually intertwines.

The [[receipts/two_sided_fisher_receipt.py|joint Fisher receipt]] checks
the Pauli-derived cross-score block, its dual and domination identities,
high-precision character quotients, weighted ramp integrals, and raw
versus invariant cylinder responses. It also checks actual quaternion
annular gradients and compares the resulting response integrals with
their analytic antiderivatives. At \(t=0.4\), the responses at
\(s=0,0.2,1,5\) are approximately \(0.39479,0.59082,0.65849,0.66081\).
Its
[[receipts/two-sided-fisher-receipt-output.txt|recorded values]] are
finite diagnostics, not the infinite-dimensional proofs above.

## Conditional restart changes both operator and carrier

One can recover the root response after a cut by retaining its boundary
state during Fisher dualization. This is a different, boundary-resolved
prescription. It restores annular restart on its own carrier but excludes
legitimate jointly neutral observables of the original construction.

Fix a cut \(s>0\), future length \(\ell>0\), and write
\[
\eta=X|_{[0,s]},\qquad b=X_s,\qquad
Z_v=b^{-1}X_{s+v},\quad 0\le v\le\ell.
\tag{JF24}
\]
Independent heat increments identify the whole state with
\(\mu_s(d\eta)\mu_\ell(dZ)\). Freeze the prefix and apply
\(X_{s+v}\mapsto k_vX_{s+v}l_v^{-1}\), where \(k_0=l_0=e\) and
the deterministic controls have finite logarithmic energy. The cut value
is unchanged. Conditional on the prefix,
\(\mathbb E[\operatorname{Ad}_{X_{s+v}}\mid\eta]
=r(v)\operatorname{Ad}_b\), rather than \(r(s+v)I\).

The conditional right-logarithm drift is still
\((u_k-\operatorname{Ad}_Y u_l)/\sqrt2\). The same deterministic
energy bound as in (JF4) gives conditional Girsanov, and taking its
logarithm under the pushed conditional law gives
\[
D(\mu_{s,b}^{k,l}\Vert\mu_{s,b})
=\frac14\int_0^\ell
\left(|v_k|^2+|v_l|^2
-2r(v)Q(v_k,\operatorname{Ad}_b v_l)\right)dv .
\tag{JF25}
\]
Here \(\mu_{s,b}\) is the conditional future law starting at \(b\).
The infinitesimal velocity Fisher block is therefore
\[
I_b(v)=\frac12
\begin{pmatrix}
I&-r(v)\operatorname{Ad}_b\\
-r(v)\operatorname{Ad}_b^{-1}&I
\end{pmatrix}.
\tag{JF26}
\]
Rotating the left source frame by \(\widehat h=\operatorname{Ad}_b^{-1}h\)
turns (JF26) into the root block in (JF6). For a smooth cylinder, let
\(p_L,p_R\) be its future gradient tails, with prefix arguments held
fixed, and put \(\bar p_L=\operatorname{Ad}_b^{-1}p_L\). Conditional
dualization before averaging over the prefix gives
\[
\Gamma_s^{\rm cond}(F)
=\int_0^\ell
\left\{
\frac{|\bar p_L-p_R|^2}{1-r(v)}
+\frac{|\bar p_L+p_R|^2}{1+r(v)}
\right\}dv .
\tag{JF27}
\]
For \(F=f(Z)\), these are exactly the root gradients of \(f\).
The source and observable frame changes are both required.

This does not recompute the original unconditional metric. Averaging
(JF25) first uses \(\mathbb E\operatorname{Ad}_b=r(s)I\) and restores
the old cross weight \(r(s+v)\). Boundary-resolved inversion instead
retains the conditional metric. In root coordinates its left controls
are \(k_v^b=b\widehat k_vb^{-1}\), which depend on the retained cut
data. They are admissible conditional controls, not the original single
Hilbert space of unconditional deterministic controls. The order of
conditional resolution and scalarization is the distinction owned by
[[program-core/center-valued-response|center-valued response]].

By (JF10), finite smooth-cylinder response requires conjugation
invariance of the future \(Z\) coordinates **with the prefix fixed**.
Consequently the natural closed carrier and operator are
\[
\begin{aligned}
\mathcal H_s^{\rm cond}
&=L^2(\mu_s)\widehat\otimes\mathcal H_{\ell,\mathrm{inv}},\\
\mathcal E_s^{\rm cond}(F)
&=\int\mathcal E_\ell(F(\eta,\cdot))\,d\mu_s(\eta),\\
H_s^{\rm cond}&=I\otimes H_\ell,\qquad
\ker H_s^{\rm cond}=L^2(\mu_s)\otimes\mathbb C\mathbf1.
\end{aligned}
\tag{JF28}
\]
The form domain consists of square-integrable sections whose fibers
belong to \(\operatorname{Dom}\mathcal E_\ell\) almost everywhere and
whose displayed energies are integrable. This direct-integral closure
uses the actual root cylinder closure, not its unproved maximal-domain
identification. It is not a densely defined form on the unrestricted
whole path carrier. All prefix observables remain in its kernel; the
threshold two is above that entire kernel, not above a single vacuum.

The future-only embedding \(J_sf=f(Z)\) now obeys exactly
\[
e^{-\tau H_s^{\rm cond}}J_s=J_se^{-\tau H_\ell}
\quad(\tau\ge0).
\tag{JF29}
\]
In particular, the conditional response of
\(\chi_{1/2}(X_s^{-1}X_{s+t})\) is \(b(t)J(t)\), independent of
\(s\). This is genuine same-clock annular restart for invariant future
observables, on the smaller carrier just specified.

### A jointly neutral endpoint is excluded

For \(SU(2)\), write
\(b=b_0I+i\mathbf b\cdot\boldsymbol\sigma\) and
\(Z_t=z_0I+i\mathbf z\cdot\boldsymbol\sigma\). The original globally
invariant cylinder is
\(F=\chi_{1/2}(X_{s+t})=\operatorname{Tr}(bZ_t)\).
With \(T_a=-i\sigma_a/2\), its future conjugation derivative satisfies
\[
\left|\nabla_L\operatorname{Tr}(bZ_t)
-\nabla_R\operatorname{Tr}(bZ_t)\right|^2
=4|\mathbf b\times\mathbf z|^2.
\tag{JF30}
\]
Thus (JF27) contains
\(4|\mathbf b\times\mathbf z|^2\int_0^t(1-e^{-2v})^{-1}dv\),
which is infinite when the cross product is nonzero. For \(s,t>0\),
the strictly positive heat densities make \(b\) noncentral and that
cross product nonzero almost surely. This endpoint had finite response
in the original root construction. Its future-only neutral projection is
\[
\int_G\operatorname{Tr}(b gZ_tg^{-1})\,dg
=\tfrac12\operatorname{Tr}(b)\operatorname{Tr}(Z_t),
\tag{JF31}
\]
which deletes the jointly invariant term
\(-2\mathbf b\cdot\mathbf z\).

The loss is exactly the danger isolated by
[[inq#The whole is assembled from dual boundary charges|charged boundary gluing]]:
diagonal invariance of the whole does not mean separate invariance of
its two factors. Restricting (JF28) further to globally invariant vectors
gives \(\mathcal H_{s,\mathrm{inv}}\widehat\otimes
\mathcal H_{\ell,\mathrm{inv}}\), still missing the nontrivial dual
charges that can combine to a singlet.

There is a sharper obstruction on the smooth cylinder core. On a fixed
grid, relative-future conjugation at every cut, including the root, is
equivalent to independent conjugation of each increment. If a cylinder
must retain this property after splitting one of its increments as
\(y=ab\), invariance under conjugation of \(a\) alone gives
\(L_{\xi-\operatorname{Ad}_a\xi}f(y)=0\) for every \(a,\xi,y\),
with other increments fixed. These directions span \(\mathfrak g\)
for the connected semisimple groups considered here. Hence that cylinder
is constant in the split increment. Requiring the property under splits
of every coarse interval leaves only constant smooth cylinders. This is
a statement about one cylinder across all refinements, not a theorem
identifying an intersection of arbitrary closed \(L^2\) domains.

Conditional restart therefore repairs neither the original operator nor
its full neutral carrier. A candidate that retains all cuts must keep
boundary-covariant charged fibers until gluing, and then construct a
compatible response on the complete diagonal-invariant carrier. Separate
fiber neutralization cannot supply that construction.

### Charged values alone do not repair the source geometry

Keep the conditional heat law, the Fisher norm (JF6), the frozen-prefix
future action, and the usual scalar action fixed. Let \(W\) carry a
finite-dimensional unitary representation \(\rho\), and let a smooth
\(W\)-valued cylinder satisfy
\[
F(gZg^{-1})=\rho(g)F(Z).
\]
A correction at the literal initial-value radical would be
\[
\nabla^0_{h,j}F=V_{h,j}F-\rho_*(\xi_0)F,\qquad
\xi_0=h(0)=j(0).
\tag{JF32}
\]
This cancels constant diagonal controls, but not their cheap based
approximations. Fix \(0<a<t_1\), where \(t_1\) is the first future
readout, and take \(h=j=b_{\varepsilon,a}\zeta\) using (JF11). Then
\[
\xi_0=0,\qquad
\nabla^0_{h,j}F=\rho_*(\zeta)F,\qquad
g_2(h,j)\le\frac{c_A|\zeta|^2}{\log(a/\varepsilon)}
\longrightarrow0.
\tag{JF33}
\]
Every readout is conjugated by the same infinitesimal \(\zeta\).
Consequently a finite extended response norm for (JF32) forces
\(\rho_*(\zeta)F=0\) for every \(\zeta\). Since \(G\) is connected,
the values lie in \(W^G\); for a nontrivial irreducible representation
the cylinder vanishes. Initial-value covariance alone therefore retains
no charged sector.

More generally, a proposed linear connection or source correction
\(\nabla_{h,j}F=V_{h,j}F-\mathcal A_Z(h,j)F\) must satisfy
\[
\bigl[\rho_*(\zeta)-
\mathcal A_Z(b_{\varepsilon,a}\zeta,b_{\varepsilon,a}\zeta)\bigr]F(Z)
\longrightarrow0
\tag{JF34}
\]
whenever its extended response is finite. A correction whose action on
\(F\) is itself bounded in the original Fisher norm tends to zero on
these ramps and cannot meet this condition for a charged value. A
connection must account for the vertical action along the completed
cheap directions before dualization, or an enlarged source must change
their cost. Formula (JF34) is a necessary condition, not a prescription
chosen after seeing the desired readout.

There is also a scalar obstruction to repairing the construction by
charged notation alone. Suppose the connection respects the pairing
between dual boundary representations and reduces to the original
derivative on scalars:
\[
\nabla\langle F_A,F_B\rangle
=\langle\nabla F_A,F_B\rangle+\langle F_A,\nabla F_B\rangle
=V\langle F_A,F_B\rangle.
\tag{JF35}
\]
Connection terms cancel in this identity. In the \(SU(2)\) example,
the prefix vector \(\mathbf b\) and future vector \(\mathbf z\) are
adjoint charges whose pairing is \(\mathbf b\cdot\mathbf z\). A
future-only cheap diagonal ramp has
\[
V\mathbf b=0,\qquad
V\mathbf z=\boldsymbol\zeta\times\mathbf z,\qquad
V(\mathbf b\cdot\mathbf z)
=\mathbf b\cdot(\boldsymbol\zeta\times\mathbf z).
\]
The last expression is generically nonzero and independent of the ramp
cost. By (JF35), a pairing-compatible connection cannot remove its
infinite scalar response. This re-establishes the endpoint obstruction
on the complete paired readout, even if charged factors have been
introduced.

The adjoint representation is important for this witness. An
\(SU(2)\)-fundamental-valued function equivariant under conjugation of
\(Z\) alone already vanishes: the center acts trivially on the base but
nontrivially on its values. Open fundamental boundary indices require
their actual left/right boundary action, not this conjugation action
with a different label.

A remedy must therefore change an upstream datum: specify an additional
boundary source and its joint transformation law, construct a response
metric that controls relative boundary rotations, or replace the
localized action and return map while proving the required scalar
gluing. Merely attaching charged fibers or subtracting the initial
gauge parameter does none of these. The obstruction holds with the
listed source, action, norm and pairing fixed; it does not exclude a
different boundary-resolved construction.

The extended [[receipts/two_sided_fisher_receipt.py|receipt]] checks the
conditional block and both frame rotations using actual \(SU(2)\)
adjoints. A Pauli-matrix endpoint witness is jointly invariant but has
nonzero future conjugation derivative; the finite cutoffs display its
logarithmically increasing cost. The analytic proof, not those cutoffs,
establishes the domain exclusion and the smooth-cylinder refinement
obstruction. [[trace-dirichlet-descent/conditional-score-shorting-and-observable-lifts|The finite conditional-score model]]
separately explains why central resolution and Fisher inversion change
the operator, without claiming to solve this charged gluing problem.

The original construction is a state-action-response triple with a constrained
observable carrier and a complete auxiliary clock. Neither a Yang--Mills
vacuum state on all four-dimensional observables nor its physical
Hamiltonian has been constructed. The group, heat law, admissible
transformations, and dual-response prescription remain inputs; their
justification and the exact Clay return conditions remain open.

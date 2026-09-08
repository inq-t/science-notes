# Interacting References Require Spectral Product Control

An interacting block can replace the Haar reference exactly, and a controlled reference drift gives a new sufficient connected-preparation estimate. But a block spectral gap does not replace the multiplication rules that made the original Fourier estimate work. A positive ground-state transform preserves the kinetic product rule while changing its eigenfunctions and their product channels. An explicit gapped compact diffusion violates the former spectral triangle inequality at arbitrarily small deformation. Beyond the drift bound, assembly requires additional product control on the boundary-charged carrier.

**Status: exact finite-carrier change of reference, a sufficient
uniform derivative theorem under reference-drift smallness, and
an analytic counterexample to extending it from a gap alone.**
An unrestricted interacting-block estimate remains open. No new Yang--Mills
Hamiltonian, continuum limit or physical clock is selected.

## Change the state and operator together

Partition the raw links into disjoint finite blocks \(E_b\).
Keep their full compact configuration carriers
\(X_b=G^{E_b}\), including boundary transformation data.
Here \(G\) is a fixed compact connected nontrivial Lie group,
its bi-invariant metric is specified, and every \(\kappa_e>0\).
Supply smooth real potentials \(V_b\), kinetic operators
\(K_b=-\sum_{e\in E_b}\kappa_e\Delta_e\), and
\[
H_b=K_b+V_b,\qquad
H_b\psi_b=E_b^0\psi_b,\qquad
\psi_b>0,\quad \|\psi_b\|_2=1.
\tag{IR1}
\]
Here \(E_b\) denotes a link set, while \(E_b^0\) is an energy.
Compact ellipticity supplies the positive simple ground vector.
It does not give a numerical gap uniform in increasing block size.

On a finite collection of blocks put
\[
\begin{aligned}
H_{\rm ref}&=\sum_bH_b,&
\psi_{\rm ref}&=\prod_b\psi_b,&
E_{\rm ref}&=\sum_bE_b^0,\\
d\nu_{\rm ref}&=\psi_{\rm ref}^2\,dU,&
w_{\rm ref}&=\log\psi_{\rm ref},&
L_{\rm ref}&=\psi_{\rm ref}^{-1}
 (H_{\rm ref}-E_{\rm ref})\psi_{\rm ref}\\
&&&&&=K-2\Gamma_K(w_{\rm ref},\,\cdot\,).
\end{aligned}
\tag{IR2}
\]
The positive generator \(L_{\rm ref}\) is self-adjoint in
\(L^2(\nu_{\rm ref})\), not Haar \(L^2\). Its initial domain
is the smooth core, with the compact elliptic \(H^2\) closure
and the inherited weighted \(H^1\) form domain.
The product reference law, its adjoint and its drift change
together. Its carré du champ remains
\(\Gamma_K(f,g)=\sum_e\kappa_e\langle\nabla_ef,\nabla_eg\rangle\).
This is the same change of reference used in
[[algebra/partial-bochner-and-ground-state-score#A product reference turns the force into a boundary force|the relative-score equation]].

Let \(M_B=\sum_{p\in B}\lambda_pq_p\) collect the added
interactions and \(H_B=H_{\rm ref}-M_B\). Define
\[
P_B(t)=e^{-t(L_{\rm ref}-M_B)}1
=\psi_{\rm ref}^{-1}e^{-t(H_B-E_{\rm ref})}\psi_{\rm ref},
\qquad v_B=\log P_B.
\tag{IR3}
\]
Thus the physical initial vector is \(\psi_{\rm ref}\).
This is not the original Haar preparation \(e^{-tH_B}1\):
transforming that vector would give initial ratio
\(\psi_{\rm ref}^{-1}\), rather than one. On each fixed
finite system both positive preparations approach the same
ground direction, but their finite-time trajectories differ.

The relative logarithm obeys
\[
\partial_tv_B=-L_{\rm ref}v_B+\Gamma_K(v_B,v_B)+M_B,
\qquad v_B(0)=0.
\tag{IR4}
\]
The finite Möbius transform
\(U_C=\sum_{B\subseteq C}(-1)^{|C|-|B|}v_B\)
therefore satisfies
\[
\partial_tU_C=-L_{\rm ref}U_C+
\mathbf1_{C=\{p\}}\lambda_pq_p+
\sum_{A\cup D=C}\Gamma_K(U_A,U_D).
\tag{IR5}
\]
The proof is exactly the finite coefficient cancellation in
[[connected-preparation-and-local-normalization|connected preparation]],
not an assumed cluster expansion. Independence is now across
**reference blocks**. Each interaction's support must include
every block it touches, since reference evolution can propagate
inside that block. Disjoint raw-link supports within one
interacting block do not imply independent evolution.

The reference projection
\(Q_{\rm ref}f=f-\nu_{\rm ref}(f)\) commutes with
\(L_{\rm ref}\). The corresponding mild quadratic term uses
\(e^{-(t-s)L_{\rm ref}}Q_{\rm ref}\), not a Haar-centered
inverse silently read as an interacting inverse.

## The inherited estimate extends under a drift condition

There is a domain-safe way to continue using the original Haar
Fourier norm without pretending that \(L_{\rm ref}\) is diagonal
there. Adjoin one label \(b\) for every reference block, with
support the entire \(E_b\). For a set \(C\) of crossing labels use
\[
\widetilde C=C\cup\{b:E_b\cap E(C)\ne\varnothing\}.
\tag{IR14}
\]
Use the induced overlap-graph diameter of these enriched labels
in the weight \(w_\mu\). Saturation respects unions,
\(\widetilde C\cup\widetilde D=\widetilde{C\cup D}\).
If \(\Gamma_K(\log\psi_b,U_C)\ne0\), then \(b\in\widetilde C\);
the drift does not expand this saturated support.
An isolated crossing interaction and its touched block labels
form a star of diameter at most two. Its source norm can therefore
pay up to \(e^{2\mu}\), rather than the original singleton weight one.

Place \(Q_H\log\psi_b\) on the singleton block label \(b\),
where \(Q_H\) removes the Haar constant. Denote this fixed
family by \(W_0\), put \(n_0=\mathcal N_\mu(W_0)\), and
use the static Fourier norm for it, equivalently its constant
time extension. Zero initial values are imposed on the unknown
relative coefficients, not on \(W_0\).

Let \(s_\times\) bound the Haar heat-integrated crossing source
in the saturated-label norm, and let \(C_\mu\) be the coefficient
in (KF13). Writing (IR5) with \(K\), rather than \(L_{\rm ref}\),
gives on functions modulo scalar coefficients
\[
U=S_\times+2\mathcal B(W_0,U)+\mathcal B(U,U).
\tag{IR15}
\]
Here \(\mathcal B\) is the original Haar heat convolution,
with its actual representation channels. The enriched labels
make the previous bilinear proof applicable without losing
internal block propagation. Set \(\beta=2C_\mu n_0\). If
\[
\boxed{\beta<1,\qquad
4C_\mu s_\times<(1-\beta)^2,}
\tag{IR16}
\]
then \(I-2\mathcal B(W_0,\cdot)\) has a Neumann inverse of norm
at most \((1-\beta)^{-1}\). After applying it, the nonlinear
map preserves the ball of radius \(2s_\times/(1-\beta)\)
and contracts with constant at most
\(4C_\mu s_\times/(1-\beta)^2\). Thus
\[
\boxed{\mathcal N_\mu(U)\le\frac{2s_\times}{1-\beta}.}
\tag{IR17}
\]
This is uniform in time and number of blocks when the declared
source and drift norms are. At zero crossing source the relative
solution is identically zero.

As in the original construction, restore the omitted scalar
coefficients by integrating their actual equations. On every
finite graph the norm gives convergent second derivatives;
exponentiation and uniqueness of the linear heat equation
identify the resulting solution with (IR3). The small norm of
an unknown exact preparation has not been assumed.
The derivative bounds (KF7) apply with the radius in (IR17).
The reference ground data, including the required Fourier norm
of their logarithms, are still inputs to this extension.

The static identity clarifies the centering. On smooth functions
modulo constants put
\[
G=K^{-1}Q_H,\qquad D=2G\Gamma_K(w_{\rm ref},\cdot).
\]
Then
\[
\boxed{[L_{\rm ref}]^{-1}=(I-D)^{-1}G.}
\tag{IR18}
\]
Indeed \(Q_H L_{\rm ref}h=Q_Hg\) is equivalent to
\(h-Dh=Gg\) for the Haar-centered representative. Integrating
\(L_{\rm ref}h-g=\text{constant}\) against \(\nu_{\rm ref}\)
identifies that constant as \(-\nu_{\rm ref}(g)\).
Thus the result is the Haar-centering of
\(L_{\rm ref}^{-1}Q_{\rm ref}g\), not an assertion that
Haar and ground-state means agree.
The formula is used where the inverse exists; (IR16) supplies
its bounded Neumann realization in this norm.

This replaces bare internal-potential smallness by reference-drift
smallness in the same comparison geometry. It is a genuine
conditional extension, but no wider Wilson coupling regime has
yet been certified from it.

## What survives in an interacting eigenbasis

For one full block choose real orthonormal eigenfunctions
\[
L_b\phi_\alpha=\epsilon_\alpha\phi_\alpha,\qquad
\phi_0=1,\quad \epsilon_0=0,
\qquad
c_{\alpha\beta}^{\gamma}
=\int\phi_\alpha\phi_\beta\phi_\gamma\,d\nu_b.
\]
For smooth eigenfunctions, self-adjointness and the product rule
give the exact channel identity
\[
\boxed{
\langle\Gamma_K(\phi_\alpha,\phi_\beta),\phi_\gamma\rangle_{\nu_b}
=\frac{\epsilon_\alpha+\epsilon_\beta-\epsilon_\gamma}{2}
c_{\alpha\beta}^{\gamma}.}
\tag{IR6}
\]
On a product of blocks the energies add and product coefficients
factor. These identities do survive the change of reference.

What does not follow is the Haar representation rule
\[
c_{\alpha\beta}^{\gamma}\ne0
\ \Longrightarrow\
\sqrt{\epsilon_\gamma}\le
\sqrt{\epsilon_\alpha}+\sqrt{\epsilon_\beta},
\tag{IR7}
\]
or the corresponding cross-Casimir coefficient bound.
[[kinetic-smoothing-and-connected-fourier-control|The kinetic Fourier proof]]
uses actual representation fusion and trace contraction to
obtain those estimates. General interacting eigenfunctions
are not representations. A lower bound on
\(\epsilon_\gamma\) alone supplies neither their product
coefficients nor their differentiated summability.

## A positive gap does not preserve spectral fusion

Use normalized Haar measure \(d\theta/(2\pi)\) on the unit
circle and set
\[
\begin{aligned}
w_\varepsilon&=\varepsilon\cos\theta,&
d\nu_\varepsilon&=Z_\varepsilon^{-1}
 e^{2\varepsilon\cos\theta}\frac{d\theta}{2\pi},\\
L_\varepsilon&=-\partial_\theta^2+
 2\varepsilon\sin\theta\,\partial_\theta,&
H_\varepsilon&=-\partial_\theta^2
 +\varepsilon^2\sin^2\theta-\varepsilon\cos\theta.
\end{aligned}
\tag{IR8}
\]
This is an actual ground-state transform:
\(H_\varepsilon e^{w_\varepsilon}=0\), and
\[
H_\varepsilon=(\partial_\theta-w_\varepsilon')^*
             (\partial_\theta-w_\varepsilon').
\]
The positive ground is simple. Multiplication by
\(Z_\varepsilon^{-1/2}e^{w_\varepsilon}\) is the unitary
map from weighted to Haar \(L^2\).

There is an explicit gap throughout any bounded
\(\varepsilon\)-interval. The density ratio has
\(\sup\rho_\varepsilon/\inf\rho_\varepsilon
=e^{4|\varepsilon|}\). Comparing the variational variance
and Dirichlet form with the Haar Poincare inequality gives
\[
\boxed{\operatorname{gap}(L_\varepsilon)
\ge e^{-4|\varepsilon|}.}
\tag{IR9}
\]
Indeed \(\operatorname{Var}_{\nu}F=\inf_a\int|F-a|^2d\nu\);
bound the integral above by \(\sup\rho\) times Haar variance,
then bound Haar gradient energy by \((\inf\rho)^{-1}\) times
weighted gradient energy.

Parity is preserved. At zero, the energy-one odd eigenvector
\(\sin\theta\) and the energy-nine even eigenvector
\(\cos3\theta\) are simple in their parity subspaces.
The bounded potential of \(H_\varepsilon\) is analytic on
the fixed periodic \(H^2\) domain. Resolvent Neumann expansion
around each isolated eigenvalue gives analytic spectral
projections; elliptic regularity gives expansions in every
fixed smooth norm. Choose the weighted eigenfunctions with
their respective leading Haar Fourier coefficients equal to one.
Their first terms are
\[
\begin{aligned}
f_\varepsilon&=\sin\theta-\frac{\varepsilon}{3}\sin2\theta
 +O(\varepsilon^2),&
\epsilon_f&=1+O(\varepsilon^2),\\
g_\varepsilon&=\cos3\theta-\frac{3\varepsilon}{5}\cos2\theta
 -\frac{3\varepsilon}{7}\cos4\theta
 +O(\varepsilon^2),&
\epsilon_g&=9+O(\varepsilon^2).
\end{aligned}
\tag{IR10}
\]
For example \(2\sin\theta\,\partial_\theta\sin\theta
=\sin2\theta\); solving the first-order equation divides
by \(4-1\). For \(\cos3\theta\), that forcing is
\(-3\cos2\theta+3\cos4\theta\), with energy differences
\(4-9\) and \(16-9\). Both first eigenvalue derivatives vanish.

Since \(Z_\varepsilon=1+O(\varepsilon^2)\), direct integration
gives
\[
\begin{aligned}
\langle f_\varepsilon^2,g_\varepsilon\rangle_{\nu_\varepsilon}
&=\varepsilon
\left(\frac16+\frac3{20}-\frac14\right)
 +O(\varepsilon^2)\\
&=\boxed{\frac{\varepsilon}{15}+O(\varepsilon^2)}.
\end{aligned}
\tag{IR11}
\]
The three terms are respectively the correction to \(f^2\),
the correction to \(g\), and the density tilt. Normalizing the
two eigenfunctions in weighted \(L^2\) changes the leading
coefficient to \(2\sqrt2\,\varepsilon/15\), not to zero.
Thus for every sufficiently small nonzero \(\varepsilon\),
the product \(f_\varepsilon^2\) has a nonzero \(g_\varepsilon\)
channel, although
\[
\sqrt{\epsilon_g}>2\sqrt{\epsilon_f}.
\tag{IR12}
\]
Its multiplier in (IR6) tends to \(-7/2\), whose absolute
value exceeds \(\epsilon_f\to1\). Both proposed Haar-channel
substitutions fail despite (IR9).

This is a smooth inverse-designed compact reference, not a
Wilson counterexample. It rejects an inference from a gapped
block alone. It does not prove that every weighted product
estimate fails, nor that an interacting block cannot be used.

The same reference makes the limitation of (IR18) quantitative.
In the mean-zero circle norm
\(\|h\|_{\mathcal F_2}=\sum_{n\ne0}n^2|\widehat h_n|\),
write \(e_n=e^{in\theta}\). Direct differentiation gives
\[
D e_n=-\frac{\varepsilon n}{(n+1)^2}e_{n+1}
      +\frac{\varepsilon n}{(n-1)^2}e_{n-1},
\tag{IR19}
\]
with the term of frequency zero discarded before dividing.
For \(|n|\ge2\) the weighted column ratio is
\(2|\varepsilon|/|n|\); for \(|n|=1\) it is
\(|\varepsilon|\). The induced weighted \(\ell^1\) operator norm
is the supremum of these column ratios, so
\[
\boxed{\|D\|_{\mathcal F_2\to\mathcal F_2}=|\varepsilon|.}
\tag{IR20}
\]
The sufficient test \(\|D\|<1\) therefore stops closing at
\(|\varepsilon|\ge1\), even though (IR9) still guarantees
a positive gap at every fixed finite \(\varepsilon\).
This does not assert divergence of the actual Neumann series
whenever its norm test fails.

The [[receipts/interacting_reference_fusion_receipt.py|focused receipt]]
checks the exact first derivative and independently computes
the interacting eigenfunction overlap at refined cutoffs.
The analytic nonzero derivative, not those cutoffs, proves
the obstruction.

## A block certificate must retain boundary charges

The reference in (IR1) is not a closed physical universe.
[[gauge-boundary-frame-gluing/inq|Charged boundary gluing]]
shows why a globally invariant interaction can have nontrivial
regional charges whose tensor product is invariant. Projecting
each block separately to its trivial boundary representation
can remove the very crossing interaction in (IR3).

In particular,
[[certified-ground-marginal-and-late-preparation|the completed two-plaquette certificate]]
works on the complete simultaneous-conjugation-invariant
relational carrier. Its ground vector is useful: uniqueness
and positivity identify it with the gauge-invariant ground
of the raw operator. But its excited-sector bound does not
certify the entire boundary-charged raw-block resolvent.
The bare raw \(SU(2)\) link has first Casimir \(3/4\), whereas
the closed two-plaquette invariant calculation uses its
different lower edge \(3\). Those constants cannot be exchanged.

This is not a failure of the completed marginal theorem.
It identifies the additional carrier needed for the new
assembly theorem.

In fact a nonsharp full raw-block gap can already be supplied
at every fixed Wilson coupling. Suppose the block is nonempty,
has \(p_b\) elementary four-distinct-link plaquettes, common
\(\kappa>0\), and common \(\lambda\ge0\).
[[algebra/partial-bochner-and-ground-state-score#Compact gauge normalization|The raw-link score bound]]
gives \(\|\nabla_e\log\psi_b\|_\infty\le\lambda n_e/\kappa\).
The \(Q=-2\operatorname{Tr}\) sphere has radius two and diameter
\(2\pi\). Connecting two configurations one link at a time gives
\[
\operatorname{osc}(\log\psi_b)
\le2\pi\sum_e\|\nabla_e\log\psi_b\|_\infty
\le8\pi p_b\lambda/\kappa.
\]
The same density comparison as in (IR9), now against the full
raw electric gap \(3\kappa/4\), therefore proves
\[
\boxed{\operatorname{gap}(L_b)\ge
\frac{3\kappa}{4}\exp[-16\pi p_b\lambda/\kappa].}
\tag{IR21}
\]
It extends from smooth functions to the weighted \(H^1\) form
domain. At \(p_b=0\) it returns the raw Haar gap.
Thus a fixed finite family of such blocks has an explicit
common positive lower bound, including charged directions.
The bound deteriorates with block size and coupling, and gives
no spectral product moments. Existence of a fixed-block gap is
not the remaining assembly theorem.

## Regrouping does not select a clock

For \(a>0\), rescale both the reference Hamiltonians and added
interactions by \(a\). The ground reference and its law stay
fixed, while energies, \(L_{\rm ref}\), and \(\Gamma_K\)
all scale by \(a\). Consequently
\[
(aL_{\rm ref})^{-1}Q_{\rm ref}(a\Gamma_K)
=L_{\rm ref}^{-1}Q_{\rm ref}\Gamma_K,\qquad
P_B^{(a)}(t)=P_B(at).
\tag{IR13}
\]
The inverse means the centered inverse. Static response and
all-time derivative bounds can remain unchanged while the
rate per unit of the supplied parameter changes.
This does not invalidate dimensionless gap statements;
it says that changing reference has not supplied the missing
clock-selection law.

Beyond (IR16), the constructive obligation is now more specific: control
the complete interacting product channels and their kinetic
inverse in a local derivative norm, with constants stable
under the proposed block assembly.
[[block-spectral-moments-and-connected-assembly|Four one-block spectral moment bounds]]
are a proved sufficient certificate: their tensorized estimate
allows channels beyond the failed spectral triangle without a
constant accumulating per block. Those infinite row bounds
are not yet verified for the Wilson references.
[[first-order-lift-and-spectral-product-tails|The fixed-multiplier test]]
does give all-input-energy, degeneracy-independent spectral
window bounds on the actual Wilson reference. They do not
need (IR21), but neither do they prove the arbitrary two-input
product certificate. [[charged-link-probes-and-vacuum-spectral-width|The charged-link spectral law]]
separately measures the actual vacuum's contribution to the
width around the electric mean, without assuming a sharp
energy-fusion rule.
Neither the neutral block
gap, exact ground-state conjugation, nor an internal positive
associator supplies that estimate. A nonassociative parent
would add content if it constrained this shared product,
state and response law before they were chosen.

Two subsequent tests separate the remaining obligations.
[[transition-score-and-lipschitz-product-control|The actual transition score]]
does control arbitrary two-input response in a homogeneous
Lipschitz quotient, uniformly over independent copies of fixed
blocks. That is not yet a local norm for an extensive source.
More decisively, [[product-boundary-frames-and-crossing-susceptibility|independent boundary frames]]
leave a genuinely crossing loop Haar-distributed under every
such exact product vacuum. Its neutral ground-state tangent
cannot be made small simply by strengthening the internal
interactions. A correlated interface reference would change
that assumption; merely enlarging independent blocks does not.

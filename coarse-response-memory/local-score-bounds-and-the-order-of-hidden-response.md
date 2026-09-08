# Local Score Bounds and the Order of Hidden Response

A plaquette's complete scalar readout admits a volume-uniform bound on its hidden first derivative, using the actual interacting vacuum. This proves preservation of the full form domain and an exact form-valued memory resolvent without assuming a hidden gap. But this class of estimates is not closed under joining scalar readouts: two adjacent traces omit a mixed response coefficient, producing a hidden second derivative even at the Haar vacuum. The assembly problem is therefore about closure of the response geometry, not only bounds on a state's drift.

**Status: exact finite-graph estimates uniform over the stated bounded-incidence family; exact two-plaquette join obstruction.** The gauge Hamiltonian is supplied. No four-dimensional vacuum, continuum trajectory or physical mass gap is constructed.

## The operator acts on every retained finite-energy function

Use the actual finite open-box \(SU(2)\) Hamiltonian, vacuum
\(\psi_\lambda\), density \(w=\psi_\lambda^2\), and nonpositive
ground-state generator \(\mathcal L\) from
[[interacting-gauge-vacuum-and-local-memory|the physical local-memory construction]].
Write
\[
\mathcal E[F]=\kappa\int\sum_e|\nabla_eF|^2w\,dU,\qquad
D(\mathcal E)=H^1(SU(2)^E)^{\mathrm{gauge}}.
\tag{SO1}
\]
The domain is the inherited one at this fixed graph. For an
elementary square \(p\), retain \(q=q_p\), put \(h(q)=1-q^2\),
and let \(P=\mathbb E_w[\cdot\mid q]\), \(Q_\perp=I-P\).
The metric \(Q=-2\operatorname{Tr}\) is not this projection.
Identify a retained function with its lift \(f(q)\), and set
\[
a[f]=\kappa\int h(q)|f'(q)|^2w\,dU,\qquad
N_1=\sum_{e\in p}n_e\le16,\qquad
\beta=\frac{\lambda N_1}{\sqrt\kappa}.
\tag{SO2}
\]
Here \(n_e\) counts plaquettes incident on \(e\). The retained
closed form is the actual marginal radial form, not a separately
fitted generator.

The score contraction and its centered part are
\[
S=\sum_{e\in p}\langle\nabla_e\log\psi_\lambda,\nabla_eq\rangle,
\qquad S^\circ=S-\mathbb E_w[S\mid q].
\tag{SO3}
\]
[[algebra/partial-bochner-and-ground-state-score|Partial Bochner]]
gives \(|\nabla_e\log\psi_\lambda|\le\lambda n_e/\kappa\).
Each of the four plaquette gradients has norm \(\sqrt h/2\),
so, pointwise and then conditionally,
\[
|S|\le\frac{\lambda N_1}{2\kappa}\sqrt h,\qquad
\operatorname{Var}_w(S\mid q)
\le\frac{\lambda^2N_1^2}{4\kappa^2}h.
\tag{SO4}
\]
The conditional variance is bounded by the second moment; no
extra factor is needed for subtracting its mean.

Let \(K=-\mathcal L\ge0\). On smooth retained functions its
hidden part is exactly
\[
Bf=Q_\perp Kf(q)=-2\kappa f'(q)S^\circ.
\]
Consequently
\[
\boxed{\|Bf\|_w^2\le\beta^2a[f].}
\tag{SO5}
\]
It extends uniquely as a bounded map from the retained **form
domain**, with its form norm, to hidden \(L^2(w)\). It is not
asserted to be bounded on retained \(L^2\). For the particular
character \(2q\), this gives
\(\mathcal D_p\le4\lambda^2N_1^2\mathbb E_w h\).
The all-coupling bound supplements, rather than invalidates,
the earlier one-link integrated estimates.

## Conditional projection preserves the inherited domain

This needs a proof: conditioning need not preserve an arbitrary
energy domain. In the regular set \(-1<q<1\), define the raw
horizontal vector field
\[
X=\frac{\nabla q}{h(q)}.
\]
The unweighted identities \(|\nabla q|^2=h\) and
\(\Delta q=-3q\) imply
\[
Xq=1,\qquad \operatorname{div}_{H}X=-q/h.
\tag{SO6}
\]
The divergence is a function of \(q\), so it cancels when
differentiating a normalized conditional average. Coarea or
integration by parts gives, for smooth physical \(F\),
\[
(PF)'=\mathbb E_w[XF\mid q]
 +2\operatorname{Cov}_w(F,S/h\mid q).
\tag{SO7}
\]
This is a derivative along the horizontal field, not a naive
coordinate derivative holding arbitrary hidden coordinates fixed.

Conditional Cauchy--Schwarz, (SO4), and the triangle inequality
in the marginal \(L^2\) norm now give
\[
\boxed{
\sqrt{a[PF]}\le\sqrt{\mathcal E_p[F]}
 +\beta\|Q_\perp F\|_w
\le\sqrt{\mathcal E[F]}+\beta\|Q_\perp F\|_w,
}
\tag{SO8}
\]
where \(\mathcal E_p\) keeps only the four plaquette gradients.
For the first term, use
\(\sqrt h\,|XF|\le|\nabla_pF|\); for the second, use the
conditional variance bound in (SO4).

The apparent singularity of \(X\) at \(q=\pm1\) creates no
additional boundary condition. For smooth \(F,w\), Haar
conditioning can be written by replacing one plaquette link
with its full holonomy, integrating the other links, and
averaging conjugations of that holonomy. Thus
\[
PF=\frac{P_H(wF)}{P_Hw}
\]
lifts to a smooth class function on \(SU(2)\); its denominator
is strictly positive. Applying (SO8) to differences of smooth
approximants proves \(P D(\mathcal E)\subset D(\mathcal E)\).
It also proves this for \(Q_\perp\). The graph-norm estimate
contains no global maximum/minimum ratio of \(w\).

The retained and hidden form domains therefore give the actual
topological decomposition
\[
D(\mathcal E)=D(a)\oplus D(c),\qquad
c=\mathcal E|_{\operatorname{Ran}Q_\perp}.
\tag{SO9}
\]
Both restrictions are densely defined and closed. Let \(A,C\)
be their associated nonnegative self-adjoint operators. On
these **form** domains,
\[
\mathcal E[f+y]=a[f]+2\operatorname{Re}\langle Bf,y\rangle+c[y].
\tag{SO10}
\]
Integration by parts proves the cross identity on smooth
retained functions and then (SO5) extends it. No identity
\(D(K)=D(A)\oplus D(C)\), or unrestricted \(B^*y\), is used.

## The memory law exists as a form-valued resolvent

Here \(z>0\) is a Laplace parameter, distinct from the
orientation coordinate used in the later pair test. Define
on \(D(a)\)
\[
s_z[f]=z\|f\|^2+a[f]
 -\|(C+z)^{-1/2}Bf\|^2.
\tag{SO11}
\]
Minimizing \(\mathcal E[f+y]+z(\|f\|^2+\|y\|^2)\) over hidden
\(y\) gives (SO11), attained at
\(y=-(C+z)^{-1}Bf\). In particular no inverse at zero frequency
and no hidden spectral floor has been assumed.

These are closed forms with the same domain for every \(z>0\):
\[
\boxed{
z\|f\|^2+\frac{z}{z+\beta^2}a[f]
\le s_z[f]\le z\|f\|^2+a[f].
}
\tag{SO12}
\]
For a direct proof, positivity Cauchy--Schwarz in (SO10) gives
\[
\sqrt{a[f]}\le\sqrt{\mathcal E[f+y]}+\beta\|y\|.
\]
Weighted scalar Cauchy--Schwarz bounds its square by
\((1+\beta^2/z)(\mathcal E[f+y]+z\|y\|^2)\).
Minimize over \(y\) and add \(z\|f\|^2\). The two-sided form
comparison proves closedness as well as positivity.

If \(\mathsf S_z\) denotes the operator of \(s_z\), the exact
compressed physical resolvent is
\[
\boxed{P(K+z)^{-1}|_{\operatorname{Ran}P}=\mathsf S_z^{-1},}
\qquad
(z+A)^{-1}\le\mathsf S_z^{-1}
\le\left[z+\frac{z}{z+\beta^2}A\right]^{-1}.
\tag{SO13}
\]
Eliminating the hidden component of the weak variational
resolvent equation proves the identity. It is not a formal
block-operator inversion.

For \(f,g\in D(a)\), the memory kernel is safely the form
\[
m_t(f,g)=\langle Bf,e^{-tC}Bg\rangle,\qquad
|m_t(f,g)|\le\beta^2\sqrt{a[f]a[g]}.
\tag{SO14}
\]
Its Laplace transform is
\(\langle Bf,(C+z)^{-1}Bg\rangle\). Thus (SO11) is the same
hidden-return mechanism as
[[inq#Eliminating the hidden evolution leaves a memory kernel|the bounded-block construction]],
now justified on this unbounded physical form domain.
It does not assert a bounded \(L^2\) kernel or an unproved
strong Volterra equation.

The bound stays uniform when further plaquettes are attached
within the cubical bounded-incidence family, for this same
kind of single-plaquette readout and each graph's **own actual
vacuum**. It does not say those finite vacua have compatible
marginals, or construct one from another. Moreover,
\(z/(z+\beta^2)\to0\) as \(z\downarrow0\) when \(\beta>0\).
Even a positive marginal form gap cannot turn (SO12) into a
positive physical gap. It gives no missing low-frequency
control for free.

## Joining scalar readouts changes the differential order

There is a stricter assembly test than enlarging the exterior
of one fixed trace. On
[[two-plaquette-vacuum-and-relational-state|the complete adjacent-pair carrier]],
retain **both** traces \((a,b)\), but discard their relative
orientation \(z=\mathbf x\cdot\mathbf y\). At zero magnetic
coupling the vacuum is Haar, and
\[
\begin{aligned}
B_{ab}F&=-\frac{\kappa}{2}z\,\partial_a\partial_bF,\\
\|B_{ab}F\|^2
&=\frac{\kappa^2}{12}
  \int(1-a^2)(1-b^2)|F_{ab}|^2\,d\mu_H(a)d\mu_H(b),\\
a_{ab}[F]&=\kappa\int
 [(1-a^2)|F_a|^2+(1-b^2)|F_b|^2]\,d\mu_H(a)d\mu_H(b).
\end{aligned}
\tag{SO15}
\]
The conditional Haar variance is
\(\mathbb E[z^2\mid a,b]=(1-a^2)(1-b^2)/3\). This is a
hidden **second** derivative, unlike (SO5).

Let \(U_n=C_n^1\) be the normalized Haar \(SU(2)\) character,
so \(\|U_n\|_{L^2(\mu_H)}=1\) and its radial energy is
\(n(n+2)\). The centered smooth functions
\(F_n(a,b)=U_n(a)U_n(b)\), \(n\ge1\), satisfy
\[
\boxed{
\frac{\|B_{ab}F_n\|^2}{a_{ab}[F_n]}
=\frac{\kappa n(n+2)}{24}\longrightarrow\infty.
}
\tag{SO16}
\]
Each single-trace readout is autonomous at Haar. Their
joined scalar algebra nonetheless fails every bound
\(\|B_{ab}F\|^2\le b^2a_{ab}[F]\) with finite \(b\).
The two individual estimates cannot be assembled by adding
their constants.

There is an exact sharper statement about the correct order.
At Haar, \(A_{ab}=\kappa(K_a+K_b)\), where
\(K_aU_n=n(n+2)U_n\). Derivative orthogonality in the full
product-character expansion gives
\[
\boxed{\|B_{ab}F\|^2\le\frac1{48}\|A_{ab}F\|^2,
\qquad F\in D(A_{ab}).}
\tag{SO16a}
\]
Indeed each \((n,m)\) coefficient contributes
\(\kappa^2 n(n+2)m(m+2)/12\) on the left and
\(\kappa^2[n(n+2)+m(m+2)]^2\) to the squared operator norm.
Use \(xy\le(x+y)^2/4\). Every \(n=m\ge1\) attains equality.
The joined hidden map is bounded in the **operator graph
norm**, not the form norm used in (SO5).

This failure persists at every fixed finite magnetic coupling.
The positive smooth interacting density leaves the conditional
orientation variance strictly positive in the interior. For
the positive transformed generator, the highest-order hidden
term on trace-only functions is
\[
-\frac{\kappa}{2}
\bigl(z-\mathbb E_w[z\mid a,b]\bigr)F_{ab};
\tag{SO17}
\]
all remaining hidden terms have at most one derivative.
Choose a nonzero smooth cutoff \(\eta\) compactly supported
in the regular \((a,b)\) interior and
\(F_N=\eta(a,b)e^{iN(a+b)}\).
Its retained energy is \(O(N^2)\), whereas
\[
\|B_{ab}F_N\|^2
=\frac{\kappa^2N^4}{4}
 \int|\eta|^2\operatorname{Var}_w(z\mid a,b)\,d\bar\nu_w
 +O(N^3).
\tag{SO18}
\]
The leading coefficient is strictly positive. These are
fixed-system estimates; no large-coupling-uniform remainder
is claimed. Subtracting the actual mean leaves derivatives
and the hidden response unchanged.

Conditional projection itself remains well-defined on the
inherited Sobolev domains. In this pair,
\(P_wF=P_H(wF)/(P_Hw)\), and \(P_H\) is averaging over the
independent conjugations of the two holonomies. This compact
isometric averaging preserves ordinary \(H^1,H^2\);
multiplication by the smooth positive factors does so at
each fixed coupling. The failure is the order of the hidden
operator, not an ill-defined projection.

## The structure a composable readout must preserve

For a diffusion with coordinate readout \(r=(r_i)\), the
second-order coefficients on \(f(r)\) are the mixed responses
\(\Gamma(r_i,r_j)\). If all are functions of \(r\), hidden
response begins at first order; drift bounds can then be
relevant. If a quadratic combination has nonzero conditional
variance on a regular patch, the oscillatory test above
detects a hidden principal part that no first-energy bound
can absorb.

For one plaquette, \(\Gamma(q,q)=\kappa(1-q^2)\) is retained.
For the pair, \(\Gamma(a,b)=\kappa z/4\) is not a function of
the two traces. Retaining that mixed response supplies \(z\),
which completes this pair's invariant carrier. The
[[gauge-boundary-frame-gluing/oriented-context-gluing-and-mixed-response|response-generated invariant construction]]
addresses how further relational invariants enter larger
joins; pair completion is not a proof of general closure.

The resulting operator-type constraint is specific: a
whole-to-local programme seeking lower-order memory must
control closure under **mixed response**, not merely closure
under multiplication or separate regional evolution.
[[boundary-interaction-and-conditional-score-budget|A disjoint raw-link regional cut]]
retains that principal geometry and extends the conditional
form-domain argument to the full regional carrier. Its relative
vacuum Fisher budget counts crossing interactions, but only in
an integrated or gradient-sup register. The presently proved
form-relative constant still counts the links in the region.
A construction may instead retain higher-order, form-valued
memory, but it must prove estimates in that stronger topology.
This is not fundamental nonassociativity: the scalar algebras
here remain associative. Nor does completing a finite
invariant carrier select its Hamiltonian or force a continuum
gap.

[[receipts/two_plaquette_vacuum_receipt.py|The interacting receipt]]
checks the full first-derivative Gram against the retained
energy on eight class-polynomial directions, using computed
vacua and independent cutoffs and quadratures. With
\(\kappa=1\), its maximal quotients at \(\lambda=0.5,1\) are
approximately \(0.001923415312,0.008293765672\), below the
respective bounds \(6.25,25\). A separate check differentiates
the actual conditional mean of \(ab+z\) and verifies (SO7)
with the full mixed cometric. Sampled score values do not
prove the global supremum in (SO4); the Bochner proof does.
These finite checks are not interval-certified estimates or
evidence of a uniform physical gap.

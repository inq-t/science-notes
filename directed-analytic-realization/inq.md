---
inq.module: "directed-analytic-realization"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
  - "**/*.txt"
---
# Directed Analytic Realization

A one-sided process can forget an initial history while its persistent analytic tail determines a Hilbert quotient, positive clock and stationary state action. Harmonic boundary response relates that clock to compression; opposed value and normal-response data extend the construction to a local scalar action in \(3+1\) coordinates. The circle edge closes under refinement, while a capped three-dimensional member opens a clock gap but violates locality. These explicit returns and failures constrain the sought directed realization without yet supplying an interacting Yang–Mills theory.

The [[harmonic-boundary-realization|harmonic boundary construction]] selects the original tail's complex orientation from a real tangent derivative and identifies its positive modulus with boundary response. [[algebra/hardy-compression-and-boundary-response|The compression theorem]] owns the exact residue calculation. [[local-weyl-realization|The local Weyl construction]] then uses that response as a one-particle norm and its odd partner as a local commutation form. This last step is an additional CCR/Fock realization, not the claim that compressing multiplication preserves locality.

The [[three-dimensional-boundary-test|three-dimensional test]] requires a different pairing: one scalar harmonic graph has zero Green form, while two opposed graphs supply a full Cauchy carrier. [[algebra/cauchy-response-and-local-action|The shared Cauchy theorem]] derives its clock and local wave action from the same response. [[algebra/three-dimensional-weighted-compression-response|A Green-weighted compression trace]] computes that response in three dimensions; simply reusing the circle's unweighted trace would diverge. The three-dimensional metric, clock-realization prescription and bosonic vacuum remain inputs.

## The primitive member

Fix \(R>0\). The process address \(x\geq0\) has no assigned spacetime or clock unit. Let

\[
\mathcal P_R
=\left\{
p(x)=\sum_{n=0}^{N}a_n e^{-inx/R}
\right\},
\qquad
\mathcal N=L^2_c([0,\infty)).
\tag{DA1}
\]

The literal tail period is \(2\pi R\). Here \(L^2_c\) consists of square-integrable functions of compact essential support, identified almost everywhere. Set

\[
\mathcal V_R=\mathcal P_R+\mathcal N,\qquad
(T_sf)(x)=f(x+s),\quad s\geq0.
\tag{DA2}
\]

This is a complex vector-space construction. No closed physical observable *-algebra is claimed; products of arbitrary \(L^2_c\) functions need not lie in \(L^2_c\).

The decomposition \(f=p+r\) is unique: a periodic trigonometric polynomial vanishing outside a compact set vanishes everywhere. Each \(T_s\) preserves \(\mathcal V_R\), obeys \(T_{s+t}=T_sT_t\), and for \(s>0\) annihilates every transient supported inside \([0,s)\). The process is therefore noninjective before realization.

It is nevertheless onto: to lift \(p+r\), translate the polynomial backward and take the transient \(r(x-s)\) for \(x\geq s\), zero for \(x<s\). Thus failure of an inverse is a genuine loss of initial data, not failure to reach a later presentation.

The primitive choices are the additive future-address monoid, the periodic analytic tail, complex scalars and the mean pairing below. They are not claimed to follow from pure algebra without further principles.

## The same law selects the quotient

Define

\[
g_R(f,h)=\lim_{L\to\infty}\frac1L
\int_0^L\overline{f(x)}h(x)\,dx.
\tag{DA3}
\]

For \(f=p+r\), \(h=q+v\), the limit exists. Transient terms have finite integrals, and polynomial–transient cross terms are integrable by compact support and Cauchy–Schwarz. Dividing them by \(L\) sends them to zero. Fourier averaging gives

\[
\boxed{g_R(f,h)=\sum_{n\geq0}\overline{a_n}b_n.}
\tag{DA4}
\]

Consequently \(g_R\geq0\) and its radical is exactly \(\mathcal N\). The quotient completion is

\[
\mathcal H_R
=\overline{\mathcal V_R/\mathcal N}
\cong\ell^2(\mathbb N_0)
\cong H^2(\mathbb D).
\tag{DA5}
\]

The last identification sends \(e^{-inx/R}\) to \(z^n\). It is an analytic boundary representation, not a statement that the disk is physical space.

The quotient \(q_R\) and dynamics come from the same presentations:

\[
q_RT_s=U_s q_R,\qquad
(U_sa)_n=e^{-ins/R}a_n.
\tag{DA6}
\]

Thus \(g_R\) is preserved and \(T_s\) is onto modulo its radical. The induced semigroup extends to a unitary group and is strongly continuous: first check finite sequences, then use density and norm preservation.

Initial transients can be changed freely without altering the realized norm or clock. Conversely, a nonzero tail cannot be discarded by this particular realization rule.

## A positive generator without an appended Hamiltonian

Differentiating (DA6) yields

\[
K_Ra=\left(\frac nR a_n\right)_{n\geq0},
\qquad
\operatorname{Dom}K_R
=\left\{a:\sum_{n\geq0}\frac{n^2}{R^2}|a_n|^2<\infty\right\}.
\tag{DA7}
\]

The diagonal operator is self-adjoint and positive, and \(U_s=e^{-isK_R}\). Its vacuum is the constant tail \(\Omega=(1,0,\ldots)\):

\[
\sigma(K_R)=\{n/R:n\in\mathbb N_0\},\qquad
\ker K_R=\mathbb C\Omega,\qquad
\inf\sigma(K_R|_{\Omega^\perp})=1/R.
\tag{DA8}
\]

These values were not supplied as a Hamiltonian. They are forced by translation on the declared analytic periodic tails. Positivity comes from retaining only the chosen Fourier orientation; admitting both signs gives spectrum \(\mathbb Z/R\), unbounded below. Forgetting initial data alone does not select the orientation.

The [[harmonic-boundary-realization|oriented disk member]] gives a geometric selection relative to its declared metric and orientation. It does not derive that disk or a preferred orientation from the unstructured tail space.

This is not a physical mass calculation. \(R\) fixes the period in the process address, not a spatial radius or a measured cosmic scale. Its selection and its physical normalization remain open.

## Stationary action is a quotient description

[[algebra/quotient-clock-and-stationary-action|The quotient-action theorem]] applies with the norm in (DA4) and generator (DA7). It returns

\[
\omega(a,b)=2\operatorname{Im}\sum_n\overline{a_n}b_n
\]

and the exact state functional

\[
\mathcal S[a]=\int
\left[
\frac i2\sum_n
(\overline{a_n}\dot a_n-\dot{\overline{a_n}}a_n)
-\sum_n\frac nR|a_n|^2
\right]\,ds.
\tag{DA9}
\]

On the declared graph-domain path class, stationarity with fixed endpoint variations is equivalent to \(i\dot a=K_Ra\). Its pullback to presented histories is unchanged by every compact transient.

The equation describes the retained dynamics and says nothing about which transient occurs. The whole process was defined by composition and translation, not by extrema of (DA9). No spacetime integral, classical path-integral measure or field equation has been constructed by writing this state action.

## The exact compositional invariant

The return has a simple invariant:

\[
g_R(T_sf,T_sh)=g_R(f,h),
\qquad
q_RT_{s+t}=U_sU_tq_R.
\tag{DA10}
\]

Mean boundary response and composition agree across a nonfaithful realization. This is a concrete model of directed presentation with reversible observable evolution. It does not assign a positive mean-response cost to discarded transients: their cost in \(g_R\) is zero. A theory identifying a nonzero residue with mass must therefore add a genuinely selected response relation, not rename this radical.

The process parameter and the physical clock are still different types. Equation (DA6) returns one mathematical parameter in two representations; it does not calibrate seconds or construct factual record ordering.

## Refinement that preserves the law and removes the gap

Let \(R_j=j!R_0\), \(j\geq1\). If \(R_{j+1}=kR_j\), embed the old tail in the new one by

\[
e^{-inx/R_j}=e^{-i(kn)x/R_{j+1}}.
\tag{DA11}
\]

These inclusions preserve the actual functions, \(g_R\), the vacuum and all \(T_s\). Old modes keep their rates. New modes occur between them; this is not merely a change of units.

The direct union has finite sums of nonnegative rational frequencies,

\[
\Gamma=\mathbb Q_{\geq0}/R_0,\qquad
p(x)=\sum_{\lambda\in F\subset\Gamma}
a_\lambda e^{-i\lambda x}.
\]

Distinct frequencies are orthogonal in the same mean pairing. The completion and its generator are

\[
\mathcal H_\infty=\ell^2(\Gamma),\qquad
(K_\infty a)_\lambda=\lambda a_\lambda,\qquad
\sigma(K_\infty)=\overline\Gamma=[0,\infty).
\tag{DA12}
\]

The self-adjoint generator has its maximal diagonal domain

\[
\operatorname{Dom}K_\infty
=\left\{a\in\ell^2(\Gamma):
\sum_{\lambda\in\Gamma}\lambda^2|a_\lambda|^2<\infty\right\}.
\]

The vacuum remains unique. For any prescribed \(\varepsilon>0\), a unit tail at a rational frequency \(0<\lambda<\varepsilon\) has response norm one and generator expectation \(\lambda\). It is not a transient and cannot be erased by the existing kernel.

Therefore one-sided forgetting, positivity of the generator, quotient unitarity and exact stationary state action all survive this refinement while the gap disappears. The periodic member is not a solution to the continuum mass-gap problem. This period refinement is not claimed to be the Yang–Mills ultraviolet limit. The full goal needs a structural reason to control or exclude soft retained directions under the limits of its actual four-dimensional realization.

## A whole-history quotient is not a finite-cut readout

No finite initial interval determines \(q_R f\). For distinct tails \(p,q\) and any \(A>0\), set

\[
r(x)=(p(x)-q(x))\,\mathbf1_{[0,A]}(x).
\]

Then \(q+r\) and \(p\) agree almost everywhere on \([0,A]\), but their realized classes are \(q\) and \(p\). Consequently the quotient map cannot factor through restriction to that finite interval.

The long-interval mean is an asymptotic whole-history construction. Calling its return a finite causal-patch observable would require a separate observable net and realization theorem. This does not invalidate the quotient-action result; it identifies another obligation before that result can model local observation.

## What this member changes in the programme

The member supplies an explicit relationship among process, quotient metric, generator and action. It is more than a freely appended Hamiltonian on an unrelated quotient. It does not prove that these primitive choices are necessary or identify the member with nature.

The remaining choices in the tail construction are now visible: analytic polarization, periodic versus refined tail class, averaging rule and process parameter. The harmonic extension constrains the first relative to an oriented metric disk; the Weyl realization constructs local circle algebras but additionally selects bosonic CCR and a Gaussian vacuum. No three-dimensional spatial arena, gauge group, gravity, interacting vacuum or cosmological history is derived here. The [[contemporary-puzzles/yang-mills-mass-gap/directed-realization-and-foundational-restart|foundational restart]] remains aimed at the full [[contemporary-puzzles/yang-mills-mass-gap/clay-contract-and-scale-assumptions|Clay return]], not at substituting these members for that target.

[[receipt.py|The finite receipt]] checks composition, transient erasure, pairing, symplectic invariance, action-variation signs and compatible refinement on representative modes. The proofs above, not finite sampling, establish the infinite-dimensional quotient and spectra.

[[boundary_response_receipt.py|The boundary receipt]] separately checks harmonic integration against compression and clock forms, both orientation signs, local-readout failure, the central Weyl relation, and the changed normalization under period covers. It uses exact finite-polynomial Hardy matrices with a sufficient halo, avoiding the spurious second boundary of a finite matrix cut. [[boundary-response-receipt-output.txt|Its stored output]] records these finite checks, not a certification of the full observable theory.

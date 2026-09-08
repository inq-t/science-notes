---
inq.module: scale-incidence-response
inq.include:
  - './'
inq.ambient:
  - 'receipts/*.py'
  - 'receipts/*.txt'
  - 'junk-drawer/**'
keywords:
  - paired filtrations
  - joint incidence
  - reciprocal scale
  - closed quadratic form
  - compensated response
  - four-dimensional balance
  - lower frame bound
---
# Scale Incidence Response

A floor for an inverse-scale response can arise either because sufficiently deep joint incidences are absent or because an independently constructed response compensates their attenuation. This module gives the exact support and closed-form criteria for those alternatives on supplied carriers. A physical realization must construct the filtrations, cover the complete vacuum complement and compare the response with the physical energy or Casimir before either criterion becomes a mass-gap theorem.

## Joint support constrains reciprocal distinctions

[[trace-dirichlet-descent/inq|Trace Dirichlet descent]] supplies the shared projection and response-filtration setting. [[scale-incidence-response/paired-scale-filtrations-and-the-invariant-incidence-wall|The paired-filtration theorem]] assigns fixed scale labels to two strongly commuting shell decompositions. On their joint-active carrier, nonzero joint projections \(Q_{jk}\) define the mean address

\[
A=\sum_{j,k}\frac{N_j^++N_k^-}{2}Q_{jk},
\qquad M_p=e^{-pA},\quad p>0.
\]

A uniform floor for \(M_p\) is equivalent to an upper bound on occupied mean addresses. Each directional address may remain unbounded, and opposite translations of the two labels leave their mean fixed. The constrained datum is their incidence relation, not either marginal filtration or a smallest spatial pixel. [[logistic-scale-geometry/resolvent-logistic-scale-transform|The resolvent center theorem]] gives the corresponding exact spectral presentation: a lower positive operator edge is an upper bound on its negative logarithm.

Strong commutation makes the joint intersections genuine orthogonal projections. Terminal tails and one-sided sectors must also be accounted for: a joint-active estimate covers the full physical vacuum complement only when those omitted sectors introduce no additional nonvacuum kernel. A physical null-pair interpretation further requires the appropriate Lorentz reconstruction and same-carrier comparison; the scale labels alone do not supply it.

## A closed response can compensate deep incidence

[[scale-incidence-response/compensated-incidence-response-and-four-dimensional-balance|Compensated incidence response]] replaces support exclusion by the closed pullback

\[
C=\overline{R^{1/2}M_p},
\qquad q[f]=\|Cf\|^2,
\]

assuming the raw product is densely defined and closable. If \(R\) reduces the joint shells, write \(a_\alpha\) for their addresses and \(\rho_\alpha\) for the bottom of each response block. The exact condition is

\[
q\geq\kappa^2 I
\quad\Longleftrightarrow\quad
\inf_{\alpha:Q_\alpha\ne0}
\rho_\alpha e^{-2pa_\alpha}\geq\kappa^2.
\]

The support wall is the special case \(R=I\). With noncommuting response, the criterion remains the closed-form inequality \(C^*C\geq\kappa^2I\); formal multiplication or subtraction of unbounded operators cannot replace the domain argument. Compensation cannot repair an exact kernel of the presentation map. Boundary channel count likewise cannot replace the lower frame estimate on every shell.

For bilateral address support, the homogeneous law \(R=r_0e^{qA}\) has a uniform floor exactly at \(q=2p\). A one-sided carrier has weaker conditions and does not force that equality. [[scale-incidence-response/codimension-two-response-balance|The codimension-two application]] separately requires an independent identification of \(A\) with log length, first inverse-length presentation \(p=1\), and response character \(q=D-2\). Those power characters cancel at \(D=4\). With a residual factor \(Z_D(A)\), the four-dimensional response is still \(r_0Z_4(A)\); power cancellation does not prove its uniform positive lower bound.

[[finite-index-distinction/finite-index-duality-and-the-square-response|Standard finite-index duality]] provides a separate algebraic square normalization. Its use here requires a scale family and a realization of its intertwiner as the same physical response, rather than identification of a fixed scalar index with stiffness. [[measured-response-carriers/response-to-energy-comparison|The response-to-energy theorem]] then states the distinct coverage and energy-comparison hypotheses needed to carry any constructed response floor to a physical one.

Both theorem notes link their finite receipts and stored outputs. The calculations check selected projection, support, compensation and kernel examples; they do not establish bilateral infinite support, the geometric exponent assumptions, or a Yang--Mills continuum limit. [[scale-incidence-response/research-history|The research history]] retains the combined exposition from before the geometric application was separated.

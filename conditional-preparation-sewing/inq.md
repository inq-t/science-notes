---
inq.module: conditional-preparation-sewing
inq.include:
  - './'
keywords: [conditional-preparation, marked-sewing, access, ancestral-readout, normalization, clock]
---
# Conditional Preparation Sewing

A preparation can acquire a new comparison while preserving the complete experiment accessible through an old one. The necessary normalization depends on the retained preparation, not only on a scalar partition function. This module constructs positive marked kernels with exact ancestral readout, derives their finite returned clocks and differentiates their full conditional law. The construction also proves where preservation fails: changing the retained parent, forgetting an ancestor or replacing an inherited composite by a fresh comparison can change the response.

## Preservation concerns the processed experiment

[[conditional-preparation-sewing/access-ports-and-conditional-sewing|Access ports]] specify where a preparation and its readout live. A conditional Gaussian extension preserves the old prior and all its marks. After a new comparison is inserted, integration over that comparison generally reweights the retained preparation. Equality of prior marginals therefore does not imply equality of the old marked transfer.

[[conditional-preparation-sewing/conditional-normalization-and-marked-access|Conditional normalization]] makes this distinction exact. For old preparation \(\xi\), conditional extension \(\eta\), and the group-comparison kernels \(p_\xi,q_\eta\) with boundary-independent row integrals, put
\[
b(\xi)=\mathbb E\!\left[\int q_\eta(B,B')\,dB'\mid\xi\right].
\]
The raw extension retains the factor \(b(\xi)\) in every old marked readout. A single scalar removes it for all old marks only when \(b\) is almost surely constant. The different law
\[
\widetilde F^M(A,B;A',B')
=z^{-1}\mathbb E\!\left[M(\xi)p_\xi(A,A')\frac{q_\eta(B,B')}{b(\xi)}\right]
\]
preserves the old marked kernel exactly after the new outgoing boundary is integrated; \(z\) is the old source-free row normalization. The denominator is source-free and stays fixed when marks are differentiated. It is part of the comparison prescription, not a disposable determinant factor.

[[conditional-preparation-sewing/conditional-preparation-extension-at-new-access|The single-access construction]] realizes the comparison on actual multiplication paths. A correlated innovation restores motion in a newly physical loop, but a single joint Gaussian normalization changes the old clock. The conditional prescription preserves that clock and still permits finite new dynamics. Their different joint responses exhibit a constitutive choice that correlation or positivity alone does not settle.

## Compose over an ancestral access diagram

[[conditional-preparation-sewing/conditional-preparation-diagrams-and-ancestral-readout|Preparation diagrams]] allow several retained parents. On a finite directed acyclic diagram \(D\), choose a faithful conditional preparation law and actual independently variable group words with the proved product-Haar carrier. For each node define
\[
b_i(\xi_{\operatorname{pa}(i)})
=\mathbb E\!\left[\int q_i(g_i,g_i';\xi_i)\,dg_i'
\mid\xi_{\operatorname{pa}(i)}\right].
\]
The complete kernel is
\[
F_D^M(g,g')=\mathbb E\!\left[M(\xi)\prod_{i\in D}\frac{q_i(g_i,g_i';\xi_i)}{b_i(\xi_{\operatorname{pa}(i)})}\right].
\]
For an ancestral subset \(J\), integrating forgotten outgoing words gives \(F_J^M\) whenever the mark uses only retained data. Reverse leaf elimination proves the identity, including its scalar factors; every permitted elimination order agrees. It intertwines the retained operators and their temporal products with retained insertions.

This theorem assumes the actual word-coordinate and gauge transport conditions. Dependent words cannot be treated as new independent Haar variables. Correlations at independently gauged ports require invariant sectors or explicit transported maps. [[conditional-preparation-sewing/access-ports-and-conditional-sewing|The access-port obstruction]] also shows that normalization with one retained root need not equal normalization with the opposite root. A nonancestral readout retains hidden normalization data. The theorem supplies coherence for the declared diagram, not invariance under every change of access.

## Returned clocks and closed response use the same law

[[conditional-preparation-sewing/conditional-access-families-and-the-returned-clock|Conditional access families]] prove finite Casimir returns for a growing family over one retained root, under explicit preparation-rank and moment assumptions. The diagram theorem extends the return to several parents without increasing its sufficient matrix inventory. Joint preparation correlations survive in marked observables, but do not by themselves create the mixed derivatives required by spatial incidence. The paces, arrows, covariance and word inventory remain specified data.

[[conditional-preparation-sewing/conditional-scale-scores-and-the-closed-response|Conditional scale scores]] differentiate every parent normalizer. The resulting innovation-variance scores are conditionally centered; their complete Fisher matrix, observed Fisher loss and Hessian contact terms follow from that same law. Closed weighting and physical readout can couple those directions. Common dilation returns the declared \(H_s=s^{-1}K+sV\) family with its normalizers transported; an auxiliary Fisher bound is not yet a physical gap or cosmic curvature theorem.

[[general-causal-action/general-group-preparation-and-the-casimir-return|The preparation/Casimir theorem]] supplies the analytic localization input, and [[general-causal-action/marked-gaussian-constraints-and-sewing-measures|marked Gaussian sewing]] supplies the source and reference-measure conventions. For a spatial realization, [[general-causal-action/shared-preparation-actions-and-the-conditional-return|shared prepared actions]] must match the actual incidence. [[general-causal-action/prepared-readout-algebra-and-physical-source-completeness|Readout completeness]] then constructs its physical source algebra, and [[physical-response-coercivity/conditional-vacuum-rigidity-and-the-physical-gap|complete-source susceptibility]] states the stronger spectral test. The exact preservation identities above do not supply that uniform physical estimate or select the primitive preparation law.

# Causal Order and Metric Scale

Under the standard causality and regularity hypotheses, causal order determines a Lorentzian spacetime only up to conformal scale. A positive scale section then selects a metric representative, so causal structure and metric calibration are related but mathematically distinct data.

Let \((M,g)\) be a time-oriented Lorentzian spacetime. Metrics related by a positive Weyl factor,

$$
\widehat g_{ab}=\Omega^2g_{ab},
\qquad
\Omega>0,
$$

have the same timelike and null cones and hence the same causal order.

Conversely, in spacetime dimension at least three and in the standard causal-reconstruction regime—for example, future- and past-distinguishing spacetimes with the usual smoothness hypotheses—an order-preserving identification between already-given smooth spacetimes determines the conformal metric. The theorem-level rigidity statement is therefore

$$
\boxed{
\text{causal order}
\Longrightarrow
[g],}
$$

not

$$
\text{causal order}
\Longrightarrow
g.
$$

The hypotheses matter. The statement does not automatically cover causally pathological spaces, singular causal sets without a manifold reconstruction, or an arbitrary relation merely called causal. In particular, it is a rigidity result between spacetimes already carrying the required manifold and regularity structure, not an existence theorem reconstructing a spacetime from any abstract order.

## Scale as a section

Let \(\mathcal E[1]\) denote the weight-one density bundle in a chosen conformal convention and let

$$
\mathbf g\in\Gamma(S^2T^*M\otimes\mathcal E[2])
$$

denote the conformal metric. A positive section

$$
\sigma\in\Gamma(\mathcal E[1]),
\qquad
\sigma>0,
$$

selects the ordinary metric representative

$$
\boxed{
(g_\sigma)_{ab}
=\sigma^{-2}\mathbf g_{ab}.}
$$

Changing conformal presentation changes the displayed representatives of \(\mathbf g\) and \(\sigma\) together while leaving \(g_\sigma\) unchanged. The pair is a presentation of one calibrated metric, not two independent physical metrics.

[[library/an-introduction-to-conformal-geometry-and-tractor-calculus/inq|Curry and Gover]] give the standard density-bundle and tractor formulation. A metrological unit line is not automatically \(\mathcal E[1]\): changing from metres to centimetres is a basis change for a quantity, whereas choosing a different physical section \(\sigma\) can select a different metric representative. A theory that identifies the two must supply the comparison map.

The scale section is not an additional causal relation. It is the datum that turns conformally meaningful comparisons into calibrated intervals, curvatures, temperatures, and densities.

The logarithmic comparison of two nonzero scale sections is dimensionless:

$$
N_2-N_1
:=-\ln\frac{\sigma_2}{\sigma_1}.
$$

In a homogeneous FLRW representative with \(\sigma\propto a^{-1}\), this becomes

$$
N_2-N_1
=\ln\frac{a_2}{a_1}.
$$

The FLRW equality is a specialization; logarithmic scale is not thereby proper time, conformal time, modular time, or renormalization-group scale.

## What the reconstruction theorem does not supply

Causal reconstruction does not determine:

- which positive scale section is physically realized;
- a quantum state associated with changing scale;
- an information metric or response law;
- a gravitational field equation;
- a conserved charge; or
- a theory of facts and records.

Those require additional structures with declared maps and logical statuses. [[program-core/axioms-and-principles#Physical principles|The programme's observable-scale principle]] is one such proposed bridge; it is not part of the causal-reconstruction theorem.

# Relative Distinguishability Deficit

Restriction to an accessible algebra cannot increase relative distinguishability. The resulting deficit is an exact, nonnegative measure of what the chosen readout fails to retain about a pair of states. It is a natural model for information hidden beyond a causal wall, but it is relational bookkeeping rather than an independently conserved substance, and no theorem presently identifies it with geometry.

## Data processing under restriction

Let \(\mathcal D\subseteq\mathcal M\) be a unital inclusion of observable algebras, and let \(\omega\) and \(\varphi\) be states for which the relevant relative entropy is defined. Restriction gives

$$
i^*:S(\mathcal M)\longrightarrow S(\mathcal D),
\qquad
i^*\omega=\omega|_{\mathcal D}.
$$

Monotonicity of quantum relative entropy gives

$$
D_{\mathcal M}(\omega\Vert\varphi)
\geq
D_{\mathcal D}(i^*\omega\Vert i^*\varphi).
$$

Define

$$
\Delta_{\mathcal D\subseteq\mathcal M}(\omega,\varphi)
:=
D_{\mathcal M}(\omega\Vert\varphi)
-D_{\mathcal D}(i^*\omega\Vert i^*\varphi).
$$

Then

$$
\boxed{
\Delta_{\mathcal D\subseteq\mathcal M}(\omega,\varphi)\geq0.
}
$$

In finite dimensions this is the usual data-processing theorem. For local quantum field theory the corresponding statement belongs to Araki relative entropy on von Neumann algebras, with the necessary support and normality qualifications. [[basic-concepts/hessians/symmetrized-relative-entropy-hessian#Continuum boundary|The Hessian theorem's continuum boundary]] records the required qualifications.

## Equality and recovery

Under the standard hypotheses, equality in data processing is associated with sufficiency or recoverability: there exists a recovery map that reconstructs the relevant state pair from their restrictions. Strict inequality means that the chosen readout channel has discarded distinctions relevant to that pair.

This makes the deficit more precise than an absolute phrase such as “hidden information.” It depends on

- two states, not one;
- a selected accessible algebra or channel;
- a direction of comparison in relative entropy; and
- a regulator or algebraic prescription in continuum theories.

It is therefore not a context-free inventory of ontological bits.

## A conditional expectation gives an intrinsic remainder

The general data-processing deficit is only a difference. A stronger theorem is available in the finite tracial representation, where a trace-preserving conditional expectation \(E:\mathcal M\to\mathcal N\) is identified with its trace adjoint on density matrices and the faithful comparison density \(\varphi\) lies in \(\mathcal N\). Then

$$
\boxed{
D_{\mathcal M}(\rho\Vert\varphi)
=D_{\mathcal M}(\rho\Vert E\rho)
+D_{\mathcal N}(E\rho\Vert\varphi).}
$$

The remainder now has its own intrinsic expression,

$$
D(\rho\Vert E\rho)
=S(E\rho)-S(\rho),
$$

and its coincidence Hessian is the BKM norm of \((1-E)X\). [[spectral-wall-descent/conditional-expectation-balance|The conditional-expectation balance]] proves the split and states why a continuum version requires modular admissibility. This is more than a deficit introduced by subtraction, but it is still not a conserved substance.

## Why the displayed sum is not yet conservation

The equation

$$
D_{\mathcal M}
=D_{\mathcal D}+\Delta
$$

is exact in general because \(\Delta\) was defined as the difference. Outside the conditional-expectation case it does not exhibit an intrinsic wall object. Even inside that case, the term \(D(\rho\Vert E\rho)\) measures noninvertible loss relative to a context; it need not be stored in a complementary physical subsystem. A Stinespring dilation is a representation theorem, not evidence that the missing distinction survives ontologically in an environment.

Schematically, one might seek

$$
I(R:OG)
=I(R:O)+I(R:G\mid O),
$$

where \(O\) is an accessible record and \(G\) a constructed complementary sector. The conditional term shows why a naive two-term split can fail: correlations between the accessible and residual sectors may carry irreducible information.

The proposed gravitational step is therefore not

$$
\Delta=\text{gravity}
$$

by renaming. It is an equivariant construction in which a connection, curvature, edge response, or area measure represents the otherwise inaccessible distinction on a spacetime carrier. [[state-geometry-charge-weld]] states that conjecture.

## Restriction is not fact formation

When \(\mathcal D\) is commutative, the restricted state corresponds to a probability measure on \(\operatorname{Spec}(\mathcal D)\). A fact is instead a character, hence a point of that spectrum. Thus

$$
S(\mathcal M)
\longrightarrow
\operatorname{Prob}(\operatorname{Spec}\mathcal D)
$$

does not supply

$$
\chi\in\operatorname{Spec}(\mathcal D).
$$

This is the distinction established in [[sufficient-reason/inq|Sufficing and Necessitating Reason]]. The relative-entropy deficit belongs to observational restriction; a conservation law governing actual pointing requires the additional structure proposed in [[factive-descent-and-records]].

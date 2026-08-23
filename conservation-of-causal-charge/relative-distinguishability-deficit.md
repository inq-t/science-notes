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

In finite dimensions this is the usual data-processing theorem. For local quantum field theory the corresponding statement belongs to Araki relative entropy on von Neumann algebras, with the necessary support and normality qualifications. [[causal-wall-spectral-theory/information-geometric-weld|The information-geometric weld]] records the continuum obligations.

## Equality and recovery

Under the standard hypotheses, equality in data processing is associated with sufficiency or recoverability: there exists a recovery map that reconstructs the relevant state pair from their restrictions. Strict inequality means that the chosen readout channel has discarded distinctions relevant to that pair.

This makes the deficit more precise than an absolute phrase such as “hidden information.” It depends on

- two states, not one;
- a selected accessible algebra or channel;
- a direction of comparison in relative entropy; and
- a regulator or algebraic prescription in continuum theories.

It is therefore not a context-free inventory of ontological bits.

## Why the displayed sum is not yet conservation

The equation

$$
D_{\mathcal M}
=D_{\mathcal D}+\Delta
$$

is exact because \(\Delta\) was defined as the difference. It does not exhibit a complementary physical subsystem that stores the missing distinguishability. A non-tautological conservation claim would require an enlarged realization—such as a reversible dilation with an observable output and a complementary residual output—and a chain rule that keeps correlations explicit.

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

by renaming. It is an equivariant construction in which a residual channel, connection, curvature, edge charge, or area measure represents the otherwise inaccessible distinction. [[state-geometry-charge-weld]] states that conjecture.

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

This is the distinction established in [[sufficient-reason/entry|Sufficing and Necessitating Reason]]. The relative-entropy deficit belongs to observational restriction; a conservation law governing actual pointing requires the additional structure proposed in [[factive-descent-and-records]].

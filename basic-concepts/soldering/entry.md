# Soldering

In its standard differential-geometric sense, soldering is the equivariant identification that makes an internal model vector space serve as the tangent space of a manifold. The canonical solder form on a frame bundle says not merely how frames transform, but what those frames are frames *of*. Algebraic geometry expresses the same structure through frame torsors, tautological forms, reductions of structure group, and isomorphisms of associated bundles; broader uses of “soldering” for maps between physical registers should be marked as extensions of this precise meaning.

## The canonical form on a frame bundle

Let $M$ be a smooth $n$-manifold and let $V$ be an $n$-dimensional vector space. A point of the frame bundle

$$
\pi:F(M)\longrightarrow M
$$

over $x\in M$ is an isomorphism

$$
u:V\overset{\sim}{\longrightarrow}T_xM.
$$

The group $\operatorname{GL}(V)$ acts on the right by

$$
u\cdot g=u\circ g.
$$

Thus each [[basic-concepts/fibers/entry|fiber]] of $F(M)$ is a $\operatorname{GL}(V)$-[[basic-concepts/torsors/entry|torsor]]: it contains every frame but no preferred frame.

The **solder form**, also called the tautological or canonical form, is the $V$-valued one-form

$$
\theta\in\Omega^1(F(M);V)
$$

defined at a frame $u$ by

$$
\boxed{
\theta_u(\xi)=u^{-1}\bigl(d\pi_u(\xi)\bigr).
}
$$

A tangent vector $\xi$ to the frame bundle projects to an actual displacement $d\pi_u(\xi)\in T_xM$; the frame $u$ then writes that displacement in the model space $V$. This is the meaning of soldering: the abstract vector space carried by the structure group is attached pointwise to the tangent geometry of the base.

The form has three defining features:

1. It annihilates vertical vectors, because changing a frame at fixed $x$ produces no displacement in $M$.
2. It is equivariant:

   $$
   R_g^*\theta=g^{-1}\theta.
   $$

3. It induces an isomorphism

   $$
   T_uF(M)/\ker(d\pi_u)
   \overset{\sim}{\longrightarrow}V.
   $$

Equivalently, it realizes the canonical associated-bundle isomorphism

$$
F(M)\times^{\operatorname{GL}(V)}V
\overset{\sim}{\longrightarrow}TM,
\qquad
[u,v]\longmapsto u(v).
$$

The frame bundle does not need a global section for $\theta$ to exist. For example, $S^2$ has no global frame, but its frame bundle still carries the global canonical solder form. Local frames pull that form back to local coframes, and transition functions relate them on overlaps.

## Solder form versus connection

A solder form and a principal connection answer different questions.

- A solder form says how the internal model $V$ represents tangent displacements of the base.
- A connection says how to compare internal frames over different base points by specifying horizontal transport.

Their behavior on vertical directions is complementary. The solder form kills vertical vectors. A connection form

$$
\omega\in\Omega^1(P;\mathfrak h)
$$

reproduces the Lie-algebra generator on a vertical fundamental vector. A principal bundle can carry connections without being identified with the tangent frame bundle, and the canonical solder form on $F(M)$ exists before a connection is chosen.

Given both $\theta$ and $\omega$, one can form torsion,

$$
T=d\theta+\omega\wedge\theta,
$$

with the representation understood. Neither vanishing torsion nor metric compatibility follows from soldering alone.

## General soldering data

Let $P\to M$ be a principal $H$-bundle and let

$$
\rho:H\longrightarrow\operatorname{GL}(V)
$$

be an $n$-dimensional representation. A solder form on $P$ is a horizontal, equivariant form

$$
e\in\Omega^1(P;V),
\qquad
R_h^*e=\rho(h)^{-1}e,
$$

whose induced bundle map is an isomorphism

$$
\bar e:TM\overset{\sim}{\longrightarrow}P\times^H V.
$$

On an arbitrary principal bundle this is additional structure. It can fail to exist even when $P$ itself exists. If $H\subseteq\operatorname{GL}(V)$ and the data are suitably faithful, such an isomorphism identifies $P$ with an $H$-reduction of the frame geometry of $TM$.

This definition isolates two requirements that loose talk about “connecting two spaces” often misses:

- **equivariance**, so the identification does not depend on a chosen frame; and
- **nondegeneracy**, so every tangent direction corresponds to exactly one internal direction.

If the map has unequal ranks or drops rank, it may still be a meaningful bundle morphism, but it is not a solder form in this strong sense.

## Vielbeins and tetrads

Choose a local section of $P$. The solder form becomes a $V$-valued coframe on an open set $U\subseteq M$,

$$
e=e^a\mathbf e_a,
\qquad
e^a=e^a{}_{\mu}\,dx^\mu,
\qquad
\det(e^a{}_{\mu})\neq0.
$$

In dimension four with $V\simeq\mathbb R^{1,3}$, this is a **tetrad**; in general dimension it is a **vielbein**. If $V$ carries an $H$-invariant nondegenerate bilinear form $\eta$, soldering pulls it back to a metric on spacetime:

$$
g(v,w)=\eta\bigl(\bar e(v),\bar e(w)\bigr),
$$

or locally

$$
g_{\mu\nu}
=\eta_{ab}e^a{}_{\mu}e^b{}_{\nu}.
$$

A change of local frame transforms $e$ by the inverse $H$-representation and leaves $g$ invariant. A degenerate tetrad can still be written as a matrix of one-forms, but it no longer solders $TM$ to the internal bundle and its pullback metric is degenerate.

On an orthonormal frame bundle, the solder form is the restriction of the canonical form on $F(M)$. A spin structure obtained by lifting that frame bundle already makes its associated vector bundle canonically isomorphic to $TM$; in formulations that begin instead with an abstract spin bundle, a tetrad supplies this isomorphism. This is what permits spinorial internal data and spacetime tensor data to interact without identifying spinors themselves with tangent vectors.

In Cartan geometry, a Cartan connection contains a component valued in the model tangent space $\mathfrak g/\mathfrak h$. Under the appropriate hypotheses, that component is a solder form. This is a richer construction, but the same core act remains: identify infinitesimal directions of the base with the translational directions of a homogeneous model.

## The algebraic-geometric form

Let $X\to S$ be smooth of relative dimension $n$. Its relative tangent sheaf $T_{X/S}$ is locally free, and its frame scheme

$$
P=\operatorname{Fr}(T_{X/S})
=\operatorname{Isom}_X(\mathcal O_X^n,T_{X/S})
$$

is a $\operatorname{GL}_n$-torsor. Over $P$ there is a universal frame

$$
u:\mathcal O_P^n\overset{\sim}{\longrightarrow}\pi^*T_{X/S}.
$$

Composing the differential of the projection with the inverse universal frame gives the algebraic tautological form

$$
T_{P/S}
\xrightarrow{d\pi}
\pi^*T_{X/S}
\xrightarrow{u^{-1}}
\mathcal O_P^n.
$$

It vanishes on $T_{P/X}$ and is $\operatorname{GL}_n$-equivariant. Dually, one may express it using Kähler differentials and the universal coframe.

More generally, if $P\to X$ is an $H$-torsor and $V$ an $H$-representation, algebraic soldering data are an isomorphism

$$
T_{X/S}\overset{\sim}{\longrightarrow}P\times^H V.
$$

After pullback to $P$, this becomes an equivariant identification of $\pi^*T_{X/S}$ with the trivial bundle $\mathcal O_P\otimes V$. Local matrices for the identification must transform compatibly on overlaps; [[basic-concepts/gluing/entry|gluing]] constructs the bundle from those matrices, while [[basic-concepts/descent/entry|descent]] expresses why the equivariant local maps determine a global map.

Algebraic geometers do not use *soldering* as a universal umbrella term for all such constructions. Depending on context, the standard language is **frame bundle**, **tautological form**, **$G$-structure**, **reduction of structure group**, or **isomorphism of associated bundles**. Using those terms makes the precise object easier to recognize.

Smoothness matters. On a singular scheme, $T_{X/S}$ need not be locally free, so an ordinary frame torsor and nondegenerate solder form may not exist. A construction using the cotangent complex or a perfect complex can generalize the idea, but it is new data and should not be presented as the classical solder form without qualification.

## What soldering can obstruct

An abstract internal bundle $E=P\times^H V$ is not automatically tangent geometry. An isomorphism

$$
TM\simeq E
$$

requires at least equal rank and compatible global topology. In smooth geometry their characteristic classes must agree; in algebraic geometry their Chern-class and related invariants must agree. Failure of such equalities obstructs soldering even if both bundles separately exist.

Several distinct failures should be kept apart:

- **rank failure:** source and target have different dimensions;
- **degeneracy:** a proposed vielbein loses rank on some locus;
- **equivariance failure:** local formulas change incompatibly under a change of frame and therefore do not descend;
- **topological failure:** the associated bundle is not isomorphic to the tangent bundle;
- **compatibility failure:** the map exists, but does not preserve the metric, orientation, symplectic form, grading, or other structure claimed for it;
- **dynamical failure:** a map can be posited kinematically without being selected or generated by the field equations.

A Higgs field, a connection, a conversion factor, and a bundle homomorphism can each relate structures, but none is a solder form merely by doing so. The source, target, symmetry action, covariance law, and required degree of invertibility must be stated.

## Extended use in this project

The project uses *soldering* more broadly for explicit maps between ontologically distinct registers. This vocabulary is useful precisely when it enforces the [[cosmodynamics/registers-and-type-discipline|type discipline of the registers]], but the broader maps should not be confused with the canonical form on a tangent frame bundle.

### Scale and state

In [[causal-scale-master/scale-soldering|Connes-cocycle scale soldering]], a multiplicative scale ratio $r$ is related to an additive modular parameter by

$$
\theta(r)=-\varrho_\perp\ln r.
$$

Under the stated ratio, rank-one, cocycle, and measurability assumptions, the logarithmic form follows from a homomorphism equation. The slope $\varrho_\perp$ does not: setting it to one is a physical representation choice. This is soldering in the extended sense of an equivariant or compositional bridge between scale and state registers. It is not the differential-geometric tautological form, and it does not by itself identify either register with $TM$.

### Dimensionful constants

[[cosmodynamics/soldering-constants|Constants as soldering structures]] treats $c$, $\hbar$, $G$, and $k_B$ as conversions between independently typed physical quantities—for example,

$$
\text{phase}=\frac{S}{\hbar},
\qquad
S_{\mathrm{therm}}=k_Bs.
$$

This use captures a genuine relational function: quantities from different registers become mutually expressible. But multiplication by a dimensionful scalar is not normally a solder form. Its numerical value depends on units, and naming the conversion does not derive the constant or prove that the linked registers share one underlying origin.

### Proposed kernel identifications

The [[causal-wall-spectral-theory/information-geometric-weld|information-geometric weld]] proposes a chain from a state-space Hessian to a cosmological precision kernel. Here the relevant question is even stronger than whether two expressions have matching dimensions: the construction must supply a common domain, the intervening maps, their covariance and analytic continuation, and the claimed positivity and invertibility. Until those arrows are built, *weld* or *soldering* names a research obligation rather than an achieved identification.

## A test for future uses

Whenever two structures are said to be soldered, ask:

1. What are the independently defined source and target objects?
2. What map relates them, and on what base does it live?
3. Which group acts on each side, and is the map equivariant?
4. Is the map an isomorphism, an injection, a pairing, a conversion, or only an analogy?
5. What local data glue it, and what guarantees global descent?
6. Which structures must it preserve?
7. Is it canonical, freely chosen, empirically calibrated, conditionally derived, or dynamically forced?

In the strict case, soldering turns internal coordinates into the coordinates of actual infinitesimal displacement. In the extended case, these questions preserve that standard’s essential lesson: a bridge between types is explanatory only when the bridge itself is a defined and controlled mathematical object.

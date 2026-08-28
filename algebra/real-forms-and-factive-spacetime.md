# Real Forms and Factive Spacetime

An atemporal complex threefold is already a six-real-dimensional mathematical reality. If it carries a suitable antiholomorphic involution, its smooth fixed locus is exactly three-real-dimensional; a separate realization functor can then send fact-producing processes to time-oriented Lorentzian histories whose objects are those spatial three-manifolds and whose arrows are four-dimensional spacetimes. This gives a rigorous candidate meaning to “six gives rise to \(3+1\)”: the three is obtained by real-form descent, while the one is the orientation of composable factual history, not a seventh coordinate or a subtraction of dimensions.

## Reality does not begin after realization

The source and target of the proposed construction are both mathematical and, on the programme's ontological reading, equally real. The distinction is not

$$
\text{mathematical model}
\longrightarrow
\text{nonmathematical reality}.
$$

It is a typed relation between two mathematical regimes,

$$
\text{atemporal internal structure}
\longrightarrow
\text{factive Lorentzian presentation}.
$$

A presentation need not be an illusion or approximation. It can be the way one structure is realized by a functor in another category. What requires proof is not that the target is “more real,” but that the proposed functor exists, preserves the claimed invariants, forgets only declared distinctions, and returns the observed causal and dimensional structure.

## Exact fixed-locus theorem

Let \(X\) be a complex manifold of complex dimension \(n\), and let

$$
\tau:X\longrightarrow X
$$

be an antiholomorphic involution. Suppose its fixed locus

$$
X^\tau:=\{x\in X:\tau(x)=x\}
$$

is nonempty. Then every connected component of \(X^\tau\) is a smooth real \(n\)-dimensional submanifold of \(X\), and it is totally real.

At a fixed point \(x\), the derivative \(D\tau_x\) is a conjugate-linear involution of the complex vector space \(T_xX\). Its fixed subspace is a real vector space \(V_x\) satisfying

$$
T_xX
\simeq
V_x\otimes_{\mathbb R}\mathbb C,
\qquad
\dim_{\mathbb R}V_x=n.
$$

Local coordinates equivariant with respect to the involution identify the fixed set with the real coordinate plane. Hence, for a complex threefold,

$$
\boxed{
\dim_{\mathbb R}X=6,
\qquad
\dim_{\mathbb R}X^\tau=3.}
$$

This is the first exact algebraic-geometric mechanism in the present programme that can turn a six-real-dimensional carrier into a three-real-dimensional candidate spatial carrier without compactifying three ordinary spatial coordinates or calling half the dimensions unphysical. It is still conditional on the additional datum \(\tau\). A complex threefold by itself does not select a real form, and its fixed locus may be empty, disconnected, nonorientable, or topologically unsuitable for physical space.

This construction is ordinary Galois descent from \(\mathbb C\) to \(\mathbb R\) in geometric form. [[basic-concepts/descent/inq|The descent module]] owns the general rule that the complex object alone does not determine its real form: the semilinear comparison datum is essential.

## Three-space as object, spacetime as process

The fixed-locus theorem supplies three real dimensions, not time. The proposed fourth dimension has a different categorical origin.

Let \(\mathsf P_{\mathrm{fact}}\) be a category of physically admissible fact-producing processes after presentation equivalences have been identified, and let

$$
\mathcal R:
\mathsf P_{\mathrm{fact}}
\longrightarrow
\mathsf{Rec}
$$

be a persistent record functor as in [[algebra/local-global-individuation|local--global individuation]]. Define a target category \(\mathsf{LorHist}_3\) whose objects are suitably decorated real three-manifolds carrying spatial or Cauchy data and whose forward arrows are time-oriented four-dimensional Lorentzian histories or cobordisms between them. The decisive realization would be a functor

$$
\boxed{
\mathfrak L:
\mathsf P_{\mathrm{fact}}
\longrightarrow
\mathsf{LorHist}_3.}
$$

It must satisfy at least:

1. presentation equivalences are sent to isomorphisms of the realized data;
2. proper record extension is sent to forward-oriented causal composition;
3. composition of factive processes agrees with gluing of Lorentzian histories;
4. the realized three-manifolds are Cauchy carriers in the stated regime; and
5. the returned metric, signature, cones, fields, constraints, and boundary data are derived without using their measured values as construction input.

On this formulation, space and spacetime occupy different categorical levels:

$$
\boxed{
\text{three-dimensional space is an object},
\qquad
\text{four-dimensional spacetime is a history arrow}.}
$$

The temporal “one” is therefore not one of the six internal real coordinates. It is the oriented compositional dimension by which spatial presentations become stages of one factual history. This agrees with the record-order criterion while leaving metric proper time to a later soldering theorem.

## Atemporal spectral selection

A functional on internal spectral data can be fundamental without being a time-evolution law. For example, a spectral functional of the schematic form

$$
S_{\mathrm{int}}(D)
=\operatorname{Tr}f(D/\Lambda)
$$

may select or weight objects in an internal configuration groupoid. Extremization is then a relation on a moduli problem, not motion through an already existing time coordinate. In that precise sense a spectral principle can be atemporal.

This possibility must be separated from two different claims. If \(D\) already contains a Dirac operator on a four-dimensional manifold, the Lorentzian or Euclidean spacetime carrier has been imported. If the functional is the downstream observable spectral action studied in [[spectral-wall-descent/observable-spectral-action|the observable spectral-action note]], it governs an already realized geometry and cannot also be cited as the operation that created that realization. An upstream internal selector requires its own domain, equivalences, existence theorem, and relation to \(\mathfrak L\).

## The two real structures must not be conflated

An antiholomorphic involution \(\tau\) on a complex threefold and the antiunitary real-structure operator \(J\) of a real spectral triple are not the same type of object:

$$
\tau:X\to X,
\qquad
J:\mathcal H\to\mathcal H.
$$

The first can define a real fixed locus in a complex manifold. The second supplies KO-sign relations with \(D\) and \(\gamma\). A bridge between them would require a represented function algebra, compatibility of \(J\) with complex conjugation on that algebra, and a reconstruction theorem. [[ko-dimension-as-morita-class/inq|KO-dimension six]] is mod-eight operator data, not six metric coordinates.

Likewise, the conditional complex-threefold claim in [[algebra/s6-manuscript-branch|the \(S^6\) manuscript branch]] does not provide an antiholomorphic involution with a physical three-dimensional fixed locus. Even if that complex structure exists, the datum \(\tau\), the topology of \(X^\tau\), and the functor \(\mathfrak L\) remain separate construction gates.

## Consequences for CST and CWST

The theorem changes the audit of the causal programmes without completing them.

- For CWST W2, \(X^\tau\) is a mathematically exact candidate for a three-dimensional carrier. It does not provide the BKM-to-spatial response transform, measure conversion, positivity, or probability-1PI kernel.
- For CWST W3, \(\mathsf{LorHist}_3\) gives the correct return type for the wall-to-curvature map. It does not construct the gauge-reduced scalar phase space, symplectic normalization, or Lorentzian state.
- For CST, the functor \(\mathfrak L\) could make a scale-indexed internal process appear as a homogeneous Lorentzian history. It does not derive the CST source, temperature, stress tensor, or acceleration law.
- For both, a three-dimensional real fixed locus does not select three large approximately homogeneous spatial dimensions unless its metric, topology, scale, and observable net have the required properties.

The exact result is therefore substantial but sharply bounded:

$$
\boxed{
\text{complex dimension three}
+\text{selected real structure}
\Longrightarrow
\text{real dimension three};}
$$

$$
\boxed{
\text{real three-space}
+\text{factive Lorentzian history functor}
\Longrightarrow
\text{candidate }3+1\text{ realization}.}
$$

Only the first implication is presently a theorem. The second is the central construction target.

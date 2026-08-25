# Center-Valued Response and Scalarization

A response resolved over central sectors is more informative than either a sector average or one selected sector. The canonical pre-consumer datum therefore retains the center, its positive response density, and the normal central law inherited from the whole state; this is W1 in the CWST ledger. This note owns the classical Fisher term produced by varying sector weights and the exact distinction among unconditioned averaging, sectorwise reasoning, and factive selection.

## Why the center must be retained

Let a transported family of descended contexts have finite center

$$
Z(\mathcal M_\lambda)
=
\bigoplus_\alpha\mathbb CP_\alpha,
$$

with the central projections coherently identified over the parameter neighborhood. A faithful whole state \(\varphi_\lambda\) supplies, rather than merely permits, a normal probability law on this center:

Here \(\mathcal M_\lambda\) denotes the carrier algebra on which \(\varphi_\lambda\) is defined. If \(\varphi_\lambda=\omega_\lambda\circ j_\lambda\) for a readout \(j_\lambda:\mathcal B_\lambda\to\mathcal A_\lambda\), then \(\mathcal M_\lambda=\mathcal B_\lambda\); replacing its center by \(Z(\mathcal A_\lambda)\) requires a separately constructed center-preserving identification.

$$
q_\alpha(\lambda)
:=\varphi_\lambda(P_\alpha)>0,
\qquad
\sum_\alpha q_\alpha=1.
$$

Its normalized conditional sector states are

$$
\varphi_{\lambda,\alpha}(a)
:=
\frac{\varphi_\lambda(P_\alpha aP_\alpha)}{q_\alpha}.
$$

For two faithful block-diagonal states on the same transported center, relative entropy has the exact classical--quantum decomposition

$$
D(\varphi\Vert\psi)
=
D_{\mathrm{KL}}(q\Vert r)
+\sum_\alpha q_\alpha
D(\varphi_\alpha\Vert\psi_\alpha).
$$

Write the internal sector metric as

$$
G^{(\alpha),\mathrm{int}}_{IJ}
:=
g^{\mathrm{BKM}}_{\varphi_\alpha}
(\dot\varphi_{I,\alpha},\dot\varphi_{J,\alpha}).
$$

The coincidence Hessian is therefore

$$
\boxed{
G_{IJ}^{\mathrm{whole}}
=
I^{\mathrm F}_{IJ}[q]
+\sum_\alpha q_\alpha
G^{(\alpha),\mathrm{int}}_{IJ}.}
$$

The first term measures variation of the central law. It is not optional when the \(q_\alpha\) vary, and it becomes a response of records only if the central labels have separately been realized as record values.

## The center-valued response density

The internal response density of the normalized conditional states is

$$
\mathbf G^{Z,\mathrm{int}}_{IJ}
:=
\sum_\alpha
G^{(\alpha),\mathrm{int}}_{IJ}P_\alpha.
$$

The corresponding center-valued Fisher density is

$$
\mathbf F^Z_{IJ}
:=
\sum_\alpha
(\partial_I\log q_\alpha)
(\partial_J\log q_\alpha)P_\alpha.
$$

The full sector-resolved response is

$$
\boxed{
\mathbf G^Z_{IJ}
:=
\mathbf F^Z_{IJ}
+\mathbf G^{Z,\mathrm{int}}_{IJ}}
\in
Z(\mathcal M_\lambda)\otimes
\operatorname{Sym}^2(T^*\mathfrak D_{\mathrm{phys}}).
$$

It is positive in central order because, for every real tangent vector \(v\),

$$
v^Iv^J\mathbf G^Z_{IJ}
=
\sum_\alpha
\left[
(\partial_v\log q_\alpha)^2
+G^{(\alpha),\mathrm{int}}(v,v)
\right]P_\alpha
\geq0.
$$

If the weights are fixed, \(\mathbf F^Z=0\). Calling \(\mathbf G^{Z,\mathrm{int}}\) the full joint response without this qualification would discard a genuine response direction.

## The retained pre-consumer package

Before a consumer changes carrier or representation, retain

$$
\boxed{
\mathfrak G^Z_\lambda
:=
\left(
Z(\mathcal M_\lambda),
\mathbf G^Z,
\omega^Z_\lambda
\right),
\qquad
\omega^Z_\lambda
:=\varphi_\lambda\!\restriction_{Z(\mathcal M_\lambda)},
\qquad
\omega^Z_\lambda(P_\alpha)=q_\alpha.}
$$

Normal evaluation by the law inherited from the whole state recovers the scalar BKM response:

$$
\boxed{
G^{\omega^Z}_{IJ}
:=\omega^Z_\lambda(\mathbf G^Z_{IJ})
=I^{\mathrm F}_{IJ}[q]
+\sum_\alpha q_\alpha G^{(\alpha),\mathrm{int}}_{IJ}.}
$$

An alternative normal central state is additional member data, not a normalization convention.

## Four different evaluation policies

1. **Trivial center.** If \(Z(\mathcal M_\lambda)=\mathbb C\mathbf1\), the scalar return is unique.
2. **Normal unconditioned evaluation.** Applying \(\omega^Z_\lambda=\varphi_\lambda|_Z\) averages sectors with the law already carried by the whole state. It does not select a fact.
3. **Sectorwise conditional theorem.** One may normalize inside sector \(\alpha\) and prove a statement about \(G^{(\alpha),\mathrm{int}}\). Conditioning the theorem on a sector does not assert that this sector has become actual.
4. **Character and factive outcome.** Algebraically evaluating the joint density gives

   $$
   \operatorname{ev}_\beta(\mathbf G^Z_{IJ})
   =
   (\partial_I\log q_\beta)(\partial_J\log q_\beta)
   +G^{(\beta),\mathrm{int}}_{IJ},
   $$

   which is not the normalized conditional metric in item 3 when the central law varies. A character represents an actual sector only when a declared instrument returns \(\beta\) as an outcome and compatible records support that interpretation; the post-outcome response must then be calculated from the instrument's conditional state. A bare character is neither conditionalization nor a fact. [[conservation-of-causal-charge/factive-descent-and-records|Factive descent and records]] owns the stronger construction.

For a diffuse center, the sums become direct integrals. Point characters may then be nonnormal and cannot be inserted into the von Neumann-state construction as normal states. Any consumer must also state whether localization or another carrier-changing map acts center-linearly before evaluation or acts on a declared scalar or sectorwise input afterward; these orders are not equal by notation alone.

## Ownership boundary

[[program-core/common-response-form|The common response form]] owns how the homogeneous, mean-zero observational, mixed, and hidden blocks belong to one response geometry. This note owns only their central resolution and evaluation. CST and CWST may choose an evaluation policy, but they must link here rather than reconstructing the Fisher decomposition or treating an unannounced character as a physical outcome.

The primary operator-algebraic sources for relative-entropy Hessians and BKM geometry are maintained in [[hessian-response-geometry/sources|the Hessian-response source ledger]]. The finite direct-sum formula above follows directly by applying the functional calculus block by block; its use for a continuum center still requires a declared direct-integral measure and regularity hypotheses.

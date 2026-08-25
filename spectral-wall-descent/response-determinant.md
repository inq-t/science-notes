# Response and Determinant from One Hidden Operator

For a positive hidden Gaussian block, the same background-dependent operator can produce two distinct descendants: its Schur complement changes the retained common response, while its determinant contributes a central observable effective action. The negative log determinant generates the positive classical Gaussian Fisher metric, whereas bosonic elimination contributes the opposite sign. This supplies an exact finite-dimensional bridge between response geometry and downstream action without making the principle of least action fundamental upstream or pretending that the determinant's absolute normalization is fixed.

## The two outputs of elimination

Let \(\bar x\) denote a retained background, \(x\) its real fluctuation coordinates, and \(h\) real hidden coordinates. At each \(\bar x\), take a real symmetric quadratic operator

$$
\mathcal K[\bar x]
=
\begin{pmatrix}
G[\bar x]&B[\bar x]\\
B[\bar x]^T&L[\bar x]
\end{pmatrix},
\qquad
L[\bar x]>0.
$$

Stationary elimination gives the Schur complement already used in [[spectral-wall-descent/hidden-resolvent-and-seesaw|the hidden-resolvent construction]]:

$$
G_{\mathrm{eff}}[\bar x]
=G[\bar x]-B[\bar x]L[\bar x]^{-1}B[\bar x]^T.
$$

The exact determinant identity is

$$
\boxed{
\det\mathcal K[\bar x]
=\det L[\bar x]\,
\det G_{\mathrm{eff}}[\bar x].}
$$

In the real Euclidean bosonic convention, Gaussian integration over \(h\) therefore returns, pointwise in the background,

$$
\boxed{
\Gamma_{\mathrm{eff}}(x;\bar x)
=\frac12x^TG_{\mathrm{eff}}[\bar x]x
+\frac12\log\det(L[\bar x]/\mu^2)
+\text{constant},}
$$

For a constant finite matrix \(L\), the determinant is only an additive normalization and has no \(x\)-dependent dynamics. It becomes an effective action only when \(L\) depends on a background field or geometry. A complex boson gives a different determinant power, while fermionic and Majorana integrations produce determinant or Pfaffian factors with different signs and halves.

The two descendants have different roles:

- \(-BL^{-1}B^T\) is a noncentral correction to retained precision or response;
- \(\tfrac12\log\det L[\bar x]\) is a scalar effective-action contribution whose regulated local expansion can contain cosmological, Einstein, and higher-curvature terms.

The cosmological part is not contained in the Schur correction. This is one algebraic reason that a trace-free or normalized response can determine a pulse while leaving a central residual undetermined.

## The same determinant generates positive response

Consider the centered real Gaussian family

$$
p_L(h)
=\frac{(\det L)^{1/2}}{(2\pi)^{n/2}}
\exp\left(-\frac12h^TLh\right),
\qquad
L>0.
$$

Its log partition function is

$$
\Psi(L)
=-\frac12\log\det L
+\text{constant}.
$$

For affine matrix directions \(A_I=\partial_IL\),

$$
\partial_I\partial_J\Psi
=\frac12
\operatorname{Tr}
\left(
L^{-1}A_I
L^{-1}A_J
\right).
$$

Hence

$$
\boxed{
g_{IJ}^{\mathrm F}
=g_{IJ}^{\mathrm{BKM,comm}}
=\frac12
\operatorname{Tr}
\left(
L^{-1}\partial_IL
L^{-1}\partial_JL
\right).}
$$

This equality is exact for the classical Gaussian statistical family: classical Fisher is the commutative BKM metric. It is not the general BKM metric of noncommuting quantum Gaussian density operators.

The sign is important. In affine directions,

$$
\operatorname{Hess}\!\left(-\frac12\log\det L\right)
=g^{\mathrm F},
$$

whereas the real bosonic effective-action term obeys

$$
\operatorname{Hess}\!\left(+\frac12\log\det L\right)
=-g^{\mathrm F}.
$$

Thus the same determinant datum supports a positive state geometry and a downstream action, but the action term itself does not have the positive Fisher Hessian. The correctly signed relation is

$$
\boxed{
g^{\mathrm F}
=-\operatorname{Hess}\Gamma_{\det}^{\mathrm{bos}},
\qquad
\Gamma_{\det}^{\mathrm{bos}}
=+\frac12\log\det L[\bar x].}
$$

The arrow to an observable action is a consumer map. Least action may govern the resulting fields without being the principle that first selected \(L\), the wall, or the state family.

## Spectral regularization and the normalization problem

For a background-dependent elliptic operator \(L[\bar x,g,\ldots]\), one may represent the determinant through a heat trace or zeta function. Schematically,

$$
\log\det(L/\mu^2)
=-\left.\frac{\mathrm d}{\mathrm ds}\right|_{s=0}
\operatorname{Tr}(L/\mu^2)^{-s}.
$$

Its regulated heat-kernel expansion produces local terms organized by Seeley--DeWitt coefficients. An Einstein coefficient can therefore descend from the same hidden operator that supplies the common response form, conditional on the field content, regulator, gauge quotient, and background dependence actually agreeing.

This does not yet derive \(G\):

- the scale \(\mu\), cutoff prescription, and local counterterms affect the absolute determinant;
- bosonic and fermionic determinants carry different powers and signs;
- gauge zero modes and ghosts require a physical quotient;
- Lorentzian continuation and causal boundary conditions must be supplied; and
- the coefficient must agree with the independent central area-density weld.

The determinant bridge is consequently stronger than a verbal analogy but weaker than a numerical prediction.

## Relation to the singlet

If an actual background-dependent \(L=L_\sigma\) is derived as the positive fluctuation operator of a central or gauge-singlet normal mode, then one hidden ingredient could simultaneously

1. repair a rank-one mismatch in the retained common response through its Schur complement;
2. contribute an Einstein and cosmological coefficient through its determinant; and
3. retain a central normalization invisible to normalized-state BKM comparisons.

[[program-core/singlet-response-completion|The singlet response-completion test]] states exactly when one positive scalar can repair the response matrix. [[spectral-wall-descent/majorana-square-and-cosmic-pulse|The Majorana square and cosmic pulse]] exhibits the separate positive square and central residual in the observable spectral action.

## Failure conditions

- If \(L\) is not positive on the physical Euclidean sector, the classical Gaussian Fisher metric and stable elimination do not exist as written.
- If the hidden state is non-Gaussian, the determinant does not contain the full effective action or response.
- If the response and determinant use independently chosen operators or regulators, the claimed common source has disappeared.
- Equality of finite classical Gaussian Hessians does not prove a quantum BKM identity, covariance, locality, or universality in the continuum wall theory.
- A central determinant term is not an actual fact or record and cannot provide ontological time.

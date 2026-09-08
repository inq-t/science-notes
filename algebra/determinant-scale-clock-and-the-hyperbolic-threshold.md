# The Determinant-Scale Clock and the Hyperbolic Threshold

The positive complex corner's determinant separates scale from shape and yields a static Lorentzian product \(\mathbb R\times\mathbb H^3\). Its hyperbolic spatial Laplacian has a positive lower edge, but the massless field returned from the flat determinant metric contains a correction that cancels that edge exactly. The same arena therefore supports distinct clock equations; choosing a geometrical threshold is not yet deriving mass. This explicit test narrows the missing action-selection law.

## Scale and shape are derived coordinates

Use [[algebra/positive-cone-processes-and-the-complex-corner|the complex positive cone]] \(X_{++}=\mathfrak h_2(\mathbb C)_{++}\), with
\[
\mathcal F(u)=-\tfrac12\log\det u,\qquad
h=D^2\mathcal F,\qquad \theta=-d\mathcal F,\qquad
g=h-2\theta^2.
\tag{DH1}
\]
The Hessian refers to the original matrix-affine connection. Although the potential will become linear in the coordinate below, ordinary second derivatives in that nonlinear coordinate system do not compute \(h\). [[hessian-response-geometry/affine-hessian-structure|Affine Hessian structure]] owns this distinction.

Every \(u>0\) has the unique decomposition
\[
u=e^s v,\qquad s=\tfrac12\log\det u,\qquad
v>0,\quad\det v=1.
\tag{DH2}
\]
Since \(u^{-1}du=I\,ds+v^{-1}dv\) and
\(\operatorname{Tr}(v^{-1}dv)=d\log\det v=0\),
\[
h=ds^2+h_{\rm sh},\qquad
\theta=ds,\qquad
g=-ds^2+h_{\rm sh},
\quad
h_{\rm sh}=\tfrac12\operatorname{Tr}\bigl[(v^{-1}dv)^2\bigr].
\tag{DH3}
\]
Thus one determinant supplies a scale coordinate, a positive scale–shape metric and an opposite-sign metric. Translation in \(s\) is a reversible isometry of this product; a directed ledger may use only its increasing paths. These are different process classes, not conflicting descriptions.

The shape manifold has the parametrization
\[
v=\cosh r\,I+\sinh r\,\mathbf n\cdot\boldsymbol\sigma,
\qquad |\mathbf n|=1,
\]
which gives
\[
h_{\rm sh}=dr^2+\sinh^2r\,d\Omega^2.
\tag{DH4}
\]
It is hyperbolic three-space with curvature \(-1\): the radial and tangential sectional curvatures are
\[
-\frac{(\sinh r)''}{\sinh r}=-1,\qquad
\frac{1-(\cosh r)^2}{\sinh^2r}=-1.
\]
This unit curvature follows from the specified half-log-determinant normalization; it is not a measured inverse length.

Let \(\eta=-D\) be the constant bilinear form obtained by polarizing minus the determinant on \(X\). The corner identity gives
\[
\boxed{\eta=e^{2s}g
=e^{2s}(-ds^2+h_{\mathbb H^3}).}
\tag{DH5}
\]
This chart covers the open future timelike cone in the flat determinant vector space, not all Minkowski space.

## The spatial lower edge is exact

Let \(-\Delta_{\mathbb H^3}\) be the Friedrichs operator of the gradient form initially on \(C_c^\infty(\mathbb H^3)\). In radial coordinates put
\[
z(r,\Omega)=\sinh r\,f(r,\Omega).
\]
Then integration by parts gives
\[
\begin{aligned}
\|f\|^2&=\int|z|^2\,dr\,d\Omega,\\
\int|\nabla f|^2\,dV
&=\int\left(
|z_r|^2+|z|^2+
\frac{|\nabla_\Omega z|^2}{\sinh^2r}
\right)\,dr\,d\Omega.
\end{aligned}
\tag{DH6}
\]
The endpoint term vanishes: compact support handles infinity, while regularity gives \(z=O(r)\) at the origin. Therefore \(-\Delta_{\mathbb H^3}\geq1\).

The lower bound is sharp. For a radial form-domain trial function, let
\[
z_L(r)=
\begin{cases}
\sin\!\bigl(\pi(r-1)/L\bigr),&1\leq r\leq1+L,\\
0,&\text{otherwise},
\end{cases}
\qquad f_L=z_L/\sinh r.
\]
Smooth form approximations have the same limiting quotient, and
\[
\frac{\int|\nabla f_L|^2\,dV}{\|f_L\|^2}
=1+\frac{\pi^2}{L^2}\longrightarrow1.
\tag{DH7}
\]
There is no \(L^2\) eigenvector at the lower edge: equality in (DH6) would require \(z_r=0\), incompatible with a nonzero square-integrable \(z\). The radial restriction is the Dirichlet half-line operator \(-d^2/dr^2+1\). In particular, the shifted nonnegative operator \(-\Delta_{\mathbb H^3}-1\) has bottom zero and arbitrarily soft normalized form directions.

## Which field equation does the scale clock carry?

A minimally coupled massless scalar on the **product metric** \(g\) satisfies
\[
\partial_s^2\psi-\Delta_{\mathbb H^3}\psi=0.
\tag{DH8}
\]
Its positive-frequency generator would be
\[
A_{\min}=\sqrt{-\Delta_{\mathbb H^3}},\qquad
\inf\sigma(A_{\min})=1.
\tag{DH9}
\]
This is a valid candidate field prescription, not a consequence of the determinant alone.

Now instead start with the massless equation on the **flat determinant metric** \(\eta\). With signature \((-+++)\), (DH5) gives directly
\[
\Box_\eta=e^{-2s}
(-\partial_s^2-2\partial_s+\Delta_{\mathbb H^3}).
\tag{DH10}
\]
Set \(\phi=e^{-s}\psi\). Differentiation, without invoking a general conformal theorem, yields
\[
\boxed{
\Box_\eta\phi
=e^{-3s}(-\psi_{ss}+\Delta_{\mathbb H^3}\psi+\psi).}
\tag{DH11}
\]
Thus the same flat massless equation has scale-clock presentation
\[
\psi_{ss}+A_{\rm conf}^2\psi=0,\qquad
A_{\rm conf}^2=-\Delta_{\mathbb H^3}-1,
\qquad
\inf\sigma(A_{\rm conf})=0.
\tag{DH12}
\]
The correction cancels the hyperbolic floor exactly. Omitting it changes the equation; it does not reveal a previously hidden mass in the original one.

Once either positive generator has been selected, [[algebra/wick-real-forms-and-positive-preparation|positive preparation]] supplies its spectral-core kernel and corresponding unitary boundary clock. For the gapless branch, inverse factors are interpreted on the specified domain rather than assumed bounded. This does not choose between the two field equations or provide a preferred quantum vacuum.

A constant flat mass coefficient also illustrates why clock type matters. The equation \((\Box_\eta-m^2)\phi=0\) becomes
\[
\psi_{ss}+
\bigl(-\Delta_{\mathbb H^3}-1+m^2e^{2s}\bigr)\psi=0.
\tag{DH13}
\]
A constant parameter in the flat presentation is a time-dependent coefficient in the determinant-scale presentation.

## The scale clock is not a translation generator

On the ambient determinant vector space,
\[
\partial_s=u^\mu\partial_{u^\mu}.
\tag{DH14}
\]
It generates dilations about the cone vertex, not constant Minkowski translations. It is Killing for \(g\) but only conformal Killing for \(\eta\): \(\mathcal L_{\partial_s}\eta=2\eta\). A spectral statement about its field generator is therefore not automatically a statement about the Poincaré mass Casimir.

This is a concrete example of the [[global-local-response-reconstruction/causal-patch-boundary-and-two-times|different temporal roles]], not a claim that logarithmic clocks are illegitimate. [[misner-log-time/inq|Misner time]] also separates scale from shape in its own gravitational carrier. Equality of the logarithmic grammar does not identify that carrier or its lapse with (DH2).

There is a direct classical Yang–Mills comparison. On a supplied four-dimensional cone patch, the Hodge operator on two-forms is unchanged by \(\eta=e^{2s}g\): the volume contributes \(e^{4s}\), while the two inverse metrics contribute \(e^{-4s}\). Hence, for one connection and one invariant Lie-algebra pairing,
\[
\int\langle F\wedge *_\eta F\rangle
=\int\langle F\wedge *_g F\rangle.
\tag{DH15}
\]
This is conformal covariance of the declared classical action. It neither constructs a quantum measure nor removes its renormalization and continuum obligations. It does show why changing the arena's presentation cannot by itself be treated as inserting a Yang–Mills mass.

## What the test requires of a master object

The determinant has removed an independent choice of scale line relative to a chosen barrier and affine carrier. It has not selected a field action, state or physical normalization. A complete law must decide how its response geometry is realized dynamically and prove that the chosen realization returns the stipulated local theory.

The positive result of [[algebra/qubit-cone-interiorization-and-the-clock-gap|cone interiorization]] concerns a different, explicitly supplied transfer generator on the finite corner. Its exact gap identity must not be transferred to the spatial Laplacians here merely because both use the same cone.

A successful explanation must retain a nonzero physical vacuum edge after these return maps and limits. The cancellation in (DH12) is a useful test: a proposed mass generated solely by this hyperbolic reparametrization fails it. The broader search for a jointly constrained response, clock and interacting field law remains open.

[[directed-analytic-realization/positive_cone_process_receipt.py|The shared receipt]]
compares the original radial gradient integral with (DH7) and its shifted
quotient by numerical quadrature. [[directed-analytic-realization/positive-cone-process-receipt-output.txt|The stored output]]
does not replace the full form argument (DH6) or the exact continuation
calculation (DH11).

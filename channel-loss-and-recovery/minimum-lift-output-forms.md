# Minimum-Lift Output Forms

A surjective contraction between finite-dimensional inner-product spaces induces a least-cost metric on its reachable output. Subtracting the supplied output metric gives a nonnegative output form, while the remaining input loss lies in the channel kernel. Successive output forms compose by constrained minimization rather than direct addition.

## Minimal-lift transgression puts a form on the output

Let $(V,g_V)$ and $(W,g_W)$ be finite-dimensional real inner-product spaces, and let

$$
A:V\longrightarrow W
$$

be a surjective contraction:

$$
g_W(Ax,Ax)\leq g_V(x,x).
$$

For a channel derivative, take $V$ to be the input BKM tangent space and restrict $W$ to the reachable output tangent $\operatorname{im}A$. Define the minimal-lift metric

$$
\boxed{
g_A^\uparrow(y,y)
:=
\inf_{Ax=y}g_V(x,x).}
\tag{D8}
$$

Contraction implies

$$
g_A^\uparrow(y,y)\geq g_W(y,y).
$$

The **output transgression** is therefore

$$
\boxed{
\tau_A(y)
:=
g_A^\uparrow(y,y)-g_W(y,y)
=
\inf_{Ax=y}\ell_A[x]
\geq0,}
\tag{D9}
$$

where $\ell_A[x]:=g_V(x,x)-g_W(Ax,Ax)$. Unlike $\ell_A$, the form $\tau_A$ operates on retained output tangents. It is the least upstream distinction lost among all realizations of the same output change, not the total information forgotten by the fiber. For the derivative of a preserving expectation with its adapted BKM metrics, the recovery section is isometric and [[channel-loss-and-recovery/preserving-expectation-loss#The preserving-expectation Hessian is vertical|(D5h.5)]] gives \(\tau_A\equiv0\). That single adapted expectation cannot supply a positive output form merely through forgetfulness; a modified metric comparison or jointly transverse data would be additional inputs. A general contracting channel can instead have positive output transgression with its ordinary input and output BKM metrics, as the [[channel-loss-and-recovery/binary-channel-witness|binary witness]] shows.

Indeed, let

$$
V=(\ker A)^{\perp_{g_V}}\oplus\ker A
$$

and let $s_A:W\to(\ker A)^{\perp_{g_V}}$ be the unique minimum-norm lift. Every $x\in V$ decomposes as

$$
x=s_A(Ax)+k,
\qquad
k\in\ker A,
$$

and Pythagoras gives the sharper **[EXACT CARRIER SPLIT]**

$$
\boxed{
\ell_A[x]
=
\tau_A(Ax)
+g_V(k,k).}
\tag{D9a}
$$

The first term is the minimum-output shadow of metric contraction. The second is inaccessible vertical residue and remains entirely on the incoming carrier.

In coordinates, let $G_V$ and $G_W$ be the positive metric matrices and let $A$ have full row rank. Lagrange minimization gives

$$
\boxed{
g_A^\uparrow(y,y)
=
y^{\mathsf T}
\left(AG_V^{-1}A^{\mathsf T}\right)^{-1}
y,}
\tag{D10}
$$

The inverse exists because $G_V$ is positive definite and $A$ has full row rank on the reachable output. [[trace-dirichlet-descent/conditional-score-shorting-and-observable-lifts#Singular conditional shorting|Conditional score shorting]] treats a different, covector-valued construction with singular Fisher matrices and explicit range constraints. A bare pseudoinverse does not remove those constraints.

The output form is

$$
\tau_A(y)
=
y^{\mathsf T}
\left[
\left(AG_V^{-1}A^{\mathsf T}\right)^{-1}
-G_W
\right]y.
\tag{D11}
$$

The bracket is positive semidefinite. Relative to $g_W$, it defines a positive semidefinite self-adjoint operator

$$
T_A
=
G_W^{-1}
\left[
\left(AG_V^{-1}A^{\mathsf T}\right)^{-1}
-G_W
\right].
\tag{D12}
$$

The operator is self-adjoint relative to $g_W$; its coordinate matrix need not be symmetric in an independently chosen Euclidean norm. [[hessian-response-geometry/relative-response-spectrum|The relative response spectrum]] states why the denominator metric belongs to the numerical comparison.

## Composition minimizes over the intermediate carrier

For another surjective contraction $B:W\to Z$, minimization by the intermediate value yields the exact dynamic-programming law

$$
g_{BA}^\uparrow(z,z)
=
\inf_{By=z}g_A^\uparrow(y,y),
\tag{D13}
$$

and hence

$$
\boxed{
\tau_{BA}(z)
=
\inf_{By=z}
\left\{
\tau_A(y)
+g_W(y,y)-g_Z(z,z)
\right\}.}
\tag{D14}
$$

The incoming defects add exactly along a chosen lift by [[channel-loss-and-recovery/bkm-loss-operators|(D5)]]; their output transgressions compose by infimizing over the forgotten intermediate carrier. In general $\tau_{BA}$ is not $\tau_A+\tau_B$. This infimal law, rather than ordinary addition, is the appropriate noninvertible analogue of path-cost composition.

[[trace-dirichlet-descent/inq#The missing arrow is an infimal pushforward|Trace Dirichlet descent]] owns the general least-cost pushforward of a nonnegative whole form. Here the input is specifically a metric and $\tau_A$ subtracts a second, supplied output metric. Positivity of this finite quadratic form does not establish a Markov generator, while infinite-dimensional extensions require their own domain and closed-range control.

## Metric contraction and forgotten fibers are distinct

In the BKM application both metrics are dimensionless, so $T_A$ is dimensionless. For arbitrary abstract inner-product spaces that typing is not automatic. The construction is canonical only relative to the supplied channel and two supplied metrics. It does not choose them, fix their normalization, or turn $T_A$ into a Hamiltonian. Two counterexamples fix its interpretation:

- for the Euclidean projection $A(x_1,x_2)=x_1$, the entire $x_2$ fiber is forgotten while $\tau_A=0$; all loss is the vertical term in (D9a);
- for the [[channel-loss-and-recovery/binary-channel-witness|binary channel]] with $0<\lambda<1$, the tangent map is invertible and has no nontrivial fiber, yet $\tau_\lambda(s)>0$ for every $s\ne0$ because its inverse is not a stochastic contraction. The allowed endpoint $\lambda=1$ is the identity channel and has $\tau_1\equiv0$.

Thus $\tau_A$ measures minimum metric distortion of retained directions. It is not fiber multiplicity, branch count, or all forgotten distinction.

---
inq.module: "hessians"
inq.include:
  - "**/*.md"
---
# Hessians

A Hessian is the second-order part of a scalar quantity: it measures how the first-order response changes when the underlying object is varied. In coordinates it is a matrix of second partial derivatives, but that matrix is not automatically an intrinsic tensor away from a critical point. Hessians become especially powerful when further structure turns them into quadratic forms governing stability, information metrics, fluctuation operators, or inverse propagators; those identifications are theorems with hypotheses, not synonyms built into the word *Hessian*.

## The second variation

Let $V$ be a finite-dimensional real vector space, let $U\subseteq V$ be open, and let

$$
f:U\longrightarrow\mathbb R
$$

be twice differentiable. Its first derivative at $p$ is a covector

$$
D f_p\in V^*,
$$

which assigns to a direction $v$ the first-order change of $f$. Its second derivative is a symmetric bilinear form

$$
\boxed{
D^2f_p:V\times V\longrightarrow\mathbb R.
}
$$

It compares two infinitesimal variations. Equivalently, it differentiates the gradient-like object $Df$:

$$
D^2f_p(u,v)
=\left.\frac{\partial^2}{\partial s\,\partial t}
f(p+su+tv)\right|_{s=t=0}.
$$

In affine coordinates $x^1,\ldots,x^n$, the bilinear form is represented by the **Hessian matrix**

$$
H_f(p)=
\left(\frac{\partial^2f}{\partial x^i\partial x^j}(p)\right)_{i,j}.
$$

The equality of mixed partials makes this matrix symmetric under the usual regularity assumptions. The matrix is a representation of the second variation in a chosen basis; it is not the primary object.

Taylor's formula fixes a ubiquitous normalization:

$$
f(p+v)
=f(p)+Df_p(v)
+\frac12D^2f_p(v,v)
+O(\lVert v\rVert^3).
$$

The factor $1/2$ belongs to the quadratic Taylor term. It is not part of the definition of $D^2f_p$. Some authors instead call $\tfrac12D^2f_p(v,v)$ the quadratic form; formulas should be checked before factors are compared.

The simplest meaning is visible in one dimension. For $f(x)=x^2$, the first derivative vanishes at $0$, while $f''(0)=2$ records the positive quadratic cost of moving away from $0$. For $f(x)=-x^2$ the cost has the opposite sign. For $f(x)=x^4$, the Hessian vanishes at the minimum, so the second-order approximation is silent even though the point is stable. A Hessian detects quadratic behavior, not every form of behavior.

## Why a coordinate Hessian is not always a tensor

Let $x^i=x^i(y)$ be a nonlinear change of coordinates. The chain rule gives

$$
\frac{\partial^2 f}{\partial y^a\partial y^b}
=
\frac{\partial x^i}{\partial y^a}
\frac{\partial x^j}{\partial y^b}
\frac{\partial^2f}{\partial x^i\partial x^j}
+
\frac{\partial^2x^i}{\partial y^a\partial y^b}
\frac{\partial f}{\partial x^i}.
$$

The second term is not part of the tensorial transformation law. Thus the bare array $(\partial_i\partial_jf)$ depends on the coordinate system whenever $df\neq0$.

At a **critical point** $p$, however,

$$
df_p=0,
$$

so the unwanted term vanishes. The Hessian at a critical point is therefore an intrinsic element

$$
\operatorname{Hess}_p(f)\in\operatorname{Sym}^2T_p^*M
$$

on any smooth manifold. This is why the Hessian classifies stationary points without requiring a metric or connection.

Away from a critical point, a connection $\nabla$ supplies the missing comparison rule. Define

$$
\boxed{
\operatorname{Hess}^{\nabla}f(X,Y)
:=(\nabla df)(X,Y)
=X(Yf)-(\nabla_XY)f.
}
$$

If $\nabla$ is torsion-free, this Hessian is symmetric. If $\nabla'$ is another connection, their Hessians differ by a term proportional to $df$:

$$
\operatorname{Hess}^{\nabla'}f(X,Y)
-\operatorname{Hess}^{\nabla}f(X,Y)
=-df\bigl((\nabla'_X-\nabla_X)Y\bigr).
$$

They consequently agree at a critical point. A Riemannian metric selects its Levi--Civita connection, but the metric is additional structure; it is not contained in the scalar function.

This distinction is a small instance of a general lesson developed in [[basic-concepts/fibers/inq|fibers]] and [[basic-concepts/soldering/inq|soldering]]: data living over nearby points cannot be compared until a comparison law has been specified.

## Stability, convexity, and degeneracy

At a critical point of a real-valued function, the signature of the Hessian describes the quadratic approximation:

- positive definite implies a strict local minimum;
- negative definite implies a strict local maximum;
- indefinite implies a saddle; and
- degenerate or merely semidefinite leaves the question open and requires higher-order terms or global information.

A critical point with nondegenerate Hessian is a **Morse critical point**. Its index is the number of negative eigenvalues of the Hessian after choosing a real basis. The index does not depend on that basis. Morse theory uses these local quadratic models to constrain global topology.

Degeneracy can have several meanings. It may indicate a genuine flat direction, a continuous family of critical points, an impending bifurcation, an unremoved symmetry, or simply that the leading nonzero term occurs above second order. In a Morse--Bott situation the critical locus is a submanifold, and the Hessian is nondegenerate only in directions normal to that locus; tangent zero modes express motion within the family of critical points.

For a $C^2$ function on an open convex subset of an affine space,

$$
D^2f_p\succeq0\quad\text{for all }p
$$

is equivalent to convexity. This statement uses the affine straight lines of the domain. On a Riemannian manifold the analogous notion is geodesic convexity and uses the covariant Hessian along geodesics. A positive Hessian at one point is local information; it does not by itself establish global convexity, uniqueness of a minimum, or convergence of an optimization algorithm.

## Constraints and gauge zero modes

Suppose $f$ is extremized subject to constraints

$$
c^a(x)=0.
$$

At a regular constrained critical point, choose multipliers $\lambda_a$ such that

$$
df=\lambda_a\,dc^a.
$$

The quadratic form relevant to constrained stability is not the unrestricted Hessian of $f$. It is the Hessian of the Lagrangian

$$
L=f-\lambda_ac^a
$$

restricted to vectors tangent to the constraint surface:

$$
v\in\bigcap_a\ker dc^a.
$$

Extrinsic curvature of the constraint is encoded by the multiplier terms. Ignoring them can reverse the stability conclusion.

Gauge symmetry is a more structural version of the same issue. If an action $S$ is invariant under a continuous gauge group, then its Hessian at a solution has zero modes tangent to the gauge orbit. The unreduced operator is not invertible because physically equivalent configurations have been counted as different directions. One must pass to a quotient, impose gauge fixing together with its determinant or ghost data, or formulate the Hessian on the tangent complex. A zero mode that disappears after this reduction is gauge; a zero mode that survives may represent a physical modulus, instability threshold, or genuine massless excitation.

This is one reason moduli problems are naturally expressed using [[basic-concepts/groupoids/inq|groupoids]] and [[basic-concepts/stacks/inq|stacks]]. Automorphisms are not noise to be deleted from the presentation: they determine the degree-$-1$ part of the deformation complex and hence the correct domain on which a second variation can be nondegenerate.

## The algebraic-geometric Hessian

Let $X$ be smooth over a field $k$, let $p\in X(k)$, and let $f$ be a regular function near $p$. The differential

$$
df\in\Gamma(X,\Omega^1_{X/k})
$$

defines the critical locus as its zero scheme. If $df_p=0$, then in the regular local ring $\mathcal O_{X,p}$,

$$
f-f(p)\in\mathfrak m_p^2.
$$

Its leading class lies in

$$
\mathfrak m_p^2/\mathfrak m_p^3
\cong
\operatorname{Sym}^2(\mathfrak m_p/\mathfrak m_p^2).
$$

Because $\mathfrak m_p/\mathfrak m_p^2\cong T_p^*X$, this class is the intrinsic quadratic term of $f$ at $p$. When $2$ is invertible in $k$, polarization turns it into the symmetric bilinear Hessian on $T_pX$. In characteristic $2$, a quadratic form is not determined by its polarized bilinear form: diagonal second derivatives can vanish while the quadratic term remains nonzero. Divided-power or Hasse-derivative formulations may therefore be needed. The phrase “nondegenerate Hessian” should always register the characteristic.

In étale coordinates $x_1,\ldots,x_n$, the intrinsic form is represented by

$$
\left(\frac{\partial^2f}{\partial x_i\partial x_j}(p)\right).
$$

Nondegeneracy means that the induced map

$$
T_pX\longrightarrow T_p^*X
$$

is an isomorphism. This is the algebraic analogue of an isolated Morse critical point. In a family $X\to S$, one may similarly study the relative differential and the vertical Hessian along $T_{X/S}$; this measures degeneracy inside each [[basic-concepts/fibers/inq|fiber]], not variation along the base.

### Polynomial and projective Hessians

For a polynomial $F\in k[x_0,\ldots,x_n]$, its coordinate Hessian matrix is

$$
\operatorname{Hess}(F)
=\left(\frac{\partial^2F}{\partial x_i\partial x_j}\right),
$$

and its **Hessian determinant** is

$$
\operatorname{hess}(F)
:=\det\operatorname{Hess}(F).
$$

If $F$ is homogeneous of degree $d$, this determinant is homogeneous of degree

$$
(n+1)(d-2).
$$

Its zero locus is the classical Hessian hypersurface. It records where the differential of the gradient or polar map drops rank and is used in the geometry of plane curves, projective duality, inflection phenomena, and the study of singularities. Under a linear change of homogeneous coordinates the determinant changes by an invertible scalar factor determined by the coordinate change, so its projective zero locus is intrinsic up to that change.

The Hessian determinant is not the equation of the critical locus. The critical locus of $F$ is defined by its first derivatives; a hypersurface $F=0$ is singular where $F$ and all first derivatives vanish. The Hessian refines the second-order structure after that first-order condition has been imposed. In small characteristic, Euler identities and vanished numerical coefficients can make classical Hessians degenerate for arithmetic reasons, so characteristic-zero intuitions cannot be imported unchanged.

Hessian determinants also occur as discriminants of quadratic approximations and as tests for ramification of gradient maps. But the determinant forgets the full quadratic form: it records whether degeneracy occurs, not its signature, kernel, or higher-order replacement.

### Jets, sheaves, and the absence of a canonical splitting

The second jet $j^2_pf$ remembers the value, first derivative, and quadratic behavior of $f$ at $p$. Thinking in jets clarifies why a Hessian is not automatically intrinsic. A second jet contains all three orders together; separating its quadratic component from the lower-order pieces requires affine coordinates or a connection. At a critical point the linear part vanishes, so the quadratic class becomes independent of that choice.

For a smooth scheme, sheaves of principal parts and jet bundles package these local Taylor data. Their filtrations have graded pieces built from symmetric powers of $\Omega^1_{X/S}$, but a filtration need not split canonically. Local arrays of second derivatives therefore do not [[basic-concepts/gluing/inq|glue]] as a global tensor merely because their entries agree syntactically. One needs a connection, a critical-locus restriction, or some other invariant construction. [[basic-concepts/sheafs/inq|Sheaves]] are what make the locality of the coefficients precise; descent of the resulting object is a separate question.

On a singular scheme, $\Omega^1_X$ need not be locally free and the tangent space can have excess dimension. The cotangent complex then carries the deformation data that an ordinary tangent bundle loses. For derived critical loci or quotient stacks, the appropriate “Hessian” is naturally a morphism involving tangent and cotangent complexes rather than a square matrix of functions. This generalization retains relations, obstructions, and infinitesimal automorphisms instead of pretending the singular object is smooth.

### Real, complex, and Kähler Hessians

Several second derivatives coexist on a complex manifold. For a real-valued function $f$ one may form:

- the real covariant Hessian $\nabla df$;
- the complex Hessian or Levi form $i\partial\bar\partial f$; and
- a holomorphic $(2,0)$ component such as $\nabla^{1,0}\partial f$ once a connection is chosen.

They answer different questions. Positivity of $i\partial\bar\partial f$ defines plurisubharmonicity and tests complex lines; it is not the same as real convexity. A Kähler metric supplies a distinguished Levi--Civita connection compatible with the complex structure, making the comparison especially clean, but it does not collapse the $(2,0)$, $(1,1)$, and real pieces into one object. In Kähler geometry, Hessians appear in Kähler potentials, moment-map functionals, geodesic convexity on spaces of metrics, and stability problems; each use must specify which Hessian and on what space.

## Functional Hessians

In field theory and infinite-dimensional geometry, the scalar quantity is often a functional $F[\phi]$. Its second variation at a background $\bar\phi$ is written formally as

$$
\delta^2F_{\bar\phi}(\eta,\xi)
=
\iint
\eta(x)
\frac{\delta^2F}{\delta\phi(x)\delta\phi(y)}\bigg|_{\bar\phi}
\xi(y)\,dx\,dy.
$$

The functional Hessian is consequently a kernel, usually a distribution rather than an ordinary function. For a local action it is often supported on the diagonal and represented by a differential operator. For example, the Euclidean scalar action

$$
S[\phi]
=\int_M
\left(\frac12\lvert d\phi\rvert^2+V(\phi)\right)d\operatorname{vol}
$$

has, at a classical solution $\bar\phi$, fluctuation operator

$$
S^{(2)}_{\bar\phi}
=-\Delta+V''(\bar\phi)
$$

after integration by parts.

That displayed operator is incomplete until its function space, boundary conditions, and domain are specified. The same differential expression with Dirichlet, Neumann, retarded, advanced, or Feynman conditions has different inverses and different physical meaning. Integration by parts can move derivatives between the two kernel variables and generate boundary terms. Functional differentiation of local expressions also produces delta functions and their derivatives—**contact terms**—while renormalization can add local counterterm contributions. Equality of nonlocal or spectral parts does not automatically imply equality of the full distributions.

For an unbounded Hessian operator, symmetry of the formal differential expression does not guarantee self-adjointness. Positivity, closedness, essential self-adjointness, Fredholm properties, and the treatment of zero modes are analytic questions. “Invert the Hessian” is therefore an instruction that requires a domain and a physical subspace.

## Log-partition Hessians and Fisher geometry

Let a regular classical exponential family have natural coordinates $\theta^i$:

$$
p_\theta(x)
=\exp\!\left(\theta^iT_i(x)-\psi(\theta)\right)p_0(x),

\qquad
\psi(\theta)=\log Z(\theta).
$$

Differentiating the log-partition potential gives

$$
\partial_i\psi
=\mathbb E_\theta[T_i],
$$

and

$$
\boxed{
\partial_i\partial_j\psi
=\operatorname{Cov}_\theta(T_i,T_j)
=g^{\mathrm F}_{ij}.
}
$$

Here one object has three justified descriptions: it is the Hessian of $\psi$, the covariance matrix of the sufficient statistics, and the Fisher information metric in natural coordinates. The equality follows from the normalized exponential-family form. It is not true for an arbitrary scalar potential, arbitrary random variables, or arbitrary coordinates.

The natural parameter space carries a preferred affine structure. After a nonlinear reparametrization, the Fisher metric still transforms tensorially because it is independently defined by score covariances, whereas the raw coordinate Hessian of the re-expressed scalar $\psi$ acquires the extra gradient term displayed earlier. Calling a metric “Hessian” therefore means that suitable affine coordinates and a potential have been specified.

For a faithful finite-dimensional quantum exponential family

$$
\rho_\theta
=\exp\!\left(\theta^iA_i-\psi(\theta)\right),
$$

the noncommuting analogue is the Bogoliubov--Kubo--Mori inner product. Writing $\widetilde A_i=A_i-\langle A_i\rangle_\rho\mathbf1$,

$$
g^{\mathrm{BKM}}_{ij}
=\int_0^1
\operatorname{Tr}\!\left(
\rho^s\widetilde A_i\rho^{1-s}\widetilde A_j
\right)ds.
$$

It reduces to ordinary covariance when the relevant operators commute with the state. In general it is not equal to the unsymmetrized product $\operatorname{Tr}(\rho\widetilde A_i\widetilde A_j)$.

The same metric appears as the coincidence Hessian of Umegaki relative entropy. For a smooth faithful family,

$$
D(\rho_{\theta+d\theta}\Vert\rho_\theta)
=\frac12g^{\mathrm{BKM}}_{ij}(\theta)
d\theta^i d\theta^j
+O(\lVert d\theta\rVert^3).
$$

The linear term vanishes because relative entropy is minimized on the diagonal. Faithfulness and regularity matter: at the boundary of state space, supports can change and the quadratic expansion can diverge or cease to exist. In continuum QFT, local algebras are generally not described by trace-class density matrices, so one needs an operator-algebraic relative entropy and a controlled class of perturbations rather than this finite-dimensional formula by assertion. [[basic-concepts/hessians/symmetrized-relative-entropy-hessian|The symmetrized-Hessian theorem]] isolates the exact factor of two and its continuum boundary, while [[basic-concepts/hessians/higher-relative-entropy-is-not-cumulants|the higher-derivative no-go]] shows why this quadratic coincidence cannot be extrapolated into a cumulant hierarchy. [[basic-concepts/hessians/gibbs-free-energy-relative-entropy|The Gibbs specialization]] records the exact fixed-Hamiltonian free-energy identity and its strict coincidence boundary.

## Actions, effective actions, and inverse covariance

For a Euclidean functional integral with source $J$,

$$
Z[J]
=\int\mathcal D\phi\,
e^{-S[\phi]+\langle J,\phi\rangle},
\qquad
W[J]=\log Z[J],
$$

the first source derivative is the mean field and the second is the connected covariance:

$$
\frac{\delta W}{\delta J}=\varphi,
\qquad
W^{(2)}[J]=\langle\phi\phi\rangle_c
=:\mathcal C.
$$

When the Legendre transform is regular, define the quantum effective action

$$
\Gamma[\varphi]
=\sup_J\bigl(\langle J,\varphi\rangle-W[J]\bigr).
$$

Differentiating the inverse maps $J\leftrightarrow\varphi$ gives

$$
\boxed{
\Gamma^{(2)}[\varphi]
=\bigl(W^{(2)}[J]\bigr)^{-1}
=\mathcal C^{-1}.
}
$$

This is the exact relation between the two-point 1PI kernel and the connected covariance, subject to convexity, differentiability, gauge reduction, boundary conditions, and invertibility on the chosen physical subspace. In translationally invariant settings it becomes an operator or momentum-by-momentum inverse, not necessarily the reciprocal of a pointwise position-space function. [[basic-concepts/hessians/fourier-covariance-and-precision|Fourier covariance and precision]] records the convention, units, physical-subspace restriction, and Gaussian boundary explicitly.

The classical action Hessian $S^{(2)}$ is different. In a Gaussian theory it is the exact precision operator after zero modes and boundary data are handled. In an interacting theory it is the tree-level fluctuation operator; loop corrections replace it by $\Gamma^{(2)}$. Lorentzian conventions add factors of $i$ and require a choice among time-ordered, retarded, advanced, and in-in kernels. A dynamical response kernel is often a retarded commutator, while a Euclidean covariance is an equilibrium fluctuation kernel; fluctuation--dissipation or analytic-continuation hypotheses are required to relate them.

## Five objects that should not be conflated

| Object | Defining role | When it can coincide with another |
|---|---|---|
| **Hessian** | Second derivative or second variation of a specified scalar function or functional | Becomes a covariance for a regular log-partition potential; becomes a 1PI precision for the effective action |
| **Metric** | A smoothly varying, usually nondegenerate bilinear form on tangent spaces | A positive Hessian defines a Hessian metric only with the relevant affine or connection data |
| **Covariance** | Centered two-point fluctuation $\langle(X-\langle X\rangle)(Y-\langle Y\rangle)\rangle$ | Equals a log-partition Hessian in a regular exponential/source family; in the quantum case the ordering or KMS transform matters |
| **Precision** | Inverse covariance on a declared domain or quotient | Equals $\Gamma^{(2)}$ under a regular Legendre transform; equals $S^{(2)}$ only in a Gaussian or tree-level approximation |
| **Response kernel** | Derivative of an expectation value with respect to a source or perturbation | May equal a covariance in equilibrium Euclidean settings, or be related by fluctuation--dissipation; contact terms and causal prescription remain part of the object |

Even when two columns are represented by the same formula in one model, the equality has a direction of explanation. For example,

$$
\operatorname{Hess}(\log Z)=\operatorname{Cov}
$$

is proved from the exponential family, while

$$
\Gamma^{(2)}=\operatorname{Cov}^{-1}
$$

is proved from Legendre duality. Neither follows from the bare fact that all four are quadratic kernels.

## Use in the causal-response programme

[[program-core/response-registers|The response register]] routes the programme's uses of Hessians without making this general note a second owner of their physical applications. [[binary-information-geometry/balanced-exponential-family|Binary information geometry]] owns the exact commuting two-state specialization; [[causal-scale-theory/anchored-response-density-postulate|the CST source note]] owns its constitutive promotion beyond the coincidence expansion; and the independent [[causal-wall-spectral-theory/conjectures/bkm-to-spatial-precision|W2]] and [[causal-wall-spectral-theory/conjectures/wall-scalar-to-cosmological-curvature|W3]] conjectures own the carrier and field changes into cosmological precision.

Those applications inherit the exact Hessian results above only after their state family, tangent, carrier, central-evaluation policy, domain, and analytic prescription have been declared. A claim to recover a perturbative QFT sector additionally needs the covariant action, gauge complex, stable physical spectrum, and observable interface required by [[compatible-with-existing-physics/local-physics-interface|the local-physics interface]].

The durable diagnostic is therefore:

$$
\boxed{
\text{What scalar is being differentiated, on what space, in which directions, and why does its second variation equal the physical kernel being claimed?}
}
$$

Answering all four clauses is what turns a Hessian from a formal resemblance into explanatory structure.

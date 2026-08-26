# Octonionic Phase Space and Associative (3+1) Descent

The precise replacement for “the octonionic wavefunction of the cosmos collapses to (3+1)” is a staged associative descent. The exceptional Jordan algebra and its Freudenthal system provide exact octonion-organized state and symplectic carriers. A chosen rank-two corner followed by a chosen complex slice contains an exact Lorentz-vector space (mathfrak h_2(mathbb C)congmathbb R^{1,3}). That construction selects a local causal presentation, not yet a spacetime, a quantum collapse, or a cosmological perturbation; dynamics, positivity, tangent soldering, and gluing remain separate obligations.

## The exceptional carrier

Let

$$
J:=\mathfrak h_3(\mathbb O)
$$

be the (27)-dimensional exceptional Euclidean Jordan algebra. Its product

$$
X\circ Y:=\frac12(XY+YX)
$$

is well defined despite octonionic nonassociativity, but (J) is exceptional: it is not the self-adjoint part of an associative complex operator algebra preserving this product. Its spectral decomposition and cubic norm are exact; a conventional complex Hilbert-space dynamics does not follow from them.

The associated Freudenthal vector space is

$$
\mathcal F(J)
:=
\mathbb R\oplus\mathbb R\oplus J\oplus J,
$$

of real dimension

$$
2+2\dim J=56.
$$

For (x=(\alpha,\beta,X,Y)) and (x'=(\alpha',\beta',X',Y')), it carries an invariant alternating form of the schematic normalization

$$
\Omega(x,x')
=
\alpha\beta'-\beta\alpha'
+\operatorname{tr}(X\circ Y')
-\operatorname{tr}(Y\circ X'),
$$

together with a quartic invariant. These are the right mathematical ingredients for a classical phase-space carrier. In established supergravity applications they organize electric-magnetic black-hole charge space; they are not thereby the phase space of the whole cosmos. The exceptional Jordan/Freudenthal role is documented by [Ferrara and Günaydin](https://arxiv.org/abs/hep-th/9708025) and [Borsten, Duff, Ferrara, Marrani, and Rubens](https://arxiv.org/abs/0903.5517).

## Why the wavefunction should not be octonion-valued

A real symplectic vector space does not itself define a quantum theory. A conventional quantization still needs

$$
(\mathcal F(J),\Omega)
+H_{\mathcal F}
+P
+\mu
+\text{positive Hilbert completion},
$$

where (H_{\mathcal F}) is a Hamiltonian, (P) a polarization, and (mu) a measure. On a Lagrangian polarization (L), the state could then take the ordinary form

$$
\Psi\in L^2(L,\mathrm d\mu;\mathbb C),
\qquad
i\hbar\partial_\tau\Psi
=\widehat H_{\mathcal F}\Psi.
$$

The amplitude is complex-valued. The octonionic structure lives in the variables, invariants, sector geometry, and Hamiltonian. This avoids the associativity, tensor-product, spectral, and positivity problems of treating unit octonions as ordinary quantum phases.

There is also a Jordan-state route. A normalized positive state can be represented by

$$
\rho\in J_+,
\qquad
\operatorname{tr}\rho=1,
\qquad
\omega_\rho(X)=\operatorname{tr}(\rho\circ X).
$$

Primitive idempotents form the pure-state space (mathbb OP^2), not the entire mixed-state space. Neither route supplies a Born rule for cosmological records until composition, dynamics, measurement contexts, and an observable descent are fixed. [[complex-presentation-without-polarization/holomorphic-wavefunctions|Holomorphic wave functions and complex integrals]] owns the analogous warning for complex geometry.

## First restriction: a rank-two octonionic corner

Choose a rank-two idempotent (q\in J). Its quadratic Peirce compression is

$$
U_q(X)
:=
2q\circ(q\circ X)-q\circ X.
$$

For the frame choice

$$
q=\operatorname{diag}(1,1,0),
$$

the image is the exact Jordan corner

$$
U_qJ\cong\mathfrak h_2(\mathbb O).
$$

An element has the form

$$
Y=
\begin{pmatrix}
t+z & x\\
\bar x & t-z
\end{pmatrix},
\qquad
t,z\in\mathbb R,
\quad
x\in\mathbb O,
$$

and determinant

$$
\det Y=t^2-z^2-|x|^2.
$$

Therefore

$$
\mathfrak h_2(\mathbb O)
\cong
\mathbb R^{1,9}
$$

as a quadratic space. This is the octonionic rung of the division-algebra Lorentz construction; see [Baez and Huerta](https://arxiv.org/abs/0909.0551).

The choice of (q) is already a reduction of the exceptional carrier. A cosmological theory must explain whether it is fixed by a state, a wall, a factive event, a boundary condition, or spontaneous sector selection.

## Second restriction: an associative complex slice

Choose a unit imaginary octonion

$$
u\in\operatorname{Im}\mathbb O,
\qquad
u^2=-1.
$$

It generates the associative subalgebra

$$
\mathbb C_u
:=
\operatorname{span}_{\mathbb R}\{1,u\}
\subset\mathbb O.
$$

The choices of (u) form

$$
S^6\cong G_2/SU(3).
$$

The real orthogonal projection onto this slice can be written

$$
\pi_u(x)
:=
\frac12\bigl(x-u(xu)\bigr).
$$

Alternativity makes the two-generated products unambiguous. Applying the restriction entrywise selects the Jordan subalgebra

$$
\mathfrak h_2(\mathbb C_u)
\subset
\mathfrak h_2(\mathbb O).
$$

For

$$
Y_u=
\begin{pmatrix}
t+z & w\\
\bar w & t-z
\end{pmatrix},
\qquad
w=x+uy\in\mathbb C_u,
$$

one has

$$
\det Y_u
=
t^2-z^2-x^2-y^2.
$$

Hence

$$
\boxed{
\mathfrak h_2(\mathbb C_u)
\cong
\mathbb R^{1,3}
}
$$

as a Lorentz quadratic space. This is the strongest exact mathematical content presently available for “octonionic possibility reduces to (3+1).”

The entrywise projection (pi_u) is not automatically a Jordan homomorphism, a positive conditional expectation, a dynamically consistent truncation, or a state update. The exact claim is the existence of the selected associative subalgebra and its Lorentz determinant. A physical descent must show why discarded directions do not source the retained sector.

## Why the quaternionic shortcut is not enough

Associative quaternionic subalgebras are also selected inside (mathbb O); their space is (G_2/SO(4)). But

$$
\mathbb H\cong\mathbb R^4
$$

with its natural norm is Euclidean, while

$$
\mathfrak h_2(\mathbb H)
\cong
\mathbb R^{1,5}.
$$

Thus “one real plus three imaginary quaternionic directions” is only a dimension count. It does not derive the Lorentz cone of (3+1) spacetime. The complex Hermitian (2\times2) corner is the correct division-algebra construction for that signature.

## From a Lorentz vector space to spacetime

The algebraic reduction still lacks locality. At every would-be spacetime point, one needs a solder

$$
\sigma_x:
\mathfrak h_2(\mathbb C_{u(x)})
\longrightarrow
T_xM
$$

that preserves the determinant cone, fixes units, and varies consistently. The complete construction must provide

- a four-manifold or equivalent local site;
- a time orientation and Lorentzian metric;
- transition maps relating (u(x)) and (q(x)) on overlaps;
- a connection and curvature;
- causal dynamics and constraints;
- a state on the descended observable algebra; and
- a gluing theorem or controlled defect where contexts fail to agree.

This is where [[basic-concepts/soldering/entry|soldering]] and [[basic-concepts/gluing/entry|gluing]] become literal mathematical obligations. The determinant cone is a local model of causality; it is not yet an arena of facts.

## Four meanings of collapse

The word *collapse* hides four different arrows:

| Reading | Mathematical content | Present status |
|---|---|---|
| contextual restriction | select (q), (u), and (mathfrak h_2(\mathbb C_u)) | exact after the choices |
| dynamical reduction | show unselected directions decouple or become inaccessible | open |
| quantum state update | define an instrument and conditional post-measurement state | open |
| factive realization | produce one Lorentzian history and records from a whole-state carrier | open |

The present model uses **associative descent** for the first arrow and reserves *collapse* for a future theory that actually constructs one of the latter two noninvertible processes.

## Where (A_2) enters and where resonance does not

Every element of (J) obeys a cubic characteristic equation. On the trace-zero slice, three eigenvalue branches and their differences organize an (A_2) root geometry with Weyl group

$$
W(A_2)\cong S_3.
$$

This can supply a three-branch phase organization, multiplicities, or selection rules. It does not by itself supply oscillation frequencies. If a descended associative Hamiltonian has ordered levels (E_1<E_2<E_3), the transition gaps obey the exact identity

$$
\omega_{13}
=
\omega_{12}+\omega_{23},
\qquad
\omega_{ij}:=\frac{E_j-E_i}{\hbar}.
$$

But a Jordan eigenvalue collision is a discriminant, not a resonance pole. A physical line still requires a Hamiltonian or wave operator, domain, state, boundary conditions, meromorphic continuation, width, residue, and observable coupling. [[the-grain-of-causal-scale/causal-spectrum|The causal spectrum]] owns this firewall.

## CMB return type

To become cosmology, the descent must continue

$$
(J,\mathcal F(J),\omega)
\xrightarrow{(q,u)}
\mathcal H_{q,u}
\xrightarrow{\mathfrak S_\zeta}
(\zeta,\pi_\zeta,h_\lambda,\omega_{\mathrm L})
\xrightarrow{\mathfrak M_{\mathrm{hot}}}
\Delta_\ell^{T,E,B}.
$$

Here (mathcal H_{q,u}) denotes an associative Hilbert carrier only after quantization; it is not shorthand for (mathfrak h_2(\mathbb C_u)) alone. The second arrow must return gauge-invariant scalar and tensor variables with a Lorentzian state and dynamics. The third must match them into the hot universe. Without these arrows, the octonionic structure is compelling kinematics but has no CMB prediction.

## Kill conditions

The proposed descent fails as a physical explanation if

- no dynamics selects (q) and (u) without inserting the desired (3+1) answer;
- the projection is not positive or does not preserve the selected state;
- discarded octonionic directions source large unobserved modes;
- local complex slices cannot be glued into a Lorentzian causal net;
- the resulting state has no positive covariance or stable evolution; or
- the descended primordial modes do not reproduce the observed passive adiabatic TT/TE/EE phase relations.

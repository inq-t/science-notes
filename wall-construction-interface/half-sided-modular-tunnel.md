# The Half-Sided Modular Tunnel

A half-sided modular inclusion constructs an exact nested family of von Neumann algebras with positive orientation and coherent cross-fiber transport. The invariant reference state supplied with the inclusion makes that family horizontally response-null; a nonzero BKM wall is obtained only after an independent faithful state path is added. This separates the solved transport problem from the unsolved physical selection problem without importing measured gravity or a fitted expansion history.

## Exact transport from one inclusion

Let \(\mathcal N\subset\mathcal M\subset B(\mathcal H)\) satisfy the hypotheses of the general half-sided modular-inclusion theorem for a normal faithful semifinite weight \(\chi\): the restriction \(\chi|_{\mathcal N}\) is semifinite, both algebras have the required standard forms, and, in the convention used here,

$$
\Delta_{\mathcal M}^{it}\mathcal N\Delta_{\mathcal M}^{-it}
\subseteq\mathcal N
\qquad(t\leq0).
$$

The Araki--Zsido theorem constructs

$$
P=\overline{\frac{\log\Delta_{\mathcal N}-\log\Delta_{\mathcal M}}{2\pi}}
\geq0,
\qquad
U(r)=e^{irP},
\qquad
\alpha_r=\operatorname{Ad}U(r),
$$

such that, for \(r\geq0\),

$$
\alpha_r(\mathcal M)\subseteq\mathcal M,
\qquad
\mathcal N=\alpha_1(\mathcal M),
\qquad
\alpha_{r+s}=\alpha_r\alpha_s.
$$

This is **[STANDARD]**; [[library/extension-of-borchers-structure-theorem/inq|Araki and Zsido]] is the primary-source owner. Define the algebraic tunnel

$$
\mathcal A_r:=\alpha_r(\mathcal M).
$$

For \(r_2\geq r_1\geq0\), put

$$
\boxed{
\iota_{r_2:r_1}
:=
\left.\alpha_{r_2-r_1}\right|_{\mathcal A_{r_1}}
:
\mathcal A_{r_1}\overset{\sim}{\longrightarrow}\mathcal A_{r_2}.}
$$

If \(a=\alpha_{r_1}(x)\), then \(\iota_{r_2:r_1}(a)=\alpha_{r_2}(x)\). Thus the displayed map is onto its stated fiber, even though \(\alpha_{r_2-r_1}\) is only an endomorphism when regarded as a map from \(\mathcal M\) into itself. Its inverse between the two fibers is the restriction of the global automorphism \(\operatorname{Ad}U(r_1-r_2)\). Moreover,

$$
\iota_{r_3:r_2}\circ\iota_{r_2:r_1}
=\iota_{r_3:r_1}.
$$

The ordered base therefore has exact composition and zero holonomy. This is a genuine cross-fiber construction, not an identification written down after the comparison.

## Additive translation is not yet logarithmic cosmic scale

The theorem parameter \(r\) is additive. If a candidate introduces a logarithmic label

$$
N:=\log\frac r{r_*},
\qquad
r(N)=r_*e^N,
$$

then the exact transport is

$$
\boxed{
\iota_{N_2:N_1}
=\operatorname{Ad}U\!\left(r_*(e^{N_2}-e^{N_1})\right)
\big|_{\mathcal A_{N_1}},}
$$

not \(\operatorname{Ad}U(N_2-N_1)\). The affine relation

$$
\Delta_{\mathcal M}^{-it}U(r)\Delta_{\mathcal M}^{it}
=U(e^{2\pi t}r)
$$

explains why \(\log r\) shifts under modular boosts. It does not identify \(\log r\) with \(\log(a/a_*)\), proper time, horizon area, or factive age. That solder remains a physical construction.

## The invariant reference state is response-null

In the state version of the theorem, let \(\chi\) be the common faithful normal invariant state and set

$$
\omega_r:=\chi|_{\mathcal A_r}.
$$

The state at \(r_2\) is compared on the earlier fiber by precomposition:

$$
\widetilde\omega_{r_2}^{(r_1)}
:=\omega_{r_2}\circ\iota_{r_2:r_1}.
$$

Invariance gives

$$
\widetilde\omega_{r_2}^{(r_1)}=\omega_{r_1}.
$$

Consequently the transported Connes cocycle is the identity, the horizontal tangent vanishes, and every faithful BKM norm of that tangent is zero:

$$
[D\widetilde\omega_{r_2}^{(r_1)}:D\omega_{r_1}]_s=\mathbf1,
\qquad
v_r=0,
\qquad
G_{rr}=0.
$$

This is an exact **[NO-FREE-RESPONSE RESULT]**. Half-sided modular structure derives orientation and transport; it does not derive a distinguishable state displacement merely because its fibers are nested. The same warning applies to a dilation-covariant family of conformal diamonds with invariant vacuum: covariance supplies an exact presentation isomorphism, while vacuum invariance makes the pulled-back state path constant.

## The differentiable modular wall is defect-flat

The operator-level wall test reaches the same conclusion more sharply. Write

$$
K_{\mathcal M}:=\log\Delta_{\mathcal M},
\qquad
K_{\mathcal N}:=\log\Delta_{\mathcal N},
\qquad
P=\overline{\frac{K_{\mathcal N}-K_{\mathcal M}}{2\pi}},
$$

and define the skew generators

$$
A_{\mathcal M}:=-\frac{i}{2\pi}K_{\mathcal M},
\qquad
A_{\mathcal N}:=-\frac{i}{2\pi}K_{\mathcal N}.
$$

The affine covariance above gives, on the common smooth core,

$$
[K_{\mathcal M},P]=2\pi iP,
\qquad
[A_{\mathcal M},P]=P.
\tag{HSM1}
$$

For \(r_\sigma=r_*e^\sigma>0\), imaginary translation defines the bounded contraction

$$
T_\sigma
:=
U(ir_\sigma)
=e^{-r_\sigma P}.
\tag{HSM2}
$$

It is operator-norm \(C^1\) for every finite \(\sigma\), with

$$
T_\sigma'=-r_\sigma Pe^{-r_\sigma P}.
\tag{HSM3}
$$

For a proper nontrivial inclusion, dilation covariance forces \(\sigma(P)=[0,\infty)\). Thus \(T_\sigma\) is injective with dense range but has no bounded inverse. It is an oriented smoothing, not a many-to-one quotient.

The typing trap appears when this contraction is used as the realization \(J_\sigma\) in [[contemporary-puzzles/yang-mills-mass-gap/wall-crossing-defect-and-the-fossil-of-mass-engagement]]. The actual endpoint transport from the \(\mathcal M\) presentation to the \(\mathcal N\) presentation contains \(U(1)\), because

$$
\mathcal N=\operatorname{Ad}U(1)(\mathcal M),
\qquad
K_{\mathcal N}U(1)=U(1)K_{\mathcal M}.
\tag{HSM4}
$$

The endpoint-aligned contraction is therefore

$$
J_\sigma:=U(1)e^{-r_\sigma P}.
\tag{HSM5}
$$

Its wall defect is

$$
\begin{aligned}
\mathfrak D_\sigma
&=
J_\sigma'
+J_\sigma A_{\mathcal M}
-A_{\mathcal N}J_\sigma\\
&=
U(1)\left(
-r_\sigma Pe^{-r_\sigma P}
+[e^{-r_\sigma P},A_{\mathcal M}]
\right)\\
&=0.
\end{aligned}
\tag{HSM6}
$$

The final equality follows from (HSM1). More generally, the same cancellation holds for sufficiently regular endpoint-aligned functional-calculus profiles \(U(1)f(r_\sigma P)\). Canonical modular transport plus canonical affine smoothing is an equivariant presentation change; it does not pay a wall residue.

If the endpoint transporter is omitted and the bare \(T_\sigma\) is incorrectly placed between the two endpoint generators, the formal defect is nonzero:

$$
\mathfrak D_\sigma^{\mathrm{bare}}
=iPe^{-r_\sigma P}.
\tag{HSM7}
$$

That term measures the missing endpoint identification, not a physical fossil. It also cannot supply a gap:

$$
\left(\mathfrak D_\sigma^{\mathrm{bare}}\right)^*
\mathfrak D_\sigma^{\mathrm{bare}}
=P^2e^{-2r_\sigma P},
\qquad
\inf_{p\in(0,\infty)}p^2e^{-2r_\sigma p}=0.
\tag{HSM8}
$$

This is an exact **[ENDPOINT-ALIGNED WALL-DEFECT NO-GO]**. HSMI supplies orientation, an affine scale law, and exact cross-fiber transport, but its natural differentiable realization is defect-flat. A nonzero wall needs additional, independently selected non-equivariant data.

Sharp core cuts do not evade the conclusion. Spectral projections \(e_N=\mathbf1_{(-\infty,N]}(X)\) can be genuinely noninjective, but whenever the intervening spectral slice is nonzero,

$$
\|e_{N+h}-e_N\|=1.
$$

They are not operator-norm continuous and do not satisfy the differentiable wall hypotheses. Smoothing the cut restores differentiability only by supplying a new profile whose physical selection remains open.

## The strongest nonzero abstract assembly

The transport can be combined with a separately specified state law without type error. Let

$$
j_r:=\left.\alpha_r\right|_{\mathcal M}:
\mathcal M\overset{\sim}{\longrightarrow}\mathcal A_r
$$

and choose a faithful \(C^2\) state path \(r\mapsto\psi_r\) on the fixed reference algebra \(\mathcal M\), with finite or renormalized Araki-relative-entropy Hessian. Define

$$
\omega_r:=\psi_r\circ j_r^{-1}.
$$

For \(a=j_{r_1}(x)\), exact transport gives

$$
(\omega_{r_2}\circ\iota_{r_2:r_1})(a)
=\psi_{r_2}(x).
$$

Hence the whole cross-fiber comparison pulls back to one well-typed comparison on \(\mathcal M\):

$$
[D(\omega_{r_2}\circ\iota_{r_2:r_1}):D\omega_{r_1}]_s
=j_{r_1}\!\left([D\psi_{r_2}:D\psi_{r_1}]_s\right),
$$

and

$$
G_{rr}(r)
=g^{\mathrm{BKM}}_{\psi_r}(\dot\psi_r,\dot\psi_r).
$$

[[library/relative-hamiltonian-for-faithful-normal-states/inq|Bounded Araki perturbations]] provide standard faithful examples of such paths. This is an exact, type-III-capable **[ABSTRACT INTERFACE CONSTRUCTION]** and it uses neither \(G\) nor a fitted FLRW curve. It does not make the response a consequence of the half-sided inclusion: the choice of \(\psi_r\), its generator, its rate, and its physical interpretation are new input. To recover half-sided modularity for the perturbed states, one would additionally have to prove the appropriate modular containment at every \(r\) and compatibility with the already reconstructed \(U\); that is open and may force the response back to zero.

## What is closed, and what is not

This benchmark closes the claim that cross-fiber comparison is mathematically unavailable. It supplies a nested algebra tunnel, a positive orientation, exact transport, composition, and—after an explicit independent state law—a well-typed relative cocycle and BKM tangent.

It does not construct causal regions or codimension-two cuts, select a cosmological state law, identify \(r\) with scale age, produce a state-preserving expectation or operator-valued weight, define a renormalized Weyl or TT source, fix an area density, derive \(G\), or solve a background. Nor does the theorem prove that an independently proposed wall family is this reconstructed tunnel. [[finite-cellular-markov-wall|The finite cellular Markov wall]] supplies the complementary exact nonzero benchmark; [[cross-fiber-transport|cross-fiber transport and state selection]] owns the generic alternatives and the remaining physical gate.

The next construction target is therefore not another isomorphism. It is a natural state-compatible normal UCP map or pointed correspondence

$$
\Phi_\sigma:\mathcal M_-\longrightarrow\mathcal M_+
$$

whose \(L^2\) implementation is operator-norm \(C^1\), preserves a common generator core, respects the required regional maps, is not an equivariant presentation equivalence, and has a wall defect that survives the physical quotient. Its stabilizer should be computed only after this completed asymmetric primitive has been constructed.

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

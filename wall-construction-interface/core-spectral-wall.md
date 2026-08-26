# The Core Spectral Wall

A type-$\mathrm{III}_1$ factor, a pointed spectral coordinate in its canonical core, and one faithful normal core state construct an exact two-level algebraic pre-wall. The capacity level consists of nested finite cuts of trace $e^N$ and type-$\mathrm{II}_1$ corners; the response level consists of labelled copies of the whole core, coherent dual-flow transport, and state-compatible binary contexts. These carriers must not be conflated: $W^*(e_N)$ is a subalgebra of the whole core, not of the corner $e_N\mathcal Ce_N$. Every normalizable core state breaks exact scale invariance, and one fixed logistic spectral state gives the balanced binary Fisher--BKM response $\nu^2\operatorname{sech}^2(\nu(N-N_c))$. This is not yet a Lorentzian causal wall; its physical cut, locality, source, area, and record maps remain open.

## The canonical core and its scale orientation

Let $M$ be a type-$\mathrm{III}_1$ factor with a faithful normal state $\varphi$. A modular crossed-product presentation of its Falcone--Takesaki canonical core is the type-$\mathrm{II}_\infty$ factor

$$
\mathcal C:=M\rtimes_{\sigma^\varphi}\mathbb R
$$

with a faithful normal semifinite trace $\tau$ and a dual action. [[library/noncommutative-flow-of-weights/entry|Falcone and Takesaki]] own the weight-independent core and trace-scaling theorem. [[library/de-sitter-observables-algebra/entry|Chandrasekaran, Longo, Penington, and Witten]] give the crossed-product trace formula and the finite spectral-corner construction used below.

If $\theta_s$ denotes the standard dual action with $\tau\circ\theta_s=e^{-s}\tau$, define the sign-oriented flow $\beta_s:=\theta_{-s}$. Then

$$
\tau\circ\beta_s=e^s\tau.
$$

Let $h_\varphi$ be the positive affiliated density of the dual weight and define

$$
X:=-\log h_\varphi.
$$

The standard density covariance and its sign-oriented form are

$$
\theta_s(h_\varphi)=e^{-s}h_\varphi,
\qquad
\beta_s(h_\varphi)=e^s h_\varphi.
$$

Therefore

$$
\beta_s(X)=X-s.
$$

For the spectral functions used here, the trace disintegrates as

$$
\boxed{
\tau(f(X))
=\int_{-\infty}^{\infty}e^x f(x)\,\mathrm dx.}
$$

The core and its scaling action are canonical up to their natural equivalence, but the spectral filtration is pointed data. Rescaling one weight by a positive scalar translates $X$ by a constant. Replacing $\varphi$ by a genuinely different faithful state generally relates the affiliated densities by a noncommuting Connes cocycle, not by a scalar translation. The construction therefore does not claim that $\{e_N\}$ is state-independent.

## Exact nested cuts and finite corners

For every $N\in\mathbb R$, define

$$
e_N:=\mathbf1_{(-\infty,N]}(X).
$$

Then

$$
e_{N_1}\le e_{N_2}\quad(N_1\le N_2),
\qquad
e_N\downarrow0\quad(N\to-\infty),
\qquad
e_N\uparrow\mathbf1\quad(N\to+\infty).
$$

The trace and dual transport are exact:

$$
\boxed{
\tau(e_N)=\int_{-\infty}^Ne^x\,\mathrm dx=e^N,}
$$

$$
\boxed{
\beta_s(e_N)=e_{N+s}.}
$$

Put

$$
\mathcal K_N:=e_N\mathcal C e_N.
$$

Each $\mathcal K_N$ is a type-$\mathrm{II}_1$ factor with unit $e_N$ and normalized trace

$$
\operatorname{tr}_N(x):=e^{-N}\tau(x).
$$

For $N_2\ge N_1$, define

$$
\boxed{
\kappa_{N_2:N_1}
:=
\left.\beta_{N_2-N_1}\right|_{\mathcal K_{N_1}}
:
\mathcal K_{N_1}\overset\sim\longrightarrow\mathcal K_{N_2}.}
$$

These maps compose exactly and carry units to units. They are different from the nonunital corner inclusion $\mathcal K_{N_1}\subset\mathcal K_{N_2}$. Moreover,

$$
\operatorname{tr}_{N_2}(\kappa_{N_2:N_1}(x))
=\operatorname{tr}_{N_1}(x).
$$

Thus the normalized tracial corner family is exactly response-null after transport. Connes scale flow constructs scale, finite capacity, and comparison; by itself it does not construct a nonzero state tangent.

## Infinity of what?

The construction answers this question without metaphor:

$$
\frac{\mathrm d}{\mathrm dN}\tau(e_N)=\tau(e_N),
\qquad
\frac{\mathrm d}{\mathrm dN}\log\tau(e_N)=1,
\qquad
\tau(\mathbf1)=+\infty.
$$

The infinity is the semifinite trace-capacity of the whole core. The $N\to-\infty$ boundary is the zero projection; the $N\to+\infty$ boundary is the full identity, which has no normalized tracial state. Every finite corner admits its canonical normalized trace. Neither end is, merely from these equations, infinite spatial volume, energy, proper time, entropy, or cosmological expansion.

The two ends must not be collapsed into one meaning of nothing. As $N\to-\infty$, the spectral cut tends to the zero projection. As $N\to+\infty$, the cuts exhaust an infinite-trace carrier that has no normalized tracial state. [[scale-character-solder|The scale-character solder]] pairs the latter asymptotic boundary, conditionally, with the $A_2$ cusp where positive sheet distinctions collapse to $\mathbb C\mathbf1$. The unbounded whole is not a larger normalized state; it is a weight-valued carrier exhausted by finite corners.

## Whole-core fibers and why a normal state must produce response

Let $d\in L^1(\mathcal C,\tau)_+$ have support $\mathbf1$ and $\tau(d)=1$. It defines one faithful normal state on the whole core,

$$
\Omega_d(x):=\tau(d^{1/2}xd^{1/2}).
$$

For the response carrier, let $\mathcal A_N:=\mathcal C^{(N)}$ be a labelled copy of the whole core, put $\omega_N:=\Omega_d$ in its native presentation, and define

$$
\iota_{N_2:N_1}:=\beta_{N_2-N_1}:
\mathcal A_{N_1}\overset\sim\longrightarrow\mathcal A_{N_2}.
$$

The maps compose exactly and have zero holonomy. Pulling every native state back to $\mathcal A_0$ gives the transported state orbit

$$
\psi_N:=\Omega_d\circ\beta_N.
$$

This is not an arbitrary path $N\mapsto d_N$: it is the orbit of one global state under the already constructed transport. Its $\tau$-density is

$$
d_N=e^N\beta_{-N}(d),
$$

because $\tau\circ\beta_N=e^N\tau$.

There is no nonzero $\tau$-integrable density whose normal state is invariant under every $\beta_s$. Invariance would imply

$$
\beta_s(d)=e^s d.
$$

For the spectral tail

$$
F(\lambda):=\tau\!\left(\mathbf1_{(\lambda,\infty)}(d)\right),
$$

trace scaling would then give

$$
F(e^{-s}\lambda)=e^sF(\lambda),
$$

so $F(\lambda)=C/\lambda$. If $C>0$, the layer-cake formula $\tau(d)=\int_0^\infty F(\lambda)\,\mathrm d\lambda$ diverges; if $C=0$, then $d=0$. Hence

$$
\boxed{
\text{the scale-covariant whole is a weight, while every normal $L^1$ state points}.}
$$

This statement does not exclude singular invariant states. Under the regularity needed for a BKM tangent, the raw full-core normal-state orbit cannot be response-null everywhere. The theorem forces symmetry breaking by normalizability, not a unique state, a response profile, or survival after the later physical quotient.

The finite corner also has the conditioned state

$$
\widehat\omega_N(x)
:=
\frac{\Omega_d(x)}{\Omega_d(e_N)},
\qquad x\in\mathcal K_N,
$$

This state is faithful and normal. Pulled back along $\kappa_{N_2:N_1}$, it is governed by the dual orbit of the single density $d$. This finite-corner family records normalized capacity, but it is not the binary response carrier used below: inside $\mathcal K_N$, the projection $e_N$ is the unit and $\mathbf1-e_N$ is absent.

## A fixed timeless state that returns the binary pulse

Let

$$
q_{\nu,N_c}(x)
:=
\frac{\nu}{2}\operatorname{sech}^2\!\bigl(\nu(x-N_c)\bigr),
\qquad \nu>0,
$$

and choose the single affiliated density

$$
\boxed{
d_{\nu,N_c}:=e^{-X}q_{\nu,N_c}(X).}
$$

It is positive, has full support, and is normalized because

$$
\tau(d_{\nu,N_c})
=\int_{-\infty}^{\infty}q_{\nu,N_c}(x)\,\mathrm dx
=1.
$$

For $\nu\ge\tfrac12$ the density is bounded; for smaller positive $\nu$ it is an unbounded affiliated $L^1$ density, which still defines a normal state.

Read the cut as the two-outcome question $e_N$ versus $\mathbf1-e_N$. Its positive-sector probability in this one timeless state is

$$
\begin{aligned}
Z(N)
&:=\Omega_d(e_N)\\
&=\int_{-\infty}^{N}q_{\nu,N_c}(x)\,\mathrm dx\\
&=\frac12\left[1+\tanh\!\bigl(\nu(N-N_c)\bigr)\right].
\end{aligned}
$$

Equivalently, pull the native context $W^*(e_N)$ back to $\mathcal A_0$ by $\beta_{-N}$; it becomes the fixed algebra $W^*(e_0)$. The transported state $\psi_N$ restricted to that fixed binary algebra is

$$
\rho_N^{\mathrm{bin}}
=
\operatorname{diag}(Z(N),1-Z(N)).
$$

Because it is commuting, its Fisher metric is its BKM metric. Direct calculation gives

$$
\boxed{
G_{NN}^{\mathrm{bin}}
=\frac{(Z'(N))^2}{Z(N)(1-Z(N))}
=\nu^2\operatorname{sech}^2\!\bigl(\nu(N-N_c)\bigr).}
$$

Thus the exact binary curve used by CST is realized as the presentation of one atemporal normal state through moving spectral cuts. In the transported picture, the cut is fixed and the state moves; the two descriptions are related by $\beta_N$ and contain the same mathematics.

For the logistic density, the full transported core density is explicitly

$$
d_N=e^{-X}q_{\nu,N_c}(X+N).
$$

These densities commute, so the full core state orbit is a location family. Its BKM metric is constant:

$$
G_{NN}^{\mathrm{core}}
=\int_{-\infty}^{\infty}
\left(\partial_N\log q_{\nu,N_c}(x+N)\right)^2
q_{\nu,N_c}(x+N)\,\mathrm dx
=\frac{4\nu^2}{3}.
$$

Therefore the pulse is the BKM/Fisher response **after restriction to the fixed transported binary context**, not the full core information metric. Monotonicity under that fixed restriction gives

$$
G_{NN}^{\mathrm{bin}}
\le G_{NN}^{\mathrm{core}}.
$$

This distinction prevents a recurrence of the error in which a response on one carrier is silently promoted to every carrier.

## Exact readout

In the native fiber $\mathcal A_N$, let

$$
\mathcal B_N:=W^*(e_N)\cong\mathbb C^2.
$$

Since $e_N$ commutes with $d_{\nu,N_c}$, it belongs to the centralizer of $\Omega_d$. The normal conditional expectation

$$
E_N(x)
=
\frac{\Omega_d(e_Nxe_N)}{Z(N)}e_N
+
\frac{\Omega_d((\mathbf1-e_N)x(\mathbf1-e_N))}{1-Z(N)}(\mathbf1-e_N)
$$

defines a map $E_N:\mathcal A_N\to\mathcal B_N$. It is unital, completely positive, idempotent, and $\Omega_d$-preserving for every finite $N$. This is a constructed context and readout, not an expectation inferred from commutativity alone.

The carrier firewall is essential:

$$
\mathcal B_N\subset\mathcal A_N=\mathcal C^{(N)},
\qquad
\mathcal B_N\not\subset\mathcal K_N=e_N\mathcal C e_N.
$$

The first inclusion owns the Bernoulli readout. The second carrier owns finite trace-capacity. The construction relates them through their common projection $e_N$ but does not identify their state spaces.

## What the construction closes

The construction has two exact subpackages. The finite-capacity filtration is

$$
\mathfrak W_{\mathrm{cap}}
=
\bigl(
\{e_N,\mathcal K_N,\operatorname{tr}_N\},
\{\widehat\omega_N\},
\{\kappa_{N_2:N_1}\}
\bigr),
$$

while the response-and-readout pre-wall is

$$
\mathfrak W_{\mathrm{ctx}}
=
\bigl(
\{\mathcal A_N=\mathcal C^{(N)}\},
\{\omega_N=\Omega_d\},
\{\iota_{N_2:N_1}\},
\{\mathcal B_N,E_N\}
\bigr).
$$

They share the pointed projection $e_N$, but they are not one algebra: $\mathcal K_N$ is a finite corner of $\mathcal A_N$, whereas $\mathcal B_N$ also contains its complement. Their paired use is denoted $\mathfrak W_{\mathrm{core}}^{\mathrm{alg}}=(\mathfrak W_{\mathrm{cap}},\mathfrak W_{\mathrm{ctx}};e_N)$. This notation records the common spectral datum without asserting a same-carrier identification.

It has:

- an exact pointed logarithmic scale $N=\log\tau(e_N)$, with unit slope fixed by trace scaling;
- nested cut projections and finite factor corners on the capacity level;
- labelled whole-core fibers with exact, compositional, zero-holonomy transport;
- one global faithful state rather than a path fitted at every scale;
- faithful conditioned corner states, kept separate from the response carrier;
- a state-preserving binary readout on each whole-core fiber; and
- an exact nonzero Fisher--BKM member, including the existing balanced pulse.

It uses no measured $G$, FLRW solution, fitted $H(z)$, dark-energy density, or target primordial spectrum. [[receipts/verify-core-spectral-wall.py|The receipt]] checks the scalar trace, logistic, binary-Fisher, and full-location-Fisher identities; it does not verify operator-algebraic hypotheses or physical realization.

## What remains open

This construction changes the keystone gap. It is no longer true that the repository lacks any scale-indexed algebra, state, transport, and readout law. What remains is the **physical realization** of this pre-wall:

1. construct a functor taking the spectral context $e_N$ to a codimension-two causal cut $\Sigma_N$ and the corner order to causal nesting;
2. recover a local type-III net and explain whether its physical wall algebra is represented by the whole-core response carrier, the finite corner, or a controlled relation between them;
3. construct a nondegenerate binary context inside each finite corner, or prove why the ambient context is the physically correct response carrier;
4. select $\varphi$ and the global density $d$ from deeper algebra rather than choosing a convenient member;
5. derive or measure the dimensionless width $\nu$—core scale fixes $N$, not the state width;
6. construct renormalized Weyl and TT source tangents and the physical quotient;
7. identify the trace-capacity measure with edge, spectral-area, and gravitational response on the same tangent; and
8. construct factual records and a Lorentzian history functor.

The logistic density is therefore a mathematically natural exact member, not yet a uniqueness theorem. [[algebra/a2-positive-completion|The $A_2$ positive-completion theorem]] supplies independent fiberwise boundary types and, after a subgroup choice, a binary stabilizer expectation. [[scale-character-solder|The scale-character solder]] states the precise optional matching among its discriminant depth, this trace capacity, and HSMI affine scale.

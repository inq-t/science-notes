# Noninvertible Presentation and Apparent Chance

A deterministic pre-observable history can have an observer-facing stochastic law when its readout is noninjective. The readout alone supplies neither probabilities nor indeterminism: a state or disintegration weights the unresolved fibers, while the underlying point and its evolution may remain determinate. Groupoids, torsors, and strict descent organize local choices and their compatibility; strict effective descent is not itself lossy. Apparent chance enters only when a separately declared realization forgets part of that structure and a state weights what remains unresolved. The 2026 Jacobian counterexamples give an unusually sharp local-to-global model: the derivative is invertible everywhere, yet no global inverse exists because the map is nonproper and generically many-to-one.

**Status: [EXACT FINITE AND PATH-SPACE THEOREMS; EXACT LOCAL--GLOBAL PRECEDENT; ONTOLOGICAL INTERPRETATION; OPEN PHYSICAL REALIZATION].** Nothing below proves that nature is deterministic. It proves that a stochastic observable law does not, by itself, entail stochastic ontology.

## Four objects that must not be collapsed

Let

$$
T:X\longrightarrow X
$$

be a deterministic evolution on a pre-observable carrier, let

$$
q:X\longrightarrow Y
$$

be a readout, and let $\mu$ be a state or ensemble on $X$. These data have different outputs:

| Datum | Type | What it determines |
|---|---|---|
| $x\in X$ | pre-observable point | one determinate history $T^nx$ |
| $q$ | readout map | the accessible value $q(x)$ |
| $\mu$ | state on possible source points | predictive weights |
| $q_*\mu$ | observable law | weights of readout values |

For a fixed $x$, the value $q(T^nx)$ is determinate. If $q$ is many-to-one, knowing $q(x)$ does not determine $x$. That is failure of backward accessibility, not failure of forward determination.

Point-noninjection and categorical nonfaithfulness are related only after a carrier has been specified. A map of configuration spaces can identify source points, whereas a nonfaithful functor identifies arrows in hom-sets. Neither statement implies the other without a construction translating configurations into objects and transformations into arrows.

The pushforward law

$$
(q_*\mu)(B)=\mu(q^{-1}(B))
$$

depends on both $q$ and $\mu$. The same noninjective map can carry different probability laws, so noninvertibility alone cannot generate Born weights, a thermal distribution, or any other numerical probability.

## The exact finite conditional law

Take finite sets $X$ and $Y$, a surjection $q:X\to Y$, a deterministic map $T:X\to X$, and a full-support probability $\mu$ on $X$. Put

$$
\nu(y)=\sum_{q(x)=y}\mu(x),
\qquad
\mu(x\mid y)=\frac{\mu(x)}{\nu(y)}
\quad(q(x)=y).
$$

The one-step observable conditional law is

$$
\boxed{
K_\mu(y,y')
=
\sum_{q(x)=y}
\mu(x\mid y)\,
\mathbf 1_{\{q(Tx)=y'\}}.}
\tag{A1}
$$

This is an **[EXACT LEMMA]**. The source update is deterministic; the probability in (A1) expresses uncertainty about which point of the present fiber $q^{-1}(y)$ is actual. Changing $\mu$ generally changes $K_\mu$ without changing either $T$ or $q$.

There is an induced deterministic map $\bar T:Y\to Y$ satisfying

$$
q\circ T=\bar T\circ q
\tag{A2}
$$

if and only if $q(Tx)$ is constant on every fiber of $q$. Under this **strong deterministic lumpability** condition,

$$
K_\mu(y,\cdot)=\delta_{\bar T(y)}
$$

for every full-support $\mu$. Conversely, if $K_\mu(y,\cdot)$ is a Dirac measure for every $y$ for even one full-support $\mu$, then $q(Tx)$ must be constant on each fiber. A many-to-one readout can therefore leave observable dynamics deterministic. Gauge quotient is a basic example: if the fibers are gauge orbits and $qT$ is orbit-constant, quotienting introduces no observed chance. When (A2) fails, (A1) gives a one-step conditional kernel after a state has been chosen, but the full observed process need not be Markov: unresolved fiber information can reappear as memory.

The operator-algebraic analogue is equally strict. In the Heisenberg picture, let $J:\mathcal N\to\mathcal M$ be an accessible embedding, let $E:\mathcal M\to\mathcal N$ be unital and completely positive with $E\circ J=\operatorname{id}_{\mathcal N}$, and let $\alpha_t:\mathcal M\to\mathcal M$ be an automorphism group. The maps

$$
\Phi_t:=E\circ\alpha_t\circ J
$$

are operational channels. They form a semigroup only if an additional closure identity holds, for example

$$
E\circ\alpha_t\circ J\circ E\circ\alpha_s\circ J
=
E\circ\alpha_{t+s}\circ J.
\tag{A3}
$$

Complete positivity, probabilities, and the semigroup law are extra structure; none follows from the word *descent*.

## Every stationary stochastic law has a deterministic factor presentation

Let $Y$ be a standard measurable space and let $\mathbb P$ be a stationary probability law on the two-sided path space

$$
\Omega:=Y^{\mathbb Z}.
$$

The shift

$$
(S\omega)_n:=\omega_{n+1}
$$

is deterministic and invertible, stationarity says that it preserves $\mathbb P$, and the coordinate readout $q(\omega)=\omega_0$ obeys

$$
q(S^n\omega)=\omega_n.
$$

Thus every stationary stochastic process is the observable factor of an invertible deterministic measure-preserving system. This is an **[EXACT REPRESENTATION]**. It proves underdetermination of ontology by the observed law; it does not explain the law, privilege this enlarged path carrier, or prove that its inaccessible coordinates are physically real. The entire history has simply been placed into one source point.

This is the same caution as for Stinespring dilation. A channel can be represented inside a larger reversible system, but a representation theorem does not by itself identify the dilation space with ontology. [[algebra/nonfaithful-realization|Nonfaithful realization]] states that firewall categorically.

## What the Jacobian counterexample makes exact

The [[library/counterexamples-to-the-jacobian-conjecture/inq|2026 Jacobian counterexamples]] record polynomial maps

$$
F:\mathbb C^n\longrightarrow\mathbb C^n,
\qquad n>2,
$$

with constant nonzero Jacobian determinant that are nevertheless noninjective. For [[library/counterexample-to-the-jacobian-conjecture/inq|Alpöge's original three-dimensional map]],

$$
\det JF\equiv-2,
$$

while the generic fiber has three points. The inverse-function theorem supplies a local analytic inverse branch at every source point. The global inverse fails because the map is nonproper: sheets escape through infinity rather than meeting at a finite ramification point.

Gao's later tangent-sweep construction contains a different three-dimensional map with determinant $+2$ and generic degree four. The two examples make the same local--global point, but their numerical invariants must not be conflated.

This gives an exact local-to-global separation:

$$
\boxed{
\text{invertible differential everywhere}
\not\Longrightarrow
\text{globally accessible inverse}.}
\tag{A4}
$$

After restriction to a suitable target open locus on which the map is finite and the inverse branches remain separated, the branches form a finite etale cover with monodromy. [[a2-spectral-geometry-of-jacobian-counterexample-3d/inq|The workspace's $A_2$ inverse-cover computation]] identifies full $S_3$ monodromy for the three-sheeted member. There is no globally single-valued choice of inverse branch compatible with every loop.

The categorical vocabulary must remain exact:

- the inverse branches and their analytic continuation form a groupoid or covering datum;
- strict descent asks whether coherent local objects glue and may preserve all branch and stabilizer data;
- forgetting the branch label is a further nonfaithful map;
- a three-element fiber with the transitive $S_3$ action is $S_3/S_2$, not an $S_3$-torsor, because the action has stabilizers; a torsor description would require a free transitive action or passage to separately constructed principal data.

The Jacobian example therefore models inaccessible inverse determination, not probability. A probability appears only after a measure weights the sheets. Nor does its local Jacobian produce an arrow of time. It shows that locally reversible presentation and globally unavailable reconstruction can coexist.

## Sufficing reason and necessitating reason lie on a second axis

The programme's two species of reason are termini of explanation:

$$
\begin{aligned}
\text{necessitating reason}&\longrightarrow\text{the fact that obtains},\\
\text{sufficing reason}&\longrightarrow\text{a law over possible facts}.
\end{aligned}
$$

Accessibility is independent of that distinction. A necessitating reason may be inaccessible to the observer, while a sufficing law is accessible and predictively complete in the observable register. The proposed deterministic reading is therefore

$$
\boxed{
\text{inaccessible necessitating ground}
\xrightarrow{\text{nonfaithful readout + state}}
\text{accessible sufficing law}
\dashrightarrow
\text{recorded fact}.}
\tag{A5}
$$

The dashed arrow remains the factive problem. A probability measure, conditional expectation, or instrument calculates weights and post-readout states; it does not select the fact merely by being noninvertible. [[conservation-of-causal-charge/factive-descent-and-records|Factive descent and records]] owns that additional construction.

## Quantum and causal firewalls

Equation (A5) is compatible with a deterministic interpretation only after the quantum no-go theorems are paid in full. Bell excludes the package of Bell-local causation, measurement independence, and the relevant predetermined responses. Kochen--Specker excludes a global noncontextual valuation under its hypotheses. A deterministic pre-observable completion must therefore be contextual, nonlocal in the relevant Bell sense, reject another explicit hypothesis, or fail empirically. Declaring ordinary spacetime locality nonfundamental can open that logical door; it does not construct a model that reproduces the correlations.

Clock evolution and causal orientation also remain different. An invertible source shift, a noninvertible readout, a one-sided record extension, and a Lorentzian automorphism group have different carriers. The mass gap belongs to the generator of the recovered Lorentzian translation representation, not to the uncertainty kernel (A1), the entropy of $q_*\mu$, or the mixing rate of an auxiliary Markov description.

The lesson for [[contemporary-puzzles/yang-mills-mass-gap/descent-loss-cocycle-and-recovery-fork|the mass-gap descent problem]] is global. A locally nonsingular readout Jacobian or positive pointwise Hessian can coexist with globally unresolved sheets and poor behavior at infinity. The stopping condition must therefore be a global closed-range, Poincare, or spectral-coercivity estimate on the effective physical carrier. Local invertibility is not the gap; it explains how locally lawful appearance can fail to reveal its global determining reason.

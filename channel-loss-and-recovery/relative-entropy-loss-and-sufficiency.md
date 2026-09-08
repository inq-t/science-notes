# Relative-Entropy Loss and Sufficiency

A channel's relative-entropy loss measures distinguishability erased from a declared state pair. These nonnegative losses add with transported state arguments under composition, and their zero set is exact recovery. For restrictions of faithful normal states with finite Araki relative entropy, the same criterion is retention of the Connes cocycle. This is an information comparison, without an energy scale or an assumption of ontological randomness.

## Relative-entropy loss is an arrow cost

Use the Schrödinger convention: \(\Phi\) is a completely positive trace-preserving map from input to output density matrices. For faithful finite-dimensional states $\rho$ and $\sigma$, define

$$
\boxed{
\mathcal L_\Phi(\rho;\sigma)
:=
D(\rho\Vert\sigma)
-D(\Phi\rho\Vert\Phi\sigma).}
\tag{D1}
$$

Data processing gives

$$
\mathcal L_\Phi(\rho;\sigma)\geq0.
$$

For composable channels $\Phi$ and $\Psi$, direct cancellation gives the **[EXACT COCYCLE LAW]**

$$
\boxed{
\mathcal L_{\Psi\circ\Phi}(\rho;\sigma)
=
\mathcal L_\Phi(\rho;\sigma)
+
\mathcal L_\Psi(\Phi\rho;\Phi\sigma).}
\tag{D2}
$$

This is a state-pair-indexed additive valuation on channel arrows. It is not a single number attached to $\Phi$, a Noether charge, or a substance stored behind the wall. [[channel-loss-and-recovery/preserving-expectation-loss|A preserving expectation]] gives a stronger relative-entropy chain rule and an orthogonal tangent decomposition, using the restriction and recovery maps associated with the expectation. Equation (D2) applies to arbitrary finite-dimensional channels but supplies no orthogonal decomposition.

[[library/sufficiency-of-channels-over-von-neumann-algebras/inq|Petz sufficiency]] determines the zero set. Let $\Phi^\dagger$ denote the Hilbert--Schmidt adjoint. With inverses taken on supports, the finite-dimensional recovery map associated with $\sigma$ is

$$
\mathcal R_{\sigma,\Phi}(Y)
=
\sigma^{1/2}
\Phi^\dagger\!\left(
(\Phi\sigma)^{-1/2}
Y
(\Phi\sigma)^{-1/2}
\right)
\sigma^{1/2}.
\tag{D3}
$$

It recovers $\sigma$. On $\operatorname{supp}\Phi(\sigma)$ it is trace preserving; if that support is not the entire output space, it can be extended on the orthogonal complement to a CPTP recovery channel. Moreover,

$$
\mathcal L_\Phi(\rho;\sigma)=0
$$

if and only if
\(\mathcal R_{\sigma,\Phi}(\Phi\rho)=\rho\), with
\(\mathcal R_{\sigma,\Phi}(\Phi\sigma)=\sigma\). Zero residue means sufficiency for the declared state pair; positive residue means failure of exact recovery relative to that channel and pair. Sufficiency for a whole statistical family requires one common recovery channel, not a different reference-dependent recovery chosen pair by pair. Neither statement decides whether the underlying reality is determinate.

## Restriction loss and sufficiency in Type III

Restriction gives the same loss without a density-matrix presentation. Let

$$
\mathcal N\subseteq\mathcal M
$$

be a unital inclusion of von Neumann algebras and let \(\varphi,\sigma\) be faithful normal states with finite \(S_{\mathcal M}(\varphi\Vert\sigma)\). Data processing makes the restricted relative entropy finite as well, so the following difference never subtracts two infinities. Define the restriction loss

$$
\boxed{
\mathcal L_{\sigma,\mathcal N}(\varphi)
:=
S_{\mathcal M}(\varphi\Vert\sigma)
-
S_{\mathcal N}(\varphi|_{\mathcal N}\Vert
\sigma|_{\mathcal N})
\geq0.}
\tag{D5d}
$$

This uses no trace and is therefore compatible with Type III local algebras. [[library/sufficient-subalgebras-and-relative-entropy/inq|Petz's Theorem 4]] gives the exact zero criterion under these faithful and finite-entropy hypotheses:

$$
\boxed{
\mathcal L_{\sigma,\mathcal N}(\varphi)=0
\quad\Longleftrightarrow\quad
[D\varphi:D\sigma]_t\in\mathcal N
\ \text{for every }t\in\mathbb R,}
\tag{D5e}
$$

equivalently to the corresponding channel-sufficiency/generalized-expectation conditions. Petz calls the equality condition *weak sufficiency*. It does not by itself assert an ordinary expectation onto all of \(\mathcal N\) preserving both states. The local algebra loses no distinction relevant to the pair exactly when it retains their Connes cocycle. This gives a rigorous meaning to “something is forgotten in descent” without turning forgetting into ontological randomness.

An ordinary \(\sigma\)-preserving normal conditional expectation onto
\(\mathcal N\) exists exactly under
[[library/conditional-expectations-in-von-neumann-algebras/inq|Takesaki's modular-invariance condition]]. When that condition fails, [[library/conditional-expectations-and-a-theorem-of-takesaki/inq|the Accardi--Cecchini generalized expectation]] still supplies a state-dependent standard-form contraction. Thus the carrier map is available more generally than an idempotent expectation, but its existence alone contributes no stiffness.

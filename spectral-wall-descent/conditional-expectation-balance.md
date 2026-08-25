# Conditional Expectation, Lost Distinction, and Gained Entropy

A trace- or state-preserving conditional expectation supplies the first exact wall-crossing law matching the proposed ontology. It is nonunitary, idempotent, and genuinely forgetful. In the finite tracial model, the entropy gained after the wall is exactly the relative distinguishability lost to the chosen observable subalgebra, and its coincidence Hessian is the missing positive block of the common response form.

## The finite tracial theorem

Let \(\mathcal A\subseteq M_N(\mathbb C)\) be a finite-dimensional \(C^*\)-algebra equipped with the restriction of the ambient matrix trace \(\operatorname{Tr}\). Let \(\mathcal B\subseteq\mathcal A\) be a unital subalgebra and let

$$
E:\mathcal A\longrightarrow\mathcal B
$$

be the \(\operatorname{Tr}\)-preserving conditional expectation. It is unital, completely positive, idempotent, and \(\mathcal B\)-bimodular. Identify states with the usual density matrices satisfying \(\operatorname{Tr}\rho=1\), and set

$$
\bar\rho:=E(\rho).
$$

For every faithful density matrix \(\rho\in\mathcal A\) and faithful \(\sigma\in\mathcal B\), one has the **[EXACT PYTHAGOREAN IDENTITY]**

$$
\boxed{
D_{\mathcal A}(\rho\Vert\sigma)
=D_{\mathcal A}(\rho\Vert\bar\rho)
+D_{\mathcal B}(\bar\rho\Vert\sigma).}
$$

Indeed, \(\log\bar\rho,\log\sigma\in\mathcal B\), and trace preservation plus bimodularity imply

$$
\operatorname{Tr}(\rho b)
=\operatorname{Tr}(\bar\rho b)
\qquad(b\in\mathcal B).
$$

Expanding the three relative entropies then makes all cross terms cancel.

Because \(\log\bar\rho\in\mathcal B\), trace orthogonality gives directly

$$
\operatorname{Tr}(\rho\log\bar\rho)
=\operatorname{Tr}(\bar\rho\log\bar\rho).
$$

Hence one obtains the **[EXACT ENTROPY-GAIN IDENTITY]**

$$
\boxed{
\Sigma_E(\rho)
:=D(\rho\Vert\bar\rho)
=S(\bar\rho)-S(\rho)
\geq0.}
$$

No complementary environment and no unitary dilation has been used. The increase is a property of the noninvertible expectation itself.

## Entropy as anti-information in a declared register

For the maximally mixed reference \(\tau_N=\mathbf1/N\),

$$
D(\rho\Vert\tau_N)=\ln N-S(\rho).
$$

The Pythagorean identity becomes

$$
\boxed{
\underbrace{\ln N-S(\rho)}_{I_{\mathrm{pre}}}
=
\underbrace{\ln N-S(\bar\rho)}_{I_{\mathrm{obs}}}
+
\underbrace{S(\bar\rho)-S(\rho)}_{\Sigma_E}.}
$$

This is the precise finite meaning in which entropy is anti-information: relative distinction from the tracial state decreases by exactly the amount that entropy increases. The statement is not reference free. Changing the reference, algebra, or trace changes the decomposition.

When \(\mathcal B\) is commutative, its restricted state defines a probability law over characters. The ambient von Neumann entropy of \(\bar\rho\) equals the Shannon entropy of that law only for a rank-one atomic maximal abelian context. For \(\mathcal B=\bigoplus_i\mathbb CP_i\) with \(d_i=\operatorname{rank}P_i\),

$$
S(\bar\rho)
=H(p)+\sum_i p_i\log d_i.
$$

Neither quantity is the entropy of an actual fact. Conditioning on a realized character can reduce an observer's uncertainty even though the unconditioned wall state has larger entropy. Thus wall restriction, factual selection, and record formation are three different arrows.

## The BKM response split

Let \(\rho_t=\sigma+tX+O(t^2)\), with \(\sigma\in\mathcal B\) faithful and \(E\sigma=\sigma\), and let \(X=X^*\) satisfy \(\operatorname{Tr}X=0\). Using the density-tangent Hessian convention for the BKM metric, differentiation of the Pythagorean identity twice at \(t=0\) gives

$$
\boxed{
g^{\mathrm{BKM},\mathcal A}_\sigma(X,X)
=g^{\mathrm{BKM},\mathcal B}_\sigma(EX,EX)
+g^{\mathrm{BKM},\mathcal A}_\sigma((1-E)X,(1-E)X).}
$$

Polarization gives the corresponding bilinear equality. For a tangent family \(X_I\), define

$$
\begin{aligned}
G^{\mathrm{pre}}_{IJ}
&:=g_\sigma(X_I,X_J),\\
G^{\mathrm{obs}}_{IJ}
&:=g_\sigma(EX_I,EX_J),\\
G^{\mathrm{wall}}_{IJ}
&:=g_\sigma((1-E)X_I,(1-E)X_J).
\end{aligned}
$$

Then

$$
\boxed{
G^{\mathrm{pre}}_{IJ}
=G^{\mathrm{obs}}_{IJ}
+G^{\mathrm{wall}}_{IJ}.}
$$

This is the exact quadratic balance sought by [[program-core/common-response-matrix|the common response construction]]. It is a Pythagorean decomposition of response, not conservation of a scalar information substance. [[spectral-wall-descent/receipts/verify-spectral-wall.py|The finite receipt]] checks both the relative-entropy closure and its Hessian closure for a noncommuting \(M_3(\mathbb C)\) state.

## Nested expectations and scale towers

Let

$$
\mathcal M_0\supseteq\mathcal M_1\supseteq\mathcal M_2
$$

and let \(E_1:\mathcal M_0\to\mathcal M_1\) and \(E_2:\mathcal M_1\to\mathcal M_2\) extend to orthogonal projections for the same BKM inner product at one faithful reference fixed by both expectations. Writing \(E_{20}:=E_2E_1\), the two projection defects are orthogonal and give the **[EXACT NESTED PYTHAGOREAN IDENTITY]**

$$
\boxed{
\|X-E_{20}X\|_{\mathrm{BKM}}^2
=
\|X-E_1X\|_{\mathrm{BKM}}^2
+
\|E_1X-E_2E_1X\|_{\mathrm{BKM}}^2.}
$$

Thus lost quadratic distinction can add across a scale tower without being a conserved substance or a unitary environment. The common reference and common BKM projection structure are load bearing; two unrelated state-preserving expectations do not supply the identity by notation alone.

For a nontrivial center, a center-valued version requires coherently identified centers and sector-preserving expectations whose extensions satisfy these hypotheses in every sector. A scalar equality does not automatically lift to central order, and changing sector weights contributes the separate central Fisher term owned by [[program-core/center-valued-response|center-valued response and scalarization]].

## Equivariance through a family of broken contexts

Let a group \(G\) act by trace-preserving \(*\)-automorphisms \(\alpha_g\) on \(\mathcal A\), and let observable contexts be indexed by a homogeneous space \(G/H\). A \(G\)-equivariant family satisfies

$$
\alpha_g(\mathcal B_x)=\mathcal B_{gx},
\qquad
E_{gx}\circ\alpha_g
=\alpha_g\circ E_x.
$$

Then

$$
\Sigma_{E_{gx}}(\alpha_{g*}\rho)
=\Sigma_{E_x}(\rho).
$$

Here \(\alpha_{g*}\rho:=\alpha_g(\rho)\) uses the finite trace identification. The selected context has only its stabilizer \(H\) manifest, while the whole action groupoid \(G\ltimes G/H\) and the loss functional remain \(G\)-equivariant. This is symmetry maintained through observable symmetry breaking without a Noether-energy interpretation.

## The modular existence gate

The finite trace makes expectations look easier than they are. For a von Neumann inclusion \(\mathcal N\subseteq\mathcal M\) and faithful normal state \(\varphi\), a unique \(\varphi\)-preserving normal conditional expectation exists if and only if the Takesaki modular condition holds:

$$
\sigma_t^\varphi(\mathcal N)=\mathcal N
\qquad(t\in\mathbb R).
$$

In a finite atomic commutative context, continuous modular invariance forces the context into the centralizer of \(\varphi\). A generic measurement context therefore does not admit the expectation required by the exact theorem. The continuum wall must either select a modularly admissible context, use an instrument rather than an expectation, or replace the exact equality by a controlled inequality.

Jones index applies to subfactors, while Pimsner--Popa index treats more general expectations. If a normal expectation from a type-III factor onto a commutative algebra exists, it cannot have finite Pimsner--Popa index: finite-index expectations preserve the relevant type decomposition. The final observational step is consequently infinite-index or belongs to a different categorical construction. [[semiorthogonal-decompositions/entry|Semiorthogonal decompositions]] propose an exact categorical selection stage before this analytic gate; their projectors do not carry positivity or states and therefore do not bypass Takesaki's condition.

## The revised gravitational typing

The exact theorem stops at

$$
G^{\mathrm{pre}}
=G^{\mathrm{ret}}+G^{\mathrm{lost}}.
$$

For physical perturbations with classical asymptotically AdS duals, to second order about a vacuum CFT ball and in its AdS Rindler wedge, holographic relative-entropy results show that the controlled canonical-energy map uses the retained term:

$$
G^{\mathrm{ret}}
\stackrel{\mathrm{AdS\ calibration}}{=}
\mathfrak S^*\mathcal E_{\mathrm{can}}^{\mathrm{grav}},
$$

while in exact complementary-recovery code models the edge-area term is a separate central operator that cancels from fixed-code relative entropy. After fixed edge states and compatible central spectral area have been constructed, the coefficient weld is therefore

$$
\mathcal L_\chi(U)
\stackrel{?}{=}
\eta_*\mathcal A_D^Z(U)
$$

for every admissible patch, with \(\mathcal A_D^Z\) independently normalized. [[spectral-wall-descent/finite-index-area-weld|The finite-index area weld]] gives an exact product-edge debugging identity for the auxiliary tracial expectation, not a general single-expectation index--area theorem. [[spectral-wall-descent/ads-calibration-and-ds-carrier|The AdS/dS note]] states the retained-response calibration.

This refinement does not make \(G^{\mathrm{lost}}\) irrelevant. It remains the exact BKM cost of the expectation and the entropy gained by coarse graining. In the type-I product cell, the tracial defect complements a separately chosen input edge entropy inside one log-dimension identity. But that edge state need not be selected by the tracial expectation, and the lost block is not automatically the gravitational canonical-energy metric.

A completed construction still requires localization, tangent transport, fixed-edge-state selection, spectral area, covariance, Ward and Bianchi consistency, soldering, and a noncircular \(\eta_*\). Until those are supplied, \(\Sigma_E\) is lost relative distinction and gained observable entropy, while \(\mathcal L_\chi\) is only a candidate central geometry.

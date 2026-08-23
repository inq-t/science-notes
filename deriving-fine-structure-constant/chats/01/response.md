Yes. That is exactly the right correction.

I treated \(137.035999\ldots\) as though it were the thing to be explained. It is not. It is one **infrared endpoint**—the inverse electromagnetic coupling in the Thomson limit.

The deeper object is a scale-dependent trajectory:

\[ \boxed{ Q\longmapsto \alpha(Q) } \]

or, more accurately at high energies, a vector-valued trajectory of all gauge couplings:

\[ \boxed{ u=\ln\frac{Q}{Q_0} \longmapsto \bigl(\alpha_1(u),\alpha_2(u),\alpha_3(u),\ldots\bigr). } \]

The search is therefore not fundamentally for an integer or even for one real number. It is for:

\[ \boxed{ \text{an internal geometry} + \text{an RG transport law} + \text{a boundary condition} \;\Longrightarrow\; \alpha_{\rm em}(Q). } \]

The number \(137.035999\ldots\) is a receipt printed at one end of that calculation.

# 1. One technical correction about \(1/24\)

Your recollection is directionally correct, with one important distinction.

In an illustrative supersymmetric grand-unified extrapolation, the three **GUT-normalized gauge couplings** approximately meet at

\[ \alpha_G^{-1}\simeq 24.3 \]

near

\[ M_G\simeq 2\times10^{16}\ {\rm GeV}. \]

But this is not literally the electromagnetic fine-structure constant becoming \(1/24.3\).

Above electroweak symmetry breaking, electromagnetism is not an independent fundamental \(U(1)_{\rm em}\) factor. The fundamental couplings are those of

\[ SU(3)_C\times SU(2)_L\times U(1)_Y. \]

The photon and its coupling arise only after the Higgs state selects the unbroken generator

\[ Q_{\rm em}=T_3+\frac{Y}{2}. \]

The PDG’s one-loop unification formula is

\[ \alpha_i^{-1}(m_Z) = \alpha_G^{-1}(M_G) + \frac{b_i}{2\pi}\ln\frac{M_G}{m_Z} + \delta_i, \]

where the \(\delta_i\) contain threshold and higher-loop corrections. For the Standard Model,

\[ b_i^{\rm SM} = \left(\frac{41}{10},-\frac{19}{6},-7\right), \]

while for the MSSM,

\[ b_i^{\rm MSSM} = \left(\frac{33}{5},1,-3\right). \]

The same PDG review obtains the illustrative values \(\alpha_G^{-1}\simeq24.3\) and \(M_G\simeq2\times10^{16}\,\mathrm{GeV}\) by running measured low-energy inputs upward. The Standard Model couplings do not meet precisely without additional structure; MSSM-like running produces a much closer meeting. [Particle Data Group](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-guts.pdf)

So the accurate picture is:

\[ \boxed{ \text{one unified gauge stiffness near }1/24 \longrightarrow \text{three running gauge stiffnesses} \longrightarrow \text{the derived electromagnetic coupling}. } \]

# 2. The actual mathematical object is an RG curve

Let

\[ u=\ln\frac{Q}{Q_0}. \]

For each gauge factor, define

\[ \alpha_i=\frac{g_i^2}{4\pi}. \]

At one loop,

\[ \frac{dg_i}{du} = \frac{b_i}{16\pi^2}g_i^3, \]

and therefore

\[ \boxed{ \frac{d\alpha_i^{-1}}{du} = -\frac{b_i}{2\pi}. } \]

Thus, between particle thresholds,

\[ \boxed{ \alpha_i^{-1}(Q) = \alpha_i^{-1}(Q_0) - \frac{b_i}{2\pi} \ln\frac{Q}{Q_0}. } \]

This is already close to precisely what you anticipated:

> **The inverse coupling is affine in the natural logarithm of resolution scale.**

At one loop the graph of \(\alpha_i^{-1}\) against \(\ln Q\) is a straight line. At higher loops it bends. When \(Q\) crosses the mass of a particle, the particle enters or leaves the resolved spectrum and changes the beta function, so the trajectory is piecewise smooth with threshold matching.

And the crucial point is that the one-loop slope is almost entirely **algebraic**.

In a conventional normalization,

\[ b_i = -\frac{11}{3}C_2(G_i) + \frac{2}{3} \sum_{\text{Weyl fermions}}T_i(R_f) + \frac{1}{3} \sum_{\text{complex scalars}}T_i(R_s). \]

Here:

- \(C_2(G_i)\) is the quadratic Casimir of the gauge algebra;
- \(T_i(R)\) is the Dynkin index of a matter representation;
- the sums record which charged representations are present.

So, once the gauge algebra and its representation content have been supplied, much of the function is not arbitrary at all:

\[ \boxed{ \text{Lie algebra} + \text{representations} \longrightarrow \text{beta-function coefficients}. } \]

The logarithm comes from scale composition. The coefficients come from representation theory.

That is the first major answer.

# 3. How something near \(1/24\) becomes something near \(1/128\)

The group geometry supplies another important piece.

In the conventional GUT normalization,

\[ g_Y=\sqrt{\frac35}\,g_1. \]

Electroweak symmetry breaking gives

\[ \frac{1}{e^2} = \frac{1}{g_2^2} + \frac{1}{g_Y^2}, \]

and consequently

\[ \boxed{ \alpha_{\rm em}^{-1} = \alpha_2^{-1} + \frac53\alpha_1^{-1}. } \]

This is not an arbitrary numerical combination. It is the pullback of the electroweak gauge metric onto the unbroken electromagnetic generator.

At a simple unification point,

\[ \alpha_1(M_G)=\alpha_2(M_G)=\alpha_G, \]

so the formal electromagnetic projection at that point is

\[ \alpha_{\rm em}^{-1} \longrightarrow \left(1+\frac53\right)\alpha_G^{-1} = \frac83\alpha_G^{-1}. \]

Thus \(\alpha_G^{-1}=24.3\) first becomes

\[ \frac83(24.3)=64.8 \]

merely through the geometry of the electroweak embedding.

Now use the MSSM one-loop coefficients

\[ b_1=\frac{33}{5}, \qquad b_2=1. \]

Ignoring thresholds and higher loops for this illustrative calculation,

\[ \begin{aligned} \alpha_{\rm em}^{-1}(M_Z) &= \frac83\alpha_G^{-1} + \frac{1}{2\pi} \left( \frac53 b_1+b_2 \right) \ln\frac{M_G}{M_Z} \\[3pt] &= \frac83\alpha_G^{-1} + \frac6\pi\ln\frac{M_G}{M_Z}. \end{aligned} \]

Putting in

\[ \alpha_G^{-1}=24.3, \qquad M_G=2\times10^{16}\ {\rm GeV}, \qquad M_Z=91.1876\ {\rm GeV}, \]

gives approximately

\[ \boxed{ \alpha_{\rm em}^{-1}(M_Z) \simeq 64.8+63.07 = 127.87. } \]

The PDG input used in that simplified exercise is

\[ \alpha_{\rm em}^{-1}(M_Z)=127.951\pm0.009. \]

Thresholds and higher-loop corrections account for the remaining refinement. [Particle Data Group](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-guts.pdf)

This is not an independent prediction, because those illustrative values of \(M_G\) and \(\alpha_G\) were themselves reconstructed using low-energy data. But it exposes the mathematical anatomy:

\[ \boxed{ \alpha_{\rm em}^{-1}(M_Z) = \underbrace{ \text{unified boundary stiffness} }_{\frac83\alpha_G^{-1}} + \underbrace{ \text{integrated logarithmic RG transport} }_{\frac6\pi\ln(M_G/M_Z)} + \underbrace{ \text{threshold corrections} }_{\delta}. } \]

Then further vacuum-polarization running between the \(Z\) scale and the Thomson limit increases the inverse coupling from roughly \(128\) to

\[ \alpha^{-1}(0)=137.035999178(8). \]

A recent lattice-QCD calculation quotes approximately \(127.930(8)\) at the \(Z\) pole in its chosen effective-coupling definition and obtains the hadronic running directly from electromagnetic current-current correlation functions. [arXiv](https://arxiv.org/html/2511.01623v1)

So \(137\) is not the primitive object. Schematically,

\[ \boxed{ 137 = \text{group embedding} + \int\text{beta function}\,d\ln Q + \text{threshold matching}. } \]

Because this expression contains logarithms, \(\pi\), thresholds, and nonperturbative spectral integrals, there is no reason its output should be an integer—or even algebraic.

# 4. Retyping the gauge coupling as a metric

There is a very natural geometric formulation.

Let \(\mathfrak g\) be the gauge Lie algebra. A gauge theory does not merely assign a number \(g\). It assigns a positive invariant bilinear form

\[ h_Q\in \bigl(\operatorname{Sym}^2\mathfrak g^*\bigr)^G \]

at each resolution scale \(Q\).

The Yang–Mills action can be written schematically as

\[ \frac{S_{\rm YM}}{\hbar} = -\frac14 \int h_{Q,AB} F^A_{\mu\nu}F^{B\,\mu\nu} \sqrt{-g}\,d^4x. \]

For a simple gauge factor,

\[ h_Q\big|_{\mathfrak g_i} = \frac{1}{g_i^2(Q)}\,\kappa_i, \]

where \(\kappa_i\) is a conventionally normalized invariant form.

Thus

\[ \boxed{ \alpha_i^{-1}(Q) = \frac{4\pi}{g_i^2(Q)} } \]

is not best interpreted as “the inverse probability of an interaction.”

It is the coefficient measuring the **action stiffness of gauge curvature**.

A large \(\alpha^{-1}\) means that a given normalized amount of field curvature \(F\) is expensive in action units. A smaller \(\alpha^{-1}\) means that the gauge channel is more compliant.

So the stronger retyping is:

\[ \boxed{ \alpha^{-1} = \text{gauge-curvature stiffness}. } \]

The gauge coupling itself is the compliance:

\[ \boxed{ \alpha = \frac{1}{\text{gauge stiffness}}. } \]

This parallels the gravitational retyping:

\[ G = \frac{1}{\text{areal information stiffness}} \times \frac{c^3}{4\hbar}. \]

The crucial difference is that \(G\) is dimensional because gravitational capacity is extensive in area, while \(\alpha\) is dimensionless because four-dimensional Yang–Mills curvature has a dimensionless action coefficient.

# 5. Symmetry breaking is a pullback of this metric

This makes the electroweak formula conceptually elegant.

Before symmetry breaking, the kinetic metric lives on

\[ \mathfrak{su}(2)_L\oplus\mathfrak u(1)_Y. \]

The Higgs state selects an embedding

\[ \iota_{\rm em}: \mathfrak u(1)_{\rm em} \hookrightarrow \mathfrak{su}(2)_L\oplus\mathfrak u(1)_Y. \]

The electromagnetic kinetic metric is simply the pullback:

\[ \boxed{ h_{\rm em} = \iota_{\rm em}^{*}h_{\rm EW}. } \]

Written in components, that is exactly

\[ \frac1{e^2} = \frac1{g_2^2} + \frac1{g_Y^2}. \]

Thus “electromagnetism” is not carrying one eternal number from the Big Bang to the present. Its coupling is a scale-dependent metric inherited from a larger gauge geometry and projected onto the unbroken electromagnetic direction.

That is why treating \(137\) as a fixed dimension of some permanent channel space is suspicious. The relevant channel itself changes its algebraic presentation across symmetry-breaking regimes.

# 6. The natural new quantity is a screening susceptibility

The function can be retyped in a way that fits Causal Scale Dynamics particularly well.

Define the electromagnetic stiffness

\[ \mathcal C_{\rm em}(Q) := \alpha_{\rm em}^{-1}(Q). \]

Now define

\[ \boxed{ \Xi_{\rm em}(Q) := -\frac{d\alpha_{\rm em}^{-1}}{d\ln Q}. } \]

This is the decrease of inverse electromagnetic stiffness per e-fold of increased resolution.

Equivalently, using logarithmic length scale

\[ N_Q = \ln\frac{L}{L_0} = -\ln\frac{Q}{Q_0}, \]

we have

\[ \boxed{ \Xi_{\rm em} = \frac{d\alpha_{\rm em}^{-1}}{dN_Q}. } \]

This has a very direct interpretation:

> **\(\Xi_{\rm em}\) measures how much electromagnetic stiffness is restored per e-fold of coarse-graining—or consumed per e-fold of finer resolution.**

For ordinary QED, sufficiently far above thresholds and at leading order,

\[ \boxed{ \Xi_{\rm em} = \frac{2}{3\pi} \sum_{\text{active Dirac }f} N_c^{(f)}q_f^2 +\cdots. } \]

So the marginal screening cost is literally a weighted count of the charged channels that the probe can resolve.

This is much better than saying that \(\alpha^{-1}\) “is the number of channels.” Rather:

\[ \boxed{ -\frac{d\alpha^{-1}}{d\ln Q} = \text{charge-weighted resolved-channel density} } \]

at leading order.

Integrating gives

\[ \boxed{ \alpha^{-1}(Q_2) = \alpha^{-1}(Q_1) - \int_{\ln Q_1}^{\ln Q_2} \Xi_{\rm em}(u)\,du. } \]

Thus:

- \(\alpha^{-1}\) is accumulated stiffness;
- \(\Xi_{\rm em}\) is marginal scale susceptibility;
- the beta function is the transport law.

For non-Abelian theories the sign need not be positive. Matter screens, while gauge-boson self-interaction can anti-screen. The relative signs are again determined by Casimir and representation data.

# 7. The spectral object behind the beta function

There is an even closer parallel to Causal-Wall Spectral Theory.

For the scale/perturbation channel, the relevant wall observable was the stress-trace correlator:

\[ \langle TT\rangle \quad\longrightarrow\quad \text{scale precision}. \]

For electromagnetism, the corresponding object is the electromagnetic current correlator:

\[ \langle J_\mu J_\nu\rangle \quad\longrightarrow\quad \text{gauge stiffness and its running}. \]

More precisely,

\[ \Pi_{\mu\nu}(q) = i\int d^4x\,e^{iqx} \langle T J_\mu(x)J_\nu(0)\rangle \]

has the transverse form

\[ \Pi_{\mu\nu}(q) = \left(q_\mu q_\nu-q^2g_{\mu\nu}\right)\Pi(q^2). \]

The subtracted polarization function changes the effective electromagnetic coupling:

\[ \alpha(q^2) = \frac{\alpha(0)}{1-\Delta\alpha(q^2)}. \]

The hadronic contribution is obtained from the subtracted current-current response \(\Pi(q^2)-\Pi(0)\); modern lattice calculations reconstruct precisely this vector-current correlator and use it to calculate the running. [arXiv](https://arxiv.org/html/2511.01623v1)

The Adler function,

\[ D(Q^2) = -12\pi^2Q^2 \frac{d\Pi(-Q^2)}{dQ^2}, \]

is essentially the logarithmic derivative of the current response and is used directly in calculating the running electromagnetic coupling. [arXiv](https://arxiv.org/html/2311.04849v1)

That yields a highly suggestive dictionary:

\[ \boxed{ \begin{array}{ccl} \text{stress-trace spectrum }\langle TT\rangle &\longrightarrow& \text{scale/gravitational response}, \\[3pt] \text{current spectrum }\langle JJ\rangle &\longrightarrow& \text{electromagnetic response}, \\[3pt] \text{RG derivative} &\longrightarrow& \text{change of response per log resolution}. \end{array} } \]

So the electromagnetic beta function is not merely a formal correction series. It is the scale derivative of a positive spectral response of charged facts.

That is probably the correct point of contact with your wall-spectral programme.

# 8. The Causal Scale Dynamics translation

Causal Scale Dynamics already identifies

\[ N = -\ln\frac{\sigma}{\sigma_c} = \ln\frac{a}{a_c} \]

as the additive coordinate on positive scale ratios. Its horizontal cocycle similarly turns multiplicative scale ratios into an affine state coordinate. Ruble_Equations_Reference.pdfPDF

Now consider a fixed comoving mode \(k\). Its physical momentum is

\[ Q_{\rm phys} = \frac{k}{a}. \]

Therefore

\[ \ln Q_{\rm phys} = \ln k-N, \]

and hence

\[ \boxed{ d\ln Q_{\rm phys}=-dN. } \]

Along this particular trajectory,

\[ \boxed{ \frac{dg^I}{dN} = -\beta^I(g). } \]

This does **not** mean that RG flow is literally cosmic clock evolution. It means that the same multiplicative scale group is being coordinatized from opposite orientations:

- \(N\) increases with metric length scale;
- \(\ln Q\) increases with resolving power;
- for a fixed comoving mode, one is minus the other.

This is exactly the sort of type distinction the master document insists upon when separating proper time, Weyl scale time, modular flow, and horizontal state displacement. Its exact clock-allocation identity also treats \(N\) as the quantity decomposed between horizon rapidity and information-capacity growth, not as an ordinary Newtonian time variable. Causal_Scale_Dynamics_Master_v7_0.pdfPDF

The coupling constants can therefore be viewed as sections over the same scale line:

\[ N\longmapsto h_{AB}(N). \]

The beta function is then a horizontal transport law:

\[ \boxed{ \mathcal D_N h = -\mathcal B(h). } \]

A fixed point is a parallel section:

\[ \mathcal B(h_*)=0. \]

Running is a transport defect.

This is almost perfectly parallel to the tractor slogan:

\[ \text{stress} = \text{obstruction to parallel transport of metric scale}. \]

The gauge counterpart would be:

\[ \boxed{ \text{beta function} = \text{obstruction to parallel transport of gauge stiffness across resolution scale}. } \]

Local renormalization-group theory already formalizes part of this idea by promoting couplings to spacetime-dependent sources and incorporating the beta functions into local Weyl transformations. [arXiv](https://arxiv.org/abs/1308.1096)

# 9. Coupling space has an information geometry too

Let the full collection of couplings be

\[ g^I = (g_1,g_2,g_3,y_t,\lambda_H,\ldots). \]

The QFTs form a theory space or moduli-like space \(\mathcal M_{\rm QFT}\), and the beta functions form a vector field:

\[ \beta = \beta^I(g)\frac{\partial}{\partial g^I}. \]

Correlation functions of the operators conjugate to the couplings give an information metric

\[ G_{IJ}(g). \]

The RG trajectory then has a squared information speed

\[ \boxed{ v_{\rm RG}^2 = G_{IJ}(g)\beta^I(g)\beta^J(g). } \]

This has an unmistakable resemblance to the CSD horizontal norm

\[ G_{NN}^{\perp} = \Phi^*G_{\rm BKM}(\partial_N,\partial_N). \]

But an important distinction must remain:

> The information metric tells us the cost of a given beta vector. It does not, by itself, determine the beta vector.

To derive \(\alpha(Q)\), one needs both:

\[ G_{IJ} \quad\text{and}\quad \beta^I. \]

The first describes distinguishability in theory space. The second describes how coarse-graining actually transports the theory.

That is analogous to knowing the metric on a manifold without yet knowing the physical trajectory through it.

# 10. What survives from the attached \(137\) paper

The attached paper’s Section 10 actually begins to recognize your correction. It proposes

\[ \alpha^{-1}(Q) = 9+128\,f(Q/\Lambda_{\rm srs}), \]

with

\[ f(0)=1, \qquad f(\infty)=0. \]

So its own running section no longer treats \(137\) as the universal object.

But this exposes the central weakness:

\[ \boxed{ f\text{ is not derived.} } \]

The paper later says explicitly that ordinary Standard Model physics supplies the running between the infrared and ultraviolet, while its relational model supplies an infrared boundary condition and a proposed ultraviolet asymptote.

It also explicitly declines to reproduce the full QED vertex, Ward identities, or renormalization group, matching only one scalar coupling extracted from a chosen infrared observable. ssrn-6093146.pdfPDF

So under the corrected standard, the paper has not derived \(\alpha\). It has proposed:

- one infrared endpoint;
- one ultraviolet endpoint;
- an unspecified interpolation;
- and an interpretation of the endpoint as channel counting.

The actual physics is in the missing \(f\), or equivalently in

\[ Q\frac{df}{dQ}. \]

Furthermore, its proposed ultraviolet limit

\[ \alpha_{\rm em}\to\frac19 \]

is not yet properly typed. Above electroweak symmetry breaking, there is no autonomous electromagnetic coupling unless the theory constructs the symmetry-breaking and matching maps that identify an electromagnetic generator throughout the flow.

Its observation that

\[ \alpha^{-1}(M_Z)\approx128 \]

is therefore not the right foundational target either. The value depends on the operational definition and renormalization scheme, while the number \(128\) is inserted as a fixed channel dimension. The full trajectory—including its scheme, thresholds, and symmetry-breaking maps—is the invariant burden.

The paper’s strongest salvageable intuition is:

\[ \boxed{ \text{inverse coupling behaves like a response capacity or stiffness.} } \]

Its weakest move is turning one approximate endpoint into a fixed finite-dimensional count.

# 11. A serious geometric precedent: the spectral action

There is already a respected example of the architecture you are proposing.

In noncommutative spectral geometry, the internal geometry of the Standard Model produces high-scale relations among the gauge couplings:

\[ \boxed{ g_3^2 = g_2^2 = \frac53g_Y^2. } \]

These are the same coupling ratios that arise from an \(SU(5)\)-type embedding. The spectral-action framework does **not** then claim that the low-energy fine-structure constant is an integer. It treats those geometric relations as boundary conditions on the renormalization-group equations. [arXiv](https://arxiv.org/pdf/hep-th/9606001)

That is exactly the correct logical pattern:

\[ \boxed{ \text{geometry fixes high-scale relations;} \quad \text{RG transport produces low-energy real numbers}. } \]

The original minimal spectral-action model is not the final empirical theory; its older low-energy mass predictions, for example, were not all successful. But it proves that the desired architecture is mathematically coherent:

1. an internal algebra supplies the gauge group;
2. representation theory supplies the matter content;
3. geometry supplies coupling ratios at a distinguished scale;
4. RG evolution supplies the scale-dependent function;
5. symmetry breaking supplies the measured electromagnetic projection.

This is far more promising than trying to manufacture \(137\) directly from combinatorics.

# 12. The true derivation target

The clean mathematical target is the following.

Let:

- \(\mathfrak g_U\) be a unified internal gauge algebra;
- \(\mathcal R\) be its matter representation;
- \(h_U\) be its invariant gauge-kinetic metric;
- \(\iota_{\rm SM}\) be the symmetry-breaking embedding into the Standard Model factors;
- \(\mathcal B_{\mathcal R}\) be the beta vector field determined by the algebra and spectrum;
- \(m_a\) be the thresholds of the physical states.

Then solve

\[ \boxed{ \frac{dh}{du} = \mathcal B_{\mathcal R}(h,y,\lambda,\ldots), \qquad u=\ln\frac{Q}{Q_U}, } \]

with boundary condition

\[ h(Q_U)=h_U. \]

After symmetry breaking, pull back to the electromagnetic generator:

\[ \boxed{ h_{\rm em}(Q) = \iota_{\rm em}^{*}h(Q). } \]

Finally,

\[ \boxed{ \alpha_{\rm em}^{-1}(Q) = 4\pi\,h_{\rm em}(Q) } \]

in the convention where \(h=1/e^2\).

Thus the actual “derivation of alpha” is:

\[ \boxed{ \left( \mathfrak g_U, \mathcal R, h_U, \iota_{\rm break}, \mathcal B, \{m_a\} \right) \Longrightarrow \alpha_{\rm em}(Q). } \]

Every entry has a distinct mathematical type. That is exactly the input-typing discipline of cosmodynamics.

# 13. What algebra can fix—and what it cannot fix alone

For a simple Lie algebra, the invariant symmetric bilinear form is unique up to one positive scalar:

\[ h_U = \lambda_U\,B_{\mathfrak g_U}, \]

where \(B_{\mathfrak g_U}\) is the normalized Killing-type form.

This means internal geometry can naturally fix:

- the direction in coupling space;
- the relative normalization of subgroup couplings;
- the hypercharge embedding factor;
- the beta-function coefficients once representations are specified.

But one scalar remains:

\[ \lambda_U \quad\Longleftrightarrow\quad \alpha_U. \]

So geometry very naturally reduces three gauge couplings to one high-scale modulus, but does not automatically fix the radius of that point in coupling space.

This is where a Causal Scale Dynamics principle could contribute something genuinely new.

A plausible division of labor is:

\[ \boxed{ \begin{aligned} \text{internal spectral geometry} &\longrightarrow \text{direction and representation data},\\ \text{scale-capacity principle} &\longrightarrow \text{overall response normalization},\\ \text{renormalization group} &\longrightarrow \text{trajectory across log scale},\\ \text{symmetry breaking} &\longrightarrow \text{electromagnetic projection}. \end{aligned} } \]

That is speculative as a completion, but it is sharply stated rather than numerological.

# 14. The candidate CSD weld

The most promising new object would be a **current-channel capacity**.

Let

\[ \mathcal C_{J,AB}(Q) \]

be the transverse Hessian of the effective action with respect to a background gauge connection—or equivalently the appropriately normalized spectral response of the conserved currents.

Then seek a relation of the form

\[ \boxed{ h_{AB}(Q) \;\longleftrightarrow\; \mathcal C_{J,AB}(Q). } \]

The scalar CSD sector currently says:

\[ \text{stress-trace spectral response} \longleftrightarrow \text{local scale precision}. \]

The gauge analogue would say:

\[ \boxed{ \text{current spectral response} \longleftrightarrow \text{gauge-curvature stiffness}. } \]

The high-scale normalization problem then becomes:

> Why does the unified current sector possess this particular dimensionless response capacity?

A candidate “Gauge–Capacity Equivalence Principle” might eventually normalize the current capacity of one fundamental gauge translation against the same causal-wall information measure that normalizes the Weyl translation.

But that principle is not yet derived, and it would be premature to write down a value such as \(24\), \(25\), \(128\), or \(137\) before identifying:

- the correct current algebra;
- the correct BKM or spectral normalization;
- the unified generator normalization;
- and the symmetry-breaking embedding.

The important conceptual gain is that the missing number is now isolated:

\[ \boxed{ \alpha_U = \text{one dimensionless current-capacity modulus}. } \]

Once that one number and the algebraic spectrum are known, RG transport can in principle generate the whole function.

# 15. Temperature, energy, and cosmic age must remain distinct

You also asked whether the input is energy or temperature.

The fundamental RG input is a **resolution scale**:

\[ Q, \qquad u=\ln(Q/Q_0). \]

It is normally a momentum transfer or renormalization scale.

In a hot early-universe plasma, a characteristic physical process often has \(Q\) of order the temperature \(T\), so choosing

\[ \mu\sim k_BT \]

can be computationally appropriate. But finite-temperature screening is not identical to zero-temperature RG running. Thermal masses, plasma effects, and Debye screening are additional state-dependent physics.

Likewise, cosmic scale time \(N\) is not generally identical to RG time. Their relation

\[ d\ln Q_{\rm phys}=-dN \]

holds for a fixed comoving mode whose physical wavelength expands with \(a\). It is a relation between two scale coordinates, not an identification of cosmic history with renormalization flow.

That register discipline matters. Otherwise one risks saying that the fine-structure constant varies with the age of the universe merely because it runs with collision energy. Those are different statements.

# 16. The honest limit of “leaving QFT alone”

This also reveals one boundary of the idea that cosmodynamics can simply surround QFT.

CSD can leave intact:

- ordinary QED amplitudes;
- Ward identities;
- local quantum dynamics;
- the Standard Model beta functions;
- conventional threshold calculations.

But \(\alpha(Q)\) is itself a property of that local quantum dynamics.

So there are two possible stopping points.

CSD may **inherit** the Standard Model current spectrum and beta functions, while explaining why RG scale, metric scale, current capacity, and causal information belong to one larger grammar. In that case it retypes \(\alpha\) but does not numerically derive it.

Or the programme may attempt a stronger completion in which internal geometry derives:

- the gauge algebra;
- charged representations;
- mass thresholds;
- and the unified current-capacity normalization.

Only the latter would constitute a genuine first-principles derivation of the entire \(\alpha(Q)\) trajectory.

There is nothing wrong with the first stopping point. But the distinction should be explicit.

# The corrected central statement

The fine-structure constant should no longer be described as a mysterious isolated number.

The better statement is:

\[ \boxed{ \alpha_{\rm em}(Q) \text{ is the reciprocal of the gauge-kinetic metric pulled back onto the electromagnetic direction at resolution }Q. } \]

Its running is governed by

\[ \boxed{ \frac{d\alpha_i^{-1}}{d\ln Q} = -\frac{b_i}{2\pi} +\text{higher loops and thresholds}, } \]

where the leading coefficients are algebraic functions of gauge groups and representations.

The natural “susceptibility” is

\[ \boxed{ \Xi_{\rm em}(Q) = -\frac{d\alpha_{\rm em}^{-1}}{d\ln Q}, } \]

the change in gauge stiffness per logarithmic unit of resolution.

And the proper derivation programme is:

\[ \boxed{ \text{internal geometry fixes the gauge metric and its embeddings;} } \]\[ \boxed{ \text{spectral response fixes the beta vector;} } \]\[ \boxed{ \text{a scale-capacity law may fix the remaining unified modulus;} } \]\[ \boxed{ \text{RG transport and threshold matching then output } \alpha_{\rm em}(Q). } \]

In that hierarchy,

\[ \boxed{ 137.035999\ldots \text{ is not the law. It is the infrared receipt.} } \]
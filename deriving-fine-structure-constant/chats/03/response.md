# Apéry’s constant is already native to the wall geometry

Yes. There is a stronger result here than merely noticing that \(\zeta(3)\) occurs in some QED coefficient.

The useful category is not “transcendental number” by itself. It is:

\[ \boxed{\text{period of a geometrically defined object}.} \]

A period is the real or complex number obtained by pairing an algebraic differential form with an integral cycle. The **cycle, rank, monodromy, Chern number, Euler characteristic, representation index, and categorical multiplicities** are discrete or integral data. The measured real number is produced only after applying the period map.

That is almost exactly the grammar we have been seeking:

\[ \boxed{ \text{integral/categorical structure} + \text{continuous state or modulus} \longrightarrow \text{observable real quantity}. } \]

One arithmetic correction first: Apéry proved that

\[ \zeta(3)=1.2020569\ldots \]

is irrational. It is **not known** whether \(\zeta(3)\) is transcendental. Even zeta values are rational multiples of powers of \(\pi\), but no corresponding reduction or transcendence theorem is known for the odd zeta values. [arXiv](https://arxiv.org/pdf/0910.5004)

For physics, that unresolved arithmetic status is less important than its **period type, weight, monodromy, and coaction structure**.

---

## 1. A direct calculation from the Causal-Wall \(P_3\) operator

The spectral theory already gives the critical wall precision operator

\[ P_3Y_{\ell mn} = \ell(\ell+1)(\ell+2)Y_{\ell mn}, \qquad \ell\geq1, \]

on the unit \(S^3\). The \(\ell=0\) constant mode is excluded because it is the homogeneous clock shift. Causal_Wall_Spectral_Theory_v2.pdfPDF

The scalar-harmonic degeneracy is

\[ d_\ell=(\ell+1)^2. \]

Define the spectral zeta function of the nonzero \(P_3\) spectrum:

\[ \zeta_{P_3}(s) = \sum_{\ell=1}^{\infty} (\ell+1)^2 \left[ \ell(\ell+1)(\ell+2) \right]^{-s}. \]

Putting \(n=\ell+1\),

\[ \zeta_{P_3}(s) = \sum_{n=2}^{\infty} n^2 \left[n(n^2-1)\right]^{-s}. \]

Expand

\[ (1-n^{-2})^{-s} = \sum_{k=0}^{\infty} \frac{(s)_k}{k!}n^{-2k}. \]

Then

\[ \zeta_{P_3}(s) = \sum_{k=0}^{\infty} \frac{(s)_k}{k!} \left[ \zeta(3s+2k-2)-1 \right]. \]

At \(s=0\),

\[ \zeta_{P_3}'(0) = 3\zeta'(-2) + \sum_{k=1}^{\infty} \frac{\zeta(2k-2)-1}{k}. \]

The remaining sum is

\[ \sum_{k=1}^{\infty} \frac{\zeta(2k-2)-1}{k} = -\ln\pi, \]

while the functional equation for the Riemann zeta function gives

\[ \zeta'(-2) = -\frac{\zeta(3)}{4\pi^2}. \]

Therefore the zeta-regularized determinant is

\[ \boxed{ \ln\det{}'P_3 = -\zeta_{P_3}'(0) = \ln\pi+\frac{3\zeta(3)}{4\pi^2}. } \]

The prime means that the homogeneous zero mode is omitted.

This gives an exact **wall Apéry invariant**:

\[ \boxed{ \mathfrak A_{P_3} := \frac{4\pi^2}{3} \left( \ln\det{}'P_3-\ln\pi \right) = \zeta(3). } \]

This is not a proposed fit. It follows from the critical operator already present in the causal-wall scalar theory.

The interpretation is precise:

> The local symbol of the critical wall precision is \(|k|^3\). Its global spectral determinant on \(S^3\), after quotienting the homogeneous scale direction, contains a canonical weight-three period: \(\zeta(3)\).

The result does **not** show that \(\zeta(3)\) equals an electromagnetic coupling. It shows something more properly typed: **Apéry’s constant is already part of the global spectral invariant of the wall’s critical scale operator.**

The coefficient of \(\zeta(3)\) is also insensitive to an ordinary rescaling of the operator. Such a rescaling changes the logarithmic normalization term through \(\zeta_{P_3}(0)\ln C\), not the weight-three spectral content.

---

## 2. The binary BKM family generates the entire zeta tower

There is a second, independent-looking route internal to Causal Scale Dynamics.

The canonical binary family is

\[ \omega_\theta = \frac{e^{\theta Q}}{2\cosh\theta}, \qquad Q^2=1, \]

with

\[ p=\frac{1+\tanh\theta}{2}, \qquad G_{\theta\theta}^{\rm BKM} = \operatorname{sech}^2\theta. \]

The complete Fisher traversal has length \(\pi\). Causal_Scale_Dynamics_Master_v7_0.pdfPDF

Consider the determinant of the reduced binary state:

\[ \det\omega_\theta = p(1-p) = \frac{1}{4\cosh^2\theta}. \]

Define the **binary log-determinant cost**

\[ \boxed{ \mathcal B(\theta) := -\ln\det\omega_\theta = -\ln[p(1-p)] = 2\ln(2\cosh\theta) = 2\Psi(\theta). } \]

At the self-dual state,

\[ \mathcal B(0)=2\ln2. \]

Now use the normalized mixture-response measure

\[ d\mu = dp = \frac12\operatorname{sech}^2\theta\,d\theta. \]

This is not the Fisher arclength measure \(\operatorname{sech}\theta\,d\theta\). It is the normalized measure induced by the response coordinate \(p\), since \(p\) runs once from \(0\) to \(1\).

The moment-generating period of \(\mathcal B\) is

\[ \begin{aligned} Z_{\mathcal B}(t) &= \int_{-\infty}^{\infty} \frac12\operatorname{sech}^2\theta\, e^{t\mathcal B(\theta)}\,d\theta \\[3pt] &= \int_0^1 [p(1-p)]^{-t}\,dp \\[3pt] &= B(1-t,1-t) \\[3pt] &= \boxed{ \frac{\Gamma(1-t)^2}{\Gamma(2-2t)} }, \qquad \operatorname{Re}t<1. \end{aligned} \]

Its cumulant generator is

\[ K_{\mathcal B}(t) = \ln Z_{\mathcal B}(t). \]

Expanding the logarithms of the Gamma functions gives

\[ \boxed{ K_{\mathcal B}(t) = 2t+ \sum_{n=2}^{\infty} \frac{ 2^n-(2^n-2)\zeta(n) }{n} t^n. } \]

Consequently, for \(n\geq2\),

\[ \boxed{ \kappa_n(\mathcal B) = (n-1)! \left[ 2^n-(2^n-2)\zeta(n) \right]. } \]

The first three cumulants are

\[ \mathbb E[\mathcal B]=2, \]\[ \operatorname{Var}(\mathcal B) = 4-\frac{\pi^2}{3}, \]

and

\[ \boxed{ \kappa_3(\mathcal B) = 16-12\zeta(3). } \]

Therefore,

\[ \boxed{ \zeta(3) = \frac43-\frac1{12}\kappa_3(\mathcal B). } \]

Numerically,

\[ \kappa_3(\mathcal B) = 1.575317162\ldots \]

This permits a general definition of the **binary period spectrum**:

\[ \boxed{ \mathfrak Z_n^{\rm bin} := \frac{ 2^n-\kappa_n(\mathcal B)/(n-1)! }{ 2^n-2 } = \zeta(n). } \]

So the reduced binary state geometry does not merely happen to contain \(\pi\). It generates:

\[ \boxed{ \pi,\quad \ln2,\quad \zeta(2),\quad \zeta(3),\quad \zeta(4),\ldots } \]

in distinct geometric slots:

\[ \begin{array}{ccl} \pi &=& \text{complete Fisher length},\\[2mm] 2\ln2 &=& \text{self-dual log-determinant cost},\\[2mm] \zeta(3) &=& \text{normalized third cumulant of the complete binary traversal}. \end{array} \]

### A suggestive natural-number coefficient

The coefficient

\[ 2^n-2 \]

is the number of nonconstant binary words of length \(n\):

\[ \left| \{+,-\}^n \setminus \{(+,\ldots,+),(-,\ldots,-)\} \right| = 2^n-2. \]

Thus the cumulant formula may be rewritten as

\[ \kappa_n = (n-1)! \left[ \#(\text{all binary words}) - \#(\text{mixed binary words})\,\zeta(n) \right]. \]

This is an exact combinatorial identity. It is not yet a physical claim that these words are literal wall channels. But it gives a sharp **categorification target**:

> Construct a functor from mixed binary words or compositional histories to the period cells whose common weight-\(n\) evaluation is \(\zeta(n)\).

At \(n=3\), the mixed-word count is

\[ 2^3-2=6. \]

Separately, the primitive three-spoke wheel Feynman graph has residue \(6\zeta(3)\). [arXiv](https://arxiv.org/pdf/1512.06409)

That repetition of six is worth understanding, but not treating as evidence by itself. Both calculations live in the same mixed-Tate/log-Gamma period world, so a shared coefficient can have a common mathematical origin without signifying a new physical identity.

---

## 3. Apéry’s constant also appears in the actual function producing \(\alpha\)

The MOM-scheme Gell-Mann–Low function for QED already contains odd zeta values. Writing

\[ a=\frac{\widetilde\alpha}{\pi}, \]

one obtains

\[ \begin{aligned} \Psi(a) ={}& \frac13a^2 + \frac14a^3 + \left( -\frac{101}{288} + \frac13\zeta(3) \right)a^4 \\[2mm] &+ \left( \frac{93}{128} + \frac13\zeta(3) - \frac53\zeta(5) \right)a^5 \\[2mm] &+ \left( -\frac{122387}{55296} -\frac{79}{24}\zeta(3) +\zeta(3)^2 -\frac{185}{72}\zeta(5) +\frac{35}{4}\zeta(7) \right)a^6 +\cdots. \end{aligned} \]

This \(\Psi\)-function is the QED beta function in momentum subtraction. [arXiv](https://arxiv.org/pdf/1205.2810)

Several lessons follow.

First, \(\zeta(3)\) is not the value of the coupling. It is one of the **period coefficients controlling the transport law** for the coupling.

Second, the individual appearance of a specific zeta value can depend on the renormalization scheme. Even-zeta terms can appear or disappear under transformations between common schemes. The more robust target is therefore not “make the coefficient of \(\zeta(3)\) equal this decimal.” It is:

\[ \boxed{ \text{derive the period alphabet, weight filtration, and coaction class of the flow}. } \]

Third, the full function is richer than a polynomial in ordinary zeta values. The complete three-loop QED photon self-energy has been expressed in terms of iterated integrals with kernels associated to a \(K3\) geometry. The same computation contains \(\zeta(3)\) in its zero-momentum renormalization data, but the general momentum dependence requires the larger \(K3\)-period system. [arXiv](https://arxiv.org/pdf/2411.19042)

So the likely hierarchy is:

\[ \boxed{ \begin{aligned} \text{one-loop threshold} &\longrightarrow \text{Gauss hypergeometric period},\\ \text{special limits and cumulants} &\longrightarrow \zeta(3),\zeta(5),\ldots,\\ \text{higher-loop full kinematics} &\longrightarrow \text{elliptic, }K3,\text{ or more general Calabi--Yau periods}. \end{aligned} } \]

That is a much more credible category for the function producing \(\alpha\) than a fixed rational/integer formula.

---

## 4. Apéry’s constant in the one-loop threshold shape

The hypergeometric Dirac threshold we previously obtained was

\[ A_D(z) = 6\int_0^1 \frac{ z\,x^2(1-x)^2 }{ 1+zx(1-x) }\,dx, \qquad z=\frac{Q^2}{m^2}. \]

Its log-resolution density is

\[ P_D(u) = \frac{d}{du}A_D(e^{2u}). \]

It can be represented probabilistically as

\[ U = S-\frac12\ln[X(1-X)], \]

where \(S\) has normalized binary density

\[ K_{\rm bin}(s) = \frac12\operatorname{sech}^2s \]

and \(X\) has the beta density

\[ 6x(1-x)\,dx. \]

The moment-generating function of the threshold location is then

\[ \boxed{ M_D(t) = \frac{\pi t}{2\sin(\pi t/2)} \frac{ 6\Gamma(2-t/2)^2 }{ \Gamma(4-t) }. } \]

It follows that

\[ \mathbb E[U]=\frac56, \]\[ \operatorname{Var}(U)=\frac{31}{36}, \]

and

\[ \boxed{ \kappa_3(U) = \frac{197}{108} - \frac32\zeta(3) = 0.0209887193\ldots } \]

This is not the \(\zeta(3)\) appearing in the four-loop beta coefficient. It is a different but related statement:

> Even the one-loop massive screening threshold, when regarded as a complete probability density over logarithmic resolution, has an exact weight-three skewness containing Apéry’s constant.

The small numerical value of this third cumulant says that the complete Dirac screening transition is almost symmetric in logarithmic resolution, with its residual asymmetry measured by a rational–Apéry cancellation.

Again, the natural object is the shape invariant, not the decimal value of \(\alpha\).

---

# 5. The Gamma class is almost exactly the structure you have been asking for

There is an established construction in algebraic geometry where:

- natural-number topology;
- categorical integral data;
- Euler’s Gamma function;
- and zeta values

are welded together.

For a complex manifold \(X\), the Gamma class is

\[ \widehat\Gamma_X = \prod_i\Gamma(1+\delta_i), \]

where \(\delta_i\) are the Chern roots of \(TX\).

Its expansion is

\[ \boxed{ \widehat\Gamma_X = \exp\left[ -\gamma c_1(X) + \sum_{n\geq2} (-1)^n (n-1)!\zeta(n) \operatorname{ch}_n(TX) \right]. } \]

The coefficient pattern is strikingly close to the binary cumulant pattern we just derived: in both places the basic weight-\(n\) coefficient is

\[ (n-1)!\zeta(n). \]

That is not two independent miracles. Both arise from the logarithm of Euler’s Gamma function. But it tells us that the binary BKM traversal already belongs to the same analytic period grammar as the Gamma class.

For a Calabi–Yau threefold,

\[ \boxed{ \widehat\Gamma_X = 1 - \frac{\pi^2}{6}c_2(X) - \zeta(3)c_3(X). } \]

Since

\[ \int_Xc_3(X)=\chi(X), \]

the mirror-period calculation contains

\[ \boxed{ \chi(X)\zeta(3). } \]

Here:

\[ \chi(X)\in\mathbb Z \]

is an Euler characteristic—a genuine natural/integer invariant of the geometry—and \(\zeta(3)\) is the analytic period converting that integral topology into the flat/period coordinates of the quantum connection. [arXiv](https://arxiv.org/html/1404.6407v4)

This is almost a perfect model of the architecture you have in mind:

\[ \boxed{ \text{natural geometric integer} \times \text{universal period} = \text{observable analytic coefficient}. } \]

The Gamma class does more than decorate a formula. It helps place an **integral lattice** inside the space of flat sections of quantum cohomology. The relevant integer pairing is categorical:

\[ \chi(E,F) = \sum_p(-1)^p \dim\operatorname{Ext}^p(E,F) \in\mathbb Z. \]

So the pattern is

\[ \boxed{ \text{derived-category/}K\text{-theory lattice} \quad\xrightarrow{\;\widehat\Gamma\;} \quad \text{period lattice}. } \]

This is likely closer to the kind of “natural number from category theory” that we need than a raw dimension such as \(137\).

There is also a loop-space interpretation: the Gamma class arises from a zeta-regularized product over the positive Fourier modes normal to the constant-loop locus. [arXiv](https://arxiv.org/html/1404.6407v4)

That makes it especially relevant to our language:

> The zeta values measure the analytic cost of translating an integral geometric object through an infinite tower of loop or scale modes.

This does **not** imply that the causal wall is a Calabi–Yau threefold. A Calabi–Yau threefold has six real dimensions; the numeral three alone proves no identification. The relevance is structural: **integral categorical data are converted into period-valued physical coordinates by a Gamma correction.**

---

## 6. Apéry’s original proof is itself a model for the desired mechanism

Apéry did not begin with the decimal value of \(\zeta(3)\). He constructed two sequences satisfying the same integer recurrence:

\[ (n+1)^3x_{n+1} - (34n^3+51n^2+27n+5)x_n + n^3x_{n-1} = 0. \]

One solution is integral, and the ratio of the two canonical solutions tends rapidly to \(\zeta(3)\).

Subsequent work connected this recurrence to modular forms and the Picard–Fuchs equation of a one-parameter family of \(K3\) surfaces. The associated mirror-map and Yukawa-coupling descriptions contain integral and periodic instanton numbers. [arXiv](https://arxiv.org/pdf/1911.02608)

This is extremely close to the desired architecture:

\[ \boxed{ \begin{aligned} &\text{integer recurrence / monodromy},\\ &\text{canonical basis of solutions},\\ &\text{boundary or regularity condition} \end{aligned} \quad \Longrightarrow \quad \text{transcendental connection coefficient}. } \]

The implication for \(\alpha\) is important:

> The remaining modulus may not be a natural number directly. It may be a **period ratio or connection coefficient selected by integral monodromy**.

That is already how exact gauge couplings behave in controlled supersymmetric examples: in Seiberg–Witten theory, the effective complexified gauge coupling is encoded by periods or the period matrix of an algebraic curve. [arXiv](https://arxiv.org/pdf/hep-th/9408099?utm_source=chatgpt.com)

So the serious target is not necessarily

\[ \alpha_U^{-1}=N \qquad N\in\mathbb N. \]

It may instead be

\[ \boxed{ \tau_U = \frac{\Pi_B}{\Pi_A}, } \]

where \(\Pi_A,\Pi_B\) are periods in an integral symplectic basis whose monodromy and normalization are fixed geometrically.

---

# 7. The “natural numbers” should form a period signature

A single integer is probably too impoverished.

The more natural discrete input is a **period signature**

\[ \boxed{ \Sigma_\alpha = \left( r,\, W_\bullet,\, h^{p,q},\, T,\, N_{\rm cyc},\, \mathbf I \right). } \]

Here:

\[ r = \text{rank of the period local system}, \]\[ W_\bullet = \text{weight filtration}, \]\[ h^{p,q} = \text{Hodge numbers}, \]\[ T\in GL_r(\mathbb Z) = \text{integral monodromy}, \]\[ N_{\rm cyc} = \text{cyclotomic or finite-phase level}, \]

and

\[ \mathbf I = \text{Dynkin, embedding, Chern, Euler, intersection, or charge indices}. \]

These are the sorts of natural numbers geometry and category theory actually provide.

Other legitimate integral data include:

\[ \begin{aligned} &\dim H^i,\qquad \chi(X),\qquad \int_Xc_i\,c_j,\qquad \operatorname{rank}K_0(\mathcal C),\\ &\dim\operatorname{Ext}^p(E,F),\qquad N_{ij}^{\ k}\text{ fusion multiplicities},\\ &C_2(G),\qquad T(R),\qquad \operatorname{Tr}_{\mathcal R}Q^2. \end{aligned} \]

One caution: category theory also has **quantum dimensions**, which may be algebraic numbers rather than natural numbers. We should not impose integrality where the category naturally supplies an algebraic integer.

The coupling is then not itself one of these natural numbers. It is a period produced from them:

\[ \boxed{ \alpha^{-1}(u) = \operatorname{per} \left[ \mathfrak h^{\mathfrak m}(u) \right], } \]

where

\[ \mathfrak h^{\mathfrak m}(u) \]

is a motivic or categorical gauge metric and

\[ \operatorname{per} \]

is the period map to an ordinary real number.

The state dependence is carried by a Gauss–Manin or Picard–Fuchs connection:

\[ \boxed{ \nabla_u\Pi(u)=0 } \]

or, in a chosen basis,

\[ \boxed{ \frac{d\Pi}{du} = A(u)\Pi, \qquad A(u)\in\operatorname{Mat}_r\bigl(\mathbb Q(e^u)\bigr). } \]

Then

\[ \alpha^{-1}(u) \]

is a component, ratio, or positive quadratic form constructed from the period vector \(\Pi(u)\).

This gives the right division:

\[ \boxed{ \begin{aligned} \text{category/topology} &\longrightarrow \text{integer lattice and monodromy},\\ \text{algebraic geometry} &\longrightarrow \text{Picard--Fuchs transport},\\ \text{state/scale }u &\longrightarrow \text{point on the period trajectory},\\ \text{period map} &\longrightarrow \text{measured real coupling}. \end{aligned} } \]

Brown’s motivic treatment of Feynman periods formalizes exactly this kind of structure: Feynman periods have a weight filtration, Picard–Fuchs connection, motivic rank, Hodge polynomial, unipotency filtration, and an action of a cosmic Galois group. Weight is generally a filtration rather than a pure grading. [arXiv](https://arxiv.org/pdf/1512.06409)

That is a much stronger invariant than the decimal value or the occurrence of a single \(\zeta(3)\).

---

# 8. A triadic theory should have a cyclotomic fingerprint

The attached relational-physics paper begins from the categorical functor

\[ F(X)=\mathbb Z_3\times X^3. \]

It treats the order-three phase and ternary branching as fundamental inputs. ssrn-6093146.pdfPDF

That gives us a sharp mathematical test.

If the \(\mathbb Z_3\) structure genuinely enters the analytic geometry producing the coupling, the natural period category should not generally be only

\[ \mathbb P^1\setminus\{0,1,\infty\}. \]

It should resemble the level-three cyclotomic geometry

\[ \boxed{ \mathbb P^1 \setminus \left( \{0,\infty\}\cup\mu_3 \right), } \]

where

\[ \mu_3=\{1,\omega,\omega^2\}, \qquad \omega=e^{2\pi i/3}. \]

Its periods include multiple polylogarithms evaluated at cubic roots of unity, cyclotomic multiple zeta values, and related Dirichlet \(L\)-values. Mixed-Tate categories for level \(N=3\) are generated by the motivic fundamental groupoid of precisely such a punctured projective line. [arXiv](https://arxiv.org/pdf/1411.4947)

That yields a powerful audit criterion:

\[ \boxed{ \mathbb Z_3\text{ is physically active} \quad\Longrightarrow\quad \text{level-3 cyclotomic periods should appear in the response}. } \]

Conversely:

\[ \boxed{ \text{only ordinary }\pi^n\text{ and }\zeta(n)\text{ appear} \quad\Longrightarrow\quad \mathbb Z_3\text{ has not yet entered the analytic period geometry}. } \]

This does not prove the triadic proposal false. It tells us what calculation would demonstrate that its categorical input is doing more than supplying a convenient integer.

Since the measured coupling is real, the physical period must be a real Galois-invariant combination, such as

\[ P(\omega)+P(\bar\omega), \]

or a Hermitian pairing of conjugate periods. That reality condition is itself a useful constraint.

---

# 9. A motivic screening law for \(\alpha\)

The earlier screening index was

\[ \mathfrak n_J(u) = -\frac{3\pi}{2} \frac{d\alpha^{-1}}{du}, \qquad u=\ln(Q/Q_0). \]

The algebraic-geometric refinement would be to define a motivic current response

\[ \boxed{ \mathfrak n_J^{\mathfrak m}(u) = \sum_\Gamma I_\Gamma\, \mathcal P_\Gamma^{\mathfrak m} \!\left(e^{u-u_\Gamma}\right) a(u)^{L(\Gamma)-1}. } \]

Here:

\[ I_\Gamma\in\mathbb Z \]

is a charge, Dynkin, embedding, multiplicity, or intersection index;

\[ L(\Gamma)\in\mathbb N \]

is loop or cohomological degree;

\[ u_\Gamma \]

is the logarithmic threshold location;

and

\[ \mathcal P_\Gamma^{\mathfrak m} \]

is a motivic period function satisfying the appropriate Picard–Fuchs system.

The physical function is obtained only after applying the period map:

\[ \boxed{ \frac{d\alpha^{-1}}{du} = -\frac{2}{3\pi} \operatorname{per} \left[ \mathfrak n_J^{\mathfrak m}(u) \right]. } \]

This formula has the desired type structure:

\[ \boxed{ \text{integer coefficients} \times \text{geometric period functions} \times \text{state-dependent scale} \longrightarrow \text{real running coupling}. } \]

At special degenerations the periods may reduce to

\[ \pi^n,\quad \ln2,\quad \zeta(3),\quad \zeta(5),\quad \operatorname{Li}_n(\omega), \]

while at generic kinematics they may remain elliptic or \(K3\)-valued.

This is better than trying to express the entire function using a short list of constants. The constants are boundary values or degeneration periods of the larger function.

---

# 10. A concrete wall calculation for the boundary gauge modulus

The one genuinely continuous datum left in the gauge problem is the high-scale gauge metric

\[ h_\diamond. \]

A plausible way to compute it is through a deformed \(S^3\) wall partition function.

For free conformal fields on \(S^3\), the dimensionless sphere free energies already contain Apéry’s constant:

\[ \boxed{ F_{\rm scalar} = \frac1{16} \left( 2\ln2-\frac{3\zeta(3)}{\pi^2} \right), } \]

and

\[ \boxed{ F_{\rm Dirac} = \frac{\ln2}{4} + \frac{3\zeta(3)}{8\pi^2}. } \]

These follow from spectral determinants of the corresponding sphere operators. [arXiv](https://arxiv.org/pdf/1105.4598)

Introduce a primitive gauge holonomy or real-mass coordinate

\[ \varphi\sim\varphi+2\pi \]

fixed by the integral charge lattice. Then define the wall current capacity

\[ \boxed{ \mathcal C_{J,AB} := \left. \frac{\partial^2F_{S^3}(\varphi)} {\partial\varphi^A\partial\varphi^B} \right|_{\varphi=0}. } \]

The desired Gauge–Capacity weld would be something like

\[ \boxed{ 4\pi h_{\diamond,AB} \stackrel{?}{=} \frac{k_B}{S_\diamond} \mathcal C_{J,AB}, } \]

with the normalization fixed by the primitive integral holonomy, not adjusted afterward.

Then

\[ \boxed{ \alpha_U^{-1} = 4\pi\, h_\diamond(q_{\rm em},q_{\rm em}) } \]

would be calculated from a wall free-energy Hessian rather than inserted.

In controlled three-dimensional supersymmetric theories, real-mass-deformed \(S^3\) free energies are computable by localization and encode current-sector response; derivatives of squashed-sphere free energy similarly determine the stress-tensor two-point coefficient \(C_T\). [arXiv](https://arxiv.org/html/2112.06931v1)

Causal Scale Dynamics is not presently such a supersymmetric theory. The significance is methodological:

> A three-dimensional wall free energy can carry both the integral symmetry data and the transcendental period corrections required to produce a gauge stiffness.

The calculation to attempt is therefore not

\[ \text{guess a combination containing }\zeta(3). \]

It is

\[ \boxed{ \text{construct }F_{S^3}(\varphi) \quad\Longrightarrow\quad \partial_\varphi^2F \quad\Longrightarrow\quad h_\diamond \quad\Longrightarrow\quad \alpha(Q). } \]

---

# 11. The emerging transcendental alphabet

The existing CSD and wall equations now exhibit a surprisingly coherent period ladder:

|Mathematical slot|Native number|
|---|---|
|Complete binary Fisher traversal|\(\pi\)|
|Self-dual binary normalization|\(\ln 2\)|
|Third binary log-determinant cumulant|\(\zeta(3)\)|
|\(P_3\) spectral determinant on \(S^3\)|\(\zeta(3)/\pi^2\)|
|Free \(S^3\) determinant|\(\ln2,\ \zeta(3)/\pi^2\)|
|Perturbative QED transport|\(\zeta(3),\zeta(5),\zeta(7),\ldots\)|
|Full three-loop photon response|\(K3\) iterated periods|
|Genuine \(\mathbb Z_3\) period geometry|level-three cyclotomic periods|

This suggests that the correct primitive is not one magic transcendental constant. It is a **period category**.

The particular numbers arise because different observables project that category into different real coordinates.

---

# 12. What I think has genuinely been found

There are now four rigorous results, with different status.

### Exact within the present wall mathematics

The critical \(P_3\) operator has

\[ \boxed{ \ln\det{}'P_3 = \ln\pi+ \frac{3\zeta(3)}{4\pi^2}. } \]

The reduced binary BKM family has

\[ \boxed{ \kappa_n(\mathcal B) = (n-1)! \left[ 2^n-(2^n-2)\zeta(n) \right]. } \]

Thus Apéry’s constant is extractable both from the global spectral determinant of the critical wall operator and from the third cumulant of the canonical binary state traversal.

These are not two independent empirical confirmations. Both ultimately belong to the same Gamma/period algebra. But they show that the appearance of \(\zeta(3)\) is **native**, not externally inserted.

### Exact in established QED

The physical running of the electromagnetic effective charge is governed by current spectral response. Its perturbative transport contains odd zeta values, while its full higher-loop momentum dependence enters elliptic and \(K3\)-period classes.

### Exact in algebraic geometry

The Gamma class converts integral/categorical data into flat period coordinates and contains

\[ \chi(X)\zeta(3) \]

for a Calabi–Yau threefold.

### Still conjectural for Causal Scale Dynamics

The causal wall has not yet been shown to possess:

- the internal category;
- integral charge lattice;
- Gamma-class correction;
- current-period local system;
- or Gauge–Capacity equivalence law

needed to compute the boundary gauge metric.

That is the honest remaining gap.

---

# The sharpened research hypothesis

The most promising formulation is now:

\[ \boxed{ \textbf{Period-Capacity Hypothesis} } \]

> The gauge and gravitational couplings of a cosmos are period-valued metrics obtained by transporting integral categorical charge data through the information geometry of the causal wall.

For gravity, the period metric is extensive in area:

\[ G = \frac{c^3}{4\hbar\chi_\downarrow}. \]

For electromagnetism, the metric is dimensionless:

\[ \alpha^{-1}(u) = 4\pi\,h_{\rm em}(u). \]

For both, the real number is not primitive. It is the evaluated period of a structured transport law.

The new theorem target should therefore be:

\[ \boxed{ \begin{aligned} &\text{construct the integral current category } \mathcal C_J,\\ &\text{derive its charge lattice }K_0(\mathcal C_J),\\ &\text{derive its Gamma/motivic correction},\\ &\text{derive the Picard--Fuchs connection over }u=\ln Q,\\ &\text{compute the resulting positive gauge metric}. \end{aligned} } \]

The natural numbers will be the ranks, monodromies, Euler pairings, Chern numbers, and representation indices of that structure.

The \(\pi\), \(\ln2\), \(\zeta(3)\), cyclotomic values, and \(K3\) periods will be the **translation quotients by which that integral structure becomes an observable real coupling**.

That is, I think, the mathematically mature version of the intuition:

\[ \boxed{ \text{Do not derive }137. \quad \text{Derive the period geometry whose state-dependent output is }\alpha(Q). } \]
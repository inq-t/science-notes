# The function that produces \(\alpha\)

Yes. We can now do something more precise than gesture toward “vacuum screening.”

The most important result is not a numerical approximation to \(137\). It is an explicit mathematical factorization:

\[ \boxed{ \text{charged spectral data} \;\xrightarrow{\;\text{binary BKM resolution kernel}\;} \text{screening susceptibility} \;\xrightarrow{\;\text{integration over log scale}\;} \alpha^{-1}(Q). } \]

More concretely,

\[ \boxed{ \rho_J(r) \;\longmapsto\; \mathfrak n_J(u) = \int_{-\infty}^{\infty} \rho_J(r)\, \frac12\operatorname{sech}^2(u-r)\,dr \;\longmapsto\; \alpha^{-1}(u), } \]

where

\[ u=\ln\frac{Q}{Q_0} \]

is logarithmic resolution scale and \(\rho_J\) is the spectral density of the conserved electromagnetic current.

This is not merely an analogy with the Causal Scale Dynamics susceptibility. The normalized kernel

\[ \frac12\operatorname{sech}^2(u-r) \]

really appears when the standard dispersion relation for vacuum polarization is written in logarithmic scale coordinates. The CSD binary family independently produces

\[ G_{\theta\theta}^{\mathrm{BKM}}=\operatorname{sech}^2\theta. \]

Thus, the same binary information-geometric shape governs:

- CSD’s distinguishability under causal-scale displacement;
- the resolution of charged spectral channels by vacuum polarization.

The two uses are not yet proved to be one physical object, but the mathematical coincidence is exact and quite striking. The CSD binary geometry is given explicitly in the master document.

---

## 1. First, what \(\alpha\) actually is

At low energy,

\[ \alpha_{\rm em} = \frac{e^2}{4\pi\hbar c}. \]

But this should not primarily be read as “the strength of electricity.” Electricity is the static, macroscopic sector of the electromagnetic interaction.

A better reading is:

\[ \boxed{ \alpha_{\rm em}^{-1} = \text{action stiffness of curvature in the electromagnetic gauge direction}. } \]

Normalize the gauge connection so that its holonomies and charges are integral. Then the gauge action takes the schematic form

\[ \frac{S_{\rm gauge}}{\hbar} = \frac14 \int h_{AB}(Q)\, F^A_{\mu\nu}F^{B\,\mu\nu}\,d^4x, \]

where

\[ h_Q\in \bigl(\operatorname{Sym}^2\mathfrak g^*\bigr)^G_{>0} \]

is a positive invariant metric on the gauge algebra.

For one \(U(1)\) factor,

\[ h_Q=\frac1{e^2(Q)}, \qquad \alpha^{-1}(Q)=4\pi h_Q. \]

So:

\[ \boxed{ \alpha(Q)=\text{gauge compliance}, \qquad \alpha^{-1}(Q)=\text{gauge stiffness}. } \]

Vacuum polarization changes that stiffness because charged possibilities become resolvable at different scales.

The Gell-Mann–Low effective charge is especially suitable here because its physical scale is the virtuality \(Q\) of the exchanged photon, and the dressed coupling is determined by the vacuum-polarization function. [arXiv](https://www.arxiv.org/pdf/1107.0338v3?utm_source=chatgpt.com)

Above electroweak symmetry breaking, however, there is no independent fundamental photon coupling. One has the running metric on

\[ \mathfrak{su}(2)_L\oplus\mathfrak u(1)_Y, \]

and the electromagnetic value is obtained only after pulling that metric back onto the unbroken generator

\[ Q_{\rm em}=T_3+\frac{Y}{2}. \]

Thus the full object is not one scalar function but a path of gauge metrics.

---

# 2. The correct type signature

The most economical type signature I can formulate is

\[ \boxed{ \mathsf{GaugeFlow}: \left( \mathfrak g,\, \Lambda_{\rm ch},\, \mathcal R,\, D_F,\, h_\diamond,\, \omega \right) \longmapsto \left[ u\longmapsto h_\omega(u) \right]. } \]

The inputs have different mathematical types:

\[ \begin{aligned} \mathfrak g &=\text{gauge Lie algebra},\\ \Lambda_{\rm ch} &=\text{integral charge/cocharacter lattice},\\ \mathcal R &=\text{graded matter representation},\\ D_F &=\text{mass or internal Dirac operator},\\ h_\diamond &=\text{gauge metric at one distinguished scale},\\ \omega &=\text{physical state or thermal sector}. \end{aligned} \]

The measured electromagnetic coupling is then

\[ \boxed{ \alpha_{\rm em}^{-1}(u) = 4\pi\, \bigl(\iota_{\rm em}^{*}h_\omega(u)\bigr) (q_{\rm em},q_{\rm em}), } \]

where

\[ \iota_{\rm em}: \mathfrak u(1)_{\rm em} \hookrightarrow \mathfrak g \]

is the symmetry-breaking embedding.

This already exposes the logical structure:

- algebra determines the available gauge directions;
- representation theory determines the screening indices;
- the spectrum of \(D_F\) determines where thresholds occur;
- the RG equation transports the metric through logarithmic scale;
- one boundary metric supplies the integration constant;
- the state \(\omega\) determines whether the response is vacuum, thermal, dense, curved, and so on.

The attached \(137\) paper instead proposes

\[ \alpha^{-1}(Q) = z^2+2^{g-3}f(Q/\Lambda_{\rm srs}), \]

but leaves \(f\) unspecified and subsequently allows ordinary Standard Model running to supply the interpolation. Thus the paper proposes endpoints and an interpretation, but not the function carrying the physics between them. ssrn-6093146.pdfPDF

We can do better than that.

---

# 3. Run the actual one-loop screening calculation

Consider one Dirac field with:

- mass \(m\);
- charge \(q\) in units of the primitive electromagnetic charge;
- multiplicity \(\nu\), such as color.

Let

\[ C(Q):=\alpha^{-1}(Q). \]

For a spacelike probe \(Q^2>0\), the one-loop, on-shell-subtracted vacuum-polarization result gives

\[ \boxed{ C(Q)-C(Q_0) = -\frac{2\nu q^2}{\pi} \int_0^1 dx\,x(1-x) \ln \frac{ m^2+Q^2x(1-x) }{ m^2+Q_0^2x(1-x) }. } \]

This is the genuine screening function. It is not fitted.

Let

\[ u=\ln\frac{Q}{m}, \qquad z=\frac{Q^2}{m^2}=e^{2u}, \qquad y=x(1-x). \]

Now differentiate with respect to logarithmic resolution:

\[ \frac{dC}{du} = -\frac{4\nu q^2}{\pi} \int_0^1 dx\, \frac{z\,y^2}{1+zy}. \]

Define the **Dirac-normalized current-channel index**

\[ \boxed{ \mathfrak n_J(u) := -\frac{3\pi}{2} \frac{d\alpha^{-1}}{du}. } \]

Then a single massive Dirac channel contributes

\[ \boxed{ \mathfrak n_J(u) = \nu q^2\,A_D(e^{2u}), } \]

where

\[ \boxed{ A_D(z) = 6\int_0^1 dx\, \frac{z\,x^2(1-x)^2} {1+z\,x(1-x)}. } \]

This function satisfies

\[ A_D(0)=0, \qquad A_D(\infty)=1. \]

Therefore:

\[ \mathfrak n_J(-\infty)=0, \qquad \mathfrak n_J(+\infty)=\nu q^2. \]

Its meaning is:

> \(\mathfrak n_J(Q)\) is the effective charge-square rank of the channels that the probe can currently resolve.

At low resolution, the massive charged channel is invisible to vacuum screening.

At high resolution, it contributes its full algebraic index

\[ \nu q^2. \]

The running equation becomes

\[ \boxed{ \frac{d\alpha^{-1}}{d\ln Q} = -\frac{2}{3\pi}\, \mathfrak n_J(Q). } \]

For several Dirac sectors,

\[ \boxed{ \mathfrak n_J(Q) = \sum_a \nu_aq_a^2\, A_D\!\left(\frac{Q^2}{m_a^2}\right) +\text{interaction corrections}. } \]

This is already a considerable reduction of the mystery.

The function depends on:

- natural multiplicities \(\nu_a\);
- charge-lattice values \(q_a\);
- eigenvalues \(m_a\) of the mass operator;
- one universal activation function \(A_D\).

---

# 4. The activation function is hypergeometric

The integral can be evaluated as

\[ \boxed{ A_D(z) = \frac{z}{5}\, {}_2F_1 \left( 1,3;\frac72;-\frac z4 \right). } \]

It therefore belongs to the Gauss hypergeometric class.

Equivalently, it is the regular physical solution of

\[ \boxed{ z^2(z+4)A_D''(z) + 3z(z+2)A_D'(z) - 6A_D(z) = 0, } \]

with

\[ A_D(z)\sim\frac z5 \quad(z\rightarrow0), \qquad A_D(z)\rightarrow1 \quad(z\rightarrow\infty). \]

This is very close to what you expected:

> The shape is fixed by an algebraic differential equation with rational and natural-number coefficients.

Its singular points are

\[ z=0,\qquad z=-4,\qquad z=\infty. \]

The point \(z=-4\) is the analytic continuation of the two-particle threshold

\[ q^2=4m^2. \]

So the number \(4\) is not decorative: it is the geometry of a two-particle threshold.

The function is also expressible in elementary transcendental form:

\[ A_D(z) = 1-\frac6z \left[ 1- \frac4{\sqrt{z(z+4)}} \operatorname{artanh} \sqrt{\frac{z}{z+4}} \right]. \]

What matters is not the decimal value of this function at one point. What matters is its category:

\[ \boxed{ \text{one-loop vacuum screening} = \text{a hypergeometric period with a threshold singularity}. } \]

This is genuinely algebraic-geometric.

---

# 5. The exact \(\operatorname{sech}^2\) relation

Differentiate \(A_D\) with respect to \(u=\ln(Q/m)\). Define

\[ P_D(u) := \frac{dA_D(e^{2u})}{du}. \]

Then

\[ P_D(u) = 12\int_0^1dx\, \frac{ e^{2u}x^2(1-x)^2 }{ \left[1+e^{2u}x(1-x)\right]^2 }. \]

Now set

\[ s_x = u+\frac12\ln[x(1-x)]. \]

Using

\[ \frac12\operatorname{sech}^2s = \frac{2e^{2s}}{(1+e^{2s})^2}, \]

we obtain the exact identity

\[ \boxed{ P_D(u) = \int_0^1 6x(1-x)\, \frac12 \operatorname{sech}^2 \left( u+\frac12\ln[x(1-x)] \right) dx. } \]

This says:

> The turn-on of one Dirac vacuum-screening channel is a convex mixture of canonical binary BKM susceptibility pulses.

The mixing weight is

\[ w(x)=6x(1-x), \qquad \int_0^1w(x)\,dx=1. \]

And every elementary pulse is

\[ K_{\rm bin}(v) = \frac12\operatorname{sech}^2v, \qquad \int_{-\infty}^{\infty}K_{\rm bin}(v)\,dv=1. \]

The CSD binary state geometry gives

\[ G_{\theta\theta}^{\rm BKM} = \operatorname{sech}^2\theta. \]

So the QED threshold kernel is precisely the normalized version of the CSD BKM metric.

This does **not** prove that CSD generates QED. It does establish a strong common grammar:

\[ \boxed{ \text{a distinction crossing from unresolved to resolved} \quad\Longrightarrow\quad \operatorname{sech}^2 \text{ susceptibility in log scale}. } \]

That is exactly the sort of structure your programme is seeking.

---

# 6. Universal numbers of the threshold pulse

The function \(P_D(u)\) is a normalized probability density over logarithmic resolution:

\[ \int_{-\infty}^{\infty}P_D(u)\,du=1. \]

Its first two moments can be calculated exactly:

\[ \boxed{ \int_{-\infty}^{\infty}uP_D(u)\,du = \frac56, } \]

and

\[ \boxed{ \int_{-\infty}^{\infty} \left(u-\frac56\right)^2 P_D(u)\,du = \frac{31}{36}. } \]

Thus the logarithmic centroid of the threshold is

\[ u_{\rm cent}=\frac56, \]

or

\[ \boxed{ Q_{\rm cent} = e^{5/6}m \simeq 2.301\,m. } \]

Its standard width in logarithmic scale is

\[ \sqrt{\frac{31}{36}} \simeq0.928 \]

e-folds.

These are not candidates for the value of \(\alpha\). They are universal invariants of the **shape of one Dirac screening threshold**.

The cancellation producing

\[ \operatorname{Var}(u)=\frac{31}{36} \]

is particularly appealing. Each elementary binary pulse has variance

\[ \frac{\pi^2}{12}, \]

while the distribution of its Feynman-parameter centers contributes

\[ \frac{31}{36}-\frac{\pi^2}{12}. \]

The \(\pi^2\) terms cancel in the total variance.

This is the sort of natural-number/rational structure that is meaningful: it follows from the simplex measure and the exponential family, not from reverse-engineering a decimal.

---

# 7. The more general spectral formula

The one-loop calculation is only the simplest member of a much broader result.

Define the electromagnetic current correlator by

\[ \left( -q^2\eta^{\mu\nu}+q^\mu q^\nu \right)\Pi(q^2) = i\int d^4x\,e^{iqx} \langle T J_{\rm em}^{\mu}(x)J_{\rm em}^{\nu}(0) \rangle. \]

The Adler function is

\[ \boxed{ D(Q^2) = -12\pi^2Q^2 \frac{d\Pi(-Q^2)}{dQ^2}. } \]

It is precisely a logarithmic derivative of the current response and is used in determining the running electromagnetic coupling. [arXiv](https://arxiv.org/html/2311.04849v1?utm_source=chatgpt.com)

Its dispersion representation is

\[ D(Q^2) = Q^2 \int_0^\infty \frac{R(s)}{(s+Q^2)^2}\,ds, \]

where \(R(s)\) is the physical charged spectral density.

Now write

\[ Q=e^u, \qquad \sqrt{s}=e^r, \qquad ds=2e^{2r}dr. \]

Then

\[ \frac{2Q^2s}{(Q^2+s)^2} = \frac12\operatorname{sech}^2(u-r). \]

Therefore

\[ \boxed{ D(e^{2u}) = \int_{-\infty}^{\infty} dr\, R(e^{2r}) \frac12 \operatorname{sech}^2(u-r). } \]

This is the general form promised at the beginning.

The Adler function is the charged spectral density viewed through a binary-resolution kernel.

In the conventional normalization, one asymptotically massless unit-charge Dirac channel contributes

\[ D\rightarrow1. \]

Thus, to leading electromagnetic order,

\[ \boxed{ \mathfrak n_J(u) := -\frac{3\pi}{2} \frac{d\alpha^{-1}}{du} = D(e^{2u}). } \]

Consequently,

\[ \boxed{ \alpha^{-1}(u_2)-\alpha^{-1}(u_1) = -\frac{1}{3\pi} \int_{-\infty}^{\infty} dr\, R(e^{2r}) \left[ \tanh(u_2-r)-\tanh(u_1-r) \right]. } \]

This is an actual function-producing formula.

Its inputs are:

- the charged spectral state \(R(s)\);
- the two resolution scales \(u_1,u_2\);
- one boundary value \(\alpha^{-1}(u_1)\).

There is no \(137\) built into it.

---

# 8. The fundamental quantities to define

I would introduce three quantities.

## 8.1 Gauge stiffness

\[ \boxed{ \mathcal C_{\rm em}(u) := \alpha_{\rm em}^{-1}(u). } \]

This is the cumulative action cost of electromagnetic gauge curvature.

## 8.2 Current-channel screening index

\[ \boxed{ \mathfrak n_J(u) := -\frac{3\pi}{2} \frac{d\mathcal C_{\rm em}}{du}. } \]

At weak electromagnetic coupling,

\[ \mathfrak n_J(u)=D(e^{2u}). \]

In a regime where a set of Dirac channels is fully resolved,

\[ \boxed{ \mathfrak n_J \longrightarrow \sum_a\nu_aq_a^2. } \]

This is the natural algebraic number.

It is the quadratic index of the charged representation.

## 8.3 Threshold density

\[ \boxed{ \chi_J(u) := \frac{d\mathfrak n_J}{du}. } \]

For isolated free thresholds,

\[ \chi_J(u) = \sum_a \nu_aq_a^2 P_D\!\left(u-\ln m_a\right). \]

Its integrated weight is

\[ \boxed{ \int\chi_J(u)\,du = \sum_a\nu_aq_a^2. } \]

So:

\[ \boxed{ \text{charge-square index} = \text{total screening susceptibility accumulated across all thresholds}. } \]

This is a much more defensible “fundamental number” than a dimension chosen to resemble \(137\).

---

# 9. Why the coefficients are algebraic

For a general gauge factor \(G_i\), the one-loop beta coefficient has the form

\[ \boxed{ b_i = -\frac{11}{3}C_2(G_i) + \frac{2}{3} \sum_{\text{Weyl fermions}}T_i(R_f) + \frac{1}{3} \sum_{\text{complex scalars}}T_i(R_s). } \]

The ingredients are:

- quadratic Casimirs;
- Dynkin indices;
- multiplicities;
- charge-lattice norms.

These are representation-theoretic data.

Between thresholds,

\[ \boxed{ \frac{d\alpha_i^{-1}}{d\ln Q} = -\frac{b_i}{2\pi}. } \]

Thus one-loop inverse couplings are affine functions of logarithmic resolution.

The logarithm is forced because scales multiply:

\[ Q_3/Q_1 = (Q_3/Q_2)(Q_2/Q_1), \]

while RG displacement adds:

\[ u_{31}=u_{32}+u_{21}. \]

Euler’s \(e\) enters as the exponential map

\[ Q=Q_0e^u \]

from the additive scale line to the multiplicative positive scale group.

The \(2\pi\) enters through quantum phase, loop integration, and Chern–Weil normalization.

The coefficients multiplying them are group-theoretic indices.

A recent spectral-geometry calculation provides an especially relevant demonstration: the heat-kernel coefficient \(a_4\) of a twisted Dirac operator on \(S^3\times S^1\) reproduces

\[ \beta(e)=\frac{e^3}{12\pi^2} \]

for one Dirac fermion, independently of the radii or gauge background. This is evidence that the one-loop flow coefficient really can be read as spectral geometry rather than only as a flat-space Feynman integral. [arXiv](https://arxiv.org/pdf/2603.14081?utm_source=chatgpt.com)

---

# 10. Run the electroweak calculation

In the usual \(SU(5)\)-normalized convention,

\[ \alpha_1 = \frac53\frac{\alpha_{\rm em}}{\cos^2\theta_W}, \qquad \alpha_2 = \frac{\alpha_{\rm em}}{\sin^2\theta_W}. \]

Therefore

\[ \boxed{ \alpha_{\rm em}^{-1} = \frac53\alpha_1^{-1} + \alpha_2^{-1}. } \]

This is the pullback of the electroweak kinetic metric onto the electromagnetic generator. [arXiv](https://arxiv.org/pdf/1912.07624?utm_source=chatgpt.com)

Suppose a simple high-scale geometry gives

\[ \alpha_1(Q_U)=\alpha_2(Q_U)=\alpha_U. \]

Then

\[ \alpha_{\rm em}^{-1}(Q) = \frac83\alpha_U^{-1} + \frac{B_{\rm em}}{2\pi} \ln\frac{Q_U}{Q}, \]

where

\[ \boxed{ B_{\rm em} = \frac53b_1+b_2. } \]

The factor

\[ \boxed{\frac83} \]

is the electroweak embedding index seen by the electromagnetic direction.

## Standard Model field content

For the Standard Model,

\[ b_1=\frac{41}{10}, \qquad b_2=-\frac{19}{6}, \qquad b_3=-7. \]

These are the standard one-loop coefficients in the \(SU(5)\)-normalized convention. [arXiv](https://arxiv.org/pdf/2006.01406?utm_source=chatgpt.com)

Therefore

\[ B_{\rm em}^{\rm SM} = \frac53\frac{41}{10} -\frac{19}{6} = \boxed{\frac{11}{3}}. \]

Hence

\[ \boxed{ \alpha_{\rm em}^{-1}(Q) = \frac83\alpha_U^{-1} + \frac{11}{6\pi} \ln\frac{Q_U}{Q} } \]

in the massless one-loop approximation.

## MSSM-like field content

For the MSSM,

# [  
(b_1,b_2,b_3)

\left(  
\frac{33}{5},1,-3  
\right).  
] [arXiv](https://arxiv.org/pdf/1405.3692?utm_source=chatgpt.com)

Therefore

\[ B_{\rm em}^{\rm MSSM} = \frac53\frac{33}{5}+1 = \boxed{12}. \]

So

\[ \boxed{ \alpha_{\rm em}^{-1}(Q) = \frac83\alpha_U^{-1} + \frac6\pi \ln\frac{Q_U}{Q}. } \]

This is where the familiar high-scale number near \(24\) comes from.

Take, illustratively,

\[ Q_U=2\times10^{16}\ {\rm GeV}, \qquad Q=M_Z=91.1876\ {\rm GeV}, \]

so

\[ \ln(Q_U/M_Z)=33.02159. \]

Using

\[ \alpha_{\rm em}^{-1}(M_Z)\simeq127.95 \]

as the illustrative input used in the attached discussion gives:

|Spectrum assumption|\(B_{\rm em}\)|Integrated RG contribution|Inferred \(\alpha_U^{-1}\)|
|---|---|---|---|
|Standard Model|\(11/3\)|\(19.27035\)|\(40.75487\)|
|MSSM-like|\(12\)|\(63.06659\)|\(24.33128\)|

This calculation is deliberately diagnostic, not a prediction:

- the unification scale was assumed;
- the measured low-energy value was supplied;
- thresholds and higher loops were neglected;
- the MSSM spectrum was assumed active over the interval.

But it shows exactly what \(24\) means.

It is not “the early-universe fine-structure constant.”

It is the inferred inverse metric of a hypothetical unified gauge direction after accounting for:

\[ \boxed{ \frac83 \quad\text{embedding} \qquad+\qquad 12 \quad\text{RG index} \qquad+\qquad \ln(Q_U/M_Z) \quad\text{scale displacement}. } \]

---

# 11. Temperature is a map into RG scale—not RG scale itself

Your intuition about temperature is important, but the quantities must remain typed.

The vacuum running coupling is fundamentally a function of probe virtuality:

\[ \alpha_{\rm vac}(Q). \]

A thermal effective response is more general:

\[ \boxed{ \alpha_{\rm eff} = \alpha_{\rm eff} \left( \omega_T,\, q^0,\, |\mathbf q|,\, \text{longitudinal/transverse channel} \right). } \]

A thermal plasma selects a rest frame and breaks vacuum Lorentz symmetry. Electric and magnetic/static-current responses can then differ, so there is not always one scalar “\(\alpha(T)\).” [arXiv](https://arxiv.org/html/1310.5160v1?utm_source=chatgpt.com)

Temperature becomes a useful RG input only after a physical process supplies a relation such as

\[ Q=\xi k_BT. \]

Then

\[ u_T = \ln\frac{\xi k_BT}{Q_0}. \]

In an adiabatically expanding thermal sector,

\[ g_{*s}(T)T^3a^3=\text{constant}, \]

so

\[ \boxed{ d\ln T = -dN -\frac13d\ln g_{*s}. } \]

The standard thermal history uses precisely this relation between expansion, temperature, entropy density, and the changing number of relativistic degrees of freedom. [arXiv](https://arxiv.org/pdf/2411.03018?utm_source=chatgpt.com)

Using

\[ \frac{d\alpha^{-1}}{du} = -\frac{2}{3\pi}\mathfrak n_J(u), \]

we obtain, along a thermal cosmic trajectory,

\[ \boxed{ d\alpha^{-1} = \frac{2}{3\pi}\, \mathfrak n_J(T) \left( dN+\frac13d\ln g_{*s} \right). } \]

This is already an information–temperature–scale relation.

It says:

- the coupling does not intrinsically “know the age”;
- the cosmic state supplies a path through resolution scale;
- each e-fold of cooling integrates a definite amount of vacuum-screening capacity;
- changes in the number of entropy-bearing species produce threshold corrections.

---

# 12. Insert the CSD clock-allocation identity

Causal Scale Dynamics gives, for the flat FLRW apparent horizon,

\[ \boxed{ dN = d\eta_A + \frac14d\ln\mathcal S_A, } \]

where

\[ \mathcal S_A=\frac{S_A}{k_B} \]

is dimensionless horizon entropy and \(\eta_A\) is the vertical horizon-rapidity coordinate. The master document explicitly distinguishes this vertical clock from horizontal state displacement.

Substitution yields

\[ \boxed{ d\alpha^{-1} = \frac{2}{3\pi} \mathfrak n_J(T) \left[ d\eta_A + \frac14d\ln\mathcal S_A + \frac13d\ln g_{*s} \right]. } \]

This may be the cleanest preliminary **cosmokinetic alpha equation**.

It decomposes the change in inverse electromagnetic stiffness along a thermal cosmic history into:

\[ \begin{aligned} d\eta_A &:\quad\text{causal/horizon boost advance},\\ \frac14d\ln\mathcal S_A &:\quad\text{horizon-information growth},\\ \frac13d\ln g_{*s} &:\quad\text{change in matter entropy channels}. \end{aligned} \]

The coefficient multiplying all three is

\[ \mathfrak n_J(T), \]

the charge-square screening capacity currently visible to the thermal state.

This equation is conditional on:

- approximate thermal equilibrium;
- adiabatic matter expansion;
- a specified relation \(Q\propto T\);
- using the vacuum-like transverse effective charge;
- no additional explicit state-dependent polarization term.

But the algebra is exact under those conditions.

It is also important that

\[ T_{\rm plasma} \neq T_{\rm horizon} \]

in general. The former describes matter occupation. The latter is a modular/geometric normalization. They should only be identified when a genuine equilibrium argument licenses it.

---

# 13. Hawking entropy as an RG coordinate

For a causal horizon of radius \(R\),

\[ k_BT_H = \frac{\hbar c}{2\pi R}, \]

and

\[ \mathcal S_H = \frac{S_H}{k_B} = \frac{\pi R^2}{\ell_P^2}. \]

Let

\[ E_P=\frac{\hbar c}{\ell_P}. \]

Then

\[ \boxed{ \frac{k_BT_H}{E_P} = \frac{1}{2\sqrt{\pi\mathcal S_H}}. } \]

Therefore

\[ \boxed{ d\ln T_H = -\frac12d\ln\mathcal S_H. } \]

If a gauge response is evaluated at the horizon modular scale \(Q=k_BT_H\), then

\[ \boxed{ \frac{d\alpha^{-1}}{d\ln\mathcal S_H} = \frac{1}{3\pi}\mathfrak n_J. } \]

In a regime where the screening index is constant,

\[ \boxed{ \alpha^{-1}(\mathcal S_H) = \alpha^{-1}(\mathcal S_{H,0}) + \frac{\mathfrak n_J}{3\pi} \ln\frac{\mathcal S_H}{\mathcal S_{H,0}}. } \]

This does not mean that the present cosmic horizon entropy numerically generates low-energy \(\alpha\). Its Hawking temperature is far below every charged-particle threshold, so

\[ \mathfrak n_J\approx0 \]

there and the infrared coupling is effectively frozen.

The significance is structural:

> Horizon entropy can serve as a logarithmic coordinate on the same scale line on which the gauge metric runs.

---

# 14. The algebraic-geometric hierarchy

There are three increasingly deep mathematical layers.

## 14.1 Characteristic numbers determine the slope

At one loop, the beta coefficients are combinations of

\[ C_2(G),\qquad T(R),\qquad \operatorname{Tr}_{\mathcal R}Q^2. \]

These are characteristic and representation-theoretic numbers.

For a \(U(1)\) factor,

\[ \operatorname{Tr}_{\mathcal R}Q^2 = \sum_a\nu_aq_a^2 \]

is the quadratic charge index.

## 14.2 Graph periods determine the threshold functions

The one-loop polarization function is a period over the simplex

\[ \Delta^1=\{0\le x\le1\}, \]

with graph polynomial

\[ 1+zx(1-x). \]

Its hypergeometric differential equation is a Picard–Fuchs equation for that family of periods.

Thus:

\[ \boxed{ \text{beta coefficient} = \text{characteristic index}, } \]

while

\[ \boxed{ \text{massive threshold profile} = \text{period of the graph geometry}. } \]

## 14.3 The determinant line carries the anomaly

The fermion partition function is naturally a section of a determinant line over the moduli space or stack of gauge connections. The curvature of that line is computed by a family index theorem and represents the anomaly. Recent work has explicitly formulated one-loop gauge beta coefficients as such index data. [arXiv](https://arxiv.org/html/2510.26764?utm_source=chatgpt.com)

This gives the genuinely geometric sequence

\[ \boxed{ \text{connection moduli stack} \longrightarrow \text{determinant line} \longrightarrow \text{scale anomaly} \longrightarrow \text{beta vector field}. } \]

At higher loops, the function class becomes richer rather than arbitrary. A modern analytic calculation of the three-loop QED photon self-energy finds iterated-integral kernels associated with a \(K3\) geometry; related multi-loop diagrams produce elliptic and higher Calabi–Yau periods. [arXiv](https://arxiv.org/pdf/2411.19042?utm_source=chatgpt.com)

So your suspicion about algebraic geometry is well placed:

> The full running function is not generally elementary, but its complexity is organized by the algebraic geometry of graph varieties.

---

# 15. What remains as the one genuine modulus

Suppose the high-energy gauge algebra is simple.

Then its invariant positive bilinear form is unique up to one positive scalar:

\[ \boxed{ h_U=\lambda_U B_{\mathfrak g}, } \]

where \(B_{\mathfrak g}\) is the integrally normalized invariant form.

Internal geometry can fix:

- the gauge algebra;
- the charge lattice;
- subgroup embedding indices;
- relative coupling normalizations;
- representation content;
- beta-function coefficients;
- threshold multiplicities.

But one scalar remains:

\[ \lambda_U. \]

Equivalently,

\[ \alpha_U^{-1}. \]

This is why ordinary unification reduces three gauge couplings to one coupling rather than deriving no continuous coupling at all.

The honest obstruction is:

\[ \boxed{ \text{algebra fixes the direction in coupling space; it does not automatically fix the radial modulus.} } \]

There is no general theorem that four-dimensional Yang–Mills coupling constants must be integers.

The natural integer candidates are instead:

- Dynkin indices;
- embedding indices;
- Chern numbers;
- current-algebra levels;
- dimensions and multiplicities of representations;
- flux or charge-lattice pairings.

To make the final modulus a natural number, one needs an additional structural law.

---

# 16. A Gauge–Capacity Equivalence Principle

CSD already supplies the model for such a move.

Its scale-capacity number is

\[ \mathfrak R_c = \frac{k_B}{S_c} G_{NN}^{\perp}(N_c), \]

with fundamental value

\[ \mathfrak R_c=1. \]

This identifies an entropy-normalized BKM norm with a fundamental Weyl translation. Causal_Scale_Dynamics_Master_v7_0.pdfPDF

The gauge analogue should begin with a **topologically normalized** gauge coordinate.

Let

\[ \varphi\sim\varphi+2\pi \]

be a primitive holonomy or flux coordinate on the integral charge lattice. Define the current-sector BKM capacity

\[ \boxed{ \mathcal C_J := \left. \frac{k_B}{S_\diamond} \frac{\partial^2}{\partial\varphi^2} \mathscr J(\omega_\varphi,\omega_0) \right|_{\varphi=0}. } \]

Because \(\varphi\) has fixed \(2\pi\) periodicity, its normalization is no longer freely rescalable.

The desired theorem would be an equality of bilinear forms on the integral charge lattice:

\[ \boxed{ 4\pi h_\diamond \stackrel{?}{=} \Phi_J^* \left( \frac{k_B}{S_\diamond} G_{\rm BKM}^{J} \right). } \]

If this held, then

\[ \boxed{ \alpha_U^{-1} = \mathcal C_J(q_{\rm em},q_{\rm em}) } \]

after the appropriate group embedding.

The remaining “number” would no longer be an unexplained real input. It would be the entropy-normalized information cost of one primitive gauge twist.

That would give an exact meaning to your proposed concept:

> **Gauge coupling is the transport cost of making a charged distinction observable across a causal wall.**

The possible natural number would be the integral level or embedding index of the current direction.

But this equality has not yet been derived. Writing

\[ \alpha_U^{-1}=k \]

for a convenient integer without constructing the BKM current family would merely recreate the \(137\) problem at a different scale.

---

# 17. The proposed master formula

The strongest defensible formula is therefore

\[ \boxed{ \alpha_{\rm em}^{-1}(u) = 4\pi \bigl(\iota_{\rm em}^{*}h_\diamond\bigr) (q_{\rm em},q_{\rm em}) - \frac{2}{3\pi} \int_{u_\diamond}^{u} \mathfrak n_J(v)\,dv + \text{higher-loop and phase-transition terms}, } \]

with

\[ \boxed{ \mathfrak n_J(u) = \int_{-\infty}^{\infty} dr\, \rho_J(r) \frac12\operatorname{sech}^2(u-r). } \]

And, for free massive Dirac channels,

\[ \boxed{ \mathfrak n_J(u) = \sum_a \nu_aq_a^2\, \frac{e^{2(u-u_a)}}{5} {}_2F_1 \left( 1,3;\frac72; -\frac{e^{2(u-u_a)}}4 \right), \qquad u_a=\ln m_a. } \]

The mathematical roles are now clean:

\[ \begin{array}{ccl} u=\ln Q &:& \text{additive resolution coordinate},\\[2mm] \rho_J &:& \text{state’s charged spectral content},\\[2mm] \frac12\sech^2 &:& \text{binary resolution/BKM kernel},\\[2mm] \mathfrak n_J &:& \text{resolved charge-square capacity},\\[2mm] \int\mathfrak n_J\,du &:& \text{accumulated vacuum screening},\\[2mm] h_\diamond &:& \text{one global gauge-stiffness modulus},\\[2mm] \iota_{\rm em} &:& \text{algebraic symmetry-breaking projection}. \end{array} \]

---

# What I think we have genuinely found

The shape of the function producing \(\alpha\) is not arbitrary.

At the most structural level, it is:

\[ \boxed{ \text{a spectral transform over logarithmic scale}. } \]

At one loop, each massive Dirac threshold is:

\[ \boxed{ \text{a hypergeometric/Picard–Fuchs period}. } \]

Its marginal activation is:

\[ \boxed{ \text{a convex mixture of binary } \operatorname{sech}^2 \text{ BKM pulses}. } \]

The natural numbers and rational coefficients are:

- charge-square indices;
- representation multiplicities;
- Casimirs and Dynkin indices;
- embedding factors such as \(8/3\);
- beta indices such as \(11/3\) or \(12\);
- threshold invariants such as \(5/6\) and \(31/36\).

The state-dependent real data are:

- the spectrum of the internal mass operator;
- symmetry-breaking scales;
- the current spectral density;
- the one boundary gauge modulus.

Thus the decisive remaining problem is not “explain the decimal \(137.035999\ldots\).”

It is:

\[ \boxed{ \text{derive the boundary gauge metric from causal-wall current capacity.} } \]

Once that weld is supplied, the rest is transport:

\[ \boxed{ \text{integral geometry} + \text{spectral state} + \text{BKM resolution} + \text{RG flow} \longrightarrow \alpha_{\rm em}(Q). } \]

The most surprising concrete result is the middle equality:

\[ \boxed{ D(e^{2u}) = \int dr\, R(e^{2r}) \frac12\operatorname{sech}^2(u-r). } \]

The vacuum-screening function is already speaking the same binary information-geometric language as the Ruble equations.
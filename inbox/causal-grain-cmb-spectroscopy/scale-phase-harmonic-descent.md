# Scale--Phase Harmonic Descent

A causal scale becomes capable of producing a harmonic spectrum only after a positive noncompact scale coordinate is paired with the compact phase of a selected associative complex observable fiber. Inside each octonionic slice \(\mathbb C_u\), the exact polar decomposition \(\mathbb C_u^\times\cong\mathbb R_{>0}\times U(1)_u\) separates logarithmic modulus from local phase. The CMB proposal is that global causal directedness owns the first factor, while the realized photon--baryon oscillator reads the second. This supplies a precise algebraic grammar for coherent harmonics, but the character selecting the phase from the scale and the physical map to curvature modes remain open constructions.

## One complex slice contains both scale and phase

Choose a unit imaginary octonion

$$
u\in S^6,
\qquad
u^2=-1.
$$

The subalgebra

$$
\mathbb C_u:=\operatorname{span}_\mathbb R\{1,u\}
$$

is associative and commutative. Every nonzero element has the polar form

$$
z
=
e^{\sigma+u\theta}
=
e^\sigma e^{u\theta},
\qquad
\sigma\in\mathbb R,
\quad
\theta\in\mathbb R/2\pi\mathbb Z,
$$

so, as Lie groups,

$$
\boxed{
\mathbb C_u^\times
\cong
\mathbb R_{>0}\times U(1)_u,
\qquad
\log\mathbb R_{>0}\cong(\mathbb R,+).
}
$$

The two coordinates are not the same quantity:

- \(\sigma\) is a noncompact logarithmic modulus and composes additively;
- \(\theta\) is a compact phase defined modulo \(2\pi\).

This is an exact mathematical home for the proposed positivity/integrability duality. A positive scale character belongs to the radial factor; ordinary wave interference belongs to the associative \(U(1)\) factor. Selecting \(u\) supplies the ordinary complex structure required by local observables, but it does not select a state, Hamiltonian, phase law, or physical spacetime.

## The missing scale-to-phase character

Every continuous character from additive scale to the chosen phase circle has the form

$$
\chi_{\varpi,u}:
(\mathbb R,+)
\longrightarrow
U(1)_u,
\qquad
\chi_{\varpi,u}(\sigma)
=
e^{u\varpi\sigma}.
$$

If the wall goes further and identifies scale modulo a primitive period,

$$
\sigma\sim\sigma+\delta\sigma_g,
$$

then the quotient \(\mathbb R/\delta\sigma_g\mathbb Z\) is a circle and its integral characters are

$$
\chi_{n,u}([\sigma])
=
\exp\!\left(
2\pi u n\frac{\sigma}{\delta\sigma_g}
\right),
\qquad n\in\mathbb Z.
$$

This explains why a **periodic quotient** of logarithmic scale would generate a harmonic ladder. A discrete unit by itself is weaker: the Pontryagin dual of the lattice \(\delta\sigma_g\mathbb Z\) is a circle of continuous Bloch phases, so the unit alone does not select one \(\varpi\). Nor does the algebra prove that the unit-nat response \(s_*=1\) is the same object as \(\delta\sigma_g\), or that any such character acts on the primordial curvature field. Those are separate correspondence claims.

The construction can be made natural across the \(S^6\) family. If \(g\in G_2\) transports \(u\) to \(v=g(u)\), then

$$
g\!\left(e^{u\theta}\right)
=
e^{g(u)\theta}
=
e^{v\theta}.
$$

Thus the scalar phase \(\theta\) can be common while its local imaginary generator changes covariantly with the observable context. A groupoid of complex slices can therefore compare local phase presentations without declaring one preferred \(u\) globally. The physical selection of a context and the descent to records remain additional arrows.

## Hyperbolic scale and circular phase

The proposed grain--acoustic characteristic

$$
q(q^2+\kappa_g)=L_g^3,
\qquad
\kappa_g=\frac83,
\qquad
L_g=3+\Sigma_c,
$$

is solved by a hyperbolic triple-angle because

$$
\sinh3s=4\sinh^3s+3\sinh s.
$$

The trace-free de Sitter horizon cubic is solved by the compact triple-angle

$$
\cos3\theta=4\cos^3\theta-3\cos\theta.
$$

These identities exhibit a precise compact/noncompact sign contrast within one third-order motif:

$$
\begin{array}{ccl}
\text{noncompact positive scale}
&:&
\text{cubic plus linear}\quad(\sinh),
\\[4pt]
\text{compact local phase}
&:&
\text{cubic minus linear}\quad(\cos).
\end{array}
$$

The one-parameter groups can be written explicitly as

$$
B(s)
:=
\begin{pmatrix}
\cosh s&\sinh s\\
\sinh s&\cosh s
\end{pmatrix}
\in SO^+(1,1),
\qquad
R(\theta)
:=
\begin{pmatrix}
\cos\theta&\sin\theta\\
-\sin\theta&\cos\theta
\end{pmatrix}
\in SO(2).
$$

Both satisfy \(B(s_1)B(s_2)=B(s_1+s_2)\) and \(R(\theta_1)R(\theta_2)=R(\theta_1+\theta_2)\). The triple-angle polynomials follow from additive composition in these matrix representations: \(2\cos\theta\) and \(2\cosh s\) are traces or characters, whereas \(\sinh s\) is an off-diagonal matrix coefficient. A formal analytic continuation relates their parameters; a physical scale-to-phase descent does not follow from that continuation.

For Schwarzschild--de Sitter,

$$
r^3-L^2r+2mL^2=0,
$$

and its three roots are exactly

$$
r_k
=
\frac{2L}{\sqrt3}
\cos\!\left(\theta-\frac{2\pi k}{3}\right),
\qquad
\cos3\theta=-3\sqrt3\frac{m}{L}.
$$

This three-real-root trigonometric parametrization applies when

$$
\left|3\sqrt3\frac{m}{L}\right|\leq1,
$$

with \(0\leq m\leq L/(3\sqrt3)\) on the physical positive-mass Schwarzschild--de Sitter branch. The three roots are one phase sampled at \(120^\circ\) intervals. This is an exact \(A_2\) example of a cubic root system written trigonometrically, not yet a dynamical harmonic resonance and not evidence that CMB acoustic peaks are de Sitter horizons. The missing theorem is a real-form or descent functor carrying the positive scale characteristic to the compact phase representation while preserving the appropriate invariant.

## The local acoustic representation

Once a local complex fiber and a photon--baryon history exist, an ideal acoustic mode evolves in a two-dimensional quadrature plane. Write

$$
J_u
:=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
J_u^2=-I,
$$

and

$$
U_k(\eta_*)
:=
e^{J_u\Theta_k}
\in SO(2),
\qquad
\Theta_k
=
kr_s(\eta_*)+\delta_{\mathrm{tr}}(k).
$$

Here \(\delta_{\mathrm{tr}}(k)\) collects the phase shifts calculated by the declared transfer dynamics, including gravitational and neutrino effects. The \(n\)-th characters obey

$$
U_k^n=e^{J_un\Theta_k},
\qquad
\operatorname{tr}(U_k^n)
=
2\cos(n\Theta_k)
=
2T_n(\cos\Theta_k).
$$

These are genuine higher characters of one compact phase. The **ordinary acoustic peak sequence**, however, does not require \(n>1\): it comes from successive extrema of the fundamental \(n=1\) oscillator as \(k\) varies. If \(k_p\) labels those crossings, then in the ideal projection \(kD_M\simeq\ell\),

$$
\Theta(k_p)\simeq p\pi
\quad\Longrightarrow\quad
\ell_p^{\mathrm{ideal}}
\simeq
p\pi\frac{D_M}{r_s}
=
p\pi q_*.
$$

[[inbox/causal-grain-cmb-spectroscopy/grain-acoustic-characteristic|The grain--acoustic characteristic]] is a candidate law for \(q_*\), the common spacing scale. Higher \(n\) characters would instead describe additional harmonic observables or residuals. They must not be used to rederive the same peak index \(p\). The characteristic does not replace the local oscillator or its transfer corrections.

At source level, the temperature-like displacement and velocity-generated polarization quadratures have the ideal form

$$
S_T\propto\cos\Theta_k,
\qquad
S_E\propto\sin\Theta_k.
$$

Consequently,

$$
|S_T|^2\propto\frac{1+\cos2\Theta_k}{2},
\qquad
|S_E|^2\propto\frac{1-\cos2\Theta_k}{2},
$$

and

$$
S_TS_E
\propto
\frac12\sin2\Theta_k.
$$

This gives the qualitative TT/EE interleaving and TE sign alternation as three readings of one phase. The observed \(C_\ell^{TT}\), \(C_\ell^{TE}\), and \(C_\ell^{EE}\) are not these pointwise expressions: different line-of-sight kernels, visibility weighting, projection, reionization, diffusion, and lensing act before the recorded spectra are formed.

## Reflectionless phase as a deterministic correction

The exact [[binary-information-geometry/witten-darboux|Witten--Darboux system]] supplies a second useful precedent. Its continuum scattering data are

$$
R(\nu)=0,
\qquad
T(\nu)=\frac{\nu+i}{\nu-i},
\qquad
|T(\nu)|=1,
$$

with phase

$$
\delta_{\mathrm{WD}}(\nu)
=
2\arctan(\nu^{-1})
\pmod{2\pi},
\qquad
\nu>0.
$$

If a covariant wall-to-curvature map were to derive a dimensionless mode coordinate \(\nu(k)\), then

$$
\Theta_k
=
kr_s
+
\delta_{\mathrm{standard}}(k)
+
\delta_{\mathrm{WD}}(\nu(k))
$$

would be a rigid phase-coherence prediction: the wall changes phase with unit transmission and no reflected branch. This is more constrained than adding arbitrary oscillatory power. It remains an analogy until the same physical second-variation operator, domain, and mode map are constructed. It must also be distinguished from the established free-streaming-neutrino phase shift already present in standard cosmology.

## A cyclic selector inside \(A_2\)

Choose the cyclic subgroup \(C_3\subset W(A_2)\cong S_3\), and suppose a physical coupling assigns three local branches the regular cyclic phases

$$
\Theta_a
=
\Theta+\frac{2\pi a}{3},
\qquad a=0,1,2.
$$

At equal weight,

$$
\frac13\sum_{a=0}^{2}e^{i\Theta_a}=0,
$$

so the fundamental cancels. The first phase-dependent equal-weight moment occurs cubically:

$$
\frac13\sum_{a=0}^{2}\cos^3\Theta_a
=
\frac14\cos3\Theta.
$$

This is an exact \(C_3\) root-of-unity filter. \(A_2\) supplies a Weyl group containing that cyclic subgroup, but \(A_2\) alone does not force the phase coupling or equal weights. If the causal wall constructs this particular cyclic triplet, it gives a reason to search for a third-harmonic residual rather than an unrestricted catalogue of features. Unequal realized weights restore the fundamental through the character

$$
\Xi_1
:=
\sum_{a=0}^{2}w_ae^{2\pi ia/3}.
$$

Neither the branch weights nor their coupling to \(\zeta\) have been derived.

## Coherence is not the denial of covariance

Calling primordial Fourier amplitudes stochastic does not make the acoustic phase random. A statistically distributed amplitude \(A_k\) can multiply a common passive growing-mode response,

$$
X_k(\eta_*)
=
A_k\cos\Theta_k,
\qquad
V_k(\eta_*)
=
A_k\sin\Theta_k,
$$

while every mode retains the same phase convention determined by its causal history. The observed covariance describes the distribution of amplitudes and records; the TT/TE/EE phase relation describes coherent transfer. The cosmodynamic programme may take Born positivity or a record rule as constitutive and seek an algebraic reason for the common state and its phase without claiming that the measured sky has no statistical covariance.

This distinction identifies a plausible explanatory gain. Standard cosmology already supplies the synchronization through passive adiabatic growing-mode initial conditions and then tells how that coherent mode rings. The causal-grain programme must ground that condition more deeply or predict something beyond it; merely renaming standard coherence is not an empirical gain.

## Two distinct observational routes

The algebra permits two hypotheses that should not be blended in a fit:

1. **Characteristic route:** the total logarithmic depth \(\Sigma_c\) fixes the single acoustic count \(q_*\), while the standard phase remains approximately \(kr_s\). This is the economical primary route.
2. **Residual-character route:** an additionally constructed periodic quotient \(\sigma\sim\sigma+\delta\sigma_g\) produces a periodic character in \(\ln k\), possibly with the cyclic fundamental suppressed and a third harmonic surviving. This is a secondary feature search with the null amplitude as baseline.

The first predicts the global spacing. The second predicts an additional modulation. A successful model must declare which one is meant before comparing with data.

## The construction that would make this physics

The missing object is a natural scale--phase solder

$$
\mathfrak S_{\mathrm{sp}}:
(\text{positive wall character},\text{complex-slice groupoid},
\text{hot-history state})
\longrightarrow
(\zeta_k,\pi_{\zeta,k},U_k),
$$

with the following obligations:

1. fix the character frequency or the characteristic polynomial without fitting the CMB phase;
2. commute with \(G_2\)-transport among complex slices;
3. preserve positivity and the physical real condition on perturbations;
4. produce one phase law shared by TT, TE, and EE after their distinct transfer kernels;
5. reproduce the established neutrino, baryon, visibility, and projection corrections rather than relabeling them;
6. predict a held-out phase, polarization relation, BAO ratio, or representation-theoretic residual.

Failure of naturality, a need for independent TT/TE/EE phases, or an arbitrary function \(\nu(k)\) would turn the proposal into a redescription rather than an explanation.

# The Classical-Quantum Construction

A classical-quantum state assigns to each classical configuration an unnormalised density matrix. Requiring that this state space be preserved under dynamics — even when acting on part of a system — forces the evolution to be completely positive and trace preserving, and that requirement is what makes the classical sector diffuse and the quantum sector decohere. The two effects are locked together by a trade-off, and at its saturation the quantum state remains pure conditioned on the classical trajectory. The published paper's own gloss on that regime is that purity is preserved on the quantum system and no quantum information is lost.

## The state and what consistency costs

A CQ state associates to each classical configuration $z=(q,\dot q)$ an unnormalised density matrix

$$
\varrho(z,t)=p(z,t)\,\hat\sigma(z,t),
\qquad
\operatorname{Tr}_{\mathcal H}\varrho(z,t)=p(z,t)\geq0,
\qquad
\int dq\,\operatorname{Tr}\varrho=1 .
$$

Intuitively $p$ is the probability of the classical configuration and $\hat\sigma$ the quantum state *given* that configuration. Dynamics must map CQ states to CQ states, including when applied to a subsystem, so it must be a CPTP map on the hybrid. The classification of such dynamics is imported, not re-derived in these sources.

## The path integral

The configuration-space CQ path integral of [[sources/2rcd-dzcf.pdf|Oppenheim and Weller-Davies]] evolves the components of the density matrix with weight $e^{\mathcal I_{CQ}}$, where

$$
\mathcal I_{CQ}
=i\mathcal S_Q[q,\phi^+]-i\mathcal S_Q[q,\phi^-]
+i\mathcal S_{FV}[q,\phi^+,\phi^-]
+\mathcal S_{\mathrm{diff}}[q,\phi^+,\phi^-].
$$

The doubled fields $\phi^\pm$ are the ket and bra of the Schwinger--Keldysh or Feynman--Vernon formalism. The third term is a Feynman--Vernon influence action, which couples bra to ket and decoheres. The fourth is a classical-quantum Onsager--Machlup functional, which diffuses the classical variable around its deterministic equation of motion.

The decisive structural feature is the shape of that fourth term. In the purely classical case,

$$
\mathcal I_{OM}[q]=-\frac{1}{2D_2}\int dt\left(\ddot q-\frac{F(q,\dot q)}{m}\right)^2 ,
$$

which is *an equation of motion squared*. It suppresses paths in proportion to how badly they violate the equation of motion, and the deterministic solution is the global maximum of the weight rather than the only history. Everything downstream — the absence of ghosts, the reinterpretation of higher-derivative terms, the meaning of the saddle points — follows from the fact that this is a probability weight and not an amplitude.

## Gravity

For general relativity the construction gives

$$
\mathcal I_{CQ}=\int dx\Big[
i\bigl(\mathcal L_Q[\phi^+]-\mathcal L_Q[\phi^-]\bigr)
-\tfrac{\det[-g]}{8}\,\Delta T^{\mu\nu}D_{0,\mu\nu\rho\sigma}\Delta T^{\rho\sigma}
-\tfrac{\det[-g]}{128\pi^2G_N^2}\,\mathcal E^{\mu\nu}D_{0,\mu\nu\rho\sigma}\mathcal E^{\rho\sigma}\Big],
$$

with $\Delta T^{\mu\nu}=T^{\mu\nu+}-T^{\mu\nu-}$ and $\mathcal E^{\mu\nu}=G^{\mu\nu}+\Lambda g^{\mu\nu}-4\pi G_N(T^{\mu\nu+}+T^{\mu\nu-})$. *If* $D_{0,\mu\nu\rho\sigma}$ is positive definite, geometries that deviate from Einstein's equations sourced by the average stress-energy over bra and ket are suppressed; the quantum field is decohered in the stress-energy basis. The conditional matters, because it is exactly what fails below. The published construction establishes diffeomorphism invariance and complete positivity directly, without passing through a master equation, and notes that the theory may be inequivalent to the master-equation one.

Diffeomorphism invariance requires the kernel to be built from the metric. The candidate is the generalised deWitt metric, which in the renormalisation paper's normalisation reads

$$
D_{0,\mu\nu\rho\sigma}
=\frac{D_0}{2\sqrt{-g}}\bigl(g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}-2\beta g_{\mu\nu}g_{\rho\sigma}\bigr),
$$

and which in Lorentzian signature is **not** positive semidefinite outside the slow-moving weak-field limit. This is the construction's central technical wound. The published paper is explicit that because of it, normalisability is not proven — adding that it has since been shown for the scalar and tensor sectors. [[renormalisation]] argues the negative eigenvalues are benign because they sit in a boundary term or are cancelled by normalisation, and [[stochastic-modes]] localises them in a sector that is non-dynamical, subject to a further prescription.

## The trade-off, and conditional purity

Decoherence and diffusion are not separately adjustable. The published paper writes the trade-off as $4D_0\succeq D_2^{-1}$; the renormalisation paper writes its saturation as $4D_2=D_1D_0^{-1}D_1$, with the coefficients playing transposed roles. At saturation the bra--ket cross terms in the Feynman--Vernon action cancel those in the diffusion action, the $\phi^\pm$ integrals factorise, and

$$
\boxed{\ \hat\sigma(z,t)\ \text{remains pure, conditioned on the classical trajectory.}\ }
$$

The published paper proves this by the factorisation, calls it **a remarkable consequence of saturating the decoherence versus diffusion trade-off**, and notes that it was established by master-equation methods in the trajectories literature. Separately, and more generally, it introduces CQ dynamics with the remark that although the quantum state decoheres, purity is preserved on the quantum system, so that "there is no loss of quantum information" — a claim it immediately qualifies as holding "under certain natural conditions" and attributes to prior work. That general remark, not the saturation theorem, is the sentence this module's commentary quotes.

Whether conditional purity survives integrating out mediating gravitational modes is not settled in these sources, and [[stochastic-modes]] leaves related questions open about constraints at higher order and non-Markovianity.

## What the classical field cannot do

The published paper proves that **local** CQ dynamics cannot generate entanglement — requiring a sufficiently local noise kernel and that direct quantum interactions be negligible or screened. The hypothesis is load-bearing: Lindbladians with nonlocal noise kernels *can* generate entanglement, including those implementing Diósi--Penrose decoherence or the Tilloy--Diósi model.

The mechanism is the LOCC argument. Acting on a product state, the map produces a statistical mixture of product states — a *separable* state. So the classical field can establish ordinary classical correlation between two systems and cannot create entanglement between them. This is the theory's sharpest falsifiable commitment and makes gravitationally induced entanglement experiments decisive.

Relatedly, classicalisation is derived rather than postulated. There is no external collapse model — the classical nature of spacetime induces the decoherence, and the dynamics does not reduce to a Lindblad equation when the gravitational degrees of freedom are integrated out.

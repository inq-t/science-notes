# Renormalisation and the Sign of the Couplings

The pure-gravity postquantum path integral has the same functional form as quadratic gravity, whose renormalisability has been known since Stelle and whose ghost has been its standing objection. Because the classical-quantum couplings are real where quadratic gravity's are imaginary, the ghost does not arise, and the beta functions acquire the opposite sign — so that the dimensionless couplings grow in the ultraviolet and diffusion becomes larger at short distances. The result is *formal* renormalisability: power counting plus a mapping, with the positivity of the measure and the behaviour of pole prescriptions in loops still open.

Source: [[library/renormalisation-of-postquantum-gravity/inq|Grudka, Morris, Oppenheim, Russo and Sajjad]].

## The mapping

Using

$$
R_{\mu\nu}R^{\mu\nu}
=\tfrac12C^{\mu\nu\rho\sigma}C_{\mu\nu\rho\sigma}
+\tfrac13R^2
-\tfrac12\mathcal G,
$$

with $\mathcal G$ the Gauss--Bonnet term, the pure-gravity part of the CQ action can be rewritten in the curvature-squared basis of quadratic gravity. The pure-gravity action then takes the curvature-squared form
$\int dx\sqrt{-g}\,(-R^2/\Delta_2-C^2/2\Delta_w+\mathcal G/\Delta_{gb}+\alpha_1R+\alpha_0)$;
the compact vacuum form $-\tfrac{D_0c^6}{G_N^2}\int d^4x\sqrt{-g}(R^{\mu\nu}R_{\mu\nu}-\beta R^2)$ appears in the companion rotation-curve paper rather than here. Either way the propagator scales as $1/p^4$, which is the power-counting statement behind renormalisability. The difference from quadratic gravity is not the form but the coefficient: real here, imaginary there — the distinction developed in [[no-ghosts-and-real-couplings]].

## Consequences of the sign

**No ghosts or tachyons.** The higher-derivative terms are Onsager--Machlup structure rather than higher-derivative dynamics, so Ostrogradsky does not apply.

**Beta functions flip sign, and diffusion grows in the ultraviolet.** Because the beta functions depend on the *square* of the couplings, the authors expect them to resemble those computed for quadratic gravity but with opposite sign, so that the dimensionless couplings $\Delta_2$ and $\Delta_w$ run to infinity in the ultraviolet and **diffusion becomes larger at shorter distances**. This is an expectation rather than a computation, and even in quadratic gravity the direction of running depends on initial coupling values.

**Asymptotic freedom is inherited, not derived.** With $\alpha_1=0$ the action is that of scale-invariant gravity, which is known from the quadratic-gravity literature to be renormalisable and asymptotically free; the postquantum theory inherits the property through the mapping. It is a cited result about the related quantum theory, and should not be presented as a consequence of the sign flip.

**Positivity selects a theory.** Requiring the two-point function to be positive semidefinite appears to force the coefficients corresponding to a bare cosmological constant to vanish, and singles out the scale-invariant, asymptotically free theory. The authors immediately qualify this: the matter couplings differ from quadratic gravity's, so the condition may be relaxable, and "further work will clarify whether this condition can be relaxed."

**A new length scale.** Since the relevant dimensionless coupling runs to zero in the ultraviolet, dimensional transmutation should generate a scale, as in QCD. Its value would be experimental input, and gravity is tested only to millimetre scales.

**A conjecture about singularities.** If diffusion does grow at short distances, then near a would-be singularity the metric becomes progressively less constrained, and the Schwarzschild form need not hold. The authors conjecture that dominance of fluctuations over the singular deterministic solution is the mechanism by which the singularity is avoided. This is labelled a conjecture in the source and should not be repeated as a result.

## What is not established

The authors are explicit, and the list matters more than the headline:

- The deWitt kernel is not positive semidefinite in Lorentzian signature. Its negative eigenvalues "appear benign" because they correspond to a boundary term or one cancelled by normalisation — but the effect of the normalisation on the *magnetic part of the Weyl curvature* is not understood, and could have unintended consequences, possibly including loss of covariance.
- Dropping the Gauss--Bonnet term is standard in higher-derivative gravity, but "a fuller understanding of the boundary terms in a stochastic theory would be prudent."
- The $1/p^4$ propagator is positive semidefinite under the mod-squared pole prescription, but an infrared divergence appears, attributed to linearising about Minkowski rather than a spacetime with a horizon.
- Both scalar and tensor propagators must be shown positive semidefinite; this is taken further in [[stochastic-modes]].
- Pole prescriptions in loop diagrams are not understood well enough to guarantee that renormalisability and positivity hold together. This is the single largest gap: renormalisability is established at the level of power counting and a formal mapping, not by a completed programme.

The honest summary is the authors' own framing: the key remaining question is whether the renormalisation prescription retains completely positive dynamics.

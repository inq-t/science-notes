# Material Realizations and Fisher Response

The required \(46\)--\(47\,\mathrm{MeV}\) scale is allowed to be a correlation momentum, response stiffness, or resonance center rather than a particle pole. Two nearby material scales are structurally suggestive—the deuteron binding momentum and half the low-energy pion decay constant—but neither is selected by the wall construction. Their proper use is to sharpen the kind of microscopic theorem required, not to identify the grain by numerical resemblance.

## What Fisher response means here

For a regular probability family \(p(x\mid\theta)\), the Fisher response in the parameter direction \(\theta\) is

$$
I_{\theta\theta}
:=
\mathbb E_\theta
\left[
\left(\partial_\theta\ln p(X\mid\theta)\right)^2
\right].
$$

It measures local statistical distinguishability: how sharply the distribution changes under an infinitesimal parameter displacement. On a commuting faithful quantum family, the BKM response reduces to this classical Fisher form. [[program-core/response-registers|The response-register ledger]] owns the distinction from entropy, conserved charge, precision on spacetime, and gravitational canonical energy.

The relevant parameter is logarithmic scale. Let

$$
p_a(r)=ae^{-ar},
\qquad
r\ge0,
\qquad
\theta:=\ln a.
$$

Then

$$
\partial_\theta\ln p_a(r)=1-ar.
$$

Since \(ar\) is unit exponential,

$$
\mathbb E[ar]=1,
\qquad
\mathbb E[(ar)^2]=2,
$$

and therefore

$$
\boxed{
I_{\theta\theta}
=
\mathbb E[(1-ar)^2]
=1.
}
$$

This is the precise meaning of **unit log-scale Fisher response**. It is coordinate-natural for multiplicative scale changes. Calling it “one nat per cell” is an economical project presentation; it is not a proof that the BKM Hessian is thermodynamic entropy, and it avoids the unit dependence of raw differential entropy.

## The deuteron binding momentum

For neutron--proton reduced mass \(\mu_{np}\) and deuteron binding energy \(B_d\), the leading nonrelativistic binding momentum is

$$
\kappa_d
=
\sqrt{2\mu_{np}B_d}
\simeq45.70\,\mathrm{MeV}/c.
$$

Its reduced correlation length is

$$
\frac{\hbar}{\kappa_d}
\simeq4.318\,\mathrm{fm}.
$$

At large separation, the leading \(S\)-wave radial probability has the exponential form

$$
p(r)
\simeq
\frac{2\kappa_d}{\hbar}
\exp\left(-\frac{2\kappa_d r}{\hbar}\right).
$$

It therefore carries exactly the unit Fisher response above when differentiated with respect to \(\ln\kappa_d\). This is a genuine structural rhyme: the nearby scale is a correlation pole with a unit log-scale response, not merely a decimal from a particle table.

It is not an identification. The deuteron is composite and contingent on low-energy nuclear parameters. A universal gravitational calibration cannot depend on deuteron abundance or composition. Moreover, inserted into the fixed-physical-density oracle, \(45.70\,\mathrm{MeV}\) predicts roughly \(H_0=66.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\), below the branch used to define the target. The deuteron is therefore a useful model of the *type* of object sought and a currently disfavored literal carrier.

The numerical inputs are checked against the [Particle Data Group constants and nuclear data](https://pdg.lbl.gov/2024/reviews/constants_atomic_and_related.html); the calculation is reproduced in [[the-grain-of-causal-scale/grain_receipts.py|the receipt]].

## The pion vacuum-response scale

The charged-pion decay constant has two common conventions. In the PDG normalization,

$$
f_{\pi^+}\simeq130.2\,\mathrm{MeV},
$$

while the chiral convention is

$$
F_\pi:=\frac{f_{\pi^+}}{\sqrt2}
\simeq92.07\,\mathrm{MeV}.
$$

The nearby scale is specifically

$$
\boxed{
\frac{F_\pi}{2}
=
\frac{f_{\pi^+}}{2\sqrt2}
\simeq46.03\,\mathrm{MeV}.
}
$$

Writing merely “\(f_\pi/2\)” is convention-ambiguous: in the PDG convention it would mean \(65.1\,\mathrm{MeV}\). The source is the [PDG review of charged pseudoscalar decays](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-pseudoscalar-meson-decay-cons.pdf).

This candidate is intriguing because \(F_\pi\) is a vacuum-current response scale, not a pole mass. Its numerical match to the CMB grain is closer than the deuteron's. [[minimal-cosmodynamic-closure/unit-wall-correspondence|The unit wall correspondence]] now states two precise conjectural requirements: a dimensionful homothety from the normalized wall tangent to the chiral stiffness \(F_\pi^2/4\), followed by an independent identification of that response energy with the inverse bulk correlation ruler. No such operator map or ruler construction has been supplied, and the candidate remains a post-search siren until the composite conjecture returns an independent result.

## Why nearby numbers are cheap

The interval contains many manufactured combinations of Standard Model masses, decay constants, binding momenta, and simple numerical factors. [[the-grain-of-causal-scale/inbox/the-grain-in-every-register/entry.md|The exploratory siren census]] shows that sub-percent coincidences are statistically cheap once this search freedom is admitted. In particular, combinations such as \(2\pi\sqrt{m_em_\mu}\) can match even more closely while carrying no known mechanism.

A candidate earns promotion only if it supplies a map, not a resemblance. At minimum it must explain:

- why this operator or correlation function is the wall's carrier;
- why its scale is universal across matter rulers;
- why its effective positive-support multiplicity is \(\gamma=2\);
- why its log-scale response is \(s_*=1\);
- why its value is frozen at the crossing rather than running with \(H(N)\); and
- why the same object determines a second observable such as a width, residue, or line ratio.

## Pole mass, correlation scale, and resolution scale

Three meanings must remain separate:

| Scale | Definition | Could vary? |
|---|---|---|
| particle pole mass | pole of a matter two-point function in a declared renormalization scheme | fixed for a stable particle; running parameters are different objects |
| correlation or response scale | inverse decay length or stiffness extracted from a state/correlation function | can be state-, environment-, and channel-dependent |
| causal-capacity resolution | \(m_{\mathrm{cap}}(H)\propto H^{1/3}\) obtained by evaluating the ledger at a cut | presentation-dependent diagnostic unless fossilized |

The fact that a thermal bath is observer-dependent does not force a universal pole mass or \(G\) to run. It may instead change the KMS presentation \(\beta E_*\) of one fixed crossing fossil. Cosmic \(H\)-flow, modular flow, KMS temperature, and renormalization-group flow must be written with different parameters.

## A useful microscopic target

The material selector should be sought as a spectral statement. Let \(C_J(z)\) be a response or correlation function of an operator \(J\) that is independently connected to the descended wall projection. The required theorem would identify a presentation-invariant pole or threshold

$$
z_*=E_*-\frac i2\Gamma_*
$$

and derive

$$
E_*^3=\frac38E_P^2(\hbar H_c),
\qquad
\Gamma_*=\hbar H_c,
$$

with rank-two residue and unit logarithmic response. The deuteron and \(F_\pi/2\) then become controlled tests: either the derived pole lands on a known material structure for a stated reason, or the grain is a new collective scale.

Until that theorem exists, the epistemically correct statement is:

> The closure requires a \(4.2\,\mathrm{fm}\) correlation grain. Known low-energy matter contains suggestive structures in that neighborhood, but the carrier is unselected.

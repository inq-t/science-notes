# The Trace Residue as a Scale Cocycle

For a homogeneous expanding state, the dimensionless integral of the nonconformal trace ratio is an exact additive cocycle on ordered logarithmic-scale intervals: \(\Xi_\Theta(N_1,N_2)=\int_{N_1}^{N_2}(\rho-3p)\rho^{-1}\,\mathrm dN=\log[(a_2^4\rho_2)/(a_1^4\rho_1)]\). It vanishes during ideal radiation transport and records the accumulated failure of the radiation scaling law without leaving behind a microscopic object. This is the first standard cosmological quantity in the programme that shares the proposed causal-grain valuation's additive composition law. Their domains and meanings remain different: a wall-to-stress realization must still show that one primitive pre-clock class controls this FLRW interval coboundary, and a full material transfer must show that its profile survives in CMB or BAO observables.

**Status: [EXACT] for the homogeneous conservation identity and cocycle law; [EXACT UNDER THE DECLARED EQUILIBRIUM PARAMETRIZATION] for the thermal entropy ledger; [INTERPRETIVE] for calling the cocycle a trace fossil; [OPEN] for quantization, wall realization, Yang--Mills transport, and observable identifiability.**

## The exact relative invariant

Set \(c=1\), let

$$
N:=\log a,
\qquad
\Theta:=\rho-3p,
$$

and assume that \(\rho\) is positive and absolutely continuous on the scale interval under consideration. Homogeneous conservation of the declared total stress tensor holds almost everywhere and gives

$$
\frac{\mathrm d\rho}{\mathrm dN}
=-3(\rho+p)
=-4\rho+\Theta.
\tag{TR1}
$$

It follows that

$$
\frac{\mathrm d}{\mathrm dN}
\log\!\left(e^{4N}\rho(N)\right)
=
\frac{\Theta(N)}{\rho(N)}.
\tag{TR2}
$$

Define the **trace residue** between two ordered scale cuts by

$$
\boxed{
\Xi_\Theta(N_1,N_2)
:=
\int_{N_1}^{N_2}
\frac{\Theta(N)}{\rho(N)}\,\mathrm dN
=
\log\!\left(
\frac{e^{4N_2}\rho(N_2)}
{e^{4N_1}\rho(N_1)}
\right).}
\tag{TR3}
$$

Equivalently,

$$
\Xi_\Theta(N_1,N_2)
=
4(N_2-N_1)
+
\log\frac{\rho(N_2)}{\rho(N_1)}.
\tag{TR4}
$$

This form makes two invariances transparent. The quantity is dimensionless, and it is unchanged by translating the arbitrary origin of logarithmic scale, \(N\mapsto N+N_0\).

For three ordered cuts,

$$
\boxed{
\Xi_\Theta(N_1,N_3)
=
\Xi_\Theta(N_1,N_2)
+
\Xi_\Theta(N_2,N_3).}
\tag{TR5}
$$

Thus \(\Xi_\Theta\) is an additive one-cocycle on the pair groupoid of scale cuts, and

$$
\mathcal X_\Theta(N_1,N_2)
:=e^{\Xi_\Theta(N_1,N_2)}
=
\frac{a_2^4\rho_2}{a_1^4\rho_1}
\tag{TR6}
$$

is its multiplicative character. Because (TR3) is the endpoint difference of \(\log(a^4\rho)\), this cocycle is a coboundary on one contractible history interval. It is a relative scale record, not by itself a topological charge or an irreversible arrow. A physical orientation, branch restriction, or record map must still be supplied.

## What the residue remembers

For a constant equation-of-state ratio \(w=p/\rho\),

$$
\Xi_\Theta(N_1,N_2)
=(1-3w)(N_2-N_1).
\tag{TR7}
$$

Ideal radiation has \(w=1/3\), hence \(\Xi_\Theta=0\). A finite episode with \(\Theta\neq0\) changes the subsequent constant value carried by \(a^4\rho\) by the factor \(e^{\Xi_\Theta}\) after the system returns to radiation scaling. Positive and negative trace contributions can cancel, so it leaves a nontrivial endpoint residue exactly when \(\Xi_\Theta\neq0\). In that precise sense an episode can be historically spent while its endpoint residue remains.

The residue does **not** uniquely mean rest mass:

- nonrelativistic matter gives \(\Theta\simeq\rho\);
- vacuum stress, interactions, and quantum anomalies also contribute;
- a statewise expectation of \(\Theta\) can vanish without proving that the theory has no massive sector; and
- a nonzero trace anomaly supplies no lower bound on the vacuum Poincare Casimir.

The safe statement is therefore:

> \(\Xi_\Theta\) measures accumulated nonconformality of one homogeneous history. Calling it a record of “mass engagement” additionally requires a material theorem identifying the relevant trace profile with the realization of stable rest-bearing or dwell sectors.

## Entropy and the trace are related but not identical

The entropy bookkeeping becomes exact under an equilibrium parametrization. In this subsection, temperature is measured in energy units and entropy in units of \(k_B\), equivalently \(k_B=\hbar=c=1\). The conserved density \(\rho\) in (TR1) is assumed to be exactly the equilibrated sector parameterized below. If that thermal sector exchanges energy with another component, its continuity equation contains a source and the following ledger is not automatically the total trace cocycle. Write

$$
\rho(T)
=
\frac{\pi^2}{30}g_{*\rho}(T)T^4,
\qquad
s(T)
=
\frac{2\pi^2}{45}g_{*s}(T)T^3,
\qquad
S_c:=a^3s,
\tag{TR8}
$$

where \(S_c\) is entropy in a fixed comoving coordinate volume. Algebraically eliminating \(aT\) gives

$$
a^4\rho
\propto
g_{*\rho}\,
g_{*s}^{-4/3}\,
S_c^{4/3}.
\tag{TR9}
$$

Hence, between two equilibrium endpoints,

$$
\boxed{
\Xi_\Theta
=
\log\frac{g_{*\rho,2}}{g_{*\rho,1}}
-
\frac43\log\frac{g_{*s,2}}{g_{*s,1}}
+
\frac43\log\frac{S_{c,2}}{S_{c,1}}.}
\tag{TR10}
$$

For adiabatic evolution, \(S_{c,2}=S_{c,1}\), so

$$
\Xi_\Theta^{\mathrm{ad}}
=
\log\frac{g_{*\rho,2}}{g_{*\rho,1}}
-
\frac43\log\frac{g_{*s,2}}{g_{*s,1}}.
\tag{TR11}
$$

This is an important distinction. A trace episode need not be entropy production: an adiabatic change in the effective energy and entropy degrees of freedom already changes the radiation-normalized energy ledger. Conversely, genuine comoving entropy production contributes the last term of (TR10). The appearance of an arrow in thermodynamic records must therefore not be inferred from \(\Xi_\Theta\) alone. [[library/primordial-gravitational-waves-precisely/inq|The thermal-history degree-of-freedom tables]] keep \(g_{*\rho}\) and \(g_{*s}\) separate, while [[library/equation-of-state-in-2-plus-1-flavor-qcd/inq|the HotQCD equation of state]] supplies a concrete nonconformal crossover rather than a literal instantaneous switch. [[standard-model-trace-fossil-diagnostic]] uses these degree counts to show that \(46.27\,\mathrm{MeV}\) is on the lower-temperature trace tail rather than at the sampled QCD trace maximum.

## The operator-typed comparison with the causal grain

The proposed primitive grain and the exact trace residue occupy parallel but currently disconnected registers. Three fossil notions must not be collapsed: \(\Xi_\Theta\) is an intermediate FLRW material-history functional; it is neither the whole-solution calibration fossil, which is constant on the cuts of one solution, nor the final observable fossil \(O=\mathscr T\circ\mathscr R\), which is a weighted and generally lossy CMB/BAO image.

| Register | Object | Exact operation |
|---|---|---|
| pre-clock realization | oriented wall class \(q\) or index \(\nu(q)\) | composition of realization arrows |
| abstract scale | additive valuation \(v(q)\) | \(v(q_2q_1)=v(q_2)+v(q_1)\) |
| homogeneous material history | trace residue \(\Xi_\Theta(N_1,N_2)\) | interval concatenation (TR5) |
| observable readout | CMB/BAO transfer functional | many-to-one integration over the realized history |
| physical mass | lower edge of \(H^2-c^2\mathbf P^2\) | joint spectrum on the reconstructed vacuum carrier |

The exact match of *algebraic shape* is

$$
v(q_2q_1)=v(q_2)+v(q_1),
\qquad
\Xi_\Theta(N_1,N_3)
=
\Xi_\Theta(N_1,N_2)+\Xi_\Theta(N_2,N_3).
\tag{TR12}
$$

The missing physical solder is a natural, normalization-rigid map such as

$$
\boxed{
q
\xmapsto{\ \mathfrak W_{\mathrm{mat}}\ }
\bigl(\Phi(q),\rho_q,p_q,\ldots\bigr)
\xmapsto{\ \int_{\Phi(q)}(\rho_q-3p_q)\rho_q^{-1}\,\mathrm dN\ }
\Xi_\Theta[\Phi(q)],
\qquad
\Xi_\Theta[\Phi(q)]
\stackrel{?}{=}
\alpha\,v(q),}
\tag{TR13}
$$

Here \(\Phi(q)=[N_-(q),N_+(q)]\) is itself an independently constructed realization of pre-clock order as an FLRW scale interval, not notation smuggled in after the fact, and \(\alpha\) must be fixed before consulting a mass, CMB, or BAO target. Equality on one interval would determine only a fitted normalization; the proposed solder must respect composition on a family of composable realization arrows. Nothing presently proves discreteness of \(\Xi_\Theta\), equality with one nat, or equality with the Fredholm index. Equation (TR13) is a stopping condition, not a derived quantization rule.

This is also where the “mass switched on” language becomes precise enough to test. The wall does not operate on a pre-existing particle mass parameter. It would operate on the admissible realization class. The material map would then return a trace and constitutive history; only after Poincare reconstruction could a separate Casimir theorem say that the realized carrier contains a stable rest-bearing sector.

## Why one integrated charge cannot determine BAO

The endpoint cocycle forgets the location and shape of its source. Distinct profiles can have the same \(\Xi_\Theta\), while the sound horizon weights epochs differently. Under the fixed-initial-radiation-density condition used in [[causal-grain-as-a-mass-engagement-fossil]], its first variation is already a weighted history functional:

$$
\boxed{
\delta\Xi_\Theta(N_i,N_d)
=
\frac{\delta\rho(N_d)}{\rho(N_d)}
=
\int_{N_i}^{N_d}
K_{\Xi\leftarrow\Theta}(s)\,\delta\Theta(s)\,\mathrm ds,}
\tag{TR14}
$$

where

$$
K_{\Xi\leftarrow\Theta}(s)
=
\frac{e^{4(s-N_d)}}{\rho(N_d)}.
\tag{TR15}
$$

By contrast, the expansion-only acoustic response is

$$
\delta r_d
=
\int K_\Theta(N)\,\delta\Theta(N)\,\mathrm dN,
\tag{TR16}
$$

with a nonconstant negative kernel that tends to zero as \(s\to N_d\) under the declared flat-FLRW assumptions. The positive kernel (TR15) and this acoustic kernel are not proportional. Therefore equal first-order trace residues need not give equal acoustic shifts even in the restricted expansion channel, and equal acoustic rulers need not imply equal trace residues once loading, opacity, drag, abundance, and primordial-state variations are allowed.

A defensible “shell casing” interpretation consequently requires a common-origin certificate consisting of:

1. an upstream realization signature;
2. its dimensionless trace-residue image;
3. a predeclared family of weighted history functionals that separates an independently specified profile class; and
4. a forward transfer into CMB, polarization, lensing, and galaxy BAO observables.

A harmonic “sweet spot” would then mean nonzero, structured overlap of the realized source profile with these transfer kernels. Nonzero overlap gives a response, not detectability or common origin; it must also survive nuisance projection with sufficient signal-to-noise. It would not mean that a \(4.264\,\mathrm{fm}\) wave was stretched into a \(147\,\mathrm{Mpc}\) ruler.

## The fossil readout is a quotient operator

This gives an exact answer to the question “what does the operator operate on?” Let \(X\) be a declared infinite-dimensional **real** Banach space of admissible material-source perturbations on frozen scale and wavenumber domains. Its construction must specify the component function spaces, gauge and constraint quotient, reference scales, and product norm; complex Fourier components are realified subject to the appropriate conjugate-symmetry condition. A source vector can include distinct components,

$$
x
=
\bigl(
\delta\Theta(N),
\delta R_b(N),
\delta\dot\tau_{\mathrm{opt}}(N),
\delta S(k,N),
\delta\mathcal I(k),
\ldots
\bigr),
\tag{TR17}
$$

where \(\delta S\) is an active perturbative stress source and \(\delta\mathcal I\) changes the primordial or boundary data. The background trace, constitutive loading, active-source, and initial-condition channels are different arguments of the transfer theory; the phrase “mass wave” must not slide among them.

Let \(\mathcal O:U\subset X\to Y\) be the resulting forward map after a background, gauge, recombination prescription, nuisance convention, and observable bins have been frozen. Normalize every output by a declared reference quantity and, when a covariance is used, whiten it, so that \(Y=\mathbb R^{m+1}\) is a dimensionless finite-dimensional normed space. Assume \(\mathcal O\) is Fréchet differentiable at the baseline \(x_0\). Its bounded derivative has coordinate functionals \(\ell_0,\ldots,\ell_m\in X^*\). A merely formal or Gâteaux linearization would not be enough for the closed-kernel statement below. For example, \(\ell_0\) can be the normalized version of (TR14), another component can be the normalized expansion contribution (TR16), and further components can be dimensionless CMB or BAO band responses. Define

$$
\mathfrak F:=D\mathcal O(x_0):X\longrightarrow Y,
\qquad
\mathfrak F(x)
=
\bigl(\ell_0(x),\ldots,\ell_m(x)\bigr).
\tag{TR18}
$$

Because \(\mathfrak F\) has finite rank,

$$
x\sim_{\mathfrak F}y
\quad\Longleftrightarrow\quad
x-y\in\ker\mathfrak F
\tag{TR19}
$$

is the exact equality relation for noiseless **linearized predictions** under the frozen conventions. Its kernel is closed, has codimension at most \(m+1\), and remains infinite-dimensional. An exact linearized prediction vector therefore determines a class \([x]\in X/\ker\mathfrak F\), not a unique history. This nonuniqueness is already present before experimental noise. Actual finite data with noise and marginalized nuisances define a likelihood over quotient classes or neighborhoods, not one exact coset.

The result also states the legitimate escape. If an independently derived engagement theory restricts the allowed source profiles to a finite-dimensional subspace \(V\subset X\), then

$$
\boxed{
\mathfrak F|_V\text{ is injective}
\quad\Longleftrightarrow\quad
V\cap\ker\mathfrak F=\{0\}
\quad\Longleftrightarrow\quad
\{\ell_j|_V\}_{j=0}^{m}\text{ spans }V^*.}
\tag{TR20}
$$

For a one-profile amplitude model \(V=\operatorname{span}\{x_*\}\) with \(x_*\neq0\), the condition reduces to \(\ell_j(x_*)\neq0\) for at least one predeclared channel. For a multi-parameter \(V\), the restricted response must have rank \(\dim V\). On a nonlinear profile family this derivative test is only local; it does not prove global identifiability. Even in the linear case, quantitatively stable recovery after nuisance projection requires a declared codomain covariance or norm and a positive smallest singular value, not injectivity alone. For a genuinely oscillatory resonance claim, mere overlap is insufficient: the material realization must construct an evolution or Green operator with the claimed mode, pole, or spectral enhancement and then show its phase-coherent image across observables. [[library/distinguishing-causal-seeds-from-inflation/inq|Active causal seeds]] and passive primordial acoustic data have different phase signatures, so these routes are empirically distinguishable in principle.

Thus BAO can be a shell casing only in a disciplined sense: it is one coordinate of \(\mathfrak F(x)\). To infer that it came from a mass-engagement transition, the theory must first restrict \(x\) for independent reasons, then pass (TR20), and finally show that the same upstream invariant also reaches the metric/common-count and Casimir branches.

## Stopping conditions

This route becomes explanatory only if it:

- constructs \(\mathfrak W_{\mathrm{mat}}\) without assuming FLRW clock time in the pre-observable domain;
- derives the normalization in (TR13) rather than setting it to one;
- distinguishes a crossover profile from an instantaneous event;
- proves how the same upstream signature enters both the common-count metric branch and the trace/material branch;
- computes the full correlated transfer, not only the expansion contribution;
- identifies observables whose common nuisance-marginalized images are separated; and
- keeps the Yang--Mills vacuum Casimir theorem independent of the later full-QCD and cosmological fossil theorem.

The exact gain is narrower but substantial: **one exact summary available for a spent nonconformal episode is an additive defect of radiation-normalized scale transport, not a surviving microscopic length.**

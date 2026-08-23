# Misner Logarithmic Time

Misner's logarithmic time is the logarithm of the inverse mean scale factor, conventionally written $\Omega=-\ln(a/a_*)=-\tfrac13\ln(V/V_*)$ for a homogeneous universe. Equal intervals of $\Omega$ represent equal *ratios* of size rather than equal durations, and a zero-volume singularity is pushed to $\Omega\to+\infty$. In Hamiltonian cosmology this variable separates the overall volume of space from its anisotropic shape and, on any branch where the volume changes monotonically, can serve as an internal clock for classical or quantum evolution. It is not proper time, does not by itself fix the lapse, and is not a global clock through a bounce or a point of maximum expansion.

## Definition from the spatial metric

Write a diagonal homogeneous spatial metric in the form

$$
h_{ij}=a_*^2 e^{-2\Omega}(e^{2\beta})_{ij},
\qquad
\operatorname{tr}\beta=0.
$$

The traceless matrix $\beta$ changes shape without changing volume. For the usual two anisotropy variables,

$$
\beta=\operatorname{diag}
\left(
\beta_+ + \sqrt3\,\beta_-,
\beta_+ - \sqrt3\,\beta_-,
-2\beta_+
\right).
$$

Since $\det(e^{2\beta})=1$, a fixed homogeneous spatial cell has

$$
\frac{V}{V_*}=e^{-3\Omega},
\qquad
\Omega=-\frac13\ln\frac{V}{V_*}.
$$

Thus $(\Omega,\beta_+,\beta_-)$ split geometry into one **scale** coordinate and two **shape** coordinates. In the isotropic limit $\beta_+=\beta_-=0$, the ordinary scale factor is simply

$$
\frac{a}{a_*}=e^{-\Omega}.
$$

The reference scales $a_*$ and $V_*$ only set the additive zero of $\Omega$. Differences are reference-independent:

$$
\Delta\Omega
=-\ln\frac{a_2}{a_1}
=-\frac13\ln\frac{V_2}{V_1}.
$$

A change $\Delta\Omega=1$ therefore means that the mean scale factor has changed by a factor $e^{-1}$ and the volume by $e^{-3}$.

## In what sense it is time

General relativity does not attach physical significance to an arbitrary coordinate label $t$. For a homogeneous metric

$$
\mathrm ds^2=-N(t)^2\mathrm dt^2+h_{ij}(t)\,\omega^i\omega^j,
$$

proper time along the homogeneous normal observers is $\mathrm d\tau=N\,\mathrm dt$. Define the mean Hubble rate by

$$
H:=\frac13\frac{\mathrm d\ln V}{\mathrm d\tau}.
$$

Then

$$
\frac{\mathrm d\Omega}{\mathrm d\tau}=-H.
$$

If $H$ never vanishes on the branch under study, $\Omega$ is monotonic and every dynamical variable $F$ may be described relationally as $F(\Omega)$:

$$
\frac{\mathrm dF}{\mathrm d\Omega}
=-\frac1H\frac{\mathrm dF}{\mathrm d\tau}.
$$

Calling $\Omega$ a time variable means making this **internal-clock choice**. It does not mean that $\Omega$ measures the readings of a comoving clock. One may choose coordinates so that $t=\Omega$ locally, but that is a gauge condition and determines a corresponding lapse; the definition of $\Omega$ alone makes no such choice.

## Why the logarithm matters

### It turns multiplicative expansion into translation

Cosmological scale factors span enormous ranges. Taking a logarithm converts repeated rescaling into addition. The number of expansion e-folds is

$$
N_e:=\ln\frac{a}{a_*}=-\Omega.
$$

The $N_e$ convention in [[flrw-kinematics|FLRW scale-section kinematics]] therefore runs in the opposite direction to the conventional Misner $\Omega$: expansion increases $N_e$ and decreases $\Omega$.

If $a_*$ is today's scale factor, then

$$
\Omega-\Omega_0=\ln(1+z),
$$

so logarithmic redshift is the same scale clock up to its zero point.

### It sends a finite-proper-time singularity to infinite clock time

For a power-law scale factor $a\propto\tau^p$ with $p>0$,

$$
\Omega=\text{constant}-p\ln\tau.
$$

The big-bang limit $\tau\to0^+$ occurs at $\Omega\to+\infty$. This magnifies the asymptotic regime: arbitrarily small ratios of scale occupy finite increments of $\Omega$, making sequences of Kasner epochs and curvature-wall collisions easier to resolve. The reparametrization does not remove or regularize the physical singularity; it only relocates it to an infinite value of the chosen clock.

### It exposes the causal structure of minisuperspace

After the ADM reduction of a diagonal homogeneous model, the Hamiltonian constraint has the schematic form

$$
\mathcal C
=A(\Omega)
\left[
-p_\Omega^2+p_+^2+p_-^2
+\mathcal U(\Omega,\beta_+,\beta_-;\text{matter})
\right]
\approx0,
$$

where $A(\Omega)$ is a nonzero convention-dependent factor. Numerical constants and the normalization of the potential vary among authors, but the relative minus sign is structural: the scale direction is timelike in the Lorentzian DeWitt metric on this minisuperspace, while the anisotropy directions are spacelike. This makes $\Omega$ the natural candidate for the evolution coordinate.

## How it is used

### Classical Bianchi and Mixmaster dynamics

In vacuum Bianchi I, the curvature potential vanishes. The point $(\beta_+,\beta_-)$ then follows straight segments as a function of $\Omega$; these are the Kasner solutions in scale-shape variables.

In Bianchi IX, the curvature of the homogeneous spatial slices produces steep exponential terms in $\mathcal U$. The evolution can be pictured as a point moving in the anisotropy plane and reflecting from moving potential walls. Free segments correspond to Kasner epochs and reflections change the Kasner exponents. Because $\Omega$ increases without bound toward the classical singularity, it orders the successive epochs by logarithmic contraction. Misner--Chitré variables refine this construction by transforming the asymptotic moving-wall problem into a billiard description with stationary walls on a hyperbolic space.

This picture is useful because the overall contraction is carried by one coordinate while the nontrivial gravitational dynamics appears as changing shape. It underlies much of the Hamiltonian and chaotic analysis of Bianchi VIII and IX cosmologies.

### Deparametrizing the Hamiltonian constraint

On a monotonic branch the constraint may be solved for the momentum conjugate to the clock,

$$
p_\Omega
=\pm\sqrt{p_+^2+p_-^2+\mathcal U}.
$$

The sign distinguishes the expanding and contracting branches, subject to the author's momentum convention. Substituting one branch back into the action gives a reduced system in which $(\beta_+,\beta_-)$ evolve with respect to $\Omega$. This is an example of **deparametrization**: a constrained, reparametrization-invariant system is rewritten as relational evolution using one of its own degrees of freedom as the clock.

### Wheeler--DeWitt quantum cosmology

Canonical quantization promotes the momenta to derivatives. Ignoring factor-ordering details, the constraint becomes a Klein--Gordon-like equation on minisuperspace,

$$
\left[
\frac{\partial^2}{\partial\Omega^2}
-\frac{\partial^2}{\partial\beta_+^2}
-\frac{\partial^2}{\partial\beta_-^2}
+\widehat{\mathcal U}
\right]\Psi(\Omega,\beta_+,\beta_-)=0.
$$

The sign pattern suggests reading $\Omega$ as the time coordinate and the anisotropies as the evolving degrees of freedom. Equivalently, after choosing a frequency or expansion/contraction branch, one can try to write a first-order evolution equation in $\Omega$ using the square root of the remaining operator.

That interpretation is useful but not automatic. The potential generally depends on $\Omega$; choosing a square-root branch, inner product, factor ordering, and self-adjoint domain introduces real physical and mathematical questions. Positive- and negative-frequency sectors can also mix when the effective potential is time dependent. The logarithmic volume variable supplies a candidate internal time, not a complete solution to the problem of time in quantum gravity.

### Isotropic cosmology and numerical evolution

For FLRW models, $\beta_\pm=0$ and Misner time reduces to minus the usual e-fold variable. Evolution equations can be rewritten with $\Omega$, $N_e$, or $\ln(1+z)$ as the independent variable. This is convenient for inflation, long cosmological integrations, and fixed fractional changes of scale. In this isotropic setting the construction is elementary, but the name “Misner variables” is most informative in anisotropic models, where the separation between volume and shape does real work.

## Conventions and limitations

The sign is not universal. A common alternative uses

$$
\alpha:=\ln(a/a_*)=-\Omega.
$$

| Feature | Conventional $\Omega$ used here | Alternative $\alpha$ |
|---|---:|---:|
| Mean scale factor | $a/a_*=e^{-\Omega}$ | $a/a_*=e^\alpha$ |
| Volume ratio | $V/V_*=e^{-3\Omega}$ | $V/V_*=e^{3\alpha}$ |
| Expansion | $\Omega$ decreases | $\alpha$ increases |
| Zero-volume limit | $\Omega\to+\infty$ | $\alpha\to-\infty$ |

Some literature calls the volume itself, a multiple of its logarithm, or a lapse-adapted coordinate parameter “Misner time.” The metric definition is more reliable than the name: check whether the spatial metric carries $e^{-2\Omega}$ or $e^{2\alpha}$ and which direction approaches the singularity.

The main limitations are intrinsic to using geometry as a clock:

- At a bounce, turnaround, or maximum expansion, $H=0$ and $\mathrm d\Omega/\mathrm d\tau=0$. The same $\Omega$ then labels more than one event, so separate monotonic branches or a different clock are required.
- In a homogeneous model there is a single well-defined cell volume up to a fixed reference factor. In a general inhomogeneous spacetime, a global volume depends on the foliation and need not provide a local or monotonic clock.
- Sending $V=0$ to $\Omega=+\infty$ does not establish geodesic completeness or singularity resolution.
- Results that depend on rates per unit $\Omega$ are not rates per unit proper time; conversion requires the lapse or $H$.

## Sources

- Charles W. Misner, [“Quantum Cosmology. I”](sources/1969-misner-quantum-cosmology-i.pdf) (1969; [publisher record](https://doi.org/10.1103/PhysRev.186.1319)): the Hamiltonian treatment of homogeneous cosmologies and its quantum version.
- Charles W. Misner, [“Mixmaster Universe”](sources/1969-misner-mixmaster-universe.pdf) (1969; [publisher record](https://doi.org/10.1103/PhysRevLett.22.1071)): the Bianchi IX singular dynamics that made the logarithmic scale variable especially useful.
- Charles W. Misner, [“The Mixmaster Cosmological Metrics”](sources/1994-misner-mixmaster-cosmological-metrics-arxiv-source/9405068.tex) (1994; [repository record](https://arxiv.org/abs/gr-qc/9405068)): a retrospective account of the model, its equations, and the Misner--Chitré development. The complete arXiv source package and figures are preserved locally.
- Leonardo Agostini, Francesco Cianfrani, and Giovanni Montani, [“Probabilistic interpretation of the wave function for the Bianchi I model”](sources/2017-agostini-cianfrani-montani-bianchi-i-internal-time.pdf) (2017; [repository record](https://arxiv.org/abs/1704.08502)): an explicit comparison of reduced-phase-space and semiclassical treatments using the isotropic Misner variable as time.

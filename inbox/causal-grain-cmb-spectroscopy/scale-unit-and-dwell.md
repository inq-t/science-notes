# The Causal Grain as a Unit of Scale and Dwell

Calling the causal grain a **scale unit** is coherent only after separating its native algebraic order from its later clock and ruler presentations. The causal unit is first a primitive positive index in a local compression semigroup induced by an ambient reversible whole; an additive valuation assigns that index one unit of scale. Length, dwell, mass, density, entropy response, and logarithmic position are downstream realizations. This removes a recurrent ambiguity: the grain is neither one particle per cell, a smallest spacetime voxel, nor an integer jump of clock time or one e-fold.

## Causal order before ruler

Let \(G\) be an ambient reversible symmetry group and \(W\) a local accessible context. The local causal order is carried by the compression semigroup

$$
S_W
:=
\{g\in G:
\operatorname{Ad}_g\mathcal A(W)
\subseteq\mathcal A(W)\},
$$

whose reversible stabilizer is

$$
K_W:=S_W\cap S_W^{-1}.
$$

The full semigroup need not be commutative or singly generated. A scale assignment is an additive valuation

$$
v:S_W\longrightarrow\Gamma_+,
\qquad
v(st)=v(s)+v(t),
\qquad
v(k)=0\quad(k\in K_W),
$$

or equivalently the multiplicative character

$$
\chi_{\mathrm{sc}}(s):=e^{v(s)}.
$$

Suppose the causal order supplies a primitive positive class \(q_{\mathrm{ord}}\in S_W/K_W\), while positive completion at the wall supplies a carrier-changing event \(q_{\mathrm{wall}}\) with integer boundary index

$$
\nu(q_{\mathrm{wall}})=+1.
$$

The proposed unit correspondence is

$$
q_{\mathrm{ord}}
\longmapsto
q_{\mathrm{wall}}
\xmapsto{\mathfrak W_{\mathrm{sc}}}
s_g:=v(q_{\mathrm{ord}}).
$$

This proposed weld is the precise premetric meaning of “one grain of causality becomes one scale unit.” The number \(+1\) belongs to oriented index or spectral flow, while \(s_g\) belongs to the scale character. Setting \(s_g=1\) is a normalization or a further unit-response law, not a consequence of positivity alone.

This native unit is not automatically

- one unit of Shannon or von Neumann entropy;
- the value of an intensive Fisher metric;
- one e-fold of expansion;
- one unit of length;
- one quantum of energy; or
- one unit of scalar curvature;
- one interval of proper or conformal time.

The metric ruler comes from a later carrier-changing realization,

$$
\mathfrak W_\lambda:
s_g\longmapsto\lambda_*.
$$

Under the selected rank-two common-count ansatz,

$$
\eta_*A_c
=
\gamma s_*\frac{V_c}{\lambda_*^3},
\qquad
(\gamma,s_*)=(2,1),
$$

and under the imported Einstein area presentation,

$$
\lambda_*^3
=
\frac{8}{3}\ell_P^2R_c.
$$

The same causal index is thus assigned a scale valuation and later realized metrically. [[inbox/causal-grain-cmb-spectroscopy/causal-order-before-clock-time|Causal order before clock time]] owns the complete global-to-local hierarchy.

## Continuous scale is not yet a scale lattice

[[minimal-cosmodynamic-closure/unit-wall-correspondence|The unit-wall correspondence]] uses the continuous coordinate

$$
s=N-N_c,
\qquad
N=\ln\frac{a}{a_0},
\qquad
\frac{\mathrm ds}{\mathrm dN}=1.
$$

This fixes the rate and normalization of the scale character. It does not imply

$$
s\in\mathbb Z.
$$

Likewise,

$$
g_{ss}^{\mathrm{BKM}}(0)=1
$$

is an intensive local-curvature statement, whereas

$$
s_*=1
$$

is the proposed extensive channel weight. Equating them without the carrier-changing correspondence would turn a coordinate normalization into a count theorem.

A continuous positive character has no canonical primitive interval: if \(v(r)=\alpha\ln r\) is admissible, rescaling \(\alpha\) changes every proposed unit. A grain therefore requires an independently constructed integer index or a discrete positive image. Only after the wall supplies such a quantizer may one write

$$
I_{g,n}=[\sigma_0+n\delta\sigma_g,
\sigma_0+(n+1)\delta\sigma_g),
$$

with constant \(\delta\sigma_g\) and one boundary index per cell. That is the **discrete-scale postulate**. When \(\sigma=\ln(k/k_0)\), it yields

$$
k_n=k_0e^{n\delta\sigma_g},
$$

so successive marks form a geometric sequence. The literal identification \(\delta\sigma_g=1\) would predict a dilation ratio \(e\); it is a strong empirical claim, not a consequence of \(\mathrm ds/\mathrm dN=1\).

## Dwell is a local clock presentation

After a conformal class, metric scale, local Lorentz frame, and worldline have been realized, the metric image \(\lambda_g\) may be converted into

$$
\tau_g:=\frac{\lambda_g}{c}.
$$

On an FLRW history,

$$
H\tau_g
=
\frac{\lambda_g}{R_A}
$$

is the instantaneous fraction of a scale e-fold represented by one local light-crossing dwell. It is useful because \(H\) has native type \(T^{-1}\), but it is downstream of the causal order and scale valuation. A finite tick gives \(\Delta N=\int H\,\mathrm d\tau\), not generally the product of one fixed \(H\) and one fixed dwell.

## Born dwell is a measure of residence, not matter density

The repository contains one concrete dwell identity. In the dust-clock minisuperspace model of [[inbox/the-box-spectrum-functor/the-box-spectrum-functor|the box-spectrum functor]], a declared factor ordering gives

$$
i\hbar\frac{\partial\psi}{\partial\tau}
=\widehat H\psi,
\qquad
\widehat H\psi=m\psi,
$$

and the WKB current gives

$$
|\psi(a)|^2\,\mathrm da=C\,\mathrm d\eta.
$$

Thus the Born weight in a scale-factor interval is proportional to conformal time spent there. The claim is exact only at the stated WKB/current level and depends on clock choice, ordering, state, and boundary conditions; naive WKB fails at a turning point and must be matched there. It is not the radiation-era wave equation of the photon--baryon plasma.

For a future quantization of a scale carrier, the analogous construction would be

$$
\mathrm d\mu_{\mathrm{dw}}(\sigma)
=D(\sigma)\,\mathrm d\sigma,
$$

where, after a polarization and positive Hilbert measure exist,

$$
D(\sigma)
:=
\int_L|\Psi(x,\sigma)|^2\,\mathrm d\mu_L(x).
$$

This \(D\) is a marginal Born-dwell density on scale. It becomes a primordial curvature spectrum only after a constitutive map such as

$$
\mathfrak S_\zeta:
D(\sigma),\ \text{phase data},\ \text{branch data}
\longmapsto
\mathcal P_\zeta(k).
$$

Writing \(\mathcal P_\zeta=D\) by inspection would confuse a state measure on the pregeometric carrier with the covariance of a gauge-invariant Lorentzian perturbation.

## The register ledger

The words *dwell*, *information*, *entropy*, *density*, *mass*, and *scale* touch the same construction but carry different types.

| Register | Object | Meaning | Required bridge |
|---|---|---|---|
| scale coordinate | \(s=N-N_c\) or \(\sigma=\ln(k/k_0)\) | continuous logarithmic address | core-to-cosmic scale map |
| intensive response | \(g_{ss}^{\mathrm{BKM}}\) | local distinguishability under scale displacement | selected state and tangent |
| channel entropy | \(-\sum p_a\ln p_a\) | uncertainty of a normalized finite allocation | declared sample space |
| extensive scale count | \(\mu_{\mathrm{sc}}\), \(s_*=1\) | additive response weight of one realized unit | channel-weight correspondence |
| dwell | \(\mathrm d\mu_{\mathrm{dw}}\) | residence weight with respect to a chosen clock/scale measure | quantization, state, and clock |
| bulk cell density | \(\lambda_*^{-3}\) | inverse effective correlation volume | metric realization |
| areal response density | \(\eta_*\) | response count per area | area-writing correspondence |
| horizon entropy density | \(k_Bc^3/(4\hbar G)\) | Bekenstein--Hawking entropy per area | Einstein/horizon solder |
| effective cosmic density | \(\rho_X\) | homogeneous source in the imported FLRW equations | source square |
| mass presentation | \(m_*=\hbar/(c\lambda_*)\) | optional reduced-Compton ruler | pole/correlation solder |
| curvature response | \(\mathcal K_{\mu\nu}{}^{\rho\sigma}\) | metric-channel susceptibility | covariant perturbation theory |

The source square of the minimal closure is

$$
\rho_X(N)
=
\frac{k_BT_c}{2V_c}G^\perp_{NN}(N),
$$

not \(\rho_X=m_*/\lambda_*^3\). The mass ruler and the homogeneous response density arrive through independent maps.

## A decisive filled-cell contradiction

The distinction is numerically compulsory. Using the diagnostic CMB-conditioned values

$$
\lambda_*=4.264\,\mathrm{fm},
\qquad
m_*c^2=46.27\,\mathrm{MeV},
$$

a literal rest energy in every correlation volume would give

$$
u_{\mathrm{cell}}
:=
\frac{m_*c^2}{\lambda_*^3}
\simeq
9.6\times10^{31}\,\mathrm{J\,m^{-3}}.
$$

The crossing critical energy density for \(H_c=83.1058\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\) is only

$$
u_{\mathrm{crit},c}
=
\frac{3H_c^2c^2}{8\pi G}
\simeq
1.17\times10^{-9}\,\mathrm{J\,m^{-3}}.
$$

The one-particle-per-cell reading overshoots by about \(8.2\times10^{40}\), or \(1.6\times10^{41}\) if the two area-writing channels are counted as two material occupants. The cells therefore cannot be an ordinary gas of \(46\,\mathrm{MeV}\) rest masses. They are response/correlation cells unless an entirely different energy bookkeeping law is constructed.

## When may the grain be called a gravity quantum?

A graviton is a spin-two excitation of a quantized metric perturbation on a declared background or asymptotic state. A quantum of curvature would likewise require a metric or connection observable with a discrete spectrum or a pole carrying specified spin, residue, sign, and coupling. The common-count length alone supplies none of these.

The missing covariant object could have the schematic form

$$
\delta T^{g}_{\mu\nu}(\omega,k)
=
\mathcal K_{\mu\nu}{}^{\rho\sigma}
(\omega,k;m_*,\Gamma_*)
\delta g_{\rho\sigma}(\omega,k).
$$

Only if the same associative operator produces a pole at \(m_*\), couples it to the physical transverse-traceless or scalar metric channel, and returns the correct low-energy gravitational response would “gravity quantum” become more than an interpretation. Until then, the strongest warranted phrase is:

> The grain is a candidate quantum of **causal-scale realization**, with an optional mass ruler and an unconstructed gravitational solder.

## Failure conditions

The scale-unit reading fails or must be weakened if

- no additive positive measure \(\mu_{\mathrm{sc}}\) can be constructed from the wall carrier;
- the supposed unit depends arbitrarily on reparameterizing \(s\);
- the same \(s_*=1\) is used both as an intensive metric normalization and as an extensive count without a preservation theorem;
- no invariant correlation pole or other independent ruler selects \(\lambda_*\);
- the material-energy interpretation requires the excluded filled-cell density; or
- a claimed discrete scale period is absent at the sensitivity predicted by a frozen wall-to-CMB map.

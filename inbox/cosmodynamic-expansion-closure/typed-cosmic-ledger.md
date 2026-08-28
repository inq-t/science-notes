# The Cosmic Horizon Ledger Has Rank One

At fixed \(G\), \(c\), \(\hbar\), and \(k_B\), the flat Einstein--FLRW apparent-horizon radius, quasilocal mass and energy, critical density, area entropy, canonical horizon temperature, and Planck resolution depth are invertible functions of one positive number \(H\). They are different physical presentations, but not independent data capable of determining an expansion law by themselves.

## The age words name different objects

The repository does not have one unqualified *natural age*.

| Name | Definition | Type |
|---|---|---|
| scale-age | \(N=\ln(a/a_*)\) | additive coordinate on multiplicative scale change |
| Misner logarithmic time | \(\Omega=-N=-\frac13\ln(V/V_*)\) in isotropic FLRW | oppositely oriented internal coordinate on a monotone branch |
| proper age | \(\tau_2-\tau_1=\int_{N_1}^{N_2}\mathrm dN/H(N)\) | elapsed clock duration after \(H(N)\) is known |
| resolution depth | \(X_P=\ln(R_A/\ell_P)\) | logarithmic horizon-to-Planck ratio |
| nat | the unit attached to a natural logarithm of a dimensionless information quantity | not a clock interval |

Thus \(\Omega=-N\) is an exact coordinate conversion, while

$$
\frac{\mathrm dN}{\mathrm d\tau}=H
$$

is dynamical calibration. [[cosmodynamics/scale-age|Scale-age]], [[misner-log-time/inq|Misner logarithmic time]], and [[hyperbolic-counting/two-nats-per-e-fold|resolution depth]] must not be merged merely because all use logarithms.

## Rank-one proposition

**[EXACT AFTER THE DECLARED HORIZON AND EINSTEIN STIPULATIONS]** Define

$$
t_P:=\sqrt{\frac{\hbar G}{c^5}},
\qquad
\ell_P:=ct_P,
\qquad
R_A:=\frac cH.
$$

For a spatially flat Einstein--FLRW apparent horizon,

$$
\begin{aligned}
M_A&=\frac{c^3}{2GH},
&E_A&=\frac{c^5}{2GH},\\
\rho_{\mathrm{crit}}^{(E)}&=\frac{3c^2H^2}{8\pi G},
&\iota_A:=\frac{S_A}{k_B}&=\frac{\pi}{(Ht_P)^2},\\
k_BT_A&=\frac{\hbar H}{2\pi},
&X_P&=\ln\frac{R_A}{\ell_P}.
\end{aligned}
$$

Each displayed quantity determines \(H\) uniquely:

$$
\boxed{
H
=\frac c{R_A}
=\frac{c^3}{2GM_A}
=\frac{c^5}{2GE_A}
=\sqrt{\frac{8\pi G\rho_{\mathrm{crit}}^{(E)}}{3c^2}}
=\frac{2\pi k_BT_A}{\hbar}
=\frac1{t_P}\sqrt{\frac\pi{\iota_A}}.}
$$

Consequently the horizon data have one scalar degree of freedom once the constants and geometric prescription are fixed. Their joint identity

$$
k_BT_A\,\iota_A=E_A=\rho_{\mathrm{crit}}^{(E)}V_A
$$

is the [[conformal-scale-geometry/hawking-friedmann-identity|Hawking--Friedmann identity]]. It is a powerful compatibility relation, not another equation for the unknown \(H\).

The collapse is especially transparent in Planck units. With

$$
m_P:=\sqrt{\frac{\hbar c}{G}},
\qquad
E_P:=m_Pc^2,
\qquad
T_P:=\frac{E_P}{k_B},
$$

one obtains

$$
\boxed{
\frac{M_A}{m_P}
=\frac{E_A}{E_P}
=\frac12e^{X_P},
\qquad
\iota_A=\pi e^{2X_P},
\qquad
\frac{T_A}{T_P}=\frac1{2\pi}e^{-X_P}.}
$$

The famous huge mass and entropy numbers and tiny horizon temperature are powers of one height \(X_P\), not separate large-number coincidences.

“Total” must also be qualified. \(M_A\) and \(E_A\) are quasilocal quantities assigned to the apparent-horizon sphere. They are not the total mass or energy of an entire spatial slice, which can be noncompact and has no ordinary global time-translation charge.

## One expansion curve, several ledgers

For \(E(N):=H(N)/H_0\), the same history appears as

$$
\frac{R_A(N)}{R_{A0}}
=\frac{M_A(N)}{M_{A0}}
=\frac{E_A(N)}{E_{A0}}
=E(N)^{-1},
$$

$$
\frac{T_A(N)}{T_{A0}}=E(N),
\qquad
\frac{\iota_A(N)}{\iota_{A0}}=E(N)^{-2},
\qquad
X_P(N)-X_{P0}=-\ln E(N).
$$

The exact derivative

$$
\frac{\mathrm dX_P}{\mathrm dN}=1+q,
\qquad
\frac{\mathrm d\ln\iota_A}{\mathrm dN}=2(1+q)
$$

is therefore a reconstruction of the expansion shape. It is not an independent law selecting that shape. In particular, “two nats per e-fold” means two units of *log-ledger growth per resolution-depth e-fold*; it does not mean that the horizon gains only two entropy nats.

## Minimal independent inputs

The forward calculation needs one datum from each applicable row, not every item in a row.

| Role | Admissible datum | What it supplies |
|---|---|---|
| absolute calibration | one of \(H_0,R_{A0},M_{A0},E_{A0},\rho_{\mathrm{crit},0},T_{A0},\iota_{A0},X_{P0}\) | height and physical units |
| present sector position | \(r_0:=\rho_{X0}/\rho_{\mathrm{non-X},0}\), with non-\(X\) contents declared | present response fraction under flatness |
| radiation split | \(\Omega_{r0}\), or \(T_{\mathrm{CMB}},N_{\mathrm{eff}}\), and a neutrino prescription | separates matter from radiation |
| constitutive member | response family, \(\nu\), \(\mathfrak R_c\), residual sector, conservation law, and root policy | dimensionless shape |
| independent chronology | a clock or stellar age not inferred from the same background | test of \(H_0t_0\), or an alternative calibration |

The horizon temperature in the first row is not \(T_{\mathrm{CMB}}\). The former is fixed by \(H\); the latter is matter-sector data that helps determine radiation. Likewise, horizon entropy is not matter entropy, BKM capacity, edge entropy, or record count. [[compatible-with-existing-physics/cosmic-structure-tests|Tests of cosmic structure]] owns the wider type audit.

## What an absolute wall calculation would change

If a physical wall independently returned an absolute crossing ledger \(\iota_c\), without using measured \(H_0\), a \(G\)-defined area, or the target expansion history, then

$$
\boxed{H_c=\frac1{t_P}\sqrt{\frac\pi{\iota_c}}}
$$

would calibrate the relative curve. The current core wall returns relative trace capacity \(\tau(e_N)=e^N\), with a movable origin under weight rescaling; it does not yet return this absolute physical count. Feeding the observed \(H_c\) into the area law, calculating \(\iota_c\), and then claiming to predict \(H_c\) would simply reverse an identity.

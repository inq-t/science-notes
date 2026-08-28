# Logarithmic Time, Grain Ticks, E-Folds, and Nats

The repository’s repeated use of Misner time, e-folds, trace scaling, resolution depth, and nats has one exact common skeleton: the logarithm turns multiplication of positive scales or weights into addition. The causal grain lies one level earlier, as a primitive positive index carrying a presentation-invariant scale valuation in the global-to-local order. Under the strong causal-wall correspondence, dual trace scale, cosmic scale-age, horizon resolution, and information depth become distinct affine presentations of that additive architecture. Only after Lorentzian and metric realization does the Hubble rate convert the grain’s local dwell \(\tau_g=\lambda_g/c\) into the clock reading \(H\tau_g\); this is not the grain’s native definition.

## One mathematical operation in several registers

The continuous homomorphism

$$
\ln:(\mathbb R_{>0},\times)
\longrightarrow
(\mathbb R,+)
$$

turns a composed ratio into a sum:

$$
\ln(xy)=\ln x+\ln y.
$$

The relevant repository variables are all instances of this operation:

| Register | Additive coordinate | Multiplicative datum |
|---|---|---|
| scale age | \(N=\ln(a/a_*)\) | ratio of scale factors |
| Misner time | \(\Omega=-N=-\tfrac13\ln(V/V_*)\) | inverse mean scale or volume ratio |
| redshift | \(\ln(1+z)=-N\) relative to today | inverse scale factor |
| core dual trace scale | \(\tau_{\mathrm{core}}\circ\beta_s=e^s\tau_{\mathrm{core}}\) | trace rescaling on the canonical core |
| resolution depth | \(N_P=\ln(R_A/\ell_P)\) | horizon-to-Planck ratio |
| grain depth | \(\Sigma_A=\ln(R_A/\lambda_g)\) | horizon-to-grain ratio |
| information | \(I=\ln W\) nats | multiplicity or likelihood ratio |

[[cosmodynamics/scale-age|Scale age]] proves the additive composition law for \(N\). [[misner-log-time/inq|Misner logarithmic time]] makes the scale direction an internal clock on a monotonic branch. [[scale-as-modular-observable/inq|Scale as a modular observable]] and [[minimal-cosmodynamic-closure/unit-wall-correspondence|the unit-wall correspondence]] propose that the core trace character and cosmic scale character have the same unit slope.

The recurrence is therefore structural. The distinction is equally structural: causal order, proper time, conformal time, modular flow, core dual scaling, scale age, resolution depth, and information are different domains until a map relates them.

## The logarithm first grades causal processes

Let \(S_W\) be the local compression semigroup induced by an ambient reversible whole, with reversible stabilizer \(K_W=S_W\cap S_W^{-1}\). The native scale datum is

$$
v:S_W\longrightarrow\Gamma_+,
\qquad
v(st)=v(s)+v(t),
\qquad
v(K_W)=0.
$$

Its multiplicative form is \(\chi_{\mathrm{sc}}=e^v\). A wall index \(\nu(q)=+1\) may select one primitive process \(q\); the proposed scale grain is the welded value \(v(q)=s_g\). A continuous character alone has no smallest positive unit, so the discrete index is not optional if *grain* is meant literally.

Everything below this section is a realization of \(v\) on more familiar carriers. [[inbox/causal-grain-cmb-spectroscopy/causal-order-before-clock-time|Causal order before clock time]] owns the prior global/local construction.

## Hubble rate is the local time-to-scale converter

By definition,

$$
N=\ln\frac{a}{a_*},
\qquad
H=\frac{1}{a}\frac{\mathrm da}{\mathrm d\tau}
=\frac{\mathrm dN}{\mathrm d\tau},
$$

where \(\tau\) is FLRW cosmic proper time on the declared homogeneous branch. Thus an interval of proper time has the scale increment

$$
\mathrm dN=H\,\mathrm d\tau.
$$

Let one causal grain have the light-crossing dwell

$$
\tau_g:=\frac{\lambda_g}{c}.
$$

One grain tick at epoch \(N\) corresponds to

$$
\boxed{
\delta N_g(N)
:=H(N)\tau_g(N)
=\frac{\lambda_g(N)}{R_A(N)}.
}
$$

This is the precise local-clock representation of a grain already defined algebraically. It is not generally one whole e-fold. It is the instantaneous epoch-relative fraction of an e-fold traversed during one grain dwell. Its inverse,

$$
\boxed{
\frac{1}{\delta N_g}
=\frac{\omega_g}{H}
=\frac{R_A}{\lambda_g}
=e^{\Sigma_A},
\qquad
\omega_g:=\tau_g^{-1},
}
$$

is the instantaneous number of grain ticks per differential e-fold at that epoch. It equals a finite one-e-fold count only when the rate can be treated as constant or explicitly integrated.

At the diagnostic crossing,

$$
\tau_*\simeq1.4223\times10^{-23}\,\mathrm s,
\qquad
H_c\simeq2.6933\times10^{-18}\,\mathrm s^{-1},
$$

so

$$
\delta N_*
=H_c\tau_*
\simeq3.83\times10^{-41},
$$

and the instantaneous crossing rate is about \(2.61\times10^{40}\) grain ticks per differential e-fold. Metres and seconds disappear from the invariant product.

## One ratio in four physical costumes

Let

$$
T_H:=H^{-1},
\qquad
R_A:=\frac{c}{H},
\qquad
E_H:=\hbar H,
$$

and

$$
\tau_g:=\frac{\lambda_g}{c},
\qquad
\omega_g:=\tau_g^{-1},
\qquad
E_g:=\hbar\omega_g.
$$

Then

$$
\boxed{
\frac{\lambda_g}{R_A}
=
\frac{\tau_g}{T_H}
=
\frac{H}{\omega_g}
=
\frac{E_H}{E_g}
=H\tau_g.
}
$$

Length, dwell, frequency, and energy are not four independent facts. They are presentations of one dimensionless scale ratio through \(c\) and \(\hbar\). This is why the Hubble constant’s native type \(T^{-1}\) is so important: it compares directly with a resonance frequency without any imported metre stick.

At the selected crossing these identities belong to the granted common-count package. Writing them as functions of an arbitrary epoch \(N\) invokes the additional **live-cut axiom** that the same closure is re-evaluated on every cosmological slice. All epoch-dependent derivatives below are conditional on that extension.

## The common-count law is a clock-frequency mean

Use

$$
\ell_P=ct_P,
\qquad
R_A=\frac{c}{H},
\qquad
\lambda_g=c\tau_g
$$

in the common-count relation

$$
\lambda_g^3
=\frac83\ell_P^2R_A.
$$

All powers of \(c\) cancel:

$$
\boxed{
\tau_g^3
=
\frac83\,t_P^2H^{-1}.
}
$$

Equivalently,

$$
\boxed{
(H\tau_g)^3
=
\frac83(Ht_P)^2.
}
$$

In frequency and energy dressings,

$$
\boxed{
\omega_g^3
=
\frac38\,\omega_P^2H,
\qquad
E_g^3
=
\frac38\,E_P^2E_H,
}
$$

where \(\omega_P=t_P^{-1}\) and \(E_P=\hbar/t_P\).

The causal grain is therefore a weighted geometric mean of the ultraviolet Planck clock and the infrared Hubble clock. For any fixed reference duration \(t_0>0\), the dimensionless logarithmic form is

$$
\boxed{
\ln\frac{\tau_g}{t_0}
=
\frac23\ln\frac{t_P}{t_0}
+\frac13\ln\frac{H^{-1}}{t_0}
+\frac13\ln\frac83.
}
$$

The programme’s \(2/3\) appears here as an exact UV/IR weight: two powers of the Planck time and one power of the cosmic time produce the intermediate dwell. The exponent comes from the areal factor \(\ell_P^2\) followed by the cubic root in the three-volume common count; the rank-two wall assumptions contribute to the coefficient \(8/3\), not by themselves to the exponent. This is a derived scaling law, not a nearby-number observation.

## Resolution depth, grain depth, and the ledger

Define

$$
N_P:=\ln\frac{R_A}{\ell_P},
\qquad
\Sigma_A:=\ln\frac{R_A}{\lambda_g}.
$$

The common-count clock equation gives the affine relation

$$
\boxed{
\Sigma_A
=
\frac23N_P
-\frac13\ln\frac83.
}
$$

For the Einstein apparent-horizon ledger,

$$
\iota_A
=
\frac{\pi R_A^2}{\ell_P^2}
=
\pi e^{2N_P}.
$$

Hence

$$
\boxed{
\ln\iota_A
=
\ln\frac{8\pi}{3}
+3\Sigma_A,
}
$$

or

$$
\iota_A
=
\frac{8\pi}{3}e^{3\Sigma_A}.
$$

The chain is now explicit:

$$
N
\xrightarrow{\,1+q\,}
N_P
\xrightarrow{\,2/3\,}
\Sigma_A
\xrightarrow{\,3\,}
\ln\iota_A.
$$

Indeed,

$$
\frac{\mathrm dN_P}{\mathrm dN}=1+q,
$$

so

$$
\boxed{
\frac{\mathrm d\Sigma_A}{\mathrm dN}
=\frac23(1+q),
\qquad
\frac{\mathrm d\ln\iota_A}{\mathrm dN}
=2(1+q).
}
$$

This is the exact bridge among cosmic e-folds, resolution e-folds, grain depth, deceleration, and logarithmic ledger growth.

## What “nats per e-fold” means

A nat is the unit obtained when information is a natural logarithm. If \(W\) is a multiplicity, then

$$
I=\ln W
$$

is measured in nats. For a Bekenstein--Hawking horizon,

$$
\frac{S_A}{k_B}=\iota_A
$$

is itself an entropy in nats because it is interpreted as the logarithm of an underlying microstate multiplicity.

Two different statements must be kept distinct:

1. **Primitive channel weight:** \(s_*=1\) assigns one unit of additive response—and, under the strong entropy solder, one nat—to each primitive channel. With \(\gamma=2\), one effective bulk cell writes two channel-nats into the areal ledger:

   $$
   \iota_A=2N_{\mathrm{cells}}.
   $$

2. **Logarithmic ledger growth:** 

   $$
   \frac{\mathrm d\ln\iota_A}{\mathrm dN_P}=2
   $$

   says that one resolution e-fold multiplies the entropy count \(\iota_A\) by \(e^2\). It does not say that the enormous entropy \(\iota_A\) increases by only two additive nats.

Thus “two nats per e-fold” is safest when read as **two natural-log units of ledger growth per resolution e-fold**. The additive number of newly written horizon nats is instead

$$
\frac{\mathrm d\iota_A}{\mathrm dN}
=2(1+q)\iota_A.
$$

The same coefficient \(2\) occurs in the rank-two channel count and in codimension-two area growth. Under the granted common correspondence this is a candidate unification; without it, the two appearances remain typed separately.

## Expansion and coordinate-light slowing

In flat FLRW,

$$
c_\chi:=\frac{c}{a}
$$

is the radial comoving coordinate speed of light. Therefore

$$
\frac{\mathrm d\ln a}{\mathrm d\tau}=H,
\qquad
\frac{\mathrm d\ln c_\chi}{\mathrm d\tau}=-H.
$$

Across a finite grain dwell beginning at \(\tau\), the exact increments are

$$
\Delta_g\ln a
=
\int_{\tau}^{\tau+\tau_g}H(\tau')\,\mathrm d\tau'
\simeq
+H(\tau)\tau_g,
$$

$$
\Delta_g\ln c_\chi
=
-\int_{\tau}^{\tau+\tau_g}H(\tau')\,\mathrm d\tau'
\simeq
-H(\tau)\tau_g.
$$

The final approximations are the instantaneous, first-order reading \(\delta N_g=H(\tau)\tau_g\). The grain writes exactly opposite logarithmic increments into the expansion and coordinate-light registers when both are integrated over the same interval. At \(u=N-N_c\),

$$
\frac{a}{a_c}=e^u,
\qquad
\frac{c_\chi}{c_{\chi,c}}=e^{-u}.
$$

Normalizing this reciprocal pair gives

$$
p_\pm(u)
=
\frac{e^{\pm u}}{2\cosh u},
$$

which is precisely the balanced family of minimal cosmodynamics. The conjectural interpretive payoff is large: the wall’s binary information geometry may be the normalized relation between the cosmos getting larger and light covering less comoving coordinate distance per unit proper time.

## CMB phase in logarithmic time

Any physical oscillator phase satisfies

$$
\mathrm d\theta_k=\omega_{k,\mathrm{phys}}\,\mathrm d\tau.
$$

Because \(\mathrm dN=H\,\mathrm d\tau\),

$$
\boxed{
\theta_k(N_*)
=
\int^{N_*}
\frac{\omega_{k,\mathrm{phys}}(N)}{H(N)}
\,\mathrm dN.
}
$$

Insert the grain frequency:

$$
\frac{\omega_k}{H}
=
\frac{\omega_k}{\omega_g}
\,
\frac{\omega_g}{H}
=
\frac{\omega_k}{\omega_g}
e^{\Sigma_A}.
$$

Therefore

$$
\boxed{
\theta_k(N_*)
=
\int^{N_*}
\frac{\omega_k}{\omega_g}
e^{\Sigma_A}
\,\mathrm dN.
}
$$

For the photon--baryon acoustic mode,

$$
\omega_k
=
\frac{c_s k}{a},
\qquad
\frac{\omega_k}{\omega_g}
=
\frac{k\lambda_g}{a}
\,
\frac{c_s}{c}.
$$

Writing

$$
\kappa_g:=\frac{k\lambda_g}{a},
\qquad
\mathfrak n_{\gamma b}:=\frac{c}{c_s},
$$

gives the scale-only resonance law

$$
\boxed{
\theta_k(N_*)
=
\int^{N_*}
\kappa_g(N)
\frac{e^{\Sigma_A(N)}}
{\mathfrak n_{\gamma b}(N)}
\,\mathrm dN.
}
$$

Every factor is dimensionless. The CMB harmonics occur when this accumulated phase reaches approximately \(m\pi\). Here \(N\) is logarithmic scale age; the repository's Misner coordinate has the opposite orientation, \(\Omega=-N\).

The grain factors cancel exactly:

$$
\kappa_g
\frac{e^{\Sigma_A}}{\mathfrak n_{\gamma b}}
=
\frac{k\lambda_g}{a}
\frac{R_A}{\lambda_g}
\frac{c_s}{c}
=
\frac{k c_s}{aH}.
$$

Thus this bridge is an exact dimensionless re-expression of

$$
\theta_k=\int k c_s\,\mathrm d\eta,
$$

not by itself a new acoustic prediction. That cancellation is appropriate for a scale unit: changing the local ruler cannot change the phase. Explanatory content begins when the common causal construction fixes the functions that survive the cancellation—\(H(N)\), \(c_s(N)\) through baryonic dwell, opacity and recombination, or the primordial state—or predicts a residual that cannot be absorbed into the standard transfer history.

## The unification claim

The maximally economical claim is not that all logarithmic quantities are numerically equal. It is:

> A single additive scale character is represented as cosmic e-fold, inverse coordinate-light e-fold, modular trace exponent, grain-clock fraction, resolution depth, and natural-log information. The physical coefficients arise from dimension, deceleration, channel rank, and the chosen causal region.

This claim earns its keep if the unit correspondence fixes those coefficients once and the resulting phase/count laws predict the background, acoustic ruler, TT/TE/EE phase geometry, horizon information, and a scale residual without introducing a separate normalization for each register.

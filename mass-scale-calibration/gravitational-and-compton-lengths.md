# Gravitational and Compton Lengths

For a given positive mass, the constants \(G,c,\hbar\) define a gravitational length and a reciprocal reduced Compton length. Their product is the Planck area and their ratio is a dimensionless gravitational coupling. These exact conversions compare an already supplied mass with geometric scales; they neither generate that mass nor establish gravitational localization dynamics.

Take \(G,c,\hbar>0\). For a mass \(m>0\), define the gravitational length without the conventional Schwarzschild factor \(2\),

$$
\ell_G(m):=\frac{Gm}{c^2}.
\tag{S2}
$$

Conversely,

$$
m=\frac{c^2}{G}\,\ell_G.
\tag{S3}
$$

Thus \(G/c^2\) converts mass into a gravitational length, while \(c^2/G\) is a mass-per-length modulus. In the Einstein equation,

$$
G_{ab}+\Lambda g_{ab}
=
\frac{8\pi G}{c^4}T_{ab},
\tag{S4}
$$

the coefficient \(8\pi G/c^4\) converts stress--energy into curvature. It is useful, but interpretive, to call this a geometric **compliance**; the Einstein--Hilbert coefficient \(c^3/(16\pi G)\), with its convention-dependent normalization, supplies the reciprocal stiffness language at the action level. Hence larger \(G\) means stronger curvature response in the field equation and a smaller action coefficient. The constant \(G\) is not itself the amplitude of a scalar scale field. [[deriving-value-of-g/areal-information-modulus#Curvature response|Curvature response]] and [[deriving-value-of-g/areal-information-modulus#Action stiffness|action stiffness]] give the two normalization conventions.

For \(m>0\), the reduced Compton wavelength is

$$
\lambda_C(m):=\frac{\hbar}{mc}.
\tag{S5}
$$

The two length presentations obey the exact identities

$$
\boxed{
\ell_G(m)\lambda_C(m)
=
\frac{\hbar G}{c^3}
=
\ell_P^2,}
\tag{S6}
$$

$$
\boxed{
\frac{\ell_G(m)}{\lambda_C(m)}
=
\frac{Gm^2}{\hbar c}
=
\alpha_G(m).}
\tag{S7}
$$

The same two maps define an exact involution on the positive mass line. With

$$
m_P:=\sqrt{\frac{\hbar c}{G}},
\qquad
\mathcal D(m):=\frac{m_P^2}{m},
$$

one has

$$
\mathcal D^2=1,
\qquad
\ell_G(\mathcal Dm)=\lambda_C(m),
\qquad
\lambda_C(\mathcal Dm)=\ell_G(m).
\tag{S7a}
$$

Its fixed point is the Planck mass, where the two length presentations coincide. This is a duality of dimensional presentations on \(m>0\), not a dynamical duality and not a prediction that any Yang--Mills excitation has Planck mass.

The mass is an input to both conversions: increasing \(m\) enlarges its gravitational length and contracts its reduced Compton wavelength, while their product is fixed by \(\hbar,G,c\). The latter is a characteristic relativistic quantum wavelength, not a theorem imposing a universal localization bound on every interacting, composite, or unstable excitation. [[deriving-value-of-g/capacity-identities|Capacity, compactness, and gravitational strength]] applies the ratio to energetic information budgets and spherical horizon capacity, with \(r_s=2\ell_G\). Those capacity assumptions are additional to the dimensional identities here.

For the calibrated Minkowski metric \(\eta_\sigma\) specified by [[quantity-lines-and-conformal-scales|the metric and quantity-line comparison]], there is also a chain:

$$
\boxed{
(H,\mathbf P;\eta_\sigma)
\xrightarrow{\text{Casimir norm}}
M
\xrightarrow{\,G/c^2\,}
\text{gravitational length }\ell_G.}
\tag{S8}
$$

The first arrow combines clock and spatial translation generators into their Lorentz-invariant norm. Only at rest does it reduce to \(M=H/c^2\). For any positive invariant-mass lower bound \(m_*>0\) in the [[mass-as-casimir-and-realization#Quantum reversal: mass labels Poincare representation components|Poincare joint-spectrum theorem]], Lorentz covariance and the spectrum condition give \(\Delta_E\geq m_*c^2\). Equality holds when both are defined as the optimal lower thresholds of the nonvacuum joint spectrum and the positive Hamiltonian spectrum. The second arrow interprets an already obtained mass as a gravitational length. Neither arrow derives the threshold. Equations \((S2)\)--\((S7)\) reuse \(G\) and \(m\); they expose structure but cannot explain either numerical value.


The quantity-line typing belongs to [[quantity-lines-and-conformal-scales]]. Applying these conversions to Yang--Mills inside a gravitational theory additionally requires [[yang-mills-scale-and-gravity-decoupling|pure-gauge recovery and scale matching]].

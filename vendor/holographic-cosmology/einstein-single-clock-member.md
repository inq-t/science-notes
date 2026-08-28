# Einstein Single-Clock Member

When the holographic dictionary is evaluated in ordinary four-dimensional Einstein gravity with one canonical clock, it reproduces the standard leading scalar and tensor spectra and their consistency relations. This is a controlled member and normalization check; it does not show that every holographic cosmology, or any independent causal-wall theory, reduces to this member.

## Unit convention

For the derivation below set

$$
c=\hbar=1,
\qquad
M_{\mathrm P}^{-2}=8\pi G,
$$

where \(M_{\mathrm P}\) is the reduced Planck mass. Define the dimensionless de Sitter or apparent-horizon entropy number

$$
\boxed{
\mathcal S_H
:=\frac{8\pi^2M_{\mathrm P}^2}{H^2}
=\frac{\pi}{GH^2}.}
$$

With constants restored, the same dimensionless quantity is

$$
\boxed{
\mathcal S_H
=\frac{S_H}{k_B}
=\frac{\pi c^5}{\hbar G H^2}.}
$$

The symbol \(\mathcal S_H\) is deliberate: it is an entropy number, not the state-to-gravity soldering map \(\mathfrak S_\Sigma\) in [[program-core/causal-capacity-equivalence|the programme core]].

## Leading spectra

For one canonical slow-roll clock with

$$
\epsilon:=-\frac{\dot H}{H^2},
$$

the standard leading spectra are

$$
\boxed{
\Delta_\zeta^2
=\frac{H^2}{8\pi^2\epsilon M_{\mathrm P}^2}
=\frac1{\epsilon\mathcal S_H},}
$$

$$
\boxed{
\Delta_T^2
=\frac{2H^2}{\pi^2M_{\mathrm P}^2}
=\frac{16}{\mathcal S_H}.}
$$

These formulas assume the canonical Bunch--Davies single-clock member and leading semiclassical order.

## Translation into spectral coefficients

Combining these spectra with [[vendor/holographic-cosmology/scalar-and-tensor-spectra|the registered spectral convention]] gives

$$
\boxed{
c^{(0)}
=\frac{4\epsilon\mathcal S_H}{\pi^4},
\qquad
c^{(2)}
=\frac{2\mathcal S_H}{\pi^4}.}
$$

The dimensionless inverse scalar power is

$$
\frac1{\Delta_\zeta^2}
=\epsilon\mathcal S_H.
$$

Consequently,

$$
\boxed{
r=16\epsilon,
\qquad
n_t=-2\epsilon=-\frac r8}
$$

at leading order.

## Meaning of the match

The member demonstrates that the holographic response dictionary can encode the same perturbative physics as standard single-field inflation in its regime of validity. It establishes coefficient consistency among bulk response, QFT stress response, and cosmological spectra once the complete member is granted.

It does not establish that:

- the Einstein member is selected uniquely;
- the QFT response functions are known without specifying a dual theory;
- a general positive spin-zero response predicts \(r=16\epsilon\);
- the three-dimensional QFT is the ontology of the cosmological state; or
- a causal-wall BKM Hessian equals the holographic stress response.

The original recovery of standard inflationary results is given in [[library/holography-for-cosmology/inq|Holography for Cosmology]]. The controlled deformed-CFT reproduction of the scalar slow-roll spectrum to second order in its stated regime is given in [[library/on-the-power-spectrum-of-inflationary-cosmologies-dual-to-a-deformed-cft/inq|McFadden's deformed-CFT analysis]].

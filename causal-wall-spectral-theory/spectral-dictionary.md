# Spectral Dictionary

The spectral dictionary is a chain of normalization identities inside a specified domain-wall/cosmology representation. Its algebra is internally consistent, but the representation assumes a holographic dual, a state and renormalization prescription, and simultaneous analytic continuation of momentum and theory parameters; it is not a model-independent identity for an arbitrary causal wall.

Throughout this note, $\zeta$ means the target cosmological curvature perturbation $\zeta_{\mathrm{cos}}$. Decompose the scale variation as $-\delta\ln\sigma=\delta N+\zeta_{\mathrm{wall}}$ after projecting out the homogeneous mode. The proposed identification $\zeta_{\mathrm{wall}}\stackrel{?}{=}\zeta_{\mathrm{cos}}$ is the open spacetime-descent problem, not part of the dictionary.

## Fourier precision

Fix

$$
\langle\zeta_{\mathbf k}\zeta_{\mathbf k'}\rangle
=(2\pi)^3\delta^{(3)}(\mathbf k+\mathbf k')P_\zeta(k),
\qquad
\Delta_\zeta^2(k)
:=\frac{k^3}{2\pi^2}P_\zeta(k).
$$

On the physical subspace where the covariance is invertible, define

$$
\boxed{
\mathcal K_\zeta(k)
:=P_\zeta(k)^{-1}
=\frac{k^3}{2\pi^2\Delta_\zeta^2(k)}.}
$$

This is an exact definition of inverse covariance. It is also the kernel of a Gaussian probability weight. In a non-Gaussian theory it should be understood as the two-point 1PI kernel unless a Gaussian approximation is explicitly invoked.

## Three-dimensional stress response

For a homogeneous and isotropic three-dimensional Euclidean QFT, decompose the stress-tensor two-point function as

$$
\langle\!\langle T_{ij}(q)T_{kl}(-q)\rangle\!\rangle
=A(q^2)\Pi_{ijkl}+B(q^2)\pi_{ij}\pi_{kl}.
$$

Since $\delta^{ij}\pi_{ij}=2$ in three dimensions,

$$
\boxed{
\langle\!\langle T(q)T(-q)\rangle\!\rangle=4B(q^2).}
$$

This contraction is exact. It does not establish that this three-dimensional trace is the tangent generator of the Lorentzian observer-wall state family.

## Holographic domain and sign convention

The McFadden--Skenderis domain-wall/cosmology formula is conventionally written schematically as

$$
\Delta_S^2(k)
=-\frac{k^3}{16\pi^2\operatorname{Im}B_{\mathrm{cont}}(-ik)},
\qquad
\Delta_T^2(k)
=-\frac{2k^3}{\pi^2\operatorname{Im}A_{\mathrm{cont}}(-ik)}.
$$

The continuation acts not only on Euclidean momentum but also on gravitational or QFT parameters, such as the large-$N$ parameter in the perturbative examples. It also presupposes the restricted [[causal-wall-spectral-theory/sources/papers/0610253-skenderis-townsend-domain-wall-cosmology-correspondence.pdf|domain-wall/cosmology correspondence]] and the appropriate vacuum/state. These hypotheses are part of the published construction, not mere sign conventions; the spectral formula is given by [[causal-wall-spectral-theory/sources/papers/0907.5542-mcfadden-skenderis-holography-for-cosmology.pdf|McFadden and Skenderis]]. [[causal-wall-spectral-theory/sources/papers/1104.2621-harlow-stanford-operator-dictionaries-wave-functions.pdf|Harlow and Stanford]] further show why continuation of a wavefunction does not make all dS operator and expectation-value dictionaries equivalent.

To keep positivity and branch orientation explicit, define the cosmologically continued coefficients by the observable powers:

$$
\rho_B^{\mathrm{cos}}(k)
:=\frac{k^3}{16\pi^2\Delta_S^2(k)}>0,
\qquad
\rho_A^{\mathrm{cos}}(k)
:=\frac{2k^3}{\pi^2\Delta_T^2(k)}>0.
$$

In the convention above these are $-\operatorname{Im}B_{\mathrm{cont}}$ and $-\operatorname{Im}A_{\mathrm{cont}}$. Version 3 instead writes $+\operatorname{Im}B(-k^2-i0)$ and $+\operatorname{Im}A(-k^2-i0)$ after choosing a lower-lip branch. Those notations are equivalent only after the full pseudo-QFT continuation and the orientation

$$
\operatorname{Disc}F(s)
:=F(s+i0)-F(s-i0)
$$

or its opposite are registered. The master does not define that orientation, so the sign should not be inferred from `Disc` alone.

Local polynomial counterterms have zero discontinuity and therefore do not affect $\rho_A^{\mathrm{cos}}$ or $\rho_B^{\mathrm{cos}}$ in the stated analytic setting. The renormalized source/response and scheme terms are treated by [[causal-wall-spectral-theory/sources/papers/0002230-de-haro-solodukhin-skenderis-holographic-renormalization.pdf|de Haro, Solodukhin, and Skenderis]] and [[causal-wall-spectral-theory/sources/papers/0407071-papadimitriou-skenderis-holographic-rg-flow-correlators.pdf|Papadimitriou and Skenderis]]. [[information-geometric-weld|The weld note]] records the qualifications on treating zero discontinuity as a complete quotient by local contacts.

## Scalar normalization

Define the spin-zero response coefficient and scalar discernibility by

$$
\rho_B^{\mathrm{cos}}(k)
:=\frac{\pi^2}{64}c^{(0)}(k)k^3,
\qquad
\mathcal I_\zeta(k)
:=\frac{\pi^4}{4}c^{(0)}(k).
$$

Then the holographic scalar formula and the Fourier definition give

$$
\boxed{
\Delta_\zeta^2(k)
=\frac{4}{\pi^4c^{(0)}(k)},}
$$

$$
\boxed{
\mathcal K_\zeta(k)
=8\rho_B^{\mathrm{cos}}(k)
=\frac{\pi^2}{8}c^{(0)}(k)k^3
=\frac{\mathcal I_\zeta(k)}{2\pi^2}k^3,}
$$

and

$$
\boxed{
\mathcal I_\zeta(k)=\Delta_\zeta^2(k)^{-1}.}
$$

These equalities are algebraic after the holographic member has been selected. They do not show that a causal-wall relative-entropy Hessian equals $8\rho_B^{\mathrm{cos}}$; that is the independent open statement in [[information-geometric-weld]].

[[causal-wall-spectral-theory/sources/papers/1308.0331-mcfadden-power-spectrum-inflationary-cosmologies-deformed-cft.pdf|McFadden's deformed-CFT analysis]] is the closest published source for expressing the scalar spectrum through the continued stress-trace spectral density. It supplies a worked holographic member, not a theorem that every positive CWST precision has such a representation.

The coefficient $c^{(0)}$ is a convention-dependent spin-zero trace response. It is not automatically a fixed-point central charge, a count of microscopic degrees of freedom, or evidence for a rank $N\sim\sqrt{c^{(0)}}$.

## Tensor normalization

Define

$$
\rho_A^{\mathrm{cos}}(k)
:=\frac{\pi^2}{16}c^{(2)}(k)k^3.
$$

Then

$$
\boxed{
\Delta_T^2(k)=\frac{32}{\pi^4c^{(2)}(k)},
\qquad
r(k):=\frac{\Delta_T^2}{\Delta_\zeta^2}
=8\frac{c^{(0)}(k)}{c^{(2)}(k)}.}
$$

If $\Delta_T^2$ sums two tensor polarizations, the precision of one polarization is

$$
\mathcal K_\gamma(k)
=\frac{k^3}{\pi^2\Delta_T^2(k)},
\qquad
\boxed{
\frac{\mathcal K_\gamma}{\mathcal K_\zeta}=\frac2r.}
$$

Thus $c^{(2)}/c^{(0)}=8/r$ and the per-polarization precision ratio $2/r$ are different quantities.

## Numerical calibration is a target

At $k_*=0.05\,\mathrm{Mpc}^{-1}$, v3 inserts

$$
\ln(10^{10}A_s)=3.044,
\qquad
A_s=2.098903\times10^{-9}.
$$

The dictionary then gives

$$
\boxed{
\mathcal I_\zeta(k_*)=4.764393\times10^8,
\qquad
c^{(0)}(k_*)=1.956447\times10^7.}
$$

Using the published BK18 limit $r_{0.05}<0.036$ gives

$$
\boxed{
\frac{c^{(2)}}{c^{(0)}}>222.2,
\qquad
\frac{\mathcal K_\gamma}{\mathcal K_\zeta}>55.6.}
$$

The scalar tilt used by v3 is consistent with the [[causal-wall-spectral-theory/sources/papers/1807.06211-planck-2018-inflation.pdf|Planck 2018 inflation analysis]], and the tensor bound is the [[causal-wall-spectral-theory/sources/papers/2110.00483-bicep-keck-2018-primordial-gravitational-waves.pdf|BICEP/Keck 2018-season result]]. The official chains, likelihoods, spectra, and released code are indexed in [[causal-wall-spectral-theory/sources/data/entry|the local data note]]. These numbers specify what a microscopic member must calculate. Reproducing them by algebra after inserting $A_s$ and $r$ is not a prediction.

## Vocabulary

- **Covariance:** $P_\zeta$ or $\mathcal C_\zeta$.
- **Precision:** $\mathcal K_\zeta=\mathcal C_\zeta^{-1}$ on the physical subspace.
- **Discernibility:** $\mathcal I_\zeta=1/\Delta_\zeta^2$.
- **Spin-zero response:** $c^{(0)}$ in the normalization above.
- **Spin-two response:** $c^{(2)}$; it becomes a capacity-like $c_T$ only when a microscopic normalization justifies that identification.

None of these terms should be used as a synonym for the others.

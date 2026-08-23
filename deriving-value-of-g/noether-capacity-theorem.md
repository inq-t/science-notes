# The Noether--Capacity Theorem

Conservation of the dilation current fixes the entropy-normalized thermal capacity of a conformal system: in \(n\) spatial dimensions \(C/\mathcal S=n\), and therefore a genuine \(1+1\)-dimensional conformal thermal channel has \(C=\mathcal S\). Combined with an escort-state realization of the physical scale tangent, this gives a short conditional proof of the unit Ruble law. The unresolved work is to show that a dynamical causal wall actually satisfies those hypotheses.

Write dimensionless entropy as

$$
\mathcal S:=\frac{S}{k_B}.
$$

## The BKM lemma

Let \(\rho\) be a faithful density operator and

$$
K:=-\ln\rho.
$$

Its normalized replica, or escort, family is

$$
\rho_\alpha
:=\frac{\rho^\alpha}{\operatorname{Tr}\rho^\alpha}
=\frac{e^{-\alpha K}}{Z(\alpha)}.
$$

Use logarithmic modular temperature

$$
\vartheta:=-\ln\alpha.
$$

Because the family commutes with \(K\), its logarithmic score is

$$
\left.\partial_\vartheta\ln\rho_\alpha\right|_{\alpha=1}
=K-\langle K\rangle_\rho.
$$

The BKM norm of this tangent is therefore

$$
\boxed{
g^{\mathrm{BKM}}_\rho
\!\left(\partial_\vartheta\rho,
\partial_\vartheta\rho\right)
=\operatorname{Var}_\rho(K)
=:C_E(\rho).}
$$

This is an exact exponential-family identity. It is a statement about one particular tangent, not about every path through \(\rho\). The relation between modular variance, replica derivatives, and heat capacity is reviewed by [[deriving-value-of-g/sources/papers/1807.07357-de-boer-jarvela-keski-vakkuri-aspects-capacity-entanglement.pdf|de Boer, Järvelä, and Keski-Vakkuri]].

For a physical scale coordinate \(N\), decompose its tangent at the wall as

$$
v_N=\lambda v_{\vartheta}+v_\perp,
\qquad
g_{\mathrm{BKM}}(v_\perp,v_{\vartheta})=0.
$$

Then

$$
\boxed{
G^{\perp}_{NN}
=\lambda^2 C_E+\lVert v_\perp\rVert^2_{\mathrm{BKM}}.}
$$

Thus a canonical sufficient condition for \(G^{\perp}_{NN}=C_E\) is a unit, purely escort-directed scale tangent:

$$
|\lambda|=1,
\qquad
v_\perp=0.
$$

The equality of the two scalar norms does not conversely prove tangent alignment: a smaller escort component can be compensated by a nonzero orthogonal component. The wall theory must establish the same-tangent statement independently.

## The Noether lemma

Let a homogeneous relativistic thermal sector have \(n\) spatial dimensions, no chemical potential, and a conserved stress tensor. Its dilation current is

$$
D^\mu=x_\nu T^{\mu\nu}.
$$

Stress conservation gives the Ward identity

$$
\partial_\mu D^\mu=T^\mu{}_{\mu}.
$$

In a flat conformal regime with no relevant trace anomaly,

$$
T^\mu{}_{\mu}=0.
$$

For an isotropic equilibrium state this implies

$$
\epsilon=np.
$$

The thermodynamic relations

$$
s=\frac{\partial p}{\partial T},
\qquad
\epsilon=Ts-p
$$

then give

$$
T\frac{\mathrm dp}{\mathrm dT}=(n+1)p.
$$

Consequently,

$$
p=aT^{n+1},
\qquad
s=(n+1)aT^n,
\qquad
c_V=\frac{\mathrm d\epsilon}{\mathrm dT}=n s.
$$

At fixed spatial volume and with \(k_B=1\), the modular capacity of the Gibbs state is its dimensionless heat capacity,

$$
C_E=\beta^2\operatorname{Var}(H)=V c_V.
$$

Therefore

$$
\boxed{\frac{C_E}{\mathcal S}=n.}
$$

The unit value is therefore not a generic consequence of conformal invariance. It is the distinctive thermodynamic consequence of one active spatial dimension:

$$
n=1
\quad\Longrightarrow\quad
\boxed{C_E=\mathcal S.}
$$

The coefficient \(a\), or equivalently the relevant central charge and channel multiplicity, cancels from the ratio. The Ward identity fixes the ratio but not the number of channels per physical area.

For a finite circle, a curved background, or a theory away from the local thermodynamic/Cardy regime, additional scales and anomaly terms can spoil the exact relation. For interval entanglement in a \(1+1\) CFT, the equality holds for the universal leading term; regulator-dependent constants can differ. In higher-dimensional CFTs the ratio is generally theory- and scheme-dependent.

## Conditional unit-Ruble theorem

Consider a self-dual causal cut \(\Sigma_c\). Suppose:

1. the full wall state is faithful and its physical horizontal tangent is the unit escort tangent, so \(G^{\perp}_{NN}=C_E\);
2. the active horizontal sector is a homogeneous \(1+1\) conformal thermal sector to which the dilation Ward identity applies;
3. the entropy of that same regulated state is the causal-horizon entropy,

   $$
   \mathcal S_c=\eta_{\mathrm E}A_c;
   $$

4. any reduction to a binary normal channel preserves the BKM norm of the physical tangent; and
5. entropy, capacity, and area are compared in one renormalization prescription.

Then

$$
G^{\perp}_{NN}(N_c)
=C_E
=\mathcal S_c
=\eta_{\mathrm E}A_c,
$$

and hence

$$
\boxed{
\mathfrak R_c
=\frac{G^{\perp}_{NN}}{\mathcal S_c}
=1,
\qquad
\chi_{\downarrow}
=\frac{G^{\perp}_{NN}}{A_c}
=\eta_{\mathrm E}.}
$$

This is a proof of the central conjecture from explicit hypotheses. It is not yet an unconditional theorem about the proposed FLRW wall, because hypotheses 1--4 have not been obtained from its algebra.

## The algebraic symmetry behind the candidate

For a half-sided modular inclusion \(\mathcal N\subset\mathcal M\), the Borchers--Wiesbrock structure theorem, in the corrected and extended form of [[deriving-value-of-g/sources/papers/math-0412061-araki-zsido-borchers-half-sided-modular-inclusions.pdf|Araki and Zsidó]], gives a positive translation generator and the affine-group relation

$$
\Delta_{\mathcal M}^{it}U(a)\Delta_{\mathcal M}^{-it}
=U\!\left(e^{-2\pi t}a\right).
$$

This is the operator-algebraic form of “modular flow acts as dilation on a null translation.” It supplies a natural logarithmic scale, a universal \(2\pi\), and a positivity law. Under additional standardness and locality hypotheses, suitable modular inclusions can reconstruct chiral conformal nets.

The implication is not automatic. Half-sided inclusions can be singular and have trivial relative commutant; [[deriving-value-of-g/sources/papers/2111.03172-lechner-scotford-half-sided-modular-inclusions.pdf|Lechner and Scotford]] construct explicit examples. A half-sided inclusion by itself therefore does not provide a local chiral CFT, a stress tensor, a Cardy regime, or a capacity normalization.

The recent gravitational construction summarized in [[causal-wall-spectral-theory/causal-scale-interface|the causal-scale interface]] realizes horizon-cut crossed products, edge-mode area charges, and the same affine modular algebra in perturbative gravity. It gives a serious candidate for the wall's symmetry skeleton. It does not yet turn vertical localization flow into the required horizontal state deformation, and its gravitational action already contains the coefficient whose value is at issue.

## The Noether-charge route and its exact limit

The covariant phase-space identity of [[deriving-value-of-g/sources/papers/gr-qc-9403028-iyer-wald-noether-charge-dynamical-black-hole-entropy.pdf|Iyer and Wald]] identifies horizon entropy with a diffeomorphism Noether charge and relates its first variation to the Hamiltonian charge. Controlled holographic results identify a relative-entropy Hessian with gravitational canonical energy; [[deriving-value-of-g/sources/papers/1508.00897-lashkari-van-raamsdonk-canonical-energy-quantum-fisher-information.pdf|Lashkari and Van Raamsdonk]] prove this for perturbations of a CFT vacuum ball with an AdS Rindler wedge dual.

These results align the correct kinds of objects:

$$
\text{BKM quadratic form}
\longleftrightarrow
\text{canonical energy}
\longleftrightarrow
\text{gravitational Noether structure}.
$$

They do not generally equate a chosen second-order norm to the zeroth-order background entropy. In a two-derivative Einstein holographic theory, a spherical region does satisfy \(C_E=\mathcal S\) at leading semiclassical order with a common regulator. Higher-curvature duals provide counterexamples; in four boundary dimensions the ratio can become \(c/a\) rather than one.

The genuinely noncircular version of this route must keep the gravitational kinetic coefficient symbolic, compute the wall BKM form independently, prove a same-tangent BKM--canonical-energy isometry, and only then solve for the kinetic coefficient. Importing the Bekenstein--Hawking or Wald coefficient before that step checks consistency but cannot derive \(G\).

---
inq.module: "gaussian-bridge-gap-calibration"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Gaussian Bridge-Gap Calibration

For a stationary Gaussian Euclidean mode, the conditional variance left at
the middle of a slab after both boundary values are fixed has the exact
dimensionless floor

$$
\kappa_{\mathrm{br}}(\ell)=\tanh(\omega\ell).
$$

Here \(\omega\) is the mode's inverse correlation length when Euclidean time
is measured as a length. Thus the bridge residue determines the Gaussian
Euclidean decay rate exactly:

$$
\omega
=
\frac{1}{\ell}\operatorname{artanh}\kappa_{\mathrm{br}}(\ell).
$$

For a product Gaussian field the worst mode survives tensorization, so a
positive one-particle frequency edge is equivalent to a positive bridge
angle at any fixed physical half-slab. It becomes a relativistic mass edge
only after the free dispersion, spectrum condition, and Poincare
representation are supplied. This is an exact free-field calibration of a
rate-like bridge residue; interpreting that residue as factification remains
a further claim requiring an outcome-and-record construction. It is not a
proof for interacting Yang--Mills: there the unresolved theorem is a
regulator- and volume-uniform lower frame for the actual Perron-dressed
Wilson bridge.

**Status: [EXACT] for stationary scalar Gaussian modes, finite products, and
Gaussian Fock/direct-integral extensions under the stated covariance
hypotheses; [CALIBRATION] for free Euclidean fields; [INTERPRETIVE] for
factification; [OPEN] for interacting Yang--Mills and for any cosmological
selection of the dimensional yardstick.**

## One mode

Let \((X_s)_{s\in\mathbb R}\) be a centered, variance-one stationary
Gaussian Markov process with covariance

$$
\mathbb E[X_sX_t]
=
e^{-\omega|s-t|},
\qquad
\omega>0.
\tag{G1}
$$

Choose a half-slab \(\ell>0\) and put

$$
X_-:=X_{-\ell},
\qquad
Y:=X_0,
\qquad
X_+:=X_{+\ell},
\qquad
Z:=(X_-,X_+).
\tag{G2}
$$

With

$$
r:=e^{-\omega\ell},
\tag{G3}
$$

the covariance matrix, in the order \((X_-,Y,X_+)\), is

$$
\Sigma_ω(\ell)
=
\begin{pmatrix}
1&r&r^2\\
r&1&r\\
r^2&r&1
\end{pmatrix}.
\tag{G4}
$$

Gaussian regression gives

$$
\mathbb E[Y\mid Z]
=
\frac{r}{1+r^2}(X_-+X_+)
\tag{G5}
$$

and

$$
\begin{aligned}
q^2
&:=
\operatorname{Var}(\mathbb E[Y\mid Z])\\
&=
\begin{pmatrix}r&r\end{pmatrix}
\begin{pmatrix}1&r^2\\r^2&1\end{pmatrix}^{-1}
\begin{pmatrix}r\\r\end{pmatrix}\\
&=
\frac{2r^2}{1+r^2}.
\end{aligned}
\tag{G6}
$$

Therefore the residual linear variance is

$$
1-q^2
=
\frac{1-r^2}{1+r^2}
=
\tanh(\omega\ell).
\tag{G7}
$$

For a general law, linear regression would only give an upper bound on the
true conditional residual. Gaussianity is what promotes (G7) to a theorem
on the whole \(L^2\) carrier.

## Why nonlinear endpoint functions cannot do better

Let

$$
W:=q^{-1}\mathbb E[Y\mid Z].
\tag{G8}
$$

Then \(W\) is standard Gaussian, \(\operatorname{Corr}(Y,W)=q\), and the
Gaussian residual \(Y-qW\) is independent of the entire endpoint pair
\(Z\). Hence

$$
Y\longrightarrow W\longrightarrow Z
\tag{G9}
$$

is sufficient in both directions relevant to predicting functions of
\(Y\) from \(Z\): every endpoint predictor of \(Y\) factors through the
single Gaussian coordinate \(W\).

Let \(h_k\) be the normalized Hermite polynomial of degree \(k\). The
Mehler identity gives

$$
\mathbb E[h_k(Y)\mid Z]
=
q^k h_k(W),
\qquad
k\geq0.
\tag{G10}
$$

Thus the conditional transport

$$
K_\ell f:=\mathbb E[f(Y)\mid Z]
\tag{G11}
$$

has singular values \(1,q,q^2,\ldots\). Its centered norm is \(q\). This is
the Gaussian instance of the Hirschfeld--Gebelein--Renyi maximal-correlation
theorem: nonlinear functions cannot exceed the Gaussian canonical
correlation. See [[library/on-the-maximal-correlation-coefficient/inq|On the
Maximal Correlation Coefficient]].

The canonical bridge data-augmentation chain and its residue are

$$
S_\ell:=K_\ell^*K_\ell,
\qquad
B_\ell^{\mathrm{br}}:=I-S_\ell.
\tag{G12}
$$

On the \(k\)-th Hermite chaos,

$$
S_\ell h_k=q^{2k}h_k,
\qquad
B_\ell^{\mathrm{br}}h_k=(1-q^{2k})h_k.
\tag{G13}
$$

Writing \(Q:=I-\Pi_{\mathbf1}\), the smallest nonconstant eigenvalue occurs
in the first chaos. Consequently

$$
\boxed{
B_\ell^{\mathrm{br}}
\geq
\tanh(\omega\ell)Q,}
\tag{G14}
$$

and the constant is sharp.

Equivalently, the middle--boundary Friedrichs cosine is

$$
\rho_{\mathrm{br}}(\ell)
=
\sqrt{\frac{2e^{-2\omega\ell}}
{1+e^{-2\omega\ell}}},
\qquad
\kappa_{\mathrm{br}}=1-\rho_{\mathrm{br}}^2.
\tag{G15}
$$

This is the exact answer to the question "what does the operator operate
on?" It operates on middle-slice distinctions in \(L^2\) of the stationary
slice law. It subtracts the part recoverable from the two boundary slices.
Its value is not a pixel size, a particle mass, or an outcome probability;
it is a dimensionless conditional non-recoverability.

## Exact comparison with physical Euclidean transfer

Let \(P_\ell\) be the one-ended Ornstein--Uhlenbeck transfer through length
\(\ell\). It acts on the Hermite basis as

$$
P_\ell h_k=r^kh_k.
\tag{G16}
$$

The general physical solder from
[[bridge-data-augmentation-solder/inq|Bridge Data-Augmentation Solder]] is
visible mode by mode:

$$
P_\ell^2\leq S_\ell,
\qquad
0\leq B_\ell^{\mathrm{br}}\leq I-P_\ell^2.
\tag{G17}
$$

In this Gaussian model the sharper relative quasi-factorization is also
exact:

$$
\boxed{
I-P_\ell^2
\leq
(1+r^2)B_\ell^{\mathrm{br}},}
\tag{G18}
$$

with optimal constant \(1+r^2\). The first chaos saturates (G18). Thus the
endpoint-refinement information is never more than \(r^2\) times the
irreducible bridge residue. This is precisely the kind of quantitative
"no approximate two-ended recovery" estimate that is missing in the
interacting theory.

The generic one-way bridge theorem gives only

$$
\omega
\geq
-\frac{1}{2\ell}
\log(1-\kappa_{\mathrm{br}}).
\tag{G19}
$$

Gaussian structure supplies the exact inverse:

$$
\boxed{
\omega
=
\frac{1}{\ell}
\operatorname{artanh}\kappa_{\mathrm{br}}.}
\tag{G20}
$$

Equation (G20) uses the **optimal** Gaussian bridge floor. If only a
certificate \(0<\kappa_{\mathrm{cert}}\leq
\kappa_{\mathrm{br}}\) is known, monotonicity gives the lower bound

$$
\omega
\geq
\frac{1}{\ell}
\operatorname{artanh}\kappa_{\mathrm{cert}},
\tag{G20a}
$$

not an equality.

The difference matters. Equation (G19) is a universal sufficient lower
bound following from operator order. Equation (G20) is a model-specific
identity and must not be used for an interacting bridge without a theorem
identifying its functional calculus.

## A free field is the product of the mode calibrations

At finite spatial volume and ultraviolet cutoff, a free scalar Euclidean
field decomposes into finitely many independent stationary Gaussian modes.
Write the inverse-length dispersion as

$$
\Omega(p)=\sqrt{|p|^2+\mu^2},
\qquad
\mu:=\frac{Mc}{\hbar}.
\tag{G21}
$$

The normalized time covariance of the \(p\)-mode is
\(e^{-\Omega(p)|s-t|}\). Maximal correlation tensorizes by a maximum, so

$$
\begin{aligned}
\rho_{\mathrm{field}}(\ell)
&=
\sup_p
\sqrt{
\frac{2e^{-2\Omega(p)\ell}}
{1+e^{-2\Omega(p)\ell}}},\\
\kappa_{\mathrm{field}}(\ell)
&=
\inf_p\tanh(\Omega(p)\ell).
\end{aligned}
\tag{G22}
$$

Therefore, whenever \(\Omega_*\) is the bottom of the one-particle spectral
support (the essential infimum in a continuous-momentum representation),

$$
\boxed{
\kappa_{\mathrm{field}}(\ell)
=
\tanh(\Omega_*\ell).}
\tag{G23}
$$

For a massive free field, \(\Omega_*=\mu>0\). For a massless field in the
thermodynamic limit, modes with \(|p|\downarrow0\) force
\(\kappa_{\mathrm{field}}\downarrow0\). A finite box with its zero mode
removed can have a positive finite-size floor of order \(\tanh(2\pi
\ell/L)\); it disappears as \(L\to\infty\). This is why finite-regulator
strict positivity is not the mass-gap theorem.

The finite-product proof extends to a Gaussian Fock or direct-integral
carrier when conditional transport is the second quantization of the
one-particle canonical-correlation operator. Its centered norm is then the
one-particle norm, and (G23) remains valid. This extension requires the
stationary Gaussian measure or reconstructed Gaussian Hilbert carrier to
exist; the spatially constant mode of a massless scalar is a familiar
normalizability caveat, not a counterexample to the thermodynamic statement.

The full bridge Gramian should not be identified with
\(\tanh(\ell H/(\hbar c))\). They have the same first-chaos floor, but on the
\(k\)-th chaos the bridge eigenvalue is \(1-q^{2k}\), whereas the direct
functional calculus would give \(\tanh(k\omega\ell)\). The rate reconstruction
uses the sharp bottom edge, not an operator identity on every excitation.

## Mass is a rate, once the arrow is typed

If Euclidean clock duration is \(\tau=\ell/c\), define

$$
\Gamma:=c\omega.
\tag{G24}
$$

Then \(\Gamma\) has dimensions of inverse time and

$$
\boxed{
\Gamma
=
\frac{1}{\tau}
\operatorname{artanh}\kappa_{\mathrm{br}},
\qquad
\Delta_E=\hbar\Gamma,
\qquad
M=\frac{\hbar}{c^2}\Gamma.}
\tag{G25}
$$

Equivalently, with the inverse-length rate \(\omega\),

$$
\Delta_E=\hbar c\omega,
\qquad
M=\frac{\hbar}{c}\omega.
\tag{G26}
$$

This is a clean answer to the dimensional question. In the free Gaussian
calibration, mass is the clock-rate quantity \(\Gamma\) converted by
\(\hbar/c^2\), or the inverse-length quantity \(\omega\) converted by
\(\hbar/c\). The primitive dimensionless observable is the bridge angle;
the dimensional input is the physical slab duration or length.

Nothing here derives \(\hbar\), \(c\), or a preferred \(\ell\). If a deeper
causal geometry independently selects a slab \(\ell_*\) and proves a pure
number \(\kappa_*\), then (G20) supplies the rate. Choosing \(\ell_*\) from
the observed gap, or choosing \(\kappa_*\) after inspecting it, would be
circular. Importing \(G\), a Hubble rate, temperature, or a causal-grain
length is legitimate only after a carrier map proves that it is the same
slab yardstick and after pure Yang--Mills is recovered in the appropriate
decoupling limit.

## The Copernican reading

The usual free-field language starts with a Hamiltonian eigenvalue and then
computes exponential correlations. The reversed statement is equally exact:
start with the whole three-slice Gaussian relation, ask how much of a middle
distinction remains after both boundaries have been presented, and recover
the spectral rate from that residual angle.

The result gives precise content to three philosophical clues:

- **Pointing requires forgotten alternatives.** The bridge residue is the
  part of a middle distinction not representable by endpoint data. Its
  positivity is conditional ambiguity, not ontological randomness.
- **A gap is a uniform distinction theorem.** A mass gap says that no
  normalized nonvacuum direction can become arbitrarily recoverable from
  both sides of a fixed physical slab.
- **Mass is rate-like.** In the Gaussian sector, the rate at which the
  dimensionless bridge angle grows with slab thickness is exactly the
  inverse Compton scale.

This also types the unitarity claim. The endpoint conditional-expectation
projection, \(K_\ell\), and \(S_\ell=K_\ell^*K_\ell\) are contractions;
none is a Lorentzian clock automorphism, and only a named projection or
quotient with nonzero kernel should be called information-losing. Under the
full Osterwalder--Schrader hypotheses, the Euclidean theory reconstructs a
positive contractive semigroup and a unitary Lorentzian group on the
physical Hilbert carrier. Descent can therefore forget whole-level
information while the retained clock theory is unitary, but only because
these are different arrows. The phrase "the whole is nonunitary" has no
mathematical content until the whole carrier and the noninvertible arrow are
named.

[[algebra/os-descent-naturality-and-clock-no-go|The idempotent-clock no-go]]
turns this firewall into an exact theorem. An idempotent conditional
projection cannot descend to a nonidentity unitary, and the positive
operators \(S_\ell\) and \(P_\ell\) could be unitary only if they were the
identity. Their strictly subunit Hermite eigenvalues are therefore
recoverability and Euclidean attenuation, whereas the corresponding
Lorentzian clock eigenvalues are unit-modulus phases obtained from a
different functional calculus.

## Interacting target

The Gaussian calculation identifies the form an interacting theorem should
imitate without assuming Gaussianity. For the stationary Perron-dressed
Wilson path law at fixed physical half-slab \(\ell_*\), prove

$$
\boxed{
\mathbb E\!\left[
\operatorname{Var}
\bigl(f(X_{\ell_*})\mid X_0,X_{2\ell_*}\bigr)
\right]
\geq
\kappa_*\|Qf\|^2,}
\tag{G27}
$$

uniformly in volume, boundary-flux sector, and continuum regulator, with
\(\kappa_*>0\). Equivalently,

$$
\|K_{\ell_*}Q\|\leq\sqrt{1-\kappa_*}<1.
\tag{G28}
$$

The direct Gaussian inverse (G20) is then unavailable, but the already
proved physical solder still yields

$$
\Delta_E
\geq
-\frac{\hbar c}{2\ell_*}\log(1-\kappa_*).
\tag{G29}
$$

The analytical burden is now explicit: exclude *approximate* two-ended
recovery on every nonvacuum gauge-invariant direction. Excluding only exact
recovery, proving a one-slice sampler gap, or assuming an already known
transfer gap is insufficient. The complete bridge-innovation matrix and
same-carrier edge-measure solder are two noncircular routes to (G27).

## Claim boundary

- The theorem is exact for Gaussian Euclidean modes, not for interacting
  gauge fields.
- Conditional variance is a property of a law and a subalgebra. It does not
  decide whether the underlying ontology is stochastic or deterministic.
- The bridge angle is dimensionless. A mass appears only after an
  independently justified length or duration is supplied.
- A positive fixed-volume floor is not enough; the same \(\kappa_*\) must
  survive volume and regulator removal at fixed physical \(\ell_*\).
- A bridge floor supplies a Hamiltonian-gap bound only after the actual
  Euclidean transfer, vacuum carrier, and reflection-positive reconstruction
  have been identified.
- A Hamiltonian gap becomes a relativistic mass statement only after
  Poincare covariance, the spectrum condition, and the vacuum-kernel theorem
  have been reconstructed.

## Dependencies

- [[bridge-data-augmentation-solder/inq|Bridge Data-Augmentation Solder]]
- [[bridge-score-fusion-geometry/inq|Bridge-Score Fusion Geometry]]
- [[two-slice-innovation-geometry/inq|Two-Slice Innovation Geometry]]
- [[library/covariance-structure-of-the-gibbs-sampler-with-applications-to-the-comparisons-of-estimators-and-augmentation-schemes/inq|Covariance Structure of the Gibbs Sampler]]
- [[library/on-sequences-of-pairs-of-dependent-random-variables/inq|On Sequences of Pairs of Dependent Random Variables]]
- [[library/on-the-maximal-correlation-coefficient/inq|On the Maximal Correlation Coefficient]]

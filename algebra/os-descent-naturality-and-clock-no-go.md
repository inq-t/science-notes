# OS Descent Naturality and the Idempotent-Clock No-Go

A whole Euclidean law, a nonfaithful realization, a positive transfer
semigroup, and a Lorentzian unitary group have different mathematical types.
An OS-bounded translation-covariant realization intertwines the reconstructed
positive generators and hence their clock groups, even when the realization
is noninjective. If it is surjective, a local spectral band is absent exactly
when its whole spectral subspace lies in the realization kernel. By contrast,
an idempotent expectation cannot itself descend to a nontrivial unitary:
polynomial identities survive every surjective factor. This makes
“forgetting permits local unitarity” an exact compatibility diagram while
ruling out the stronger claim that forgetting becomes or causes the clock.

**Status: [EXACT] for the factor, functional-calculus, spectral-deletion,
polynomial-identity, positive-contraction, and underdetermination lemmas;
[STANDARD UNDER FULL OSTERWALDER--SCHRADER HYPOTHESES] for the clock
reconstruction; [OPEN] for a physical whole-to-local OS morphism and uniform
Yang--Mills gap estimate.**

## A law is not an operator

A joint law \(\mathsf J\) is an object in a probability category. It is
neither unitary nor nonunitary. A measure-preserving action on its path space
may have a unitary Koopman implementation on \(L^2(\mathsf J)\), but that is
an additional arrow on a derived inner-product carrier.

For \(a\in\{W,L\}\), let \(\mathscr E_{a,+}\) carry an OS-positive
semidefinite form

$$
\beta_a(F,G)
:=
\omega_a\!\left((\Theta_aF)^*G\right),
\qquad
N_a:=\operatorname{rad}\beta_a,
\tag{ON1}
$$

and let

$$
q_a:\mathscr E_{a,+}\longrightarrow
\mathcal H_a
:=
\overline{\mathscr E_{a,+}/N_a}
\tag{ON2}
$$

be the OS null quotient followed by completion. Assume the full relevant OS
hypotheses, including the continuity and covariance needed for Euclidean
translations \(\tau_\ell^a\), give

$$
C_\ell^a q_aF
=
q_a\tau_\ell^aF,
\qquad
C_\ell^a=e^{-\ell K_a},
\qquad
K_a\geq0.
\tag{ON3}
$$

Here \(K_a\) has inverse-length type. Only after a physical normalization has
been supplied may one put

$$
H_a:=\hbar cK_a,
\qquad
U_t^a:=e^{-itH_a/\hbar}=e^{-ictK_a}.
\tag{ON4}
$$

Reflection positivity by itself does not supply all of (ON3), a Poincare
representation, or a local observable net.

## OS-natural descent intertwines the reconstructed clocks

Let

$$
D:\mathscr E_{W,+}\longrightarrow\mathscr E_{L,+}
\tag{ON5}
$$

be linear. Suppose

$$
\beta_L(DF,DF)\leq M^2\beta_W(F,F)
\tag{ON6}
$$

and, on a common translation-invariant core,

$$
D\tau_\ell^W=\tau_\ell^LD
\qquad(\ell\geq0).
\tag{ON7}
$$

Equation (ON6) sends \(N_W\) into \(N_L\), so there is a unique bounded map

$$
\widehat D:\mathcal H_W\longrightarrow\mathcal H_L,
\qquad
\widehat Dq_WF=q_LDF,
\qquad
\|\widehat D\|\leq M.
\tag{ON8}
$$

Equations (ON3) and (ON7) first give the semigroup intertwiner on the dense
quotient core and then, by continuity, on the completions:

$$
\boxed{
\widehat D C_\ell^W=C_\ell^L\widehat D.}
\tag{ON9}
$$

For every \(\lambda>0\), the Laplace transform of (ON9) gives

$$
\begin{aligned}
\widehat D(K_W+\lambda)^{-1}
&=
\int_0^\infty e^{-\lambda\ell}
\widehat D e^{-\ell K_W}\,\mathrm d\ell\\
&=
(K_L+\lambda)^{-1}\widehat D.
\end{aligned}
\tag{ON10}
$$

Resolvent intertwining for the two self-adjoint generators yields their
spectral-projection intertwining and hence bounded Borel functional calculus:

$$
\widehat D\,E_{K_W}(B)
=
E_{K_L}(B)\widehat D
\qquad
\text{for every Borel }B\subseteq[0,\infty).
\tag{ON11}
$$

Applying (ON11) to the unit-modulus clock function gives

$$
\boxed{
\widehat D U_t^W=U_t^L\widehat D.}
\tag{ON12}
$$

No injectivity of \(\widehat D\) is required. If it is surjective and
noninjective, (ON12) is an exact quotient intertwiner between reconstructed
clock representations. The theorem proves covariance and coexistence; it
does not say that \(D\) creates either generator.

Surjectivity has a sharp spectral consequence. For every Borel set
\(B\subseteq[0,\infty)\), (ON11) gives

$$
\boxed{
E_{K_L}(B)=0
\quad\Longleftrightarrow\quad
\widehat D E_{K_W}(B)=0
\quad\Longleftrightarrow\quad
\operatorname{Ran}E_{K_W}(B)\subseteq\ker\widehat D.}
\tag{ON12a}
$$

Indeed, the forward implication is immediate from (ON11), while the reverse
implication gives \(E_{K_L}(B)\widehat D=0\) and then uses surjectivity. In
particular,

$$
\sigma(K_L)\subseteq\sigma(K_W).
\tag{ON12b}
$$

Taking \(B=(0,\delta)\) gives an exact spectral-deletion formulation of the
Copernican proposal: the local carrier has no spectral subspace in that band
exactly when
every whole-carrier spectral vector in the band is invisible to the
realization. A
gapless whole generator may therefore have a gapped quotient presentation.
This still does not select \(\delta\), prove vacuum uniqueness, or show that
the reconstructed local generator is Yang--Mills. Used backward, (ON12a) is
only a reformulation of a known local gap. A noncircular explanation must
construct \(\ker\widehat D\) geometrically and prove the whole-band inclusion
without assuming the spectral conclusion it is meant to explain.

There is a concrete Hilbert-semigroup witness of the spectral conclusion. Let
\(\kappa>0\) have inverse-length type and put

$$
\begin{aligned}
\mathcal H_W
&=
\mathbb C\Omega\oplus\ell^2(\mathbb N)\oplus\mathbb Ce,\\
K_W
&=
0\oplus\operatorname{diag}
(\kappa,\kappa/2,\kappa/3,\ldots)\oplus\kappa,\\
\mathcal H_L
&=
\mathbb C\Omega\oplus\mathbb Ce,
\qquad
K_L=0\oplus\kappa,
\end{aligned}
\tag{ON12c}
$$

and let \(\widehat D(\alpha,x,\beta)=(\alpha,\beta)\). Then

$$
\widehat D e^{-\ell K_W}
=
e^{-\ell K_L}\widehat D
\qquad(\ell\geq0).
\tag{ON12d}
$$

The whole generator has positive spectrum accumulating at zero, while the
local generator has the exact gap \(\kappa\); every soft basis vector lies in
\(\ker\widehat D\). This proves that spectral deletion is mathematically
possible. It does not exhibit the pre-OS spaces, reflection, Euclidean law,
or physical realization required by (ON5)--(ON8), and it does not make this
deliberately assembled quotient a physical explanation.

## Polynomial identities survive a surjective factor

Let \(X,Y\) be complex vector spaces, let \(r:X\twoheadrightarrow Y\) be
surjective, and suppose

$$
rA=Br
\tag{ON13}
$$

for endomorphisms \(A\) and \(B\). For every polynomial \(p\),

$$
rp(A)=p(B)r.
\tag{ON14}
$$

Thus

$$
p(A)=0
\quad\Longrightarrow\quad
p(B)=0,
\tag{ON15}
$$

because \(r\) is onto. In particular,

$$
A^2=A
\quad\Longrightarrow\quad
B^2=B.
\tag{ON16}
$$

If \(B\) is also invertible, multiplying \(B^2=B\) by \(B^{-1}\) gives

$$
\boxed{B=I_Y.}
\tag{ON17}
$$

Consequently, in a commuting square

$$
\begin{array}{ccc}
X&\xrightarrow{\ E\ }&X\\
\downarrow r&&\downarrow r\\
Y&\xrightarrow{\ V\ }&Y ,
\end{array}
\qquad
rE=Vr,
\tag{ON18}
$$

an idempotent conditional-expectation projection \(E\) and a unitary \(V\)
force \(V=I_Y\). The expectation may become the identity after all directions
outside its range have been quotiented away. It cannot become a nontrivial
clock transformation.

The permitted diagram uses a **separate** action:

$$
r\alpha_t=U_t r.
\tag{ON19}
$$

Here kernel invariance makes the action descend, while an invariant positive
state and continuity make its quotient implementation unitary. This is the
mechanism proved in
[[algebra/quotient-unitarity-and-kernel-stabilization|Quotient Unitarity and
Kernel Stabilization]]. Equation (ON17) proves why \(E\) cannot be substituted
for \(\alpha_t\).

## A positive contraction is not its clock continuation

Let \(0\leq A\leq I\) on a Hilbert space. If \(A\) is unitary, then
\(A^*A=A^2=I\); positivity and spectral calculus force

$$
\boxed{A=I.}
\tag{ON20}
$$

Two immediate specializations fix the operator types in the mass-gap
programme:

$$
S_n=K_n^*K_n\text{ unitary}
\quad\Longrightarrow\quad
S_n=I
\quad\Longrightarrow\quad
B_n^{\mathrm{br}}=I-S_n=0,
\tag{ON21}
$$

and, for \(\ell>0\),

$$
C_\ell=e^{-\ell K}\text{ unitary}
\quad\Longrightarrow\quad
C_\ell=I
\quad\Longrightarrow\quad
K=0.
\tag{ON22}
$$

Thus the positive bridge recovery operator and Euclidean transfer cannot be
the nontrivial Lorentzian clock. The clock is the distinct functional
calculus \(e^{-ictK}\) after \(K\) has been physically reconstructed. In the
Gaussian calibration these three operators have, respectively, strictly
subunit recovery eigenvalues, strictly subunit Euclidean attenuation
eigenvalues, and unit-modulus clock phases on every nonvacuum Hermite mode.

## Nonfaithful formation does not select the local spectrum

Let \(\mathcal N\neq0\) and define

$$
r:\mathcal H\oplus\mathcal N\twoheadrightarrow\mathcal H,
\qquad
r(x,n)=x.
\tag{ON23}
$$

For arbitrary nonnegative self-adjoint \(K\) on \(\mathcal H\) and \(R\) on
\(\mathcal N\),

$$
\widetilde C_\ell=e^{-\ell K}\oplus e^{-\ell R},
\qquad
C_\ell=e^{-\ell K}
\tag{ON24}
$$

obey

$$
r\widetilde C_\ell=C_\ell r.
\tag{ON25}
$$

The same fixed noninjective quotient is therefore compatible with arbitrary
local generators and arbitrary gap values. Neither nonfaithfulness nor the
dimension of the forgotten fibre selects \(K\). A Yang--Mills explanation
still needs an independently normalized whole action, the OS-natural map,
and a uniform lower edge on the complete physical vacuum complement.

## Local covariance does not preserve each fixed local algebra

After full OS/Wightman reconstruction, the unitary Poincare action belongs to
the global physical Hilbert carrier. Covariance of a local net means

$$
\boxed{
U(a,\Lambda)\mathcal A(O)U(a,\Lambda)^*
=
\mathcal A(\Lambda O+a).}
\tag{ON26}
$$

A time translation generally maps \(\mathcal A(O)\) to a different regional
algebra rather than acting as an automorphism of that one fixed algebra. It
is an automorphism of the quasilocal algebra, and the implementing unitary
need not belong to any local algebra.

The algebraic lesson is therefore stricter than “the whole is nonunitary so
that the local theory is unitary.” The whole law is an object; formation is
a possibly noninvertible arrow; Euclidean transfer is a positive contraction;
and Lorentzian clock evolution is a unitary functional calculus on a
reconstructed carrier. Their compatibility is expressed by (ON9), (ON12),
and (ON19), while (ON17) rules out identifying them.

## Dependencies

- [[conservation-of-causal-charge/unitarity-and-ontological-time|Why Unitarity Is Not the Wall Symmetry]]
- [[algebra/quotient-unitarity-and-kernel-stabilization|Quotient Unitarity and Kernel Stabilization]]
- [[contemporary-puzzles/yang-mills-mass-gap/past-future-angle-and-the-transfer-gap|Past--Future Angle and the Transfer Gap]]
- [[bridge-data-augmentation-solder/inq|Bridge Data-Augmentation Solder]]
- [[gaussian-bridge-gap-calibration/inq|Gaussian Bridge-Gap Calibration]]

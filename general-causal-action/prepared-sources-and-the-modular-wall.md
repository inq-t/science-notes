# Prepared Sources and the Modular Wall

The finite preparation programme now returns a complete physical source algebra and an interacting clock, but their two immediate algebraic completions do not supply a modular wall. The equal-time source algebra is commutative and has trivial modular flow. Adjoining even one positive heat step generates the full operator algebra, on which the pure vacuum is not separating. A modular reconstruction therefore needs proper regional operator algebras and their relative positions, constructed from the same preparation rather than inferred from source completeness.

## The returned source algebra has a trivial modular operator

Fix one nontrivial finite graph construction of [[local-incidence-preparations-and-the-gauge-transfer|local incidence preparation]] or [[conditional-preparation-sewing/conditional-access-families-and-the-returned-clock|conditional access]]. Write its entire gauge-invariant configuration space as the compact quotient \(Q=X/\mathcal G\), with quotient Haar measure \(\mu\). Its positive normalized ground vector \(\psi_0\) is invariant and descends to \(Q\). The ground-state transform gives
\[
\mathcal H=L^2(Q,\nu),\qquad d\nu=\psi_0^2d\mu,\qquad
\Omega=1,\qquad L=\psi_0^{-1}(H-E_0)\psi_0\ge0.
\tag{MW1}
\]
Assume \(\dim\mathcal H>1\); a fully gauged tree with only constant physical functions is outside the nontrivial assertion. No finite-dimensional Hilbert-space assumption is made. Finite link graphs here generally have infinite-dimensional \(L^2\) carriers.

[[prepared-readout-algebra-and-physical-source-completeness|Prepared readout completeness]] proves that the represented physical multiplication sources have von Neumann closure
\[
\mathcal A_0=L^\infty(Q,\nu)
\quad\text{acting by multiplication on }\mathcal H.
\tag{MW2}
\]
It is maximal abelian. The vector \(1\) is cyclic because bounded functions are dense in \(L^2\), and separating because \(f1=0\) implies \(f=0\) almost everywhere. Its Tomita operator initially sends \(f\Omega\) to \(\overline f\Omega\), and closes to complex conjugation. Therefore
\[
\boxed{\Delta_{\mathcal A_0,\Omega}=I,\qquad
\sigma_t^\Omega\big|_{\mathcal A_0}=\operatorname{id}.}
\tag{MW3}
\]
This faithful state can have nonzero covariance, nonzero information response and the nontrivial external clock \(L\). None is its modular flow. The general distinction between a commutative readout and its excitation algebra is developed in [[algebra/characters-factorization-and-the-modular-carrier|characters and the modular carrier]]; (MW3) applies it to the newly constructed physical sources without replacing their nonmultiplicative state by a character.

## One heat step and the full source algebra generate every operator

For any fixed \(t>0\), put \(T_t=e^{-tL}\). On the compact covering product, the uniformly elliptic real Hamiltonian with bounded smooth potential has a strictly positive smooth heat kernel. Ground-state transformation preserves strict positivity. Gauge averaging its second argument gives a bounded strictly positive measurable kernel \(p_t(q,q')\) on the quotient, with respect to \(\nu\). The heat operator on the full invariant carrier is thus
\[
(T_tf)(q)=\int_Qp_t(q,q')f(q')d\nu(q'),\qquad p_t(q,q')>0.
\tag{MW4}
\]
This uses the finite constructed heat operator, not a claim of instantaneous Lorentzian influence between spacetime regions.

Explicitly, if \(K_t(x,y)\) is the covering Hamiltonian kernel relative to covering Haar, then
\[
p_t([x],[y])=\frac{e^{tE_0}}{\psi_0(x)\psi_0(y)}
\int_{\mathcal G}K_t(x,h\cdot y)\,dh.
\tag{MW4a}
\]
The measure in (MW4) is \(\nu=\psi_0^2\mu\), accounting for both ground-state factors. Simultaneous gauge covariance of \(K_t\) makes (MW4a) invariant in both representatives. Positivity and boundedness follow from compactness and \(\psi_0>0\).

Let \(B\) commute with \(\mathcal A_0\) and \(T_t\). Maximal abelianness gives \(B=M_b\) for some bounded measurable \(b\). The commutator has the Hilbert–Schmidt kernel
\[
[M_b,T_t](q,q')=[b(q)-b(q')]p_t(q,q').
\tag{MW5}
\]
Vanishing of this kernel and strict positivity give \(b(q)=b(q')\) for \(\nu\times\nu\)-almost every pair, hence \(b\) is constant. The double-commutant theorem proves
\[
\boxed{W^*(\mathcal A_0,T_t)=B(\mathcal H).}
\tag{MW6}
\]
The result is not peculiar to imaginary time. The function \(\lambda\mapsto e^{-t\lambda}\) is injective on the nonnegative spectrum of \(L\), so bounded Borel functional calculus recovers all \(e^{isL}\) from \(T_t\); its possible spectral value zero has zero spectral projection. Conversely the real-time spectral algebra contains \(T_t\). Adjoining the complete real-time clock gives the same algebra in (MW6).

On \(B(\mathcal H)\), the vector state \(\Omega\) is pure and cyclic but not separating:
\[
(I-|\Omega\rangle\langle\Omega|)\Omega=0,
\qquad I-|\Omega\rangle\langle\Omega|\ne0.
\tag{MW7}
\]
There is no faithful-vector Tomita construction on this global algebra with that vector. Moving to a faithful mixed state on another standard representation would change the declared state and carrier. [[algebra/faithful-stationary-states-and-the-positive-clock|The faithful-state clock theorem]] owns the broader obstruction to a nontrivial positive stationary clock preserving an entire algebra for which the same vacuum is cyclic and separating. Local relativistic time instead moves the regional algebras.

## Regional modular position is a further joint return

These two results locate a missing construction, rather than excluding modular methods. Seek from the same comparison and access law proper noncommutative algebras \(\mathcal M_W\subset B(\mathcal H)\), indexed by constructed wedge-like access contexts, with one vacuum cyclic and separating on each. Their inclusions, commutants and modular operators must satisfy a specified reconstruction theorem. Taking the full multiplication algebra gives (MW3); adjoining the unrestricted whole clock gives (MW6). Merely choosing a smaller coordinate sigma algebra also does not solve the problem: its orbit on \(\Omega\) closes to \(L^2\) of that sigma algebra and is not cyclic on the whole carrier unless the readout already retains everything.

A possible construction is to generate each regional algebra from prepared sources and only those time transports admitted by its access context. The context law must supply those transports and prove the resulting algebra is proper, with a cyclic and separating vacuum. Bounded Euclidean-time preparation, a conditional expectation, and a spacelike commuting algebra are different operations. Existing [[wall-construction-interface/half-sided-modular-tunnel|half-sided modular transport]] is an exact downstream template once its compatible algebra and state data exist; it does not provide those data here.

The immediate target can be stated without calling every label spacetime:
\[
\boxed{
(\text{prepared sources},\text{access comparisons},\text{returned state})
\longrightarrow
\{(\mathcal M_W,\Omega),\text{relative modular positions}\}
\longrightarrow U(a,\Lambda).}
\tag{MW8}
\]
The first arrow is open. The second requires the actual hypotheses of a modular reconstruction theorem, such as the finite algebra constellation in [[library/modular-theory-and-the-reconstruction-of-four-dimensional-quantum-field-theories/inq|Kähler–Wiesbrock]], including its mutual modular positions. A generic poset with a faithful state does not satisfy them by definition.

The reconstructed positive generator of a half-sided inclusion is a translation obtained from two modular logarithms; it is not the modular logarithm of one faithful state. Its dilation covariance forces a nontrivial spectrum down to zero. [[mass-scale-calibration/joint-causal-generators-and-the-mass-casimir|Joint causal generators]] already proves the correct route: compatible opposite causal translations, a completed Poincare representation, and a separate full-carrier Casimir bound. No modular non-geometricity or global/local purity slogan supplies that bound.

The [[physical-response-coercivity/conditional-vacuum-rigidity-and-the-physical-gap|complete-source susceptibility]] estimates a candidate returned clock on an actual vacuum complement. It can supply a physical energy-gap certificate if that clock is identified with the reconstructed translation Hamiltonian in the required limit. The modular constellation and the uniform source-response bound are thus complementary returns of one proposed law. Their equality of carrier, state and clock is a construction to prove, not a choice of names.

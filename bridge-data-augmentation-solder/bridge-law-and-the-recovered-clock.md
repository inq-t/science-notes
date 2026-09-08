# Bridge Laws and the Recovered Clock

A compatible family of strictly positive two-ended conditional laws on a finite carrier determines one homogeneous Markov transition and its stationary law. Endpoint-reversal symmetry is exactly detailed balance; an additional Hilbert-positivity condition then permits a positive Hamiltonian logarithm. This reverses the usual input order, but does not yet reduce the family of possible dynamics: arbitrary one-endpoint data parametrize every positive stochastic matrix. The missing foundational input is a law selecting those data, not another freely chosen clock.

**Status: [EXACT FINITE RECONSTRUCTION].** The proofs below are elementary inverse-kernel arguments in the setting of reciprocal processes, not a claimed new Yang–Mills construction. [[library/markov-processes-with-identical-bridges/inq|Fitzsimmons]] proves related continuous-time rigidity under different hypotheses, using whole pinned path laws rather than one sampled midpoint.

## Conditional composition determines a normalized transition

Fix a finite set \(X\), \(|X|=N\ge2\), and counting measure. All matrix entries in this section are strictly positive. A transfer matrix \(T\), acting on functions by rows, has middle conditional law

$$
b_T(y\mid x,z)=\frac{T_{xy}T_{yz}}{(T^2)_{xz}}.
\tag{IB1}
$$

This \(T\) is not the conditional-expectation operator \(K_n\) in [[inq|the data-augmentation construction]]. The proposed primitive here is the entire array \(b(y\mid x,z)\), with positive normalized rows indexed by endpoint pairs.

Two transfers give the same array exactly when

$$
b_{T'}=b_T
\quad\Longleftrightarrow\quad
T'=aD^{-1}TD,\qquad a>0,\quad D=\operatorname{diag}(d_x)>0.
\tag{IB2}
$$

**Proof.** Set \(R_{xy}=T'_{xy}/T_{xy}\). Equality of conditionals says that \(R_{xy}R_{yz}\) is independent of \(y\). Comparing middle states \(x,z\) shows \(R_{xx}=R_{zz}=a\). Fix \(o\). Comparing middle states \(o,x\) gives

$$
R_{xz}=\frac{R_{xo}R_{oz}}a,\qquad R_{ox}R_{xo}=a^2.
$$

With \(d_x=R_{ox}/a\), this is \(R_{xz}=a\,d_z/d_x\). Conversely, these factors cancel from (IB1).

There is an explicit existence test, not just uniqueness conditional on a hidden transfer. Choose \(o\in X\), and form

$$
C_{xy}:=\frac{b(y\mid x,o)}{b(o\mid x,o)},\qquad C_{xo}=1.
\tag{IB3}
$$

The supplied full array is compatible with one homogeneous positive transfer if and only if

$$
\boxed{
\frac{b(y\mid x,z)}{b(o\mid x,z)}
=\frac{C_{xy}C_{yz}}{C_{oz}}
}
\quad\text{for every }x,y,z.
\tag{IB4}
$$

Indeed, the right side is the ratio of the corresponding \(b_C\) entries. Positive normalization turns equality of these ratios into \(b_C=b\). Necessity follows either from (IB2), or directly from
\(C=T_{oo}^{-1}\operatorname{diag}(T_{xo})^{-1}T\operatorname{diag}(T_{xo})\).

Let \(Ch=\rho h\), \(h>0\), be its Perron pair. Then

$$
\boxed{P_{xy}=\frac{C_{xy}h_y}{\rho h_x}}
\tag{IB5}
$$

is stochastic and has the given bridges. It is the unique positive stochastic matrix with them. Under (IB2), \(h\) changes to \(D^{-1}h\) and \(\rho\) to \(a\rho\); these changes cancel in (IB5). For an already stochastic matrix its Perron normalization is itself.

If \(l^TC=\rho l^T\), with \(l^Th=1\), then

$$
\nu_x=l_xh_x,\qquad
\nu P=\nu,\qquad
J_{xz}=\nu_x(P^2)_{xz}.
\tag{IB6}
$$

Thus the **homogeneous stationary Markov realization** fixes the invariant law, endpoint-pair law, and \(L^2(\nu)\) norm together. An arbitrary preparation or endpoint mixture is not fixed. Such mixtures preserve conditional bridges but generally cease to be homogeneous Markov laws; [[library/reciprocal-processes-a-measure-theoretical-point-of-view/inq|the reciprocal-process survey]] explains the broader distinction.

The positive diagonal freedom in (IB2) is a presentation equivalence, not a Yang–Mills gauge group. If \(A_{xy}=-\log T_{xy}\), then

$$
A'_{xy}=A_{xy}-\log a+\log d_x-\log d_y.
\tag{IB7}
$$

Summing over a path leaves only an endpoint term and a constant per step. This is an exact coboundary law for history weights, not a stationary-action principle or the operator logarithm of \(T\).

## Endpoint symmetry specifies the reversible subclass

Within the compatible class of (IB4),

$$
\boxed{
b(y\mid x,z)=b(y\mid z,x)
\quad\Longleftrightarrow\quad
\nu_xP_{xy}=\nu_yP_{yx}.
}
\tag{IB8}
$$

To prove it, reverse the stationary transition:
\(P^{\rm rev}_{xy}=\nu_yP_{yx}/\nu_x\). Direct cancellation gives
\(b_{P^{\rm rev}}(y\mid x,z)=b_P(y\mid z,x)\).
Endpoint symmetry and stochastic uniqueness imply \(P^{\rm rev}=P\); the converse follows from the same identity.

Equivalently, with \(w_x=C_{ox}\), check
\(w_xC_{xy}=w_yC_{yx}\). Then

$$
T_{\rm sym}
=\operatorname{diag}(\sqrt w)\,C\,\operatorname{diag}(1/\sqrt w)
\tag{IB9}
$$

is symmetric. Its normalized Perron vector is
\(\psi_x=\sqrt{w_x}h_x/\sqrt{\sum_yw_yh_y^2}\), so \(\nu_x=\psi_x^2\).

The condition is a geometric symmetry of the full conditional specification. It is not a derivation of symmetry from unrestricted asymmetric data, and endpoint symmetry without (IB4) need not admit any homogeneous realization.

## Diagonal contexts and Hellinger completion

The symmetric subclass admits a smaller presentation. Write

$$
D_{xy}:=b_T(y\mid x,x),\qquad
z_x=(T^2)_{xx}.
$$

For symmetric entry-positive \(T\), \(z_xD_{xy}=T_{xy}^2\). Hence \(D\) is reversible with stationary law \(\omega_x=z_x/\sum z\).
Conversely, every strictly positive reversible stochastic \(D\) determines the unique ray of symmetric entry-positive transfers

$$
B_{xy}=\sqrt{\omega_xD_{xy}},\qquad T=cB,\quad c>0.
\tag{IB10}
$$

Detailed balance makes \(B\) symmetric, and \((B^2)_{xx}=\omega_x\), proving the inverse. The full bridge family is then forced:

$$
\boxed{
b(y\mid x,z)=
\frac{\sqrt{D_{xy}D_{zy}}}
{\sum_r\sqrt{D_{xr}D_{zr}}}.
}
\tag{IB11}
$$

The denominator is the Hellinger affinity of the two diagonal-context distributions. The construction uses their normalized geometric mean. Independently supplied off-diagonal contexts must satisfy (IB11); reversibility of \(D\) alone does not validate them.

For a general nonsymmetric positive transfer, diagonal bridges also satisfy
\(z_xD_{xy}=T_{xy}T_{yx}\). They recover the geometric symmetrization \(\sqrt{T_{xy}T_{yx}}\), not directed cycle currents. Thus diagonal data alone can forget precisely the asymmetry that a foundational programme intends to retain.

Also, \(\omega\), the invariant law of the diagonal bridge \(D\), generally differs from the clock vacuum law \(\nu=\psi^2\). They are different outputs of different operators.

## Positive transfer, Hamiltonian, and observable algebra

Entry positivity is not Hilbert positivity. Impose, and verify, the additional condition \(T_{\rm sym}\succ0\) on the complete finite carrier. With Perron value \(\rho\), define

$$
\widehat T=T_{\rm sym}/\rho,\qquad
H=-\log\widehat T,\qquad
U_t=e^{-itH}.
\tag{IB12}
$$

Strict Perron dominance and positive definiteness give
\(H\ge0\), \(H\psi=0\), and a unique vacuum. The transfer is unitarily equivalent to \(P\) on \(L^2(\nu)\). Scalar normalization cancels; the spectral floor was not separately prescribed. This is nevertheless a finite-system conclusion, not a uniform mass bound.

The counting carrier supplies diagonal projections \(E_x=|x\rangle\langle x|\). Since
\(E_x\widehat T E_y=\widehat T_{xy}|x\rangle\langle y|\) and every entry is nonzero, these projections and \(\widehat T\) generate \(B(\mathbb C^X)\). The same \(U_t\) acts on this algebra, with invariant vector state \(\psi\). This finite realization fits [[directed-analytic-realization/preparation-overlaps-and-the-transition-algebra|the transition-algebra construction]]; it does not select spatial regions, commuting local algebras, or dimension \(3+1\).

Zero eigenvalues do not admit a finite logarithm on the full carrier. Removing them silently changes the realization. A pure vacuum on \(B(\mathbb C^X)\) is also not faithful for \(N>1\); no contradiction with [[algebra/faithful-stationary-states-and-the-positive-clock|the faithful-stationary-state obstruction]] is implied.

Two additional failures prevent overreading positivity:

- Even a reversible, Hilbert-positive diagonal bridge can reconstruct an indefinite transfer. Let
  \[
  B_0=\begin{pmatrix}10&8&8\\8&10&1\\8&1&10\end{pmatrix},
  \quad F=B_0\circ B_0,\quad
  D=\operatorname{diag}(228,165,165)^{-1}F.
  \]
  The leading principal minors of \(F\) are \(100,5904,188892>0\); thus \(D\) is Hilbert-positive on its stationary \(L^2\) space. But \(\det B_0=-162\), so (IB10) reconstructs an indefinite transfer. Entrywise square roots do not preserve operator positivity.
- A positive Hamiltonian logarithm need not give a continuous **Markov** interpolation in the configuration algebra. For
  \[
  P=\frac1{60}\begin{pmatrix}43&1&16\\1&43&16\\16&16&28\end{pmatrix},
  \quad \operatorname{spec}(P)=\{1,7/10,1/5\},
  \]
  one has
  \[
  (\log P)_{12}=\tfrac16\log(1/5)-\tfrac12\log(7/10)<0.
  \]
  Therefore \(P^s_{12}<0\) for sufficiently small positive \(s\). Reversible continuous Markov embeddability requires nonnegative off-diagonal entries of \(\log P\), or a compatible all-time positive semigroup. It does not follow from (IB12).

## What the conditional data cannot choose

**Support.** Strict positivity cannot be replaced by irreducibility or even \(P^2>0\). On the five-cycle, take stay, clockwise, and anticlockwise probabilities \(r,p,q>0\), with \(p\ne q\). Swapping \(p,q\) preserves every two-step bridge: displacement zero has weights \(r^2,pq,pq\); displacement one has two equal path weights; displacement two has a unique midpoint. Yet the transitions differ, and a five-step oriented circuit distinguishes \(p^5\) from \(q^5\). Sparse presentations require longer-path information.

**Duration and refinement.** A bridge sampled at block width \(n\) reconstructs \(P^n\), not a physical duration. In the Hilbert-positive subclass and with known \(n\), the unique positive root recovers \(P\), while \(H_n=nH_1\). Without that subclass, even roots need not be unique: the stochastic matrices with diagonal entries \(1/4\) and \(3/4\), respectively, and complementary off-diagonal entries have the same square. Assigning a duration \(\tau\) replaces (IB12) by \(H/\tau\); no seconds or mass unit follows from bridge normalization.

**The gap.** For \(T_\epsilon=\left(\begin{smallmatrix}1&\epsilon\\\epsilon&1\end{smallmatrix}\right)\), \(0<\epsilon<1\), all the positive-clock conditions hold, but
\[
\Delta_\epsilon=\log\frac{1+\epsilon}{1-\epsilon}\longrightarrow0.
\]
Thus compatibility, full support, and Hilbert positivity alone give no uniform floor. On continuous carriers even diagonal endpoint data require regular versions or a diagonal limit; almost-everywhere conditional laws do not determine values on a null diagonal.

**Explanatory choice.** Every positive normalized one-anchor slice \(b(\cdot\mid x,o)\) already yields a \(C\) whose bridge agrees on that slice. It has \(N(N-1)\) free coordinates, exactly as a positive stochastic \(P\). The inverse is a bijective reparameterization of that entire class. It prevents independently changing \(P,\nu,J\) while holding a compatible full \(b\) fixed, but proves no parameter economy relative to ordinary finite Markov theory.

The construction does not equate \(P\) with the auxiliary operator \(S_n=K_n^*K_n\). Once \(\nu,J\) have been reconstructed, that auxiliary operator can also be calculated, but it is a different output. Nor does one scalar bridge floor determine the full conditional family.

The stronger [[general-causal-action/directed-realization-and-foundational-restart|foundational milestone]] therefore remains open: derive or restrict the conditional law through an upstream composition or realization principle, and carry that restriction through spatial refinement with the required Yang–Mills ultraviolet return. A supplied full bridge family is not less information merely because it is written before the clock.

[[receipts/bridge_kernel_reconstruction_receipt.py|The inverse receipt]] checks generic kernels, symmetric reconstructions, incompatible conditional specifications, and the support and positivity failures. It also inverts the existing interacting finite Wilson rectangle and cube examples on their complete 4- and 32-state gauge carriers; their supplied dynamics are withheld from the inverse, then used as an independent numerical comparison. The blocked logarithm check reports its conditioning explicitly: the strongest cube case has a transfer eigenvalue near \(10^{-13}\), so its logarithm is not recovered to machine precision. [[receipts/bridge-kernel-reconstruction-receipt-output.txt|The saved output]] is a finite implementation check, not a proof of a continuum inverse, a generated scale, or a Yang–Mills return.

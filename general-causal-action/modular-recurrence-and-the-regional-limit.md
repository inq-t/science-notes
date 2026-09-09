# Modular Recurrence and the Regional Limit

A faithful regional density can supply nontrivial modular dynamics, but its type-I factor modular group is strongly recurrent. Such a group cannot dilate a nonzero positive translation generator. Consequently a proper half-sided modular inclusion with a common cyclic and separating vector cannot occur in this finite-preparation standard form. The constructive task is to transport regional preparations into a limit that loses this recurrence while retaining the source algebra and the physical clock. A bounded resolvent identity gives an exact test of the required failure of uniform approximation.

## Recurrence excludes an affine translation

Let \(V_t\) be a strongly continuous unitary group on a Hilbert space. Call it strongly recurrent here when there is a sequence
\[
t_n\longrightarrow+\infty,\qquad V_{t_n}\longrightarrow I
\quad\text{strongly}.
\tag{MR1}
\]
This is a condition on the common group, not merely separate return times for separate vectors.

**Recurrence theorem.** If \(P\ge0\) is self-adjoint and, for some \(c>0\),
\[
V_tPV_t^*=e^{-ct}P\qquad(t\in\mathbb R),
\tag{MR2}
\]
then (MR1) implies \(P=0\). Equality in (MR2) includes equality of self-adjoint operators and their transported domains.

The proof needs only bounded functional calculus. Put
\[
Q=(I+P)^{-1},\qquad Q_t=(I+e^{-ct}P)^{-1}.
\]
Then
\[
V_tQV_t^*=Q_t,\qquad Q_t\longrightarrow I
\quad(t\longrightarrow+\infty)
\tag{MR3}
\]
strongly, by the spectral theorem and bounded convergence. Unitary strong convergence to \(I\) also gives strong convergence of the adjoints. Thus the left side of (MR3), evaluated at \(t_n\), converges strongly to \(Q\), while its right side converges to \(I\). Hence \(Q=I\) and \(P=0\). No subtraction of unbounded modular logarithms is used in this argument.

A related point-spectrum test is useful even without recurrence. If (MR2) holds and \(V_t\xi=e^{it\omega}\xi\), the spectral measure of \(P\) in \(\xi\) is invariant under every positive dilation. The intervals \([e^{ck},e^{c(k+1)})\), \(k\in\mathbb Z\), are disjoint and have the same measure. Finiteness of the measure makes all their measures zero. Therefore
\[
\mathcal H_{\mathrm{pp}}(V)\subseteq\ker P,
\tag{MR4}
\]
where the left side is the closed span of the generator's eigenvectors. A nonzero affine translation must live outside that modular point-spectrum subspace.

## Faithful density-matrix preparation is recurrent

Let \(\mathcal K\) be separable and let \(D\) be a faithful positive trace-class operator with \(\operatorname{Tr}D=1\). In the Hilbert--Schmidt standard form of \(B(\mathcal K)\), the cyclic and separating vector is \(D^{1/2}\), and
\[
\Delta_D(T)=DTD^{-1},\qquad
\Delta_D^{it}(T)=D^{it}TD^{-it}.
\tag{MR5}
\]
The unbounded formula has its spectral domain; the second formula is a unitary on the whole Hilbert--Schmidt carrier. If \(De_i=p_i e_i\), all \(p_i>0\), then its orthonormal matrix-unit basis satisfies
\[
\Delta_D^{it}E_{ij}
=e^{it(\log p_i-\log p_j)}E_{ij}.
\tag{MR6}
\]
Thus the modular generator has pure point spectral type. Accumulation, or even density, of its eigenvalues does not turn these vector spectral measures into continuous measures.

For completeness, any unitary group with a countable orthonormal eigenbasis has the recurrence (MR1). Enumerate its frequencies as \(\omega_1,\omega_2,\ldots\). For finitely many frequencies, the integer powers of
\(z=(e^{i\omega_1},\ldots,e^{i\omega_N})\)
lie in a compact torus. They have a convergent subsequence. Differences of two sufficiently late powers can be chosen arbitrarily large while their quotient is arbitrarily close to the identity. Hence there exists an integer \(t_N>N\) such that
\[
\max_{j\le N}|e^{it_N\omega_j}-1|<1/N.
\tag{MR7}
\]
Every finite eigenvector combination returns along this sequence. The norm bound \(\|V_t-I\|\le2\) and density extend convergence to every vector. This proves strong recurrence of (MR5), including when \(\dim\mathcal K=\infty\).

The same proof applies to a countable direct sum of type-I factor standard forms with a faithful normal state. Each block contributes its matrix-unit frequencies. It applies in particular to the charged factors and faithful represented sector blocks in [[regional-preparation-algebras-and-vacuum-support|the regional support construction]]. Finite graph does not mean finite-dimensional Hilbert space; trace-class faithfulness in these factors is the relevant hypothesis here. A general type-I algebra with diffuse center is not covered by this countable matrix-unit argument.

The atomic-center qualification matters. On the type-I algebra \(L^\infty([0,1])\overline\otimes M_2\), use Lebesgue measure and the faithful density field
\[
D(x)=\frac{\operatorname{diag}(e^x,1)}{1+e^x}.
\tag{MR7a}
\]
In its direct-integral Hilbert--Schmidt standard form, the constant field \(E_{12}\) has norm one and evolves to \(e^{itx}E_{12}\). Therefore
\[
\|(\Delta^{it}-I)E_{12}\|^2
=2-2\frac{\sin t}{t}\longrightarrow2
\quad(|t|\longrightarrow\infty).
\tag{MR7b}
\]
This faithful normal state is not strongly recurrent. Thus nonrecurrence alone neither selects an algebra type nor proves a modular inclusion. A diffuse central preparation variable can spread modular frequencies, but its physical meaning and the required relative algebra positions remain separate constructions.

## The precise modular-inclusion consequence

Let \(\mathcal N\subseteq\mathcal M\) have a common cyclic and separating vector \(\Omega\) on one Hilbert space. In the convention of [[wall-construction-interface/half-sided-modular-tunnel|the modular tunnel]], suppose
\[
\Delta_{\mathcal M}^{it}\mathcal N\Delta_{\mathcal M}^{-it}
\subseteq\mathcal N\qquad(t\le0).
\tag{MR8}
\]
The [[library/extension-of-borchers-structure-theorem/inq|Araki--Zsido theorem]], with its compatible common standard-form hypotheses, supplies a positive self-adjoint \(P\), \(U(s)=e^{isP}\), and
\[
\Delta_{\mathcal M}^{it}P\Delta_{\mathcal M}^{-it}
=e^{-2\pi t}P,\qquad
\mathcal N=U(1)\mathcal M U(1)^*.
\tag{MR9}
\]
These are the theorem's affine covariance and algebra-return statements; their operator-domain conclusions are not inferred from a formal commutator. Combining them with (MR1) gives
\[
\boxed{\Delta_{\mathcal M}^{it}\text{ strongly recurrent}
\quad\Longrightarrow\quad P=0,
\quad\mathcal N=\mathcal M.}
\tag{MR10}
\]
The opposite half-sided convention gives the same conclusion by reversing the modular parameter. For a type-I factor \(\mathcal M\) with a common cyclic and separating vector, its faithful normal vector state is unitarily represented by (MR5); a countable direct sum of such factors is represented blockwise. Therefore no proper inclusion satisfying these common-vector hypotheses exists there.

This statement does not prohibit proper type-I subalgebras, nontrivial modular flow, or faithful entanglement. It also does not cover arbitrary semifinite weights by replacing them with states without justification. In particular, the faithful heat preparation in the regional owner has a nontrivial modular group and passes its Schmidt support test, while (MR10) prevents using it as an exact proper common-vector half-sided inclusion at that regulator.

The [[algebra/faithful-stationary-states-and-the-positive-clock|faithful stationary-clock theorem]] has a different hypothesis: its clock fixes the vacuum and normalizes one algebra for both time directions. Here the obstruction concerns the recurrence of the modular group that would dilate a separate positive translation. The [[mass-scale-calibration/joint-causal-generators-and-the-mass-casimir|opposed causal-generator construction]] remains the owner of the subsequent joint mass invariant; a single nontrivial affine translation is itself gapless.

## A quantitative test for the limiting programme

At a regulator, let a proposed positive generator \(P_a\) and modular group \(V_{a,t}\) be specified on the same carrier. No affine law is assumed. Define its bounded defect by
\[
\begin{aligned}
Q_a&=(I+P_a)^{-1},\\
Q_{a,t}&=(I+e^{-ct}P_a)^{-1},\\
E_a(t)&=V_{a,t}Q_aV_{a,t}^*-Q_{a,t}.
\end{aligned}
\tag{MR11}
\]
For any vector \(\xi\), the triangle inequality gives
\[
\begin{aligned}
\|(I-Q_a)\xi\|
\le{}&\|(I-Q_{a,t})\xi\|+\|E_a(t)\xi\|\\
&+\|(V_{a,t}-I)Q_a\xi\|
+\|(V_{a,t}^*-I)\xi\|.
\end{aligned}
\tag{MR12}
\]
Indeed \(VQV^*-Q=(V-I)Q+VQ(V^*-I)\) and \(\|Q\|\le1\). At a recurrent fixed regulator, choose its return times \(t_n\to\infty\). All terms on the right except the defect vanish, so
\[
\liminf_n\|E_a(t_n)\xi\|
\ge\|(I-Q_a)\xi\|.
\tag{MR13}
\]
If \(P_a\xi\ne0\) in the spectral sense \(\xi\notin\ker P_a\), the right side is strictly positive. Exact affine covariance, or a vanishing defect uniformly over all modular times on that vector, is impossible at this regulator. Approximation on each fixed finite time window can still be meaningful: the return times and the relevant spectral weight may escape as the regulator is removed.

This identifies a concrete order-of-limits obligation. Construct comparison maps for the regional carriers and sources, prove convergence of the modular unitaries and proposed translations on fixed time windows, and show that the limiting modular group has the required nonrecurrent sector. A recurrence sequence common to the limiting group would force its proposed translation to vanish by (MR10). Infinite entanglement, small Schmidt eigenvalues, or a named algebra type do not establish the required convergence or the relative position of two limiting algebras.

The ambitious next conjecture can therefore be stated without imposing an impossible finite test: a coherently sewn regional preparation family admits a nonrecurrent modular limit with the precise modular-inclusion and modular-intersection relations needed for the physical translation return. Those translations must be identified with the same returned clock tested by [[physical-response-coercivity/conditional-vacuum-rigidity-and-the-physical-gap|complete physical susceptibility]]. Neither that construction nor its uniform Yang--Mills gap estimate is proved here.

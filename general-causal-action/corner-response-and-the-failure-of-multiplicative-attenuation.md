# The Corner Rejects Multiplicative Local Attenuation

The matched corner Hamiltonians have a smaller absolute joint energy correction for \(SU(2)\) than for \(U(1)\), but their one-seam corrections are also smaller. Dividing out those already observed local responses reverses the comparison: the normalized non-Abelian connected gain is larger by the exact factor \(299687/239239>1\). This falsifies a rule that bounds the joint correction by the product of the two local attenuation factors. It does not refute oriented innovation transport or every possible bound on accumulated spatial response.

**Status: exact finite-graph comparison of the declared Wilson and heat Hamiltonians.** [[corner-hamiltonian-and-the-complete-fusion-response|The complete fusion response]] evaluates the non-Abelian coefficient; [[abelian-corner-and-the-joint-seam-energy|the Abelian control]] evaluates its counterpart. This note compares derivatives of those same fixed laws. No coupling or source is retuned to obtain the result.

## Retain the complete sector and the common temporal calibration

Use the nine-edge corner of [[three-face-corner-and-joint-seam-response|CJ]], with the source on \(U\) and two seams on \(V,W\). Keep the physical strengths \(g_i\), the energy scale \(\epsilon>0\), and the Hamiltonians
\[
\mathsf H^{SU}_{\mathbf g}
=\frac{4\epsilon}{3}\sum_{\text{raw }e}j_e(j_e+1)
+g_1(2-G_1)+g_2(2-G_2),
\]
\[
\mathsf H^{U}_{\mathbf g}
=\epsilon\sum_{\text{raw }e}n_e^2
+g_1(\sqrt2-G_1)+g_2(\sqrt2-G_2).
\tag{MA1}
\]
Here \(G_i\) is the fundamental \(SU(2)\) character or the \(U(1)\) real character \(\sqrt2\cos\theta_i\), respectively. Both have unit Haar variance. The fundamental raw-link energy is \(\epsilon\) in both laws. Their higher-representation energies remain different declared data.

Let \(E_{SU}(\mathbf g)\) denote the lowest excitation energy in the complete source-face odd sector, and \(E_U(\mathbf g)\) that in the complete retained central-flux \(+1\) sector. The latter has a conjugate \(-1\) sector with the same energy. In both cases subtract the actual vacuum energy. At zero seam strength,
\[
E_{SU}(0)=E_U(0)=4\epsilon.
\]
Each selected eigenbranch is simple and isolated within its retained sector near zero. These are not asserted to be the full physical gaps at nonzero seams.

Write
\[
D_i^A=-\partial_{g_i}^2E_A(0),\qquad
J_A=-\partial_{g_1}^2\partial_{g_2}^2E_A(0),
\quad A\in\{SU,U\}.
\tag{MA2}
\]
The derivatives computed below are positive in this sign convention: their contributions lower the corresponding excitation energy.

## The one-seam response is already reduced

For a free branch with seed \(e\) and energy \(E_0\), let \(R=(\mathsf H_0-E_0)^{-1}\) on its orthogonal complement. A zero-mean seam character \(G\) gives the ordinary quadratic energy coefficient
\[
-\langle Ge,RGe\rangle.
\tag{MA3}
\]
The derivative is twice this coefficient. The actual vacuum has \(\langle G,RG\rangle=1/(4\epsilon)\) for either group.

For the \(SU(2)\) source seed \(F\), the shared-edge singlet and triplet weights are \(1/4,3/4\). Their excitation denominators above \(F\) are \(2\epsilon,14\epsilon/3\), so
\[
\langle GF,RGF\rangle
=\frac{1/4}{2\epsilon}+\frac{3/4}{14\epsilon/3}
=\frac2{7\epsilon}.
\]
For \(U(1)\), the two unit-normalized charge moves have weights \(1/2,1/2\), with denominators \(2\epsilon,6\epsilon\), giving \(1/(3\epsilon)\). Subtracting the actual vacuum quadratic coefficient therefore yields
\[
\boxed{
D_1^{SU}=D_2^{SU}=\frac1{14\epsilon},\qquad
D_1^U=D_2^U=\frac1{6\epsilon}.}
\tag{MA4}
\]
Thus each local attenuation factor is \(D_i^{SU}/D_i^U=3/7\). This benchmark uses the same Hamiltonian limit as the fourth-order comparison; a small-transfer-parameter ratio is not substituted for it.

The complete corner calculations give
\[
\boxed{
J_{SU}=\frac{299687}{5885880\,\epsilon^3},\qquad
J_U=\frac{239}{1080\,\epsilon^3}.}
\tag{MA5}
\]
Their absolute ratio is
\[
\frac{J_{SU}}{J_U}
=\frac{2697183}{11722711}\simeq0.23008.
\tag{MA6}
\]
Both vacuum and disconnected fourth-order terms are included in these values.

## A normalization-invariant connected gain

Define
\[
\boxed{\mathcal M_A=\frac{\epsilon J_A}{D_1^A D_2^A}.}
\tag{MA7}
\]
This is a dimensionless comparison of the already computed response coefficients. Rescaling either seam character by \(c_i\) multiplies \(D_i\) by \(c_i^2\) and \(J\) by \(c_1^2c_2^2\), so those conventions cancel in \(\mathcal M\). Equivalently it is unchanged by independent linear reparametrizations of the two physical seam strengths.

It is also independent of a common choice of energy units. Under \(\widetilde E(\widetilde{\mathbf g})=cE(\widetilde{\mathbf g}/c)\), one has \(\widetilde\epsilon=c\epsilon\), \(\widetilde D_i=c^{-1}D_i\), and \(\widetilde J=c^{-3}J\). Equation (MA7) is unchanged. The corresponding clock convention is \(\widetilde a_t=a_t/c\), keeping the dimensionless evolution fixed. These covariance checks do not alter either Hamiltonian in (MA1).

Substitution gives
\[
\mathcal M_{SU}=\frac{299687}{30030},\qquad
\mathcal M_U=\frac{239}{30},
\]
\[
\boxed{
\frac{\mathcal M_{SU}}{\mathcal M_U}
=\frac{299687}{239239}
=1+\frac{60448}{239239}>1.}
\tag{MA8}
\]
The joint \(SU(2)\) response is therefore amplified relative to its two one-seam responses when compared with this Abelian control. This statement removes the local susceptibility factors; it does not remove all differences between their higher-representation kinetic laws.

## The precise strengthened rule that fails

Suppose an accumulation argument assigned each seam its observed attenuation factor \(a_i=D_i^{SU}/D_i^U\), and asserted that the joint energy-lowering correction could not exceed their product:
\[
J_{SU}\le a_1a_2J_U.
\tag{MA9}
\]
With the matched \(\epsilon\), this is equivalent to \(\mathcal M_{SU}\le\mathcal M_U\). But
\[
\frac{J_{SU}}{a_1a_2J_U}
=\frac{299687}{239239}>1,
\qquad a_1a_2=\frac9{49}.
\tag{MA10}
\]
Thus (MA9) is false on the actual complete corner sectors. The absolute reduction (MA6) remains true; it is insufficient evidence for multiplicative suppression of connected feedback.

[[corner-hamiltonian-and-the-complete-fusion-response|The changed-graph control]] also locates this response: replacing the shared seam edge by two independent links makes the connected Hamiltonian energy coefficient zero for \(SU(2)\), with every recoupling channel retained. The corresponding Abelian coefficient vanishes as well. This is a different graph. On that control both normalized joint gains are zero; it supplies no ratio of gains and no all-coupling conclusion.

The elementary singlet factors do not control the completed sum by themselves. For example, the single-seam product already redistributes unit norm between the weights \(1/4\) and \(3/4\). At fourth order, the free resolvents, the complete fusion weights and the disconnected contacts together determine (MA5). Keeping only the small outer-loop overlap omits terms that affect the normalized gain.

Any next accumulation estimate must therefore control those complete connected responses, rather than multiply the two local attenuation factors. It may use a different proved operator or cluster bound. No statement here excludes the [[determinant-response-sewing-and-relational-rigidity#Active candidate: oriented innovation transport|oriented innovation surplus conjecture]], establishes growth with volume, or promotes this finite comparison into a Yang–Mills continuum conclusion.

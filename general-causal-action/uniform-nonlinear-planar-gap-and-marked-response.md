# Uniform Nonlinear Planar Gap and Marked Response

The actual compact planar gap and the prescribed centered scalar susceptibility have uniform second-order expansions on the growing-patch confinement window. Their fourth-order remainders are bounded by \(Ch^4(L+1)^{21}\) and \(Ch^4(L+1)^{23}\), respectively. This resolves the stronger quantitative version of the marked-well test. The proof uses actual compact quasimodes and a centered Poisson equation, retaining the density, cutoff, moving vacuum and observable normalization.

**Status: uniform nonlinear return for the specified isolated planar family.** Keep the full Gauss carrier, comb connectors and fixed compact source of [[planar-patch-confinement-and-the-spatial-soft-mode|PP]], [[comb-face-transport-and-the-first-nonlinear-jet|FJ]] and [[uniform-marked-well-return-and-the-growing-patch-test|GW]]. The local coefficient algebra is owned by [[comb-chart-ellipticity-and-uniform-local-comparison|UC]], the actual operator remainder by [[compact-operator-taylor-remainder-on-planar-wells|OT]], and the compact cutoff by [[compact-cutoffs-and-uniform-polynomial-quasimodes|CQ]]. The marked Poisson proof is in [[uniform-centered-poisson-return-and-the-planar-source|the centered-source return]].

## The theorem keeps the actual source and clock

For the open \(L\times L\) square patch, impose Gauss law at every vertex, including the boundary. Fix \(\kappa>0\), equal magnetic strength \(g>0\), and put
\[
n=L+1,\qquad h=(\kappa/g)^{1/4},\qquad
E=\sqrt{\kappa g},\qquad
\epsilon=hn^{10},\qquad \theta=hn^{11/2}.
\tag{UN1}
\]
Let \(\Delta_L(g)\) be the complete physical gap of the actual compact operator. For the same comb-based plaquettes at every strength, retain
\[
\mathcal B_L=\left|\sum_pv_{11}(p)\mathbf q_p\right|^2,\qquad
B_h=4\mathcal B_L/h^2,\qquad
\mathcal S_L(h)
=E\frac{\mathcal X_{\mathcal B_L}}
{\operatorname{Var}(\mathcal B_L)}.
\]
The variance and reduced-resolvent susceptibility use the same actual normalized vacuum. Multiplying by \(4/h^2\) cancels from the normalized response.

There exist \(C,\eta>0\), independent of \(L,h\), such that throughout \(0<\epsilon\le\eta\),
\[
\boxed{
\left|\frac{\Delta_L(g)}E-c_L-h^2d_L\right|
\le Ch^4n^{21},\qquad
c_L=4\sqrt2\sin\frac{\pi}{2n},}
\tag{UN2}
\]
\[
\boxed{
\left|\mathcal S_L(h)-c_L^{-1}-h^2S_{2,L}\right|
\le Ch^4n^{23}.}
\tag{UN3}
\]
The coefficients \(d_L,S_{2,L}\) are the same complete fixed-patch coefficients as in [[nonlinear-scalar-source-and-the-vacuum-response-coefficient|NV]]. In particular, the source coefficient includes the spectral leakage term. The theorem makes no assumption on the sign of \(d_L\) at general \(L\).

## The formal energy branch becomes an actual compact eigenvalue

Take either the vacuum or first physical scalar oscillator branch. UC constructs normalized formal coefficients \(\psi_r,e_r\) with
\[
\|\psi_r\|\le C_rn^{11r/2},\qquad
|e_r|\le C_rn^{11r/2-1},\qquad r\ge1.
\]
For the sixth-order truncation, CQ supplies a normalized physical compact vector \(\Psi^{[6]}\) and real approximate energy \(e^{[6]}\) satisfying
\[
\boxed{
\|(\widehat H-e^{[6]})\Psi^{[6]}\|
\le \rho_6,\qquad
\rho_6=Ch^7n^{75/2}.}
\tag{UN4}
\]
This is a residual in the actual Haar norm. OT bounds the interior differential remainder, including coefficient derivatives and density divergence. CQ controls the cutoff commutator using \(\Gamma(W)\le8W\) and \(\mathsf C_{\rm raw}W=3W-6L^2\). Thus (UN4) is not inferred from a quadratic-form Taylor estimate alone.

The two seeds have even oscillator parity. The graded jets and normalized recursion therefore give \(e_r=0\) for odd \(r\). Consequently
\[
|e^{[6]}-e_0|
\le Cn^{-1}(\theta^2+\theta^4+\theta^6).
\]
The actual ordered comparison in [[uniform-planar-localization-and-the-first-physical-levels|UP]] and the isolation criterion in [[planar-physical-cluster-separation-and-the-uniform-window|PS]] place exactly one actual eigenline near each seed. A size-independent smaller choice of \(\eta\) puts \(e^{[6]}\) in that line's isolated interval and makes \(\rho_6\) smaller than its separation. The spectral theorem then gives
\[
|\widehat E_j-e_j^{[6]}|\le \rho_6,\qquad
\|(I-P_j)\Psi_j^{[6]}\|\le Cn\rho_6,\qquad j=0,1.
\tag{UN5}
\]
Ordered min–max has excluded additional low states; a small residual alone would not select the branch.

Subtract the two actual energies. Their constant difference is \(c_L\), and their \(h^2\) difference is \(d_L\). The remaining terms are bounded by
\[
C\bigl(h^4n^{21}+h^6n^{32}+h^7n^{75/2}\bigr)
=Ch^4n^{21}(1+\theta^2+\theta^3).
\tag{UN6}
\]
Since \(\theta=\epsilon n^{-9/2}\) is uniformly small, this proves (UN2). In physical energy units the bound is \(C\kappa h^2n^{21}\) for the remainder after \(Ec_L+\kappa d_L\).

## The source response requires the actual centered Poisson equation

The [[uniform-centered-poisson-return-and-the-planar-source|marked Poisson construction]] proves the following error ledger for this source. Its normalized formal source coefficients obey
\(\|z_r\|\le C_rn^{11r/2}\), and its formal centered Poisson coefficients obey
\(\|y_r\|\le C_rn^{11r/2+1}\).
The scalar component of \(y_r\) is fixed by orthogonality to the moving vacuum, not discarded.

At order six, CQ's forced-equation estimate makes the intrinsic compact Poisson residual \(O(h^7n^{77/2})\). The exact graph-norm source estimate of [[weighted-compact-source-return-on-growing-patches|WS]] transfers the actual vacuum from (UN4), giving normalized source-vector error \(O(h^7n^{83/2})\). The actual reduced inverse costs at most \(Cn\). Together with the independently retained source, normalization and cutoff errors, this gives
\[
\left|\mathcal S_L(h)-\mathcal S^{[6]}_{\rm formal}(h)\right|
\le Ch^7n^{85/2}.
\tag{UN7}
\]
Here
\(\mathcal S^{[6]}_{\rm formal}=\langle\sum_{r=0}^6h^rz_r,\sum_{r=0}^6h^ry_r\rangle\)
is the full Gaussian inner product of the two degree-six series, including their products through order twelve. The cutoff changes it by at most \(Ch^8n^{13}\), already smaller than the bound in (UN7). Its odd coefficients vanish by graded parity. Its coefficients through order two are exactly \(c_L^{-1}\) and \(S_{2,L}\); the remaining even terms are bounded by \(Ch^4n^{23}\) in this window.

Thus the complete susceptibility error is at most
\[
C\bigl(h^4n^{23}+h^7n^{85/2}\bigr)
\le Ch^4n^{23}.
\tag{UN8}
\]
Indeed the ratio of the second term to the first is
\(h^3n^{39/2}=\epsilon^3n^{-21/2}\).
This proves (UN3), with actual centering and variance division justified by the marked-source proof. It does not replace the source susceptibility by the inverse gap.

## The window preserves the soft harmonic behavior

Using UC's \(|d_L|\le Cn^{10}\), \(|S_{2,L}|\le Cn^{12}\) and \(c_L\asymp n^{-1}\), (UN2)–(UN3) give
\[
\boxed{
\left|\frac{\Delta_L(g)}{Ec_L}-1\right|
+|c_L\mathcal S_L(h)-1|
\le C(h^2n^{11}+h^4n^{22})
=C(\epsilon^2n^{-9}+\epsilon^4n^{-18}).}
\tag{UN9}
\]
These are stronger bounds than the proposed \(h^4n^{39}\), \(h^4n^{41}\) remainders in GW. Both that subordinate test and its marked asymptotic consequences are now supplied on the stated window.

For every sequence \(L\to\infty\), \(0<\epsilon_L\le\eta\),
\[
\frac{\Delta_L(g)}E\sim\frac{2\sqrt2\pi}{n},\qquad
\mathcal S_L(h)\sim\frac{n}{2\sqrt2\pi}.
\tag{UN10}
\]
The controlled nonlinear terms cannot replace the soft harmonic coefficient by a size-independent positive coefficient in this regime. At fixed \(\kappa\), the physical gap instead grows as
\(2\sqrt2\pi\kappa n^{19}/\epsilon_L^2\),
and the physical normalized susceptibility tends to zero. The complete innovation floor therefore has the same scaled-time versus physical-time distinction as UP and GW8.

The four-face control remains exact within this theorem: its negative gap correction coexists with a decreasing susceptibility of the original source, and the fixed oriented counterprobe removes its leading leakage. No positive nonlinear mass term has been inserted.

The window is a rapidly confining trajectory of an isolated planar vacuum. It is not a fixed-coupling thermodynamic limit, an inherited regional vacuum, or the four-dimensional Yang–Mills continuum trajectory. The remaining research task is to carry the complete marked law through spatial assembly and controlled crossover, where these estimates cease to be automatically small.

[[uniform-weighted-character-return-and-the-soft-gap|The weighted-character extension]] verifies the changed potential and uniform well before applying this proof structure to EH's preparation family. Differentiating its finite quasimode construction yields the sharper gap-contrast error \(C_I|\varepsilon_2-\varepsilon_1|h^4n^{13}\), because only single-face multiplication terms vary. That estimate resolves a contrast too small for subtracting two instances of the \(n^{21}\) remainder. It is a spectral extension; a uniform return of conditional fourth-moment products is a separate requirement.

# Regional Gauge Readouts and Conditional Lifting

A normalized gauge kernel can satisfy the probabilistic response-lifting hypotheses on the actual Wilson law when its core and boundary readouts remain regional. The unchanged conditional channel gives a sharper discarded-core estimate, and quantitative Fisher contraction bounds retained sensitivity to the boundary. The construction preserves the original observable carrier; it does not turn readout noise or a smooth coarse law into a physical gap.

**Status: [EXACT ONE-STEP SUFFICIENT NONLINEAR BOUNDS], uniform under the displayed incidence and strong-coupling conditions; [OPEN] for a continuum gauge-blocking tower and physical reconstruction.**

## One Wilson law and two regional kernels

Partition the active raw links into core \(Y\) and boundary \(Z\), with arbitrary fixed exterior links. Use the product-Haar \(SU(r)\) metric and Wilson action from [[nonlinear-conditional-gauge-response|the nonlinear conditional calculation]]. Choose normalized kernels
\[
q_X(X\mid Y),\qquad q_W(W\mid Z)
\]
of the [[normalized-gauge-kernels-and-markov-residues|compact path-average form]]. Every path for \(q_X\) uses only \(Y\)-links; every path for \(q_W\) uses only \(Z\)-links. Path endpoints must match within each average. Shared vertices and their gauge transformations are allowed; shared random seeds or opposite-region link dependence are not.

The enlarged law is
\[
d\widetilde\mu
=Z_\beta^{-1}e^{-S_\beta(Y,Z)}
q_X(X\mid Y)q_W(W\mid Z)\,dY\,dZ\,dX\,dW.
\tag{RGF1}
\]
All original \(Y,Z\) expectations and their complete bridge floor are preserved by [[bridge-data-augmentation-solder/regional-randomization-and-response-lifting|regional augmentation]]. This is stronger than merely keeping the partition function unchanged.

The normalized gauge-blocking precedent in [[library/the-classically-perfect-fixed-point-action-for-su3-gauge-theory/inq|DeGrand--Hasenfratz--Hasenfratz--Niedermayer]] supplies the kernel pattern, not a theorem that its usual averaging stencil respects this core--boundary split. A stencil crossing the split requires an explicit collar/state reassignment and a new carrier check.

## Original and posterior curvature constants

Let \(n_p\) count fine-edge occurrences in each plaquette, and \(n_{bi}^X\) those in the \(X\)-readout paths, extended by zero outside \(Y\). Set
\[
D_\beta=\beta\sum_p n_pn_p^{\mathsf T},\qquad
R_X=2\kappa_X\sum_{b,i}w_{bi}n_{bi}^X(n_{bi}^X)^{\mathsf T},
\]
\[
\rho_0:=r^2/2-\|D_\beta\|>0,\qquad
\rho_X:=r^2/2-\|D_\beta+R_X\|>0.
\tag{RGF2}
\]
Take a uniform bound \(h\) for the mixed \(Y,Z\) Hessian operator norm of the original action. For the elementary hypercubic convention without repeated-edge plaquettes,
\[
\|D_\beta\|\le8\beta(d-1),\qquad h=6\beta(d-1)
\tag{RGF3}
\]
are sufficient. Length-weighted readout incidence controls \(\|R_X\|\); it is not enough to count paths without their lengths.

The original law and each frozen-link conditional have Poincare constant at least \(\rho_0\). At a fixed readout \(X=x\), the actual posterior \((Y,Z)\mid X=x\) has potential
\[
S_\beta(Y,Z)
-\kappa_X\sum_b\phi(x_b,Z_b^X(Y))
+\sum_b\log N_{\kappa_X}(Z_b^X(Y)).
\tag{RGF4}
\]
The exact normalized Hessian gives constant \(\rho_X\), uniformly in \(x\). The marginal \(Y\mid X=x\) inherits this constant.

The fine-dependent log normalizers remain in (RGF4). Their \(Y,Z\) cross derivatives vanish because they depend only on \(Y\), not because they are dropped. Integrating out \(W\) uses its normalization; it does not add a \(q_W\) term to this posterior.

## Use the unchanged opposite conditional channel

At fixed \(X=x\),
\[
\mathcal L(Z\mid Y,X=x)=\mathcal L(Z\mid Y).
\tag{RGF5}
\]
Its normalized score in a \(Y\)-tangent has variance at most \(h^2/\rho_0\), by the original \(Z\mid Y\) Poincare estimate and mixed Hessian bound.

Apply conditional Fisher coercivity with actual context \(Y\mid X=x\), whose constant is \(\rho_X\), and hidden variable \(Z\). Equality of centered adjoint prediction norms then gives the required complete bridge floor for predicting \(Y\) from \(Z\) in that same fixed-\(X\) law:
\[
\boxed{b\ge
\frac{\rho_0\rho_X}{\rho_0\rho_X+h^2}.}
\tag{RGF6}
\]
This holds uniformly in \(x\), hence covers every enlarged-core observable \(F(Y,X)\). Testing only \(F(Y)\) would not suffice. The direct opposite orientation, using two posterior bounds, gives the weaker \(\rho_X^2/(\rho_X^2+h^2)\); (RGF5) avoids that unnecessary second loss.

## Quantitative Fisher contraction reduces relative leakage

Let \(\mathsf P_X\) be the weighted path-incidence matrix of \(q_X\), and put
\[
C_X=\kappa_X^2\|\mathsf P_X\|^2,\qquad
\tau_X=\frac{C_X}{\rho_0+C_X}.
\tag{RGF7}
\]
For each \(Z=z\), the actual \(Y\mid z\) law has Poincare constant \(\rho_0\), and [[joint-fisher-response-of-normalized-gauge-blocking|the whole normalized forward score]] is bounded by \(C_X\). Thus [[conditional-fisher-coercivity/coarse-graining-and-moving-context|quantitative Fisher contraction]] gives
\[
I_z^{\,X\mid Z}
\le\tau_X I_z^{\,Y\mid Z}
\le\frac{\tau_Xh^2}{\rho_0}g_Z.
\tag{RGF8}
\]
For \(g(Z)=\mathbb E[f(X)\mid Z]\), the actual \(Z\) marginal inherits Poincare constant \(\rho_0\). Therefore
\[
\begin{aligned}
\mathbb E\operatorname{Var}(g(Z)\mid W)
&\le\operatorname{Var}_{\mu_Z}g\\
&\le\frac{\tau_Xh^2}{\rho_0^2}
\mathbb E\operatorname{Var}(f(X)\mid Z).
\end{aligned}
\tag{RGF9}
\]
This proves relative leakage with
\[
\boxed{r_{\partial}\le\tau_Xh^2/\rho_0^2.}
\tag{RGF10}
\]
It works for any normalized regional \(q_W\); no curvature estimate for the posterior \(Z\mid W\) is needed in this regime. The estimate is conservative: it discards the information retained by \(W\), so it does not approach zero merely because \(W\) approaches a faithful boundary readout. At \(\kappa_X=0\), however, \(\tau_X=0\) and the retained core is independent of the boundary, as it should be.

If the readout depends only on a smaller core \(C\subset Y\), separated from \(Z\) by a collar, [[collared-quasi-factorization-and-surface-response/fisher-collar-bound-for-wilson-laws|the integrated collar estimate]] gives \(I_Z^{C\mid Z}\le h_{\rm eff}^2/\rho_0\). Apply the same channel contraction on \(C\mid Z\) and replace \(h^2\) by \(h_{\rm eff}^2\) in (RGF8)--(RGF10). This does not improve (RGF6) automatically: the complete discarded core still contains collar observables touching \(Z\).

## The one-step return to the original response

If the actual retained pair \(X,W\) has a proved complete floor \(\kappa_c>0\), then
\[
\boxed{
\kappa_{\rm original}\ge
\frac{\rho_0\rho_X}{\rho_0\rho_X+h^2}
\frac{\rho_0^2}{\rho_0^2+\tau_Xh^2}\,\kappa_c.}
\tag{RGF11}
\]
The hypotheses are on original and posterior product-Haar carriers, not a singular orbit quotient. Restricting a proved full-carrier inequality to gauge-invariant original observables is valid; quotienting regions independently before gluing is not part of this construction.

The formula makes the two conditional obligations explicit for genuinely probabilistic gauge blocking. It need not improve the direct strong-coupling response bound. In particular, making \(X\) an independent readout leaves all original difficulty in the discarded-core term; its coarse floor one is not a physical gap.

[[exact-wilson-interface-statistics|Exact cross-plaquette statistics]] take another route: retaining all predictive interface data gives \(b=1\) and zero leakage at arbitrary finite coupling, but leaves the induced interface law to be controlled. A common-positive noisy kernel cannot achieve that exact sufficiency for dependent regions. [[bridge-data-augmentation-solder/predictive-sufficient-interfaces|Discarded-prediction lifting]] also avoids demanding a uniform conditional-fiber coefficient when a direct complete operator-norm estimate is available.

Every later exact RG marginal is an effective law, generally not a Wilson action with one replaced coupling. Iteration needs its own posterior constants, channel bounds, induced metrics and uniformly finite logarithmic loss. The estimates (RGF2) are strong-bare-coupling sufficient conditions and do not control the weak-bare-coupling continuum path. The conservative global leakage bound (RGF9) also does not prove decay of loss across scales. Those estimates and the nontrivial continuum/OS return remain the load-bearing open work.

[[bridge-data-augmentation-solder/receipts/regional_randomization_receipt.py|The regional receipt]] checks normalized finite-subgroup examples, the enlargement identities, quantitative score contraction and the stated sufficient-constant arithmetic. It is not a numerical verification of the \(SU(r)\) curvature theorem or its continuum hypotheses.

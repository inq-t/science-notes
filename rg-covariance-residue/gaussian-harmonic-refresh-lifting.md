# Gaussian Harmonic Lifts and Retained Dynamics

A Gaussian coarse observation admits an exact energy-orthogonal split into retained data and independent discarded fluctuations. Harmonic lifting turns dynamics on those two carriers into commuting dynamics of the original law. For regular gauge averages the lift stays uniformly bounded across arbitrarily many aligned blocking steps, allowing one fine/coarse gradient comparison without multiplying a loss at every level. The retained Maxwell modes remain massless; this constructs an interface, not a Yang--Mills mass gap.

**Status: exact finite-dimensional Gaussian theorem, with uniform geometric constants for the specified linear gauge quotient. No nonlinear Wilson transport or physical-time identification is asserted.**

## What the lift operates on

Let \(H_f,H_c\) be finite-dimensional real Euclidean spaces, \(K_f>0\), and \(Q:H_f\to H_c\) onto. The spaces carry configuration variations, not quantum states. Define
\[
C_f=K_f^{-1},\quad C_c=QC_fQ^*,\quad K_c=C_c^{-1},\quad
M=C_fQ^*K_c,\quad V=\ker Q.
\tag{HL1}
\]
For \(X\sim\mathcal N(0,C_f)\), set \(Z=QX\) and \(\zeta=X-MZ\). Direct multiplication gives
\[
QM=I,\quad Q\zeta=0,\quad
\operatorname{Cov}(\zeta,Z)=0.
\tag{HL2}
\]
Joint Gaussianity therefore makes \(\zeta\) and \(Z\) independent. With
\(K_V=\Pi_VK_f|_V\), the energy identity is
\[
\langle \zeta+Mz,K_f(\zeta+Mz)\rangle
=\langle\zeta,K_V\zeta\rangle+\langle z,K_cz\rangle.
\tag{HL3}
\]
The cross term vanishes because \(K_fM=Q^*K_c\). The conditional fluctuation law is \(\mathcal N_V(0,K_V^{-1})\); its covariance on \(H_f\) is \(C_f-MC_cM^*\). The constant Jacobian of this linear change of coordinates is absorbed by Gaussian normalization.

## Two commuting dynamics, on the actual law

The bijection \(T:V\oplus H_c\to H_f\), \(T(\zeta,z)=\zeta+Mz\), induces a unitary
\[
Uf=f\circ T:
L^2(\mu_f)\longrightarrow L^2(\mu_V\otimes\mu_c).
\tag{HL4}
\]
Take ergodic reversible Markov semigroups on the two actual Gaussian marginals, with nonnegative self-adjoint generators \(L_V,L_c\) and gaps \(\gamma_V,\gamma_c\). Their product lifts to
\[
\mathscr L=U^{-1}(L_V\otimes I+I\otimes L_c)U,\qquad
\boxed{\operatorname{gap}\mathscr L=\min\{\gamma_V,\gamma_c\}.}
\tag{HL5}
\]
The sum is defined by its closed nonnegative form. Product spectral calculus proves the bound on the complete \(L^2\) space, including mixed observables; observables of either factor alone give equality.

A retained move \(z\to z'\) becomes
\[
X\longmapsto X+M(z'-QX).
\tag{HL6}
\]
It preserves \(\zeta\). A discarded move changes \(\zeta\) while preserving \(z\). Thus the lifted semigroups commute and preserve the original fine Gaussian law. Complete conditional refresh of \(\zeta\) at unit rate has \(\gamma_V=1\), but cannot improve a gapless retained dynamics. Rate normalization matters: multiplying either generator is not a derivation of a mass.

## Composition without repeated losses

For a hard Gaussian tower \(C_{j+1}=Q_jC_jQ_j^*\), put \(M_j=C_jQ_j^*C_{j+1}^{-1}\). Cancellation of neighboring covariance factors gives
\[
\boxed{
M_0\cdots M_{k-1}
=C_0(Q_{k-1}\cdots Q_0)^*C_k^{-1}.}
\tag{HL7}
\]
Aligned regular averages compose to the single composite average \(Q_n\). Use the physical quotient metrics and remove harmonics as in [[endpoint-averages-and-quadratic-ultraviolet-control|the endpoint-average theorem]]. Its (EA15)--(EA18) give, for \(b=na\),
\[
\|M\|\le r_d=(\pi/2)^{d+1},\qquad
K_V\ge\frac{c_d^{\rm fib}}{b^2}I,\qquad
c_d^{\rm fib}=\frac4{1+r_d^2}.
\tag{HL8}
\]
The bound is for the composite lift itself, not a product \(r_d^k\) of separate estimates. Also \(\|Q\|\le1\) and
\(T^{-1}X=((I-MQ)X,QX)\), so
\(\|T^{-1}\|^2\le(1+r_d)^2+1\).
Uniform conditioning of this change of variables says nothing by itself about its spatial range.

## One comparison to the fine gradient form

Now choose the natural Gaussian gradient forms, all with coefficient one in their stated physical Euclidean metrics. For a smooth \(f\),
\[
\mathcal E_{\rm prod}(Uf)
=\int\left(\|\Pi_V\nabla f\|^2+\|M^*\nabla f\|^2\right)d\mu_f
\le(1+r_d^2)\mathcal E_f(f).
\tag{HL9}
\]
The identity extends to the closed form domains by density. Their Poincare gaps are the least precision eigenvalues: \(\lambda_f=\lambda_{\min}(K_f)\), \(\lambda_c=\lambda_{\min}(K_c)\). Product Poincare, (HL8), and (HL9) yield
\[
\boxed{
\lambda_f\ge\frac1{1+r_d^2}
\min\left\{\frac{c_d^{\rm fib}}{b^2},\,\lambda_c\right\}.}
\tag{HL10}
\]
This is a comparison with the original fine gradient dynamics, not just a gap chosen for a new process. Apply it once at any composite scale. Its dimensions are inverse length squared in the stated configuration metric; it is not yet a Hamiltonian energy or an inverse physical clock time.

## Where the long-wavelength response remains

For the same hard Gaussian quotient,
\[
K_b\le K_c\le C_d^{\rm Max}K_b,\qquad
C_d^{\rm Max}=\frac{\pi^2}{4}r_d^2.
\tag{HL11}
\]
On a cubic torus with physical side \(\mathcal R=Nb\), the least nonzero Maxwell eigenvalue is \(4b^{-2}\sin^2(\pi/N)\). Hence the actual retained precision still has lowest eigenvalue of order \(\mathcal R^{-2}\), uniformly in blocking depth. Eliminating short-wavelength fluctuations does not eliminate this retained mode.

The actual noisy tower of [[soft-gaussian-gauge-blocking|soft Gaussian blocking]] has the hard covariance plus a positive accumulated-noise covariance. Inverting, and combining with (SG6), gives
\[
\boxed{\Gamma^{-1}K_{b_k}\le P_k\le C_d^{\rm Max}K_{b_k}.}
\tag{HL12}
\]
Thus that retained law also remains of Maxwell order. This comparison does not transfer the hard identity \(QM=I\) to the noisy observation channel.

## The nonlinear replacement need not be flat

For a nonlinear law, conditional fibers need not be translates of one common measure. The replacement for (HL6) must transport the actual conditional law over \(z\) to the actual conditional law over \(z'\), with controlled distortion in the relevant derivative or refresh form. A merely measurable trivialization supplies neither that control nor locality. Fiber coercivity alone leaves the retained dynamics untouched.

[[conditional-fisher-coercivity/measure-preserving-horizontal-lifts|Measure-preserving horizontal lifts]] now construct this transport for smooth compact conditional families. Curvature need not vanish: conditional expectation still reduces the lifted diffusion. [[nonlinear-gauge-fiber-transport|The actual gauge application]] supplies finite-regulator existence and a quantitative one-step strong-coupling comparison. Uniform distortion, retained response and physical source control through the continuum trajectory remain unproved. [[conditional-fisher-coercivity/tensor-local-refresh-and-inverse-square-patches|The Wilson projection criterion]] offers a separate finite-region route. Neither route identifies an auxiliary generator with the reconstructed physical Hamiltonian.

The [[receipts/harmonic_refresh_lifting_receipt.py|finite verification receipt]] checks the Gaussian split, harmonic composition and physical-metric bounds on finite quotient matrices. Such checks supplement the proof and do not establish its nonlinear extension.

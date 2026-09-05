# Volume-Uniform Fusion Envelopes

A compact-group bridge admits a prediction envelope that survives arbitrarily many independent factors when its representation cost is controlled under tensor-product fusion. Combining a low-mode contraction with a decaying fusion bound removes the prefactor before tensorization. Haar heat kernels supply this structure for every compact connected Lie group with a fixed bi-invariant metric; a different transfer kernel needs its own fusion-cost estimate.

**Status: [EXACT] under the declared compact-kernel and fusion-growth hypotheses; [EXACT] for Haar heat and independent products; [OPEN] for interacting Wilson laws and uniform continuum calibration.** [[compact-heat-bridge-fusion-tail|The compact heat-bridge calculation]] owns the weighted insertion and Peter--Weyl diagonalization. The argument here extends that calculation beyond a fixed \(SU(2)\) cutoff and avoids a prefactor raised to the number of links.

## The representation cost must match the supplied kernel

Let \(G\) be a compact connected Lie group with Haar probability. Let \(h\) be a strictly positive continuous central symmetric probability density. Assume its convolution operator \(P\) has strictly positive eigenvalues
\[
0<\lambda_r\le1,\qquad \lambda_0=1,\qquad
w_r:=-\log\lambda_r
\tag{VE1}
\]
on irreducible matrix-coefficient blocks. Strict positivity of a density alone does not imply strict Hilbert positivity; both hypotheses are being supplied.

The midpoint law is \(dy\,h(y^{-1}x)h(y^{-1}z)\,dx\,dz\). Write \(K\) for prediction from the two endpoints and \(S=K^*K\). Simultaneous left/right equivariance makes \(S\) scalar, with eigenvalue \(\gamma_r\), on each \(V_r\otimes V_r^*\).

Put \(h_2=h*h\), \(m=\min h\), \(m_2=\min h_2\), \(M_2=\max h_2\). The kernel insertion calculation gives
\[
\gamma_r\le\frac{N_r}{m_2},\qquad
N_r=\frac1{d_r}\sum_{a,b}d_a d_b N_{ab}^{\,r}
\lambda_a^2\lambda_b^2.
\tag{VE2}
\]
Here \(N_{ab}^{\,r}\) is the nonnegative tensor-product multiplicity, not a fitted degeneracy. The sums are absolutely convergent: \(h\in L^2\) implies \(\sum_r d_r^2\lambda_r^2<\infty\), and \(|\chi_r|\le d_r\).

Suppose there are independently proved constants \(C>0,D\ge0\) such that
\[
N_{ab}^{\,r}>0\quad\Longrightarrow\quad
w_r\le C(w_a+w_b)+D.
\tag{VE3}
\]
Then \(\lambda_a\lambda_b\le e^{D/C}\lambda_r^{1/C}\) on every contributing channel. Keeping one of the two product factors in (VE2) gives
\[
N_r\le e^{D/C}\lambda_r^{1/C}
\frac1{d_r}\int_Gh(g)^2\overline{\chi_r(g)}\,dg
\le e^{D/C}\|h\|_2^2\lambda_r^{1/C}.
\tag{VE4}
\]
The middle Fourier coefficient is nonnegative because it is a fusion sum. An \(L^2\) approximation justifies its expansion even when the series for \(h\) is not absolutely convergent. No fractional power of \(P\) has been assumed to be a Markov kernel.

## Remove the prefactor before multiplying carriers

Every normalized midpoint bridge density is at least \(m^2/M_2\) relative to Haar. Conditional variance therefore gives, for nontrivial \(r\),
\[
\gamma_r\le1-\varepsilon=e^{-u},\qquad
\varepsilon:=\min\{1/2,m^2/M_2\},\qquad u:=-\log(1-\varepsilon)>0.
\]
Together with (VE4), put
\[
A:=e^{D/C}\|h\|_2^2/m_2\ge1,\qquad
\gamma_r\le\min\{e^{-u},A e^{-w_r/C}\}.
\tag{VE5}
\]
The two branches meet at \(w=C(u+\log A)\). On either side their smaller value is bounded by
\[
\boxed{\gamma_r\le e^{-\vartheta w_r},\qquad
\vartheta:=\frac1C\frac{u}{u+\log A}>0.}
\tag{VE6}
\]
The trivial block has \(\gamma_0=1\) and satisfies the same inequality. Thus, with \(W=-\log P\) defined spectrally,
\[
\boxed{S\le e^{-\vartheta W}.}
\tag{VE7}
\]
Unlike \(S\le A e^{-W/C}\), this estimate has no prefactor to multiply.

For independent factors with coefficients \(\vartheta_e\ge\vartheta_*>0\), positivity of tensor products gives
\[
\boxed{\bigotimes_eS_e
\le\exp\left[-\vartheta_*\sum_e W_e\right].}
\tag{VE8}
\]
This is an operator comparison on all product observables, including mixed modes. For a spectral tail above \(\Lambda>0\) of \(\sum_eW_e\),
\[
\|K_{\rm product}Q_\Lambda\|^2\le e^{-\vartheta_*\Lambda},
\tag{VE9}
\]
independently of the number of factors. It extends on a supplied countable product through its dense cylinder carrier. It does not apply to correlated factors merely because the interaction is spatially local.

## Haar heat supplies the fusion-growth law

For the heat kernel \(h_t\) of a fixed bi-invariant Laplacian \(L\),
\(\lambda_r=e^{-tc_r}\), where \(c_r\) is the nonnegative Casimir eigenvalue. On a tensor-product representation the self-adjoint generators are \(J_i^{(a)}\otimes I+I\otimes J_i^{(b)}\). The operator identity
\[
2(c_a+c_b)I-\sum_i(J_i^{(a)}\otimes I+I\otimes J_i^{(b)})^2
=\sum_i(J_i^{(a)}\otimes I-I\otimes J_i^{(b)})^2\ge0
\]
implies
\[
N_{ab}^{\,r}>0\quad\Longrightarrow\quad c_r\le2(c_a+c_b).
\tag{VE10}
\]
Thus (VE3) holds with \(C=2,D=0\) for any such compact group, not just \(SU(2)\). Also \(\|h_t\|_2^2=h_{2t}(e)=\max h_{2t}\). Certified bounds
\[
0<l_t\le\min h_t,\qquad 0<l_{2t}\le\min h_{2t},\qquad
U_{2t}\ge h_{2t}(e)
\]
therefore give
\[
\varepsilon=\min\{1/2,l_t^2/U_{2t}\},\quad
u=-\log(1-\varepsilon),\quad A=U_{2t}/l_{2t},\quad
\boxed{S_t\le e^{-b(t)L},\qquad
b(t)=\frac t2\frac{u}{u+\log A}>0.}
\tag{VE11}
\]
Heat-kernel minima increase with time and maxima decrease, by convolution with a probability density. Bounds certified at \(t_0>0\) consequently give one \(b_0>0\) valid for every \(t\ge t_0\). The coefficient is not uniform down to zero heat time: the general lower order \(S_t\ge e^{-2tL}\) forces any admissible \(b(t)\le2t\) on a nontrivial block.

## Concave costs inherit the same fusion constant

The cost need not be linear in the Casimir. Let \(F:[0,\infty)\to[0,\infty)\) be increasing and concave with \(F(0)=0\). Concavity gives
\[
F(a+b)\le F(a)+F(b),\qquad F(2a)\le2F(a).
\]
For the first inequality, apply concavity between \(0\) and \(a+b\) separately at \(a\) and \(b\), then add. Thus a cost \(w_r=F(c_r)\) satisfies
\[
c_r\le2(c_a+c_b)
\quad\Longrightarrow\quad
\boxed{w_r\le2(w_a+w_b).}
\tag{VE14}
\]
It supplies (VE3) with \(C=2,D=0\), without supplying a positive lower comparison \(F(c)\ge\eta c\).

One source of such functions is a positive measure, not a freely fitted spectral profile:
\[
\phi(s)=\int_0^\infty e^{-st}\,\mu(dt),\qquad
F(s)=-\log\phi(s),\qquad \mu([0,\infty))=1.
\tag{VE15}
\]
The Laplace transform is positive and log-convex by Hölder's inequality, so \(F\) is increasing and concave. Where moments under the tilted measure exist, \(F'(s)=\mathbb E_s t\) and \(F''(s)=-\operatorname{Var}_s(t)\). These facts require neither infinite divisibility of \(\mu\) nor a Markov interpretation of every fractional power of \(\phi(L)\). The kernel regularity and strict-positivity hypotheses in (VE1) still have to be checked.

[[wilson-bridge-envelopes-under-temporal-blocking|Wilson temporal blocking]] realizes this mechanism through the Hartman--Watson measure and obtains the sharp universal fusion constant \(2\) for the actual \(SU(2)\) Wilson weights.

## An elementary \(SU(2)\) certificate

In the convention \(c_j=j(j+1)\), define
\[
T_t=\sum_{n\ge1}(n+1)^2e^{-t n(n+2)/4}.
\]
If \(q_t=(9/4)e^{-5t/4}<1\), successive terms have ratio at most \(q_t\), so
\[
T_t\le\frac{4e^{-3t/4}}{1-q_t}.
\tag{VE12}
\]
This certifies \(T_3<9/20\) and \(T_6<1/20\), hence
\[
l_3=11/20,\qquad l_6=19/20,\qquad U_6=21/20.
\]
Using \(u\ge\varepsilon=121/420\) and
\(\log A\le A-1=2/19\) in (VE11) gives
\[
b(3)\ge\frac{6897}{6278}>1.
\]
Therefore the deliberately conservative exact calibration is
\[
\boxed{S_t^{(E)}\le e^{-\sum_eL_e}\quad(t\ge3)}
\tag{VE13}
\]
at every finite product size. These numbers certify a chosen group-heat convention, not a mass in physical units. [[receipts/volume_uniform_envelope_receipt.py|The receipt]] uses rational exponential bounds to verify the heat certificate, not an uncertified sampled minimum.

## What survives gauge reduction and what does not

[[gauge-quotients-of-midpoint-bridges|Independent endpoint gauge quotients]] preserve (VE8) by order, although they need not preserve equality with the restricted raw bridge or its spectral diagonalization. The existing [[contemporary-puzzles/yang-mills-mass-gap/gauge-descent-flux-fisher-coercivity|girth--Casimir theorem]] then supplies the pure-electric gauge-invariant lower spectral edge. That is a controlled product calibration.

Two separate changes prevent a direct promotion to the physical theory. First, the finite-spacing Wilson kinetic eigenvalues have a different high-spin logarithmic cost from the heat Casimir; [[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder|the bounded-flux audit]] already rules out a uniform positive electric-form lower comparison for that kernel. The \(SU(2)\) case now has [[wilson-bridge-envelopes-under-temporal-blocking|its own sharp fusion law and temporally uniform blocked envelope]], using those Bessel logarithmic weights rather than an assumed Gaussian tail. Second, the interacting Perron state changes the fixed vector and norm. [[vacuum-aligned-innovation-completion/heat-envelopes-and-the-vacuum-vector|Vacuum-compatible heat comparisons]] gives an analytic counterexample to simply dressing the Haar estimate.

The progress is a volume-independent fusion criterion and a complete compact calibration. It does not select the interacting law, establish its low-energy response, or construct the nontrivial continuum limit.

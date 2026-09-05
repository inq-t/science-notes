# Wilson Bridge Envelopes Under Temporal Blocking

The actual \(SU(2)\) Wilson transfer cost obeys a sharp fusion-growth law even though it is not a quadratic Casimir. Its Bessel ratios are a positive mixture of heat weights, whose negative logarithm is an increasing concave function of the Casimir. Composing genuine Wilson steps then gives an explicit bridge envelope uniform in coupling and independent product size at a fixed positive blocked depth. The remaining obstruction is the interacting vacuum, not the absence of a pure-kernel fusion bound.

**Status: [EXACT] for normalized \(SU(2)\) Wilson convolution, independent products, the declared gauge quotient and temporal blocking; [OPEN] for interacting four-dimensional Yang--Mills and its simultaneous continuum and infinite-volume limits.** The [[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder|bounded-flux audit]] owns the Wilson character calculation, high-spin no-go and pure transfer edge. [[volume-uniform-fusion-envelopes|The general envelope theorem]] owns the passage from fusion cost to complete two-ended prediction.

## The positive measure behind the Wilson cost

Use the group Laplacian convention \(L|_j=j(j+1)\). Write \(l=2j\in\mathbb N_0\), \(d=l+1\), and
\[
Z(x)=\frac{2I_1(x)}x,\qquad
h_x(q)=\frac{e^{xq_0}}{Z(x)},\qquad
p_l(x)=\frac{I_{l+1}(x)}{I_1(x)},\qquad
w_l(x)=-\log p_l(x),\quad x>0.
\tag{WB1}
\]
Here \(q\in SU(2)\cong S^3\), \(q_0=\tfrac12\operatorname{ReTr}q\), and Haar measure has total mass one. \(P_x\) denotes convolution by \(h_x\), not an interacting transfer.

[[library/exponential-functionals-of-brownian-motion-i/inq|Matsumoto--Yor, Section 2]] supplies a positive probability measure \(\eta_x\) satisfying
\[
\frac{I_\nu(x)}{I_0(x)}
=\int_0^\infty e^{-\nu^2 a/2}\,\eta_x(da),\qquad \nu\ge0.
\tag{WB2}
\]
Equation (2.8) gives a concrete realization: the conditioned law of \(\int_0^tR_s^{-2}\,ds\) for an index-zero Bessel process with positive endpoints \(r,\rho\), where \(r\rho/t=x\). This is a mathematical representation of the kernel, not a claim that nature has a primitive random clock.

Tilt the measure by the vacuum normalization:
\[
\mu_x(da):=\frac{e^{-a/2}\eta_x(da)}{I_1(x)/I_0(x)},\qquad
F_x(s):=-\log\int_0^\infty e^{-sa/2}\mu_x(da).
\tag{WB3}
\]
Then \(\mu_x\) is a probability measure, \(F_x(0)=0\), and
\[
\boxed{w_l(x)=F_x(l(l+2)),\qquad
P_x=\int_0^\infty e^{-2aL}\mu_x(da)
=e^{-F_x(4L)}.}
\tag{WB4}
\]
The integral is a bounded strong operator integral. The factor \(4\) follows from \(l(l+2)=4j(j+1)\); the factor \(2\) in heat time is equally fixed. No auxiliary Bessel duration has been identified with laboratory time.

By [[volume-uniform-fusion-envelopes#Concave costs inherit the same fusion constant|log-Laplace concavity]], \(F_x\) is increasing and concave. In an \(SU(2)\) fusion channel \(r\subset m\otimes l\), one has \(r\le m+l\), hence
\[
r(r+2)\le2\{m(m+2)+l(l+2)\}.
\]
Consequently
\[
\boxed{w_r(x)\le2\{w_m(x)+w_l(x)\}.}
\tag{WB5}
\]
This is uniform over coupling and representations. It uses neither infinite divisibility nor a Markov assumption for fractional powers.

The constant \(2\) is universally sharp. The fixed-order large-\(x\) expansion gives
\[
w_l(x)=\frac{l(l+2)}{2x}+O_l(x^{-2}).
\]
For \(m=l=N,\ r=2N\), the ratio \(w_{2N}/(2w_N)\) tends to \(2(N+1)/(N+2)\), which approaches \(2\) as \(N\to\infty\). These are successive limits; no uniform large-\(x\) expansion in \(N\) is assumed.

## Exact one-step constants expose the refinement problem

Rotational invariance of Haar measure on \(S^3\) gives
\[
(h_x*h_x)(q)
=\frac{Z(x\sqrt{2+2q_0})}{Z(x)^2}.
\tag{WB6}
\]
Indeed the exponent in the convolution is \(xv\cdot(e+q)\), and \(|e+q|=\sqrt{2+2q_0}\). Since \(Z\) is increasing on nonnegative arguments and \(Z(0)=1\),
\[
\min h_x=\frac{e^{-x}}{Z(x)},\quad
\min(h_x*h_x)=\frac1{Z(x)^2},\quad
\max(h_x*h_x)=\frac{Z(2x)}{Z(x)^2}.
\tag{WB7}
\]
Thus the generic theorem has
\[
A_x=Z(2x),\quad
\varepsilon_x=\min\{1/2,e^{-2x}/Z(2x)\},\quad
\vartheta_x=\frac12\frac{-\log(1-\varepsilon_x)}
{-\log(1-\varepsilon_x)+\log A_x}>0.
\tag{WB8}
\]
It proves \(S_x\le P_x^{\vartheta_x}\), but this particular one-step certificate deteriorates rapidly as \(x\to\infty\). A vanishing certificate is not a proof that the blocked physical process is gapless.

## Actual temporal blocking removes that loss

Let \(n\in\mathbb N\), \(h_{x,n}=h_x^{*n}\), and \(W_{x,n}=-n\log P_x\). Let \(K_{x,n}\) predict the midpoint from endpoints \(n\) steps away under the stationary Haar law; set \(S_{x,n}=K_{x,n}^*K_{x,n}\).

[[library/inequalities-for-modified-bessel-functions/inq|Näsell's Proposition 1]] gives, for integers \(d\ge2\),
\[
\frac{I_d(x)}{I_1(x)}
<\prod_{\nu=1}^{d-1}\frac{x}{x+\nu}.
\]
For \(x\ge1\), the increasing function \(x\log(1+\nu/x)\) is at least \(\log(1+\nu)\). Therefore
\[
\boxed{x\ge1,\quad n/x\ge\tau_->0
\quad\Longrightarrow\quad
p_{d-1}(x)^n\le(d!)^{-\tau_-}.}
\tag{WB9}
\]
This bound covers all representations at once, not just a fixed finite collection.

Using the spin-indexed character bound \(|\chi_{(d-1)/2}|\le d\) in the character expansion yields
\[
\|h_{x,n}-1\|_\infty
\le\sum_{d\ge2}\frac{d^2}{(d!)^{\tau_-}}.
\tag{WB10}
\]
At \(n/x\ge4\), successive terms of the fourth-power sum have ratio at most \(1/36\), while the first term is \(1/4\). At \(2n/x\ge8\), the corresponding ratio is at most \(1/2916\), with first term \(1/64\). Hence
\[
\|h_{x,n}-1\|_\infty\le\frac9{35},\qquad
\|h_{x,2n}-1\|_\infty
\le\frac{729}{46640}<\frac1{60}.
\tag{WB11}
\]
In particular
\[
\min h_{x,n}\ge\frac{26}{35},\qquad
\frac{59}{60}\le h_{x,2n}\le\frac{61}{60}.
\]
These are analytic tail certificates, not sampled minima.

Multiplication by \(n\) preserves (WB5). The envelope theorem may therefore use \(C=2,D=0\), \(\varepsilon=1/2\) and \(A=61/59\): indeed \((26/35)^2/(61/60)>1/2\). Since \(\log2\ge2/3\) and \(\log(61/59)\le2/59\), it gives
\[
\boxed{
S_{x,n}\le e^{-\vartheta_*W_{x,n}},\qquad
\vartheta_*=\frac{59}{124},\qquad
x\ge1,\quad n/x\ge4.}
\tag{WB12}
\]
The rational numbers certify a deliberately conservative group-kernel convention. They are not fundamental constants or mass predictions.

## Products and the physical quotient

For independent links with \(x_e\ge1\) and \(n_e/x_e\ge4\), tensorization gives
\[
\bigotimes_e S_{x_e,n_e}
\le\exp\!\left[-\vartheta_*\sum_eW_{x_e,n_e}\right],
\tag{WB13}
\]
without a factor raised to the number of links. [[gauge-quotients-of-midpoint-bridges|The gauge quotient theorem]] passes this inequality to separately quotiented physical endpoints.

For one common \(x,n\), the full-vertex, unconstrained-link spin-network support theorem gives
\[
\sum_e W_{x,n,e}\ge
g(\Gamma)n\,w_1(x)Q_0.
\]
Equation (WB9) also gives \(n w_1(x)\ge4\log2\). Thus
\[
\boxed{I-\bar S_{x,n}^{(\Gamma)}
\ge\left(1-2^{-(59/31)g(\Gamma)}\right)Q_0.}
\tag{WB14}
\]
A fully gauged tree has only constants; charged boundaries, matter or holonomy constraints change the support argument. This is a complete response bound for the declared independent kinetic law, not the magnetic Wilson vacuum.

## The heat limit is uniform, but not a finite-spacing Casimir bound

For \(x\to\infty\) and \(n/x\to\tau>0\), fixed-order asymptotics give
\[
p_l(x)^n\longrightarrow
e^{-\tau l(l+2)/2}
=e^{-2\tau j(j+1)}.
\tag{WB15}
\]
The factorial majorant (WB9) is summable with every fixed polynomial weight in \(d\). Dominated convergence therefore upgrades the fixed-order statement to uniform convergence of kernels, and of every fixed number of group derivatives:
\[
h_{x,n}\longrightarrow h^{\mathrm{heat}}_{2\tau}.
\tag{WB16}
\]
On compact positive intervals of \(n/x\), the comparison with \(h^{\mathrm{heat}}_{2n/x}\) is uniform. Positive limiting minima also give operator-norm convergence of the one-factor prediction return: after whitening the endpoint law, the kernel of \(K_{x,n}\) is
\[
\frac{h_{x,n}(y^{-1}u)h_{x,n}(y^{-1}v)}
{\sqrt{h_{x,2n}(u^{-1}v)}},
\]
which converges uniformly on the compact triple carrier. This implies Hilbert--Schmidt convergence of \(K\), hence norm convergence of \(K^*K\).

None of this licenses a Gaussian envelope at finite \(x,n\). There \(w_l\sim l\log l\), so \(n w_l/[j(j+1)]\to0\). The exact one-boundary order \(P_x^{2n}\le S_{x,n}\) rules out \(S_{x,n}\le e^{-bL}\) for every \(b>0\). The correct finite-spacing cost in (WB12) remains \(W_{x,n}\). Nor does one-factor norm convergence imply a uniform norm approximation for an unbounded number of tensor factors; (WB13) is a separate uniform inequality.

## The remaining interacting problem

Temporal blocking changes a genuine path length, not the observation algebra. A physical interpretation still needs the independently calibrated relation among \(x\), temporal spacing and spatial coupling. Even the temporal-continuum limit with a fixed spatial regulator is not the four-dimensional Clay limit.

The magnetic sandwich changes the kernel and its Perron vacuum, and its powers are not products of blocked kinetic kernels. [[vacuum-aligned-innovation-completion/heat-envelopes-and-the-vacuum-vector|The vacuum obstruction]] remains in force. [[vacuum-aligned-innovation-completion/local-perron-oscillation-and-conditional-coercivity|Local Perron control]] supplies actual conditional-vacuum estimates and isolates the residual cross-block covariance; it does not yet supply the uniform interacting bridge floor.

[[receipts/wilson_fusion_blocking_receipt.py|The receipt]] checks the Bessel costs, fusion channels, rational constants, exact quaternion convolution, blocked-kernel convergence and selected bridge numerators. Finite calculations do not prove the infinite inequalities or the physical continuum construction.

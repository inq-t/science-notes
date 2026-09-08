# A Quartic State Produces an Off-Diagonal Sewing Defect

The first variation of a symmetrically balanced Gaussian proximity kernel has an explicit Hermite response. A quartic state deformation gives a nonzero composition defect between the first and third Hermite modes, which no scalar change of comparison duration can cancel. This is an exact obstruction in the linearized balance equations, and a conditional first-variation theorem for a balanced branch satisfying the stated weighted differentiability hypothesis. The separate Gaussian sewing rigidity theorem supplies the nonperturbative obstruction without that hypothesis.

**Status: exact linearized-balance calculation and exact finite Hermite matrix elements; conditional interpretation as the derivative of an actual unbounded quartic balancing branch.** Differentiability of that branch is not proved here. These are configuration-comparison operators, not an identified physical transfer direction or a Yang–Mills Hamiltonian.

## Fix the state, comparison width and common carrier

Let \(\gamma=N(0,1)\), and use probabilists' Hermites
\[
H_0=1,\quad H_1=x,\quad H_2=x^2-1,\quad
H_3=x^3-3x,\quad H_4=x^4-6x^2+3,
\qquad \langle H_m,H_n\rangle_\gamma=n!\delta_{mn}.
\tag{QT1}
\]
The positive number operator is \(N=-\partial_x^2+x\partial_x\). At width \(\epsilon=\sinh t\), \(t>0\), [[gaussian-overlap-balancing-and-clock-sewing|Gaussian endpoint balancing]] returns \(Q_t=e^{-tN}\), with \(Q_tH_n=e^{-nt}H_n\).

Perturb the state by
\[
d\mu_\lambda=\rho_\lambda\,d\gamma,\qquad
\rho_\lambda=\frac{e^{-\lambda V}}{\int e^{-\lambda V}\,d\gamma},
\quad V=H_4,\quad \lambda\ge0.
\tag{QT2}
\]
This is normalizable: \(H_4\ge-6\), with positive quartic leading term. It is already centered under \(\gamma\). More generally write \(V_c=V-\gamma(V)\). The state half-density obeys
\[
v_\lambda:=\sqrt{\rho_\lambda}
=1-\frac{\lambda}{2}V_c+o(\lambda)
\tag{QT3}
\]
in every Gaussian polynomial-weighted finite \(L^p\) norm. For this one-sided quartic family, domination follows from the lower bound on \(V\) and finite Gaussian moments. This state derivative needs no balancing theorem.

Keep the raw kernel \(\exp[-(x-y)^2/(4\sinh t)]\) fixed while changing \(\lambda\). If positive balancing factors \(a_{\lambda,t}\) exist, their operator acts on \(L^2(\mu_\lambda)\). Transport it to \(L^2(\gamma)\) by the unitary \(f\mapsto v_\lambda f\). Its kernel is
\[
\widetilde Q_{\lambda,t}(x,y)
=h_{\lambda,t}(x)Q_t(x,y)h_{\lambda,t}(y),
\qquad h_{\lambda,t}=\frac{a_{\lambda,t}}{a_{0,t}}v_\lambda.
\tag{QT4}
\]
Its normalized vacuum is \(v_\lambda\), not \(1\). Exact balance is equivalently
\[
h_{\lambda,t}Q_t(h_{\lambda,t}v_\lambda)=v_\lambda.
\tag{QT5}
\]

## State explicitly what differentiation requires

One sufficient hypothesis at each duration used below is the existence of \(d_t\) with all polynomial-weighted Gaussian \(L^2\) norms finite such that, for every integer \(M\ge0\),
\[
\int (1+|x|+|y|)^M
\left|
\frac{h_{\lambda,t}(x)h_{\lambda,t}(y)-1}{\lambda}
-d_t(x)-d_t(y)
\right|\,dR_t(x,y)\longrightarrow0,
\quad dR_t=d\gamma(x)Q_t(x,dy).
\tag{QT6}
\]
The limit is one-sided. This weighted kernel hypothesis justifies differentiating polynomial matrix elements and (QT5): \(v_\lambda\) is uniformly bounded above for small positive \(\lambda\), and (QT3) controls its derivative. No operator-norm differentiability is presumed.

For differentiation of \(\widetilde Q_{\lambda,t}\widetilde Q_{\lambda,s}\), also require the product rule on the tested Hermite vectors. It suffices that the difference quotients on every fixed Hermite polynomial converge strongly in \(L^2(\gamma)\) to the returned derivative. Contraction of the operators then gives strong convergence on the whole carrier and the two-factor product rule. These requirements have not been established here for the unbounded quartic balancing branch.

Without those hypotheses, the next equations remain a unique, exactly solvable linearized-balance problem. [[gaussian-sewing-rigidity|Gaussian sewing rigidity]] addresses exact composition separately, so the nonperturbative conclusion does not depend on promoting (QT6) to a theorem.

## The linearized balance fixes the endpoint response

Differentiating (QT5) against the Hermite core gives
\[
(I+Q_t)d_t=-\frac12(I-Q_t)V_c.
\tag{QT7}
\]
Since \(0\le Q_t\le I\), \(I+Q_t\) has a bounded inverse on \(L^2(\gamma)\). Hence
\[
\boxed{
d_t=-\frac12\frac{I-Q_t}{I+Q_t}V_c
=-\frac12\tanh(tN/2)V_c.}
\tag{QT8}
\]
If \(b_t\) denotes the corresponding logarithmic balancing-factor variation, \(b_t=d_t+V_c/2\), so
\[
b_t=(I+Q_t)^{-1}Q_tV_c.
\tag{QT9}
\]
The kernel derivative on the Hermite core is
\[
\boxed{\dot Q_t=M_{d_t}Q_t+Q_tM_{d_t}.}
\tag{QT10}
\]
For a quartic polynomial this defines a bounded operator at fixed \(t>0\): multiplication by \(H_4\) has finitely many Hermite diagonals with polynomially growing coefficients, while the adjoining \(Q_t\) supplies exponential decay. This bounded candidate does not prove differentiability of the nonlinear branch.

For \(V=H_4\), set \(r=e^{-t}\) and \(h(r)=(1-r^4)/(1+r^4)\). Then
\[
d_t=-\frac12h(r)H_4,\qquad
\langle H_m,\dot Q_tH_n\rangle_\gamma
=-\frac12h(r)(r^m+r^n)
\langle H_m,H_4H_n\rangle_\gamma.
\tag{QT11}
\]
The moving vacuum supplies a control:
\(\dot Q_t1=-\tfrac12(I-Q_t)H_4\).
This is the differentiated identity \(\widetilde Q_{\lambda,t}v_\lambda=v_\lambda\), not a normalization failure.

## A single off-diagonal entry detects failed sewing

Define
\[
\mathscr D_{t,s}
=\dot Q_{t+s}-\dot Q_tQ_s-Q_t\dot Q_s.
\tag{QT12}
\]
Under the product differentiability hypothesis, it is the derivative of the actual composition defect. For \(r=e^{-t}\), \(u=e^{-s}\), and \(C_{mn}=\langle H_m,H_4H_n\rangle_\gamma\),
\[
\begin{aligned}
\langle H_m,\mathscr D_{t,s}H_n\rangle_\gamma
=-\frac{C_{mn}}2\big[
&h(ru)((ru)^m+(ru)^n)\\
&-h(r)(r^m+r^n)u^n\\
&-h(u)r^m(u^m+u^n)\big].
\end{aligned}
\tag{QT13}
\]
The identity \(xH_3=H_4+3H_2\) gives \(C_{13}=24\). At \(t=s=\log2\), the actual widths are \(\epsilon(t)=3/4\) and \(\epsilon(2t)=15/8\). With \(h(1/2)=15/17\) and \(h(1/4)=255/257\),
\[
\boxed{
\langle H_1,\mathscr D_{t,t}H_3\rangle_\gamma
=\frac{8505}{8738}>0.}
\tag{QT14}
\]
For normalized Hermites \(e_n=H_n/\sqrt{n!}\), the entry is
\(2835\sqrt6/17476\).
The vacuum-to-fourth-mode entry vanishes exactly:
\(\langle H_0,\mathscr D_{t,t}H_4\rangle=0\).
A correct vacuum tangent alone would miss the obstruction.

Allow any scalar first-order clock correction
\(\tau_\lambda(t)=t+\lambda\alpha(t)+o(\lambda)\).
Its additional derivative is \(-\alpha(t)NQ_t\), and its change to the defect is
\[
-[\alpha(t+s)-\alpha(t)-\alpha(s)]NQ_{t+s}.
\tag{QT15}
\]
This is Hermite-diagonal and cannot cancel (QT14). In one dimension a scalar cometric adjustment only changes the width and is included in this test. The \(H_4\) deformation also leaves the variance unchanged to first order, since \(\gamma(x^2H_4)=0\).

A common Hilbert-space presentation change cannot repair an actual composition defect: it conjugates the complete defect. Infinitesimally, a duration-independent conjugation contributes \([B,Q_t]\), whose contributions to (QT12) cancel by the unperturbed semigroup law.

## The witness also detects a joint interaction

For \(V=x^4/4\), the centered perturbation is
\[
V_c=\frac14H_4+\frac32H_2.
\tag{QT16}
\]
The \(H_2\) contribution to the \(1,3\) defect vanishes: its degree separation is two, and substituting \(h_2(r)=(1-r^2)/(1+r^2)\) into (QT13) gives zero. The quartic contribution remains, giving \(8505/34952\). Subtracting a constant from a potential does not affect its normalized state.

On two independent standard Gaussian coordinates, instead take \(V=H_2(x)H_2(y)\). For \(0\le\lambda<1/2\) its perturbed density is normalizable, since the full exponent is
\[
(1/2-\lambda)(x^2+y^2)+\lambda x^2y^2+\lambda.
\tag{QT17}
\]
This genuinely joint perturbation is centered, leaves every covariance entry unchanged to first order, and has total Hermite degree four. Between \(H_1(x)H_0(y)\) and \(H_1(x)H_2(y)\), the multiplication coefficient is
\[
\gamma(x^2H_2(x))\,\gamma(H_2(y)^2)=2\cdot2=4.
\]
The total degrees are again one and three, so at \(t=s=\log2\) the unnormalized defect is \(2835/17476>0\). The scalar-clock exclusion and conditional status are the same. Unlike the one-dimensional \(H_4\), this potential is not bounded below. For this example, require (QT6) with an additional weight \(e^{\delta(|z|^2+|z'|^2)}\), where \(z=(x,y)\) and \(\delta>0\) is sufficiently small for Gaussian integrability, together with the stated strong product differentiability. The estimate \(v_\lambda(z)\le C_\lambda e^{\lambda|z|^2/2}\) then supplies the required domination for small \(\lambda\). This stronger hypothesis is also not proved here.

## The next construction must change more than endpoint weights

The calculation identifies the missing channel: endpoint balancing preserves the state but cannot supply the off-diagonal terms required by exact composition of the fixed Gaussian proximity family. An interaction-sensitive replacement must change the comparison family or retain additional boundary information with a controlled composition defect. Taking the desired interacting heat kernel as the starting comparison would encode the requested clock as input.

[[gaussian-sewing-rigidity|The nonperturbative rigidity theorem]] supplies the stronger exact restriction under its stated positivity and integrability hypotheses. The tangent identifies the first missing Hermite channel for testing a proposed correction. Such a correction still has to be compared with [[coarse-response-memory/correlated-interface-tangent|the actual interacting plaquette response]], rather than interpreting this comparison clock as physical Euclidean transfer.

[[receipts/quartic_overlap_sewing_receipt.py|The quartic sewing receipt]] uses conditional Gaussian polynomial integration to check linearized balance, the moving vacuum, the nonzero defect, its zero controls, and immunity to scalar clock correction. Its arithmetic proves the displayed finite coefficients, not existence or differentiability of an infinite-dimensional balancing branch.

---
inq.module: "coarse-response-memory"
inq.include:
  - "**/*.md"
  - "**/*.py"
---
# Coarse Response Memory

Removing hidden variables from an evolution does not generally produce another autonomous evolution on the retained variables. It produces a frequency-dependent response: the hidden sector can receive a disturbance, retain it, and return it later. The static least-cost response is only its zero-frequency limit. This distinction gives both a quantitative gap criterion and an explicit example where an apparently fast local rate misses a slow physical mode.

**Status: [EXACT] for the stated self-adjoint block setting and finite reversible example; [CONDITIONAL] for a physical application supplying that block decomposition and uniform estimates; [OPEN] for the Yang--Mills continuum construction or a cosmological realization.** No assumption about fundamental randomness is made.

## What the operator operates on

Let \(\mathcal H\) be a Hilbert space of variations, with a specified nonnegative self-adjoint generator \(L\). A chosen readout is an isometry \(J:\mathcal H_R\to\mathcal H\). Write
\[
P=JJ^*,\qquad Q=I-P,\qquad
\mathcal H=\mathcal H_R\oplus\mathcal H_H,\qquad
L=\begin{pmatrix}A&B^*\\B&C\end{pmatrix}.
\tag{CM1}
\]
Thus \(B:\mathcal H_R\to\mathcal H_H\) carries a retained variation into its hidden response, and \(B^*\) carries a hidden response back. These are maps of variations, not maps selecting measurement outcomes.

For the theorem below assume \(A,C\ge0\) self-adjoint, \(B\) bounded, and \(D(L)=D(A)\oplus D(C)\). Every bounded nonnegative \(L\) with an orthogonal readout satisfies this setting. An unbounded field generator with a general conditional expectation need not: projection invariance of its form domain and the off-diagonal extension must be checked.

For a reversible Markov law \(\mu\) and measurable readout \(r\), the canonical example is
\[
\mathcal H=L^2(\mu),\quad
\mathcal H_R=L^2(r_*\mu),\quad Jf=f\circ r.
\tag{CM2}
\]
Here \(P\) is conditional expectation onto the readout algebra. For a spectral-gap statement, remove the actual vacuum first, retain its orthogonal complement, and require that the readout preserve the vacuum splitting. A chosen reference constant is not automatically the physical vacuum.

## Eliminating the hidden evolution leaves a memory kernel

Let \(R_t=J^*e^{-tL}J\). Starting from \((f,0)\), the block equations are
\[
\dot x=-Ax-B^*y,\qquad
\dot y=-Bx-Cy,\qquad x(0)=f,\quad y(0)=0.
\]
Variation of constants gives
\[
y(t)=-\int_0^t e^{-(t-s)C}Bx(s)\,ds.
\]
Consequently
\[
\boxed{\dot R_t=-AR_t+\int_0^t M(t-s)R_s\,ds,\qquad
M(t)=B^*e^{-tC}B,\qquad R_0=I.}
\tag{CM3}
\]
The derivative equation holds on the generator domain; the corresponding integrated mild equation holds on all retained vectors. For nonzero initial hidden data \(y_0\), add the forcing \(-B^*e^{-tC}y_0\). A statistical treatment of that forcing requires a state or preparation law; the algebra does not declare it ontically random.

For real \(z>0\), its Laplace transform is the exact Schur resolvent
\[
\boxed{\widehat R(z)=J^*(z+L)^{-1}J
=\big[z+A-\Sigma(z)\big]^{-1},\qquad
\Sigma(z)=B^*(z+C)^{-1}B.}
\tag{CM4}
\]
This follows either by eliminating the hidden block of \(z+L\) or by transforming (CM3). It is an operator identity, not a fitted memory ansatz. If \(\mathsf E_C\) is the spectral measure of \(C\), the same hidden response measure determines
\[
M(t)=\int e^{-t\lambda}\,B^*d\mathsf E_C(\lambda)B,\qquad
\Sigma(z)=\int\frac{B^*d\mathsf E_C(\lambda)B}{z+\lambda}.
\tag{CM5}
\]
In particular \(M(t)\ge0\), and the derivatives of \(\Sigma\) alternate in operator order. This positivity concerns response on a Hilbert space, not pointwise positivity of every matrix entry.

[[library/optimal-prediction-and-the-mori-zwanzig-representation-of-irreversible-processes/inq|Chorin, Hald and Kupferman]] give the projection/Dyson memory construction in a more general dynamical setting. Equations (CM3)--(CM5) are the explicit self-adjoint specialization proved here, not a new attribution of a Wilson estimate to that source.

## Zero frequency and the first retained metric

Suppose \(C\ge c_HI\) for \(c_H>0\). The symbol \(c_H\) is a hidden-generator bound, not the speed of light. Define
\[
S=A-B^*C^{-1}B,\qquad
Z_0=I+B^*C^{-2}B.
\tag{CM6}
\]
The static short \(S\) minimizes the whole quadratic form over hidden representatives:
\[
\langle(x,y),L(x,y)\rangle
=\langle x,Sx\rangle+
\|C^{1/2}(y+C^{-1}Bx)\|^2.
\tag{CM7}
\]
[[trace-dirichlet-descent/inq|Trace Dirichlet descent]] owns this least-cost construction and its distinction from the pullback \(A\). Neither \(S\) nor \(A\) is generally the generator of \(R_t\).

The new metric has an exact geometric meaning. The harmonic lift is \(h x=(x,-C^{-1}Bx)\), so \(h^*Lh=S\) as a form and \(h^*h=Z_0\). Thus the whole norm of a least-cost representative is \(\langle x,Z_0x\rangle\), not \(\|x\|^2\). Its Rayleigh quotient is \(\langle x,Sx\rangle/\langle x,Z_0x\rangle\). Restricting to this harmonic graph does not find the full spectrum, but it explains why a static response must be paired with an induced norm before being read as a rate.

The first frequency correction is a positive metric, not another arbitrary scalar rate. Spectral calculus gives, for real \(z\ge0\),
\[
\begin{aligned}
z+A-\Sigma(z)&=S+zZ_0-\mathcal R(z),\\
\mathcal R(z)&=z^2B^*C^{-2}(C+z)^{-1}B,\\
0\le\mathcal R(z)&\le\frac{z^2}{c_H+z}(Z_0-I).
\end{aligned}
\tag{CM8}
\]
Thus \(S+zZ_0\) is a controlled low-frequency response denominator when \(z/c_H\) is small. This is not yet a uniform error bound for its inverse or for long-time trajectories: inverse estimates also require distance from the relevant spectrum.

The same denominator continued to \(z=-E\), for \(0<E<c_H\), is
\[
A-E-B^*(C-E)^{-1}B.
\tag{CM9}
\]
Its singularities detect retained spectral modes. A static positive number from \(S\) is therefore not, by itself, their physical decay exponent.

## A sharp three-quantity lower bound

On the complete nonvacuum splitting, assume
\[
C\ge c_HI,\qquad S\ge sI,\qquad
k=\|C^{-1}B\|<\infty,\qquad c_H,s>0.
\tag{CM10}
\]
Then
\[
\boxed{
L\ge\delta I,\qquad
\delta=\frac{s+c_H+c_Hk^2-\sqrt{(s+c_H+c_Hk^2)^2-4sc_H}}2>0.}
\tag{CM11}
\]
To prove this when \(k>0\), test \(L-\delta I\) by its hidden Schur complement. Put \(D=C^{-1}B\). For \(0<\delta<c_H\),
\[
\begin{aligned}
A-\delta-B^*(C-\delta)^{-1}B
&=S-\delta-\delta D^*C(C-\delta)^{-1}D\\
&\ge\left[s-\delta-\frac{\delta c_H k^2}{c_H-\delta}\right]I.
\end{aligned}
\]
The smaller root in (CM11) makes the last bracket zero. If \(k=0\), the blocks decouple and the bound is \(\min(s,c_H)\). The scalar blocks \(C=c_H,\ B=c_Hk,\ A=s+c_Hk^2\) attain (CM11), so the bound cannot be improved using only these three quantities.

Equivalently,
\[
\frac{\delta}{c_H}
=\frac{r+1+k^2-\sqrt{(r+1+k^2)^2-4r}}2,\qquad r=s/c_H.
\tag{CM12}
\]
This is the useful quotient: static retained stiffness and hidden relaxation must be compared together with their coupling. Under \(L\mapsto aL\), \(r,k,\delta/c_H\) are unchanged. Geometry may constrain those dimensionless relations; it does not thereby select the dimensional clock.

The scalar root is the existing [[contemporary-puzzles/yang-mills-mass-gap/two-scale-rg-descent-and-the-crossover-lemma#A conditional-Fisher version for Poincare bounds|two-scale Fisher budget]] with \((\rho,\lambda,C_{\mathrm{Fisher}})=(c_H,s,c_Hk^2)\), not a new numerical constant. The additional content here is its operator-memory interpretation and the positive metric \(Z_0\). It assumes estimates for \(S,C,B\); positivity or elimination alone supplies none of the required uniform constants.

There is also a direct static-approximation check. Since
\(0\le\Sigma(0)-\Sigma(z)\le zk^2I\), inverse order gives
\[
[(1+k^2)z+S]^{-1}\le\widehat R(z)\le[z+S]^{-1},
\qquad
\|\widehat R(z)-(z+S)^{-1}\|
\le\frac{zk^2}{(z+s)^2}.
\tag{CM12a}
\]
The norm estimate follows by the resolvent identity. These are resolvent bounds, not pointwise bounds between exponential semigroups: the exponential is not operator monotone.

## A fast instantaneous rate with a slow observable tail

Consider the symmetric three-state chain, in orthonormal coordinates for its uniform stationary Hilbert space,
\[
L_\varepsilon=
\begin{pmatrix}
1&-1&0\\
-1&1+\varepsilon&-\varepsilon\\
0&-\varepsilon&\varepsilon
\end{pmatrix},\qquad \varepsilon>0.
\tag{CM13}
\]
Retain only whether the state is \(1\) or in \(\{2,3\}\). The normalized centered retained and hidden vectors are
\[
f=(2,-1,-1)/\sqrt6,\qquad h=(0,1,-1)/\sqrt2.
\]
On the centered space,
\[
A=\frac32,\quad B=-\frac{\sqrt3}{2},\quad
C=\frac12+2\varepsilon,\quad
S=\frac{6\varepsilon}{1+4\varepsilon}.
\tag{CM14}
\]
The exact centered return is
\[
\begin{aligned}
r_\varepsilon(t)&=\alpha e^{-\lambda_-t}+(1-\alpha)e^{-\lambda_+t},\\
\lambda_\pm&=1+\varepsilon\pm\sqrt{1-\varepsilon+\varepsilon^2},\\
\alpha&=\frac{\lambda_+-3/2}{\lambda_+-\lambda_-}.
\end{aligned}
\tag{CM15}
\]
As \(\varepsilon\downarrow0\), the actual gap is \(\lambda_-\sim3\varepsilon/2\), with retained weight \(\alpha\to1/4\), although \(A=3/2\) never changes. The static short behaves as \(6\varepsilon\); dividing by \(Z_0\to4\) recovers the leading slow exponent. Formula (CM11) is exact in this scalar block example.

Each full-space readout compression is reversible and Markov, but its family is not a semigroup:
\[
r_\varepsilon(2t)-r_\varepsilon(t)^2
=\alpha(1-\alpha)
\big(e^{-\lambda_-t}-e^{-\lambda_+t}\big)^2>0
\tag{CM16}
\]
for \(t>0\). A smaller state space did not eliminate the physical slow mode; it placed that mode in a memory-dependent return.

## Use the physical bounded defect when domains are difficult

For an actual positive injective physical transfer
\[
T_\tau=e^{-\tau(H-E_0)/\hbar},\qquad L=I-T_\tau,
\tag{CM17}
\]
all blocks in (CM1) are bounded. If (CM10) is proved for this \(L\) on the full physical vacuum complement, then (CM11) gives, for \(0<\delta<1\),
\[
H-E_0\ge-\frac{\hbar}{\tau}\log(1-\delta)\,Q_{\mathrm{vac}}.
\tag{CM18}
\]
Here \(e^{-tL}\) is an auxiliary bounded-defect evolution, not physical clock time. The physical conclusion follows from functional calculus of the supplied \(T_\tau\), not from renaming the memory parameter. If the slab is calibrated by length \(\ell=c\tau\), replace \(\hbar/\tau\) by \(\hbar c/\ell\).

This gives a domain-safe operator signature for the next Yang--Mills estimate: a derived readout, a hidden defect floor \(c_H\), a retained short floor \(s\), and a bounded return coupling \(k\), all controlled along the actual continuum trajectory. The [[temporal-column-response/spatial-elimination-and-self-return|static column comparison]] is a different estimate on conditional laws; it does not supply these physical blocks.

Nothing in the construction privileges large or small systems. A cosmological application would still need its own state, readout and evolution before the same response signature could be compared with the vacuum one. [[global-local-response-reconstruction/cosmological-reconvergence-contract|Cosmological reconvergence]] owns that additional common-source requirement.

[[coarse-response-memory/receipts/coarse_response_memory_receipt.py|The finite receipt]] checks the block resolvent, memory equation, frequency remainder, sharp gap bound and full three-state conditional readout. It tests algebraic calibrations, not the missing continuum estimates.

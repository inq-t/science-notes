# Unbounded Projection Cycles Inherit Their Entire Spectrum

A triangle of closed operator graphs produces a dissipative evolution and a positive unitary generator on an infinite-dimensional carrier. The construction works for every nonnegative self-adjoint operator, including operators with continuous spectrum and no gap. It therefore extends the analytic scope of [[oriented-projection-cycles-and-joint-response|oriented projection cycles]] while identifying their remaining freedom exactly: the spectrum is encoded in the input graph, not selected by the projection protocol. The extension also distinguishes strong convergence, positive-time norm convergence, and the domain on which a finite loss rate exists.

**Status: [EXACT FUNCTIONAL-CALCULUS CONSTRUCTION]; [OPEN] a principle selecting the input operator or forcing a positive excitation threshold.** No novelty is claimed for closed-operator graph projections, polar decomposition, or the spectral-calculus arguments below.

## A closed response and its three comparison spaces

Let \(V,N\) be complex Hilbert spaces and let

\[
D:\operatorname{Dom}D\subset V\longrightarrow N
\]

be densely defined and closed. Then \(T=D^*D\) is nonnegative and self-adjoint, with

\[
\operatorname{Dom}T^{1/2}=\operatorname{Dom}D,\qquad
\|T^{1/2}v\|=\|Dv\|.
\tag{UP1}
\]

In \(\mathcal K=V\oplus N\), write \(\iota v=(v,0)\), \(P_0=\iota\iota^*\), and let \(P_D(\epsilon)\), \(P_{iD}(\epsilon)\) project onto the closed graphs of \(\epsilon D\), \(i\epsilon D\). For \(\delta=\epsilon^2>0\), the ordered returned cycle is

\[
C_\delta=\iota^*P_0P_{iD}(\epsilon)P_D(\epsilon)\iota.
\tag{UP2}
\]

The closed operator, complex structure, quarter-turn \(D\mapsto iD\), comparison order, and duration assignment \(\delta=\epsilon^2\) are inputs. Reversing the cycle will reverse its phase. No spacetime interpretation of \(\delta\) is assumed.

Put \(R_\delta=(I+\delta T)^{-1}\). The maps

\[
J_D=
\begin{pmatrix}R_\delta^{1/2}\\ \epsilon D R_\delta^{1/2}\end{pmatrix},
\qquad
J_{iD}=
\begin{pmatrix}R_\delta^{1/2}\\ i\epsilon D R_\delta^{1/2}\end{pmatrix}
\tag{UP3}
\]

are bounded isometries from \(V\) onto the two graphs. Indeed, \(R_\delta^{1/2}\) maps \(V\) onto \(\operatorname{Dom}D\), and
\(\|R_\delta^{1/2}v\|^2+\delta\|DR_\delta^{1/2}v\|^2=\|v\|^2\).
Thus the graph projections are \(J_DJ_D^*\), \(J_{iD}J_{iD}^*\). Their overlap is the bounded spectral function

\[
J_{iD}^*J_D=(I-i\delta T)R_\delta.
\]

Multiplication gives the exact returned operator

\[
\boxed{C_\delta=(I-i\delta T)(I+\delta T)^{-2}
=c(\delta T),\qquad c(x)=\frac{1-ix}{(1+x)^2}.}
\tag{UP4}
\]

Every expression in (UP3–4) denotes its bounded spectral-calculus realization; no undefined product \(D^*D\) on an arbitrary vector has been used. In particular, \(C_\delta\) is an everywhere-defined normal contraction.

## Polar return and the domains of the generators

For finite \(x\ge0\), \(c(x)\ne0\). Consequently \(C_\delta\) is injective and has dense range. If \(T\) is unbounded, \(|c(\delta\lambda)|\to0\) along its high spectrum, so \(C_\delta\) does not have a bounded inverse. Nevertheless its polar factor is the everywhere-defined unitary

\[
\boxed{U_\delta=(I-i\delta T)(I+\delta^2T^2)^{-1/2}
=e^{-i\arctan(\delta T)}.}
\tag{UP5}
\]

The formal expression \(C_\delta|C_\delta|^{-1}\) initially acts only on \(\operatorname{Ran}|C_\delta|\); (UP5) is its continuous extension. Bounded invertibility, used in the finite-dimensional calculation, is not required.

On \(\operatorname{Dom}T\),

\[
\frac{I-C_\delta}{\delta}v\longrightarrow(2+i)Tv,
\qquad
\frac{I-U_\delta}{\delta}v\longrightarrow iTv.
\tag{UP6}
\]

For the first assertion,

\[
\frac{1-c(\delta\lambda)}{\delta}
=\lambda\,\frac{2+i+\delta\lambda}{(1+\delta\lambda)^2}
\longrightarrow(2+i)\lambda,
\]

with modulus bounded by a constant times \(\lambda\). For the second, use
\(\left|1-e^{-i\arctan x}\right|\le\arctan x\le x\).
Spectral dominated convergence proves both assertions. The limiting raw generator is \(-(2+i)T\), with domain \(\operatorname{Dom}T\); the returned unitary group has self-adjoint generator \(T\) on the same domain. Its positivity follows from the particular graph choice \(B=iD\), not from ordering alone.

## Exact strong limits and the different norm limits

For \(n_\delta(t)=\lfloor t/\delta\rfloor\),

\[
\boxed{
C_\delta^{n_\delta(t)}\longrightarrow e^{-(2+i)tT}
\quad(t\ge0),\qquad
U_\delta^{n_\delta(t)}\longrightarrow e^{-itT}
\quad(t\in\mathbb R).
}
\tag{UP7}
\]

Both limits are strong and uniform on compact intervals in their stated time ranges. Negative powers in the second expression are well defined because \(U_\delta\) is unitary.

**Proof.** For every fixed \(\lambda\ge0\),

\[
\log c(\delta\lambda)=-(2+i)\delta\lambda+O(\delta^2\lambda^2),
\qquad
\arctan(\delta\lambda)=\delta\lambda+O(\delta^3\lambda^3).
\]

These expansions are uniform for \(\lambda\) in a bounded interval. Hence both limits hold uniformly in \(t\) on compact intervals on each bounded spectral subspace \(E_T([0,R])V\). All powers in (UP7) have norm at most one. For an arbitrary \(v\), the remaining error is at most \(2\|E_T((R,\infty))v\|\), uniformly in \(t,\delta\). First choose \(R\), then let \(\delta\downarrow0\). This proves the strong assertions. \(\square\)

The raw convergence is stronger away from zero:

\[
\sup_{a\le t\le b}
\left\|C_\delta^{n_\delta(t)}-e^{-(2+i)tT}\right\|
\longrightarrow0
\qquad(0<a\le b<\infty).
\tag{UP8}
\]

To prove this without a bounded-spectrum assumption, use
\[
|c(x)|=\frac{\sqrt{1+x^2}}{(1+x)^2}\le\frac1{1+x}.
\]
For \(\lambda\ge R\), \(\delta\le1/R\), and \(\delta\le a/2\), one has \(n_\delta(t)\ge a/(2\delta)\), giving
\[
|c(\delta\lambda)|^{n_\delta(t)}
\le(1+\delta R)^{-a/(2\delta)}
\le e^{-aR/4}.
\]
The limiting exponential is bounded there by \(e^{-2aR}\). Low-spectrum convergence is uniform, and both high-spectrum bounds can be made arbitrarily small by increasing \(R\). This proves (UP8).

For unbounded \(T\), uniform raw norm convergence on a time interval containing zero fails. At \(t=\delta/2\) there are zero repetitions, whereas
\[
\left\|I-e^{-(2+i)\delta T/2}\right\|\ge1
\tag{UP9}
\]
because the spectral multiplier of the exponential tends to zero along the unbounded spectrum.

Polar convergence can fail in norm even at every fixed positive time. Take \(T=M_\lambda\), multiplication by \(\lambda\) on \(L^2(\mathbb R_+,d\lambda)\). For every \(t,\delta>0\),

\[
\boxed{\left\|U_\delta^{n_\delta(t)}-e^{-itT}\right\|=2.}
\tag{UP10}
\]

Indeed, the phase difference
\[
f(\lambda)=t\lambda-n_\delta(t)\arctan(\delta\lambda)
\]
is continuous, starts at zero, and tends to \(+\infty\). It therefore attains an odd multiple of \(\pi\). Continuity gives positive-measure neighborhoods with multiplier difference arbitrarily close to two, establishing the essential supremum. This is compatible with the strong convergence in (UP7). It is a counterexample to general fixed-time norm convergence, not a claim about every possible unbounded discrete spectrum.

## The finite-loss domain is exactly the form domain

For \(x_0=\iota v\), set \(x_1=P_Dx_0\), \(x_2=P_{iD}x_1\), \(x_3=P_0x_2\). As in the finite construction, the residue map
\[
\mathcal D_\epsilon v=(x_0-x_1,x_1-x_2,x_2-x_3)\in\mathcal K^{\oplus3}
\]
satisfies
\(\mathcal D_\epsilon^*\mathcal D_\epsilon=I-C_\delta^*C_\delta\).
Define the bounded nonnegative loss form

\[
\ell_\delta[v]=\frac{\|v\|^2-\|C_\delta v\|^2}{\delta}.
\]

If \(\mu_v(B)=\langle v,E_T(B)v\rangle\), then

\[
\ell_\delta[v]=\int_0^\infty \lambda g(\delta\lambda)\,d\mu_v(\lambda),
\qquad
g(x)=\frac{4+5x+4x^2+x^3}{(1+x)^4}.
\tag{UP11}
\]

This follows by expanding
\(1-|c(x)|^2=xg(x)\).
Moreover,

\[
g(0)=4,\qquad
g'(x)=-\frac{11+7x+5x^2+x^3}{(1+x)^5}<0.
\]

Thus the forms increase as \(\delta\downarrow0\), and monotone convergence gives the exact extended-valued limit

\[
\boxed{
\ell_\delta[v]\uparrow
\begin{cases}
4\|Dv\|^2,&v\in\operatorname{Dom}D,\\
+\infty,&v\notin\operatorname{Dom}D.
\end{cases}}
\tag{UP12}
\]

The limiting closed quadratic form is therefore \(4T\), with form domain \(\operatorname{Dom}D\), not operator domain \(\operatorname{Dom}T\). A finite loss rate is not automatic for every Hilbert vector.

There is also convergence of the residue vectors themselves. With each normal component placed in its own slot,

\[
\epsilon^{-1}\mathcal D_\epsilon v
\longrightarrow
\bigl((0,-Dv),(0,(1-i)Dv),(0,iDv)\bigr),
\qquad v\in\operatorname{Dom}D.
\tag{UP13}
\]

For a direct check, \(x_1=(R_\delta v,\epsilon DR_\delta v)\) and
\(x_2=(C_\delta v,i\epsilon DC_\delta v)\).
Both \(DR_\delta v\) and \(DC_\delta v\) tend to \(Dv\) on \(\operatorname{Dom}D\). The upper components divided by \(\epsilon\) tend to zero: their spectral multipliers are
\(\sqrt\delta\,\lambda/(1+\delta\lambda)\) and
\((1+i)\sqrt\delta\,\lambda/(1+\delta\lambda)^2\).
After extracting \(\sqrt\lambda\), the remaining factors are bounded and tend pointwise to zero. Spectral dominated convergence proves (UP13). Its squared norm is \(4\|Dv\|^2\), in agreement with (UP12).

The residue slots provide exact norm accounting. They are not automatically measurement records or an entropy-production functional. Retaining them gives an isometric enlargement; forgetting them is a specified readout. Even when \(T\) is unbounded, the returned cycle remains injective.

## Unbounded graphs are not uniformly nearby

The projections approach \(P_0\) strongly as \(\epsilon\downarrow0\). They do not approach it in operator norm when \(D\) is unbounded:

\[
\boxed{\|P_D(\epsilon)-P_0\|^2
=\left\|\delta T(I+\delta T)^{-1}\right\|=1.}
\tag{UP14}
\]

For example, the square of \(P_D-P_0\) is block diagonal, with upper block \(I-R_\delta\) and lower block
\(\delta DD^*(I+\delta DD^*)^{-1}\). Their nonzero spectral ranges agree, giving the norm identity. Strong convergence follows from the bounded graph-projection blocks and spectral dominated convergence.

Consequently, the finite-dimensional operator-norm Taylor expansion is not a uniform argument for this extension. The strong spectral limit and the form-domain calculation above replace it. Likewise, an ambient evolution preceded by \(P_0\) does not become strongly continuous at zero on the discarded normal space; the returned carrier here is \(V\).

## Every positive spectrum can be encoded

For any nonnegative self-adjoint operator \(T\) on \(V\), choose \(N=V\) and \(D=T^{1/2}\). Equations (UP4–13) then realize exactly

\[
\text{raw exponent operator }(2+i)T,\qquad
\text{polar generator }T,\qquad
\text{limiting loss form }4T.
\tag{UP15}
\]

No restriction on spectral type or a positive threshold was used. For a concrete comparison on one carrier, let

\[
V=\mathbb C\Omega\oplus L^2(\mathbb R_+,d\lambda),\qquad
T_g=0\oplus M_{\lambda+g},\qquad g\ge0.
\tag{UP16}
\]

Every \(T_g\) has the one-dimensional kernel \(\mathbb C\Omega\), with unbounded continuous excitation spectrum \([g,\infty)\). The same construction therefore admits both a gapless member \(g=0\) and any chosen positive gap \(g>0\). The common line is an explicitly supplied zero mode; it has not been derived as a vacuum.

This is an analytic realization theorem, not a spectrum-selection theorem. With \(D\), its closed domain, and the ordered comparison rule fixed, the loss and phase cannot be retuned independently. But choosing \(D=T^{1/2}\) can encode an arbitrary desired positive generator in advance. A further principle must select that input geometry, its domain and its behavior under refinement. The positivity in this control does not by itself identify \(T\) with a field Hamiltonian or with the joint mass invariant of [[contemporary-puzzles/yang-mills-mass-gap/mass-as-casimir-and-realization|the mass-Casimir construction]].

[[directed-analytic-realization/projection_cycle_receipt.py|The projection-cycle receipt]] includes a spectral quadrature check for \(T=M_\lambda\) and a vector with spectral density \(e^{-\lambda}\). It separately locates spectral values where the polar approximation differs from the limiting group by two. The quadrature illustrates strong convergence for that vector, not operator-norm convergence or control of all vectors.

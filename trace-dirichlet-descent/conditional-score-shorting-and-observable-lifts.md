# Conditional Score Shorting and Observable Lifts

A conditional score field has an associative whole-to-local dual: retain its ranges, average its Fisher forms, and obtain the inverse response by minimizing over compatible finer responses. In a finite frame experiment the minimizing response is realized by one actual Gaussian observable through every cut. This does not identify that variance quotient with a pointwise diffusion form. Scalarizing before dualization, dualizing over a retained boundary, and resolving every frame give three different closed clocks; compatibility with normalized restriction distinguishes these prescriptions when the permitted boundary sectors are declared.

**Status: [EXACT] for finite conditional score geometry, singular shorting, observable lifts and the stated Gaussian generators; [OPEN] for a noncommutative boundary version, selection of the state and transformations, and a Yang--Mills physical realization.** The inputs below are a statistical state and its transformation family, not a spacetime or a Hamiltonian.

## A frame experiment supplies its entropy and score

Let \(B,R\in\{-1,1\}\) be independent with means \(a,b\in(-1,1)\), and let \(W\) be an independent standard Gaussian. Their law is
\[
\mu=\pi_a\otimes\pi_b\otimes\gamma,
\qquad \pi_a(B)=\frac{1+aB}{2}.
\]
Declare the additive transformation
\[
T_\theta(B,R,W)=(B,R,W+\theta_L+BR\theta_R),
\qquad \ell_{BR}=\binom{1}{BR}.
\tag{CS1}
\]
The frame probabilities are independent of \(\theta\). These boundary variables are therefore ancillary for this experiment; there is no omitted central-weight score. The actual pushed law satisfies
\[
\frac{d\mu_\theta}{d\mu}
=\exp\left((\ell^T\theta)W-\tfrac12(\ell^T\theta)^2\right),
\qquad
D(\mu_\theta\Vert\mu)=\tfrac12\theta^T I_0\theta.
\tag{CS2}
\]
Its score is the random column \(s=W\ell\). Conditioning its Gram matrix on successively exposed frames gives
\[
I_0=\begin{pmatrix}1&ab\\ab&1\end{pmatrix},\qquad
I_B=\begin{pmatrix}1&Bb\\Bb&1\end{pmatrix},\qquad
I_{BR}=\ell\ell^T,
\tag{CS3}
\]
with \(I_0=\mathbb E I_B\) and \(I_B=\mathbb E[I_{BR}\mid B]\). The last matrix has rank one, not two. Its admissible response covectors lie in \(\mathbb R\ell\); its pseudoinverse is \(I_{BR}^{+}=\ell\ell^T/4\).

The relative-frame transformation \(D_B=\operatorname{diag}(1,B)\) obeys
\[
D_B I_BD_B=\begin{pmatrix}1&b\\b&1\end{pmatrix}.
\tag{CS4}
\]
It removes dependence on the earlier frame without changing the remaining increment law. For independent increments \(R_1,R_2\) with means \(b_1,b_2\), replace \(BR\) by \(BR_1R_2\). Conditioning at the intermediate frame \(C=BR_1\) gives an off-diagonal entry \(Cb_2\); averaging over \(R_1\) gives \(Bb_1b_2\). Multiplication of frames and the conditional-expectation tower supply an exact composition law before inversion.

This is a finite instance of [[program-core/center-valued-response|center-valued response and scalarization]]. Its fixed affine parameter space also gives the explicit conditional quadratic potential \(\theta^TI_B\theta/2\); no general center-valued Hessian structure is being inferred from a name.

## Singular conditional shorting

Let \(\mathcal Z\subseteq\mathcal Y\) be finite sigma-algebras with positive atom probabilities. Let \(I_{\mathcal Y}\) be a positive semidefinite matrix field and put
\[
I_{\mathcal Z}=\mathbb E[I_{\mathcal Y}\mid\mathcal Z].
\]
For a \(\mathcal Y\)-measurable covector field \(\eta\), define
\[
q_{\mathcal Y}(\eta)=\eta^TI_{\mathcal Y}^{+}\eta
\quad\hbox{if }\eta\in\operatorname{Ran}I_{\mathcal Y},
\qquad q_{\mathcal Y}(\eta)=+\infty\hbox{ otherwise}.
\tag{CS5}
\]
The range condition is essential. Assigning zero cost to arbitrary null-direction covectors with a bare pseudoinverse would change the quotient.

For a \(\mathcal Z\)-measurable field \(u\in\operatorname{Ran}I_{\mathcal Z}\), the exact conditional identity is
\[
\boxed{
u^TI_{\mathcal Z}^{+}u
=\min_{\mathbb E[\eta\mid\mathcal Z]=u}
\mathbb E[q_{\mathcal Y}(\eta)\mid\mathcal Z],
\qquad
h_{\mathcal Y\leftarrow\mathcal Z}u
=I_{\mathcal Y}I_{\mathcal Z}^{+}u.
}
\tag{CS6}
\]
The minimizing field is unique among range-admissible fields. This is a finite conditional instance of [[inq|infimal response descent]], not a new definition of an inverse matrix.

**Proof.** Within each coarse atom, positivity implies
\(\ker I_{\mathcal Z}\subseteq\ker I_{\mathcal Y}\) on every finer atom: a zero quadratic average is an average of nonnegative terms. Thus finer ranges lie in the coarse range. The displayed lift has conditional mean \(u\), belongs to each finer range, and has cost \(u^TI_{\mathcal Z}^{+}u\). For any admissible \(\eta\) with the same mean, expansion gives the exact residue
\[
\mathbb E[q_{\mathcal Y}(\eta)\mid\mathcal Z]
-u^TI_{\mathcal Z}^{+}u
=\mathbb E\left[
(\eta-hu)^TI_{\mathcal Y}^{+}(\eta-hu)
\mid\mathcal Z\right].
\tag{CS7}
\]
The cross term vanishes by the mean constraint. The pseudoinverse is strictly positive on its range, giving uniqueness. For three nested finite contexts \(\mathcal Z\subseteq\mathcal Y\subseteq\mathcal X\), range inclusion also gives
\[
\boxed{
h_{\mathcal X\leftarrow\mathcal Y}
h_{\mathcal Y\leftarrow\mathcal Z}
=h_{\mathcal X\leftarrow\mathcal Z}.
}
\tag{CS8}
\]
Indeed \(I_{\mathcal X}I_{\mathcal Y}^{+}I_{\mathcal Y}=I_{\mathcal X}\). Both the minimum cost and its selected lift therefore compose. \(\square\)

The matrix pseudoinverse uses an auxiliary Euclidean chart. The quantity in (CS5), on the annihilator of the tangent radical, is the intrinsic dual form of the tangent/radical quotient, as in [[conditional-fisher-coercivity/inq#Degeneracy and coordinate invariance|the existing intrinsic score convention]]. It is invariant under simultaneous invertible changes of source coordinates. The lift is invariant too: different representatives of \(I_{\mathcal Z}^{+}u\) differ by a coarse radical vector, which every finer Fisher form annihilates.

## The minimizer is an actual observable

The previous theorem concerns covectors. Its observable realization needs an additional map. [[conditional-fisher-coercivity/inq#The score projection theorem|The score projection theorem]] owns the general Bessel estimate and score-span projection. Its derivative there is the context derivative of a conditional mean \(Kf\); the derivative here is generated by the declared transformation (CS1), with the discrete context held fixed. For a Gaussian Sobolev observable \(F\),
\[
dF=\ell\,\partial_WF,
\qquad
\mathcal R_{\mathcal Z}F
=\mathbb E[sF\mid\mathcal Z]
=\mathbb E[\ell\,\partial_WF\mid\mathcal Z].
\tag{CS9}
\]
The first equality specifies the actual infinitesimal action. The second is Gaussian integration by parts, not a declaration that every covector is a pointwise gradient. The score-pairing formula extends \(\mathcal R_{\mathcal Z}\) to \(L^2(\mu)\). It computes the first derivative of the conditional expectation of \(F\) under the declared transformation.

All discrete contexts here satisfy \(\mathbb E[s\mid\mathcal Z]=0\). If \(u\) is an admissible \(\mathcal Z\)-response, define
\[
\boxed{
F_{\mathcal Z,u}=s^TI_{\mathcal Z}^{+}u.
}
\tag{CS10}
\]
It is conditionally centered and satisfies
\[
\mathcal R_{\mathcal Z}F_{\mathcal Z,u}=u,
\qquad
\mathbb E[F_{\mathcal Z,u}^{\,2}\mid\mathcal Z]
=u^TI_{\mathcal Z}^{+}u.
\tag{CS11}
\]
This is the least conditional variance among all conditionally centered \(L^2\) observables with that response. This stronger assertion has its own proof: \(F-F_{\mathcal Z,u}\) is conditionally orthogonal to every score-linear observable, so its squared norm adds to (CS11). It is not inferred merely from the pointwise covector theorem, and it is not a claim about the energy of arbitrary observables.

For a finer context, the same observable has response
\(I_{\mathcal Y}I_{\mathcal Z}^{+}u\). Moreover,
\[
F_{\mathcal Y,h_{\mathcal Y\leftarrow\mathcal Z}u}
=F_{\mathcal Z,u}.
\tag{CS12}
\]
The score lies almost surely in the range of each conditional Gram matrix; therefore the intermediate range projection changes nothing. The harmonic lift thus preserves an actual observable through repeated cuts, not only a matrix norm.

For a fixed whole response \(u\), put \(v=I_0^{-1}u\). At full resolution,
\[
F_u=(\ell^Tv)W,
\qquad
dF_u=I_{BR}v,
\qquad
\mathbb E[dF_u\mid B]=I_Bv.
\tag{CS13}
\]
The finest lift really is a pointwise gradient. The coarser \(I_Bv\) is generally only a conditional mean of gradients: it need not lie on the line \(\mathbb R\ell_{BR}\) at an individual observation. Keeping the rank-one score field resolves this distinction.

For example, \(a=1/2,b=1/3,u=(1,0)^T\) gives
\[
v=(36,-6)^T/35,\qquad
F_u=\begin{cases}(6/7)W,&BR=1,\\(6/5)W,&BR=-1,\end{cases}
\quad
\operatorname{Var}(F_u)=36/35.
\tag{CS14}
\]
The response quotient is not an observable-algebra quotient. The polynomial \(W^2-1\) has zero first-order response, whereas \((W^2-1)W\) has response \(2(1,ab)^T\ne0\). The kernel is not a multiplicative ideal. Higher Hermite observables and their products remain part of the whole carrier; the two score directions do not exhaust observations.

## Three dualization policies give three different clocks

Return to the actual pointwise gradient in (CS9). Applying the inverse at three different stages gives
\[
\begin{aligned}
\Gamma_0(F)&=(dF)^TI_0^{-1}dF
=\frac{2}{1+abBR}|\partial_WF|^2,\\
\Gamma_B(F)&=(dF)^TI_B^{-1}dF
=\frac{2}{1+bR}|\partial_WF|^2,\\
\Gamma_{BR}(F)&=(dF)^TI_{BR}^{+}dF
=|\partial_WF|^2.
\end{aligned}
\tag{CS15}
\]
The last evaluation is allowed because \(dF\in\operatorname{Ran}I_{BR}\). For any finite rank-one score frame \(I_z=\ell_z\ell_z^T\), the whole-first coefficient is the leverage \(\ell_z^T\bar I^+\ell_z\); its mean is \(\operatorname{rank}\bar I\). The fully resolved coefficient is one wherever \(\ell_z\ne0\). Here this explains the mean coefficients two and one; it does not identify either number with a mass.

Integrating (CS15) against the same \(\mu\) gives three closed symmetric Dirichlet forms on
\[
\mathcal H=L^2(\mu),\qquad
D(\mathcal E)=\bigoplus_{B,R}H^1(\gamma).
\]
Their generators are the displayed sector coefficients times
\[
N=-\partial_W^2+W\partial_W.
\tag{CS16}
\]
The coefficients are positive and bounded above and below, so these are genuine finite direct sums of Gaussian Ornstein--Uhlenbeck generators with the same form domain. Each has the four-dimensional kernel of functions of \(B,R\), not a unique constant vacuum. The fully resolved form is bounded above by either coarser form; the two coarser forms are not ordered in general.

Indeed for \(F_\pm=\mathbf1_{\{R=\pm1\}}W\),
\[
\mathcal E_0(F_\pm)
=\frac{(1\pm b)(1\mp a^2b)}{1-a^2b^2},
\qquad
\mathcal E_B(F_\pm)=1,
\qquad
\mathcal E_{BR}(F_\pm)=\frac{1\pm b}{2}.
\tag{CS17}
\]
At \(a=0,b>0\), the first pair is \(1+b,1-b\), straddling the second pair. Testing only \(F=W\) misses this: both coarser energies are two, while the finest is one.

The shorting theorem does not equate these three Dirichlet forms. It minimizes over conditional response lifts and proves a variance statement on the score-linear image. Substituting an averaged inverse into every pointwise gradient is a different operation. [[conditional-fisher-coercivity/moving-fiber-connection|Transporting moving-fiber derivatives]] likewise requires transforming the derivative rather than changing only its metric coefficient.

The boundary-first policy specifically uses a center-valued metric and its module-valued dual before normal evaluation. Enlarging an ordinary scalar parameter space to controls \(h_B\in\mathbb R^2\) would instead give scalar Fisher blocks \(\pi_a(B)I_B\); a point-evaluation covector would then acquire a factor \(1/\pi_a(B)\). These constructions must not be interchanged under the phrase “boundary-dependent controls.”

## Which boundary law distinguishes the clocks?

All-time annular intertwining alone is insufficient. At \(a=0\), all three generators preserve the subspace of functions \(F(R,W)\), and all three semigroups intertwine its isometric pullback. Their decay rates remain different: for \(F_+\), the respective correlations are
\[
\frac{1+b}{2}e^{-2t},\qquad
\frac{1+b}{2}e^{-2t/(1+b)},\qquad
\frac{1+b}{2}e^{-t}.
\tag{CS18}
\]

A stronger requirement compares **normalized restriction to a declared boundary sector, including the transformation family**, with reconstructing the response from that conditional experiment. Restricting the whole-first operator to \(B=\beta\) retains coefficient
\(2/(1+ab\beta R)\). Reconstructing from \(\mu(\cdot\mid B=\beta)\) gives \(2/(1+bR)\). These differ in general. The boundary-first policy commutes with this \(B\)-restriction. If normalized restriction to the finer \(R\)-sectors is also required, the conditional experiment has rank-one Fisher matrix and returns coefficient one; the fully resolved policy is the one of the three compatible with both restrictions.

This is a selection **among the stated policies with the same Fisher normalization**, not a uniqueness theorem for every possible clock. Which sectors are admissible boundaries is additional structural data. Conditional restriction does not assert that a sector has become an actual measurement outcome. In a noncommutative setting these central-sector maps cannot simply be presumed.

Finally, scalarizing conditional Fisher data is not forgetting the boundary variable in the statistical experiment. If \(B\) is genuinely marginalized, the observable is \((R,W)\), its score at \(\theta=0\) is \(W(1,aR)^T\), and
\[
I_{\mathrm{marginal}}
=\begin{pmatrix}1&ab\\ab&a^2\end{pmatrix}
\ne I_0.
\tag{CS19}
\]
At \(a=0\), the right first-order score vanishes after forgetting \(B\), although higher-order dependence of the marginal family can remain. This is an actual information-loss map, distinct from either a conditional theorem or central evaluation.

The [[gauge-boundary-frame-gluing/two-sided-fisher-completion-and-the-neutral-carrier#Annular restart is a different law, and it fails here|root-sensitive two-sided path response]] motivates this test. Its source shifts may move proposed conditioning variables, unlike the ancillary frames here: extending this construction requires the actual conditional source family and any central Fisher terms. Pointwise pseudoinversion alone does not turn its two-handed response into a one-handed clock. What is now constructed is a finite conditional score object with associative, observable-realized shorting and a precise boundary-policy discriminator, not a physical field clock.

[[receipts/conditional_score_shorting_receipt.py|The finite receipt]] checks the actual Gaussian shift likelihood, conditional score Gramians, singular-range lifts, full finite-observable least-variance problem, repeated cuts, the three generators and the restriction discriminator. Its finite checks supplement the proofs above; they do not establish a continuum or Yang--Mills result.

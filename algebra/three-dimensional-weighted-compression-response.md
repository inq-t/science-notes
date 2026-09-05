# Three-Dimensional Weighted Compression Response

In three flat boundary dimensions, the ordinary trace of a Clifford compression defect diverges. Changing the input from boundary values to normal sources gives a finite replacement: the squared Hilbert–Schmidt norm of the leak composed with the Neumann-to-Dirichlet map is exactly the harmonic boundary response. This derives an order-one quadratic form from a specified compression and Green operator, not from a fitted mass term. Unlike the circle construction, its scalar-symbol pairing has no nonzero odd central part.

## The retained and discarded channels

Take Hermitian Clifford matrices on \(\mathbb C^r\), with

\[
C_iC_j+C_jC_i=2\delta_{ij}I,
\qquad \operatorname{tr}(C_iC_j)=r\delta_{ij}.
\]

The irreducible three-dimensional choice has \(r=2\). On \(L^2(\mathbb R^3,\mathbb C^r)\), define

\[
D=-i\sum_{j=1}^3C_j\partial_j,
\qquad A=|D|=\sqrt{-\Delta}\,I,
\qquad P(p)=\frac12(I+\widehat p\cdot C).
\tag{TC1}
\]

The value of \(P\) at \(p=0\) is immaterial for Lebesgue measure. Reversing its sign selects the opposite polarization and leaves the response below unchanged. For a scalar Schwartz symbol \(f\), put

\[
T_f=PM_fP|_{\operatorname{Ran}P},
\qquad H_f=(I-P)M_fP.
\tag{TC2}
\]

As in [[algebra/hardy-compression-and-boundary-response|Hardy compression]],

\[
T_{|f|^2}-T_f^*T_f=H_f^*H_f\geq0.
\tag{TC3}
\]

For real \(f\), this is \(T_{f^2}-T_f^2\). The operator records intermediate channels excluded by the polarization; it does not itself specify an outcome, entropy production or a clock.

## Why the ordinary circle trace does not transfer

First use the unit torus \((\mathbb R/2\pi\mathbb Z)^3\), with normalized volume and momentum \(p\in\mathbb Z^3\). For \(f=e^{ik\cdot x}\), multiplication sends \(p\) to \(p+k\). Away from the two exceptional zero momenta, the exact contribution to the squared Hilbert–Schmidt norm is

\[
\operatorname{tr}\bigl[P(p)(I-P(p+k))P(p)\bigr]
=\frac r4\left(1-\frac{p\cdot(p+k)}{|p|\,|p+k|}\right).
\tag{TC4}
\]

Let \(\Pi_\Lambda\) cut only the input momenta to \(|p|\leq\Lambda\). For fixed nonzero \(k\),

\[
\lim_{\Lambda\to\infty}\frac1\Lambda
\|H_{e^{ik\cdot x}}\Pi_\Lambda\|_{\mathrm{HS}}^2
=\frac{r\pi}{3}|k|^2>0.
\tag{TC5}
\]

Indeed the summand in (TC4) is
\(r[|k|^2-(\widehat p\cdot k)^2]/(8|p|^2)+O_k(|p|^{-3})\).
The remainder sums to \(O_k(\log\Lambda)\). The homogeneous leading term has the same limit as its ball integral: comparison with unit lattice cells again has logarithmic error, and its spherical angular integral is \((8\pi/3)|k|^2\). The zero-mode convention changes only finitely many terms.

For a trigonometric polynomial, distinct Fourier shifts have orthogonal outputs for each input momentum. Thus the corresponding limit is
\((r\pi/3)\sum_k|k|^2|f_k|^2\).
Every nonconstant real polynomial has infinite ordinary defect trace. Dividing the cutoff trace by \(\Lambda\) produces an **order-two** Dirichlet form, not the circle's order-one response. A large finite cutoff is not evidence of a finite ordinary trace; cutting the multiplication algebra on both sides also introduces a different artificial boundary.

## A Green-weighted trace is exactly finite

Return to \(\mathbb R^3\), with unitary Fourier convention

\[
\widehat f(k)=(2\pi)^{-3/2}\int e^{-ik\cdot x}f(x)\,dx.
\]

Define the weighted leak initially on spinors whose Fourier transforms are smooth, compactly supported and avoid zero momentum:

\[
\mathcal A_f:=H_fA^{-1}.
\tag{TC6}
\]

Although \(A^{-1}\) is unbounded at zero, this composition extends to a Hilbert–Schmidt operator. For real or complex Schwartz \(f\), its exact norm is

\[
\boxed{\operatorname{Tr}(\mathcal A_f^*\mathcal A_f)
=\frac{r}{8\pi^2}\int_{\mathbb R^3}|k|\,|\widehat f(k)|^2\,dk.}
\tag{TC7}
\]

To prove this, its Fourier kernel is

\[
\mathcal A_f(q,p)
=(2\pi)^{-3/2}\widehat f(q-p)
\frac{(I-P(q))P(p)}{|p|}.
\tag{TC8}
\]

Applying (TC4) and the nonnegative integral theorem reduces the claim to

\[
\int_{\mathbb R^3}\frac{r}{4|p|^2}
\left(1-\widehat p\cdot\widehat{p+k}\right)dp
=r\pi|k|.
\tag{TC9}
\]

For \(a=|k|>0\), radial coordinate \(t=|p|\), and angular cosine \(u\), direct integration gives

\[
\int_{-1}^1\left(1-\frac{t+au}{\sqrt{t^2+a^2+2tau}}\right)du
=
\begin{cases}
2-4t/(3a),&0<t<a,\\
2a^2/(3t^2),&t>a.
\end{cases}
\tag{TC10}
\]

One can obtain this by differentiating
\(\int_{-1}^1\sqrt{t^2+a^2+2tau}\,du\) with respect to \(t\).
The two radial integrals in (TC10) are \(4a/3\) and \(2a/3\). Multiplication by the azimuthal factor \(2\pi\) and \(r/4\) proves (TC9), including the vanishing case \(k=0\).

This proof handles the infrared domain explicitly: the kernel (TC8) is square integrable and agrees with the initial composition on a dense domain, hence supplies its unique bounded closure. No gap or bounded inverse at zero was assumed. By completion, the symbol-to-kernel map extends to \(H^{1/2}(\mathbb R^3)\); for symbols that are not bounded, that extension does not require separately defining an unbounded Toeplitz subtraction.

## The weight changes what the operator operates on

The harmonic extension to \(\mathbb R^3\times(0,\infty)\) is
\(\widehat u_f(k,t)=e^{-t|k|}\widehat f(k)\). Its outward normal derivative at \(t=0\) is \(Af\), and

\[
\int_0^\infty\int_{\mathbb R^3}
\left(|\partial_tu_f|^2+|\nabla_xu_f|^2\right)dx\,dt
=\int |k|\,|\widehat f(k)|^2dk.
\tag{TC11}
\]

Thus (TC7) is exactly \(r/(8\pi^2)\) times this Dirichlet-to-Neumann form, the flat half-space member of [[trace-dirichlet-descent/inq|trace Dirichlet descent]]. It is an independently calculated analogue of the [[directed-analytic-realization/harmonic-boundary-realization|oriented disk response]].

Here \(A^{-1}\) is the same geometry's Neumann-to-Dirichlet map: it converts prescribed normal source data into boundary values before compression. At the level of the squared norm, the inserted weight is the inverse Laplacian \(A^{-2}\). This motivates a specific change of input type, not a numerical cutoff or an adjustable mass parameter. The Euclidean metric, Clifford presentation, source-space \(L^2\) trace and this Green prescription remain declared inputs. The theorem does not force their physical selection. Spinor amplification also multiplies the trace by \(r\); its normalization must be retained.

The exact coefficient uses flat continuous momentum integration. The similarly weighted torus sum, with the inverse set to zero on zero modes, is finite, but is not identically (TC7) with an integral replaced by a sum: discrete momentum lacks the scaling substitution used above.

## The even response does not supply the odd local form

Polarizing (TC7) gives

\[
\operatorname{Tr}(\mathcal A_f^*\mathcal A_g)
=\frac{r}{8\pi^2}\int |k|\,
\overline{\widehat f(k)}\widehat g(k)\,dk.
\tag{TC12}
\]

For real scalar \(f,g\), this pairing is real and symmetric, by \(k\mapsto-k\). Its antisymmetric trace is zero. It therefore cannot replace the nonzero odd central form of the circle's [[directed-analytic-realization/local-weyl-realization|local Weyl construction]]. [[algebra/cauchy-response-and-local-action|Opposed Cauchy response]] instead uses the Green pairing of separate boundary-value and normal-source slots; that paired carrier is additional structure, not the imaginary part of (TC12). Nor does (TC12) imply that compressed readouts commute on disjoint supports.

The positive response acts on **symbol labels**; \(\mathcal A_f^*\mathcal A_f\) for one fixed label acts on **source spinors**. They are related by the trace theorem, not identical operators. Finally, \(A=\sqrt{-\Delta}\) on flat space has arbitrarily soft modes. This construction derives a boundary-response identity without a scalar mass insertion; it does not by itself derive a positive mass floor.

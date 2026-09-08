# Positive Amplitude Kernels and the Prepared State

The two-plaquette Haar preparation is a positive integral kernel: conditioning on the shared path makes its amplitude a Gram average of strictly positive one-loop functions. The supplied heat equation therefore has a completely positive operator realization, and the local probability law is the diagonal of the normalized squared kernel. This is a genuine compatibility constraint stronger than pointwise or coefficient positivity. It still does not preserve marginal concavity for every admissible positive kernel: an explicit rank-ten example passes those positivity and symmetry tests but leaves the concavity class under the same full evolution.

**Status: exact fixed-system representation and obstruction, not a derivation of the Hamiltonian or a continuum gap.** Use the entire carrier and seven-link geometry in [[two-plaquette-vacuum-and-relational-state|the interacting two-plaquette construction]]. The group, relative electric speeds, magnetic potential and initial preparation remain declared inputs.

## The shared path supplies a positive kernel

Let \(q(g)=\tfrac12\operatorname{Tr}g\) on \(G=SU(2)\),
\(D=-\sum_jR_j^2\) in the metric \(Q=-2\operatorname{Tr}\),
and \(V(g)=\lambda[1-q(g)]\), \(\lambda\ge0\).
The unnormalized Haar amplitude is
\[
P_t(x,y)=e^{-tH_\lambda}1(x,y),\qquad
H_\lambda=4\kappa(D_x+D_y)
-2\kappa\sum_jR_{x,j}R_{y,j}+V(x)+V(y).
\tag{PK1}
\]
Represent its underlying diffusion by three independent
group Brownian paths \(U,W,S\), with electric speeds
\(3\kappa,3\kappa,\kappa\), starting at \(x,y,1\).
The two output paths are \(US^{-1}\) and \(WS^{-1}\).
These speeds are inherited from the outer three-edge paths
and the shared edge; the outputs are not independent.

For a fixed entire shared path \(S\), define
\[
f_{t,S}(x)=\mathbb E_{U_0=x}
\exp\!\left[-\int_0^t V(U_sS_s^{-1})\,ds\right].
\]
Conditional independence of the two outer paths gives
\[
\boxed{
P_t(x,y)=\mathbb E_S[f_{t,S}(x)f_{t,S}(y)],\qquad
A_t=\mathbb E_S|f_{t,S}\rangle\langle f_{t,S}|\ge0.
}
\tag{PK2}
\]
Here \(A_t:L^2(G)\to L^2(G)\) is the integral operator
with kernel \(P_t\), not the physical Hamiltonian.
The expectation is a trace-class Bochner integral:
\(0<f_{t,S}\le1\) and
\(\operatorname{Tr}A_t=\mathbb E\|f_{t,S}\|_2^2\le1\).
In particular \(A_0=|1\rangle\langle1|\).
The Brownian notation is a mathematical representation of
the given positive heat equation, not a postulate of
ontological randomness.

## The same full evolution is completely positive on kernels

Identify \(L^2(G\times G)\) with Hilbert--Schmidt kernels.
On smooth finite-rank kernels, differentiation in the second
variable sends \(R_{y,j}\) to \(-A R_j\), because
\(R_j^*=-R_j\). Thus (PK1) becomes
\[
\boxed{
\dot A=-\{3\kappa D+V,A\}
       +\kappa\sum_j[R_j,[R_j,A]].
}
\tag{PK3}
\]
The braces denote an anticommutator. The plus sign before
the double commutator is required for skew-adjoint \(R_j\).
Equivalently the right side is
\(-\{4\kappa D+V,A\}+2\kappa\sum_jR_j A R_j^*\).

Both elementary evolutions preserve complete positivity:
\[
A\longmapsto e^{-s(3\kappa D+V)}Ae^{-s(3\kappa D+V)},
\qquad
A\longmapsto\int T_gAT_g^*\,p_{\kappa s}(g)\,dg,
\]
where \(T_g h(x)=h(xg)\) and \(p_{\kappa s}\) is the
shared heat law. Their form-product limit is the
self-adjoint elliptic kernel evolution (PK1), with the
inherited smooth/Peter--Weyl core and \(H^2(G^2)\) domain.
No independent boundary condition on orbit coordinates is
introduced.

The same conditional-path argument gives a trace-class
extension for arbitrary positive initial kernels:
\(A\mapsto\mathbb E_S B_{t,S}AB_{t,S}^*\).
Here \(B_{t,S}\) is the outer, time-dependent killed heat
operator including the terminal translation by \(S_t^{-1}\).
It is an \(L^2\) contraction: time slicing uses heat
contractions, multiplication by numbers in \([0,1]\), and
a unitary terminal translation. This proves complete
positivity and trace nonincrease, not trace preservation.

The kernel positivity is an additional consequence of the
equal outer speeds, identical potentials and this preparation.
It is not a property of every positive physical wavefunction.
Nor is this operator semigroup a newly reconstructed
Lorentzian dynamics: under vectorization it is exactly
the supplied Euclidean evolution.

## The readout uses the square, and the metric keeps the frame

The physical vector is normalized in \(L^2(G^2)\), hence
in Hilbert--Schmidt norm. Its complete \(x\)-marginal is
\[
\boxed{
R_t(x)=\frac{(A_t^2)(x,x)}{\operatorname{Tr}(A_t^2)},
\qquad
\Phi_x(y)=\frac{P_t(x,y)}{\sqrt{(A_t^2)(x,x)}}.
}
\tag{PK4}
\]
Gauge invariance makes \(R_t\) a function of \(a=q(x)\).
Neither \((A_t)(x,x)\) nor trace-normalizing \(A_t\)
gives this probability law. The normalized square and
its diagonal do not inherit a linear semigroup from (PK3).

The fixed-\(y\) row overlap is
\((A_t^2)(x,x')/
\sqrt{(A_t^2)(x,x)(A_t^2)(x',x')}\).
Its derivatives give a row metric, but not automatically
the raw physical conditional metric. If the retained
shared link is \(g\), and outer products are \(B,C\),
then \(x=Bg^{-1},y=Cg^{-1}\). Comparing two retained
configurations therefore gives the raw overlap
\[
\frac{(A_t T_{gg'^{-1}}A_t)(x,x')}
{\sqrt{(A_t^2)(x,x)(A_t^2)(x',x')}}.
\tag{PK5}
\]
The hidden row is translated when the retained shared
frame changes. Mixed derivatives of this overlap,
not of the fixed-frame overlap alone, recover the
[[conditional-fisher-coercivity/moving-fiber-connection|inherited conditional metric]].

In particular its retained kinetic trace is
\[
T_A=3\sum_j\|R_{x,j}\Phi\|_y^2
       +\sum_j\|(R_{x,j}+R_{y,j})\Phi\|_y^2;
\qquad
T_B=3\sum_j\|R_{y,j}\Phi\|_y^2.
\tag{PK6}
\]
The shared derivative cannot be replaced by another
independent \(R_x\). This is the same metric content as
the full cometric in (TP4). Thus the amplitude kernel,
the declared raw comparison law and the marginal
normalization jointly supply the conditional response.
Kernel positivity by itself supplies neither that metric
nor its lower spectral bound.

## A necessary second-moment compatibility condition

Let the initial kernel be any smooth strictly positive
real central convolution \(k(xy^{-1})\), with squared
norm \(Z=\int_Gk(g)^2dg\) and normalized amplitude
\(k/\sqrt Z\). Its two full configuration
marginals are Haar. Define moments of the relative
law \(\beta(dg)=k(g)^2dg/Z\) by
\[
\alpha_1=\mathbb E_\beta q(g),\qquad
\alpha_2=\mathbb E_\beta[4q(g)^2-1]/3.
\]
Rotational invariance of this law gives
\[
\mathbb E[b\mid x]=\alpha_1a,\qquad
\operatorname{Var}(b\mid x)
=(\alpha_2-\alpha_1^2)a^2+(1-\alpha_2)/4.
\tag{PK11}
\]
For the actual heat evolution from that kernel, put
\(v(t,a)=\partial_a^2\log\sqrt{R_t(a)}\). Then
\[
\boxed{
v(0,a)=v_t(0,a)=0,\qquad
v(t,a)=2\lambda^2(\alpha_2-\alpha_1^2)t^2+O(t^3).
}
\tag{PK12}
\]
The remainder is controlled on the closed latitude
interval for this fixed smooth initial vector and
fixed coefficients.

Here is the kinetic cancellation, including the shared
edge. With \(c=q(xy^{-1})=ab+z\), \(S=a+b\), and
\(K=H_0/\kappa\), the full operator gives
\[
\Gamma_K(S,c)=\tfrac34(1-c)S,\qquad
K(Sk)=S Kk+3Sk-2k'\Gamma_K(S,c).
\]
The operator \(K\) preserves relative-convolution
functions. For hidden Haar integration \(I\),
\[
I[Sf(c)]=aI[(1+c)f(c)],\qquad
I[f(c)\Gamma_K(S,c)]=\tfrac{3a}{4}I[(1-c^2)f(c)].
\]
Consequently all pure kinetic contributions to
\(\partial_t^2R|_0\) are constant in \(a\), and every
mixed \(\kappa\lambda\) contribution is affine.
The corresponding logarithmic cross terms are also
constant or affine. The magnetic-square contribution
to \(\log\sqrt R\) is
\(\lambda^2t^2\operatorname{Var}(b\mid x)\).
Two latitude derivatives prove (PK12).
This uses a finite Taylor expansion on the inherited
smooth domain, not a zero-diffusion approximation.

For \(\lambda>0\), any class that contains such initial
kernels and preserves latitude concavity must therefore
obey
\[
\boxed{\alpha_2\le\alpha_1^2.}
\tag{PK13}
\]
It is a necessary condition on relative correlations,
not a sufficient preservation theorem or a gap bound.
Equality leaves higher time orders undecided. Haar has
\(\alpha_1=\alpha_2=0\), and its negative cubic curvature
is the distinct calculation in (TP44).

[[replica-weighted-correlations-and-the-local-readout#Averaging to convolution does not transport the evolution|The averaging audit]]
fixes this criterion's scope: common-left averaging preserves
the relative moments but does not intertwine the magnetic
evolution. Applying (PK13) to that averaged state tests a
new convolution restart, not the actual nonconvolution
trajectory. The latter's local curvature requires the
separate posterior identity (RW13).

## A positive-feature Gram kernel can still lose marginal concavity

Use \(\chi_n(g)=C_n^1(q(g))\) for the character of
dimension \(n+1\); thus \(\chi_2(g)=4q(g)^2-1\).
For \(0<d<1\), take
\[
k_d(x,y)=1+\frac d3\chi_2(xy^{-1}),\qquad
Z_d=\|k_d\|_{L^2(G^2)}^2=1+d^2/9.
\tag{PK7}
\]
This kernel is smooth, gauge invariant, exchange symmetric
and strictly positive. Its operator has eigenvalue \(1\)
on constants and \(d/9\) on the nine spin-one matrix
coefficients, and zero elsewhere. It is positive of rank
ten. More strongly,
\[
k_d(x,y)=\int_G
[1+\sqrt d\,\chi_2(xh^{-1})]
[1+\sqrt d\,\chi_2(yh^{-1})]\,dh.
\tag{PK8}
\]
Both features are strictly positive, since \(\chi_2\ge-1\).
Thus the example passes the positive-feature Gram test
in (PK2), not only abstract operator positivity.
The normalized vector \(k_d/\sqrt{Z_d}\) has both
complete \(SU(2)\) configuration marginals exactly Haar.

Under its actual conditional law on \(y\), character
orthogonality and
\(\chi_2^2=\chi_0+\chi_2+\chi_4\) give
\[
\mathbb E[b\mid x]=0,\qquad
\mathbb E[b^2\mid x]=\tfrac14+\alpha(a^2-\tfrac14),
\qquad
\alpha=\frac{d(6+d)}{3(9+d^2)}>0.
\tag{PK9}
\]
Now evolve this initial vector with the **same full**
\(H_\lambda\) in (PK1), and define
\(v(t,a)=\partial_a^2\log\sqrt{R_t(a)}\).
For fixed \(\kappa,\lambda>0\),
\[
\boxed{
v(0,a)=\partial_tv(0,a)=0,\qquad
v(t,0)=2\lambda^2\alpha\,t^2+O(t^3)>0.
}
\tag{PK10}
\]
This is the strict violation of (PK13) with
\(\alpha_1=0,\alpha_2=\alpha>0\).
In this finite example free heat is explicitly
\(e^{-tH_0}k_d=1+(d/3)e^{-12\kappa t}\chi_2(xy^{-1})\).
The cancellation argument proving (PK12) retains all
kinetic contributions. This is not a counterexample
obtained by freezing the hidden dynamics.

The example disproves preservation of the sufficient
latitude-concavity condition, not positivity of the
kernel, existence of its finite-system gap, or the
[[heat-preparation-and-latitude-coercivity|actual Haar-preparation theorems]].
It is not the rank-one initial vector \(A_0=|1\rangle\langle1|\).
The extra information in that prepared trajectory cannot
be replaced by the entire positive-feature Gram cone,
even after both local marginals and exchange symmetry
are fixed.

The
[[receipts/two_plaquette_vacuum_receipt.py|full interacting receipt]]
checks the kernel's complete relational basis, free
eigenvalue twelve, positive operator blocks and both flat
initial marginals. At \(d=1/2,\kappa=\lambda=1\),
\(\alpha=13/111\). On cutoffs six and eight, the actual
evolved ratios \(v(t,0)/(2\alpha t^2)\) at
\(t=0.01,0.005,0.0025\) are approximately
\(0.854355,0.924995,0.961937\), approaching one.
The maximum cutoff difference is below \(8.3\,10^{-10}\).
These checks test the finite coefficient, not a uniform
remainder or a failure of the actual Haar trajectory.

The constructive gain is an exact positive-kernel
representation tying a joint amplitude to its readout
and transported response. The remaining selecting
question is quantitative: which correlations are
reachable from the specified primitive preparation,
and what inequalities does that reachability force?
Positivity, symmetry and loss accounting alone have
not supplied such an inequality.

# Pauli Transport and the Continuum Scaling Obstruction

The Pauli connection has a genuine volume-independent spectral edge, but its gap and its spatial kinetic coefficients cannot be scaled independently by positive edge weights. An exact identity shows that retaining finite nonzero continuum propagation in at least two directions forces the squared clock gap to diverge. A finite massive, one-direction limit is possible. A multidirectional massive continuum envelope can instead be obtained after an explicit subtraction from the response operator, but that changes the model and supplies its limiting mass. These distinctions concern one specified free operator family, not every possible geometric origin of mass.

## The square of the clock fixes the typing

Use the [[short-loop-holonomy-and-quantitative-gluing|Pauli connection]] on \(\mathbb Z^d\), \(d=2\) or \(3\), with fiber \(\mathbb C^2\) and forward transports \(\sigma_j\). Give direction \(j\) a strictly positive weight \(w_j(a)\), where \(a>0\) is the declared spatial lattice spacing. The response form is
\[
\mathcal E_a[x]=\sum_{v,j}w_j(a)
\|x_{v+\hat j}-\sigma_jx_v\|^2.
\tag{PS1}
\]
It defines a bounded positive operator \(L_a\) for each fixed \(a\). Multiplying both vertex and edge sums by \(a^d\) does not change that operator; any derivative factor \(a^{-2}\) belongs explicitly in the weights.

Choose the clock \(A_a=L_a^{1/2}\), as in the
[[cauchy-response-and-local-action|opposed-response wave prescription]].
Then eigenvalues of \(L_a\) are **squared clock rates**. Calling them energy squared requires an additional energy–time calibration. Choosing \(L_a\) itself as clock would be a different prescription.

For dimensionless momentum \(k\in(-\pi,\pi]^d\), set
\[
s_a=\sum_jw_j(a),\qquad r_a=\sqrt{\sum_jw_j(a)^2}.
\]
The exact Fourier symbol and bands are
\[
L_a(k)=2s_aI-2\sum_jw_j(a)\cos k_j\,\sigma_j,
\qquad
\lambda_{\pm,a}(k)=2s_a\pm2\sqrt{\sum_jw_j(a)^2\cos^2k_j}.
\tag{PS2}
\]
Anticommutation gives these formulas without a continuum approximation. The lower spectral edge is
\[
\Gamma_a=2(s_a-r_a)>0,\qquad
\inf\sigma(A_a)=\sqrt{\Gamma_a}.
\tag{PS3}
\]
There are \(2^d\) lower-band minima, at \(k_j\in\{0,\pi\}\). The same minima occur on even periodic tori; the infinite-lattice edge need not be an eigenvalue. This is not yet a vacuum-plus-excitation realization.

## An exact relation between the gap and spatial curvature

Write physical momentum near any minimum as \(k=k_*+ap\). Define the quadratic coefficients by the exact derivatives
\[
b_{j,a}:=\frac12
\left.\frac{\partial^2}{\partial p_j^2}
\lambda_{-,a}(k_*+ap)\right|_{p=0}
=\frac{a^2w_j(a)^2}{r_a}.
\tag{PS4}
\]
Mixed second derivatives vanish. In the chosen wave prescription these are the squared propagation-speed coefficients of a possible continuum envelope. This derivative identity is valid at every \(a\), even if the weights diverge.

Since \(\sum_jb_{j,a}=a^2r_a\), elimination of the weights gives
\[
\boxed{
a^2\Gamma_a
=2\left[
\sqrt{\sum_jb_{j,a}}\sum_j\sqrt{b_{j,a}}
-\sum_jb_{j,a}
\right].}
\tag{PS5}
\]
Suppose \(b_{j,a}\to v_j^2\), with all limits finite and at least two \(v_j>0\). Continuity of the right side yields
\[
a^2\Gamma_a\longrightarrow
2\left[
\sqrt{\sum_jv_j^2}\sum_jv_j-\sum_jv_j^2
\right]>0.
\tag{PS6}
\]
The strict inequality is precisely \(\|v\|_1>\|v\|_2\) for a nonnegative vector with at least two nonzero components. Thus \(\Gamma_a\) diverges like \(a^{-2}\), and the clock gap diverges like \(a^{-1}\).

Unequal spatial spacings do not evade the obstruction. At a fixed positive spacing vector, write \(k_j=k_{*,j}+a_jp_j\), suppress the family index, and set
\(b_j=a_j^2w_j^2/r\), \(c_j=\sqrt{b_j}/a_j=w_j/\sqrt r\), and \(t=\|c\|_2=\sqrt r\). Exactly,
\[
\Gamma
=2t(\|c\|_1-t)
=\frac{4t\sum_{i<j}c_ic_j}{\|c\|_1+t}
\ge\frac4{\sqrt d+1}\sum_{i<j}c_ic_j,
\tag{PS6a}
\]
where \(\|c\|_1\le\sqrt d\,t\) supplies the inequality. In particular, for any distinct \(i,j\),
\[
\boxed{\Gamma\ge
\frac4{\sqrt d+1}\frac{\sqrt{b_ib_j}}{a_ia_j}.}
\tag{PS6b}
\]
Along a family with \(a_i,a_j\to0\) and \(b_i,b_j\) bounded below by positive constants, the squared clock gap therefore diverges. No boundedness or convergence assumption on the remaining directional coefficients is needed for this estimate. It retains the fixed Pauli transports and positive-weight hypotheses.

This rules out a bounded gap together with finite nonzero propagation in two or more directions for this entire positive-weight family. It is stronger than substituting one familiar \(a^{-2}\) normalization. An arbitrary overall clock rescaling is already included: replacing \(A_a\) by \(c_aA_a\) replaces every weight by \(c_a^2w_j(a)\), so (PS5) still applies.

For equal weights in three dimensions, write \(\gamma=6-2\sqrt3\), \(m_a=\sqrt{\Gamma_a}\), and \(v_a=\sqrt{b_{j,a}}\). The ratio is especially simple:
\[
\boxed{\frac{a\,m_a}{v_a}
=\sqrt{\sqrt3\,\gamma}
=\sqrt{6(\sqrt3-1)}.}
\tag{PS7}
\]
No overall choice of clock unit changes it. A finite-speed, finite-gap continuum cannot be obtained merely by renaming the lattice scale.

## The one-direction exception is real

For \(d=3\), choose
\[
w_1(a)=v^2/a^2,\qquad w_2(a)=u,\qquad w_3(a)=z,
\qquad v,u,z>0.
\]
Then
\[
\Gamma_a\to2(u+z),\qquad
b_{1,a}\to v^2,\qquad b_{2,a},b_{3,a}\to0.
\tag{PS8}
\]
On bounded momentum sets the lower squared-frequency band tends to
\(2(u+z)+v^2p_1^2\).
It retains a positive gap without an on-site subtraction, but loses propagation in the other two directions. It is not a three-spatial-dimensional massive wave limit. This exception is why the hypothesis “at least two directions” cannot be omitted.

## The isotropic band is rotational only to quadratic order

Take unit weights and \(d=3\). Put
\(s_2=\sum_jk_j^2\), \(s_4=\sum_jk_j^4\). Near any minimum, using its local momentum coordinates,
\[
\lambda_-(k)
=\gamma+\frac{s_2}{\sqrt3}
+\frac{s_2^2-4s_4}{12\sqrt3}
+O(|k|^6).
\tag{PS9}
\]
This follows from
\(\cos^2t=1-t^2+t^4/3+O(t^6)\).
For \(m_0=\sqrt\gamma\), the clock band itself is
\[
\sqrt{\lambda_-(k)}
=m_0+\frac{s_2}{2\sqrt3\,m_0}
+\frac{s_2^2-4s_4}{24\sqrt3\,m_0}
-\frac{s_2^2}{24m_0^3}
+O(|k|^6).
\tag{PS10}
\]

At equal momentum magnitude \(q\), the squared-frequency quartic coefficient is \(-1/(4\sqrt3)\) along an axis, but \(-1/(36\sqrt3)\) along the body diagonal. The \(s_4\) term distinguishes the cubic lattice axes. The finite-lattice dispersion therefore is not the Lorentz-invariant formula \(m^2+v^2|p|^2\), even though its first spatial correction has that isotropic form.

The complete unit-weight bands satisfy
\[
\lambda_-\in[\gamma,6],\qquad
\lambda_+\in[6,6+2\sqrt3].
\tag{PS11}
\]
They touch where all \(\cos k_j=0\). Around each of the eight lower minima, however, the lower eigenspace is a smooth rank-one complex line, separated from the upper band. At \(k_*\), its projector is
\[
\Pi_*(0)=\frac12\left(I+\frac1{\sqrt3}\sum_j\eta_j\sigma_j\right),
\qquad \eta_j=\cos(k_{*,j})\in\{\pm1\}.
\]
An envelope construction retaining all low-momentum neighborhoods must account for all eight valleys, with any reality or charge constraints separately specified. Selecting one is an additional carrier restriction, not a consequence of its positive edge.

## A continuum envelope after changing the response

There is a precise positive construction, but it uses an extra term. For declared \(m,v>0\), define
\[
\widetilde L_a
=m^2I+\frac{\sqrt3\,v^2}{a^2}(L_{\rm Pauli}-\gamma I),
\qquad
\widetilde A_a=\sqrt{\widetilde L_a}.
\tag{PS12}
\]
The exact bound \(L_{\rm Pauli}\ge\gamma I\) makes this operator positive with lower edge \(m^2\). In each lower-band valley,
\[
\widetilde\lambda_{-,a}(k_*+ap)
=m^2+v^2|p|^2
+\frac{v^2a^2}{12}
\left(|p|^4-4\sum_jp_j^4\right)
+O(a^4|p|^6).
\tag{PS13}
\]
On fixed compact momentum sets this converges uniformly to
\(m^2+v^2|p|^2\); its positive square root converges uniformly to the corresponding massive clock. Smooth local band frames therefore give convergence on wave packets supported in those sets. The upper band has squared frequency at least \(m^2+6v^2/a^2\), and regions separated from every lower minimum also escape to infinite frequency.

These are controlled envelope statements, not a completed convergence theorem for observable nets, states or interactions. The limiting free wave symbol can enter the separate local realization in
[[cauchy-response-and-local-action]] and its
[[wick-real-forms-and-positive-preparation|positive-preparation construction]].
Those realization choices do not derive the coefficient \(m\) in (PS12).

The subtraction in (PS12) is
\(-(\sqrt3v^2/a^2)\gamma I+m^2I\). More generally,
\(L_a-\Gamma_aI+m^2I\) changes the response whose square root defines the clock. It is not a coordinate conversion or an irrelevant shift of the vacuum energy. Even shifting a one-particle clock itself becomes a particle-number term after Fock realization, not a scalar shift of the entire many-body Hamiltonian.

[[directed-analytic-realization/neutral-gaussian-return-of-holonomy-response|The fixed-lattice Gaussian return]] constructs a vacuum and a cyclic neutral observable sector with this gap. What fails is the attempt to obtain a multidirectional finite-gap continuum solely by positive reweighting of this unchanged Pauli transport. [[refining-holonomy-and-a-finite-continuum-threshold|Changing the holonomy to \(e^{iag\sigma_j}\)]] now gives a finite continuum probe threshold with no on-site subtraction, but fails the source-free-background and forward-cone-spectrum tests. Deriving a different interaction or constructing another master object also lies outside the present obstruction. A physical mass Casimir requires the actual translation and Lorentz structure; it is not established by the word “gap” or by quadratic agreement of one band.

[[directed-analytic-realization/neutral_transport_receipt.py|The neutral-transport receipt]] checks exact radical-elimination identities for rational weights, prescribed-speed refinements and the one-direction exception; the quartic remainder checks are numerical. [[directed-analytic-realization/neutral-transport-receipt-output.txt|Its output]] does not replace (PS5)–(PS6b) or certify convergence of an observable theory.

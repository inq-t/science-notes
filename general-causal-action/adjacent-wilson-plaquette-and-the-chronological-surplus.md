# An Adjacent Wilson Plaquette Changes the Chronological Surplus

Switching on the right plaquette of the actual two-square Wilson transfer leaves the left spatial marginal exactly Haar, but changes its chronological correlations at second order. The shared edge supplies singlet and triplet channels with weights \(1/4\) and \(3/4\). Their exact response also produces source leakage through the three-slab boundary law. A fixed left source's normalized surplus can increase while the lowest left-odd energy decreases: these are different tests of the same interacting transfer.

**Status: exact finite-graph perturbation and analytic sign controls; no uniform gap estimate.** The transfer is the one returned in [[cycle-moments-and-the-pure-gauge-vacuum-return|CM7]]. [[seam-coupling-response-and-the-vacuum-cap|SV]] owns its general seam-response calculus; [[spatial-block-sewing-and-the-vacuum-cap-response|SB]] owns the regional variance comparison and its source leakage. This calculation evaluates those changes on one actual adjacent-plaquette geometry.

## The seven raw links fix the free channels

Take two spatial squares sharing one edge, with \(G=SU(2)\). Orient the two three-link outer paths \(p,q\) and the common one-link path \(e\) from the same vertex to the same vertex. Keep all raw boundary frames and impose the joint Gauss action. Define the unit-Haar-norm sources
\[
f=\chi_{1/2}(pe^{-1}),\qquad
g=\chi_{1/2}(qe^{-1}),\qquad \chi_{1/2}=\operatorname{Tr}.
\tag{AP1}
\]
The temporal Wilson coupling \(b_t>0\) and temporal duration \(a_t>0\) stay fixed. Put
\[
x=2b_t,\qquad
z_t=\int e^{-b_t(2-\chi_{1/2}(U))}\,dU,\qquad
t_j=\frac{I_{2j+1}(x)}{I_1(x)},\qquad t=t_{1/2},\quad v=t_1 .
\]
At zero spatial magnetic coupling, the normalized transfer \(P_0\) has Haar vacuum. On the physical theta basis of [[interacting-vacuum-support-at-the-balanced-cut|IS2–6]],
\[
P_0\Psi_{(j_p,j_e,j_q)}
=t_{j_p}^{\,3}t_{j_e}t_{j_q}^{\,3}\Psi_{(j_p,j_e,j_q)}.
\tag{AP2}
\]
Each of the seven raw links contributes its own multiplier. The character integral and strict ordering \(1=t_0>t_{1/2}>t_1>\cdots>0\) follow from [[relative-multiplication-transfer-and-the-rotor-limit|RT4–7]].

Set \(\alpha=t^4\). Then \(P_0f=\alpha f\), \(P_0g=\alpha g\), and the exact shared-edge fusion is
\[
fg=\frac12\Psi_0+\frac{\sqrt3}{2}\Psi_1,\qquad
\Psi_0=\Psi_{(1/2,0,1/2)},\quad
\Psi_1=\Psi_{(1/2,1,1/2)},
\]
\[
P_0\Psi_j=\beta_j\Psi_j,\qquad
\beta_0=t^6,\quad\beta_1=t^6v,\qquad
w_0=\frac14,\quad w_1=\frac34.
\tag{AP3}
\]
These coefficients are IS6's normalized Clebsch projections. In particular \(\Psi_0=\chi_{1/2}(pq^{-1})\) is the six-edge outer-loop source. An independent product of loop clocks would give the single product eigenvalue \(\alpha^2\); the actual raw graph gives both \(\beta_j\).

## The true vacuum changes only on the right

Switch on the right spatial potential with strength \(s\):
\[
V_R=2-g,\qquad
T_s=z_t^7e^{-2s}B_s,\qquad
B_s=e^{sg/2}P_0e^{sg/2}.
\]
Let \(B_s\psi_s=\Lambda_s\psi_s\), \(\psi_s>0\), \(\int\psi_s^2=1\). The actual normalized transition and vacuum are
\[
P_sh=\frac{B_s(\psi_sh)}{\Lambda_s\psi_s},\qquad
\pi_s=\psi_s^2dU,\qquad
\lambda_s=z_t^7e^{-2s}\Lambda_s .
\tag{AP4}
\]
The scalar factor is retained in the raw normalization. In particular \((\log\lambda_s)'_0=-2\).

Right-loop class functions form an invariant subspace: \(\chi_j(qe^{-1})\) has multiplier \(t_j^4\), and multiplication by \(e^{sg/2}\) preserves that subspace. Its strictly positive Perron function lifts to a strictly positive eigenfunction on the whole graph, so uniqueness makes it the actual \(\psi_s\). Consequently \(\psi_s\) depends only on the right loop. Integrating the three right-exclusive raw links supplies Haar measure for that loop, independently of all four left raw links. Thus
\[
\mathbb E_{\pi_s}f=0,\qquad
\mathbb E_{\pi_s}f^2=1,\qquad
\text{the complete left raw-link marginal is Haar for every }s.
\tag{AP5}
\]
With the shared edge retained as the separator, the conditional vacuum copula of SB2 is exactly one. This statement does not apply after assigning that edge to one block in SB's unfrozen chronological test: the right-loop vacuum can then couple that block to the other one.

Analytic perturbation of the positive compact kernel gives, with \(c=(1+\alpha)/[2(1-\alpha)]\),
\[
\psi'_0=cg,\qquad
\Lambda'_0=0,\qquad
\Lambda''_0=\frac{1+\alpha}{1-\alpha}=2c,\qquad
\langle1,\psi''_0\rangle=-c^2 .
\tag{AP6}
\]
The last identity is the derivative of the vacuum normalization. The other components of \(\psi''_0\) are right-loop functions and have zero overlap with \(f^2\) after subtracting their Haar mean. All Taylor statements below hold at fixed \(b_t\) and graph.

## The complete chronological correlation has an exact second derivative

For \(n\ge0\), define the actual stationary moment
\[
C_n(s)=\langle f,P_s^nf\rangle_{\pi_s}
=\Lambda_s^{-n}
 \langle\psi_sf,B_s^n\psi_sf\rangle .
\tag{AP7}
\]
Changing the sign of one right-exclusive raw link at every time slice preserves the free kinetic law, fixes \(f\), and sends \(g\) to \(-g\). After the common scalar in (AP4) cancels, it intertwines \(s\) and \(-s\). Hence \(C_n\) is even; its first derivative vanishes. Also \(C_0(s)=1\) exactly.

Put \(D_0=0\), and for \(n\ge1\) put
\[
D_n(\alpha,\beta)
=\sum_{r=0}^{n-1}[1+r(1-\alpha)]
                  \alpha^r\beta^{n-1-r}.
\]
Then
\[
\boxed{
C_n''(0)=
\frac{2}{(1-\alpha)^2}
\sum_{j=0}^1w_j(\beta_j-\alpha^2)D_n(\alpha,\beta_j).}
\tag{AP8}
\]
This includes the vacuum endpoints, the normalized transition, and all insertions inside the \(n\)-step transfer.

Here is a finite derivation. Write \(m=(\alpha+\beta)/2\),
\[
S_n=\sum_{r=0}^{n-1}\beta^r\alpha^{n-1-r},\qquad
F_n=\sum_{r=0}^{n-2}(n-1-r)\alpha^{n-2-r}\beta^r,
\]
with an empty sum zero. Since
\[
B'_0=\tfrac12(gP_0+P_0g),\qquad
B''_0=\tfrac14(g^2P_0+2gP_0g+P_0g^2),
\]
the contribution of each channel of weight \(w_j\) to \(C_n''\), before multiplying by that weight, is
\[
2c^2(\beta^n-\alpha^n)+4cmS_n
+n\alpha^{n-1}m+2m^2F_n-2nc\alpha^n.
\tag{AP9}
\]
The first two terms include the differentiated vacuum vectors; the last term differentiates \(\Lambda_s^{-n}\). Its generating function in \(n\) simplifies exactly to
\[
\sum_{n\ge0}(\text{AP9})z^n
=\frac{2(\beta-\alpha^2)}{(1-\alpha)^2}
\frac{z(1-\alpha^2z)}
     {(1-\alpha z)^2(1-\beta z)}.
\]
Coefficient extraction gives (AP8). The power series can first be taken at sufficiently small \(|z|\); equality of coefficients is a finite algebraic identity.

An independent one-step check uses \(\varphi_s=e^{sg/2}\psi_s\). Its fundamental right-loop coefficient is \(s/(1-\alpha)+O(s^2)\), and
\[
C_1(s)=
\frac{\langle f\varphi_s,P_0(f\varphi_s)\rangle}
     {\langle\varphi_s,P_0\varphi_s\rangle}.
\]
Haar fusion contributes \(\bar\beta=(\beta_0+3\beta_1)/4\) to the numerator's fundamental-square term and \(\alpha\) to the denominator's. The common constant coefficient cancels, giving
\[
\boxed{C_1''(0)=\frac{2(\bar\beta-\alpha^2)}{(1-\alpha)^2}.}
\tag{AP10}
\]
Thus omitting the vacuum or the leading normalization would change an independently checkable result.

For the one-link Wilson law on \(a=\operatorname{Tr}U/2\), \(t=\mathbb E_xa\). Integration by parts against \(e^{xa}\sqrt{1-a^2}\,da\) gives
\[
v=1-\frac{4t}{x},\qquad
t'(x)=1-\frac{3t}{x}-t^2=\operatorname{Var}_x(a)>0,
\qquad
\bar\beta-\alpha^2=t^6t'(x)>0.
\tag{AP11}
\]
Since \(D_n\) is positive and nondecreasing in \(\beta>0\), the two-point covariance inequality gives
\(\sum_jw_j(\beta_j-\alpha^2)D_n>0\). Therefore \(C_n''(0)>0\) for every \(n\ge1\) and \(b_t>0\): the unchanged left marginal has strictly increased chronological correlations at second order.

## The actual surplus has two different sign regimes

Fix \(k\ge1\), \(A_s=P_s^k\), and the same physical duration \(\ell=ka_t\). For \(h_{f,s}=\delta_s f\), OI gives
\[
\mathcal D_k(s)=\|h_{f,s}\|^2=1-C_{2k}(s),\qquad
\mathcal S_k(s)=V_Q-C_{\rm lag}
=1-2C_{2k}(s)+C_{4k}(s).
\]
Its normalized source quotient is \(r_k(s)=\mathcal S_k(s)/\mathcal D_k(s)\). With all derivatives evaluated at \(s=0\),
\[
\boxed{\mathcal S_k''=C_{4k}''-2C_{2k}'',\qquad
r_k''=\frac{C_{4k}''-(1+\alpha^{2k})C_{2k}''}
                    {1-\alpha^{2k}}.}
\tag{AP12}
\]
These are complete sourced changes of the same chronology, including the changing innovation norm and lag cost.

The sign is not universally positive. The Haar Taylor expansion gives \(t=x/4-x^3/96+O(x^5)\), \(v=(2/3)t^2+O(t^4)\). For each fixed \(n\ge1\), (AP8) then gives
\[
C_n''=\frac n2t^{4n+2}[1+O(t^2)].
\]
Consequently, at small positive temporal coupling,
\[
\mathcal S_k''=-2k\,t^{8k+2}[1+O(t^2)]<0,\qquad
r_k''=-k\,t^{8k+2}[1+O(t^2)]<0.
\tag{AP13}
\]
At the other end, Laplace expansion of the explicit Haar integral gives
\[
t=1-\frac{3}{2x}+\frac{3}{8x^2}+O(x^{-3}),\qquad
\alpha=1-\frac6x+\frac{15}{x^2}+O(x^{-3}),
\]
\[
\beta_0=1-\frac9x+\frac{36}{x^2}+O(x^{-3}),\qquad
\beta_1=1-\frac{13}{x}+\frac{78}{x^2}+O(x^{-3}).
\]
For example, substituting \(u=x(1-a)\) makes that integral proportional to
\(e^x x^{-3/2}\int_0^{2x}e^{-u}u^{1/2}\sqrt{1-u/(2x)}\,du\); expanding on \(u\le x\) and bounding the exponential tail justifies the displayed remainders. In (AP8),
\[
\sum_jw_j(\beta_j-\alpha^2)=\frac{3}{2x^2}+O(x^{-3}),
\quad
\sum_jw_j(\beta_j-\alpha^2)(\beta_j-1)=\frac3{x^2}+O(x^{-3}).
\]
Together with \(D_n=n+\tfrac12n(n-1)(\beta-1)+O(x^{-2})\), these give
\[
\boxed{
C_n''\longrightarrow\frac{n^2}{12},\qquad
\mathcal S_k''\longrightarrow\frac{2k^2}{3}>0,\qquad
r_k''\sim\frac{kx}{18}>0.}
\tag{AP14}
\]
The \(s\)-derivative is taken first, with \(k\) fixed. These Taylor expansions are not uniform interacting limits as \(x\to\infty\); the undeformed quotient itself tends to zero. For each \(k\), the curvature is analytic in \(x>0\) and not identically zero. At its isolated zero-curvature couplings, the first nonzero higher-order surplus term has not been computed.

## The three-slab source leakage is nonzero

The seam score in SV14 gives
\[
B_kf:=\left.\partial_sP_s^kf\right|_0
=\sum_{j=0}^1c_jb_j(k)\Psi_j,\qquad
(c_0,c_1)=\left(\frac12,\frac{\sqrt3}{2}\right),
\]
\[
b_j(k)=\frac{\beta_j-\alpha^2}{1-\alpha}
 \sum_{r=0}^{k-1}\beta_j^r\alpha^{k-1-r}.
\tag{AP15}
\]
For example,
\[
b_0(k)=\frac{t^{4k+2}(1-t^{2k})}{1-t^4}>0.
\]
Retain all four left raw links at both outer endpoints, denoted \(O_L\), in the actual outer law \(\mu_{3,s}=\pi_sP_s^{3k}\). Define exactly SB's discarded source
\[
\zeta_s=f(U_+)-(P_s^kf)(U_-),\qquad
d_s=\zeta_s-\mathbb E_{\mu_{3,s}}[\zeta_s\mid O_L].
\]
At \(s=0\), \(\zeta_0=f(U_+)-\alpha^kf(U_-)\) is \(O_L\)-measurable, so its conditional projection equals itself for every \(s\). This cancels the derivative of the projection acting on that zeroth-order source.

Simultaneously multiplying a right-exclusive raw edge by \(-I\) at both outer endpoints preserves the full free \(\mu_{3,0}\) density. Equivalently, perform the same flip at every slice of the \(3k\)-step history; all temporal plaquettes are unchanged. It fixes \(O_L\) and negates both \(\Psi_j\). Therefore
\[
\mathbb E_{\mu_{3,0}}[B_kf(U_-)\mid O_L]=0,
\qquad
\boxed{
d_s=-sB_kf(U_-)+O(s^2),\quad
\|d_s\|_{\mu_{3,s}}^2
=s^2\left(\frac{b_0(k)^2}{4}+\frac{3b_1(k)^2}{4}\right)+O(s^3).}
\tag{AP16}
\]
Analytic kernels and uniformly positive finite-graph marginals justify these expansions in the actual varying norm. The coefficient is strictly positive by \(b_0(k)>0\). This is a three-slab conditional calculation, not a substitution of the equal-time marginal.

The leaked direction is itself an explicit bounded joint Wilson source:
\[
B_kf=b_1(k)fg+\frac{b_0(k)-b_1(k)}2\chi_{1/2}(pq^{-1}).
\]
With this fixed mixed probe,
\[
\left.\partial_s\mathbb E_{\mu_{3,s}}
[d_s B_kf(U_-)]\right|_0
=-\|B_kf\|_{\rm Haar}^2<0.
\tag{AP17}
\]
Every retained left-only outer mark is orthogonal to \(d_s\) by definition; the actual outer-loop mark detects what it misses. Static marginal agreement and a trivial separator-conditioned cap therefore do not supply chronological source closure.

## A spectral edge can soften while the fixed source hardens

The right potential preserves the center parity of a left-exclusive edge. In the left-odd physical sector, \(f=\Psi_{(1/2,1/2,0)}\) has the unique largest free multiplier \(\alpha\). Indeed \(j_p\) must be half-integer. If \(j_q=0\), admissibility gives \(j_e=j_p\) and multiplier \(t_{j_p}^4\), with equality only at \(j_p=1/2\). If \(j_e=0\), the multiplier is \(t_{j_p}^6<\alpha\); if both \(j_e,j_q>0\), it is at most \(t^7<\alpha\). Strict multiplier ordering treats all higher spins.

Let \(\Lambda_L(s)\) be this simple top eigenvalue continued in \(B_s\), and \(\theta_L(s)=\Lambda_L(s)/\Lambda_s\). Its first derivative vanishes. The second-order eigenvalue formula uses only the two channels (AP3):
\[
\frac{\Lambda_L''(0)}{\alpha}
=\sum_jw_j\frac{\alpha+\beta_j}{\alpha-\beta_j},\qquad
(\log\theta_L)''_0
=\sum_jw_j\frac{\alpha+\beta_j}{\alpha-\beta_j}
 -\frac{1+\alpha}{1-\alpha}.
\tag{AP18}
\]
To check the numerator, \(B'_0f\) has channel coefficient \(c_j(\alpha+\beta_j)/2\), while
\(\langle f,B''_0f\rangle=\sum_jw_j(\alpha+\beta_j)/2\).
Adding the resolvent contributions \(2|\langle\Psi_j,B'_0f\rangle|^2/(\alpha-\beta_j)\) gives the displayed expression.

Using (AP11), it simplifies to
\[
\boxed{
(\log\theta_L)''_0
=\frac{2t^2[t'(x)+t^3/x]}
        {(1-t^4)(1-t^2v)}>0,\qquad
E_L''(0)=-a_t^{-1}(\log\theta_L)''_0<0,}
\tag{AP19}
\]
where \(E_L=-a_t^{-1}\log\theta_L\) is the lowest left-odd energy for sufficiently small \(s\). Thus this actual sector edge softens at every temporal coupling, including the regime in (AP14) where the fixed source's normalized surplus hardens. The source redistributes among chronological eigenmodes; its quotient does not determine the spectral infimum.

The full physical gap also decreases from this free starting point. At \(s=0\), \(\alpha\) is the largest nonvacuum multiplier, with multiplicity two, carried by \(f\) and \(g\). If only one outer spin is nonzero, admissibility gives its fourth-power multiplier; if both are nonzero, their outer paths already bound the multiplier by \(t^6<\alpha\). Hence \(\Delta(0)=-a_t^{-1}\log\alpha=E_L(0)\). The right-edge center flip makes the continued left-odd eigenvalue even in \(s\), so (AP19) implies
\[
\boxed{\Delta(s)\le E_L(s)<\Delta(0)}
\qquad\text{for every fixed }x>0
\text{ and sufficiently small }s>0.
\tag{AP20}
\]
The Taylor remainder for \(E_L\) is \(O(s^4)\). No decision about which split physical branch is lowest is needed for this upper bound. At large fixed \(x\), the normalized source quotient therefore improves while the actual full finite-system gap decreases.

This is an interacting finite-graph response with a retained physical clock, not a gap-closing limit. It rejects automatic positivity of an adjacent-block surplus and identifies the missing comparison: control the complete transported source and lag terms on the full innovation carrier, including charged interface channels, rather than infer that control from unchanged regional states or one improving source quotient.

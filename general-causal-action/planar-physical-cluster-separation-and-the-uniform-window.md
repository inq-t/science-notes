# Planar Physical Cluster Separation and the Uniform Window

The planar harmonic vacuum and first physical scalar excitation are simple and isolated from the rest of the complete Gauss-invariant spectrum by explicit constants divided by \(L+1\). The next level is a two-dimensional scalar cluster, whose upper separation has the same scale. These elementary bounds turn a quantitative ordered-eigenvalue comparison into uniform compact spectral isolation and residual-to-projector estimates. They do not assume that the actual compact comparison has already been proved.

**Status: exact harmonic spectrum and conditional perturbation criterion.** [[planar-patch-confinement-and-the-spatial-soft-mode|PP]] fixes the open square patch with every boundary vertex gauged. [[compact-source-normalization-and-the-nonlinear-return|CS]] supplies the fixed-patch expansion. [[uniform-marked-well-return-and-the-growing-patch-test|GW]] asks for estimates uniform in the growing patch; the separation below identifies one precise input for that test.

## The complete scalar carrier determines the first clusters

Put \(n=L+1\), \(a=\pi/(2n)\), and let
\[
\omega_{rs}=\sqrt{4-2\cos(r\pi/n)-2\cos(s\pi/n)},\qquad
1\le r,s\le L .
\]
The oscillator vacuum energy and its centered operator are
\[
\mathcal E_{0,L}=\frac32\sum_{r,s}\omega_{rs},\qquad
K_L=\mathcal O_L-\mathcal E_{0,L}.
\tag{PS1}
\]
Every spatial mode has three color creation operators transforming together as the adjoint representation of \(SU(2)\), equivalently the vector representation of \(SO(3)\). The physical carrier is the invariant part of this entire oscillator Fock space. It is not the product of the individual mode-scalar spaces.

The vacuum is the unique zero-quantum state. A one-quantum vector is spin one and has no scalar component. At two quanta, each unordered pair of spatial modes \(\{\alpha,\beta\}\), including \(\alpha=\beta\), supplies exactly one scalar:
\[
\sum_{b=1}^3 a^\dagger_{\alpha,b}a^\dagger_{\beta,b}\Omega .
\tag{PS2}
\]
Distinct unordered pairs are orthogonal by mode occupation. Their excitation energies are \(\omega_\alpha+\omega_\beta\). Three or more quanta cost at least three times the smallest spatial frequency. Thus the entire physical spectrum below that threshold consists of the vacuum and these two-quantum scalar pairs. Accidental frequency sums are counted with their full multiplicities.

For \(L\ge2\), write
\[
\omega=\omega_{11}=2\sqrt2\sin a,\qquad
\nu=\omega_{12}=\omega_{21}
=\omega\sqrt{\frac12+2\cos^2a},\qquad
\zeta=\omega_{22}=2\omega\cos a .
\tag{PS3}
\]
The smallest frequency \(\omega\) is simple. The second frequency \(\nu\) occurs exactly twice: monotonicity in each spatial index rules out any other mode at that value.

The third distinct frequency is \(\zeta\). For \(L=2\), it is the only remaining mode. For \(L\ge3\), the only competing lowest candidate is \(\omega_{13}=\omega_{31}\). With \(u=\cos(\pi/n)\),
\[
\omega_{13}^2-\omega_{22}^2=4(1-u)(2u^2-1)\ge0 .
\]
Equality holds only at \(n=4\), or \(L=3\); hence \(\zeta\) has multiplicity three there, from \(22,13,31\), and multiplicity one at every other \(L\ge2\).

Since \(\nu<2\omega\), \(\zeta<2\omega\), and
\[
2\sqrt{\frac12+2\cos^2a}>1+2\cos a ,
\]
the first ordered physical excitation energies, including multiplicity, are
\[
\boxed{
e_{0,L}=0,\qquad
e_{1,L}=2\omega=:c_L,\qquad
e_{2,L}=e_{3,L}=\omega+\nu,\qquad
e_{4,L}=\omega+\zeta .}
\tag{PS4}
\]
The last displayed level is the next distinct level; it has multiplicity three at \(L=3\) and one otherwise. The inequality comparing \(2\nu\) with \(\omega+\zeta\) follows by squaring: their squared difference in units of \(\omega^2\) is \((2\cos a-1)^2>0\). All displayed nonzero levels lie below \(3\omega\), so higher-particle invariant sectors cannot intrude.

For \(L=1\), there is one three-component oscillator with frequency \(2\). Its invariant states are the radial scalar states, with simple excitation energies
\[
e_{m,1}=4m,\qquad m=0,1,2,\ldots .
\tag{PS5}
\]
This exceptional case has no two-dimensional cluster.

## Explicit lower separations scale as \(1/n\)

For \(n\ge3\), \(a\le\pi/6\), so \(\cos a\ge\sqrt3/2\). Concavity of sine on \([0,\pi/6]\) gives \(\sin a\ge3/(2n)\). Therefore
\[
\nu-\omega
\ge(\sqrt2-1)\omega
\ge\frac{3(2-\sqrt2)}n .
\]
The function \(F(t)=2t-\sqrt{1/2+2t^2}\) is strictly increasing for \(t\ge0\). Evaluating it at \(\sqrt3/2\) gives
\[
\zeta-\nu
\ge(\sqrt3-\sqrt2)\omega
\ge\frac{3(\sqrt6-2)}n .
\]
Define
\[
\boxed{A_*=3(2-\sqrt2),\qquad B_*=3(\sqrt6-2),\qquad
0<B_*<A_* .}
\tag{PS6}
\]
Both constants are sharp uniform constants for their respective separations over \(L\ge2\): equality holds on the four-face patch \(L=2\).

For every \(L\ge1\), the sine chord bound on \([0,\pi/4]\) also gives
\[
\boxed{\frac8n\le c_L\le\frac{2\sqrt2\pi}{n}.}
\tag{PS7}
\]
Combining (PS4)–(PS7),
\[
\operatorname{dist}\!\left(c_L,\,
\sigma(K_L)\setminus\{c_L\}\right)\ge\frac{A_*}{n}
\qquad(L\ge1).
\tag{PS8}
\]
For \(L\ge2\), the rank-two cluster at \(\omega+\nu\) has distance at least \(B_*/n\) from both neighboring distinct levels. Consequently intervals of radius \(B_*/(4n)\) around the vacuum, first scalar level and double cluster are disjoint and contain precisely the indicated harmonic ranks.

In particular,
\[
\|K_L^{-1}\|_{\Omega^\perp}\le\frac n8,\qquad
\|(K_L-c_L)^{-1}\|_{\phi^\perp,\,{\rm phys}}\le\frac n{A_*}.
\tag{PS9}
\]
The second inverse is taken in the complete physical carrier; deleting only the scalar vector from the full colored carrier would leave non-scalar states at the same energy. The stronger odd-sector bounds in CS13 remain available for odd perturbative correctors.

## Ordered comparison is sufficient for actual compact isolation

Let \(\mathsf A_{L,h}\) be a semibounded self-adjoint operator with compact resolvent on its actual physical Hilbert space, with ordered eigenvalues \(\Lambda_{j,L,h}\), counting multiplicity. It need not act on the harmonic Hilbert space. Assume a quantitative comparison of the **ordered** levels:
\[
\boxed{
\left|\Lambda_{j,L,h}-(\mathcal E_{0,L}+e_{j,L})\right|
\le\delta_{L,h},\qquad j=0,1,2,\qquad
\delta_{L,h}\le\frac{A_*}{4n}.}
\tag{PS10}
\]
This is an explicit hypothesis, not a consequence of a small quasimode residual alone. A proof normally needs both upper trial spaces and a lower min–max comparison excluding additional low compact states.

Subtracting the inequalities in (PS10) proves
\[
\begin{aligned}
\left|(\Lambda_1-\Lambda_0)-c_L\right|&\le2\delta_{L,h},\\
\Lambda_1-\Lambda_0&\ge\frac{8-A_*/2}{n}>0,\\
\Lambda_2-\Lambda_1&\ge\frac{A_*}{2n}>0 .
\end{aligned}
\tag{PS11}
\]
Thus the actual vacuum and first physical excitation are simple. Their spectral projections \(P_{0,L,h},P_{1,L,h}\) are isolated uniformly on the \(1/n\) scale. The actual vacuum-subtracted inverse is bounded by
\(n/(8-A_*/2)\).

For \(j=0,1\), let \(v\) be a normalized vector in the domain of \(\mathsf A_{L,h}\), and choose an approximate energy \(z\) satisfying
\[
\left|z-(\mathcal E_{0,L}+e_{j,L})\right|\le\frac{A_*}{4n}.
\]
Every actual spectral value outside the target eigenline is then at distance at least \(A_*/(2n)\) from \(z\). The spectral theorem gives the typed residual estimate
\[
\boxed{
\|(I-P_{j,L,h})v\|
\le\frac{2n}{A_*}\|(\mathsf A_{L,h}-z)v\| .}
\tag{PS12}
\]
This uses no operator-norm resolvent identification between compact and harmonic carriers. If the right-hand side tends to zero, it controls the norm distance to the selected line; an isometric source or chart map is still needed to identify its vector with a specified harmonic state.

To protect the rank-two third cluster as a whole, require the comparison through indices \(j=0,\ldots,4\), with \(\delta_{L,h}\le B_*/(4n)\). An interval of radius \(B_*/(2n)\) around \(\mathcal E_{0,L}+\omega+\nu\) then has actual rank two. The comparison permits internal splitting and does not select two canonical eigenlines. Controlling only indices \(0,1,2\) does not establish this rank-two assertion.

## The actual coarse comparison supplies the isolation input

[[uniform-planar-localization-and-the-first-physical-levels|UP1–12]] proves for the actual scaled compact operator \(H_{L,g}/\sqrt{\kappa g}\) that
\[
\left|\Lambda_{j,L,h}-(\mathcal E_{0,L}+e_{j,L})\right|
\le C\epsilon^{2/3}n^{-4},\qquad
\epsilon=h n^{10},\qquad j=0,1,2
\tag{PS13}
\]
satisfies (PS10) throughout a size-independent sufficiently small \(\epsilon\)-window. Indeed
\(\delta_{L,h}n\le C\epsilon^{2/3}n^{-3}\), and a fixed choice of the window makes this less than \(A_*/4\) for every \(n\ge2\). An analogous bound through index four would protect the next double cluster.

The harmonic absolute energies relevant to this comparison obey
\(\mathcal E_{0,L}\le3\sqrt2\,L^2\), and their displayed excitation energies are \(O(1/n)\). A relative form error multiplying the uncentered oscillator therefore carries an \(O(n^2)\) vacuum-energy factor. It cannot be treated as an error only of the order of the gap. High-dimensional Gaussian cutoffs must likewise retain their dependence on the \(3L^2\) variables, for example through normalized fixed-degree moments or an explicit Gaussian moment-generating bound.

The compact proof of (PS13) is supplied by UP's lower and upper min–max comparison. This isolation selects the actual eigenbranches in [[uniform-nonlinear-planar-gap-and-marked-response|uniform nonlinear return]]. The additional operator and cutoff residuals give the eigenvalue remainder, while the [[uniform-centered-poisson-return-and-the-planar-source|centered Poisson construction]] retains the moving vacuum, source mean and variance in the susceptibility bound. The harmonic counting here supplies the spectral separation factors in those proofs.

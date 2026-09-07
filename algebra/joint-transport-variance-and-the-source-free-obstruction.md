# Joint Transport Variance and the Source-Free Obstruction

A constant Hermitian connection gives its transported probe a positive spectral edge exactly when its component matrices have no common eigenvector. The edge is the least total variance of those matrices on one unit vector. This is an exact continuum statement, but it does not make the background a vacuum: a constant source-free magnetic Yang–Mills stationary point must have commuting components, so this particular probe edge then vanishes. The distinction identifies what a proposed arena-making law must supply beyond incompatible transport on a previously specified arena.

## The operator acts on a probe section

Fix Euclidean \(\mathbb R^d\), Lebesgue measure, and a finite-dimensional fiber \(\mathbb C^r\). Let \(B_1,\ldots,B_d\) be constant Hermitian matrices. On
\(\mathcal H=L^2(\mathbb R^d,\mathbb C^r)\), define
\[
P_j=-i\partial_j,\qquad
L_B=\sum_{j=1}^d(P_j-B_j)^2.
\tag{JV1}
\]
The corresponding closed form is
\[
q_B[f]=\sum_j\|(P_j-B_j)f\|_2^2,\qquad
\operatorname{Dom}q_B=H^1(\mathbb R^d,\mathbb C^r).
\tag{JV2}
\]
Its operator domain is \(H^2\), and Schwartz functions are an operator and form core. Fourier transformation gives the Hermitian polynomial symbol
\[
L_B(p)=|p|^2I-2\sum_jp_jB_j+\sum_jB_j^2.
\tag{JV3}
\]
Boundedness of the matrices makes the form norm equivalent to the \(H^1\) norm and the operator graph norm equivalent to the \(H^2\) norm. In particular the cross term grows only linearly in \(|p|\), while the leading term is \(|p|^2I\).

The input \(f(x)\) is a section transported by a **fixed** connection. It is not a wavefunction on the space of connections. The matrices, spatial arena and metric have already been supplied.

## The exact joint-variance edge

For a unit vector \(z\in\mathbb C^r\), put
\[
b_j(z)=\langle z,B_jz\rangle\in\mathbb R,\qquad
V_B(z)=\sum_j\left(\langle z,B_j^2z\rangle-b_j(z)^2\right).
\]
Completing the square gives
\[
\boxed{
\langle z,L_B(p)z\rangle
=|p-b(z)|^2+V_B(z),\qquad
V_B(z)=\sum_j\|(B_j-b_j(z)I)z\|^2.}
\tag{JV4}
\]
Consequently,
\[
\boxed{
\kappa(B):=\inf\sigma(L_B)
=\min_{\|z\|=1}V_B(z).}
\tag{JV5}
\]
Indeed the bottom is the infimum of (JV4) over \(p,z\). Minimization over \(p\) sets \(p=b(z)\), and continuity on the finite-dimensional unit sphere supplies a minimizing \(z_*\). At \(p_*=b(z_*)\), its Rayleigh value equals the global minimum, so it is also a lowest eigenvector of the matrix \(L_B(p_*)\).

This matrix eigenvector is not a normalizable spatial vacuum. The function
\(\lambda_{\min}(L_B(p))\) is continuous, tends to infinity as \(|p|\to\infty\), and takes every value from its minimum onward. Thus
\(\sigma(L_B)=[\kappa(B),\infty)\).
There is no \(L^2\) eigenvector at the bottom: the nonzero polynomial
\(\det(L_B(p)-\kappa I)\), with leading term \(|p|^{2r}\), vanishes only on a set of Lebesgue measure zero. Wave packets approaching a minimizing momentum realize the spectral infimum.

Since every summand in (JV4) is nonnegative,
\[
\boxed{\kappa(B)=0
\quad\Longleftrightarrow\quad
B_1,\ldots,B_d\text{ have a common eigenvector}.}
\tag{JV6}
\]
Pairwise noncommutation alone is insufficient. For instance,
\(B_1=0\oplus\sigma_1\) and \(B_2=0\oplus\sigma_2\) do not commute, but share the first coordinate as an eigenvector and have zero edge.

Finite fiber dimension is load-bearing. On \(\bigoplus_{n\ge1}\mathbb C^2\), the bounded matrices
\(B_1=\bigoplus_n n^{-1}\sigma_1\) and
\(B_2=\bigoplus_n n^{-1}\sigma_2\)
have no common eigenvector, yet their variance infimum is zero. Absence of an exactly compatible vector does not uniformly exclude almost-compatible ones on that carrier.

## Presentation changes and the supplied scale

The variance and edge obey
\[
\kappa(UB_1U^*,\ldots,UB_dU^*)=\kappa(B),\qquad
\kappa(B_1+\beta_1I,\ldots,B_d+\beta_dI)=\kappa(B),
\tag{JV7}
\]
for constant unitary \(U\) and real \(\beta_j\). The first identity changes the fiber frame; the second changes only \(b(z)\), not its variance. On \(\mathbb R^d\), multiplication by \(e^{i\beta\cdot x}\) implements
\(L_{B+\beta I}=U_\beta L_BU_\beta^*\).
On a torus that multiplication need not preserve periodic boundary conditions, so no unrestricted finite-volume shift claim follows.

For real \(s\),
\[
\kappa(sB)=s^2\kappa(B).
\tag{JV8}
\]
If the chosen clock is \(A_B=\sqrt{L_B}\), its lower rate scales as
\(|s|\sqrt{\kappa(B)}\). This uses the
[[cauchy-response-and-local-action|square-response clock prescription]];
it does not derive a conversion into physical mass. The \(B_j\) have the same inverse-length type as \(P_j\). Their nonzero magnitude is still an input.

This also separates the present family from
[[pauli-transport-and-the-continuum-scaling-obstruction|fixed Pauli links under spatial refinement]].
The [[refining-holonomy-and-a-finite-continuum-threshold|smooth-connection discretization]] uses transports \(e^{iaB_j}\to I\), rather than keeping each link equal to \(\sigma_j\). It changes the holonomy with scale and lies outside that fixed-transport obstruction.

## Pauli components give an explicit positive probe edge

Let \(B_j=g\sigma_j\), \(d=2\) or \(3\), \(g\ne0\). For a pure qubit vector, its Bloch components satisfy \(\sum_{j=1}^3n_j^2=1\), so
\[
V_B(z)=g^2\left(d-\sum_{j=1}^dn_j^2\right),\qquad
\boxed{\kappa(B)=(d-1)g^2.}
\tag{JV9}
\]
The complete symbol confirms the same result:
\[
\lambda_\pm(p)=|p|^2+dg^2\pm2|g|\,|p|
=(|p|\pm|g|)^2+(d-1)g^2.
\tag{JV10}
\]
The lower minimum occurs on \(|p|=|g|\), not at zero momentum. Even though the expression is rotationally symmetric, it is not the massive relativistic dispersion \(|p|^2+m^2\). A positive lower clock rate alone is not a Lorentz mass Casimir.

Already two components produce the effect. The general variance theorem holds for every \(d\), and adding zero components embeds a two-direction example in higher dimensions. It selects neither three spatial dimensions nor a gauge group.

## Source-free constant Yang–Mills backgrounds remove this edge

Now impose an additional equation on the background itself. For a constant, time-independent, purely magnetic Hermitian connection, source-free classical Yang–Mills stationarity requires
\[
S_j(B):=\sum_i[B_i,[B_i,B_j]]=0
\quad\text{for every }j.
\tag{JV11}
\]
These are the stationary equations of the magnetic density
\[
\Phi(B)=\frac12\sum_{i<j}\|[B_i,B_j]\|_{\rm HS}^2
\]
in the real trace metric on Hermitian matrices. An overall positive coupling does not change their zero set. This is a finite matrix calculation at a spatial point, not an integral of a constant nonzero density over infinite volume.

Cyclicity of trace gives
\[
\boxed{
\sum_j\operatorname{Tr}(B_jS_j(B))
=\sum_{i,j}\|[B_i,B_j]\|_{\rm HS}^2
=4\Phi(B).}
\tag{JV12}
\]
Thus (JV11) forces every commutator to vanish. Commuting finite Hermitian matrices have a common eigenbasis, so
\[
\boxed{
\text{constant source-free magnetic stationarity}
\quad\Longrightarrow\quad
\kappa(B)=0.}
\tag{JV13}
\]
For the Pauli example,
\[
S_j(B)=4(d-1)g^3\sigma_j
=4(d-1)g^2B_j\ne0.
\tag{JV14}
\]
Its positive probe edge is therefore obtained on a background that does not satisfy these source-free stationary equations.

The [[directed-analytic-realization/chern-simons-response-and-gauge-action|transgression return]] supplies the separate magnetic action and canonical gauge prescription.
The [[directed-analytic-realization/compact-lie-gauge-positive-realization|homogeneous quantum construction]] instead makes the matrices themselves configuration variables, adds their kinetic derivatives and constructs a vacuum of that different operator. The classical stationary-point conclusion above does not exclude that quantum gap, time-dependent solutions, spatially varying fields or another specified source law.

Nor is \(L_B\) the gauge-field Hessian. Varying a Yang–Mills connection produces a vector-valued operator with curvature terms and gauge constraints, on a different carrier. A probe estimate cannot be transferred to that operator by relabeling its argument.

The constructive diagnostic is therefore twofold: joint transport variance exactly measures one obstruction to compatible probe propagation; background selection must separately make that transport part of an actual law and state. A proposed arena-making operator must return both sides of that relation. The present calculation neither constructs such an arena nor identifies its scale exchange rate. It rules out only the shortcut from an incompatible supplied background to a source-free Yang–Mills vacuum and its physical mass gap.

[[directed-analytic-realization/refining_holonomy_receipt.py|The shared refining-holonomy receipt]] checks the variance decomposition and source double commutators; [[directed-analytic-realization/refining-holonomy-receipt-output.txt|its output]] distinguishes these finite checks from the continuum spectral proof.

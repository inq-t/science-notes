# A Finite Spectral Wall

The two-level matrix algebra provides a complete debugging model of spectral wall descent. A Dirac operator selects a maximal commutative readout, its conditional expectation produces an exact entropy and BKM loss, relative \(K\)-theory produces a binary zero-sum class, and the bulk spectral action remains constant along conjugacy orbits even when the fixed-context wall entropy changes.

## A finite real spectral datum

Let

$$
\mathcal A=M_2(\mathbb C),
\qquad
\mathcal H=M_2(\mathbb C)
$$

with the Hilbert--Schmidt inner product, left representation \(\pi(a)=L_a\), and real structure

$$
J(X)=X^*.
$$

For

$$
h=m\sigma_z,
\qquad m>0,
$$

define

$$
D_h:=L_h+R_h.
$$

Then

$$
[D_h,L_a]=L_{[h,a]},
\qquad
[[D_h,L_a],R_b]=0.
$$

All spectral-triple boundedness and compactness conditions are automatic in finite dimension. The spectrum is

$$
\operatorname{Spec}(D_h)=\{-2m,0,0,2m\}.
$$

The algebra is simple and factorial. Moreover, \(PU(2)\) acts by inner automorphisms transitively on the fixed-spectrum directions \(uhu^*\), so the family of spectral contexts is a homogeneous orbit even though no microscopic classical space has been introduced.

For a traceless inner fluctuation

$$
h_\phi=m\sigma_z+\phi_x\sigma_x+\phi_y\sigma_y,
\qquad
r:=\sqrt{m^2+\phi_x^2+\phi_y^2},
$$

one has

$$
\operatorname{Spec}(D_{h_\phi})
=\{-2r,0,0,2r\},
$$

and therefore

$$
\operatorname{Tr}D_{h_\phi}^2=8r^2,
\qquad
\operatorname{Tr}D_{h_\phi}^4=32r^4,
$$

$$
\operatorname{Tr}e^{-tD_{h_\phi}^2}
=2+2e^{-4tr^2}.
$$

These spectral actions depend on the orbit radius \(r\), not on an orientation inside the orbit.

## The spectral readout

The commutant of \(h\) inside \(\mathcal A\) is the diagonal maximal abelian subalgebra

$$
\mathcal B_h=\{h\}'\cong\mathbb C^2.
$$

Let \(P_\pm\) be the spectral projections of \(h\). The trace-preserving conditional expectation is

$$
\boxed{
E_h(X)
=P_+XP_++P_-XP_-
=\frac12(X+\sigma_zX\sigma_z).}
$$

The same map is determined by the Dirac generator:

$$
\boxed{
E_h(X)
=X-\frac{1}{4m^2}[h,[h,X]].}
$$

Thus the wall removes precisely the double-commutator component that fails to commute with the spectral direction.

Use the density-tangent Hessian convention for the BKM metric. For a faithful state \(\rho\) commuting with \(h\), \(E_h\) is BKM-orthogonal on self-adjoint trace-zero density tangents. Hence

$$
g_\rho(X,X)
=g_\rho(E_hX,E_hX)
+g_\rho((1-E_h)X,(1-E_h)X).
$$

For an off-diagonal Hermitian density tangent \(A\),

$$
\boxed{
g_\rho(A,A)
=\frac{1}{4m^2}
g_\rho(i[h,A],i[h,A]).}
$$

This is a positive Dirac-derived wall cost. It is not the Hessian of the raw spectral action.

## Exact entropy variation on a conjugacy orbit

Let

$$
\rho_0=\operatorname{diag}(p,1-p),
\qquad
\frac12<p<1,
$$

and rotate it through

$$
\rho_\theta
=U_\theta\rho_0U_\theta^*,
\qquad
U_\theta=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}.
$$

The spectrum and von Neumann entropy of \(\rho_\theta\) are constant. Its fixed-context wall defect is

$$
\Sigma_h(\theta)
=D(\rho_\theta\Vert E_h\rho_\theta)
=S(E_h\rho_\theta)-S(\rho_0).
$$

At the aligned context,

$$
\Sigma_h(0)=0.
$$

At maximal misalignment,

$$
E_h\rho_{\pi/4}=\frac{\mathbf1}{2},
$$

and therefore

$$
\boxed{
\Sigma_h(\pi/4)
=\ln2-h_2(p).}
$$

Near \(\theta=0\),

$$
\boxed{
\Sigma_h(\theta)
=(2p-1)\ln\frac{p}{1-p}\,\theta^2
+O(\theta^4).}
$$

Consequently,

$$
\left.\frac{\mathrm d^2\Sigma_h}{\mathrm d\theta^2}\right|_0
=2(2p-1)\ln\frac{p}{1-p},
$$

which equals the BKM norm of the unitary-orbit tangent. For \(p=0.8\),

$$
\Sigma_h(\pi/4)
\simeq0.192744757,
\qquad
\Sigma_h''(0)
\simeq1.663553233.
$$

Meanwhile any bulk spectral action of the conjugated Dirac operator \(U_\theta hU_\theta^*\) is constant in \(\theta\). This proves the finite conjugacy-orbit no-go in [[spectral-wall-descent/observable-spectral-action|the observable-action note]].

## Relative \(K\)-theory and the binary distinction

For the inclusion

$$
\mathbb C^2\cong\mathcal B_h
\hookrightarrow
M_2(\mathbb C),
$$

the map on \(K_0\) is

$$
\mathbb Z^2\longrightarrow\mathbb Z,
\qquad
(k_+,k_-)\longmapsto k_++k_-.
$$

With the shifted mapping-cone convention \(K_j(\mathcal A,\mathcal B):=K_{j+1}(C_i)\) fixed in [[spectral-wall-descent/index-and-curvature-transgression#Relative K-theory of an observable context|the relative \(K\)-theory note]], the relative groups are therefore

$$
\boxed{
K_0(M_2,\mathbb C^2)=0,
\qquad
K_1(M_2,\mathbb C^2)
\cong\mathbb Z(1,-1).}
$$

The homogeneous vector \((1,1)\) survives as total rank. The contextual difference \((1,-1)\) vanishes in the homogeneous simple algebra but survives as the relative wall class. This is the integer skeleton of the binary mean-zero sector; its BKM norm remains state dependent.

## What the model establishes

The finite model constructs, without unitarity or energy conservation,

- a homogeneous noncommutative algebra;
- a Dirac-selected commutative context;
- an exact nonunitary expectation;
- entropy gain equal to lost distinction;
- a positive Dirac-commutator wall response;
- a relative zero-sum \(K\)-class; and
- a proof that bulk spectral action cannot determine wall entropy.

It does not construct a causal wall, Lorentzian spacetime, gravity, or fact selection. Those are precisely the carrier, soldering, and record obligations exposed by the model.

## Receipt

[[spectral-wall-descent/receipts/verify-spectral-wall.py|The verification receipt]] checks the spectra, trace moments, entropy identity, entropy-defect Hessian, kernel of the relative rank map, and mixed-response jet by matrix diagonalization and finite differences. The analytic BKM identification and full mapping-cone sequence are proved in the notes rather than independently reconstructed by the script.

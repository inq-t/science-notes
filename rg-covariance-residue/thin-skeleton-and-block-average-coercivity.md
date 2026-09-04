# Thin Skeletons and Block-Average Coercivity

A coarse variable can be smooth, gauge covariant, and exactly disintegrable while failing to retain long-wavelength information. Straight path products on a sparse coarse skeleton provide an explicit example: their fiber contains transverse, nonharmonic Maxwell variations whose physical stiffness tends to zero under simultaneous refinement and volume growth. Volume averages satisfy a different, uniform block Poincare estimate. This distinguishes a valid change of variables from a valid ultraviolet separation; neither estimate is a quantum mass-gap theorem.

## The carrier and the quantity being tested

Take the four-dimensional periodic lattice
\(\Lambda_N=(\mathbb Z/N\mathbb Z)^4\), with
$$
N=Mn,\qquad n,M\ge3,\qquad a=b/n,\qquad R=Na=Mb.
\tag{TS1}
$$
Here \(a\) is fine spacing, \(b\) coarse spacing, and \(R\) the physical side length. Retain the straight coordinate paths of \(n\) fine links starting at coarse vertices \(n\mathbb Z^4\). These are an instance of [[wilson-path-product-fibers|the exact path-product carrier]]. Repeated aligned straight blocking can produce the same composite map.

At the identity connection, write its normalized linearization as
$$
(Q_bA)_\mu(y)=\frac1n\sum_{j=0}^{n-1}A_\mu(y+je_\mu).
\tag{TS2}
$$
The raw path sum has the same kernel. For a Lie-algebra-valued link field with a fixed inner product, define
$$
\begin{aligned}
\|A\|_a^2&=a^4\sum_{x,\mu}|A_\mu(x)|^2,\\
q_a(A)&=a^2\sum_{x,\mu<\nu}
|\nabla_\mu^{\rm lat}A_\nu(x)-\nabla_\nu^{\rm lat}A_\mu(x)|^2,\\
\nabla_\mu^{\rm lat}u(x)&=u(x+e_\mu)-u(x).
\end{aligned}
\tag{TS3}
$$

The operator here is the linear Maxwell configuration Hessian on link variations. Its Rayleigh quotient \(q_a(A)/\|A\|_a^2\) has units of inverse length squared. It is not the physical Hamiltonian acting on gauge-invariant quantum states.

The proposed geometric ultraviolet condition would be
$$
q_a(A)\ge c\,b^{-2}\|A\|_a^2
\quad\text{on }\ker Q_b
\text{ after removing gauge and harmonic directions},
\tag{TS4}
$$
with \(c>0\) independent of refinement and volume. For this composite skeleton, (TS4) is false.

## An exact blind direction

Write \(z=(x_2,x_3,x_4)\), fix a unit Lie-algebra direction \(T\), and put
$$
\begin{aligned}
H&=(n\mathbb Z/N\mathbb Z)^3,\\
s(z)&=\sin(2\pi x_2/N),\qquad
f(z)=s(z)(1-\mathbf1_H(z)),\\
A_1(x)&=f(z)T,\qquad A_\nu(x)=0\quad(\nu\ne1).
\end{aligned}
\tag{TS5}
$$

Every retained path in direction \(1\) has transverse coordinates in \(H\), where \(f=0\). The other components vanish. Thus \(Q_bA=0\).

This is not a pure-gauge artifact. The discrete divergence vanishes because \(A_1\) is independent of \(x_1\). Both the full sine sum and its sum over \(H\) vanish, so \(A\) has zero mean. On the periodic linearized complex it is therefore orthogonal to gradients and harmonic one-forms. Its curl is nonzero.

Let \(L_\perp\) be the positive unit-spacing transverse Laplacian. Then
$$
L_\perp s=\lambda s,\qquad
\lambda=4\sin^2(\pi/N),\qquad
\|s\|^2=N^3/2.
\tag{TS6}
$$
For \(r=s\mathbf1_H\), the holes are nonadjacent and
$$
\|r\|^2=M^3/2,\qquad
\langle r,L_\perp r\rangle=6\|r\|^2,\qquad
\langle r,L_\perp s\rangle=\lambda\|r\|^2.
\tag{TS7}
$$
Since \(f=s-r\),
$$
\begin{aligned}
\|f\|^2&=(N^3-M^3)/2,\\
\langle f,L_\perp f\rangle
&=\bigl[\lambda N^3+(6-2\lambda)M^3\bigr]/2.
\end{aligned}
\tag{TS8}
$$
The four-dimensional norm and curl sum acquire the same factor \(N\). Consequently,
$$
\boxed{
\mathcal R_{n,M}:=\frac{q_a(A)}{\|A\|_a^2}
=\frac{\lambda}{a^2}
+\frac{6-\lambda}{a^2(n^3-1)}
\le
\frac{4\pi^2}{(Mb)^2}
+\frac{6a}{b^3(1-n^{-3})}.}
\tag{TS9}
$$

At fixed \(b\), take \(M=n\to\infty\). Then \(b^2\mathcal R_{n,n}\to0\), disproving (TS4). The long-wave sine has been modified only on a thin array of lines; the correction's stiffness vanishes with refinement. No continuum capacity theorem is needed for this finite-lattice calculation.

## The blind direction remains in the nonlinear fiber

For any compact matrix gauge group with \(T\) in its Lie algebra, set
$$
U_1(x;t)=\exp(ta f(z)T),\qquad U_\nu(x;t)=1\quad(\nu\ne1).
\tag{TS10}
$$
Every retained path product is exactly the identity, for every \(t\). Nevertheless,
$$
U_{1j}(x;t)
=\exp\!\bigl(ta[f(z)-f(z+e_j)]T\bigr)
\tag{TS11}
$$
is nontrivial on some plaquettes for sufficiently small nonzero \(t\). A unitary representation with \(\mathrm d\mathsf R(T)\ne0\) detects this through its plaquette character. These configurations are not gauge-equivalent to the identity.

For the Wilson normalization in (WP10),
$$
\left.\frac{\mathrm d^2}{\mathrm dt^2}S_\beta(U(t))\right|_{t=0}
=\beta\chi_{\mathsf R}\,q_a(A),\qquad
\chi_{\mathsf R}
=-\frac{\operatorname{ReTr}(\mathrm d\mathsf R(T)^2)}
{d_{\mathsf R}}>0.
\tag{TS12}
$$
All varied links are unused by the retained skeleton. Thus pivot compensation and the product-chart metric issue do not explain away this witness.

Several limits are essential. A fixed adjacent blocking factor \(n=L\) does not follow the sequence above: its correction term remains of order \(b^{-2}\). The counterexample therefore does not disprove an adjacent-shell estimate. Nor does a soft classical Hessian direction prove failure of a nonlinear conditional Poincare inequality, an actual gauge-invariant correlation bound, or the quantum Yang--Mills gap. A fixed-color tangent is not a singlet Hilbert-space excitation. Even multiplication of (TS9) by a logarithmically growing \(\beta_n\) remains soft along \(M=n\); this is still only a bare-Hessian statement.

## What volume averaging changes

For a scalar field on a cell of \(n^d\) sites, retain its mean. Give the cell only its internal nearest-neighbor edges, so its positive Laplacian has Neumann graph boundary conditions. On the mean-zero subspace, its exact physical first eigenvalue is
$$
\boxed{
\lambda_{\rm cell}(a,n)
=\frac4{a^2}\sin^2\!\left(\frac{\pi}{2n}\right)
\ge\frac4{b^2},\qquad b=na.}
\tag{TS13}
$$
The one-dimensional path-graph eigenvalues are
\(4a^{-2}\sin^2(k\pi/(2n))\), \(0\le k<n\). Cartesian products add these eigenvalues. Removing the constant mode and using
\(\sin x\ge2x/\pi\) on \(0\le x\le\pi/2\) proves the bound. At fixed \(b\), the first eigenvalue tends to \(\pi^2/b^2\).

If the field has zero mean in every disjoint cell, sum these inequalities. Adding cross-cell edges only increases the gradient form, so the bound remains independent of the number of cells.

There is also a restricted linear Maxwell comparison. On a periodic lattice, with the adjoint divergence \(\delta_a\), forward exterior derivative \(d_a\), and form norms summing increasing index tuples once, the discrete Hodge identity is
$$
\|\nabla_a A\|_a^2
=\|d_aA\|_a^2+\|\delta_aA\|_a^2.
\tag{TS14}
$$
If every component has zero mean in each cell and \(\delta_aA=0\), (TS13) implies \(q_a(A)\ge4b^{-2}\|A\|_a^2\). This is a statement on that prescribed gauge-fixed linear subspace. Component averaging is not thereby a non-Abelian gauge-covariant block map.

The important contrast is what each readout controls. Vanishing on sampled lines allows an extended field to escape at negligible stiffness cost. Vanishing cell means forces fluctuations within the cells. The second can hold in an entirely massless theory: low-energy behavior remains in the retained variables. An ultraviolet fiber floor must never be advertised as a physical mass gap.

## A gauge-compatible replacement criterion

[[library/covariant-axial-gauge/inq|Dimock's covariant axial gauge]] supplies an Abelian precedent. Equation (25) averages parallel path sums over block basepoints, not just one path. Proposition 6 gives a positive fluctuation bound, uniform in volume and RG depth at fixed blocking factor, under the averaged-block and compatible axial constraints. The proof is chiefly three-dimensional and Gaussian. Its toron constraint is separate from gauge fixing.

For a candidate nonlinear replacement, the corresponding initial test is on
$$
\ker DB_U\ \cap\ \mathsf S_U,
\tag{TS15}
$$
where \(\mathsf S_U\) is a declared compatible gauge slice, with the physical tangent metric and treatment of harmonic or holonomy sectors specified. A regular-field analysis should establish scale-normalized coercivity and spatial response bounds on this carrier. Passing that test does not control the full large-field law.

[[endpoint-averages-and-quadratic-ultraviolet-control|Endpoint averages]] now proves a gauge-compatible positive version: the transported path average differs from volume averaging by an exact coarse gradient. A two-block axial estimate supplies the fixed-factor floor, and curvature contraction preserves it for successive exact Gaussian effective forms at arbitrary depth.

[[regular-gauge-averages-and-the-selection-obstruction|The anchored global average]] and [[normalized-gauge-kernels-and-markov-residues|normalized gauge kernels]] separately supply full-domain nonlinear candidates and finite conditional laws under their stated hypotheses. The outstanding construction is to join the spatial estimate to the **same** nonlinear conditional law, its [[conditioned-source-transport|score and source transport]], and the shell and terminal estimates of [[inq|the covariance-residue theorem]]. Neither the scalar comparison nor the Gaussian gauge proof controls the interacting large-field law.

The accompanying finite receipt checks (TS8)--(TS9), exact skeleton blindness, and (TS13). It does not test an interacting Yang--Mills law, OS reconstruction, or continuum existence.

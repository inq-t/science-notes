# Rigidity Certificates and Soft Escape

Exact gluing can identify the kernel of a comparison without bounding its nonzero response. Two constructive certificates provide that stronger conclusion: a finite-polynomial positive identity, or a bounded repair assembled independently of the desired spectrum. Concentrating non-Abelian comparisons, integer gluing matrices and escaping Hilbert-space directions show why positivity, exactness and pointwise convergence alone do not supply a uniform bound.

## A positive algebraic certificate

Suppose the directed gluing relations select a positive bounded element \(R\) in a declared ordered \(*\)-algebra or admissible \(C^*\)-completion, and force
\[
\boxed{R^2-\kappa R=\sum_jB_j^*B_j,\qquad R\ge0,\quad\kappa>0.}
\tag{QD5}
\]
Every bounded admissible \(*\)-representation then has
\[
\sigma(\pi(R))\subset\{0\}\cup[\kappa,\infty).
\tag{QD6}
\]
Indeed, positivity of the represented right side gives
\(x(x-\kappa)\ge0\) on the spectrum; positivity of \(R\) excludes the negative branch. The spectral theorem proves (QD6).

Here the gap follows from an identity that can be checked before diagonalizing the physical Hamiltonian. [[library/noncommutative-real-algebraic-geometry-of-kazhdans-property-t/inq|Ozawa's property-(T) theorem]] is an exact precedent for this kind of algebraic certificate. [[categorical-gauge-response/quantum-g2-categorical-rigidity-and-the-carrier-firewall|Quantum-\(G_2\) categorical rigidity]] suggests an admissible-representation version; its positivity must be that of the appropriate tube or annular completion, not just formal fusion rules.

The zero sector still has to be identified in each representation. The certificate bounds the spectrum away from its kernel; it does not identify that kernel with a vacuum. In particular, a gauge action that fixes every neutral observable cannot distinguish the vacuum from neutral excitations.

The word *certificate* must restrict how the right side is built. If arbitrary spectral functional calculus is allowed after assuming the exclusion, one can set \(B=(R^2-\kappa R)^{1/2}\) and obtain one square. That gives no independent reason for a gap. The proposed algebraic route requires explicit finite linear combinations of words in primitive comparison generators, with coefficients and \(\kappa\) deduced from their declared relations.

## A concentrating non-Abelian comparison

There is an immediate non-Abelian test for any such proposed relations. Use [[general-causal-action/sewn-overlap-and-conditional-clock|the sewn-overlap family]], with \(G=SU(2)\), fundamental character \(\chi_1\) indexed by twice the spin, and
\[
p_k(g)=\frac{(4+\chi_1(g))^k}{Z_k},\qquad
q_k=p_k*p_k,\qquad
d\pi_k(x,y)=q_k(xy^{-1})\,dx\,dy,\qquad
R_k=\frac{2I-P_{x,k}-P_{y,k}}2.
\tag{QD6a}
\]
Here \(P_{x,k},P_{y,k}\) are the actual conditional-expectation projections in \(L^2(\pi_k)\). Every finite positive integer \(k\) has full support, a positive state, state-preserving comparisons and a vacuum-only common fixed space. Put
\[
b_k=\frac12\int p_k(g)\chi_1(g)\,dg,\qquad
F_k=\frac{\chi_1(x)+\chi_1(y)}{\sqrt{2(1+b_k^2)}}.
\tag{QD6b}
\]
The source \(F_k\) is centered, normalized and invariant under simultaneous conjugation. The exact two-projection calculation gives
\[
R_kF_k=r_kF_k,\qquad r_k=\frac{1-b_k^2}{2}>0,\qquad
\langle F_k,(R_k^2-\kappa R_k)F_k\rangle=r_k(r_k-\kappa).
\tag{QD6c}
\]
The function \(4+\chi_1\) has its unique maximum at the identity. Its normalized powers concentrate there, so \(b_k\to1\) and \(r_k\to0\). Thus (QD6c) is negative eventually for every fixed \(\kappa>0\). Non-Abelianity, positivity, exact sewing, conditional comparisons and a vacuum-only kernel cannot alone force a uniform certificate. A stronger primitive relation must explain why this family is excluded or why its particular comparison law changes. This is an internal comparison-family control at fixed update pace, not an identification of \(R_k\) with the physical slab defect or a Yang--Mills continuum limit.

## A constructive quantitative gluing map

For each index \(r\), let \(\mathcal H_{0,r}\) and \(\mathcal K_r\) be complex Hilbert spaces, let \(\mathscr C_r\subset\mathcal H_{0,r}\) be a dense linear domain, and let \(T_r:\mathscr C_r\to\mathcal K_r\) be linear. The analysis \(T_r\) need not be bounded. For \(C>0\), construct an independently specified bounded return map \(B_r:\mathcal K_r\to\mathcal H_{0,r}\) and a bounded error \(E_r:\mathcal H_{0,r}\to\mathcal H_{0,r}\) with
\[
B_rT_r=I-E_r,\qquad
\|B_r\|\le C,\qquad\|E_r\|\le\rho<1
\tag{QD7}
\]
on \(\mathscr C_r\), uniformly in \(r\). Then, for every \(\psi\in\mathscr C_r\),
\[
\boxed{\|T_r\psi\|^2
\ge\frac{(1-\rho)^2}{C^2}\|\psi\|^2.}
\tag{QD8}
\]
This follows from
\((1-\rho)\|\psi\|\le\|(I-E_r)\psi\|
\le C\|T_r\psi\|\).

The estimate is on the declared dense domain; it does not assert closedness of \(T_r\) or construct a self-adjoint response operator. Those require separate closure hypotheses. In a physical application, \(\mathcal H_{0,r}\) is the complete vacuum complement and \(T_r\) must be the represented response on that domain.

The meaningful construction is a gluing algorithm assembled from local extension maps, with bounded overlap or congestion and an error margin independent of the number of boundary cells. Choosing \(B_r\) as an inverse whose boundedness is inferred from the desired gap would be circular. [[gauge-boundary-frame-gluing/inq|Gauge boundary frames]] and [[markov-edge-measure-solder/inq|local form comparison]] describe relevant ingredients: keep boundary charge data open until parts have been glued, and avoid paying a separate uncontrolled loss for every surface cell.

[[algebra/short-loop-holonomy-and-quantitative-gluing|The short-loop theorem]] constructs such a return map on an explicit section carrier: uniformly visible holonomy defects and bounded loop congestion give \(\mathcal RD_T=I\) and \(\|\mathcal R\|\le\sqrt{B/\kappa}\). Pauli edge transports realize the hypotheses with a volume-independent floor. The corresponding adjoint observable process loses the central defect and is instead diffusive. Thus the theorem realizes the gluing mechanism, while its physical carrier comparison remains substantive.

This is what “geometry forces the bound” could mean concretely: a bounded reconstruction of every physical distinction from its response, with constants fixed by gluing geometry.

The arrow being inverted matters. Here \(T_r\) denotes the response analysis, not Euclidean transfer. [[physical-response-coercivity/physical-distinction-coercivity#Stable inversion of which arrow?|The inversion fork]] proves that bounded inversion of physical transfer would impose an ultraviolet ceiling, whereas bounded inversion of its defect detects an infrared gap. [[hessian-response-geometry/response-rigidity-and-multiplicity|Response rigidity]] separately tests when a simple scalar matching law can control the complete response: exact irreducibility or a uniform comparison is needed; a fixed entropy profile and total trace do not suffice.

## Exact gluing and convergence can retain soft directions

Topological nontriviality is too weak. A local integer gluing matrix \(A_n=I-S_n\), with \(S_n\) the nilpotent shift, has determinant one, zero kernel, trivial integral cokernel, and norm at most two. Yet
\[
\lambda_{\min}(A_n^*A_n)
=4\sin^2\!\frac{\pi}{4n+2}\longrightarrow0.
\tag{QD11}
\]
The formula follows by solving the tridiagonal eigenvalue recurrence with one free and one fixed endpoint. Even bounded local coefficients and a unit residue do not give a bounded gluing inverse.

Convergence must not allow soft normalized states to escape into growing volume, changing representations, or increasingly collective observables. Strong operator convergence alone does not exclude this: on \(\ell^2\),
\[
R_n=I-(1-1/n)|e_n\rangle\langle e_n|
\longrightarrow I\quad\text{strongly},
\qquad\inf\sigma(R_n)=1/n.
\tag{QD12}
\]
A compactness route would need a no-escape theorem for normalized low-response vectors, not just compact configuration fibers.

## Preserve the certificate through a readout

An admissible *-representation preserves the polynomial identity, while a completely positive readout need not preserve products. [[scale-bearing-descent/variance-completed-rigidity|Variance-completed descent]] retains that product defect and proves separate transport estimates for the certificate and the repair. Its compression lemma assumes bounded analysis and repair operators; it does not replace the dense-domain statement of (QD7)–(QD8).

A physical conclusion additionally needs a source map, the correct vacuum norm and a compatible energy or transfer comparison. [[measured-response-carriers/response-to-energy-comparison|Response-to-energy comparison]] states that separate implication. Neither a finite-word identity nor a repair estimate selects a physical clock or establishes a continuum theory.

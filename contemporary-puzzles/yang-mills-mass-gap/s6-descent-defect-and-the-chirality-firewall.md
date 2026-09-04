# The $S^6$ Descent Defect and the Chirality Firewall

The $(3,4,\infty)$ complex-$S^6$ construction contains an exact finite grammar of projection, global sign choice, and quotient annihilation: finite-order monodromies project a common lattice seed to invariant directions, the global gluing chooses their relative sign, and the resulting unit defect makes an integer relation cokernel trivial. This is a valuable model of descent residue. It is not yet $SU(3)$ color, weak chirality, charge, or a spectral gap: those live on different carriers and require explicit realization maps. In particular, the defect is unchanged when a candidate Hamiltonian is multiplied by any positive scalar, so topology alone cannot determine a mass rate.

## The exact finite spine

Let $\Lambda\cong\mathbb Z^4$ be the first-homology lattice of the complex two-torus fibers in the open family. The orbifold fundamental group of the $(3,4,\infty)$ base has a monodromy representation

$$
\rho:\pi_1^{\mathrm{orb}}(B^\circ)
\longrightarrow\operatorname{Aut}(\Lambda)
\cong GL_4(\mathbb Z).
\tag{SD1}
$$

For finite monodromies $A_1^3=A_2^4=I$, cyclic averaging gives rational projectors

$$
P_m(A)=\frac1m\sum_{k=0}^{m-1}A^k.
\tag{SD2}
$$

On the selected integral seed $\widehat\gamma$, the construction obtains integral invariant vectors

$$
\epsilon=P_3(A_1)\widehat\gamma,
\qquad
\epsilon'=P_4(A_2)\widehat\gamma.
\tag{SD3}
$$

The projectors do **not** choose handedness. The relative sign is separate global gluing data:

$$
v_1=\epsilon,
\qquad
v_2=-\epsilon'.
\tag{SD4}
$$

For the corresponding winding integers $(\ell_0,\ell_1,\ell_2)=(0,1,-1)$, the two-relation determinant is

$$
p=12\ell_0-4\ell_1-3\ell_2=-1.
\tag{SD5}
$$

In the formal integer interface, coprimality of $3$ and $4$ identifies the relation cokernel with $\mathbb Z/|p|\mathbb Z$. Thus $|p|=1$ makes that cokernel trivial. After the manuscript's geometric boundary maps and integral Leray transgressions are imported, the same unit is used to eliminate the fundamental-group residue and middle integral cohomology. The other cusp certificate

$$
B_0:\Lambda/\Lambda_{\mathrm{tor}}
\xrightarrow{\ \cong\ }
\Lambda_{\mathrm{tor}}
\tag{SD6}
$$

is a rank-two unimodular exchange map, not a $4\times4$ gauge holonomy.

This gives the exact algebraic pattern

$$
\widehat\gamma
\xrightarrow{(P_3,P_4)}
(\epsilon,\epsilon')
\xrightarrow{\text{relative sign}}
(v_1,v_2)
\xrightarrow{\text{integer relations}}
\operatorname{coker}R=0.
\tag{SD7}
$$

The same-sign choice has $p=-7$ in the finite relation formula and hence leaves a $\mathbb Z/7\mathbb Z$ cokernel. That arithmetic fact does not by itself prove that the alternative sign completes to another compact complex threefold. Conversely, reversing the relevant orientations reverses $p$ but not $|p|$. The sign of $p$ is therefore not an invariant physical handedness without additional orientation-sensitive data.

## The root object is mixed descent data

The slogan “locally continuous, globally discrete” is useful only if *globally discrete* is not taken literally. The construction needs both

$$
\begin{aligned}
&\text{analytic data:}&&
\text{period map, varying complex tori, holomorphic fillings, properness, gluing},\\
&\text{arithmetic data:}&&
\text{integral local system, monodromy, primitive twists, unimodular relations}.
\end{aligned}
\tag{SD8}
$$

The root object is therefore a holomorphic family equipped with an integral local system and compatible descent data. The image of (SD1) is not a global symmetry group of the completed threefold. Monodromy records how local fiber coordinates return after transport around singular values; a global automorphism would instead act on the completed object itself.

The triangle group is necessary to this **particular presentation**, not presently known to be necessary for every integrable complex structure on $S^6$. Independent existence proofs do not by themselves establish that all such structures factor through the $(3,4,\infty)$ family. Any physical proposal must therefore use the actual descent data it constructs, rather than promote one construction method into a universal necessity claim.

Nor does $\Lambda\cong\mathbb Z^4$ represent microscopic spacetime pixels. It is the homology lattice of an already continuous complex torus. The upper half-plane $\mathfrak H$ is the Riemannian hyperbolic plane; calling it Euclidean $\mathrm{AdS}_2$ identifies a shared analytic continuation, not a Lorentzian spacetime or a holographic duality.

Standard local QFT requires complex state spaces and smooth differential locality, but it does **not** require physical spacetime itself to carry an integrable complex structure. The valid comparison is structural: local complex-analytic or differential calculations can be continuous while their globally admissible sections are selected by discrete descent. Turning that comparison into QFT needs a net, adjoint, positive state, causal real form, and dynamics; [[complex-presentation-without-polarization/inq|the complex-presentation firewall]] records these missing types.

This is nevertheless a genuine Copernican lesson. A locally ordinary presentation need not be grounded by one larger local symmetry. Its global identity can instead be fixed by the compatibility of analytic continuation, discrete transport, singular filling, and a quotient relation.

## The winding defect has a coercive automorphic shadow

The closest rigorous bridge to a mass gap does not identify $p$ with energy. It lets the signed winding data select the global domain of a continuous operator. For

$$
\Delta^+(3,4,\infty)
=\langle a,b\mid a^3=b^4=1\rangle,
\qquad
c=(ab)^{-1},
$$

define the unitary line character

$$
\chi_\ell(a)=e^{2\pi i\ell_1/3},
\qquad
\chi_\ell(b)=e^{2\pi i\ell_2/4}.
\tag{SD9}
$$

Then the integer defect has the exact phase shadow

$$
\boxed{
\chi_\ell(c)
=e^{2\pi ip/12}.}
\tag{SD10}
$$

For $p=-1$, this is a primitive twelfth root. [[triangle-character-cusp-coercivity]] proves that every nontrivial unitary character of this triangle group removes the zero Fourier channel at the cusp. Its twisted hyperbolic Laplacian consequently has compact resolvent, zero kernel, and a strictly positive lowest eigenvalue. This is an exact instance of a smooth local Casimir becoming coercive because only globally equivariant sections are admissible.

The theorem is not supplied by the rank-four monodromy itself. That monodromy has nonidentity unipotent cusp action, cannot preserve a positive-definite Hermitian form, and has fixed cusp directions. Equation (SD10) constructs a separate one-dimensional unitary shadow from the winding exponents.

Nor does automorphic coercivity select the sphere topology uniquely. The automorphic operator sees only $p\bmod12$, every nonzero class removes the cusp channel, and the same-sign value $p=-7$ is also primitive and coercive. Replacing $p$ by $-p$ conjugates the character without changing the spectrum. Thus the topological unit condition, automorphic gapping, and chirality are three different consequences.

If a curvature radius $L_*$ is then supplied, a dimensionless Laplace eigenvalue $\lambda_0$ has the dimensional conversion

$$
m_*c^2=\frac{\hbar c}{L_*}\sqrt{\lambda_0}.
\tag{SD10a}
$$

This has exactly the desired form “dimensionless number from geometry times a dimensional yardstick.” It is not yet the Yang--Mills gap. The automorphic theorem lives on a fixed finite-area two-dimensional orbifold; a physical conclusion requires a same-carrier comparison and a positive lower edge surviving volume and continuum removal. The toric construction fills the complex fiber over the cusp, not the hyperbolic base metric or the domain of its Laplacian, so cusp filling is not the spectral mechanism.

## The two $SU(3)$ appearances must not be identified

There are two different structures on the underlying smooth six-sphere:

1. The torus-fibration construction supplies an integrable complex structure $J_{\mathrm{int}}$. Its complex frame bundle initially has structure group $GL_3(\mathbb C)$; after choosing a Hermitian metric it reduces to $U(3)$. Since $H^2(S^6;\mathbb Z)=0$, its first Chern class vanishes and a further *topological* $SU(3)$ reduction can be chosen. This does not canonically trivialize the canonical bundle holomorphically and does not make the holonomy of a selected connection $SU(3)$.

2. The octonionic presentation supplies the nonintegrable homogeneous almost-complex structure

$$
S^6\cong G_2/SU(3).
\tag{SD11}
$$

Here $SU(3)$ is the isotropy of a selected unit imaginary octonion. [[octonionic-slice-groupoid-and-orientation-torsor|The octonionic quotient-stack theorem]] retains that stabilizer as

$$
[S^6/G_2]\simeq\mathbf B SU(3),
\tag{SD12}
$$

and its free-path transgression gives the ordinary lattice gauge groupoid. That exact result belongs to the octonionic $G_2$ action, not to the $GL_4(\mathbb Z)$ monodromy in (SD1).

No canonical comparison has yet been constructed between $J_{\mathrm{int}}$ and the octonionic slice groupoid. A physical use of both must provide such a comparison rather than moving the name $S^6$ across the type boundary.

## Complex type, a genuine index seed, and physical chirality

Integrability gives

$$
T_{\mathbb C}S^6
=T^{1,0}S^6\oplus T^{0,1}S^6.
\tag{SD13}
$$

It does not discard either summand: complex conjugation exchanges them. This splitting is not the Lorentz-spinor decomposition selected by $P_{L,R}=(1\mp\gamma_5)/2$, and the sign in (SD4) is not a fermionic projector.

There is, however, an exact chiral-index seed on the *octonionic* side. Let

$$
E:=G_2\times_{SU(3)}\mathbb C^3\longrightarrow S^6.
\tag{SD14}
$$

Its clutching map generates $\pi_5(SU(3))$. With the orientation fixed appropriately, $c_3(E)=2[S^6]$ while $c_1(E)=c_2(E)=0$. Since the positive-degree terms of $\widehat A(TS^6)$ cannot contribute in degree six,

$$
\operatorname{ind}D_E^+
=\int_{S^6}\widehat A(TS^6)\operatorname{ch}(E)
=\int_{S^6}\operatorname{ch}_3(E)
=\frac12\int_{S^6}c_3(E)
=1,
\tag{SD15}
$$

up to simultaneous orientation sign. This is genuine topology producing a chiral Fredholm index. It is not yet Standard-Model chirality: one still needs a Lorentzian or finite spectral carrier, the observed gauge representations, anomaly cancellation, and a theorem relating this octonionic bundle to the integrable complex presentation.

Likewise, the invariant homomorphism $\gamma:\Lambda\to\mathbb Z$ measures winding exponents in the gluing calculation. It is not a Noether charge, electric charge, color weight, or causal charge until a carrier, action, and generator map identify it as one.

## Unit defect is not positive coercivity

The mass-gap stopping condition is an inequality on the physical vacuum-complement carrier:

$$
\mathfrak h_{\mathrm{YM}}[\Psi]
\ge
\Delta_E\,
\|(1-P_\Omega)\Psi\|^2,
\qquad
\Delta_E>0.
\tag{SD16}
$$

The unit relation (SD5) is an invertibility statement over $\mathbb Z$. Equation (SD16) is a positivity statement for a closed quadratic form over a Hilbert space. Neither implies the other. The elementary rescaling

$$
H\longmapsto\varepsilon H,
\qquad \varepsilon>0,
\tag{SD17}
$$

leaves $\Lambda$, monodromy, $B_0$, $p$, and every topological quotient unchanged while multiplying every energy gap by $\varepsilon$. Thus no topological certificate by itself determines even a dimensionless transfer rate.

The needed theorem is a **descent-to-coercivity realization**. It must:

1. map the automorphic or monodromy object to an $SU(3)$ torsor with connection or directly to the gauge-invariant Wilson/OS carrier;
2. construct from the global descent condition a positive closed form $q_{\mathrm{desc}}$ on that same carrier;
3. prove a noncircular comparison

   $$
   \mathfrak h_{\mathrm{YM}}\ge\kappa q_{\mathrm{desc}},
   \qquad
   q_{\mathrm{desc}}[\Psi]\ge\epsilon\|(1-P_\Omega)\Psi\|^2;
   \tag{SD18}
   $$

4. control $\kappa\epsilon$ through volume removal and the continuum limit; and
5. separately calibrate the surviving inverse time or inverse length into mass.

Until then, the $S^6$ unit defect is an unusually crisp model of **topological residue cancellation**, while [[triangle-character-cusp-coercivity|the automorphic theorem]] is an exact model of **global unitary descent restricting a local continuum into a coercive sector**. The unproved step is transporting that mechanism to the Yang--Mills carrier and limit.

## Evidence boundary

- **[EXACT FINITE INTERFACE]** The cyclic projections, signed winding data, unit determinant, relation-cokernel classification, and finite Lean certificates in `inbox/s6-proof-master`.
- **[CONDITIONAL SOURCE-SPECIFIC GEOMETRY]** The use of those certificates in the particular period family, cusp filling, Hausdorff assembly, van Kampen calculation, and Leray computation. The short proof explicitly imports these results; its own audit leaves their independent verification open.
- **[INDEPENDENT EXISTENCE EVIDENCE]** Existence of an integrable complex structure on the smooth $S^6$ has an independent geometric proof and a direct Lean proof recorded in [[algebra/s6-manuscript-branch|the integrable-$S^6$ branch]], while conventional publication and community assimilation remain in progress. This does not automatically certify every invariant of the $(3,4,\infty)$ construction.
- **[EXACT AUTOMORPHIC THEOREM]** The character formula $\chi_\ell(c)=e^{2\pi ip/12}$ and positive-bottom result for every nontrivial unitary character of $\Delta^+(3,4,\infty)$; this is a theorem on the hyperbolic-orbifold carrier, not on Yang--Mills.
- **[EXACT, SEPARATE OCTONIONIC INDEX]** The generator clutching class of $G_2\to S^6$ and the index calculation (SD15); no comparison with $J_{\mathrm{int}}$ is supplied.
- **[OPEN]** A comparison of the two $S^6$ structures, physical chirality or charge, a same-carrier automorphic-to-Yang--Mills coercivity map, continuum survival, and any mass scale.

[[complex-presentation-without-polarization/inq|Complex presentation without polarization]] supplies the broader categorical setting; [[physical-distinction-coercivity]] states why discrete algebraic distinction and positive spectral separation must remain different types.

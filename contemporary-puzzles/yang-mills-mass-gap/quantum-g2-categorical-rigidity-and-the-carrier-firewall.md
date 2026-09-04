# Quantum G2 Categorical Rigidity and the Carrier Firewall

The exceptional clue can be sharpened from “\(G_2\) contains an \(SU(3)\) stabilizer” to an exact dimensionless coercivity theorem: for every positive \(q\neq1\), the quantum \(G_2\) tensor category has property \((T)\), so its normalized fundamental fusion operator has a representation-uniform positive edge above the trivial categorical presentation. The same category supplies an intrinsic statistical dimension and hence an abstract additive log-dimension address; under a standard finite-index infinite-factor realization this becomes an operational index capacity. These are independent coordinates: at the classical point \(q=1\), the address remains \(2\log7>0\) while categorical rigidity disappears. Under the explicitly conjectural multiplicative cosmic-capacity weld, a finite cosmological ledger depth selects \(|\log q|\) uniquely up to \(q\leftrightarrow q^{-1}\); a physical mass gap follows only after a new admissible action on the neutral Yang--Mills tangent carrier, a lower frame, a regional relative-entropy domination, a localization-width solder, and the usual continuum and Poincare reconstruction.

**Status: [EXACT] for the universal categorical averaging theorem, quantum-\(G_2\) property \((T)\), the scalar log-dimension/rigidity separation, and the conditional deformation-selection calculus; [STANDARD CONDITIONAL COROLLARY] for interpreting \(2\log d_q(X)\) as supremal relative-entropy capacity after the stated minimal finite-index infinite-factor realization; [EXACT CONDITIONAL] for the carrier-to-energy inequality under the displayed representation, frame, entropy, and localization hypotheses; [CONJECTURE] for the multiplicative cosmic-capacity weld and the exceptional-to-Yang--Mills carrier map; [OPEN] for selection of \(q\), fusion depth, Q-system, cosmic cut, absolute normalization, fossil transport, neutral coverage, continuum construction, Poincare recovery, and gravity decoupling.**

## The Copernican clue is categorical, not merely group-theoretic

The classical homogeneous space

\[
S^6\cong G_2/SU(3)
\]

explains how an \(SU(3)\) stabilizer can appear after selecting an octonionic unit. It does not provide a positive analytic edge. Conversely, the triangle presentation in [[global-discreteness-kazhdan-rigidity-and-the-gap]] is globally discrete but its group \(C_3*C_4\) is not Kazhdan. Neither a stabilizer nor discreteness alone excludes almost-trivial nonvacuum directions.

The stronger object is a rigid \(C^*\)-tensor category \(\mathcal C\). It contains fusion, conjugation, statistical dimension, annular positivity, and the admissible representations of its fusion algebra. Popa and Vaes emphasize that admissibility depends on the tensor category and not merely on its fusion rules. This is already a Copernican reversal: the observed group labels need not be the source of rigidity; both the labels and the allowed ways of presenting them may descend from a deeper compositional object.

## The universal categorical averaging operator

Let \(S\subset\operatorname{Irr}(\mathcal C)\setminus\{\mathbf1\}\) be a finite symmetric tensor-generating set and let \(\nu:S\to(0,\infty)\) satisfy \(\nu(\bar\alpha)=\nu(\alpha)\). In the fusion corner of the tube algebra, define

\[
Z_{S,\nu}
:=
\sum_{\alpha\in S}\nu(\alpha)d(\alpha),
\qquad
h_{S,\nu}
:=
\frac{1}{Z_{S,\nu}}
\sum_{\alpha\in S}\nu(\alpha)[\alpha],
\qquad
L_{S,\nu}:=1-h_{S,\nu}.
\tag{QG1}
\]

The normalized fusion average \(h_{S,\nu}\) is a self-adjoint contraction on every nondegenerate right Hilbert tube-algebra module. Vaes and Valvekens prove the equivalence

\[
\mathcal C\text{ has property }(T)
\quad\Longleftrightarrow\quad
1\text{ is isolated in }\sigma_{\mathrm{univ}}(h_{S,\nu}).
\tag{QG2}
\]

The fixed vectors of \(h_{S,\nu}\) are exactly the categorical invariant vectors. If

\[
\kappa_{S,\nu}
:=
1-\sup\bigl(\sigma_{\mathrm{univ}}(h_{S,\nu})\setminus\{1\}\bigr)>0,
\tag{QG3}
\]

and \(p_{\mathrm K}\) is the Popa--Vaes Kazhdan projection, functional calculus gives

\[
\boxed{
L_{S,\nu}
\geq
\kappa_{S,\nu}(1-p_{\mathrm K}).}
\tag{QG4}
\]

Thus every admissible representation

\[
\Theta:C_u(\mathcal C)\longrightarrow B(\mathcal K)
\]

obeys

\[
I-\Theta(h_{S,\nu})
\geq
\kappa_{S,\nu}\bigl(I-\Theta(p_{\mathrm K})\bigr).
\tag{QG5}
\]

The operator acts on **admissible presentations of the fusion algebra**, equivalently on the relevant annular or tube-algebra carrier. It does not act on spacetime points, color vectors, masses, or arbitrary Hilbert-space states.

This is the exact lower-bound structure missing from finite index by itself. The index answers how large a channel can be; \(L_{S,\nu}\) asks whether a nontrivial admissible presentation can approach the undifferentiated one at arbitrarily small cost.

The projection \(p_{\mathrm K}\) is intrinsic, but the numerical constant \(\kappa_{S,\nu}\) depends on the generating set and its relative weights. Adding \(m\) trivial summands to a generator rescales its Laplacian and can make the displayed edge arbitrarily small without changing the category. A principled physical construction must therefore select the averaging object before using its number.

## A Q-system supplies a relative normalization, not energy

Suppose a standard generating Q-system has underlying algebra object

\[
\theta\cong\bigoplus_{\alpha}n_\alpha\alpha,
\qquad
n_{\mathbf1}:=\dim\operatorname{Hom}(\mathbf1,\theta)\geq1.
\]

Its self-duality makes the support symmetric, but the tensor-unit summand must not be inserted into the generating set in (QG1). Put

\[
S_\theta
:=
\operatorname{supp}(\theta)\setminus\{\mathbf1\},
\qquad
Z_\theta
:=
d(\theta)-n_{\mathbf1},
\]

and, when \(S_\theta\) tensor-generates the declared category, take

\[
h_\theta^\circ
:=
\frac{[\theta]-n_{\mathbf1}[{\mathbf1}]}{Z_\theta},
\qquad
L_\theta^\circ:=1-h_\theta^\circ.
\tag{QG6}
\]

The normalized full algebra-object character is instead

\[
\bar h_\theta
:=
\frac{[\theta]}{d(\theta)}
=
\frac{n_{\mathbf1}}{d(\theta)}\,1
+
\frac{d(\theta)-n_{\mathbf1}}{d(\theta)}\,h_\theta^\circ,
\]

so

\[
1-\bar h_\theta
=
\frac{d(\theta)-n_{\mathbf1}}{d(\theta)}
L_\theta^\circ.
\tag{QG6a}
\]

Thus the two averages have the same fixed vectors, while including the compulsory unit summand rescales the nontrivial edge by \((d(\theta)-n_{\mathbf1})/d(\theta)\). For a connected Q-system, \(n_{\mathbf1}=1\).

Here \(d(\theta)\) means the categorical dimension of the underlying algebra object; for an inclusion \(N\subset M\), \(d(\theta)=[M:N]\). Some subfactor references instead call \(d_A=\sqrt{d(\theta)}=\sqrt{[M:N]}\) the “dimension of the Q-system,” equal to the dimension of the generating \(N\)-\(M\) one-morphism. Writing the formulas through \(d(\theta)\) prevents that convention from introducing a factor-of-two error in logarithmic capacity.

Equations (QG6)--(QG6a) are natural relative to a selected Q-system, but the averaging operator uses only its underlying fusion object; it does not use the multiplication or unit maps and it contains no time-translation generator. If \(S_\theta\) does not generate all of \(\mathcal C\), the operator tests only the generated subcategory. Selecting the Q-system and proving that its normalization is physically energetic remain separate tasks.

## The quantum-\(G_2\) theorem

For \(q>0,\ q\neq1\), let

\[
\mathcal C_q
:=
\operatorname{Rep}_{\mathrm{type\,1}}^{\mathrm{unitary}}
U_q(\mathfrak g_2),
\qquad
\mathcal C_1:=\operatorname{Rep}(G_2).
\]

The category has a distinguished self-dual trivalent generator \(X\), the deformation of the fundamental seven-dimensional representation. Its statistical dimension is

\[
\delta_q:=d_q(X)
=q^{10}+q^8+q^2+1+q^{-2}+q^{-8}+q^{-10}.
\tag{QG7}
\]

This is Jones's deformation-parameter normalization.

Because \(S=\{X\}\) is a symmetric generating set, the natural fundamental average and Laplacian are

\[
h_q=\frac{[X]}{\delta_q},
\qquad
L_q=1-\frac{[X]}{\delta_q}.
\tag{QG8}
\]

Corey Jones proves

\[
\boxed{
\mathcal C_q\text{ has property }(T)
\quad\text{for every }q>0,\ q\neq1.}
\tag{QG9}
\]

Thus (QG4)--(QG5) give a dimensionless number \(\kappa_q>0\) at every deformed point. Jones's proof isolates the trivial character by a tube-algebra positivity obstruction in a two-coordinate admissible spectrum. One local exclusion derivative in that proof is

\[
\rho_q
:=
\left.\frac{\partial f}{\partial t}\right|_{(0,\delta_q)}
=
(q-q^{-1})^2(q^2+1+q^{-2})
>0
\quad(q\neq1).
\tag{QG10}
\]

For \(q=e^\eta\),

\[
\rho_{e^\eta}=12\eta^2+O(\eta^4).
\tag{QG11}
\]

This is an explicit witness that Jones's admissibility-exclusion certificate turns on away from the classical point. It is **not** the optimal Kazhdan constant \(\kappa_q\), and the displayed asymptotic does not prove an asymptotic for \(\kappa_q\).

At \(q=1\), \(\operatorname{Rep}(G_2)\) is an infinite amenable category and does not have property \((T)\). Accordingly the endpoint \(1\) is not isolated in the universal admissible spectrum of \(h_1\), and the corresponding spectral-separation number is zero.

## Size and rigidity are independent categorical coordinates

In a standard minimal infinite-factor realization, the sector associated with \(X\) carries the index-capacity address

\[
\mathfrak C_q(X)
=
2\log d_q(X)
=
2\log\delta_q.
\tag{QG12}
\]

At the undeformed point,

\[
\mathfrak C_1(X)=2\log7>0,
\qquad
\kappa_1=0.
\tag{QG13}
\]

This is a decisive firewall:

\[
\boxed{
\text{positive statistical dimension or log-index capacity}
\not\Rightarrow
\text{positive categorical stiffness}.}
\tag{QG14}
\]

For \(q\neq1\), the same categorical source supplies both numbers,

\[
\mathcal C_q
\longmapsto
\bigl(2\log\delta_q,\ \kappa_q\bigr),
\tag{QG15}
\]

but no theorem identifies them. The first is additive under fusion and measures a maximum information-loss capacity after the appropriate finite-index factor realization. The second is a minimum spectral separation across admissible presentations. Maximum capacity and minimum coercivity are different quantifiers even when they arise from one category.

This is the exact refinement of [[two-sided-index-capacity-and-the-cosmic-weld]]: the missing floor need not be manufactured from the index. It may be a second invariant of the same deeper compositional structure.

## A conditional cosmic selector for the deformation magnitude

Put

\[
\eta:=\log q,
\qquad
\delta(\eta)
=1+2\cosh(2\eta)+2\cosh(8\eta)+2\cosh(10\eta).
\tag{QG16}
\]

The function is even, has minimum \(\delta(0)=7\), and is strictly increasing with \(r=|\eta|>0\), because

\[
\frac{\mathrm d}{\mathrm dr}\delta(r)
=4\sinh(2r)+16\sinh(8r)+20\sinh(10r)>0.
\tag{QG17}
\]

Now assume the **multiplicative effective-cell-count weld**, not merely additive entropy:

\[
\frac{\iota_c}{\iota_b}
=
d_q(X)^{2n}
=
\delta_q^{2n},
\qquad n\in\mathbb N_{>0}.
\tag{QG18}
\]

For the cosmological ledger depth

\[
\mathscr D_c
:=
\log\frac{\iota_c}{\iota_b}
=
2\int_{N_b}^{N_c}\epsilon(N)\,\mathrm dN,
\tag{QG19}
\]

equation (QG18) becomes

\[
\frac{\mathscr D_c}{2n}
=
\log\delta(\eta).
\tag{QG20}
\]

The monotonicity theorem gives an exact conditional trichotomy:

\[
\boxed{
\begin{array}{rcl}
\mathscr D_c<2n\log7
&\Longrightarrow& \text{no positive-real-}q\text{ solution},\\[2mm]
\mathscr D_c=2n\log7
&\Longrightarrow& q=1\text{ and }\kappa_q=0,\\[2mm]
\mathscr D_c>2n\log7
&\Longrightarrow& \text{a unique }|\log q|>0\text{ and }\kappa_q>0.
\end{array}}
\tag{QG21}
\]

This is the first precise way the global cosmic ledger can select a **dimensionless rigidity regime** rather than directly stipulating a microscopic mass. It uses a whole-history logarithm and a natural fusion integer. It also exposes what remains arbitrary: the integer \(n\), the birth section \(\iota_b\), the physical truth of the multiplicative weld, and the synchronization of the categorical crossings with the cosmological interval.

The equation only determines \(|\eta|\). Both \(\delta_q\) and \(\rho_q\) are invariant under \(q\leftrightarrow q^{-1}\). Consequently this construction supplies no physical handedness by itself. The residual twofold presentation may be redundant under categorical equivalence; calling it chirality would require a separate orientation-sensitive invariant and an observable image.

On the same conjectural branch, [[two-sided-index-capacity-and-the-cosmic-weld]] gives

\[
\frac{H_c}{H_b}=\delta_q^{-n},
\qquad
\frac{E_{*,c}}{E_{*,b}}=\delta_q^{-n/3}.
\tag{QG22}
\]

These are ratio laws. They do not fix the absolute scale without an independently normalized birth capacity, proper duration, or equivalent section of the cosmic dilation orbit.

## The one-channel-birth depth produces a quarantined integer clue

The proposed one-channel boundary condition already present in [[minimal-cosmodynamic-closure/inbox/the-constants-of-nature/entry|the constants-of-nature synthesis]] is

\[
\iota_b=1.
\tag{QG22a}
\]

If this proposal, the Einstein apparent-horizon ledger, and the multiplicative weld (QG18) are all granted, then

\[
H_b=\left(\frac{\pi c^5}{G\hbar}\right)^{1/2},
\qquad
\mathscr D_c=2\log\frac{H_b}{H_c},
\qquad
H_c=H_b\delta_q^{-n}.
\tag{QG22b}
\]

Because \(\delta_q\geq7\) on the positive-real branch, a supplied finite depth permits only

\[
n\leq n_{\max}
:=
\left\lfloor
\frac{\mathscr D_c}{2\log7}
\right\rfloor.
\tag{QG22c}
\]

For the two previously recorded crossing-rate anchors, the finite receipt gives

\[
\begin{array}{c|c|c|c|c}
H_c\;(\mathrm{km\,s^{-1}\,Mpc^{-1}})
&\mathscr D_c&n_{\max}
&\mathscr D_c-144\log7
&q\text{ at }n=72\\ \hline
83.1058&281.3142&72&1.1032&1.01804\\
88.2608&281.1938&72&0.9828&1.01702
\end{array}
\tag{QG22d}
\]

This is a **post-search numerical diagnostic**, not a selection theorem. It says something more precise than a free recurrence of integers: under the displayed conjectures, the cosmic depth has a largest admissible positive-real quantum-\(G_2\) fusion depth, and that integer is stable at seventy-two on both existing calibration branches. The residual above the classical \(q=1\) threshold is of order one nat, so the maximal-depth solution lies close to, but strictly away from, the amenable classical point.

The number seventy-two also occurs in the exceptional normal decomposition: each of the \(24\mathbf3\) and \(24\bar{\mathbf3}\) colored halves has dimension seventy-two. This recurrence is not yet licensed as an identification. Fusion depth \(X^{\boxtimes n}\), direct-sum multiplicity, real orbit dimension \(36\), and the two orientation branches are different categorical types. A valid upgrade must construct a monoidal functor or incidence theorem making one of those exact exceptional counts equal to the exponent in (QG18) before the cosmological values are consulted. Without that map, \(72=2\cdot6^2\) remains a useful target for falsification rather than evidence.

With (QG22a), the candidate common-count energy also obtains the explicit conditional form

\[
E_{*,c}
=
\left(\frac{3\sqrt\pi}{4\gamma s_*}\right)^{1/3}
E_P\,\delta_q^{-n/3},
\qquad
E_P:=\left(\frac{\hbar c^5}{G}\right)^{1/2}.
\tag{QG22e}
\]

This makes the order of explanation visible: a boundary section fixes the overall dilation orbit, the dimension character fixes a hierarchy ratio, and categorical property \((T)\) supplies a dimensionless floor. None of those steps yet proves that the floor acts on the neutral Yang--Mills energy carrier.

## The carrier-correct conditional mass-gap theorem

Let

\[
\mathcal K_0
\subset
(1-P_0)\operatorname{Dom}(H_{\mathrm{YM}}^{1/2})
\]

be a complex energy-form core for the vacuum-reduced physical Yang--Mills Hilbert space. A categorical explanation requires the following data, constructed without inspecting the desired Hamiltonian edge:

1. an admissible representation \(\Theta_q:C_u(\mathcal C_q)\to B(\mathcal L_q)\);
2. a complex-linear analysis map \(J_q:\mathcal K_0\to\mathcal L_q\) with

   \[
   \Theta_q(p_{\mathrm K})J_q=0,
   \qquad
   \|J_q\psi\|^2\geq a_J\|\psi\|^2,
   \qquad a_J>0;
   \tag{QG23}
   \]

3. a positive Hermitian regional restriction-loss form \(\widehat q_{\mathrm{loss},B}\) satisfying

   \[
   \widehat q_{\mathrm{loss},B}[\psi]
   \geq
   b_{\mathrm{cat}}
   \left\langle
   J_q\psi,
   \Theta_q(L_q)J_q\psi
   \right\rangle,
   \qquad b_{\mathrm{cat}}>0;
   \tag{QG24}
   \]

4. the finite-width energy comparison from [[localized-relative-entropy-and-the-energy-solder]],

   \[
   \widehat q_{\mathrm{loss},B}[\psi]
   \leq
   \frac{2\pi R_B}{\hbar c}
   \langle\psi,H_{\mathrm{YM}}\psi\rangle.
   \tag{QG25}
   \]

Then (QG5) gives

\[
\langle\psi,H_{\mathrm{YM}}\psi\rangle
\geq
\frac{\hbar c}{2\pi R_B}
b_{\mathrm{cat}}a_J\kappa_q\|\psi\|^2,
\tag{QG26}
\]

and hence

\[
\boxed{
\Delta_E
\geq
\frac{\hbar c}{2\pi R_B}
b_{\mathrm{cat}}a_J\kappa_q.}
\tag{QG27}
\]

If an independently proved whole-to-local width map gives \(R_B=\alpha\lambda_*\), with \(E_*=\hbar c/\lambda_*\), then

\[
\boxed{
\Delta_E
\geq
\frac{b_{\mathrm{cat}}a_J\kappa_q}{2\pi\alpha}
E_*.}
\tag{QG28}
\]

On the common-count branch this can be written

\[
\Delta_E
\geq
\frac{b_{\mathrm{cat}}a_J\kappa_q}{2\pi\alpha}
\left(\frac{6\pi^2}{\gamma s_*}\right)^{1/3}
E_{A,c}\,\iota_c^{-2/3}.
\tag{QG29}
\]

Equation (QG29) displays the desired factorization without equivocation:

\[
\underbrace{\kappa_q}_{\substack{\text{dimensionless categorical}\\\text{rigidity}}}
\times
\underbrace{E_{A,c}\iota_c^{-2/3}}_{\substack{\text{whole-cosmos}\\\text{dimensional yardstick}}}
\times
\underbrace{
\frac{b_{\mathrm{cat}}a_J}{2\pi\alpha}
\left(\frac{6\pi^2}{\gamma s_*}\right)^{1/3}
}_{\substack{\text{carrier, entropy, and}\\\text{localization solders}}}.
\tag{QG30}
\]

If \(\iota_c\) is independently primitive, the middle factor may be presented using \(c,G,H_c\) without writing \(\hbar\):

\[
E_{A,c}\iota_c^{-2/3}
=
\frac{c^5}{2GH_c}\iota_c^{-2/3}.
\tag{QG31}
\]

If instead \(\iota_c=S_{A,c}/k_B\) is identified through the Bekenstein--Hawking formula, \(\hbar\) has already entered that capacity. Boltzmann's constant changes entropy units; it does not provide a rate. The distinction between these two routes is the \(\hbar\) firewall, not a notational preference.

## Why this still does not act on glueballs

The exact categorical carrier is not yet the Yang--Mills carrier. Admissible fusion-algebra representations are restrictions of tube-algebra representations and can be realized through annular states or subfactor symmetric-enveloping correspondences. DHR sectors also form rigid tensor categories under suitable AQFT hypotheses. None of those facts constructs \(J_q\) in (QG23).

There is an especially sharp DHR firewall. Neutral glueball excitations belong to the vacuum representation, which is the tensor unit. That unit sector has statistical dimension and index one regardless of whether

\[
\mathcal H_0\ominus\mathbb C\Omega
\]

is massive, gapless, or has spectrum accumulating at zero. Finite-index charged-sector data therefore cannot resolve the spectral structure *inside* the neutral tensor unit. A valid use of (QG5) must construct a new admissible presentation action on vacuum-sector state tangents; it cannot identify categorical objects with particle species. This is consistent with the DHR carrier distinctions surveyed in [[library/algebraic-quantum-field-theory/inq|algebraic quantum field theory]].

There are three immediate failure modes:

- If the category acts as an ordinary internal charge symmetry, neutral glueballs can lie in the trivial subspace, and \(L_q\) vanishes on the target rather than gapping it.
- If \(\mathcal C_q\) is assigned to superselection sectors, confinement may leave the observable vacuum representation with no corresponding charged DHR carriers.
- If \(J_q\) covers only a selected finite family of observables, the orthogonal complement can still contain arbitrarily soft physical directions.

The required action is therefore not “\(G_2\) rotates a glueball.” It is a global-presentation comparison on **localized gauge-invariant state tangents**, with trivial categorical presentation corresponding exactly to the vacuum direction. That is the substantive content of (QG23)--(QG24).

The classical exceptional chain and the quantum category are also not yet the same object. The \(S^6=G_2/SU(3)\) stabilizer, the \(F_4/H\) flag torsor, and the exact Wilson-factor response in [[exceptional-wilson-same-carrier-factorization]] live on classical compact-group carriers. The \(q\neq1\) rigidity theorem lives in a deformed tensor category. A deformation, functor, or Q-system must recover the local \(SU(3)\) Wilson carrier while retaining a uniform categorical edge. Merely sharing the name \(G_2\) is not that theorem.

## Stopping condition

This route makes a genuine dent in the conceptual problem if, and only if, all of the following are proved:

1. an internal rule selects \(q\neq1\), a fusion depth \(n\), and a standard Q-system or inclusion without fitting the glueball spectrum;
2. the cosmic/index weld (QG18) is realized by a composition-preserving map, with a selected birth section and a wall-to-cosmos synchronization;
3. the quantum-\(G_2\) categorical data descend to the classical local \(SU(3)\) observable regulator in a controlled branch;
4. an admissible representation and analysis map (QG23) are constructed on a regulator-complete neutral Yang--Mills tangent core;
5. its trivial categorical subspace pulls back to exactly the vacuum, and the lower frame \(a_J\) is uniform in volume and cutoff;
6. one genuine regional Type-III restriction-loss form dominates the categorical form as in (QG24), with a positive Hermitian extension on the complex energy-form core;
7. the width \(R_B=\alpha\lambda_*\) and fossil transport of \(\lambda_*\) are derived rather than declared;
8. Osterwalder--Schrader and Poincare reconstruction turn the energy edge into the complete invariant-mass gap; and
9. the gravity-coupled selection construction has a controlled pure-Yang--Mills limit in which the positive dimensionless coefficient survives.

The new exact advance is narrow but important: the exceptional framework now contains a mathematically genuine **minimum distinction operator** in addition to a maximum distinction capacity. It also supplies a hard counterexample to their conflation at \(q=1\). What remains is no longer “find some discrete number.” It is to prove that the categorical Laplacian operates on every physical neutral distinction and that the whole-cosmos capacity selects its dimensional realization.

Primary sources: [[library/representation-theory-for-subfactors-lambda-lattices-and-c-star-tensor-categories/inq|Popa and Vaes on admissible categorical representations, property (T), and the Kazhdan projection]], [[library/property-t-discrete-quantum-groups-and-subfactors-with-triangle-presentations/inq|Vaes and Valvekens on the universal tube-algebra averaging operator]], [[library/quantum-g2-categories-have-property-t/inq|Jones on property (T) for quantum \(G_2\) categories]], and [[library/tensor-categories-and-endomorphisms-of-von-neumann-algebras/inq|Bischoff, Longo, Kawahigashi, and Rehren on Q-system reconstruction and dimension conventions]].

[[contemporary-puzzles/yang-mills-mass-gap/receipts/quantum-g2-categorical-rigidity-receipt.py|The finite receipt]] and its [[contemporary-puzzles/yang-mills-mass-gap/receipts/quantum-g2-categorical-rigidity-receipt-output.txt|stored output]] check the quantum-dimension symmetry, the explicit Jones certificate, the classical capacity/certificate contrast, inversion of the conditional cosmic-depth equation, and the separately declared one-channel-birth numerical diagnostic. It does not calculate the universal Kazhdan constant, test the classical rigidity theorem, prove property \((T)\), construct a Q-system or physical carrier, validate the cosmic weld, select fusion depth, or establish a Yang--Mills gap.

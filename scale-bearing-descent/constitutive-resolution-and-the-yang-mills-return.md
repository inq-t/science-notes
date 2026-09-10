# Constitutive Resolution and the Yang–Mills Return

Finster's causal fermion systems suggest that resolution can help constitute an arena of comparisons. The variational object includes the measure whose support is spacetime; changing its microscopic realization can therefore change what counts as a point. This sharpens scale-bearing descent: seek one law that selects admissible realizations and returns both local Yang–Mills structure and a surviving comparison scale. Auxiliary cutoffs must cease to affect the exact return, but the master object need not lose every constitutive distinction. The missing conjecture concerns what its local return forgets, what it preserves, and why.

## The action can select its own arena

[[factive-cosmos/causal-fermion-systems-and-the-action-of-the-whole|The action of the whole]] identifies the decisive move in [[library/causal-fermion-systems-an-elementary-introduction/inq|Finster–Jokel's introduction]]. With a supplied separable complex Hilbert space \(\mathcal H\) and positive integer \(n\), let
\[
\mathcal F_n=\{x=x^*\in\mathcal B(\mathcal H):
n_+(x)\le n,\ n_-(x)\le n,\ \operatorname{rank}x<\infty\}.
\]
A causal fermion system is \((\mathcal H,\mathcal F_n,\rho)\), where \(\rho\) is a positive Borel measure for the operator-norm topology. Its spacetime is
\[
\boxed{M=\operatorname{supp}\rho.}
\tag{CR1}
\]
Spectra of products \(xy\) determine causal comparisons. The action varies \(\rho\), including its support, under specified constraints. It does not merely vary fields on an independently fixed set of spacetime points.

This is a substantive precedent for [[factive-cosmos/why-an-arena-of-facts|the backwards question]]. The arena and the relations expressed within it can be aspects of one variational object. In this language a point is already a local correlation operator, and its relation to another point involves their product. The starting \(\mathcal H\), positivity, complex scalars, rank bound and action are still supplied mathematical structure. Spin dimension \(n\) bounds local signatures; it does not derive spacetime dimension \(2n\). Nor is the initial \(\mathcal H\) automatically the vacuum Hilbert space of a returned quantum field theory.

Calling \(M\) factual has a limited exact meaning here: it is the support selected by the measure. A support point is not yet an obtained measurement record, and the universal measure is not automatically a Born probability. [[factive-cosmos/one-action-and-emitted-spacetime|Emitted spacetime]] adds the stronger requirement that the law supply record extension and the chronology against which its persistence is compared.

## A regulator can be an operation of realization

The introduction's concrete construction starts with a Lorentzian spin geometry and a chosen Hilbert space of Dirac solutions. A smoothing map \(\mathfrak R_\epsilon\), with bounded point evaluations, defines
\[
\begin{aligned}
\langle\psi,F^\epsilon(p)\phi\rangle_{\mathcal H}
&=-\prec(\mathfrak R_\epsilon\psi)(p)\mid
             (\mathfrak R_\epsilon\phi)(p)\succ_p,\\
\rho_\epsilon&=(F^\epsilon)_*\mu.
\end{aligned}
\tag{CR2}
\]
Thus \(\mathfrak R_\epsilon\) affects the local correlation operators and the spacetime they realize. The indefinite spin pairing on the right is distinct from the positive Hilbert pairing on the left. This construction encodes a supplied geometry; the abstract variational problem is the proposed place to select one.

In §4.2, Finster and Jokel explicitly treat different regularizations as different microscopic structures. Variable regularization examines a class of such structures. Their account seeks robust effective equation forms while allowing microscopic details to enter masses and couplings; selecting a preferred regularization through the causal action remains a further problem in that presentation. The meaningful borrowing is therefore **constitutive resolution**, not the claim that an arbitrary finite cutoff already returns the required quantum theory.

The same introduction explicitly studies a continuum limit as \(\epsilon\to0\). Its §5(b) describes a return of classical bosonic equations interacting with fermions through analysis of the causal-action Euler–Lagrange equations. Constitutive microscopic meaning and a mathematical removal limit coexist in this programme. That equation-level return does not by itself establish convergence of the complete quantum correlation hierarchy.

Three roles must be distinguished before assigning removal obligations.

| Data | Mathematical role | Obligation of an exact return |
|---|---|---|
| Auxiliary approximation \(a\) | A presentation used to calculate or approximate an object | Remove it, or prove independence of the admissible presentation |
| Constitutive realization \(\mathfrak X\), possibly represented using \(\mathfrak R_\epsilon\) | Data belonging to the master object and its comparison geometry | Specify which distinctions affect the returned theory and which become inaccessible |
| Returned scale \(\ell_G\) and dimensionless parameters | Invariants or calibration data of the local realization | Preserve a nonzero finite comparison duration and identify the allowed parameter freedom |

These are roles, not necessarily three independent numerical coordinates. The same symbol \(\epsilon\) can play different roles in different constructions. Finite rank, finite Hilbert dimension, finite total measure and discrete support are likewise different restrictions.

There are two admissible strategies. One can prove a limit in which microscopic details disappear while renormalized relations survive. Alternatively, one can construct an exact local sector or quotient of a richer realization. In the second strategy, products, state, covariance, domains and chronology must descend with the required strength; naming a quotient does not establish them. An approximation valid only above a fixed resolution is a different output.

## What the causal action teaches about scale

For the \(2n\) eigenvalues of \(xy\), padded with zeros, the causal Lagrangian is
\[
\mathcal L(x,y)=
\sum_i|\lambda_i^{xy}|^2
-\frac1{2n}\left(\sum_i|\lambda_i^{xy}|\right)^2,
\qquad
\mathcal S[\rho]=\iint\mathcal L\,d\rho\,d\rho.
\tag{CR3}
\]
The variational problem fixes total measure and integrated trace and imposes a spectral boundedness constraint. Its homogeneity makes a transcendental question especially visible: **which conditions prevent a candidate arena from losing all content under the very variations meant to select it?**

[[scale-bearing-descent/causal-action-normalization-and-coercivity|The normalization calculation]] proves that rescaling measure by \(u\) and operators by \(v\) sends
\[
(V,\tau,\mathcal S,\mathcal T)
\longmapsto(uV,uv\tau,u^2v^4\mathcal S,u^2v^4\mathcal T).
\tag{CR4}
\]
Nonzero volume and trace fix these two elementary normalization freedoms. They do not identify a metric length, and the quartic degree does not derive four-dimensional spacetime. Dimensionless constraint data remain.

The useful lesson is that admissibility does mathematical work before a local action is written. The stronger foundational programme would derive the admissibility conditions from the composition of comparisons. It need not derive a privileged numeral for a dimensional constant. It must explain a nontrivial realization class and relations that cannot be changed by choosing a different ruler.

There is a second, sharper requirement. Fixed volume and trace can coexist with action tending to zero as their weight is distributed among increasingly many orthogonal operator sectors. The same companion gives this exact example. It diagnoses what the normalization constraints alone permit; it does not compute a physical response or refute a stability theorem with additional hypotheses. Excluding the empty measure therefore leaves complete response control as a separate task. Ordinary algebraic connectedness or nonzero pairwise coupling would also be too weak: such couplings can approach zero.

This identifies a promising form of the missing law: **admissible extension must carry enough shared comparison structure that the norm of a complete distinction cannot be dispersed into arbitrarily weakly related channels.** [[scale-bearing-descent/coherent-comparison-lifts-and-bounded-descent|Bounded constructive descent and source extension]] is already a proposed algebraic implementation. The claim is to be established on a selected branch through its source relations, not imposed on every possible causal fermion system.

## Scale as a residue of local realization

[[library/causal-fermion-systems-spacetime-as-a-web-of-correlations/inq|Fischer and Paganini]] interpret spacetime as a web of correlations. For a specified class of systems, they relate causal-action minimization to suppression of causal-structure fluctuations. Their Minkowski example begins with a supplied Dirac mass and geometry; it does not select a pure Yang–Mills mass. Its importance here is that a background can become a collective description of correlations rather than their independent container.

This suggests a precise use of indiscernibility. Fix a candidate class of realizations by upstream composition, constraints, branch and renormalization conditions. Two microscopic presentations are equivalent for a given return only when they give the same **complete** local source functional, after the declared matching of units and renormalized operators. Agreement on one action term or a few two-point functions is insufficient. Defining this equivalence clarifies the target; proving that a useful class shares such a return is the universality conjecture.

The conjectural operation has type
\[
\mathsf{Ret}_G:
[\mathfrak X]_{\mathrm{admissible}}
\rightsquigarrow
\bigl(S_G,\mathsf{Id}^{\mathrm{ren}}_G,\ell_G,R_G\bigr).
\tag{CR5}
\]
Here \(S_G\) is the complete local evaluation, \(\mathsf{Id}^{\mathrm{ren}}_G\) its Yang–Mills field correspondence, \(\ell_G>0\) an inherited comparison duration, and \(R_G\) the response of the same source comparisons. The bracket does not posit a pre-existing categorical quotient. Its equivalences must be specified and its return proved.

The matching conditions must be fixed before using the gap they are meant to explain. A common change of units is harmless; retuning dimensionless microscopic data to impose the desired threshold would leave the selection problem unanswered.

The local classical expression can retain the curvature pairing while forgetting data that still distinguish the full state and its scale. [[scale-bearing-descent/scale-symmetry-and-cosmic-response|Scale-family covariance]] then permits
\[
\ell_G\mapsto s\ell_G,\qquad
H_G\mapsto s^{-1}U_sH_GU_s^{-1},\qquad
\ell_Gm_G\mapsto\ell_Gm_G.
\tag{CR6}
\]
The maps compare scale-related realizations; they need not be dilation symmetries of one fixed vacuum. We use a common length convention, with \(H_G,m_G\) in inverse-length units and duration expressed in length units. In four dimensions the classical curvature action is scale invariant, but that expression alone need not specify the complete realization from which it descends.

**The proposed duality is between a homogeneous local law and a pointed realization of comparison.** Their common parent would explain why a scale-free expression and a positive threshold belong together. CFS supplies a serious model for changing the variational domain in this way; the duality and its Yang–Mills return are our conjecture.

## A critical microscopic limit can have a massive return

For a fixed returned mass scale \(m>0\), its associated length \(\xi=1/m\) obeys
\[
am\longrightarrow0,\qquad
\frac{\xi}{a}=\frac1{am}\longrightarrow\infty
\quad(a\longrightarrow0).
\tag{CR7}
\]
The scale remains finite in the returned length convention while diverging in cutoff units. This is a scaling identity, not a theorem selecting a critical family. Thus a continuum construction should not demand a fixed positive gap in units of a vanishing lattice step. It can demand a positive comparison margin at one fixed returned duration \(\ell_G\).

The [[factive-cosmos/correlated-boundary-limit-and-yang-mills|correlated boundary proposal]] explores a complementary preservation law:
\[
\lambda_*^3=\alpha\ell_P^2R_*,
\qquad
\ell_P=\epsilon,\quad
R_*=\frac{L_0^3}{\epsilon^2}
\quad\Longrightarrow\quad
\lambda_*=\alpha^{1/3}L_0.
\tag{CR8}
\]
Here \(\alpha>0\) is dimensionless. This is an exact dimensional relation within the proposed family, not a derived selection of that family. It suggests how a local grain might survive vanishing gravitational length and receding boundary. CFS supplies no identification of its regularization with these variables merely because both use \(\epsilon\).

The next signature would connect the CFS constraints or their replacement to this relation, or to another law preserving \(\ell_G\). The resulting local theory must become autonomous: its exact correlations cannot require a finite cosmic box or residual propagating gravitational or matter fields. A common origin can survive as an inherited parameter without requiring the entire cosmic realization to remain inside the pure-gauge output.

## What must survive together

[[library/causal-fermion-systems-as-an-effective-collapse-theory/inq|Finster, Kleiner and Paganini]] give a relevant precedent for comparing norms. Under their small-potential assumptions, a nonlocal conserved inner product is related to the ordinary one through \(G_t=I+\Sigma_t>0\):
\[
\widetilde U_{t,t_0}=G_t^{1/2}U_{t,t_0}G_{t_0}^{-1/2}.
\tag{CR9}
\]
This transports the norm and evolution together, using the same supplied time parameter. It is a one-particle, generally time-dependent comparison in an effective construction, not a selection of chronology or the full neutral vacuum estimate needed here. Its structural lesson is that a returned norm should be transported with the dynamics.

The newer [Holographic Mixing and Fock Space Dynamics, §§1, 6–8](https://arxiv.org/html/2410.18045v2) develops a QED return with a cutoff in a controlled limiting regime, assuming stochastic fields and dephasing and making a specific covariance choice. The paper distinguishes that return from ultraviolet removal and records residual nonlocality. It gives a useful model of how microscopic composition can return quantum dynamics with identifiable corrections. Our target asks those defects to disappear in an exact local pure Yang–Mills return, with the same state and complete source hierarchy.

The quantitative condition is already owned by [[scale-bearing-descent/yang-mills-return-signature|the return signature]]. For all finite complex combinations of a source-complete positive-time family, put
\[
N_G(F)=\|Q_\Omega[F]\|^2,\qquad
D_{G,\ell_G}(F)
=\langle Q_\Omega[F],(I-e^{-2\ell_GH_G})Q_\Omega[F]\rangle.
\]
The missing positive Hermitian response satisfies
\[
b_GN_G(F)\le R_G(F,F)
\le L_G^2D_{G,\ell_G}(F)+\eta_GN_G(F),
\qquad b_G>\eta_G\ge0,\quad 0<L_G<\infty.
\tag{CR10}
\]
It suffices that this comparison hold uniformly through the chosen return. A constrained second variation of the causal action is one possible source of a response, provided its domain, constraint terms, redundant directions and map to complete marked sources are constructed. A Hessian on classical linearized variations alone is not source complete for the interacting quantum theory. Surface-layer inner products and second variations also must not be identified merely because both are bilinear.

There is an elementary reason to keep this slot explicit: the nonnegative causal Lagrangian is not a positive-definite preparation kernel on the full operator class. The two-point counterexample in [[scale-bearing-descent/causal-action-normalization-and-coercivity|the normalization companion]] excludes an unqualified identification \(\mathcal L=R_G\). A selected restriction might behave differently, but it would require its own proof. The same variational law would have to generate an appropriately typed response.

## The sharpened conjecture

**Conjecture — admissible resolution with a stable local return.** A finite law of complete comparison specifies a nonempty class of constrained pointed realizations before their spectra are chosen. For each compact simple \(G\), it admits a branch whose renormalized local return is Yang–Mills. Admissible changes of microscopic presentation within the specified basin preserve that complete return after declared parameter matching. The same law supplies a finite relational duration and a complete response satisfying (CR10), with a surviving positive margin.

The class must be described by upstream relations, not defined as the realizations that already have the desired Yang–Mills limit. Independence is required of auxiliary presentation choices; it need not erase genuine phase choices or all relevant dimensionless parameters. This is a refinement of the existing source-law and return conjectures, not a fourth independent mechanism.

Conditional on the full return, any
\[
0<\kappa_G<
\min\{1,(b_G-\eta_G)/L_G^2\}
\]
gives
\[
\boxed{\ell_Gm_G\ge-\tfrac12\log(1-\kappa_G)>0.}
\tag{CR11}
\]
[[positive-semigroup-decay/source-pairing-limit-and-the-mass-gap|The source-pairing theorem]] transports this bound using the complete reflected correlations; neither the microscopic measure nor its repairs must converge as operators on the physical carrier.

Finster's most useful challenge is consequently to the domain of explanation. The question becomes: **what makes a complete realization admissible, and what must remain distinguishable when it admits a local description?** If one algebraic law fixes both, the classical scale invariance and the mass threshold become two outputs of its realization map. The remaining work is to specify and establish that common law, rather than choose a scale after the local theory has been supplied.

# Modular Mirror Response and the Analytic Domain

Modular theory extends the finite Schmidt mirror to a cyclic–separating von Neumann algebra: an analytic observable has a bounded partner in the commutant with exactly the same action on the vacuum. Their difference annihilates the vacuum and acts on vacuum-created vectors as a commutator. This gives a concrete relational loss carrier and, for any finite bounded row, a normal completely positive whole process with a positive returned Hilbert generator. Analyticity fixes a real domain issue, not a physical clock or a uniform gap; the construction still has to justify its row, local compatibility and limits.

## The half-modular mirror

Let \(M\subseteq B(\mathcal H)\) have a cyclic and separating unit vector \(\Omega\). Write
\[
S(x\Omega)=x^*\Omega,\qquad S=J\Delta^{1/2},
\qquad \sigma_t(x)=\Delta^{it}x\Delta^{-it}.
\tag{MM1}
\]
Here the first rule is initially on \(M\Omega\), and \(S\) denotes its closed Tomita extension. In particular \(J\Omega=\Omega\), \(\Delta^{it}\Omega=\Omega\), and \(JMJ=M'\). The [[faithful-stationary-states-and-the-positive-clock|stationary-state theorem]] owns the core/domain argument, while the [[library/the-standard-form-of-von-neumann-algebras/inq|standard-form source]] supplies the surrounding representation framework.

Use the entire analytic \(*\)-subalgebra \(M_{\mathrm{an}}\): for \(A\in M_{\mathrm{an}}\), the real orbit \(t\mapsto\sigma_t(A)\) extends to an operator-norm entire function \(z\mapsto\sigma_z(A)\) with values in \(M\). This sufficient domain is chosen so that the imaginary-time values below are bounded operators and their products and adjoints remain defined.

For \(A\in M_{\mathrm{an}}\), put
\[
\boxed{
R_A=J\sigma_{-i/2}(A^*)J\in M',
\qquad D_A=A-R_A\in M\vee M'.
}
\tag{MM2}
\]
These are represented operators on the same \(\mathcal H\); \(R_A\) is not a new scalar-valued symbol or an unbounded formal exponential.

**Mirror theorem.**
\[
\boxed{
R_A\Omega=A\Omega,\qquad
D_A\Omega=0,\qquad
D_A(B\Omega)=[A,B]\Omega\quad(B\in M).
}
\tag{MM3}
\]
The test operator \(B\) need not be analytic.

Indeed, analytic continuation of
\(\Delta^{it}A^*\Omega=\sigma_t(A^*)\Omega\) gives
\[
\sigma_{-i/2}(A^*)\Omega=\Delta^{1/2}A^*\Omega.
\]
The vector \(A^*\Omega\) lies in \(\operatorname{Dom}S=\operatorname{Dom}\Delta^{1/2}\), and the entire analytic orbit identifies this vector-domain value with the bounded operator value. Hence
\[
R_A\Omega
=J\Delta^{1/2}A^*\Omega
=SA^*\Omega=A\Omega.
\]
Since \(R_A\) commutes with \(B\), the last identity of (MM3) follows:
\(AB\Omega-R_AB\Omega=AB\Omega-BA\Omega\).

The bounded mirror is unique whenever it exists. If \(R,\widetilde R\in M'\) have the same value on \(\Omega\), then
\((R-\widetilde R)B\Omega=B(R-\widetilde R)\Omega=0\).
Cyclicity for \(M\) gives \(R=\widetilde R\).

## Products reverse, while adjoints acquire a modular twist

The map \(A\mapsto R_A\) is complex-linear: the conjugate-linearity of \(A\mapsto A^*\) is canceled by that of \(X\mapsto JXJ\). Direct multiplication gives
\[
\boxed{
R_I=I,\qquad R_{AB}=R_BR_A.
}
\tag{MM4}
\]
Thus this is an opposite-algebra action on its analytic domain.

It is generally not a \(*\)-action. The analytic adjoint identity
\(\sigma_z(A)^*=\sigma_{\bar z}(A^*)\) gives
\[
\boxed{
R_A^*=R_{\sigma_{-i}(A^*)},
\qquad
\|R_A\|=\|\sigma_{i/2}(A)\|.
}
\tag{MM5}
\]
For example,
\[
R_{\sigma_{-i}(A^*)}
=J\sigma_{-i/2}\bigl(\sigma_{-i}(A^*)^*\bigr)J
=J\sigma_{i/2}(A)J=R_A^*.
\]
On the modular centralizer, where \(\sigma_t(A)=A\) for every real \(t\), the formula reduces to \(R_A=JA^*J\), the usual \(*\)-preserving opposite action. The centralizer is one sufficient extra condition; arbitrary analytic elements do not satisfy it.

In particular,
\[
\boxed{\|D_A\|\le\|A\|+\|\sigma_{i/2}(A)\|.}
\tag{MM6}
\]
The second norm is not controlled by the first uniformly without an additional analytic bound.

There is also an exact distinction between a central observable and a zero relational defect:
\[
D_A=0\quad\Longleftrightarrow\quad A\in Z(M),
\qquad A\in M_{\mathrm{an}}.
\tag{MM7}
\]
The forward implication uses \(A=R_A\in M\cap M'\). Conversely a central \(A\) has \([A,B]=0\) for all \(B\in M\), so the bounded \(D_A\) vanishes on the dense set \(M\Omega\).

For a factor, a nonscalar analytic \(A\) therefore gives a nonzero \(D_A\), and that defect belongs to neither \(M\) nor \(M'\). If it belonged to \(M\), its vacuum-annihilation property and separatingness would force it to vanish; the same argument uses separatingness for \(M'\). The [[local-vacuum-faithfulness-and-the-loss-carrier|local-loss theorem]] is respected precisely because the defect acts between the opposed algebras, not inside either one.

## The finite density formula fixes the sign

For \(M_d(\mathbb C)\) acting by left multiplication on Hilbert–Schmidt matrices, take
\[
\Omega=\rho^{1/2},\qquad \rho>0,\quad\operatorname{Tr}\rho=1,\qquad
J(T)=T^*.
\]
Then \(\sigma_t(A)=\rho^{it}A\rho^{-it}\), and (MM2) becomes
\[
\boxed{
R_A(T)=T\,\rho^{-1/2}A\rho^{1/2}.
}
\tag{MM8}
\]
The minus sign in \(\sigma_{-i/2}(A^*)\) is essential: its adjoint, entering the right multiplication, is \(\rho^{-1/2}A\rho^{1/2}\).

In the Schmidt tensor presentation, right multiplication by this matrix becomes action on the second factor by its transpose
\[
B_A=\rho^{1/2}A^T\rho^{-1/2}
\]
when \(\rho\) is diagonal in the chosen Schmidt basis. This is exactly the [[local-vacuum-faithfulness-and-the-loss-carrier#A loss can operate between two faithful factors|finite opposed-factor mirror]], not a different prescription. Its finite common-kernel and uniform-state response proofs remain in that owner.

## Analytic approximation is available, but its bounds can deteriorate

The domain \(M_{\mathrm{an}}\) is not an empty regularity demand. For any \(A\in M\) and \(\varepsilon>0\), define the Gaussian modular smoothing by an ultraweak integral:
\[
A_\varepsilon
=\frac1{\sqrt{\pi\varepsilon}}
\int_{\mathbb R}e^{-t^2/\varepsilon}\sigma_t(A)\,dt.
\tag{MM9}
\]
Its analytic extension is
\[
\sigma_z(A_\varepsilon)
=\frac1{\sqrt{\pi\varepsilon}}
\int_{\mathbb R}e^{-(t-z)^2/\varepsilon}\sigma_t(A)\,dt.
\]
For real \(z\) this is a change of variables in the modular action; the integral extends it to an operator-norm entire function. The Gaussian kernel and its complex derivatives are locally dominated in \(L^1\), proving norm analyticity. Its elementary bound is
\[
\boxed{
\|\sigma_z(A_\varepsilon)\|
\le e^{(\operatorname{Im}z)^2/\varepsilon}\|A\|,
\qquad
\|R_{A_\varepsilon}\|
\le e^{1/(4\varepsilon)}\|A\|.
}
\tag{MM10}
\]
Strong-\(*\) continuity of the modular group and the Gaussian approximate identity give \(A_\varepsilon\to A\) strongly-\(*\), with \(\|A_\varepsilon\|\le\|A\|\). This proves strong-\(*\) density of analytic elements. It does not give a uniform bounded mirror as the smoothing is removed; (MM10) is an upper estimate, not a sharp necessary cost or a physical scale law.

There can genuinely be no bounded mirror for a bounded nonanalytic input. On the standard Hilbert–Schmidt representation of \(B(\ell^2(\mathbb N))\), choose a faithful density
\[
\rho e_n=p_ne_n,\qquad p_n=Z^{-1}2^{-n^2},\qquad n\ge1,
\]
where \(Z=\sum_{n\ge1}2^{-n^2}\), and let \(V e_n=e_{n+1}\) be the unilateral shift. Each matrix unit \(A_n=|n+1\rangle\langle n|\) is entire analytic, with
\[
\|A_n\|=1,\qquad
\|R_{A_n}\|=\sqrt{p_n/p_{n+1}}=2^{n+1/2}\longrightarrow\infty.
\tag{MM11}
\]
The formal right coefficient of the bounded \(V\) is
\[
C=\rho^{-1/2}V\rho^{1/2},\qquad
Ce_n=2^{n+1/2}e_{n+1},
\]
which is unbounded. The failure of a bounded mirror can also be proved without manipulating that formal product. If \(R\in M'\) satisfied \(R\Omega=V\Omega\), set \(B_n=p_{n+1}^{-1/2}|1\rangle\langle n+1|\). On the Hilbert–Schmidt carrier,
\[
B_n\Omega=|1\rangle\langle n+1|,\qquad
R(B_n\Omega)=B_nV\Omega
=2^{n+1/2}|1\rangle\langle n|.
\]
The input vectors have norm one, while their images have unbounded norms. Such an \(R\) cannot be bounded. Thus not every bounded observable admits the bounded mirror in (MM2).

The example separates three facts: each \(A_n\) is analytic; its mirror is bounded individually; their mirror norms are not uniformly bounded. Passing to a row, a cutoff removal or an infinite family must retain this distinction.

## A finite bounded analytic row has an exact whole-process return

Choose finitely many \(A_1,\ldots,A_r\in M_{\mathrm{an}}\), and put
\[
\mathbf D\psi=(D_{A_1}\psi,\ldots,D_{A_r}\psi),\qquad
\boxed{K=\tfrac12\mathbf D^*\mathbf D
=\tfrac12\sum_{a=1}^rD_{A_a}^*D_{A_a}.}
\tag{MM12}
\]
This is a bounded positive operator, \(K\Omega=0\), with
\[
\|K\|
\le\frac12\sum_{a=1}^r
\bigl(\|A_a\|+\|\sigma_{i/2}(A_a)\|\bigr)^2.
\tag{MM13}
\]
No finite-dimensional hypothesis on \(\mathcal H\) is needed for this bounded-row statement.

On \(B(\mathcal H)\), define
\[
\mathscr G(X)=\sum_aD_{A_a}^*XD_{A_a}-KX-XK.
\tag{MM14}
\]
This is a bounded normal generator of a uniformly continuous normal UCP semigroup \(T_s=e^{s\mathscr G}\), \(s\ge0\). To verify this directly, the maps
\[
X\mapsto e^{-sK}Xe^{-sK},\qquad
\mathscr J(X)=\sum_aD_{A_a}^*XD_{A_a}
\]
are normal CP. Their ordered Dyson series converges in operator-map norm, with the \(n\)-jump term bounded by \(\|\mathscr J\|^ns^n/n!\). Its normal CP terms give a normal CP limit. Since \(\mathscr G(I)=0\), the limit is unital.

For the pure vector state \(\omega_\Omega\) on this full algebra,
\[
\mathscr G(X)\Omega=-KX\Omega.
\]
Bounded exponentiation therefore gives the exact return
\[
\boxed{
T_s(X)\Omega=e^{-sK}X\Omega,\qquad
\omega_\Omega T_s=\omega_\Omega.
}
\tag{MM15}
\]
The map \(q:X\mapsto X\Omega\) is onto \(\mathcal H\), since rank-one \(X=|\psi\rangle\langle\Omega|\) realizes any \(\psi\). Thus the finite [[directed-analytic-realization/pure-vacuum-loss-and-the-returned-clock|pure-vacuum quotient proof]] extends to an arbitrary \(\mathcal H\) for this finite bounded row. It is still a Hilbert quotient by a left ideal, not a quotient algebra.

The same bounded proof gives the stationary Schwarz response
\[
\omega_\Omega\!\left(T_s(X^*X)-T_s(X)^*T_s(X)\right)
=\int_0^s\|\mathbf D e^{-uK}X\Omega\|^2\,du.
\tag{MM16}
\]
The positive clock \(e^{-itK}\) normalizes the full \(B(\mathcal H)\), with automorphisms \(X\mapsto e^{itK}Xe^{-itK}\). This clock is an analytic continuation of the returned Hilbert semigroup, not of the dissipative superoperator as an automorphism group.

If \(M\) is a factor, then \(M\vee M'=B(\mathcal H)\), since its commutant is \(Z(M)=\mathbb C I\). The full operator algebra in this case is exactly the algebra generated by both partners. Its vector state is nonfaithful when \(\dim\mathcal H>1\), despite being faithful on \(M\) and \(M'\) separately.

For nonzero \(K\), the [[faithful-stationary-states-and-the-positive-clock|faithful stationary clock theorem]] prohibits this positive group from normalizing the same \(M\) for every time. Returning a clock on the joined algebra is not yet returning clock dynamics on a net of appropriate local algebras. Modular time \(\sigma_t\), used to construct the mirror, has not been identified with this positive clock parameter.

## Factoriality does not supply the missing lower bound

For the chosen row, the exact condition for a centered bound remains
\[
\boxed{
K\ge\delta(I-P_\Omega)
\quad\Longleftrightarrow\quad
\sum_a\|D_{A_a}\psi\|^2\ge2\delta\|\psi\|^2
\quad(\psi\perp\Omega).
}
\tag{MM17}
\]
Factoriality identifies the center, not the common kernel or quantitative coercivity of an arbitrarily selected finite row.

For example, in the tracial standard representation of the factor \(M_2\), the single analytic \(A=Z\) gives
\(D_A(T)=[Z,T]\), whose kernel contains both \(I\) and \(Z\). Even a generating row need not have a uniform gap in a family. Take
\[
A_1=Z,\qquad A_2=\varepsilon X,\qquad 0<\varepsilon\le1.
\]
Both elements are analytic, they generate \(M_2\), and their common defect kernel is the scalar line. In the Hilbert–Schmidt Pauli basis \(I,X,Y,Z\),
\[
\boxed{
K_\varepsilon
=\operatorname{diag}\bigl(0,\ 2,\ 2(1+\varepsilon^2),\ 2\varepsilon^2\bigr),
\qquad \operatorname{gap}K_\varepsilon=2\varepsilon^2.
}
\tag{MM18}
\]
One row norm stays fixed and the common kernel stays a line while the gap closes. In infinite dimension, even identification of a one-dimensional kernel is not a proof that the remaining spectrum is separated from zero.

The construction has eliminated an arbitrary bounded mirror choice: the state and modular analytic observable determine it uniquely. It has not selected a finite analytic row, its channel metric, a uniform analytic bound, a spatial arena or a dimensionful rate. Countably infinite or unbounded rows require closability, domain control and a conservative process realization beyond the bounded Dyson argument above. Those are concrete next interfaces; neither factoriality nor the name “modular” discharges them.

[[expected-inclusions-and-mirror-clock-consistency|The inclusion calculation]]
shows the next compatibility issue on a concrete finite carrier:
commutators and squared forms intertwine, while mirror adjoints and the
clock can leak outside a correlated local inclusion.
[[coarse-response-memory/spectral-readout-and-the-visible-gap|Complete spectral readouts]]
retain that information without imposing autonomous local clocks.

[[directed-analytic-realization/mirror_inclusion_receipt.py|The mirror-inclusion receipt]] checks the cyclic commutator action and Hilbert–Schmidt adjoint identities, including the nonuniform modular twist. [[directed-analytic-realization/mirror-inclusion-receipt-output.txt|Its output]] records exact finite comparisons; the analytic-domain, norm-growth and bounded infinite-carrier proofs are given above.

# The Trichotomy Identification

The conjugacy classification of $\mathrm{SL}(2,\mathbb R)$ — elliptic, parabolic, hyperbolic — and the classification of Lorentz transformations in $2{+}1$ dimensions — rotations, null rotations, boosts — are one classification, because $\mathrm{SL}(2,\mathbb R)\cong\mathrm{Spin}(2,1)$. The parabolic class is exactly the non-semisimple one: its elements are $\mathbf1+N$ with $N$ nilpotent. This note fixes the exact statement, its operator-algebraic instance at the wall, and the reading it licenses.

## The exact statement

**[EXACT]** For $g\in\mathrm{SL}(2,\mathbb R)$, $g\ne\pm\mathbf1$: $|\operatorname{tr}g|<2$ iff $g$ is conjugate to a rotation (elliptic; fixed point in the upper half-plane; finite order possible); $|\operatorname{tr}g|>2$ iff conjugate to a dilation $\operatorname{diag}(\lambda,\lambda^{-1})$ (hyperbolic; two fixed points on the boundary; a boost); $|\operatorname{tr}g|=2$ iff conjugate to a unipotent $\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}$ (parabolic; one boundary fixed point; a null rotation). Under $\mathrm{SL}(2,\mathbb R)\cong\mathrm{Spin}(2,1)$ these are the timelike, spacelike, and null one-parameter subgroups of the $2{+}1$ Lorentz group. Parabolic is the unique class that cannot be diagonalized: its generator is nilpotent, $N^2=0$ in the defining representation. **Nilpotency is the algebraic signature of null.**

## The wall instance

**[STANDARD]** A half-sided modular inclusion is equivalent to a positive-energy representation of the two-parameter affine group: a modular flow $\Delta^{it}$ (hyperbolic — the boost, hence temperature, per [[deriving-g-v2/the-modular-register-is-g-free|the modular audit]]) and a null-translation semigroup $U(a)=e^{iaP}$, $P\ge0$ (parabolic), obeying

$$
\Delta^{it}\,U(a)\,\Delta^{-it}=U(e^{-2\pi t}a).
$$

The horizon's two algebraic ingredients are thus exactly one hyperbolic and one parabolic element, and the radical-copernicanism audit's dissolution of the "non-invertible frame" puzzle — the arrow as spectral positivity seen from a corner — is this pair doing its work. The gating question recorded there and consumed by [[construction-bridges|the bridges note]] is whether the programme's wall family realizes this pair as a chain.

## The reading

**[PROPOSED READING, built on the exact core]** *Cusp is to modular family as horizon is to spacetime.* In the $(3,4,\infty)$ family of [[s6-deep-read|the manuscript]], the base's three special classes are two elliptic and one parabolic; the parabolic point is the cusp, its monodromy is $T_0=\mathbf1+N$ with $N^2=0$ (receipt-verified in `receipts/`), and its rank-two image $\Lambda_{\mathrm{tor}}=\langle\hat w,\hat\delta\rangle$ is the vanishing data. In spacetime, the wall's generator is the parabolic $U(a)$ with the boost as its dilator. Both are the locus where the acting element stops being diagonalizable — where semisimple presentation fails. The programme's slogan form: **semisimple = bulk; nilpotent = wall.** This dovetails with [[algebra/local-global-individuation|the presentation/process split]]: reversible presentation changes live in the semisimple directions, while the wall's defining datum is precisely the non-semisimple part — which is why [[construction-bridges|Bridge 1]] proposes nilpotent holonomy as a *requirement* on cross-fiber transport rather than a defect.

## Boundary

The identification is exact for the group theory and standard for the operator algebra; everything connecting it to the manuscript's cusp is conditional on that source's status ([[algebra/s6-manuscript-branch|the branch note]]), and everything connecting it to cosmological walls is open until the gate question is answered. The trichotomy does not by itself supply a state, a ledger, or an arrow — it supplies the *type* of the datum a wall must carry.

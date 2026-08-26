# The Positive $C^*$-Envelope of a Real $A_2$ Degeneration

The real $A_2$ cubic has an exact fiberwise observable-completion theorem: its enveloping $C^*$-algebra is $\mathbb C^r$, where $r$ is the number of distinct real roots. In the closure of the three-real-root chamber this gives the type profile $\mathbb C^3$, $\mathbb C^2$, and $\mathbb C$ on the generic, double-root, and triple-root strata. These are fiber types, not a canonical chain of specialization homomorphisms. A separate stabilizer-average construction does give actual completely positive maps $\mathbb C^3\to\mathbb C^2\to\mathbb C$. The distinction is the point: nilpotent infinitesimal thickness survives in the algebraic fibers while every $*$-representation by bounded operators kills its self-adjoint nilpotents, but neither fact makes monodromy into unitary transport or selects a physical state law.

## The cubic family and its real chamber

Consider

$$
p_{a,b}(u)=u^3+au+b,
\qquad
E_{a,b}:=\mathbb C[u]/(p_{a,b}),
\qquad
a,b\in\mathbb R,
$$

with the involution $u^*=u$. Use the repository's signed discriminant coordinate

$$
\Delta_{A_2}(a,b):=4a^3+27b^2,
$$

which is the negative of the usual polynomial discriminant. Its zero locus is the discriminant cusp. Only $|\Delta_{A_2}|$ will enter the scale character.

Restrict first to the chamber in which all three roots are real. Away from the discriminant, evaluation at the three roots gives

$$
E_{a,b}\cong\mathbb C^3
$$

as a finite-dimensional commutative $*$-algebra. This is the positive version of the three-sheet sector used in [[a2-ternary-response/entry|the ternary-response test]]. In the one-real-root chamber the declared real $*$-structure has enveloping $C^*$-algebra $\mathbb C$; retaining the conjugate nonreal sheets as positive characters would require a different real-form problem.

At a smooth real point of the discriminant, write

$$
p(u)=(u-q)^2(u+2q),
\qquad q\ne0.
$$

The Chinese remainder theorem separates the spectator root from the double root:

$$
E_{a,b}
\cong
\mathbb C[\epsilon]/(\epsilon^2)\times\mathbb C.
$$

At the cusp $(a,b)=(0,0)$,

$$
E_{0,0}=\mathbb C[\epsilon]/(\epsilon^3).
$$

The powers of $\epsilon$ record nonreduced scheme structure. They are not extra ordinary points.

## The positive-completion theorem

**Proposition.** Let $A$ be a $C^*$-algebra and let $x=x^*\in A$. If $x^k=0$ for some positive integer $k$, then $x=0$.

**Proof.** A self-adjoint element is normal. Its norm equals its spectral radius, while a nilpotent has spectrum $\{0\}$. Hence $\lVert x\rVert=0$. $\square$

**Theorem.** Let $r(a,b)$ be the number of distinct real roots of $p_{a,b}$. The enveloping $C^*$-algebra over $*$-representations by bounded operators is

$$
\boxed{
C_u^*(E_{a,b})\cong\mathbb C^{r(a,b)}.}
$$

Equivalently, for $[f]\in E_{a,b}$ its universal seminorm is

$$
\lVert[f]\rVert_u
:=
\sup_{\pi}\lVert\pi([f])\rVert
=
\max_{\lambda\in Z_{\mathbb R}(p_{a,b})}|f(\lambda)|.
$$

**Proof.** In any $*$-representation by bounded operators, the image $T$ of $u$ is self-adjoint and satisfies $p_{a,b}(T)=0$. The spectral theorem therefore puts $\operatorname{spec}(T)$ inside the distinct real zero set of $p_{a,b}$; root multiplicities and nonreal roots contribute no characters. Conversely, evaluation at every distinct real root gives a bounded one-dimensional $*$-representation. Lagrange interpolation realizes every function on that finite root set by a polynomial, so the direct sum of the evaluation representations has image $\mathbb C^{r(a,b)}$ and gives the displayed norm. $\square$

Consequently, in the closure of the three-real-root chamber, the fiber types are

$$
\boxed{
\bigl(\mathbb C^3,\mathbb C^2,\mathbb C\bigr),}
$$

for the generic three-real-root stratum, a smooth double-root stratum, and the triple-root cusp respectively. A generic cubic in the one-real-root chamber also has completion $\mathbb C$, so scalar completion alone does not characterize the cusp. The cusp is distinguished by its discriminant position and nonreduced algebraic source.

## Fiber types are not specialization arrows

The displayed triple does not itself construct homomorphisms between completions at different parameter values. Evaluation characters move and collide as $(a,b)$ changes, and a specialization map requires a declared family, identifications, or a continuous-field construction. Calling the type profile a chain of $*$-homomorphisms would add data the cubic equation has not supplied.

There is, however, a separate exact chain on one labelled generic sheet algebra. Choose

$$
\{1\}\subset\mathbb Z_2\subset S_3,
$$

where $\mathbb Z_2$ transposes the pair that collides at the chosen smooth wall. Then

$$
(\mathbb C^3)^{\{1\}}
\supset
(\mathbb C^3)^{\mathbb Z_2}
\supset
(\mathbb C^3)^{S_3}
\cong
\mathbb C^3\supset\mathbb C^2\supset\mathbb C.
$$

Group averaging supplies the first conditional expectation, and restriction of the full $S_3$ average supplies the second:

$$
\mathbb C^3
\xrightarrow{E_{\mathbb Z_2}}
(\mathbb C^3)^{\mathbb Z_2}
\xrightarrow{\left.E_{S_3}\right|_{(\mathbb C^3)^{\mathbb Z_2}}}
(\mathbb C^3)^{S_3}.
$$

The second formula is not an average for an $S_3$ action on $(\mathbb C^3)^{\mathbb Z_2}$, since that subalgebra is not $S_3$-stable. In coordinates $(a,a,b)$ it is

$$
(a,a,b)\longmapsto\frac{2a+b}{3}\mathbf1,
$$

and it preserves the binary state with orbit weights $(2/3,1/3)$, not the balanced state $(1/2,1/2)$. More generally, a group expectation is state-preserving only for an invariant state, which the cubic geometry does not itself select.

The observable expectation $E_{\mathbb Z_2}:\mathbb C^3\to\mathbb C^2$ is the Heisenberg-picture retraction. The corresponding coarse-graining of a sheet distribution comes from restricting states along $\mathbb C^2\hookrightarrow\mathbb C^3$:

$$
(p_1,p_2,p_3)\longmapsto(p_1+p_2,p_3).
$$

Thus the subgroup choice constructs a binary observable algebra and an exact coarse-graining, but it does not construct an open binary state family or the CST balanced law. These maps agree with the three fiber types but are not induced by specialization.

This result is exact elementary algebra for the declared real cubic. Its use in the complex inverse-cover programme additionally requires a compatible real structure and a real-rooted slice, besides the conditional source status recorded in [[algebra/a2-inverse-cover|the $A_2$ inverse-cover note]].

## Why nilpotent monodromy is not unitary transport

There is a second exact same-representation obstruction. If a bounded operator on a positive-definite Hilbert space is unitary and has the form

$$
U=\mathbf1+L,
\qquad L^k=0,
$$

then $L=0$. Indeed, $L=U-\mathbf1$ is normal because it is a polynomial in the normal operator $U$, and a normal nilpotent vanishes. Therefore

$$
\boxed{
\text{one nonidentity operator cannot be both unitary and unipotent}.}
$$

This forbids a literal operator identification. It does not forbid an abstract unipotent group element from having a nontrivial unitary image in a different representation. A nilpotent may instead live in a Gauss--Manin or vanishing-cycle register, in a non-self-adjoint operator realization, or in the kernel of a nonfaithful positive realization. A positive process can be built from such an operator only after an involution, Hilbert structure, and completely positive law have been supplied. None of those is selected by the nonreduced algebra alone.

This is also why the parabolic translation in a half-sided modular inclusion must be typed carefully. The affine or Möbius subgroup is parabolic in its finite-dimensional Lie-group representation; its Hilbert-space implementer $U(r)=e^{irP}$ is unitary but is not thereby algebraically unipotent in that representation, and the positive generator $P$ is not thereby nilpotent.

## A literal discriminant depth

The symmetric real ray

$$
p_t(u)=u^3-t^2u,
\qquad t>0,
$$

has roots $(-t,0,t)$ and

$$
\Delta_{A_2}(t)=-4t^6.
$$

Writing $t=t_*e^{-N}$ gives the exact logarithmic degeneration coordinate

$$
\boxed{
N=-\frac16\log\frac{|\Delta_{A_2}(t)|}{|\Delta_{A_2}(t_*)|}.}
$$

Thus $N\to+\infty$ literally means infinite logarithmic depth toward the triple-root cusp. It does not mean infinite proper time, distance, energy, or entropy. Those identifications require separate realization maps.

For every finite $N$ on this ray the enveloping $C^*$-algebra has type $\mathbb C^3$; the cusp fiber at the ideal boundary has type $\mathbb C$. This is a jump in fiberwise completion type, not a continuous deletion map between the fibers. The nonreduced cusp still remembers infinitesimal thickness while its $*$-representations by bounded operators distinguish only the scalar unit. In the language of [[inbox/radical-copernicanism/commentary-part-2/varieties-of-nothing|the null-structure audit]], the cusp is not the zero algebra. It is **nothing in particular** under this functor.

## Programme consequence

This closes one part of the wall problem and kills one proposed shortcut.

- $A_2$ has a binary enveloping-$C^*$ **fiber type** at a smooth fold: the double root and spectator give two real characters.
- After a sheet labelling and subgroup choice, stabilizer averaging constructs a binary observable subalgebra, while state restriction performs the coarse-graining $(p_1,p_2,p_3)\mapsto(p_1+p_2,p_3)$.
- The cusp completion is scalar, but so is the generic one-real-root chamber; the discriminant and nonreduced source, not scalarity alone, identify the cusp.
- Nilpotent structure is a candidate source of nonfaithful realization, not a candidate unitary cross-fiber transport.
- The algebraic degeneration coordinate is internally defined and can be compared with another logarithmic scale character without using $G$ or an expansion history.

[[wall-construction-interface/core-spectral-wall|The core spectral wall]] constructs the complementary positive state, transport, and response data. [[wall-construction-interface/scale-character-solder|The scale-character solder]] states exactly what is gained—and what remains a choice—when its trace scale is matched to the discriminant depth above.

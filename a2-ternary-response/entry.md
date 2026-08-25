# The $A_2$ Ternary Response Test

The three-sheeted inverse cover associated conditionally with the local $A_2$ construction supplies a natural audit of the programme's balanced binary response. On the equal-weight commuting three-state model, a trace-zero root generator has Fisher--BKM response $2(\cosh\theta+2)/(1+2\cosh\theta)^2$, not $\operatorname{sech}^2\theta$. The calculation is exact in the finite model and shows that a binary wall must be derived by a specified decoupling, conditioning, or sufficient channel; the algebraic cover alone does not remove its third sheet.

## Why $A_2$ poses a ternary question

Conditional on [[algebra/a2-inverse-cover|the $A_2$ inverse-cover construction]], the complement of the inverse discriminant carries a connected degree-three finite étale cover with full sheet monodromy

$$
S_3=W(A_2).
$$

Here **ternary** comes from the three sheets of that cover. The name $A_2$ comes from the transverse cusp singularity and its Weyl monodromy. Rank two, three sheets, six roots, and the order of a monodromy element are different invariants.

Étale-locally the pushforward algebra splits as three labeled lines. That motivates the finite commutative model

$$
\mathcal A_3=\mathbb C^3
$$

with its uniform reference state. It does not prove that the holomorphic pushforward algebra is already a physical $C^*$-algebra or that a faithful state has been selected on a wall. Passing to $\mathbb C^3$ is a **[FINITE MODEL]** used to ask what the most symmetric three-sheet response would be.

Choose one trace-zero root direction,

$$
Q=\operatorname{diag}(1,-1,0).
$$

The choice is local: full $S_3$ monodromy permutes the roots, so it supplies no globally preferred $Q$. The uniform reference makes every root choice isometric, but it does not turn the choice into a canonical global section.

## The equal-weight three-state family

Let

$$
\rho_0=\frac13\mathbf1_3
$$

and form the commuting exponential family

$$
\rho_\theta
:=
\frac{\rho_0e^{\theta Q}}
{\operatorname{Tr}(\rho_0e^{\theta Q})}
=
\frac1{1+2\cosh\theta}
\operatorname{diag}(e^\theta,e^{-\theta},1).
$$

The log-partition potential, up to its irrelevant constant, is

$$
\Psi_{A_2}(\theta)
=\log\!\left(\frac{1+2\cosh\theta}{3}\right).
$$

Writing

$$
Z(\theta):=1+2\cosh\theta,
$$

the three probabilities are

$$
p_+(\theta)=\frac{e^\theta}{Z(\theta)},
\qquad
p_-(\theta)=\frac{e^{-\theta}}{Z(\theta)},
\qquad
p_0(\theta)=\frac1{Z(\theta)}.
$$

The polarization along $Q$ is

$$
m(\theta)
:=\operatorname{Tr}(\rho_\theta Q)
=\Psi_{A_2}'(\theta)
=\frac{2\sinh\theta}{1+2\cosh\theta}.
$$

Because the family commutes, its BKM coefficient is its ordinary Fisher information and the variance of $Q$; [[fisher-response|Fisher response]] explains this equality and its meaning. Direct differentiation gives the **[EXACT FINITE CALCULATION]**

$$
\boxed{
g_{A_2}(\theta)
:=\Psi_{A_2}''(\theta)
=\operatorname{Var}_{\rho_\theta}(Q)
=\frac{2(\cosh\theta+2)}{(1+2\cosh\theta)^2}.}
$$

Its first response variation is likewise exact:

$$
\boxed{
C_{A_2}(\theta)
:=\Psi_{A_2}'''(\theta)
=-\frac{2\sinh\theta(2\cosh\theta+7)}
{(1+2\cosh\theta)^3}.}
$$

These formulas are a new project calculation in the finite three-state model. They are not claimed by the inverse-cover or singularity-theory sources.

## The ternary allocation identity

Unlike a binary involution, $Q$ has a zero eigenspace:

$$
Q^2=\operatorname{diag}(1,1,0).
$$

Consequently,

$$
\langle Q^2\rangle_{\rho_\theta}=1-p_0(\theta)
$$

and variance decomposition gives

$$
\boxed{
m(\theta)^2+g_{A_2}(\theta)+p_0(\theta)=1.}
$$

The normalized unit is therefore allocated among resolved polarization, local susceptibility, and occupancy of the neutral sheet. The final term is not automatically lost information, gravity, or a hidden reservoir. In this model it is simply the probability of the $Q=0$ outcome.

At the symmetric point,

$$
m(0)=0,
\qquad
g_{A_2}(0)=\frac23,
\qquad
p_0(0)=\frac13.
$$

The third sheet is maximally visible exactly where the balanced binary model would place its unit response peak.

## Comparison with balanced binary geometry

The existing [[binary-information-geometry/balanced-exponential-family|balanced binary family]] is exact once a two-outcome channel has been granted:

$$
g_{\mathrm{bin}}(\theta)=\operatorname{sech}^2\theta.
$$

The two models differ before any cosmological interpretation is added:

| datum | balanced binary | equal-weight three-sheet model |
|---|---:|---:|
| generator spectrum | $\{+1,-1\}$ | $\{+1,-1,0\}$ |
| raw Boltzmann-weight sum | $2\cosh\theta$ | $1+2\cosh\theta$ |
| response at $\theta=0$ | $1$ | $2/3$ |
| large-$|\theta|$ response | $4e^{-2|\theta|}$ | $e^{-|\theta|}$ |
| normalized allocation | $m^2+g=1$ | $m^2+g+p_0=1$ |

An undetermined extensive multiplicity can rescale either metric, so peak height alone is not a physical discriminator until normalization is fixed. The different shape, tail, and third allocation term remain genuine mathematical differences in the normalized families.

## What would derive the binary limit

Deleting the symbol $0$ from the display is not a construction. At least three mathematically different routes could produce a binary family:

1. **Spectral decoupling.** Give the neutral state a positive gap $\Delta$ and use

   $$
   \rho_{\theta,\Delta}
   =\frac{\operatorname{diag}(e^\theta,e^{-\theta},e^{-\Delta})}
   {2\cosh\theta+e^{-\Delta}}.
   $$

   For fixed $\theta$, the limit $\Delta\to+\infty$ gives the balanced binary family.

2. **Conditioning or postselection.** Compress to the $\{+,-\}$ sector and renormalize. This yields the binary law, but the renormalization is a selective instrument rather than an everywhere deterministic trace-preserving loss map.

3. **A derived sufficient channel.** Construct a physical channel onto two outcomes and prove that its pushed-forward family is balanced and has no residual third-mode response. A generic coarse graining that merely merges the neutral outcome with one of the others does not return $\operatorname{sech}^2\theta$.

At a smooth point of a cubic discriminant, local inertia exchanges a pair of sheets while the third remains separate. That fold geometry suggests where a two-level effective sector might arise, but it supplies neither a gap nor a state-selection law. Those belong to [[wall-construction-interface/binary-channel|the binary-channel obligation]].

## Claim boundary

The displayed response and allocation identities are exact for faithful finite commuting states at finite $\theta$. Everything connecting them to the foundational programme remains separately typed:

- the degree-three $A_2$ inverse package is conditional on an unreviewed local construction and its exceptional 2026 input;
- the holomorphic inverse cover has not been realized as a wall observable algebra with a positive involution and faithful state;
- $Q$ is a locally selected root direction, not a globally selected scale tangent;
- $\theta$ is an affine statistical parameter, not yet time, scale, or a cosmological e-fold;
- monodromy is reversible relabeling and does not itself implement forgetting;
- neither response profile is yet a spatial covariance, a probability precision, an area modulus, a source for gravity, or an empirical prediction.

[[programme-impact|The programme impact]] is therefore an upgrade in discrimination: algebraic geometry supplies a natural competitor to the binary ansatz and names the exact operation that a binary theory must construct. [[sources-and-status|The source ledger]] separates the primary literature, conditional $A_2$ import, and new finite calculation.

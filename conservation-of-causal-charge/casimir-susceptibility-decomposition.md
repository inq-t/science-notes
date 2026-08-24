# Casimir--Susceptibility Decomposition

A quadratic Casimir in a finite-dimensional unitary representation decomposes into the squared norm of the state's mean generator and a positive covariance remainder. The binary causal-wall identity is the rank-one example. Interpreting the remainder as BKM capacity or gravity is a further construction, but the proposition identifies the group-theoretic form that such a construction should generalize.

## Proposition

Let \(T_a=T_a^*\) be generators in a finite-dimensional unitary representation, and let \(\kappa^{ab}\) be a real symmetric positive-definite invariant form on their span. Suppose the symmetrized quadratic Casimir acts as

$$
C_2
:=\frac12\kappa^{ab}\{T_a,T_b\}
=c_R\mathbf1.
$$

For a state \(\omega\), define

$$
m_a:=\omega(T_a)
$$

and the symmetrized covariance matrix

$$
\Sigma_{ab}
:=\frac12\omega\!\left(
\{T_a-m_a\mathbf1,T_b-m_b\mathbf1\}
\right).
$$

Then

$$
\boxed{
c_R
=\kappa^{ab}m_am_b
+\kappa^{ab}\Sigma_{ab}.
}
$$

Because \(\kappa\) is positive definite and \(\Sigma\) is positive semidefinite as a real covariance form,

$$
0\leq \kappa^{ab}m_am_b\leq c_R,
\qquad
0\leq \kappa^{ab}\Sigma_{ab}\leq c_R.
$$

## Proof

Expanding the centered anticommutator gives

$$
\Sigma_{ab}
=\frac12\omega(\{T_a,T_b\})-m_am_b.
$$

Contracting with \(\kappa^{ab}\) yields

$$
\kappa^{ab}\Sigma_{ab}
=\omega(C_2)-\kappa^{ab}m_am_b
=c_R-\kappa^{ab}m_am_b,
$$

which is the claimed identity.

## Binary specialization

For a single self-adjoint involution \(Q\), take

$$
T_1=Q,
\qquad
\kappa^{11}=1,
\qquad
c_R=1.
$$

Then

$$
m_1=\omega(Q)=m,
\qquad
\Sigma_{11}=\operatorname{Var}_\omega(Q),
$$

and the proposition reduces to [[binary-information-geometry/involutive-casimir|the involutive Casimir identity]]

$$
1=m^2+\operatorname{Var}_\omega(Q).
$$

[[binary-casimir-balance]] supplies the conservation-specific reading: an apparently symmetry-broken state can retain an invariant whole because the order parameter changes while the representation norm continues to be divided between the mean and susceptibility sectors.

## BKM qualification

For a commuting exponential family whose tangent score is a generator, the BKM metric equals the corresponding variance. For a general noncommutative family, the BKM form is an integral or operator-mean covariance and need not equal the symmetrized covariance used above. A physical generalization must therefore either

- prove that the selected orbit and state family make the two forms coincide;
- formulate the Casimir decomposition directly in the relevant BKM geometry; or
- explain why a different monotone metric is physically selected.

Likewise, noncompact groups may have indefinite invariant forms, and infinite-dimensional representations introduce domain and renormalization questions. The positivity statement above should not be exported beyond its hypotheses.

## Research interpretation

The conjectural generalization is

$$
\text{fixed causal-scale representation norm}
=\text{resolved moment-map norm}
+\text{residual information-geometric susceptibility}.
$$

The further claim that the susceptibility has a local area measure and becomes gravitational response belongs to [[state-geometry-charge-weld]]. The proposition supplies a group-theoretic target; it does not itself identify the physical group, representation, or spacetime carrier.

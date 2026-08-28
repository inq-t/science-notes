# The Majorana Block as a Downstream Common Source

Connes' finite Majorana block supplies a concrete observable common-source calculation. Its positive combination \(R=M_R^*M_R\) changes the Einstein coefficient, cosmological coefficient, and Higgs mass parameter, while the full block \(M_R\), including its orientation relative to \(M_\nu\), controls the seesaw spectrum. This is stronger than analogy because the bosonic response Jacobian is explicit, but it remains downstream of the wall and its spectral-action Hessian is not the BKM common response.

## Shared spectral invariants

In [[library/ncg-standard-model-neutrino-mixing/inq|the local Standard Model spectral geometry]], define

$$
R:=M_R^*M_R,
\qquad
K:=M_\nu^*M_\nu,
$$

and

$$
c:=\operatorname{Tr}R,
\qquad
d:=\operatorname{Tr}R^2,
\qquad
e:=\operatorname{Tr}(RK).
$$

The displayed observable coefficients are

$$
\kappa_0^{-2}
=\frac{96f_2\Lambda^2-f_0c}{12\pi^2},
$$

$$
\gamma_0
=\frac{48f_4\Lambda^4-f_2\Lambda^2c+\frac14f_0d}{\pi^2},
$$

and

$$
\mu_0^2
=2\frac{f_2\Lambda^2}{f_0}-\frac ea,
$$

where \(a\) is the declared Yukawa trace invariant.

Holding \(a\), \(f_k\), \(\Lambda\), and \(K\) fixed, formal differentiation in the ambient invariant coordinates gives the **[EXACT AMBIENT RESPONSE JACOBIAN]**

$$
\boxed{
\frac{\partial(\kappa_0^{-2},\gamma_0,\mu_0^2)}
{\partial(c,d,e)}
=
\begin{pmatrix}
-\dfrac{f_0}{12\pi^2}&0&0\\[6pt]
-\dfrac{f_2\Lambda^2}{\pi^2}&
\dfrac{f_0}{4\pi^2}&0\\[6pt]
0&0&-\dfrac1a
\end{pmatrix}.}
$$

The coordinates \(c,d,e\) are not independent on the physical locus \(R=M_R^*M_R\). The coordinate Jacobian is therefore an invariant-coordinate calculus, not a free physical variation. For an actual ambient Hermitian variation \(X=\delta R\),

$$
\delta\kappa_0^{-2}
=-\frac{f_0}{12\pi^2}\operatorname{Tr}X,
$$

$$
\delta\gamma_0
=\frac1{\pi^2}
\operatorname{Tr}
\left[
\left(-f_2\Lambda^2\mathbf1+\frac{f_0}{2}R\right)X
\right],
$$

and

$$
\delta\mu_0^2
=-\frac1a\operatorname{Tr}(KX).
$$

The cosmological coefficient has the positive Hessian

$$
\boxed{
\operatorname{Hess}_R\gamma_0(X,Y)
=\frac{f_0}{2\pi^2}\operatorname{Tr}(XY)}
$$

when \(f_0>0\). This is a Hilbert--Schmidt form in \(R\)-coordinates. Its pullback through \(M_R\mapsto M_R^*M_R\) is not the same Hessian in \(M_R\)-coordinates, and neither is the BKM metric unless an additional state-dependent identification is proved.

## Neutrino seesaw from the same block

For one simplified Dirac mass \(m\) and Majorana scale \(M\), the ordinary symmetric \(2\times2\) neutrino mass block has eigenvalues

$$
\lambda_\pm
=\frac12
\left(M\pm\sqrt{M^2+4m^2}\right).
$$

A doubled spectral Dirac representation may carry the associated opposite-sign partners; those are not four independent sign choices in the \(2\times2\) mass block.

For \(M\gg m\),

$$
m_{\mathrm{light}}
\sim\frac{m^2}{M},
\qquad
m_{\mathrm{heavy}}
\sim M.
$$

Thus one finite Dirac datum participates simultaneously in

- the effective Newton coefficient through \(c\);
- the cosmological coefficient through \(c\) and \(d\);
- the Higgs mass parameter through \(e\); and
- the light neutrino scale through the seesaw.

This is the strongest calculated opening for a common hidden algebraic source among the three phenomena. It does not show that dark energy is a Majorana condensate or that Newton's constant is numerically derived from neutrino mass.

## Relation to the wall programme

The response belongs to the observable spectral action. The source itself discusses fixing the scale of \(M_R\) by minimizing the observable cosmological term. Under the present register order, that minimization cannot be used as a pre-observable necessity.

[[spectral-wall-descent/majorana-square-and-cosmic-pulse|The Majorana square and cosmic pulse]] completes \(\gamma_0(R)\) into a positive square about \(r\mathbf1\) plus an \(R\)-independent residual. It distinguishes the source's fixed-ray minimization from a project-chosen traceless hyperbolic orbit that leaves \(\kappa_0^{-2}\) fixed while producing an exact \(\operatorname{sech}^2\) spectral deficit. Those are downstream spectral-action identities, not yet the horizontal wall state.

The desired upstream extension would construct a state family \(\rho_R\), calculate its BKM response

$$
G^{\mathrm{BKM}}_R(X,Y),
$$

pass it through the noninvertible wall, and then prove that the observable Jacobian above is the consumer map of the retained and geometric response blocks. Until that is done, the Majorana calculation is a downstream common-source theorem rather than the common response form itself.

## Failure conditions

- Varying \(R=M_R^*M_R\) does not specify a variation of \(M_R\) uniquely.
- Holding \(a\) fixed is part of the displayed Jacobian; a joint Yukawa variation adds terms.
- The Hilbert--Schmidt Hessian is not automatically BKM or canonical gravitational energy.
- Spectral-action coefficients are defined at the cutoff or unification scale and require renormalization-group transport before comparison with low-energy observations.
- The seesaw approximation requires \(M\gg m\).
- Shared dependence is not a causal explanation until \(R\) is independently selected and the wall/state map is constructed.

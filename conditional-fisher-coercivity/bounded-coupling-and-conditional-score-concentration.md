# Vanishing Coupling Can Hide Unbounded Conditional Response

Even a smooth interaction tending to zero can produce an exact correlated ground state whose integrated relative Fisher cost vanishes while its conditional score covariance diverges. The carrier, positive bare Ricci curvature and kinetic coefficient stay fixed; the regional reference develops an explicit soft mode. Thus no uniform estimate from upper bounds on the boundary interaction and its first two derivatives can replace control of the whole reference state. This is an inverse-designed counterexample, not a Wilson-family obstruction or a proposed physical selecting law.

## A smooth reference with an explicit soft mode

Use \(SU(2)\times SU(2)\) with normalized Haar, metric
\(Q=-2\operatorname{Tr}\), fixed \(\kappa>0\), and
\(a=\tfrac12\operatorname{Tr}x,\ b=\tfrac12\operatorname{Tr}y\).
For class functions,
\[
\Delta_QF(a)=\tfrac14[(1-a^2)F''-3aF'],\qquad
|\nabla a|^2=(1-a^2)/4,\qquad
\operatorname{Hess}a=-aQ/4.
\tag{SC1}
\]
Both bare Ricci tensors are \(Q/2\). For \(\eta>0\), put
\[
\begin{aligned}
d&=a^2+\eta^2,& h_\eta(a)&=a/\sqrt d,\\
v_\eta(a)&=\tfrac34\log d+\frac{3a^2}{4(1+\eta^2)},&
\phi_\eta(a)&=Z_\eta^{-1/2}e^{v_\eta(a)},\\
\omega_\eta&=\frac{3\eta^2}{4(1+\eta^2)},&
m_\eta&=\int h_\eta^2\phi_\eta^2dx .
\end{aligned}
\tag{SC2}
\]
Here \(Z_\eta\) normalizes \(\phi_\eta\). It is smooth, positive
and even; \(h_\eta\) is smooth, bounded and odd. Define
\[
H_{A,\eta}=-\kappa\Delta_x+
             \kappa\frac{\Delta_x\phi_\eta}{\phi_\eta},
\qquad H_{B,\eta}\text{ identically on }y,\qquad
H_{0,\eta}=H_{A,\eta}+H_{B,\eta}.
\tag{SC3}
\]
For each \(\eta>0\), the ground-state transform proves
\(H_{0,\eta}\ge0\), with unique normalized product ground vector
\(\phi_\eta(a)\phi_\eta(b)\), energy zero and inherited compact
\(H^2\) domain. This operator is defined from the chosen vector;
its state has not been derived from independent primitives.

Let
\(\mathscr D_\phi=\Delta_x+2\nabla v_\eta\cdot\nabla_x\),
without a factor of \(\kappa\). Direct differentiation gives
\[
\begin{aligned}
h_\eta'&=\eta^2d^{-3/2},&
h_\eta''&=-3a\eta^2d^{-5/2},\\
v_\eta'&=\frac{3a}{2d}+\frac{3a}{2(1+\eta^2)},&
\boxed{\mathscr D_\phi h_\eta=-\omega_\eta h_\eta.}
\end{aligned}
\tag{SC4}
\]
To check the last identity, the first drift term cancels
\(h_\eta''\). The remaining terms combine as
\[
-\frac{3\eta^2h_\eta}{4d}
+\frac{3\eta^2h_\eta(1-a^2)}{4d(1+\eta^2)}
=-\omega_\eta h_\eta.
\]
Thus \(\kappa\omega_\eta\to0\) is an **actual centered
eigenvalue** of the reference transformed generator. Its gap
is at most this value; no claim that it is the lowest positive
eigenvalue is needed.

## A vanishing interaction and an exact correlated vacuum

Fix \(0<\epsilon<1\), write \(s=h_\eta(a)h_\eta(b)\), and set
\[
u_\eta=1+\epsilon s,\qquad
\boxed{W_\eta=-2\kappa\omega_\eta
                  \frac{\epsilon s}{1+\epsilon s}.}
\tag{SC5}
\]
The sum of the two reference diffusions sends
\(u_\eta\) to \(-2\omega_\eta\epsilon s\). Consequently
\[
\psi_\eta=
\frac{\phi_\eta(a)\phi_\eta(b)(1+\epsilon s)}
     {\sqrt{1+\epsilon^2m_\eta^2}}
\tag{SC6}
\]
is a normalized, smooth, positive **exact** zero-energy ground
vector of \(H_{0,\eta}+W_\eta\).
The denominator follows from oddness:
\(\mathbb E_{\phi^2}s=0\), \(\mathbb E_{\phi^2}s^2=m_\eta^2\).
The eigen-equation follows by substitution through the
ground-state transform, not by a variational approximation.

The coupling and force obey
\[
\begin{aligned}
\|W_\eta\|_\infty
&\le\frac{2\kappa\omega_\eta\epsilon}{1-\epsilon}
       =O(\eta^2),\\
\|\nabla_xW_\eta\|_\infty,\ \|\nabla_yW_\eta\|_\infty
&\le\frac{\kappa\omega_\eta\epsilon}
          {\eta(1-\epsilon)^2}=O(\eta).
\end{aligned}
\tag{SC7}
\]
These use \(|h_\eta|\le1\) and \(|\nabla h_\eta|\le1/(2\eta)\).
Even the full product Hessian is uniformly bounded:
\[
\|\operatorname{Hess}W_\eta\|_\infty
\le\frac{3\kappa\epsilon}{2(1-\epsilon)^3}.
\tag{SC8}
\]
Hessian norms here are operator norms in the product metric.
For a direct bound, (SC1) gives
\(\|\operatorname{Hess}h_\eta\|\le3/(4\eta^2)+1/4\).
Hence
\(\|\operatorname{Hess}s\|\le1/\eta^2+1/4\) and
\(|\nabla s|^2\le1/(2\eta^2)\).
Differentiate (SC5) twice and use the exact \(\omega_\eta\).

## Vanishing average cost and diverging optimal form constant

The [[coarse-response-memory/boundary-interaction-and-conditional-score-budget|relative ground-state identity]]
gives an exact cost, since both ground energies are zero:
\[
\boxed{
R_\eta:=
\kappa\int\left|\nabla\log
 \frac{\psi_\eta}{\phi_\eta(a)\phi_\eta(b)}\right|^2\psi_\eta^2
=-\langle W_\eta\rangle_{\psi_\eta^2}
=\frac{2\kappa\omega_\eta\epsilon^2m_\eta^2}
       {1+\epsilon^2m_\eta^2}\longrightarrow0.}
\tag{SC9}
\]
This uses the generic interaction identity, not the special
zero-reference-mean Wilson sharpening.

Retain the full \(x\) coordinate. Its conditional law is
\[
q_x(y)=
\frac{\phi_\eta(b)^2(1+\epsilon h_\eta(a)h_\eta(b))^2}
     {1+\epsilon^2h_\eta(a)^2m_\eta}.
\]
Taking the variance of the half-density score gives the
rank-one covariance tensor
\[
\boxed{
M_x=
\frac{\epsilon^2m_\eta}
 {(1+\epsilon^2m_\eta h_\eta(a)^2)^2}
 \nabla h_\eta(a)\otimes\nabla h_\eta(a).}
\tag{SC10}
\]
Indeed its uncentered second moment is
\(\epsilon^2m_\eta|\nabla h_\eta|^2/
 (1+\epsilon^2m_\eta h_\eta^2)\), and subtracting the squared
conditional mean gives (SC10).

Its largest eigenvalue is attained at \(a=0\):
\[
\boxed{\operatorname*{ess\,sup}_x\|M_x\|
=\frac{\epsilon^2m_\eta}{4\eta^2},\qquad
\beta_{\rm best}^2=
4\kappa\operatorname*{ess\,sup}\|M_x\|
=\frac{\kappa\epsilon^2m_\eta}{\eta^2}.}
\tag{SC11}
\]
To see the maximum, use
\(|\nabla h_\eta|^2=
\eta^4(1-a^2)/(4d^3)\) in (SC10); the expression decreases
with \(a^2\). Smoothness makes this an essential-supremum
statement, not a value limited to one null fiber.
The optimal first-energy constant is the localized-oscillation
identity (BC18), not an estimate inferred from a finite test set.

Dominated convergence in the explicitly normalized
\(\phi_\eta^2\) law gives \(m_\eta\to1\). Therefore the
first-energy constant diverges while (SC9) vanishes.
More strongly, choose \(\epsilon=\sqrt\eta\) and
\(0<\eta\le1/4\). Then (SC7)--(SC8) show
\(\|W_\eta\|_{C^2}\to0\), while
\(\operatorname*{ess\,sup}\|M_x\|\sim1/(4\eta)\to\infty\).
The same formulas establish this refinement; it is not a
different background construction.

## The missing control lies in the reference

The regional potential is not uniformly bounded:
\[
\left.\kappa\frac{\Delta\phi_\eta}{\phi_\eta}\right|_{a=0}
=\frac{3\kappa}{8\eta^2}+\frac{3\kappa}{8(1+\eta^2)},
\qquad
\left.\kappa\frac{\Delta\phi_\eta}{\phi_\eta}\right|_{a=1}
=-\frac{9\kappa}{4(1+\eta^2)}.
\tag{SC12}
\]
Its oscillation, and hence some regional force on this fixed
compact metric space, diverges. The reference weighted curvature
at \(a=0\) in a unit latitude direction is
\(1/2-3/(4\eta^2)-3/[4(1+\eta^2)]\).
Its exact soft eigenmode was already exposed in (SC4).

Thus a bound allowed to use full regional force, curvature or
independently proved coercivity data has not been contradicted.
The interaction is not a Wilson plaquette sum and need not
have zero partial Haar means. The
[[algebra/partial-bochner-and-ground-state-score#A product reference turns the force into a boundary force|weighted-reference sufficient estimate]]
fails its reference hypothesis, not its proof.

The implication is stronger than “an average does not bound
a maximum”: very small, smoothly controlled boundary coupling
can act on an increasingly soft reference to produce arbitrarily
large conditional response. A whole-to-local law must constrain
that susceptibility as well as the crossing cost.
[[transport-cost-and-uniform-distortion|The transport-distortion control]]
makes a related distinction for connections, but does not
construct this exact coupled Schrödinger vacuum.
No physical scale or Yang--Mills gap is inferred.

# Measured Operations and GNS Defects

A normal state-preserving UCP operation acts on observables and contracts the corresponding GNS vectors. A GNS-symmetric operation gives a positive dimensionless defect; a family detects precisely the complement of its joint fixed space. Vacuum ergodicity removes fixed nonvacuum directions but does not by itself give a uniform edge or identify that edge with physical energy.

## The measured operation

Let \(\mathcal A\) be a von Neumann algebra, let \(\omega\) be a faithful
normal state, and let

\[
(\pi_\omega,\mathcal H_\omega,\Omega_\omega)
\]

be its GNS representation. Suppose

\[
\Phi:\mathcal A\longrightarrow\mathcal A
\]

is normal, unital, completely positive, and state preserving:

\[
\omega\circ\Phi=\omega.
\tag{MC1}
\]

Assume also that \(\Phi\) has a normal unital completely positive
\(\omega\)-adjoint \(\Phi^\sharp\), meaning

\[
\omega\!\left(a^*\Phi(b)\right)
=
\omega\!\left(\Phi^\sharp(a)^*b\right)
\qquad
(a,b\in\mathcal A).
\tag{MC2}
\]

Existence of this adjoint is a genuine hypothesis outside the tracial case.
The operation is **GNS symmetric** when
\(\Phi^\sharp=\Phi\).

## First carrier: the observable algebra

On \(\mathcal A\), the map says how one declared readout, coarse graining,
defect, or correspondence transforms observables. Its fixed algebra is

\[
\mathcal A^\Phi
:=
\{a\in\mathcal A:\Phi(a)=a\}.
\tag{MC3}
\]

This is the correct carrier for multiplicative structure, complete
positivity, bimodularity, locality or regional naturality, and fusion laws.
It is not itself a Hilbert space, and the phrase “spectral gap of \(\Phi\)”
is incomplete until a normed representation has been selected.

The fixed space is an algebra under the declared faithfulness and state-preservation hypotheses. If \(\Phi(a)=a\), Kadison--Schwarz gives \(\Phi(a^*a)\ge a^*a\); the positive difference has zero \(\omega\)-value and therefore vanishes. Applying the same argument to \(aa^*\) puts \(a\) in the multiplicative domain. Products of fixed elements are consequently fixed, and normality makes the fixed algebra ultraweakly closed.

## Second carrier: GNS state vectors

Define initially on the dense subspace
\(\pi_\omega(\mathcal A)\Omega_\omega\)

\[
V_\Phi\pi_\omega(a)\Omega_\omega
:=
\pi_\omega(\Phi(a))\Omega_\omega.
\tag{MC4}
\]

Kadison--Schwarz and (MC1) give

\[
\begin{aligned}
\|V_\Phi\pi_\omega(a)\Omega_\omega\|^2
&=
\omega\!\left(\Phi(a)^*\Phi(a)\right)\\
&\leq
\omega\!\left(\Phi(a^*a)\right)
=
\omega(a^*a),
\end{aligned}
\]

so \(V_\Phi\) extends uniquely to a contraction on
\(\mathcal H_\omega\). Equation (MC2) gives

\[
V_\Phi^*=V_{\Phi^\sharp},
\qquad
V_\Phi\Omega_\omega=\Omega_\omega.
\tag{MC5}
\]

These are **[EXACT]** consequences of the measured-operation hypotheses.

If \(\Phi\) is GNS symmetric, then \(V_\Phi\) is a self-adjoint contraction
and

\[
D_\Phi:=I-V_\Phi\geq0.
\tag{MC6}
\]

Its closed bounded form is

\[
\mathcal E_\Phi[\xi]
:=
\langle\xi,D_\Phi\xi\rangle,
\qquad
\ker D_\Phi=\operatorname{Fix}(V_\Phi).
\tag{MC7}
\]

This is a dimensionless distinction defect on the chosen GNS carrier. Its
vacuum-reduced edge is

\[
\kappa_\Phi
:=
\inf_{\substack{\xi\perp\Omega_\omega\\\|\xi\|=1}}
\langle\xi,D_\Phi\xi\rangle.
\tag{MC8}
\]

A positive \(\kappa_\Phi\) requires the fixed
space to be exactly \(\mathbb C\Omega_\omega\). If a nonvacuum subspace is fixed,
the form assigns those distinctions zero cost.

## Families and vacuum ergodicity

Let \(\{\Phi_i\}_{i\in I}\) be a finite or countable family of
GNS-symmetric measured operations and let \(\nu_i>0\),
\(\sum_i\nu_i=1\). The countable sums below converge in operator norm. Put

\[
V_\nu:=\sum_i\nu_iV_{\Phi_i},
\qquad
D_\nu:=I-V_\nu
=
\sum_i\nu_i(I-V_{\Phi_i}).
\tag{MC9}
\]

Because every summand is positive,

\[
\boxed{
\ker D_\nu
=
\bigcap_i\operatorname{Fix}(V_{\Phi_i}).}
\tag{MC10}
\]

Thus the exact fixed-space condition needed by a vacuum-centered theory is

\[
\bigcap_i\operatorname{Fix}(V_{\Phi_i})
=
\mathbb C\Omega_\omega.
\tag{MC11}
\]

This is **vacuum ergodicity**. It removes zero-cost nonvacuum directions; it
does not by itself prove a positive lower edge, select the family, or make
the form dynamical.

Indeed, a vacuum-only fixed space and an order-one edge can be cheap. For a
product state on
\(\mathcal A_1\bar\otimes\mathcal A_2\), the preserving expectations onto
the two tensor factors have GNS projections

\[
e_1=I\otimes P_{\Omega_2},
\qquad
e_2=P_{\Omega_1}\otimes I,
\qquad
e_1e_2=P_{\Omega_\omega}.
\]

Consequently

\[
(I-e_1)+(I-e_2)
\geq
I-P_{\Omega_\omega}.
\tag{MC12}
\]

This floor exists independently of any Hamiltonian or categorical
rigidity. It proves that fixed-space engineering plus a numerical edge is
not yet evidence of mass.

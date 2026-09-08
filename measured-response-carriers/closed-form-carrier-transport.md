# Closed-Form Carrier Transport

A bounded Hilbert-space isomorphism transports a closed nonnegative form by congruence, preserving its kernel and carrying a coercivity bound with explicit norm distortion. Unitary transport also preserves the numerical spectrum; a general congruence need not, and neither operation changes the response into a different physical quantity.

## Closed-form transport across carriers

Let \(q\) be a densely defined closed nonnegative Hermitian form on a Hilbert
space \(\mathcal K\), with associated positive self-adjoint operator \(L\).
If

\[
R:\mathcal K\longrightarrow\mathcal K'
\]

is a bounded Hilbert-space isomorphism with bounded inverse, define

\[
\operatorname{Dom}(q_R):=R\,\operatorname{Dom}(q),
\qquad
q_R[R\xi,R\eta]:=q[\xi,\eta].
\tag{MC21d}
\]

Then \(q_R\) is densely defined, closed, and nonnegative. With
\(R^{-*}:=(R^{-1})^*\), its associated operator is the congruence

\[
\boxed{
L_R=R^{-*}LR^{-1},
\qquad
\operatorname{Dom}(L_R)=R\,\operatorname{Dom}(L).}
\tag{MC21e}
\]

In particular,

\[
\ker L_R=R\ker L.
\tag{MC21e'}
\]

## Coercivity modulo the kernel

If \(N=\ker L\) and the original form obeys

\[
q[\xi]\geq\kappa\,\operatorname{dist}_{\mathcal K}(\xi,N)^2,
\]

then the transported form obeys the norm-distorted bound

\[
q_R[u]
\geq
\frac{\kappa}{\|R\|^2}
\operatorname{dist}_{\mathcal K'}(u,RN)^2.
\tag{MC21e''}
\]

Thus positivity, closedness, the kernel, and coercivity modulo the kernel
transport exactly in the stated senses. A unitary \(R\) preserves the
numerical spectrum; a general bounded congruence is not a similarity and
need not do so.

## When inverse transport is unavailable

This theorem licenses an inverse-conjugation formula only after both Hilbert
carriers, form domains, and the bounded inverse have been constructed. If
\(R\) has a kernel, nonclosed range, or changes a configuration carrier into
a phase space without a chosen polarization and state norm, (MC21e) is not
defined. One must instead quotient, pull back, short a form, or construct a
different comparison. [[measured-response-carriers/response-pullbacks-and-radicals|Response
pullbacks]] retain the analysis-map kernel explicitly;
[[trace-dirichlet-descent/standard-form-pullback-and-reducing-wall|standard-form
pullback]] and [[trace-dirichlet-descent/inq|least-cost trace descent]] supply
separate constructions under their own hypotheses. They are not inverse
congruences through a noninvertible map.

Form congruence transports a response; it does not change its native
register. A spatial probability precision transported by \(R\) remains a
spatial probability precision. It does not become a Hamiltonian, transfer
generator, or Poincare Casimir.

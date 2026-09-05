# Signed Curvature Must Be Tested on Its Compatible Image

A negative coefficient in an ambient curvature form need not give an unstable variation of the underlying object: admissible curvatures occupy the image of a derivative map. Conversely, positive response along every coordinate separately need not exclude a collective unstable direction. A finite-dimensional compression theorem makes the missing relation exact.

**Status: [EXACT FINITE-DIMENSIONAL RELATIVE-SPECTRUM THEOREM]; not a Hamiltonian gap or a classification of physical null directions.**

## The operator acts on compatible variations

Let \(D:V\to W\) be a nonzero linear map of finite-dimensional real or complex Hilbert spaces. Let \(B\) be an orthogonal projection on \(W\), and let \(\alpha>0\). Compare the forms
\[
q_0(v)=\|Dv\|^2,\qquad
q(v)=\|Dv\|^2-\alpha\|BDv\|^2.
\tag{CI1}
\]
The reference form vanishes on \(\ker D\). For this relative stability question, work on \(V/\ker D\), equivalently \((\ker D)^\perp\). This is a declared mathematical quotient, not proof that every removed direction is physically redundant.

Put \(Q_0=D^*D\), let \(Q_0^\dagger\) denote its Moore--Penrose inverse, and define
\[
P=DQ_0^\dagger D^*.
\tag{CI2}
\]
Singular-value decomposition shows that \(P\) is the orthogonal projection onto \(\operatorname{ran}D\). Then
\[
\boxed{
\inf_{Dv\ne0}\frac{q(v)}{q_0(v)}
=1-\alpha\|BPB\|.}
\tag{CI3}
\]
Indeed the supremum of \(\|By\|^2/\|y\|^2\) over nonzero \(y\in\operatorname{ran}D\) is \(\|BP\|^2=\|BPB\|\). Substitution into (CI1) proves (CI3).

Consequently \(q\) has a negative direction exactly when \(\alpha\|BPB\|>1\), and is nonnegative exactly when that quantity is at most one. Equality can leave extra null directions; the theorem says nothing about higher-order stability at such points. With an independently chosen domain metric, even a positive relative edge also needs a lower bound on \(Q_0\) to yield an ordinary positive edge.

The projection \(B\) describes where negative response is assigned. The projection \(P\) describes which response patterns are actually possible. Their overlap, not either projection alone, decides the sign. This sharpens [[relative-response-spectrum|the requirement to specify both response and reference metric]].

## Two minimal distinctions

Take \(D:\mathbb R\to\mathbb R^2\), \(Dx=(x,x)\), \(B=\operatorname{diag}(0,1)\) and \(\alpha=3/2\). The ambient weights are \(1,-1/2\), but
\[
q(x)=\tfrac12x^2>0,\qquad \|BPB\|=1/2.
\tag{CI4}
\]
A negative ambient weight was insufficient because its coordinate could not vary independently.

In the opposite direction, the form with matrix
\[
\begin{pmatrix}1&2\\2&1\end{pmatrix}
\tag{CI5}
\]
is positive on either coordinate axis and negative on \((1,-1)\). Independent-coordinate stability does not imply joint stability. Neither example selects a physical field or a rate.

## Central Wilson curvature is a signed compatible image

At a central \(SU(3)\) link configuration, let \(d\) be the real link-to-plaquette cochain differential and let \(B\) select nontrivial central plaquettes. Their real weights are \(-1/2\), while trivial plaquettes have weight one. In each orthonormal Lie-algebra direction,
\[
\operatorname{Hess}S[X,X]
=\beta\left(\|dX\|^2-\tfrac32\|BdX\|^2\right).
\tag{CI6}
\]
Thus the exact instability threshold is
\[
\boxed{\|B\,d(d^*d)^\dagger d^*B\|>2/3.}
\tag{CI7}
\]
Restricting to a selected set of links means replacing \(d\) by its restriction to variations supported there. It does not mean dropping the surrounding plaquettes from its output.

Compatibility has two layers. The central background must itself come from admissible link data. Its infinitesimal curvature must then lie in \(\operatorname{ran}d\), satisfying the linear cochain identities and any global period constraints. Treating plaquettes as independent would omit the latter condition.

[[rg-covariance-residue/critical-context-and-collective-escape|The critical Wilson example]] supplies compatible background links and a finite supported collective direction. It also converts that direction into an actual-law localization estimate. Neither the pointwise Hessian nor the compression criterion alone provides that last step.

[[rg-covariance-residue/receipts/collective_context_escape_receipt.py|The finite receipt]] checks (CI3) on rank-deficient matrix maps and the central Wilson realization. Infinite-dimensional extensions require closed-range and form-domain control; they are not supplied by a finite pseudoinverse.

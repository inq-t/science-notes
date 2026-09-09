# Five-by-Five Resonance and the Source-Selection Test

The exact frequency-sum resonance on the five-by-five planar patch does not produce a resonant interaction in the actual first odd kinetic jet. All five modes in its frequency-two eigenspace satisfy the required cancellation after the sixty raw comb rows are contracted. Some uncombined coefficients are nonzero. The result clears the resonant obstruction at this order and size, but leaves a physical source-selection freedom: a resonant skew generator can preserve both the harmonic operator and vacuum while changing the multiplier product contact.

**Status: exact finite-patch kinetic-jet calculation and complete cubic-resonance check at \(L=5\).** [[comb-face-transport-and-the-first-nonlinear-jet|FJ]] fixes the full edge inventory and based connectors. [[all-group-oriented-kinetic-jet-and-source-lift|AJ]] derives the alternating Lie-bracket contraction without a three-dimensional identity. [[oriented-triad-resonance-and-the-physical-source-block|RT]] owns the general compatibility equation and its neutral physical matrix element. No larger-patch normal form or uniform denominator bound is asserted.

## Keep all sixty edge rows

Use the open \(5\times5\) patch, with its \(36\) vertices, \(60\) edges and full vertex Gauss law. The comb coordinates retain \(25\) based face variables with simultaneous conjugation. On their logarithmic cover write
\[
hZ_{e,T}=\sum_p s_{ep}Q(T,\nabla_p)
+h\sum_{p,q}z_{epq}Q([x_q,T],\nabla_p)+O(h^2).
\tag{RF1}
\]
The row inventory is \(25\) horizontal chords, \(5\) bottom tree edges and \(30\) vertical edges. The following is FJ13 with the finite ranges made explicit:

- A horizontal row \((i,j)\) has \(s_{i,j}=-1\), \(z_{(i,j),(i,j)}=-1/2\); if \(j<5\), also \(s_{i,j+1}=1\), \(z_{(i,j+1),(i,j+1)}=-1/2\).
- A bottom row \(i\) has \(s_{i,1}=1\), \(z_{(i,1),(i,1)}=-1/2\), and \(z_{(a,k),(a,k)}=-1\) for all \(a>i\).
- A vertical row \((c,j)\), \(0\le c\le5\), has on its left face \(s_{c,j}=1\), \(z_{(c,j),(c,j)}=-1/2\) and \(z_{(c,j),(c,k)}=-1\) for \(k<j\), when \(c\ge1\). On its right face it has \(s_{c+1,j}=-1\), \(z_{(c+1,j),(c+1,j)}=-1/2\), and the conjugation tail \(z_{(c+1,k),(c+1,k)}=-1\) for \(k>j\), when \(c<5\).

Unlisted entries vanish. In particular,
\[
s^{\mathsf T}s=A_5=4I-\operatorname{Adj}_{5\times5}.
\tag{RF2}
\]
The prefix terms and conjugation tails in (RF1) are retained even though they do not contribute to (RF2).

## Resolve the whole degenerate eigenspace

The real orthonormal sine modes are
\[
O_{(x,y),(r,s)}=\frac13
\sin\frac{r\pi x}{6}\sin\frac{s\pi y}{6},\qquad
\omega_{rs}^2=4-2\cos\frac{r\pi}{6}-2\cos\frac{s\pi}{6}.
\tag{RF3}
\]
Set \(a=(1,1)\), \(c=(5,5)\), and
\[
\mathcal M=\{(1,5),(2,4),(3,3),(4,2),(5,1)\}.
\]
Then
\[
\omega_a=\sqrt3-1,\qquad
\omega_m=2\quad(m\in\mathcal M),\qquad
\omega_c=\sqrt3+1=\omega_a+\omega_m .
\tag{RF4}
\]

For each row put \(\bar s=O^{\mathsf T}s\), \(\bar z=O^{\mathsf T}zO\). For the ordered triple \((a,m,c)\), the cyclic coefficients of
\[
V_1^{a m c}
=v_aT_G(Y_a,\nabla_m,\nabla_c)
+v_mT_G(\nabla_a,Y_m,\nabla_c)
+v_cT_G(\nabla_a,\nabla_m,Y_c)
\]
are obtained from
\[
v_{\ell;jk}
=2\sum_e\left(\bar s_{ek}\bar z_{ej\ell}
-\bar s_{ej}\bar z_{ek\ell}\right).
\tag{RF5}
\]
The slot orientations agree with RT. Exact contraction gives:

| \(m\) | \(36v_a\) | \(36v_m\) | \(36v_c\) |
| --- | --- | --- | --- |
| \((1,5)\) | \(3-\sqrt3\) | \(5-3\sqrt3\) | \(-5+3\sqrt3\) |
| \((2,4)\) | \(0\) | \(0\) | \(0\) |
| \((3,3)\) | \(0\) | \(0\) | \(0\) |
| \((4,2)\) | \(0\) | \(0\) | \(0\) |
| \((5,1)\) | \(5+3\sqrt3\) | \(-5-3\sqrt3\) | \(-3-\sqrt3\) |

Consequently every channel obeys
\[
\boxed{r_m=(\sqrt3-1)v_a+2v_m-(\sqrt3+1)v_c=0.}
\tag{RF6}
\]
For example, the first numerator multiplied by \(36\) is
\[
(\sqrt3-1)(3-\sqrt3)+2(5-3\sqrt3)
-(\sqrt3+1)(-5+3\sqrt3)=0.
\]
The last row cancels in the same field. Thus \(\sum_{m\in\mathcal M}r_m^2=0\), independently of the orthonormal basis chosen inside the degenerate frequency-two space.

The two nonzero rows show why neither a frequency equality nor an individual raw coefficient decides the question. RT8–9 identify the actual resonant ladder coefficient as \(-r_m/(4\sqrt{\omega_a\omega_m\omega_c})\), and its normalized neutral physical matrix element as that coefficient times \(\sqrt{2\mathfrak F_Q/\dim\mathfrak g}\). Both vanish here.

## The finite frequency check is exhaustive

All squared frequencies lie in \(\mathbb Q(\sqrt3)\). They are
\[
\lambda_{rs}=4-u_r-u_s,\qquad
(u_1,\ldots,u_5)=(\sqrt3,1,0,-1,-\sqrt3).
\]
For positive \(\lambda,\mu,\nu\), the identity
\(\sqrt\nu=\sqrt\lambda+\sqrt\mu\) is equivalent to
\[
d=\nu-\lambda-\mu>0,\qquad d^2=4\lambda\mu .
\tag{RF7}
\]
Checking these two exact conditions on all thirteen squared-frequency classes, allowing repeated classes, gives only
\[
(\lambda,\mu,\nu)=(4-2\sqrt3,\ 4,\ 4+2\sqrt3),
\]
up to exchange of the first two entries.

The executable proof receipt [five_by_five_odd_resonance_receipt.py](receipts/five_by_five_odd_resonance_receipt.py) uses rational arithmetic in \(\mathbb Q(\sqrt3)\). It checks the full \(25\times25\) identity (RF2), the selected modes' normalization and kinetic eigenvalues, every entry of the table, every cancellation (RF6), and the exhaustive test (RF7). The sign test compares rational squares; it uses no floating-point frequency tolerance.

A cubic ladder monomial can have zero frequency difference only through such a positive-frequency triangle; terms with a single net quantum cannot do so. The repeated-mode angular terms also cause no untested resonance. Thus the actual first odd jet has zero projection onto every resonant cubic ladder channel at this fixed size. The off-resonant terms admit a finite polynomial normal form by division by their nonzero frequency differences.

## Cancellation leaves a source-selection question

The normal form is nevertheless not unique. For each triple in (RF4), RT constructs a nonzero odd skew polynomial generator \(N\) satisfying
\[
[K_0,N]=0,\qquad N\Omega=0.
\tag{RF8}
\]
Adding \(\theta N\) to a solution preserves its first kinetic equation and its vacuum correction. It can still change the lifted neutral sources and their product contact. RT gives an explicit radius-pair contact for this freedom; the equal-energy states involved survive simultaneous Gauss reduction.

With consistent differential operator lifts, RT also proves that every finite chronological vacuum word is unchanged through first order: its variation is the vacuum expectation of a commutator with \(N\). Contact nonuniqueness therefore does not by itself establish an observable physical ambiguity. The distinction enters when scalar multiplier returns or a specified source-access algebra must be retained.

[[regional-conditional-projection-and-the-vacuum-score|The actual conditional tangent]] now permits that source-selection test. [[two-face-source-access-and-the-normal-form-obstruction|The complete pair-access obstruction]] proves that no invariant odd normal form matches every fixed prepared one- and two-face projection through first order. A rigid lowest-mode radius component supplies the witness, independently of the compatible resonant freedom. Setting a resonant component to zero therefore cannot remove the required embedding response. This calculation still supplies no spatially uniform inverse bound, actual all-orders transport, or continuum mass-gap conclusion.

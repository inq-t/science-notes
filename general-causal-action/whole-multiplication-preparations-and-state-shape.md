# Whole Multiplication Preparations and State Shape

One Gaussian preparation can support both parenthesizations of a three-input multiplication and both unit insertions, with all sources and normalization transported together. For \(\mathbb C\oplus\mathbb C\), this construction is completely explicit. It also admits a dimensionless state-shape parameter that changes the output response while preserving the multiplication, pairing, algebra symmetry and unmarked determinant. Whole-diagram coherence therefore leaves a substantive preparation choice.

## One algebra and one marked carrier

Let \(V=\mathbb C e_0\oplus\mathbb C e_1\), with
\[
\mu(e_i\otimes e_j)=\delta_{ij}e_i,\qquad
1=e_0+e_1,\qquad h(e_i,e_j)=\delta_{ij}.
\tag{WM1}
\]
Use the tensor pairings, \(X=V^{\otimes3}\), \(Y=V^{\otimes2}\), and
\[
A_L=\mu\otimes I,\quad A_R=I\otimes\mu,\quad
F=\mu A_L=\mu A_R,\qquad
Lv=1\otimes v,\quad Rv=v\otimes1.
\tag{WM2}
\]
Thus \(\mu L=\mu R=I\). As in [[multiplication-reassociation-and-the-process-metric|the reassociation construction]], \(x\in X\) is one arbitrary tensor, not three independent \(V\)-valued configurations.

Take the marked ambient preparation carrier
\[
\mathcal E=X\oplus Y_{y_L}\oplus Y_{y_R}\oplus V_v
\oplus Y_{u_L}\oplus Y_{u_R},
\qquad \dim_{\mathbb C}\mathcal E=26,
\]
\[
Bx=(x,A_Lx,A_Rx,Fx,LFx,RFx)
=\begin{bmatrix}I\\M\end{bmatrix}x,\qquad
\mathscr R=[-M,I].
\tag{WM3}
\]
The row map \(\mathscr R\) has rank eighteen and \(\ker\mathscr R=\operatorname{ran}B\). Conditioning once on these independent graph relations enforces
\[
\mu y_L=\mu y_R=v,\qquad
\mu u_L=\mu u_R=v.
\tag{WM4}
\]
These consequences are not appended as redundant delta constraints. The two intermediate tensor carriers and the two unit carriers remain distinct marked copies.

## The complete sourced amplitude

Fix a positive background covariance \(G\) on \(\mathcal E\). Use the declared product measure \(d_{\mathcal E}\xi=d^{52}\xi/\pi^{26}\), and the constraint delta normalized against \(d^{36}r/\pi^{18}\). For a Hermitian quadratic mark \(\mathsf T\), assume \(Q=G^{-1}+\mathsf T>0\). Define
\[
\mathcal Z_G(J,\mathsf T)
=\int_{\mathcal E}
e^{-\xi^\dagger Q\xi+2\operatorname{Re}(J^\dagger\xi)}
\delta_{\mathbb C}^{18}(\mathscr R\xi)\,d_{\mathcal E}\xi.
\tag{WM5}
\]
This is an unnormalized amplitude: no division by a partition factor is implicit.

The change \((x,\mathrm{rest})\mapsto(x,\mathrm{rest}-Mx)\) has determinant one. Direct integration of the constrained coordinates therefore gives
\[
\boxed{
\mathcal Z_G(J,\mathsf T)
=\frac{\exp(q^\dagger K_{G,\mathsf T}^{-1}q)}
{\det K_{G,\mathsf T}},
\qquad
q=B^\dagger J,\quad
K_{G,\mathsf T}=B^\dagger(G^{-1}+\mathsf T)B.}
\tag{WM6}
\]
[[marked-gaussian-constraints-and-sewing-measures|Marked Gaussian constraints]] owns the general formula and its density conventions. Here the graph coordinates make its normalization cancellation explicit. A spectral mark \(z\Gamma\) can be included in \(\mathsf T\) after \(\Gamma\) is declared; this does not select that coefficient or a physical clock.

For \(J=(j_x,j_{y_L},j_{y_R},j_v,j_{u_L},j_{u_R})\), the source transport is
\[
q=j_x+A_L^\dagger j_{y_L}+A_R^\dagger j_{y_R}
+F^\dagger(j_v+L^\dagger j_{u_L}+R^\dagger j_{u_R}).
\tag{WM7}
\]
Removing a unit carrier transports its source into the \(v\)-source by \(L^\dagger\) or \(R^\dagger\). It does not permit keeping an arbitrary erased source without this projection. Sources differing by an element of \(\operatorname{ran}\mathscr R^\dagger\) agree on the constrained preparation. Quadratic marks likewise descend through \(B^\dagger\mathsf T B\). Thus both parenthesizations and units are tested with their full marked preparation, not merely their endpoint means.

## Presentations inherit their states and measures

Put \(K_G=B^\dagger G^{-1}B\) and \(Z_G=(\det K_G)^{-1}\). For a linear presentation readout \(P:\mathcal E\to\mathcal E_P\), with a declared Hermitian pairing on its target, its actual covariance and sourced amplitude are
\[
H_P=PBK_G^{-1}B^\dagger P^\dagger,\qquad
\mathcal Z_G(P^\dagger j,0)=Z_Ge^{j^\dagger H_Pj}.
\tag{WM8}
\]
On \(\mathcal S=\operatorname{ran}(PB)\), the pushforward has density
\[
\frac{Z_G}{\det_{\mathcal S}H_P}
e^{-y^\dagger H_P^+y}\,d_{\mathcal S}y,
\tag{WM9}
\]
where \(H_P^+\) is its supported inverse and the measure uses the inherited pairing. No nonsingular ambient density is claimed when the presentation covariance is singular.

Further readouts push this same measure forward and pull their sources back. Fine sources or quadratic marks that do not factor through a retained readout require the hidden-source factor in the general marked-conditioning theorem. Dropping that factor would lose part of (WM6).

This differs from constructing a fresh isotropic Gaussian on each reduced diagram. After eliminating the other coordinates, the input precision is \(K_G\), not automatically \(I_X\). Its determinant and all inherited source insertions are part of the remaining amplitude. The marked preparations here are one declared finite family; no general refinement functor has been constructed.

## A shape family preserves the determinant and changes the response

Write \(e_{ijk}=e_i\otimes e_j\otimes e_k\). The columns \(Be_{ijk}\) are orthogonal. Since \(L^\dagger L=R^\dagger R=2I\),
\[
B^\dagger B
=I+A_L^\dagger A_L+A_R^\dagger A_R+5F^\dagger F.
\tag{WM10}
\]
Its three classes are:

| Input subspace | Basis | Dimension | \(B^\dagger B\) |
|---|---|---:|---:|
| \(\mathcal D\) | \(000,111\) | 2 | \(8I\) |
| \(\mathcal A\) | \(010,101\) | 2 | \(I\) |
| Remaining \(\mathcal M\) | \(001,011,100,110\) | 4 | \(2I\) |

Let \(\widehat P_D,\widehat P_A\) be the orthogonal projectors in \(\mathcal E\) onto \(B\mathcal D,B\mathcal A\). These subspaces lie in \(\ker\mathscr R\). For \(t>0\), set
\[
\boxed{
G_t=t\widehat P_D+t^{-1}\widehat P_A
+I-\widehat P_D-\widehat P_A.}
\tag{WM11}
\]
This is positive and invariant under the simultaneous exchange \(e_0\leftrightarrow e_1\). It obeys
\[
\det G_t=1,\qquad
\mathscr R G_t\mathscr R^\dagger=\mathscr R\mathscr R^\dagger.
\tag{WM12}
\]
The first identity follows from the two equal projector ranks; the second follows because the projectors lie in the constraint kernel.

With \(P_D,P_A,P_M\) the input projectors, direct restriction gives
\[
K_t=\frac8tP_D+tP_A+2P_M,\qquad
\det K_t=2^{10},\qquad
\boxed{\mathcal Z_t(0,0)=2^{-10}.}
\tag{WM13}
\]
Nevertheless, the normalized input variances are \(t/8\), \(1/t\) and \(1/2\) on these three subspaces, and
\[
\operatorname{Cov}_t(v)=FK_t^{-1}F^\dagger=\frac t8I_V.
\tag{WM14}
\]
The ratio between a \(\mathcal D\) variance and an \(\mathcal A\) variance is \(t^2/8\); this is a shape change, not a uniform rescaling.

For a linear source \(j\) and a sufficiently small Hermitian quadratic mark \(T\) on \(v\), the complete specialization is
\[
\boxed{
\mathcal Z_t(j,T)
=2^{-10}
\frac{\exp\!\left[j^\dagger((8/t)I_V+T)^{-1}j\right]}
{\det(I_V+(t/8)T)}.}
\tag{WM15}
\]
Thus the marked normalization detects the changing response, as required by [[closed-normalization-and-cosmic-response|the common-source identity]], while its unmarked value stays fixed.

At \(t=1\), the inherited input precision has determinant \(2^{10}\) and output covariance \(I_V/8\). Replacing the reduced preparation by a fresh isotropic input instead gives partition one and output covariance \(I_V\). This changes both the state and the closed weight; it is not a coordinate change or legitimate omission of an auxiliary determinant.

This construction is a positive conditional preparation with exact finite unit, reassociation and source identities. It places all displayed variables on one constrained state; it supplies no independent transition noise, genuine cycle stiffness or physical time. The family (WM11) proves that these coherence conditions, fixed \(\mu,h\), the stated symmetry and unmarked normalization do not select the preparation shape. A further principle must fix \(G\), and its physical readouts and limits remain to be constructed.

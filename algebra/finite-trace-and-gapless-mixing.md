# Finite Trace and Gapless Mixing

A single infinite-dimensional finite factor admits a trace-symmetric quantum Markov semigroup with a unique stationary normal state and a unique zero-mode vector, yet no positive spectral gap. Every centered vector decays, but arbitrarily slow modes prevent a uniform decay rate. The same algebra has a finite maximum of entropy relative to its normalized trace. Thus a trace entropy ceiling, even together with mixing and a unique vacuum, does not supply a dynamical floor.

## One fixed finite factor

Form the increasing matrix algebras \(A_N=\bigotimes_{n=1}^NM_2(\mathbb C)\), with embeddings \(x\mapsto x\otimes I\) and normalized product trace. In its tracial GNS representation, put
\[
\mathcal R=\left(\bigcup_NA_N\right)'',\qquad
\tau=\bigotimes_{n\ge1}\frac{\operatorname{Tr}_2}{2},\qquad
\mathcal H=L^2(\mathcal R,\tau),\qquad \Omega=1.
\tag{FT1}
\]
The product trace extends to a faithful normal tracial state. To check factoriality, let \(F_N:\mathcal R\to A_N\) be the trace-preserving conditional expectation. If \(x\) is central, bimodularity makes \(F_Nx\) central in \(A_N\), hence \(F_Nx=\tau(x)1\). Since \(F_Nx\to x\) in \(L^2\), \(x=\tau(x)1\). The increasing matrices are weakly dense, so this is the hyperfinite factor. It contains matrices of arbitrarily large size and is finite, hence is type \(\mathrm{II}_1\), rather than a finite matrix factor.

In particular, \(\tau(1)=1\) does not imply \(\dim\mathcal H<\infty\). The trace \(\tau\) is on \(\mathcal R\); it is not the ordinary operator trace on \(B(\mathcal H)\).

## A conservative process with arbitrarily slow modes

Let \(E_n\) erase only site \(n\): on finite elementary tensors it replaces that factor by its normalized trace times \(I\). Its normal extension is a unital completely positive, trace-preserving conditional expectation; on \(\mathcal H\) it is an orthogonal projection. These projections commute. Define
\[
\boxed{H=\sum_{n\ge1}2^{-n}(I-E_n),\qquad P_t=e^{-tH},\quad t\ge0.}
\tag{FT2}
\]
The series converges in operator norm both as a bounded map on \(\mathcal R\) and on \(\mathcal H\). On the latter, \(0\le H\le I\), with domain all of \(\mathcal H\). Moreover,
\[
P_t=\prod_{n\ge1}\left[E_n+e^{-t2^{-n}}(I-E_n)\right].
\tag{FT3}
\]
Each factor is a convex combination of \(E_n\) and the identity. Summability of the rates makes the products converge in map norm, uniformly on bounded time intervals. Thus \(P_t\) is a normal UCP semigroup preserving \(\tau\), and its \(L^2\) implementation is self-adjoint.

Write \(\sigma_0=I,\sigma_1,\sigma_2,\sigma_3\) for the Pauli basis. The finite words \(w_{\boldsymbol\nu}=\bigotimes_n\sigma_{\nu_n}\), where only finitely many \(\nu_n\ne0\), form an orthonormal basis of \(\mathcal H\). Direct site erasure gives
\[
Hw_{\boldsymbol\nu}=\lambda_{\boldsymbol\nu}w_{\boldsymbol\nu},\qquad
\lambda_{\boldsymbol\nu}=\sum_{\nu_n\ne0}2^{-n}.
\tag{FT4}
\]
Only the empty word has eigenvalue zero. A Pauli matrix at site \(n\) is a normalized centered eigenvector with eigenvalue \(2^{-n}\). Therefore
\[
\boxed{\ker H=\mathbb C\Omega,\qquad
\inf\sigma(H|_{\Omega^\perp})=0.}
\tag{FT5}
\]
Indeed the finite binary sums are dense in \([0,1]\), so the complete spectrum is \(\sigma(H)=[0,1]\). This is one fixed algebra and generator, not a family approaching loss of uniqueness.

Let \(P_0^{\rm vac}\psi=\langle\Omega,\psi\rangle\Omega\). Dominated convergence in the Pauli expansion proves
\[
\boxed{\lim_{t\to\infty}\|P_t\psi-P_0^{\rm vac}\psi\|_2=0
\quad(\psi\in\mathcal H),\qquad
\|P_t-P_0^{\rm vac}\|_{2\to2}=1\quad(t<\infty).}
\tag{FT6}
\]
The last equality follows from the site eigenvectors and \(\sup_ne^{-t2^{-n}}=1\). Thus the process mixes strongly without a uniform rate. Its fixed algebra is \(\mathbb C1\). The predual converges in \(L^1\) for every normal state: approximate its density by bounded densities, use \(L^1\) contractivity, and apply the \(L^2\) convergence to the approximants. Consequently \(\tau\) is its unique stationary normal state.

## An entropy maximum remains present

For a normal-state density \(\rho\in L^1(\mathcal R,\tau)_+\), \(\tau(\rho)=1\), define entropy relative to the trace by
\[
\boxed{S_\tau(\rho)=-\tau(\rho\log\rho)\le0,
\qquad S_\tau(1)=0.}
\tag{FT7}
\]
Use \(0\log0=0\) and allow the value \(-\infty\). Functional calculus applied to \(u\log u-u+1\ge0\) proves the inequality; faithfulness makes equality equivalent to \(\rho=1\). Thus the maximum exists and is unique. Rank-one projections \(p_N\in A_N\) have \(\tau(p_N)=2^{-N}\); their normalized densities satisfy \(S_\tau(p_N/\tau(p_N))=-N\log2\). A finite upper bound is compatible with infinitely many distinguishable directions.

[[qubit-cone-interiorization-and-the-clock-gap|The finite qubit example]] varies a slow rate on a fixed finite carrier. Here the rate sequence is fixed, every nonvacuum mode has positive decay, and their infimum is zero. A positive floor needs a uniform coercive estimate on the chosen process, beyond finite trace, an entropy maximum or uniqueness of the stationary state.

The rates \(2^{-n}\) and the process parameter are supplied. \(H\) is the nonnegative generator of this dissipative \(L^2\) process; it has not been identified with physical energy or spacetime translations. The example refutes an algebraic implication from a \(\mathrm{II}_1\) entropy ceiling to a spectral gap. It makes no claim about the actual dynamics of a gravitational static patch or the Yang–Mills vacuum.

# The QFT Recovery Contract

A theory proposed as more fundamental than QFT must do more than coexist with imported local fibers. It must construct comparison maps that recover the local observable net, state, dynamics, covariance, and tested correlation data in a controlled regime; a Clay-level claim must additionally remove the regulator and produce a nontrivial continuum theory. Selection of the gauge group, vacuum, scale, or coupling trajectory is a separate explanatory burden.

**Status: [EXACT TYPE CONTRACT] for the required return data and distinctions among compatibility relations; [CONDITIONAL] for the gap-preservation theorem under form convergence; [OPEN] for a four-dimensional Yang--Mills realization.**

## The return type

For each compact simple group \(G\) and regulator/background datum \(r\), let \(\mathfrak U_{r,G}\) be the proposed upstream object. A reconstruction must return

$$
\operatorname{Rec}_{r,G}(\mathfrak U_{r,G})
=
\bigl(
\mathsf{Reg},
\mathcal A_{r,G},
\iota_{r},
\omega_{r},
\pi_r,\mathcal H_r,\Omega_r,
U_r,P_{\mu,r},h_r
\bigr).
\tag{RC1}
$$

Here:

- \(\mathsf{Reg}\) is the category of physical regions and inclusions;
- \(\mathcal A_{r,G}:\mathsf{Reg}\to\mathsf{vNAlg}\) is an isotonic local observable net;
- \(\iota_r\) denotes its inclusion structure and comparison maps;
- \(\omega_r\) is a selected compatible state family;
- \((\pi_r,\mathcal H_r,\Omega_r)\) is its physical GNS representation and vacuum;
- \(U_r\) is the covariance representation;
- \(P_{\mu,r}\) obeys the spectrum condition and supplies the physical translations;
- \(h_r\) is the closed vacuum-subtracted energy form; and
- gauge-invariant field, Ward-identity, and short-distance/OPE data identify the returned member as Yang--Mills.

An abstract algebra, a Type-III factor, a positive Hessian, or a symmetry group does not inhabit all these slots.

## The response must descend to the returned carrier

Suppose the upstream object has a distinction map

$$
\delta^{\mathrm{pre}}_{r,w}:
\mathcal D^{\mathrm{pre}}_{r,w}
\longrightarrow
\mathcal K^{\mathrm{pre}}_{r,w}
\tag{RC2}
$$

and the state defines a quotient-and-completion

$$
Q_{r,\omega}:
\mathfrak C_{r,G}
\longrightarrow
\mathcal H_r.
\tag{RC3}
$$

The response is physically realized only if it annihilates the state-null ideal and factors through that quotient. Concretely, one needs bounded response-carrier maps \(V_{r,w}\) and closable physical maps \(\delta^{\mathrm{phys}}_{r,w}\) satisfying

$$
\boxed{
V_{r,w}\delta^{\mathrm{pre}}_{r,w}
=
\delta^{\mathrm{phys}}_{r,w}Q_{r,\omega}.}
\tag{RC4}
$$

Naming an upstream Hessian “energy” does not supply (RC4). Nor does equality of dimensions identify the response form with \(h_r\).

## Six relations that must not be conflated

1. **Compatibility:** two theories do not disagree on observables in their common domain.
2. **Conservative restriction:** the surrounding theory restricts to an imported local net, state, and dynamics.
3. **Constitutive closure:** the whole theory supplies a vacuum, boundary law, gluing, or state selection that an imported local theory accepts.
4. **Effective recovery:** local correlators, amplitudes, Ward identities, and matrix elements agree with controlled errors in a declared physical window.
5. **Strong recovery:** a scaling or renormalization system converges to a Wightman or Haag--Kastler theory, or reflection-positive Euclidean data reconstruct it.
6. **Derivation or selection:** the upstream principles additionally determine why this group, representation, state, scale, and coupling trajectory occur.

[[compatible-with-existing-physics/relations-among-theories|Relations among theories]] owns the general distinction. The present mass-gap programme claims a structure beneath QFT, so recovery rather than verbal compatibility is mandatory. Selection remains orthogonal: recovering an \(SU(3)\) theory does not explain why the color member was selected, and selecting a stabilizer does not recover its dynamics.

## Pure-gauge and Higgs recovery are different return types

The Clay member contains no Higgs variable. Its reconstruction must therefore close on the pure gauge observable net and prove the neutral vacuum edge without importing an electroweak scalar, vacuum expectation value, Yukawa coupling, or measured particle mass. This is the pure-gauge firewall.

A stronger Standard-Model reconstruction would add distinct output slots, schematically

$$
\operatorname{Rec}^{\mathrm{SM}}(\mathfrak U)
\supset
\bigl(
P\to M,\,
E_{\mathrm H}=P\times_GV_{\mathrm H},\,
\widehat\Phi,\,
r,\,
\mathcal R_{\mathrm{chiral}},\,
Y
\bigr),
\tag{RC4a}
$$

where the orbit-direction section \(\widehat\Phi\) presents a stabilizer reduction on its regular locus, \(r\) is the separate gauge-invariant radial mode, \(\mathcal R_{\mathrm{chiral}}\) is the chiral matter representation data, and \(Y\) denotes the Yukawa maps. [[higgs-reduction-as-local-shadow/inq|Higgs reduction as a local shadow]] owns this split. Returning (RC4a) does not prove the pure-gauge response edge; proving that edge does not yet reconstruct (RC4a). A proposed pre-QFT theory must not use either output to define the other after the fact.

## Effective recovery below a threshold

“Below the UV threshold” should not mean sharply truncating every local algebra by a global spectral projection. It means bounds on suitably smeared observables and on matrix elements between energy-controlled states.

Let

$$
r=(a,L,M,b,\ldots)
\tag{RC5}
$$

collect a length cutoff \(a\), a volume scale \(L\), a heavy matching energy \(M\), and background data \(b\). For a physical probe energy \(E\), the natural dimensionless error ledger is

$$
\boxed{
\boldsymbol\epsilon(E,r)
=
\left(
\frac{aE}{\hbar c},
\frac{E}{M},
\frac{\hbar c}{LE},
\epsilon_{\mathrm{bg}}(E;b)
\right).}
\tag{RC6}
$$

Comparison maps must be natural under region inclusion and must intertwine states and dynamics up to bounds controlled by \(\|\boldsymbol\epsilon(E,r)\|\). At fixed physical \(E\), the decoupling limit requires

$$
a\to0,
\qquad
L\to\infty,
\qquad
\frac{M}{\Lambda_{\mathrm{YM}}}\to\infty,
\qquad
\epsilon_{\mathrm{bg}}(E;b)\to0.
\tag{RC7}
$$

Holding a finite UV cutoff may suffice for an effective laboratory model. It cannot discharge the Clay existence problem.

## Strong recovery and preservation of the edge

Suppose the regulated systems provide vacuum projections \(P_{\Omega_r}\), closed forms \(h_r\), and independently constructed dimensionless response forms \(\mathfrak d_r\) such that

$$
\mathfrak d_r
\geq
\kappa_*(I-P_{\Omega_r}),
\qquad
h_r
\geq
\eta_*\Lambda_r\mathfrak d_r,
\tag{RC8}
$$

where \(\kappa_*,\eta_*>0\) are regulator-independent and

$$
\Lambda_r\longrightarrow\Lambda_{\mathrm{YM}}^{(\mathsf s)}>0
\tag{RC9}
$$

in one fixed renormalization convention. If:

1. the varying Hilbert spaces have declared comparison maps;
2. \(h_r\) converges to a densely defined closed form \(h\) in generalized Mosco sense or a comparably strong topology;
3. the normalized vacua and their projections converge strongly enough along recovery sequences;
4. reflection positivity and the remaining Osterwalder--Schrader hypotheses survive; and
5. the reconstructed local net is nontrivial, Poincare covariant, positive-energy, and Yang--Mills identified,

then the uniform lower bound passes to the limiting form:

$$
h
\geq
\kappa_*\eta_*\Lambda_{\mathrm{YM}}^{(\mathsf s)}
(I-P_\Omega).
\tag{RC10}
$$

This is a conditional preservation theorem. It does not establish any of the five convergence and identification hypotheses.

## The admissible hybrid

The least overcommitted programme that can still explain the infrared gap is:

- import the local gauge kinematics, gauge-invariant observable language, and renormalization/OPE data;
- do not import the vacuum spectrum or a fitted glueball correlation length;
- let the whole-law construction select the admissible state, boundary response, and complete distinction carrier;
- prove a regulator-uniform response lower bound independently;
- recover ordinary local QFT in its validated window; and
- reconstruct Poincare time before calling the resulting energy edge a mass.

This is stronger than surrounding an already complete QFT and weaker than deriving the Standard Model. For the Clay problem it must nevertheless work for every compact simple \(G\), yield a nontrivial continuum theory, and prove the gap on its complete physical vacuum complement.

## Failure conditions

The recovery claim fails if any of the following occurs:

- comparison maps are absent or ignore states and dynamics;
- the upstream response does not factor through the physical null quotient;
- the “low-energy sector” is defined using the desired spectrum;
- a finite-cutoff effective theory is presented as a continuum construction;
- the response floor collapses with volume or lattice refinement;
- vacuum projections do not converge;
- only a charged, twisted, or finite-probe sector is controlled;
- local Poincare covariance or the spectrum condition is not recovered; or
- the returned theory is not identified as nontrivial Yang--Mills.

---
inq.module: "binary-information-geometry"
inq.include:
  - "**/*.md"
---
# Binary Information Geometry

A normalized involution supplies an exact binary allocation between resolved polarization and residual susceptibility; a balanced reference state then selects the centered hyperbolic family whose Fisher line, relative entropies, and Witten--Darboux factorization are calculated in this module. All results are internal to the stated reduced statistical model and carry no automatic interpretation as spacetime dynamics, gravity, entropy, or conserved Noether charge.

Begin with a self-adjoint involution \(Q\). The relation \(Q^2=\mathbf 1\) fixes its two spectral values but neither their weights nor their physical meaning. For any state with finite second moment, [[involutive-casimir|the involutive Casimir identity]]

$$
m^2+\operatorname{Var}(Q)=1,
\qquad
m:=\langle Q\rangle,
$$

is exact. It is a second-moment decomposition: the representation normalization is fixed while the state-dependent mean and variance redistribute it.

A distinguished centered curve requires more structure. If a faithful reference state commutes with \(Q\) and gives equal total weight to the \(Q=\pm1\) sectors, [[balanced-exponential-family|the balanced exponential family]] has

$$
m(\theta)=\tanh\theta,
\qquad
g^{\mathrm{bin}}_{\theta\theta}
=\operatorname{sech}^2\theta,
\qquad
m^2+g^{\mathrm{bin}}_{\theta\theta}=1.
$$

Balance is a hypothesis, not a consequence of involutivity. Without it the same hyperbolic profile is translated away from \(\theta=0\). [[a2-ternary-response/inq|The \(A_2\) ternary-response test]] audits the still earlier assumption that the physical reduction has exactly two outcomes: its natural three-sheet finite model has a different response until the neutral sheet is removed by a specified channel, conditioning, or decoupling limit.

The metric is globally simpler than its exponential coordinate suggests. [[fisher-line|The binary Fisher line]] is flattened by the Gudermannian,

$$
\phi=\operatorname{gd}(\theta),
\qquad
\mathrm ds_{\mathrm{bin}}^2=\mathrm d\phi^2,
$$

and the two fully polarized endpoint states lie a finite information distance \(\pi\) apart. This finite normalized length says nothing by itself about the multiplicity or renormalized norm of a larger physical system.

Relative entropy remembers the affine coordinate as well as the metric. [[reflected-divergence|The binary divergence formula]] gives the exact two-point expression

$$
D(\rho_\theta\Vert\rho_\vartheta)
=(\theta-\vartheta)m(\theta)
-\psi(\theta)+\psi(\vartheta),
$$

whose coincidence Hessian is \(g^{\mathrm{bin}}_{\theta\theta}\). Reflection through the balanced point produces an even divergence, so the reduced geometry cannot choose an orientation of evolution.

Finally, the square root of the susceptibility is the unique normalizable zero mode of [[witten-darboux|the binary Witten--Darboux pair]]:

$$
\psi_0(\theta)
=\frac{1}{\sqrt2}\operatorname{sech}\theta,
\qquad
|\psi_0|^2
=\frac12g^{\mathrm{bin}}_{\theta\theta}.
$$

After restoring inverse width \(\nu\) and address \(N_c\), the partner operator is free above \(\nu^2\), the nontrivial potential is reflectionless, and the same factorization is unitarily equivalent to the sharp logistic Poincare inequality with lower edge \(\nu^2\). Conversely, a homogeneous partner with an initially unspecified real constant and one normalizable ordered zero mode force that constant to be positive and uniquely force the translated logistic family. These are exact statements about the one-dimensional reduced carrier. Turning them into a perturbation operator, field equation, causal charge, gravitational response, or physical mass requires additional mathematical objects and independent physical principles.

# Salvage Ledger

These results exist in exactly one place. Several live inside receipt scripts rather than prose, which means a consolidation working from the two newest documents would silently drop them. Each entry gives the claim, where it is, and where it should land.

Priority reflects how hard the result would be to rediscover, not how important it is. A computed no-go that took a real calculation is expensive to lose; a framing is cheap to restate.

## Computed no-go results

The two below are quantitative and specific. [[causal-scale-theory/sources/legacy/causal-scale-master-v8/perturbation-and-qft-interface|v8's no-go list]] contains four generic statements — that the smooth-dark-energy growth equation is not the Pöschl–Teller operator, that the response density is not a wave potential, that reflectionlessness fixes no signal speed, and that factorization fixes no kinetic sign — but not these.

**N2 — no single-field completion, at the critical coupling.** For a canonical scalar, $z^2\propto1+w_X=(2\nu/3)\tanh\theta$ is negative across the entire pre-crossing branch: a ghost over a cosmological epoch, not a point defect. Near $\theta=0$, $z\sim\lvert\theta\rvert^{1/2}$ and

$$
\frac{z''}{z}\longrightarrow-\frac{1}{4\theta^2},
$$

the inverse-square potential at exactly the critical coupling $1/4$ for fall-to-the-centre. The crossing is marginal in a precise sense, which is *why* small deformations of one-field models do not cure it — a fact the generic statement does not convey. Source: [[scale-as-modular-observable/misc/scale-as-a-modular-observable|Revision 2]] §23. Target: `no-go-register.md`.

**N4 — no canonical sigma model.** Imposing the soldering $\dot\theta=\nu H$ on $\Gamma=\int\sqrt{-g}\,[(\chi/2)G(\theta)(\partial\theta)^2-V]$ together with the target profile requires

$$
H^2=\frac{2\rho_*}{3\chi\nu}\tanh\theta<0
$$

across the whole pre-crossing branch. An exact no-go, and the sharpest available statement that the response cannot be a field in the ordinary sense. Same source and target. It is independently receipted as R20 in [[scale-as-modular-observable/chats/03/outputs/receipts_transparency_fold.py|the fold receipt]].

**Version-B falsification.** The conformally natural alternative — taking the response fraction proportional to a pure number, avoiding a dimensionful constant altogether — is dead by exhaustion: below a threshold the solution cannot reach the present epoch, above it the fraction becomes singular, and inside the viable window the density peak sits where $w_X\simeq0$ rather than $-1$, losing both the crossing coincidence and the shape invariant. This is the argument that *forces* a dimensionful amplitude, so losing it makes the amplitude look like an unforced choice. It exists only as R21 in the fold receipt and in neither monograph. Target: `no-go-register.md`, with the receipt as its provenance.

## Sharper versions of statements the canon already has

**The free-energy counterexample** and **the $\operatorname{Var}(-\ln\rho)$ versus BKM separation**, both in [[scale-as-modular-observable/claim-audit|the claim audit]] and both stronger than their v8 counterparts. Restated with their algebra in [[synthesis-plan|the synthesis plan]]; targets `free-energy-source.md` and [[wall-construction-interface/cross-fiber-transport|cross-fiber transport]] respectively.

## Structural results about testability

**Background data cannot see the shape invariant.** Embedding the profile in $\rho_X\propto\operatorname{sech}^p(\beta x)$ gives

$$
9X^2+6\frac{\mathrm dX}{\mathrm dN}
=X^2\!\left(9-\frac{18}{p}\right)+2p\beta^2,
$$

constant if and only if $p=2$. The reason the exponent is unconstrained is analytic, not statistical: the accessible data span roughly $\theta\in[-0.42,+0.28]$, under one transition width, while $p$ controls the tails where the response is subdominant. Reaching $\theta\simeq-2$ would need data near $z\simeq48$. Source: [[scale-as-modular-observable/chats/02/outputs/P1_shape_invariant_result|the P1 result]], which concluded the test should be demoted. Target: `observables.md`, as the power statement attached to the invariant row.

The accompanying numbers — a profile likelihood flat to $\Delta\chi^2\simeq0.8$ across two orders of magnitude in $p$, and forecast requirements of several to twenty times better background data — are versioned fit outputs and belong under the withheld-claims ledger in [[receipts-plan|the receipts plan]], not in the canon. The structural argument stands without them.

**The negative control.** A null ensemble of matched smooth positive transient histories reproduced the model's CMB-lensing response direction closely enough that the great majority of the ensemble passed the same test, so the apparent agreement measures class membership rather than discrimination — and the evidence ledger *excluded it on those grounds*. Source: [[scale-as-modular-observable/misc/scale-as-a-modular-observable|Revision 2]] §28. Target: `observables.md`. Worth keeping as much for the method as the result: it is the archive's clearest instance of discarding a favourable-looking result on principle, and the receipt contract should require that move.

## Geometry and structure

**The tractor-parallel / tractor-source split.** Having killed the identification of the pullback state metric with the tractor norm, the fold receipt proposes a different reading: since $w_X=-1$ exactly at the crossing, the trace-free stress $\tau^0_{ab}=(\rho+p)[u_au_b+g_{ab}/4]$ vanishes there, so the response is entirely tractor-parallel and sources nothing in the trace-free channel — and $\mathfrak R_c$ at its unit value makes the energy budget split one-to-one between the tractor-parallel and tractor-source sectors.

This is the highest-value orphan. It is a *geometric* reading of the amplitude law that does not pass through the capacity argument, which matters precisely because the capacity argument is where the invalid Cardy step lived. If it holds it is a bridge between [[causal-scale-theory/sources/legacy/causal-scale-master/scale-tractor|tractor geometry]] and the information-geometric amplitude. Source: R17 in the fold receipt, absent from all five master documents. Caveat: it cites an identifier whose description [[scale-as-modular-observable/claim-audit|the claim audit]] flags as mismatched, so the citation needs checking before reuse. Target: [[quarantine|quarantine]] first, `scale-capacity.md` only if it survives.

**The Gudermannian half-turn, in both position and momentum.** With $\varphi=\operatorname{gd}(\theta)=\arctan(\sinh\theta)$ one has $\mathrm d\varphi=\operatorname{sech}\theta\,\mathrm d\theta=\mathrm ds_{\rm Fisher}$, so

$$
L_F=\int_{-\infty}^{\infty}\operatorname{sech}\theta\,\mathrm d\theta=\pi
$$

is the Fisher diameter of the binary simplex, the crossover is a complete traversal between extremal states, and $\rho_X/\rho_*=\cos^2\varphi$. [[causal-scale-theory/sources/legacy/causal-scale-master/binary-geometry|binary-geometry]] keeps $L_F=\pi$ but not the Gudermannian or the reparameterization. The momentum-space partner — the transmission phase sweeping the same Gudermannian in $\ln k$ — is in [[scale-as-modular-observable/chats/02/outputs/rubles_equations|rubles_equations]] and in neither monograph; it is the step that actually welds the two appearances of $\pi$ rather than noting they coincide. Targets: `binary-geometry.md` and [[causal-scale-theory/sources/legacy/causal-scale-master/witten-pair|witten-pair]].

## Framing and fallback positions

**The impossibility argument for a dimensionful constant.** Mathematics produces forms and dimensionless ratios; it cannot produce a dimensionful number. Demanding a derivation of the dimensionful amplitude therefore demands something provably impossible, and postulating it is not a deficiency but the only available move. Source: [[scale-as-modular-observable/chats/02/outputs/rubles_equations|rubles_equations]] §7, absent from both monographs, which instead route the amplitude through the capacity chain and advertise zero free dimensionful constants.

My view is that this should be recovered and kept explicitly as the fallback: it is the position the theory retreats to if the amplitude principle is falsified, and a programme with a stated fallback is in better shape than one whose only account of a constant is a chain containing a known invalid step. It also connects directly to [[cosmodynamics/soldering-constants|constants as soldering structures]], which asks the same question in general form. Target: `scale-capacity.md`, as a declared alternative to the principle.

**The state coordinate as a collective constitutive quantity.** Typed the same as inverse temperature, a chemical potential, or an order parameter — neither a propagating local field, which N4 excludes, nor a function reconstructed from the metric, which the independence test excludes. The accompanying observation is that temperature is real, gravitates, and has gradients that do physics, and nobody demands its kinetic term. [[causal-scale-theory/sources/legacy/causal-scale-master/free-energy-source|v7's note]] has a compressed version; the full typing argument and its use against the phantom-ghost objection are in Revision 2 §23. Target: `free-energy-source.md`, and it should link to [[cosmodynamics/registers-and-type-discipline|type discipline]], which owns exactly this kind of argument.

## Not evergreen — do not recover

**The directedness theorem.** Revision 2 §24 argues that non-negativity of relative entropy forces the phantom-to-quintessence orientation of the crossover. [[scale-as-modular-observable/claim-audit|The claim audit]] refutes it: the symmetrized divergence is even under $\theta\mapsto-\theta$ and cannot select an arrow; the orientation follows from the chosen profile, a positive slope, increasing scale, and conservation. Recorded here so it is not rediscovered and re-promoted. The genuine question it gestures at — the arrow of time — belongs to [[sufficient-reason/algebraic-arrow-of-time|the algebraic arrow of time]], not here.

**The retarded-pole argument.** That the internal scattering problem's pole location establishes retardedness. The internal coordinate is not physical time, and retardedness needs a physical evolution equation and convention the factorization does not supply. Same source, same refutation.

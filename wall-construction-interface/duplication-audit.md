# Duplication Audit

This ledger records the ownership boundary between the shared wall-construction interface, the exact mathematical leaves in Causal Scale Theory, and the consumer programmes. It is an architectural audit: each statement should have one canonical owner even when several modules depend on it.

## Ownership of shared statements

| Statement | Canonical owner | Related consumers |
|---|---|---|
| The scale-indexed package of regions, algebras, states, modular data, transport, scale law, cocycle, and generator | [[entry]] | [[causal-wall-spectral-theory/causal-scale-interface]], [[scale-as-modular-observable/observable-map]] |
| A derivative of the state family is undefined before transport | [[cross-fiber-transport]] | [[causal-wall-spectral-theory/causal-scale-interface]] |
| The four transport strategies | [[cross-fiber-transport]] | — |
| Vertical modular flow and horizontal state deformation are different types of motion | [[causal-scale-theory/modular-flow]] | [[cross-fiber-transport]], [[causal-wall-spectral-theory/causal-scale-interface]], [[scale-as-modular-observable/observable-map]] |
| Only the state-change term in the three-term modular decomposition can carry the proposed horizontal response | [[causal-scale-theory/modular-flow]] | [[cross-fiber-transport]] formulates the construction obligation |
| Geometric reflection is not automatically Tomita conjugation; factoriality obstructs a naive identification | [[binary-channel]] | [[causal-scale-theory/balanced-channel-premise]], [[causal-scale-theory/binary-geometry]] |
| The channel $\mathcal E_N$ has several non-interchangeable readings | [[binary-channel]] | [[causal-scale-theory/balanced-channel-premise]] |
| Balanced reference weights are an additional premise, not a normalization convention | [[causal-scale-theory/balanced-channel-premise]] | [[binary-channel]] |
| Ratio dependence, additivity, and regularity imply an affine scale coordinate but do not fix its slope | [[causal-scale-theory/scale-soldering]] | [[cross-fiber-transport]] formulates the transport-side obligation |
| Cocycle failure modes | [[cross-fiber-transport]] | [[causal-scale-theory/scale-soldering]] |
| State selection is substantive; no covariantly preferred state is supplied for free | [[cross-fiber-transport]] | [[causal-wall-spectral-theory/causal-scale-interface]], [[causal-wall-spectral-theory/open-problems]] |
| Independence and anti-circularity tests | [[elimination-test]] | both consumer programmes |
| Conservative-restriction test | [[elimination-test]] | [[compatible-with-existing-physics/local-physics-interface]], [[causal-wall-spectral-theory/causal-scale-interface]] |
| Two completion levels | [[entry]] | [[causal-wall-spectral-theory/causal-scale-interface]] |
| The five-rung construction ladder and its literature precedents | [[construction-ladder]] | [[cross-fiber-transport]] |

## Remaining architectural cautions

**External-scale regularity is not modular-parameter regularity.** Sigma-weak continuity of $u_t$ in its cocycle parameter does not establish measurability with respect to the external scale ratio. [[cross-fiber-transport]] owns this distinction, while [[causal-scale-theory/scale-soldering]] states exactly which regularity premise its affine theorem needs.

**Reflection and Tomita conjugation remain distinct.** The canonical algebra now uses geometric reflection $J_{\rm refl}$ and makes balance explicit in [[causal-scale-theory/balanced-channel-premise]]. [[binary-channel]] owns the still-open construction that would obtain such a quotient from a local algebra. This prevents exact binary algebra from being mistaken for a derivation of the channel.

**CWST still repeats one internal claim audit.** The three rank-one claims in [[causal-wall-spectral-theory/causal-scale-interface]] overlap with the rank-one discussion in [[causal-wall-spectral-theory/claim-audit]]. Only the first claim is an obligation of this shared interface; the remaining two are consumer-side. That consolidation belongs inside CWST.

**The source-library boundary remains unsettled.** [[construction-ladder]] and [[cross-fiber-transport]] cite primary sources stored inside `causal-wall-spectral-theory/sources/papers/`. If that library is vault-wide infrastructure, it should eventually become a top-level source module; if it is CWST's working bibliography, this interface should carry a small provenance ledger of its own.

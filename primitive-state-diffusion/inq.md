---
inq.module: primitive-state-diffusion
inq.include:
  - './'
keywords: [primitive states, Jordan algebra, overlap kernels, harmonic analysis, diffusion, loss rate]
---
# Primitive State Diffusion

Repeated comparisons between primitive Jordan states construct a diffusion on their complete square-integrable function space. Sharper tensor-overlap comparisons determine the limiting spectral shape, while their lost squared norm determines the same closed energy form. The result is exact for the declared compact orbit, invariant law and comparison rule; a physical observable algebra and clock require further construction.

## A comparison law determines every harmonic rate

[[primitive-state-diffusion/overlap-kernels-and-harmonics|Overlap kernels and harmonics]] starts with the trace pairing on the primitive sphere \(S^8\) or Cayley plane \(\mathbb OP^2\). Its tensor powers give positive Markov operators \(B_k\) on all of \(L^2(X,\mu)\), with exact Jacobi multipliers on every harmonic degree. These operators have finite rank. Their action on linear symbols is therefore only one part of the function-space comparison; it does not identify them with the [[exceptional-state-comparison/primitive-peirce-response|Peirce pinching of matrices]].

## Refinement retains the complete carrier

[[primitive-state-diffusion/comparison-refinement-and-loss-rate|Comparison refinement and loss rate]] processes comparisons at rate \(k\). Both ordinary repeated comparison and the continuous interpolation converge to the generator with eigenvalues \(\ell(\ell+\rho-1)\), where \(\rho=8\) on the sphere and \(\rho=12\) on the Cayley plane. A bound on the full spectral tail proves operator-norm heat convergence for every fixed positive time. The rescaled loss \(\tfrac{k}{2}(I-B_k^*B_k)\) recovers the same closed quadratic form and its domain.

## The geometric return fixes the metric convention

[[primitive-state-diffusion/trace-metric-and-ball-return|Trace metric and ball return]] identifies the limit as \(-\tfrac12\Delta_{g_{\rm tr}}\). For the rank-two orbit this supplies the round-sphere generator used in the fixed sphere-to-ball projection, including all retained polynomial modes and the inherited boundary realization. A gap on a fixed compact state orbit does not supply a physical mass gap: observable composition, spatial locality, physical time and the vacuum representation remain separate obligations.

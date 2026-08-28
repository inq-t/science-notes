---
inq.module: "a2-spectral-geometry-of-jacobian-counterexample-3d"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.tex"
  - "**/*.py"
  - "**/*.txt"
---
# The $A_2$ Spectral Geometry of the 2026 Jacobian Counterexample

The explicit polynomial counterexample to the Jacobian Conjecture announced in July 2026 has an inverse problem governed by the binary cubic $\Phi_{p,q,r}(S,T)=2pS^3-qS^2T+2ST^2-rT^3$, and its nonproperness set is that cubic's discriminant hypersurface. Three consequences follow. Near the triple-root curve an explicit change of parameters identifies the family with the miniversal deformation $u^3+au+b$ of the $A_2$ singularity times one smooth parameter, so the germ of the nonproperness locus is the standard cuspidal discriminant $4a^3+27b^2=0$ times a line. The generic inverse cover has full $S_3=W(A_2)$ monodromy. And the pushforward algebra of the three-sheeted cover carries a canonical bundle of Lie algebras with fibers $\mathfrak{sl}_3(\mathbb{C})$, together with a Cartan subbundle, the six $A_2$ root spaces, and Weyl monodromy. All three are intrinsic to the finite étale inverse cover; no physical gauge-theoretic interpretation is asserted.

## Main theorem

Let $\Gamma$ be the triple-root curve of the inverse cubic and $\Sigma$ its discriminant hypersurface, which is also the nonproperness locus of $F$.

1. Along $\Gamma$, the germ of the pair $(\Sigma,\Gamma)$ is analytically isomorphic to $(\{4a^3+27b^2=0\},0)\times(\mathbb{C},0)$ — the nonproperness hypersurface is transversely the discriminant of the miniversal $A_2$ deformation.
2. Over $U=\mathbb{C}^3\setminus\Sigma$ the inverse map is a connected finite étale cover of degree three with full monodromy group $S_3=W(A_2)$.
3. For $E=\pi_*\mathcal{O}_{X^\circ}$ the rank-three pushforward algebra of the inverse cover $\pi:X^\circ\to U$, $\mathrm{End}_0(E)$ is a canonical Lie-algebra bundle with fibers $\mathfrak{sl}_3(\mathbb{C})$; the trace-zero multiplication operators form a Cartan subbundle, and étale-locally the remaining six line bundles are the root spaces of type $A_2$.

The map itself satisfies $\det JF=-2$, with $F(0,0,-\tfrac14)=F(1,-\tfrac32,\tfrac{13}{2})=F(-1,\tfrac32,\tfrac{13}{2})=(-\tfrac14,0,0)$. The two-variable case remains open.

## Exact verification

`verify_a2_spectral_geometry.py` checks five displayed identities in exact SymPy arithmetic — the depressed-cubic identity, the discriminant identity $\Delta = 4p^4(-4a^3-27b^2)$, the coordinate-Jacobian identity and its nonvanishing on $\Gamma$, the cusp certificate, and the discriminant of $\Delta$ as a quadratic in $r$. Each is an `assert`; the script prints "All exact checks passed." and the recovered normal forms. Its captured output is `verify_a2_spectral_geometry-output.txt`.

## Provenance

Research note, version 0.1, dated 23 July 2026; not peer reviewed. Reserved Zenodo DOI `10.5281/zenodo.21519096`. MSC 2020: Primary 14R15; Secondary 32S25, 14D05, 17B20.

The counterexample itself is Alpöge's; the identification of the inverse problem with the displayed cubic and the equality of the nonproperness locus with its discriminant are taken from the public verification manuscript. The normal-form calculation and the organization of the inverse cover into the type-$A_2$ package are this note's own contribution.

`a2_spectral_geometry_standalone.tex` carries the metadata as editable macros at the top of the preamble (`\AuthorName`, `\PreprintVersion`, `\PreprintDate`, `\PreprintDOI`) and a self-contained `thebibliography`; it compiles without external files. The three filenames had browser download-duplicate suffixes (`(3)`, `(1)`) when this module was assembled, which were stripped.

---
inq.module: "holographic-cosmology"
inq.include:
  - "**/*.md"
---
# Holographic Cosmology

Holographic cosmology represents primordial cosmological observables through correlation functions of a lower-dimensional Euclidean quantum field theory. In the McFadden--Skenderis construction, a four-dimensional single-scalar cosmology is paired with a Euclidean domain wall, gauge/gravity duality is applied to the wall, and the resulting QFT response functions are analytically continued back to cosmology. The scalar, tensor, and higher-point dictionaries are controlled within that class; they are not identities for every cosmology, every three-dimensional QFT, or every object called a wall.

Claim labels use [[program-core/axioms-and-principles#Status vocabulary|the programme-wide status vocabulary]]. Notes outside the commentary directory present the vendored theory in its own terms. [[vendor/holographic-cosmology/commentary/cwst-translation|The CWST boundary commentary]] and [[vendor/holographic-cosmology/commentary/representation-is-not-ontology|the representation commentary]] state project-specific judgments, while [[causal-wall-spectral-theory/holographic-spectral-adapter|CWST's optional holographic adapter]] owns the canonical consumer-side qualification.

## The construction

The logical chain is

$$
\begin{aligned}
\text{single-scalar cosmology}
&\xleftrightarrow[\text{analytic continuation}]
{\text{domain-wall/cosmology}}
\text{Euclidean domain wall}\\
&\xleftrightarrow[\text{gauge/gravity}]{}
\text{three-dimensional QFT}\\
&\xrightarrow[\text{continue }q\text{ and theory parameters}]{}
\text{cosmological correlators}.
\end{aligned}
$$

[[vendor/holographic-cosmology/domain-wall-cosmology-correspondence|The domain-wall/cosmology correspondence]] owns the first arrow. It is a relation between solutions and their perturbations, not yet holography. [[vendor/holographic-cosmology/stress-tensor-response|Stress-tensor response]] owns the Euclidean QFT decomposition and holographic response functions. [[vendor/holographic-cosmology/analytic-continuation-and-state|Analytic continuation and state selection]] records the branch, parameter continuation, regularity condition, and Bunch--Davies state that make the second passage physical.

For a member satisfying those hypotheses, [[vendor/holographic-cosmology/scalar-and-tensor-spectra|the scalar and tensor dictionary]] expresses primordial spectra through the continued spin-zero and spin-two stress responses. The dictionary distinguishes a response calculated from a QFT from a target inferred backward from measured power. Agreement is a test; the data-inferred target cannot serve as the model's calculation.

[[vendor/holographic-cosmology/higher-point-dictionary|The higher-point dictionary]] shows why one cannot extend the map by merely replacing a two-point function with a three-point function. Semilocal metric-variation terms and the cosmological in-in prescription are essential. [[vendor/holographic-cosmology/einstein-single-clock-member|The Einstein single-clock member]] then checks the normalization by reproducing the standard leading scalar and tensor relations when semiclassical Einstein gravity and one canonical clock are supplied.

## Claim status

- **[STANDARD]:** gauge/gravity stress-response methods, holographic renormalization, cosmological perturbation theory, and the in-in formalism within their ordinary domains.
- **[CONDITIONAL THEOREM]:** the domain-wall/cosmology response and spectrum dictionaries after the stated background, state, continuation, renormalization, and gauge/gravity hypotheses are granted.
- **[EXACT]:** tensor contractions and normalization conversions after one convention has been fixed.
- **[CONDITIONAL OUTPUT]:** response functions and cosmological correlators independently calculated by one fully specified holographic member.
- **Empirical test:** comparison of those calculated return values with independently inferred cosmological targets.
- **Not supplied:** a universal holographic dual for arbitrary cosmology, a theory of quantum measurement, a causal-wall algebra, or an information-geometric derivation of the QFT response.

The foundational papers are mirrored locally: [[library/pseudo-supersymmetry-and-the-domain-wall-cosmology-correspondence/inq|Skenderis--Townsend on the domain-wall/cosmology correspondence]], [[library/holography-for-cosmology/inq|McFadden--Skenderis on holographic cosmology]], [[library/cosmological-3-point-correlators-from-holography/inq|McFadden--Skenderis on three-point correlators]], and [[library/on-the-power-spectrum-of-inflationary-cosmologies-dual-to-a-deformed-cft/inq|McFadden on the deformed-CFT spectral function]].

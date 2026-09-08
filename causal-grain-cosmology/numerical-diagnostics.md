# Horizon-Ratio Diagnostics and Their Calibration Limits

The early numerical experiments ask whether a conditionally calibrated grain can fix a late-time horizon ratio, and whether that ratio represents drag, entropy, or a geometric boundary. They contain useful algebraic comparisons but retain supplied cosmological parameters and additional event choices. Their historical captions are not promoted to physical conclusions. The common-count law, the acoustic likelihood result, and the material-history tests in [[causal-grain-cosmology/inq|the module synthesis]] remain separate from these diagnostics.

## Equality and cubic degeneracy are different cuts

[[causal-grain-cosmology/drag_and_bit.py|The drag-and-bit calculation]] compares the Schwarzschild radius of the matter enclosed in a flat-background Hubble sphere with that sphere's radius. With \(R_A=c/H\), \(M=(4\pi/3)\rho_mR_A^3\), and \(\Omega_m=8\pi G\rho_m/(3H^2)\), the identity is

\[
\frac{2GM/c^2}{R_A}=\Omega_m.
\]

For dust plus a positive cosmological constant, neglecting radiation, \(n=H/H_\Lambda\) additionally gives \(\Omega_m=1-n^{-2}\). Thus \(n^2=2\) is matter--vacuum equality, while \(n^2=3\) is acceleration onset. Some numerical sections include radiation; the dust--vacuum equalities are not exact for that enlarged background.

[[causal-grain-cosmology/nariai_check.py|The Nariai comparison]] inserts the enclosed mass into the Schwarzschild--de Sitter cubic. In its stated \(c=1\) convention,

\[
2GM\sqrt{\Lambda}=\sqrt3\,\frac{n^2-1}{n^3}
\]

has maximum \(2/3\) at \(n^2=3\). This is an exact algebraic correspondence between the selected homogeneous constraint and the static cubic. It does not identify the full FLRW spacetime with a static black-hole geometry or turn a varying enclosed mass into one conserved Schwarzschild parameter. The distinction from a spectral-support crossing is developed in [[the-grain-of-causal-scale/causal-spectrum|the causal-spectrum audit]].

The bit and logarithm comparisons likewise depend on their declared conventions: \(2\ln\sqrt2=\ln2\), but choosing natural logarithms does not derive an event or prevent a consistent change of information units. The scripts' quoted offsets and “sigma” labels use fixed background numbers and a restricted propagated error; neither script evaluates an observational likelihood or establishes a statistical exclusion.

## Horizon ratios do not determine dissipation

[[causal-grain-cosmology/friction_test.py|The friction test]] first evaluates the prescription \(T_H=\hbar H/(2\pi k_B)\), whose ratio to its asymptotic value is algebraically \(n\). That substitution is not a derivation of the temperature of an arbitrary evolving horizon. Its stronger diagnostic compares two different supplied expansion laws: dust plus vacuum gives \(n=\sqrt{1+Ka^{-3}}\), whereas its constant-bulk-viscosity model gives \(n=1+Ba^{-3/2}\). Matching them today does not make their earlier histories agree. The script's “ruled out” wording exceeds its calculation: no supernova likelihood is evaluated there.

[[causal-grain-cosmology/leak_test.py|The leakage test]] separates comoving-box work, Hubble radius, particle horizon, and event horizon in a fixed background, then evaluates the matter contribution to a chosen apparent-horizon flux law. Its background contains radiation, but its printed flux omits radiation's contribution to \(\rho+p\); the identification with \((3/2)(1-n^{-2})c^5/G\) is the dust--vacuum specialization. Statements about a reversible perfect-fluid model do not exclude entropy production in a different matter model. In particular, changing comoving energy, horizon flux, and lost distinguishability are not one quantity. [[causal-grain-cosmology/trace-residue-as-a-scale-cocycle|The trace cocycle]] now makes the narrower conserved-sector history statement without interpreting all redshift as dissipation.

## An e-fold anchor is a conditional calibration, not a mass-creation date

[[causal-grain-cosmology/grain_efold_anchor.py|The e-fold anchor calculation]] starts with the hard-coded chiral-branch value \(E_*=46.03\,\mathrm{MeV}\), propagates an \(F_\pi\)-only error, and inverts the common-count law to obtain \(H_c\). It compares this with \(H_\Lambda=H_0\sqrt{\Omega_\Lambda}\) from supplied background parameters. Predicting a second asymptotic plateau additionally assumes \(H_c/H_\Lambda=\sqrt2\). The resulting resolution depth is

\[
N_P=\ln\frac{c}{H\ell_P},\qquad
\frac{dN_P}{d\ln a}=-\frac{d\ln H}{d\ln a}.
\]

The script places the origin of its shifted e-fold coordinate at a supplied \(155\,\mathrm{MeV}\) thermal reference, using declared entropy-degree counts. Its phrase “birth of mass” is that historical label, not a proved event. [[causal-grain-cosmology/standard-model-trace-fossil-diagnostic|The thermal trace diagnostic]] and [[causal-grain-cosmology/pair-annihilation-quotient-and-the-baryon-acoustic-carrier|the pair-exposure model]] distinguish a constitutive crossover, exposure of a conserved excess, and a spectral mass statement.

[[causal-grain-cosmology/grain_efold_plot.py|The plotting companion]] presents these comparisons in [[causal-grain-cosmology/grain-efold-anchor.png|the retained three-panel figure]]. The blue asymptotic plateau uses the supplied \(H_0,\Omega_\Lambda\); the red plateau uses the extra equality assumption. The figure's restricted input list, approximate dust-only label on a radiation-inclusive curve, and mass-origin caption must be read with those qualifications. It is not an additional fit or a replacement for the frozen acoustic-transfer tests.

The two scripts retain their original execution contract: the calculator writes `/home/claude/grain_efold.npz`, and the plotter reads that archive and writes `/home/claude/grain_efold_anchor.png`. The intermediate archive is not included in this module; the retained image has a hyphenated filename. NumPy, SciPy, and Matplotlib are required across the pair. These historical paths and scripts are preserved, not portable plotting commands or a claim of a fresh reproduction.

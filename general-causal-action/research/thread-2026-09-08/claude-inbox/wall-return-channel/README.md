# Return channel of a wall — receipts (2026-09-09)

D = E_omega o iota : N -> N, E_omega the Accardi–Cecchini/Petz omega-dual of the inclusion N ⊂ M.
Takesaki: D = id iff N is invariant under the modular flow of (M, omega).

- `wall_receipt.py` — two finite walls (qubit diagonal MASA; qubit subsystem), closed-form gaps, Takesaki check.
- `wall_fermion_verify.py` — fermionic Gaussian wall: brute-force D on a 5-site Kitaev/TFI chain vs the derived one-particle formula
      X = [sqrt(1+Γ_R²)]_AA · [sqrt(1+Γ_AA²)]^{-1}   (agreement 1e-7; full spectrum of D generated multiplicatively from spec X).
      The case R = whole chain fails, correctly: omega is then pure on M, not separating, and the wall is undefined.
- `wall_fermion_rate.py` — exact infinite chain (45 digits): one central site inside R = ±R sites.
      h=J (critical): lam_1 ~ R^{-1}.   h>J: lam_1 ~ R^{-1/2} exp(-2R/xi), rate = 2 ln(h/J) = 2/xi to 3 digits after 1/R extrapolation.
- `wall_fermion_controls.py` — two-site small region gives the same rate; critical exponent -> 1 at R = 16..32.

Outputs are stored alongside as *_output.txt. Nothing here touches four dimensions or gauge fields.

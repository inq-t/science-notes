# Mass Is Acceleration-Flux

The translation equation between mass, acceleration, gravity, and "gradient of space" exists in closed form twice over — once in Newton, once in Einstein — and in both the cubed meters of $G$'s units are doing exact work. This note states both forms with their types and fixes what "gradient of space" can mean without a category error.

## The Newtonian form

Gauss's law for gravity:

$$
\oint_{\partial V}\mathbf g\cdot\mathrm d\mathbf A=-4\pi G\,M_{\mathrm{enc}} .
$$

Type it: the left side is an acceleration integrated over an area — units $\mathrm{m^3\,s^{-2}}$. So $GM$ *is* an acceleration-flux, and $G$ is the conversion from the SI mass register to the flux register. This is why the astronomically exposed quantity is always the product $GM$ ([[gm-not-g]]): orbits couple to the flux, not to the kilogram count.

"Gradient of space": in the weak-field metric the acceleration is $\mathbf g=-c^2\nabla\hat\Phi$ with $\hat\Phi=\Phi/c^2$ dimensionless — an acceleration is $c^2$ times the spatial gradient of a pure number. Equivalently $a=c^2/d$ where $d$ is the distance to the acceleration's own Rindler horizon; the de Sitter case $a=cH=c^2/R_H$ is the same identity at the cosmological horizon. Acceleration is geometry ($1/\mathrm{length}$) dressed by $c^2$ — the first rung of [[the-saturation-ladder|the ladder]].

## The Einstein form

For a small ball of test particles initially at relative rest, the full Einstein equation is equivalent to

$$
\frac{\ddot V}{V}\Big|_{t=0}
=-4\pi G\Bigl(\rho+\frac{3p}{c^2}\Bigr),
$$

the volume-acceleration form (Baez and Bunn, Am. J. Phys. **73**, 644 (2005); the timelike-congruence Raychaudhuri identity). Every element of the intuition being chased is present exactly: a second time derivative (acceleration), of a volume ($\mathrm{m^3}$), per volume, sourced by mass — with time squared in the denominator. Gravity is the *volume response of the arena to density*, and $G$ is the response coefficient — the same compliance typing as [[deriving-value-of-g/capacity-identities|the capacity identities]] and [[deriving-g-v2/the-g-free-first-law|the presentation reading]], reached here with no thermodynamics at all.

## The typed boundary

Neither form derives the other register's content: the flux form does not know the ledger, and the volume form does not know temperature. Their agreement on $G$ is the universality demand of [[deriving-value-of-g/causal-scale-derivation-target|the derivation target]] — any wall-derived ledger density must reproduce *these* coefficients in the Einstein regime, which is what makes the ladder a test set rather than a derivation route.

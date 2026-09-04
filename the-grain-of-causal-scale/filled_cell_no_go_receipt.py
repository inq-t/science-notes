"""Numerical receipt for the causal-grain filled-cell no-go."""

from math import pi


ELECTRONVOLT_J = 1.602_176_634e-19
MEGAPARSEC_M = 3.085_677_581_491_367_3e22
C = 299_792_458.0
G = 6.674_30e-11

LAMBDA_M = 4.264e-15
ENERGY_J = 46.27e6 * ELECTRONVOLT_J
H_SI = 83.1058e3 / MEGAPARSEC_M

CELL_DENSITY = ENERGY_J / LAMBDA_M**3
CRITICAL_DENSITY = 3.0 * H_SI**2 * C**2 / (8.0 * pi * G)
RATIO = CELL_DENSITY / CRITICAL_DENSITY

print("causal-grain filled-cell no-go receipt")
print(f"cell energy density:     {CELL_DENSITY:.12e} J m^-3")
print(f"critical energy density: {CRITICAL_DENSITY:.12e} J m^-3")
print(f"density ratio:           {RATIO:.12e}")

assert 9.55e31 < CELL_DENSITY < 9.58e31
assert 1.16e-9 < CRITICAL_DENSITY < 1.18e-9
assert 8.19e40 < RATIO < 8.22e40
print("all checks passed")


"""Finite checks for the Delta+(3,4,infinity) cusp-character theorem."""

from fractions import Fraction
from math import gcd


def order_mod_12(k: int) -> int:
    """Multiplicative order of exp(2*pi*i*k/12)."""
    k %= 12
    return 1 if k == 0 else 12 // gcd(k, 12)


rows: list[tuple[int, int, int, Fraction, int]] = []
for r in range(3):
    for s in range(4):
        # c=(ab)^-1, so the exponent is -(r/3+s/4) modulo one.
        p_mod_12 = (-4 * r - 3 * s) % 12
        distance = min(Fraction(p_mod_12, 12), 1 - Fraction(p_mod_12, 12))
        rows.append((r, s, p_mod_12, distance, order_mod_12(p_mod_12)))

trivial_cusp = [(r, s) for r, s, k, _, _ in rows if k == 0]
assert trivial_cusp == [(0, 0)]

nontrivial_distances = [distance for r, s, _, distance, _ in rows if (r, s) != (0, 0)]
assert min(nontrivial_distances) == Fraction(1, 12)

# The signed and same-sign gluing choices both give primitive cusp characters.
p_signed = 12 * 0 - 4 * 1 - 3 * (-1)
p_same = 12 * 0 - 4 * 1 - 3 * 1
assert p_signed == -1 and order_mod_12(p_signed) == 12
assert p_same == -7 and order_mod_12(p_same) == 12

# Orbifold Euler characteristic and commutator-cover topology.
orbifold_euler = Fraction(1, 3) + Fraction(1, 4) - 1
cover_degree = 12
cover_euler = cover_degree * orbifold_euler
cusp_count = cover_degree // order_mod_12(p_signed)
genus = (2 - cusp_count - cover_euler) // 2
assert orbifold_euler == Fraction(-5, 12)
assert cover_euler == -5
assert cusp_count == 1
assert genus == 3

print("TRIANGLE_CHARACTER_COUNT=12")
print(f"TRIVIAL_CUSP_CHARACTERS={trivial_cusp}")
print(f"MIN_NONTRIVIAL_CUSP_PHASE_DISTANCE={min(nontrivial_distances)}")
print(f"SIGNED_DEFECT={p_signed}; SIGNED_CUSP_ORDER={order_mod_12(p_signed)}")
print(f"SAME_SIGN_DEFECT={p_same}; SAME_SIGN_CUSP_ORDER={order_mod_12(p_same)}")
print(f"ORBIFOLD_EULER={orbifold_euler}")
print(f"COMMUTATOR_COVER_EULER={cover_euler}")
print(f"COMMUTATOR_COVER_CUSPS={cusp_count}")
print(f"COMMUTATOR_COVER_GENUS={genus}")
print("ALL_FINITE_CHECKS_PASSED")

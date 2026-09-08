"""Finite checks for the C12 regular augmentation descent carrier."""

from math import gcd


ORDER = 12


def orbit_count(shift: int) -> int:
    """Number of orbits of translation by shift on Z/12."""
    return gcd(ORDER, shift % ORDER)


rows: list[tuple[int, int, int]] = []
for shift in range(ORDER):
    regular_fixed_dimension = orbit_count(shift)
    augmentation_fixed_dimension = regular_fixed_dimension - 1
    rows.append((shift, regular_fixed_dimension, augmentation_fixed_dimension))

generators = [shift for shift, _, aug_dim in rows if aug_dim == 0]
assert generators == [1, 5, 7, 11]

# The regular representation of a generator has all twelfth roots once;
# removing the constant line leaves precisely the eleven nontrivial phases.
fourier_exponents = list(range(1, ORDER))
assert len(fourier_exponents) == 11
assert 0 not in fourier_exponents

# Inverting the generator permutes the nontrivial Fourier spectrum.
inverted_exponents = sorted((-k) % ORDER for k in fourier_exponents)
assert inverted_exponents == fourier_exponents

# The two winding examples select primitive line-character phases, while the
# augmentation carrier itself is canonical and contains all nontrivial phases.
p_signed = -1 % ORDER
p_same = -7 % ORDER
assert p_signed in generators and p_same in generators

print(f"DECK_GROUP_ORDER={ORDER}")
print(f"AUGMENTATION_DIMENSION={ORDER - 1}")
print(f"GENERATOR_SHIFTS_WITH_ZERO_AUGMENTATION_FIXED_SPACE={generators}")
print(f"GENERATOR_REGULAR_FIXED_DIMENSION={rows[1][1]}")
print(f"GENERATOR_AUGMENTATION_FIXED_DIMENSION={rows[1][2]}")
print(f"NONTRIVIAL_FOURIER_EXPONENTS={fourier_exponents}")
print("ORIENTATION_REVERSAL_PRESERVES_PHASE_SET=True")
print(f"SIGNED_PHASE_EXPONENT={p_signed}; SAME_SIGN_PHASE_EXPONENT={p_same}")
print("ALL_AUGMENTATION_CHECKS_PASSED")

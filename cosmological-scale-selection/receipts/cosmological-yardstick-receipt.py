from fractions import Fraction
from math import exp, isclose, log, pi, sqrt


# Dimension vectors are ordered as (mass, length, time, temperature).
M = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
E = (Fraction(1), Fraction(2), Fraction(-2), Fraction(0))
c = (Fraction(0), Fraction(1), Fraction(-1), Fraction(0))
G = (Fraction(-1), Fraction(3), Fraction(-2), Fraction(0))
hbar = (Fraction(1), Fraction(2), Fraction(-1), Fraction(0))
H = (Fraction(0), Fraction(0), Fraction(-1), Fraction(0))
k_B = (Fraction(1), Fraction(2), Fraction(-2), Fraction(-1))
temperature = (Fraction(0), Fraction(0), Fraction(0), Fraction(1))


def add(*vectors):
    return tuple(sum(entries, Fraction(0)) for entries in zip(*vectors))


def scale(power, vector):
    return tuple(power * entry for entry in vector)


def sub(left, right):
    return add(left, scale(Fraction(-1), right))


assert add(hbar, H) == E
assert sub(scale(5, c), add(G, H)) == E
assert add(k_B, temperature) == E
assert add(G, hbar, scale(2, H), scale(-5, c)) == (0, 0, 0, 0)

# E_*^3 = const * hbar^2 c^5 H / G.
assert add(scale(2, hbar), scale(5, c), H, scale(-1, G)) == scale(3, E)

# m_*^3 = const * hbar^2 H / (G c).
assert add(scale(2, hbar), H, scale(-1, G), scale(-1, c)) == scale(3, M)

# E_A = c^5/(2 G H), and iota is dimensionless.
assert sub(scale(5, c), add(G, H)) == E

# Algebraic coefficient check:
# [(6 pi^2)/(gamma s)] * [E_A^3 / iota^2]
# = [3/(4 gamma s)] * hbar^2 c^5 H/G.
# After cancelling 1/(gamma s), both sides have rational coefficient 3/4;
# pi cancels through iota^2.
assert Fraction(6, 1) * Fraction(1, 8) == Fraction(3, 4)

# With an equal-volume three-ball, cubing the Longo shape coefficient and
# multiplying by the whole-capacity coefficient cancels all powers of pi:
# [(4 pi/3)/(8 pi^3)] * [6 pi^2/(gamma s)] = 1/(gamma s).
assert Fraction(4, 3) * Fraction(6, 1) / Fraction(8, 1) == Fraction(1, 1)

# A selected logarithmic depth fixes capacity, absolute Hubble normalization,
# and the candidate energy consistently. Set c=G=hbar=1 for this coefficient check.
for gamma, cell_weight, sigma in ((2.0, 1.0, 4.0), (1.3, 0.8, 7.25)):
    capacity = 4 * gamma * cell_weight * pi * exp(3 * sigma) / 3
    hubble = sqrt(3 / (4 * gamma * cell_weight)) * exp(-3 * sigma / 2)
    energy_from_rate = hubble * exp(sigma)
    energy_from_planck = (
        sqrt(3 / (4 * gamma * cell_weight)) * exp(-sigma / 2)
    )
    assert isclose(capacity, pi / hubble**2, rel_tol=2e-14)
    assert isclose(energy_from_rate, energy_from_planck, rel_tol=2e-14)

# The two-boundary mint law is the same normalization in integral form.
gamma = 2.0
cell_weight = 1.0
for ledger_depth in (3.0, 17.5, 281.31):
    capacity = exp(ledger_depth)
    hubble = sqrt(pi) * exp(-ledger_depth / 2)
    sigma = (ledger_depth + log(3 / (4 * gamma * cell_weight * pi))) / 3
    assert isclose(capacity, pi / hubble**2, rel_tol=2e-14)
    assert isclose(
        sigma,
        log((3 * capacity / (4 * gamma * cell_weight * pi)) ** (1 / 3)),
        rel_tol=2e-14,
    )

print("COSMOLOGICAL_YARDSTICK_DIMENSIONS_PASSED")
print("WHOLE_CAPACITY_COEFFICIENT_PASSED")
print("ISOTROPIC_BALL_CANCELLATION_PASSED")
print("LOG_DEPTH_NORMALIZATION_IDENTITIES_PASSED")
print("TWO_BOUNDARY_MINT_IDENTITIES_PASSED")

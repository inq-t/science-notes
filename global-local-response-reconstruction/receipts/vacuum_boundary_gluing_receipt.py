"""Finite-state receipt for vacuum boundary gluing.

This checks that an invertible, strictly positive transfer matrix can remain
injective at every finite depth while reflected boundary amplitudes converge
projectively to the squared vacuum. It also checks the periodic-cylinder
marginal, the vacuum Doob transform, and a finite reflection-Markov example
in which conditional expectation realizes the OS quotient isometrically on
the interface. It makes no continuum Yang--Mills claim.
"""

from fractions import Fraction


def mat_vec(matrix, vector):
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(matrix))
    )


def mat_mul(left, right):
    size = len(left)
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(size))
            for j in range(size)
        )
        for i in range(size)
    )


def mat_pow(matrix, exponent):
    size = len(matrix)
    result = tuple(
        tuple(Fraction(int(i == j)) for j in range(size))
        for i in range(size)
    )
    factor = matrix
    power = exponent
    while power:
        if power % 2:
            result = mat_mul(result, factor)
        factor = mat_mul(factor, factor)
        power //= 2
    return result


def normalize_squares(vector):
    denominator = sum(value * value for value in vector)
    return tuple(value * value / denominator for value in vector)


def total_variation(left, right):
    return sum(abs(x - y) for x, y in zip(left, right, strict=True)) / 2


vacuum = (Fraction(4, 5), Fraction(3, 5))
excited = (Fraction(-3, 5), Fraction(4, 5))
r = Fraction(1, 4)

# T=P_vac+r P_exc has eigenvalues 1 and r, positive entries, and det(T)=r.
transfer = (
    (Fraction(73, 100), Fraction(9, 25)),
    (Fraction(9, 25), Fraction(13, 25)),
)

assert mat_vec(transfer, vacuum) == vacuum
assert mat_vec(transfer, excited) == tuple(r * value for value in excited)
assert transfer[0][0] * transfer[1][1] - transfer[0][1] ** 2 == r
assert all(entry > 0 for row in transfer for entry in row)

vacuum_law = tuple(value * value for value in vacuum)
boundary = (Fraction(1), Fraction(0))
previous_tv = Fraction(1)

for depth in range(1, 7):
    amplitude = mat_vec(mat_pow(transfer, depth), boundary)
    sewn_law = normalize_squares(amplitude)
    tv = total_variation(sewn_law, vacuum_law)
    assert tv < previous_tv
    previous_tv = tv

    even_power = mat_pow(transfer, 2 * depth)
    trace = even_power[0][0] + even_power[1][1]
    periodic_law = (even_power[0][0] / trace, even_power[1][1] / trace)
    expected_periodic = tuple(
        (vacuum[i] ** 2 + r ** (2 * depth) * excited[i] ** 2)
        / (1 + r ** (2 * depth))
        for i in range(2)
    )
    assert periodic_law == expected_periodic

# The vacuum Doob transform is stochastic and reversible for psi_0^2.
doob = tuple(
    tuple(transfer[i][j] * vacuum[j] / vacuum[i] for j in range(2))
    for i in range(2)
)
assert all(sum(row) == 1 for row in doob)
assert vacuum_law[0] * doob[0][1] == vacuum_law[1] * doob[1][0]


# Reflection-Markov receipt.  The interface label is fixed by reflection, and
# the negative and positive variables are conditionally independent copies
# with the following laws given interface i.
interface_law = (Fraction(2, 5), Fraction(3, 5))
conditional = (
    (Fraction(1, 3), Fraction(2, 3)),
    (Fraction(3, 4), Fraction(1, 4)),
)


def boundary_map(observable):
    return tuple(
        sum(
            conditional[i][x] * observable[i][x]
            for x in range(2)
        )
        for i in range(2)
    )


def interface_inner(left, right):
    return sum(
        interface_law[i] * left[i] * right[i]
        for i in range(2)
    )


def os_inner(left, right):
    # Reflection sends the positive observable to the conditionally
    # independent negative copy.  Values are real in this receipt.
    return sum(
        interface_law[i]
        * sum(conditional[i][y] * left[i][y] for y in range(2))
        * sum(conditional[i][x] * right[i][x] for x in range(2))
        for i in range(2)
    )


basis = (
    ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0))),
    ((Fraction(0), Fraction(1)), (Fraction(0), Fraction(0))),
    ((Fraction(0), Fraction(0)), (Fraction(1), Fraction(0))),
    ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(1))),
)
for left in basis:
    for right in basis:
        assert os_inner(left, right) == interface_inner(
            boundary_map(left), boundary_map(right)
        )

# A conditionally mean-zero function is OS-null.
null_observable = (
    (Fraction(2), Fraction(-1)),
    (Fraction(1), Fraction(-3)),
)
assert boundary_map(null_observable) == (0, 0)
assert os_inner(null_observable, null_observable) == 0

# Interface insertions are fixed by the boundary map.  An insertion centered
# against the distinguished constant reference line therefore has exact
# coverage one; this finite Markov receipt does not identify that line with a
# unique Hamiltonian vacuum.
centered_interface = (Fraction(3), Fraction(-2))
assert sum(
    interface_law[i] * centered_interface[i]
    for i in range(2)
) == 0
centered_insertion = tuple(
    (centered_interface[i], centered_interface[i])
    for i in range(2)
)
assert boundary_map(centered_insertion) == centered_interface
assert os_inner(centered_insertion, centered_insertion) == interface_inner(
    centered_interface, centered_interface
)

print("transfer determinant:", transfer[0][0] * transfer[1][1] - transfer[0][1] ** 2)
print("finite transfer is injective:", True)
print("vacuum law:", tuple(str(value) for value in vacuum_law))
print("depth-6 sewn total-variation error:", str(previous_tv))
print("Doob row sums:", tuple(str(sum(row)) for row in doob))
print("reflection-Markov OS factorization on basis:", True)
print("OS null equals boundary-map kernel in receipt:", True)
print("reference-complement interface coverage:", "1")
print("all vacuum boundary-gluing receipts passed")

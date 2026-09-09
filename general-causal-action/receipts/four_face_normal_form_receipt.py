"""Exact four-face first normal form and all ten invariant quadratic lifts.

Reuses the twelve raw comb rows and an independently assembled Hermite model.
All arithmetic is rational or in Q(sqrt(2),sqrt(3)); no sampled dynamics,
numerical spectrum, package installation, or finite spectral approximation.
"""
from fractions import Fraction as F
from itertools import combinations, permutations

from four_face_cubic_response_receipt import raw_rows
from four_face_nonlinear_receipt import Model, Q, add, cross, scaled


def solve(matrix, rhs):
    a = [list(map(F, row)) + [F(y)] for row, y in zip(matrix, rhs)]
    for k in range(len(rhs)):
        pivot = next(i for i in range(k, len(rhs)) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        z = a[k][k]
        a[k] = [x / z for x in a[k]]
        for i in range(len(rhs)):
            if i != k:
                z = a[i][k]
                a[i] = [x - z * y for x, y in zip(a[i], a[k])]
    return [row[-1] for row in a]


def coefficient_tables():
    O = [[F(x, 2) for x in row] for row in
         ((1, 1, 1, 1), (1, -1, 1, -1),
          (1, 1, -1, -1), (1, -1, -1, 1))]
    rows = []
    for _, s, z in raw_rows()[1]:
        sm = [sum(O[p][mu] * s[p] for p in range(4))
              for mu in range(4)]
        zm = [[sum(O[p][mu] * z[p][q] * O[q][nu]
                   for p in range(4) for q in range(4))
               for nu in range(4)] for mu in range(4)]
        rows.append((sm, zm))

    def v(lam, j, k):
        return 2 * sum(s[k] * z[j][lam] - s[j] * z[k][lam]
                       for s, z in rows)

    squared = [2, 4, 4, 6]
    triples, repeated = {}, {}
    for i, j, k in combinations(range(4), 3):
        values = [v(i, j, k), v(j, k, i), v(k, i, j)]
        matrix = [
            [0, 2 * squared[k], 2 * squared[j], F(1, 2)],
            [2 * squared[k], 0, 2 * squared[i], F(1, 2)],
            [2 * squared[j], 2 * squared[i], 0, F(1, 2)],
            [1, 1, 1, 0],
        ]
        solution = solve(matrix, values + [0])
        for row, target in zip(matrix, values + [0]):
            assert sum(x * y for x, y in zip(row, solution)) == target
        triples[i, j, k] = (tuple(values), tuple(solution))
    for i, j in combinations(range(4), 2):
        ci, cj = v(i, i, j), v(j, i, j)
        ui, uj = -ci / (2 * squared[j]), -cj / (2 * squared[i])
        assert 2 * squared[j] * ui == -ci
        assert 2 * squared[i] * uj == -cj
        repeated[i, j] = ((ci, cj), (ui, uj))
    expected_v = [(0, -1, 0), (3, -3, -1), (-1, 1, -1), (-1, 2, -2)]
    expected_s = [
        (F(-1, 28), F(1, 7), F(-3, 28), F(-4, 7)),
        (F(-1, 4), F(1, 4), 0, 0),
        (0, F(-1, 4), F(1, 4), 0),
        (0, F(-1, 4), F(1, 4), 0),
    ]
    assert [data[0] for data in triples.values()] == expected_v
    assert [data[1] for data in triples.values()] == expected_s
    assert [data[0] for data in repeated.values()] == [
        (-3, 1), (1, 0), (0, 0), (1, 1), (-1, 1), (-2, 1)]
    return triples, repeated


def main():
    triples, repeated = coefficient_tables()
    model = Model(2)
    vac = {model.zero: Q(1)}
    Y = [[{(3 * i + a,): Q(1)} for a in range(3)] for i in range(4)]
    field = [{} for _ in range(12)]
    thirds = []

    def insert(i, j, k, value):
        for a, component in enumerate(cross(Y[j], Y[k])):
            field[3 * i + a] = add(field[3 * i + a], component, value)

    for (i, j, k), (_, (ai, aj, ak, b)) in triples.items():
        insert(i, j, k, ai)
        insert(j, k, i, aj)
        insert(k, i, j, ak)
        if b:
            thirds.append((i, j, k, b))
    for (i, j), (_, (ui, uj)) in repeated.items():
        insert(i, i, j, ui)
        insert(j, i, j, uj)

    def derivative(p, coordinate):
        return add(model.derivative(p, coordinate), model.y(p, coordinate),
                   -1 / (2 * model.w[coordinate // 3]))

    def S(p):
        result = model.row(field, p)
        for i, j, k, coefficient in thirds:
            for a, b, c in permutations(range(3)):
                sign = (-1) ** ((a > b) + (a > c) + (b > c))
                term = derivative(derivative(derivative(p, 3*k+c),
                                             3*j+b), 3*i+a)
                result = add(result, term, coefficient * sign)
        return result

    def multiply_quadratic(p, i, j):
        result = {}
        for a in range(3):
            result = add(result, model.y(model.y(p, 3*i+a), 3*j+a))
        return result

    def triple_vector(i, j, k):
        result = {}
        for a, b, c in permutations(range(3)):
            sign = (-1) ** ((a > b) + (a > c) + (b > c))
            n = list(model.zero)
            n[3*i+a] += 1
            n[3*j+b] += 1
            n[3*k+c] += 1
            result[tuple(n)] = Q(sign)
        return result

    target_triples = [triple_vector(*I) for I in triples]
    q = lambda a=0, b=0: Q(F(a), F(b))
    expected_lifts = [
        [q(F(-1,7)), q(F(-1,2)), q(), q()],
        [q(), q(F(1,12)), q(), q()],
        [q(F(1,4)), q(F(1,4)), q(F(1,6)), q(F(1,4))],
        [q(F(1,4)), q(F(1,4)), q(F(-1,4)), q(F(-1,14))],
        [q(F(2,7),F(-1,14)), q(F(1,2)), q(), q()],
        [q(F(-1,4)), q(F(-1,4)), q(F(1,4)), q(F(1,12))],
        [q(F(-1,4)), q(F(-1,4)), q(F(-1,7),F(1,28)), q(F(-1,4))],
        [q(F(-3,14),F(-1,14)), q(), q(F(-1,2)), q(F(-1,2))],
        [q(), q(F(-3,28),F(-1,28)), q(), q()],
        [q(), q(), q(F(1,2)), q(F(1,2))],
    ]
    tests = [vac] + [model.y(vac, a) for a in range(12)]
    pairs = [(i, j) for i in range(4) for j in range(i, 4)]
    for index, (i, j) in enumerate(pairs):
        source = multiply_quadratic(vac, i, j)
        tests.append(source)
        lift = add(S(source), multiply_quadratic(S(vac), i, j), -1)
        expected = {}
        for coefficient, vector in zip(expected_lifts[index], target_triples):
            expected = add(expected, vector, coefficient)
        assert lift == expected, (i, j, lift, expected)
        print("D(Y_%d dot Y_%d):" % (i, j), expected_lifts[index])
    for p in tests:
        commutator = add(model.K(S(p)), S(model.K(p)), -1)
        assert not add(commutator, model.H1(p)), "Raw Hermite commutator failed"
    assert S(vac) == scaled(model.inv(model.H1(vac)), -1)
    phi = model.f(vac)
    assert S(phi) == scaled(model.inv(model.H1(phi), 2*model.w[0]), -1)
    for I, data in triples.items():
        print("Distinct:", I, data)
    for I, data in repeated.items():
        print("Repeated:", I, data)
    print("PASS: all 24 raw coefficients, rational commutator systems,")
    print("vacuum plus 12 colored plus 10 quadratic Hermite checks,")
    print("all ten universal lifts, and both known first eigenvector correctors.")


if __name__ == "__main__":
    main()

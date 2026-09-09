"""Exact comb-row cubic response on the complete four-face oscillator carrier.

Only rational arithmetic in Q(sqrt(2),sqrt(3)) is used.  The alternating
three-mode channels and their degree-five radial partners are an exact
closure of the specified order, not a numerical spectral truncation.
"""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations

from corner_hamiltonian_spin_receipt import Rad


def reciprocal(value):
    """Inverse in Q(sqrt(2),sqrt(3)) by its three Galois conjugates."""
    if not isinstance(value, Rad):
        return Rad(1 / Q(value))
    assert value and set(value.d) <= {1, 2, 3, 6}
    others = []
    for sign2, sign3 in [(-1, 1), (1, -1), (-1, -1)]:
        others.append(Rad.terms({
            sf: c * (sign2 if sf in (2, 6) else 1)
            * (sign3 if sf in (3, 6) else 1)
            for sf, c in value.d.items()
        }))
    numerator = others[0] * others[1] * others[2]
    denominator = (value * numerator).rational()
    return numerator / denominator


def divide(a, b):
    return a * reciprocal(b)


def parity(seq):
    return (-1) ** sum(x > y for i, x in enumerate(seq)
                       for y in seq[i + 1:])


def raw_rows():
    """Return FJ13 as rational face arrays (s_p, z_pq), one per raw edge."""
    faces = [(1, 1), (2, 1), (1, 2), (2, 2)]
    index = {p: i for i, p in enumerate(faces)}
    rows = []

    def empty():
        return defaultdict(Q), defaultdict(lambda: defaultdict(Q))

    def append(name, s, z):
        rows.append((name, [s[p] for p in range(4)],
                     [[z[p][q] for q in range(4)] for p in range(4)]))

    for i in range(1, 3):
        for j in range(1, 3):
            s, z = empty()
            p = index[i, j]
            s[p] -= 1
            z[p][p] -= Q(1, 2)
            if j < 2:
                p = index[i, j + 1]
                s[p] += 1
                z[p][p] -= Q(1, 2)
            append(("horizontal", i, j), s, z)
    for i in range(1, 3):
        s, z = empty()
        p = index[i, 1]
        s[p] += 1
        z[p][p] -= Q(1, 2)
        for col in range(i + 1, 3):
            for j in range(1, 3):
                p = index[col, j]
                z[p][p] -= 1
        append(("bottom", i), s, z)
    for col in range(3):
        for j in range(1, 3):
            s, z = empty()
            if col:
                p = index[col, j]
                s[p] += 1
                z[p][p] -= Q(1, 2)
                for k in range(1, j):
                    z[p][index[col, k]] -= 1
            if col < 2:
                p = index[col + 1, j]
                s[p] -= 1
                z[p][p] -= Q(1, 2)
                for k in range(j + 1, 3):
                    p = index[col + 1, k]
                    z[p][p] -= 1
            append(("vertical", col, j), s, z)
    assert len(rows) == 12
    return faces, rows


def main():
    faces, rows = raw_rows()
    O = [[Q(x, 2) for x in row] for row in
         [(1, 1, 1, 1), (1, -1, 1, -1),
          (1, 1, -1, -1), (1, -1, -1, 1)]]
    omega = [Rad.sqrt(2), Rad(2), Rad(2), Rad.sqrt(6)]
    precision = [reciprocal(2 * w) for w in omega]
    c = 2 * omega[0]
    root6 = Rad.sqrt(6)
    radial_three = divide(Rad(2), root6)
    source_gradient = divide(Rad(2), root6 * omega[0])
    mode_rows = []
    for name, s, z in rows:
        sm = [sum(O[p][mu] * s[p] for p in range(4))
              for mu in range(4)]
        zm = [[sum(O[p][mu] * z[p][q] * O[q][nu]
                   for p in range(4) for q in range(4))
               for nu in range(4)] for mu in range(4)]
        mode_rows.append((name, sm, zm))

    # The same raw rows recover PP's full incidence kinetic matrix.
    for mu in range(4):
        for nu in range(4):
            value = sum(s[mu] * s[nu] for _, s, _ in mode_rows)
            assert Rad(value) == (omega[mu] ** 2 if mu == nu else 0)

    channels = {}
    virtual_vacuum = Rad()
    virtual_excited = Rad()
    leakage_norm = Rad()
    leakage_susceptibility = Rad()
    for triple in combinations(range(4), 3):
        a, b = Rad(), Rad()
        for _, s, z in mode_rows:
            for nu, mu, lam in permutations(triple):
                a += (-2 * parity((nu, mu, lam)) * s[nu] * z[mu][lam]
                      * precision[nu] * precision[mu])
            if 0 in triple:
                others = [i for i in triple if i]
                for mu, lam in permutations(others):
                    b += (2 * source_gradient * s[0] * precision[mu]
                          * z[mu][lam] * parity((0, mu, lam)))
                for nu, lam in permutations(others):
                    b += (2 * source_gradient * z[0][lam] * s[nu]
                          * precision[nu] * parity((nu, 0, lam)))
        energy = sum((omega[i] for i in triple), Rad())
        norm = 6 * omega[triple[0]] * omega[triple[1]] * omega[triple[2]]
        qnorm_ratio = Q(5, 3) if 0 in triple else Q(1)
        three = radial_three if 0 in triple else Rad()
        a3 = a * three + b
        ell = divide(a3, energy - c) - divide(a * three, energy)
        vacuum_piece = divide(norm * a * a, energy)
        excited_piece = (divide(norm * a3 * a3, energy - c)
                         + divide(norm * qnorm_ratio * a * a, energy))
        norm_piece = norm * ell * ell
        susceptibility_piece = norm_piece * (reciprocal(energy) - reciprocal(c))
        channels[triple] = (a, b, energy, norm, a3, ell)
        virtual_vacuum += vacuum_piece
        virtual_excited += excited_piece
        leakage_norm += norm_piece
        leakage_susceptibility += susceptibility_piece
        print("channel", triple)
        print("  a =", a)
        print("  b =", b)
        print("  energy =", energy, "; norm =", norm)
        print("  excited cubic =", a3)
        print("  ell =", ell)
        print("  norm contribution =", norm_piece)
        print("  susceptibility contribution =", susceptibility_piece)
    assert channels[(1, 2, 3)][1] == 0
    assert channels[(1, 2, 3)][5] == 0
    root2, root3 = Rad.sqrt(2), Rad.sqrt(3)
    expected_a = [
        -root2 / 16,
        -root2 / 16 - root3 / 8 + root6 / 16,
        -root2 / 16 + root3 / 24 - root6 / 48,
        -Rad(1) / 8 + root6 / 48,
    ]
    expected_b = [
        root3 / 12, root2 / 4 + root3 / 12,
        -root2 / 12 + root3 / 12, Rad(),
    ]
    expected_ell = [root3 / 42, root3 / 12, Rad(), Rad()]
    for i, data in enumerate(channels.values()):
        assert data[0] == expected_a[i]
        assert data[1] == expected_b[i]
        assert data[5] == expected_ell[i]
    assert virtual_vacuum == (-Rad(117) / 56 + 111 * root2 / 112
                              + root3 / 8 + 5 * root6 / 16)
    assert virtual_excited == (-Rad(117) / 56 + 37 * root2 / 16
                               + 7 * root3 / 24 + 5 * root6 / 16)
    assert virtual_vacuum - virtual_excited == -37 * root2 / 28 - root3 / 6
    assert leakage_norm == 2 * root2 / 49 + root3 / 2
    assert leakage_susceptibility == (-Rad(1101) / 2744
                                     + 4 * root2 / 343 + root3 / 8)
    print("virtual vacuum =", virtual_vacuum)
    print("virtual excitation =", virtual_excited)
    print("virtual gap contribution =", virtual_vacuum - virtual_excited)
    print("leakage norm =", leakage_norm)
    print("leakage susceptibility =", leakage_susceptibility)
    print("Exact raw-row, mode-spectrum, cubic-channel, resolvent, "
          "leakage and virtual-energy checks passed.")


if __name__ == "__main__":
    main()

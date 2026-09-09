"""Exact first-odd-jet resonance test on the 5 by 5 planar patch.

This is a finite rational/radical contraction of the FJ/AJ comb rows,
not a simulation or a numerical spectral truncation.  The field helper
uses exact Fraction arithmetic; no floating-point sign test is used.
"""
from fractions import Fraction as Q

from corner_hamiltonian_spin_receipt import Rad


def raw_rows(L):
    """FJ/AJ arrays: h Z_e = sum s_ep d_p + h sum z_epq [x_q,T].d_p."""
    rows = []

    def inc(d, key, value):
        d[key] = d.get(key, Q(0)) + value

    for i in range(1, L + 1):
        for j in range(1, L + 1):
            s, z = {}, {}
            inc(s, (i, j), -1)
            inc(z, ((i, j), (i, j)), -Q(1, 2))
            if j < L:
                inc(s, (i, j + 1), 1)
                inc(z, ((i, j + 1), (i, j + 1)), -Q(1, 2))
            rows.append((("horizontal", i, j), s, z))
    for i in range(1, L + 1):
        s, z = {}, {}
        inc(s, (i, 1), 1)
        inc(z, ((i, 1), (i, 1)), -Q(1, 2))
        for col in range(i + 1, L + 1):
            for j in range(1, L + 1):
                inc(z, ((col, j), (col, j)), -1)
        rows.append((("bottom", i), s, z))
    for col in range(L + 1):
        for j in range(1, L + 1):
            s, z = {}, {}
            if col:
                inc(s, (col, j), 1)
                inc(z, ((col, j), (col, j)), -Q(1, 2))
                for k in range(1, j):
                    inc(z, ((col, j), (col, k)), -1)
            if col < L:
                inc(s, (col + 1, j), -1)
                inc(z, ((col + 1, j), (col + 1, j)), -Q(1, 2))
                for k in range(j + 1, L + 1):
                    inc(z, ((col + 1, k), (col + 1, k)), -1)
            rows.append((("vertical", col, j), s, z))
    assert len(rows) == 2 * L * (L + 1)
    return rows


def sign_qsqrt3(x):
    """Exact sign of an element of Q(sqrt(3))."""
    assert set(x.d) <= {1, 3}
    a, b = x.d.get(1, Q(0)), x.d.get(3, Q(0))
    if a >= 0 and b >= 0:
        return 1 if a or b else 0
    if a <= 0 and b <= 0:
        return -1
    if a > 0:
        return 1 if a * a > 3 * b * b else -1
    return 1 if 3 * b * b > a * a else -1


def main():
    L, root3 = 5, Rad.sqrt(3)
    # sin(k*pi/6), k modulo 12.
    sine = [Rad(0), Rad(Q(1, 2)), root3 / 2, Rad(1),
            root3 / 2, Rad(Q(1, 2)), Rad(0), Rad(-Q(1, 2)),
            -root3 / 2, Rad(-1), -root3 / 2, Rad(-Q(1, 2))]
    twice_cos = [None, root3, Rad(1), Rad(0), Rad(-1), -root3]
    faces = [(i, j) for j in range(1, L + 1)
             for i in range(1, L + 1)]
    middle = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
    low, high = (1, 1), (5, 5)
    modes = [low] + middle + [high]
    # Unit sine basis: 2/(L+1) sin(mu*pi*i/(L+1)) sin(nu*pi*j/(L+1)).
    O = {m: {p: sine[m[0] * p[0] % 12]
                  * sine[m[1] * p[1] % 12] / 3
             for p in faces} for m in modes}
    omega = {low: root3 - 1, high: root3 + 1,
             **{m: Rad(2) for m in middle}}
    rows = raw_rows(L)

    # Check the complete raw incidence metric before selecting any modes.
    for p in faces:
        for q in faces:
            value = sum(s.get(p, Q(0)) * s.get(q, Q(0))
                        for _, s, _ in rows)
            target = (4 if p == q else
                      -1 if abs(p[0] - q[0]) + abs(p[1] - q[1]) == 1
                      else 0)
            assert value == target
    mode_rows = []
    for name, s, z in rows:
        sm = {m: sum((v * O[m][p] for p, v in s.items()), Rad())
              for m in modes}
        zm = {(m, n): sum((v * O[m][p] * O[n][q]
                           for (p, q), v in z.items()), Rad())
              for m in modes for n in modes}
        mode_rows.append((name, sm, zm))
    for m in modes:
        for n in modes:
            assert sum((O[m][p] * O[n][p] for p in faces), Rad()) == (
                Rad(1) if m == n else Rad())
            value = sum((s[m] * s[n] for _, s, _ in mode_rows), Rad())
            assert value == (omega[m] ** 2 if m == n else Rad())

    # V1 = v_a T(Y_a,d_b,d_c) + cyclic terms.
    expected = {
        (1, 5): ((3 - root3) / 36, (5 - 3 * root3) / 36,
                 (-5 + 3 * root3) / 36),
        (2, 4): (Rad(), Rad(), Rad()),
        (3, 3): (Rad(), Rad(), Rad()),
        (4, 2): (Rad(), Rad(), Rad()),
        (5, 1): ((5 + 3 * root3) / 36, (-5 - 3 * root3) / 36,
                 (-3 - root3) / 36),
    }
    for b in middle:
        a, c = low, high
        coeff = tuple(sum((2 * (s[k] * z[j, i] - s[j] * z[k, i])
                           for _, s, z in mode_rows), Rad())
                      for i, j, k in [(a, b, c), (b, c, a), (c, a, b)])
        assert coeff == expected[b]
        # The a_a^dagger a_b^dagger a_c coefficient is
        # N / (4 sqrt(omega_a omega_b omega_c)).
        numerator = (omega[c] * coeff[2] - omega[a] * coeff[0]
                     - omega[b] * coeff[1])
        assert numerator == Rad()
        print("middle", b, "cyclic v =", tuple(map(str, coeff)),
              "resonant numerator =", numerator)

    # Exhaust every frequency class, including repeated classes. For positive
    # squared frequencies, sqrt(lc)=sqrt(la)+sqrt(lb) iff
    # d=lc-la-lb>0 and d*d=4*la*lb.
    classes = {}
    for p in faces:
        lam = Rad(4) - twice_cos[p[0]] - twice_cos[p[1]]
        assert sign_qsqrt3(lam) > 0
        key = tuple(sorted(lam.d.items()))
        classes.setdefault(key, []).append(p)
    frequency_classes = [(Rad.terms(dict(key)), ps)
                         for key, ps in classes.items()]
    assert len(frequency_classes) == 13
    resonances = []
    for i, (la, aa) in enumerate(frequency_classes):
        for lb, bb in frequency_classes[i:]:
            for lc, cc in frequency_classes:
                d = lc - la - lb
                if sign_qsqrt3(d) > 0 and d * d == 4 * la * lb:
                    resonances.append((la, lb, lc, aa, bb, cc))
    assert len(resonances) == 1
    la, lb, lc, aa, bb, cc = resonances[0]
    assert (la, lb, lc) == (4 - 2 * root3, Rad(4), 4 + 2 * root3)
    assert aa == [low] and set(bb) == set(middle) and cc == [high]
    print("Only positive-frequency triangle: omega_55=omega_11+2;"
          " all five frequency-2 channels checked.")
    print("PASS: 60 raw rows, full incidence matrix, normalized sine modes,"
          " exact cyclic coefficients, all resonant numerators,"
          " and exhaustive triangle-class check.")


if __name__ == "__main__":
    main()

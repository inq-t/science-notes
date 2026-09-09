"""Exact complete first chronological radius--orientation Gram response.

All finite Hermite blocks and raw V1 rows are retained. No simulation or
approximate spectral diagonalization is used.
"""
from fractions import Fraction as F
from four_face_nonlinear_receipt import Q, Model, add, scaled, omultiply, cross
from first_chronological_exterior_receipt import derivative, dot


def main():
    model = Model(2)
    vacuum = {model.zero: Q(1)}
    modes = [[{(3*i+a,): Q(1)} for a in range(3)] for i in range(4)]
    alpha = {}
    for triple, coefficient in [
        ((0, 1, 2), Q(-F(1, 112), F(1, 56))),
        ((0, 1, 3), Q(-F(1, 16), F(1, 16))),
        ((0, 2, 3), Q(F(1, 16), 0, 0, -F(1, 48))),
        ((1, 2, 3), Q(F(1, 16), 0, 0, -F(1, 48))),
    ]:
        i, j, k = triple
        alpha = add(alpha, dot(modes[i], cross(modes[j], modes[k])), coefficient)
    v1_vacuum = model.H1(vacuum)
    assert model.times(alpha, vacuum) == scaled(model.inv(v1_vacuum), -1)

    variance_a = sum(model.w, Q()) / 4
    f = add(dot(model.x[0], model.x[0]), {(): Q(1)}, -3*variance_a)
    g = dot(model.x[0], cross(model.x[1], model.x[2]))
    f0 = model.times(f, vacuum)
    g0 = model.times(g, vacuum)
    assert model.inner(vacuum, f0) == 0
    assert model.inner(vacuum, g0) == 0
    assert model.inner(f0, g0) == 0
    f1 = model.times(alpha, f0)
    g1 = model.times(alpha, g0)

    def blocks(vector):
        answer = {}
        for occupation, coefficient in vector.items():
            energy = model.energy(occupation).v
            answer.setdefault(energy, {})[occupation] = coefficient
        return answer

    f_blocks = blocks(f0)
    g_blocks = blocks(g0)
    f_energy = sorted(f_blocks, key=lambda e: Q(*e).approx())
    g_energy = sorted(g_blocks, key=lambda e: Q(*e).approx())
    # No equality is resolved using floats; ordering is only for display.
    assert not set(f_energy) & set(g_energy)
    coefficient = {e: model.inner(f_blocks[e], g1) for e in f_energy}
    coefficient.update({e: model.inner(f1, g_blocks[e]) for e in g_energy})
    insertion = {}
    for odd in g_energy:
        applied = model.H1(g_blocks[odd])
        for even in f_energy:
            entry = model.inner(f_blocks[even], applied)
            insertion[even, odd] = entry
            divided = entry / (Q(*odd) - Q(*even))
            coefficient[even] -= divided
            coefficient[odd] += divided

    moment0 = sum(coefficient.values(), Q())
    assert moment0 == 2 * model.inner(f1, g0)
    derivative0 = -sum((Q(*e)*a for e, a in coefficient.items()), Q())
    raw_derivative = -model.inner(f1, model.K(g0))
    raw_derivative -= model.inner(model.K(f0), g1)
    raw_derivative -= sum(insertion.values(), Q())
    assert derivative0 == raw_derivative

    # Independently use the actual positive ground-generator derivative.
    v1_g = model.H1(g0)
    l1_g = add(v1_g, model.times(g, v1_vacuum), -1)
    drift = {}
    for k in range(12):
        drift = add(drift, omultiply(derivative(alpha, k), derivative(g, k)),
                    -2*model.w[k//3]**2)
    l1_g = add(l1_g, model.times(drift, vacuum))
    function_derivative = -model.inner(f0, l1_g)
    function_derivative -= 2*model.inner(f1, model.K(g0))
    assert derivative0 == function_derivative
    expected = {
        Q(0, 2).v: Q(F(3, 14), 0, 0, -F(1, 4)),
        Q(2, 1).v: Q(0, 1, -F(5, 6)),
        Q(0, 1, 0, 1).v: Q(0, 0, F(11, 14)),
        Q(4).v: Q(F(8, 7), -F(2, 7), 0, -F(1, 3)),
        Q(2, 0, 0, 1).v: Q(0, 0, -F(11, 14), F(4, 7)),
        Q(0, 0, 0, 2).v: Q(0, -F(3, 4)),
        Q(4, 1).v: Q(F(1, 7), F(1, 28)),
        Q(2, 1, 0, 1).v: Q(0, 0, F(1, 21), F(1, 14)),
        Q(4, 0, 0, 1).v: Q(0, 0, 0, F(1, 84)),
    }
    assert set(coefficient) == set(expected)
    assert all(coefficient[e] == 6*a for e, a in expected.items())
    expected_moments = [
        Q(F(3, 2), 0, -F(11, 14), F(1, 14)),
        Q(-F(78, 7), -F(12, 7), 7),
        Q(F(400, 7), -F(319, 14), -F(38, 7), -F(51, 14)),
        Q(-F(1376, 7), -F(69, 7), 124, -15),
    ]
    for order, answer in enumerate(expected_moments):
        calculated = sum(((-Q(*e))**order*a for e, a in coefficient.items()), Q())
        assert calculated == 6*answer
    det_triple = Q(0, 1, 2, 1)
    gamma_triple = Q(9, 3, -7)/(28*det_triple)
    assert moment0 == 24*gamma_triple*variance_a*det_triple

    print("complete exponent coefficients divided by F_Q=6")
    for e in f_energy + g_energy:
        print("energy", Q(*e), "coefficient", coefficient[e]/6)
    for order in range(4):
        moment = sum(((-Q(*e))**order*a for e, a in coefficient.items()), Q())
        print("time derivative", order, "divided by F_Q", moment/6)
    print("harmonic f variance divided by d=3:", model.inner(f0, f0)/3)
    print("harmonic g variance divided by F_Q=6:", model.inner(g0, g0)/6)
    print("raw insertion table divided by F_Q=6")
    for even in f_energy:
        print("energy", Q(*even),
              [insertion[even, odd]/6 for odd in g_energy])
    print("all nine coefficients, four moments, raw-row, vacuum, and independent checks: PASS")


if __name__ == "__main__":
    main()

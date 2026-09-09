"""Exact four-face chronological exterior coefficient; no sampled dynamics.

The imported Model uses all actual raw comb rows.  Arithmetic remains in
Q(sqrt(2),sqrt(3)); polynomial degrees close exactly at the requested jet.
"""
from fractions import Fraction as F
from four_face_nonlinear_receipt import Q, Model, add, scaled, omultiply, cross


def derivative(p, k):
    out = {}
    for mon, coefficient in p.items():
        count = mon.count(k)
        if count:
            reduced = list(mon)
            reduced.remove(k)
            reduced = tuple(reduced)
            out[reduced] = out.get(reduced, Q()) + count * coefficient
    return out


def total(*polynomials):
    result = {}
    for polynomial in polynomials:
        result = add(result, polynomial)
    return result


def dot(v, w):
    return total(*(omultiply(x, y) for x, y in zip(v, w)))


def vector_add(v, w, coefficient=1):
    return [add(x, y, coefficient) for x, y in zip(v, w)]


def vector_scale(v, coefficient):
    return [scaled(x, coefficient) for x in v]


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
    first_vacuum = model.H1(vacuum)
    assert model.times(alpha, vacuum) == scaled(model.inv(first_vacuum), -1)

    def positive_first_generator(polynomial):
        """H_1 on functions, as a Hermite vector multiplied by Omega."""
        source = model.times(polynomial, vacuum)
        result = add(model.H1(source), model.times(polynomial, first_vacuum), -1)
        drift = {}
        for k in range(12):
            drift = add(drift, omultiply(derivative(alpha, k),
                                        derivative(polynomial, k)),
                        -2 * model.w[k//3]**2)
        return add(result, model.times(drift, vacuum))

    covariance = [[sum((model.V[p][i] * model.V[q][i] * model.w[i]
                       for i in range(4)), Q()) for q in range(4)] for p in range(4)]
    precision = [[sum((model.V[p][i] * model.V[q][i] / model.w[i]
                      for i in range(4)), Q()) for q in range(4)] for p in range(4)]
    x, y, z, omitted = model.x
    mean_omitted = [{}, {}, {}]
    for p in range(3):
        mean_omitted = vector_add(mean_omitted, model.x[p],
                                 -precision[3][p] / precision[3][3])
    innovation = vector_add(omitted, mean_omitted, -1)
    sigma = 1 / precision[3][3]

    # Retain S={a,b,c}. Both f and g are invariant physical scalar sources.
    f = dot(x, x)
    g = dot(x, cross(y, z))
    af = scaled(dot(x, innovation), 2 * covariance[0][3])
    w = vector_add(vector_scale(cross(y, z), covariance[0][3]),
                   cross(z, x), covariance[1][3])
    w = vector_add(w, cross(x, y), covariance[2][3])
    ag = dot(w, innovation)
    af_h = model.times(af, vacuum)
    ag_h = model.times(ag, vacuum)
    assert model.inner(vacuum, af_h) == 0
    assert model.inner(vacuum, ag_h) == 0
    assert model.inner(af_h, ag_h) == 0

    # The first conditional-projector terms land in the retained range and
    # are orthogonal to af and ag. These are the full three contributions.
    pieces = [
        model.inner(positive_first_generator(f), ag_h),
        model.inner(af_h, positive_first_generator(g)),
        2 * model.inner(model.times(alpha, af_h), ag_h),
    ]
    value = sum(pieces, Q())
    expected = [
        Q(F(612, 7), -F(510, 7), F(192, 7), -F(90, 7)),
        Q(-F(702, 7), F(774, 7), -F(558, 7), F(234, 7)),
        Q(F(1746, 7), -F(972, 7), F(702, 7), -F(648, 7)),
    ]
    assert pieces == expected
    beta = Q(F(276, 7), -F(118, 7), 8, -12)
    assert value == 6 * beta
    # Certified rational radical bounds, not a floating-point sign test.
    intervals = {
        2: (F(141421356237, 10**11), F(141421356238, 10**11)),
        3: (F(173205080756, 10**11), F(173205080757, 10**11)),
        6: (F(244948974278, 10**11), F(244948974279, 10**11)),
    }
    for radicand, (lo, hi) in intervals.items():
        assert lo * lo < radicand < hi * hi
    lower = F(276, 7) - F(118, 7) * intervals[2][1]
    lower += 8 * intervals[3][0] - 12 * intervals[6][1]
    assert lower > 0
    print("retained conditional variance:", sigma)
    for label, piece in zip(("generator f", "generator g", "vacuum density"), pieces):
        print(label + ":", piece)
    print("total SU2 coefficient:", value)
    print("coefficient divided by F_Q=6:", value / 6)
    print("certified rational lower bound for beta:", lower)
    print("leading source exterior norms:", model.inner(af_h, af_h),
          model.inner(ag_h, ag_h))
    print("exact raw-row and parity checks: PASS")


if __name__ == "__main__":
    main()

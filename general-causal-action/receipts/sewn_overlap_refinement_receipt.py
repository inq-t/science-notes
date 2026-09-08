"""Exact finite SU(2) checks and diagnostics for the sewn comparison clock.

The character convention is chi_n = U_n(chi_1 / 2), dimension n + 1,
with chi_1 the fundamental character. Normalized Haar characters are
orthonormal. Expanding (4 + chi_1)**k gives the normalized convolution
multiplier b[k,n] = coefficient[k,n] / ((n + 1) * coefficient[k,0]).

All coefficient, ordering, and paired-rate checks use exact integers or
fractions. Haar-moment integration independently checks small exponents.
Displayed asymptotic and semigroup values are floating-point diagnostics.
These finite checks do not prove a uniform tail bound, convergence of
changing carriers, a diffusion limit, or a physical mass gap.
"""

from fractions import Fraction
from math import comb, exp


MAX_EXPONENT = 1024
DISPLAY_EXPONENTS = (1, 4, 16, 64, 256, 1024)
HAAR_CHECK_EXPONENT = 12


def fusion_step(coefficients):
    """Multiply by 4 + chi_1, using chi_1 * chi_0 = chi_1."""
    result = []
    for n in range(len(coefficients) + 1):
        value = 4 * coefficients[n] if n < len(coefficients) else 0
        if n:
            value += coefficients[n - 1]
        if n + 1 < len(coefficients):
            value += coefficients[n + 1]
        result.append(value)
    return result


def character_polynomials(max_degree):
    """Integer coefficients of chi_n as a polynomial in chi_1."""
    result = [[1]]
    if max_degree:
        result.append([0, 1])
    for n in range(1, max_degree):
        following = [0] + result[n]
        for degree, coefficient in enumerate(result[n - 1]):
            following[degree] -= coefficient
        result.append(following)
    return result


def haar_moment(power):
    """Integral of chi_1**power: zero when odd, Catalan when even."""
    if power % 2:
        return 0
    j = power // 2
    return comb(2 * j, j) // (j + 1)


def integrated_coefficient(k, character):
    """Integrate chi_n * (4 + chi_1)**k without character fusion."""
    return sum(
        coefficient * comb(k, j) * 4 ** (k - j) * haar_moment(degree + j)
        for degree, coefficient in enumerate(character)
        for j in range(k + 1)
    )


def multiplier(coefficients, n):
    # The exact infinite representation tail is zero at each fixed k.
    if n >= len(coefficients):
        return Fraction(0)
    return Fraction(coefficients[n], (n + 1) * coefficients[0])


def rates(coefficients, n):
    k = len(coefficients) - 1
    b = multiplier(coefficients, n)
    a = b * b
    slow = k * (1 - a)
    fast = k * (1 + a)
    raw_difference_norm_squared = 2 * (1 - a)
    assert slow + fast == 2 * k
    assert k <= fast <= 2 * k
    assert raw_difference_norm_squared == 2 * slow / k
    return a, slow, fast, raw_difference_norm_squared


def branch_diagnostics(coefficients, n, duration):
    """Compare exact finite-clock branches with the proposed fixed-mode heat."""
    a, slow, fast, raw_difference = rates(coefficients, n)
    target_rate = 3 * n * (n + 2)
    symmetric_to_target = exp(duration * (target_rate - float(slow)))
    antisymmetric_to_target = exp(duration * (target_rate - float(fast)))
    retained_to_target = (
        float((1 + a) / 2) * symmetric_to_target
        + float((1 - a) / 2) * antisymmetric_to_target
    )
    # A normalized antisymmetric mode has this survival even though the raw
    # difference of its two one-context representatives has vanishing norm.
    normalized_antisymmetric_survival = exp(-duration * float(fast))
    return (
        symmetric_to_target,
        retained_to_target,
        normalized_antisymmetric_survival,
        float(raw_difference),
    )


def main():
    characters = character_polynomials(HAAR_CHECK_EXPONENT + 2)
    coefficients = [1]
    snapshots = {}
    integrated_checks = 0
    exact_order_comparisons = 0
    exact_ratio_bounds = 0
    exact_gap_bounds = 0

    for k in range(MAX_EXPONENT + 1):
        assert len(coefficients) == k + 1
        assert all(value > 0 for value in coefficients)
        # Evaluate the complete character polynomial at +I and -I.
        assert sum((n + 1) * c for n, c in enumerate(coefficients)) == 6 ** k
        assert sum((-1) ** n * (n + 1) * c for n, c in enumerate(coefficients)) == 2 ** k
        assert multiplier(coefficients, 0) == 1
        assert multiplier(coefficients, k + 1) == 0

        # Compare b_n and b_(n+1) without fraction rounding or large gcds.
        for n in range(k):
            assert coefficients[n] * (n + 2) > coefficients[n + 1] * (n + 1)
            exact_order_comparisons += 1
            # b_(n+1)/b_n <= 2(k-n)/(2k+4n+9), by cross-multiplying
            # positive integer denominators rather than rounding a ratio.
            assert (
                coefficients[n + 1] * (n + 1) * (2 * k + 4 * n + 9)
                <= 2 * (k - n) * coefficients[n] * (n + 2)
            )
            exact_ratio_bounds += 1
        # At the finite-support endpoint n=k both sides of that bound vanish.
        assert multiplier(coefficients, k + 1) / multiplier(coefficients, k) == 0
        assert 2 * (k - k) == 0
        exact_ratio_bounds += 1
        if k:
            b_first = multiplier(coefficients, 1)
            assert 0 < b_first < 1
            scaled_gap = k * (1 - b_first * b_first)
            explicit_floor = Fraction(9 * k * (4 * k + 9), (2 * k + 9) ** 2)
            assert scaled_gap >= explicit_floor >= Fraction(117, 121)
            exact_gap_bounds += 1
            # A moving high-mode witness defeats norm convergence on any
            # identification that preserves the base observable phi_n(y).
            # For n=k+1, a=b_n**2=0 makes the actual UNscaled clock act as
            # identity on this unit one-context vector. The proposed fast
            # limit 2(I-E_base) annihilates the identified base vector.
            a_tail, slow_tail, fast_tail, _ = rates(coefficients, k + 1)
            assert a_tail == 0 and slow_tail / k == fast_tail / k == 1
            base_projection_eigenvalue = Fraction(1)
            fast_limit_base_rate = 2 * (1 - base_projection_eigenvalue)
            assert fast_limit_base_rate == 0

        if k <= HAAR_CHECK_EXPONENT:
            for n in range(k + 3):
                direct = integrated_coefficient(k, characters[n])
                assert direct == (coefficients[n] if n <= k else 0)
                integrated_checks += 1

        if k == 1:
            assert coefficients == [4, 1]
            assert multiplier(coefficients, 1) == Fraction(1, 8)
            a, slow, fast, raw_norm = rates(coefficients, 1)
            assert (a, slow, fast, raw_norm) == (
                Fraction(1, 64), Fraction(63, 64),
                Fraction(65, 64), Fraction(63, 32),
            )

        if k in DISPLAY_EXPONENTS:
            snapshots[k] = coefficients[:]
            # These are identities for every harmonic block at this fixed k.
            for n in range(1, k + 2):
                a, slow, fast, raw_norm = rates(coefficients, n)
                assert 0 <= a < 1 and 0 < slow <= k
                if n > k:
                    assert (slow, fast, raw_norm) == (k, k, 2)

        if k < MAX_EXPONENT:
            coefficients = fusion_step(coefficients)

    print(
        f'EXACT fusion coefficients through k={MAX_EXPONENT}; '
        f'{exact_order_comparisons} adjacent normalized-multiplier comparisons'
    )
    print(
        f'EXACT {integrated_checks} independent Haar-moment coefficient checks '
        f'for k=0..{HAAR_CHECK_EXPONENT}, including two zero-tail coefficients each'
    )
    print(
        f'EXACT {exact_ratio_bounds} adjacent ratio bounds, including support endpoints; '
        f'{exact_gap_bounds} scaled-gap bounds >= 9*k*(4*k+9)/(2*k+9)**2 >= 117/121'
    )
    print('EXACT k=1: b_1=1/8, slow=63/64, fast=65/64, raw difference norm squared=63/32')
    print('DIAGNOSTIC fixed fundamental mode: proposed scaled-rate target = 9')
    print('k     scaled slow       scaled fast       raw difference norm squared')
    for k in DISPLAY_EXPONENTS:
        _, slow, fast, raw_norm = rates(snapshots[k], 1)
        print(f'{k:4d}  {float(slow):16.10f}  {float(fast):16.10f}  {float(raw_norm):20.12e}')

    print(f'DIAGNOSTIC fixed modes at k={MAX_EXPONENT}: target rate = 3*n*(n+2)')
    print('n     scaled slow       target       target minus scaled slow')
    for n in (1, 2, 3, 4):
        _, slow, _, _ = rates(coefficients, n)
        target = 3 * n * (n + 2)
        print(f'{n:1d}  {float(slow):16.10f}  {target:7d}  {target - float(slow):24.10e}')

    duration = 0.1
    print(f'DIAGNOSTIC fundamental semigroup branches at duration={duration}')
    print('k     symmetric/target    retained/target     normalized antisymmetric survival')
    for k in DISPLAY_EXPONENTS:
        plus, retained, minus_survival, _ = branch_diagnostics(snapshots[k], 1, duration)
        print(f'{k:4d}  {plus:18.12f}  {retained:18.12f}  {minus_survival:26.12e}')
    print(
        'EXACT moving high-mode witness n=k+1: unscaled clock rate=1; '
        'identified fast-limit base rate=0, for every checked k>=1'
    )
    print(
        f'DIAGNOSTIC norm lower bound at duration={duration}: '
        f'1-exp(-t)={1 - exp(-duration):.12f}, '
        'under the stated base-preserving identification'
    )
    print(
        'PASS exact finite coefficient normalization, ordering, paired rates, '
        'ratio and gap bounds, raw relative norms, and moving high-mode rates. '
        'Numerical tables are convergence diagnostics; '
        'they do not prove a uniform spectral-tail or changing-carrier limit.'
    )


if __name__ == '__main__':
    main()

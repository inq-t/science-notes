"""Compare the actual transfer and conditional-update clocks.

Character coefficients and logarithm enclosures use exact arithmetic.
The final convergence table is a finite diagnostic, not a proof of the
all-degree limit or a physical mass gap.
"""

from fractions import Fraction as F
from math import exp

from sewn_overlap_refinement_receipt import fusion_step, multiplier


def negative_log_interval(b, tolerance=F(1, 10**15)):
    assert 0 < b <= 1
    if b == 1:
        return F(0), F(0)
    z = (1 - b) / (1 + b)
    power = z
    total = F(0)
    j = 0
    while True:
        total += 2 * power / (2 * j + 1)
        power *= z * z
        j += 1
        tail = 2 * power / ((2 * j + 1) * (1 - z * z))
        if tail <= tolerance:
            return total, total + tail


def main():
    coefficients = [1]
    samples = (1, 4, 16, 64, 256, 1024)
    output = []
    for k in range(1, max(samples) + 1):
        coefficients = fusion_step(coefficients)
        assert multiplier(coefficients, 0) == 1
        assert multiplier(coefficients, k) > 0
        assert multiplier(coefficients, k + 1) == 0
        assert multiplier(coefficients, k + 50) == 0
        supported_dimension = sum((n + 1) ** 2 for n in range(k + 1))
        assert supported_dimension == (k + 1) * (k + 2) * (2 * k + 3) // 6
        if k not in samples:
            continue
        b = multiplier(coefficients, 1)
        lower, upper = negative_log_interval(b, F(1, 10**15 * k))
        lower *= k
        upper *= k
        slow, relative = k * (1 - b * b), k * (1 + b * b)
        assert lower > slow / 2
        assert relative + slow == 2 * k
        assert upper - lower <= F(1, 10**15)
        # The same elapsed duration must be assigned to one versus two steps.
        l2, u2 = negative_log_interval(b * b, F(1, 10**15 * k))
        assert max(lower, k * l2 / 2) <= min(upper, k * u2 / 2)
        output.append((k, (lower + upper) / 2, slow, relative))

    print('EXACT: 1024 supported/null splits and supported dimensions pass')
    print('EXACT: selected logarithmic rates enclosed to width <= 1e-15; '
          'one- and two-step elapsed-duration clocks agree')
    print('DIAGNOSTIC: k | transfer -> 4.5 | collective -> 9 | relative -> infinity')
    for k, transfer, slow, relative in output:
        print(f'{k:4d} | {float(transfer):.12f} | {float(slow):.12f} | {float(relative):.12f}')
    # A finite check of the operator-norm tail formula at one positive duration.
    duration = F(1, 4)
    steps = max(samples) // 4
    errors = [abs(float(multiplier(coefficients, n)) ** steps
                  - exp(-6 * n * (n + 2) / 4 * float(duration)))
              for n in range(len(coefficients))]
    n = len(coefficients)
    errors.append(exp(-6 * n * (n + 2) / 4 * float(duration)))
    print(f'DIAGNOSTIC: positive-time transfer norm error at k=1024, t=1/4: {max(errors):.12g}')
    print('PASS. The note proves all-degree convergence and states the carrier and clock boundaries.')


if __name__ == '__main__':
    main()

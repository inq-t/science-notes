"""Arithmetic receipts for the exceptional normal-holonomy note.

The script checks the 149-dimensional H-module decomposition, its three trace
indices, the central-kernel count, the exact SU(3)-color character/Wilson-action
conversion, the minimal S6 tangent response, the stable comparison with the
octonionic Jordan-frame tangent,
the induced Haar-frame floor, and the reduced oriented-flag Hessian
multiplicities.  It does not
prove Yokota's centralizer theorem, the cited F4/H tangent branching, the
Spin(8)-triality branching or O = C + C^3 under color SU(3), the
physical choice of this normal quotient or color-only member, lattice reflection
positivity, a continuum limit, or a Yang--Mills mass gap.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Multiplet:
    multiplicity: int
    su2_dimension: int
    su3_dimension: int
    charge: int

    @property
    def dimension(self) -> int:
        return self.multiplicity * self.su2_dimension * self.su3_dimension


def su2_index(dimension: int) -> Fraction:
    """Dynkin index with T(2)=1/2."""

    return Fraction(dimension * (dimension**2 - 1), 12)


def su3_index(dimension: int) -> Fraction:
    """Only the singlet and (anti)fundamental occur here."""

    if dimension == 1:
        return Fraction(0)
    if dimension == 3:
        return Fraction(1, 2)
    raise ValueError(f"unsupported SU(3) dimension {dimension}")


def record(name: str, passed: bool, detail: str) -> bool:
    print(f"{'PASS' if passed else 'FAIL'} {name}: {detail}")
    return passed


def cyclotomic_multiply(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    """Multiply a+b*w in Q[w]/(w^2+w+1)."""

    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c - b * d


def su2_tensor_dimensions(left: int, right: int) -> range:
    """Dimensions occurring once in the tensor product of two SU(2) irreps."""

    return range(abs(left - right) + 1, left + right, 2)


def main() -> None:
    checks: list[bool] = []

    fixed_dimension = 9
    rotating_complex_dimension = 9
    real_trace_w = fixed_dimension + rotating_complex_dimension * 2 * Fraction(-1, 2)
    checks.append(
        record(
            "order-three trace and fixed rank",
            real_trace_w == 0 and fixed_dimension + 2 * rotating_complex_dimension == 27,
            "trace(w) = 9 + 9*(2 cos(2*pi/3)) = 0 and rank(P_B) = 9",
        )
    )
    w_minus_w_squared = (Fraction(1), Fraction(2))
    residue_square = cyclotomic_multiply(w_minus_w_squared, w_minus_w_squared)
    checks.append(
        record(
            "signed cyclic residue",
            residue_square == (Fraction(-3), Fraction(0)),
            "(w-w^2)^2 = w+w^2-2 = -3 on B-perp, hence I_w^2 = -1",
        )
    )
    checks.append(
        record(
            "orientation reversal parity",
            (-1) ** rotating_complex_dimension == -1,
            "I_w -> -I_w sends the ninth symplectic power to its negative",
        )
    )

    # Representation-ring derivation.  A key is (SU2 dimension, color sign,
    # integral charge), where color sign is 0, +1 (3), or -1 (bar 3).
    b_rep = Counter(
        {
            (1, 0, 0): 2,
            (3, 0, 0): 1,
            (2, 0, 3): 1,
            (2, 0, -3): 1,
        }
    )
    c_rep = Counter(
        {
            (2, 1, -1): 1,
            (1, 1, 2): 1,
            (2, -1, 1): 1,
            (1, -1, -2): 1,
        }
    )
    b_dual = Counter(
        {(d2, color, -charge): mult for (d2, color, charge), mult in b_rep.items()}
    )
    v_rep = b_rep + c_rep
    for (d2_b, _, charge_b), mult_b in b_dual.items():
        for (d2_c, color_c, charge_c), mult_c in c_rep.items():
            for d2_out in su2_tensor_dimensions(d2_b, d2_c):
                v_rep[(d2_out, color_c, charge_b + charge_c)] += mult_b * mult_c

    tangent_rep = Counter(
        {
            (2, 0, 3): 1,
            (2, 0, -3): 1,
            (3, 1, 2): 1,
            (2, 1, -1): 1,
            (1, 1, -4): 1,
            (3, -1, -2): 1,
            (2, -1, 1): 1,
            (1, -1, 4): 1,
        }
    )
    derived_normal = v_rep.copy()
    for key, multiplicity in tangent_rep.items():
        derived_normal[key] -= multiplicity
        if derived_normal[key] == 0:
            del derived_normal[key]

    uncolored = [
        Multiplet(2, 1, 1, 0),
        Multiplet(1, 3, 1, 0),
    ]
    colored_half = [
        Multiplet(4, 2, 3, -1),
        Multiplet(4, 1, 3, 2),
        Multiplet(1, 4, 3, -1),
        Multiplet(1, 3, 3, 2),
        Multiplet(1, 3, 3, -4),
        Multiplet(1, 2, 3, 5),
    ]
    normal = uncolored + colored_half + [
        Multiplet(item.multiplicity, item.su2_dimension, item.su3_dimension, -item.charge)
        for item in colored_half
    ]
    expected_normal = Counter({(1, 0, 0): 2, (3, 0, 0): 1})
    for item in colored_half:
        expected_normal[(item.su2_dimension, 1, item.charge)] += item.multiplicity
        expected_normal[(item.su2_dimension, -1, -item.charge)] += item.multiplicity

    checks.append(
        record(
            "normal branching subtraction",
            derived_normal == expected_normal,
            "(J + Hom(B,C)) - T(F4/H) equals the displayed H-module",
        )
    )

    uncolored_dimension = sum(item.dimension for item in uncolored)
    half_dimension = sum(item.dimension for item in colored_half)
    normal_dimension = sum(item.dimension for item in normal)
    checks.append(
        record(
            "normal representation dimension",
            (uncolored_dimension, half_dimension, normal_dimension) == (5, 72, 149),
            f"{uncolored_dimension} + {half_dimension} + {half_dimension} = {normal_dimension}",
        )
    )

    index_su2 = sum(
        item.multiplicity * item.su3_dimension * su2_index(item.su2_dimension)
        for item in normal
    )
    index_su3 = sum(
        item.multiplicity * item.su2_dimension * su3_index(item.su3_dimension)
        for item in normal
    )
    integral_u1_trace = sum(item.dimension * item.charge**2 for item in normal)
    normalized_u1_index = Fraction(integral_u1_trace, 12)

    checks.append(
        record(
            "SU(2) index",
            index_su2 == 71,
            f"I_SU2 = {index_su2}",
        )
    )
    checks.append(
        record(
            "SU(3) index",
            index_su3 == 24,
            f"I_SU3 = {index_su3}",
        )
    )
    color_fundamental_copies = sum(
        item.multiplicity * item.su2_dimension for item in colored_half
    )
    color_character_constant = uncolored_dimension
    color_character_re_trace_coefficient = 2 * color_fundamental_copies
    color_hs_constant = 2 * (normal_dimension - color_character_constant)
    color_hs_re_trace_coefficient = 2 * color_character_re_trace_coefficient
    wilson_action_multiplier = color_hs_constant
    beta_wilson_multiplier = wilson_action_multiplier // 2
    checks.append(
        record(
            "exact color character",
            (
                color_fundamental_copies,
                color_character_constant,
                color_character_re_trace_coefficient,
            )
            == (24, 5, 48),
            "chi_N|SU3 = 5 + 24*tr_3 + 24*tr_bar3 = 5 + 48*Re tr_3",
        )
    )
    checks.append(
        record(
            "exact color Wilson pullback",
            (
                color_hs_constant,
                color_hs_re_trace_coefficient,
                wilson_action_multiplier,
                beta_wilson_multiplier,
            )
            == (288, 96, 288, 144),
            "||sigma_N(U)-I||^2 = 96*(3-Re tr_3 U) = 288*q_W; beta_W = 144*beta",
        )
    )

    # On the Jordan-frame tangent, Spin(8) triality gives three real octonion
    # slots.  Under the same color SU(3), O = C + C^3 as a real module, so if
    # W=(C^3)_R then T_fr = R^6 + 3W.  The normal restriction is R^5 + 24W.
    # Trivial summands do not affect the trace form.
    real_fundamental_dimension = 6
    frame_triality_slots = 3
    frame_trivial_dimension = 2 * frame_triality_slots
    frame_real_fundamental_copies = frame_triality_slots
    frame_dimension = (
        frame_trivial_dimension
        + frame_real_fundamental_copies * real_fundamental_dimension
    )
    stable_copy_count = color_fundamental_copies // frame_real_fundamental_copies
    trivial_stabilization = (
        stable_copy_count * frame_trivial_dimension - uncolored_dimension
    )
    checks.append(
        record(
            "stable triality comparison",
            (
                stable_copy_count,
                trivial_stabilization,
                color_fundamental_copies,
                uncolored_dimension + trivial_stabilization,
                normal_dimension + trivial_stabilization,
            )
            == (8, 43, 24, 48, 8 * frame_dimension),
            "N_def|SU3 + R^43 = 8*T(F4/Spin8)|SU3; reduced real representation classes agree",
        )
    )
    slice_real_fundamental_copies = 1
    slice_hs_wilson_multiplier = 12 * slice_real_fundamental_copies
    frame_hs_wilson_multiplier = 12 * frame_real_fundamental_copies
    normal_hs_wilson_multiplier = 12 * color_fundamental_copies
    checks.append(
        record(
            "S6 tangent-to-Wilson response ladder",
            (
                slice_hs_wilson_multiplier,
                frame_hs_wilson_multiplier,
                normal_hs_wilson_multiplier,
                frame_hs_wilson_multiplier // slice_hs_wilson_multiplier,
                normal_hs_wilson_multiplier // frame_hs_wilson_multiplier,
            )
            == (12, 36, 288, 3, 8),
            "Q_TS6 = 12*q_W, Q_Tfr = 3*Q_TS6 = 36*q_W, Q_N = 8*Q_Tfr = 288*q_W",
        )
    )
    normal_to_killing_metric = Fraction(index_su3, 3)
    frame_to_killing_metric = Fraction(frame_real_fundamental_copies, 3)
    slice_to_killing_metric = Fraction(slice_real_fundamental_copies, 3)
    normal_metric_single_link_gap = Fraction(4, 9) / normal_to_killing_metric
    square_girth_haar_gap = 4 * normal_metric_single_link_gap
    checks.append(
        record(
            "normal-metric Haar floor",
            (
                slice_to_killing_metric,
                frame_to_killing_metric,
                normal_to_killing_metric,
                normal_metric_single_link_gap,
                square_girth_haar_gap,
            )
            == (Fraction(1, 3), 1, 8, Fraction(1, 18), Fraction(2, 9)),
            "b_TS6 = (-Killing)/3, b_Tfr = -Killing, b_N = 8*b_Tfr; lambda_link,N = 1/18",
        )
    )
    checks.append(
        record(
            "normalized U(1) index",
            integral_u1_trace == 828 and normalized_u1_index == 69,
            f"sum dim*q^2 = {integral_u1_trace}; divide by 12 to get {normalized_u1_index}",
        )
    )

    # Write z=exp(2*pi*i*n/6), zeta^k=exp(2*pi*i*2k/6),
    # and epsilon=exp(2*pi*i*3e/6).  The two faithful test multiplets impose
    # epsilon*zeta^k*z^-1=1 and zeta^k*z^2=1.
    central_solutions = [
        (epsilon_exponent, u1_exponent, color_exponent)
        for epsilon_exponent in range(2)
        for u1_exponent in range(6)
        for color_exponent in range(3)
        if (3 * epsilon_exponent + 2 * color_exponent - u1_exponent) % 6 == 0
        and (2 * color_exponent + 2 * u1_exponent) % 6 == 0
    ]
    z6_generated = {
        ((power * 1) % 2, (power * 5) % 6, (power * 1) % 3)
        for power in range(6)
    }
    checks.append(
        record(
            "global central kernel",
            set(central_solutions) == z6_generated,
            f"the two test multiplets leave exactly {len(central_solutions)} central lifts, generated cyclically as Z6",
        )
    )

    total_oriented_ambient = (52 - 16) + (9 - 1)
    zero_locus_dimension = (52 - 16) + 4
    normal_hessian_dimension = total_oriented_ambient - zero_locus_dimension
    checks.append(
        record(
            "reduced oriented-flag Hessian",
            (total_oriented_ambient, zero_locus_dimension, normal_hessian_dimension)
            == (44, 40, 4),
            "dim ambient 44, spec(Hess V) = {0^(40), 1^(4)}",
        )
    )

    passed = sum(checks)
    total = len(checks)
    print(f"SUMMARY {passed}/{total} checks passed")
    if passed != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

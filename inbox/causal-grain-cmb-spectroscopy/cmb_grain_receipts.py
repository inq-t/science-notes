"""Arithmetic and local-data receipts for the causal-grain CMB notebook.

These checks establish dimensional identities and reproduce features of bundled
Planck/ACT best-fit products.  They do not prove the proposed causal ontology,
the wall weld, or a new cosmological likelihood.
"""

from __future__ import annotations

import cmath
import math
import re
from pathlib import Path


MODULE = Path(__file__).resolve().parent
REPO = MODULE.parents[1]
PLANCK = REPO / "causal-wall-spectral-theory" / "sources" / "data" / "planck-2018"
ACT = (
    REPO
    / "causal-wall-spectral-theory"
    / "sources"
    / "data"
    / "act-dr6"
    / "best_fits_pact_lcdm"
    / "pact_lcdm_best_fits"
)

PLANCK_MINIMUM = PLANCK / (
    "COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt"
)
PLANCK_THEORY = PLANCK / (
    "COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt"
)
ACT_THEORY = ACT / "cmb.dat"

C = 299_792_458.0
HBAR = 1.054_571_817e-34
G = 6.674_30e-11
EV = 1.602_176_634e-19
MPC = 3.085_677_581_491_367e22


def close(a: float, b: float, *, rel: float = 1e-10, abs_: float = 0.0) -> None:
    if not math.isclose(a, b, rel_tol=rel, abs_tol=abs_):
        raise AssertionError(f"{a:.16g} != {b:.16g}")


def read_planck_parameters(path: Path) -> dict[str, float]:
    wanted = {"H0", "zstar", "rstar", "thetastar", "DAstar"}
    values: dict[str, float] = {}
    row = re.compile(r"^\s*\d+\s+([+-]?\d*\.?\d+(?:[Ee][+-]?\d+)?)\s+(\w+)\b")
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = row.match(line)
        if match and match.group(2) in wanted:
            values[match.group(2)] = float(match.group(1))
    missing = wanted.difference(values)
    if missing:
        raise ValueError(f"missing Planck parameters: {sorted(missing)}")
    return values


def read_numeric_table(path: Path) -> list[list[float]]:
    rows: list[list[float]] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        rows.append([float(item) for item in line.split()])
    return rows


def separated_local_maxima(
    rows: list[list[float]],
    value_column: int,
    ell_min: int,
    ell_max: int,
    minimum_separation: int = 80,
) -> list[int]:
    points = [(int(row[0]), row[value_column]) for row in rows]
    candidates = [
        points[i]
        for i in range(1, len(points) - 1)
        if ell_min <= points[i][0] <= ell_max
        and points[i][1] > points[i - 1][1]
        and points[i][1] >= points[i + 1][1]
    ]
    selected: list[tuple[int, float]] = []
    for candidate in candidates:
        if not selected or candidate[0] - selected[-1][0] >= minimum_separation:
            selected.append(candidate)
        elif candidate[1] > selected[-1][1]:
            selected[-1] = candidate
    return [ell for ell, _ in selected]


def zero_crossings(
    rows: list[list[float]],
    value_column: int,
    ell_min: int,
    ell_max: int,
) -> list[float]:
    points = [
        (float(row[0]), row[value_column])
        for row in rows
        if ell_min <= row[0] <= ell_max
    ]
    crossings: list[float] = []
    for (ell_0, value_0), (ell_1, value_1) in zip(points, points[1:]):
        if value_0 == 0.0:
            crossings.append(ell_0)
        elif value_0 * value_1 < 0.0:
            fraction = -value_0 / (value_1 - value_0)
            crossings.append(ell_0 + fraction * (ell_1 - ell_0))
    return crossings


def unit_and_closure_receipts() -> None:
    lambda_g = 4.264e-15
    hubble_km_s_mpc = 83.1058
    hubble = hubble_km_s_mpc * 1_000.0 / MPC
    tau_g = lambda_g / C
    energy_mev = HBAR * C / lambda_g / EV / 1e6
    radius_a = C / hubble
    delta_n = hubble * tau_g
    planck_time = math.sqrt(HBAR * G / C**5)

    close(delta_n, lambda_g / radius_a)
    lhs = delta_n**3
    rhs = (8.0 / 3.0) * (hubble * planck_time) ** 2
    close(lhs, rhs, rel=6e-4)

    sigma_a = math.log(radius_a / lambda_g)
    iota_direct = math.pi * (radius_a / (C * planck_time)) ** 2
    iota_from_grain = (8.0 * math.pi / 3.0) * math.exp(3.0 * sigma_a)
    close(iota_direct, iota_from_grain, rel=6e-4)

    print("LOCAL UNIT DRESSINGS")
    print(f"  lambda_g                    = {lambda_g:.6e} m")
    print(f"  tau_g = lambda_g/c          = {tau_g:.6e} s")
    print(f"  hbar*c/lambda_g             = {energy_mev:.6f} MeV")
    print(f"  H_c                         = {hubble:.6e} s^-1")
    print(f"  H_c*tau_g=lambda_g/R_A      = {delta_n:.6e}")
    print(f"  ticks per e-fold            = {1.0 / delta_n:.6e}")
    print(f"  Sigma_A=ln(R_A/lambda_g)    = {sigma_a:.9f} nats")
    print(f"  closure relative residual   = {(lhs / rhs) - 1.0:+.3e}")


def grain_cancellation_receipt() -> None:
    wavelength_unit = 4.264e-15
    hubble = 2.37e-18
    radius_a = C / hubble
    scale_factor = 9.1e-4
    wave_number = 1.8e-23
    baryon_loading = 0.63
    sound_fraction = 1.0 / math.sqrt(3.0 * (1.0 + baryon_loading))
    sound_speed = C * sound_fraction

    factored = (
        (wave_number * wavelength_unit / scale_factor)
        * (radius_a / wavelength_unit)
        * sound_fraction
    )
    standard = wave_number * sound_speed / (scale_factor * hubble)
    close(factored, standard, rel=2e-15)

    print("ACOUSTIC PHASE FACTORIZATION")
    print(f"  grain-factorized integrand  = {factored:.12e}")
    print(f"  standard k*c_s/(aH)         = {standard:.12e}")
    print("  lambda_g cancels exactly: this identity alone is not a new prediction")


def a2_receipt() -> None:
    theta = 0.371
    phases = [theta + 2.0 * math.pi * index / 3.0 for index in range(3)]
    fundamental = sum(cmath.exp(1j * phase) for phase in phases)
    cubic = sum(math.cos(phase) ** 3 for phase in phases)
    cubic_expected = 0.75 * math.cos(3.0 * theta)
    close(abs(fundamental), 0.0, abs_=1e-14)
    close(cubic, cubic_expected, rel=1e-13, abs_=1e-14)

    # A primitive idempotent has an algebraically fixed unit representative.
    e = ((0.5, 0.5), (0.5, 0.5))
    e_squared = tuple(
        tuple(sum(e[i][k] * e[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )
    if e_squared != e:
        raise AssertionError("rank-one Jordan representative is not idempotent")

    print("A2 / JORDAN TOY RECEIPTS")
    print(f"  equal-weight fundamental    = {abs(fundamental):.3e}")
    print(f"  cubic / third harmonic      = {cubic:.12e}")
    print("  primitive rank-one representative satisfies e^2=e and tr(e)=1")


def cmb_data_receipts() -> None:
    params = read_planck_parameters(PLANCK_MINIMUM)
    theta_star = params["thetastar"] / 100.0
    ell_a = math.pi / theta_star
    distance_ratio = params["DAstar"] * 1_000.0 / params["rstar"]
    close(distance_ratio, 1.0 / theta_star, rel=5e-5)

    planck_rows = read_numeric_table(PLANCK_THEORY)
    act_rows = read_numeric_table(ACT_THEORY)
    planck_tt = separated_local_maxima(planck_rows, 1, 100, 2500)
    planck_ee = separated_local_maxima(planck_rows, 3, 250, 3000)
    act_tt = separated_local_maxima(act_rows, 1, 100, 2500)
    act_ee = separated_local_maxima(act_rows, 6, 250, 3000)
    planck_te_zeros = zero_crossings(planck_rows, 2, 50, 2500)
    act_te_zeros = zero_crossings(act_rows, 2, 50, 2500)

    if len(planck_tt) < 6 or len(planck_ee) < 7:
        raise AssertionError("too few Planck acoustic extrema found")
    if len(act_tt) < 6 or len(act_ee) < 7:
        raise AssertionError("too few ACT acoustic extrema found")
    if len(planck_te_zeros) < 8 or len(act_te_zeros) < 8:
        raise AssertionError("too few TE sign changes found")
    for index in range(min(6, len(planck_ee), len(planck_tt) - 1)):
        if not planck_tt[index] < planck_ee[index] < planck_tt[index + 1]:
            raise AssertionError("Planck EE/TT quadrature interleaving failed")

    print("BUNDLED CMB PRODUCTS")
    print(f"  Planck z_*                  = {params['zstar']:.4f}")
    print(f"  Planck r_*                  = {params['rstar']:.4f} Mpc")
    print(f"  Planck D_M(z_*)             = {params['DAstar']:.5f} Gpc")
    print(f"  100 theta_*                 = {params['thetastar']:.6f}")
    print(f"  ell_A=pi/theta_*            = {ell_a:.6f}")
    print(f"  D_M/r_*                     = {distance_ratio:.6f}")
    print(f"  Planck-theory TT maxima     = {planck_tt[:8]}")
    print(f"  Planck-theory EE maxima     = {planck_ee[:9]}")
    print(
        "  Planck-theory TE zeroes     = "
        f"{[round(value, 1) for value in planck_te_zeros[:10]]}"
    )
    print(f"  P-ACT-theory TT maxima      = {act_tt[:8]}")
    print(f"  P-ACT-theory EE maxima      = {act_ee[:9]}")
    print(
        "  P-ACT-theory TE zeroes      = "
        f"{[round(value, 1) for value in act_te_zeros[:10]]}"
    )
    print("  Planck EE maxima interleave successive TT maxima (first six checked)")


def main() -> None:
    for path in (PLANCK_MINIMUM, PLANCK_THEORY, ACT_THEORY):
        if not path.is_file():
            raise FileNotFoundError(path)
    unit_and_closure_receipts()
    print()
    grain_cancellation_receipt()
    print()
    a2_receipt()
    print()
    cmb_data_receipts()
    print()
    print("ALL RECEIPTS PASS")
    print("Scope: arithmetic identities and bundled best-fit products, not a physics proof.")


if __name__ == "__main__":
    main()

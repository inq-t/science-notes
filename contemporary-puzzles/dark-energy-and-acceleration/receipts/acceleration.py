#!/usr/bin/env python3
"""Receipt for the dark-energy-and-acceleration module.

Recomputes the unit-branch chronology from the generalized closure, verifies
the shape invariant and the CPL locus along the orbit, and compares the
predicted local CPL tangent with published DESI DR2 w0waCDM fits.

Relation to the canonical receipt in causal-scale-theory/receipts/: the closure
residual is the same equation and both use bisection, so this is NOT an
independent implementation of the root finder. What is independent here is the
cosmography: q and j are obtained by finite differences on E^2(N) and then
compared against the analytic tangent formulas, whereas the canonical receipt
compares against stored literals. Treat the overlap as a regression check and
the cosmography as the added coverage.

Scope. This checks arithmetic internal to the declared background closure and
compares against published fitted parameters. It does not validate the wall
construction, either unit principle, the constitutive source law, the
horizontal-temperature identification, or any perturbation observable, and it
is not a likelihood.

Stdlib only. Exits nonzero if any check fails, including under --json.
"""

from __future__ import annotations

import argparse
import json
import math
import sys

# Inherited benchmark ordinary abundances.
OM_BENCH = 0.310598
OR_BENCH = 9.15e-5

# Published DESI DR2 w0waCDM fits: arXiv:2503.14738, Table 5 / Eqs. (25)-(28).
# label, Omega_m, sig(Omega_m), w0, sig(w0), wa, sig_up(wa), sig_dn(wa), sigma-pref
DESI_DR2 = [
    ("DESI+CMB",            0.353,  0.021,  -0.42,  0.21, -1.75, 0.58, 0.58, "3.1"),
    ("DESI+CMB+Pantheon+",  0.3114, 0.0057, -0.838, 0.055, -0.62, 0.22, 0.19, "2.8"),
    ("DESI+CMB+Union3",     0.3275, 0.0086, -0.667, 0.088, -1.09, 0.31, 0.27, "3.8"),
    ("DESI+CMB+DESY5",      0.3191, 0.0056, -0.752, 0.057, -0.86, 0.23, 0.20, "4.2"),
]

FAILURES: list[str] = []


# --- numerics -----------------------------------------------------------------
def log_cosh(v: float) -> float:
    a = abs(v)
    return a + math.log1p(math.exp(-2.0 * a)) - math.log(2.0)


def sech2(v: float) -> float:
    return math.exp(-2.0 * log_cosh(v))


def matter_sum(x: float, om: float, orad: float) -> float:
    return om * math.exp(3.0 * x) + orad * math.exp(4.0 * x)


def closure_residual(x: float, nu: float, ruble: float, om: float, orad: float) -> float:
    """(R/(2-R)) M(x) sech^2(nu x) - D, per the canonical flatness closure."""
    d = 1.0 - om - orad
    return (ruble / (2.0 - ruble)) * matter_sum(x, om, orad) * sech2(nu * x) - d


def bisect(f, lo: float, hi: float, tol: float = 1e-14, itmax: int = 300) -> float:
    flo, fhi = f(lo), f(hi)
    if flo == 0.0:
        return lo
    if fhi == 0.0:
        return hi
    if flo * fhi > 0.0:
        raise ValueError("no sign change on bracket")
    for _ in range(itmax):
        mid = 0.5 * (lo + hi)
        fmid = f(mid)
        if fmid == 0.0 or (hi - lo) < tol:
            return mid
        if flo * fmid < 0.0:
            hi, fhi = mid, fmid
        else:
            lo, flo = mid, fmid
    return 0.5 * (lo + hi)


def late_root(nu: float, ruble: float, om: float, orad: float,
              allow_negative: bool = False) -> float:
    """Smallest positive root of present flatness: the canonical late branch.

    The canon defines x_c := ln(1+z_c) > 0, so only positive roots are admitted
    dates. allow_negative=True additionally scans x < 0; those solve the same
    equation but fall outside the canonically admitted domain, and are exposed
    only so the R_c threshold at which the root leaves that domain is visible
    rather than silently pruned.
    """
    f = lambda x: closure_residual(x, nu, ruble, om, orad)
    f0 = f(0.0)
    directions = (+1.0, -1.0) if allow_negative else (+1.0,)
    for direction in directions:
        lo, hi, step = 0.0, 0.0, 1e-4
        while abs(hi) < 60.0:
            hi += direction * step
            if f0 * f(hi) < 0.0:
                return bisect(f, min(lo, hi), max(lo, hi))
            lo = hi
            step *= 1.0005
    raise ValueError(f"no admitted root for nu={nu}, R={ruble}, Om={om}")


# --- background ---------------------------------------------------------------
def e2(nn: float, xc: float, nu: float, ruble: float, om: float, orad: float) -> float:
    """E^2(N) = (H/H0)^2 on the declared branch. N = ln(a/a0), x = N + xc."""
    resp = (ruble / (2.0 - ruble)) * matter_sum(xc, om, orad) * sech2(nu * (nn + xc))
    return om * math.exp(-3.0 * nn) + orad * math.exp(-4.0 * nn) + resp


def q_of_N(nn: float, xc: float, nu: float, ruble: float, om: float, orad: float) -> float:
    """q = -1 - (1/2) d ln E^2 / dN, by central difference."""
    h = 1e-5
    dln = (math.log(e2(nn + h, xc, nu, ruble, om, orad))
           - math.log(e2(nn - h, xc, nu, ruble, om, orad))) / (2.0 * h)
    return -1.0 - 0.5 * dln


def cosmography_analytic(nn: float, xc: float, nu: float, ruble: float,
                         om: float, orad: float) -> tuple[float, float]:
    """(q, j) from closed-form derivatives of E^2(N).

    Exists so the finite-difference values used elsewhere have something to be
    checked against, rather than only against stored literals.
    """
    amp = (ruble / (2.0 - ruble)) * matter_sum(xc, om, orad)
    u = nu * (nn + xc)
    t, s2 = math.tanh(u), sech2(u)
    m3, m4 = om * math.exp(-3.0 * nn), orad * math.exp(-4.0 * nn)

    ee = m3 + m4 + amp * s2
    d1 = -3.0 * m3 - 4.0 * m4 - 2.0 * nu * amp * s2 * t
    d2 = (9.0 * m3 + 16.0 * m4
          - 2.0 * nu * nu * amp * s2 * (s2 - 2.0 * t * t))

    l1 = d1 / ee
    l2 = d2 / ee - l1 * l1
    q = -1.0 - 0.5 * l1
    qp = -0.5 * l2
    return q, q + 2.0 * q * q - qp


def chronology(nu: float = 1.0, ruble: float = 1.0, om: float = OM_BENCH,
               orad: float = OR_BENCH, allow_negative: bool = False) -> dict:
    xc = late_root(nu, ruble, om, orad, allow_negative)
    zc = math.exp(xc) - 1.0

    w0 = -1.0 + (2.0 * nu / 3.0) * math.tanh(nu * xc)
    wa = -(2.0 * nu * nu / 3.0) * sech2(nu * xc)

    q0 = q_of_N(0.0, xc, nu, ruble, om, orad)
    h = 1e-4
    dqdN = (q_of_N(h, xc, nu, ruble, om, orad)
            - q_of_N(-h, xc, nu, ruble, om, orad)) / (2.0 * h)
    j0 = q0 + 2.0 * q0 * q0 - dqdN

    qf = lambda n: q_of_N(n, xc, nu, ruble, om, orad)
    z_entry = a_exit = None
    try:
        z_entry = math.exp(-bisect(qf, -3.0, 0.0)) - 1.0
    except ValueError:
        pass
    try:
        a_exit = math.exp(bisect(qf, 0.0, 6.0))
    except ValueError:
        pass

    n_in = -math.log1p(z_entry) if z_entry is not None else None
    n_out = math.log(a_exit) if a_exit is not None else None
    window = (n_out - n_in) if (n_in is not None and n_out is not None) else None

    return {
        "nu": nu, "ruble": ruble, "Omega_m0": om, "Omega_r0": orad,
        "x_c": xc, "z_c": zc,
        "Omega_X_c": ruble / 2.0,
        "w_0": w0, "w_a": wa, "q_0": q0, "j_0": j0,
        "z_acceleration_entry": z_entry,
        "a_over_a0_acceleration_exit": a_exit,
        "acceleration_window_efolds": window,
        "present_fraction_through_window": (-n_in / window) if window else None,
        "x_c_in_widths": xc * nu,
    }


# --- comparison helpers -------------------------------------------------------
def implied_nu(w0: float, wa: float) -> float | None:
    """Width implied by treating a published CPL pair as the exact tangent.

    Inverts w_a = (3/2)(1+w_0)^2 - (2/3) nu^2. This is an effective-shape
    statement about a fitted pair, not a measurement of modular width.
    """
    arg = 1.5 * (1.5 * (1.0 + w0) ** 2 - wa)
    return math.sqrt(arg) if arg >= 0.0 else None


def implied_nu_range(w0, s_w0, wa, s_up, s_dn) -> tuple[float | None, float | None]:
    """Range of implied nu over the 1-sigma box on (w0, wa).

    A box, not an ellipse: the published covariance is not available, and the
    (w0, wa) posteriors are strongly anticorrelated, so this is an envelope and
    not a confidence interval. It exists to stop a four-decimal point value
    from reading as a precise determination.
    """
    vals = [implied_nu(w0 + dw, wa + dwa)
            for dw in (-s_w0, 0.0, +s_w0)
            for dwa in (-s_dn, 0.0, +s_up)]
    vals = [v for v in vals if v is not None]
    return (min(vals), max(vals)) if vals else (None, None)


def cpl_crossing_z(w0: float, wa: float) -> float | None:
    """Redshift where a CPL pair itself crosses w = -1: a = 1 + (1+w0)/wa."""
    if wa == 0.0:
        return None
    a = 1.0 + (1.0 + w0) / wa
    return (1.0 / a - 1.0) if a > 0.0 else None


def sigma_distance(pred: float, obs: float, s_up: float, s_dn: float) -> float:
    return (pred - obs) / (s_up if pred > obs else s_dn)


# --- checks -------------------------------------------------------------------
def check(name: str, got, want, tol: float) -> None:
    if want is None or got is None:
        FAILURES.append(f"{name}: missing value")
        print(f"FAIL  {name}: got={got} want={want}")
        return
    ok = abs(got - want) <= tol
    if not ok:
        FAILURES.append(f"{name}: got={got!r} want={want!r} tol={tol}")
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got={got:.10g} want={want:.10g} tol={tol:g}")


def assert_true(name: str, ok: bool, detail: str = "") -> None:
    if not ok:
        FAILURES.append(f"{name}: {detail or 'assertion failed'}")
    print(f"{'PASS' if ok else 'FAIL'}  {name}{('  ' + detail) if detail else ''}")


def run_checks(c: dict) -> None:
    nu, xc = c["nu"], c["x_c"]

    print("# unit-branch benchmark (causal-scale-theory/unit-branch)")
    check("late root x_c", c["x_c"], 0.2940066, 2e-7)
    check("crossing redshift z_c", c["z_c"], 0.3417927, 2e-7)
    check("w_0", c["w_0"], -0.8094545, 2e-7)
    check("w_a", c["w_a"], -0.6122053, 2e-7)
    check("q_0", c["q_0"], -0.3369025, 1e-6)
    check("j_0", c["j_0"], -0.1112465, 1e-5)
    check("acceleration entry z", c["z_acceleration_entry"], 0.7856935, 1e-5)
    check("acceleration exit a/a0", c["a_over_a0_acceleration_exit"], 11.7865, 1e-3)

    print("\n# closure and structural identities")
    check("flatness residual at x_c",
          closure_residual(xc, nu, c["ruble"], c["Omega_m0"], c["Omega_r0"]), 0.0, 1e-13)
    # The response fraction today must equal D independently of how it was
    # constructed: recompute it from the profile rather than from the closure.
    amp = (c["ruble"] / (2.0 - c["ruble"])) * matter_sum(xc, c["Omega_m0"], c["Omega_r0"])
    check("rho_X(0)/rho_crit,0 = D", amp * sech2(nu * xc),
          1.0 - c["Omega_m0"] - c["Omega_r0"], 1e-13)
    # The density peak must sit at x = 0, not merely be asserted there.
    peak = max((amp * sech2(nu * xx), xx)
               for xx in [i * 1e-4 for i in range(-20000, 20001)])[1]
    check("density peak location x", peak, 0.0, 1e-4)
    # Cosmography: finite difference against closed form, not against literals.
    q_an, j_an = cosmography_analytic(0.0, xc, nu, c["ruble"], c["Omega_m0"], c["Omega_r0"])
    check("q_0 finite-diff vs analytic", c["q_0"], q_an, 1e-9)
    check("j_0 finite-diff vs analytic", c["j_0"], j_an, 1e-6)
    check("j_0 analytic vs canon", j_an, -0.1112465, 1e-7)

    print("\n# shape invariant 9(1+w)^2 + 6 w' = 4 nu^2 along the orbit")
    for x in (-2.0, -0.75, -0.1, 0.0, 0.2940066, 1.0, 3.0):
        w = -1.0 + (2.0 * nu / 3.0) * math.tanh(nu * x)
        wp = (2.0 * nu * nu / 3.0) * sech2(nu * x)
        check(f"invariant at x={x:+.7g}", 9.0 * (1.0 + w) ** 2 + 6.0 * wp,
              4.0 * nu * nu, 1e-12)

    print("\n# CPL locus w_a = (3/2)(1+w_0)^2 - (2/3) nu^2")
    check("locus at benchmark",
          1.5 * (1.0 + c["w_0"]) ** 2 - (2.0 / 3.0) * nu * nu, c["w_a"], 1e-12)

    print("\n# invariant is amplitude- and date-independent; generalizes in nu")
    for ruble in (0.6, 1.0, 1.3):
        cc = chronology(nu=1.0, ruble=ruble)
        check(f"invariant, R={ruble}",
              9.0 * (1.0 + cc["w_0"]) ** 2 - 6.0 * cc["w_a"], 4.0, 1e-11)
    for nu_t in (0.6, 1.0, 1.4, 1.75):
        cc = chronology(nu=nu_t)
        check(f"invariant, nu={nu_t}",
              9.0 * (1.0 + cc["w_0"]) ** 2 - 6.0 * cc["w_a"], 4.0 * nu_t * nu_t, 1e-11)

    print("\n# where the root leaves the canonically admitted domain x_c > 0")
    print("# threshold R_c = 2D is the exact x_c = 0 condition, nu-independent")
    print("# since sech^2(0) = 1. Value inherited from the archived v8 master.")
    two_d = 2.0 * (1.0 - c["Omega_m0"] - c["Omega_r0"])
    check("2D at benchmark", two_d, 1.378621, 1e-6)
    assert_true("no admitted root above 2D",
                _no_positive_root(1.45), "R_c=1.45 > 2D: closure root is x_c < 0")
    assert_true("admitted root below 2D",
                not _no_positive_root(1.30), "R_c=1.30 < 2D: closure root is x_c > 0")

    print("\n# benchmark fold anchors (causal-scale-theory/flatness-branches)")
    print("# these are benchmark-specific, not universal width bounds")
    for nu_t, want_n in ((1.5, 1), (1.7, 3), (1.9, 1), (2.0, 0)):
        n = _count_positive_roots(nu_t)
        assert_true(f"root count at nu={nu_t}", n == want_n, f"got {n}, want {want_n}")
    # the canon's own counterexample to a universal ceiling
    for nu_t in (2.0, 2.2):
        n = _count_positive_roots(nu_t, ruble=1.9)
        assert_true(f"root exists at nu={nu_t}, R=1.9", n >= 1, f"got {n} positive roots")

    print("\n# no future w crossing of -1/3, unit branch")
    print("# 1+3w = 2(tanh x - 1) = -4/(e^{2x}+1) < 0, -> 0 from below.")
    print("# Evaluated as log|1+3w| = log 4 - log(e^{2x}+1), finite for every x:")
    print("# the magnitude itself goes subnormal near x ~ 355 and to zero near")
    print("# x ~ 373, so a direct evaluation would report a spurious zero.")
    prev_lg = None
    for x in (-5.0, 0.0, 5.0, 20.0, 300.0, 500.0, 5000.0):
        lg = math.log(4.0) - (2.0 * x + math.log1p(math.exp(-2.0 * x)))
        # negative sign is structural: -4/(e^{2x}+1) has a positive numerator
        # over a positive denominator, negated. Assert magnitude > 0 via the
        # log being finite, and strict decrease toward zero via monotonicity.
        ok = math.isfinite(lg) and (prev_lg is None or lg < prev_lg)
        assert_true(f"log|1+3w| finite and decreasing at x={x:+g}", ok,
                    f"= {lg:.6g}")
        prev_lg = lg
    # and the closed form is negative wherever it is representable at all
    for x in (-5.0, 0.0, 5.0, 20.0, 300.0):
        v = -4.0 / (math.exp(2.0 * x) + 1.0)
        assert_true(f"1+3w < 0 at x={x:+g}", v < 0.0, f"= {v:+.6g}")

    print("\n# NEGATIVE CONTROL: is the recent crossing distinctive? No.")
    print("# LCDM matter-Lambda equality sits at N_eq = (1/3) ln(Om/OL), the")
    print("# reciprocal ratio to the CST small-x form, same factor of three.")
    print("# The two epochs track each other closely, so the compression is")
    print("# shared and is NOT evidence for either framework.")
    print(f"  {'Omega_m0':>9} {'x_c (CST)':>11} {'-N_eq (LCDM)':>13} {'gap':>8}")
    gaps = {}
    for om in (0.05, 0.10, 0.15, 0.20, 0.3106, 0.40, 0.50, 0.60, 0.80, 0.85, 0.95):
        cc = chronology(om=om, allow_negative=True)
        minus_neq = math.log((1.0 - om) / om) / 3.0
        gap = abs(cc["x_c"] - minus_neq)
        gaps[om] = gap
        print(f"  {om:>9.4f} {cc['x_c']:>+11.5f} {minus_neq:>+13.5f} {gap:>8.4f}")
    g_bench = gaps[0.3106]
    g_wide = max(g for o, g in gaps.items() if 0.15 <= o <= 0.85)
    assert_true("gap at benchmark < 0.03 e-folds", g_bench < 0.03, f"= {g_bench:.4f}")
    assert_true("gap over Om in [0.15,0.85] < 0.20 e-folds", g_wide < 0.20,
                f"max = {g_wide:.4f}")
    print(f"  -> agreement is {g_bench:.3f} e-folds at the benchmark but degrades to")
    print(f"     {g_wide:.2f} across Omega_m0 in [0.15,0.85]. Close, not identical;")
    print("     either way, shared between the frameworks and not a gain.")


def _no_positive_root(ruble: float) -> bool:
    try:
        late_root(1.0, ruble, OM_BENCH, OR_BENCH, allow_negative=False)
        return False
    except ValueError:
        return True


def _count_positive_roots(nu: float, ruble: float = 1.0,
                          om: float = OM_BENCH, orad: float = OR_BENCH) -> int:
    f = lambda x: closure_residual(x, nu, ruble, om, orad)
    n, x, step, prev = 0, 1e-6, 1e-4, None
    while x < 60.0:
        v = f(x)
        if prev is not None and prev * v < 0.0:
            n += 1
        prev = v
        x += step
        step *= 1.0004
    return n


# --- DESI comparison ----------------------------------------------------------
def desi_comparison() -> list[dict]:
    rows = []
    bench = chronology()
    for label, om, om_s, w0, w0_s, wa, wa_up, wa_dn, pref in DESI_DR2:
        matched = chronology(om=om)
        lo, hi = implied_nu_range(w0, w0_s, wa, wa_up, wa_dn)
        rows.append({
            "combination": label,
            "quoted_sigma_pref_over_LCDM": pref,
            "Omega_m_fit": om, "Omega_m_fit_err": om_s,
            "w0_obs": w0, "w0_err": w0_s,
            "wa_obs": wa, "wa_err_up": wa_up, "wa_err_dn": wa_dn,
            "implied_nu": implied_nu(w0, wa),
            "implied_nu_envelope": [lo, hi],
            "cpl_self_crossing_z": cpl_crossing_z(w0, wa),
            "benchmark": {
                "Omega_m0": bench["Omega_m0"],
                "w0_pred": bench["w_0"], "wa_pred": bench["w_a"],
                "z_c_pred": bench["z_c"],
                "w0_sigma": sigma_distance(bench["w_0"], w0, w0_s, w0_s),
                "wa_sigma": sigma_distance(bench["w_a"], wa, wa_up, wa_dn),
            },
            "matched": {
                "Omega_m0": om,
                "w0_pred": matched["w_0"], "wa_pred": matched["w_a"],
                "z_c_pred": matched["z_c"],
                "w0_sigma": sigma_distance(matched["w_0"], w0, w0_s, w0_s),
                "wa_sigma": sigma_distance(matched["w_a"], wa, wa_up, wa_dn),
            },
        })
    return rows


def print_comparison(rows: list[dict]) -> None:
    print("\n# INDICATIVE comparison with published DESI DR2 w0waCDM fits")
    print("# Prediction is a point: nu=1, R_c=1, and the row's own Omega_m.")
    print("# It is the local CPL tangent at z=0 of a sech^2 history; the observed")
    print("# pair is a CPL fit over a redshift range. The canon's own test")
    print("# hierarchy warns that generic CPL posteriors need not equal the local")
    print("# tangent. These offsets are indicative and are NOT significances.")
    hdr = (f"{'combination':<22} {'Om_fit':>7} {'w0_obs':>16} {'w0_pred':>9} {'dw0':>7} "
           f"{'wa_obs':>18} {'wa_pred':>9} {'dwa':>7}")
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        m = r["matched"]
        w0o = f"{r['w0_obs']:+.3f}+/-{r['w0_err']:.3f}"
        wao = f"{r['wa_obs']:+.2f}+{r['wa_err_up']:.2f}/-{r['wa_err_dn']:.2f}"
        print(f"{r['combination']:<22} {r['Omega_m_fit']:>7.4f} {w0o:>16} "
              f"{m['w0_pred']:>+9.4f} {m['w0_sigma']:>+6.2f}s "
              f"{wao:>18} {m['wa_pred']:>+9.4f} {m['wa_sigma']:>+6.2f}s")

    print("\n# same rows at the fixed benchmark Omega_m0 = 0.310598")
    for r in rows:
        b = r["benchmark"]
        print(f"  {r['combination']:<22} w0 {b['w0_sigma']:+6.2f}s   "
              f"wa {b['wa_sigma']:+6.2f}s")

    print("\n# phantom-crossing epoch: predicted vs where each CPL pair itself crosses")
    print(f"  {'combination':<22} {'z_c predicted':>14} {'z_cross(CPL)':>13} {'later by':>9}")
    for r in rows:
        zc_p = r["matched"]["z_c_pred"]
        zc_o = r["cpl_self_crossing_z"]
        d = (zc_o - zc_p) if zc_o is not None else None
        print(f"  {r['combination']:<22} {zc_p:>14.4f} "
              f"{('n/a' if zc_o is None else format(zc_o, '.4f')):>13} "
              f"{('n/a' if d is None else format(d, '+.4f')):>9}")
    print("  Every CPL-implied crossing is LATER than predicted. The ranges do not")
    print("  overlap: predicted 0.24-0.34, CPL-implied 0.35-0.50. Adjacent and")
    print("  systematically offset, in the same direction as the w0 offsets.")

    print("\n# width implied by inverting the CPL locus on each published pair")
    print("# Envelope is the 1-sigma BOX on (w0,wa), not a confidence interval:")
    print("# the published covariance is unavailable and the pair is strongly")
    print("# anticorrelated. This restates the wa offset; it does not add to it.")
    for r in rows:
        lo, hi = r["implied_nu_envelope"]
        print(f"  {r['combination']:<22} nu = {r['implied_nu']:.2f} "
              f"[{lo:.2f}, {hi:.2f}]")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    bench = chronology()
    rows = desi_comparison()

    if args.json:
        # Checks run regardless of output mode, so the failure list is real.
        import io
        import contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            run_checks(bench)
        print(json.dumps({"benchmark": bench, "desi_dr2_comparison": rows,
                          "failures": FAILURES}, indent=2, sort_keys=True))
        return 1 if FAILURES else 0

    run_checks(bench)
    print_comparison(rows)

    print("\n# the acceleration episode is finite, unit branch, benchmark abundances")
    print(f"  entry  z = {bench['z_acceleration_entry']:.7f}")
    print(f"  exit   a/a0 = {bench['a_over_a0_acceleration_exit']:.5f}")
    print(f"  window = {bench['acceleration_window_efolds']:.6f} e-folds")
    print(f"  present epoch sits {100.0 * bench['present_fraction_through_window']:.2f}% in")
    print(f"  present displacement from crossing = {bench['x_c_in_widths']:.6f} widths")

    print("\n# width sensitivity of the tangent, benchmark abundances")
    for nu_t in (0.8, 0.9, 1.0, 1.1, 1.2):
        cc = chronology(nu=nu_t)
        print(f"  nu={nu_t:.2f}  z_c={cc['z_c']:.4f}  w_0={cc['w_0']:+.4f}  "
              f"w_a={cc['w_a']:+.4f}  q_0={cc['q_0']:+.4f}")

    if FAILURES:
        print(f"\nFAIL ({len(FAILURES)} checks failed)")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print("\nPASS (all checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Receipts for the bath-crossover reading. Stdlib only; exit nonzero on failure.

A pass establishes arithmetic only: the crossover value, its ratio to the
measured RAR scale under the stated convention, the convention-sensitivity
negative control, the predicted redshift drift, and solar-system silence.
It does NOT establish a mechanism, a covariant sector, or anything about
clusters or the CMB (conceded in the module as NG1/NG2).
"""
import json, math, sys

FAIL = []
def check(name, val, ref, rtol=1e-2):
    if abs(val - ref) > rtol * abs(ref): FAIL.append((name, val, ref))
    return val

c   = 299792458.0
Mpc = 3.0856775814913673e22
Om, OL = 0.315, 0.685
g_dagger = 1.20e-10          # McGaugh-Lelli-Schombert 2016 (stat 0.02, syst 0.24)

out = {}
def a0(H0kms):
    return c * (H0kms*1e3/Mpc) / (2*math.pi)

a67 = out["cH0_over_2pi_H67p4"] = check("a0(67.4)", a0(67.4), 1.042e-10)
a73 = out["cH0_over_2pi_H73"]   = check("a0(73)",   a0(73.0), 1.128e-10)
out["ratio_H67p4"] = check("ratio67", g_dagger/a67, 1.152, 1e-2)
out["ratio_H73"]   = check("ratio73", g_dagger/a73, 1.064, 1e-2)
aL = out["c2_sqrtLambda3_over_2pi"] = check("a0(Lambda)", a0(67.4*math.sqrt(OL)), 0.862e-10)
out["ratio_Lambda_form"] = check("ratioL", g_dagger/aL, 1.392, 1e-2)

# the order-one claim, asserted as a window (not tuned):
assert 0.7 <= g_dagger/a67 <= 1.5 and 0.7 <= g_dagger/a73 <= 1.5

# NEGATIVE CONTROL: without the 2pi convention the match fails by > 5x.
no2pi = a67 * 2*math.pi
out["no_2pi_miss_factor"] = check("no2pi", no2pi/g_dagger, 5.46, 1e-2)
assert no2pi/g_dagger > 5.0   # the agreement is convention-sensitive; say so.

# N1: predicted drift of the RAR normalization if g_dagger tracks cH(z)/2pi
E = lambda z: math.sqrt(Om*(1+z)**3 + OL)
out["E_of_z"] = {z: round(check(f"E({z})", E(z), r), 3)
                 for z, r in [(0.5, 1.322), (1.0, 1.790), (2.0, 3.032)]}

# NG3: solar-system silence (Saturn), five orders above the scale
GM_sun, r_sat = 1.32712440018e20, 1.4335e12
a_sat = out["a_Saturn"] = check("Saturn", GM_sun/r_sat**2, 6.46e-5, 1e-2)
assert a_sat / g_dagger > 1e5

print(json.dumps(out, indent=1))
if FAIL:
    print("FAILED:", FAIL, file=sys.stderr); sys.exit(1)
print("ALL RECEIPTS PASS")

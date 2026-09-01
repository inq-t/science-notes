#!/usr/bin/env python3
"""Audit of the claim "Lambda is the inverse quadratic Casimir of the trace-zero Jordan cell".
Stdlib only; exit nonzero on failure.

What a pass establishes: (A) the SdS horizon cubic r^3 - L^2 r + 2 m L^2 = 0 has
sigma_1 = 0, sigma_2 = -L^2, sum r_i^2 = 2 L^2 for EVERY m below Nariai -- so
"Lambda = 6/|X|^2" is Vieta's formula Lambda = 3/L^2 restated; (B) the identity
Lambda = 64 l_P^4 / (3 lambda_Lambda^6) is an exact inversion of the grain lemma
evaluated at the Lambda horizon, and its ~1e-15 residual is floating-point noise
carrying no information (negative control: an arbitrary fake Lambda returns the
same residual); (C) the "Lambda-grain" 40.5 MeV is m_cap(N -> infinity), and the
ratio of crossing grain to Lambda-grain is (H_c/H_Lambda)^(1/3), not ^(2/3).
It establishes nothing about the value of Lambda, the grain, or any Casimir.
"""
import json, math, sys

FAIL = []
def check(name, val, ref, rtol=1e-9, atol=0.0):
    ok = abs(val - ref) <= max(atol, rtol*abs(ref))
    if not ok: FAIL.append((name, val, ref))
    return val

out = {}
# ---- A. Vieta on the SdS cubic ---------------------------------------------
def cubic_roots(p, q):
    # depressed cubic t^3 + p t + q = 0 with p < 0 and three real roots (below Nariai),
    # trigonometric form: roots A cos((phi - 2 pi k)/3), A = 2 sqrt(-p/3), cos phi = -q/(2 sqrt(-p^3/27))
    A = 2*math.sqrt(-p/3)
    r = math.sqrt(-p**3/27); phi = math.acos(max(-1.0, min(1.0, -q/(2*r))))
    return [A*math.cos((phi - 2*math.pi*k)/3) for k in range(3)]

L = 1.0
m_N = L/(3*math.sqrt(3))                    # Nariai mass
for frac in (0.0, 0.2, 0.5, 0.9, 0.999):
    m = frac*m_N
    roots = cubic_roots(-L**2, 2*m*L**2)
    s1 = sum(roots); s2 = roots[0]*roots[1] + roots[0]*roots[2] + roots[1]*roots[2]
    normsq = sum(r*r for r in roots)
    out[f"A_m/mN={frac}"] = {"roots": [round(r, 6) for r in roots], "sigma1": round(s1, 12),
                              "sigma2": round(s2, 12), "sum_r2": round(normsq, 12)}
    check(f"A_sigma1_zero_{frac}", s1, 0.0, atol=1e-9)
    check(f"A_sigma2_is_minus_L2_{frac}", s2, -L**2)
    check(f"A_sum_r2_is_2L2_{frac}", normsq, 2*L**2)
    check(f"A_Lambda_is_6_over_normsq_{frac}", 6.0/normsq, 3.0/L**2)   # Lambda = 3/L^2
    # positivity of the root count: two positive roots for 0 < m < m_N, exactly one at m = 0 (the other is 0)
    npos = sum(1 for r in roots if r > 1e-9)
    check(f"A_two_positive_roots_{frac}", float(npos), 2.0 if frac > 0 else 1.0)
out["A_verdict"] = "sigma2 = -L^2 independent of m: |X|^2 = 2L^2 is a function of Lambda alone, by Vieta"

# ---- B. The 'exact' inversion and its negative control --------------------
hbar, c, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
lP2 = hbar*G/c**3
def grain_from_Lambda(Lam):
    Lds = math.sqrt(3.0/Lam)                                   # de Sitter radius c/H_Lambda
    return ((8.0/3.0)*lP2*Lds)**(1.0/3.0)
def Lambda_from_grain(lam):
    return 64.0*lP2**2/(3.0*lam**6)
H0, OmL = 67.36, 0.6847                                      # Planck 2018
H_L = H0*math.sqrt(OmL)*1e3/3.0856775814913673e22
Lam = 3*H_L**2/c**2
lam_L = grain_from_Lambda(Lam)
out["B_Lambda_m^-2"] = check("B_Lambda_vs_parallel_note", Lam, 1.0890e-52, rtol=2e-4)
out["B_lambda_Lambda_fm"] = check("B_lambda_vs_parallel_note", lam_L*1e15, 4.872, rtol=2e-4)
out["B_E_Lambda_MeV"] = check("B_E_vs_parallel_note", 197.3269804/(lam_L*1e15), 40.50, rtol=3e-4)
res = Lambda_from_grain(lam_L)/Lam - 1
out["B_residual"] = check("B_residual_is_roundoff", abs(res), 0.0, atol=1e-13)
# negative control: any Lambda whatsoever inverts to the same precision
fake = 7.3e-50
res_fake = Lambda_from_grain(grain_from_Lambda(fake))/fake - 1
out["B_negative_control_fake_Lambda_residual"] = res_fake
check("B_fake_inverts_too", Lambda_from_grain(grain_from_Lambda(fake)), fake, rtol=1e-12)
out["B_verdict"] = "the residual measures floating point, not physics: the fake Lambda passes identically"

# ---- C. Lambda-grain is m_cap at the asymptote; exponent is 1/3 -------------
H_c = 83.1058*1e3/3.0856775814913673e22
E_c = 46.27
E_L = out["B_E_Lambda_MeV"]
ratio = E_c/E_L
out["C_Ec_over_EL"] = ratio
out["C_(Hc/HL)^(1/3)"] = (H_c/H_L)**(1/3)
out["C_(Hc/HL)^(2/3)"] = (H_c/H_L)**(2/3)
check("C_exponent_is_one_third", ratio, (H_c/H_L)**(1/3), rtol=3e-3)
out["C_relative_miss_if_two_thirds"] = round(abs(ratio - (H_c/H_L)**(2/3))/ratio, 3)
out["C_verdict"] = "E ~ H^(1/3) from lambda^3 ~ R; the two 'grains' are one function m_cap(N) at two epochs"

if "--json" in sys.argv:
    print(json.dumps({"results": out, "failures": FAIL}, indent=2, default=str))
else:
    for k, v in out.items(): print(f"{k:44s} {v}")
    print("FAILURES:", FAIL if FAIL else "none")
sys.exit(1 if FAIL else 0)

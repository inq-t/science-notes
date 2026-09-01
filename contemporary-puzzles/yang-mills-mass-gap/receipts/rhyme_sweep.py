#!/usr/bin/env python3
"""Rhyme sweep of the causal grain against QCD/hadronic scales. Stdlib only; exit nonzero on failure.

What a pass establishes: that the grain mass m* (46.27 MeV on the CMB-conditional
crossing branch, 47.21 MeV on the Cepheid branch) has NO numerical rhyme with any
scale of Yang-Mills or QCD beyond the chance rate, and that the seductive
"ln(m_P/m*) ~ 47 ~ m*/MeV" coincidence is a unit artifact. It does NOT establish
anything about the grain itself; it is a negative result and a trap census.

Checks
  1. Grid: 21 scales x 46 distinct factors x 2 branches = 1932 trials; hits are |m* f - s|/s < 1%.
     The scale list deliberately carries two 0++ glueball determinations, both pion charge
     states, both f_pi conventions, and both m_p and m_p/3; trials are therefore correlated
     and 1932 overstates the independent count. The empirical control in check 4 does not
     depend on that count.
  2. Null test: a two-sided Poisson tail test of the observed hit count against the analytic
     base rate (log-uniform ratios over ~[0.1, 100] give 2%/ln(1000) ~ 0.29% per trial).
     Fails if min(P(N>=n), P(N<=n)) < 0.025.
  3. Branch stability: assert ZERO hits survive on both branches (the 2% branch spread exceeds
     the 1% tolerance, so no branch-independent 1%-level rhyme is statable).
  4. Empirical negative control: 4000 seeded fake grains, log-uniform in [20, 200] MeV, swept
     identically. Reports the hit-count distribution; fails if either real branch's hit count
     falls outside the fakes' central 95% interval, i.e. if the grain were anomalously rhyming.
  5. Unit artifact (report only, nothing to assert): ln(m_P/m*) is dimensionless; the count
     m*/unit is not. Both are printed in MeV and GeV.
  6. Correlation length (report only): hbar c / m(0++) vs the grain length, ratio ~36-37.
"""
import json, math, sys, random

FAIL = []
def check(name, cond, detail=None):
    if not cond: FAIL.append((name, detail))
    return cond

MSTAR = {"CMB": 46.27, "Cepheid": 47.21}          # MeV, diagnostic inversions (grain module)
MP_MEV = 1.220890e22                             # Planck mass energy, MeV

SCALES = {  # MeV; sources: PDG (masses, f_pi, Lambda), lattice (glueballs, string tension)
    "m_e": 0.51100, "m_u+m_d": 6.8, "f_pi(92)": 92.07, "m_s(2GeV)": 93.4, "m_mu": 105.658,
    "f_pi(130)": 130.2, "m_pi0": 134.977, "m_pi+": 139.570, "Lambda_MS_nf5": 210.0,
    "Lambda_MS_nf0": 260.0, "m_p/3": 312.757, "Lambda_MS_nf3": 332.0, "sqrt_sigma": 440.0,
    "m_K": 493.677, "m_eta": 547.86, "m_rho": 775.26, "m_p": 938.272, "4pi_f_pi": 4*math.pi*92.07,
    "glueball_0++_MP": 1653.0, "glueball_0++_Chen": 1730.0, "glueball_2++": 2390.0,
}
FACT = {}
for n in range(1, 13): FACT[f"{n}"] = float(n); FACT[f"1/{n}"] = 1.0/n
for n in range(1, 7):  FACT[f"{n}pi"] = n*math.pi; FACT[f"1/({n}pi)"] = 1.0/(n*math.pi)
FACT.update({"pi^2": math.pi**2, "2pi^2": 2*math.pi**2, "4pi^2": 4*math.pi**2,
             "sqrt2": math.sqrt(2), "sqrt3": math.sqrt(3), "3/2": 1.5, "2/3": 2/3, "8/3": 8/3,
             "3/8": 0.375, "e": math.e, "e^2": math.e**2})
# deduplicate factors by value ("1" and "1/1" coincide)
_seen = {}
for k, v in list(FACT.items()):
    key = round(v, 12)
    if key in _seen: del FACT[k]
    else: _seen[key] = k

def sweep(masses, tol=0.01):
    hits = {}
    trials = 0
    for br, m in masses.items():
        for sn, s in SCALES.items():
            for fn, f in FACT.items():
                trials += 1
                if abs(m*f - s)/s < tol:
                    hits.setdefault((sn, fn), set()).add(br)
    return trials, hits

def poisson_cdf(n, lam):
    return sum(math.exp(-lam) * lam**k / math.factorial(k) for k in range(n+1))

out = {}
trials, hits = sweep(MSTAR)
n_hits = sum(len(v) for v in hits.values())
per_branch = {br: sum(1 for b in hits.values() if br in b) for br in MSTAR}
expected = trials * 0.02 / math.log(1000.0)
out["1_trials"] = trials; out["1_distinct_factors"] = len(FACT); out["1_hits"] = n_hits
out["1_hits_per_branch"] = per_branch
out["1_hit_list"] = sorted(f"{sn} ~ m* x {fn} [{','.join(sorted(b))}]" for (sn, fn), b in hits.items())
check("1_grid_size", trials == len(SCALES)*len(FACT)*len(MSTAR), trials)

# 2. two-sided Poisson tail test against the analytic base rate
p_le = poisson_cdf(n_hits, expected); p_ge = 1.0 - poisson_cdf(n_hits-1, expected)
out["2_expected_by_chance_analytic"] = round(expected, 2)
out["2_poisson_P(N<=n)"] = round(p_le, 3); out["2_poisson_P(N>=n)"] = round(p_ge, 3)
check("2_null_not_rejected", min(p_le, p_ge) >= 0.025, (n_hits, expected, p_le, p_ge))

# 3. branch stability
stable = [k for k, b in hits.items() if len(b) == 2]
out["3_branch_stable_hits"] = len(stable)
check("3_zero_branch_stable", len(stable) == 0, stable)

# 4. empirical negative control: many theory-free fake grains, same sweep
rng = random.Random(20260901)
fake_counts = []
for _ in range(4000):
    mf = math.exp(rng.uniform(math.log(20.0), math.log(200.0)))
    _, hf = sweep({"fake": mf})
    fake_counts.append(sum(len(v) for v in hf.values()))
fake_counts.sort()
lo95, hi95 = fake_counts[int(0.025*len(fake_counts))], fake_counts[int(0.975*len(fake_counts))-1]
mean_fake = sum(fake_counts)/len(fake_counts)
out["4_fake_grains"] = len(fake_counts)
out["4_fake_mean_hits_per_grain"] = round(mean_fake, 3)
out["4_fake_central_95pct"] = [lo95, hi95]
out["4_analytic_expected_per_grain"] = round(expected/len(MSTAR), 3)
for br, n in per_branch.items():
    check(f"4_real_branch_within_fake_95pct_{br}", lo95 <= n <= hi95, (br, n, lo95, hi95))

# 5. unit artifact -- report only; the log is dimensionless by construction
for br, m in MSTAR.items():
    out[f"5_ln_mP_over_mstar_{br}"] = round(math.log(MP_MEV/m), 4)
    out[f"5_mstar_in_MeV_{br}"] = m; out[f"5_mstar_in_GeV_{br}"] = m/1000.0
out["5_note"] = "ln(m_P/m*) ~ 47.0 on both branches; the count m*/MeV ~ 46-47 changes to 0.046-0.047 in GeV"

# 6. correlation length -- report only
hbarc = 197.3269804
out["6_gap_length_fm_range"] = [round(hbarc/1730.0, 4), round(hbarc/1653.0, 4)]
out["6_grain_length_fm_branches"] = {"CMB": round(hbarc/46.27, 4), "Cepheid": round(hbarc/47.21, 4)}
out["6_grain_over_gap_range"] = [round((hbarc/47.21)/(hbarc/1653.0), 1), round((hbarc/46.27)/(hbarc/1730.0), 1)]
out["6_lattice_consistent_pure_numbers"] = {"m0pp_over_sqrt_sigma_LuciniTeper": 3.55,
                                            "m0pp_over_sqrt_sigma_convention_mixed_1730_over_440": round(1730/440, 2),
                                            "m2pp_over_m0pp": round(2390/1730, 2)}

if "--json" in sys.argv:
    print(json.dumps({"results": out, "failures": FAIL}, indent=2, default=str))
else:
    for k, v in out.items():
        if isinstance(v, list):
            print(k); [print("   ", x) for x in v]
        else: print(f"{k:36s} {v}")
    print("FAILURES:", FAIL if FAIL else "none")
sys.exit(1 if FAIL else 0)

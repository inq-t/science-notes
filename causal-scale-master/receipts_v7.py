#!/usr/bin/env python3
"""Exact and numerical receipts for Causal Scale Dynamics v7.0.

The script checks algebraic consequences only. It does not prove the physical
Scale-Capacity Equivalence Principle, geometric modular flow for FLRW, or a
covariant perturbation completion.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.optimize import brentq

out: dict[str, object] = {}

# 1. Binary/BKM geometry
th = sp.symbols('theta', real=True)
Psi = sp.log(2*sp.cosh(th))
eta = sp.diff(Psi, th)
g = sp.simplify(sp.diff(Psi, th, 2))
SJ = sp.simplify(4*th*sp.tanh(th))
out['binary_geometry'] = {
    'eta': str(eta),
    'metric': str(g),
    'normalization_residual': str(sp.simplify(eta**2 + g - 1)),
    'symmetrized_relative_entropy': str(SJ),
    'self_dual_value': str(sp.simplify(SJ.subs(th,0))),
    'self_dual_first_derivative': str(sp.simplify(sp.diff(SJ,th).subs(th,0))),
    'self_dual_second_derivative': str(sp.simplify(sp.diff(SJ,th,2).subs(th,0))),
    'fisher_length': 'pi',
}

# 2. Shape law and conservation
N, Nc, varrho = sp.symbols('N N_c varrho', real=True, positive=True)
thetaN = varrho*(N-Nc)
y = sp.sech(thetaN)**2
Delta = sp.simplify(-sp.diff(sp.log(y),N))
w = sp.simplify(-1+Delta/3)
out['shape_law'] = {
    'Delta': str(Delta),
    'w': str(w),
    'invariant_residual': str(sp.simplify(9*(1+w)**2 + 6*sp.diff(w,N) - 4*varrho**2)),
    'conic_residual': str(sp.simplify(y + sp.diff(sp.log(y),N)**2/(4*varrho**2)-1)),
    'riccati_residual': str(sp.simplify(sp.diff(Delta,N) - (2*varrho**2-Delta**2/2))),
}

# 3. Witten/Darboux pair
D = sp.Function('D')
# algebraic potentials W^2 +/- W', W=tanh(theta)
W = sp.tanh(th)
Vminus = sp.simplify(W**2 - sp.diff(W,th))
Vplus = sp.simplify(W**2 + sp.diff(W,th))
psi0 = sp.sech(th)/sp.sqrt(2)
zero_mode_residual = sp.simplify(sp.diff(psi0,th)+W*psi0)
out['witten_pair'] = {
    'V_minus': str(Vminus),
    'V_plus': str(Vplus),
    'zero_mode_residual': str(zero_mode_residual),
    'zero_mode_norm_density_relation': str(sp.simplify(2*psi0**2-g)),
}

# 4. Relative free-energy Hessian and scale-capacity identities
# Symbolic placeholders: GNN = R*Sbar; kBT*Sbar/V = 2/(d-1) rho_crit
Ruble, d, rhocrit = sp.symbols('Ruble d rho_crit', positive=True)
OmegaX = sp.simplify(Ruble/(d-1))
rord = sp.simplify(OmegaX/(1-OmegaX))
out['dimension_generalization'] = {
    'Omega_X_crossing': str(OmegaX),
    'r_ordinary_crossing': str(rord),
    'unit_Ruble_ratio': str(sp.simplify(rord.subs(Ruble,1))),
    'd3_unit_Ruble_ratio': str(sp.simplify(rord.subs({Ruble:1,d:3}))),
}

# 5. Hawking-Friedmann conversion in 3+1 dimensions
R,c,G,hbar,kB = sp.symbols('R c G hbar k_B', positive=True)
A = 4*sp.pi*R**2
V = 4*sp.pi*R**3/3
Sbar = sp.simplify(A*c**3/(4*G*hbar))
kBT = hbar*c/(2*sp.pi*R)
Ems = c**4*R/(2*G)
out['hawking_friedmann'] = {
    'kBT_times_dimensionless_entropy_minus_Ems': str(sp.simplify(kBT*Sbar-Ems)),
    'energy_density': str(sp.simplify(Ems/V)),
    'source_amplitude_for_unit_Ruble': str(sp.simplify(kBT*Sbar/(2*V))),
}

# 6. Central shift invariance
beta,C,E1,E2 = sp.symbols('beta C E1 E2', real=True)
p1_shift = sp.exp(-beta*(E1+C))/(sp.exp(-beta*(E1+C))+sp.exp(-beta*(E2+C)))
p1 = sp.exp(-beta*E1)/(sp.exp(-beta*E1)+sp.exp(-beta*E2))
out['central_shift'] = {'gibbs_probability_residual': str(sp.simplify(p1_shift-p1))}

# 7. Benchmark with capacity-normalized ordinary-sector equality
Om0=0.310598
Or0=9.15e-5

def root_eq(Nc_: float) -> float:
    rho_ord=Om0*np.exp(-3*Nc_)+Or0*np.exp(-4*Nc_)
    return Om0+Or0+rho_ord/np.cosh(Nc_)**2-1
Nc_num=brentq(root_eq,-2,0)
rho_star=Om0*np.exp(-3*Nc_num)+Or0*np.exp(-4*Nc_num)

def comps(x: float):
    rm=Om0*np.exp(-3*x)
    rr=Or0*np.exp(-4*x)
    rx=rho_star/np.cosh(x-Nc_num)**2
    wx=-1+(2/3)*np.tanh(x-Nc_num)
    return rm,rr,rx,wx

def qnum(x: float):
    rm,rr,rx,wx=comps(x)
    return -1+1.5*(rm+(4/3)*rr+rx*(1+wx))/(rm+rr+rx)

h=1e-5
q0=qnum(0.0)
dq=(qnum(h)-qnum(-h))/(2*h)
j0=q0+2*q0*q0-dq
Nentry=brentq(qnum,-1.5,Nc_num)
Nexit=brentq(qnum,0.1,5)
rmc=Om0*np.exp(-3*Nc_num)
rrc=Or0*np.exp(-4*Nc_num)
out['benchmark']={
    'Omega_m0':Om0,'Omega_r0':Or0,
    'N_c':Nc_num,'z_c':np.exp(-Nc_num)-1,
    'rho_star_over_rhocrit0':rho_star,
    'rho_star_over_matter_at_crossing':rho_star/rmc,
    'rho_star_over_all_ordinary_at_crossing':rho_star/(rmc+rrc),
    'Omega_r_at_crossing':rrc/(rmc+rrc+rho_star),
    'Omega_X_at_crossing':rho_star/(rmc+rrc+rho_star),
    'w0':-1+(2/3)*np.tanh(-Nc_num),
    'wa_tangent':-(2/3)/np.cosh(-Nc_num)**2,
    'q_crossing':qnum(Nc_num),
    'mu_A_crossing':(1-qnum(Nc_num))/2,
    'q0':q0,'j0':j0,
    'z_acceleration_entry':np.exp(-Nentry)-1,
    'a_exit_over_a0':np.exp(Nexit),
    'shape_invariant':4.0,
    'Ruble_number':1.0,
}

# 8. Exact residual ledger
res=[]
for sec,v in out.items():
    if isinstance(v,dict):
        for k,val in v.items():
            if 'residual' in k and isinstance(val,str): res.append(val)
out['all_exact_residuals_zero']=all(x=='0' for x in res)

path=Path(__file__).with_name('receipts_v7.json')
path.write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))

#!/usr/bin/env python3
"""
receipts_transparency_fold.py
=============================
Verification receipts for: "Transparency, Binariness, and the Fold"
Modular-Weyl programme -- structural derivations on the rigid branch.

Every numbered receipt corresponds to a labelled claim in the hand-off document.
Run:  python3 receipts_transparency_fold.py
No external data required. numpy + scipy only.
"""
import numpy as np
from scipy.optimize import brentq, curve_fit
from scipy.integrate import quad

# ---- fiducial background (from Direct_CMB_Response_Test sec. 4) -------------
OM, OR   = 0.310598, 8.5e-5
OM_LCDM  = 0.314957          # CMB-distance-matched flat LCDM comparator
BANNER   = "=" * 78

def solve_Nc(Om, Or, vp):
    """Flat normalisation on the r_c = 1 branch: rho_* = rho_m(N_c)."""
    return brentq(lambda Nc: Om + Or + Om*np.exp(-3*Nc)/np.cosh(vp*Nc)**2 - 1.0,
                  -3.0, 2.0, xtol=1e-14)

def d1(f, N, h=1e-5): return (f(N+h) - f(N-h)) / (2*h)
def d2(f, N, h=1e-4): return (f(N+h) - 2*f(N) + f(N-h)) / h**2


# ============================================================ R1 : T5, T6
def receipt_1():
    print(BANNER); print("R1  binary family -> sech^2, the Q^2=1 invariant, Fisher length pi")
    print(BANNER)
    th = np.linspace(-8, 8, 200001)
    pp, pm = np.exp(th)/(2*np.cosh(th)), np.exp(-th)/(2*np.cosh(th))
    meanQ = pp - pm
    varQ  = 1.0 - meanQ**2
    print(f"  max |<Q> - tanh(th)|         = {np.max(np.abs(meanQ-np.tanh(th))):.3e}")
    print(f"  max |Var(Q) - sech^2(th)|    = {np.max(np.abs(varQ-1/np.cosh(th)**2)):.3e}")
    print(f"  max |<Q>^2 + Var(Q) - 1|     = {np.max(np.abs(meanQ**2+varQ-1.0)):.3e}   [T6]")
    dp = 0.5/np.cosh(th)**2
    gF = dp**2/(pp*pm)
    print(f"  max |g_Fisher - sech^2(th)|  = {np.max(np.abs(gF-1/np.cosh(th)**2)):.3e}")
    L, _  = quad(lambda t: 1/np.cosh(t), -30, 30)
    D, _  = quad(lambda p: 1/np.sqrt(p*(1-p)), 0.0, 1.0)
    print(f"  Fisher length  int sech dth  = {L:.12f}")
    print(f"  simplex diameter             = {D:.12f}   pi = {np.pi:.12f}   [T5]")
    print("  => the crossover traverses the ENTIRE binary state space, pure to pure.")
    print("  => the traversed length is varrho-independent.\n")


# ============================================================ R2 : T6
def receipt_2():
    print(BANNER); print("R2  exact invariant  9(1+w)^2 + 6 w' = 4 varrho^2   [T6]")
    print(BANNER)
    for vp in [0.6, 0.8, 1.0, 1.2, 1.4, 1.5]:
        Nc = solve_Nc(OM, OR, vp)
        u  = np.linspace(-4, 4, 40001)
        w  = -1 + (2*vp/3)*np.tanh(vp*u)
        inv = 9*(1+w)**2 + 6*np.gradient(w, u)
        print(f"  varrho={vp:4.2f}  N_c={Nc:+.6f}  z_c={np.exp(-Nc)-1:.5f}"
              f"  <inv>={inv.mean():.9f}  (4v^2={4*vp**2:.6f})  sd={inv.std():.1e}")
    print("  => the invariant is exactly <Q>^2 + Var(Q) = <Q^2> = 1, rescaled by 4varrho^2.\n")


# ============================================================ R3 : T2
def receipt_3():
    print(BANNER); print("R3  A2 saddle-node normal form in the (X, X') phase plane   [T2]")
    print(BANNER)
    print("  X := 1+w  obeys   X' = A - B X^2,  A = (2/3)varrho^2,  B = 3/2 (fixed by gravity)")
    for vp in [0.0, 0.5, 1.0, 1.5]:
        A, B = (2/3)*vp**2, 1.5
        if A > 0:
            Xf = np.sqrt(A/B)
            print(f"  varrho={vp:4.2f}  A={A:.6f}   X* = +-{Xf:.6f}"
                  f"   w_past={-1-Xf:+.6f}  w_future={-1+Xf:+.6f}")
        else:
            print(f"  varrho={vp:4.2f}  A={A:.6f}   fixed points MERGED  <-- A2 FOLD POINT")
    vp = 1.0; A, B = (2/3)*vp**2, 1.5
    u = np.linspace(-6, 6, 60001)
    X = (2*vp/3)*np.tanh(vp*u)
    print(f"  residual max |X' - (A - B X^2)| = {np.max(np.abs(np.gradient(X,u)-(A-B*X**2))):.2e}")
    print("  rescaling X=(2v/3)u_hat, tau=vN gives the canonical form  du/dtau = 1 - u^2.")
    print("  => varrho is the normal-form scaling; varrho=0 is the fold.\n")


# ============================================================ R4 : T3
def receipt_4():
    print(BANNER); print("R4  future attractor, deceleration, event horizon   [T3]")
    print(BANNER)
    print("  Dark-dominated future: E ~ exp(-sN), s = (3/2)(1+w_inf).")
    print("  Comoving event horizon  int dN/(aH) ~ int exp((s-1)N) dN  converges iff s<1,")
    print("  i.e. iff w_inf < -1/3.")
    print("   varrho    w_inf     q_inf    a(t)~t^p    event horizon")
    for vp in [0.7, 0.9, 1.0, 1.1, 1.3]:
        wf = -1 + (2/3)*vp
        s  = 1.5*(1+wf)
        eh = "YES" if s < 1-1e-12 else ("MARGINAL - none" if abs(s-1) < 1e-12 else "no")
        print(f"   {vp:5.2f}  {wf:+8.5f}  {0.5*(1+3*wf):+7.4f}   {2/(3*(1+wf)):7.4f}    {eh}")
    print("  => varrho = 1 is the UNIQUE value with q_inf = 0 exactly:")
    print("     the future attractor sits on the acceleration separatrix, a(t) ~ t,")
    print("     and the event horizon is marginally absent (asymptotic observables exist).\n")


# ============================================================ R5 : T1
def receipt_5():
    print(BANNER); print("R5  theta-frame reduction: Poschl-Teller strength is chi_perp   [T1]")
    print(BANNER)
    print("  Given   psi_NN + [K^2 + c rho_X] psi = 0,  rho_X = chi_perp varrho^2 sech^2(varrho u)")
    print("  set theta = varrho u.  Then d^2/dN^2 = varrho^2 d^2/dtheta^2 and")
    print("     psi_thth + [K^2/varrho^2 + c chi_perp sech^2(theta)] psi = 0.")
    print("  Lambda = c chi_perp is INDEPENDENT of varrho: the varrho^2 in rho_X (from")
    print("  the pullback (dtheta/dN)^2) cancels the varrho^2 from the chain rule.")
    print("  Equivalently  X_sigma dN^2 = sech^2(theta) dtheta^2  is varrho-free.\n")
    def T_coef(Lam, k):
        lam = 0.5*(-1 + np.sqrt(1 + 4*Lam + 0j))
        s2  = np.sinh(np.pi*k)**2
        return float(np.real(s2/(s2 + np.cos(np.pi*(lam+0.5))**2)))
    print("   Lambda      ell        |R|^2 (k=0.7)     status")
    for Lam in [0.5, 2.0, 3.7, 6.0, 12.0]:
        ell = 0.5*(-1 + np.sqrt(1 + 4*Lam))
        R   = 1 - T_coef(Lam, 0.7)
        tag = "REFLECTIONLESS" if abs(ell - round(ell)) < 1e-9 else ""
        print(f"   {Lam:6.3f}   {ell:8.6f}    {R:.4e}      {tag}")
    print("  Transparency <=> c chi_perp = l(l+1).  l=1 -> c chi_perp = 2, one bound state.\n")


# ============================================================ R6 : NEGATIVE
def receipt_6():
    print(BANNER); print("R6  [NEGATIVE] the growth operator is NOT of Poschl-Teller type")
    print(BANNER)
    vp = 1.0; Nc = solve_Nc(OM, OR, vp)
    E2X = lambda N: OM*np.exp(-3*N)+OR*np.exp(-4*N)+OM*np.exp(-3*Nc)/np.cosh(vp*(N-Nc))**2
    E2L = lambda N: OM_LCDM*np.exp(-3*N)+OR*np.exp(-4*N)+(1-OM_LCDM-OR)
    def W(E2f, Om):
        lnE = lambda x: 0.5*np.log(E2f(x))
        return lambda N: (2+d1(lnE,N))**2/4 + d2(lnE,N)/2 + 1.5*Om*np.exp(-3*N)/E2f(N)
    WX, WL = W(E2X, OM), W(E2L, OM_LCDM)
    Ns  = np.linspace(-4, 3, 1401)
    dW  = np.array([WX(N)-WL(N) for N in Ns])
    rho = OM*np.exp(-3*Nc)/np.cosh(vp*(Ns-Nc))**2
    r   = dW/rho
    print("  D'' + (2 + dlnH/dN) D' - (3/2)Om(N) D = 0  ->  psi'' = W psi,")
    print("  W = (2+h)^2/4 + h'/2 + (3/2)Om(N),  psi = D a sqrt(H).")
    print(f"  ratio dW/Omega_X spans {r.min():+.3f} .. {r.max():+.3f}  (would be CONSTANT if T1 applied)")
    fit = lambda N, A, nc, v: A/np.cosh(v*(N-nc))**2
    try:
        p, _ = curve_fit(fit, Ns, dW, p0=[dW.max(), Nc, vp], maxfev=40000)
        res  = np.sqrt(np.mean((dW-fit(Ns,*p))**2))
        print(f"  best free sech^2 fit: A={p[0]:+.5f} N_c={p[1]:+.4f} varrho_fit={p[2]:.4f}")
        print(f"  fractional RMS residual = {res/np.abs(dW).max():.1%}   <-- FIT FAILS")
    except Exception as e:
        print(f"  fit failed outright: {e}")
    print("  => T1's hypothesis does NOT hold for the growth operator. The growth")
    print("     equation is a ZERO-ENERGY problem in N with no scattering channel;")
    print("     transparency must be sought in the dark-sector perturbation operator.\n")


# ============================================================ R7 : no-go
def receipt_7():
    print(BANNER); print("R7  single-field completion: the crossing no-go, quantified")
    print(BANNER)
    vp = 1.0
    print("  Mukhanov-Sasaki  v'' + (c_s^2 k^2 - z''/z)v = 0,")
    print("  z^2 ~ a^2(rho_X + p_X)/(c_s^2 H^2)  proportional to (1+w_X) = (2v/3)tanh(theta).")
    print("  (a) 1+w_X < 0 for ALL theta < 0: wrong-sign kinetic term over the whole")
    print("      pre-crossing era. A ghost, not a localised defect.")
    print("  (b) near theta = 0, z ~ |theta|^{1/2}:")
    zz = lambda x: np.sqrt(np.abs(np.tanh(x)))
    for e in [1e-2, 1e-3, 1e-4, 1e-5]:
        v = d2(zz, e, h=e/20)/zz(e)
        print(f"      theta={e:.0e}:  z''/z = {v:+16.4f}   -(1/4)/theta^2 = {-0.25/e**2:+16.4f}"
              f"   ratio {v/(-0.25/e**2):.6f}")
    print("  => z''/z -> -(1/4)/theta^2: inverse-square at EXACTLY the critical")
    print("     coupling g = 1/4 for fall-to-the-centre. Critically marginal.\n")


# ============================================================ R8 : T4
def receipt_8():
    print(BANNER); print("R8  [NEW] existence ceiling on varrho from flatness + r_c = 1   [T4]")
    print(BANNER)
    print("  Flatness:  Om e^{-3Nc} sech^2(v Nc) = 1 - Om - Or.")
    print("  With x = -Nc > 0:  F(x) = e^{3x} sech^2(v x) = T := (1-Om-Or)/Om.")
    print("  dlnF/dx = 3 - 2 v tanh(v x).")
    print("    v <= 3/2 : F strictly increasing -> unique root, always exists.")
    print("    v >  3/2 : F rises then decays -> root exists only if Fmax(v) >= T.")
    print("  Double root (fold) when F(x*)=T and F'(x*)=0, i.e. tanh(v x*) = 3/(2v):")
    print("     T_ceiling(v) = (1 - 9/(4v^2)) exp[(3/v) artanh(3/(2v))],   v > 3/2\n")
    Tc = lambda v: (1-9/(4*v**2))*np.exp((3/v)*np.arctanh(3/(2*v)))
    print("     v        T_ceiling")
    for v in [1.55, 1.6, 1.7, 1.8, 1.9, 2.0, 2.5]:
        print(f"   {v:6.3f}    {Tc(v):10.6f}")
    print("\n     Om        T        varrho_max")
    for Om in [0.28, 0.30, 0.310598, 0.32, 0.34]:
        T = (1-Om-OR)/Om
        vm = brentq(lambda v: Tc(v)-T, 1.5000001, 30, xtol=1e-13)
        print(f"   {Om:.6f}  {T:7.4f}   {vm:9.6f}")
    T = (1-OM-OR)/OM
    vmax = brentq(lambda v: Tc(v)-T, 1.5000001, 30, xtol=1e-13)
    xs = np.arctanh(3/(2*vmax))/vmax
    print(f"\n  fiducial Om={OM}:  varrho_max = {vmax:.9f}")
    print(f"  at the ceiling the two roots merge at N_c = {-xs:.6f} (z_c = {np.exp(xs)-1:.5f})")
    print(f"  varrho = 1 sits at {1/vmax:.4f} of the ceiling -- NOT saturating.")
    print("  => a SECOND A2 fold, this one in the moduli of solutions rather than")
    print("     in the phase plane: two crossing epochs merge and annihilate.\n")


# ============================================================ R9 : predictions
def receipt_9():
    print(BANNER); print("R9  observable map  varrho -> (z_c, w_0, w_a)  and the inverse estimator")
    print(BANNER)
    print("   varrho     N_c        z_c       w_0        w_a     [9(1+w0)^2-6wa]/4")
    for v in [0.7, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.2, 1.4]:
        nc = solve_Nc(OM, OR, v)
        w0 = -1 + (2*v/3)*np.tanh(-v*nc)
        wa = -(2*v**2/3)/np.cosh(v*nc)**2
        print(f"   {v:5.2f}   {nc:+.5f}   {np.exp(-nc)-1:.5f}   {w0:+.5f}  {wa:+.5f}"
              f"    {(9*(1+w0)**2-6*wa)/4:.6f}  (v^2={v**2:.4f})")
    print("\n  Inverse estimator  varrho^2 = [9(1+w_0)^2 - 6 w_a]/4  on published CPL fits")
    print("  (correlation rho(w0,wa) = -0.9 assumed; substitute the real covariance):")
    def est(w0, wa, s0, sa, rc=-0.9):
        v2 = (9*(1+w0)**2 - 6*wa)/4
        a, b = 4.5*(1+w0), -1.5
        var = (a*s0)**2 + (b*sa)**2 + 2*a*b*rc*s0*sa
        return np.sqrt(v2), np.sqrt(var)/(2*np.sqrt(v2))
    for lbl, args in {
        "DESI DR2 + CMB + Pantheon+": (-0.838, -0.62,  0.055, 0.205),
        "DESI DR2 + CMB  (no SN)   ": (-0.42,  -1.75,  0.21,  0.58),
    }.items():
        v, s = est(*args)
        print(f"    {lbl}:  varrho = {v:.3f} +- {s:.3f}")
    Tc = lambda v: (1-9/(4*v**2))*np.exp((3/v)*np.arctanh(3/(2*v)))
    vmax = brentq(lambda v: Tc(v)-(1-OM-OR)/OM, 1.5000001, 30)
    print(f"\n  ceiling varrho_max = {vmax:.5f}  ->  the no-SN determination sits AT the")
    print("  boundary of the r_c=1 branch. Boundary-dominated, exactly the pathology")
    print("  diagnosed for Sum m_nu >= 0 one level down.\n")


# ============================================================ R10 : T8
def solve_Nc_rc(Om, Or, vp, rc):
    """Flatness with general r_c: rho_* = r_c rho_m(N_c)."""
    return brentq(lambda Nc: Om + Or + rc*Om*np.exp(-3*Nc)/np.cosh(vp*Nc)**2 - 1.0,
                  -6.0, 3.0, xtol=1e-14)

def receipt_10():
    print(BANNER); print("R10 what r_c = 1 says: a three-epoch identification   [T8]")
    print(BANNER)
    vp, rc = 1.0, 1.0
    Nc = solve_Nc_rc(OM, OR, vp, rc)
    print("  rho_X/rho_m = r_c sech^2(theta) exp(3 theta / varrho)")
    print("  d/dtheta ln(rho_X/rho_m) = -2 tanh(theta) + 3/varrho > 0 for varrho < 3/2")
    print("  => strictly monotone: matter-dark equality is UNIQUE, and at theta = 0")
    print("     the ratio equals r_c exactly.\n")
    rhoX = lambda N: rc*OM*np.exp(-3*Nc)/np.cosh(vp*(N-Nc))**2
    rhom = lambda N: OM*np.exp(-3*N)
    E2   = lambda N: rhom(N) + OR*np.exp(-4*N) + rhoX(N)
    def qN(N):
        wx = -1 + (2*vp/3)*np.tanh(vp*(N-Nc))
        return 0.5*(rhom(N) + 2*OR*np.exp(-4*N) + rhoX(N)*(1+3*wx))/E2(N)
    zeq  = np.exp(-brentq(lambda N: rhoX(N)-rhom(N), -4, 3)) - 1
    zacc = np.exp(-brentq(qN, -2, 1)) - 1
    print(f"    (a) susceptibility peak / w_X = -1 crossing : z = {np.exp(-Nc)-1:.5f}")
    print(f"    (b) matter-dark equality                    : z = {zeq:.5f}   <- identified by r_c=1")
    print(f"    (c) acceleration onset  (q = 0)             : z = {zacc:.5f}   <- DERIVED, not input")
    print("\n  Is (a)=(b) nontrivial? Test on the DESI CPL best fit (w0=-0.838, wa=-0.62):")
    w0, wa, OmL = -0.838, -0.62, 0.3106
    zcr = 1/(1 - (-1-w0)/wa) - 1
    rde = lambda a: a**(-3*(1+w0+wa))*np.exp(-3*wa*(1-a))
    aeq = brentq(lambda a: (1-OmL)*rde(a) - OmL*a**-3, 0.05, 2.0)
    print(f"    CPL  w = -1 crossing   : z = {zcr:.5f}")
    print(f"    CPL  matter-DE equality: z = {1/aeq-1:.5f}     separation dz = {zcr-(1/aeq-1):+.5f}")
    print("  => generic dark energy does NOT identify these epochs.")
    print("     r_c = 1 is a falsifiable coincidence claim, not a convention.\n")


# ============================================================ R11 : T9
def receipt_11():
    print(BANNER); print("R11 the shape invariant is blind to r_c -> separability   [T9]")
    print(BANNER)
    print("  r_c is a pure AMPLITUDE: w_X = -1 + (2v/3)tanh(v(N-N_c)) does not contain it.")
    print("  Hence 9(1+w)^2 + 6w' = 4 varrho^2 for every r_c.\n")
    vp = 1.0
    print("    r_c    N_c        z_c        w_0        w_a      invariant")
    for rc in [0.5, 0.8, 1.0, 1.5, 2.0, 3.0]:
        nc = solve_Nc_rc(OM, OR, vp, rc)
        w0 = -1 + (2*vp/3)*np.tanh(-vp*nc)
        wa = -(2*vp**2/3)/np.cosh(vp*nc)**2
        print(f"   {rc:5.2f}  {nc:+.5f}  {np.exp(-nc)-1:8.5f}  {w0:+.5f}  {wa:+.5f}"
              f"   {9*(1+w0)**2-6*wa:.6f}")
    print("\n  Distances trade r_c against varrho along a degeneracy:")
    print("    varrho   r_c    z_c        w_0        w_a     invariant   4varrho^2")
    for v, rc in [(1.0,1.00), (1.2,0.72), (1.4,0.55)]:
        nc = solve_Nc_rc(OM, OR, v, rc)
        w0 = -1 + (2*v/3)*np.tanh(-v*nc)
        wa = -(2*v**2/3)/np.cosh(v*nc)**2
        print(f"     {v:4.2f}  {rc:5.2f}  {np.exp(-nc)-1:8.5f}  {w0:+.5f}  {wa:+.5f}"
              f"   {9*(1+w0)**2-6*wa:9.5f}  {4*v**2:9.5f}")
    print("\n  => the invariant fixes varrho INDEPENDENTLY of r_c; the residual")
    print("     amplitude then fixes r_c. The observed degeneracy is a DATA")
    print("     degeneracy, not a structural one, and P1 breaks it.\n")


# ============================================================ R12 : T10
def receipt_12():
    print(BANNER); print("R12 the T4 ceiling scales with r_c   [T10]")
    print(BANNER)
    print("  F(x) = r_c e^{3x} sech^2(varrho x) = T  =>  ceiling condition is on T/r_c:")
    print("     T/r_c = (1 - 9/(4v^2)) exp[(3/v) artanh(3/(2v))]\n")
    Tc = lambda v: (1-9/(4*v**2))*np.exp((3/v)*np.arctanh(3/(2*v)))
    T  = (1-OM-OR)/OM
    print("     r_c    varrho_max")
    for rc in [0.5, 0.8, 1.0, 1.5, 2.0, 5.0]:
        try:
            print(f"    {rc:5.2f}   {brentq(lambda v: Tc(v)-T/rc, 1.5000001, 60, xtol=1e-13):9.5f}")
        except Exception:
            print(f"    {rc:5.2f}   unbounded (T/r_c < 1)")
    print("\n  => raising r_c raises the ceiling. A fit that frees r_c and drifts to")
    print("     varrho ~ 1.7-1.8 is moving ALONG this degeneracy toward a MOVING")
    print("     boundary. Report such fits as boundary-dominated, not as evidence.\n")


# ============================================================ R13 : T11
def _p(th):  return np.array([np.exp(th), np.exp(-th)])/(2*np.cosh(th))
def _S(r, s): return float(np.sum(r*np.log(r/s)))
def SJ(th):  return _S(_p(th), _p(-th)) + _S(_p(-th), _p(th))

def receipt_13():
    print(BANNER); print("R13 the binary family is a Chatterjee self-dual family   [T11]")
    print(BANNER)
    print("  Chatterjee arXiv:2605.19106 Eq.(29)-(33):  rho_J = J rho J = rho(r(g)),")
    print("  S_J(g) = S(rho||rho_J) + S(rho_J||rho),  self-dual point r(g*)=g*.")
    print("  Here JQJ = -Q  =>  rho_J(theta) = rho_{-theta}  =>  r(theta) = -theta,")
    print("  and Eq.(40) r(g*+d) = g*-d holds with g* = 0.  [hypothesis satisfied]\n")
    print("   theta    S_J direct     4 th tanh(th)     diff")
    for th in [-2.0, -0.7, -0.1, 0.1, 0.7, 2.0]:
        print(f"  {th:+6.2f}   {SJ(th):12.8f}   {4*th*np.tanh(th):12.8f}   {abs(SJ(th)-4*th*np.tanh(th)):.1e}")
    print("\n  => S_J(theta) = 4 theta tanh(theta)  [CLOSED FORM]")
    h = 1e-4
    print(f"  S_J(0) = 0                   (Eq.35): {SJ(1e-9):.2e}")
    print(f"  dS_J/dtheta|_0 = 0           (Eq.36): {(SJ(h)-SJ(-h))/(2*h):.2e}")
    IJ = (SJ(h)+SJ(-h))/h**2
    print(f"  I_J(0) = d2 S_J/dtheta2|_0   (Eq.37): {IJ:.8f}   (exact 8)")
    print("\n  S_J >= 0, vanishing only at theta = 0, strictly increasing in |theta|:")
    print("  theta = 0 is the UNIQUE self-dual point and the UNIQUE global minimum.")
    print("  => N_c is a variational object, not a chosen parameter.\n")


# ============================================================ R14 : T11 cont.
def receipt_14():
    print(BANNER); print("R14 Hessian = BKM form on the modular-selected tangent   [T11]")
    print(BANNER)
    rho_s = np.array([0.5, 0.5])                  # rho_* = I/2 at theta = 0
    X_s   = np.array([0.5, -0.5])                 # X_* = d rho/d theta|_0 = Q/2
    gam   = lambda X, Y: 2*float(np.sum(X*Y))     # K_rho*(X)=X/2 => K^-1=2X (Eq.46)
    print("  rho_* = I/2,  X_* = Q/2,  K_rho*(X) = X/2  =>  K^-1(X) = 2X")
    print(f"  gamma_BKM(X_*,X_*)      = {gam(X_s,X_s):.8f}   = G^BKM_thth(0) = sech^2(0) = 1")
    print("  reflected difference rho - rho_J = 2 delta X_*  (Eq.41)")
    print(f"  gamma_BKM(2X_*,2X_*)    = {gam(2*X_s,2*X_s):.8f}")
    print(f"  2 gamma_BKM(2X_*,2X_*)  = {2*gam(2*X_s,2*X_s):.8f}")
    h = 1e-4
    print(f"  I_J(0) from entropy     = {(SJ(h)+SJ(-h))/h**2:.8f}   [MATCH]")
    print("\n  => I_J = 2 gamma_BKM(DeltaX, DeltaX) = 8 G^BKM at the self-dual point.")
    print("     Factor 8 = 2 (symmetrisation) x 4 (tangent doubled by reflection).\n")


# ============================================================ R15 : T12
def receipt_15():
    print(BANNER); print("R15 [NEW] cosmological form of S_J, and the crossing direction   [T12]")
    print(BANNER)
    vp = 1.0; nc = solve_Nc(OM, OR, vp)
    print("  theta = varrho(N-N_c),  1+w_X = (2varrho/3) tanh(theta)  =>")
    print("\n      S_J = 4 theta tanh theta = 6 (N - N_c)(1 + w_X)    <- varrho CANCELS\n")
    print("     z        N-N_c      1+w_X       6(N-Nc)(1+w)     4 th tanh th")
    for z in [3.0, 1.0, 0.5, 0.342016, 0.2, 0.0, -0.3, -0.6]:
        N = -np.log(1+z); u = N-nc; th = vp*u
        opw = (2*vp/3)*np.tanh(th)
        print(f"   {z:+6.3f}  {u:+9.5f}  {opw:+9.5f}    {6*u*opw:13.8f}    {4*th*np.tanh(th):13.8f}")
    print("\n  Relative entropy is non-negative, so S_J >= 0 forces")
    print("        (N - N_c)(1 + w_X) >= 0")
    print("  i.e.  w_X < -1 BEFORE the crossing, w_X > -1 AFTER it.")
    print("  The phantom -> quintessence DIRECTION is a theorem of relative-entropy")
    print("  positivity, not an input. The time-reversed pulse is forbidden.")
    print(f"\n  S_J today (z=0) = {6*(0-nc)*((2*vp/3)*np.tanh(-vp*nc)):.6f} nats")
    print("  Testable: reconstruct w(z), form 6 ln[(1+z_c)/(1+z)](1+w(z)), check >= 0.\n")


# ============================================================ R16 : T13
def receipt_16():
    print(BANNER); print("R16 [NEW] the scale tractor: I.I = -mu_A H^2   [T13]")
    print(BANNER)
    vp = 1.0; nc = solve_Nc(OM, OR, vp)
    rm = lambda N: OM*np.exp(-3*N); rr_ = lambda N: OR*np.exp(-4*N)
    rX = lambda N: OM*np.exp(-3*nc)/np.cosh(vp*(N-nc))**2
    wX = lambda N: -1 + (2*vp/3)*np.tanh(vp*(N-nc))
    E2 = lambda N: rm(N)+rr_(N)+rX(N)
    wt = lambda N: (rr_(N)/3 + wX(N)*rX(N))/E2(N)
    mu = lambda N: 0.5*(1-0.5*(1+3*wt(N)))
    lnE = lambda N: 0.5*np.log(E2(N))
    II = lambda N: -(E2(N)*d1(lnE,N) + 2*E2(N))/2
    print("  FLRW is conformally flat (Weyl = 0), so ALL content is in the SCALE.")
    print("  Take the conformal structure flat; g = a^2 eta means sigma = 1/a.")
    print("  sigma' = -H, sigma'' = -a Hdot  =>  I.I = -(H^2 + Hdot/2) = -R/12.")
    print("  Confirmed by arXiv:2208.09302 eq.(3.20): I.I = -R/(n(n-1)).\n")
    print("     N       -(Hdot+2H^2)/2       -R/12       (3w_tot-1)H^2/4")
    for N in [-3,-1,nc,0,1,3]:
        print(f"  {N:+7.4f}  {II(N):+14.8f}  {-6*(E2(N)*d1(lnE,N)+2*E2(N))/12:+14.8f}"
              f"  {(3*wt(N)-1)*E2(N)/4:+14.8f}")
    print("\n  IDENTITY:  q = (1+3w)/2  =>  (3w-1)/4 = (q-1)/2 = -mu_A, so\n")
    print("        I.I = - mu_A H^2\n")
    print("     z          mu_A        -I.I/H^2      diff")
    for z in [1000,3,1,0.342016,0,-0.9,-0.99]:
        N = -np.log(1+z)
        print(f"  {z:+9.4f}   {mu(N):.8f}   {-II(N)/E2(N):.8f}   {abs(mu(N)+II(N)/E2(N)):.1e}")
    print("\n  => the VERTICAL horizon clock rate mu_A = d eta_A/dN IS (minus) the")
    print("     normalised scale-tractor norm. The erratum's vertical direction is")
    print("     exactly conformal tractor data.")
    print("     Allocation law becomes:  1 = -I.I/H^2 + (1/4) d(ln S_A)/dN")
    print("     dS: I.I/H^2 = -1.  Minkowski: 0.  varrho=1 => I.I/H^2 -> -1/2,")
    print("     exactly halfway between the null tractor and de Sitter.\n")


# ============================================================ R17 : NEGATIVE + T14
def receipt_17():
    print(BANNER); print("R17 [NEGATIVE] Phi*G_BKM ~ I.I fails; [T14] the correct split")
    print(BANNER)
    vp = 1.0; nc = solve_Nc(OM, OR, vp)
    rm = lambda N: OM*np.exp(-3*N); rr_ = lambda N: OR*np.exp(-4*N)
    rX = lambda N: OM*np.exp(-3*nc)/np.cosh(vp*(N-nc))**2
    wX = lambda N: -1 + (2*vp/3)*np.tanh(vp*(N-nc))
    E2 = lambda N: rm(N)+rr_(N)+rX(N)
    wt = lambda N: (rr_(N)/3 + wX(N)*rX(N))/E2(N)
    mu = lambda N: 0.5*(1-0.5*(1+3*wt(N)))
    Xs = lambda N: vp**2/np.cosh(vp*(N-nc))**2
    print("     N       X_sigma      mu_A = -I.I/H^2     ratio")
    for N in [-3,-1,nc,0,1,3]:
        print(f"  {N:+7.4f}  {Xs(N):12.8f}   {mu(N):12.8f}   {Xs(N)/mu(N):10.5f}")
    print("\n  Ratio spans >2 decades. X_sigma peaks at N_c and vanishes both ways;")
    print("  mu_A never vanishes. NOT proportional. [NEGATIVE]")
    print("  DIAGNOSIS: I.I is a NORM built from sigma -> VERTICAL. X_sigma is the")
    print("  horizontal BKM form. The conjecture re-committed the exact conflation")
    print("  the v5.1 erratum corrected. Also: Weyl = Cotton = 0 for FLRW, so the")
    print("  tractor CONNECTION is flat and carries no horizontal data at all.\n")
    print("  REPAIR. arXiv:2208.09302 eq.(3.22): grad_a I is sourced by the")
    print("  TRACE-FREE stress tau0_ab. For a perfect fluid in n=4,")
    print("      tau0_ab = (rho+p)[u_a u_b + g_ab/4]   =>   tau0 = 0 <=> rho+p = 0.")
    print("  So the tractor is PARALLEL exactly on the pure-Lambda sector.\n")
    print("  At N_c the dark sector has w_X = -1 exactly, so rho_X + p_X = 0:")
    print("  it is entirely tractor-parallel and sources NOTHING. Only matter does.\n")
    print("     N        rho_X+p_X      rho_m+p_m    source fraction")
    for N in [nc-1, nc-0.3, nc, nc+0.3, nc+1]:
        sx = rX(N)*(1+wX(N))
        print(f"  {N:+8.5f}   {sx:+12.8f}   {rm(N):12.8f}    {(sx+rm(N))/E2(N):.8f}")
    print(f"\n  at N_c:  rho_X+p_X = {rX(nc)*(1+wX(nc)):.2e}   source fraction ="
          f" {rm(nc)/E2(nc):.8f} = Omega_m(N_c) = 1/(1+r_c)\n")
    print("     r_c    parallel frac   source frac")
    for rc in [0.5, 1.0, 2.0]:
        print(f"    {rc:5.2f}     {rc/(1+rc):.6f}      {1/(1+rc):.6f}")
    print("\n  *** r_c = 1  <=>  at the modular self-dual point the energy budget")
    print("      splits EXACTLY 1:1 between the tractor-PARALLEL (Einstein,")
    print("      tau0 = 0) sector and the tractor-SOURCE (tau0 != 0) sector. ***")
    print("\n  And the dark source is the scale-derivative of the susceptibility:")
    chi = OM*np.exp(-3*nc)/vp**2
    print("      rho_X + p_X = -(chi_perp/3) dX_sigma/dN      [continuity]")
    for N in [nc-1, nc-0.3, nc+0.3, nc+1]:
        lhs = rX(N)*(1+wX(N)); d = (Xs(N+1e-6)-Xs(N-1e-6))/2e-6
        print(f"   N={N:+8.5f}  lhs={lhs:+.8f}  rhs={-(chi/3)*d:+.8f}  diff={abs(lhs+(chi/3)*d):.1e}")
    print("\n  NORM <-> vertical.  DERIVATIVE <-> horizontal.  Two slots, again.\n")


# ============================================================ R18 : T15
def receipt_18():
    print(BANNER); print("R18 [NEW] Levinson phase density = BKM line element   [T15]")
    print(BANNER)
    a = 1.0
    argt = lambda k: np.pi - 2*np.arctan(k/a)
    print("  l=1 reflectionless potential V = -2 a^2 sech^2(a x):")
    print("     t(k) = -(a - ik)/(a + ik)   |t| = 1, a single Blaschke factor")
    print("     arg t(k) = pi - 2 arctan(k/a)")
    for k in [1e-6, 1.0, 1e6]:
        tt = -(a-1j*k)/(a+1j*k)
        print(f"     k={k:8.1e}  |t|={abs(tt):.10f}  arg t={np.angle(tt)%(2*np.pi):.8f}")
    print(f"  arg t(0) - arg t(inf) = {argt(1e-9)-argt(1e9):.10f}  = pi  [LEVINSON, l=1]\n")
    print("  In log-momentum s = ln(k/a):   |d(arg t)/ds| = sech(s)")
    print("     s        -d(arg t)/ds        sech(s)         diff")
    for s in [-3,-1.5,-0.5,0.0,0.5,1.5,3]:
        h = 1e-6
        num = -(argt(a*np.exp(s+h)) - argt(a*np.exp(s-h)))/(2*h)
        print(f"  {s:+6.2f}   {num:14.10f}   {1/np.cosh(s):14.10f}   {abs(num-1/np.cosh(s)):.1e}")
    I1, _ = quad(lambda s: 1/np.cosh(s), -40, 40)
    I2, _ = quad(lambda t_: 1/np.cosh(t_), -40, 40)
    print(f"\n  int |d(arg t)/ds| ds = {I1:.12f}")
    print(f"  BKM/Fisher length int sech(theta) dtheta = {I2:.12f}   (T5)")
    print(f"  difference = {abs(I1-I2):.2e}   both = pi = simplex diameter")
    print("\n  => theta <--> ln(k/alpha): the modular polarisation IS log-momentum,")
    print("     and the BKM line element IS the transmission phase differential.\n")
    print("  DIRECTEDNESS: t(k) has its single pole at k = +i*alpha, the UPPER half")
    print("  plane = retarded/causal. Reflectionlessness means that pole is the ENTIRE")
    print("  scattering content, so the arrow IS the pole's half-plane. Time reversal")
    print("  moves it to the lower half plane: acausal. Agrees with T12's entropy arrow.\n")


# ============================================================ R19 : T16
def receipt_19():
    print(BANNER); print("R19 [NEW] why: sech is Fourier self-reciprocal   [T16]")
    print(BANNER)
    print("  int sech(a x) e^{-ikx} dx = (pi/a) sech(pi k/(2a))")
    a = np.sqrt(np.pi/2)
    x = np.linspace(-60, 60, 400001); f = 1/np.cosh(a*x)
    for k in [0.0, 0.5, 1.0, 2.0]:
        num = np.trapezoid(f*np.exp(-1j*k*x), x).real
        ana = (np.pi/a)/np.cosh(np.pi*k/(2*a))
        print(f"   k={k:4.1f}   numeric={num:12.8f}   analytic={ana:12.8f}   diff={abs(num-ana):.1e}")
    print(f"\n  a = sqrt(pi/2) = {a:.8f}  =>  pi/(2a) = {np.pi/(2*a):.8f} = a")
    print("  sech(sqrt(pi/2) x) is an EIGENFUNCTION of the Fourier transform.")
    print("  (Gaussian and sech are the two classical self-reciprocal profiles.)\n")
    print("  CONSEQUENCE: V ~ sech^2(theta) IS G^BKM_thth in POSITION; its square")
    print("  root, the Fisher line element, is the SAME function appearing as the")
    print("  phase density in LOG-MOMENTUM. The matching pi is Fourier self-duality")
    print("  of the profile, not a numerical coincidence.\n")
    print("  LEDGER: transparency gives c*chi_perp = l(l+1); r_c = chi_perp v^2/rho_m(N_c)")
    print("     =>  r_c = l(l+1) v^2 / (c rho_m(N_c))")
    nc = solve_Nc(OM, OR, 1.0); rhomc = OM*np.exp(-3*nc)
    print(f"     rho_m(N_c) = {rhomc:.6f} (units rho_crit,0);  l=1, v=1, r_c=1 require")
    print(f"     c * rho_m(N_c) = 2   =>   c = {2/rhomc:.6f}   [PREREGISTERED]\n")


# ============================================================ R20 : N4
def receipt_20():
    print(BANNER); print("R20 [NEGATIVE N4] canonical sigma-model Gamma_MW cannot carry the soldering")
    print(BANNER)
    print("  Gamma = int sqrt(-g)[(chi/2) G(theta)(d theta)^2 - V(theta)] gives")
    print("     1 + w = chi G thetadot^2 / rho.")
    print("  Impose soldering thetadot = varrho H, target 1+w_X = (2v/3)tanh(theta),")
    print("  rho_X = rho_* sech^2(theta), and G = sech^2(theta):")
    print("     chi sech^2 v^2 H^2 / (rho_* sech^2) = (2v/3) tanh")
    print("     =>  H^2 = (2 rho_*/(3 chi v)) tanh(theta)\n")
    print("     theta     tanh(theta)      required H^2")
    for th in [-2,-1,-0.3,0.3,1,2]:
        tag = "NEGATIVE - impossible" if th < 0 else "positive"
        print(f"    {th:+5.1f}    {np.tanh(th):+11.6f}     {tag}")
    print("\n  H^2 < 0 across the entire pre-crossing branch. Exact no-go: no canonical")
    print("  sigma model with the BKM target metric realises the rigid pulse under the")
    print("  soldering law. (N2 seen from the Lagrangian side.)\n")


# ============================================================ R21 : Version B
def receipt_21():
    print(BANNER); print("R21 the conformally natural constitutive law is falsified")
    print(BANNER)
    print("  X_sigma is dimensionless; rho_X is 1/length^2. So in")
    print("     Version A:  rho_X   = chi_perp X_sigma   -> chi_perp FIXES A LENGTH")
    print("     Version B:  Omega_X = lambda   X_sigma   -> lambda is a pure number")
    print("  Only B respects 'causal order fixes geometry up to scale'. Test B:\n")
    print("     lambda   Omega_X max   N_c with Omega_X(0)=0.6893      status")
    for lam in [0.5, 0.6893, 0.75, 0.90, 1.0]:
        if lam < 0.6893 - 1e-12:
            print(f"     {lam:5.3f}     {lam:8.5f}     none                     CANNOT REACH TODAY")
        else:
            nc = brentq(lambda n: lam/np.cosh(n)**2 - 0.6893, -4, 0)
            s = "SINGULAR Omega_X->1" if lam >= 1.0 else "viable"
            print(f"     {lam:5.3f}     {lam:8.5f}     {nc:+.5f} (z_c={np.exp(-nc)-1:.4f})    {s}")
    lam = 0.85; nc = brentq(lambda n: lam/np.cosh(n)**2-0.6893, -4, 0)
    OmX = lambda N: lam/np.cosh(N-nc)**2
    H2  = lambda N: (OM*np.exp(-3*N)+OR*np.exp(-4*N))/(1-OmX(N))
    rX  = lambda N: OmX(N)*H2(N)
    dl  = lambda f,N,h=1e-5: (np.log(f(N+h))-np.log(f(N-h)))/(2*h)
    print(f"\n  lambda=1/2 (equipartition) EXCLUDED; lambda=1 (no coefficient) SINGULAR.")
    print(f"  Viable window (0.689, 1) contains no natural value. And at lambda={lam}:")
    print(f"     w_X at the susceptibility peak = {-1-dl(rX,nc)/3:+.6f}   (needs -1)")
    print("  Version B does not put w_X = -1 at the peak, so it loses T8 (the three-")
    print("  epoch coincidence) AND the shape invariant. Version B is DEAD.")
    print("  => the dimensionful chi_perp is FORCED, and with it a fixed length.\n")


if __name__ == "__main__":
    for f in (receipt_1, receipt_2, receipt_3, receipt_4, receipt_5,
              receipt_6, receipt_7, receipt_8, receipt_9,
              receipt_10, receipt_11, receipt_12,
              receipt_13, receipt_14, receipt_15,
              receipt_16, receipt_17, receipt_18, receipt_19,
              receipt_20, receipt_21):
        f()
    print(BANNER); print("all receipts complete"); print(BANNER)

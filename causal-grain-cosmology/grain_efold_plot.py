#!/usr/bin/env python3
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

d = np.load("/home/claude/grain_efold.npz")
N_tot=float(d["N_tot"]); x_c=float(d["x_c"]); x_eq=float(d["x_eq"]); x_acc=float(d["x_acc"])
H0=float(d["H0"]); Om=float(d["Om"]); OL=float(d["OL"]); Or=float(d["Or"])
NP_inf=float(d["NP_inf"]); NP_inf_pred=float(d["NP_inf_pred"]); NP_today=float(d["NP_today"])
n_c=float(d["n_c"]); dn_c=float(d["dn_c"]); lam=float(d["lam_star"]); Es=float(d["E_star"])

c=2.99792458e8; l_P=1.616255e-35; kmsMpc=1e3/3.0856775814913673e22
H0_s=H0*kmsMpc

E   = lambda x: np.sqrt(Or*np.exp(-4*x)+Om*np.exp(-3*x)+OL)
NP  = lambda x: np.log(c/(H0_s*E(x)*l_P))
nn  = lambda x: E(x)/np.sqrt(OL)
def opq(x):
    e=E(x); return -0.5*(-4*Or*np.exp(-4*x)-3*Om*np.exp(-3*x))/e**2

x  = np.linspace(-N_tot, 8.0, 4000)      # ln a ; N = x + N_tot
N  = x + N_tot

ACC="#c2410c"; EQ="#0f766e"; GR="#7c2d92"; BLUE="#1d4ed8"; GREY="#94a3b8"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9,
                     "axes.edgecolor":"#334155","axes.labelcolor":"#0f172a",
                     "xtick.color":"#334155","ytick.color":"#334155"})

fig = plt.figure(figsize=(11.0, 11.6))
gs  = fig.add_gridspec(3,1, height_ratios=[1.5,1.0,0.85], hspace=0.30,
                       left=0.085, right=0.965, top=0.898, bottom=0.062)

def marks(ax, ytxt=None, lab=True):
    for xx,col,lb in [(x_acc,ACC,"acceleration onset  $n=\\sqrt{3}$"),
                      (x_eq,EQ,"matter–$\\Lambda$ equality  $n=\\sqrt{2}$"),
                      (x_c,GR,"grain crossing  $H=H_c$")]:
        ax.axvline(xx+N_tot, color=col, lw=1.1, ls="--", alpha=.85,
                   label=(lb if lab else None), zorder=2)
    ax.axvline(N_tot, color="#0f172a", lw=1.2, alpha=.8,
               label=("today  $N=27.71$" if lab else None), zorder=2)

# ---------------------------------------------------------------- panel A
axA = fig.add_subplot(gs[0])
axA.plot(N, NP(x), color=BLUE, lw=2.4, zorder=4, label="$N_P(N)=\\ln(R_A/\\ell_P)$")
axA.axhline(NP_inf, color=GREY, lw=1.4, ls=":", zorder=3)
axA.axhline(NP_inf_pred, color="#be123c", lw=1.6, ls="-.", zorder=3)
axA.fill_between([N[0],N[-1]], NP_inf_pred-0.0276*3, NP_inf_pred+0.0276*3,
                 color="#be123c", alpha=.10, zorder=1)
marks(axA)
axA.set_ylim(86, 143.5); axA.set_xlim(-0.6, N[-1])
axA.set_ylabel("resolution depth   $N_P=\\ln(R_A/\\ell_P)$   [nats]")
axA.text(0.45, 100.5, "birth of mass\n(QCD crossover)\n$N_P=89.4$", fontsize=8.2,
         color="#334155", va="bottom")
axA.annotate("", xy=(0,89.0), xytext=(0,143.5),
             arrowprops=dict(arrowstyle="-", color="#0f172a", lw=1.2))
axA.text(12.0, NP_inf+0.75, "observed de Sitter plateau   $N_P(\\infty)=140.484$",
         ha="left", fontsize=8.6, color="#475569")
axA.text(12.0, NP_inf_pred-2.6,
         "grain prediction   $3\\ln(\\lambda_*/\\ell_P)+\\ln\\frac{3\\sqrt{2}}{8}=140.447$",
         ha="left", fontsize=8.6, color="#be123c")
axA.legend(loc="upper left", frameon=True, framealpha=.94, fontsize=8.2,
           edgecolor="#cbd5e1", bbox_to_anchor=(0.015,0.965))
axA.set_title("A   The monotone: one function of e-fold time, anchored by the grain",
              loc="left", fontsize=10.5, fontweight="bold", pad=8)

# inset: the last 1.5 e-folds
ins = axA.inset_axes([0.545,0.075,0.435,0.44])
xi=np.linspace(-1.2,1.6,800); Ni=xi+N_tot
ins.plot(Ni, NP(xi), color=BLUE, lw=2.0)
ins.axhline(NP_inf, color=GREY, lw=1.2, ls=":")
ins.axhline(NP_inf_pred, color="#be123c", lw=1.3, ls="-.")
ins.fill_between([Ni[0],Ni[-1]], NP_inf_pred-0.0828, NP_inf_pred+0.0828,
                 color="#be123c", alpha=.13)
for xx,col in [(x_acc,ACC),(x_eq,EQ),(x_c,GR)]: ins.axvline(xx+N_tot,color=col,lw=1.0,ls="--")
ins.axvline(N_tot, color="#0f172a", lw=1.1)
ins.set_xlim(Ni[0],Ni[-1]); ins.set_ylim(139.7,140.62)
ins.tick_params(labelsize=7); ins.set_facecolor("#f8fafc")
ins.set_zorder(20); ins.patch.set_alpha(1.0)
ins.set_title("last 1.2 e-folds  ·  $3\\sigma$ band from $F_\\pi$", fontsize=7.6, pad=3)

# ---------------------------------------------------------------- panel B
axB = fig.add_subplot(gs[1])
axB.plot(N, nn(x)**2, color=BLUE, lw=2.4, zorder=4,
         label="$n^2(N)=H^2/H_\\Lambda^2=1+\\rho_m/\\rho_\\Lambda$")
axB.set_yscale("log")
axB.axhline(2.0, color=EQ, lw=1.6, ls="-", alpha=.9, zorder=3)
axB.axhline(3.0, color=ACC, lw=1.2, ls="-", alpha=.6, zorder=3)
axB.axhline(1.0, color=GREY, lw=1.2, ls=":", zorder=3)
axB.errorbar([N_tot+x_c],[n_c**2], yerr=[2*n_c*dn_c], fmt="o", ms=8,
             color=GR, ecolor=GR, elinewidth=2.2, capsize=5, zorder=6,
             label="grain:  $n_c^2=2.15\\pm0.12$")
marks(axB, lab=False)
axB.set_ylim(0.8, 4e5); axB.set_xlim(-0.6, N[-1])
axB.set_ylabel("$n^2 = 1+\\rho_m/\\rho_\\Lambda$")
axB.text(0.8, 1.06, "$n^2=2$  matter–$\\Lambda$ equality", ha="left",
         fontsize=8.6, color=EQ)
axB.annotate("", xy=(3.0,2.0), xytext=(3.0,1.35),
             arrowprops=dict(arrowstyle="-", color=EQ, lw=0.9))
axB.text(0.8, 6.8, "$n^2=3$  acceleration onset ($q=0$)", ha="left",
         fontsize=8.6, color=ACC)
axB.annotate("", xy=(3.0,3.0), xytext=(3.0,5.6),
             arrowprops=dict(arrowstyle="-", color=ACC, lw=0.9))
axB.legend(loc="upper right", frameon=True, framealpha=.94, fontsize=8.4,
           edgecolor="#cbd5e1")
axB.set_title("B   “Off by 2” — the residual is $n_c^2$, and it is $1.3\\sigma$ from exactly 2",
              loc="left", fontsize=10.5, fontweight="bold", pad=8)
ib = axB.inset_axes([0.415,0.34,0.255,0.52])
xj=np.linspace(-0.9,0.4,500)
ib.plot(xj+N_tot, nn(xj)**2, color=BLUE, lw=2.0)
ib.axhline(2.0, color=EQ, lw=1.5)
ib.errorbar([N_tot+x_c],[n_c**2], yerr=[2*n_c*dn_c], fmt="o", ms=7, color=GR,
            ecolor=GR, elinewidth=2.0, capsize=4)
ib.set_xlim(N_tot-0.9, N_tot+0.4); ib.set_ylim(1.0, 3.4)
ib.tick_params(labelsize=7); ib.set_facecolor("#f8fafc")
ib.set_zorder(20); ib.patch.set_alpha(1.0)

# ---------------------------------------------------------------- panel C
axC = fig.add_subplot(gs[2])
axC.plot(N, opq(x), color=BLUE, lw=2.4, zorder=4, label="$dN_P/dN=1+q$")
for yv,lb,col in [(2.0,"radiation  $1+q=2$","#64748b"),
                  (1.5,"matter  $1+q=3/2$","#64748b"),
                  (1.0,"$q=0$: acceleration begins",ACC),
                  (0.0,"de Sitter  $1+q=0$","#64748b")]:
    axC.axhline(yv, color=col, lw=1.1, ls=("-" if yv==1.0 else ":"), alpha=.8)
    axC.text(N[-1]-0.3, yv+0.06, lb, ha="right", fontsize=8.0, color=col)
marks(axC, lab=False)
axC.fill_between(N, 0, opq(x), where=(opq(x)<1.0), color=ACC, alpha=.10)
axC.set_ylim(-0.15, 2.25); axC.set_xlim(-0.6, N[-1])
axC.set_ylabel("$1+q$   (nats of depth per e-fold)")
axC.set_xlabel("$N$  —  e-folds since the birth of mass   "
               "($N=0$: QCD crossover $T=155$ MeV;  $N=27.71$: today)")
axC.set_title("C   The slope: two nats per e-fold, decaying to zero",
              loc="left", fontsize=10.5, fontweight="bold", pad=8)

fig.suptitle("Dark energy anchored by the causal grain, over e-fold time from the birth of mass",
             x=0.085, ha="left", y=0.970, fontsize=13.5, fontweight="bold", color="#0f172a")
fig.text(0.085, 0.9375,
  "$\\lambda_*^3=\\frac{8}{3}\\ell_P^2R_c$    $\\lambda_*=\\hbar c/E_*=4.287$ fm (from $F_\\pi$)"
  "    $\\Rightarrow$    $H_c=81.8\\pm2.3$ km/s/Mpc.        Inputs: $c$, $G$, $\\hbar$, $F_\\pi$.",
  ha="left", fontsize=8.9, color="#475569")
fig.text(0.085, 0.9205,
  "$\\Lambda$CDM ($\\Omega_m=0.315$) supplies only the shape of the curve between the endpoints "
  "— not the plateau it ends on.",
  ha="left", fontsize=8.9, color="#475569")
fig.savefig("/home/claude/grain_efold_anchor.png", dpi=190, facecolor="white")
print("wrote grain_efold_anchor.png")

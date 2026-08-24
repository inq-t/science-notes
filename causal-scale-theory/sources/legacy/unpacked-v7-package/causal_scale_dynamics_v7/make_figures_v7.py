#!/usr/bin/env python3
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from scipy.optimize import brentq

OUT=Path(__file__).resolve().parent/'figures'; OUT.mkdir(exist_ok=True)

# 1. Scale-capacity closure diagram
fig,ax=plt.subplots(figsize=(12,5.5)); ax.set_xlim(0,12); ax.set_ylim(0,6); ax.axis('off')
boxes=[
(0.4,3.8,2.2,1.2,'Binary normal pair',r'$Q^2=1,\ JQJ=-Q$'),
(3.0,3.8,2.2,1.2,'BKM response',r'$G^\perp_{NN}=\frac{S_c}{k_B}\,\mathrm{sech}^2(N-N_c)$'),
(5.6,3.8,2.2,1.2,'Modular free energy',r'$\rho_X=\frac{k_BT_c}{2V_c}G^\perp_{NN}$'),
(8.2,3.8,3.2,1.2,'Hawking-Friedmann conversion',r'$k_BT_c\,S_c/k_B=E_{\rm MS,c}=\rho_{\rm crit,c}V_c$'),
(4.2,1.2,3.6,1.3,'Closed cosmic source',r'$\rho_X=\frac{1}{2}\rho_{\rm crit,c}\,\mathrm{sech}^2(N-N_c)$'),
]
for x,y,w,h,t,e in boxes:
    p=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',fc='#EEF4F8' if y>2 else '#ECF6EF',ec='#345B83',lw=1.5)
    ax.add_patch(p); ax.text(x+w/2,y+h*0.68,t,ha='center',va='center',fontsize=12,fontweight='bold'); ax.text(x+w/2,y+h*0.28,e,ha='center',va='center',fontsize=11)
for a,b in [((2.6,4.4),(3.0,4.4)),((5.2,4.4),(5.6,4.4)),((7.8,4.4),(8.2,4.4)),((9.8,3.8),(7.3,2.5)),((6.7,3.8),(6.2,2.5))]:
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,lw=1.4,color='#345B83'))
ax.text(6,5.55,'Scale-Capacity closure of the homogeneous amplitude',ha='center',fontsize=17,fontweight='bold')
ax.text(6,0.45,r'$\Omega_{X,c}=1/2\quad\Longrightarrow\quad\rho_X(N_c)=\rho_{\rm ordinary}(N_c)$ in three spatial dimensions',ha='center',fontsize=13)
fig.tight_layout()
for ext in ('png','pdf'): fig.savefig(OUT/f'scale_capacity_closure.{ext}',dpi=240,bbox_inches='tight')
plt.close(fig)

# 2. Dimension dependence
D=np.arange(3,11) # spatial dimensions d, starting d=3 because d=2 diverges ratio
r=1/(D-2)
Omega=1/(D-1)
fig,ax=plt.subplots(figsize=(8.4,5.4))
ax.plot(D,r,'o-',label=r'$r_c^{\rm ord}=1/(d-2)$')
ax.plot(D,Omega,'s--',label=r'$\Omega_{X,c}=1/(d-1)$')
ax.axhline(1,ls=':',lw=1); ax.axvline(3,ls=':',lw=1)
ax.scatter([3],[1],s=120,zorder=5)
ax.annotate('equal ordinary/dark crossing\noccurs at d=3',(3,1),xytext=(4.1,1.15),arrowprops=dict(arrowstyle='->'))
ax.set_xlabel('number of spatial dimensions $d$'); ax.set_ylabel('dimensionless crossing fraction/ratio')
ax.set_title('Dimension dependence of unit scale-capacity response')
ax.set_xticks(D); ax.grid(alpha=.22); ax.legend(frameon=False)
fig.tight_layout()
for ext in ('png','pdf'): fig.savefig(OUT/f'dimension_crossing_ratio.{ext}',dpi=240,bbox_inches='tight')
plt.close(fig)

# 3. Updated rigid history
Om,Or=0.310598,9.15e-5
def root_eq(Nc):
    rho_ord=Om*np.exp(-3*Nc)+Or*np.exp(-4*Nc)
    return Om+Or+rho_ord/np.cosh(Nc)**2-1
Nc=brentq(root_eq,-2,0); rs=Om*np.exp(-3*Nc)+Or*np.exp(-4*Nc)
N=np.linspace(-4,3.5,1400)
rm=Om*np.exp(-3*N); rr=Or*np.exp(-4*N); rx=rs/np.cosh(N-Nc)**2
wx=-1+(2/3)*np.tanh(N-Nc); E2=rm+rr+rx
q=-1+1.5*(rm+(4/3)*rr+rx*(1+wx))/E2; mu=(1-q)/2
fig,axs=plt.subplots(4,1,figsize=(10,12),sharex=True,gridspec_kw={'height_ratios':[1.25,.85,.85,.85]})
axs[0].semilogy(N,rr,label='radiation'); axs[0].semilogy(N,rm,label='matter'); axs[0].semilogy(N,rx,label='scale-capacity response')
axs[0].set_ylabel(r'$\rho_i/\rho_{\rm crit,0}$'); axs[0].legend(frameon=False,ncol=3); axs[0].set_ylim(1e-5,2e5)
axs[1].plot(N,wx); axs[1].axhline(-1,ls=':'); axs[1].set_ylabel(r'$w_X$')
axs[2].plot(N,q,label='$q$'); axs[2].plot(N,mu,label=r'$\mu_A=(1-q)/2$'); axs[2].axhline(0,ls=':'); axs[2].axhline(.5,ls='--'); axs[2].legend(frameon=False,ncol=2); axs[2].set_ylabel('kinematics')
axs[3].plot(N,mu,label='horizon rapidity share'); axs[3].plot(N,1-mu,label='horizon-information share'); axs[3].legend(frameon=False); axs[3].set_ylabel('one-e-fold allocation'); axs[3].set_xlabel(r'$N=\ln a$')
for ax in axs:
    ax.axvline(Nc,ls='--',lw=1); ax.grid(alpha=.18)
axs[0].set_title('Parameter-free capacity-normalized background (given present matter/radiation state)')
fig.tight_layout()
for ext in ('png','pdf'): fig.savefig(OUT/f'rigid_history_v7.{ext}',dpi=240,bbox_inches='tight')
plt.close(fig)

# 4. One-principle dependency diagram
fig,ax=plt.subplots(figsize=(11,7)); ax.set_xlim(0,11); ax.set_ylim(0,8); ax.axis('off')
nodes={
'A':(1.2,6.6,'Causal order','conformal class $[g]$'),
'B':(4.0,6.6,'Scale section',r'$\sigma\in\mathcal{E}[1]$'),
'C':(7.0,6.6,'Normal state pair',r'$Q=P_+-P_-$'),
'D':(4.0,4.4,'Scale-Capacity Principle',r'$\frac{k_B}{S_c}\Phi^*G^\perp_{\rm BKM}=\mathrm{sech}^2(N-N_c)dN^2$'),
'E':(1.4,2.2,'Tractor gravity',r'$\mathcal{E}_{ab}(\sigma)\propto T^\circ_{ab}$'),
'F':(5.0,2.2,'Closed dark history',r'$\rho_X=\frac{1}{2}\rho_{\rm crit,c}\mathrm{sech}^2(N-N_c)$'),
'G':(8.6,2.2,'Predictions',r'$9(1+w)^2+6w\prime=4$'),
}
for k,(x,y,t,e) in nodes.items():
    w=2.6 if k!='D' else 4.6; h=1.05
    p=FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=.06',fc='#F3EFF8' if k=='D' else '#EEF4F8',ec='#345B83',lw=1.3); ax.add_patch(p)
    ax.text(x,y+.15,t,ha='center',fontsize=11.5,fontweight='bold'); ax.text(x,y-.2,e,ha='center',fontsize=10.5)
for a,b in [('A','B'),('B','D'),('C','D'),('B','E'),('D','F'),('E','F'),('F','G')]:
    x1,y1=nodes[a][0],nodes[a][1]; x2,y2=nodes[b][0],nodes[b][1]
    ax.add_patch(FancyArrowPatch((x1,y1-.55),(x2,y2+.55) if y2<y1 else (x2-1.3,y2),arrowstyle='-|>',mutation_scale=13,lw=1.2,color='#345B83'))
ax.text(5.5,7.7,'Dependency structure of Causal Scale Dynamics',ha='center',fontsize=17,fontweight='bold')
fig.tight_layout()
for ext in ('png','pdf'): fig.savefig(OUT/f'dependency_v7.{ext}',dpi=240,bbox_inches='tight')
plt.close(fig)

print('figures written',OUT)

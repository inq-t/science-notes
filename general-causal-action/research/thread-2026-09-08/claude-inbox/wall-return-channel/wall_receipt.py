"""Receipt: return channel D = E_omega o iota of a pointed inclusion (N in M, omega), two smallest walls.
E_omega = Accardi-Cecchini / Petz omega-dual of the inclusion.  Heisenberg form used here:
   E_omega(x) = rho_N^{-1/2} E_tr( rho^{1/2} x rho^{1/2} ) rho_N^{-1/2},   rho_N = E_tr(rho)
Claims checked: unital, omega_N-preserving, D = id iff N is sigma^omega-invariant (Takesaki), closed-form gaps."""
import numpy as np
from numpy.linalg import eigvals
from scipy.linalg import sqrtm, logm
rng = np.random.default_rng(1)
def relent(A,B): return float(np.real(np.trace(A@(logm(A)-logm(B)))))

# ---- Example 1: M=M_2, N=diagonal, rho=(I + r n.sigma)/2 ----
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
def D_diag_wall(r,th):
    rho=(np.eye(2)+r*(np.sin(th)*sx+np.cos(th)*sz))/2
    R=sqrtm(rho); rhoN=np.diag(np.diag(rho)); rNi=np.linalg.inv(sqrtm(rhoN))
    D=np.zeros((2,2))
    for j in range(2):
        x=np.zeros((2,2)); x[j,j]=1
        out=rNi@np.diag(np.diag(R@x@R))@rNi
        D[:,j]=np.real(np.diag(out))
    return D,rhoN
print("Example 1: g(r,theta) = (1 - sqrt(1-r^2)) sin^2(theta) / (1 - r^2 cos^2(theta))")
for r,th in [(0.6,1.0),(0.9,0.4),(0.3,2.0),(0.999,np.pi/2),(0.7,0.0),(0.0,1.2)]:
    D,rhoN=D_diag_wall(r,th); ev=np.sort(eigvals(D).real)[::-1]
    g_num=1-ev[1]; g_form=(1-np.sqrt(1-r*r))*np.sin(th)**2/(1-r*r*np.cos(th)**2)
    unital=np.allclose(D.sum(axis=1),1); pres=np.allclose(np.diag(rhoN)@D, np.diag(rhoN))
    print(f"  r={r:5.3f} th={th:4.2f}: gap numeric={g_num:.8f} formula={g_form:.8f}  unital={unital} state-pres={pres}")

# ---- Example 2: M=M_2(x)M_2, N=M_2(x)1, rho isotropic ----
def D_subsystem_wall(rhoAB):
    rhoA=np.einsum('ijkj->ik',rhoAB.reshape(2,2,2,2)); R=sqrtm(rhoAB); RAi=np.linalg.inv(sqrtm(rhoA))
    basis=[np.array([[1,0],[0,0]]),np.array([[0,1],[0,0]]),np.array([[0,0],[1,0]]),np.array([[0,0],[0,1]])]
    D=np.zeros((4,4),complex)
    for j,a in enumerate(basis):
        X=R@np.kron(a,np.eye(2))@R; TrB=np.einsum('ijkj->ik',X.reshape(2,2,2,2)); D[:,j]=(RAi@TrB@RAi).reshape(4)
    return D,rhoA
phi=np.array([1,0,0,1])/np.sqrt(2); P=np.outer(phi,phi)
print("\nExample 2: D is depolarising with q(p) = [1 + p - sqrt((1+3p)(1-p))]/2")
print("   p     lambda_2(numeric)  1-q(formula)   I(A:B)")
for p in [0.0,0.1,0.3,0.5,0.7,0.9,0.99]:
    rhoAB=(1-p)*np.eye(4)/4+p*P; D,rhoA=D_subsystem_wall(rhoAB); ev=np.sort(eigvals(D).real)[::-1]
    q=(1+p-np.sqrt((1+3*p)*(1-p)))/2
    rhoB=np.einsum('ijik->jk',rhoAB.reshape(2,2,2,2)); I=relent(rhoAB,np.kron(rhoA,rhoB))
    print(f"  {p:4.2f}   {ev[1]:.8f}        {1-q:.8f}    {I:.6f}")

# ---- Takesaki check on a random correlated state: D=id iff product ----
print("\nTakesaki check (random states): ||D - id|| vs distance of rho_AB from rho_A (x) rho_B")
for trial in range(4):
    G=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); rho=G@G.conj().T; rho/=np.trace(rho).real
    D,rhoA=D_subsystem_wall(rho); rhoB=np.einsum('ijik->jk',rho.reshape(2,2,2,2))
    print(f"  ||D-id||={np.linalg.norm(D-np.eye(4)):.4f}   ||rho - rhoA(x)rhoB||={np.linalg.norm(rho-np.kron(rhoA,rhoB)):.4f}")
rho=np.kron(np.array([[0.7,0.2],[0.2,0.3]]),np.array([[0.6,0.1j],[-0.1j,0.4]])); D,_=D_subsystem_wall(rho)
print(f"  product state: ||D-id||={np.linalg.norm(D-np.eye(4)):.2e}")

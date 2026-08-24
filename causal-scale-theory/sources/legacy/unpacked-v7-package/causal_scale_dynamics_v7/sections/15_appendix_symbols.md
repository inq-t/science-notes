\appendix

# Symbol dictionary

| symbol | definition | mathematical type / status |
|---|---|---|
| $(M,[g])$ | conformal spacetime | standard Lorentzian conformal geometry |
| $\boldsymbol g$ | conformal metric | section of the weighted metric bundle |
| $\sigma\in\Gamma(\mathcal E[1])$ | positive scale | density-bundle section |
| $g_{\rm phys}=\sigma^{-2}\boldsymbol g$ | physical metric | conformally invariant combination |
| $I_A=\tfrac14D_A\sigma$ | scale tractor | packages the scale two-jet |
| $P_{ab}$ | Schouten tensor | standard conformal curvature tensor |
| $N=-\ln(\sigma/\sigma_c)$ | Weyl e-fold coordinate | additive scale displacement |
| $s$ | vertical modular automorphism parameter | state-preserving modular flow |
| $\eta_A$ | vertical horizon rapidity potential | geometric definition; modular interpretation conditional |
| $\theta$ | horizontal state coordinate | noncentral relative modular polarization |
| $Q=P_+-P_-$ | normal chirality | binary quotient, $Q^2=1$, $JQJ=-Q$ |
| $\Psi(\theta)=\ln(2\cosh\theta)$ | log-partition potential | binary exponential family |
| $\eta=\langle Q\rangle$ | mixture coordinate | $\eta=\tanh\theta$ |
| $G^{\rm BKM}$ | BKM metric | Hessian of Umegaki relative entropy |
| $G^{\perp}_{NN}$ | pullback BKM norm | extensive horizontal capacity per squared e-fold |
| $S_c$ | self-dual wall entropy | Bekenstein--Hawking entropy in the closure law |
| $T_c$ | horizontal modular temperature | canonical $2\pi$ normal-boost normalization |
| $V_c$ | causal-wall volume | areal volume of the crossing apparent horizon |
| $\Ruble$ | scale-capacity number | $(k_B/S_c)G^{\perp}_{NN}(N_c)$; fundamental value $1$ |
| $\vperp$ | horizontal soldering slope | $d\theta/dN$; fundamental representation value $1$ |
| $\rho_X,p_X,w_X$ | effective homogeneous response variables | derived from the scale-capacity source and conservation |
| $N_c,z_c$ | self-dual crossing location | intrinsic event, cosmic date fixed by the solution |
| $\mu_A$ | horizon modular--Weyl index | $(1-q)/2=-I^2/H^2$; running state variable |
| $\Lambda_g,\Lambda_{\rm res}$ | scalar lift/global residual | global sector, not local trace-free source |
| $\mathcal A,\mathcal A^\dagger$ | Witten/Darboux first-order operators | generate the horizontal pair |
| $\mathcal H_\pm$ | horizontal partner operators | one reflectionless Pöschl--Teller partner and one free partner |

# Core derivations

## Binary information geometry

For

$$
\omega_\theta=\frac{e^{\theta Q}}{2\cosh\theta},
\qquad Q^2=1,
$$

the partition potential is

$$
\Psi=\ln\operatorname{tr}e^{\theta Q}=\ln(2\cosh\theta).
$$

Therefore

$$
\Psi'=\tanh\theta,
\qquad
\Psi''=\sech^2\theta,
$$

and

$$
\langle Q\rangle^2+\operatorname{Var}(Q)=1.
$$

## Cocycle soldering

Assume the reduced noncentral Connes cocycle depends on two scales only through $r=\sigma_2/\sigma_1$ and is measurable. Cocycle composition gives

$$
\theta(r_1r_2)=\theta(r_1)+\theta(r_2).
$$

The measurable solutions are

$$
\theta(r)=-\vperp\ln r.
$$

Since $N=-\ln(\sigma/\sigma_c)$,

$$
\theta=\vperp(N-N_c).
$$

The equation fixes the form but not the value of $\vperp$.

## Free-energy Hessian

For a KMS reference state with physical modular Hamiltonian $\mathcal H_c=k_BT_cK_c$,

$$
F_c(\rho)-F_c(\omega_c)=k_BT_cS(\rho\|\omega_c).
$$

At coincidence,

$$
S(\omega_{c+\delta N}\|\omega_c)
=\frac12G^{\perp}_{NN}(N_c)\delta N^2+O(\delta N^3).
$$

Therefore the quadratic free-energy curvature per causal-wall volume is

$$
\rho_{X,c}=\frac{k_BT_c}{2V_c}G^{\perp}_{NN}(N_c).
$$

## Hawking--Friedmann conversion

In $3+1$ dimensional flat FLRW,

$$
R_c=\frac{c}{H_c},
\quad
\frac{S_c}{k_B}=\frac{\pi R_c^2c^3}{G\hbar},
\quad
k_BT_c=\frac{\hbar c}{2\pi R_c}.
$$

Thus

$$
k_BT_c\frac{S_c}{k_B}=\frac{c^4R_c}{2G}=E_{\rm MS,c}.
$$

Since

$$
V_c=\frac{4\pi R_c^3}{3},
$$

$$
\frac{E_{\rm MS,c}}{V_c}=\frac{3c^4}{8\pi GR_c^2}=\frac{3c^2H_c^2}{8\pi G}=\rho_{\rm crit,c}.
$$

## Scale-capacity amplitude

The equivalence law is

$$
G^{\perp}_{NN}(N_c)=\Ruble\frac{S_c}{k_B}.
$$

Therefore

$$
\rho_{X,c}=\frac{\Ruble}{2}\rho_{\rm crit,c}.
$$

For $\Ruble=1$, flatness gives

$$
\rho_{X,c}=\rho_{\rm ordinary,c}=\frac12\rho_{\rm crit,c}.
$$

## General dimension

For $d$ spatial dimensions,

$$
A=\Omega_{d-1}R^{d-1},
\qquad
V=\frac{\Omega_{d-1}}{d}R^d,
$$

and Einstein--Friedmann marginality gives

$$
\frac{k_BT(S/k_B)}{V}=\frac{2}{d-1}\rho_{\rm crit}.
$$

Thus

$$
\Omega_{X,c}=\frac{\Ruble}{d-1},
$$

and

$$
\frac{\rho_{X,c}}{\rho_{\rm ordinary,c}}=
\frac{\Ruble}{d-1-\Ruble}.
$$

## Shape invariant

With

$$
\rho_X=\rho_*\sech^2(N-N_c),
$$

$$
\Delta_X:=-\frac{\dd\ln\rho_X}{\dd N}=2\tanh(N-N_c).
$$

Then

$$
\Delta_X'=2\sech^2(N-N_c)=2-\frac12\Delta_X^2,
$$

so

$$
\Delta_X^2+2\Delta_X'=4.
$$

Using $\Delta_X=3(1+w_X)$ gives

$$
9(1+w_X)^2+6w_X'=4.
$$

## Witten pair

Let $\eta=\tanh\theta$. Then

$$
\eta^2+\eta'=1.
$$

With

$$
\mathcal A=\partial_\theta+\eta,
\qquad
\mathcal A^\dagger=-\partial_\theta+\eta,
$$

$$
\mathcal A^\dagger\mathcal A=-\partial_\theta^2+1-2\sech^2\theta,
$$

$$
\mathcal A\mathcal A^\dagger=-\partial_\theta^2+1.
$$

The normalized zero mode is $\psi_0=2^{-1/2}\sech\theta$.

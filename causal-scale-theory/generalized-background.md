# The Generalized Homogeneous Background

The generalized CST background composes a reduced binary shape, a constitutive homogeneous source, present-flatness branch selection, and ordinary GR--FLRW evolution. It is a **[CONDITIONAL OUTPUT]** whose response has two independent parameters—the width \(\nu\) and the integrated crossing ratio \(\mathfrak R_c\)—while abundances, root branch, and residual-sector data remain additional background inputs. Neither response parameter is a universal constant merely because the unit branch proposes the value one.

Let

$$
x:=N-N_c.
$$

The canonical types are fixed by [[program-core/ruble-equations|the programme core]]:

- \(m:=\langle Q\rangle\) is the normalized binary polarization;
- \(\nu:=|\mathrm d\theta/\mathrm dN|>0\) is the constant width after affine scale--state soldering has been granted;
- \(\mathfrak R_c\) is the integrated state-to-gravitational-entropy ratio evaluated at the distinguished crossing cut.

After balanced binary reduction and the response-orientation choice \(\theta=\nu x\), with \(\nu=|\mathrm d\theta/\mathrm dN|\), [[binary-information-geometry/balanced-exponential-family|the balanced-family theorem]] gives the exact reduced shape

$$
m(x)=\tanh(\nu x),
\qquad
g^{\mathrm{bin}}_{\theta\theta}(x)
=\operatorname{sech}^2(\nu x),
\qquad
m^2+g^{\mathrm{bin}}_{\theta\theta}=1.
$$

This normalized identity does not supply an extensive wall norm or a cosmological density. Those require the independent construction, constant-extensivity assumption, anchored source law, and horizon conversion declared in the core.

With those bridges, spatially flat \(3+1\)-dimensional GR--FLRW, separate response conservation, and a residual-sector choice, the homogeneous interface is

$$
\boxed{
\rho_X(x)
=\frac{\mathfrak R_c}{2}\rho_{\mathrm{crit},c}
\operatorname{sech}^2(\nu x),
\qquad
w_X(x)
=-1+\frac{2\nu}{3}m(x).}
$$

[[causal-scale-theory/theorems/rigid-sech-response-identities|The rigid-response theorem]] owns the equation-of-state derivation and all differential identities. The result is exact given the pulse and separate conservation, but the physical pulse itself remains downstream of constitutive and identification premises.

On the zero-residual branch with no additional crossing component, present flatness yields the branch-valued equation in [[causal-scale-theory/theorems/present-flatness-closure|the closure theorem]]. A nonzero residual or additional sector changes that closure. A chosen root then fixes [[causal-scale-theory/future-asymptotics|the expansion history and future class]], while [[causal-scale-theory/theorems/acceleration-condition|the acceleration theorem]] tests the zero-residual active-mass balance. Width fixes transition shape and asymptotic dilution; \(\mathfrak R_c\) fixes the crossing amplitude; the root fixes the placement of that shape relative to the present epoch.

The two unit principles are logically independent:

$$
\nu=1
\not\Longrightarrow
\mathfrak R_c=1,
\qquad
\mathfrak R_c=1
\not\Longrightarrow
\nu=1.
$$

[[causal-scale-theory/unit-branch|The unit branch]] evaluates their conjunction with one branch and residual choice. [[causal-scale-theory/observables|The observables note]] separates tests of this effective background from tests requiring a covariant wall response.

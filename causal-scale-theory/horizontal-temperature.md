# The Horizontal Temperature Identification

CST uses the unsigned canonical horizon temperature to normalize horizontal state-space response. This choice is a physical identification, distinct from both the exact Hawking--Friedmann product and the dynamical Kodama--Hayward temperature.

For a flat-FLRW apparent horizon of radius $R_A=c/H$, define the canonical $2\pi$ scale

$$
k_BT_{\mathrm{hor}}
:=\frac{\hbar c}{2\pi R_A}.
$$

The dynamical apparent-horizon surface gravity instead supplies

$$
k_BT_{\mathrm{KH}}
=\mu_A k_BT_{\mathrm{hor}},
\qquad
\mu_A:=\left|\frac{1-q}{2}\right|.
$$

They coincide only when $\mu_A=1$. The signed quantity $\widehat\mu_A=(1-q)/2$ belongs to [[causal-scale-theory/horizon-clock|the clock identity]] and must not be inserted into a non-negative temperature without taking its magnitude.

## CST's choice

The background closure stipulates

$$
\boxed{T_c:=T_{\mathrm{hor}}(N_c)}
$$

for the horizontal state-space channel. This retains the canonical boost/KMS $2\pi$ normalization while leaving the dynamical horizon factor outside the conversion.

This is **[IDENTIFICATION — OPEN]**. The exact product in [[causal-scale-theory/hawking-friedmann]] follows once the temperature is chosen, but that algebra does not select the choice.

## Why the distinction matters

Replacing $T_{\mathrm{hor}}$ by $T_{\mathrm{KH}}$ would multiply the source amplitude by $\mu_{A,c}$ and make it depend on the background deceleration at the crossing. That would alter the definition of $\mathfrak R_c$, the equality condition, and the flatness closure.

The canonical choice would be upgraded by a constructed wall modular generator whose KMS normalization is geometrically tied to the horizon boost independently of the solved FLRW response. It fails if the microscopic horizontal generator instead couples to the Kodama--Hayward surface gravity or to another local temperature.

No argument based only on dimensional analysis distinguishes the alternatives.

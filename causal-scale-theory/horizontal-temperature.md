# The Horizontal Temperature Identification

CST identifies the conversion temperature of its horizontal state response with the unsigned canonical apparent-horizon temperature at the crossing. This is an open physical identification; the exact horizon algebra begins only after it has been made.

For a flat-FLRW apparent horizon \(R_A=c/H\), define

$$
k_BT_{\mathrm{hor}}
:=\frac{\hbar c}{2\pi R_A}.
$$

The dynamical Kodama--Hayward temperature is instead

$$
k_BT_{\mathrm{KH}}
=|\widehat\mu_A|\,k_BT_{\mathrm{hor}},
$$

where [[conformal-scale-geometry/horizon-allocation|the signed apparent-horizon index]]

$$
\widehat\mu_A
:=\frac{1-q}{2}
$$

tracks the canonical dynamical factor and integrates to the signed horizon rapidity through \(\mathrm d\widehat\zeta_A=\widehat\mu_A\,\mathrm dN\). The two temperatures coincide only when \(|\widehat\mu_A|=1\); the signed factor itself is not a non-negative temperature.

CST stipulates

$$
\boxed{T_c:=T_{\mathrm{hor}}(N_c).}
$$

The motivation is the canonical boost/KMS \(2\pi\) normalization. No dimensional argument or FLRW identity proves that the physical horizontal generator uses this temperature rather than \(T_{\mathrm{KH}}\) or another local scale.

Changing the temperature prescription would change the source conversion and hence the inferred response amplitude and background closure. It would **not** change the definition of the independently formed integrated ratio \(\mathfrak R_c\). Keeping those statements separate prevents a conversion choice from being mistaken for a state-space normalization.

The identification is upgraded only if a constructed wall modular generator is tied to the horizon boost without using the solved CST background as input. [[wall-construction-interface/elimination-test|The independence test]] makes that requirement precise.

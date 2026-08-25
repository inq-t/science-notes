# Scale Coordinates and Reference Sections

A logarithmic scale coordinate requires a declared reference section, while displacement from a distinguished crossing requires a second, derived subtraction. Keeping those two operations separate prevents the crossing from being used once to define \(N\) and again to define \(x=N-N_c\).

Let \(a_*>0\) be a fixed reference scale factor and let the corresponding conformal scale be \(\sigma_*\), with \(\sigma\propto a^{-1}\) on the FLRW branch. Define

$$
\boxed{
N:=\ln\frac{a}{a_*}
=-\ln\frac{\sigma}{\sigma_*}.}
$$

If \(a_c\) and \(\sigma_c\) denote the distinguished crossing, then its coordinate is

$$
N_c:=\ln\frac{a_c}{a_*}
=-\ln\frac{\sigma_c}{\sigma_*}.
$$

The crossing-centered displacement is therefore

$$
\boxed{
x:=N-N_c
=\ln\frac{a}{a_c}
=-\ln\frac{\sigma}{\sigma_c}.}
$$

These are coordinate identities. Choosing the reference \(a_*=a_c\) is allowed, but then \(N_c=0\) and \(x=N\); one must not subsequently subtract a second nonzero \(N_c\). Choosing the present reference \(a_*=a_0\) instead gives

$$
N_0=0,
\qquad
x_0=-N_c
=\ln\frac{a_0}{a_c}
=\ln(1+z_c).
$$

Thus the common notation \(x_c:=x_0=-N_c\) denotes the present displacement from the crossing when \(N\) is present-centered. Along the same convention,

$$
x=N+x_c.
$$

The reference choice changes coordinate labels, not the scale ratio \(x\), the response profile as a function of \(x\), or the physical location of the crossing. Nor does any choice turn \(N\) into proper time, modular time, or the orientation of factual history; [[cosmodynamics/scale-age|scale-age]] owns those distinctions.

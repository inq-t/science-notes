# Gaussian Refresh as a Projection Frame

For a Gaussian law, conditional refresh in a linear direction is an orthogonal projection on the first Hermite chaos. The complete \(L^2\) gap of a finite sum of such refresh defects equals the least eigenvalue of their first-chaos frame operator. This identifies exactly what a quadratic patch calculation controls, including after a linear gauge quotient; it is not a formula for an arbitrary non-Gaussian law or physical time.

## The whitened carrier

Let \(Y\) have standard Gaussian law on a finite-dimensional Euclidean space \(W\). Choose unit directions \(u_i\) spanning \(W\), rates \(r_i>0\), and
\[
p_i=I-u_i u_i^*,\qquad
E_i f=\mathbb E[f(Y)\mid p_iY],\qquad
H=\sum_i r_i(I-E_i).
\tag{GP1}
\]
The operator acts on Gaussian random variables, not on points \(Y\) themselves. On the first chaos of linear functions \(f_v(Y)=\langle v,Y\rangle\), its matrix is
\[
F=\sum_i r_i u_i u_i^*.
\tag{GP2}
\]

On Hermite degree \(k\), the conditional expectation is the symmetric tensor power \(p_i^{\otimes_s k}\). This follows by conditioning the Gaussian exponential generating function; homogeneous coefficients give the Hermite action. The tensor factors commute and have eigenvalues zero or one, so
\[
I-p_i^{\otimes k}
\ge\frac1k\sum_{j=1}^k
I^{\otimes(j-1)}\otimes(I-p_i)\otimes I^{\otimes(k-j)}.
\]
Summing in \(i\) yields \(H|_{\mathcal H_k}\ge\lambda_{\min}(F)I\) for every \(k\ge1\). First chaos attains the bound, while constants are the kernel. Therefore
\[
\boxed{\operatorname{gap}(H)=\lambda_{\min}(F).}
\tag{GP3}
\]
No finite Hermite truncation is being substituted for the complete Gaussian carrier.

The same proof works for arbitrary orthogonal projections \(p_i\), with
\(F=\sum_i r_i(I-p_i)>0\). Each refresh then resamples the whole subspace
\(\ker p_i\) jointly. It is not the sum of separate scalar refreshes in that subspace: the processes can differ on higher Hermite degrees even when their first-chaos matrices agree.

[[library/adapting-the-gibbs-sampler/inq|Chimisov--Latuszynski--Roberts, Section 2, Theorems 2--3]] give the coordinate-block Gaussian result and linear leading eigenfunction. The projection proof above also treats a declared overcomplete family of directions. Normalized random-scan probabilities and rate-one-per-coordinate generators differ by their total update rate.

## A quotient precision and its projected coordinate updates

Let \(K\ge0\) on \(\mathbb R^m\), with \(K_{ii}>0\), and set \(W=(\ker K)^\perp\). Use the normalized Gaussian on \(W\) with precision \(K|_W\). The original coordinate direction becomes \(\Pi_W e_i\) on the quotient. Refreshing along that line, conditional on the transverse quotient coordinates, becomes after whitening
\[
u_i=\frac{K^{1/2}e_i}{\sqrt{K_{ii}}},\qquad
F=K^{1/2}\operatorname{diag}\!\left(\frac{r_i}{K_{ii}}\right)K^{1/2}\Big|_W.
\tag{GP4}
\]
Each \(u_i\) has norm one; the directions span \(W\). This defines a proper quotient process without integrating an infinite gauge volume.

If \(r_i=1\) and \(K_{ii}=d_0\), then
\[
\operatorname{gap}(H)=\frac{\lambda_{\min}^{+}(K)}{d_0}.
\tag{GP5}
\]
For a color space \(\mathbb R^c\) with precision \(K\otimes I_c\), a rate-one **link** refresh resamples its \(c\) colors together. Its whitened retained projection is \(p_e=(I-u_eu_e^*)\otimes I_c\); the general projection theorem gives \(F=(K/d_0)|_W\otimes I_c\) and the same gap (GP5), with no factor \(c\).

For a fixed linear observable \(f_v(X)=v^*X\), \(v\in W\),
\[
\operatorname{Var}(f_v)=v^*K^+v,\qquad
\langle f_v,Hf_v\rangle=\sum_i\frac{r_i v_i^2}{K_{ii}}.
\tag{GP6}
\]
For equal diagonals and unit rates, Cauchy--Schwarz gives
\[
\frac{\langle f_v,Hf_v\rangle}{\operatorname{Var}(f_v)}
=\frac{\|v\|^2}{d_0\,v^*K^+v}
\le\frac{v^*Kv}{d_0\|v\|^2}.
\tag{GP7}
\]
The inequality need not be equality: a useful geometric trial need not be an eigenvector.

## The Gaussian scope is essential

A further symmetry restriction can remove first chaos. Then (GP3) remains a lower bound on the restricted gap but need not be sharp there. In particular, interior additive gauge reduction and simultaneous adjoint color invariance are different operations.

For a non-Gaussian law, its covariance matrix alone does not give its refresh spectrum. [[weak-coupling-patch-threshold|The weak-coupling patch theorem]] instead proves convergence of the variance and conditional-refresh numerator of one fixed smooth test. That supports a one-sided limiting upper bound, not spectral convergence or a non-Gaussian lower bound.

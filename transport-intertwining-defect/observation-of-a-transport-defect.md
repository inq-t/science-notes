# Observation of a Transport Defect

A nonzero transport defect need not survive observation. Its observable derivative depends on the occupied input, the outgoing evolution, the readout and the nuisance directions admitted by the experiment. A finite linearized experiment therefore sees a quotient of defect space, while stable inference requires a quantitative response bound beyond mere nonvanishing.

## First-order sensitivity after nuisance removal

Use [[transport-intertwining-defect/propagator-intertwining-and-placement|the terminal composite and defect]] with fixed input \(x_i\), endpoints and baseline address \(\sigma_0\). Regard complex carriers as real Banach spaces when differentiating real parameters. Let \(\mathcal O\) be a Fréchet-differentiable observation map near the baseline terminal state into a finite-dimensional real Hilbert space \(Y\), with bounded real-linear derivative
\[
P:=D\mathcal O_{x_f}:X_+\longrightarrow Y.
\tag{WD8a}
\]
Here \(P\) is evaluated at the declared baseline. The observation law has no explicit insertion-address dependence and no additional wall or environment input.

Let \(Z\subset Y\) be the linear tangent space of allowed nuisance changes. Fix the output inner product, including any declared whitening by a positive definite noise covariance, and project orthogonally onto \(Z^\perp\). The residual insertion derivative is
\[
\mathcal S_\sigma(x_i):=\Pi_{Z^\perp}P
U_+(N_f,\sigma)\mathfrak D_\sigma U_-(\sigma,N_i)x_i.
\tag{WD9}
\]
At \(\sigma_0\), one scalar insertion parameter has a nonzero response modulo these linearized nuisances if and only if
\[
\boxed{\|\mathcal S_{\sigma_0}(x_i)\|_Y>0.}
\tag{WD10}
\]
The corresponding first-order change is \(\mathcal S_{\sigma_0}(x_i)\,\delta\sigma+o(|\delta\sigma|)\). This criterion does not assert global identifiability or finite-noise detectability, and a vanishing derivative does not rule out a higher-order signature. Several parameters require the nuisance-projected response map to have full restricted rank. A stable family of experiments requires a uniform lower singular bound in specified parameter and output norms.

The successive maps in (WD9) distinguish a nonzero abstract operator from a nonzero action on occupied inputs, survival under outgoing transport and survival under readout. [[measured-response-carriers/response-pullbacks-and-radicals|Response pullbacks and radicals]] gives the associated parameter quadratic form: its null directions are those killed by the complete analysis map.

## A finite experiment returns a response class

Fix the baseline and a real normed linear space of candidate operators
\[
\mathfrak E_\sigma\subseteq\operatorname{Hom}(D_-,X_+),\qquad
\mathfrak D_\sigma\in\mathfrak E_\sigma,
\tag{WD16a}
\]
on which the following experiment map is bounded:
\[
\mathfrak F_\sigma:\mathfrak E_\sigma\longrightarrow Y,\qquad
\mathfrak F_\sigma(D):=\Pi_{Z^\perp}P
U_+(N_f,\sigma)D U_-(\sigma,N_i)x_i.
\tag{WD17}
\]
The declaration of a norm and boundedness matters when the defect is initially defined only on an unbounded-generator domain. The other factors are held fixed in this linearized operator comparison; changing the entire evolution law is a different inverse problem.

Factoring through the kernel gives the algebraic isomorphism
\[
\overline{\mathfrak F}_\sigma:
\mathfrak E_\sigma/\ker\mathfrak F_\sigma
\xrightarrow{\ \sim\ }\operatorname{im}\mathfrak F_\sigma,\qquad
\overline{\mathfrak F}_\sigma(D+\ker\mathfrak F_\sigma)=\mathfrak F_\sigma(D).
\tag{WD17a}
\]
An exact noiseless linearized response with known baseline distinguishes only
\[
\mathfrak D_\sigma+\ker\mathfrak F_\sigma
\in\mathfrak E_\sigma/\ker\mathfrak F_\sigma.
\tag{WD17b}
\]
Several occupied inputs use the direct sum of their response maps. The rank remains bounded by the total finite output dimension, so a finite readout cannot reconstruct an unrestricted infinite-dimensional defect space. Noisy measurements instead constrain regions in the response model. Equation (WD17) predicts an output derivative, not an observed output value by itself.

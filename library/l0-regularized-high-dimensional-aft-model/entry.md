# $\ell_0$-Regularized High-dimensional Accelerated Failure Time Model

We develop a constructive approach for $\ell_0$-penalized estimation in the sparse accelerated failure time (AFT) model with high-dimensional covariates. Our proposed method is based on Stute's weighted least squares criterion combined with $\ell_0$-penalization. This method is a computational algorithm that generates a sequence of solutions iteratively, based on active sets derived from primal and dual information and root finding according to the KKT conditions. We refer to the proposed method as AFT-SDAR (for support detection and root finding). An important aspect of our theoretical results is that we directly concern the sequence of solutions generated based on the AFT-SDAR algorithm. We prove that the estimation errors of the solution sequence decay exponentially to the optimal error bound with high probability, as long as the covariate matrix satisfies a mild regularity condition which is necessary and sufficient for model identification even in the setting of high-dimensional linear regression. We also proposed an adaptive version of AFT-SDAR, or AFT-ASDAR, which determines the support size of the estimated coefficient in a data-driven fashion. We conduct simulation studies to demonstrate the superior performance of the proposed method over the lasso and MCP in terms of accuracy and speed. We also apply the proposed method to a real data set to illustrate its application.

## Metadata

- **Authors:** Xingdong Feng, Jian Huang, Yuling Jiao, and Shuang Zhang.
- **Year:** 2020.
- **First submitted:** 2020-02-09.
- **Primary category:** `stat.ME`.
- **arXiv:** [2002.03318v1](https://arxiv.org/abs/2002.03318).
- **Local artifacts:** `AFT_SDAR2.9.bbl`, `AFT_SDAR2.9.tex`, `ECA_jasa.bst`, `JASA_manu.sty`, `asa.bst`, `example.eps`, `example1.png`, `example2.png`, `jasa_harvard.sty`, `spbasic.bst`, `spmpsci.bst`, `spphys.bst`, `svglov3.clo`, `svjour3.cls`.

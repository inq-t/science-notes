# Diagonal Charge Balance

Two sectors rigorously carry parts of one conserved charge when they are Hamiltonian representations of the same continuous symmetry. Their moment maps add under the diagonal action, and invariance of the combined dynamics conserves the sum. This standard theorem is the clean mathematical template for the conjecture that modular, gravitational, and record charges are representations of one causal charge.

## Product moment map

Let \(G\) be a Lie group with Lie algebra \(\mathfrak g\). For \(i=1,\ldots,n\), let

$$
(P_i,\Omega_i,\mu_i)
$$

be Hamiltonian \(G\)-spaces, with equivariant moment maps

$$
\mu_i:P_i\longrightarrow\mathfrak g^*.
$$

On the product

$$
P:=P_1\times\cdots\times P_n,
\qquad
\Omega:=\Omega_1\oplus\cdots\oplus\Omega_n,
$$

the diagonal \(G\)-action has moment map

$$
\boxed{
\mu_{\mathrm{tot}}
=\mu_1+\cdots+\mu_n.
}
$$

The sum is well typed because every term lies in the same dual Lie algebra \(\mathfrak g^*\).

## Conservation theorem

Let \(H:P\to\mathbb R\) be a Hamiltonian invariant under the diagonal \(G\)-action. For \(\xi\in\mathfrak g\), define

$$
Q_\xi
:=\langle\mu_{\mathrm{tot}},\xi\rangle.
$$

Then

$$
\boxed{
\frac{\mathrm dQ_\xi}{\mathrm dt}=0.
}
$$

Indeed, the moment-map condition identifies the Hamiltonian vector field of \(Q_\xi\) with the infinitesimal action \(\xi_P\). Hence

$$
\frac{\mathrm dQ_\xi}{\mathrm dt}
=\{Q_\xi,H\}
=-\mathcal L_{\xi_P}H
=0.
$$

Componentwise,

$$
\frac{\mathrm d}{\mathrm dt}
\left(
\langle\mu_1,\xi\rangle+\cdots+
\langle\mu_n,\xi\rangle
\right)=0.
$$

One sector's charge may change while another changes oppositely. Conservation attaches to the diagonal whole, not necessarily to each representation separately.

## Flux form

For a subsystem bounded by two cuts and an intervening wall, the appropriate statement is generally

$$
\boxed{
Q_\xi[\Sigma_2]-Q_\xi[\Sigma_1]
+\mathcal F_\xi[W]=0,
}
$$

where \(\mathcal F_\xi[W]\) is the charge flux through the remaining boundary. Declaring a subsystem charge conserved while omitting its boundary flux is an incomplete application of the theorem.

In gauge theories and gravity, the presymplectic form is degenerate before quotienting constraints, and boundary or corner terms can carry the physical charge. The finite-dimensional theorem is therefore a template, not a direct proof for a causal horizon.

## Application template

The proposed causal application would require Hamiltonian or covariant-presymplectic sectors

$$
P_{\mathrm{state+matter}},
\qquad
P_{\mathrm{grav}},
\qquad
P_{\mathrm{record}},
$$

with one causal boost or dilation group acting diagonally, so that

$$
\boldsymbol\mu_\Sigma^{\mathrm{causal}}
=\boldsymbol\mu_\Sigma^{\mathrm{state+matter}}
+\boldsymbol\mu_\Sigma^{\mathrm{grav}}
+\boldsymbol\mu_\Sigma^{\mathrm{record}}.
$$

Only then would the phrase

$$
\text{state charge}+
\text{geometric charge}+
\text{record charge}
$$

be mathematically literal. [[causal-individuation-balance]] states this as a physical conjecture.

Here the state phase space includes the nongravitational bulk contribution. Splitting it into independent wall and bulk factors would be another application of the product theorem, but only after that factorization and its gauge compatibility have been established.

## Claim boundary

The theorem does not provide the causal group, its normalized generator, the gravitational corner phase space, a state-space moment map, or a record sector. It also does not identify the positive quadratic BKM capacity with the signed linear moment map. That different-type comparison is the task of [[state-geometry-charge-weld]].

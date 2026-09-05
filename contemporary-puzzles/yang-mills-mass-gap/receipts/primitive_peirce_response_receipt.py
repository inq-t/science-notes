"""Exact Albert regular-gap certificate and finite Peirce response checks.

The polynomial certificate uses integer arithmetic with a checked overflow
bound, not rounded eigenvalues. It reuses the repository's explicit Albert
multiplication table. The scalar-commutant proof and invariant orbit moment
are analytic inputs in algebra/primitive-peirce-response.md. This receipt
does not establish a physical field-theory or continuum mass gap.
"""

from __future__ import annotations

import numpy as np

import exceptional_flag_linearization_receipt as jordan


def require_close(label, actual, expected, atol=1e-10):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    if error > atol:
        raise AssertionError(f"{label}: error {error:.6g} exceeds {atol}")


def integer_certificate():
    # M_i = 2 L_bi in the original integral coordinate basis.
    # The trace Gram matrix has diagonal n_i, so D = sum_i ad(L_bi)^2/n_i.
    gram = np.array([1] * 3 + [2] * 24, dtype=np.int64)
    multipliers = np.array([
        [jordan.jordan_product_twice(x, y) for y in jordan.FULL_BASIS]
        for x in jordan.FULL_BASIS
    ], dtype=np.int64).transpose(0, 2, 1)
    if np.max(np.abs(multipliers)) > 2:
        raise AssertionError("multiplication table exceeded construction bound")
    coefficients = 2 // gram
    identity = np.eye(27, dtype=np.int64)
    eight_s = sum(c * m @ m for c, m in zip(coefficients, multipliers))
    # Row-major vectorization: vec(M T M) = (M tensor M^T) vec(T).
    z = np.kron(eight_s, identity) + np.kron(identity, eight_s.T)
    z -= 2 * sum(c * np.kron(m, m.T)
                 for c, m in zip(coefficients, multipliers))
    # Every construction sum above is bounded by
    # 2*27*2*27*4 + 2*27*2*4 < 13000, far below int64 capacity.
    # z represents 8D, not D, and is not symmetric in these coordinates.
    hs_weights = (2 * gram[:, None] // gram[None, :]).reshape(-1)
    if not np.array_equal(hs_weights[:, None] * z, z.T * hs_weights[None, :]):
        raise AssertionError("weighted Hilbert--Schmidt self-adjointness failed")
    if np.any(z @ identity.reshape(-1)):
        raise AssertionError("scalar identity not in kernel")

    rows, columns = np.nonzero(z)
    values = z[rows, columns]
    row_norm = int(np.max(np.sum(np.abs(z), axis=1)))
    roots = (0, 24, 40, 48, 96, 144)
    polynomial = np.eye(729, dtype=np.int64)
    safe_bound = 1  # Python integer; does not overflow.
    bounds = []
    for root in roots:
        # This conservative bound also covers partial sums BEFORE diagonal
        # cancellation in the sparse column accumulation below.
        safe_bound *= row_norm + abs(root)
        if safe_bound >= 2**63:
            raise AssertionError("int64 certificate no longer certified safe")
        bounds.append(safe_bound)
        result = -root * polynomial
        for i, j, value in zip(rows, columns, values):
            result[:, j] += value * polynomial[:, i]
        polynomial = result
    if np.any(polynomial):
        raise AssertionError("exact annihilating polynomial failed")
    print("PASS exact polynomial for 8D, roots:", roots)
    print("PASS conservative integer intermediate bounds:", bounds)
    print(f"PASS matrix certificate: shape={z.shape}, nnz={len(values)}, "
          f"max_entry={int(np.max(np.abs(z)))}")
    return gram, multipliers


def finite_checks(gram, multipliers):
    scales = np.sqrt(gram)
    regulars = np.array([
        (m / 2) * scales[:, None] / scales[None, :] / scales[i]
        for i, m in enumerate(multipliers)
    ])
    identity = np.eye(27)
    unit = np.array([1.0] * 3 + [0.0] * 24)
    unit_projection = np.outer(unit, unit) / 3
    square_sum = sum(l @ l for l in regulars)
    require_close("sum of multiplier squares", square_sum,
                  3 * identity + 6 * unit_projection)

    def response(t):
        return square_sum @ t + t @ square_sum - 2 * sum(
            l @ t @ l for l in regulars)

    derivation = regulars[0] @ regulars[3] - regulars[3] @ regulars[0]
    if np.linalg.norm(derivation) == 0:
        raise AssertionError("missing nonzero sharpness witness")
    require_close("sharp derivation eigenvalue", response(derivation),
                  3 * derivation)
    balance = 27 * unit_projection - identity
    require_close("balance eigenvalue", response(balance), 18 * balance)
    for i, l in enumerate(regulars):
        scalar = unit[i] / 3
        require_close("regular image eigenvalue", response(l),
                      6 * (l - scalar * identity))

    # Independent finite diagnostic for the differentiated cyclic context:
    # its restriction to derivations retains 16 of the 52 real directions.
    # The exact Haar frame uses the analytic adjoint irreducibility proof.
    commutators = np.stack([
        (regulars[i] @ regulars[j] - regulars[j] @ regulars[i]).reshape(-1)
        for i in range(27) for j in range(i + 1, 27)
    ], axis=1)
    vectors, singular_values, _ = np.linalg.svd(commutators, full_matrices=False)
    rank = int(np.sum(singular_values > 1e-9))
    if rank != 52:
        raise AssertionError(f"unexpected derivation rank {rank}")
    derivation_basis = vectors[:, :rank]
    w = identity.copy()
    for block in range(3):
        start = 3 + 8 * block
        for j in range(2, 8):
            w[start + j, start + j] = -0.5
            sign, output = jordan.OCTONION_TABLE[1][j]
            w[start + output, start + j] += np.sqrt(3) * sign / 2
    w2 = w @ w
    require_close("cyclic automorphism cube", w2 @ w, identity)
    twirled = np.stack([
        ((t + w @ t @ w.T + w2 @ t @ w2.T) / 3).reshape(-1)
        for t in derivation_basis.T.reshape(-1, 27, 27)
    ], axis=1)
    adjoint_expectation = derivation_basis.T @ twirled
    require_close("derivation context preserves carrier", twirled,
                  derivation_basis @ adjoint_expectation)
    require_close("adjoint expectation projection",
                  adjoint_expectation @ adjoint_expectation,
                  adjoint_expectation)
    require_close("centralizer dimension", np.trace(adjoint_expectation), 16)
    require_close("adjoint loss ratio",
                  (52 - np.trace(adjoint_expectation)) / 52, 9 / 13)

    lp = regulars[0]  # p = diag(1,0,0), primitive of trace one.
    projections = (
        2 * lp @ lp - lp,
        4 * lp - 4 * lp @ lp,
        identity - 3 * lp + 2 * lp @ lp,
    )
    require_close("Peirce projection sum", sum(projections), identity)
    for i, (projection, rank) in enumerate(zip(projections, (1, 16, 10))):
        require_close("Peirce rank", np.trace(projection), rank)
        require_close("Peirce self-adjointness", projection, projection.T)
        for j, other in enumerate(projections):
            require_close("Peirce orthogonality", projection @ other,
                          projection if i == j else np.zeros((27, 27)))

    def pinch(t):
        return sum(p @ t @ p for p in projections)

    require_close("balance loss ratio",
                  np.linalg.norm(balance - pinch(balance))**2
                  / np.linalg.norm(balance)**2, 6 / 13)
    rng = np.random.default_rng(105)
    for _ in range(12):
        t = rng.normal(size=(27, 27)) + 1j * rng.normal(size=(27, 27))
        loss = np.linalg.norm(t - pinch(t))**2
        commutator = np.linalg.norm(lp @ t - t @ lp)**2
        if not commutator - 1e-10 <= loss <= 4 * commutator + 1e-10:
            raise AssertionError("pinching--commutator comparison failed")
        u = t @ t.conj().T
        rho = u / np.trace(u)
        sigma = pinch(rho)

        def entropy(state):
            eigenvalues = np.linalg.eigvalsh(state)
            if eigenvalues.min() <= 0:
                raise AssertionError("test density not faithful")
            return -float(np.sum(eigenvalues * np.log(eigenvalues)))

        entropy_loss = entropy(sigma) - entropy(rho)
        hs_loss = float(np.linalg.norm(rho - sigma)**2)
        if entropy_loss + 1e-10 < hs_loss / 2:
            raise AssertionError("finite entropy quadratic lower bound failed")
        if np.log(27) - entropy(rho) > (
                27 * np.linalg.norm(rho - identity / 27)**2 + 1e-10):
            raise AssertionError("relative entropy upper bound failed")

    print("PASS multiplier identities and sharp eigenvalue-3 witness")
    print("PASS numerical adjoint-context diagnostic: rank 52, retained 16, lost 36")
    print("PASS Peirce ranks (1,16,10) and balance loss ratio 6/13")
    print("PASS finite commutator comparisons and entropy controls")
    print("SCOPE orbit moment and scalar-only kernel use the analytic proof")
    print("SCOPE no assertion of continuum coverage or physical clock rate")


if __name__ == "__main__":
    finite_checks(*integer_certificate())

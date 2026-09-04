"""Finite checks for the vacuum-aligned transfer cocycle."""

from __future__ import annotations

import numpy as np


def op_norm(operator: np.ndarray) -> float:
    return float(np.linalg.svd(operator, compute_uv=False)[0])


def positive_power(operator: np.ndarray, exponent: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(operator)
    assert np.all(eigenvalues > 0.0)
    return (eigenvectors * eigenvalues**exponent) @ eigenvectors.T.conj()


def block_norm_matrix(
    operator: np.ndarray,
    output_blocks: list[list[int]],
    input_blocks: list[list[int]],
) -> np.ndarray:
    result = np.zeros((len(output_blocks), len(input_blocks)))
    for row, output_indices in enumerate(output_blocks):
        for column, input_indices in enumerate(input_blocks):
            block = operator[np.ix_(output_indices, input_indices)]
            result[row, column] = op_norm(block)
    return result


def main() -> None:
    first_centered = np.array(
        [
            [0.35, 0.08, -0.04],
            [0.02, 0.28, 0.05],
            [0.06, -0.03, 0.22],
            [0.01, 0.04, 0.18],
        ]
    )
    second_centered = np.array(
        [
            [0.42, -0.05, 0.03, 0.01],
            [0.02, 0.31, -0.04, 0.05],
            [0.01, 0.06, 0.27, -0.02],
        ]
    )
    initial_blocks = [[0], [1, 2]]
    middle_blocks = [[0, 1], [2, 3]]
    final_blocks = [[0], [1, 2]]

    first_majorant = block_norm_matrix(
        first_centered, middle_blocks, initial_blocks
    )
    second_majorant = block_norm_matrix(
        second_centered, final_blocks, middle_blocks
    )
    product_centered = second_centered @ first_centered
    exact_product_blocks = block_norm_matrix(
        product_centered, final_blocks, initial_blocks
    )
    product_majorant = second_majorant @ first_majorant

    assert np.all(exact_product_blocks <= product_majorant + 1e-12)
    assert op_norm(product_centered) <= op_norm(product_majorant) + 1e-12

    first_full = np.zeros((5, 4))
    first_full[0, 0] = 1.0
    first_full[1:, 1:] = first_centered
    second_full = np.zeros((4, 5))
    second_full[0, 0] = 1.0
    second_full[1:, 1:] = second_centered
    initial_vacuum = np.array([1.0, 0.0, 0.0, 0.0])
    middle_vacuum = np.array([1.0, 0.0, 0.0, 0.0, 0.0])
    final_vacuum = np.array([1.0, 0.0, 0.0, 0.0])
    assert np.allclose(first_full @ initial_vacuum, middle_vacuum)
    assert np.allclose(first_full.T @ middle_vacuum, initial_vacuum)
    assert np.allclose(second_full @ middle_vacuum, final_vacuum)
    assert np.allclose(second_full.T @ final_vacuum, middle_vacuum)

    # Forward vacuum preservation alone is enough for exact centered
    # composition. These arrows deliberately fail adjoint vacuum
    # preservation: excited directions may fall into the vacuum line, but
    # the vacuum line cannot return to the centered carrier.
    forward_only_first = np.array(
        [
            [1.0, 0.31, -0.17],
            [0.0, 0.42, 0.08],
            [0.0, -0.06, 0.37],
        ]
    )
    forward_only_second = np.array(
        [
            [1.0, -0.23, 0.19],
            [0.0, 0.51, -0.04],
            [0.0, 0.07, 0.33],
        ]
    )
    forward_vacuum = np.array([1.0, 0.0, 0.0])
    forward_complement = np.diag([0.0, 1.0, 1.0])
    assert np.allclose(forward_only_first @ forward_vacuum, forward_vacuum)
    assert np.allclose(forward_only_second @ forward_vacuum, forward_vacuum)
    assert not np.allclose(
        forward_only_first.T @ forward_vacuum, forward_vacuum
    )
    centered_first = (
        forward_complement @ forward_only_first @ forward_complement
    )
    centered_second = (
        forward_complement @ forward_only_second @ forward_complement
    )
    centered_direct = (
        forward_complement
        @ forward_only_second
        @ forward_only_first
        @ forward_complement
    )
    centered_iterated = centered_second @ centered_first
    assert np.allclose(centered_direct, centered_iterated)

    walsh = np.array([[1.0, 1.0], [1.0, -1.0]]) / np.sqrt(2.0)
    walsh_shadow = np.abs(walsh)
    walsh_composite_shadow = np.abs(walsh @ walsh)
    walsh_shadow_product = walsh_shadow @ walsh_shadow
    assert np.all(walsh_composite_shadow <= walsh_shadow_product + 1e-12)
    assert np.isclose(walsh_composite_shadow[0, 1], 0.0)
    assert np.isclose(walsh_shadow_product[0, 1], 1.0)

    retained = 0.61
    complementary_first = np.diag([1.0, retained])
    complementary_second = np.diag([retained, 1.0])
    complementary_product = complementary_second @ complementary_first
    assert np.isclose(op_norm(complementary_first), 1.0)
    assert np.isclose(op_norm(complementary_second), 1.0)
    assert np.allclose(complementary_product, retained * np.eye(2))
    first_defect = (
        np.eye(2) - complementary_first.T @ complementary_first
    )
    second_defect = (
        np.eye(2) - complementary_second.T @ complementary_second
    )
    transported_defect = (
        first_defect
        + complementary_first.T
        @ second_defect
        @ complementary_first
    )
    total_product_defect = (
        np.eye(2) - complementary_product.T @ complementary_product
    )
    assert np.allclose(transported_defect, total_product_defect)
    assert np.allclose(
        transported_defect,
        (1.0 - retained**2) * np.eye(2),
    )

    transfer = np.array([[0.73, 0.12], [0.12, 0.55]])
    visible = np.diag([1.0, 0.0])
    hidden = np.eye(2) - visible
    direct_visible = visible @ transfer @ transfer @ visible
    naive_visible = visible @ transfer @ visible @ transfer @ visible
    memory_residue = visible @ transfer @ hidden @ transfer @ visible
    assert np.allclose(direct_visible, naive_visible + memory_residue)
    assert np.isclose(memory_residue[0, 0], 0.12**2)

    probability = 0.8
    vacuum_reference = np.eye(2) / np.sqrt(2.0)
    vacuum_target = np.diag(
        [np.sqrt(probability), np.sqrt(1.0 - probability)]
    )
    phases = np.diag(
        [
            np.exp(1j * np.log(2.0 * probability)),
            np.exp(1j * np.log(2.0 * (1.0 - probability))),
        ]
    )
    real_cocycle_image = phases @ vacuum_reference
    half_density = np.diag(
        [
            np.sqrt(2.0 * probability),
            np.sqrt(2.0 * (1.0 - probability)),
        ]
    )
    assert np.allclose(
        np.abs(np.diag(real_cocycle_image)),
        np.array([1.0, 1.0]) / np.sqrt(2.0),
    )
    assert not np.allclose(real_cocycle_image, vacuum_target)
    assert np.allclose(half_density @ vacuum_reference, vacuum_target)
    assert not np.allclose(half_density.T @ half_density, np.eye(2))

    # Three faithful, pairwise noncommuting states test the multiplication
    # order in the finite-dimensional Araki amplitude chain rule.
    def rotated_density(weight: float, angle: float) -> np.ndarray:
        rotation = np.array(
            [
                [np.cos(angle), -np.sin(angle)],
                [np.sin(angle), np.cos(angle)],
            ]
        )
        return rotation @ np.diag([weight, 1.0 - weight]) @ rotation.T

    density_0 = rotated_density(0.68, 0.11)
    density_1 = rotated_density(0.79, 0.57)
    density_2 = rotated_density(0.61, -0.36)
    amplitude_1_0 = positive_power(density_1, 0.5) @ positive_power(
        density_0, -0.5
    )
    amplitude_2_1 = positive_power(density_2, 0.5) @ positive_power(
        density_1, -0.5
    )
    amplitude_2_0 = positive_power(density_2, 0.5) @ positive_power(
        density_0, -0.5
    )
    amplitude_chain = amplitude_2_1 @ amplitude_1_0
    reverse_chain = amplitude_1_0 @ amplitude_2_1
    assert np.allclose(amplitude_chain, amplitude_2_0)
    assert not np.allclose(reverse_chain, amplitude_2_0)
    assert np.allclose(
        amplitude_chain @ positive_power(density_0, 0.5),
        positive_power(density_2, 0.5),
    )

    print("vacuum-aligned transfer cocycle receipt: PASS")
    print(
        "rectangular exact/product-majorant norms = "
        f"{op_norm(product_centered):.9f} / "
        f"{op_norm(product_majorant):.9f}"
    )
    print(
        "strict Walsh off-diagonal exact/majorant = "
        f"{walsh_composite_shadow[0, 1]:.9f} / "
        f"{walsh_shadow_product[0, 1]:.9f}"
    )
    print(
        "forward-only centered composition residue = "
        f"{op_norm(centered_direct - centered_iterated):.9f}"
    )
    print(
        "complementary one-step/product norms = "
        f"{op_norm(complementary_first):.9f}, "
        f"{op_norm(complementary_second):.9f} / "
        f"{op_norm(complementary_product):.9f}"
    )
    print(
        "transported defect-frame floor = "
        f"{np.linalg.eigvalsh(transported_defect)[0]:.9f}"
    )
    print(f"leave-and-return residue = {memory_residue[0, 0]:.9f}")
    print(
        "real cocycle diagonal moduli = "
        f"{np.abs(np.diag(real_cocycle_image)).tolist()}"
    )
    print(
        "target diagonal moduli = "
        f"{np.abs(np.diag(vacuum_target)).tolist()}"
    )
    print(
        "noncommuting Araki chain/reverse residues = "
        f"{op_norm(amplitude_chain - amplitude_2_0):.9f} / "
        f"{op_norm(reverse_chain - amplitude_2_0):.9f}"
    )


if __name__ == "__main__":
    main()

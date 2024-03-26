"""Computation of the harmonic sum."""

from fractions import Fraction

import utils


def compute_harmonic_sum(n: int) -> Fraction:
    """Returns the harmonic sum computed of to the n-th term."""
    if n <= 0:
        raise ValueError(f"harmonic sum cannot be computed to a negative term! Got {n}")
    if n == 1:
        return Fraction(1)

    return Fraction(1, n) + compute_harmonic_sum(n - 1)


def main() -> None:
    """Compute the harmonic sum to the n-th term."""
    number_of_terms = utils.get_int_from_user("Enter a positive number: ", value_min=1)
    harmonic_sum = compute_harmonic_sum(number_of_terms)
    print(
        f"Harmonic sum to the {number_of_terms}-th term is {harmonic_sum} ({float(harmonic_sum)})"
    )


if __name__ == "__main__":
    main()

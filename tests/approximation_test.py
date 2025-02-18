import unittest

import sympy as sp

from src.c_space import derivative_forms, vectors, integral_forms
from src.approximation import matrix_of


def hilbert_matrix(n):
    return sp.Matrix(
        [[sp.Rational(1, i + j - 1) for j in range(1, n + 1)] for i in range(1, n + 1)]
    )


class TestMatrixOf(unittest.TestCase):
    def test_for_taylor_polynomials(self):
        x, n = sp.symbols("x n")

        self.assertEqual(
            matrix_of(derivative_forms(1), vectors(x**n, 1)),
            sp.Matrix([[1, 0], [0, 1]]),
        )
        self.assertEqual(
            matrix_of(derivative_forms(3), vectors(x**n, 3)),
            sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 6]]),
        )

    def test_with_moment_measures(self):
        x, n = sp.symbols("x n")

        self.assertEqual(
            matrix_of(integral_forms(x**n, 4), vectors(x**n, 4)),
            hilbert_matrix(5),
        )

    def test_with_legendre_polynomials(self):
        x, n = sp.symbols("x n")

        self.assertEqual(
            matrix_of(
                integral_forms(sp.legendre(n, x), 2, a=-1, b=1),
                vectors(sp.legendre(n, x), 2),
            ),
            sp.Matrix([[2, 0, 0], [0, sp.S(2) / 3, 0], [0, 0, sp.S(2) / 5]]),
        )


if __name__ == "__main__":
    unittest.main()

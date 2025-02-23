import unittest

import numpy as np
import sympy as sp

from src.c_space import (
    derivative_forms,
    vectors,
    integral_forms,
    nth_legendre_approximation,
)
from src.approximation import matrix_of, approximation


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


class TestApproximation(unittest.TestCase):
    def test_for_taylor_polynomials(self):
        x, n = sp.symbols("x n")

        for func in [sp.sin(x), sp.exp(x), x**2]:
            for n0 in [0, 2]:
                self.assertEqual(
                    approximation(derivative_forms(n0), vectors(x**n, n0), func),
                    func.series(n=n0 + 1).removeO(),
                    "Failed for func = {}, n = {}".format(func, n0),
                )

    def test_for_legendre_polynomials(self):
        x, n = sp.symbols("x n")

        for func in [sp.sin(x), sp.exp(x), x**2]:
            for n0 in [0, 2]:
                f = approximation(
                    integral_forms(sp.legendre(n, x), n0, a=-1, b=1),
                    vectors(sp.legendre(n, x), n0),
                    func,
                )
                g = nth_legendre_approximation(func, n0)
                self.assertLessEqual(
                    supremum_norm(f, g),
                    1e-10,
                    "Failed for func = {}, n = {}".format(func, n0),
                )


def supremum_norm(f, g, a=-1, b=1, num_points=1000):
    """
    Calculate the supremum norm (maximum absolute difference) between two sympy functions f and g
    over a given interval.

    Parameters:
    f, g: sympy function expressions
    interval: tuple, (a, b) the interval over which to calculate the supremum norm
    num_points: int, number of points to sample between the interval for estimation

    Returns:
    float: the supremum norm between f and g on the given interval
    """
    x_vals = np.linspace(a, b, num_points)
    diff_vals = np.abs(sp.lambdify("x", f)(x_vals) - sp.lambdify("x", g)(x_vals))
    return np.max(diff_vals)


if __name__ == "__main__":
    unittest.main()

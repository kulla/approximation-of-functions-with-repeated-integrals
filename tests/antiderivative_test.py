import unittest

import sympy as sp

from src.antiderivative import (
    antiderivative,
    repeated_antiderivative,
    antiderivative_integral,
)


class TestAntidervative(unittest.TestCase):
    def test_function_returns_antidervative(self):
        x, a, b = sp.symbols("x a b")

        self.assertEqual(antiderivative(x, a, b), (b**2 - a**2) / 2)
        self.assertEqual(antiderivative(x**2, 0, 1), sp.Integer(1) / 3)
        self.assertEqual(antiderivative(sp.exp(x), a, b), sp.exp(b) - sp.exp(a))


class TestRepeatedAntiderivative(unittest.TestCase):
    def test_returns_antiderivative_for_n_equals_zero(self):
        x, a, b = sp.symbols("x a b")

        self.assertEqual(
            repeated_antiderivative(0, sp.sin(x), a, b), antiderivative(sp.sin(x), a, b)
        )
        self.assertEqual(repeated_antiderivative(0, x, a, b), b**2 / 2 - a**2 / 2)
        self.assertEqual(
            repeated_antiderivative(0, sp.exp(x), a, b), antiderivative(sp.exp(x), a, b)
        )

    def test_higher_values_for_n(self):
        x, a, b = sp.symbols("x a b")

        self.assertTrue(
            repeated_antiderivative(1, x, a, b).equals(
                b**3 / 6 - a**3 / 6 - a**2 / 2 * (b - a)
            )
        )
        self.assertTrue(
            repeated_antiderivative(1, sp.exp(x), a, b).equals(
                sp.exp(b) + sp.exp(a) * (a - b - 1)
            )
        )
        self.assertEqual(repeated_antiderivative(2, x, 0, b), b**4 / 24)


class TestAntiderivativeIntegral(unittest.TestCase):
    def test_returns_repeated_antidervative(self):
        x, a, b = sp.symbols("x a b")

        for f in [x, sp.sin(x), sp.exp(x)]:
            for n in range(5):
                self.assertTrue(
                    antiderivative_integral(n, f, a, b).equals(
                        repeated_antiderivative(n, f, a, b)
                    )
                )


if __name__ == "__main__":
    unittest.main()

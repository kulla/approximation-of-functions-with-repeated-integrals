import unittest

import sympy as sp

from src.antiderivative import antiderivative, repeated_antiderivative


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


if __name__ == "__main__":
    unittest.main()

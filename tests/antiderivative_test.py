import unittest

import sympy as sp

from src.antiderivative import antiderivative


class TestAntidervative(unittest.TestCase):
    def test_function_returns_antidervative(self):
        x, a, b = sp.symbols("x a b")

        self.assertEqual(antiderivative(x, a, b), (b**2 - a**2) / 2)
        self.assertEqual(antiderivative(x**2, 0, 1), sp.Integer(1) / 3)
        self.assertEqual(antiderivative(sp.exp(x), a, b), sp.exp(b) - sp.exp(a))


if __name__ == "__main__":
    unittest.main()

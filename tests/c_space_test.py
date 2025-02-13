import unittest

import sympy as sp

from src.c_space import inner_product, integral_form


class TestInnerProduct(unittest.TestCase):
    def test_returnes_inner_product(self):
        x = sp.Symbol("x")

        self.assertEqual(inner_product(x, x, 0, 1), sp.Rational(1, 3))
        self.assertEqual(inner_product(sp.sin(x), sp.sin(x), 0, sp.pi), sp.pi / 2)
        self.assertEqual(inner_product(sp.exp(x), sp.exp(x), 0, 1), (sp.exp(2) - 1) / 2)


class TestIntegralForm(unittest.TestCase):
    def test_returns_linear_form(self):
        x = sp.Symbol("x")

        self.assertEqual(integral_form(x, 0, 1)(x), sp.Rational(1, 3))
        self.assertEqual(integral_form(sp.sin(x), 0, sp.pi)(sp.sin(x)), sp.pi / 2)
        self.assertEqual(integral_form(sp.exp(x), 0, 1)(sp.exp(x)), (sp.exp(2) - 1) / 2)


if __name__ == "__main__":
    unittest.main()

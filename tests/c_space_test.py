import unittest

import sympy as sp

from src.c_space import inner_product


class TestInnerProduct(unittest.TestCase):
    def test_returnes_inner_product(self):
        x = sp.Symbol("x")

        self.assertEqual(inner_product(x, x, 0, 1), sp.Rational(1, 3))
        self.assertEqual(inner_product(sp.sin(x), sp.sin(x), 0, sp.pi), sp.pi / 2)
        self.assertEqual(inner_product(sp.exp(x), sp.exp(x), 0, 1), (sp.exp(2) - 1) / 2)


if __name__ == "__main__":
    unittest.main()

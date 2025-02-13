"""
This module provides functionality to work with the space C([a,b]),
the space of continuous real-valued functions defined on the closed interval [a, b],
using SymPy, a Python library for symbolic mathematics.
"""

import sympy as sp


def inner_product(f, g, a, b, x=sp.Symbol("x")):
    """
    Compute the inner product of two functions f and g in C([a,b]).
    """
    return sp.integrate(f * g, (x, a, b))

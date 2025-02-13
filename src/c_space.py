"""
This module provides functionality to work with the space C([a,b]),
the space of continuous real-valued functions defined on the closed interval [a, b],
using SymPy, a Python library for symbolic mathematics.
"""

import sympy as sp

from functools import partial
from sympy.abc import x, a, b


def inner_product(f, g, a=a, b=b, x=x):
    """
    Compute the inner product of two functions f and g in C([a,b]).
    """
    return sp.integrate(f * g, (x, a, b))


def integral_linear_form(f, a=a, b=b, x=x):
    """
    Create a linear form based on the inner product with a fixed function f.
    """
    return partial(inner_product, f, a=a, b=b, x=x)

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


def integral_form(f, a=a, b=b, x=x):
    """
    Create a linear form based on the inner product with a fixed function f.
    """
    return partial(inner_product, f, a=a, b=b, x=x)


def integral_forms(f, n, a=0, b=1, x=x):
    return [integral_form(f.subs({"n": i}), a, b, x) for i in range(n)]


def vectors(f, n):
    return [f.subs({"n": i}) for i in range(n)]


def derivative_form(n, x0=0, x=x):
    def derivative(f, x=x):
        if n == 0:
            return f.subs(x, x0)
        else:
            return sp.diff(f, x, n).subs(x, x0)

    return derivative


def derivative_forms(n, x0=0, x=x):
    return [derivative_form(i, x0, x) for i in range(n)]

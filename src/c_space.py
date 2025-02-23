"""
This module provides functionality to work with the space C([a,b]),
the space of continuous real-valued functions defined on the closed interval [a, b],
using SymPy, a Python library for symbolic mathematics.
"""

import numpy as np
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
    return [integral_form(f.subs({"n": i}), a, b, x) for i in range(n + 1)]


def vectors(f, n):
    return [f.subs({"n": i}) for i in range(n + 1)]


def derivative_form(n, x0=0, x=x):
    def derivative(f, x=x):
        if n == 0:
            return f.subs(x, x0)
        else:
            return sp.diff(f, x, n).subs(x, x0)

    return derivative


def derivative_forms(n, x0=0, x=x):
    return [derivative_form(i, x0, x) for i in range(n + 1)]


def nth_legendre_approximation(f, n, x=sp.symbols("x")):
    polynomials = [sp.legendre(i, x) * sp.sqrt((2 * i + 1) / 2) for i in range(n + 1)]
    coefficients = [sp.integrate(f * polynomials[i], (x, -1, 1)) for i in range(n + 1)]

    return sum(coef * p for coef, p in zip(coefficients, polynomials))


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

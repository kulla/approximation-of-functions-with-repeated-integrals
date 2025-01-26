import sympy as sp

x = sp.symbols("x")


def antiderivative(f, a, b, x=x):
    return sp.integrate(f, (x, a, b))

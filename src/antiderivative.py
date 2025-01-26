import sympy as sp

x = sp.symbols("x")


def antiderivative(f, a, b, x=x):
    """
    Returns the antiderivative of $f$ from $a$ to $b$.
    """
    return sp.integrate(f, (x, a, b))

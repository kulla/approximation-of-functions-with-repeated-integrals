import sympy as sp

x = sp.symbols("x")


def antiderivative(f, a, b, x=x):
    """
    Returns the antiderivative of $f$ from $a$ to $b$.
    """
    return sp.integrate(f, (x, a, b))


def repeated_antiderivative(n, f, a, b, x=x):
    """
    Returns the nth antiderivative $F_n(b)$ of $f$. $F_n(x)$ is defined as:

    1. $F_0(x) = \\int_a^x f(t) \\mathrm dt$
    2. $F_n(x) = \\int_a^x F_{n-1}(t) \\mathrm dt$
    """
    if n < 0:
        raise TypeError("n must be greater than or equal to zero")

    result = f

    for i in range(n + 1):
        result = antiderivative(result, a, b if i == n else x, x=x)

    return result


def antiderivative_integral(n, f, a, b):
    """
    Use the formula of Cauchy's repeated integral to calculate the antiderivative of $f$ from $a$ to $b$.
    """
    return sp.integrate((b - x) ** n / sp.factorial(n) * f, (x, a, b))

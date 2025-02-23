import sympy as sp


def matrix_of(linear_forms, vectors):
    return sp.Matrix([[M(b) for b in vectors] for M in linear_forms])


def approximation(linear_forms, vectors, func):
    matrix = matrix_of(linear_forms, vectors)
    coefficients = matrix.solve(sp.Matrix([lf(func) for lf in linear_forms]))

    return sum(coeff * basis for coeff, basis in zip(coefficients, vectors))

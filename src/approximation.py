import sympy as sp


def matrix_of(linear_forms, vectors):
    return sp.Matrix([[M(b) for b in vectors] for M in linear_forms])

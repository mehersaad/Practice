"""A custom module for special functions developed by Meher Md Saad
Visit github page for more info:
https://github.com/mehermdsaad
"""

import sympy as sp

x = sp.symbols('x')


def multiply_by_x(expr, n):
    """Function which multiplies input expression by x required number of times

    Returns
    -------
    List with each of the iterations

    """

    list = []
    for _ in [1] * n:
        expr = expr * x
        list.append(sp.expand(expr))

    return list

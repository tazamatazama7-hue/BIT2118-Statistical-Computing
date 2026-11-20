"""Source code for Task 12 – Polynomial and Nonlinear Equation Solving."""

import numpy as np
from scipy.optimize import root

def equations(z):
    x, y = z
    return [x**2 + y**2 - 4,
            y - (x**2 - 1)]

for guess in ([1.,1.], [-1.,1.]):
    sol = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection:", sol.x)
    print("Residuals:", equations(sol.x))
    print("Converged:", sol.success)
    print()

"""Source code for Task 7 – Gaussian Elimination and LU Decomposition."""

import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([[4., -1., 0.],
              [-1., 4., -1.],
              [0., -1., 3.]])
measurement_sets = [
    np.array([15., 10., 10.]),
    np.array([16., 11., 9.]),
    np.array([14., 12., 11.])
]

lu, piv = lu_factor(A)  # factor once
for number, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    print("Set", number, "solution:", x)
    print("Residual norm:", np.linalg.norm(b - A @ x))

print("Direct check:", np.linalg.solve(A, measurement_sets[0]))

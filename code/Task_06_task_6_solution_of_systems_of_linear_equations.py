"""Source code for Task 6 – Solution of Systems of Linear Equations."""

import numpy as np

A = np.array([[4., 2.], [8., 12.]])
b = np.array([20., 72.])
solution = np.linalg.solve(A, b)

print("Type A:", solution[0])
print("Type B:", solution[1])
print("Verification:", A @ solution)
print("Residual:", b - A @ solution)

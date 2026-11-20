"""Source code for Task 8 – Iterative Methods for Linear Systems."""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2.,-1.,0.,0.,0.],
              [-1.,2.,-1.,0.,0.],
              [0.,-1.,2.,-1.,0.],
              [0.,0.,-1.,2.,-1.],
              [0.,0.,0.,-1.,2.]])
b = np.array([100., 0., 0., 0., 20.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        new = (b - R @ x) / D
        err = np.linalg.norm(new - x, ord=np.inf)
        errors.append(err)
        if err < tol:
            return new, errors
        x = new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i,:i] @ x[:i]
                    - A[i,i+1:] @ old[i+1:]) / A[i,i]
        err = np.linalg.norm(x-old, ord=np.inf)
        errors.append(err)
        if err < tol:
            return x, errors
    return x, errors

xj, ej = jacobi(A, b)
xg, eg = gauss_seidel(A, b)
print("Jacobi:", xj)
print("Gauss-Seidel:", xg)
print("Direct solution:", np.linalg.solve(A, b))
plt.semilogy(ej, label="Jacobi")
plt.semilogy(eg, label="Gauss-Seidel")
plt.xlabel("Iteration"); plt.ylabel("Maximum change")
plt.title("Convergence of iterative temperature solution")
plt.legend(); plt.grid(True); plt.show()

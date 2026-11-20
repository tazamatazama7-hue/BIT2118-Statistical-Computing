"""Source code for Task 19 – Numerical Optimization."""

import numpy as np
from scipy.optimize import minimize

def cost(z):
    x, y = z
    return 12*x + 18*y

def capacity_constraint(z):
    x, y = z
    return 100*x + 170*y - 1000

constraints = {"type": "ineq", "fun": capacity_constraint}
bounds = [(0, None), (0, None)]
sol = minimize(cost, x0=[5,3], method="SLSQP",
               bounds=bounds, constraints=constraints)

x, y = sol.x
print("Success:", sol.success)
print("Type A allocation:", x)
print("Type B allocation:", y)
print("Capacity:", 100*x + 170*y)
print("Minimum planning cost:", sol.fun)

best = None
for a in range(20):
    for b in range(20):
        cap = 100*a + 170*b
        if cap >= 1000:
            total = 12*a + 18*b
            if best is None or total < best[0]:
                best = (total, a, b, cap)
print("Best whole-number solution:", best)

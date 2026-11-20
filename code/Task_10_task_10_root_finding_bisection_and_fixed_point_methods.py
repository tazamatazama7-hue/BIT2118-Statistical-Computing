"""Source code for Task 10 – Root Finding: Bisection and Fixed-Point Methods."""

import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def heat_balance(T):
    return T - 25 - 10*np.exp(-T/20)

root = root_scalar(heat_balance, bracket=[20,40],
                   method="bisect", xtol=1e-10)

def g(T):
    return 25 + 10*np.exp(-T/20)

T = 30.0
history = [T]
for _ in range(100):
    new = g(T)
    history.append(new)
    if abs(new-T) < 1e-10:
        break
    T = new

print("Bisection root:", root.root)
print("Fixed-point result:", history[-1])
print("Iterations:", len(history)-1)

temps = np.linspace(20,40,300)
plt.plot(temps, heat_balance(temps))
plt.axhline(0); plt.axvline(root.root, linestyle="--")
plt.xlabel("Temperature (C)"); plt.ylabel("Heat-balance function")
plt.title("Equilibrium temperature"); plt.grid(True); plt.show()

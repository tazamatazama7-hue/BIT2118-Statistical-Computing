"""Source code for Task 20 – Random Numbers and Monte Carlo Methods."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

demand = rng.normal(mean_demand, std_demand, N)
overloaded = demand > capacity
probability = overloaded.mean()

print("Estimated overload probability:", probability)
print("Overload cases:", overloaded.sum(), "out of", N)

running = np.cumsum(overloaded) / np.arange(1, N+1)
indices = np.unique(np.logspace(1, np.log10(N), 200).astype(int))-1
plt.semilogx(indices+1, running[indices])
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk")
plt.grid(True); plt.show()

"""Source code for Task 2 – NumPy Arrays and Numerical Computation."""

import numpy as np

temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

print("Mean:", np.mean(temperatures_c))
print("Minimum:", np.min(temperatures_c))
print("Maximum:", np.max(temperatures_c))
temperatures_f = 1.8 * temperatures_c + 32
print("First six Fahrenheit readings:", temperatures_f[:6])

"""Source code for Task 4 – Floating-Point Arithmetic and Numerical Errors."""

import numpy as np

calculated = 0.1 + 0.2
expected = 0.3
print("Calculated:", calculated)
print("Exact comparison:", calculated == expected)
print("Close comparison:", np.isclose(calculated, expected))

true_value = np.sqrt(2)
approx_value = 1.414
absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)
print("Absolute error:", absolute_error)
print("Relative error:", relative_error)

for x in [1e-4, 1e-8, 1e-12]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(x, direct, stable)

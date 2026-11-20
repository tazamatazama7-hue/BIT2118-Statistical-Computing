"""Source code for Task 13 – Interpolation."""

import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([8,9,10,11,12,13,14], dtype=float)
temperature = np.array([18.,20.,22.5,24.,25.,25.5,25.])
linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

times = np.arange(8, 14 + 1/6, 1/6)
print("Linear at 10:30:", float(linear(10.5)))
print("Cubic at 10:30:", float(cubic(10.5)))

plt.scatter(hours, temperature, label="Measurements")
plt.plot(times, linear(times), label="Linear")
plt.plot(times, cubic(times), label="Cubic spline")
plt.xlabel("Hour"); plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation")
plt.legend(); plt.grid(True); plt.show()

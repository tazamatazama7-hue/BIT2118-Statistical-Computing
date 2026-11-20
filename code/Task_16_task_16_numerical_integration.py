"""Source code for Task 16 – Numerical Integration."""

import numpy as np
from scipy.integrate import simpson

time_hours = np.array([0,2,4,6,8,10,12], dtype=float)
power_kw = np.array([0.8,1.0,1.4,1.8,1.6,1.2,0.9])

trap = np.trapezoid(power_kw, time_hours)
simp = simpson(power_kw, x=time_hours)

print("Trapezoidal energy:", trap, "kWh")
print("Simpson energy:", simp, "kWh")
print("Difference:", abs(simp-trap), "kWh")

"""Source code for Task 17 – Ordinary Differential Equations: Euler Method."""

import numpy as np
import matplotlib.pyplot as plt

ambient = 25.0
initial = 90.0
k = 0.08
h = 1.0
time = np.arange(0, 30+h, h)
temperature = np.zeros(len(time))
temperature[0] = initial

for i in range(len(time)-1):
    rate = -k*(temperature[i]-ambient)
    temperature[i+1] = temperature[i] + h*rate

exact = ambient + (initial-ambient)*np.exp(-k*time)
print("Euler temperature after 30 min:", temperature[-1])
print("Exact temperature after 30 min:", exact[-1])
print("Final absolute error:", abs(temperature[-1]-exact[-1]))

plt.plot(time, temperature, label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.xlabel("Time (minutes)"); plt.ylabel("Temperature (C)")
plt.title("Cooling of a hot object")
plt.legend(); plt.grid(True); plt.show()

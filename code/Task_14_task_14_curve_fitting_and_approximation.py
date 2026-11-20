"""Source code for Task 14 – Curve Fitting and Approximation."""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

users = np.array([50,100,150,200,250,300,350], dtype=float)
response = np.array([82,95,115,145,185,238,305], dtype=float)

def model(x, a, b, c):
    return a*x**2 + b*x + c

params, covariance = curve_fit(model, users, response)
a, b, c = params
predicted = model(users, *params)
rmse = np.sqrt(np.mean((response-predicted)**2))

print("Fitted parameters:", params)
print("RMSE:", rmse)
print("Predicted at 400 users:", model(400, *params))

xplot = np.linspace(users.min(), 400, 300)
plt.scatter(users, response, label="Measurements")
plt.plot(xplot, model(xplot, *params), label="Fitted curve")
plt.xlabel("Concurrent users"); plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting")
plt.legend(); plt.grid(True); plt.show()

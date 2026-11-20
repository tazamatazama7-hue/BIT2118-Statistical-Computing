"""Source code for Task 11 – Root Finding: Newton-Raphson and Secant Methods."""

from scipy.optimize import root_scalar

cash_flows = [-10000, 3000, 3500, 4000, 2500]

def npv(rate):
    return sum(cf/(1+rate)**t for t, cf in enumerate(cash_flows))

def d_npv(rate):
    return sum(-t*cf/(1+rate)**(t+1)
               for t, cf in enumerate(cash_flows) if t > 0)

newton = root_scalar(npv, fprime=d_npv, x0=0.10,
                     method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.05, x1=0.20,
                     method="secant", xtol=1e-12)

print("Newton IRR:", newton.root)
print("Secant IRR:", secant.root)
print("NPV at Newton solution:", npv(newton.root))

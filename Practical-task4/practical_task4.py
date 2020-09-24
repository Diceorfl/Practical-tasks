import numpy as np
from scipy.optimize import minimize, curve_fit, leastsq, dual_annealing, differential_evolution, least_squares
from matplotlib import pyplot as plt

f = lambda x: 1 / (x * x - 3 * x + 2)
Function = lambda x, a, b, c=1, d=1: (a * x + b) / (x * x + c * x + d)

def generate_data(k=10 ** 3):
    X = [3 * _ / k for _ in range(k)]
    s = list(np.random.normal(size=k))
    Y = []
    for i in range(k):
        f_val = f(X[i])
        if f_val < -100:
            Y.append(-100 + s[i])
        elif f_val > 100:
            Y.append(100 + s[i])
        else:
            Y.append(f_val + s[i])
    return X, Y

X, Y = generate_data()

def loss(params):
    summary = 0
    for x_i, y_i in zip(X, Y):
        summary += (Function(x_i, *params) - y_i) ** 2
    return summary

def fitfunc(p):
    return loss(p)

def errfunc(p, y):
    return y - fitfunc(p)

popt, pcov = curve_fit(Function, X, Y, maxfev=1000)

print("Nelder-Mead:")
nm = minimize(loss, popt, method='nelder-mead', options={'disp': True})
print("\tMSE: ", loss(nm.x),"\n")
print('Levenberg Marquardt:')
lm = leastsq(errfunc, popt, args=(Y), full_output=True, maxfev=1000)
print("\tIterations: ",lm[2]["nfev"],"\n","\tMSE: ",loss(lm[0]),"\n")
bounds = [(-2,2), (-2, 2), (-2, 2), (-2, 2)]
print('Differential Evolution:')
de = differential_evolution(loss,bounds, tol=0.001, maxiter=1000)
print("\tIterations: ",de["nit"],"\n","\tMSE: ",loss(de.x),"\n")
print('Simulated annealing:')
da = dual_annealing(loss, bounds,maxiter=1000)
print("\tIterations: ",da["nit"],"\n","\tMSE: ",loss(da.x),"\n")

plt.plot(X, Y)
plt.grid()
plt.plot(X, [Function(x, *nm.x) for x in X],"-",color="red", label='Nelder-Mead')
plt.plot(X, [Function(x, *lm[0]) for x in X],"-",color="green", label='Levenberg Marquardt')
plt.plot(X, [Function(x, *de.x) for x in X], "-",color="blue",label='Differential Evolution')
plt.plot(X, [Function(x, *da.x) for x in X], "-",color="yellow",label='Simulated annealing')
plt.legend()
plt.show()

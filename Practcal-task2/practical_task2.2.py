import random
import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model
from lmfit import Parameters

alpha = random.random()
betha = random.random()
x = [i/100 for i in range(101)]
y = [alpha*x_i + betha + np.random.normal(loc=0.0, scale=1.0) for x_i in x]

#functions for approximation
def linear(x,a,b):
    return a*x+b

def rational(x,a,b):
    return a/(1+b*x)

#loss function
def mse(a,b,y,func):
    x = np.arange(0,1.01,0.01)
    return np.sum((func(x,a,b)-y)**2)

def bruteForce(func, loss_f, y):
    minimum = float('inf')
    best = (1,1)
    a = np.arange(0,1,0.01)
    b = np.arange(0,1,0.01)
    for i in a:
        for j in b:
            value = loss_f(i,j,y,func)
            if value < minimum:
                minimum = value
                best = (i,j)
    return best

linearModel = Model(linear)
lpar = Parameters()
lpar.add('a', value=0, min=-1, max=1,brute_step=0.001)
lpar.add('b', value=0, min=-1, max=1, brute_step=0.001)
lbruteF = linearModel.fit(y, lpar, x=x, method="brute")
lgauss = linearModel.fit(y, lpar, x=x, method="cg")
lnelder = linearModel.fit(y, lpar, x=x, method="nelder")
plt.plot(x, y)
plt.title("Linear function")
plt.grid()
plt.plot(x, lbruteF.best_fit, 'r-',color='red', label='Brute Forse')
plt.plot(x, lgauss.best_fit, '+', color='blue', label='Gauss')
plt.plot(x, lnelder.best_fit, 'x', color='green', label='Nelder-Mead')
print(lbruteF.fit_report(),"\n")
print(lgauss.fit_report(),"\n")
print(lnelder.fit_report(),"\n")
plt.legend()
plt.show()

rationalModel = Model(rational)
rpar = Parameters()
rpar.add('a', value=0, min=-1, max=1,brute_step=0.001)
rpar.add('b', value=0, min=-0.9, max=1, brute_step=0.001)
rbruteF = rationalModel.fit(y, rpar, x=x, method="brute")
rgauss = rationalModel.fit(y, rpar, x=x, method="cg")
rnelder = rationalModel.fit(y, rpar, x=x, method="nelder")
plt.plot(x, y)
plt.title("Rational function")
plt.grid()
plt.plot(x, rbruteF.best_fit, 'r-',color='red', label='Brute Forse')
plt.plot(x, rgauss.best_fit, '+', color='blue', label='Gauss')
plt.plot(x, rnelder.best_fit, 'x', color='green', label='Nelder-Mead')
print(rbruteF.fit_report(),"\n")
print(rgauss.fit_report(),"\n")
print(rnelder.fit_report(),"\n")
plt.legend()
plt.show()

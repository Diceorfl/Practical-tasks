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

linearModel = Model(linear)
lpar = Parameters()
lpar.add('a', value=0, min=-1, max=1,brute_step=0.001)
lpar.add('b', value=0, min=-1, max=1, brute_step=0.001)
lbruteF = linearModel.fit(y, lpar, x=x, method="brute")
lgauss = linearModel.fit(y, lpar, x=x, method="gd")
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
rgauss = rationalModel.fit(y, rpar, x=x, method="gd")
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

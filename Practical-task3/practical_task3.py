import numpy as np
from scipy import optimize, special
from sklearn.linear_model import SGDClassifier
from sklearn import preprocessing
from autograd import grad, jacobian, hessian
from lmfit import minimize, Parameters, Parameter, report_fit
from scipy.integrate import ode
import random
from lmfit import Model
from scipy.optimize import minimize, least_squares, curve_fit, newton
from matplotlib import pyplot as plt

linear_c = 0
eps = 0.001

linear = lambda x, a, b: a * x + b
rational = lambda x, a, b: a / (1 + b * x)

def lloss(x0, X, Y):
    summary = 0
    for x_i, y_i in zip(X, Y):
        summary += (linear(x_i, x0[0], x0[1]) - y_i) ** 2
    return summary

def rloss(x0, X, Y):
    summary = 0
    for x_i, y_i in zip(X, Y):
        summary += (rational(x_i, x0[0], x0[1]) - y_i) ** 2
    return summary

def gradient_descent(loss,X, Y):
    return optimize.minimize(loss, [0, 0], args=(X, Y), tol=eps, method='BFGS', options={'disp': True})

def conjugate_gradient_descent(loss,x0, X, Y):
    return optimize.fmin_cg(loss, (0, 0), args=(X, Y), disp=True)

def Levenberg_Marquardt(func,x0, X, Y):
    model = Model(func)
    param = Parameters()
    param.add('a', value=float(x0[0]), min=-100, max=100)
    param.add('b', value=float(x0[1]), min=-100, max=100)
    lm = model.fit(Y, param, x=X, method="leastsq")
    print(lm.fit_report())
    return lm

def newtons_method(loss,x0, X, Y, eps=0.001):
    return optimize.minimize(loss, x0, args=(X, Y), tol=eps, method='Newton-CG',
                             jac=jacobian(loss), options={'disp': True})

def Plot(func,loss,X,Y,name):
    popt, pcov = curve_fit(func, X, Y)
    print("\t\t\t\t" + name)
    print('Gradient descent:')
    gd_res = gradient_descent(loss,X,Y)
    print('Conjugate gradient descent:')
    cgd_res = conjugate_gradient_descent(loss,popt, X, Y)
    print('Newton:')
    newton_res = newtons_method(loss,popt, X, Y)
    print('Levenberg_Marquardt:')
    res_lm = Levenberg_Marquardt(func,popt,X,Y)
    plt.plot(X, Y)
    plt.title(name)
    plt.grid()
    plt.plot(X, [func(x, *gd_res.x) for x in X], "-", color="green",label='Gradient descent')
    plt.plot(X, [func(x, *cgd_res) for x in X], "o", color="yellow",label='Conjugate gradient descent')
    plt.plot(X, [func(x, *newton_res.x) for x in X],"x", color="blue", label = 'Newton')
    plt.plot(X, res_lm.best_fit, "+", color="black" , label = 'Levenberg-Marquardt')
    plt.legend()
    plt.show()


alpha = random.random()
betha = random.random()
X = [i/100 for i in range(101)]
Y = [alpha*x + betha + np.random.normal(loc=0.0, scale=1.0) for x in X]
Plot(linear,lloss,X,Y,"Linear function")
Plot(rational,rloss,X,Y,"Rational function")

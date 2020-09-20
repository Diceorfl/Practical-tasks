import random
import numpy as np
import matplotlib.pyplot as plt

#decorator for count function calls
def CallCounter(f):
    def helper(*args, **kwargs):
        helper.calls +=1
        return f(*args,**kwargs)
    helper.calls = 0
    helper.__name__= f.__name__
    return helper

@CallCounter
def FirstFunction(x):
    return x**3

@CallCounter
def SecondFunction(x):
    return abs(x - 0.2)

@CallCounter
def ThirdFunction(x):
    return x*np.sin(1/x)

def ExhaustiveSearch(f,a,b):
    f.calls = 0
    eps = 0.001
    n = int((b-a)/eps)
    Function = []
    x = []
    for k in range(0,n+1):
        x.append(a + k*eps)
        Function.append(f(x[k]))
    Fmin = min(Function)
    xmin = x[Function.index(Fmin)]
    print("Function calls: ", f.calls)
    print("Minimum at: ",xmin)
    print("Iterations: ",n+1)
    return xmin, Fmin

def Dichotomy(f,a,b):
    f.calls = 0
    eps = 0.001
    delta=eps/2
    iter = 0
    while (b-a) > eps:
        iter+= 1
        x1=(a+b-delta)/2
        x2=(a+b+delta)/2
        if f(x1) <= f(x2):
            a = a
            b = x2
        else:
            a = x1
            b=b
    print("Function calls: ", f.calls)
    print("Minimum at: ", b)
    print("Iterations: ", iter)
    return b, f(b)

def GoldenSection(f,a,b):
    f.calls = 0
    eps = 0.001
    x1 = a + (3 - np.sqrt(5))*(b-a)/2
    x2 = b + (-3 + np.sqrt(5))*(b-a)/2
    FA = f(x1)
    FB = f(x2)
    iter = 0
    while abs(a - b) >= eps:
        iter+= 1
        if FA <= FB:
            b = x2
            x2 = x1
            x1 = a + (3 - np.sqrt(5))*(b-a)/2
            FB = FA
            FA = f(x1)
        else:
            a = x1
            x1 = x2
            x2 = b + (-3 + np.sqrt(5))*(b-a)/2
            FA = FB
            FB = f(x2)
    print("Function calls: ", f.calls)
    print("Minimum at: ", b)
    print("Iterations: ", iter)
    return b, f(b)

plt.plot(np.arange(0,1,0.001), FirstFunction(np.arange(0,1,0.001)), color='green',label="x^3")
plt.plot(np.arange(0,1,0.001), SecondFunction(np.arange(0,1,0.001)), color='red', label="|x-0.2|")
plt.plot(np.arange(0.01,1,0.001), ThirdFunction(np.arange(0.01,1,0.001)),color='blue', label="x*sin(1/x)")

print("Exhaustive search for 'x^3'")
plt.plot(*ExhaustiveSearch(FirstFunction,0,1), 'x',  color='green')
print("Exhaustive search for '|x-0.2|'")
plt.plot(*ExhaustiveSearch(SecondFunction,0,1), 'x', color='green')
print("Exhaustive search for 'x*sin(1/x)'")
plt.plot(*ExhaustiveSearch(ThirdFunction,0.01,1), 'x', color='green')
print("\n")
print("Dichotomy search for 'x^3'")
plt.plot(*Dichotomy(FirstFunction,0,1), 'ro', color='red')
print("Dichotomy search for '|x-0.2|'")
plt.plot(*Dichotomy(SecondFunction,0,1), 'ro', color='red')
print("Dichotomy search for 'x*sin(1/x)'")
plt.plot(*Dichotomy(ThirdFunction,0.01,1), 'ro', color='red')
print("\n")
print("Golden section search for 'x^3'")
plt.plot(*GoldenSection(FirstFunction,0,1), '+', color='blue')
print("Golden section search for '|x-0.2|'")
plt.plot(*GoldenSection(SecondFunction,0,1), '+', color='blue')
print("Golden section search for 'x*sin(1/x)'")
plt.plot(*GoldenSection(ThirdFunction,0.01,1), '+', color='blue')

plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()
plt.show()

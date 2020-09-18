import time
import random
import matplotlib.pyplot as plt
import numpy as np
import decimal #the decimal library allows arbitrary precision

def ConstantFunction(listOfRandomNums):
    Func = 1

def TheSumOfElements(listOfRandomNums):
    sum = 0
    for num in listOfRandomNums:
        sum += num

def TheProductOfElements(listOfRandomNums):
    product = 1
    for num in listOfRandomNums:
        product *= num

def DirectCalculationOf_P_(listOfRandomNums):
    P = decimal.Decimal(0)
    for i in range(0,len(listOfRandomNums)):
        P += (decimal.Decimal(1.5)**decimal.Decimal(i))*decimal.Decimal(listOfRandomNums[i])

def HornerMethod(listOfRandomNums):
    P = listOfRandomNums[-1]
    for i in range(len(listOfRandomNums)-1,0,-1):
        P *= 1.5
        P += listOfRandomNums[i-1]

def BubbleSort(listOfRandomNums):
    n = len(listOfRandomNums)
    # Traverse through all array elements
    for i in range(n):
      # Last i elements are already in place
      for j in range(0, n-i-1):
        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if listOfRandomNums[j] > listOfRandomNums[j+1] :
          listOfRandomNums[j], listOfRandomNums[j+1] = listOfRandomNums[j+1], listOfRandomNums[j]

#QuickSort is a Divide and Conquer algorithm.
#It picks an element as pivot and partitions the given array around the picked pivot.
def QuickSort(listOfRandomNums, fst, lst):
   if fst >= lst: return
   i, j = fst, lst
   pivot = listOfRandomNums[random.randint(fst, lst)]
   while i <= j:
       while listOfRandomNums[i] < pivot: i += 1
       while listOfRandomNums[j] > pivot: j -= 1
       if i <= j:
           listOfRandomNums[i], listOfRandomNums[j] = listOfRandomNums[j], listOfRandomNums[i]
           i, j = i + 1, j - 1
   # Separately sort elements before
   # partition and after partition
   QuickSort(listOfRandomNums, fst, j)
   QuickSort(listOfRandomNums, i, lst)

def TimSort(listOfRandomNums):
    listOfRandomNums.sort()

def UsualMatrixProduct(A,B):
    n = len(A)
    C = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]

#The functions calculates the average time based on five tests
def AverageTime(Function,n):
    Time = []
    for k in range(5):
      listOfRandomNums = random.sample(range(10000), n)
      start = time.time()
      Function(listOfRandomNums)
      Time.append(time.time() - start)
    return sum(Time)/5

def AverageTime1(Function,fst,n):
    Time = []
    for k in range(5):
        listOfRandomNums = random.sample(range(10000), n)
        start = time.time()
        Function(listOfRandomNums,fst,n-1)
        Time.append(time.time() - start)
    return sum(Time)/5

def AverageTime2(Function,n):
    Time = []
    for k in range(5):
      A = [random.sample(range(10000), n) for i in range(n)]
      B = [random.sample(range(10000), n) for i in range(n)]
      start = time.time()
      Function(A,B)
      Time.append(time.time() - start)
    return sum(Time)/5

#Keep average time all 2000 n
TimeOfConstantFunction = []
TimeOfSumOfElements = []
TimeOfProductOfElements = []
TimeOfDirectCalculation = []
TimeOfHornerMethod = []
TimeOfBubbleSort = []
TimeOfQuickSort = []
TimeOfTimSort = []
TimeOfUsualMatrixProduct = []
for n in range(1,2001):
    TimeOfConstantFunction.append(AverageTime(ConstantFunction,n))
    TimeOfSumOfElements.append(AverageTime(TheSumOfElements,n))
    TimeOfProductOfElements.append(AverageTime(TheProductOfElements,n))
    TimeOfDirectCalculation.append(AverageTime(DirectCalculationOf_P_,n))
    TimeOfHornerMethod.append(AverageTime(HornerMethod,n))
    TimeOfBubbleSort.append(AverageTime(BubbleSort,n))
    TimeOfQuickSort.append(AverageTime1(QuickSort,0,n))
    TimeOfTimSort.append(AverageTime(TimSort,n))
    TimeOfUsualMatrixProduct.append(AverageTime2(UsualMatrixProduct,n))

#Plots the data obtained showing the average execution time as a function of n.
#Remove comments from the desired part.

plt.title("Constant Function")
plt.ylabel("Running Time")
plt.xlabel("Size of input(n)")
plt.grid()
plt.plot(TimeOfConstantFunction,".",label = "Emprical graph")
coefficients = np.polyfit(range(1,2001),TimeOfConstantFunction,1)
p = np.poly1d( coefficients )
x = np.linspace(0,2000,2000)
plt.plot(x,p(x),label = "Theoretical estimation")
plt.legend()
plt.show()

'''plt.title("The Sum of Elements")
plt.ylabel("Running Time")
plt.xlabel("Size of input(n)")
plt.grid()
plt.plot(TimeOfSumOfElements,".",label = "Emprical graph")
coefficients = np.polyfit(range(1,2001),TimeOfSumOfElements,1)
p = np.poly1d( coefficients )
x = np.linspace(0,2000,2000)
plt.plot(x,p(x),label = "Theoretical estimation")
plt.legend()
plt.show()'''

'''plt.title("The Product of Elements")
plt.ylabel("Running Time")
plt.xlabel("Size of input(n)")
plt.grid()
plt.plot(TimeOfProductOfElements,".",label = "Emprical graph")
coefficients = np.polyfit(range(1,2001),TimeOfProductOfElements,1)
p = np.poly1d( coefficients )
x = np.linspace(0,2000,2000)
plt.plot(x,p(x),label = "Theoretical estimation")
plt.legend()
plt.show()'''

'''plt.title("Direct calculation of P(x)")
plt.ylabel("Running Time")
plt.xlabel("Size of input(n)")
plt.grid()
plt.plot(TimeOfDirectCalculation,".",label = "Emprical graph")
coefficients = np.polyfit(range(1,2001),TimeOfDirectCalculation,1)
p = np.poly1d( coefficients )
x = np.linspace(0,2000,2000)
plt.plot(x,p(x),label = "Theoretical estimation")
plt.legend()
plt.show()'''

'''plt.title("Horner's Method")
plt.ylabel("Running Time")
plt.xlabel("Size of input(n)")
plt.grid()
plt.plot(TimeOfHornerMethod,".",label = "Emprical graph")
coefficients = np.polyfit(range(1,2001),TimeOfHornerMethod,1)
p = np.poly1d( coefficients )
x = np.linspace(0,2000,2000)
plt.plot(x,p(x),label = "Theoretical estimation")
plt.legend()
plt.show()'''

'''plt.title("Bubble Sort")
plt.ylabel("Running Time")
plt.xlabel("Size of input(n)")
plt.grid()
plt.plot(TimeOfBubbleSort,".",label = "Emprical graph")
xf = np.array([i for i in range(1,2001)])
m = np.vstack([xf**2,xf,np.ones(2000)]).T
s = np.linalg.lstsq(m,TimeOfBubbleSort)[0]
x = np.linspace(0,2000,2000)
plt.plot(x,s[0]*x**2+s[1]*x+s[2],label = "Theoretical estimation")
plt.legend()
plt.show()'''

'''plt.title("Quick Sort")
plt.ylabel("Running Time")
plt.xlabel("Size of input(n)")
plt.grid()
plt.plot(TimeOfQuickSort,".",label = "Emprical graph")
xf = np.array([i for i in range(1,2001)])
m = np.vstack([xf**2,xf,np.ones(2000)]).T
s = np.linalg.lstsq(m,TimeOfQuickSort,rcond=None)[0]
x = np.linspace(0,2000,2000)
plt.plot(x,s[0]*x**2+s[1]*x+s[2],label = "Theoretical estimation")
plt.legend()
plt.show()'''

'''plt.title("TimSort")
plt.ylabel("Running Time")
plt.xlabel("Size of input(n)")
plt.grid()
plt.plot(TimeOfTimSort,".",label = "Emprical graph")
xf = np.array([i for i in range(1,2001)])
m = np.vstack([xf**2,xf,np.ones(2000)]).T
s = np.linalg.lstsq(m,TimeOfTimSort,rcond=None)[0]
x = np.linspace(0,2000,2000)
plt.plot(x,s[0]*x**2+s[1]*x+s[2],label = "Theoretical estimation")
plt.legend()
plt.show()'''

'''plt.title("Usual Matrix Product")
plt.ylabel("Running Time")
plt.xlabel("Size of input(n)")
plt.grid()
plt.plot(TimeOfUsualMatrixProduct,".",label = "Emprical graph")
xf = np.array([i for i in range(1,201)])
m = np.vstack([xf**3,xf**2,xf,np.ones(n)]).T
s = np.linalg.lstsq(m,TimeOfUsualMatrixProduct,rcond=None)[0]
x = np.linspace(0,200,200)
plt.plot(x,s[0]*x**3+s[1]*x**2+s[2]*x+s[3],label = "Theoretical estimation")
plt.legend()
plt.show()'''

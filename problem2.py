#!/usr/bin/python
#analyze newton's method versus secant method
import sys
from math import exp
from math import fabs
from math import log10
import numpy as np
import matplotlib.pyplot as plt

def secant(k):
    a = np.zeros(k+1)
    a[0] = 5
    a[1] = 4.8
    for i in range (2,k+1):
        temp1 = float(a[i-1])
        temp2 = float(a[i-2])
        a[i] = float(temp1 - (f(temp1))*(temp1-temp2)/(f(temp1)-f(temp2)))
        print(a[i])
        if fabs(f(a[i]))<=0.00000001:
            return a[i]
    return a[k]

def newton(k):
    a = np.zeros(k+1)
    a[0] = 5
    for i in range (1,k+1):
        temp1 = float(a[i-1])
        a[i] = float(temp1 - f(temp1)/f_prime(temp1))
        print(a[i])
        if fabs(f(a[i]))<=0.00000001:
            return a[i]
    return a[k]

def f(x):
    return float((5-x)*(exp(x))-5)

def f_prime(x):
    return float((5-x)*(exp(x))-exp(x))

def p2a():
    x = []
    y = []
    for i in np.arange (0, 5.0001, 0.0001):
        x.append(i)
        y.append((5-i)*(exp(i))-5)
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()  

def p2b():
    print "secant: "
    sec_2b = secant(50)                            
    print (sec_2b)

def p2c():
    print "newton: "
    newton_2c = newton(50)                         
    print(newton_2c)

def p2d():
    x = []
    y_sec = []
    y_newton = []
    for k in range (1,10):
        x.append(k)
        y_sec.append(log10(secant(k)))
        y_newton.append(log10(newton(k)))
    plt.plot(x, y_sec, label="secant")
    plt.plot(x, y_newton, label="newton")
    plt.legend(loc='lower right')
    plt.xlabel('k')
    plt.ylabel('log(xk)')
    plt.show()

def main():

    p2a()
    p2b()
    print
    p2c()
    p2d()

if __name__ == '__main__':
	 main()

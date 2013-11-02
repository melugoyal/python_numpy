#!/usr/bin/python
#use newton's method to generate newton fractals for given polynomials
import sys
from math import exp
from math import fabs
from math import log10
import numpy as np
import matplotlib.pyplot as plt

def newton(k, initial, my_plot, roots, n):
    a = np.zeros((k+1), dtype=complex)
    a[0] = initial
    real1 = initial.real
    imag1 = initial.imag
    for i in range (1,k+1):
        temp1 = a[i-1]
        a[i] = temp1 - f(temp1, n)/f_prime(temp1, n)
        for c in range (0, len(roots)):
            if (abs(roots[c] - a[i]) < 0.001):
                my_plot[(imag1+1)*256][(real1+1)*256][0] = c==0 or c==3
                my_plot[(imag1+1)*256][(real1+1)*256][1] = c==1 
                my_plot[(imag1+1)*256][(real1+1)*256][2] = c/2
                return
def f(z, n):
    if (n==0):
        return z**3-2*z+2
    elif (n==1):
        return z**3-1
    else:
        return z**4-1

def f_prime(z, n):
    if (n==0):
        return 3*z*z-2
    elif (n==1):
        return 3*z*z
    else:
        return 4*(z**3)

def fractals(n):
    my_plot = np.zeros((512, 512, 3), dtype=float)
    if (n==0):
        roots = np.array([0.884646177119316-0.589742805022206j, 0.884646177119316+0.589742805022206j, -1.76929235423863], dtype = complex)       
    elif (n==1):
        roots = np.array([-0.5-0.866025403784439j, -0.5+0.866025403784439j, 1], dtype = complex)
    else:
        roots = np.array([1, -1, 0-1j, 0+1j], dtype = complex)
    for i in np.arange(-1, 1, 0.00390625):
        for k in np.arange(-1, 1, 0.00390625):
            newton(100, complex(i,k), my_plot, roots, n)
    plt.imshow(my_plot)
    plt.savefig(str(n)+ '.png')

def main():
    
    fractals(0)
    fractals(1)
    fractals(2)

if __name__ == '__main__':
	 main()

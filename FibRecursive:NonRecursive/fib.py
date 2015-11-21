__author__ = 'Aly'

""" This part of the lab familiarizes with
"""

import time
import numpy
import math

def main():
    """ Your docstring. """

    n = int(input("Enter n: "))
    print()

    t0 = time.time()
    f1 = fib1(n)
    print("fib1(%d) = %d" % (n, f1))
    t1 = time.time()
    print("fib1 elapsed time is %5.3f." % (t1-t0))

    print()

    t0 = time.time()
    f2 = fib2(n)
    print("fib2(%d) = %d" % (n, f2))
    t1 = time.time()
    print("fib2 elapsed time is %5.3f." % (t1-t0))

    print()

    if f1 != f2:
            print("Test failed!")

    print()

    printFibHistogram(10)

def fib1(n):
    """ Your docstring -- this is the non-recursive version.
    """
    #phi = float(1+(math.sqrt(5))/2)
    #negPhi=float(1-(math.sqrt(5))/2)
    #fibSeq=phi^n

    #return fibSeq
    assert n>= 0, "Fibonacci not defined for n<0"    
    term1 = 0
    term2 = 1
    for i in range(0, n):
        temp = term1
        term1 = term2
        term2 = temp + term2
    return term1



def fib2(n):
    """ Your docstring here -- this is the recursive version
    """
    assert n>= 0, "Fibonacci not defined for n<0"
    if n<=1:
        return n
    else:
        return fib2(n-1) + fib2(n-2)

def printFibHistogram(n):
    """ docstring here """

    for i in range(n):
            print('*' * fib1(i+1))

    print("\nCheck the above and below histogram to see if they are identical")
    print("Otherwise, something is wrong!\n")

    for i in range(n):
            print('*' * fib2(i+1))

main()

a = numpy.arange(6).reshape(2,3)
for x in numpy.nditer(a):
    print (x)
    
    
    
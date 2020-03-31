# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as pl
import numpy.random
import collections

def beta(a, b):
    n = 100
    l=[]
    while n>0:
        l.append(numpy.random.beta(a,b))
        n=n-1
    ct = collections.Counter(l)
    l = list(ct.values())
    pl.plot(l,'ro')
    pl.show()
    
def binomial(n, p): 
    m = 100
    l=[]
    while m>0:
        l.append(numpy.random.binomial(n,p))
        m=m-1
    ct = collections.Counter(l)
    l = list(ct.values())
    pl.plot(l,'ro')
    pl.show()

def console():
    while True:
        menu = "Random number generator\n1.Beta distribution\n2.Binomial distribution\n"
        print(menu)
        choice = int(input())
        if choice == 1:
            print("Input a:")
            a = int(input())
            print("\nInput b:")
            b = int(input())
            beta(a, b)
        elif choice == 2:
            print("Input n:")
            n = int(input())
            print("\nInput p(0<=p<=1):")
            p=float(input())
            binomial(n, p)
        elif choice == 0:
            break
    
console()
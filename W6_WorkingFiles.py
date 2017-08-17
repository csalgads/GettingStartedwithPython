# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 11:09:25 2017

@author: Cesar
"""

def computepay(h,r):
    if h>40:
        pay = 40*r+(h-40)*r*1.5
    else:
        pay = h*r
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print("Pay",p)
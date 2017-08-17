# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 12:02:09 2017

@author: Cesar
"""
x = -5
if x > 1:
    print(x)

x = 5 
print('Before 5')
if x ==5:
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x ==6:
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('Afterwards 6')
    

# Assigment
## 3.1
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h>40 :
    pay = 40*r+(h-40)*r*1.5
else :
    pay = h*r
print(pay)
## 3.2
hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
    
except:
    print('Error, please enter numeric input')
    quit()

if h>40:
    pay = 40*r+(h-40)*r*1.5
else:
    pay = h*r
print("Pay:",pay)
## 3.3

score = input("Enter Score: ")
try:
    sco = float(score)
except:
    print('Error, please enter numeric input')
    quit()

if sco > 1:
    print("The score is out of range")
elif sco >= 0.9:
    print("A")
elif sco >= 0.8:
    print("B")
elif sco >= 0.7:
    print("C")
elif sco >= 0.6:
    print("D")
elif sco < 0:
    print("The score is out of range")
elif sco < 0.6:
    print("F")
    
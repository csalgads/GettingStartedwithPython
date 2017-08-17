# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:20:05 2017

@author: Cesar
"""

n = 5
while n>0:
    print(n)
    n = n - 1
print('Blastoff')
print(n)


print('Before')
for thing in [9,41,12,3,74,15]:
    print(thing)
print('After')
    
## Largest in an array
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far,the_num)
print('After',largest_so_far)

## Counting in a loop
zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork,thing)
print('After',zork)

## Summing in a loop
zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork,thing)
print('After',zork)

## Average in a loop
zork = 0
count = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    count = count + 1
    zork = zork + thing
    average = zork / count
    print(zork,thing, average)
print('After',zork,count,average)

## Filtering
filter = 20
print('Before', filter)
for the_num in [9,41,12,3,74,15]:
    if the_num > filter:
        print(the_num,filter)
print('After')

## Exercise 5
## 5.1
count = 0
total = 0
while True:
    rnum = input('Enter a number, done to finish :')
    if rnum == "done":
        break
    try:
        rnumb = float(rnum)
    except:
        print('Invalid input')
        continue
    
    count = count + 1
    total = total + rnumb
    average = total / count

print(total,count,average)
 ## 5.2
 
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        numb = int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = numb
    elif numb < smallest:
        smallest = numb
    if largest is None:
        largest = numb
    elif numb > largest:
        largest = numb        

print("Maximum is", largest)
print("Minimum is", smallest)











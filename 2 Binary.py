import numpy as np
from random import randint
''' Binary search'''
n=int(input('Input n:'))
a=np.zeros(n,dtype=int)
x=int(input('Find number:'))
for i in range(n):
    a[i]=randint(0,10)
a=sorted(a)
print(a)
L=0
R=len(a)-1
k=0
count=0
for i in range(n):
    k=(L+R)//2
    if a[k] == x:
        print(f' Your number {x} on {k} position')
        break
    elif a[k]<x:
        L=k+1
    elif a[k]>x:
        R=k-1
    if i==n-1:
        print('Your number not found')
    count+=1
print(f'{count} times')

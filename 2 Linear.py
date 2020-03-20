import numpy as np
from random import randint
'''Linear search'''
n=int(input('Input n:'))
a=np.zeros(n,dtype=int)
for i in range(n):
    a[i]=randint(0,10)
x=int(input('Find number:'))
print(a)
count=0
for i in range(n):
    if a[i]==x:
        print(f'Your number on {i} position')
        break
    elif i==n-1:
        print('Your number not found')
    count+=1
print(f'{count} times')

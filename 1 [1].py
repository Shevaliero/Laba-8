import numpy as np
'''виведіть на екран елементи лінійного масиву (заданий користувачем) у зворотньому порядку'''
n=int(input('Input n:'))
a=np.zeros(n,dtype=int)
b=np.zeros(n,dtype=int)
for i in range(n):
    a[i]=int(input(f'A[{i}]='))
j=-1
for i in range(n):
    b[i]=a[j]
    j-=1
print(b)
        

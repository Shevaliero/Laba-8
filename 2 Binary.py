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
L=0       #Самый низкий индекс последовательности
R=len(a)-1    #Самый высокий индекс последовательности
k=0     #Центральная позиция последовательности
count=0
for i in range(n):
    k=(L+R)//2     #Высчитывание центра позиции и последующее наближение к нужному значению
    if a[k] == x: 
        print(f' Your number {x} on {k} position')
        break
    elif a[k]<x:  #При этом условии программа будет искать в правой части последовательности
        L=k+1
    elif a[k]>x:  #При этом условии в левой
        R=k-1
    if i==n-1:
        print('Your number not found')
    count+=1      #Высчитывание количества сравнений.
print(f'{count} times')

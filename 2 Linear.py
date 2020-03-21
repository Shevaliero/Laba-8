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
for i in range(n):     #Цикл для перебора каждого елемента одного за другим
    count+=1      #Подсчет сравнений
    if a[i]==x:     #Сравнивание нынешнего елемента с нужным.
        print(f'Your number on {i} position')
        break      
    elif i==n-1:    #Если цикл дошел до конца, то нужного значения в последовательности нет.
        print('Your number not found')
    count+=1      #Подсчет сравнений
print(f'{count} comparisons')

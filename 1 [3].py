import numpy as np
from random import randint
while True:
    '''виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
    Результати множення елементів занесіть до нової матриці та виведіть її на екран;'''
    n,m=int(input('Input n for A:')), int(input('Input m for A:'))
    n1,m1=int(input('Input n for B:')), int(input('Input m for B:'))
    if n==n1 and m==m1:
        a=np.zeros((n,m),dtype=int)
        b=np.zeros((n1,m1),dtype=int)
        c=np.zeros((n,m),dtype=int)
        for i in range(n):
            for j in range(m):
                a[i][j],b[i][j]=randint(-20,20),randint(-20,20)
        print(f'A={a}\nB={b}')
        for i in range(n):
            for j in range(m):
                c[i][j]=a[i][j]*b[j][i]
        print (f'C={c}')
    else:
        print('Input same n and m for A and B!')
        continue
    
        

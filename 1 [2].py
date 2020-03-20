import numpy as np
'''виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана
користувачем).'''
n,m=int(input('Input n:')), int(input('Input m:'))
a=np.zeros((n,m),dtype=int)
b=np.zeros((n,m),dtype=int)
for i in range(n):
    for j in range(m):
        a[i,j]=int(input(f'A[{i},{j}]='))
print(a)
for i in range(n):
    for j in range(m):
        if i!=j:
            b[i][j]=a[j][i]
        else:
            b[i][j]=a[i][j]
print(f'T:\n{b}')

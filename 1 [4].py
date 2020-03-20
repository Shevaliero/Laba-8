import numpy as np
'Ініціалізувати матрицю Н-Н елементи матриці вв користувач, всі відемні елементи замінити на 0'
n,m=int(input('Input n:')), int(input('Input m:'))
a=np.zeros((n,m),dtype=int)
for i in range(n):
    for j in range(m):
        a[i,j]=int(input(f'A[{i},{j}]='))
for i in range(n):
    for j in range(m):
        if a[i,j]<0:
            a[i,j]=0
print(a)

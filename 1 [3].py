import numpy as np
from random import randint
while True:
    '''виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
    Результати множення елементів занесіть до нової матриці та виведіть її на екран;'''
    n,m=int(input('Input n for A:')), int(input('Input m for A:'))
    n1,m1=int(input('Input n for B:')), int(input('Input m for B:'))
    if n==m1 and m==n1:
        a=np.zeros((n,m),dtype=int)
        b=np.zeros((n1,m1),dtype=int)
        c=np.zeros((n,m1),dtype=int)
        for i in range(n):
            for j in range(m):
                a[i][j]=randint(0,10)
        for i in range(n1):
            for j in range(m1):
                b[i][j]=randint(0,10)
        print(f'A=\n{a}\nB=\n{b}')
        summ=0
        iA,jA,iB,jB,iC,jC=0,0,0,0,0,0   #i-n , j-m ,| n-ряд, m-столб
        for i in range(n+n1+m+m1):
                
                if jA==m and m1!=jB and n1==iB:     
                    jA,iA=0,0
                    iB=0
                    jB+=1

                if iB==n1 and jB==m1-1:
                    break
                
                if jC==m1:
                    jC=0
                    iC+=1

                for j in range(m):
                    if jA==m and m1-1==jB and n1==iB:
                        jA=0
                        iA+=1
                        iB,jB=0,0
                    c[iC][jC]=a[iA][jA]*b[iB][jB]+summ
                    summ+=c[iC][jC]

                print(f'C=\n{c}')
                summ=0
                if jC==m1-1 and iC==n-1:
                    break
                jA+=1
                iB+=1
                jC+=1
        print (f'C=\n{c}')
    else:
        print('Input n for A = m for B and m for A = n for B')
        continue
    end=input('Press 1 to rerun')
    if end =='1':
        continue
    else:
        break
    
        

'''String search'''
s=input('Write:')
p=input('Find:')
i=-1    #Переменная для индекса текста
j=0     #Переменная для индекса подстроки
count=0
while j<len(p) and i<(len(s)-len(p)): #Во втором условии проверка - больше ли подстрока чем оставшаясь часть текста
    j=0
    i+=1
    count+=2            #Подсчитывание количества сравнений
    while j<len(p) and p[j]==s[i+j]:    #цикл в котором идет сравнение каждого символа подстроки с текстом
        j+=1
        count+=2        #Подсчитывание количества сравнений
count+=1
if j==len(p):
    print(f'Pattenr founded on {i} position')
else:
    print('Pattern not found')
print(f'{count} comparisons')

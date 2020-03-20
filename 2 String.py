'''String search'''
s=input('Write:')
p=input('Find:')
i=-1
j=0
count=0
while j<len(p) and i<(len(s)-len(p)):
    j=0
    i+=1
    count+=1
    while j<len(p) and p[j]==s[i+j]:
        j+=1
        count+=1
if j==len(p):
    print(f'Pattenr founded on {i} position')
else:
    print('Pattern not found')
print(f'{count} times')

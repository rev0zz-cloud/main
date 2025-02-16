res = []
stroka = ''
i = 0
l = [a for a in input().split(' ')]
for i in range(len(l)):
    res.append(l[i][-1])

for i in res:
    stroka += str(i)
    
print(stroka) 
    

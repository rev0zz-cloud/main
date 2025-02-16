stroka = str(input())
nol = 0
odin = 0

for i in stroka:
    if i == '0':
        nol += 1
    if i == '1':
        odin +=1
if odin == nol:
    print("yes")
else:
    print("no")


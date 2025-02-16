l = [a for a in input().split(',')]
kolvo = 0

for i in l[0]:
    if i == l[1]:
        kolvo += 1
    else:
        break
print(kolvo)

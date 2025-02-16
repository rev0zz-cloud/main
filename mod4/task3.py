def evq(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return evq(b, a % b)

i = [a for a in input().split(' ')]
print(evq(int(i[0]),int(i[1])))

def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(a * a, n // 2)
    else:
        return a * pow(a, n - 1)

i = [a for a in input().split(' ')]
print(pow(int(i[0]),int(i[1])))

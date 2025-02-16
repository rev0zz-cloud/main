def chisla(a):
    if len(set(a)) == len(a):
        return "Все числа разные"
    if a.count(a[0]) == len(a):
        return "Все числа равны"
    return "Есть равные и неравные числа"

i = [a for a in input().split(' ')]
print(chisla(i))

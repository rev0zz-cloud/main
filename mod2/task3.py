def comp_func(i):
    if i[0] <= i[1] <= i[2]: return i[0], i[1], i[2]
    elif i[0] <= i[2] <= i[1]: return i[0], i[2], i[1]
    elif i[1] <= i[0] <= i[2]: return i[1], i[0], i[2]
    elif i[1] <= i[2] <= i[0]: return i[1], i[2], i[0]
    elif i[2] <= i[0] <= i[1]: return i[2], i[0], i[1]
    else: return i[2], i[1], i[0]
    
i = [int(a) for a in input().split()]
a = comp_func(i)
print(a[1])

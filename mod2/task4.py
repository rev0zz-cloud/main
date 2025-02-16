def dvoika(i):
    b = ''
    while i > 0:
        b = str(i % 2) + b
        i = i // 2
    return b

def vosmerka(i):
    b = ''
    while i > 0:
        b = str(i % 8) + b
        i = i // 8
    return b

def sheshnadc(i):
    b = ''
    while i > 0:
        b = str(i % 16) + b
        i = i // 16
    return b

a = int(input("Введите натуральное число: "))
if a > 0:
    print(dvoika(a))
    print(vosmerka(a))
    print(sheshnadc(a))
else:
    print("Неверный ввод")

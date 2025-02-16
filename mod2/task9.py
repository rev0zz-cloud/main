number = input("Введите номер телефона: ")
res = number.replace("-","").replace("(","").replace(")","").replace(" ","")
print(res)

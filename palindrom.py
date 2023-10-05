def palindrom(st):
    return st == st[::-1]   # срез, который просто разворачивает строку в обратном направлении

stroka = input('Введите строку: ')
print(palindrom(stroka))

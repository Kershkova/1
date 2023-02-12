s: str = input("Введіть рядок:")
c: str = input("Введіть символ:")
lenght = len(s)
n = 0
k = 0

n = s.find(c)
if n == -1:
    print("символ відсутній")
else:
    print("індекси елементів: ", end="")
    while n != -1 and k+1 < lenght - 1:
        n = s.find(c)
        if n != -1:
            s = s[n+1:lenght]
            k += n
            print(k, end=" ")
            k += 1










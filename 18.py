a = str(input("Введіть число: "))
kilkist_cufr = len(a)
b = int(a)
def number_collaps(c):
    if b <= 0:
        raise AttributeError("Число має бути більшим за 0!")
    c = list(map(int, c))
    k = 0
    for i in range(0,len(c)):
        k += c[i]
    if k >= 10:
        c = str(k)
        k = number_collaps(c)
    return k


print(number_collaps(a))
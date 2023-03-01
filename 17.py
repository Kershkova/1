a = str(input("Введіть число: "))


kilkist_cufr = len(a)
b = int(a)
def expanded_from(c):
    if b <= 0:
        raise AttributeError("Число має бути більшим за 0!")
    c = list(map(int, c))
    for i in range(0,kilkist_cufr):
        c[i] = c[i] * (10**(kilkist_cufr-i-1))
    c = list(map(str,c))
    c = "+".join(c)
    return (c)
print(expanded_from(a))
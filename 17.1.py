a = str(input("Введіть число: "))
kilkist_cufr = len(a)
b = int(a)


def expanded_from(c):
    if b <= 0:
        raise AttributeError("Число має бути більшим за 0!")
    c = list(map(int, c))
    m = []
    for i in range(0, kilkist_cufr):
        if c[i] == 0:
            pass
        else:
            c[i] = c[i] * (10**(kilkist_cufr-i-1))
            m.append(c[i])
    m = list(map(str, m))
    m = "+".join(m)
    return (m)


print(expanded_from(a))
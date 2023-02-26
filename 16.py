n = int(input("Введіть висоту трикутника: "))


def traingle(hight):
    for i in range(hight):
        list_s = []
        for j in range(hight*2-1):
            list_s.append(" ")
            if j == hight - 1 - i or j == hight - 1 + i:
                list_s[j] = "*"
            if i == hight - 1:
                list_s[j] = "*"
        print("".join(list_s))


def traingle_all(hight):
    for i in range(hight):
        list_s = []
        for j in range(hight*2-1):
            list_s.append(" ")
            if j >= hight - 1 - i and j <= hight - 1 + i:
                list_s[j] = "*"
            if i == hight - 1:
                list_s[j] = "*"
        print("".join(list_s))


def traingle_plus(hight):
    for i in range(hight):
        list_s = []
        for j in range(hight*2-1):
            list_s.append(" ")
            if j >= hight - 1 - i and j <= hight - 1 + i:
                list_s[j] = "*"
            if i == hight - 1:
                list_s[j] = "*"
        print("".join(list_s))
    for i in range(hight):
        list_s = []
        for j in range(hight*2-1):
            list_s.append(" ")
            if j == i or j == hight*2-i - 2:
                list_s[j] = "*"
            if i == 0:
                list_s[j] = "*"
        print("".join(list_s))


def traingle_plus_all(hight):
    for i in range(hight):
        list_s = []
        for j in range(hight*2-1):
            list_s.append(" ")
            if j >= hight - 1 - i and j <= hight - 1 + i:
                list_s[j] = "*"
            if i == hight - 1:
                list_s[j] = "*"
        print("".join(list_s))
    for i in range(hight):
        list_s = []
        for j in range(hight*2-1):
            list_s.append(" ")
            if j >= i and j <= hight*2 - i - 2:
                list_s[j] = "*"
            if i == 0:
                list_s[j] = "*"
        print("".join(list_s))

traingle(n)
print("\n")
traingle_all(n)
print("\n")
traingle_plus(n)
print("\n")
traingle_plus_all(n)

knuga_obliku = []
s = int(input("Введіть кількість замовлень: "))
list0 = []
for i in range(0, s):
    list0 = []
    print("Введіть дані замовлення(номер, назва та автор, кількість, ціна за 1 шт.): \n")
    for n in range(0, 4):
        if n == 2:
            m = int(input())
        elif n == 3:
            m = float(input())
        else:
            m = input()
        list0.append(m)
    knuga_obliku.append(list0)



def price(spysok):
    for k in range(0, s):
        list1 = spysok[k]
        if list1[2] * list1[3] < 100:
            list1[3] = list1[3] * list1[2] + 10
            list1[3] = str(list1[3])
        else:list1[3] = list1[3] * list1[2]
        list1[2] = str(list1[2])
        spysok[k] = list1
    return list(spysok)


def m(k):
    for i in range(0, s):
        print(k[i], sep="\n")




knuga_obliku = price(knuga_obliku)

m(list(map(lambda x: tuple(x), knuga_obliku)))

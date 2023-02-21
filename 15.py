knuga_obliku = []
s = int(input("Введіть кількість замовлень: "))
list1 = []
for i in range(0, s):
    list1 = []
    print("Введіть дані замовлення: \n")
    for n in range(0, 4):
        m = input()
        list1.append(m)
    knuga_obliku.append(list1)
def stolb(k):
    for i in range(0, s):
        print(k[i], sep="\n")


def vartist(spysok):
    for k in range(0, s):
        list1 = spysok[k]
        list1[0] = int(list1[0])
        list1[2] = int(list1[2])
        list1[3] = float(list1[3])
        if list1[2] * list1[3] < 100:
            list1[3] = list1[3] * list1[2] + 10
        else:list1[3] = list1[3] * list1[2]
    return spysok
def tuple1(*args):
    print(args)
print(stolb(vartist(knuga_obliku)))
order = stolb(vartist(knuga_obliku))
tuple1(order)
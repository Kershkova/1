import random
perelik = []
kilkist_elementiv = int(input("vvedit kilkist elementiv: "))
a = int(input("vid yakogo chusla generuvatu chusla? "))
b = int(input("do yakogo chusla generuvatu chusla? "))
for nomer in range(kilkist_elementiv):
    k = random.randint(a, b)
    perelik.append(k)
print("our list:", perelik)

kilkist = 0
for n in range(1, kilkist_elementiv-2):

    if perelik[n] > perelik[n-1] and perelik[n] > perelik[n+1]:
        kilkist += 1
        print("elements index: ", n)
print("Kilkist: ", kilkist)

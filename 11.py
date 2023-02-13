import random
list = []
kilkist_elementiv = int(input("vvedit kilkist elementiv: "))

for n in range(kilkist_elementiv):
     element = int(input("vvedit znachenna elementy: "))
     list.append(element)
print("our list:", list)

k = int(input("vvedit index elementa: "))
while k > kilkist_elementiv-1:
    k = int(input("vvedit index elementa v diapazoni spusky: "))
for n in range(k,kilkist_elementiv-1):
    list[n] = list [n+1]
list.pop(kilkist_elementiv-1)
print("our new list: ", list)



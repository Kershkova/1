print("vvedit kilkist uchniv u klasah A, B, C")

a = input("kilkist uchniv u klasi A ")

b = input("kilkist uchniv u klasi B ")

c = input("kilkist uchniv u klasi C ")

d = int(a)//2
m = int(a)%2
if m == 1:
    d = d+1
g = int(b)//2
n = int(b)%2
if n == 1:
    g = g+1
h = int(c)//2
v = int(c)%2
if v == 1:
    h = h+1
party = d+g+h
print("kilkist part dlya zakupivli ", party, end="\n")
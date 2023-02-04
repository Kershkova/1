print("Vvedit truznachne chyslo ")
a = input()
b = int(a)%10
c = int(a)//10
d = int(c)%10
s = int(c)//10
m = int(b)*100+int(d)*10+int(s)
print(m)
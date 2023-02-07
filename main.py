i = 0
sum = 0
a = input("input number ")
while int(a) != 0:
    i += 1
    sum = int(sum) + int(a)
    a = input("input number ")
else:
    print("number of inputs ", i, ", summary ", sum)


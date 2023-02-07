i = 0
even = 0
odd = 0
k = 0
sum = 0
middle = 0
max = 0
a = input("input number ")
min = a
if int(a) != 0:
    while int(a) != 0:
        i += 1
        sum = int(sum) + int(a)
        middle = sum / i
        k = int(a) % 2

        if k == 0:
            even += 1
        else:
            odd += 1

        if int(a) > int(max):
            max = a
        elif int(a) < int(min):
            min = a

        a = input("input number ")
    else:
        print("number of inputs ", i, "\nsummary ", sum, "\naverage ", middle, "\neven numbers ", even,
              "\nodd numbers ", odd, "\nmax number ", max, "\nmin number", min)
else:
    print("input not 0")




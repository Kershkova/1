N = input("input N ")
print(N,"  ", end='')
b = 1
i = 1
while b <= int(N):
    print(b, " ", end='')
    i +=1
    b = i
    b **=2
else:
    print("\nit's all")
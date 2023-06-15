n = int(input("Digite o valor de n:"))
i = int(input("Digite o valor de i:"))
j = int(input("Digite o valor de j:"))

x = 0
multiplo = -1

while x < n:
    while True:
        multiplo += 1
        if multiplo % i == 0:
            print(multiplo)
            break
        if multiplo % j == 0:
            print(multiplo)
            break
        if multiplo % j == 0 and multiplo % i == 0:
            print(multiplo)
            break
    x += 1        
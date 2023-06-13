n = int(input("Digite um numero inteiro impar: "))

if n % 2 == 0:
    print("Numero digitado não é impar!!!!")
else:
    for i in range(n, 0, -2):
        print(i)

n = int(input("Digite um numero inteiro impar: "))

if n % 2 == 0:
    print("Numero digitado não é impar!!!!")
else:
    for i in range(1, n+1, 2):
        print(i)

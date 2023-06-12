n = int(input("Digite um numero inteiro positivo par: "))

if n % 2 != 0:
    print("Error, o numero digitado é impar!!!")
else:
    for i in range(0, n+1, 2):
        print(i)


n = int(input("Digite um numero inteiro positivo par: "))

if n % 2 != 0:
    print("Error, o numero digitado é impar!!!")
else:
    for i in range(n , 0-1, -2):
        print(i)


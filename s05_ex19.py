x = int(input("Digite um numero inteiro: "))

if x % 3 == 0 and x % 5 != 0:
    print("Divisivel apenas por 3.")
elif x % 5 == 0 and x % 3 != 0:
    print("Divisivel por 5.")

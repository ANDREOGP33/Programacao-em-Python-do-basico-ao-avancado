x = int(input("Digite um numero inteiro: "))
y = int(input("Digite outro numero inteiro: "))

if x > y:
    print(f"Maior: {x}")
elif y > x:
    print(f"Maior: {x}")
elif x == y:
    print("Números iguais.")
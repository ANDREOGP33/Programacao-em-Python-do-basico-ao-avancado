a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))
c = int(input("Digite o valor C: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b == c:
        print("Triangulo equilatero.")
    elif (a == b) or (a == c) or (b == a) or (b == c):
        print("Triangulo isóciles.")
    elif (a != b) or (a != c) or (b != a) or (b != c):
        print("Triangulo escaleno.")
else:
    print("valores digitados nao correspondem a de um triangulo.")
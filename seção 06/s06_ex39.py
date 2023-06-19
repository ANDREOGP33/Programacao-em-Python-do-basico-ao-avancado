base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

if base <= 0 or altura <= 0:
    print("Valores digitado nao consiste de um triangulo")
else:
    area = (base*altura)/2
    print(f"Area do triangulo: {area}")

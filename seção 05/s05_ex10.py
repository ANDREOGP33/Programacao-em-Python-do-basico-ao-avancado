altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo (f ou m): ")

if sexo == "f":
    print(f"Seu peso ideal: {(62.1 * altura) - 44.:.4}")
elif sexo == "m":
    print(f"Seu peso ideal: {(72.7 * altura) - 58.:.4}")
else:
    print("Sexo invalido.")

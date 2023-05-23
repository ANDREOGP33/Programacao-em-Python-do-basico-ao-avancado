n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

if 0 <= n1 <= 10 and 0 <= n2 <= 10:
    print(f"Média = {(n1 + n2)/2}")
else:
    print("Valor inválido")
altura = int(input("Digite a altura em cm do cilindro: "))
raio = int(input("Digite o raio em cm do cilindro: "))

pi = 3.141592
volume = pi * (raio ** 2) * altura

print(f"O volume do cilindro é: {volume:.6}cm³")

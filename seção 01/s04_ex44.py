AlturaDegrau = float(input("Digite a altura do degrau em cm: "))
AlturaDesejada = float(input("Digite a altura desejada em metros: "))

AlturaDegrau = AlturaDegrau / 100

QuantidadeDegrau = AlturaDesejada / AlturaDegrau

print(f"O usuário deve subir {QuantidadeDegrau} degraus.")

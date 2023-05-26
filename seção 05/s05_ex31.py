peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

if peso <= 60 and altura < 1.20:
    print("Classificação: A")
elif peso <= 60 and altura >= 1.20 and altura < 1.70:
    print("Classificação: B")
elif peso <= 60 and altura >= 1.70:
    print("Classificação: C")
elif peso > 60 and peso <= 90 and altura < 1.20:
    print("Classificação: D")
elif peso > 60 and peso <= 90 and altura >= 1.20 and altura < 1.70:
    print("Classificação: E")
elif peso > 60 and peso <= 90 and altura >= 1.70:
    print("Classificação: F")
elif peso > 90 and altura < 1.20:
    print("Classificação: G")
elif peso > 90 and altura >= 1.20 and altura < 1.70:
    print("Classificação: H")
else:
    print("Classificação: I")
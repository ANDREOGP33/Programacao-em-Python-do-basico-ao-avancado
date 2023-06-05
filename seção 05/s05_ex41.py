kg = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = kg / altura

if imc < 18.5:
    print("Avaixo do Peso!")
elif 18.6 < imc < 24.9:
    print("Saudável!")
elif 25 < imc < 29.9:
    print("Peso em excesso!")
elif 30 < imc > 34.9:
    print("Obesidade Garu I")
elif  35 < imc < 39.9:
    print("Obesidade Garu II(severa)")
elif imc >= 40:
    print("Obesidade Garu III(mórbida)")

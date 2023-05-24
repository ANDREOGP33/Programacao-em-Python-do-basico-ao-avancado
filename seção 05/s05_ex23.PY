ano = int(input("Digite o ano: "))

if ano % 400 == 0 or ano % 4 == 0 or ano % 100 > 0:
    print("Ano bissexto.")
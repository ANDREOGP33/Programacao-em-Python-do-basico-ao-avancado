distancia = int(input("Digite a distancia percorrida em KM: "))
consumo = int(input("Digite o consumo em litros consumido durante o percuso: "))

if distancia / consumo < 8:
    print("Venda o carro!")
elif distancia / consumo >= 8 and distancia / consumo < 12:
    print("Economico!")
elif distancia /consumo >= 12:
    print("Super economico!")

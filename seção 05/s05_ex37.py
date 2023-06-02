hora_chegada = int(input("Digite a hora de chegada: "))
minuto_chegada = int(input("Digite o minuto de chegada: "))
hora_saida = int(input("Digite a hora de saida: "))
minuto_saida = int(input("Digite o minuto de saida: "))

total_minutos_chegada = (hora_chegada * 60) + minuto_chegada
total_minutos_saida = (hora_saida * 60) + minuto_saida
tempo_estacionado = total_minutos_saida - total_minutos_chegada

if 60 >= tempo_estacionado:
    print("Valor cobrado: R$1.00")
elif tempo_estacionado >= 61 and tempo_estacionado <= 180:
    print("Valor cobrado: R$2.00")

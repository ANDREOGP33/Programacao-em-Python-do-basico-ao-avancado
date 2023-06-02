hora_chegada = int(input("Digite a hora de chegada: "))
minuto_chegada = int(input("Digite o minuto de chegada: "))
hora_saida = int(input("Digite a hora de saida: "))
minuto_saida = int(input("Digite o minuto de saida: "))

total_minutos_chegada = (hora_chegada * 60) + minuto_chegada
total_minutos_saida = (hora_saida * 60) + minuto_saida

if hora_chegada < hora_saida:
    tempo_estacionado = total_minutos_saida - total_minutos_chegada
elif hora_chegada > hora_saida:
    tempo_estacionado = 1440 + total_minutos_chegada - total_minutos_saida

print(tempo_estacionado)
valor = 0

if hora_saida < hora_chegada:
    valor = 48
    hora_m24 = hora_chegada - hora_saida
    minuto_m24 = hora_m24 * 60

    if tempo_estacionado % 60 == 0:
        hora = tempo_estacionado // 60
        valor = valor + (hora * 2)
        print(valor)

    elif tempo_estacionado % 60 != 0:
        hora = tempo_estacionado // 60
        valor = 2
        valor = valor + (hora * 2)
        print(valor)

elif 60 >= tempo_estacionado:
    valor = valor + 1
    print(valor)
    print(tempo_estacionado)

elif 60 < tempo_estacionado <= 120:
    valor = valor + 2
    print(valor)

elif 120 < tempo_estacionado <= 180:
    valor = valor + 1.40
    print(valor)

    if 120 < tempo_estacionado <= 240:
        valor = valor + 2.80

elif 300 <= tempo_estacionado:
    if tempo_estacionado % 60 == 0:
        hora = tempo_estacionado // 60
        valor = valor + (hora * 2)
        print(valor)

    elif tempo_estacionado % 60 != 0:
        hora = tempo_estacionado // 60
        valor = 2
        valor = valor + (hora * 2)
        print(valor)

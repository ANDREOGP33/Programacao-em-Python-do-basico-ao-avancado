def calcular_preco(chegada, partida):
    hora_chegada, minuto_chegada = chegada
    hora_partida, minuto_partida = partida

    if hora_partida < hora_chegada or (hora_partida == hora_chegada and minuto_partida < minuto_chegada):
        hora_partida += 24

    diferenca = (hora_partida - hora_chegada) * 60 + (minuto_partida - minuto_chegada)

    preco = 0

    if diferenca <= 60:
        preco = 1
    elif diferenca <= 180:
        preco = 1 + ((diferenca - 60) // 60 + 1) * 0.4
    else:
        preco = 1 + 2 * 0.4 + ((diferenca - 180) // 60 + 1) * 2

    return preco

chegada_hora = int(input("Digite a hora de chegada: "))
chegada_minuto = int(input("Digite o minuto de chegada: "))
partida_hora = int(input("Digite a hora de partida: "))
partida_minuto = int(input("Digite o minuto de partida: "))

preco_total = calcular_preco((chegada_hora, chegada_minuto), (partida_hora, partida_minuto))

print(f"Preço cobrado: R$ {preco_total:.2f}")

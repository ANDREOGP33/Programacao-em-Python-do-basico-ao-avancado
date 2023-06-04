salario = float(input("Digite seu salario atual: "))
tempo_contratado = int(input("Digite o sem tempo de contrato em anos: "))

if salario <= 500:
    if tempo_contratado < 1:
        bonus = 0
        salario = salario + (salario * 0.25) + bonus
        print(f"Salario reajustado: {salario}")
    elif 1 <= tempo_contratado <= 3:
        bonus = 100
        salario = salario + (salario * 0.25) + bonus
        print(f"Salario reajustado: {salario}")
    elif 4 <= tempo_contratado <= 6:
        bonus = 200
        salario = salario + (salario * 0.25) + bonus
        print(f"Salario reajustado: {salario}")
    elif 7 <= tempo_contratado <= 10:
        bonus = 200
        salario = salario + (salario * 0.25) + bonus
        print(f"Salario reajustado: {salario}")
    elif 7 <= tempo_contratado <= 10:
        bonus = 300
        salario = salario + (salario * 0.25) + bonus
        print(f"Salario reajustado: {salario}")
    else:
        bonus = 500
        salario = salario + (salario * 0.25) + bonus
        print(f"Salario reajustado: {salario}")
elif salario <= 1000:
    if tempo_contratado < 1:
        bonus = 0
        salario = salario + (salario * 0.20) + bonus
        print(f"Salario reajustado: {salario}")
    elif 1 <= tempo_contratado <= 3:
        bonus = 100
        salario = salario + (salario * 0.20) + bonus
        print(f"Salario reajustado: {salario}")
    elif 4 <= tempo_contratado <= 6:
        bonus = 200
        salario = salario + (salario * 0.20) + bonus
        print(f"Salario reajustado: {salario}")
    elif 7 <= tempo_contratado <= 10:
        bonus = 200
        salario = salario + (salario * 0.20) + bonus
        print(f"Salario reajustado: {salario}")
    elif 7 <= tempo_contratado <= 10:
        bonus = 300
        salario = salario + (salario * 0.20) + bonus
        print(f"Salario reajustado: {salario}")
    else:
        bonus = 500
        salario = salario + (salario * 0.20) + bonus
        print(f"Salario reajustado: {salario}")
elif salario <= 1500:
    if tempo_contratado < 1:
        bonus = 0
        salario = salario + (salario * 0.15) + bonus
        print(f"Salario reajustado: {salario}")
    elif 1 <= tempo_contratado <= 3:
        bonus = 100
        salario = salario + (salario * 0.15) + bonus
        print(f"Salario reajustado: {salario}")
    elif 4 <= tempo_contratado <= 6:
        bonus = 200
        salario = salario + (salario * 0.15) + bonus
        print(f"Salario reajustado: {salario}")
    elif 7 <= tempo_contratado <= 10:
        bonus = 200
        salario = salario + (salario * 0.15) + bonus
        print(f"Salario reajustado: {salario}")
    elif 7 <= tempo_contratado <= 10:
        bonus = 300
        salario = salario + (salario * 0.15) + bonus
        print(f"Salario reajustado: {salario}")
    else:
        bonus = 500
        salario = salario + (salario * 0.15) + bonus
        print(f"Salario reajustado: {salario}")
elif salario <= 2000:
    if tempo_contratado < 1:
        bonus = 0
        salario = salario + (salario * 0.10) + bonus
        print(f"Salario reajustado: {salario}")
    elif 1 <= tempo_contratado <= 3:
        bonus = 100
        salario = salario + (salario * 0.10) + bonus
        print(f"Salario reajustado: {salario}")
    elif 4 <= tempo_contratado <= 6:
        bonus = 200
        salario = salario + (salario * 0.10) + bonus
        print(f"Salario reajustado: {salario}")
    elif 7 <= tempo_contratado <= 10:
        bonus = 200
        salario = salario + (salario * 0.10) + bonus
        print(f"Salario reajustado: {salario}")
    elif 7 <= tempo_contratado <= 10:
        bonus = 300
        salario = salario + (salario * 0.10) + bonus
        print(f"Salario reajustado: {salario}")
    else:
        bonus = 500
        salario = salario + (salario * 0.10) + bonus
        print(f"Salario reajustado: {salario}")
elif salario > 2000:
    if tempo_contratado < 1:
        bonus = 0
        salario = salario + (salario * 0.25) + bonus
        print(f"Salario reajustado: {salario}")
    elif 1 <= tempo_contratado <= 3:
        bonus = 100
        salario = salario + bonus
        print(f"Salario reajustado: {salario}")
    elif 4 <= tempo_contratado <= 6:
        bonus = 200
        salario = salario + bonus
        print(f"Salario reajustado: {salario}")
    elif 7 <= tempo_contratado <= 10:
        bonus = 200
        salario = salario + bonus
        print(f"Salario reajustado: {salario}")
    elif 7 <= tempo_contratado <= 10:
        bonus = 300
        salario = salario + bonus
        print(f"Salario reajustado: {salario}")
    else:
        bonus = 500
        salario = salario + bonus
        print(f"Salario reajustado: {salario}")

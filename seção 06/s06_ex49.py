salario_carlos = int(input("Digite o salario de carlos: "))
salario_joao = salario_carlos / 3
mes = 0

while True:
    salario_carlos = (salario_carlos * 0.02) + salario_carlos
    salario_joao = (salario_joao * 0.05) + salario_joao
    mes += 1

    if salario_joao > salario_carlos:
        print(f"O valor pertencente a joao ultrapassou carlos em {mes} meses")
        break
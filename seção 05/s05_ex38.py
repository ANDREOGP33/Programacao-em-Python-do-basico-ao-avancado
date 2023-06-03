print("Digite sua data de nascimento.")

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if 0 <= dia >31:
    print("Data invalida!")
elif mes == 2 and dia > 28:
    print("Data invalida!")
elif ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    
print("Digite sua data de nascimento.")

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if 0 >= dia > 31:
    print("Data invalida!")
elif ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    if mes == 30 or mes == 31:
        print("Data invalida!")
    else:
        print("Data valida")
elif mes == 2 and dia >= 29:
    print("Data invalida!")
elif 0 >= mes > 12:
    print("Data invalida!")
else:
    print("Data val8ida")

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if 1 <= dia <= 31 and 1 <= mes <= 12:
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if dia <= 29:
                print("Data válida, ano bissexto.")
            else:
                print("Data inválida.")
        else:
            if dia <= 28:
                print("Data válida, ano não bissexto.")
            else:
                print("Data inválida.")
    else:
        print("Data válida.")
else:
    print("Data inválida.")

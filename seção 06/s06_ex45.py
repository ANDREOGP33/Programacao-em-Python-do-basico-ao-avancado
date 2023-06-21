while True:
    print("(1) Km/h para M/s\n"
          "(2) M/s para Km/h\n"
          "(3) Sair")
    
    opcao = int(input())

    if opcao == 1:
        print("Opção escolhida: Km/h para M/s!")
        km = float(input("Digite a velocidade: "))
        print(f"{km}Km/h equivale {km/3.6:.4}M/s!")
    elif opcao == 2:
        print("Opção escolhida: M/s para Km/h")
        mt = float(input("Digite a velocidade: "))
        print(f"{mt}Km/h equivale {mt*3.6}Km/h!")
    elif opcao == 3:
        print("Você escolheu sair!")
        break
    else:
        print("Digite uma opção valida!")
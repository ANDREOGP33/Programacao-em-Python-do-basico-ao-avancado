opcao = int(input("1- Soma de 2 números.\n"
                  "2- Diferença entre dois numeros.\n"
                  "3- produto entre dois numeros.\n"
                  "4- Divisão entre 2 numeros (o denominador n pode ser 0).\n"
                  "Escolha a opção: "))

if opcao == 1:
    x = int(input("Digite um numero: "))
    y = int(input("Digite outro numero: "))
    print(f"Soma dos numeros digitados: {x + y}")
elif opcao == 2:
    x = int(input("Digite um numero: "))
    y = int(input("Digite outro numero: "))
    if x > y:
        print(f"Diferença entre os numero digitados: {x - y}")
    else:
        print(f"Diferença entre os numero digitados: {y - x}")
elif opcao == 3:
    x = int(input("Digite um numero: "))
    y = int(input("Digite outro numero: "))
    print(f"Produto entre os numeros digitados: {x * y}")
elif opcao == 4:
    x = int(input("Digite o numerador: "))
    y = int(input("Digite o denominador: "))
    print(f"Divisao entre os numeros digitados: {x / y}")
else:
    print("opção invalida!!!")

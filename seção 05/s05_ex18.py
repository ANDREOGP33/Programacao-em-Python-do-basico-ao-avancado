opcao = str(input("Escolha um tipo de operação a seguir: soma, subitração, multiplicação e divisão (+-*/): "))

if opcao == "+":
    print("Voce escolheu operação de soma.")
    x = int(input("Digite o primeiro numero: "))
    y = int(input("Digite o segundo numero: "))
    print(f"Resultado: {x + y}")
elif opcao == "-":
    print("Voce escolheu operação de subitração.")
    x = int(input("Digite o primeiro numero: "))
    y = int(input("Digite o segundo numero: "))
    print(f"Resultado: {x - y}")
elif opcao == "/":
    print("Voce escolheu operação de divisão.")
    x = int(input("Digite o primeiro numero: "))
    y = int(input("Digite o segundo numero: "))
    print(f"Resultado: {x / y}")
elif opcao == "*":
    print("Voce escolheu operação de multiplicação.")
    x = int(input("Digite o primeiro numero: "))
    y = int(input("Digite o segundo numero: "))
    print(f"Resultado: {x * y}")
else:
    print("Valor incorreto.")
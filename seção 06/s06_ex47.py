while True:
    print("----------------------------------------------") 
    print("adição (1)\n"
      "subtração (2)\n"
      "multiplicação (3)\n"
      "divião (4)\n"
      "sair (5)")
    
    funcao = int(input(""))

    if funcao == 5:
        break
    elif funcao == 1:
        n1 = int(input())
        n2 = int(input())
        n3 = n1 + n2
        print(f"= {n3}")
    elif funcao == 2:
        n1 = int(input())
        n2 = int(input())
        n3 = n1 - n2
        print(f"= {n3}")
    elif funcao == 3:
        n1 = int(input())
        n2 = int(input())
        n3 = n1 * n2
        print(f"= {n3}")
    elif funcao == 4:
        n1 = int(input())
        n2 = int(input())
        n3 = n1 / n2
        print(f"= {n3}")
    else:
        print("Digite uma opção valida!")
    print("----------------------------------------------")
    
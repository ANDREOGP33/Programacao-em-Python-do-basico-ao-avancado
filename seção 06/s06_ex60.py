n = int(input("Digite um número: "))
if n == 0:
    print("O usuário escolheu sair")
else:
    lista = []
    lista_par = []
    lista.append(n)
    qtd = 1

    while True:
        n = int(input("Digite outro número: "))
        if n == 0:
            print("O usuário escolheu sair")
            break
        else:
            lista.append(n)
            if n % 2 == 0:
                lista_par.append(n)
        qtd +=1
        
    qtd_par = len(lista_par)
    soma_par = sum(lista_par)
    soma = sum(lista)
    media = soma / qtd
    
    print(f"Média = {media:.2}")
    print(f"Quantidade de números digitados: {qtd}")
    print(f"Maior = {max(lista)}")
    print(f"Menor: {min(lista)}")
    
    if qtd_par > 0:
        media_par = soma_par / qtd_par
        print(f"Média dos números pares: {media_par:.2}")
    else:
        print("Não foram digitados números pares.")
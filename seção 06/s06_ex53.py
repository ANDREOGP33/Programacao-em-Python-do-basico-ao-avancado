def calcular_triangulo_floyd(n):
    triangulo = [[1]]

    for i in range(1, n):
        linha_anterior = triangulo[i - 1]
        nova_linha = [1]

        for j in range(1, i):
            novo_numero = linha_anterior[j - 1] + linha_anterior[j]
            nova_linha.append(novo_numero)

        nova_linha.append(1)
        triangulo.append(nova_linha)

    return triangulo

def exibir_triangulo(triangulo):
    for linha in triangulo:
        for numero in linha:
            print(numero, end=" ")
        print()

n = int(input("Digite o número de linhas do Triângulo de Floyd: "))
triangulo_floyd = calcular_triangulo_floyd(n)
exibir_triangulo(triangulo_floyd)
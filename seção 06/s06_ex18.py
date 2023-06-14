qtd = int(input("Quantos números você vai digitar: "))

numeros = []
maior = 0
qtd_maior_digitado = 0

for i in range(qtd):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    
    if numero > maior:
        maior = numero
        qtd_maior_digitado = 1
    elif numero == maior:
        qtd_maior_digitado += 1

print(f"O maior número digitado foi: {maior}")
print(f"Ele foi digitado {qtd_maior_digitado} vezes.")
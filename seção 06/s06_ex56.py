def verificar_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

limite = int(input("Digite o limite superior: "))
soma = 0

for numero in range(2, limite + 1):
    if verificar_primo(numero):
        soma += numero

print("A soma dos números primos até", limite, "é:", soma)

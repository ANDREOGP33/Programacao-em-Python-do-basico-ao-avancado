def verificar_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

n = int(input("Digite a quantidade de números primos que deseja imprimir: "))

print("Os", n, "primeiros números primos são:")
count = 0
numero = 2

while count < n:
    if verificar_primo(numero):
        print(numero)
        count += 1
    numero += 1
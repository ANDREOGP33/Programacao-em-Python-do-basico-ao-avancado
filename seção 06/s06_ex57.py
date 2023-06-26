def verificar_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

contador = 0

for numero in range(a, b + 1):
    if verificar_primo(numero):
        contador += 1

print("Entre", a, "e", b, "existem", contador, "números primos.")

def verificar_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

soma = 0
for num in range(a, b + 1):
    if verificar_primo(num):
        soma += num

print("A soma dos números primos entre", a, "e", b, "é:", soma)

numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Número inválido")
else:
    count = 0
    x = 1
    while x < numero:
        x *= 10
        count += 1
    
    logaritmo = count
    print("O logaritmo do número é:", logaritmo)
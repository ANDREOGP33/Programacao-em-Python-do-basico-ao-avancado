import random

numero = random.randint(1,1000)
tentativa = 0

while True:

    chute = int(input("Adivinhe o numero aleatorio de 0 a 1000: "))
    tentativa += 1
    if chute == numero:
        print(f"Acertou, tentativas: {tentativa}")
        break
    elif chute < numero:
        print("Chute um numero maior!")
    elif chute > numero:
        print("Chute um numero menor!")

    
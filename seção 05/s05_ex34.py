nota = float(input("Digite sua nota: "))
faltas = int(input("Digite a quantidade de faltas: "))

if 9 <= nota <= 10 and faltas <= 20:
    print("Conceito 'A'")
elif 9 <= nota <= 10 and faltas > 20:
    print("Conceito 'B'")
elif 7.5 <= nota <= 8.9 and faltas <= 20:
    print("Conceito 'B'")
elif 7.5 <= nota <= 10 and faltas > 20:
    print("Conceito 'C'")
elif 5 <= nota <= 7.4 and faltas <= 20:
    print("Conceito 'C'")
elif 7.5 <= nota <= 10 and faltas > 20:
    print("Conceito 'D'")
elif 4 <= nota <= 4.9 and faltas <= 20:
    print("Conceito 'D'")
elif 4 <= nota <= 4.9 and faltas > 20:
    print("Conceito 'E'")
elif 0 <= nota <= 3.9 and faltas <= 20:
    print("Conceito 'E'")
elif 0 <= nota <= 3.9 and faltas > 20:
    print("Conceito 'E'")

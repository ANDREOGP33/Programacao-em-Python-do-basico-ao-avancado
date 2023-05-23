# peso 2
nota_trab = float(input("Digite a nota do trabalho de laboratorio (0 a 10): "))
# peso 3
nota_avali = float(input("Digite a nota da avaliação semestral (0 a 10): "))
# peso 5
nota_exame = float(input("Digite a nota do exame final (0 a 10): "))

media_ponderada = ((nota_trab * 2) + (nota_avali * 3) + (nota_exame * 5)) / (2 + 3 + 5)

if media_ponderada <= 2.9:
    print("Reprovado.")
elif media_ponderada > 2.9 and media_ponderada < 4.9:
    print("Recuperação.")
else:
    print("Aprovado.")
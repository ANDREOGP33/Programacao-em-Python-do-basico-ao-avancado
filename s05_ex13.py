nota1 = float(input("Digite o valor da primeira prova: "))
nota2 = float(input("Digite o valor da segunda prova: "))
nota3 = float(input("Digite o valor da terceira prova: "))

media_ponderada = ((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / 4

print(f"Média : {media_ponderada}")

if media_ponderada >= float(60):
    print("Aprovado")
else:
    print("Reprovado")
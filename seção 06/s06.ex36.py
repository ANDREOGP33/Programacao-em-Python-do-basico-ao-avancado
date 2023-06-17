soma_quadrados = 0
quadrado_soma = 0

for i in range(1, 101):
    soma_quadrados += i**2
    quadrado_soma += i

quadrado_soma = quadrado_soma**2

print(f"Diferença entre a soma dos quarados e o quadrado das somas: {quadrado_soma - soma_quadrados}")

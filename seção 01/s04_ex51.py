# Lê as coordenadas x e y do usuário
x = int(input("Digite a coordenada x: "))
y = int(input("Digite a coordenada y: "))

# Calcula a distância da origem sem usar a biblioteca math
distancia = ((x*2) + (y**2))**(1/2)


print(f"A distância da origem ({0},{0}) até o ponto ({x},{y}) é {distancia:.2}")
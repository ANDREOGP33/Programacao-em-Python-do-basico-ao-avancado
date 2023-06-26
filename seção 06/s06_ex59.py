def calcular_total_consumo(cidade):
    total_residencial = 0
    total_comercial = 0
    total_industrial = 0

    for habitante in cidade:
        consumo = habitante['consumo']
        codigo = habitante['codigo']

        if codigo == 1:
            total_residencial += consumo
        elif codigo == 2:
            total_comercial += consumo
        elif codigo == 3:
            total_industrial += consumo

    return total_residencial, total_comercial, total_industrial


def main():
    num_habitantes = int(input("Digite o número de habitantes da cidade: "))
    valor_kwh = float(input("Digite o valor do kWh: "))

    cidade = []

    for i in range(num_habitantes):
        consumo = float(input(f"Digite o consumo do habitante {i + 1}: "))
        codigo = int(input(f"Digite o código do consumidor (1-Residencial, 2-Comercial, 3-Industrial) do habitante {i + 1}: "))

        habitante = {'consumo': consumo, 'codigo': codigo}
        cidade.append(habitante)

    consumos = [habitante['consumo'] for habitante in cidade]
    maior_consumo = max(consumos)
    menor_consumo = min(consumos)
    media_consumo = sum(consumos) / num_habitantes

    total_residencial, total_comercial, total_industrial = calcular_total_consumo(cidade)

    print("=== Resultados ===")
    print("Maior consumo:", maior_consumo)
    print("Menor consumo:", menor_consumo)
    print("Média de consumo:", media_consumo)
    print("Total de consumo residencial:", total_residencial)
    print("Total de consumo comercial:", total_comercial)
    print("Total de consumo industrial:", total_industrial)


if __name__ == '__main__':
    main()

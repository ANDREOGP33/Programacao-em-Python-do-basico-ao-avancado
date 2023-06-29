unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

lista = range(1, 1001)
caracteres = []

for i in lista:
    if i < 10:
        caracteres.append(unidades[i])
    elif i < 100:
        dezena, unidade = divmod(i, 10)
        if unidade == 0:
            caracteres.append(dezenas[dezena])
        else:
            caracteres.append(dezenas[dezena] + " e " + unidades[unidade])
    else:
        centena, resto = divmod(i, 100)
        if centena <= 9:
            if resto == 0:
                caracteres.append(centenas[centena])
            else:
                dezena, unidade = divmod(resto, 10)
                if unidade == 0:
                    caracteres.append(centenas[centena] + " e " + dezenas[dezena])
                else:
                    caracteres.append(centenas[centena] + " e " + dezenas[dezena] + " e " + unidades[unidade])

quantidade_caracteres = 0

for palavra in caracteres:
    quantidade_caracteres += len(palavra)

print("Quantidade de caracteres:", quantidade_caracteres)

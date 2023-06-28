unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

soma = 0
lista = range(1, 1001)
caracteres = []

for i in lista:
    if i < 10:
        caracteres.append(unidades[i])
    if i < 100:
        caracteres.append(dezenas[i])
    if i > 100:    
        caracteres.append(centenas[i])

print(caracteres)

hora_inicio = int(input("Digite a hora de inicio (0-23): "))
minuto_inicio = int(input("Digite o minuto de inicio (0/59): "))
segundo_inicio = int(input("Digite o segundo de inicio (0-59): "))

duracao_segundos = int(input("Digite a duração do experimento em segundos: "))

segundos_inicio = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio

segundos_termino = segundos_inicio + duracao_segundos

hora_termino = segundos_termino // 3600
minuto_termino = (segundos_termino % 3600) // 60
segundo_termino = segundos_termino % 60

print("Hora do termino do experimento: {:02d}:{:02d}:{:02d}".format(hora_termino, minuto_termino, segundo_termino))

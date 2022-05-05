def EstacaoAno(dia, mes):
    if (12 > mes > 9) or (mes == 12 and dia <= 20) or (mes == 9 and dia>= 21):
        estacao = "PRIMAVERA"
    elif (3 > mes >= 1) or (mes == 3 and dia <= 20) or (mes == 12 and dia>= 21):
        estacao = "VERAO"
    elif (6 > mes > 3) or (mes == 6 and dia <= 20) or (mes == 3 and dia>= 21):
        estacao = "OUTONO"
    elif (9 > mes > 6) or (mes == 9 and dia <= 20) or (mes == 6 and dia>= 21):
        estacao = "INVERNO"

    return estacao

dia = int(input())
mes = int(input())

print(EstacaoAno(dia, mes))

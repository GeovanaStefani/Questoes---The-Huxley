def ClassificaAluno(media, qntd_faltas):
    if qntd_faltas > 10:
      situacao = "REPROVADO POR FALTAS"
    else:
        if media < 7:
            situacao = "REPROVADO"
        elif media >= 9.5:
            situacao = "APROVADO COM LOUVOR"
        else:
            situacao = "APROVADO"

    return situacao

media = float(input())
qntd_faltas = int(input())

print(ClassificaAluno(media, qntd_faltas))
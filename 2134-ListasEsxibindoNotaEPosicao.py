qntd_notas = int(input())
if qntd_notas==0:
    print("Numero de notas invalido.")
else:
    notas = []

    for i in range(qntd_notas):
        nota = float(input())
        notas.append(nota)


    for c in range(qntd_notas):
        print("Nota {}: {}".format(c+1, notas[c]))

    print("Media: {:.2f}".format(sum(notas)/qntd_notas))
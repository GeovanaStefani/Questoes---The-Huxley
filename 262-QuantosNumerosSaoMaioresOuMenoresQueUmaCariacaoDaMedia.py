REPETICAO = int(input())
notas = []

for i in range(REPETICAO):
    nota = float(input())
    notas.append(nota)

media = sum(notas)/len(notas)
mais_10 = media*1.1
menos_10 = media*0.9

cont_acima = 0
cont_abaixo = 0
for avaliacao in notas:
    if avaliacao>mais_10:
        cont_acima+=1
    elif avaliacao<menos_10:
        cont_abaixo+=1

print("{:.2f}\n{}\n{}".format(media, cont_acima, cont_abaixo))
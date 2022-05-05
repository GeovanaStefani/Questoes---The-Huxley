QNTD_NOTAS= 5
notas = []
alunos = []
distancias = []
maior = -1 #recebe -1 pq se todas as notas forem 0 n�o tem com oq comparar

#Pede os inputs e vai adicionando tanto na lista de notas, quanto na lista de alunos
for i in range (QNTD_NOTAS):
    nota = float(input())
    nome = input()
    notas.append(nota)
    alunos.append(nome)

#copia a lista de notas e ordena de forma decrescente
ordenada = notas.copy()
ordenada.sort(reverse=True)

#calcula a media a partir da soma da lista de notas, dividido pela quantidade de notas
media = sum(notas)/QNTD_NOTAS

#Calcula a distancia entre cada nota em rela��o a media, sempre aceitando valores positivos
#adiciona em uma lista chamada distancias
#verififica qual � a maior distancia e sua posi��o e armazena em variaveis
for n in notas:
    distancia = n - media
    if distancia<0:
        distancia = distancia*-1

    distancias.append(distancia)

    if distancia>maior:
        maior = distancia
        nota_maior_distancia = n

#percorre a lista de notas, analisando se o valor das notas � igual a maior distancia, para poder armazenar o nome e a posi��o desse aluno
#o capitalize deixa a primeira letra da string mai�scula
for c in range(QNTD_NOTAS):
    if notas[c] == nota_maior_distancia:
        nome_maior_distancia = alunos[c].capitalize()
        if media == 0:
            posicao_do_maior = 0
        else:
            posicao_do_maior = c

#PRINT DOS RESULTADO
#percorre a lista das ordenadas e printa uma valor ao lado do outro
for j in range(QNTD_NOTAS):
    if j == QNTD_NOTAS -1:
        print("{:.2f}".format(ordenada[j]))
    else:
        print("{:.2f}".format(ordenada[j]), end=" ")

print("{:.2f}".format(media)) #print da media

#percorre a lista de distancias e printa um ao lado do outro
for d in range (QNTD_NOTAS):
    if d == QNTD_NOTAS -1:
        print("{:.2f}".format(distancias[d]))
    else:
        print("{:.2f}".format(distancias[d]), end=" ")

print(nome_maior_distancia) #print do nome da maior distancia
print(posicao_do_maior) #print da posicao da maior distancia
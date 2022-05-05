gabarito = input()
notas= []
nomes = []
maior = 0

while True:
    nome = input()
    if nome == "sair":
        break

    respostas = input()

    cont = 0
    for i in range(5):
        if gabarito[i] == respostas[i]:
            cont+=1

    notas.append(cont*20)
    nomes.append(nome)

media = sum(notas)/len(notas)

cont2 = 0
for nota in notas:
    if nota>media:
        cont2+=1

for c in range(len(notas)):
    if notas[c]>=maior:
        maior = notas[c]
        nome_do_maior = nomes[c]

print(cont2)
print(nome_do_maior)
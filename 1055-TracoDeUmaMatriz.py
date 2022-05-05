TAMANHO = int(input())

matriz = []
soma_diagonal = 0

resposta = "tr(A) = "

for l in range(TAMANHO):
    linha = list(map(float, input().split()))
    for c in range(TAMANHO):
        if l == c:
            resposta+="({:.2f}) + ".format(linha[c])
            soma_diagonal+=linha[c]

    matriz.append(linha)

resposta = resposta.rstrip(" + ")
resposta+=" = {:.2f}".format(soma_diagonal)

print(resposta)
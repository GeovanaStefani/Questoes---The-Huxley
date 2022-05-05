LINHA_COLUNA = 3
QNTD_VALORES = 9

matriz = []
maior_valor = -99999999
soma_matriz = 0
soma_diagonal = 0

for l in range(LINHA_COLUNA):
    linha = []
    for c in range(LINHA_COLUNA):
        valor = int(input())
        linha.append(valor)

        if valor > maior_valor:
            maior_valor = valor

        if l == c:
            soma_diagonal += valor

    soma_matriz+= sum(linha)
    matriz.append(linha)

media = soma_matriz/QNTD_VALORES

if maior_valor > 0:
    delta = 1
elif maior_valor < 0:
    delta = -1
else:
    delta = 0

print("{:.2f} {} {} {} ".format(media, maior_valor, delta, soma_diagonal))
import sys

LINHA_COLUNA = 3

matriz = []
menor_valor = sys.maxsize
soma_pares_matriz = 0
qntd_valores_pares = 0
soma_nao_diagonal = 0

for l in range(LINHA_COLUNA):
    linha = []
    for c in range(LINHA_COLUNA):
        valor = int(input())
        linha.append(valor)

        if valor>0:
            soma_pares_matriz+=valor
            qntd_valores_pares += 1

        if valor < menor_valor:
            menor_valor = valor

        if l != c:
            soma_nao_diagonal += valor

    matriz.append(linha)

media = soma_pares_matriz/qntd_valores_pares

if menor_valor%2==0:
    delta = 1
else:
    delta = 0

print("{:.2f} {} {} {}".format(media, menor_valor, delta, soma_nao_diagonal))
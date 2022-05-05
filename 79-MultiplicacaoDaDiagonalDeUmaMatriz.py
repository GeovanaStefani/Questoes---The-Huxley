TAMANHO = 4
while True:
    k = int(input())
    if k == 0:
        break

    matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    for l in range(TAMANHO):
        for c in range(TAMANHO):
            elem = int(input())
            if l == c:
                elem*=k
            matriz[c][l] = elem

    for l in range(TAMANHO):
        for c in range(TAMANHO):
            print(matriz[l][c], end=" ")
        print()
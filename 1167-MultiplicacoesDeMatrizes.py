def constroi_matriz(qntd_linhas):
    matriz = []
    for l in range(qntd_linhas):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    return matriz

def imprime_matriz(matriz, qntd_linhas, qntd_colunas):
    for l in range(qntd_linhas):
        for c in range(qntd_colunas):
            print(matriz[l][c], end=" ")
        print()
    
qual_multiplicacao = input()
matriz_a = []

if qual_multiplicacao == "m":
    qntd_linhas_a, qntd_colunas_a= map(int, input().split())
    qntd_linhas_b, qntd_colunas_b = map(int, input().split())

    if qntd_colunas_a == qntd_linhas_b:

        matriz_a = constroi_matriz(qntd_linhas_a)
        matriz_b = constroi_matriz(qntd_linhas_b)
        matriz_r = []

        for l_a in range(qntd_linhas_a): #percorre as linhas de a
            linha_r = []
            for c_b in range(qntd_colunas_b): #percorre as colunas de b
                somatorio = 0
                for l_b in range(qntd_linhas_b): #percorre os elementos da linha de b
                    somatorio += matriz_a[l_a][l_b] * matriz_b[l_b][c_b]
                linha_r.append(somatorio)
            matriz_r.append(linha_r)

        imprime_matriz(matriz_r, qntd_linhas_a, qntd_colunas_b)

    else:
        print("erro")
        
else:
    escalar = int(input())
    qntd_linhas, qntd_colunas= map(int, input().split())

    matriz = constroi_matriz(qntd_linhas)

    for l in range(qntd_linhas):
        for c in range(qntd_colunas):
            matriz[l][c] = matriz[l][c]*escalar

    imprime_matriz(matriz, qntd_linhas, qntd_colunas)
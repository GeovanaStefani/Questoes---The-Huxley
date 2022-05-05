linhas_a, colunas_a, colunas_b = map(int, input().split()) #2 3 2
linhas_b = colunas_a

matriz_a = []
matriz_b = []
matriz_r = []


for a in range(linhas_a):
    linha_a = list(map(int, input().split()))
    matriz_a.append(linha_a)

for b in range(linhas_b):
    linha_b = list(map(int, input().split()))
    matriz_b.append(linha_b)

for i in range(linhas_a):
    linha_r = []
    for l in range(linhas_a): 
        somatorio = 0
        
        for c in range(colunas_a):
            somatorio += matriz_a[i][c] * matriz_b[c][l]
        
        linha_r.append(somatorio)

    matriz_r.append(linha_r)
        

for l in range(linhas_a):
    for c in range(colunas_b):
        if c == colunas_b-1:
            print(matriz_r[l][c])
        else:
            print(matriz_r[l][c], end=" ")
n = int(input())
posicoes =[]
letras = []

for i in range(n):
    entrada = input().split()
    posicoes.append(int(entrada[0]))
    letras.append(entrada[1])

for c in range(n+1):
    if c in posicoes:
        indice = posicoes.index(c)
        print(letras[indice], end="")
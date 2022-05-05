LINHAS, COLUNAS = map(int, input().split())
matriz = []
eh_quadrada = LINHAS == COLUNAS
soma_principal = 0
soma_secundaria = 0
qntd_positivos = 0
qntd_negativos = 0

for l in range(LINHAS):
    linha = []
    for c in range(COLUNAS):
        valor = int(input())
        linha.append(valor)

        if eh_quadrada:
            if l == c:
                soma_principal +=valor
            if l == COLUNAS - 1 - c:
                soma_secundaria+=valor

        if valor > 0:
            qntd_positivos+=1
        elif valor < 0:
            qntd_negativos+=1

    matriz.append(linha)

print("Matriz formada:")
for l in range(LINHAS):
    for c in range(COLUNAS):
        if c == COLUNAS -1:
            print(matriz[l][c])
        else:
            print(matriz[l][c], end=" ")
        
if eh_quadrada:
    print("A diagonal principal e secundaria tem valor(es) {} e {} respectivamente.".format(soma_principal, soma_secundaria))
else:
    print("A diagonal principal e secundaria nao pode ser obtida.")

print("A matriz possui {} numero(s) menor(es) que zero.".format(qntd_negativos))
print("A matriz possui {} numero(s) maior(es) que zero.".format(qntd_positivos))
matriz = []
creditos = 0
debitos = 0

while True:
    entrada = input().split()
    if int(entrada[0]) == -1:
        break
    matriz.append([int(entrada[0]), float(entrada[1])])

for l in range(len(matriz)):
    if matriz[l][0] == 0:
        debitos += matriz[l][1]
    else:
        creditos += matriz[l][1]

saldo = creditos - debitos

print("""Creditos: R$ {:.2f}
Debitos: R$ {:.2f}
Saldo: R$ {:.2f}""".format(creditos, debitos, saldo))
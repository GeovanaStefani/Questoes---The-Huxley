QNTD_L1 = int(input())
QNTD_L2 = int(input())

lista1 = []
lista2 = []
intersecao = []

for i in range(QNTD_L1+QNTD_L2):
    elemento = input()
    if i < QNTD_L1:
        lista1.append(elemento)
    else: 
        lista2.append(elemento)

uniao = lista2.copy()
diferenca = lista1.copy()

for c in range(QNTD_L1):
    if lista1[c] in lista2:
        intersecao.append(lista1[c])
        diferenca.remove(lista1[c])
    else:
        uniao.append(lista1[c])

print(uniao)
print(intersecao)
print(diferenca)
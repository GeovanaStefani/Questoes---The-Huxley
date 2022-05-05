QNTD_LISTAS = 2
TAMANHO_DAS_LISTAS= int(input())

lista1 = []
lista2 = []
lista_intercalada = []

for i in range(QNTD_LISTAS):
    for c in range(TAMANHO_DAS_LISTAS):
        num = int(input())
        if i == 0 :
            lista1.append(num)
        else:
            lista2.append(num)

for j in range (TAMANHO_DAS_LISTAS):
    lista_intercalada.append(lista1[j])
    lista_intercalada.append(lista2[j])

for elemento in lista_intercalada:
    print(elemento)
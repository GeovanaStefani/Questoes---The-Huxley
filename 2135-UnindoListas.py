qntd_l1 = int(input())

if qntd_l1 == 0:
    print("Erro - A lista deve ter pelo menos 1 elemento.")
    exit(0)

lista1 = []
lista2 = []

for i in range(qntd_l1):
    n1 = int(input())
    lista1.append(n1)

qntd_l2 = int(input())

if qntd_l2 == 0:
    print("Erro - A lista deve ter pelo menos 1 elemento.")
    exit(0)

for c in range(qntd_l2):
    n2 = int(input())
    lista2.append(n2)

lista3 = lista1+lista2

for j in range(len(lista3)):
    if j == len(lista3)-1:
        print(lista3[j])
    else:
        print(lista3[j], end=" ")
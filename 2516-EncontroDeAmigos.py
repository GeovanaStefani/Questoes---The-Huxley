import sys

qntd_amigos = int(input())
distancias = list(map(int, input().split()))

maior = max(distancias)
menor_soma = sys.maxsize

for i in range(1, maior+1):
    somatorio = 0
    for distancia in distancias:
        somatorio+= abs(distancia - i)

    if somatorio<menor_soma:
        menor_soma = somatorio
        pos = i

print(menor_soma, pos)
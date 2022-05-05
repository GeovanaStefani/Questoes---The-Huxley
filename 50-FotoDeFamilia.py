import sys
TAMANHO = 4
alturas = []

for i in range(TAMANHO):
    altura = float(input())
    alturas.append(altura)

alturas.sort()
print("{:.2f}\n{:.2f}\n{:.2f}\n{:.2f}".format(alturas[0], alturas[2], alturas[3], alturas[1]))

# 40 30 20 10
#10 20 30 40
#10 30 40 20
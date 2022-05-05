import sys
tamanho_lista = int(input())

elementos = input().split()
menor = sys.maxsize

for termo in elementos:
    if int(termo)<menor:
        menor = int(termo)
        posicao = elementos.index(termo)

print("Menor valor: {}\nPosicao: {}".format(menor, posicao))
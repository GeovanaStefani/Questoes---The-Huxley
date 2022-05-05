TAMANHO = int(input())
original = []

entrada = input().split()

for num in entrada:
    original.append(int(num))

ordenada = original.copy()
ordenada.sort()

cont = 0
resposta= []
for c in range(TAMANHO):
    if original[c] == ordenada[c]:
        cont+=1
        resposta.append([original[c], c+1])

print(cont)
for j in range(len(resposta)):
    print(resposta[j][0], resposta[j][1])
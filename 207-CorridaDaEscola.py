import sys
num_comp, num_voltas = map(int, input().split())

menor = sys.maxsize

for i in range(1, num_comp+1):
    tempos = input().split()
    soma_tempos = 0
    for tempo in tempos:
        soma_tempos+=int(tempo)
        
    if soma_tempos<menor:
        menor = soma_tempos
        vencedor = i

print(vencedor)
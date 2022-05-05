habitantes = int(input())
inicio = int(input())
percentual = int(input())
fim = int(input())
anos = []

razao = (percentual/100)+1

i=1
for c in range(inicio, fim+1):
    anos.insert(i, [c, int(habitantes*(razao**(i-1)))]) # pg = p1*(razao**(n-1))
    i+=1

for ano in anos:
    print(ano[0], ano[1])
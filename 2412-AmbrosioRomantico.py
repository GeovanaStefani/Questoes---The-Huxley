num_opcoes, num_perfeito = map(int, input().split())

opcoes= input().split()

resposta = False
for i in range(num_opcoes):
    for c in range (num_opcoes):
        if (i!=c) and (int(opcoes[i])+int(opcoes[c])==num_perfeito):
            resposta = True

if resposta:
    print("SIM")
else:
    print("NAO")
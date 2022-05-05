REPETICAO = int(input())

for i in range(REPETICAO):
    frase = input()
    frase = frase.split()
    palavra = ""
    aux = ""
    for p in frase:
        palavra+= p.upper()

    for j in range(len(palavra)-1, -1, -1):
        aux+=palavra[j]

    if aux == palavra:
        print("SIM")
    else:
        print("NAO")
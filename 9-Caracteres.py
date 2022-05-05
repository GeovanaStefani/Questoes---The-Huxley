while True:
    ignora = int(input())
    if ignora == 0:
        break
    palavra = input()
    aux = ""

    for l in range(len(palavra)-1, -1, -1):
        aux += palavra[l]

    print(aux)
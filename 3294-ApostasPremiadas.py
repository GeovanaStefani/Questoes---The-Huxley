mega_sena = list(map(int, input().split()))
ganhadores = 0

while True:
    numeros_jogados = input().split(",")
    if numeros_jogados[0] == "FIM":
        break
    numeros_jogados = list(map(int, numeros_jogados))

    cont = 0
    for numero in numeros_jogados:
        if numero in mega_sena:
            cont+=1

    if cont == 6:
        ganhadores+=1

print("Total de ganhadores: {}".format(ganhadores))
CARTAS_NA_RODADA = 4

def conta_pontos(carta_1, carta_2):
    soma_das_cartas = carta_1+carta_2

    if carta_1 == carta_2:
        pontuacao = 2*soma_das_cartas
    elif carta_1+1 == carta_2 or carta_2+1 == carta_1:
        pontuacao = 3*soma_das_cartas
    else:
        pontuacao = soma_das_cartas
    
    return pontuacao

while True:
    entrada = input()
    if entrada == "sair":
        print("fim")
        break

    entrada = entrada.split()

    if len(entrada)%2 != 0:
        print("erro")
        break

    jogador_1 = entrada[0]
    jogador_2 = entrada[1]

    entrada.remove(jogador_1)
    entrada.remove(jogador_2)

    rodadas = len(entrada)/CARTAS_NA_RODADA

    pontos_j1 = 0
    pontos_j2 = 0
    for r in range(0, len(entrada), CARTAS_NA_RODADA):
        pontos_j1 += conta_pontos(int(entrada[r]), int(entrada[r+1]))
        pontos_j2 += conta_pontos(int(entrada[r+2]), int(entrada[r+3]))

    if pontos_j1 > pontos_j2:
        print(jogador_1)
    elif pontos_j2 > pontos_j1:
        print(jogador_2)
    else:
        print("empate")
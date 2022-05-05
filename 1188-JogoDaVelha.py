TAMANHO_JOGO = 3
def analisa_vencedor(jogo_da_velha):
    diagonal_principal = []
    diagonal_secundaria = []
    ganhador = "Empate ou em andamento"

    for l in range(TAMANHO_JOGO):
        for c in range(TAMANHO_JOGO):
            if c == 0:
                if jogo_da_velha[l][c] == jogo_da_velha[l][c+1] == jogo_da_velha[l][c+2]:
                    ganhador = jogo_da_velha[l][c]
                elif jogo_da_velha[c][l] == jogo_da_velha[c+1][l] == jogo_da_velha[c+2][l]:
                    ganhador = jogo_da_velha[l][c]

            if l == c:
                diagonal_principal.append(jogo_da_velha[l][c])

            if l == TAMANHO_JOGO - 1 - c:
                diagonal_secundaria.append(jogo_da_velha[l][c])
    
    if diagonal_principal[0] == diagonal_principal[1] == diagonal_principal[2]:
        ganhador = diagonal_principal[0]
    elif diagonal_secundaria[0] == diagonal_secundaria[1] == diagonal_secundaria[2]:
        ganhador = diagonal_secundaria[0]

    return ganhador


while True:
    jogo_da_velha = []

    for l in range(TAMANHO_JOGO):
        entrada = input()
        if entrada == "sair":
            exit(0)
        linha = list(entrada.split())
        jogo_da_velha.append(linha) 
            
    print(analisa_vencedor(jogo_da_velha))
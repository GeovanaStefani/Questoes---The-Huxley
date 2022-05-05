QNTD_NUMS = 2
numeros = []

def eh_primo(n):
    resposta = False
    cont_divisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont_divisores += 1

    if cont_divisores == 2:
        resposta = True

    return resposta

for i in range(QNTD_NUMS):
    n = int(input())
    numeros.append(n)
    
    if not eh_primo(n):
        print("O numero {} nao eh primo.".format(n))
        exit(0)

soma_eh_primo = eh_primo(sum(numeros))

if soma_eh_primo:
    print("A soma de {} e {} eh um primo.".format(numeros[0], numeros[1]))
else:
    print("A soma de {} e {} nao eh um primo.".format(numeros[0], numeros[1]))
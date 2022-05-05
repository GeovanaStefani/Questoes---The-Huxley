REPETICAO = int(input())
for i in range(REPETICAO):
    palavra = input()
    palavra_sem_repeticao = ""
    for l in range(len(palavra)):
        if l+1 <= len(palavra)-1:
            if not (palavra[l] == palavra[l+1]):
                palavra_sem_repeticao+=palavra[l]
        elif l == len(palavra)-1:
            palavra_sem_repeticao+=palavra[l]
            
    print(palavra_sem_repeticao)
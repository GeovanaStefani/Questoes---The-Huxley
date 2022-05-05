sequencia = input()
letra = input()
cont = 1
maior_s = cont
maior_p = 0

if letra not in sequencia:
    print("ERRO")
    exit(0)

for s in range(len(sequencia)):
    if sequencia[s] == letra:
        if s+1 <= len(sequencia)-1:
            if sequencia[s] == sequencia[s+1]:
                cont+=1
                if s == 0 or sequencia[s-1] != sequencia[s]:
                    pos = s
            else:
                if cont>maior_s:
                    maior_s = cont
                    maior_p = pos
                cont = 1
                pos = 0
print(maior_p)
print(maior_s)
QNTD_ATLETAS = int(input())
QNTD_SALTOS = int(input())

nomes = []
medias = []
media = 0

for i in range(QNTD_ATLETAS):                #recebe os nomes, e saltos e calcula a media
    nomes.append(input())
    saltos = []
    for c in range(QNTD_SALTOS):
        saltos.append(float(input()))
    
    if QNTD_SALTOS!=0:
        media = sum(saltos)/QNTD_SALTOS
    
    medias.append(media)

ordem_nomes = nomes.copy()
for a in range(len(ordem_nomes)):                   #ordena os nomes
    for b in range(a+1, len(ordem_nomes)):
        if ordem_nomes[a] > ordem_nomes[b]:
            temp = ordem_nomes[a]
            ordem_nomes[a] = ordem_nomes[b]
            ordem_nomes[b] = temp

for n in ordem_nomes:                                #faz o print pegando o indice dos nomes
    indice = nomes.index(n)
    print("{}: {:.1f}".format(n, medias[indice]))
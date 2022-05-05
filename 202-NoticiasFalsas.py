qntd_noticias = int(input())

cont_per = 0
for i in range(qntd_noticias):
    url_noticia = input()
    cont_f = 0
    for c in range(4):
        validacao = input()
        if validacao=="f":
            cont_f+=1
    
    print("{} - ".format(url_noticia), end="")
    if cont_f == 0:
        print("verdadeira")
    elif cont_f == 1:
        print("indeterminado")
    elif cont_f == 2:
        print("pode ser falsa")
    elif cont_f == 3:
        print("provavelmente falsa")
        cont_per+=1
    else:
        print("certamente falsa")
        cont_per+=1

percentual = (cont_per/qntd_noticias)*100
print("percentual de not�cias falsas {:.1f}".format(percentual))
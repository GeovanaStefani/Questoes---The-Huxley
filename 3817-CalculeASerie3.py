n = int(input())

if n==0:
    print("Sem termos para somar")
else:
    soma = 0
    num_c = 1
    num_b = 0
    contador = 3
    expressao = ""
    inteiro = 0
    for i in range(1,n+1):

        if i%2==0:
            if i>3:
                num_c+=contador
                contador+=2
            num_b +=3
            soma += num_c/num_b
            elemento = "{}/{}".format(num_c, num_b)
        else:
            inteiro+=1
            soma+=inteiro
            elemento = "{}".format(inteiro)
        
        if i==n:
            expressao += "{}".format(elemento)
        else:
            expressao += "{} + ".format(elemento)


    print("{:.2f}".format(soma))
    print(expressao)
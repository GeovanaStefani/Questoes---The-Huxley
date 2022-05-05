def contando_digitos(caractere):
    digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cont = 0
    for char in caractere:
        if char in digitos:
            cont+=1

    return cont

caractere = input()       
print(contando_digitos(caractere))
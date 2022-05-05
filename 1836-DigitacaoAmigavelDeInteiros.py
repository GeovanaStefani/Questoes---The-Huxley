validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "O", "L"]

while True:
    string = input()
    string = string.upper()

    if string == "FIM":
        break

    eh_valido = True
    aux = ""
    for l in string:
        if l in validos:
            if l == "O":
                aux += "0"
            elif l == "L":
                aux += "1"
            else:
                aux += l
        else:
            eh_valido = False

    if eh_valido:
        print(int(aux))
    else:
        print("ERRO")
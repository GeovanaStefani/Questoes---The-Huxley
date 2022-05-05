def mes_extenso(mes):
    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    
    mes_int = mes -1
    if mes_int< 0 or mes_int>= 12:
        extenso = "invalido"
    else:
        extenso = meses[mes_int]

    return(extenso)

mes = int(input())

print(mes_extenso(mes))

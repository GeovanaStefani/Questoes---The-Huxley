QNTD_NUMS = 4

def produto_primos(lista):
    cont_primos = 0
    produto = 1
    for i in range(len(lista)):
        cont_divisores = 0
        for c in range(1, lista[i]):
            if lista[i]%c == 0:
                cont_divisores+=1
        if cont_divisores==1:
            cont_primos+=1
            produto*= lista[i]
    if cont_primos != QNTD_NUMS:
        produto = "SEM PRODUTO"
        
    return produto
        

lista = list(map(int, input().split()))

print(produto_primos(lista))
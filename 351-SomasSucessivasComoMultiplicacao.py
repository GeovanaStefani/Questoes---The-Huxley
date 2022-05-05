def somas_sucessivas(num1, num2):
    soma = 0
    negativo = False

    if num2<0:
        negativo = True
        num2 *= -1
    for i in range(num2):
        soma+=num1
    
    if negativo:
        soma*=-1
    return(soma)

num1 = int(input())
num2 = int(input())

print(somas_sucessivas(num1, num2))
